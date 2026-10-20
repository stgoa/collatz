"""Sidekick probe: independent checks of R73's two pair identities and R74's word arithmetic
(main aefdf60), with this branch's own odd-only step (no main code).

R73: w = 93 mod 512, u = (9w-5)/64: P(w) - P(u) has an exact current with ordinary clocks (3,1)
     on both endpoint comparisons, i.e. S^3(3w) = S(3u) and S^3(w) = S(u) (both W5, rho decreases);
     b = 1285 mod 2048, a = 9(b-5)/256: lower clocks (3,1) and upper clocks (4,2),
     i.e. S^3(b) = S(a) and S^4(3b) = S^2(3a). Checked on 4000 members each.
R74: V(w) = (3^12 w + 311195)/2^19 and R(w) = (3^24 w + 328537586155)/2^37 on the guard
     G = {w = 40529845 mod 2^26}. For random words over {V, R} (length <= 12), the composed map
     F(w) = (3^l w + c)/2^e has e = 19#V + 37#R, l = 12#V + 24#R; on the stated domain
     (2^e 40529845 - c)(3^l)^-1 mod 2^(26+e) every intermediate image is an integer in G, the
     first-symbol domains are 2218391138229 mod 2^45 (V) and 8515171531530858421 mod 2^63 (R),
     and the images grow. Every eventually periodic word's fixed point is negative.
Standard library. Run without -O.
"""
from fractions import Fraction
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "experiments" / "packet_currents" / "negative_controls")]
from affine_controls import step  # noqa: E402


def Sn(x, n):
    for _ in range(n):
        x = step(1, x)
    return x


VC, RC = (3**12, 311195, 19), (3**24, 328537586155, 37)


def apply(sym, w):
    a, c, e = VC if sym == "V" else RC
    num = a*w + c
    assert num % 2**e == 0
    return num >> e


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(73)
    for _ in range(4000):
        w = 93 + 512*rng.randrange(0, 2**40)
        u = (9*w - 5)//64
        assert w % 8 == 5 and u % 8 == 5 and 0 < u < w
        assert Sn(3*w, 3) == Sn(3*u, 1) and Sn(w, 3) == Sn(u, 1)
        b = 1285 + 2048*rng.randrange(0, 2**40)
        a = 9*(b - 5)//256
        assert b % 8 == 5 and a % 8 == 5 and 0 < a < b
        assert Sn(b, 3) == Sn(a, 1) and Sn(3*b, 4) == Sn(3*a, 2)
    words = 0
    for _ in range(600):
        word = [rng.choice("VR") for _ in range(rng.randrange(1, 13))]
        nV, nR = word.count("V"), word.count("R")
        e, l = 19*nV + 37*nR, 12*nV + 24*nR
        A, C, E = 1, 0, 0                     # F(w) = (A w + C)/2^E, composed in order
        for sym in word:
            a, c, ee = VC if sym == "V" else RC
            A, C, E = a*A, a*C + c*2**E, E + ee
        assert (A, E) == (3**l, e)
        mod = 2**(26 + e)
        dom = ((2**e*40529845 - C)*pow(3**l, -1, mod)) % mod
        for t in range(3):
            w = dom + mod*rng.randrange(0, 2**8)
            x = w
            for sym in word:
                assert x % 2**26 == 40529845
                if sym == "V":
                    assert x % 2**45 == 2218391138229
                else:
                    assert x % 2**63 == 8515171531530858421
                y = apply(sym, x)
                assert y > x
                x = y
            assert x % 2**26 == 40529845 and x == (A*w + C) >> E
        words += 1
        # eventually periodic word: fixed point of the periodic part is negative
        a2, c2, e2 = 1, 0, 0
        for sym in word:
            a, c, ee = VC if sym == "V" else RC
            a2, c2, e2 = a*a2, a*c2 + c*2**e2, e2 + ee
        fixed = Fraction(-c2, a2 - 2**e2)
        assert a2 > 2**e2 and fixed < 0
    report = dict(scope="Independent checks of R73 identities (clocks) and R74 word arithmetic (main aefdf60).",
                  r73_members_each=4000, r74_words=words, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
