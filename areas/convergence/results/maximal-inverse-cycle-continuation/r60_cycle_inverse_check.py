"""Sidekick probe: independent check of R60's maximal cycle inverse and its acceptance table
(main cycle_inverse/CYCLE_INVERSE.md), with this branch's own step/nu.

Domain: w = 3445 mod 3456, v = (16w-13)/27 = 0 mod 3 (so v = -7 mod 2048), q = (81v+23)/32, b = 8v+1.
h = v3(b+17), k = floor(h/7), a = 2048/2187, p = a^k (b+17) - 17, j = v3(p+1), eta = 2^j (p+1)/3^j - 1.
For k >= 1: the ordinary word from eta to q is 1^j,(1,1,1,2,1,1,4)^k,2,1,1,4; eta = lambda q + beta with
lambda = (256/81) a^k t, beta = t((1274/81) a^k - 16) - 1, t = (2/3)^j; and eta < q iff
(k <= 5 and j >= 3) or (6 <= k <= 11 and j >= 2) or (12 <= k <= 17 and j >= 1) or k >= 18.
Inputs are built by CRT with prescribed k = 1..20 and j = 0..4 (h = 7k exactly). Standard library.
"""
from fractions import Fraction
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "experiments" / "packet_currents" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402
from fibre_count_check import nu  # noqa: E402


def v3(n):
    h = 0
    while n % 3 == 0:
        n //= 3
        h += 1
    return h


def accepted(k, j):
    return (k <= 5 and j >= 3) or (6 <= k <= 11 and j >= 2) or (12 <= k <= 17 and j >= 1) or k >= 18


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(60)
    tally = {}
    for k in range(1, 21):
        for jt in range(0, 5):
            made = 0
            while made < 4:
                # m: b + 17 = 3^(7k) m with m != 0 mod 3, v3(2048^k m - 16) = jt, and b = -55 mod 2^14
                mod3 = 3**(jt + 1)
                r3 = (16*pow(2048**k, -1, 3**jt)) % 3**jt if jt else 0
                cand = None
                for _ in range(200):
                    m3 = r3 + 3**jt*rng.randrange(0, 3) if jt else rng.randrange(1, 3)
                    if m3 % 3 == 0 or ((2048**k*m3 - 16) % 3**(jt + 1) == 0 and jt >= 0 and v3(2048**k*m3 - 16) != jt):
                        continue
                    if v3((2048**k*m3 - 16) % mod3 + mod3*3) < jt:
                        continue
                    m2 = (-38*pow(3**(7*k), -1, 16384)) % 16384
                    M = 16384*mod3
                    m = (m3*16384*pow(16384, -1, mod3) + m2*mod3*pow(mod3, -1, 16384)) % M
                    m += M*rng.randrange(1, 2**20)
                    if m % 3 and v3(2048**k*m - 16) == jt:
                        cand = m
                        break
                if cand is None:
                    continue
                m = cand
                b = 3**(7*k)*m - 17
                assert b % 16384 == (-55) % 16384 and (b - 1) % 8 == 0
                v = (b - 1)//8
                w = (27*v + 13)//16
                assert (27*v + 13) % 16 == 0 and w % 3456 == 3445 and v % 3 == 0 and v % 2048 == 2048 - 7
                q = (81*v + 23)//32
                assert (3*w - 1)//2 == q and v3(b + 17) == 7*k
                p = (2048**k*(b + 17))//3**(7*k) - 17
                j = v3(p + 1)
                assert j == jt
                eta = (2**j*(p + 1))//3**j - 1
                x = eta
                for a in [1]*j + [1, 1, 1, 2, 1, 1, 4]*k + [2, 1, 1, 4]:
                    assert valuation(1, x) == a
                    x = step(1, x)
                assert x == q
                t = Fraction(2, 3)**j
                ak = Fraction(2048, 2187)**k
                assert eta == Fraction(256, 81)*ak*t*q + t*(Fraction(1274, 81)*ak - 16) - 1
                assert (eta < q) == accepted(k, j), (k, j, eta < q)
                tally[(k, j)] = eta < q
                made += 1
    report = dict(scope="Independent check of R60's maximal cycle inverse words, height formula and acceptance table.",
                  cells=len(tally), cases=4*len(tally),
                  accepted_cells=sorted("k%d j%d" % kj for kj, acc in tally.items() if acc)[:12],
                  status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(dict(cells=len(tally), status="PASS")))


if __name__ == "__main__":
    main()
