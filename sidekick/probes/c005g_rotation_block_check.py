"""Independent check of Lean C005-g (claude/lean-lane 1166d1b): C005's rotation-block exclusion.

Lean proves, for a primitive mechanical base v = mech(A0, m0, l0) with m0 >= 2, A0 >= m0,
gcd(A0, m0) = 1, and w a concatenation of r >= 1 rotations of v with D_w > 0:
    H < 8L for w's cycle  ==>  D_w does not divide C_w   (reduced denominator > 1).
Here, on random bases and random concatenations (any order, repetitions allowed), we check:
  (i)  the ratio bound H/L <= R^3 < 8 (C005 part (i), the hypothesis Lean still takes as given),
       where R = h/l is the base cycle's max/min ratio;
  (ii) D_w does not divide C_w;
and C005's worked example w = (1,2,2,2,2,1): C = 1805, D = 295, gcd 5, reduced denominator 59,
raw 3x+59 cycle numerators (361, 571, 443, 347, 275, 221), H/L = 571/221.
"""
import json
import math
import random
import sys
from fractions import Fraction as Fr


def C(z):
    c = 0
    for k, a in enumerate(reversed(z)):
        c = 3**k + 2**a * c
    return c


def D(z):
    return 2**sum(z) - 3**len(z)


def rot(z, i):
    i %= len(z)
    return z[i:] + z[:i]


def mech(A, m, l):
    return [((j + 1) * A + l) // m - (j * A + l) // m for j in range(m)]


def main():
    # worked example
    w = [1, 2, 2, 2, 2, 1]
    Cw, Dw = C(w), D(w)
    g = math.gcd(Cw, Dw)
    q = Dw // g
    nums = [C(rot(w, i)) // g for i in range(len(w))]
    assert (Cw, Dw, g, q) == (1805, 295, 5, 59)
    assert nums == [361, 571, 443, 347, 275, 221] and Fr(max(nums), min(nums)) == Fr(571, 221)

    rng = random.Random(57)
    n = worst = 0
    worst_ratio = Fr(0)
    for _ in range(6000):
        m0 = rng.randint(2, 12)
        A0 = rng.randint(math.ceil(m0 * math.log2(3)), 2 * m0 + 3)
        if math.gcd(A0, m0) != 1 or 2**A0 <= 3**m0:
            continue
        l0 = rng.randrange(m0)
        v = mech(A0, m0, l0)
        base = [Fr(C(rot(v, i)), D(v)) for i in range(m0)]
        R = max(base) / min(base)
        assert R < 2
        r = rng.randint(1, 6)
        w = []
        for _ in range(r):
            w += rot(v, rng.randrange(m0))
        states = [Fr(C(rot(w, i)), D(w)) for i in range(len(w))]
        ratio = max(states) / min(states)
        assert ratio <= R**3 < 8
        assert C(w) % D(w) != 0
        worst_ratio = max(worst_ratio, ratio)
        n += 1
    out = {"probe": "c005g_rotation_block_check", "lean": "claude/lean-lane 1166d1b",
           "worked_example": {"C": 1805, "D": 295, "gcd": 5, "reduced_den": 59, "H/L": "571/221"},
           "random_concatenations": n, "max_H_over_L": float(worst_ratio), "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
