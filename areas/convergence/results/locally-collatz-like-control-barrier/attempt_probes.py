"""Probes from a direct attempt on the annular obligation; both are negative results.

1. High-level annihilation fails (d = 1). For annuli A_N on the rays, the forced
   current J_N = sum_j P^j A_N (unique by C3) always carries nonzero signed
   traffic into 1 through several entry points, and its support reaches 5.
   Positive and negative annular mass do not cancel above the bottom, so any
   proof must control the complete descent. ||J_N^+||_1 grows linearly in N.
2. The criterion fails class by class (controls). For T_-1, T_5 and T_13, each
   nontrivial cycle basin K separately has <1_K, Pi_N> > 0 at some cutoff,
   matching the class-wise maximum principle (NOTE.md, Section 12).

Finite checks only. Standard library only. Run without -O.
"""
from collections import defaultdict
from pathlib import Path
import json
import sys

from affine_controls import Basins, cutoffs, packets, step
from progress_measures_audit import increment


def forward_current(mu):
    J, current, entries = defaultdict(int), dict(mu), defaultdict(int)
    while current:
        nxt = defaultdict(int)
        for y, c in current.items():
            J[y] += c
            z = step(1, y)
            if z == 1:
                entries[y] += c
            else:
                nxt[z] += c
        current = {y: c for y, c in nxt.items() if c}
    clean = lambda m: {y: c for y, c in m.items() if c}
    return clean(J), clean(entries)


def annihilation(cases):
    rows = []
    for N in cases:
        Q = 9*N//4
        A = increment(1, N)
        J, entries = forward_current(A)
        assert sum(entries.values()) == 0 and any(entries.values())
        assert min(J) == 5 < Q
        rows.append(dict(N=N, Q=Q, current_rows=len(J), entry_traffic=sorted(entries.items()),
                         J_plus=sum(c for c in J.values() if c > 0),
                         source_positive=sum(c for c in A.values() if c > 0)))
    return rows


def classwise(d, nmax):
    basins = Basins(d)
    top = 3*cutoffs(d, nmax)[1] + 64
    for x in range(1, top, 2):
        basins(x)
    classes = sorted(m for m in basins.cycles if m not in basins.trivial())
    first = {}
    for N in range(8, nmax + 1):
        packet, _, _ = packets(d, N)
        for m in classes:
            if m not in first:
                k = sum(c for y, c in packet.items() if basins(y) == m)
                if k > 0:
                    first[m] = [N, k]
        if len(first) == len(classes):
            break
    assert len(first) == len(classes), d
    least = {m: min(x for x in range(1, top, 2) if basins(x) == m) for m in classes}
    return {str(m): dict(first_positive_cutoff=first[m][0], pairing=first[m][1],
                         least_seed=least[m]) for m in classes}


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    report = dict(scope="Negative results from a direct attempt; no universal statement is "
                  "proved or refuted for 3x+1.",
                  high_level_annihilation=annihilation((96, 168, 384, 768, 1536, 3072)),
                  classwise_controls={str(d): classwise(d, 1500) for d in (-1, 5, 13)},
                  status="PASS")
    path = Path(__file__).with_name("attempt_probes.json")
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["classwise_controls"], sort_keys=True))
    for row in report["high_level_annihilation"]:
        print(row["N"], row["J_plus"], row["entry_traffic"])


if __name__ == "__main__":
    main()
