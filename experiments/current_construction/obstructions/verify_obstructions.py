"""Finite checks for functional-graph current criteria and packet obstructions.

Standard library only. This is not a universal Collatz current constructor.
Exploratory search always has a finite depth cap and may return unresolved.
"""

from collections import defaultdict, deque
from itertools import product
import json


def clean(mu):
    return {x: c for x, c in mu.items() if c}


def syracuse(x):
    assert x and x % 2
    z = 3 * x + 1
    return z // (abs(z) & -abs(z))


def divergence(current, step, absorber):
    result = defaultdict(int)
    for x, c in current.items():
        assert x != absorber
        result[x] += c
        target = step(x)
        if target != absorber:
            result[target] -= c
    return clean(result)


def finite_certificate(mu, edges, absorber, one_sided=False):
    """Use only exposed arrows; None means unresolved on this finite graph.

    edges maps arrow origins to targets. Source/target vertex labels must be
    comparable integers. Negative traversal is permitted for signed currents.
    """
    mu = clean(mu)
    adjacency = defaultdict(list)
    for x in mu:
        adjacency[x]
    for x, y in edges.items():
        assert x != absorber
        adjacency[x].append((y, x, 1))
        adjacency[y].append((x, x, -1))
    unseen = set(adjacency)
    components = []
    while unseen:
        seed = min(unseen)
        component = {seed}
        queue = [seed]
        unseen.remove(seed)
        while queue:
            x = queue.pop()
            for y, _, _ in adjacency[x]:
                if y in unseen:
                    unseen.remove(y)
                    component.add(y)
                    queue.append(y)
        mass = sum(mu.get(x, 0) for x in component)
        if absorber not in component and (mass > 0 if one_sided else mass != 0):
            return None
        components.append((component, mass))
    current, residual = defaultdict(int), defaultdict(int)
    for component, mass in components:
        anchor = absorber if absorber in component else min(component)
        parent = {anchor: None}
        queue = deque([anchor])
        while queue:
            x = queue.popleft()
            for y, origin, direction in adjacency[x]:
                if y not in parent:
                    # The stored traversal is from child y to parent x.
                    parent[y] = (x, origin, -direction)
                    queue.append(y)
        for source in sorted(component):
            c, x = mu.get(source, 0), source
            if not c:
                continue
            while parent[x] is not None:
                target, origin, direction = parent[x]
                current[origin] += c * direction
                x = target
        if anchor != absorber:
            residual[anchor] += mass
    current, residual = clean(current), clean(residual)
    assert not one_sided or all(c < 0 for c in residual.values())
    if not one_sided:
        assert not residual
    return current, residual


def capped_search(mu, step, absorber, max_depth, one_sided=False):
    """Complete in the unbounded-depth limit, with an explicit finite cap."""
    assert max_depth >= 0
    mu = clean(mu)
    assert absorber not in mu
    edges = {}
    frontiers = set(mu)
    for depth in range(max_depth + 1):
        certificate = finite_certificate(mu, edges, absorber, one_sided)
        if certificate is not None:
            current, residual = certificate
            check = defaultdict(int, divergence(current, step, absorber))
            for x, c in residual.items():
                check[x] += c
            assert clean(check) == mu
            return dict(status="certificate", depth=depth,
                        current=current, residual=residual)
        if depth == max_depth:
            break
        new_frontiers = set()
        for x in frontiers:
            if x == absorber:
                continue
            y = step(x)
            edges[x] = y
            new_frontiers.add(y)
        frontiers = new_frontiers
    return dict(status="unresolved", depth=max_depth)


def orbit_component_labels(mapping):
    """Independent finite-map labels via eventual cycles, absorber label ()."""
    labels = {0: ()}
    for source in mapping:
        seen, path, x = {}, [], source
        while x not in labels and x not in seen:
            seen[x] = len(path)
            path.append(x)
            x = mapping[x]
        label = labels[x] if x in labels else tuple(sorted(path[seen[x]:]))
        for x in path:
            labels[x] = label
    return labels


def check_finite_graphs():
    checked = 0
    for targets in product(range(4), repeat=3):
        mapping = dict(zip(range(1, 4), targets))
        labels = orbit_component_labels(mapping)
        for weights in product((-1, 0, 1), repeat=3):
            mu = clean(dict(zip(range(1, 4), weights)))
            masses = defaultdict(int)
            for x, c in mu.items():
                masses[labels[x]] += c
            for one_sided in (False, True):
                expected = all((mass <= 0 if one_sided else mass == 0)
                               for label, mass in masses.items() if label)
                certificate = finite_certificate(mu, mapping, 0, one_sided)
                assert (certificate is not None) == expected
                if certificate is not None:
                    current, residual = certificate
                    result = defaultdict(int, divergence(current, mapping.__getitem__, 0))
                    for x, c in residual.items():
                        result[x] += c
                    assert clean(result) == mu
            checked += 1
    return checked


def check_packet_obstruction(H):
    K = 2 * H + 7
    y, N = 9 * 2**K - 1, 4 * 2**K + 5
    t = 3 * 2**(K - 1) - 1
    n1 = (3 * N + 1) // 2
    last = (n1 - 3) // 4
    assert 5 + 6 * t == y and last == t + 2
    assert (last + 1) % 3 == t % 3 == 2
    assert [3 * int((3 + 4 * (t + j)) % 3 == 2) - 1
            for j in range(3)] == [2, -1, -1]
    paths = []
    for source in (y, y + 6, y + 12):
        path = [source]
        for _ in range(H):
            path.append(syracuse(path[-1]))
        paths.append(path)
    assert all(x % 32 == 31 for x in paths[0])
    assert all(x % 32 in {1, 5, 11, 13, 17} for path in paths[1:] for x in path)
    assert not set(paths[0]).intersection(paths[1] + paths[2] + [1])
    return dict(H=H, K=K, source_bits=y.bit_length(),
                minimum_certificate_rows=H + 1)


def main():
    finite_cases = check_finite_graphs()
    negative = {-1: 1, -5: -1}
    assert syracuse(-1) == -1 and syracuse(-5) == -7 and syracuse(-7) == -5
    assert capped_search(negative, syracuse, 1, 8, one_sided=True)["status"] == "unresolved"
    lag = capped_search({2: 1, 3: -1}, lambda n: n + 1, 0, 1)
    assert lag["status"] == "certificate" and lag["current"] == {2: 1}
    for one_sided in (False, True):
        result = capped_search({27: 2, 33: -1, 39: -1}, syracuse, 1, 100, one_sided)
        assert result["status"] == "certificate"
    obstructions = [check_packet_obstruction(H) for H in (0, 1, 2, 4, 8, 16, 32, 64, 128)]
    for t in range(10000):
        x, z = 69 + 256 * t, 75 + 256 * t
        u, v = syracuse(syracuse(x)), syracuse(syracuse(z))
        assert u == 5 + 18 * t and v == 16 * u + 5
        assert syracuse(u) == syracuse(v)
    report = dict(status="PASS", finite_graph_measure_cases=finite_cases,
                  certificate_modes_per_case=2, coalescence_parameter_range=[0, 9999],
                  bounded_template_obstructions=obstructions,
                  universal_current_existence_proved=False)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
