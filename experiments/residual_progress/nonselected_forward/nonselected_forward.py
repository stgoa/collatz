"""Whole two-run forward interface for nonselected critical-five pairs.

All plans retain signed missing premises. Acceptance uses a proved strict
critical-image rank bound; it never supplies an unknown absorption current.
"""
from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name, relative):
    spec = spec_from_file_location(name,HERE.parent/relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


OLD = _load('nonselected_forward_old','returning_phase/returning_phase.py')
RUN = _load('nonselected_forward_run','complementary_bridge/run_bridge.py')
ESCAPE = _load('nonselected_forward_escape','inverse_escape/inverse_escape.py')
NORMAL, INVERSE, NINE, T = OLD.NORMAL, OLD.INVERSE, OLD.NINE, OLD.TRIPLING
combine, atoms, divergence, rho = OLD.combine, OLD.atoms, OLD.divergence, OLD.rho


def eligible(w):
    NORMAL._odd(w)
    return w % 8 == 5 and not NORMAL.selected(3*w)


def parameters(w):
    if not eligible(w):
        raise ValueError('Require a W5 pair with nonselected3w')
    q = 3*w
    a,t,d,u = RUN.parameters(q)
    f = RUN.target(q)
    assert a >= 3 and t % 4 == -3**a % 4
    assert (2**a*t-1) % 3 == 0 and t % 3
    assert (w % 3 == 0) == ((2**a*t-1) % 9 == 0)
    assert u % 3 == (1 if d % 2 else 2)
    assert f % 3 == (0 if d % 2 else 1)
    n = NORMAL.normal_form(f)
    return dict(seed=w,rank=q,a=a,t=t,d=d,unit=u,endpoint=f,minimum=n,
                quotient_length=a+d//2-1,
                ordinary_left_length=a+(d-1)//2 if d % 2 else a+d//2-1,
                ordinary_right_length=1 if d % 2 else 0)


def small_exponent_domain(data):
    """Exact classification of the endpoint-bound test at a=3 and a=4."""
    a,d,f,n = data['a'],data['d'],data['endpoint'],data['minimum']
    if a not in (3,4):
        raise ValueError('This complete table is for a=3 or4')
    if d % 2:
        return True
    selected = NORMAL.selected(f)
    if a == 3:
        return d >= 6 or selected
    return d >= 10 or (selected and (d >= 6 or (d == 4 and n % 8 != 3)))


def stratum_test(data, forward=False):
    """Exact sufficient inequality on each complete elementary endpoint stratum."""
    a,t,d = data['a'],data['t'],data['d']
    f = data['endpoint']
    norm = NORMAL.normalization(f)
    k,partner,n = norm['F_exponent'],norm['selected_partner'],norm['minimum']
    scale = 4**k*(2 if partner else 1)
    offset = (4**(k+1)-1)//3 if partner else (4**k-1)//3
    assert f == scale*n+offset
    b = d//2
    multiplier, epsilon = (1,0) if d % 2 else (2,1)
    A, C = multiplier*3**(a-1+b),multiplier*3**b
    if forward:
        if n <= 1 or n % 8 != 1:
            raise ValueError('Require a nonabsorbing1-modulo8 canonical minimum')
        lhs = 2**(a+d+5)*scale-27*A
        rhs = 61*2**d*scale+27*2**d*(epsilon-offset)-27*C
        bound = Fraction(27*n+29,32)
    else:
        lhs = 2**(a+d+3)*scale-9*A
        rhs = 13*2**d*scale+9*2**d*(epsilon-offset)-9*C
        bound = Fraction(9*n+5,8)
    assert (lhs*t > rhs) == (bound < data['rank'])
    return dict(scale=scale,offset=offset,F_exponent=k,selected_partner=partner,
                slope_difference=lhs,intercept=rhs,accepted=lhs*t>rhs,
                bound=[bound.numerator,bound.denominator])


def forward_plan(w):
    data = parameters(w)
    bridge = RUN.bridge(data['rank'])
    f = data['endpoint']
    lower_bridge = NORMAL.bridge(w)
    z = lower_bridge['minimum']
    high,low = INVERSE.absorption_five_plan(f),INVERSE.absorption_five_plan(z)
    current = combine((1,bridge['current']),(-1,lower_bridge['current']),
                      (1,high['current']),(-1,low['current']))
    coefficients = Counter(high['coefficients'])
    coefficients.subtract(low['coefficients'])
    coefficients = NINE.clean(coefficients)
    bound_data = OLD.absorption_rank_bound(f)
    bound,rank = bound_data['bound'],data['rank']
    assert all(rho(u) <= bound for u in high['coefficients'])
    assert 4*z <= w-1
    assert all(8*rho(u) <= 9*z+5 < 8*rank for u in low['coefficients'])
    accepted = bound < rank
    if data['a'] in (3,4):
        assert accepted == small_exponent_domain(data)
    if accepted:
        assert all(u % 8 == 5 and rho(u) < rank for u in coefficients)
    expected = T.pair_source(w)
    for u,c in coefficients.items():
        expected = combine((1,expected),(-c,T.pair_source(u)))
    assert divergence(current) == expected
    assert len(bridge['left'])-1 == data['ordinary_left_length']
    assert len(bridge['right'])-1 == data['ordinary_right_length']
    x = data['rank']
    for _ in range(data['quotient_length']):
        x = NORMAL.quotient_step(x)
    assert x == data['minimum']
    return dict(seed=w,rank=rank,status='descending' if accepted else 'unresolved',
                current=current,coefficients=coefficients,parameters=data,
                lower_seed=z,input_rank_bound=[bound.numerator,bound.denominator],
                bound_kind=bound_data['kind'],uniform_stratum=stratum_test(data))


def compile_plan(data,supplied):
    if data['status'] != 'descending':
        raise ValueError('The endpoint-rank criterion remains unresolved')
    assert all(rho(u) < rho(data['seed']) for u in data['coefficients'])
    return NINE.compile_five_plan(data,supplied)


def even_undo(w):
    data = parameters(w)
    if data['d'] % 2 or not NORMAL.canonical(data['endpoint']):
        raise ValueError('Require an even block with canonical raw endpoint')
    inverse = ESCAPE.spine_bridge(data['endpoint'])
    assert inverse['D'] == data['d']//2 and inverse['j'] == data['a']-1
    assert inverse['p'] == data['rank']
    assert combine((1,RUN.bridge(data['rank'])['current']),(1,inverse['current'])) == {}
    return dict(seed=w,endpoint=data['endpoint'],D=inverse['D'],j=inverse['j'],
                restored=data['rank'])


def long_family(a,index=0,d=None):
    """Complete accepted families within3|w, at every first exponent a>=3."""
    if not isinstance(a,int) or a < 3 or not isinstance(index,int) or index < 0:
        raise ValueError('Require a>=3 and nonnegative index')
    def sufficient(depth):
        return 2**depth*(2**(a+3)-13) > 9*3**((depth-1)//2)*(3**(a-1)-1)
    if d is None:
        d = 3
        while not sufficient(d):
            d += 2
    if not isinstance(d,int) or d < 3 or d % 2 != 1 or not sufficient(d):
        raise ValueError('Require an odd second depth satisfying the uniform inequality')
    binary = 2**(d+1)
    t_binary = (1+2**d)*pow(3**(a-1),-1,binary) % binary
    t_ternary = pow(2**a,-1,9)
    first = t_binary+binary*((t_ternary-t_binary)*pow(binary,-1,9) % 9)
    period = 9*binary
    t = first+period*index
    w = (2**a*t-1)//3
    data = parameters(w)
    assert w % 3 == 0 and (data['a'],data['d'],data['t']) == (a,d,t)
    assert Fraction(9*data['endpoint']+5,8) < data['rank']
    assert OLD.absorption_rank_bound(data['endpoint'])['bound'] < data['rank']
    return dict(seed=w,a=a,d=d,t=t,t_residue=first,t_period=period,
                seed_residue=(2**a*first-1)//3,seed_period=3*2**a*binary)
