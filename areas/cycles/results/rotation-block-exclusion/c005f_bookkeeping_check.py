"""Independent check of Lean C005-f (claude/lean-lane cf7865c): rotation of a power and the ofWord criteria.

  (z^k).rotate u = (z.rotate u)^k for all u (random z, k <= 5, u < 3|z|k);
  for positive words with D > 0 rotated to the minimal intercept: reduced parameter q = D/gcd(C, D)
  equals 1 iff D | C; and every rotated intercept < 8 C_w implies every height <= 2.
"""
import json
import math
import random
import sys


def C(z):
    c = 0
    for k, a in enumerate(reversed(z)):
        c = 3**k + 2**a * c
    return c


def rot(z, i):
    if not z:
        return z
    i %= len(z)
    return z[i:] + z[:i]


def main():
    rng = random.Random(56)
    n_rot = 0
    for _ in range(20000):
        z = [rng.randint(0, 4) for _ in range(rng.randint(0, 6))]
        k = rng.randint(0, 5)
        for u in range(0, 3 * max(1, len(z) * k)):
            assert rot(z * k, u) == rot(z, u) * k
            n_rot += 1
    n_q = n_b = 0
    for _ in range(40000):
        m = rng.randint(1, 12)
        w = [rng.randint(1, 4) for _ in range(m)]
        A = sum(w)
        D = 2**A - 3**m
        if D <= 0:
            continue
        Cs = [C(rot(w, i)) for i in range(m)]
        w = rot(w, Cs.index(min(Cs)))
        Cs = [C(rot(w, i)) for i in range(m)]
        g = math.gcd(Cs[0], D)
        assert (D // g == 1) == (Cs[0] % D == 0)
        n_q += 1
        if all(c < 8 * Cs[0] for c in Cs):
            n0 = Cs[0] // g
            for c in Cs:
                n = c // g
                h = 0
                while n >= 2**(h + 1) * n0:
                    h += 1
                assert h <= 2
            n_b += 1
    out = {"probe": "c005f_bookkeeping_check", "lean": "claude/lean-lane cf7865c",
           "rep_rotate_cases": n_rot, "q_eq_one_criterion_words": n_q, "B_le_two_words": n_b,
           "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
