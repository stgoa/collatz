"""A second prescribed forward block before requesting any pair inputs.

Every plan retains its signed W5 premises. Acceptance uses the existing rho
rank, not a newly assumed absorption current or an unrestricted orbit search.
"""
from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, relative):
    spec = spec_from_file_location(name, HERE.parent / relative)
    result = module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


OLD = load('continuation_returning', 'returning_phase/returning_phase.py')
RUN = load('continuation_run', 'complementary_bridge/run_bridge.py')
RANK = load('continuation_rank', 'critical_rank/rank_closure.py')
NORMAL, NINE, INVERSE, T = OLD.NORMAL, OLD.NINE, OLD.INVERSE, OLD.TRIPLING
combine, atoms, divergence, rho = OLD.combine, OLD.atoms, OLD.divergence, OLD.rho


def parameters(w):
    first = OLD.parameters(w)
    r = first['endpoint']
    normalization = NORMAL.bridge(r)
    n = normalization['minimum']
    if n == 1:
        second = dict(kind='absorber', root=n, target=n, current={}, quotient_length=0)
    elif n % 8 == 1:
        f = NORMAL.step(n)
        second = dict(kind='canonical_forward', root=n, target=f,
                      current={n: 1}, quotient_length=1)
    else:
        second = dict(RUN.bridge(n), kind='complete_run')
        second['quotient_length'] = second['a'] + second['d']//2 - 1
    f = second['target']
    bound = OLD.absorption_rank_bound(f)
    first_bound = OLD.absorption_rank_bound(r)['bound']
    return dict(seed=w, rank=rho(w), first=first, first_minimum=n,
                normalization=normalization, second=second, endpoint=f,
                minimum=NORMAL.normal_form(f), rank_bound=bound['bound'],
                bound_kind=bound['kind'],
                first_rejected=first_bound >= rho(w),
                quotient_length=first['a']-1+second['quotient_length'])


def continuation_plan(w):
    data = parameters(w)
    upper, lower = NORMAL.bridge(3*w), NORMAL.bridge(w)
    z = lower['minimum']
    high, low = RANK.absorption_plan(data['endpoint']), RANK.absorption_plan(z)
    current = combine((1, upper['current']), (1, data['first']['prefix']),
                      (1, data['normalization']['current']),
                      (1, data['second']['current']), (-1, lower['current']),
                      (1, high['current']), (-1, low['current']))
    coefficients = Counter(high['coefficients'])
    coefficients.subtract(low['coefficients'])
    coefficients = NINE.clean(coefficients)
    assert all(rho(u) <= data['rank_bound'] for u in high['coefficients'])
    assert all(8*rho(u) <= 9*z+5 < 8*data['rank'] for u in low['coefficients'])
    expected = T.pair_source(w)
    for u, c in coefficients.items():
        expected = combine((1, expected), (-c, T.pair_source(u)))
    assert divergence(current) == expected
    accepted = data['rank_bound'] < data['rank']
    result = dict(seed=w, rank=data['rank'], status='descending' if accepted else 'unresolved',
                  current=current, coefficients=coefficients, parameters=data,
                  input_rank_bound=[data['rank_bound'].numerator, data['rank_bound'].denominator])
    if accepted:
        RANK.validate_step(w, result)
    return result


def recognized(w):
    return OLD.returning(w) and parameters(w)['rank_bound'] < rho(w)


def compile_plan(plan, supplied):
    if plan['status'] != 'descending':
        raise ValueError('The second-block rank test remains unresolved')
    RANK.validate_step(plan['seed'], plan)
    return RANK.compile_plan(plan, supplied)


def low_exponent_domain(data):
    """Exact endpoint-bound classification on a=3 first failures, A=2,3,4."""
    first, second = data['first'], data['second']
    if (first['a'] != 3 or data['first_minimum'] != first['endpoint']
            or first['endpoint'] % 4 != 3 or second['kind'] != 'complete_run'):
        raise ValueError('Require a=3 and a complementary canonical first endpoint')
    A, d, f, n = second['a'], second['d'], data['endpoint'], data['minimum']
    if A not in (2, 3, 4):
        raise ValueError('The complete low-exponent table has A=2,3,4')
    selected = NORMAL.selected(f)
    if A == 2:
        return bool(d % 2 or d >= 4 or selected)
    if A == 3:
        return bool(d % 2 or d >= 8 or (selected and (d >= 4 or n % 8 != 3)))
    return bool(d % 2 or d >= 10 or (selected and (d >= 6 or (d == 4 and n % 8 == 1))))


def cell_family(a, A, d, index=0):
    """Exact CRT cell, retaining the entire original ternary phase."""
    if (not all(isinstance(x, int) for x in (a, A, d, index))
            or a < 3 or A < 2 or d < 2 or index < 0):
        raise ValueError('Require a>=3, A>=2, d>=2, and a nonnegative index')
    ternary = 3**(a+2)
    r_residue = ((10*3**(a-1)*pow(2**a, -1, ternary)-1)*pow(2, -1, ternary)) % ternary
    v_ternary = ((r_residue+1)*pow(2**A, -1, ternary)) % ternary
    binary = 2**(d+1)
    v_binary = ((1+2**d)*pow(3**(A-1), -1, binary)) % binary
    residue = v_binary + binary*((v_ternary-v_binary)*pow(binary, -1, ternary) % ternary)
    period = binary*ternary
    v = residue + period*index
    r = 2**A*v-1
    assert (2*r+1) % 3**(a-1) == 0
    t = (2*r+1)//3**(a-1)
    w = (2**a*t-1)//3
    data = parameters(w)
    assert data['first']['a'] == a and data['first']['endpoint'] == r
    assert data['first_minimum'] == r and data['first_rejected']
    assert data['second']['a'] == A and data['second']['d'] == d
    return dict(seed=w, a=a, A=A, d=d, index=index, v=v,
                v_residue=residue, v_period=period, endpoint=r,
                seed_residue=(2**a*((2*(2**A*residue-1)+1)//3**(a-1))-1)//3,
                seed_period=2**(a+A+1)*3**2*binary)


def long_family(a, A, index=0, d=None):
    """Complete newly accepted CRT families for every a>=3 and A>=2.

    The first endpoint is complementary canonical, so the old returning rule
    fails. A sufficiently long odd second valuation block makes the new bound
    strictly smaller than the original critical rank for every positive member.
    """
    if not all(isinstance(x, int) for x in (a, A, index)) or a < 3 or A < 2 or index < 0:
        raise ValueError('Require a>=3, A>=2, and a nonnegative index')

    def sufficient(value):
        return 7*3**(a+A+value//2-3) <= 2**(a+A+value-1)

    if d is None:
        d = 3
        while not sufficient(d):
            d += 2
    if not isinstance(d, int) or d < 3 or d % 2 == 0 or not sufficient(d):
        raise ValueError('Require an odd second depth satisfying the uniform slope bound')
    result = cell_family(a, A, d, index)
    data = parameters(result['seed'])
    r = result['endpoint']
    assert data['rank_bound'] < data['rank']
    c = Fraction(2**(a-1), 3**(a-1))
    slope = Fraction(3**(A-1+d//2), 2**(A+d))
    assert data['rank'] > c*r and Fraction(7, 3)*slope <= c
    assert data['rank_bound'] < Fraction(7, 3)*slope*r
    return result
