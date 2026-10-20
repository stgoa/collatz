"""Transfer checked partial annular currents to exact complement currents."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = spec_from_file_location(name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


COMPLEMENT = load("transfer_complement", HERE.parent / "complement/complement_constructor.py")
PACKING = load("transfer_packing", HERE.parent / "release_packing/release_packing.py")
RELEASE = load("transfer_release", HERE.parent / "release/check_release.py")
LOCAL = COMPLEMENT.LOCAL
step, divergence, combine = COMPLEMENT.step, LOCAL.divergence, LOCAL.combine


def residual_coefficient(N, x):
    """Point evaluation, including the full coefficient2 profile."""
    if not N < x < 3 * N // 2:
        return 0
    if x % 12 == 3:
        return 1
    if x % 12 != 7:
        return 0
    if 8 * x > 9 * N:
        return 1
    return 2 if x % 36 in (7, 19) else 0


def positive_ancestor(N, y):
    """The exact <=2-arrow ancestor certificate for an A_(N/64) positive."""
    if y <= N:
        path = [y]
    elif 8 * y < 9 * N:
        if y % 18 in (11, 17):
            path = [(2 * y - 1) // 3, y]
        else:
            assert y % 18 == 13
            path = [(8 * y - 5) // 9, (4 * y - 1) // 3, y]
    else:
        assert y % 18 == 17
        path = [(4 * y - 5) // 9, (2 * y - 1) // 3, y]
    assert 1 < path[0] <= N
    assert all(x % 2 for x in path)
    assert all(step(a) == b for a, b in zip(path, path[1:]))
    return path


def transfer_block(M, source, current, lower_current):
    """Certify selected R_(64M) atoms from a supplied capacity-checked block.

    No input is discovered here. Positive atoms are absorbed on lower_current's
    existing graph. The signed difference current then certifies negative atoms,
    and actual integral path currents are extracted on its finite graph.
    """
    if not isinstance(M, int) or M < 8 or M % 8:
        raise ValueError("M must be a positive multiple of8")
    N = 64 * M
    source, current = ({x: c for x, c in table.items() if c}
                       for table in (source, current))
    assert divergence(current) == source
    assert divergence(lower_current) == LOCAL.count(N)
    for x, c in source.items():
        a = PACKING.OLD.COMPILER.coefficient_at(M, x)
        assert (0 < c <= a) or (a <= c < 0), "Annular source capacity violated"
    positive = {x: c for x, c in source.items() if c > 0}
    negative = {x: -c for x, c in source.items() if c < 0}
    lower_edges = {x: step(x) for x, c in lower_current.items() if c}
    for y in positive:
        path = positive_ancestor(N, y)
        assert all(lower_edges.get(x) == z for x, z in zip(path, path[1:]))
    positive_current = COMPLEMENT.extract_exact(positive, lower_edges)
    signed_negative_current = combine((1, positive_current), (-1, current))
    assert divergence(signed_negative_current) == negative
    negative_edges = {x: step(x) for x in signed_negative_current}
    negative_current = COMPLEMENT.extract_exact(negative, negative_edges)

    target = {}
    for t in negative:
        if t % 3 != 2:
            continue
        x = (2 * t - 1) // 3
        c = residual_coefficient(N, x)
        if c:
            assert step(x) == t
            target[x] = c
    edges = {x: step(x) for x in negative_current}
    edges.update({x: step(x) for x in target})
    target_current = COMPLEMENT.extract_exact(target, edges)
    assert set(target_current) <= set(lower_edges) | set(current) | set(target)
    return dict(M=M, N=N, target=target, current=target_current,
                negative_source_current=negative_current,
                signed_negative_current=signed_negative_current,
                positive_source_current=positive_current)


def old_packing_roots(M):
    """All roots expected from the old two-class five-source packing."""
    roots = []
    for residue in (0, 3):
        for s in PACKING.OLD.COMPILER.family_indices(M, residue):
            j = 9 * s + residue
            roots.append(9183 + 768 * j)
    assert len(roots) == len(set(roots))
    return sorted(roots)


def delayed_descent(parameters, X):
    """Return the exact first-descent path of a remaining root, without a scan."""
    family = RELEASE.construct(parameters, X)
    M, N = family["N"], 64 * family["N"]
    x = family["zero_source_intermediate"]
    path = [x, *family["path_v_to_y1"]]
    h, r = parameters["h"], parameters["r"]
    assert residual_coefficient(N, x) == 1 and x % 36 == 31
    assert 8 * x > 9 * N and 2 * x < 3 * N
    assert path[-1] == N - 1 and all(y > N for y in path[:-1])
    assert len(path) - 1 == h + r + 2 <= 2 * h + 2
    assert all(step(a) == b for a, b in zip(path, path[1:]))
    assert len(set(path)) == len(path)
    current = dict.fromkeys(path[:-1], 1)
    assert divergence(current) == {x: 1, N - 1: -1}
    assert max(path) * 3**h > N * 4**h
    return dict(M=M, N=N, root=x, endpoint=N - 1, current=current, path=path,
                h=h, r=r, first_descent_length=h + r + 2,
                residual_weight=1, exposure_is_explicit=True)


def delayed_companion(parameters, X):
    """The other negative exit may certify one or two residual source units."""
    first = delayed_descent(parameters, X)
    t, v = first["path"][:2]
    u = (8 * v - 7) // 9
    x = (2 * u - 1) // 3
    N = first["N"]
    weight = residual_coefficient(N, x)
    if not weight:
        return None
    path = [x, u, *first["path"]]
    assert all(step(a) == b for a, b in zip(path, path[1:]))
    assert len(set(path)) == len(path)
    assert all(y > N for y in path[:-1]) and path[-1] == N - 1
    current = dict.fromkeys(path[:-1], weight)
    assert divergence(current) == {x: weight, N - 1: -weight}
    return dict(M=first["M"], N=N, root=x, endpoint=N - 1,
                current=current, path=path, h=first["h"], r=first["r"],
                first_descent_length=len(path) - 1, residual_weight=weight,
                exposure_is_explicit=True)
