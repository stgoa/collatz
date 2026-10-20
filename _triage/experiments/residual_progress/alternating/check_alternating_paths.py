"""Exact path collapse, retained frontiers, and scoped alternation obstructions.

No forward path is assumed to terminate. All exposed inverse paths have a
proved logarithmic bound; optional alternation probes have an explicit cap.
"""

from argparse import ArgumentParser
from collections import defaultdict
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "alternating_auxiliary",
    ROOT / "experiments/residual_progress/auxiliary/check_auxiliary_normal_form.py")
AUX = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUX)
ARITH, P = AUX.ARITH, AUX.P
S = ARITH.PACKETS.step


def valuation(x):
    value = 3 * x + 1
    return (value & -value).bit_length() - 1


def allowed_edge(x):
    """E0 consists of valuation1, or valuation2 with source2 modulo3."""
    return x > 1 and (valuation(x) == 1 or
                      (valuation(x) == 2 and x % 3 == 2))


def predecessor(y):
    if y % 3 == 2:
        return (2 * y - 1) // 3
    if y % 18 == 13:
        return (4 * y - 1) // 3
    return None


def ancestry(y):
    """Return y,...,root; twelve inverse edges more than halve height."""
    assert y > 1 and y % 2
    points = [y]
    cap = 12 * y.bit_length() + 1
    for _ in range(cap):
        x = predecessor(points[-1])
        if x is None:
            assert len(points) == len(set(points))
            assert 3 * max(points) < 4 * y
            return tuple(points)
        assert x > 1 and x % 2 and allowed_edge(x) and S(x) == points[-1]
        points.append(x)
    raise AssertionError("proved inverse-path bound exceeded")


def ancestor_graph(measure):
    depths, roots = {}, {}
    for state, coefficient in measure.items():
        assert state > 1 and state % 2 and isinstance(coefficient, int)
        points = ancestry(state)
        for depth, point in enumerate(reversed(points)):
            assert point not in depths or depths[point] == depth
            depths[point], roots[point] = depth, points[-1]
    return depths, roots


def check_identity(original, current, residual):
    assert ARITH.subtract(original, residual) == ARITH.subtract(current, P(current))


def _collapse(measure, positive_only):
    depths, roots = ancestor_graph(measure)
    residual, current = defaultdict(int, measure), defaultdict(int)
    for state in sorted(depths, key=lambda point: depths[point], reverse=True):
        parent = predecessor(state)
        amount = max(residual[state], 0) if positive_only else residual[state]
        if parent is None or not amount:
            continue
        residual[state] -= amount
        residual[parent] += amount
        current[parent] -= amount
    current, residual = ARITH.clean(current), ARITH.clean(residual)
    check_identity(measure, current, residual)
    assert sum(residual.values()) == sum(measure.values())
    if positive_only:
        assert all(value < 0 for value in current.values())
        assert all(value <= 0 or predecessor(state) is None
                   for state, value in residual.items())
    else:
        assert all(predecessor(state) is None for state in residual)
    return current, residual, {
        "ancestral_vertices": len(depths),
        "path_components": len(set(roots.values())),
        "maximum_inverse_depth": max(depths.values(), default=0),
    }


def signed_path_collapse(measure):
    """Return J,Bmu,stats with mu=div(J)+Bmu; combine every signed source."""
    return _collapse(measure, positive_only=False)


def capacity_normalize(measure):
    """Use every intermediate negative capacity; return nonpositive J."""
    return _collapse(measure, positive_only=True)


def frontier_collapse(measure):
    """Place each path total at its furthest supplied source, retaining path."""
    depths, roots = ancestor_graph(measure)
    frontiers = {}
    for point in measure:
        root = roots[point]
        if root not in frontiers or depths[point] > depths[frontiers[root]]:
            frontiers[root] = point
    residual, current, records = defaultdict(int, measure), defaultdict(int), []
    for root, frontier in sorted(frontiers.items()):
        path = tuple(reversed(ancestry(frontier)))
        for point, following in zip(path, path[1:]):
            amount = residual[point]
            residual[point] = 0
            residual[following] += amount
            current[point] += amount
        records.append({"root": root, "frontier": frontier, "path": path,
                        "mass": residual[frontier]})
    current, residual = ARITH.clean(current), ARITH.clean(residual)
    check_identity(measure, current, residual)
    return current, residual, records


def naive_round(normalized):
    assert all(c <= 0 or not AUX.predecessor_chain(x) for x, c in normalized.items())
    positive = {x: c for x, c in normalized.items() if c > 0}
    moved = defaultdict(int, ARITH.subtract(normalized, positive))
    for x, c in P(positive).items():
        moved[x] += c
    back, result, _ = AUX.normalize(ARITH.clean(moved))
    current = defaultdict(int, positive)
    for x, c in back.items():
        current[x] += c
    current = ARITH.clean(current)
    check_identity(normalized, current, result)
    before = sum(x * max(c, 0) for x, c in normalized.items())
    after = sum(x * max(c, 0) for x, c in result.items())
    assert after <= before
    assert (result == normalized) == (after == before)
    if result == normalized:
        assert not current
    for x, c in result.items():
        if c < 0:
            assert normalized.get(x, 0) <= c
    return current, result


def trap_points(cutoff):
    return [q for q in range(48 * cutoff + 1, 64 * cutoff, 2)
            if q % 24 == 15 or q % 48 == 27]


