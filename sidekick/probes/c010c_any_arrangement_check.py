"""Independent check of Lean C010-c (claude/lean-lane b192b3c): C010 section 2 for any cycle and any arrangement.

On every actual REDUCED (gcd(q, n_0) = 1) 3x+q cycle (ordered or not; q in 5, 7, 11, 13, 17, 19, 23, 29, 61, 233, 1201):
scaled states Z_i = 2^(B-h_i) n_i (unsorted, chronological). For the sorted arrangement and 20 random
permutations sigma of one period: gcd of the complete gaps of Z o sigma is 1, and the least common
denominator of the complete gaps of (Z o sigma)/q is exactly q; also lcd(Z/q) = q.
"""
import json
import math
import random
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles  # noqa: E402
from c010b_gap_lattice_check import cgap, lcm_den  # noqa: E402


def main():
    rng = random.Random(10)
    n_cyc = n_arr = n_nonreduced = 0
    for q, N in [(5, 40001), (7, 40001), (13, 40001), (61, 40001), (11, 20001), (17, 20001),
                 (19, 20001), (23, 20001), (29, 20001), (233, 20001), (1201, 8001)]:
        for cyc in cycles(q, N):
            if math.gcd(q, min(cyc)) != 1:
                n_nonreduced += 1     # e.g. the fixed point n = q: outside the theorem (hred)
                continue
            L = min(cyc)
            h = []
            for x in cyc:
                k = 0
                while x >= 2**(k + 1) * L:
                    k += 1
                h.append(k)
            B = max(h)
            Z = [2**(B - t) * x for t, x in zip(h, cyc)]
            m = len(Z)
            assert lcm_den([Fr(z, q) for z in Z]) == q
            arrangements = [sorted(range(m), key=lambda i: Z[i])]
            for _ in range(20):
                p = list(range(m))
                rng.shuffle(p)
                arrangements.append(p)
            for sig in arrangements:
                Zs = [Z[i] for i in sig]
                G = cgap(Zs)
                assert math.gcd(*G) == 1 if m > 1 else G[0] % 2 == 1
                assert lcm_den(cgap([Fr(z, q) for z in Zs])) == q
                n_arr += 1
            n_cyc += 1
    out = {"probe": "c010c_any_arrangement_check", "lean": "claude/lean-lane b192b3c",
           "reduced_actual_cycles_all_orders": n_cyc, "non_reduced_skipped": n_nonreduced,
           "arrangements_checked": n_arr, "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
