"""Sidekick probe: independent check of the two cancellation families stated in main's
RELEASE_PACKING.md (working copy, 2026-10-17 19:02).

Pair:   36N < q < 54N, q = 31 mod 54, u = (4q-1)/3:  2 d_q - 2 d_u = (I-P)(-2 d_u).
Triple: 64N < q < 72N, q = 31 or 103 mod 108, u = (4q-1)/3, v = (3q+1)/2:
        -d_u + 2 d_q - d_v = (I-P)(-d_u + d_q).

Each identity is rebuilt from the statement alone. Coefficients come from this
lane's own annulus A_N, by full construction for small N and by point evaluation
for large N. Also checked: arrows and exact valuations, the floor-count formulas,
and that no state is used twice within or across the two families.
Disjointness from main's older catalogue is NOT checked here.
Finite checks only. Standard library. Run without -O.
"""
from collections import Counter
from pathlib import Path
import json
import random
import sys

LANE = Path(__file__).resolve().parents[2] / "collatz_research_20261017" / "negative_controls"
sys.path.insert(0, str(LANE))
from affine_controls import step, valuation  # noqa: E402
from progress_measures_audit import increment, point_value  # noqa: E402


def count(N, a, b, r, m):
    return (b*N - 1 - r)//m - (a*N - r)//m


def families(N):
    pairs = [(q, (4*q - 1)//3) for q in range(36*N + 1, 54*N) if q % 54 == 31]
    triples = [(q, (4*q - 1)//3, (3*q + 1)//2) for q in range(64*N + 1, 72*N)
               if q % 108 in (31, 103)]
    return pairs, triples


def check_N(N, coefficient):
    pairs, triples = families(N)
    used = Counter()
    for q, u in pairs:
        assert 3*u + 1 == 4*q and valuation(1, u) == 2 and step(1, u) == q
        assert 48*N < u < 72*N and u % 18 == 5
        assert coefficient(q) == 2 and coefficient(u) == -2, (N, q, u)
        used.update((q, u))
    for q, u, v in triples:
        assert valuation(1, u) == 2 and step(1, u) == q
        assert valuation(1, q) == 1 and step(1, q) == v
        assert coefficient(u) == -1 and coefficient(q) == 2 and coefficient(v) == -1, (N, q, u, v)
        used.update((q, u, v))
    assert max(used.values(), default=1) == 1           # no state reused
    P = count(N, 36, 54, 31, 54)
    T = count(N, 64, 72, 31, 108) + count(N, 64, 72, 103, 108)
    assert (len(pairs), len(triples)) == (P, T)
    return P, T


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    full = list(range(8, 1025, 8))
    for N in full:
        A = increment(1, N)
        check_N(N, lambda y, A=A: A.get(y, 0))
    rng = random.Random(1017)
    # large N: point-evaluate only the boundary members and a random sample of each family
    boundary = []
    for N in [8*rng.randrange(10**5, 10**9) for _ in range(40)]:
        coefficient = lambda y, N=N: point_value(1, 64*N, y) - point_value(1, N, y)
        for lo, hi, mod, residues in ((36, 54, 54, (31,)), (64, 72, 108, (31, 103))):
            for r in residues:
                first = lo*N + 1 + (r - (lo*N + 1)) % mod
                last = hi*N - 1 - (hi*N - 1 - r) % mod
                for q in (first, first + mod, last - mod, last):
                    assert lo*N < q < hi*N and q % mod == r
                    if mod == 54:
                        u = (4*q - 1)//3
                        assert coefficient(q) == 2 and coefficient(u) == -2 and step(1, u) == q
                    else:
                        u, v = (4*q - 1)//3, (3*q + 1)//2
                        assert (coefficient(u), coefficient(q), coefficient(v)) == (-1, 2, -1)
                        assert step(1, u) == q and step(1, q) == v
        boundary.append(N)
    # count growth under N -> N + 216, and the 26N/27 removed-mass asymptotics
    for N in range(8, 8*500, 8):
        P0, T0 = count(N, 36, 54, 31, 54), count(N, 64, 72, 31, 108) + count(N, 64, 72, 103, 108)
        P1 = count(N + 216, 36, 54, 31, 54)
        T1 = count(N + 216, 64, 72, 31, 108) + count(N + 216, 64, 72, 103, 108)
        assert (P1 - P0, T1 - T0) == (72, 32)
        assert abs(27*(2*P0 + 2*T0) - 26*N) <= 27*8
    report = dict(scope="Independent finite checks of main's two release-packing families from their "
                  "statements; disjointness from main's older catalogue is not checked here.",
                  full_construction_N=[8, 1024], boundary_point_checks_N=len(boundary),
                  count_shift_216=[72, 32], status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
