"""Sidekick probe: independent arithmetic checks of R61, R65, R66 and R67 (main, through 7d86314),
with this branch's own step/nu/selected (no main code).

R61: q = 81*2^(11r+11) s - 17 (r >= 0, s >= 1, s odd*) has r guarded -17 cycles and exits at
     e = 11: Y = S^4(Q), V = nu(Y) = 2592 U - 21 (U = 81*3^(7r) s), a(V) = 2 with block depth 3,
     endpoint f = 3^(7r+10) s - 6; and f > q iff r >= 16.     (*s with v2 conditions as generated)
R65: the R58 exceptional canonical seeds n, the returning inputs u, and the canonical q = 31 mod 108
     are in bijection via q = (9n+5)/8, u = (2q+1)/3, z = (3n-1)/16 = (q-1)/6 = (u-1)/4, with
     n = 27 mod 96, z = 5 mod 18, 3z noncanonical, and n -(1)-> 8z+1 -(2)-> 6z+1 = q.
R66: b_L = 64^L (8v+1) + 49(64^L - 1)/63 satisfies v3(b_L - b_M) = v3(L - M).
R67: on G = {w = 40529845 mod 2^26}, V(w) = (531441 w + 311195)/524288 > w, and the maximal number
     of consecutive V-steps staying in G is 1 + floor((v2(7153 w + 311195) - 26)/19).
Standard library. Run without -O.
"""
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402
from fibre_count_check import nu, selected  # noqa: E402


def v2(n):
    return (n & -n).bit_length() - 1


def v3(n):
    h = 0
    while n % 3 == 0:
        n //= 3
        h += 1
    return h


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(61)
    r61 = 0
    for r in range(0, 22):
        made = 0
        while made < 6:
            s = rng.randrange(1, 2**16)
            q = 81*2**(11*r + 11)*s - 17
            if v2(q + 17) != 11*r + 11:
                continue
            x = q
            for _ in range(r):
                for a in (1, 1, 1, 2, 1, 1, 4):
                    assert valuation(1, x) == a
                    x = step(1, x)
            Q = x
            U = 81*3**(7*r)*s
            assert Q == 2**11*U - 17
            Y = Q
            for _ in range(4):
                Y = step(1, Y)
            V = nu(Y)
            assert V == 2592*U - 21 and v2(V + 1) == 2
            t = (V + 1) >> 2
            assert v2(3*t - 1) == 3
            f = 3*((3*t - 1) >> 3)            # odd d = 3: f = 3^floor(d/2) * u
            assert f == 3**(7*r + 10)*s - 6
            assert (f > q) == (r >= 16), (r, s)
            made += 1
            r61 += 1
    r65 = 0
    for q in range(31, 31 + 108*20000, 108):
        if nu(q) != q:
            continue
        n, u, z = (8*q - 5)//9, (2*q + 1)//3, (q - 1)//6
        assert (8*q - 5) % 9 == 0 and n % 96 == 27 and z % 18 == 5
        assert (9*n + 5)//8 == q and u == (3*n + 3)//4 and z == (3*n - 1)//16 == (u - 1)//4
        assert n % 48 == 27 and v2(3*n - 1) == 4 and nu(3*z) != 3*z and nu(n) == n
        assert u % 8 == 5 and u % 9 == 3 and selected(3*u)
        assert valuation(1, n) == 1 and step(1, n) == 8*z + 1 and valuation(1, 8*z + 1) == 2 and step(1, 8*z + 1) == 6*z + 1 == q
        r65 += 1
    r66 = 0
    for _ in range(3000):
        v = rng.randrange(1, 2**30)
        L, M = rng.randrange(0, 200), rng.randrange(0, 200)
        if L == M:
            continue
        bL = 64**L*(8*v + 1) + 49*(64**L - 1)//63
        bM = 64**M*(8*v + 1) + 49*(64**M - 1)//63
        assert v3(bL - bM) == v3(L - M)
        r66 += 1
    r67 = 0
    for _ in range(3000):
        m = rng.randrange(1, 6)
        mod = 2**(26 + 19*(m - 1))
        base = (-311195*pow(7153, -1, mod)) % mod
        w = base + mod*rng.randrange(1, 2**10) if rng.random() < 0.7 else 40529845 + 2**26*rng.randrange(0, 2**40)
        if w % 2**26 != 40529845:
            continue
        cnt, x = 0, w
        while x % 2**26 == 40529845 and (531441*x + 311195) % 524288 == 0:
            y = (531441*x + 311195)//524288
            assert y > x
            cnt += 1
            x = y
            if x % 2**26 != 40529845:
                break
        predicted = 1 + (v2(7153*w + 311195) - 26)//19
        # count of V-steps whose image is again in G, plus the first step from G
        steps_in_G, x = 0, w
        while True:
            y = (531441*x + 311195)//524288 if (531441*x + 311195) % 524288 == 0 else None
            if y is None:
                break
            steps_in_G += 1
            if y % 2**26 != 40529845:
                break
            x = y
        assert steps_in_G == predicted, (w, steps_in_G, predicted)
        r67 += 1
    report = dict(scope="Independent arithmetic checks of R61, R65, R66, R67.",
                  r61_cases=r61, r65_q_values=r65, r66_pairs=r66, r67_cases=r67, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
