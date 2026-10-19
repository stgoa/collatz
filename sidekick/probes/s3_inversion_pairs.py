"""S3 probe: dyadic inversion pairs inside actual cycles of 3x+q.

C005's inversion lemma: for normalised points z_i < z_j with h_j = h_i + k, the image order inverts iff
3r < q(2^k - 1), r = n_j - 2^k n_i (odd, positive). At q = 1 the only possibility with k <= 3 is k = 3,
r = 1: a pair (n, 8n + 1) with heights (0, 3). Here: every odd q < 400 (3 does not divide q), every cycle
found from odd starts <= 6001 (orbits capped at 4000 steps), every pair (n, 2^k n + r) in the cycle with
height gap exactly k and 3r < q(2^k - 1) (an actual inversion), k <= 11. Reports counts by k and the
r = 1, k = 3 examples (the q = 1 inversion type, realised here at q > 1).
"""
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles  # noqa: E402


def height(x, L):
    k = 0
    while x >= 2**(k + 1) * L:
        k += 1
    return k


def main():
    qs = [q for q in range(1, 400, 2) if q % 3 != 0]
    inv = Counter()
    r1 = []
    total = 0
    for q in qs:
        for cyc in cycles(q, 6001, max_steps=4000):
            if len(cyc) < 2:
                continue
            total += 1
            S = set(cyc)
            L = min(cyc)
            for n in cyc:
                for k in range(1, 12):
                    for r in range(1, 2 * 7 * q, 2):
                        y = 2**k * n + r
                        if y in S and height(y, L) - height(n, L) == k and 3 * r < q * (2**k - 1):
                            inv[k] += 1
                            if k == 3 and r == 1:
                                r1.append((q, n, y, len(cyc), height(n, L), height(y, L)))
    assert all(q > 1 for q, *_ in r1)
    out = {"probe": "s3_inversion_pairs", "q_range": "odd q < 400, 3 not dividing q",
           "cycles_m_ge_2": total, "inversions_by_height_gap_k": dict(sorted(inv.items())),
           "k3_r1_pairs_count": len(r1), "k3_r1_examples_(q,n,8n+1,m,h_n,h_8n+1)": r1[:12],
           "result": "data"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
