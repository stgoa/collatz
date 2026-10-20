"""Finite graph compiler for elementary-plus-forward known saturation.

No unknown orbit is followed. A supplied current supplies finite paths; the
compiled core has exactly two ordinary Syracuse vertices per canonical base.
"""

from bisect import bisect_right
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location("saturation_normal", HERE.parent / "bridge_normal_form/normal_form.py")
NORMAL = module_from_spec(spec)
spec.loader.exec_module(NORMAL)
step, divergence = NORMAL.step, NORMAL.divergence


def clean(current):
    return {x: c for x, c in sorted(current.items()) if x != 1 and c}


def supplied_path(seed, edges):
    """Read a path entirely in the supplied finite graph, with cycle checking."""
    path, seen, x = [seed], set(), seed
    while x != 1:
        if x in seen or x not in edges:
            raise ValueError("The supplied finite graph does not absorb the seed")
        seen.add(x)
        x = edges[x]
        path.append(x)
    return path


def graph_depths(edges):
    """Verify finite forward closure and absorption, and return exact depths."""
    if edges.get(1) != 1 or not set(edges.values()) <= set(edges):
        raise ValueError("Supply a closed finite graph with absorbing vertex1")
    depths = {1: 0}
    for start in sorted(edges):
        path, seen, x = [], set(), start
        while x not in depths:
            if x in seen:
                raise ValueError("A nonabsorbing cycle is present")
            seen.add(x)
            path.append(x)
            x = edges[x]
        depth = depths[x]
        for x in reversed(path):
            depth += 1
            depths[x] = depth
    return depths


def compile_core(canonical_bases):
    """Compile any finite absorbing T-closed base set into its ordinary-S core."""
    Q = set(canonical_bases)
    if not Q or any(not NORMAL.canonical(q) for q in Q):
        raise ValueError("Supply a nonempty set of canonical bases")
    quotient_edges = {q: NORMAL.quotient_step(q) for q in Q}
    quotient_depths = graph_depths(quotient_edges)
    W = {step(q) for q in Q} | {3*q+2 for q in Q}
    assert len(W) == 2*len(Q)
    ordinary_edges = {w: step(w) for w in W}
    assert set(ordinary_edges.values()) <= W
    ordinary_depths = graph_depths(ordinary_edges)
    assert max(W) == 3*max(Q)+2
    return dict(bases=sorted(Q), quotient_edges=quotient_edges,
                quotient_depths=quotient_depths, core_vertices=sorted(W),
                core_edges=ordinary_edges, core_depths=ordinary_depths)


def from_lower_current(N, lower_current):
    """Recover the intrinsic saturated quotient and exact minimum input origins.

    Extra rows of an exact signed input are not treated as known absorption.
    Only paths from the requested U_N source are used.
    """
    if not isinstance(N, int) or N < 1:
        raise ValueError("Expected a positive integer cutoff")
    expected = dict.fromkeys(range(3, N+1, 2), 1)
    if divergence(lower_current) != expected:
        raise ValueError("Supply a finite exact current for U_N")
    edges = {x: step(x) for x, c in lower_current.items() if c and x != 1}
    raw_states, witnesses = {1}, {}
    for seed in range(1, N+1, 2):
        path = supplied_path(seed, edges)
        raw_states.update(path)
        if not NORMAL.canonical(seed):
            continue
        for k, y in enumerate(path):
            q = NORMAL.normal_form(y)
            candidate = dict(origin=seed, step=k, state=y)
            if q not in witnesses or (seed, k) < (witnesses[q]["origin"], witnesses[q]["step"]):
                witnesses[q] = candidate
    Q = set(witnesses)
    assert Q == {NORMAL.normal_form(y) for y in raw_states}
    core = compile_core(Q)
    for q, following in core["quotient_edges"].items():
        assert witnesses[following]["origin"] <= witnesses[q]["origin"]
    core.update(N=N, origins=witnesses, raw_known_states=sorted(raw_states),
                input_rows=len(edges))
    return core


def threshold_bases(saturation, cutoff):
    """The exact smaller-cutoff quotient, from the stored minimum-origin labels."""
    if not isinstance(cutoff, int) or cutoff < 1 or cutoff > saturation["N"]:
        raise ValueError("Cutoff must lie between1 and the supplied input cutoff")
    return sorted(q for q, witness in saturation["origins"].items()
                  if witness["origin"] <= cutoff)


