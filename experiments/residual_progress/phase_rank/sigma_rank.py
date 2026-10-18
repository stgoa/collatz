"""A separate rank for W5 currents that absorbs the W9 d4 expansion.

This rank is not interchangeable with rho. All returned accepted plans
are checked with sigma, and unrecognized inputs remain supplied premises.
"""
from collections import Counter
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'double_inverse'))
import expanded_union as OLD

RANK, NORMAL, T = OLD.RANK, OLD.RANK.NORMAL, OLD.RANK.T
RETURN, FORWARD = OLD.OLD.RETURN, OLD.FORWARD
combine, atoms, divergence = T.combine, T.atoms, T.divergence


def sigma(w):
    q = RANK.rho(w)
    if w % 8 != 5:
        raise ValueError('The sigma rank is defined on W5')
    result = 4*w//3-1 if RETURN.returning(w) else q
    assert w < result <= q
    return result


def absorption_plan(seed):
    data = RANK.absorption_plan(seed)
    n = NORMAL.normal_form(seed)
    assert all(sigma(u) <= n for u in data['coefficients'])
    return data


def endpoint_bound(seed):
    """Integer upper bound on every sigma rank in the unchanged H_seed."""
    n = NORMAL.normal_form(seed)
    if n == 1:
        bound, kind = 0, 'absorber'
    elif n % 8 == 1:
        bound, kind = (3*n+1)//4, 'forward'
    elif n % 3 == 2:
        bound, kind = (2*n-1)//3, 'inverse'
    else:
        w = T.critical_inverse(n)
        bound, kind = (sigma(w), 'critical_five') if w % 8 == 5 else (n, 'critical_nine')
    return dict(minimum=n, bound=bound, kind=kind)


def validate(w, data):
    if data.get('seed') != w:
        raise ValueError('Mismatched pair seed')
    rank = sigma(w)
    expected = T.pair_source(w)
    for u, c in data['coefficients'].items():
        if not isinstance(c, int) or not c or sigma(u) >= rank:
            raise ValueError('Require nonzero integer requests of smaller sigma rank')
        expected = combine((1, expected), (-c, T.pair_source(u)))
    for x, c in data['current'].items():
        if not isinstance(x, int) or x <= 1 or x % 2 == 0 or not isinstance(c, int):
            raise ValueError('Require integer current rows on positive odd nonabsorbing states')
    if divergence(data['current']) != expected:
        raise ValueError('Incorrect pair boundary')
    return data


def forward_plan(w):
    if RETURN.returning(w):
        old = RETURN.forward_plan(w)
    elif FORWARD.eligible(w):
        old = FORWARD.forward_plan(w)
    else:
        raise ValueError('Require returning or nonselected W5 input')
    endpoint = old['parameters']['endpoint']
    bound = endpoint_bound(endpoint)
    assert all(sigma(u) <= bound['bound'] for u in absorption_plan(endpoint)['coefficients'])
    accepted = bound['bound'] < sigma(w)
    data = dict(old, rho_rank=RANK.rho(w), rank=sigma(w), rank_name='sigma',
                rho_status=old['status'], status='descending' if accepted else 'unresolved',
                sigma_bound=bound)
    if accepted:
        validate(w, data)
    return data


def one_step(w):
    """A sigma-compatible union; it does not preserve all rho-only R44 cases."""
    sigma(w)
    if not RETURN.returning(w):
        data = OLD.one_step(w)
        if data is not None:
            validate(w, data)
            return dict(data, rank=sigma(w), rank_name='sigma')
    if RETURN.returning(w) or FORWARD.eligible(w):
        data = forward_plan(w)
        if data['status'] == 'descending':
            return dict(data, rule='R51_sigma_forward')
    return None


def close(w, max_nodes=None):
    """Finite conditional expansion using sigma on every edge."""
    sigma(w)
    memo, expanded = {}, set()
    def visit(v):
        if v in memo:
            return memo[v]
        if max_nodes is not None and len(memo)+len(expanded) >= max_nodes:
            raise RuntimeError('Conditional plan resource cap reached')
        data = one_step(v)
        if data is None:
            out = dict(current={}, coefficients={v:1})
        else:
            validate(v, data)
            expanded.add(v)
            current, coefficients = data['current'], Counter()
            for u, c in data['coefficients'].items():
                child = visit(u)
                current = combine((1,current), (c,child['current']))
                for leaf, value in child['coefficients'].items():
                    coefficients[leaf] += c*value
            out = dict(current=current, coefficients={u:c for u,c in sorted(coefficients.items()) if c})
        memo[v] = out
        return out
    result = dict(visit(w), seed=w, rank=sigma(w), rank_name='sigma', expanded=sorted(expanded))
    if expanded:
        validate(w, result)
    return result


def compile_plan(data, supplied):
    if data.get('rank_name') != 'sigma':
        raise ValueError('Require a sigma plan')
    validate(data['seed'], data)
    return RANK.NINE.compile_five_plan(data, supplied)


def fifth_exponent_family(index=0):
    if not isinstance(index,int) or index < 0:
        raise ValueError('Require a nonnegative progression index')
    w = 437+512*index
    data = FORWARD.parameters(w)
    assert (data['a'],data['d']) == (5,3)
    assert data['endpoint'] < 3*w
    return dict(seed=w, residue=437, period=512, parameters=data)
