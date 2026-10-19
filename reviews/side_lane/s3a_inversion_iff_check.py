"""Independent check of Lean S3-a (claude/lean-lane 95dd4a9): C005's inversion lemma as an equivalence.

For every actual 3x+q cycle found (odd q < 120, 3 not dividing q; starts <= 4001), with Z_i = 2^(B-h_i) n_i and
F_i = 3 Z_i + 2^(B-h_i) q, and every ordered pair Z_i < Z_j:
   F_j < F_i  <=>  h_i < h_j and 3 (n_j - 2^(h_j-h_i) n_i) < q (2^(h_j-h_i) - 1);
at q = 1 every inversion has h_j - h_i >= 3, and at gap exactly 3 it is n_j = 8 n_i + 1.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles  # noqa: E402


def main():
    n_pairs = n_inv = n_cyc = 0
    for q in [q for q in range(1, 120, 2) if q % 3 != 0]:
        for cyc in cycles(q, 4001, max_steps=4000):
            m = len(cyc)
            if m < 2:
                continue
            n_cyc += 1
            L = min(cyc)
            h = []
            for x in cyc:
                k = 0
                while x >= 2**(k + 1) * L:
                    k += 1
                h.append(k)
            B = max(h)
            Z = [2**(B - t) * x for t, x in zip(h, cyc)]
            F = [3 * Z[i] + 2**(B - h[i]) * q for i in range(m)]
            for i in range(m):
                for j in range(m):
                    if not Z[i] < Z[j]:
                        continue
                    n_pairs += 1
                    lhs = F[j] < F[i]
                    k = h[j] - h[i]
                    rhs = h[i] < h[j] and 3 * (cyc[j] - 2**k * cyc[i]) < q * (2**k - 1)
                    assert lhs == rhs, (q, cyc[i], cyc[j])
                    if lhs:
                        n_inv += 1
                        if q == 1:
                            assert k >= 3 and (k != 3 or cyc[j] == 8 * cyc[i] + 1)
    out = {"probe": "s3a_inversion_iff_check", "lean": "claude/lean-lane 95dd4a9", "cycles": n_cyc,
           "ordered_pairs_Zi_lt_Zj": n_pairs, "inversions": n_inv, "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
