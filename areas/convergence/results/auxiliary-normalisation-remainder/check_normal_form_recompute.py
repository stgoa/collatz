"""Self-contained recomputation of the auxiliary normalization's finite statements.

Written at the B09-residual-R11-R24 migration; the legacy checker in this folder
loads experiments/annular_construction/arithmetic/check_arithmetic_reductions.py
by its pre-migration path and no longer runs. Standard library, exact integers.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

Checks:
  - the short-ancestor lemma for every odd 1 < y <= 4097: an odd ancestor
    1 < x < y at Syracuse distance one or two exists iff y mod 18 is 5, 11, 13
    or 17; the selected rule q (and intermediate r) is an exact path with the
    stated valuations, and 3 <= q < 8y/9;
  - for every N divisible by 8 with 8 <= N <= 512, and N = 768: the first-pass
    residual B_N (each positive active atom of A_N moved once) has total mass
    21N/4 at multiples of 3, with every such coefficient nonnegative; every
    positive coefficient of B_N lies below 64N and every first-pass current row
    is negative and below 96N;
  - full normalization (descending order) at N = 8, 96, 168, 384: initial
    positive mass, terminal positive mass and terminal positive mass at
    multiples of 3 equal the table of the README; every terminal positive atom
    is 1, 3, 7, 9 or 15 mod 18; A_N = (I-P)J + Z with J <= 0.
A_N is rebuilt from the six-band table of disjoint-annular-recursion.
"""

import heapq
import sys
from collections import defaultdict

RESIDUES = (1, 5, 7, 11, 13, 17)
ROWS = ((1, 0, 1, 0, -2, 0), (2, 1, -1, 1, -1, -2), (3, -1, -3, 2, 0, -1),
        (1, -3, -2, 3, 1, 0), (-1, -2, -1, 1, 2, 1), (0, -1, 0, -1, 0, 2))
TABLE = {8: (198, 157, 65), 96: (2376, 1859, 805), 168: (4158, 3257, 1398), 384: (9504, 7453, 3198)}
failures = []


def require(ok, message):
    if not ok:
        failures.append(message)


def val2(n):
    return (n & -n).bit_length() - 1


def S(x):
    z = 3 * x + 1
    return z >> val2(z)


def annulus(N):
    Q = 9 * N // 4
    A = {}
    for j, row in enumerate(ROWS):
        lo, hi = (2 ** j) * Q, (2 ** (j + 1)) * Q
        for x in range(lo + 1 if lo % 2 == 0 else lo + 2, hi, 2):
            r = x % 18
            if r in RESIDUES:
                c = row[RESIDUES.index(r)]
                if c:
                    A[x] = c
    return A


def rule(y):
    """Selected smaller ancestor q and the current rows (intermediates) for an active y."""
    r = y % 18
    if r in (5, 11):
        return (2 * y - 1) // 3, [(2 * y - 1) // 3]
    if r == 13:
        q, mid = (8 * y - 5) // 9, (4 * y - 1) // 3
        return q, [q, mid]
    if r == 17:
        q, mid = (4 * y - 5) // 9, (2 * y - 1) // 3
        return q, [q, mid]
    return None, None


def check_lemma():
    has = set()
    for x in range(3, 4098, 2):
        a = S(x)
        if a > x:
            has.add(a)
        if a != 1:
            b = S(a)
            if b > x:
                has.add(b)
    for y in range(3, 4098, 2):
        active = y % 18 in (5, 11, 13, 17)
        require((y in has) == active, f"short-ancestor classification at y={y}")
        if active:
            q, rows = rule(y)
            path = [q] + ([rows[1]] if len(rows) == 2 else []) + [y]
            ok = all(S(path[i]) == path[i + 1] for i in range(len(path) - 1))
            require(ok and q % 2 == 1 and 3 <= q and 9 * q < 8 * y, f"rule path at y={y}")


def first_pass(A):
    B = defaultdict(int, A)
    J = defaultdict(int)
    for y, c in A.items():
        if c > 0 and y % 18 in (5, 11, 13, 17):
            q, rows = rule(y)
            B[y] -= c
            B[q] += c
            for x in rows:
                J[x] -= c
    return {x: c for x, c in B.items() if c}, {x: c for x, c in J.items() if c}


def normalize(A):
    Z = defaultdict(int, A)
    J = defaultdict(int)
    heap = [-y for y, c in A.items() if c > 0 and y % 18 in (5, 11, 13, 17)]
    heapq.heapify(heap)
    seen = set()
    while heap:
        y = -heapq.heappop(heap)
        if y in seen:
            continue
        seen.add(y)
        c = Z[y]
        if c <= 0 or y % 18 not in (5, 11, 13, 17):
            continue
        q, rows = rule(y)
        Z[y] = 0
        Z[q] += c
        for x in rows:
            J[x] -= c
        if Z[q] > 0 and q % 18 in (5, 11, 13, 17):
            heapq.heappush(heap, -q)
    return {x: c for x, c in Z.items() if c}, {x: c for x, c in J.items() if c}


def divergence(J):
    d = defaultdict(int)
    for x, c in J.items():
        d[x] += c
        y = S(x)
        if y != 1:
            d[y] -= c
    return d


def main():
    check_lemma()
    for N in list(range(8, 513, 8)) + [768]:
        A = annulus(N)
        B, J1 = first_pass(A)
        triple = sum(c for x, c in B.items() if x % 3 == 0)
        require(4 * triple == 21 * N, f"N={N}: mass at multiples of 3 is {triple}, not 21N/4")
        require(all(c >= 0 for x, c in B.items() if x % 3 == 0), f"N={N}: negative coefficient at a multiple of 3")
        require(all(x < 64 * N for x, c in B.items() if c > 0), f"N={N}: positive first-pass coefficient above 64N")
        require(all(c < 0 and x < 96 * N for x, c in J1.items()), f"N={N}: first-pass current row sign or height")
    for N, (init, term, term3) in TABLE.items():
        A = annulus(N)
        Z, J = normalize(A)
        got = (sum(c for c in A.values() if c > 0), sum(c for c in Z.values() if c > 0),
               sum(c for x, c in Z.items() if c > 0 and x % 3 == 0))
        require(got == (init, term, term3), f"N={N}: masses {got}, expected {(init, term, term3)}")
        require(all(x % 18 in (1, 3, 7, 9, 15) for x, c in Z.items() if c > 0), f"N={N}: terminal residue")
        require(all(c < 0 for c in J.values()), f"N={N}: current not negative")
        d = divergence(J)
        for x, c in Z.items():
            d[x] += c
        require({x: c for x, c in d.items() if c} == A, f"N={N}: A_N != (I-P)J + Z")
    if failures:
        print("FAIL: " + "; ".join(failures[:10]))
        sys.exit(1)
    print("PASS: short-ancestor lemma through 4097; 21N/4 at multiples of 3 for 65 cutoffs; "
          "normal-form masses at N = 8, 96, 168, 384")


if __name__ == "__main__":
    main()
