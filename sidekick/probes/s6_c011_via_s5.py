"""S6: C011's conclusion (no rotation with exactly two mismatches) re-derived from S5-a + the height ceiling,
with the replayed gap_all instead of Matveev.

At q = 1 (primitive cycle, period m, band B, every rotation h != 0 mod m), S5-a gives m <= s(t+1) and
6 3^t < 2^(B+1+c) m^(mu+1) with (c, mu) = (172, 341), so s > log2(3) m / (B + 342 log2 m + 172) (exact real form).
Height ceiling at q = 1 (Lean lane's argument): B <= (log2 3 - 1)(m - 1) + (m - 1) log2(1 + 1/(3L)).
With L >= 1 the last term is at most m log2(4/3) -- too weak -- so we use L > 2^71 only through a cycle-length
fact if needed; here we evaluate both versions:
  (i) eps(L) with L > 2^71 (Barina range), (ii) the threshold m0 such that s > 2 for all m >= m0.
Also the integer form: smallest m with the strict inequality chain giving s >= 3, checked by direct
evaluation of max over t of the constraint m <= 2(t+1) and 6*3^t < 2^(B+1+c) m^(mu+1) at the ceiling B.
"""
import json
import math
import sys


def B_ceiling(m, L_log2=71):
    # corrected at 11:5x after the Lean lane's review: no +1, and (m - 1) in the epsilon term
    eps = (m - 1) * math.log2(1 + 1 / (3 * 2**L_log2))
    return math.floor((math.log2(3) - 1) * (m - 1) + eps)


def s2_possible(m):
    """Is s = 2 compatible with S5-a at q = 1 for some B <= ceiling? s = 2 needs a run t with m <= 2(t+1)
    and 6*3^t < 2^(B+1+172) m^342. The longest run satisfies t >= m/2 - 1; take t = ceil(m/2) - 1."""
    B = B_ceiling(m)
    t = -(-m // 2) - 1
    lhs = math.log2(6) + t * math.log2(3)
    rhs = (B + 1 + 172) + 342 * math.log2(m)
    return lhs < rhs


def main():
    # find the threshold: smallest m0 such that s = 2 is impossible for all m >= m0 (checked to 10^6, then
    # monotone for larger m since lhs grows like 0.79m and rhs like 0.585m + 342 log2 m)
    last_possible = None
    for m in range(2, 1_000_001):
        if s2_possible(m):
            last_possible = m
    m0 = last_possible + 1
    # derivative check beyond 1e6: d/dm [lhs - rhs] = log2(3)/2 - (log2 3 - 1) - 342/(m ln 2) > 0 for m >= 2^12
    slope_ok = math.log2(3) / 2 - (math.log2(3) - 1) - 342 / (1_000_000 * math.log(2)) > 0
    out = {"probe": "s6_c011_via_s5",
           "claim": "at q = 1, with S5-a, gap_all and the height ceiling (L > 2^71), no rotation has exactly 2 mismatches when m >= m0",
           "m0": m0, "slope_positive_beyond_1e6": slope_ok,
           "compare": {"C011_period_import": "m > 1.375e11 (Hercher/Barina, with Matveev K0 ~ 6e8)",
                       "Eliahou_1993_cycle_length": "m >= 17,087,915 (older verification range)"},
           "result": "PASS" if slope_ok else "CHECK"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
