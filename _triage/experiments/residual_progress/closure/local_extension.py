"""Exact local packet/absorption conversions, with every residual retained.

The caller supplies an absorption current for the inner interval. This module
does not prove that such currents exist at arbitrary cutoffs.
"""

from collections import defaultdict
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(name, path):
    spec = spec_from_file_location(name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


FORCING = load("local_extension_forcing", HERE.parent / "forcing/actual_graph_compiler.py")
PACKETS, CURRENT = FORCING.PACKETS, FORCING.CURRENT


def combine(*terms):
    result = defaultdict(int)
    for coefficient, measure in terms:
        for x, c in measure.items():
            result[x] += coefficient * c
    return {x: c for x, c in result.items() if c}


def count(N):
    return dict.fromkeys(range(3, N + 1, 2), 1)


def divergence(current):
    return CURRENT.divergence(current, PACKETS.step, 1)


def geometry(N):
    if not isinstance(N, int) or N < 8 or N % 8:
        raise ValueError("N must be a positive multiple of 8")
    packet, eta, _ = PACKETS.right_packets(N)
    inner = combine((2, count(N)), (-1, count(N // 4)),
                    (-1, count(3 * N // 4)))
    outer = combine((1, count(3 * N // 2)), (-1, count(N)))
    complement = combine((2, count(N // 4)), (1, outer))
    scale = combine((1, inner), (-1, complement))
    K = combine((1, PACKETS.initial(N)), (3, count(N)),
                (-3, count(N // 4)))
    assert scale == combine((1, packet), (1, eta), (1, divergence(K)))
    assert min(inner.values()) > 0 and min(complement.values()) > 0
    assert sum(inner.values()) == N // 2
    assert sum(complement.values()) == N // 2 - 2
    assert set(inner) == set(range(N // 4 + 1, N, 2))
    return dict(N=N, packet=packet, eta=eta, K=K, inner=inner,
                outer=outer, complement=complement, scale=scale)


def automatic_packet(geo, inner_current):
    """Construct a one-sided packet input using only the supplied inner current."""
    assert divergence(inner_current) == geo["inner"]
    eta_current = FORCING.absorption_current(geo["eta"])
    current = combine((1, inner_current), (-1, geo["K"]), (-1, eta_current))
    residual = combine((-1, geo["complement"]))
    assert combine((1, divergence(current)), (1, residual)) == geo["packet"]
    return current, residual, eta_current


def extend_packet(geo, inner_current, packet_current, packet_residual):
    """Convert a checked packet certificate into a complement/outer certificate.

    No outer trajectory is followed. Output positive residuals are returned in
    full; this function does not turn an unresolved result into success.
    """
    assert divergence(inner_current) == geo["inner"]
    assert all(c <= 0 for c in packet_residual.values())
    assert combine((1, divergence(packet_current)),
                   (1, packet_residual)) == geo["packet"]
    eta_current = FORCING.absorption_current(geo["eta"])
    current = combine((1, inner_current), (-1, geo["K"]),
                      (-1, eta_current), (-1, packet_current))
    complement_residual = combine((-1, packet_residual))
    outer_residual = combine((1, complement_residual),
                             (-2, count(geo["N"] // 4)))
    assert combine((1, divergence(current)), (1, complement_residual)) == geo["complement"]
    assert combine((1, divergence(current)), (1, outer_residual)) == geo["outer"]
    return dict(current=current, complement_residual=complement_residual,
                outer_residual=outer_residual,
                complement_positive_budget=sum(complement_residual.values()),
                outer_positive_budget=sum(c for c in outer_residual.values() if c > 0))


def inspect_exposed(geo, extension):
    """Exact component counts using only nonzero rows of the converted current."""
    edges = {x: PACKETS.step(x) for x in extension["current"]}
    vertices = set(geo["complement"]) | set(extension["complement_residual"]) | {1}
    vertices.update(edges)
    vertices.update(edges.values())
    parent = {x: x for x in vertices}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for x, y in edges.items():
        parent[find(x)] = find(y)
    absorbed = find(1)
    missed_low = [x for x in count(geo["N"] // 4) if find(x) != absorbed]
    missed_outer = [x for x in geo["outer"] if find(x) != absorbed]
    actual_mass = 2 * len(missed_low) + len(missed_outer)
    unabsorbed_exit_mass = sum(c for x, c in extension["complement_residual"].items()
                              if find(x) != absorbed)
    assert actual_mass == unabsorbed_exit_mass <= extension["complement_positive_budget"]
    assert len(missed_outer) <= extension["outer_positive_budget"]
    certificate = None
    if not missed_outer:
        certificate = CURRENT.finite_certificate(geo["outer"], edges, 1, False)
        assert certificate is not None
        exact_current, residual = certificate
        assert not residual and min(exact_current.values()) >= 0
        assert set(exact_current) <= set(edges)
        assert divergence(exact_current) == geo["outer"]
    return dict(missed_low=missed_low, missed_outer=missed_outer,
                actual_weighted_unabsorbed=actual_mass,
                unabsorbed_exit_mass=unabsorbed_exit_mass,
                exposed_rows=len(edges), outer_certificate=certificate)
