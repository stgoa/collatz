"""S4 addendum (Lean lane's structural test): on realised ordered band-1 profiles with g = gcd(C_w, D) > 1,
does g divide some block denominator 2^(A_u) - 3^|u| for a proper cyclic sub-block u of the word?
Also: tightness of the formal bound g <= C_c / n_0 (C006-e's D_mul_n_le, n_0 = C_w / g the reduced minimum),
and the exact identity g = C_w / n_0.
"""
import json
import math
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s4_band1_gcd import realise, profiles  # noqa: E402


def main():
    hit = Counter()
    ratios = []
    examples_miss = []
    n_g = 0
    for m in range(3, 19):
        for A in range(m + 1, 2 * m):
            s = A - m
            if math.gcd(s, m) != 1 or 2**A <= 3**m:
                continue
            for S1 in profiles(m, s):
                r = realise(m, A, S1)
                if r is None:
                    continue
                a, C, D = r
                g = math.gcd(C, D)
                if g == 1:
                    continue
                n_g += 1
                n0 = C // g
                assert g * n0 == C
                # normalised (mechanical) intercept C_c of the c-word: c_i = a_i + h_(i+1) - h_i
                rank = [(i * s) % m for i in range(m)]
                h = [1 if rr in S1 else 0 for rr in rank]
                c = [a[i] + h[(i + 1) % m] - h[i] for i in range(m)]
                P, Cc = 0, 0
                for j in range(m):
                    Cc += 3**(m - 1 - j) * 2**P
                    P += c[j]
                assert g <= Cc // n0
                ratios.append(g / (Cc / n0))
                found = None
                for length in range(1, m):
                    for start in range(m):
                        u = [a[(start + k) % m] for k in range(length)]
                        Du = 2**sum(u) - 3**length
                        if Du != 0 and Du % g == 0:
                            found = (start, length)
                            break
                    if found:
                        break
                hit['divides a block D' if found else 'no block D'] += 1
                if not found and len(examples_miss) < 6:
                    examples_miss.append((m, A, sorted(S1), g))
    out = {"probe": "s4b_block_divisor_test", "profiles_with_g_gt_1_(m<=18, exhaustive)": n_g,
           "g_divides_some_proper_block_D": dict(hit),
           "g_over_formal_bound_Cc_over_n0": {"min": round(min(ratios), 6), "max": round(max(ratios), 6)},
           "examples_no_block": examples_miss}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
