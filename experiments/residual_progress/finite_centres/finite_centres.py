"""Complete returning-ray comparisons and infinitely many parent poles.

These are conditional current identities.  Every missing signed pair remains
an explicit premise.  No dispatcher is changed and no universal current is
supplied.  The proof's potential class has exactly the two fixed W/E phases.
"""
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('finite_centres_debt',
                              HERE.parent/'arithmetic_progress/valuation_debt.py')
DEBT = module_from_spec(spec)
spec.loader.exec_module(DEBT)
RETURN, RANK, NORMAL = DEBT.RETURN, DEBT.RANK, DEBT.NORMAL
D, B = DEBT.D, DEBT.B_W
THETA = Fraction(-B, D)


def valuation3(x):
    if not isinstance(x, int) or x == 0:
        raise ValueError('Require a nonzero integer')
    x, order = abs(x), 0
    while x % 3 == 0:
        x //= 3
        order += 1
    return order


def affine_order(centre, x):
    """Order of the primitive integer affine form with this rational pole."""
    centre = Fraction(centre)
    value = centre.denominator*x-centre.numerator
    if not value:
        raise ValueError('An affine valuation form cannot vanish')
    return NORMAL.valuation2(abs(value))


def parameters(L):
    if not isinstance(L, int) or L < 1 or L % 3 != 1:
        raise ValueError('Require L>=1 with L=1 modulo3')
    scale, a = 4**L, 3
    slope = Fraction(6*scale*2**a, 3**a)
    while slope > 4:
        a += 1
        slope *= Fraction(2, 3)
    assert a > 3 and Fraction(8, 3) < slope <= 4
    offset = slope/9-Fraction(1, 3)+Fraction(2**a, 3**(a+1))
    assert -Fraction(1, 27) < offset < 1
    d = (2*scale+1)//9
    assert 9*d == 2*scale+1
    centre = slope*THETA+offset
    assert centre == Fraction(2**a*(D-5587204*scale)-D*3**a,
                              D*3**(a+1))
    denominator_order = valuation3(centre.denominator)
    assert a >= 3*L+2
    if L % 9 == 4:
        K = D*d-2*scale*B
        assert K % 3 == 2
        assert centre == Fraction(3*2**a*K-D*3**(a-1), D*3**a)
        assert denominator_order == a-1
    if L >= 13:
        term = D-5587204*scale
        assert abs(term) < 3**(2*L+15)
        assert valuation3(term) <= 2*L+14 < a
        assert denominator_order == a+1-valuation3(term) >= L-11
    return dict(L=L, a=a, scale=scale, slope=slope, offset=offset,
                centre=centre, centre_denominator_order=denominator_order)


def family(L, H, index=0):
    """The complete positive CRT progression for this ray and exact order."""
    if not isinstance(H, int) or H < 26:
        raise ValueError('Require exact child order H>=26')
    if not isinstance(index, int) or index < 0:
        raise ValueError('Require a nonnegative progression index')
    data = parameters(L)
    a, scale = data['a'], data['scale']
    ternary, binary = 3**(a+1), 2**(H+1)
    d = (2*scale+1)//9
    residue3 = ((10*3**(a-2)*pow(2**a, -1, ternary)-d)
                * pow(2*scale, -1, ternary)) % ternary
    residue2 = ((2**H-B)*pow(D, -1, binary)) % binary
    first = residue2+binary*((residue3-residue2)*pow(binary, -1, ternary) % ternary)
    period = binary*ternary
    u = first+period*index
    r = 3*scale*u+(scale-1)//3
    t, remainder = divmod(2*r+1, 3**(a-1))
    assert not remainder and t % 2 and t % 4 == 3**a % 4
    w, remainder = divmod(2**a*t-1, 3)
    assert not remainder and w == data['slope']*u+data['offset']
    assert 2*u < w <= 4*u
    assert t % 27 == 10*pow(2**a, -1, 27) % 27
    assert valuation3(2*r+1) == a-1
    assert DEBT.MIXED.eligible(u) and affine_order(THETA, u) == H
    assert DEBT.phase(u) == 'W' and DEBT.phase(w) == 'E'
    assert RETURN.returning(w) and NORMAL.valuation2(3*w+1) == a
    assert NORMAL.canonical(3*u) and RANK.rho(u) == 3*u
    q = (3*w-1)//2
    assert q > 3*u and Fraction(9*w+11, 32) < 3*u
    # Primitive pole forms have odd denominators.  Reduction only removes odd
    # factors, so the affine transport adds the exact binary slope order.
    assert data['centre'].denominator % 2
    assert affine_order(data['centre'], w) == H+a+2*L+1
    return dict(seed=w, child=u, rank=q, endpoint=r, t=t, L=L, H=H,
                index=index, a=a, child_residue=first, child_period=period,
                binary_residue=residue2, ternary_residue=residue3,
                slope=[data['slope'].numerator, data['slope'].denominator],
                offset=[data['offset'].numerator, data['offset'].denominator],
                parent_centre=[data['centre'].numerator, data['centre'].denominator],
                parent_centre_order=H+a+2*L+1,
                centre_ternary_denominator_order=data['centre_denominator_order'])


def comparison(L, H, index=0):
    """Retain the complete R44 current and every signed helper."""
    data = family(L, H, index)
    w, u, a, r = (data[k] for k in ('seed', 'child', 'a', 'endpoint'))
    plan = RETURN.forward_plan(w)
    assert plan['status'] == 'descending'
    assert plan['parameters']['a'] == a and plan['parameters']['endpoint'] == r
    assert plan['normalized_upper'] == 3*u
    assert plan['coefficients'][u] == 1
    assert all(RANK.rho(x) < 3*u for x in plan['coefficients'] if x != u)
    assert plan['rank'] == data['rank'] > 3*u
    upper = RANK.absorption_plan(u)
    endpoint = RANK.absorption_plan(r)
    lower = RANK.absorption_plan(plan['lower_seed'])
    assert endpoint['coefficients'] == RANK.combine((1, {u: 1}), (1, upper['coefficients']))
    assert plan['coefficients'] == RANK.combine((1, {u: 1}),
                                               (1, upper['coefficients']),
                                               (-1, lower['coefficients']))
    assert 4*plan['lower_seed'] <= w-1
    assert all(Fraction(9*plan['lower_seed']+5, 8) >= RANK.rho(x)
               for x in lower['coefficients'])
    RANK.validate_step(w, plan)
    return dict(seed=w, rank=data['rank'], current=plan['current'],
                coefficients=plan['coefficients'], family=data, leading=u,
                lower_seed=plan['lower_seed'], status='descending',
                quotient_length=a-1, ordinary_common_tail_clocks=[a, 1])


def compile_plan(data, supplied):
    """Missing negative and positive pair currents are equally mandatory."""
    RANK.validate_step(data['seed'], data)
    return RANK.compile_plan(data, supplied)
