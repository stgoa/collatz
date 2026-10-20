"""Sidekick probe: brute-force check of main's unbounded exposure-depth theorem
(experiments/residual_progress/templates/UNBOUNDED_EXPOSURE_DEPTH.md, commit 2be37b7),
and the depth at which each protected chain stops being an obstruction.

For X with 2^max(D+4,10) | X and X = 1 mod 3^(D+2), N = 3X/128, the theorem says the
component of 144N-1 in the depth-D exposure graph G_D(N) is the chain y_1..y_(D+3),
y_k = 3^k X/2^k - 1, with annular sources (-2, +2, +2) and no link to 1.

This check builds G_D(N) forward from every source of A_N with an independent
union-find. It then keeps exposing until the chain's component has nonpositive
mass or contains 1, and records which of the two happened first.
Finite checks only; no universal statement. Standard library. Run without -O.
"""
from pathlib import Path
import json
import sys

LANE = Path(__file__).resolve().parents[2] / "experiments" / "packet_currents" / "negative_controls"
sys.path.insert(0, str(LANE))
from affine_controls import step  # noqa: E402
from progress_measures_audit import increment  # noqa: E402


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


def v3(n):
    k = 0
    while n % 3 == 0:
        n, k = n // 3, k + 1
    return k


def least_X(D):
    power, modulus = 1 << max(D + 4, 10), 3 ** (D + 2)
    X = power
    while X % modulus != 1:
        X += power
    return X


def probe(X, D, cap=200):
    N = 3*X//128
    A = increment(1, N)
    chain = [3**k*X//2**k - 1 for k in range(1, D + 4)]
    assert [A.get(y) for y in chain[:3]] == [-2, 2, 2]
    graph, positions, sources = UnionFind(), list(A), list(A.items())
    for x in positions:
        graph.find(x)
    graph.find(1)
    exact = None
    for depth in range(1, cap + 1):
        positions = [1 if x == 1 else (graph.join(x, step(1, x)) or step(1, x)) for x in positions]
        root = graph.find(chain[2])
        if depth == D:
            members = {s for s in graph.parent if graph.find(s) == root}
            component_sources = sorted((s, c) for s, c in sources if graph.find(s) == root)
            exact = (members == set(chain) and component_sources == sorted(zip(chain[:3], (-2, 2, 2)))
                     and graph.find(1) != root)
            assert exact, (X, D)
        mass = sum(c for s, c in sources if graph.find(s) == root)
        linked = graph.find(1) == root
        if linked or mass <= 0:
            return dict(D=D, X=X, N=N, v3_X_minus_1=v3(X - 1), depth_D_component_is_chain=exact,
                        resolved_at_depth=depth, component_mass_then=mass, linked_to_1=linked)
    raise RuntimeError(f"unresolved within cap {cap}: X={X}, D={D}")


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rows = [probe(least_X(D), D) for D in (1, 2, 3, 4)]
    rows.append(probe(2**18, 1))                       # the theorem's ray example N = 6144
    report = dict(scope="Finite brute-force checks; the theorem's quantifiers rest on its proof.",
                  rows=rows, status="PASS")
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
