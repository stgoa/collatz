"""Exact normalization of signed W5 frontiers under two proved pair bridges.

This is a finite algebraic compiler. Terminal requests remain mandatory inputs;
no orbit search, new dispatcher rule, or universal absorption is supplied.
"""
from collections import Counter


def w5(w):
    if not isinstance(w, int) or isinstance(w, bool) or w <= 0 or w % 8 != 5:
        raise ValueError('Require a positive integer pair index congruent to5 modulo8')


def step(x):
    if not isinstance(x, int) or x <= 0 or x % 2 != 1:
        raise ValueError('Require a positive odd integer')
    if x == 1:
        return 1
    n = 3*x+1
    return n // (n & -n)


def combine(*terms):
    out = Counter()
    for weight, data in terms:
        for x, c in data.items():
            out[x] += weight*c
    return {x: c for x, c in out.items() if c}


def atom(x):
    return {} if x == 1 else {x: 1}


def pair(w):
    w5(w)
    return {3*w: 1, w: -1}


def divergence(current):
    out = {}
    for x, c in current.items():
        if not isinstance(c, int) or isinstance(c, bool) or x == 1:
            raise ValueError('Require integer ordinary current rows away from1')
        out = combine((1, out), (c, atom(x)), (-c, atom(step(x))))
    return out


def source(coefficients):
    out = {}
    for w, c in coefficients.items():
        w5(w)
        if not isinstance(c, int) or isinstance(c, bool):
            raise ValueError('Require integer signed coefficients')
        out = combine((1, out), (c, pair(w)))
    return out


def bridge(w):
    """Return P(w)-P(child), or None at a terminal of these two rules."""
    w5(w)
    if w % 512 == 93:
        u = (9*w-5)//64
        positive = (3*w, 32*u+3, 48*u+5, u)
        negative = (3*u, w, (8*u+1)//3, 4*u+1)
        label = 'I'
        clocks = [[3, 1], [3, 1]]
    elif w % 2048 == 1285:
        c = (w-5)//256
        u = 9*c
        positive = (3*w, 1152*c+23, 1728*c+35, 2592*c+53, u)
        negative = (27*c, (81*c+1)//2, w, 48*c+1, 36*c+1)
        label = 'II'
        clocks = [[3, 1], [4, 2]]
    else:
        return None
    w5(u)
    assert 0 < u < w and 64*u <= 9*w
    current = combine((1, Counter(positive)), (-1, Counter(negative)))
    assert len(current) == (8 if label == 'I' else 10)
    assert divergence(current) == combine((1, pair(w)), (-1, pair(u)))
    return dict(seed=w, child=u, label=label, current=current,
                ordinary_clocks_lower_upper=clocks, common_padded_clocks=[4, 2])


def normalize_pair(w):
    w5(w)
    x, current, chain = w, {}, []
    while True:
        data = bridge(x)
        if data is None:
            break
        chain.append(data)
        current = combine((1, current), (1, data['current']))
        x = data['child']
    assert divergence(current) == combine((1, pair(w)), (-1, pair(x)))
    return dict(seed=w, terminal=x, current=current, chain=chain,
                common_padded_clocks=[2*len(chain)+2, 2] if chain else [0, 0])


def potential(coefficients):
    source(coefficients)
    return sum(w*abs(c) for w, c in coefficients.items())


def normalize(coefficients):
    """Linear signed normalization; cancellation occurs only at equal terminals."""
    initial = combine((1, coefficients))
    original_source = source(initial)
    current, residual, chains = {}, {}, {}
    for w, c in sorted(initial.items()):
        data = normalize_pair(w)
        current = combine((1, current), (c, data['current']))
        residual = combine((1, residual), (c, {data['terminal']: 1}))
        chains[w] = [part['label'] for part in data['chain']]
    assert divergence(current) == combine((1, original_source), (-1, source(residual)))
    assert all(bridge(w) is None for w in residual)
    assert potential(residual) <= potential(initial)
    return dict(original=initial, current=current, coefficients=residual, chains=chains)


def compile_frontier(data, supplied):
    """Require and verify every nonzero terminal pair, including negative ones."""
    expected = combine((1, source(data['original'])), (-1, source(data['coefficients'])))
    if divergence(data['current']) != expected:
        raise ValueError('Incorrect normalization boundary')
    current = data['current']
    for w, c in data['coefficients'].items():
        if w not in supplied or divergence(supplied[w]) != pair(w):
            raise ValueError('Missing or incorrect exact terminal pair current')
        current = combine((1, current), (c, supplied[w]))
    assert divergence(current) == source(data['original'])
    return current


def inverse_word(labels, index=0):
    """Complete positive CRT family realizing any finite word of inverse lifts.

    Labels are read from the small child outward; every index gives all listed
    bridges. The initial small child may itself be reducible.
    """
    if not isinstance(index, int) or index < 0 or any(x not in ('I', 'II') for x in labels):
        raise ValueError('Require a finite I/II word and a nonnegative index')
    A, B, den = 1, 0, 1
    for label in labels:
        a, b = (64, 5) if label == 'I' else (256, 45)
        A, B, den = a*A, a*B+b*den, 9*den
    residue = (-B*pow(A, -1, den)) % den if den > 1 else 0
    child = residue+den*((5-residue)*pow(den, -1, 8) % 8)+8*den*index
    assert child > 0
    states = [child]
    for label in labels:
        x = (64*states[-1]+5)//9 if label == 'I' else (256*states[-1]+45)//9
        data = bridge(x)
        assert data and data['label'] == label and data['child'] == states[-1]
        states.append(x)
    return dict(seed=states[-1], child=child, states=states, labels=list(labels),
                child_period=8*den, child_residue=child-8*den*index)
