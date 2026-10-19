"""Independent check of Lean C005-d (claude/lean-lane 6136784): ofWord, the integer 3x+q cycle of a
positive word at its reduced parameter (R71 section 1 as a constructor).

For random positive words w with D_w > 0, rotated to a minimal intercept, put g = gcd(C_w, D_w),
n_i = C(w.rotate i)/g, a_i = first letter of w.rotate i, q = D_w/g. Check: g divides every rotated
intercept; every n_i is a positive odd integer; the exact arrows 2^(a_i) n_(i+1) = 3 n_i + q hold
(so a_i = v2(3 n_i + q)); gcd(q, n_0) = 1 and gcd(q, 6) = 1; n_0 is the minimum; the chronological
word of the cycle is w; and distinct rotated intercepts give distinct states.
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
    i %= len(z)
    return z[i:] + z[:i]


def main():
    rng = random.Random(5)
    n_words = n_gcd_gt1 = 0
    for _ in range(40000):
        m = rng.randint(1, 14)
        w = [rng.randint(1, 5) for _ in range(m)]
        A = sum(w)
        D = 2**A - 3**m
        if D <= 0:
            continue
        Cs = [C(rot(w, i)) for i in range(m)]
        i0 = Cs.index(min(Cs))
        w = rot(w, i0)
        Cs = [C(rot(w, i)) for i in range(m)]
        g = math.gcd(Cs[0], D)
        assert all(c % g == 0 for c in Cs)
        n = [c // g for c in Cs]
        q = D // g
        assert all(x > 0 and x % 2 == 1 for x in n)
        for i in range(m):
            a = w[i]
            assert 2**a * n[(i + 1) % m] == 3 * n[i] + q
            x = 3 * n[i] + q
            assert (x & -x).bit_length() - 1 == a
        assert math.gcd(q, n[0]) == 1 and math.gcd(q, 6) == 1
        assert n[0] == min(n)
        assert len(set(Cs)) != m or len(set(n)) == m
        n_words += 1
        n_gcd_gt1 += g > 1
    out = {"probe": "c005d_ofword_check", "lean": "claude/lean-lane 6136784",
           "words": n_words, "words_with_gcd_gt_1": n_gcd_gt1, "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
