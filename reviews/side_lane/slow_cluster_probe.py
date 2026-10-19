"""Sidekick probe: what sets the whole-annulus exposure depth d*(N)?

For N in {96, 112, 128, 144, 168} and 64N (one step along each of main's
five rays), expose every source of A_N forward with an independent union-find.
d*(N) is the first depth at which no component outside the component of 1 has
positive source mass. The probe also records the last positive component.

Test of a renormalization idea: if obstructions at scale 64N were lifted
copies of obstructions at scale N, an induction down the x64 ladder could
reach the verified base. Finite data only. Standard library. Run without -O.
"""
from collections import defaultdict
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "experiments" / "packet_currents" / "negative_controls")]
from affine_controls import step  # noqa: E402
from progress_measures_audit import increment  # noqa: E402
from depth_probe import UnionFind  # noqa: E402


def tau(x):
    t = 0
    while x != 1:
        x, t = step(1, x), t + 1
    return t


def resolve(N, cap=400):
    A = increment(1, N)
    graph, positions, sources = UnionFind(), list(A), list(A.items())
    for x in positions:
        graph.find(x)
    graph.find(1)
    last = None
    for depth in range(cap + 1):
        totals, members = defaultdict(int), defaultdict(list)
        for s, c in sources:
            root = graph.find(s)
            totals[root] += c
            members[root].append((s, c))
        sink = graph.find(1)
        positive = {r: m for r, m in totals.items() if r != sink and m > 0}
        if not positive:
            return depth, last
        root = max(positive, key=lambda r: (positive[r], len(members[r])))
        last = dict(depth=depth, components=len(positive), mass=positive[root],
                     sources=sorted(members[root]))
        positions = [1 if x == 1 else (graph.join(x, step(1, x)) or step(1, x)) for x in positions]
    raise RuntimeError(f"unresolved at cap {cap}: N={N}")


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rows = []
    for a in (12, 14, 16, 18, 21):
        for N in (8*a, 512*a):
            d_star, last = resolve(N)
            states = [s for s, c in last["sources"]]
            rows.append(dict(N=N, d_star=d_star, last_depth=last["depth"],
                             last_positive_components=last["components"], last_mass=last["mass"],
                             last_sources=last["sources"],
                             last_source_stopping_times=sorted(tau(s) for s in states)))
    big = [set(s for s, c in r["last_sources"]) for r in rows if r["N"] in (7168, 8192, 9216, 10752)]
    common = sorted(set.intersection(*big))
    assert common[:2] == [270271, 360361] and 3*360361 + 1 == 4*270271
    report = dict(scope="Finite exposure data; no universal statement.", rows=rows,
                  common_last_states_7168_8192_9216_10752=common, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    for r in rows:
        print(r["N"], r["d_star"], r["last_mass"], len(r["last_sources"]), r["last_source_stopping_times"][-3:])
    print("common:", common)


if __name__ == "__main__":
    main()