def check_cutoff(cutoff, iteration_cap=32):
    original = ARITH.ANNULAR.annular_measure(cutoff)
    old_current, old_residual, _ = AUX.normalize(original)
    current, collapsed, stats = signed_path_collapse(original)
    _, twice, _ = signed_path_collapse(collapsed)
    assert twice == collapsed
    _, capacity, _ = capacity_normalize(original)
    _, capacity_twice, _ = capacity_normalize(capacity)
    assert capacity_twice == capacity
    assert ARITH.positive_mass(capacity) <= ARITH.positive_mass(old_residual)
    frontier_current, frontier_residual, records = frontier_collapse(original)
    _, frontier_root, _ = signed_path_collapse(frontier_residual)
    assert frontier_root == collapsed
    points = trap_points(cutoff)
    assert len(points) == cutoff
    for q in points:
        assert old_residual[q] >= 2 and old_residual[S(q)] == -1
    residual = old_residual
    for round_number in range(1, iteration_cap + 1):
        _, next_residual = naive_round(residual)
        for q in points:
            assert next_residual[q] >= 1 and next_residual.get(S(q), 0) == 0
        if next_residual == residual:
            break
        residual = next_residual
    else:
        raise AssertionError(f"bounded alternation probe unresolved at N={cutoff}")
    assert all(c <= 0 or (q % 36 in (3, 7, 15, 19, 27) and
                          residual.get(S(q), 0) == 0)
               for q, c in residual.items())
    return {"N": cutoff, "original_positive_mass": ARITH.positive_mass(original),
            "old_normalized_positive_mass": ARITH.positive_mass(old_residual),
            "capacity_normalized_positive_mass": ARITH.positive_mass(capacity),
            "signed_collapsed_positive_mass": ARITH.positive_mass(collapsed),
            "signed_collapse_positive_current_cost": ARITH.positive_mass(current),
            "frontier_positive_current_cost": ARITH.positive_mass(frontier_current),
            "retained_frontiers": len(records), "naive_rounds_including_fixed_check": round_number,
            "naive_fixed_positive_mass": ARITH.positive_mass(residual),
            "identified_persistent_traps": len(points), **stats}


def mersenne_component(k):
    """Explicit growing-depth current for one complete E0 source component."""
    assert k >= 0
    cutoff, length = 96 * 64 ** k, 12 + 6 * k
    path = [3 ** j * 2 ** (length - j) - 1 for j in range(length)]
    exponent = 2 + (length & -length).bit_length() - 1
    exit_point = (3 ** length - 1) // 2 ** exponent
    original = {path[1]: -2, path[2]: 2, path[3]: 2}
    assert predecessor(path[0]) is None
    assert all(allowed_edge(x) and S(x) == y for x, y in zip(path, path[1:]))
    assert not allowed_edge(path[-1]) and S(path[-1]) == exit_point
    assert valuation(path[-1]) == exponent + 1
    assert {x: c for x in path if (c := ARITH.annular_coefficient(cutoff, x))} == original
    current = {path[1]: -2, **{x: 2 for x in path[3:]}}
    residual = {exit_point: 2}
    check_identity(original, current, residual)
    _, collapsed, _ = signed_path_collapse(original)
    assert collapsed == {path[0]: 2}
    assert ARITH.positive_mass(current) == 2 * length - 6
    if k % 2:
        assert exponent == 3 and predecessor(exit_point) is None and exit_point > path[0]
    return original, current, residual, {
        "k": k, "N": cutoff, "L": length, "root": path[0],
        "component_mass": 2, "first_forbidden_exit": exit_point,
        "exit_root": ancestry(exit_point)[-1],
        "current_rows": len(current), "positive_current_cost": 2 * length - 6,
        "full_component_ends_before_exit": True,
    }


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    for x in range(3, 4098, 2):
        points = ancestry(x)
        old = x
        for _ in range(12 * x.bit_length() + 1):
            chain = AUX.predecessor_chain(old)
            if not chain:
                break
            old = chain[0]
        else:
            raise AssertionError("old normalization root cap")
        assert old == points[-1]
        if allowed_edge(x):
            assert predecessor(S(x)) == x
            assert ancestry(S(x))[-1] == points[-1]
            if allowed_edge(S(x)):
                assert 8 * S(S(x)) > 9 * x
        if not AUX.predecessor_chain(x):
            root_after = 1 if S(x) == 1 else ancestry(S(x))[-1]
            assert (root_after == x) == (x % 4 == 3)
            assert root_after <= x
    cutoffs = list(range(8, 129, 8)) + [160, 168, 384, 768]
    cases = [check_cutoff(n) for n in cutoffs]
    ladder = [mersenne_component(k)[3] for k in (*range(9), 32, 128)]
    phases = [{"N": n, "trap_count": len(trap_points(n))} for n in (8, 16, 24)]
    small = {13: 2, 17: -2}
    small_current, small_residual, _ = capacity_normalize(small)
    assert small_current == {17: -2} and not small_residual
    assert AUX.normalize(small)[1] == {17: -2, 7: 2}
    receipt = {"status": "PASS", "classification_checked_through": 4097,
               "cutoffs": cutoffs, "iteration_cap": 32, "results": cases,
               "persistent_trap_floor_phases": phases, "mersenne_cases": ladder,
               "intermediate_capacity_example": {
                   "source": [[13, 2], [17, -2]], "new_current": [[17, -2]],
                   "new_residual": [], "old_residual": [[7, 2], [17, -2]]},
               "universal_inverse_path_termination": True,
               "universal_forward_path_termination_status": "open",
               "universal_complete_annular_certificate_status": "open"}
    path = Path(__file__).with_name("alternating_paths_audit.json")
    if args.write_receipt:
        path.write_text(json.dumps(receipt, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == receipt
    print(json.dumps({"status": "PASS", "annular_cases": len(cases),
                      "symbolic_component_cases": len(ladder),
                      "complete_certificate": False}, indent=2))


if __name__ == "__main__":
    main()
