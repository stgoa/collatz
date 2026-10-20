"""Self-contained recomputation of the finite arithmetic of the five-ray induction.

Written at the B09-residual-R11-R24 migration; the side-lane probe r24_check.py
in this folder imports affine_controls from its pre-migration path and no longer
runs. Standard library, exact integers.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

Checks:
  - the cutoffs a*2^b, a in {12, 14, 16, 18, 21}, 9 <= b <= 79, in increasing
    order (355 cutoffs): consecutive ratios cycle through 7/6, 8/7, 9/8, 7/6, 8/7,
    all at most 7/6 < 3/2, and every cutoff is divisible by 512 (the ratios
    repeat with period 5 for every b, which is the general statement);
  - the base: every odd seed <= 6144 reaches 1 under the odd-only map
    (cycle detection and a 10000-step cap; a failure exits 1).
"""

import sys
from fractions import Fraction

failures = []


def require(ok, message):
    if not ok:
        failures.append(message)


def S(x):
    z = 3 * x + 1
    return z >> ((z & -z).bit_length() - 1)


def main():
    cutoffs = sorted(a * 2 ** b for b in range(9, 80) for a in (12, 14, 16, 18, 21))
    require(len(cutoffs) == 355, "355 cutoffs")
    pattern = (Fraction(7, 6), Fraction(8, 7), Fraction(9, 8), Fraction(7, 6), Fraction(8, 7))
    for i in range(len(cutoffs) - 1):
        ratio = Fraction(cutoffs[i + 1], cutoffs[i])
        require(ratio == pattern[i % 5] and ratio < Fraction(3, 2), f"ratio at {cutoffs[i]}")
    require(all(N % 512 == 0 for N in cutoffs), "divisibility by 512")
    longest = 0
    for s in range(1, 6145, 2):
        x, steps, seen = s, 0, set()
        while x != 1:
            if x in seen or steps > 10000:
                failures.append(f"seed {s} did not reach 1")
                break
            seen.add(x)
            x, steps = S(x), steps + 1
        longest = max(longest, steps)
    if failures:
        print("FAIL: " + "; ".join(failures[:10]))
        sys.exit(1)
    print(f"PASS: 355 ordered cutoffs with ratios 7/6, 8/7, 9/8 and 512 | N; all 3072 odd seeds <= 6144 "
          f"reach 1 (longest {longest} odd steps)")


if __name__ == "__main__":
    main()
