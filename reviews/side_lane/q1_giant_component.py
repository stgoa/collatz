"""Sidekick probe for open question Q1 (absorption as a giant component).

For the annular increment A_N (imported from the negative-controls lane, as in depth_probe.py), expose
the forward graph depth by depth, joining x to S(x) along the first d steps of every source. Record the
fraction of the positive mass of A_N whose component contains 1, and the fraction of positive mass in
"resolved" components (containing 1, or with nonpositive total mass), as functions of d. Report the
depths d_q(N) at which these fractions first reach q = 0.5, 0.9, 0.99, 0.999 and 1, against log2 N.

Exposure is exact but economical: a walker that steps onto an already exposed node is dropped, since
the walker that exposed it first is ahead on the same deterministic path and exposes every later edge
no later. (Walkers at 1 stop.) Finite measurements; no asymptotic claim. Run without -O.
"""
from pathlib import Path
import json
import math
import sys
import time

LANE = Path(__file__).resolve().parents[2] / "collatz_research_20261017" / "negative_controls"
sys.path.insert(0, str(LANE))
from affine_controls import step  # noqa: E402
from progress_measures_audit import increment  # noqa: E402

QS = (0.5, 0.9, 0.99, 0.999, 1.0)


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.mass = {}

    def find(self, x):
        p = self.parent
        if x not in p:
            p[x] = x
            return x
        root = x
        while p[root] != root:
            root = p[root]
        while p[x] != root:
            p[x], x = root, p[x]
        return root

    def join(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb
            self.mass[rb] = self.mass.get(rb, 0) + self.mass.pop(ra, 0)


def measure(N, cap=2000):
    A = increment(1, N)
    pos_total = sum(c for c in A.values() if c > 0)
    uf = UnionFind()
    for x, c in A.items():
        uf.find(x)
        r = uf.find(x)
        uf.mass[r] = uf.mass.get(r, 0) + c
    uf.find(1)
    visited = set(A) | {1}
    walkers = [x for x in A if x != 1]
    pending = {x: c for x, c in A.items() if c > 0}      # positive sources not yet in 1's component
    first = {}
    first_res = {}
    absorbed_curve = []
    depth = 0
    while pending and depth < cap:
        depth += 1
        nxt = []
        for x in walkers:
            y = step(1, x)
            uf.join(x, y)
            if y not in visited:
                visited.add(y)
                if y != 1:
                    nxt.append(y)
        walkers = nxt
        r1 = uf.find(1)
        for x in [x for x in pending if uf.find(x) == r1]:
            del pending[x]
        absorbed = 1 - sum(pending.values()) / pos_total
        resolved_pending = sum(c for x, c in pending.items() if uf.mass.get(uf.find(x), 0) <= 0)
        resolved = absorbed + resolved_pending / pos_total
        absorbed_curve.append(round(absorbed, 6))
        for q in QS:
            if q not in first and absorbed >= q - 1e-12:
                first[q] = depth
            if q not in first_res and resolved >= q - 1e-12:
                first_res[q] = depth
    assert not pending, (N, depth)
    return dict(N=N, log2N=round(math.log2(N), 3), sources=len(A), positive_mass=pos_total,
                exposed_nodes=len(visited),
                depth_absorbed={str(q): first[q] for q in QS},
                depth_resolved={str(q): first_res.get(q) for q in QS},
                ratio_to_log2N={str(q): round(first[q] / math.log2(N), 3) for q in QS},
                absorbed_curve=absorbed_curve)


def main():
    assert not sys.flags.optimize
    rows = []
    for k in range(0, 10):
        N = 96 * 2**k
        t0 = time.time()
        r = measure(N)
        r["seconds"] = round(time.time() - t0, 1)
        rows.append(r)
        print({k: v for k, v in r.items() if k != "absorbed_curve"}, flush=True)
    out = {"probe": "q1_giant_component", "rows": rows, "result": "DONE"}
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main()
