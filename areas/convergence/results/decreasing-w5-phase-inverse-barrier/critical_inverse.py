"""Whole critical inverse phases, decreasing W5 inputs, and complete barriers.

All plans retain exact missing pair inputs. No unknown orbit is searched.
The inverse barrier concerns a specified number of canonical quotient steps.
"""
from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('critical_inverse_nine', HERE.parent/'w9_closure/w9_closure.py')
NINE = module_from_spec(spec)
spec.loader.exec_module(NINE)
T = NINE.TRIPLING
NORMAL = T.NORMAL
combine, atoms, divergence = T.combine, T.atoms, T.divergence


def valuation3(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError('Require a positive integer')
    h = 0
    while n % 3 == 0:
        n //= 3
        h += 1
    return h


def phase_bridge(q):
    """An exact current [q]-[p], p<q, for every positive odd q=4 modulo9."""
    NORMAL._odd(q)
    h = valuation3(2*q+1)
    if h < 2:
        raise ValueError('Require q=4 modulo9')
    p = 2**h*((2*q+1)//3**h)-1
    assert 0 < p < q
    path, current, x = [p], Counter(), p
    for a in [1]*(h-1)+[2]:
        assert NORMAL.valuation2(3*x+1) == a
        if x != 1:
            current[x] -= 1
        x = NORMAL.step(x)
        path.append(x)
    current = combine((1, current))
    assert x == q and divergence(current) == atoms((1, q), (-1, p))
    if NORMAL.canonical(q):
        assert all(NORMAL.canonical(y) for y in path)
    return dict(target=q, lower=p, h=h, word=[1]*(h-1)+[2],
                path=path, current=current)


def eligible(w):
    NORMAL._odd(w)
    return w % 8 == 5 and w % 3 == 0 and NORMAL.selected(3*w)


def phase_parameters(w):
    if not eligible(w):
        raise ValueError('Require w=5 modulo8,3|w,and selected3w')
    q = (3*w-1)//2
    data = phase_bridge(q)
    h, p = data['h'], data['lower']
    unit = w//3**(h-1)
    assert h == 1+valuation3(w) and p == 2**h*unit-1
    assert NORMAL.canonical(p) and p % 4 == 3 and p % 3 in (0, 1)
    v = T.critical_inverse(p)
    assert 9*v < 8*w
    returning = h == 2 and unit % 3 == 1
    assert returning == (w % 9 == 3)
    assert (v % 16 == 9) == returning
    if returning:
        assert unit % 24 == 7
        z = (3*unit-1)//4
        assert NORMAL.valuation2(9*v-1) == 4
        assert not NORMAL.canonical(3*z) and 4*z+1 == w
    return dict(w=w, q=q, p=p, h=h, unit=unit, pair_child=v,
                returning=returning, inverse=data)


def absorption_five_plan(seed):
    """Formal absorption using only W5 inputs strictly below the seed.

    A W9 request b in the original induction is at most seed/3; complete
    W9 elimination therefore asks W5 inputs at most(3seed+3)/4<seed.
    """
    plan = T.plan(seed)
    current, coefficients = plan['current'], Counter()
    for w in plan['pairs']:
        if w % 16 == 9:
            assert 3*w <= seed
        sub = NINE.five_plan(w)
        current = combine((1, current), (1, sub['current']))
        for u, c in sub['coefficients'].items():
            coefficients[u] += c
    coefficients = NINE.clean(coefficients)
    assert all(u % 8 == 5 and u < seed for u in coefficients)
    expected = atoms((1, seed))
    for u, c in coefficients.items():
        expected = combine((1, expected), (-c, T.pair_source(u)))
    assert divergence(current) == expected
    return dict(seed=seed, coefficients=coefficients, current=current)


def phase_pair_plan(w):
    """Complete eligible-phase classification; return self-dependency explicitly.

    In the descending classes, every W5 input is below w. The third class
    retains a coefficient+1 request for w itself and is not a constructor.
    """
    data = phase_parameters(w)
    v = data['pair_child']
    z = NORMAL.normal_form(w)
    local = combine((1, NORMAL.bridge(3*w)['current']),
                    (1, data['inverse']['current']),
                    (-1, NORMAL.bridge(3*v)['current']),
                    (-1, NORMAL.bridge(w)['current']))
    expected = combine((1, T.pair_source(w)), (-1, T.pair_source(v)),
                       (-1, atoms((1, v), (-1, z))))
    assert divergence(local) == expected
    child, high, low = NINE.five_plan(v), absorption_five_plan(v), absorption_five_plan(z)
    current = combine((1, local), (1, child['current']),
                      (1, high['current']), (-1, low['current']))
    coefficients = Counter(child['coefficients'])
    for u, c in high['coefficients'].items():
        coefficients[u] += c
    for u, c in low['coefficients'].items():
        coefficients[u] -= c
    coefficients = NINE.clean(coefficients)
    if data['returning']:
        assert coefficients[w] == 1
        assert all(u <= w for u in coefficients)
        status = 'self_dependency'
    else:
        assert all(u < w for u in coefficients)
        status = 'descending'
    expected = T.pair_source(w)
    for u, c in coefficients.items():
        expected = combine((1, expected), (-c, T.pair_source(u)))
    assert divergence(current) == expected
    return dict(seed=w, status=status, parameters=data, coefficients=coefficients,
                current=current, absorption_seeds=[v,z])


def compile_phase_plan(plan, supplied):
    if plan['status'] != 'descending':
        raise ValueError('The plan requests its own unproved current')
    assert all(u < plan['seed'] for u in plan['coefficients'])
    return NINE.compile_five_plan(plan, supplied)


# Every canonical inverse branch, including the complete unbounded rays.
# A row(A,B) means (A*y+B)/3; a ray repeats p ->64p+49.
BASES = {
    0: {'ray0': (8,3), 'ray1': (16,3)},
    1: {'ray0': (4,-1), 'ray1': (32,19)},
    2: {'point': (2,-1), 'ray0': (64,19), 'ray1': (128,83)},
}


def inverse_affine(residue, kind, ray_index=0):
    if residue not in BASES or kind not in BASES[residue]:
        raise ValueError('Invalid inverse branch')
    if not isinstance(ray_index, int) or ray_index < 0 or (kind == 'point' and ray_index):
        raise ValueError('Invalid ray index')
    A, B = BASES[residue][kind]
    factor = 64**ray_index
    alpha = Fraction(factor*A, 3)
    beta = Fraction(factor*B, 3)+49*((factor-1)//63)
    assert alpha-beta == factor*(Fraction(A-B,3)-Fraction(7,9))+Fraction(7,9)
    assert alpha-beta >= 1
    if kind != 'point':
        assert alpha-beta > 1
    return alpha, beta


def inverse_step(y, kind, ray_index=0):
    if not NORMAL.canonical(y):
        raise ValueError('Require a canonical target')
    alpha, beta = inverse_affine(y % 3, kind, ray_index)
    p = alpha*y+beta
    assert p.denominator == 1
    p = p.numerator
    assert NORMAL.canonical(p) and NORMAL.quotient_step(p) == y
    return p, alpha, beta


def inverse_lift(q, word):
    """Check any supplied complete inverse word against its shadow at1."""
    D = len(word)
    if not NORMAL.canonical(q) or q <= 1 or (q-1) % 3**D:
        raise ValueError('Require canonical q>1 and q=1 modulo3^word_length')
    actual, shadow, slope = q, 1, Fraction(1)
    states = []
    for depth, (kind, index) in enumerate(word, 1):
        assert actual % 3 == shadow % 3
        old_gap = slope-Fraction(shadow+1,2)
        actual, alpha, beta = inverse_step(actual, kind, index)
        shadow, _, _ = inverse_step(shadow, kind, index)
        slope *= alpha
        gap = slope-Fraction(shadow+1,2)
        assert gap == alpha*old_gap+(alpha-beta-1)/2
        assert gap > 0 and slope > 1
        assert actual == slope*(q-1)+shadow and actual > q
        if shadow == 1:
            assert slope == Fraction(4,3)**depth
        else:
            assert shadow >= 7 and actual > 4*q+3
        states.append(dict(depth=depth, state=actual, shadow=shadow,
                           slope=[slope.numerator,slope.denominator],
                           gap=[gap.numerator,gap.denominator]))
    return dict(target=q, word=[[kind,index] for kind,index in word], states=states)


def critical_witness(D, index=0):
    """Infinite CRT family with fixed binary phase and exact ternary precision."""
    if not isinstance(D, int) or D < 1 or not isinstance(index, int) or index < 0:
        raise ValueError('Require D>=1 and a nonnegative family index')
    ternary = 3**(D+1)
    residue = 7+32*((1+2*3**D-7)*pow(32,-1,ternary) % ternary)
    period = 32*ternary
    q = residue+period*index
    w = (2*q+1)//3
    assert q % 32 == 7 and valuation3(q-1) == D
    assert T.critical(q) and T.critical_image(w) == q
    assert w % 64 == 5 and NORMAL.selected(3*w)
    assert not eligible(w)
    return dict(D=D, index=index, target=q, pair_index=w,
                q_residue=residue, q_period=period)
