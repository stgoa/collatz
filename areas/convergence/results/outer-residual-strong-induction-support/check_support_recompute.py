"""Self-contained check of the support identity for the outer residual profile R_N.

Written at the B09-residual-R11-R24 migration; the side-lane probe
residual_vs_induction.py in this folder imports affine_controls from its
pre-migration path and no longer runs. Standard library, exact integers.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

For every N divisible by 8 with 8 <= N <= 4096, and for the six cutoffs of the
legacy receipt (96, 768, 6144, 9216, 49152, 98304), it checks that the support
of R_N (retained-graph-complement-constructor, Section 4) equals
    { odd x : N < x < 3N/2, x = 3 mod 4, x not in S([1,N]) or S^2([1,N]) }
(S the odd-only map, [1,N] the odd seeds), that no support element is 2 mod 3,
and that |supp R_N| - 23N/288 stays within [-3, 3] (the O(1) of the review).
At the six receipt cutoffs it compares support size, mass and the number of
roots divisible by 3 with residual_vs_induction.json.
"""

import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
failures = []


def require(ok, message):
    if not ok:
        failures.append(message)


def S(x):
    z = 3 * x + 1
    return z >> ((z & -z).bit_length() - 1)


def profile(N):
    R = {}
    for x in range(N + 1, 3 * N // 2, 2):
        if x % 12 == 3 or (x % 12 == 7 and 8 * x > 9 * N):
            R[x] = 1
        elif x % 36 in (7, 19) and 8 * x < 9 * N:
            R[x] = 2
    return R


def induction_residual(N):
    one = {S(s) for s in range(1, N + 1, 2)}
    two = one | {S(y) for y in one}
    return {x for x in range(N + 1, 3 * N // 2, 2) if x % 4 == 3 and x not in two}


def main():
    rows = {r["N"]: r for r in json.loads((HERE / "residual_vs_induction.json").read_text())["rows"]}
    worst = Fraction(0)
    for N in list(range(8, 4097, 8)) + sorted(rows):
        R, residual = profile(N), induction_residual(N)
        require(set(R) == residual, f"N={N}: support identity")
        require(all(x % 3 != 2 for x in residual), f"N={N}: a support element is 2 mod 3")
        dev = len(residual) - Fraction(23 * N, 288)
        worst = max(worst, abs(dev))
        require(abs(dev) <= 3, f"N={N}: support size deviation {dev}")
        if N in rows:
            got = dict(N=N, support=len(residual), R_mass=sum(R.values()),
                       multiples_of_3=sum(1 for x in residual if x % 3 == 0))
            require(got == rows[N], f"N={N}: {got} differs from the receipt")
    if failures:
        print("FAIL: " + "; ".join(failures[:10]))
        sys.exit(1)
    print(f"PASS: supp R_N = shell climbers outside S([1,N]) and S^2([1,N]) for 512 + 6 cutoffs; "
          f"max |supp - 23N/288| = {worst}; six receipt rows reproduced")


if __name__ == "__main__":
    main()
