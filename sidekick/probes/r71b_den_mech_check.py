"""Independent check of Lean R71-b (claude/lean-lane c0db6af): R71's theorem (3) in full.

den(w) = D_w / gcd(C_w, D_w). For every k <= 48, the seven totals A = ceil(k log2 3) + 0..6, and
every phase l < k: den(mech(A, k, l)) == 2^(A/g) - 3^(k/g) with g = gcd(A, k), computed directly from
C and D. Also the D < 0 side (k <= A < k log2 3, where the formula still holds), the repetition
identities mech(gA0, gk0, gh + r) = mech(A0, k0, h)^g and den(z^k) = den(z), and R71's example
(k, A) = (6, 10): D = 295, den = 5.
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


def D(z):
    return 2**sum(z) - 3**len(z)


def den(z):
    g = math.gcd(C(z), D(z))
    assert D(z) % g == 0
    return D(z) // g


def mech(A, m, l):
    return [((j + 1) * A + l) // m - (j * A + l) // m for j in range(m)]


def main():
    n_pos = n_neg = n_rep = 0
    for k in range(1, 49):
        a0 = math.ceil(k * math.log2(3))
        if 2**a0 <= 3**k:
            a0 += 1
        for A in list(range(a0, a0 + 7)) + list(range(k, a0)):
            g = math.gcd(A, k)
            target = 2**(A // g) - 3**(k // g)
            for l in range(k):
                assert den(mech(A, k, l)) == target, (k, A, l)
                if target > 0:
                    n_pos += 1
                else:
                    n_neg += 1
    rng = random.Random(59)
    for _ in range(3000):
        g, k0 = rng.randint(1, 5), rng.randint(1, 8)
        A0 = rng.randint(k0, 3 * k0)
        h, r = rng.randrange(k0), rng.randrange(g)
        assert mech(g * A0, g * k0, g * h + r) == mech(A0, k0, h) * g
        z = [rng.randint(1, 4) for _ in range(rng.randint(1, 7))]
        if D(z) != 0:
            assert den(z * g) == den(z)
        n_rep += 1
    w = mech(10, 6, 0)
    assert D(w) == 295 and den(w) == 5
    out = {"probe": "r71b_den_mech_check", "lean": "claude/lean-lane c0db6af",
           "phase_words_D_pos": n_pos, "phase_words_D_neg": n_neg, "repetition_cases": n_rep,
           "example_(k,A)=(6,10)": {"D": 295, "den": 5}, "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
