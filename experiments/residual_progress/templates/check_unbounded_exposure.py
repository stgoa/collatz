"""Exact finite audits for the written arbitrary-depth aggregate obstruction.

The all-depth claim follows from the proof in UNBOUNDED_EXPOSURE_DEPTH.md,
not from these finite samples. Every exploratory enumeration has a cap.
"""

import argparse
from fractions import Fraction
import json
from pathlib import Path

from inverse_exposure_probe import coefficient, component, step

HERE = Path(__file__).resolve().parent


def crt_parameter(depth):
    """Small positive CRT representative; not necessarily on a required ray."""
    assert depth >= 1
    binary = 2 ** max(depth + 4, 10)
    modulus = 3 ** (depth + 2)
    return binary * pow(binary, -1, modulus)


def check_hypotheses(X, depth):
    assert depth >= 1 and X > 0
    assert X % (2 ** max(depth + 4, 10)) == 0
    assert X % (3 ** (depth + 2)) == 1
    assert 3 * X % 128 == 0
    N = 3 * X // 128
    assert N > 0 and N % 8 == 0 and X >= 1024
    return N


def check_component(X, depth, family):
    N = check_hypotheses(X, depth)
    chain = []
    for k in range(1, depth + 4):
        assert (3**k * X) % (2**k) == 0
        y = 3**k * X // 2**k - 1
        assert y > 1 and y % 2
        chain.append(y)
    assert [coefficient(N, y) for y in chain] == [-2, 2, 2] + [0] * depth
    assert all(step(x) == y for x, y in zip(chain, chain[1:]))
    report, graph = component(N, depth, state_cap=1000, query_cap=100000)
    assert report["status"] == "complete_component", report
    assert graph["nodes"] == set(chain)
    assert graph["edges"] == dict(zip(chain, chain[1:]))
    assert graph["sources"] == dict(zip(chain[:3], (-2, 2, 2)))
    assert report["signed_source_mass"] == 2
    assert report["positive_component_obstruction"] and not report["linked_to_1"]
    return dict(family=family, depth=depth, X=X, N=N,
                vertices=len(chain), arrows=len(chain) - 1,
                sources=[[x, c] for x, c in zip(chain[:3], (-2, 2, 2))],
                signed_source_mass=2, queries=report["reachability_queries"],
                first_state=chain[0], last_state=chain[-1],
                state_cap=1000, query_cap=100000)


