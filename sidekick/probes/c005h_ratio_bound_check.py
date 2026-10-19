"""Independent check of Lean C005-h (claude/lean-lane 9d98bed): the state-bound wiring.

  C_split: 2^(sum u) C(t ++ u) = 3^|u| C(u ++ t) + D(u ++ t) C(u)   (random u, t);
  flatten_rotations_ratio, for ANY nonempty base v with D_v > 0 (not only mechanical): if every
  rotated intercept of v lies in [lo, hi] (take lo = min, hi = max), then for any concatenation w of
  r >= 1 rotations of v, C(w.rotate i) lo^3 <= C(w.rotate j) hi^3 for all i, j;
  rotation_block_exclusion_mech: for mechanical bases (m0 >= 2, coprime, 3^m0 < 2^A0) every such w
  has D_w not dividing C_w; and single_block_exclusion: (a)^r with a >= 3 has D not dividing C.
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


def rot(z, i):
    i %= len(z)
    return z[i:] + z[:i]


def mech(A, m, l):
    return [((j + 1) * A + l) // m - (j * A + l) // m for j in range(m)]


def main():
    rng = random.Random(58)
    n_split = 0
    for _ in range(20000):
        u = [rng.randint(0, 5) for _ in range(rng.randint(0, 6))]
        t = [rng.randint(0, 5) for _ in range(rng.randint(0, 6))]
        assert 2**sum(u) * C(t + u) == 3**len(u) * C(u + t) + D(u + t) * C(u)
        n_split += 1
    n_ratio = n_tight = 0
    for _ in range(8000):
        v = [rng.randint(1, 5) for _ in range(rng.randint(1, 6))]
        if D(v) <= 0:
            continue
        Cv = [C(rot(v, t)) for t in range(len(v))]
        lo, hi = min(Cv), max(Cv)
        w = []
        for _ in range(rng.randint(1, 5)):
            w += rot(v, rng.randrange(len(v)))
        Cw = [C(rot(w, i)) for i in range(len(w))]
        assert max(Cw) * lo**3 <= min(Cw) * hi**3
        n_ratio += 1
        n_tight += max(Cw) * lo**3 * 2 > min(Cw) * hi**3   # within a factor 2 of the bound
    n_mech = 0
    for _ in range(4000):
        m0 = rng.randint(2, 10)
        A0 = rng.randint(m0, 2 * m0 + 3)
        if math.gcd(A0, m0) != 1 or 3**m0 >= 2**A0:
            continue
        v = mech(A0, m0, rng.randrange(m0))
        w = []
        for _ in range(rng.randint(1, 5)):
            w += rot(v, rng.randrange(m0))
        assert C(w) % D(w) != 0
        n_mech += 1
    for a in range(3, 12):
        for r in range(1, 7):
            w = [a] * r
            assert C(w) % D(w) != 0
    out = {"probe": "c005h_ratio_bound_check", "lean": "claude/lean-lane 9d98bed",
           "C_split_cases": n_split, "ratio_bound_concatenations_any_base": n_ratio,
           "of_which_within_factor_2_of_bound": n_tight, "mechanical_exclusion_cases": n_mech,
           "single_letter_bases": "a = 3..11, r <= 6", "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
