"""Sidekick probe: main's framework transfers verbatim from 3x+1 to 3x+d, gcd(d, 6) = 1.

For odd d, T_d(x) = (3x + d)/2^v2(3x + d) satisfies T_d(d*y) = d*T_1(y) on 2-adic integers,
so on Z_2 (and on positive rationals with denominators prime to 6) 3x+d is 3x+1 rescaled
by d. Every valuation identity, normal-form step and cycle word therefore carries over with
x replaced by x/d. This probe checks three of main's identities in that form:
  * halving (R23): x = 2^a t - d with t/d = 3^a mod 4 gives S_d^a(x) = S_d^a((x - d)/2);
  * R54's family: n0 = 81*2^(11r+6)*s - 17d follows (1,1,1,2,1,1,4) r times, with
    Psi_d(n) + 17d = (2187/2048)(n + 17d), all states above n0;
  * the 18u + 5 form: for d = 1 and every odd u < 10^5, the orbits of u and 18u+5 meet.
for d in {1, 5, 7, 13, 61} (and the restatement only for d = 1). Standard library.
"""
from pathlib import Path
import json
import sys


def S(d, x):
    z = 3*x + d
    return z//(z & -z)


def v2(n):
    return (n & -n).bit_length() - 1


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    counts = {}
    for d in (1, 5, 7, 13, 61):
        halving = fam = 0
        for a in range(2, 12):
            for t in range(1, 400, 2):
                if (t*pow(d, -1, 4)) % 4 != pow(3, a, 4):
                    continue
                x = 2**a*t - d
                if x <= d or x % 2 == 0:
                    continue
                y = (x - d)//2
                p, r_ = x, y
                for _ in range(a):
                    p, r_ = S(d, p), S(d, r_)
                assert p == r_, (d, a, t)
                halving += 1
        for r in range(1, 5):
            for s in (1, 2, 3, 7):
                n0 = 81*2**(11*r + 6)*s - 17*d
                n = n0
                for _ in range(r):
                    m = n
                    for v in (1, 1, 1, 2, 1, 1, 4):
                        assert v2(3*m + d) == v and m >= n0
                        m = S(d, m)
                    assert 2048*(m + 17*d) == 2187*(n + 17*d)
                    n = m
                fam += 1
        counts[d] = dict(halving_cases=halving, r54_family_cases=fam)
    met = 0
    for u in range(1, 10**5, 2):
        a, b, seen = u, 18*u + 5, set()
        while a != 1:
            seen.add(a)
            a = S(1, a)
        seen.add(1)
        while b not in seen:
            b = S(1, b)
        met += 1
    report = dict(scope="3x+d transfer of main's identities; 18u+5 restatement checked for odd u < 1e5 (d = 1).",
                  by_d=counts, pairs_meeting=met, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