def certify_member(x, core, weight=1):
    """One arbitrary-height member, using one arrow and the finite core table."""
    if not isinstance(weight, int) or weight <= 0:
        raise ValueError("Expected a positive integer source multiplicity")
    q = NORMAL.normal_form(x)
    if q not in core["quotient_edges"]:
        raise ValueError("Seed is outside this elementary-forward saturation")
    edges = core["core_edges"]
    if x == 1:
        path = [1]
    else:
        successor = step(x)
        assert successor in edges
        path = [x] + supplied_path(successor, edges)
    current = clean(Counter({y: weight for y in path[:-1]}))
    assert len(path)-1 <= 2*len(core["bases"])
    assert len(path) == len(set(path))
    assert divergence(current) == ({} if x == 1 else {x: weight})
    return dict(seed=x, minimum=q, weight=weight, path=path, current=current)


def certify_via_bridge(x, target, bridge_current, core, weight=1):
    """Accept any checked finite bridge into the compiled saturation.

    This is the reusable interface for an R26 return or another exact local
    construction. All signed rows are retained before finite graph extraction.
    """
    expected = Counter({x: 1})
    expected[target] -= 1
    if divergence(bridge_current) != clean(expected):
        raise ValueError("Bridge must have divergence delta_x-delta_target")
    known = certify_member(target, core)
    signed = Counter(bridge_current)
    signed.update(known["current"])
    signed = clean(signed)
    assert divergence(signed) == ({} if x == 1 else {x: 1})
    path = supplied_path(x, {y: step(y) for y in signed})
    if not isinstance(weight, int) or weight <= 0:
        raise ValueError("Expected a positive integer source multiplicity")
    current = clean(Counter({y: weight for y in path[:-1]}))
    assert divergence(current) == ({} if x == 1 else {x: weight})
    return dict(seed=x, target=target, weight=weight, path=path, current=current)


def _counting_data(bases):
    if isinstance(bases, dict):
        weights = {q: c for q, c in bases.items() if c}
        if any(not isinstance(c, int) for c in weights.values()):
            raise ValueError("Expected integer weights")
    else:
        weights = dict.fromkeys(bases, 1)
    if not weights or any(not NORMAL.canonical(q) for q in weights):
        raise ValueError("Supply a nonempty weighted canonical set")
    points, sums = sorted(weights), [0]
    for q in points:
        sums.append(sums[-1]+weights[q])

    def count(t):
        return sums[bisect_right(points, t)]

    return weights, points[-1], count


def affine_level(s):
    factor = 2**s
    return factor, ((2 if s % 2 else 1)*factor-1)//3


def band_count(bases, X):
    """Exact weighted count for any finite canonical set; closure is unnecessary."""
    weights, M, K = _counting_data(bases)
    if not isinstance(X, int) or X < M:
        raise ValueError("Require integer X>=max(bases)")
    lower = max(0, ((X-1)//(M+1)).bit_length()-1)
    upper = (2*X).bit_length()-1
    answer, terms = 0, []
    for s in range(lower, upper+1):
        scale, offset = affine_level(s)
        low = (X-1-offset)//scale
        high = (2*X-1-offset)//scale
        mass = K(high)-K(low)
        answer += mass
        if mass:
            terms.append((s, low, high, mass))
    return answer, terms


def telescope_count(bases, X):
    weights, M, K = _counting_data(bases)
    if not isinstance(X, int) or X < M:
        raise ValueError("Require integer X>=max(bases)")

    def A(s, t):
        scale, offset = affine_level(s)
        return K((t-1-offset)//scale)

    corrections = []
    lower = max(1, ((2*X)//(M+1)).bit_length()-1)
    upper = (2*X).bit_length()-1
    max_weight = max(abs(c) for c in weights.values())
    for s in range(lower, upper+1):
        difference = A(s, 2*X)-A(s-1, X)
        assert abs(difference) <= max_weight
        if difference:
            assert 2*X < (M+1)*2**s and 2**s < 2*X
            corrections.append((s, difference))
    L = M.bit_length()-1
    assert len(corrections) <= L+1
    total = sum(weights.values())
    answer = total+sum(c for _, c in corrections)
    assert abs(answer-total) <= (L+1)*max_weight
    return answer, corrections
