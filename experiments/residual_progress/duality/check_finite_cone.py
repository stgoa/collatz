"""Reproduce the exact finite-cone audit, without numerical optimization."""

from argparse import ArgumentParser
from collections import defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
import json
from pathlib import Path

from finite_cone import (FIRST, MANTISSAS, R, contraction, finite_forcing_plan,
                         grid_cutoff, sufficient_exponent, target_index)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load_packets():
    path = ROOT / "collatz_research_20261017/right_aligned_packets.py"
    spec = spec_from_file_location("right_packets_for_cone", path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def combine(*terms):
    result = defaultdict(Fraction)
    for factor, measure in terms:
        for x, c in measure.items():
            result[x] += factor * c
    return {x: c for x, c in result.items() if c}


def counting(N):
    return {x: 1 for x in range(3, N + 1, 2)}


def check_single_cutoff(N, packets):
    nu = packets.initial(N)
    K = combine((1, nu), (3, counting(N)), (-3, counting(N // 4)))
    D = combine((3, counting(N)), (-3, counting(N // 4)),
                (-1, counting(3 * N // 2)), (-1, counting(3 * N // 4)))
    packet, eta, _ = packets.right_packets(N)
    divergence = combine((1, K), (-1, packets.push(K)))
    assert D == combine((1, packet), (1, eta), (1, divergence))
    return {"N": N, "K_rows": len(K), "D_atoms": len(D)}


def check_cone_identity(plan):
    """Check the measure identity by exact coefficients of every U_t."""
    answer = defaultdict(Fraction)
    for k, N in enumerate(plan["cutoffs"], FIRST):
        c = plan["packet_weights"][N]
        for t, factor in ((N, 3), (N // 4, -3),
                          (3 * N // 2, -1), (3 * N // 4, -1)):
            answer[t] += c * factor
        # Subtract both nonnegative rounding shells.
        high = grid_cutoff(k + 3)
        assert high >= 3 * N // 2 and high // 2 >= 3 * N // 4
        answer[high] -= c
        answer[3 * N // 2] += c
        answer[high // 2] -= c
        answer[3 * N // 4] += c
    for label in ("lower_boundary", "upper_boundary"):
        for N, c in plan[label].items():
            assert c >= 0
            answer[N] += c
    assert {N: c for N, c in answer.items() if c} == {
        plan["target_cutoff"]: Fraction(1)}
    assert max(plan["lower_boundary"]) < 96


def check_integer_gap():
    """All 64 maps and 125 half-integer currents, with 27 integer sources."""
    checked = passed = 0
    for successors in product(range(4), repeat=3):
        for current2 in product(range(-2, 3), repeat=3):
            parent = list(range(4))

            def find(x):
                while x != parent[x]:
                    x = parent[x]
                return x

            divergence2 = [0, 0, 0]
            for x, (y, c) in enumerate(zip(successors, current2), 1):
                divergence2[x - 1] += c
                if y:
                    divergence2[y - 1] -= c
                if c:
                    parent[find(x)] = find(y)
            components = [find(x) for x in range(4)]
            for source in product(range(-1, 2), repeat=3):
                checked += 1
                residual2 = [2 * mu - div
                             for mu, div in zip(source, divergence2)]
                if sum(max(0, z) for z in residual2) >= 2:
                    continue
                passed += 1
                masses = defaultdict(int)
                for component, mu in zip(components[1:], source):
                    masses[component] += mu
                assert all(mass <= 0 for component, mass in masses.items()
                           if component != components[0])
                if min(source) >= 0:
                    assert all(component == components[0]
                               for component, mu in zip(components[1:], source)
                               if mu)
    assert checked == 64 * 125 * 27
    return {"maps": 64, "half_integer_currents_per_map": 125,
            "integer_sources_per_current": 27,
            "total_cases": checked, "strict_gap_cases": passed}


def summary(plan, with_weights=False):
    result = {key: plan[key] for key in
              ("m", "target_cutoff", "target_index", "B", "forces_target")}
    result.update(packet_count=len(plan["cutoffs"]),
                  maximum_packet_cutoff=max(plan["cutoffs"]),
                  upper_boundary_mass=str(plan["upper_boundary_mass"]))
    for key in ("lower_boundary", "upper_boundary"):
        result[key] = {str(N): str(c) for N, c in plan[key].items()}
    if with_weights:
        result["packet_weights"] = {
            str(N): str(c) for N, c in plan["packet_weights"].items()}
    return result


def run():
    assert contraction() == Fraction(162742333796706147551,
                                     162889462677744140625) < 1
    assert R ** 5 > 2
    assert all(Fraction(a) / R ** i <= 12 for i, a in enumerate(MANTISSAS))
    tail_checks = []
    for m in (1, 97, 1000, 65536, 10 ** 6, 10 ** 12, 10 ** 30):
        k, B = target_index(m), sufficient_exponent(m)
        bound = 6 * R ** k * (2 / R ** 5) ** B
        assert bound < 1
        assert B == max(4, k // 5 + 1) or (
            6 * R ** k * (2 / R ** 5) ** (B - 1) >= 1)
        tail_checks.append({"m": m, "target_index": k, "B": B})
    plans = [finite_forcing_plan(97, B) for B in (8, 9, 10)]
    plans.append(finite_forcing_plan(1001))
    for plan in plans:
        check_cone_identity(plan)
    assert [p["forces_target"] for p in plans] == [False, True, True, True]
    assert finite_forcing_plan(97)["B"] == 10
    packets = load_packets()
    return {
        "status": "PASS",
        "comparison_r": str(R), "contraction": str(contraction()),
        "tail_bounds": tail_checks,
        "cones": [summary(p, with_weights=p["m"] == 97 and p["B"] == 9)
                  for p in plans],
        "single_cutoff_boundary_identities": [
            check_single_cutoff(N, packets) for N in (96, 112, 192, 5376)],
        "integer_gap_exhaustive_audit": check_integer_gap(),
        "universal_input_certificates_constructed": False,
        "collatz_proved": False,
    }


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    result = run()
    receipt = HERE / "finite_cone_audit.json"
    if args.write_receipt:
        receipt.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert json.loads(receipt.read_text()) == result
    print(json.dumps({"status": result["status"],
                      "cone_cases": len(result["cones"]),
                      "integer_gap_cases": result["integer_gap_exhaustive_audit"]["total_cases"],
                      "m97_B9_upper_mass": result["cones"][1]["upper_boundary_mass"],
                      "universal_input_certificates_constructed": False}))


if __name__ == "__main__":
    main()
