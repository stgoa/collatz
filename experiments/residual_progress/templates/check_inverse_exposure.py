"""Check complete aggregate components using finite inverse enumeration.

This verifies two fixed cutoffs, not an obstruction at every exposure depth.
The large example lies on a required ray. No Collatz assertion is inferred.
"""

import argparse
from collections import defaultdict, deque
import importlib.util
import json
from pathlib import Path

from inverse_exposure_probe import coefficient, component, predecessors, step

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SPEC = importlib.util.spec_from_file_location(
    "canonical_annular_source",
    ROOT / "experiments/current_construction/recursive/check_annular_recursion.py")
ANNULAR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ANNULAR)


def forward_graph(measure, depth):
    """Independent direct exposure of all source orbits, retaining history."""
    edges, adjacency = {}, defaultdict(set)
    for source in measure:
        x = source
        for _ in range(depth):
            if x == 1:
                break
            y = ANNULAR.PACKETS.step(x)
            edges[x] = y
            adjacency[x].add(y)
            adjacency[y].add(x)
            x = y
    return edges, adjacency


def direct_component(seed, adjacency):
    seen, queue = {seed}, deque([seed])
    while queue:
        x = queue.popleft()
        for y in adjacency[x]:
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return seen


def check_small_graphs():
    comparisons = []
    for N in (8, 16, 96, 288):
        measure = ANNULAR.annular_measure(N)
        direct_measure = {x: coefficient(N, x) for x in range(1, 144 * N, 2)
                          if coefficient(N, x)}
        assert direct_measure == measure
        seeds = sorted({min(measure), sorted(measure)[len(measure) // 2], max(measure)})
        for depth in (1, 2, 4, 8):
            edges, adjacency = forward_graph(measure, depth)
            for seed in seeds:
                report, graph = component(N, depth, seed, state_cap=50000,
                                          query_cap=200000)
                assert report["status"] == "complete_component"
                nodes = direct_component(seed, adjacency)
                assert graph["nodes"] == nodes
                assert graph["edges"] == {x: y for x, y in edges.items() if x in nodes}
                assert graph["sources"] == {x: measure[x] for x in nodes if x in measure}
                assert report["signed_source_mass"] == sum(measure.get(x, 0) for x in nodes)
                comparisons.append(dict(N=N, depth=depth, seed=seed,
                                        vertices=len(nodes), mass=report["signed_source_mass"]))
    # Check inverse completeness separately against forward images, including 1.
    bound = 2047
    brute = defaultdict(set)
    for x in range(3, bound + 1, 2):
        brute[ANNULAR.PACKETS.step(x)].add(x)
    for y in range(1, 3 * bound // 2 + 2, 2):
        assert set(predecessors(y, bound)) == brute[y]
    return comparisons


def save_graph(report, graph):
    return dict(report=report, nodes=sorted(graph["nodes"]),
                arrows=[[x, y] for x, y in sorted(graph["edges"].items())])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    comparisons = check_small_graphs()

    # A complete aggregate counterexample to the naive always-positive top chain.
    before, _ = component(10368, 1, state_cap=10000, query_cap=20000)
    assert before["status"] == "complete_component"
    assert before["signed_source_mass"] == 6 and not before["linked_to_1"]
    counter, counter_graph = component(10368, 2, state_cap=10000, query_cap=20000)
    assert counter["status"] == "complete_component"
    assert counter["vertices"] == 34 and counter["source_atoms"] == 27
    assert counter["signed_source_mass"] == 0 and not counter["linked_to_1"]
    assert sum(c for c in counter_graph["sources"].values() if c > 0) == 22
    assert sum(c for c in counter_graph["sources"].values() if c < 0) == -22
    chain_from_negative = (174761, 131071, 196607, 294911,
                           442367, 663551, 995327, 1492991)
    for x, y in zip(chain_from_negative, chain_from_negative[1:]):
        assert counter_graph["edges"][x] == y
    assert [coefficient(10368, x) for x in chain_from_negative] == [-1, 0, 3, 0, 1, 1, 2, 2]

    # A complete depth-32 obstruction on the ray 12*2^b, without expanding A_N.
    N, depth = 96 * 2**24, 32
    positive, positive_graph = component(N, depth, state_cap=10000, query_cap=20000)
    assert positive["status"] == "complete_component"
    assert positive["positive_component_obstruction"]
    assert positive["sources"] == [[64 * N - 1, -2],
                                   [96 * N - 1, 2], [144 * N - 1, 2]]
    assert positive["signed_source_mass"] == 2
    # The completed component is exactly this chain, including every incoming edge.
    chain = [64 * N - 1]
    for _ in range(depth + 2):
        numerator = 3 * chain[-1] + 1
        assert numerator % 4 == 2
        chain.append(numerator // 2)
    assert positive_graph["nodes"] == set(chain)
    assert positive_graph["edges"] == dict(zip(chain, chain[1:]))
    assert len(chain) == 35 and 1 not in chain

    # Hitting either cap is explicitly unresolved and cannot become an obstruction.
    state_capped, graph = component(96, 2, state_cap=1)
    assert state_capped["status"] == "unresolved_cap" and graph is None
    query_capped, graph = component(96, 2, query_cap=1)
    assert query_capped["status"] == "unresolved_cap" and graph is None

    result = dict(status="PASS", full_graph_comparisons=comparisons,
                  predecessor_bruteforce_bound=2047,
                  naive_top_chain_previous_depth=before,
                  naive_top_chain_counterexample=save_graph(counter, counter_graph),
                  depth_32_aggregate_obstruction=save_graph(positive, positive_graph),
                  cap_checks=[state_capped, query_capped],
                  arbitrary_depth_aggregate_obstruction_proved=False,
                  universal_current_construction_proved=False)
    path = HERE / "inverse_exposure_audit.json"
    if args.write_receipt:
        path.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == result
    print(json.dumps(dict(status="PASS", independent_full_graph_comparisons=len(comparisons),
                          counterexample={k: v for k, v in counter.items() if k != "sources"},
                          aggregate_obstruction={k: v for k, v in positive.items() if k != "sources"},
                          arbitrary_depth_aggregate_obstruction_proved=False), indent=2))


if __name__ == "__main__":
    main()
