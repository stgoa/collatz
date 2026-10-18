"""Conditional tripling-current compilers, with explicit missing inputs.

The decreasing formal plans terminate.  This module does not supply or search
for the universal tripling currents needed to realize those plans.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('tripling_normal', HERE.parent / 'bridge_normal_form/normal_form.py')
NORMAL = module_from_spec(spec)
spec.loader.exec_module(NORMAL)
step, divergence = NORMAL.step, NORMAL.divergence


def combine(*terms):
    result = {}
    for coefficient, rows in terms:
        for x, value in rows.items():
            if x != 1:
                result[x] = result.get(x, 0) + coefficient*value
    return {x: value for x, value in sorted(result.items()) if value}


def atoms(*terms):
    return combine(*[(coefficient, {x: 1}) for coefficient, x in terms])


def pair_source(w):
    NORMAL._odd(w)
    return atoms((1, 3*w), (-1, w))


def critical(q):
    NORMAL._odd(q)
    return NORMAL.canonical(q) and q % 4 == 3 and q % 3 != 2


def critical_domain(w):
    NORMAL._odd(w)
    return w % 8 == 5 or w % 16 == 9


def critical_image(w):
    if not critical_domain(w):
        raise ValueError('Require w=5 modulo8 or9 modulo16')
    q = NORMAL.normal_form(3*w)
    assert critical(q) and w < q
    return q


def critical_inverse(q):
    if not critical(q):
        raise ValueError('Require a complementary canonical q not2 modulo3')
    w = q//3 if q % 3 == 0 else (2*q+1)//3
    assert critical_domain(w) and critical_image(w) == q
    return w


def static_step(x):
    """One decreasing step using elementary currents and one formal P input.

    Returns J, lower v and missing w with div J=[x]-[v]-P(w).
    If nu(x)=1, no P input is needed.
    """
    data = NORMAL.bridge(x)
    q, current = data['minimum'], data['current']
    if q == 1:
        return dict(seed=x, canonical=q, lower=1, pair=None,
                    branch='elementary', current=current)
    residue = q % 3
    if residue == 0:
        v, w, correction = q//3, q//3, {}
    elif residue == 1:
        v = w = (2*q+1)//3
        correction = combine((-1, NORMAL.bridge(2*q+1)['current']))
    else:
        w = (4*q+1)//3
        v = (2*q-1)//3
        assert NORMAL.selected(w) and NORMAL.normal_form(w) == v
        correction = combine((1, atoms((1, q), (-1, NORMAL.F(q)))),
                             (1, NORMAL.bridge(w)['current']))
    assert 0 < v < q and 3*(v-1) <= 2*(q-1)
    current = combine((1, current), (1, correction))
    expected = combine((1, atoms((1, x), (-1, v))), (-1, pair_source(w)))
    assert divergence(current) == expected
    return dict(seed=x, canonical=q, lower=v, pair=w,
                branch='static_'+str(residue), current=current)


def critical_step(x):
    """One induction step; only missing P inputs in the exact critical domain.

    Ordinary arrows and inverse arrows are permitted in this version.
    """
    data = NORMAL.bridge(x)
    q, current = data['minimum'], data['current']
    if q == 1:
        return dict(seed=x, canonical=q, lower=1, pair=None,
                    branch='elementary', current=current)
    if q % 8 == 1:
        v, w, branch = step(q), None, 'forward_descent'
        correction = {q: 1}
    elif q % 3 == 2:
        v, w, branch = (2*q-1)//3, None, 'inverse_descent'
        assert step(v) == q
        correction = {v: -1}
    else:
        v = w = critical_inverse(q)
        branch = 'critical_pair'
        correction = combine((-1, NORMAL.bridge(3*w)['current']))
    assert 0 < v < q
    current = combine((1, current), (1, correction))
    expected = atoms((1, x), (-1, v))
    if w is not None:
        expected = combine((1, expected), (-1, pair_source(w)))
    assert divergence(current) == expected
    return dict(seed=x, canonical=q, lower=v, pair=w,
                branch=branch, current=current)


def plan(x, mode='critical'):
    """Produce a finite formal plan, retaining every missing pair occurrence."""
    NORMAL._odd(x)
    if mode not in ('critical', 'static'):
        raise ValueError('Unknown plan mode')
    advance = critical_step if mode == 'critical' else static_step
    start, steps, current, pairs = x, [], {}, []
    while x != 1:
        row = advance(x)
        assert row['lower'] < x
        steps.append(row)
        current = combine((1, current), (1, row['current']))
        if row['pair'] is not None:
            pairs.append(row['pair'])
        x = row['lower']
    expected = atoms((1, start))
    for w in pairs:
        expected = combine((1, expected), (-1, pair_source(w)))
    assert divergence(current) == expected
    return dict(seed=start, mode=mode, steps=steps, pairs=pairs, current=current)


def compile_plan(data, supplied_pairs):
    """Substitute explicitly supplied exact pair currents; fail if any is absent.

    This does not call an absorption search. Missing or incorrect premises are
    errors, never accepted as hypothetical conclusions.
    """
    current = data['current']
    for w in data['pairs']:
        if w not in supplied_pairs:
            raise ValueError('Missing tripling current for '+str(w))
        supplied = supplied_pairs[w]
        if divergence(supplied) != pair_source(w):
            raise ValueError('Incorrect tripling current for '+str(w))
        current = combine((1, current), (1, supplied))
    assert divergence(current) == atoms((1, data['seed']))
    return current
