"""Complete short-depth phase obstructions and finite cancellation coverage.

The infinite phase statements are finite symbolic proofs, not extrapolations
from the representative scan. All numerical component searches have caps.
See PHASE_COVERAGE.md for precise clocks, source capacity, and limitations.
"""

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "templates"))
sys.path.insert(0, str(HERE.parent / "release"))
from inverse_exposure_probe import COEFFICIENTS, coefficient, component, step
from symbolic_component_lift import prove_chain_lift
from check_release import family_parameters, valuation

FEED_COMMITS = ["e5f2b80726a9612576c7c7cda624f12ffbd86775",
                "f12da944dc68cfaff0884d874e11bc6c2cb98d34"]


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def chain_for(X, D):
    return [3**k * X // 2**k - 1 for k in range(1, D + 4)]


def exact_component(X, D):
    N = 3 * X // 128
    assert X % 1024 == 0 and valuation(X - 1, 3) >= 2
    report, graph = component(N, D, state_cap=2000, query_cap=30000)
    assert report["status"] == "complete_component", report
    return report, graph


def verify_additive_phase(proof, X0, period):
    """Reinterpret the complete affine proof at q=X/X0, not just integer q.

    All its sign comparisons already hold for every real q>=1. The extra
    checks below preserve integrality, oddness, inverse admissibility and
    every coefficient under X -> X+period. A zero coefficient can be stable
    with less precision than preserving its entire residue modulo18.
    """
    N0 = 3 * X0 // 128
    rows = proof["receipt"]["chain"] + [row[:4] for row in proof["queries"]]
    unique_rows = sorted(set(map(tuple, rows)))
    checks = []
    for row in unique_rows:
        a, b = Fraction(row[0], row[1]), Fraction(row[2], row[3])
        base = a + b
        assert base.denominator == 1 and base > 1 and base.numerator % 2
        increment = a * period / X0
        assert increment.denominator == 1 and increment % 6 == 0
        value, delta = base.numerator, increment.numerator
        if 9 * N0 // 4 < value < 144 * N0:
            band = (value // (9 * N0 // 4)).bit_length() - 1
            coefficients = [COEFFICIENTS[band].get((value + j * delta) % 18, 0)
                            for j in range(3)]
            assert len(set(coefficients)) == 1
        else:
            band, coefficients = None, [0, 0, 0]
        checks.append([*row, delta, band, coefficients])
    return dict(registered_states=len(unique_rows),
                translation_checks_sha256=digest(checks))


def symbolic_phase_family(h, D, K, exceptional_U):
    """Prove every complementary unit-U phase, over a full additive class."""
    binary_exponent = max(D + 4, 10)
    binary, modulus = 2**binary_exponent, 3**K
    u_modulus = 3**(K - h)
    period, common_threshold = binary * modulus, 2 * binary * modulus
    cases = []
    for U in range(u_modulus):
        if U % 3 == 0 or U == exceptional_U:
            continue
        X0 = binary * ((1 + 3**h * U) * pow(binary, -1, modulus) % modulus
                       + modulus)
        assert period <= X0 < common_threshold
        assert valuation(X0 - 1, 3) == h
        proof = prove_chain_lift(3 * X0 // 128, D, query_cap=30000)
        translation = verify_additive_phase(proof, X0, period)
        numeric = []
        for offset in (0, 1, 2):
            X = X0 + offset * period
            report, graph = exact_component(X, D)
            chain = chain_for(X, D)
            assert graph["nodes"] == set(chain)
            assert graph["edges"] == dict(zip(chain, chain[1:]))
            assert graph["sources"] == dict(zip(chain[:3], (-2, 2, 2)))
            numeric.append(dict(X=X, vertices=report["vertices"],
                                queries=report["reachability_queries"]))
        cases.append(dict(U_phase=U, X0=X0,
                          original_symbolic_receipt=proof["receipt"],
                          complete_queries_sha256=digest(proof["queries"]),
                          affine_comparisons_sha256=digest(proof["comparisons"]),
                          translation=translation, independent_numeric_checks=numeric))
    assert len(cases) == 2 * 3**(K - h - 1) - 1
    # The exceptional phase really supplies a nonzero source, not just an
    # unresolved decision in the complementary proof.
    r = h  # Exactly for the two cases h=2 and h=3 being classified here.
    assert D == h + r + 1
    assert (4**(h + 1) * exceptional_U + 2) % 3**(r + 1) == 0
    assert 3**(K - h) % 3**(r + 1) == 0
    slope = 4 * Fraction(8, 9)**h
    intercept = slope + 1 - 2 * Fraction(2, 3)**h
    assert Fraction(9, 4) < slope < Fraction(27, 8) and intercept > 1
    assert (slope - Fraction(9, 4)) * common_threshold > intercept - 1
    # Thus every exceptional v is strictly between y2 and y3. Its residue
    # 2 modulo3 and oddness force one of these nonzero top-band entries.
    assert all(COEFFICIENTS[5][residue] for residue in (5, 11, 17))
    exception_checks = []
    X0 = binary * ((1 + 3**h * exceptional_U) * pow(binary, -1, modulus) % modulus
                   + modulus)
    for offset in range(3):
        X = X0 + offset * period
        real_U = (X - 1) // 3**h
        v = 2**r * (4**(h + 1) * real_U + 2) // 3**r - 1
        N = 3 * X // 128
        assert 72 * N < v < 144 * N
        assert coefficient(N, v) in (-1, 2)
        x, word = v, [1] * r + [2] * h + [3]
        for a in word:
            assert valuation(3 * x + 1, 2) == a
            x = step(x)
        assert x == 3 * X // 2 - 1
        report, graph = exact_component(X, D)
        assert v in graph["sources"] and report["source_atoms"] > 3
        exception_checks.append(dict(X=X, v=v, coefficient=coefficient(N, v),
                                     component_sources=report["source_atoms"],
                                     component_mass=report["signed_source_mass"]))
    return dict(h=h, depth=D, binary_exponent=binary_exponent,
                X_ternary_modulus=modulus, U_modulus=u_modulus,
                exceptional_U=exceptional_U, common_X_threshold=common_threshold,
                X_translation_period=period, isolated_phase_count=len(cases),
                admissible_phase_count=len(cases) + 1, cases=cases,
                exceptional_phase_checks=exception_checks)


def select_zero_cost_current(X, graph):
    """Use at most actual negative capacities entering y1,y2,y3.

    Whole-component negative capacity alone would not ensure zero cost if
    the sources joined only above y3. This routine checks actual placement.
    """
    y1, y2, y3 = chain_for(X, 1)[:3]
    target = {y1, y2, y3}
    candidates = []
    for source, coefficient_value in graph["sources"].items():
        if coefficient_value >= 0 or source == y1:
            continue
        path, seen, x = [], set(), source
        while x not in target and x in graph["edges"] and x not in seen:
            seen.add(x)
            path.append(x)
            x = graph["edges"][x]
        if x in target:
            candidates.append((len(path), source, -coefficient_value, path, x))
    candidates.sort()
    eligible = sum(row[2] for row in candidates)
    if eligible < 2:
        return eligible, None
    measure = {y1: -2, y2: 2, y3: 2}
    current = Counter({y1: -2})
    selected, remaining = [], 2
    for _, source, capacity, _, _ in candidates:
        amount = min(capacity, remaining)
        if not amount:
            break
        measure[source] = -amount
        x, path = source, []
        while x != y3:
            assert x in graph["edges"] and len(path) <= len(graph["nodes"])
            current[x] -= amount
            path.append(x)
            x = graph["edges"][x]
        selected.append(dict(source=source, used_capacity=amount, path=path + [y3]))
        remaining -= amount
    assert remaining == 0 and sum(measure.values()) == 0
    current = {x: c for x, c in current.items() if c}
    assert all(c < 0 for c in current.values())
    divergence = Counter()
    for x, c in current.items():
        assert graph["edges"][x] == step(x)
        divergence[x] += c
        divergence[step(x)] -= c
    assert {x: c for x, c in divergence.items() if c} == measure
    N = 3 * X // 128
    for x, c in measure.items():
        actual = coefficient(N, x)
        assert 0 < c <= actual if c > 0 else actual <= c < 0
    return eligible, dict(source_rows=sorted(map(list, measure.items())),
                          current_rows=sorted(map(list, current.items())),
                          selected_negative_paths=selected,
                          positive_current_cost=0, removed_positive_mass=4,
                          entire_component_certified=(measure == graph["sources"]))


def representative_scan(h):
    """Finite check of EVERY old-family U class, using one specified X each."""
    parameters = family_parameters(h, 47)
    D, M, B = 2 * h + 1, parameters["ternary_modulus"], 2**20
    u_modulus = M // 3**h
    rows, certificates, histogram = [], [], Counter()
    max_states = max_queries = 0
    for U in range(u_modulus):
        if U % 3 == 0:
            continue
        X = B * ((1 + 3**h * U) * pow(B, -1, M) % M + M)
        report, graph = exact_component(X, D)
        extra_negative = sum(-c for x, c in graph["sources"].items()
                             if c < 0 and x != 3 * X // 2 - 1)
        eligible, certificate = select_zero_cost_current(X, graph)
        row = dict(U_phase=U, X=X, N=3 * X // 128,
                   source_atoms=report["source_atoms"],
                   signed_component_mass=report["signed_source_mass"],
                   extra_negative_capacity=extra_negative,
                   negative_capacity_entering_first_three=eligible,
                   linked_to_1=report["linked_to_1"],
                   vertices=report["vertices"], queries=report["reachability_queries"])
        assert not report["linked_to_1"]
        rows.append(row)
        histogram[(min(eligible, 2), report["source_atoms"] == 3)] += 1
        max_states = max(max_states, report["vertices"])
        max_queries = max(max_queries, report["reachability_queries"])
        if certificate:
            certificates.append(dict(U_phase=U, X=X, N=3 * X // 128,
                                     full_component_source_rows=report["sources"],
                                     certificate=certificate))
    return dict(h=h, depth=D, U_modulus=u_modulus,
                admissible_classes=len(rows), binary_exponent=20,
                representatives_per_class=1, phase_scan_sha256=digest(rows),
                finite_summary=[dict(eligible_negative_capacity_capped_at_2=k[0],
                                     exactly_three_sources=k[1], count=count)
                                for k, count in sorted(histogram.items())],
                maximum_states=max_states, maximum_queries=max_queries,
                certificates=certificates,
                universal_classification_inferred_from_scan=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    coverage = []
    for h in (2, 3):
        first, second = family_parameters(h, 47), family_parameters(h, 155)
        modulus = 3**(first["r"] + 4)
        u_classes = sorted(((p["X_residue"] - 1) // 3**h) % modulus
                           for p in (first, second))
        assert len(set(u_classes)) == 2 and all(U % 3 for U in u_classes)
        coverage.append(dict(h=h, r=first["r"], U_modulus=modulus,
                             admissible_classes=2 * 3**(first["r"] + 3),
                             delayed_family_classes=u_classes,
                             covered_fraction=str(Fraction(1, 3**(first["r"] + 3)))))
    symbolic = [symbolic_phase_family(2, 5, 5, 16),
                symbolic_phase_family(3, 7, 7, 31)]
    scans = [representative_scan(2), representative_scan(3)]
    ray_proof = prove_chain_lift(393216, 5, query_cap=30000)
    assert ray_proof["receipt"]["K"] == 5
    report, graph = exact_component(2**24, 5)
    assert graph["sources"] == dict(zip(chain_for(2**24, 5)[:3], (-2, 2, 2)))
    ray = dict(receipt=ray_proof["receipt"], graph_report=report,
               nodes=sorted(graph["nodes"]), arrows=sorted(map(list, graph["edges"].items())),
               ladder_index_residue=2, ladder_index_modulus=27,
               fixed_exact_ternary_order=2,
               query_table_sha256=digest(ray_proof["queries"]),
               comparison_table_sha256=digest(ray_proof["comparisons"]))
    result = dict(status="PASS", proof="PHASE_COVERAGE.md",
                  independently_reviewed_feed_commits=FEED_COMMITS,
                  original_delayed_family_coverage=coverage,
                  complete_symbolic_phase_classifications=symbolic,
                  finite_full_phase_scans=scans, required_ladder_counterfamily=ray,
                  all_phase_2h_plus_1_completion_refuted=True,
                  universal_annular_completion_proved=False, collatz_proved=False)
    path = HERE / "coverage_audit.json"
    if args.write_receipt:
        path.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == result
    print(json.dumps(dict(status="PASS", symbolic_isolated_phase_classes=70,
                          scanned_phase_representatives=sum(s["admissible_classes"] for s in scans),
                          finite_zero_cost_certificates=sum(len(s["certificates"]) for s in scans),
                          all_phase_2h_plus_1_completion_refuted=True,
                          universal_annular_completion_proved=False), indent=2))


if __name__ == "__main__":
    main()
