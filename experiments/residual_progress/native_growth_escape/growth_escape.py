"""Conditional original-rank escapes from the complete native H17 family.

The all-r family is symbolic; its huge CRT cells are materialized only under
explicit size limits. The exhaustive decision concerns two inverse rays plus
point inverses, not arbitrary histories or cycles. No dispatcher is changed.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('growth_escape_native', HERE.parent/'native_nine_growth/nine_growth.py')
G = module_from_spec(spec)
spec.loader.exec_module(G)
N, B = G.N, G.B
combine, atoms, divergence = B.combine, B.atoms, B.divergence


def integer(x, minimum=0):
    if not isinstance(x, int) or isinstance(x, bool) or x < minimum:
        raise ValueError('Require an integer at least '+str(minimum))


def valuation3(x):
    integer(x, 1)
    result = 0
    while x % 3 == 0:
        result += 1
        x //= 3
    return result


def entry(b):
    integer(b, 1)
    r = G.return_count(b)
    if G.order(b) != 9*r+17:
        raise ValueError('Require an exact native H17 exit')
    c = G.affine_iterate(b, r+1)
    z = (9*c-1)//16
    assert z % 8 == z % 9 == 5 and N.canonical(3*z)
    return dict(seed=b, returns=r, c=c, z=z, original_rank=3*b, exit_root=3*z)


def path(x, length, expected_word=None):
    N._odd(x)
    integer(length)
    if expected_word is not None and len(expected_word) != length:
        raise ValueError('Wrong word length')
    rows, word = Counter(), []
    for i in range(length):
        if x == 1:
            raise ValueError('The prescribed path reached the absorbing state early')
        e = N.valuation2(3*x+1)
        if expected_word is not None and e != expected_word[i]:
            raise ValueError('Incorrect exact valuation word')
        word.append(e)
        rows[x] += 1
        x = (3*x+1) >> e
    return dict(endpoint=x, current=dict(rows), word=word)


def ray_parameters(b, ray, L, max_ray=10000):
    if ray not in (0, 1) or isinstance(ray, bool):
        raise ValueError('Require inverse ray0 or1')
    integer(L)
    if max_ray is not None:
        integer(max_ray)
        if L > max_ray:
            raise ValueError('Ray materialization cap exceeded')
    data = entry(b)
    a0 = (8 if ray == 0 else 16)*data['z']+1
    a = (64**L*(9*a0+7)-7)//9
    h = valuation3(a+1)
    p = 2**h*((a+1)//3**h)-1
    assert a % 8 == 1 and N.canonical(a)
    assert N.quotient_step(a) == data['exit_root']
    assert p > 0 and N.canonical(p)
    if h:
        assert p % 4 == 3 and p % 3 != 2
        assert N.valuation2(p+1) == h+1
    descending = (p < 3*b) if h else data['returns'] == 0
    return dict(data, ray=ray, ray_index=L, base=a0, lifted=a,
                point_depth=h, endpoint=p, descending=descending)


def inverse_bridge(data, max_steps=10000):
    integer(max_steps)
    h, a, p, q = (data[k] for k in ('point_depth', 'lifted', 'endpoint', 'exit_root'))
    if h > max_steps:
        raise ValueError('Point-prefix materialization cap exceeded')
    initial = path(p, h, [1]*h) if h else dict(endpoint=p, current={}, word=[])
    assert initial['endpoint'] == a
    last = N.quotient_bridge(a)
    assert last['minimum'] == q
    current = combine((-1, initial['current']), (-1, last['current']))
    assert divergence(current) == atoms((1, q), (-1, p))
    return current


def absorption_comparison(b, ray, L, max_ray=10000, max_steps=10000):
    """Pair source minus explicit signed absorption premises +[p]-[b]."""
    data = ray_parameters(b, ray, L, max_ray=max_ray)
    inverse = inverse_bridge(data, max_steps=max_steps)
    q, p, r = data['exit_root'], data['endpoint'], data['returns']
    upper, lower = path(3*b, 6*r+12), path(q, 4)
    assert upper['endpoint'] == lower['endpoint']
    current = combine((1, upper['current']), (-1, lower['current']), (1, inverse))
    assert divergence(current) == atoms((1, 3*b), (-1, p))
    # Both ray choices have a common tail after four arrows from q.
    ppath = path(p, data['point_depth']+5)
    assert ppath['endpoint'] == upper['endpoint']
    assert current == combine((1, upper['current']), (-1, ppath['current']))
    inputs = combine((1, {p: 1}), (-1, {b: 1}))
    return dict(data, current=current, absorption_inputs=inputs,
                ordinary_clocks=[6*r+12, data['point_depth']+5],
                meeting=upper['endpoint'],
                status='descending' if data['point_depth'] and p < 3*b else 'unresolved')


def critical_comparison(b, ray, L, max_bits=256):
    """Expand formal H only for modest seeds; no unbounded orbit search."""
    integer(max_bits, 1)
    data = absorption_comparison(b, ray, L)
    p = data['endpoint']
    if max(b.bit_length(), p.bit_length()) > max_bits:
        raise ValueError('Formal-H expansion size cap exceeded')
    hp, hb = B.absorption_plan(p), B.absorption_plan(b)
    current = combine((1, data['current']), (1, hp['current']), (-1, hb['current']))
    coefficients = combine((1, hp['coefficients']), (-1, hb['coefficients']))
    result = dict(data, current=current, coefficients=coefficients)
    B.check_boundary(result)
    if data['point_depth']:
        assert all(B.rho(w) < 3*b for w in coefficients) == data['descending']
        if not data['descending']:
            lead = B.T.critical_inverse(p)
            assert coefficients[lead] == 1 and B.rho(lead) == p
            assert all(B.rho(w) < p for w in coefficients if w != lead)
    else:
        old = G.exit_plan(b)
        assert current == old['current'] and coefficients == old['coefficients']
    return result


def exhaustive_decision(b, max_rays=10000):
    """Complete two-ray/point decision at an unresolved r>=1 H17 exit."""
    data = entry(b)
    if data['returns'] < 1:
        raise ValueError('Require an unresolved H17 exit with at least one return')
    integer(max_rays, 1)
    Q = 3*b
    J = (Q-1).bit_length()-2
    P = (3**J*(Q-1))//2**J
    cases, bounds = [], []
    for ray in (0, 1):
        a0 = (8 if ray == 0 else 16)*data['z']+1
        ratio = (9*P-2)//(9*a0+7)
        L, power = 0, 1
        while power <= ratio:
            if len(cases) >= max_rays:
                return dict(status='capped', seed=b, cases=cases, bounds=bounds,
                            point_bound=J, lifted_bound=P)
            result = ray_parameters(b, ray, L, max_ray=max_rays)
            cases.append(dict(ray=ray, L=L, depth=result['point_depth'],
                              endpoint=result['endpoint'], accepted=result['descending']))
            L += 1
            power *= 64
        bounds.append(dict(ray=ray, ratio=ratio, maximum_ray=L-1))
    return dict(status='accepted' if any(x['accepted'] for x in cases) else 'exhausted',
                seed=b, point_bound=J, lifted_bound=P, bounds=bounds, cases=cases)


def ternary_log(target, depth):
    """Discrete logarithm in the cyclic subgroup1 mod9, by exact digit lifts."""
    integer(depth, 2)
    integer(target)
    if target % 9 != 1:
        raise ValueError('Require a target equal to1 modulo9')
    L, period = 0, 1
    for precision in range(3, depth+1):
        modulus = 3**precision
        choices = [L+j*period for j in range(3)
                   if pow(64, L+j*period, modulus) == target % modulus]
        assert len(choices) == 1
        L = choices[0]
        period *= 3
    return L


def family_spec(r):
    """Small exact descriptor even when the resulting integers are enormous."""
    integer(r)
    s, d = r+1, 6*(r+1)+4
    modulus = 3**d
    target = 217*pow(8272, -1, modulus) % modulus
    L = ternary_log(target, d)
    h = 11*L+8*s
    C = 223*(729**s-512**s)//217
    binary_exp = 9*s+10
    binary_mod = 2**binary_exp
    binary_residue = (512**s*137-C)*pow(729**s, -1, binary_mod) % binary_mod
    assert L >= 1 and h >= 6*s+2
    return dict(returns=r, s=s, forced_precision=d, ray=1, ray_index=L,
                point_depth=h, tertiary_point_order=h-6*s-2,
                binary_exponent=binary_exp, binary_residue=binary_residue,
                ternary_exponent=h-6*s-1,
                upper_word=[1, 2, 1]+[1, 1, 2, 1, 1, 3]*s+[1, 1, 3],
                ordinary_clocks=[6*r+12, h+5])


def beta_mod(data, precision):
    """The divided affine constant modulo a small power3, no huge ray power."""
    integer(precision, 1)
    s, d, L = data['s'], data['forced_precision'], data['ray_index']
    C = 223*(729**s-512**s)//217
    modulus = 3**(d+precision)
    numerator = (pow(64, L, modulus)*(81*C+7*512**s)+2*512**s) % modulus
    assert numerator % 3**d == 0
    return numerator//3**d


def family(r, unit=1, index=0, max_point_depth=10000):
    """Materialize the whole CRT cell only when it meets an explicit size cap."""
    if unit not in (1, 2) or isinstance(unit, bool):
        raise ValueError('Require nonzero ternary terminal unit1 or2')
    integer(index)
    integer(max_point_depth, 1)
    data = family_spec(r)
    h, m, L = data['point_depth'], data['tertiary_point_order'], data['ray_index']
    if h > max_point_depth:
        raise ValueError('Symbolic family exceeds the materialization cap')
    modulus3 = 3**(m+1)
    beta = beta_mod(data, m+1)
    residue3 = (unit*3**m-beta)*pow(pow(2, 6*L, modulus3), -1, modulus3) % modulus3
    modulus2, residue2 = 2**data['binary_exponent'], data['binary_residue']
    seed = residue2+modulus2*((residue3-residue2)*pow(modulus2, -1, modulus3) % modulus3)
    period = modulus2*modulus3
    seed += index*period
    evaluated = ray_parameters(seed, 1, L, max_ray=max_point_depth)
    assert evaluated['returns'] == r and evaluated['c'] % 1024 == 137
    assert evaluated['point_depth'] == h and (evaluated['lifted']+1)//3**h % 3 == (unit*pow(2, -9*data['s'], 3)) % 3
    assert 0 < evaluated['endpoint'] < seed
    return dict(data, seed=seed, endpoint=evaluated['endpoint'], unit=unit,
                index=index, seed_period=period, ternary_residue=residue3)


def family_comparison(r, unit=1, index=0, max_point_depth=10000):
    data = family(r, unit, index, max_point_depth)
    result = absorption_comparison(data['seed'], 1, data['ray_index'],
                                   max_ray=max_point_depth, max_steps=max_point_depth)
    h, L = data['point_depth'], data['ray_index']
    upper = path(3*data['seed'], 6*r+12, data['upper_word'])
    lower_word = [1]*h+[2, 6*L+3, 1, 2, 1]
    lower = path(data['endpoint'], h+5, lower_word)
    assert upper['endpoint'] == lower['endpoint'] == result['meeting']
    assert result['meeting'] == (2187*result['c']+925)//512 > 3*data['seed']
    assert result['endpoint'] < data['seed'] and result['status'] == 'descending'
    return dict(result, family=data, upper_word=data['upper_word'], lower_word=lower_word)


def compile_absorptions(data, supplied):
    """Supply exact absorption at each signed seed; reject any missing input."""
    b = data['seed']
    if data['status'] != 'descending':
        raise ValueError('Require a descending original-rank comparison')
    entry(b)
    for x, c in data['current'].items():
        if (not isinstance(x, int) or isinstance(x, bool) or x <= 1 or x % 2 != 1
                or not isinstance(c, int) or isinstance(c, bool) or not c):
            raise ValueError('Malformed comparison current row')
    expected = B.T.pair_source(b)
    for x, c in data['absorption_inputs'].items():
        if (not isinstance(x, int) or isinstance(x, bool) or x <= 0 or x % 2 != 1
                or not isinstance(c, int) or isinstance(c, bool) or not c or x >= 3*b):
            raise ValueError('Invalid or nondecreasing absorption premise')
        expected = combine((1, expected), (-c, atoms((1, x))))
    if divergence(data['current']) != expected:
        raise ValueError('Incorrect signed comparison boundary')
    result = data['current']
    for x, c in data['absorption_inputs'].items():
        if x not in supplied:
            raise ValueError('Missing supplied absorption current')
        rows = supplied[x]
        for state, coefficient in rows.items():
            if (not isinstance(state, int) or isinstance(state, bool) or state <= 1 or state % 2 != 1
                    or not isinstance(coefficient, int) or isinstance(coefficient, bool) or not coefficient):
                raise ValueError('Malformed supplied current row')
        if divergence(rows) != atoms((1, x)):
            raise ValueError('Incorrect supplied absorption boundary')
        result = combine((1, result), (c, rows))
    assert divergence(result) == B.T.pair_source(b)
    return result
