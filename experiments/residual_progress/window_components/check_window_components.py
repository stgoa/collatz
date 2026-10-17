"""Bounded complete annular source clusters inside the E0 path graph.

The bound is local preprocessing; no exit search or Collatz termination
claim is used. Exact valuation cylinders retain their extra binary bit.
"""

from argparse import ArgumentParser
from collections import defaultdict
from fractions import Fraction
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "window_alternating",
    ROOT / "experiments/residual_progress/alternating/check_alternating_paths.py")
PATHS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PATHS)
ARITH, S, P = PATHS.ARITH, PATHS.S, PATHS.P
SPAN = 63
# Fixes all branch/residue information in 63 queries in either direction.
GUARD_PERIOD = 2 ** 96 * 3 ** 65


def adjusted_height(x):
    assert x % 3
    return Fraction(x, 2 if x % 3 == 2 else 1)


def local_guard(anchor):
    """Return indexed E0 states from at most63 inverse/63 forward edges."""
    states = {0: anchor}
    point = anchor
    for distance in range(1, SPAN + 1):
        point = PATHS.predecessor(point)
        if point is None:
            break
        states[-distance] = point
    point = anchor
    for distance in range(1, SPAN + 1):
        if not PATHS.allowed_edge(point):
            break
        point = S(point)
        states[distance] = point
    return states


def cluster_at_source(cutoff, anchor):
    """Complete E0 source cluster, without walking to root or final exit."""
    assert cutoff > 0 and cutoff % 8 == 0
    assert ARITH.annular_coefficient(cutoff, anchor)
    guard = local_guard(anchor)
    atoms = {index: ARITH.annular_coefficient(cutoff, state)
             for index, state in guard.items()
             if ARITH.annular_coefficient(cutoff, state)}
    first, last = min(atoms), max(atoms)
    assert last - first <= SPAN
    path = tuple(guard[index] for index in range(first, last + 1))
    coefficients = tuple(ARITH.annular_coefficient(cutoff, x) for x in path)
    word = tuple(PATHS.valuation(x) for x in path[:-1])
    assert all(a in (1, 2) for a in word)
    assert all(a != 2 or b != 2 for a, b in zip(word, word[1:]))
    assert all(x < 192 * cutoff for x in path)
    mass, running, current = sum(coefficients), 0, {}
    for x, coefficient in zip(path[:-1], coefficients[:-1]):
        running += coefficient
        if running:
            current[x] = running
    source = {x: c for x, c in zip(path, coefficients) if c}
    residual = {path[-1]: mass} if mass else {}
    PATHS.check_identity(source, current, residual)
    return {"path": path, "coefficients": coefficients, "word": word,
            "source": source, "mass": mass, "frontier": path[-1],
            "current": current, "residual": residual}


def collapse_annulus(cutoff):
    """Aggregate every complete source cluster at its last source."""
    original = ARITH.ANNULAR.annular_measure(cutoff)
    pending, clusters = set(original), []
    current, residual = defaultdict(int), defaultdict(int)
    for anchor in sorted(original):
        if anchor not in pending:
            continue
        record = cluster_at_source(cutoff, anchor)
        assert set(record["source"]) <= pending
        pending.difference_update(record["source"])
        for x, c in record["current"].items():
            current[x] += c
        for x, c in record["residual"].items():
            residual[x] += c
        clusters.append(record)
    assert not pending
    current, residual = ARITH.clean(current), ARITH.clean(residual)
    PATHS.check_identity(original, current, residual)
    assert ARITH.positive_mass(current) <= SPAN * ARITH.positive_mass(original)
    return current, residual, clusters


def compile_guard(anchor):
    """Affine states for x(t)=anchor+GUARD_PERIOD*t, with fixed residues."""
    guard = local_guard(anchor)
    slopes = {0: GUARD_PERIOD}
    for index in range(-1, min(guard) - 1, -1):
        child = guard[index + 1]
        multiplier = 2 if child % 3 == 2 else 4
        assert multiplier * slopes[index + 1] % 3 == 0
        slopes[index] = multiplier * slopes[index + 1] // 3
    for index in range(1, max(guard) + 1):
        exponent = PATHS.valuation(guard[index - 1])
        assert 3 * slopes[index - 1] % 2 ** exponent == 0
        slopes[index] = 3 * slopes[index - 1] // 2 ** exponent
    assert all(value % 18 == 0 for value in slopes.values())
    return {i: (guard[i], slopes[i]) for i in guard}


