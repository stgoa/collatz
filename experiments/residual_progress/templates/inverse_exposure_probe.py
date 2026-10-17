"""Recover a complete exposed component without materializing an annulus.

Bounded inverse reachability accounts for every actual nonzero annular source.
State/query caps return unresolved. A completed positive component is a finite
dual obstruction at the chosen exposure depth; it is not a Collatz obstruction.
"""

from collections import deque
from functools import lru_cache

RESIDUES = (1, 5, 7, 11, 13, 17)
ROWS = ((1, 0, 1, 0, -2, 0), (2, 1, -1, 1, -1, -2),
        (3, -1, -3, 2, 0, -1), (1, -3, -2, 3, 1, 0),
        (-1, -2, -1, 1, 2, 1), (0, -1, 0, -1, 0, 2))
COEFFICIENTS = [dict(zip(RESIDUES, row)) for row in ROWS]


def step(x):
    """The caller suppresses the outgoing arrow at the absorbing state 1."""
    assert x > 0 and x % 2
    numerator = 3 * x + 1
    return numerator // (numerator & -numerator)


def coefficient(N, x):
    Q = 9 * N // 4
    if not Q < x < 64 * Q or x % 2 == 0:
        return 0
    band = (x // Q).bit_length() - 1
    return COEFFICIENTS[band].get(x % 18, 0)


def predecessors(y, bound):
    """All nonabsorbing odd predecessors at most bound, with exact valuation."""
    if y % 3 == 0:
        return
    power = 2 if y % 3 == 2 else 4
    while power * y <= 3 * bound + 1:
        x = (power * y - 1) // 3
        if x > 1:
            assert x % 2 and step(x) == y
            yield x
        power *= 4


class CapReached(Exception):
    pass


def component(N, depth, seed=None, state_cap=100000, query_cap=500000):
    """Return the entire seed component in D-step exposure, or unresolved.

    Depth is measured from every actual nonzero A_N source, independently.
    It is not a bound on graph distance from seed or on an undirected path.
    """
    assert N > 0 and N % 8 == 0 and depth >= 1
    seed = 144 * N - 1 if seed is None else seed
    assert coefficient(N, seed) != 0
    assert state_cap >= 1 and query_cap >= 1
    bounds = [(3**d * 144 * N) // 2**d - 1 for d in range(depth + 1)]
    queries = 0

    @lru_cache(maxsize=None)
    def reachable(x, remaining):
        nonlocal queries
        queries += 1
        if queries > query_cap:
            raise CapReached
        if coefficient(N, x):
            return True
        if remaining == 0 or x > bounds[remaining]:
            return False
        return any(reachable(p, remaining - 1) for p in predecessors(x, bounds[remaining - 1]))

    nodes, frontier, edges = {seed}, deque([seed]), {}
    try:
        while frontier:
            x = frontier.popleft()
            neighbours = []
            if x != 1 and reachable(x, depth - 1):
                y = step(x)
                edges[x] = y
                neighbours.append(y)
            for p in predecessors(x, bounds[depth - 1]):
                if reachable(p, depth - 1):
                    edges[p] = x
                    neighbours.append(p)
            for y in neighbours:
                if y not in nodes:
                    nodes.add(y)
                    frontier.append(y)
                    if len(nodes) > state_cap:
                        raise CapReached
    except CapReached:
        return dict(status="unresolved_cap", N=N, depth=depth, seed=seed,
                    visited_states=len(nodes), reachability_queries=queries), None
    sources = {x: coefficient(N, x) for x in nodes if coefficient(N, x)}
    report = dict(status="complete_component", N=N, depth=depth, seed=seed,
                  vertices=len(nodes), arrows=len(edges), source_atoms=len(sources),
                  signed_source_mass=sum(sources.values()), linked_to_1=1 in nodes,
                  reachability_queries=queries,
                  positive_component_obstruction=1 not in nodes and sum(sources.values()) > 0,
                  sources=[[x, c] for x, c in sorted(sources.items())])
    return report, dict(nodes=nodes, edges=edges, sources=sources)
