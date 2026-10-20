"""Incremental historical graph diagnostics for six-band annular measures.

Each exposed state is expanded only once, in multi-source breadth-first order.
Finite depth caps never imply nonexistence. No universal constructor is proved.
"""

from collections import defaultdict
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ANNULAR = load("annular_source", ROOT / "experiments/current_construction/recursive/check_annular_recursion.py")
CURRENT = load("finite_current", ROOT / "experiments/current_construction/obstructions/verify_obstructions.py")
step = ANNULAR.PACKETS.step


class Components:
    def __init__(self, measure, band_of):
        self.parent, self.size, self.masses, self.counts = {}, {}, {}, {}
        self.absorbed, self.minimum, self.roots = {}, {}, set()
        for x, coefficient in measure.items():
            self.add(x)
            self.masses[x][band_of[x]] = coefficient
            self.counts[x][band_of[x]] = 1

    def add(self, x):
        if x in self.parent:
            return False
        self.parent[x], self.size[x] = x, 1
        self.masses[x], self.counts[x] = [0] * 6, [0] * 6
        self.absorbed[x], self.minimum[x] = x == 1, x
        self.roots.add(x)
        return True

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.roots.remove(ry)
        self.size[rx] += self.size[ry]
        self.masses[rx] = [a + b for a, b in zip(self.masses[rx], self.masses[ry])]
        self.counts[rx] = [a + b for a, b in zip(self.counts[rx], self.counts[ry])]
        self.absorbed[rx] |= self.absorbed[ry]
        self.minimum[rx] = min(self.minimum[rx], self.minimum[ry])

    def snapshot(self):
        unresolved, linked_sources = [], 0
        band_positive_counts = [0] * 6
        band_nonzero_counts = [0] * 6
        for root in self.roots:
            source_count = sum(self.counts[root])
            if not source_count:
                continue
            if self.absorbed[root]:
                linked_sources += source_count
                continue
            masses = self.masses[root]
            for j, mass in enumerate(masses):
                band_positive_counts[j] += mass > 0
                band_nonzero_counts[j] += mass != 0
            unresolved.append(dict(minimum_state=self.minimum[root],
                                   signed_mass=sum(masses), band_masses=masses[:],
                                   source_count=source_count,
                                   band_source_counts=self.counts[root][:]))
        unresolved.sort(key=lambda c: c["minimum_state"])
        positives = [c for c in unresolved if c["signed_mass"] > 0]
        mixed_cancellations = [c for c in unresolved if c["signed_mass"] <= 0
                              and any(m > 0 for m in c["band_masses"])]
        return dict(unresolved_component_count=len(unresolved),
                    positive_component_count=len(positives),
                    positive_component_mass=sum(c["signed_mass"] for c in positives),
                    nonzero_component_count=sum(c["signed_mass"] != 0 for c in unresolved),
                    sources_linked_to_1=linked_sources,
                    sources_not_linked_to_1=sum(c["source_count"] for c in unresolved),
                    band_positive_component_counts=band_positive_counts,
                    band_nonzero_component_counts=band_nonzero_counts,
                    cross_band_cancellation_components=len(mixed_cancellations),
                    positive_components=positives,
                    unresolved_components=unresolved)


def current_for(measure, edges, one_sided):
    result = CURRENT.finite_certificate(measure, edges, 1, one_sided)
    assert result is not None
    current, residual = result
    check = defaultdict(int, CURRENT.divergence(current, step, 1))
    for x, coefficient in residual.items():
        check[x] += coefficient
    assert CURRENT.clean(check) == measure
    assert not one_sided or all(c < 0 for c in residual.values())
    return current, residual


def explore(N, max_depth=128, keep_certificates=False):
    measure = ANNULAR.annular_measure(N)
    Q = 9 * N // 4
    band_of = {x: (x // Q).bit_length() - 1 for x in measure}
    assert all(0 <= j <= 5 for j in band_of.values())
    components = Components(measure, band_of)
    frontier, edges, trace, first, certificates = list(measure), {}, [], {}, {}
    previous = None
    for depth in range(max_depth + 1):
        snapshot = components.snapshot()
        brief = {k: v for k, v in snapshot.items()
                 if k not in ("positive_components", "unresolved_components")}
        brief.update(depth=depth, exposed_arrows=len(edges), frontier_states=len(frontier))
        trace.append(brief)
        successes = {
            "aggregate_one_sided": snapshot["positive_component_count"] == 0,
            "aggregate_exact": snapshot["nonzero_component_count"] == 0,
            "each_band_one_sided": max(snapshot["band_positive_component_counts"]) == 0,
            "each_band_exact": max(snapshot["band_nonzero_component_counts"]) == 0,
        }
        for label, success in successes.items():
            if success and label not in first:
                first[label] = dict(depth=depth, exposure=snapshot,
                                    previous_positive_components=[] if previous is None else previous["positive_components"])
                if label.startswith("aggregate"):
                    current, residual = current_for(measure, edges, label.endswith("one_sided"))
                    first[label].update(current_rows=len(current),
                                        positive_current_cost=sum(c for c in current.values() if c > 0),
                                        residual=[[x, c] for x, c in sorted(residual.items())])
                    if keep_certificates:
                        certificates[label] = (current, residual)
        if successes["each_band_exact"] or depth == max_depth:
            break
        previous = snapshot
        following = []
        for x in frontier:
            if x == 1:
                continue
            assert x not in edges
            y = step(x)
            if components.add(y):
                following.append(y)
            edges[x] = y
            components.union(x, y)
        frontier = following
    return dict(N=N, source_atoms=len(measure), source_mass=sum(measure.values()),
                band_signed_masses=[sum(c for x, c in measure.items() if band_of[x] == j) for j in range(6)],
                cap=max_depth, status="all_band_certificates" if "each_band_exact" in first else "capped",
                first=first, trace=trace), certificates


if __name__ == "__main__":
    for cutoff in (96, 112, 128, 144, 168, 384):
        result, _ = explore(cutoff)
        print(json.dumps(dict(N=cutoff, first_depths={k: v["depth"] for k, v in result["first"].items()},
                              exact_unknown=result["first"].get("aggregate_exact", {}).get("exposure", {}).get("sources_not_linked_to_1"))), flush=True)
