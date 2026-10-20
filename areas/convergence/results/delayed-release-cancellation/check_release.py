"""Exact checks for the delayed five-source annular cancellation.

The family proof is in DELAYED_RELEASE.md. Finite component searches below
have explicit caps; their complete graphs are separate from the universal
partial-current identity. Only the Python standard library is used.
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
from inverse_exposure_probe import coefficient, component, step


def valuation(n, prime):
    assert n > 0
    count = 0
    while n % prime == 0:
        n //= prime
        count += 1
    return count


def family_parameters(h, residue):
    """Return exact congruence and height data, or None for a skipped h.

    residue is the desired v modulo162. The returned ternary modulus
    encodes every valuation, both negative coefficients, and the exact h.
    """
    assert h >= 2 and residue in (47, 155)
    r = 0
    slope = 4 * Fraction(4, 3) ** h
    while slope > Fraction(27, 8):
        r += 1
        slope *= Fraction(2, 3)
    assert r >= 1 and Fraction(9, 4) < slope <= Fraction(27, 8)
    assert r <= h
    if slope <= Fraction(81, 32):
        return None
    inner_modulus = 3 ** (r + 4)
    u_residue = (pow(4, -(h + 1), inner_modulus)
                 * (3**r * pow(2, -r, inner_modulus) * (residue + 1) - 2)
                 % inner_modulus)
    assert u_residue % 3 == 1
    modulus = 3**h * inner_modulus
    x_residue = (1 + 3**h * u_residue) % modulus
    constant = slope + 1 - 2 * Fraction(2, 3) ** r
    threshold = (constant + Fraction(1, 2)) / (slope - Fraction(81, 32))
    minimum_x = max(1024, threshold.numerator // threshold.denominator + 1)
    binary_exponent = max(h + 5, 10)
    binary = 2**binary_exponent
    x0 = binary * (x_residue * pow(binary, -1, modulus) % modulus)
    period = binary * modulus
    if x0 < minimum_x:
        x0 += ((minimum_x - x0 + period - 1) // period) * period
    return dict(h=h, r=r, v_residue_mod_162=residue,
                slope=str(slope), constant=str(constant),
                ternary_modulus=modulus, X_residue=x_residue,
                binary_exponent=binary_exponent, minimum_X=minimum_x,
                first_X=x0, X_period=period)


def construct(parameters, X):
    """Construct and check the actual five-source submeasure and current."""
    h, r = parameters["h"], parameters["r"]
    assert X >= parameters["minimum_X"]
    assert X % 2**parameters["binary_exponent"] == 0
    assert X % parameters["ternary_modulus"] == parameters["X_residue"]
    assert valuation(X - 1, 3) == h
    N = 3 * X // 128
    assert 8 <= N and N % 8 == 0 and 128 * N == 3 * X
    U = (X - 1) // 3**h
    numerator = 2**r * (4**(h + 1) * U + 2)
    assert numerator % 3**r == 0
    v = numerator // 3**r - 1
    assert v % 162 == parameters["v_residue_mod_162"]
    assert (2 * v - 1) % 3 == 0
    t = (2 * v - 1) // 3
    assert (4 * t - 1) % 3 == 0
    u = (4 * t - 1) // 3
    assert u == (8 * v - 7) // 9 and (8 * v - 7) % 9 == 0
    y1, y2, y3 = 3 * X // 2 - 1, 9 * X // 4 - 1, 27 * X // 8 - 1
    assert Fraction(81, 32) * X + Fraction(1, 2) < v < y3
    assert y1 < 72 * N < t < y2 < u < v < y3
    measure = {y1: -2, y2: 2, y3: 2, u: -1, v: -1}
    assert len(measure) == 5 and sum(measure.values()) == 0
    assert all(coefficient(N, x) == c for x, c in measure.items())
    assert coefficient(N, t) == 0
    assert step(u) == t and valuation(3 * u + 1, 2) == 2
    assert step(t) == v and valuation(3 * t + 1, 2) == 1
    assert step(y1) == y2 and step(y2) == y3
    path, actual_valuations = [], []
    x = v
    for expected_valuation in [1] * r + [2] * h + [3]:
        path.append(x)
        a = valuation(3 * x + 1, 2)
        assert a == expected_valuation
        actual_valuations.append(a)
        x = step(x)
    assert x == y1 and len(set(path)) == len(path)
    assert all(x > y3 for x in path[1:])
    current = Counter({u: -1, t: -1, y1: -4, y2: -2})
    for x in path:
        current[x] -= 2
    current = dict(current)
    assert all(c < 0 for c in current.values())
    divergence = Counter()
    for x, c in current.items():
        divergence[x] += c
        divergence[step(x)] -= c
    assert {x: c for x, c in divergence.items() if c} == measure
    assert len(current) == h + r + 5
    assert -sum(current.values()) == 2 * (h + r + 1) + 8
    return dict(N=N, X=X, h=h, r=r,
                source_rows=sorted(map(list, measure.items())),
                current_rows=sorted(map(list, current.items())),
                path_v_to_y1=path + [y1], valuations=actual_valuations,
                zero_source_intermediate=t, source_mass=0,
                removed_positive_mass=4, positive_current_cost=0,
                current_l1_norm=-sum(current.values()),
                current_exposure_bound=h + r + 1,
                full_annulus_certified=False)


def finite_component(X, depth):
    """Persist an entire completed component, including every source."""
    N = 3 * X // 128
    report, graph = component(N, depth, state_cap=2000, query_cap=100000)
    assert report["status"] == "complete_component", report
    return dict(report=report, nodes=sorted(graph["nodes"]),
                arrows=sorted(map(list, graph["edges"].items())),
                state_cap=2000, query_cap=100000)


def summarize_current(check):
    """Keep regenerable family audits compact; exact first-release rows remain."""
    payload = json.dumps(check, sort_keys=True, separators=(",", ":")).encode()
    return dict(X=check["X"], N=check["N"], h=check["h"], r=check["r"],
                current_rows=len(check["current_rows"]),
                current_l1_norm=check["current_l1_norm"],
                current_exposure_bound=check["current_exposure_bound"],
                removed_positive_mass=check["removed_positive_mass"],
                positive_current_cost=check["positive_current_cost"],
                exact_construction_sha256=hashlib.sha256(payload).hexdigest())


def check_refined_isolation(h, digit):
    """Independent full-component audit at D=h+1 and exact ternary order h."""
    modulus = 3**(h + 1)
    binary = 2**max(h + 5, 10)
    X = binary * ((1 + digit * 3**h) * pow(binary, -1, modulus) % modulus)
    assert valuation(X - 1, 3) == h
    depth = h + 1
    N = 3 * X // 128
    report, graph = component(N, depth, state_cap=1000, query_cap=100000)
    assert report["status"] == "complete_component", report
    chain = [3**k * X // 2**k - 1 for k in range(1, depth + 4)]
    assert graph["nodes"] == set(chain)
    assert graph["edges"] == dict(zip(chain, chain[1:]))
    assert graph["sources"] == dict(zip(chain[:3], (-2, 2, 2)))
    assert report["signed_source_mass"] == 2 and not report["linked_to_1"]
    return dict(h=h, next_ternary_digit=digit, X=X, N=N, depth=depth,
                vertices=report["vertices"], signed_source_mass=2,
                reachability_queries=report["reachability_queries"],
                state_cap=1000, query_cap=100000)


def check_refined_ray(k):
    exponent = 6 * (k + 2)
    X = 2**exponent
    h = 2 + valuation(k + 2, 3)
    assert valuation(X - 1, 3) == h
    assert exponent >= max(h + 5, 10)
    N, depth = 3 * X // 128, h + 1
    assert N == 96 * 64**k
    report, graph = component(N, depth, state_cap=1000, query_cap=100000)
    assert report["status"] == "complete_component", report
    chain = [3**j * X // 2**j - 1 for j in range(1, depth + 4)]
    assert graph["nodes"] == set(chain)
    assert graph["edges"] == dict(zip(chain, chain[1:]))
    assert graph["sources"] == dict(zip(chain[:3], (-2, 2, 2)))
    return dict(ladder_index=k, binary_exponent=exponent, h=h, N=N,
                complete_obstruction_depth=depth,
                sufficient_exposure_lower_bound=h + 2,
                reachability_queries=report["reachability_queries"],
                state_cap=1000, query_cap=100000)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    qualified, skipped = [], []
    for h in range(2, 65):
        parameters = family_parameters(h, 47)
        (qualified if parameters else skipped).append(h)
        if parameters is None:
            assert family_parameters(h + 1, 47) is not None
    families = []
    for h in (2, 3, 5, 6, 7, 9, 12, 16, 24, 32, 48, 64):
        for residue in (47, 155):
            parameters = family_parameters(h, residue)
            if parameters is None:
                continue
            checks = [construct(parameters, parameters["first_X"]
                                + offset * parameters["X_period"])
                      for offset in (0, 1, 2)]
            families.append(dict(parameters=parameters,
                                 checks=[summarize_current(check) for check in checks]))
    # Both required-ray phases for the smallest qualifying h.
    rays = []
    for residue, exponent in ((47, 3462), (155, 546)):
        parameters = family_parameters(2, residue)
        assert parameters["ternary_modulus"] == 6561
        assert pow(2, exponent, 6561) == parameters["X_residue"]
        assert pow(2, 4374, 6561) == 1
        check = construct(parameters, 2**exponent)
        ladder_index = exponent // 6 - 2
        assert check["N"] == 96 * 64**ladder_index
        rays.append(dict(residue=residue, binary_exponent=exponent,
                         exponent_period=4374, base64_ladder_index=ladder_index,
                         ladder_index_period=729, check=summarize_current(check)))
    # The first release can be neutral or can discharge the designated block.
    neutral_x = 2583691264
    neutral = [finite_component(neutral_x, D) for D in (8, 9)]
    assert [(x["report"]["source_atoms"], x["report"]["signed_source_mass"])
            for x in neutral] == [(3, 2), (6, 2)]
    resolution_x = 14512291840
    resolved = [finite_component(resolution_x, D) for D in (4, 5)]
    assert [(x["report"]["source_atoms"], x["report"]["signed_source_mass"])
            for x in resolved] == [(3, 2), (5, 0)]
    current = construct(family_parameters(2, 155), resolution_x)
    exposed = dict(resolved[-1]["arrows"])
    assert all(exposed.get(x) == step(x) for x, _ in current["current_rows"])
    assert resolved[-1]["report"]["sources"] == current["source_rows"]
    assert not resolved[-1]["report"]["linked_to_1"]
    refined_isolation = [check_refined_isolation(h, digit)
                         for h in range(2, 17) for digit in (1, 2)]
    refined_rays = [check_refined_ray(k) for k in (0, 1, 7, 25, 79, 241)]
    result = dict(status="PASS", proof="DELAYED_RELEASE.md",
                  qualifying_h_through_64=qualified, skipped_h_through_64=skipped,
                  family_checks=families, required_ray_checks=rays,
                  neutral_first_release=neutral, resolved_first_release=resolved,
                  resolved_component_current=current,
                  refined_isolation_checks=refined_isolation,
                  refined_ladder_bound_checks=refined_rays,
                  universal_identity_is_partial=True,
                  all_depth_scope_comes_from_written_proof=True,
                  universal_full_component_resolution_proved=False,
                  universal_annular_constructor_proved=False, collatz_proved=False)
    path = HERE / "release_audit.json"
    if args.write_receipt:
        path.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == result
    print(json.dumps(dict(status="PASS", checked_parameter_families=len(families),
                          checked_currents=3 * len(families) + 3,
                          neutral_component_masses=[2, 2],
                          resolved_component_masses=[2, 0],
                          refined_isolation_components=len(refined_isolation),
                          universal_annular_constructor_proved=False), indent=2))


if __name__ == "__main__":
    main()
