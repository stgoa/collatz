"""Independent check of Lean R71-c (claude/lean-lane 80ec685): R71 section 3's state bound (5).

For k = 1..80 and A = bit length of 3^k (so 3^k < 2^A < 2*3^k): every phase l satisfies
6*C(mech A k l) > k*D; the reduced integer cycle (states C_(i)/g, parameter q = D/g) satisfies
6*n_i > k*q for every state; and the tightness ratio min_l (C/D) / (k/6) is reported. Also the
threshold remark: den = 1 exactly for k = 1, 2 (words (2), (2,2)) and den > 1 for every k >= 3.
"""
import json
import math
import sys
from fractions import Fraction as Fr


def C(z):
    c = 0
    for k, a in enumerate(reversed(z)):
        c = 3**k + 2**a * c
    return c


def mech(A, m, l):
    return [((j + 1) * A + l) // m - (j * A + l) // m for j in range(m)]


def main():
    ratios = []
    den_one = []
    for k in range(1, 81):
        A = (3**k).bit_length()
        assert 3**k < 2**A < 2 * 3**k
        D = 2**A - 3**k
        Cs = [C(mech(A, k, l)) for l in range(k)]
        assert all(6 * c > k * D for c in Cs)
        w = mech(A, k, 0)
        Cw = [C(w[i:] + w[:i]) for i in range(k)]
        assert Cw[0] == min(Cw)
        g = math.gcd(Cw[0], D)
        q = D // g
        assert all(6 * (c // g) > k * q for c in Cw)
        if q == 1:
            den_one.append(k)
        ratios.append(float(Fr(min(Cs), D) / Fr(k, 6)))
    assert den_one == [1, 2]
    out = {"probe": "r71c_state_bound_check", "lean": "claude/lean-lane 80ec685",
           "k_range": "1..80", "den_equal_1_for_k": den_one,
           "min_state_over_(k/6)": {"min": round(min(ratios), 3), "max": round(max(ratios), 3),
                                    "k=80": round(ratios[-1], 3)},
           "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
