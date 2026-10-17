"""Check the finite arithmetic barrier proving unbounded exposure at h=2.

No full-annulus scan is used. Finite positive and negative-map orbit tables
certify a barrier for every inverse word; selected complete-component checks
independently verify the resulting prediction. See FIXED_H_DEPTH.md.
"""

import argparse
from fractions import Fraction
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "templates"))
from inverse_exposure_probe import component, step


def valuation(n, prime):
    assert n > 0
    exponent = 0
    while n % prime == 0:
        exponent += 1
        n //= prime
    return exponent


def negative_step(c):
    assert c > 0 and c % 2
    numerator = 3 * c - 1
    return numerator // (numerator & -numerator)


def finite_barrier():
    positive_paths = []
    orbit_states = set()
    for initial in range(1, 34, 2):
        path, x = [], initial
        while x != 1:
            assert x not in path and len(path) < 100
            path.append(x)
            x = step(x)
        path.append(1)
        positive_paths.append(dict(initial=initial, path=path))
        orbit_states.update(path)
    assert len(orbit_states) == 54 and max(orbit_states) == 3077

    smooth = set()
    three_power = 1
    while 9 * three_power < max(orbit_states):
        value = three_power
        while 9 * value < max(orbit_states):
            if value >= 4:
                smooth.add(value)
            value *= 2
        three_power *= 3

    candidates = []
    minus_orbits = {}
    for z in sorted(orbit_states):
        for u in sorted(smooth):
            c = 10 * u - z
            if not 0 < c < u or c % 2 == 0:
                continue
            if c == 1:
                outcome = "excluded: every inverse valuation would equal1"
            else:
                path, x = [], c
                while x not in path:
                    assert x != 1 and len(path) < 100
                    path.append(x)
                    x = negative_step(x)
                cycle_start = path.index(x)
                minus_orbits[c] = dict(path=path, repeat=x,
                                       cycle=path[cycle_start:])
                outcome = "excluded: negative-map orbit cycles away from1"
            candidates.append(dict(z=z, u=u, c=c, outcome=outcome))
    assert len(candidates) == 22
    assert sum(row["c"] == 1 for row in candidates) == 6
    assert len(minus_orbits) == 12
    return dict(shadow_reference=10, forbidden_odd_shadow_maximum=33,
                allowed_shadow_minimum=35,
                slope_lower_bound=str(Fraction(35, 10)),
                annular_top_slope=str(Fraction(27, 8)),
                positive_paths=positive_paths,
                positive_orbit_union=sorted(orbit_states),
                candidates=candidates,
                negative_orbits=[dict(c=c, **row)
                                 for c, row in sorted(minus_orbits.items())])


def exponent_for_ten(depth):
    """Find e with 2^e=10 modulo3^(D+2), without materializing 2^e."""
    exponent, modulus, order = 0, 3, 2
    assert pow(2, exponent, modulus) == 10 % modulus
    for _ in range(depth + 1):
        next_modulus = 3 * modulus
        candidates = [exponent + digit * order for digit in range(3)
                      if pow(2, exponent + digit * order, next_modulus)
                      == 10 % next_modulus]
        assert len(candidates) == 1
        exponent = candidates[0]
        modulus, order = next_modulus, order * 3
    assert modulus == 3**(depth + 2) and order == 2 * 3**(depth + 1)
    assert exponent % 6 == 0 and valuation(exponent, 3) == 1
    while exponent < max(depth + 4, 12):
        exponent += order
    assert pow(2, exponent, modulus) == 10
    return dict(depth=depth, ternary_modulus=modulus,
                exponent=exponent, exponent_period=order,
                ladder_index=exponent // 6 - 2,
                ladder_index_period=3**depth)


def check_component(X, depth, label):
    assert X % 2**max(depth + 4, 10) == 0
    assert X % 3**(depth + 2) == 10 % 3**(depth + 2)
    assert valuation(X - 1, 3) == 2
    N = 3 * X // 128
    report, graph = component(N, depth, state_cap=2000, query_cap=100000)
    assert report["status"] == "complete_component", report
    chain = [3**k * X // 2**k - 1 for k in range(1, depth + 4)]
    assert graph["nodes"] == set(chain)
    assert graph["edges"] == dict(zip(chain, chain[1:]))
    assert graph["sources"] == dict(zip(chain[:3], (-2, 2, 2)))
    assert report["signed_source_mass"] == 2 and not report["linked_to_1"]
    return dict(label=label, X=X, report=report,
                vertices=chain, arrows=sorted(map(list, graph["edges"].items())))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    barrier = finite_barrier()
    assert Fraction(35, 10) > Fraction(27, 8)
    assert 9 * (1024 - 1) > Fraction(27, 8) * 1024 - 1
    checks = []
    for depth in (1, 2, 5, 8, 12):
        binary, ternary = 2**max(depth + 4, 10), 3**(depth + 2)
        X = binary * ((10 * pow(binary, -1, ternary)) % ternary + ternary)
        checks.append(check_component(X, depth, "CRT representative"))
    rays = [exponent_for_ten(depth) for depth in (1, 2, 3, 5, 12, 32, 64)]
    for ray in rays[:3]:
        checks.append(check_component(2**ray["exponent"], ray["depth"],
                                      "required ladder representative"))
    result = dict(status="PASS", proof="FIXED_H_DEPTH.md", exact_h=2,
                  arbitrary_depth_theorem=True,
                  complete_annular_source_accounting=True,
                  finite_barrier_certificate=barrier,
                  numerical_complete_components=checks,
                  symbolic_required_ray_exponents=rays,
                  bounded_depth_function_of_h_refuted=True,
                  universal_annular_completion_proved=False,
                  collatz_proved=False)
    receipt = HERE / "fixed_h_audit.json"
    if args.write_receipt:
        receipt.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert json.loads(receipt.read_text()) == result
    print(json.dumps(dict(status="PASS", exact_h=2,
                          arbitrary_depth_theorem=True,
                          finite_barrier_candidate_count=len(barrier["candidates"]),
                          complete_component_checks=len(checks),
                          maximum_component_queries=max(
                              row["report"]["reachability_queries"] for row in checks),
                          bounded_depth_function_of_h_refuted=True,
                          universal_annular_completion_proved=False), indent=2))


if __name__ == "__main__":
    main()
