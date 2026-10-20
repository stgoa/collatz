"""Critical-image rank and finite signed closure of supplied decreasing rules.

No unknown orbit or missing pair current is searched. Unhandled pairs remain
explicit premises. A rule may increase its pair index if its critical image
strictly decreases; a self-request or malformed rule is rejected.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('rank_inverse', HERE.parent/'critical_inverse/critical_inverse.py')
INVERSE = module_from_spec(spec)
spec.loader.exec_module(INVERSE)
NINE, T = INVERSE.NINE, INVERSE.T
NORMAL = T.NORMAL
combine, atoms, divergence = T.combine, T.atoms, T.divergence


def rho(w):
    """Positive integer rank of a critical pair, rho(w)=nu(3w)."""
    return T.critical_image(w)


def nine_plan(w):
    """Eliminate W9, checking the critical-image bound (27w+5)/8."""
    if w % 16 != 9:
        raise ValueError('Require a positive critical-nine index')
    data = NINE.five_plan(w)
    assert all(8*rho(u) <= 27*w+5 for u in data['coefficients'])
    return data


def absorption_plan(seed):
    """Formal H_seed with every missing W5 critical image <=(9seed+5)/8."""
    data = INVERSE.absorption_five_plan(seed)
    assert all(8*rho(u) <= 9*seed+5 for u in data['coefficients'])
    return data


def validate_step(w, data):
    """Check exact signed divergence and strict critical-image decrease."""
    if w % 8 != 5 or data.get('seed') != w:
        raise ValueError('Require a matching positive W5 seed')
    rank = rho(w)
    current, coefficients = data['current'], data['coefficients']
    for u, c in coefficients.items():
        if not isinstance(u, int) or not isinstance(c, int) or c == 0 or u % 8 != 5:
            raise ValueError('Require nonzero signed integer W5 requests')
        if rho(u) >= rank:
            raise ValueError('The rule does not strictly decrease its critical image')
    if any(not isinstance(x, int) or not isinstance(c, int) for x, c in current.items()):
        raise ValueError('Require an integer current')
    expected = T.pair_source(w)
    for u, c in coefficients.items():
        expected = combine((1, expected), (-c, T.pair_source(u)))
    if divergence(current) != expected:
        raise ValueError('Incorrect formal pair boundary')
    return data


def close_plan(w, one_step, max_nodes=None):
    """Compose any finite-branching family of strict-rho rules.

    one_step(w) returns None for an unresolved premise or a dict with seed,
    current and coefficients. The whole plan remains conditional on its leaves.
    A caller's resource cap rejects computation, never certifies a missing leaf.
    """
    if not isinstance(w, int) or w <= 0 or w % 8 != 5:
        raise ValueError('Require a positive W5 seed')
    memo, steps, leaves = {}, {}, set()

    def visit(x):
        if x in memo:
            return memo[x]
        if max_nodes is not None and len(steps)+len(leaves) >= max_nodes:
            raise RuntimeError('Conditional-plan resource cap reached')
        data = one_step(x)
        if data is None:
            leaves.add(x)
            answer = dict(current={}, coefficients={x: 1})
        else:
            validate_step(x, data)
            steps[x] = data
            current, coefficients = data['current'], Counter()
            for u, c in data['coefficients'].items():
                child = visit(u)
                current = combine((1, current), (c, child['current']))
                for v, value in child['coefficients'].items():
                    coefficients[v] += c*value
            answer = dict(current=current, coefficients=NINE.clean(coefficients))
        memo[x] = answer
        return answer

    answer = visit(w)
    expected = T.pair_source(w)
    for u, c in answer['coefficients'].items():
        expected = combine((1, expected), (-c, T.pair_source(u)))
    assert divergence(answer['current']) == expected
    return dict(seed=w, rank=rho(w), current=answer['current'],
                coefficients=answer['coefficients'], expanded=sorted(steps),
                unresolved=sorted(answer['coefficients']))


def compile_plan(data, supplied):
    """Substitute exact supplied leaf currents; no current discovery occurs."""
    return NINE.compile_five_plan(data, supplied)
