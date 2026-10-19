"""S5: main's C013 (6) made quantitative with the replayed gap_all (two-library composition).

Inputs: C013-b (Lean, 9a81b08): for any agreeing run (t, E) of a word with a nonidentity rotation of a
primitive cycle, 6 D max(2^E, 3^t) < m q 2^A (2^(B+1) - 1). Pigeonhole: a rotation with s mismatches has an
agreeing run of length >= ceil((m - s)/s). gap_all (mmusson, replayed EXT-1): 2^A <= 2^172 m^341 D.
At q = 1 these give  3^t < 2^(B+173) m^342 / 6  and  s > m / (1 + (B + 342 log2 m + 173 - log2 6) / log2 3)
= log2(3) m / (B + 342 log2 m + 172)  (constant corrected at 11:35 after the Lean lane review; was 172 - log2 6).

Checks: (a) on actual 3x+q cycles (odd q < 200, 3 not dividing q), for every nonidentity rotation h: the
longest maximal agreeing run t_max(h) >= ceil((m - s_h)/s_h) and (7) holds for that run (exact integers);
(b) the q = 1 bound evaluated at the literature period m = 1.375e11 for several bands B, and the B at which it
drops below 3 (C011's existing exclusion of s = 2).
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402


def s_bound(m, B):
    return m / (1 + (B + 342 * math.log2(m) + 173 - math.log2(6)) / math.log2(3))   # = log2(3) m / (B + 342 log2 m + 172)


def main():
    n_rot = n_cyc = 0
    for q in [q for q in range(1, 200, 2) if q % 3 != 0]:
        for cyc in cycles(q, 4001, max_steps=4000):
            m = len(cyc)
            if m < 2:
                continue
            i0 = cyc.index(min(cyc))
            n = cyc[i0:] + cyc[:i0]
            a = [step(x, q)[1] for x in n]
            A = sum(a)
            D = 2**A - 3**m
            L, H = n[0], max(n)
            B = 0
            while H >= 2**(B + 1) * L:
                B += 1
            n_cyc += 1
            for h in range(1, m):
                agree = [a[j] == a[(j + h) % m] for j in range(m)]
                s = agree.count(False)
                assert s >= 2
                tmax, Emax = 0, 0
                for i in range(m):
                    if agree[(i - 1) % m]:
                        continue
                    t = 0
                    while t < m and agree[(i + t) % m]:
                        t += 1
                    E = sum(a[(i + j) % m] for j in range(t))
                    if t > tmax:
                        tmax, Emax = t, E
                assert tmax >= -(-(m - s) // s)
                assert 6 * D * max(2**Emax, 3**tmax) < m * q * 2**A * (2**(B + 1) - 1)
                n_rot += 1
    M = 137_500_000_000
    table = {f"B={B}": round(s_bound(M, B)) for B in [0, 2, 10, 100, 10**3, 10**4, 10**5, 10**6, 10**7]}
    # largest B for which the bound still exceeds 2 (i.e. adds to C011)
    lo, hi = 0, M
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if s_bound(M, mid) > 3:
            lo = mid
        else:
            hi = mid - 1
    out = {"probe": "s5_mismatch_height", "actual_cycles": n_cyc, "rotations_checked": n_rot,
           "q1_mismatch_lower_bound_at_m=1.375e11_by_band_B": table,
           "largest_B_with_bound_above_3": lo, "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
