"""Self-contained recomputation of the universal partial annular current.

Written at the B08 migration; the legacy scripts in this folder load modules by
their pre-migration paths and no longer run. Standard library, exact integers.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

For every N divisible by 8 with 8 <= N <= 1024, and N = 6144, it rebuilds A_N
from the six-band table (disjoint-annular-recursion) and checks:
  - the five short-chain families E, D, B, C, A: each chain's states are actual
    Syracuse steps, carry exactly the stated annular coefficients, chains are
    pairwise disjoint, the current rows are <= 0 and have the chain as divergence,
    and the removed positive mass equals the floor-count formula D(N)
    (D(N) = 3N/2 when 72 | N);
  - all admissible copies (t = 9s + r, r in {0, 3}, s in I_r(N)) of the
    five-source family: coefficients match A_N, supports are disjoint from each
    other and from the catalogue; C(N) = |I_0| + |I_3| (C(160) = 0);
  - A_N = (I-P)J + Z for the summed current J, with Z equal to A_N on the
    untouched atoms, ||Z+||_1 = 99N/4 - D(N) - 3C(N) and ||J+||_1 <= 3C(N).
"""

import sys
from collections import defaultdict

RESIDUES = (1, 5, 7, 11, 13, 17)
ROWS = ((1, 0, 1, 0, -2, 0), (2, 1, -1, 1, -1, -2), (3, -1, -3, 2, 0, -1),
        (1, -3, -2, 3, 1, 0), (-1, -2, -1, 1, 2, 1), (0, -1, 0, -1, 0, 2))
# name, (a, b) interval in units of N, residues mod 72, chain coefficients at (x, x1[, x2]), current at (x[, x1])
FAMILIES = (("E", (12, 16), (7,), (-3, 3), (-3,)),
            ("D", (16, 18), (23, 71), (-1, 0, 1), (-1, -1)),
            ("B", (24, 32), (7,), (-2, 1, 1), (-2, -1)),
            ("C", (32, 36), (23,), (-3, 1, 2), (-3, -2)),
            ("A", (48, 64), (7, 55), (-1, -1, 2), (-1, -2)))
SOURCES = ((4591, 384, -1), (6121, 512, -1), (6887, 576, 1), (10331, 864, 2), (13775, 1152, -1))
CURRENT = ((4591, 384, -2), (6121, 512, -1), (6887, 576, -1), (10331, 864, 1), (11623, 972, 1),
           (13775, 1152, -1), (15497, 1296, 1), (20663, 1728, -1), (30995, 2592, -1), (46493, 3888, -1))
failures = []


def require(ok, message):
    if not ok:
        failures.append(message)


def step(x):
    z = 3 * x + 1
    return z // (z & -z)


def annulus(N):
    Q = 9 * N // 4
    out = {}
    for j, row in enumerate(ROWS):
        coefficients = dict(zip(RESIDUES, row))
        for y in range((Q << j) + 1, Q << (j + 1), 2):
            c = coefficients.get(y % 18, 0)
            if c:
                out[y] = c
    return out


def count(a, b, r, N):
    return (b * N - 1 - r) // 72 - (a * N - r) // 72


def D_formula(N):
    C = lambda a, b, r: count(a, b, r, N)
    return (3 * C(12, 16, 7) + C(16, 18, 23) + C(16, 18, 71) + 2 * C(24, 32, 7)
            + 3 * C(32, 36, 23) + 2 * C(48, 64, 7) + 2 * C(48, 64, 55))


def interval(r, N):
    if r == 0:
        lo, hi = -((120 - N) // 96), (N - 96) // 72   # ceil((N-120)/96), floor((N-96)/72)
    else:
        lo, hi = -((152 - N) // 96), (N - 120) // 72
    return range(max(lo, 0), hi + 1)


def check(N):
    A = annulus(N)
    used, current, removed_pos = set(), defaultdict(int), 0
    for name, (a, b), residues, coeffs, rows in FAMILIES:
        for x in range(a * N + 1, b * N, 2):
            if x % 72 not in residues:
                continue
            states = [x]
            while len(states) < len(coeffs):
                states.append(step(states[-1]))
            require(states[1] == (3 * x + 1) // 2, f"N={N} {name} x={x}: first valuation")
            for s, c in zip(states, coeffs):
                require(A.get(s, 0) == c, f"N={N} {name} x={x}: coefficient at {s}")
                if c:
                    require(s not in used, f"N={N} {name}: state {s} reused")
                    used.add(s)
                    removed_pos += max(c, 0)
            for s, c in zip(states, rows):
                require(c < 0, f"N={N} {name}: positive current row")
                current[s] += c
    require(removed_pos == D_formula(N), f"N={N}: D(N) formula")
    if N % 72 == 0:
        require(D_formula(N) == 3 * N // 2, f"N={N}: D(N) != 3N/2")
    copies = 0
    for r in (0, 3):
        for s in interval(r, N):
            t = 9 * s + r
            copies += 1
            for x, v, c in SOURCES:
                y = x + v * t
                require(A.get(y, 0) == c, f"N={N} copy t={t}: coefficient at {y}")
                require(y not in used, f"N={N} copy t={t}: state {y} reused")
                used.add(y)
            for x, v, c in CURRENT:
                current[x + v * t] += c
    if N == 160:
        require(copies == 0, "N=160 should have no five-source copy")
    residual = {y: c for y, c in A.items() if y not in used}
    total = defaultdict(int)
    for x, c in current.items():
        if c:
            total[x] += c
            y = step(x)
            if y != 1:
                total[y] -= c
    for y, c in residual.items():
        total[y] += c
    require({y: c for y, c in total.items() if c} == A, f"N={N}: A_N != (I-P)J + Z")
    require(sum(max(c, 0) for c in residual.values()) == 99 * N // 4 - D_formula(N) - 3 * copies,
            f"N={N}: residual positive mass")
    require(sum(max(c, 0) for c in current.values()) <= 3 * copies, f"N={N}: positive current cost")
    return copies


def main():
    cutoffs = list(range(8, 1025, 8)) + [6144]
    copies = {N: check(N) for N in cutoffs}
    print(f"{len(cutoffs)} cutoffs; C(N) at 96, 160, 168, 1024, 6144: "
          + ", ".join(str(copies[N]) for N in (96, 160, 168, 1024, 6144)))
    if failures:
        print("FAIL: " + "; ".join(failures[:10]))
        sys.exit(1)
    print("PASS: catalogue, five-source packing and combined partial current")


if __name__ == "__main__":
    main()
