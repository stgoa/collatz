"""Self-contained checks of the stored annular currents and the five-source family.

Written at the B08 migration; the legacy scripts in this folder load modules by
their pre-migration paths and no longer run. Standard library, exact integers.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

Checks:
  1. A_N rebuilt from the six-band table (disjoint-annular-recursion) has
     267N/8 atoms and zero mass, for N = 96, 168, 384.
  2. annular_96_aggregate_one_sided.csv: A_96 = (I-P)J + Z with Z <= 0 (stored Z);
     annular_168_aggregate_exact.csv: A_168 = (I-P)J exactly.
  3. The finite work witnesses H_53(A_96) = 699 and H_9(A_384) = 42.
  4. The five-source affine identity mu_t = (I-P)J_t for t = 0..199 and three
     large t, and the 45 pairwise gcd tests that make the ten source
     progressions (t = 9s + r, r in {0, 3}) disjoint.
"""

import csv
import sys
from collections import defaultdict
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESIDUES = (1, 5, 7, 11, 13, 17)
ROWS = ((1, 0, 1, 0, -2, 0), (2, 1, -1, 1, -1, -2), (3, -1, -3, 2, 0, -1),
        (1, -3, -2, 3, 1, 0), (-1, -2, -1, 1, 2, 1), (0, -1, 0, -1, 0, 2))
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


def divergence(current):
    out = defaultdict(int)
    for x, c in current.items():
        out[x] += c
        y = step(x)
        if y != 1:
            out[y] -= c
    return out


def read_table(name):
    with (HERE / name).open(newline="") as f:
        reader = csv.reader(f)
        require(next(reader) == ["state", "weight"], f"{name}: header")
        return {int(x): int(c) for x, c in reader}


def clean(mu):
    return {x: c for x, c in mu.items() if c}


def work(mu, L):
    total = 0
    for x, c in mu.items():
        t, y = 0, x
        while y != 1 and t < L:
            y, t = step(y), t + 1
        total += c * t
    return total


def main():
    for N in (96, 168, 384):
        A = annulus(N)
        require(len(A) == 267 * N // 8 and sum(A.values()) == 0, f"A_{N}: size or mass")
    for N, cur, res, one_sided in ((96, "annular_96_aggregate_one_sided.csv",
                                    "annular_96_aggregate_one_sided_residual.csv", True),
                                   (168, "annular_168_aggregate_exact.csv",
                                    "annular_168_aggregate_exact_residual.csv", False)):
        J, Z = read_table(cur), read_table(res)
        total = divergence(J)
        for x, c in Z.items():
            total[x] += c
        require(clean(total) == annulus(N), f"A_{N}: stored identity fails")
        require(all(c < 0 for c in Z.values()) if one_sided else not Z, f"A_{N}: residual sign")
        print(f"A_{N}: {len(J)} current rows, residual {sorted(Z.items())}")
    w96, w384 = work(annulus(96), 53), work(annulus(384), 9)
    require((w96, w384) == (699, 42), f"work witnesses {w96}, {w384}")
    print(f"H_53(A_96) = {w96}, H_9(A_384) = {w384}")
    for t in list(range(200)) + [10**12 + 7, 3**80, 2**200 + 1]:
        mu = {x + v * t: c for x, v, c in SOURCES}
        J = {x + v * t: c for x, v, c in CURRENT}
        require(clean(divergence(J)) == mu, f"affine identity fails at t={t}")
    progressions = [(x + r * v, 9 * v) for x, v, _ in SOURCES for r in (0, 3)]
    pairs = 0
    for i in range(len(progressions)):
        for j in range(i + 1, len(progressions)):
            (a, p), (b, q) = progressions[i], progressions[j]
            require((a - b) % gcd(p, q) != 0, f"progressions {i}, {j} intersect")
            pairs += 1
    require(pairs == 45, "pair count")
    print(f"five-source identity at 203 parameters; {pairs} disjoint progression pairs")
    if failures:
        print("FAIL: " + "; ".join(failures))
        sys.exit(1)
    print("PASS: stored annular currents, work witnesses and five-source family")


if __name__ == "__main__":
    main()
