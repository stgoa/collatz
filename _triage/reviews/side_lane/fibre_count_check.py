"""Sidekick probe: independent check of main's R27 fibre count (commit 541101a,
absorbed_fibers/ABSORBED_FIBERS.md).

Normal form by descent, implemented here from the two bridge moves:
  - F^{-1}: x -> (x-1)/4 when x = 5 (mod 8), since S(4u+1) = S(u);
  - halving: x -> (x-1)/2 when x is a selected climber, since S^a(x) = S^a((x-1)/2).
nu(x) is the endpoint of the descent; I_N = {x odd : nu(x) <= N}.
Main's claim: for X >= N >= 8, #(I_N in [X, 2X)) = N/4 + O(log N), with error at
most 2 floor(log2 N) + 3, independent of X.

Checked here:
  (a) for X up to 2^14 * N, brute-force descent on every odd x in [X, 2X);
  (b) for huge X, the count over components {F^k(q), F^k(2q+1)} with q in B, q <= N;
  (c) agreement of (a) and (b) where both run.
Standard library. Run without -O.
"""
from pathlib import Path
import json
import math
import random
import sys


def selected(x):
    if x % 4 != 3:
        return False
    a = ((x + 1) & -(x + 1)).bit_length() - 1
    return ((x + 1) >> a) % 4 == pow(3, a, 4)


def nu(x):
    while True:
        if x % 8 == 5:
            x = (x - 1)//4
        elif x > 1 and selected(x):
            x = (x - 1)//2
        else:
            return x


def in_B(q):
    return q % 2 == 1 and nu(q) == q


def count_brute(N, X):
    return sum(1 for x in range(X + (X % 2 == 0), 2*X, 2) if nu(x) <= N)


def count_components(N, X):
    total = 0
    for q in range(1, N + 1, 2):
        if not in_B(q):
            continue
        for y in (q, 2*q + 1):
            z = y
            while z < X:
                z = 4*z + 1
            total += z < 2*X
    return total


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(1017)
    worst = 0.0
    rows = []
    for N in (8, 13, 64, 100, 257, 1000):
        bound = 2*math.floor(math.log2(N)) + 3
        for e in range(0, 15, 2):
            X = N*2**e + rng.randrange(0, N)
            b, c = count_brute(N, X), count_components(N, X)
            assert b == c, (N, X, b, c)
            assert abs(b - N/4) <= bound, (N, X, b)
            worst = max(worst, abs(b - N/4)/bound)
        for e in (64, 200, 512):
            X = N*2**e + rng.randrange(0, 2**e)
            c = count_components(N, X)
            assert abs(c - N/4) <= bound, (N, X, c)
            worst = max(worst, abs(c - N/4)/bound)
        rows.append(dict(N=N, bound=bound))
    report = dict(scope="Independent finite checks of main's R27 count; no orbit-hitting claim.",
                  checked=rows, max_error_over_bound=round(worst, 4),
                  brute_force_X_up_to="N*2^14", component_count_X_up_to="N*2^512", status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(report)


if __name__ == "__main__":
    main()
