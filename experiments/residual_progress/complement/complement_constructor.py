"""Improve an automatic packet input using its retained finite graph.

All absorption of the inner interval is supplied by the caller.  Construction
never exposes an arrow outside the supplied inner current and the explicit
K_N/current-core rows.  The nonnegative unresolved profile is returned whole.
"""

from collections import defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = spec_from_file_location("complement_local", HERE.parent / "closure/local_extension.py")
LOCAL = module_from_spec(spec)
spec.loader.exec_module(LOCAL)
combine, divergence = LOCAL.combine, LOCAL.divergence
step = LOCAL.PACKETS.step


def residual_profile(N):
    """Return uncompressed bad outer atoms, compression current, final profile."""
    if not isinstance(N, int) or N < 8 or N % 8:
        raise ValueError("N must be a positive multiple of 8")
    residual, transport = {}, {}
    for x in range(N + 1, 3 * N // 2, 2):
        if x % 12 == 3:
            residual[x] = 1
        elif x % 12 == 7:
            if 8 * x > 9 * N:
                residual[x] = 1
            elif x % 36 in (7, 19):
                residual[x] = 2
                predecessor = (4 * x - 1) // 3
                assert N < predecessor < 3 * N // 2
                assert step(predecessor) == x
                transport[predecessor] = 1
            else:
                assert x % 36 == 31
    uncompressed = combine((1, divergence(transport)), (1, residual))
    assert all(c == 1 for c in uncompressed.values())
    assert set(uncompressed) <= set(range(N + 1, 3 * N // 2, 2))
    return uncompressed, transport, residual


def strict_count(low, high, residue, modulus):
    """Count residue-class integers strictly between two Fraction endpoints."""
    # Every actual endpoint used below is either even or a multiple of 9,
    # and hence never belongs to its associated odd residue class.
    def floor(q):
        return q.numerator // q.denominator
    from fractions import Fraction
    lo, hi = Fraction(low), Fraction(high)
    # ceil((high-residue)/modulus)-floor((low-residue)/modulus)-1.
    q = (hi - residue) / modulus
    return -floor(-q) - floor((lo - residue) / modulus) - 1


def residual_mass_formula(N):
    from fractions import Fraction
    return (strict_count(N, Fraction(3 * N, 2), 3, 12)
            + strict_count(N, Fraction(3 * N, 2), 7, 12)
            - strict_count(N, Fraction(9 * N, 8), 31, 36)
            + strict_count(Fraction(4 * N, 3), Fraction(3 * N, 2), 9, 48)
            + strict_count(Fraction(4 * N, 3), Fraction(3 * N, 2), 25, 48))


def extract_exact(measure, edges):
    """Extract on a supplied graph, never by following a fresh arrow."""
    answer = LOCAL.CURRENT.finite_certificate(measure, edges, 1, False)
    if answer is None:
        raise ValueError("Supplied graph does not absorb the claimed source")
    current, residual = answer
    assert not residual and all(c > 0 for c in current.values())
    assert set(current) <= set(edges)
    assert divergence(current) == measure
    return current


def improve_packet(N, inner_current):
    """Return a strictly accounted partial extension from supplied inner paths.

    The output profile depends only on N.  The graph may absorb still more
    states; this constructor deliberately retains the whole arithmetic profile.
    """
    if any(not isinstance(x, int) or x <= 1 or not x % 2
           or not isinstance(c, (int, Fraction)) for x, c in inner_current.items()):
        raise ValueError("Inner-current rows must be positive odd states with exact rational coefficients")
    inner_current = {x: c for x, c in inner_current.items() if c}
    geo = LOCAL.geometry(N)
    if divergence(inner_current) != geo["inner"]:
        raise ValueError("The supplied current must exactly absorb I_N")
    automatic, _, eta_current = LOCAL.automatic_packet(geo, inner_current)
    assert set(geo["K"]) == set(range(3, 3 * N // 2, 2))
    edges = {x: step(x) for x in set(inner_current) | set(geo["K"]) | set(eta_current)}

    # This graph extraction is justified by F^k(y)=4F^(k-1)(y)+1:
    # the first lift above N/4 lies in the supplied inner interval, and
    # has the same successor as y.  K_N supplies row y.
    lower_current = extract_exact(LOCAL.count(N), edges)
    bad, transport, residual = residual_profile(N)
    good = combine((1, geo["outer"]), (-1, bad))
    assert all(c == 1 for c in good.values())
    absorbed_complement = combine((2, LOCAL.count(N // 4)), (1, good))
    known_current = extract_exact(absorbed_complement, edges)
    improved = combine((1, automatic), (-1, known_current), (-1, transport))
    assert combine((1, divergence(improved)), (-1, residual)) == geo["packet"]
    extension = combine((1, known_current), (1, transport))
    assert combine((1, divergence(extension)), (-2, LOCAL.count(N // 4)),
                   (1, residual)) == geo["outer"]
    assert set(improved) <= set(edges)
    return dict(N=N, packet_current=improved, packet_residual={x: -c for x, c in residual.items()},
                lower_current=lower_current, known_complement_current=known_current,
                extension_current=extension, compression_current=transport,
                unresolved_outer=bad, residual_profile=residual, guaranteed_outer=good,
                supplied_edges=edges, original_automatic_current=automatic)


def cutoff_components(N):
    """Independently classify the complete graph of arrows with x<3N/2."""
    edges = {x: step(x) for x in range(3, 3 * N // 2, 2)}
    vertices = set(edges) | set(edges.values()) | {1}
    parents = dict(zip(vertices, vertices))
    def root(x):
        while x != parents[x]:
            parents[x] = parents[parents[x]]
            x = parents[x]
        return x
    for x, y in edges.items():
        parents[root(x)] = root(y)
    known = {root(x) for x in range(1, N, 2)}
    bad_components = defaultdict(set)
    for x in vertices:
        r = root(x)
        if r not in known:
            bad_components[r].add(x)
    bad_outer = {x for group in bad_components.values() for x in group
                 if N < x < 3 * N // 2}
    return edges, sorted((tuple(sorted(v)) for v in bad_components.values())), bad_outer
