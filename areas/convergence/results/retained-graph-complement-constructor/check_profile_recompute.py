"""Self-contained recomputation of the retained-graph classification and the profile R_N.

Written at the B09-residual-R11-R24 migration; the legacy scripts in this folder
load ../closure/local_extension.py (and through it ../forcing/) by their
pre-migration paths and no longer run. Standard library, exact integers.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

Checks, for every N divisible by 8 with 8 <= N <= 1024 (unless stated):
  - the components of the K_N-only graph (one arrow x -> S(x) from every odd
    1 < x < 3N/2) containing no state <= N are exactly the table of Section 3:
    {x, t} for x = 3 mod 12 in (N, 3N/2) and for x = 7 mod 12 in (9N/8, 3N/2),
    {p, x, t} for x = 7 or 19 mod 36 in (N, 9N/8), with t = (3x+1)/2, p = (4x-1)/3;
  - |R_N| from the profile of Section 4 equals the floor formula (3);
  - |R_N| for N = 8, ..., 288 is the stated list of 36 values, and
    |R_(N+288)| = |R_N| + 25 for N <= 2880;
  - 25N/288 - 19/9 <= |R_N| <= 25N/288 + 5/4 for N <= 2880;
  - on the ladder N = 96*64^k, k = 0..6, |R_N| = 25N/288 - 4/3 (formula only).
"""

import sys
from fractions import Fraction
from math import ceil, floor

LIST36 = (0, 1, 2, 2, 4, 4, 4, 4, 7, 6, 8, 7, 9, 10, 11, 9, 11, 13,
          13, 13, 14, 15, 17, 16, 16, 17, 20, 18, 20, 20, 22, 22, 23, 22, 24, 25)
failures = []


def require(ok, message):
    if not ok:
        failures.append(message)


def S(x):
    z = 3 * x + 1
    return z >> ((z & -z).bit_length() - 1)


def C(L, H, r, m):
    """Number of integers strictly between rationals L < H congruent to r mod m."""
    L, H = Fraction(L), Fraction(H)
    return ceil((H - r) / m) - floor((L - r) / m) - 1


def profile(N):
    B = 3 * N // 2
    R = {}
    for x in range(N + 1, B, 2):
        if x % 12 == 3:
            R[x] = 1
        elif x % 12 == 7:
            if 8 * x > 9 * N:
                R[x] = 1
            elif x % 36 in (7, 19):
                R[x] = 2
    return R


def mass_formula(N):
    return (C(N, Fraction(3 * N, 2), 3, 12) + C(N, Fraction(3 * N, 2), 7, 12)
            - C(N, Fraction(9 * N, 8), 31, 36)
            + C(Fraction(4 * N, 3), Fraction(3 * N, 2), 9, 48) + C(Fraction(4 * N, 3), Fraction(3 * N, 2), 25, 48))


def missing_components(N):
    B = 3 * N // 2
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for x in range(3, B, 2):
        a, b = find(x), find(S(x))
        if a != b:
            parent[a] = b
    groups = {}
    for x in list(parent):
        groups.setdefault(find(x), set()).add(x)
    return {frozenset(g) for g in groups.values() if min(g) > N}


def expected_components(N):
    B = 3 * N // 2
    out = set()
    for x in range(N + 1, B, 2):
        t = (3 * x + 1) // 2
        if x % 12 == 3 or (x % 12 == 7 and 8 * x > 9 * N):
            out.add(frozenset((x, t)))
        elif x % 36 in (7, 19) and 8 * x < 9 * N:
            out.add(frozenset(((4 * x - 1) // 3, x, t)))
    return out


def main():
    for N in range(8, 1025, 8):
        require(missing_components(N) == expected_components(N), f"N={N}: component classification")
    masses = {}
    for N in range(8, 2881 + 288, 8):
        m = sum(profile(N).values())
        masses[N] = m
        require(m == mass_formula(N), f"N={N}: profile mass {m} != formula {mass_formula(N)}")
    require(tuple(masses[N] for N in range(8, 289, 8)) == LIST36, "the 36 phase values")
    for N in range(8, 2881, 8):
        require(masses[N + 288] == masses[N] + 25, f"N={N}: period 288 increment")
        require(Fraction(25 * N, 288) - Fraction(19, 9) <= masses[N] <= Fraction(25 * N, 288) + Fraction(5, 4),
                f"N={N}: bound")
    for k in range(7):
        N = 96 * 64 ** k
        require(mass_formula(N) == Fraction(25 * N, 288) - Fraction(4, 3), f"ladder k={k}")
    if failures:
        print("FAIL: " + "; ".join(failures[:10]))
        sys.exit(1)
    print("PASS: K_N-only components missing [1, N] classified for 128 cutoffs; |R_N| formula, "
          "36 phases, period 288 and bounds through N = 3168; ladder mass 25N/288 - 4/3 for k <= 6")


if __name__ == "__main__":
    main()
