"""Recompute the finite-cone part of the legacy receipt finite_cone_audit.json.

Written at the B09-residual-R11-R24 migration; the legacy checker in this folder
loads experiments/packet_currents/right_aligned_packets.py by its pre-migration
path and no longer runs. Standard library, exact rational arithmetic.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

It imports the legacy library finite_cone.py from its own folder (unchanged) and
checks, against the stored receipt:
  - r = 35/27, the exact contraction lambda(r) < 1, r^5 > 2, a_i / r^i <= 12;
  - the sufficient block exponent B for the seven stored targets m;
  - the four stored cone plans (m = 97 with B = 8, 9, 10; m = 1001 with the
    automatic B): target, block, packet count, largest cutoff, exact upper
    boundary mass T, forcing flag (T < 1), every lower and upper boundary
    coefficient, and the 30 packet weights of the m = 97, B = 9 plan;
  - for each plan, the measure identity (4) of the README, coefficient by
    coefficient over the counting measures U_t, including both rounding shells.
It does not recheck the single-cutoff boundary identities (they need the
right-aligned packets) or the exhaustive integer-gap audit.
"""

import importlib.util
import json
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("finite_cone_b09", HERE / "finite_cone.py")
FC = importlib.util.module_from_spec(spec)
spec.loader.exec_module(FC)
failures = []


def require(ok, message):
    if not ok:
        failures.append(message)


def identity_holds(plan):
    answer = defaultdict(Fraction)
    for k, N in enumerate(plan["cutoffs"], FC.FIRST):
        c = plan["packet_weights"][N]
        for t, factor in ((N, 3), (N // 4, -3), (3 * N // 2, -1), (3 * N // 4, -1)):
            answer[t] += c * factor
        high = FC.grid_cutoff(k + 3)
        if not (high >= 3 * N // 2 and high // 2 >= 3 * N // 4):
            return False
        answer[high] -= c
        answer[3 * N // 2] += c
        answer[high // 2] -= c
        answer[3 * N // 4] += c
    for label in ("lower_boundary", "upper_boundary"):
        for N, c in plan[label].items():
            if c < 0:
                return False
            answer[N] += c
    return {N: c for N, c in answer.items() if c} == {plan["target_cutoff"]: Fraction(1)}


def main():
    receipt = json.loads((HERE / "finite_cone_audit.json").read_text())
    R = FC.R
    require(str(R) == receipt["comparison_r"] == "35/27", "comparison ratio")
    lam = FC.contraction()
    require(str(lam) == receipt["contraction"] and lam < 1, "contraction lambda(35/27)")
    require(R ** 5 > 2 and all(Fraction(a) / R ** i <= 12 for i, a in enumerate(FC.MANTISSAS)),
            "r^5 > 2 and a_i/r^i <= 12")
    for row in receipt["tail_bounds"]:
        k, B = FC.target_index(row["m"]), FC.sufficient_exponent(row["m"])
        require((k, B) == (row["target_index"], row["B"]), f"tail bound m={row['m']}")
        require(6 * R ** k * (2 / R ** 5) ** B < 1, f"tail inequality m={row['m']}")
    for stored in receipt["cones"]:
        B = stored["B"] if stored["m"] == 97 else None
        plan = FC.finite_forcing_plan(stored["m"], B)
        got = dict(m=plan["m"], target_cutoff=plan["target_cutoff"], target_index=plan["target_index"],
                   B=plan["B"], forces_target=plan["forces_target"], packet_count=len(plan["cutoffs"]),
                   maximum_packet_cutoff=max(plan["cutoffs"]),
                   upper_boundary_mass=str(plan["upper_boundary_mass"]))
        for key in ("lower_boundary", "upper_boundary"):
            got[key] = {str(N): str(c) for N, c in plan[key].items()}
        if "packet_weights" in stored:
            got["packet_weights"] = {str(N): str(c) for N, c in plan["packet_weights"].items()}
        require(got == stored, f"cone plan m={stored['m']} B={stored['B']} differs from the receipt")
        require(plan["forces_target"] == (plan["upper_boundary_mass"] < 1), f"forcing flag m={stored['m']}")
        require(identity_holds(plan), f"measure identity m={stored['m']} B={plan['B']}")
    require(FC.finite_forcing_plan(97)["B"] == 10, "automatic B for m = 97")
    if failures:
        print("FAIL: " + "; ".join(failures))
        sys.exit(1)
    b9 = receipt["cones"][1]
    print(f"PASS: lambda(35/27) < 1, {len(receipt['tail_bounds'])} tail bounds, "
          f"{len(receipt['cones'])} cone plans; m=97, B=9: {b9['packet_count']} packets, T = {b9['upper_boundary_mass']}")


if __name__ == "__main__":
    main()