def sharp_component(parameter):
    """The exact63-edge source cluster: word (1,2)^31,1."""
    assert parameter >= 1
    first = 3 * 2 ** 95 * parameter - 5
    cutoff = 8 * (first // 18)
    word = (1, 2) * 31 + (1,)
    path, point = [first], first
    for exponent in word:
        assert PATHS.valuation(point) == exponent and PATHS.allowed_edge(point)
        point = S(point)
        path.append(point)
    assert point == 2 * 3 ** 64 * parameter - 7
    # A=94, so the exact cylinder is modulo2^(A+1)=2^95.
    assert sum(word) == 94 and (first + 5) % 2 ** 95 == 0
    assert first % 3 == 1
    assert 9 * cutoff < 4 * first < 18 * cutoff
    assert 288 * cutoff < 4 * point < 576 * cutoff
    record = cluster_at_source(cutoff, first)
    assert record["path"] == tuple(path)
    assert len(record["word"]) == 63
    return {"parameter": parameter, "N": cutoff, "first_source": first,
            "last_source": point, "span": 63, "mass": record["mass"],
            "coefficients": list(record["coefficients"]),
            "exact_cylinder_modulus": 2 ** 95}


def check_cutoff(cutoff):
    original = ARITH.ANNULAR.annular_measure(cutoff)
    current, residual, clusters = collapse_annulus(cutoff)
    # Independent whole-ancestry grouping checks that the local guard missed
    # no source in the complete E0 component.
    full_groups = defaultdict(dict)
    for x, c in original.items():
        full_groups[PATHS.ancestry(x)[-1]][x] = c
    assert len(full_groups) == len(clusters)
    for record in clusters:
        root = PATHS.ancestry(record["path"][0])[-1]
        assert record["source"] == full_groups.pop(root)
        path = record["path"]
        for i, x in enumerate(path):
            if record["coefficients"][i]:
                assert Fraction(9 * cutoff, 4) < adjusted_height(x) < 72 * cutoff
        span = len(path) - 1
        assert span <= (58 if span % 2 == 0 else 63)
    assert not full_groups
    _, earlier_frontiers, _ = PATHS.frontier_collapse(original)
    assert residual == earlier_frontiers
    return {"N": cutoff, "clusters": len(clusters),
            "positive_clusters": sum(record["mass"] > 0 for record in clusters),
            "negative_clusters": sum(record["mass"] < 0 for record in clusters),
            "zero_clusters": sum(record["mass"] == 0 for record in clusters),
            "maximum_source_span": max(len(record["path"]) - 1 for record in clusters),
            "maximum_cluster_mass": max(record["mass"] for record in clusters),
            "minimum_cluster_mass": min(record["mass"] for record in clusters),
            "frontier_positive_mass": ARITH.positive_mass(residual),
            "partial_current_positive_cost": ARITH.positive_mass(current),
            "current_rows": len(current)}


def check_forbidden_exits():
    checked = 0
    for x in range(3, 8194, 2):
        if PATHS.allowed_edge(x):
            continue
        exponent, y = PATHS.valuation(x), S(x)
        root = 1 if y == 1 else PATHS.ancestry(y)[-1]
        if exponent == 2:
            assert x % 3 in (0, 1)
            assert y % 18 == (7 if x % 3 == 0 else 1)
            assert root == y and y < x
        else:
            assert exponent >= 3 and 4 * root < x
        checked += 1
    return checked


def check_sharp_phases():
    """Exact affine band gaps prove the three infinite parameter phases."""
    results = []
    q_slope = 3 * 2 ** 95
    for phase in (1, 2, 3):
        first = q_slope * phase - 5
        cutoff, q = 8 * (first // 18), 18 * (first // 18)
        record = cluster_at_source(cutoff, first)
        for index, point in enumerate(record["path"]):
            j = index // 2
            slope = (3 * 2 ** (95 - 3 * j) * 9 ** j if index % 2 == 0
                     else 9 * 2 ** (94 - 3 * j) * 9 ** j)
            band = next(b for b in range(6) if 2 ** b * q < point < 2 ** (b + 1) * q)
            assert slope - 2 ** band * q_slope >= 0
            assert 2 ** (band + 1) * q_slope - slope >= 0
            assert 3 * slope % 18 == 0
        assert record["mass"] == (35 if phase == 3 else 38)
        results.append({"first_parameter": phase, "step": 3,
                        "positions_checked": len(record["path"]),
                        "mass_for_entire_phase": record["mass"]})
    return results


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    assert Fraction(9, 8) ** 29 < 32 < Fraction(9, 8) ** 30
    assert Fraction(3, 4) * Fraction(9, 8) ** 31 < 32
    assert Fraction(3, 4) * Fraction(9, 8) ** 32 > 32
    cutoffs = [8, 16, 24, 96, 160, 168, 384, 768]
    cases = [check_cutoff(n) for n in cutoffs]
    sharp = [sharp_component(t) for t in (1, 2, 3, 9)]
    affine_checks = 0
    for anchor in (5, 7, 13, 17, 255, 4095, sharp[0]["first_source"]):
        template = compile_guard(anchor)
        for shift in (1, 2):
            observed = local_guard(anchor + GUARD_PERIOD * shift)
            expected = {i: base + slope * shift for i, (base, slope) in template.items()}
            assert observed == expected
            assert all(observed[i] % 18 == template[i][0] % 18 for i in observed)
            affine_checks += 1
    empty_targets = []
    for k in (1, 3, 5, 31):
        _, _, residual, record = PATHS.mersenne_component(k)
        w = next(iter(residual))
        assert w % 18 == 1 and w > 144 * record["N"]
        assert PATHS.predecessor(w) is None
        empty_targets.append({"k": k, "N": record["N"], "exit_root": w,
                              "original_target_component_mass": 0})
    receipt = {"status": "PASS", "sharp_source_span_bound": 63,
               "even_source_separation_bound": 58, "guard_radius": 63,
               "universal_guard_period": GUARD_PERIOD, "cutoffs": cutoffs,
               "results": cases, "sharp_examples": sharp,
               "sharp_infinite_phase_checks": check_sharp_phases(),
               "affine_guard_checks": affine_checks,
               "forbidden_exits_checked_through": 8193,
               "forbidden_exits_checked": check_forbidden_exits(),
               "positive_to_source_empty_examples": empty_targets,
               "local_preprocessing_terminates_universally": True,
               "universal_complete_annular_certificate_status": "open"}
    path = Path(__file__).with_name("window_components_audit.json")
    if args.write_receipt:
        path.write_text(json.dumps(receipt, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == receipt
    print(json.dumps({"status": "PASS", "annular_cases": len(cases),
                      "sharp_examples": len(sharp), "sharp_bound": 63,
                      "complete_certificate": False}, indent=2))


if __name__ == "__main__":
    main()
