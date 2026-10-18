"""Exact fixed-word common-tail lifting and original-critical-rank currents.

The arithmetic family is complete for the two prescribed ordinary words.
Terminal pair currents remain supplied premises; no orbit search is used.
"""
from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, relative):
    spec = spec_from_file_location(name, HERE.parent/relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASIS = load('history_lift_basis', 'critical_basis/critical_basis.py')
N = BASIS.NORMAL
combine, divergence, atoms, rho = BASIS.combine, BASIS.divergence, BASIS.atoms, BASIS.rho
UPPER_WORD = (1, 2)
LOWER_WORD = (1,)*6+(2, 2)+(1,)*4+(2, 6)


def integer(x, minimum=None):
    return type(x) is int and (minimum is None or x >= minimum)


def affine(word):
    if not isinstance(word, (tuple, list)) or any(not integer(a, 1) for a in word):
        raise ValueError('Require a finite list of positive integer valuations')
    coefficient, constant, total = 1, 0, 0
    for a in word:
        coefficient, constant, total = 3*coefficient, 3*constant+2**total, total+a
    return dict(length=len(word), total=total, coefficient=coefficient, constant=constant)


def prefix(seed, word):
    if not integer(seed, 1) or seed % 2 != 1:
        raise ValueError('Require a positive odd integer seed')
    N._odd(seed)
    affine(word)
    x, current, states = seed, Counter(), [seed]
    for a in word:
        if N.valuation2(3*x+1) != a:
            raise ValueError('The prescribed exact ordinary valuation word fails')
        if x != 1:
            current[x] += 1
        x = N.step(x)
        states.append(x)
    current = combine((1, current))
    assert divergence(current) == atoms((1, seed), (-1, x))
    return dict(seed=seed, endpoint=x, current=current, states=states)


def make_spec(q0, p0, upper_word, lower_word):
    """Find the full integer solution cell, anchored at one exact merger."""
    left, right = prefix(q0, upper_word), prefix(p0, lower_word)
    if left['endpoint'] != right['endpoint']:
        raise ValueError('The designated exact prefixes do not have a common endpoint')
    a, b = affine(upper_word), affine(lower_word)
    M = 2**(a['total']+1)*3**max(b['length']-a['length'], 0)
    P = 2**(b['total']+1)*3**max(a['length']-b['length'], 0)
    positive_minimum = max(-((q0-1)//M), -((p0-1)//P))
    difference, slope_difference = q0-p0, M-P
    lower, upper = positive_minimum, None
    if slope_difference > 0:
        lower = max(lower, (-difference)//slope_difference+1)
    elif slope_difference == 0:
        if difference <= 0:
            upper = lower-1
    else:
        upper = (difference-1)//(-slope_difference)
    empty = upper is not None and upper < lower
    slope, intercept = Fraction(P, M), Fraction(p0)-Fraction(P*q0, M)
    return dict(q0=q0, p0=p0, upper_word=list(upper_word), lower_word=list(lower_word),
                upper_affine=a, lower_affine=b, q_period=M, p_period=P,
                slope=[slope.numerator, slope.denominator],
                intercept=[intercept.numerator, intercept.denominator],
                positive_index_minimum=positive_minimum,
                smaller_indices=dict(minimum=lower, maximum=upper, empty=empty),
                uniformly_smaller_for_nonnegative_indices=(p0 < q0 and P <= M))


def lift(spec, index):
    if not integer(index):
        raise ValueError('Require an integer cell index')
    exact = make_spec(spec['q0'], spec['p0'], spec['upper_word'], spec['lower_word'])
    if spec != exact:
        raise ValueError('Incorrect or incomplete lifting specification')
    q, p = spec['q0']+spec['q_period']*index, spec['p0']+spec['p_period']*index
    if min(q, p) <= 0:
        raise ValueError('Both lifted origins must be positive')
    left, right = prefix(q, spec['upper_word']), prefix(p, spec['lower_word'])
    assert left['endpoint'] == right['endpoint']
    current = combine((1, left['current']), (-1, right['current']))
    assert divergence(current) == atoms((1, q), (-1, p))
    return dict(index=index, q=q, p=p, current=current, upper=left, lower=right,
                ordinary_clocks=[len(spec['upper_word']), len(spec['lower_word'])],
                smaller=p < q)


def recover(spec, q):
    if not integer(q, 1) or q % 2 != 1:
        raise ValueError('Require a positive odd target')
    N._odd(q)
    difference = q-spec['q0']
    if difference % spec['q_period']:
        raise ValueError('Target is outside the complete common-tail cell')
    return lift(spec, difference//spec['q_period'])


def critical_plan(w, spec, index):
    if not integer(w, 1) or not BASIS.T.critical_domain(w):
        raise ValueError('Require a critical W5 or W9 pair input')
    data = lift(spec, index)
    q, p = data['q'], data['p']
    if rho(w) != q or not p < q:
        raise ValueError('Require a strictly smaller origin at the original critical rank')
    hp, hw = BASIS.absorption_plan(p), BASIS.absorption_plan(w)
    current = combine((1, N.bridge(3*w)['current']), (1, data['current']),
                      (1, hp['current']), (-1, hw['current']))
    coefficients = combine((1, hp['coefficients']), (-1, hw['coefficients']))
    out = dict(seed=w, rank=q, current=current, coefficients=coefficients,
               lift=data, status='descending', rule='fixed_word_history_lift')
    assert N.normal_form(w) < q and all(rho(v) < q for v in coefficients)
    BASIS.validate(out)
    return out


NATIVE = make_spec(11547, 11391, UPPER_WORD, LOWER_WORD)
assert NATIVE['q_period'] == 16*3**12 and NATIVE['p_period'] == 2**23


def native_family(index):
    if not integer(index, 0):
        raise ValueError('Require a nonnegative native cell index')
    data = lift(NATIVE, index)
    q, p = data['q'], data['p']
    b, y = q//3, (3*q+1)//2
    assert q % 48 == 27 and b % 16 == 9 and p < q
    assert all(N.canonical(x) for x in (q, p, y))
    assert N.normal_form(data['lower']['states'][13]) == y
    assert all(N.canonical(x) for x in data['lower']['states'][:13])
    assert max(data['lower']['states']) == 32*q+17
    assert data['upper']['endpoint'] == (9*q+5)//8 > q
    return dict(data, seed=b, quotient_clocks=[1, 13], quotient_meeting=y)


def native_plan(index):
    data = native_family(index)
    out = critical_plan(data['seed'], NATIVE, index)
    return dict(out, parameters=data)


def blocked_phase(index):
    data = native_family(index)
    q = data['q']
    D = N.valuation2(3*q-1)
    if index % 2:
        assert D >= 5
        return dict(index=index, d=D, blocked=False)
    assert D == 4
    Z = 6496+3**14*index
    h = N.valuation2(Z)
    unit = Z//2**h
    selected = unit % 4 == pow(3, h, 4)
    z = (3*q-1)//16
    assert Z == 3*z+1 and selected == (not N.canonical(3*z))
    return dict(index=index, d=D, h=h, unit=unit, blocked=selected)


def old_failure_phase(index):
    """Exact raw phase; only its critical f subdomain is a claimed old failure."""
    if not integer(index, 0) or index % 512:
        raise ValueError('Require index divisible by512')
    data = native_family(index)
    q = data['q']
    u, r, f = (3*q+3)//4, (6561*q+8965)//1024, (19683*q+27919)//4096
    assert blocked_phase(index)['blocked']
    assert N.valuation2(3*u+1) == 7 and r % 8 == 1
    assert f == 55495+2*3**21*(index//512) and f % 3 == 1
    critical = N.canonical(f) and f % 4 == 3
    v = (2*f+1)//3 if critical else None
    if critical:
        assert v % 8 == 5 and rho(v) == f > rho(u) > q
        assert BASIS.absorption_plan(r)['coefficients'][v] == 1
        assert BASIS.absorption_plan(f)['coefficients'][v] == 1
    return dict(index=index, returning=u, first_endpoint=r, second_endpoint=f,
                genuine_old_higher_request=critical, leading=v)


def compile_plan(plan, supplied):
    if plan.get('status') != 'descending':
        raise ValueError('Require a checked descending critical plan')
    BASIS.validate(plan)
    return BASIS.compile_plan(plan, supplied)
