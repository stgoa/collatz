"""Sidekick probe: independent check of main's in-progress R71 (mechanical valuation words).

R71 (main working copy, lattice_cycles/BALANCED_DENOMINATORS.md): for integers A >= k >= 1 with
2^A > 3^k and 0 <= l < k, the mechanical word a_i(l) = floor(((i+1)A+l)/k) - floor((iA+l)/k)
has a positive rational Syracuse cycle in which every state has reduced denominator
2^(A/g) - 3^(k/g), g = gcd(A, k); the only integral case is the all-2s word (cycle {1}).

Checked here with exact Fractions and this branch's own iteration (no main code): every k <= 14,
every A with 3^k < 2^A <= 2^(ceil(k log2 3) + 6), every l; the identity 3 B_i + D = 2^(a_i) B_(i+1)
for all rotations; the exact valuations; and the claimed denominators. Standard library.
"""
from fractions import Fraction
from math import ceil, gcd, log2
from pathlib import Path
import json
import sys


def word(A, k, l):
    return [((i + 1)*A + l)//k - (i*A + l)//k for i in range(k)]


def intercept(w):
    k, e, B = len(w), 0, 0
    for j, a in enumerate(w):
        B += 3**(k - 1 - j)*2**e
        e += a
    return B


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    cases = integral = 0
    for k in range(1, 15):
        for A in range(ceil(k*log2(3) + 1e-12), ceil(k*log2(3)) + 7):
            if 2**A <= 3**k:
                continue
            D = 2**A - 3**k
            g = gcd(A, k)
            d_claim = 2**(A//g) - 3**(k//g)
            for l in range(k):
                w = word(A, k, l)
                assert all(a >= 1 for a in w) and sum(w) == A
                Bs = [intercept(w[i:] + w[:i]) for i in range(k)]
                for i in range(k):
                    assert 3*Bs[i] + D == 2**w[i]*Bs[(i + 1) % k] and Bs[i] % 2 == 1
                x = Fraction(Bs[0], D)
                y = x
                for a in w:
                    z = 3*y + 1
                    v = 0
                    while z.numerator % 2 == 0:
                        z /= 2
                        v += 1
                    assert v == a and y.denominator == d_claim, (A, k, l, y)
                    y = z
                assert y == x
                cases += 1
                if d_claim == 1:
                    assert set(w) == {2}
                    integral += 1
    report = dict(scope="Independent exact check of R71's mechanical-word denominators (main working copy).",
                  cases=cases, integral_cases_all_twos=integral, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