def check_induction_constants():
    # These are the rational boundary cases in the written invariant proof.
    assert min(3**r * 2**s for r, s in ((0, 2), (1, 1), (2, 0))) == 4
    assert 3**2 == 9
    assert Fraction(2, 3) * 9 == 6
    assert Fraction(4, 3) * 4 > 4
    assert Fraction(2, 3) * 6 == 4
    assert Fraction(2, 3) * 11 > 4
    # Every solution of 2^a*z=16 with a>=1 and positive odd z is listed.
    solutions = [(a, 16 // 2**a) for a in range(1, 5)
                 if 16 % 2**a == 0 and (16 // 2**a) % 2]
    assert solutions == [(4, 1)]
    assert Fraction(16, 3) * 4 > 6
    assert 4 * (8 - 1) > Fraction(27, 8) * 8 - 1
    return dict(first_integer_slope_minimum=4, even_arrival_slope_minimum=9,
                even_to_odd_slope_minimum=6, new_shadow_5_inverse=[[4, 1]],
                height_comparison_valid_from_X=8)


def check_shadow_words(depth=6, maximum_valuation=8, state_cap=50000):
    """Enumerate bounded actual inverse words and check every proof invariant.

    This complements the algebraic induction; the valuation/depth limits
    are explicitly finite and are not used to infer its universal scope.
    """
    X = crt_parameter(depth)
    N = check_hypotheses(X, depth)
    cases = [0] * (depth + 1)
    before_integer = even_arrivals = odd_arrivals = 0
    smallest_slope = None
    visits = 0
    for k in range(1, depth + 4):
        initial = Fraction(3**k, 2**k)
        stack = [(0, 0, initial, Fraction(1), False)]
        while stack:
            length, total_valuation, u, c, integer_seen = stack.pop()
            if length == depth:
                continue
            current = u * X - c
            assert current.denominator == 1 and current > 1
            actual = current.numerator
            for a in range(1, maximum_valuation + 1):
                if length == 0 and a < 3:
                    continue
                numerator = 2**a * actual - 1
                if numerator % 3:
                    continue
                predecessor = numerator // 3
                assert predecessor > 1 and predecessor % 2
                assert step(predecessor) == actual
                next_u = 2**a * u / 3
                next_c = (2**a * c + 1) / 3
                shadow = next_u - next_c
                next_length, next_total = length + 1, total_valuation + a
                assert next_u == Fraction(3**k * 2**next_total,
                                          3**next_length * 2**k)
                assert next_u * X - next_c == predecessor
                assert next_c > 0 and shadow > 0
                assert next_total - next_length >= 2
                assert next_u >= 4
                assert predecessor > 144 * N - 1
                if next_total < k:
                    assert not integer_seen
                    assert next_c.denominator == 1 and next_c.numerator % 2
                    assert shadow.denominator != 1
                    assert next_length < k and next_u >= 9
                    before_integer += 1
                else:
                    assert shadow.denominator == 1
                    assert (Fraction(predecessor) - shadow) % 3 == 0
                    if not integer_seen:
                        assert next_length <= k and next_u.denominator == 1
                        assert next_c.denominator == 1 and next_c.numerator % 2
                        if shadow.numerator % 2 == 0:
                            assert next_u >= 9
                            even_arrivals += 1
                        else:
                            odd_arrivals += 1
                    else:
                        assert shadow.numerator % 2
                    if shadow == 5:
                        assert next_u >= 6
                visits += 1
                if visits > state_cap:
                    raise RuntimeError("bounded shadow-word audit reached its cap")
                cases[next_length] += 1
                smallest_slope = (next_u if smallest_slope is None
                                  else min(smallest_slope, next_u))
                stack.append((next_length, next_total, next_u, next_c,
                              integer_seen or next_total >= k))
    return dict(depth_cap=depth, valuation_cap=maximum_valuation,
                state_cap=state_cap, X=X, N=N, histories=visits,
                histories_by_length=cases, pre_integer_histories=before_integer,
                even_first_arrivals=even_arrivals, odd_first_arrivals=odd_arrivals,
                smallest_slope=str(smallest_slope))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    constants = check_induction_constants()
    shadow_words = check_shadow_words()
    crt_depths = (1, 2, 4, 8, 12, 16, 24, 32)
    crt_checks = [check_component(crt_parameter(D), D, "CRT") for D in crt_depths]
    ray_checks = []
    for D in (1, 2, 3, 4):
        e = 2 * 3 ** (D + 1)
        X = 2**e
        result = check_component(X, D, "required_ray_12")
        assert result["N"] == 12 * 2 ** (e - 9)
        result["ray_exponent"] = e - 9
        result["base64_ladder_index"] = 3**D - 2
        assert result["N"] == 96 * 64 ** result["base64_ladder_index"]
        ray_checks.append(result)
    modular_checks = []
    for D in (1, 2, 4, 8, 16, 32, 64, 128):
        e = 2 * 3 ** (D + 1)
        modulus = 3 ** (D + 2)
        assert e >= max(D + 4, 10) and e - 9 >= 3
        assert pow(2, e, modulus) == 1
        modular_checks.append(dict(depth=D, binary_exponent=e,
                                   ternary_modulus=modulus,
                                   power_of_two_materialized=False))
    result = dict(status="PASS", proof="UNBOUNDED_EXPOSURE_DEPTH.md",
                  induction_constants=constants, bounded_shadow_word_audit=shadow_words,
                  exact_crt_components=crt_checks, exact_required_ray_components=ray_checks,
                  modular_ray_existence_checks=modular_checks,
                  all_depth_claim_is_from_written_induction_not_finite_scan=True,
                  universal_current_construction_proved=False, collatz_proved=False)
    path = HERE / "unbounded_exposure_audit.json"
    if args.write_receipt:
        path.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == result
    print(json.dumps(dict(status="PASS", bounded_inverse_histories=shadow_words["histories"],
                          crt_component_depths=list(crt_depths),
                          required_ray_component_depths=[1, 2, 3, 4],
                          largest_modular_depth=128,
                          all_depth_claim_is_from_written_induction_not_finite_scan=True), indent=2))


if __name__ == "__main__":
    main()
