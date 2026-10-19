"""Sidekick probe for open question Q2 (what sets the end depth of the protected chains).

Setting as in depth_probe.py (main's UNBOUNDED_EXPOSURE_DEPTH.md family): X with 2^max(D+4,10) | X and
X = 1 (mod 3^(D+2)), N = 3X/128, the chain y_k = 3^k X/2^k - 1 with annular sources (-2,+2,+2), and the
depth-d exposure graph that joins x to S(x) along the first d forward steps of every source of A_N.

Claim tested (an exact identity for this graph, not a conjecture): let O = (O_0 = y_1, O_1, ..., O_tau = 1)
be the forward orbit of y_1. Since the exposure graph is a functional forest rooted at 1, the chain's
component contains 1 iff every edge (O_q, O_(q+1)) has been exposed, and a source s exposes that edge
at step j_s + (q + 1 - p_s) where s first meets O after j_s steps, at O_(p_s), with p_s <= q. Hence

    link depth = max over q < tau of  min over sources s with p_s <= q of  dist(s, O_(q+1)).

So the end depth is a bottleneck ("relay") distance along the chain's own orbit. The bottleneck edge,
the length L of the chain's valuation-1 climb, and the index at which the orbit first comes back down
to the top of the source support (max supp A_N) are recorded to show which part of the orbit sets it.
The probe runs the union-find exposure independently and compares. Imports only the negative-controls
lane (affine_controls / progress_measures_audit), as depth_probe.py does. Run without -O.
"""
from pathlib import Path
import json
import sys

LANE = Path(__file__).resolve().parents[2] / "experiments" / "packet_currents" / "negative_controls"
sys.path.insert(0, str(LANE))
from affine_controls import step  # noqa: E402
from progress_measures_audit import increment  # noqa: E402


def v2(n):
    return (n & -n).bit_length() - 1


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        self.parent.setdefault(x, x)
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def join(self, a, b):
        self.parent[self.find(a)] = self.find(b)


def least_X(D):
    power, modulus = 1 << max(D + 4, 10), 3 ** (D + 2)
    X = power
    while X % modulus != 1:
        X += power
    return X


def exposure(A, chain1, cap=1000):
    """Union-find exposure as in depth_probe: returns (first depth with nonpositive chain mass or None,
    first depth at which the chain component contains 1)."""
    graph, positions, sources = UnionFind(), list(A), list(A.items())
    for x in positions:
        graph.find(x)
    graph.find(1)
    mass_depth = None
    for depth in range(1, cap + 1):
        positions = [1 if x == 1 else (graph.join(x, step(1, x)) or step(1, x)) for x in positions]
        root = graph.find(chain1)
        if mass_depth is None and sum(c for s, c in sources if graph.find(s) == root) <= 0:
            mass_depth = depth
        if graph.find(1) == root:
            return mass_depth, depth
    raise RuntimeError("cap")


def bottleneck(A, y1):
    O = [y1]
    while O[-1] != 1:
        O.append(step(1, O[-1]))
    pos = {z: i for i, z in enumerate(O)}
    best = {}                       # p -> min (j - p) over sources first meeting O at p
    for s in A:
        x, j = s, 0
        while x not in pos:
            x, j = step(1, x), j + 1
        p = pos[x]
        best[p] = min(best.get(p, 10**9), j - p)
    run, cost, arg = 10**9, -1, None
    for q in range(len(O) - 1):
        if q in best:
            run = min(run, best[q])
        c = run + q + 1             # min over p_s <= q of j_s + (q + 1 - p_s)
        if c > cost:
            cost, arg = c, q
    return cost, arg, len(O) - 1


def climb_length(y1):
    L, y = 0, y1
    while (3*y + 1) % 4 == 2:
        y, L = step(1, y), L + 1
    return L


def main():
    assert not sys.flags.optimize
    rows = []
    for D in (1, 2, 3, 4):
        power, modulus = 1 << max(D + 4, 10), 3 ** (D + 2)
        X0 = least_X(D)
        for k in range(4):
            X = X0 + k*power*modulus
            N = 3*X//128
            A = increment(1, N)
            y1 = 3*X//2 - 1
            assert [A.get(3**i * X // 2**i - 1) for i in (1, 2, 3)] == [-2, 2, 2]
            mass_depth, link_depth = exposure(A, y1)
            cost, q, tau = bottleneck(A, y1)
            L = climb_length(y1)
            assert cost == link_depth, (D, X, cost, link_depth)
            top_src = max(A)
            O = [y1]
            while O[-1] != 1:
                O.append(step(1, O[-1]))
            reentry = next(i for i in range(L, len(O)) if O[i] <= top_src)
            # sources other than the chain whose orbits meet the chain orbit before the bottleneck edge
            rows.append(dict(D=D, X=X, N=N, climb_L=L, link_depth=link_depth, bottleneck_edge=q,
                             bottleneck_in_climb=q < L, orbit_length_to_1=tau,
                             max_source_over_N=round(top_src / N, 3), reentry_index=reentry,
                             bottleneck_minus_reentry=q - reentry,
                             nonpositive_mass_depth=mass_depth,
                             end_depth=min(link_depth, mass_depth or 10**9)))
            print(rows[-1], flush=True)
    out = {"probe": "q2_end_depth", "rows": rows,
           "identity": "link depth = bottleneck relay distance along the chain orbit (all rows)",
           "result": "PASS"}
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main()
