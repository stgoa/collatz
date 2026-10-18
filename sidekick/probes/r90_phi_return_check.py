"""Sidekick probe: independent check of R90's Phi return words and counts (main a94533a), with this
branch's own step/nu (no main code).

Phi(v) = (3^12 v + 299947)/2^19, L(v) = 7153 v + 299947 (7153 = 3^12 - 2^19).
(1) For v = 133797 mod 2^19, the ordinary words (1,1,1,1,3,1,4,1,2,1,1,2) from 6v+1 and
    (1,1,1,2,1,1,4,1,2,1,1,2) from 3v both end at 6 Phi(v) + 1 = (1594323 v + 1161985)/262144.
(2) On the re-entry cylinder v = 102642092709 mod 2^37 (= -B/D mod 2^37), T^12(3v) = 3 Phi(v),
    and L(Phi v) = (3^12/2^19) L(v).
(3) For v in the guard (2^18 | L(v)), the number of complete re-entries equals
    floor((v2(L(v)) - 18)/19), checked by direct iteration of Phi with integrality and guard tests.
Standard library. Run without -O.
"""
from fractions import Fraction
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402
from fibre_count_check import nu  # noqa: E402

A, M, B, D = 3**12, 2**19, 299947, 7153


def v2(n):
    return (n & -n).bit_length() - 1


def walk(x, word):
    for a in word:
        assert valuation(1, x) == a
        x = step(1, x)
    return x


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    assert A - M == D and (-B*pow(D, -1, 2**37)) % 2**37 == 102642092709
    rng = random.Random(90)
    for _ in range(2000):
        v = 133797 + 2**19*rng.randrange(0, 2**40)
        end = (1594323*v + 1161985)
        assert end % 262144 == 0
        end //= 262144
        assert walk(6*v + 1, (1, 1, 1, 1, 3, 1, 4, 1, 2, 1, 1, 2)) == end
        assert walk(3*v, (1, 1, 1, 2, 1, 1, 4, 1, 2, 1, 1, 2)) == end
        assert Fraction(end) == 6*Fraction(A*v + B, M) + 1
    T = lambda x: nu(step(1, x))
    for _ in range(500):
        v = 102642092709 + 2**37*rng.randrange(0, 2**30)
        assert (A*v + B) % M == 0
        phi = (A*v + B)//M
        x = 3*v
        for _ in range(12):
            x = T(x)
        assert x == 3*phi and M*(D*phi + B) == A*(D*v + B)
    counts = 0
    for _ in range(3000):
        k = rng.randrange(0, 5)
        mod = 2**(18 + 19*k)
        base = (-B*pow(D, -1, mod)) % mod
        v = base + mod*rng.randrange(1, 2**12)
        assert (D*v + B) % 2**18 == 0
        n_re, x = 0, v
        while (A*x + B) % M == 0:
            y = (A*x + B)//M
            if (D*y + B) % 2**18:
                break
            n_re, x = n_re + 1, y
        assert n_re == (v2(D*v + B) - 18)//19, (v, n_re)
        counts += 1
    report = dict(scope="Independent check of R90's return words, quotient identity and re-entry counts.",
                  word_cases=2000, quotient_cases=500, count_cases=counts, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
