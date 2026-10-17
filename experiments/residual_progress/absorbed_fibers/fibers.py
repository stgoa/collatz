"""Exact counts and conditional certificates for the known elementary fibres.

The supplied lower current is an input. No universal absorption search is used.
"""

from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location("fibre_normal", HERE.parent / "bridge_normal_form/normal_form.py")
NORMAL = module_from_spec(spec)
spec.loader.exec_module(NORMAL)


def affine_level(s):
    if not isinstance(s, int) or s < 0:
        raise ValueError("Expected a nonnegative level")
    factor = 2**s
    offset = ((2 if s % 2 else 1)*factor - 1)//3
    return factor, offset


def known(x, N):
    return NORMAL.normal_form(x) <= N


def band_count(N, X):
    """Count odd x in [X,2X) with normal form at most N, exactly.

    There are O(log N) relevant levels, regardless of X>=N. Each uses
    O(log N) exact progression counts. Arithmetic bit cost depends on X.
    """
    if not isinstance(N, int) or not isinstance(X, int) or N < 8 or X < N:
        raise ValueError("Require integer X>=N>=8")
    lower_level = max(0, ((X-1)//(N+1)).bit_length()-1)
    upper_level = (2*X).bit_length()-1
    answer, terms = 0, []
    for s in range(lower_level, upper_level+1):
        factor, offset = affine_level(s)
        low = min(N, max(0, (X-1-offset)//factor))
        high = min(N, max(0, (2*X-1-offset)//factor))
        count = NORMAL.canonical_count(high)-NORMAL.canonical_count(low)
        assert count >= 0
        answer += count
        if count:
            terms.append((s, low, high, count))
    return answer, terms


def telescope_count(N, X):
    """Exact telescope proving the uniform O(log N) error bound.

    Returns B_N(X), K(N), and all nonzero signed level corrections.  The
    possible correction levels have a proved bounded exponent interval.
    """
    if not isinstance(N, int) or not isinstance(X, int) or N < 8 or X < N:
        raise ValueError("Require integer X>=N>=8")

    def A(s, t):
        factor, offset = affine_level(s)
        bound = min(N, max(0, (t-1-offset)//factor))
        return NORMAL.canonical_count(bound)

    lower = max(1, ((2*X)//(N+1)).bit_length()-1)
    upper = (2*X).bit_length()-1
    corrections = []
    for s in range(lower, upper+1):
        difference = A(s, 2*X)-A(s-1, X)
        assert abs(difference) <= 1
        if difference:
            assert 2*X < (N+1)*2**s and 2**s < 2*X
            corrections.append((s, difference))
    L = N.bit_length()-1
    assert len(corrections) <= L+1
    canonical = NORMAL.canonical_count(N)
    answer = canonical + sum(c for _, c in corrections)
    assert abs(answer-canonical) <= L+1
    assert abs(4*answer-N) <= 4*(2*L+3)
    return answer, canonical, corrections


def independent_band(N, X):
    """Enumerate the canonical bases and locate the first power of four.

    This independent finite check does not scan the possibly huge band.
    """
    states = []
    for q in range(1, N+1, 2):
        if not NORMAL.canonical(q):
            continue
        for base in (q, 2*q+1):
            ratio = (3*X+1 + 3*base)//(3*base+1)
            exponent = ((max(1, ratio)-1).bit_length()+1)//2
            x = NORMAL.F_power(base, exponent)
            assert x >= X
            assert exponent == 0 or NORMAL.F_power(base, exponent-1) < X
            if x < 2*X:
                states.append(x)
    assert len(states) == len(set(states))
    return sorted(states)


def _clean(current):
    return {x: c for x, c in current.items() if c and x != 1}


def _path_current(source, edges):
    current, seen, x = Counter(), set(), source
    while x != 1:
        if x in seen or x not in edges:
            raise ValueError("Supplied finite graph does not absorb the source")
        seen.add(x)
        current[x] += 1
        x = edges[x]
    return dict(current)


def certify(x, N, lower_current):
    """Certify one arbitrarily high member from an exact supplied U_N current."""
    expected = dict.fromkeys(range(3, N+1, 2), 1)
    if NORMAL.divergence(lower_current) != expected:
        raise ValueError("Supply an exact current for U_N")
    data = NORMAL.bridge(x)
    q = data["minimum"]
    if q > N:
        raise ValueError("The seed is outside the known elementary closure")
    lower_edges = {u: NORMAL.step(u) for u, c in lower_current.items() if c and u != 1}
    known_path = _path_current(q, lower_edges)
    signed = Counter(known_path)
    signed.update(data["current"])
    signed = _clean(signed)
    target = {} if x == 1 else {x: 1}
    assert NORMAL.divergence(signed) == target
    current = _path_current(x, {u: NORMAL.step(u) for u in signed})
    assert NORMAL.divergence(current) == target
    assert set(current) <= set(lower_edges) | set(data["current"])
    return dict(seed=x, minimum=q, current=current,
                bridge_rows=len(data["current"]),
                new_rows=sorted(set(current)-set(lower_edges)))
