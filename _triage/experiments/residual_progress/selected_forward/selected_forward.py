"""Selected critical-five pairs: exact forward blocks and strict-rho plans.

The returned currents retain every signed missing pair premise.  No unknown
absorption current is inferred from recognition of an intermediate input.
"""
from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name, relative):
    spec = spec_from_file_location(name, HERE.parent / relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = _load('selected_forward_base', 'nonselected_forward/nonselected_forward.py')
RANK = _load('selected_forward_rank', 'critical_rank/rank_closure.py')
NORMAL, RUN, OLD = BASE.NORMAL, BASE.RUN, BASE.OLD
T, NINE = BASE.T, BASE.NINE
combine, atoms, divergence, rho = BASE.combine, BASE.atoms, BASE.divergence, BASE.rho


def eligible(w):
    NORMAL._odd(w)
    return w % 8 == 5 and NORMAL.selected(3*w)


def parameters(w):
    if not eligible(w):
        raise ValueError('Require a W5 pair with selected 3w')
    q = (3*w-1)//2
    a, t, d, u = RUN.parameters(q)
    f = RUN.target(q)
    assert q == rho(w) and q % 3 == 1 and a >= 2
    assert t % 4 == -3**a % 4 and 2**a*t % 3 == 2
    assert u % 3 == (1 if d % 2 else 2)
    return dict(seed=w, rank=q, a=a, t=t, d=d, unit=u, endpoint=f,
                minimum=NORMAL.normal_form(f), quotient_length=a+d//2-1,
                ordinary_left_length=a+d//2 if d % 2 else a+d//2-1,
                ordinary_right_length=1 if d % 2 else 0)


def small_exponent_domain(data):
    """Complete endpoint-bound test at first exponent a=2,3,4."""
    a, d, f, n = (data[k] for k in ('a', 'd', 'endpoint', 'minimum'))
    if a not in (2, 3, 4):
        raise ValueError('The complete small-exponent table is for a=2,3,4')
    if d % 2:
        return True
    selected = NORMAL.selected(f)
    if a == 2:
        return d >= 4 or selected
    if a == 3:
        return d >= 6 or selected
    return d >= 10 or (selected and (d >= 6 or (d == 4 and n % 8 != 3)))


def _assemble(w, blocks):
    data = parameters(w)
    q = data['rank']
    upper, lower = NORMAL.bridge(3*w), NORMAL.bridge(w)
    assert upper['minimum'] == q
    assert len(upper['left_prefix']) == len(upper['right_prefix']) == data['a']+2
    z = lower['minimum']
    current = combine((1, upper['current']), (-1, lower['current']))
    x, quotient_length, clocks = q, 0, []
    for _ in range(blocks):
        if not NORMAL.canonical(x) or x % 4 != 3:
            raise ValueError('A further complementary block requires a canonical climber')
        bridge = RUN.bridge(x)
        f = bridge['target']
        norm = NORMAL.bridge(f)
        current = combine((1, current), (1, bridge['current']), (1, norm['current']))
        a, _, d, _ = RUN.parameters(x)
        length = a+d//2-1
        clocks.append(dict(start=x, a=a, d=d, endpoint=f, minimum=norm['minimum'],
                           ordinary_left=len(bridge['left'])-1,
                           ordinary_right=len(bridge['right'])-1,
                           quotient=length))
        assert clocks[-1]['ordinary_left'] == (a+d//2 if d % 2 else a+d//2-1)
        assert clocks[-1]['ordinary_right'] == (1 if d % 2 else 0)
        test = x
        for _ in range(length):
            test = NORMAL.quotient_step(test)
        assert test == norm['minimum']
        quotient_length += length
        x = norm['minimum']
    high, low = RANK.absorption_plan(x), RANK.absorption_plan(z)
    current = combine((1, current), (1, high['current']), (-1, low['current']))
    coefficients = Counter(high['coefficients'])
    coefficients.subtract(low['coefficients'])
    coefficients = NINE.clean(coefficients)
    bound_data = OLD.absorption_rank_bound(x)
    bound = bound_data['bound']
    assert all(rho(u) <= bound for u in high['coefficients'])
    assert 4*z <= w-1
    assert all(8*rho(u) <= 9*z+5 < 8*q for u in low['coefficients'])
    expected = T.pair_source(w)
    for u, c in coefficients.items():
        expected = combine((1, expected), (-c, T.pair_source(u)))
    assert divergence(current) == expected
    accepted = bound < q
    answer = dict(seed=w, rank=q, status='descending' if accepted else 'unresolved',
                  current=current, coefficients=coefficients, parameters=data,
                  blocks=clocks, quotient_length=quotient_length, lower_seed=z,
                  upper_normalization_clock=len(upper['left_prefix'])-1,
                  lower_normalization_clock=len(lower['left_prefix'])-1,
                  input_rank_bound=[bound.numerator, bound.denominator],
                  bound_kind=bound_data['kind'])
    if accepted:
        RANK.validate_step(w, answer)
    return answer


def forward_plan(w):
    result = _assemble(w, 1)
    if result['parameters']['a'] in (2, 3, 4):
        assert (result['status'] == 'descending') == small_exponent_domain(result['parameters'])
    return result


def two_block_domain(data):
    """Complete second-block test after a failed selected (a,d)=(2,2)."""
    if (data['parameters']['a'], data['parameters']['d']) != (2, 2):
        raise ValueError('Require first block (2,2)')
    second = data['blocks'][1]
    b, e, y, m = (second[k] for k in ('a', 'd', 'endpoint', 'minimum'))
    if b not in (2, 3, 4):
        raise ValueError('Require second first exponent b=2,3,4')
    if e % 2:
        return True
    selected = NORMAL.selected(y)
    if b == 2:
        return e >= 4 or selected
    if b == 3:
        return e >= 8 or (selected and (e >= 4 or m % 8 != 3))
    return e >= 10 or (selected and (e >= 6 or (e == 4 and m % 8 == 1)))


def two_block_plan(w):
    first = parameters(w)
    if (first['a'], first['d']) != (2, 2) or not NORMAL.canonical(first['endpoint']):
        raise ValueError('Require a failed selected (2,2) block')
    result = _assemble(w, 2)
    if result['blocks'][1]['a'] in (2, 3, 4):
        assert (result['status'] == 'descending') == two_block_domain(result)
    return result


def one_step(w):
    if not eligible(w):
        return None
    result = forward_plan(w)
    if result['status'] == 'descending':
        return dict(result, rule='selected_forward_block')
    data = result['parameters']
    if (data['a'], data['d']) == (2, 2) and NORMAL.canonical(data['endpoint']):
        result = two_block_plan(w)
        if result['status'] == 'descending':
            return dict(result, rule='selected_forward_two_blocks')
    return None


def recognized(w):
    return one_step(w) is not None


def compile_plan(data, supplied):
    if data['status'] != 'descending':
        raise ValueError('Endpoint rank has not decreased')
    RANK.validate_step(data['seed'], data)
    return RANK.compile_plan(data, supplied)


def long_family(a, index=0, d=None):
    """Whole new selected w=2 mod3 CRT families, for every a>=2."""
    if not isinstance(a, int) or a < 2 or not isinstance(index, int) or index < 0:
        raise ValueError('Require a>=2 and nonnegative index')
    def sufficient(depth):
        return 2**depth*(2**(a+3)-13) > 9*3**((depth-1)//2)*(3**(a-1)-1)
    if d is None:
        d = 3
        while not sufficient(d):
            d += 2
    if not isinstance(d, int) or d < 3 or d % 2 != 1 or not sufficient(d):
        raise ValueError('Require odd d satisfying the uniform endpoint inequality')
    binary = 2**(d+1)
    tb = (1+2**d)*pow(3**(a-1), -1, binary) % binary
    tt = 7*pow(2**(a+1), -1, 9) % 9
    first = tb+binary*((tt-tb)*pow(binary, -1, 9) % 9)
    period = 9*binary
    t = first+period*index
    w = (2**(a+1)*t-1)//3
    data = parameters(w)
    assert w % 3 == 2 and (data['a'], data['d'], data['t']) == (a, d, t)
    assert Fraction(9*data['endpoint']+5, 8) < data['rank']
    return dict(seed=w, a=a, d=d, t=t, t_residue=first, t_period=period,
                seed_residue=(2**(a+1)*first-1)//3,
                seed_period=3*2**(a+1)*binary)


def even_undo(w):
    """The inverse block exactly undoes a failed selected (2,2) prefix."""
    data = parameters(w)
    q, f = data['rank'], data['endpoint']
    if (data['a'], data['d']) != (2, 2) or not NORMAL.canonical(f):
        raise ValueError('Require failed first block (2,2)')
    bridge = BASE.ESCAPE.spine_bridge(f)
    assert bridge['D'] == 1 and bridge['j'] == 1 and bridge['p'] == q
    assert combine((1, RUN.bridge(q)['current']), (1, bridge['current'])) == {}
    return dict(seed=w, restored=q, endpoint=f, D=1, j=1)
