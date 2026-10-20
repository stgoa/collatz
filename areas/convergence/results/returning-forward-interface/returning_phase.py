"""A forward interface for the whole returning E phase.

Accepted plans use only W5 premises of strictly smaller critical-image rank.
Unaccepted plans retain
their full signed requests; no unknown current or absorption is supplied.
"""
from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('returning_inverse', HERE.parent/'critical_inverse/critical_inverse.py')
INVERSE = module_from_spec(spec)
spec.loader.exec_module(INVERSE)
NINE, NORMAL, TRIPLING = INVERSE.NINE, INVERSE.NORMAL, INVERSE.T
combine, atoms, divergence = INVERSE.combine, INVERSE.atoms, INVERSE.divergence
rho = TRIPLING.critical_image


def returning(w):
    NORMAL._odd(w)
    return w % 8 == 5 and w % 9 == 3 and NORMAL.selected(3*w)


def parameters(w):
    if not returning(w):
        raise ValueError('Require the complete returning E row')
    a = NORMAL.valuation2(3*w+1)
    t = (3*w+1) >> a
    q = (3*w-1)//2
    r = (3**(a-1)*t-1)//2
    assert a >= 3 and t % 4 == 3**a % 4
    assert t % 27 == 10*pow(2**a, -1, 27) % 27
    assert q == 2**(a-1)*t-1 and NORMAL.canonical(q)
    assert r % 9 == 4 and INVERSE.valuation3(2*r+1) == a-1
    endpoint, path = NINE.prefix(q, a-1)
    assert endpoint == r
    x = q
    for valuation in [1]*(a-2)+[2]:
        assert NORMAL.valuation2(3*x+1) == valuation
        x = NORMAL.step(x)
    assert x == r
    return dict(seed=w, a=a, t=t, canonical_upper=q, endpoint=r,
                word=[1]*(a-2)+[2], prefix=path)


def absorption_bound(seed):
    """A proved exact rational upper bound on every formal W5 request."""
    data = NORMAL.normalization(seed)
    n = data['minimum']
    if n == 1:
        bound, kind = Fraction(0), 'absorber'
    elif n % 8 == 1:
        bound, kind = Fraction(9*n+15, 16), 'canonical_forward'
    elif n % 3 == 2:
        bound, kind = Fraction(n+1, 2), 'canonical_inverse'
    elif n % 3 == 1:
        bound, kind = Fraction(2*n+1, 3), 'direct_five'
    elif (n//3) % 8 == 5:
        bound, kind = Fraction(n, 3), 'direct_five'
    else:
        assert (n//3) % 16 == 9
        bound, kind = Fraction(3*n+3, 4), 'nine_elimination'
    return dict(seed=seed, minimum=n, kind=kind, bound=bound,
                normalization=data)


def absorption_rank_bound(seed):
    """A sharp branchwise consequence of the general(9s+5)/8 rank bound."""
    n = NORMAL.normal_form(seed)
    if n == 1:
        bound, kind = Fraction(0), 'absorber'
    elif n % 8 == 1:
        bound, kind = Fraction(27*n+29,32), 'canonical_forward'
    elif n % 3 == 2:
        bound, kind = Fraction(3*n+1,4), 'canonical_inverse'
    elif n % 3 == 1 or (n//3) % 8 == 5:
        bound, kind = Fraction(n), 'direct_five'
    else:
        assert (n//3) % 16 == 9
        bound, kind = Fraction(9*n+5,8), 'nine_elimination'
    return dict(minimum=n, kind=kind, bound=bound)


def stratum_inequality(data, forward=False):
    """Exact uniform threshold on the complete elementary stratum of r.

    With forward=True the elementary minimum must be1 modulo8 and exceed1.
    The inequality certifies a sufficient upper bound, not a necessary test.
    """
    a, t, r = data['a'], data['t'], data['endpoint']
    norm = NORMAL.normalization(r)
    k, partner = norm['F_exponent'], norm['selected_partner']
    scale = 4**k*(2 if partner else 1)
    offset = (4**(k+1)-1)//3 if partner else (4**k-1)//3
    n = norm['minimum']
    assert r == scale*n+offset
    if forward:
        if n <= 1 or n % 8 != 1:
            raise ValueError('Forward stratum bound requires a nonabsorbing1-modulo8 minimum')
        left = 2**(a+5)*scale-3**(a+2)
        right = 122*scale-54*offset-27
        bound = Fraction(9*n+15,16)
        rank_bound = Fraction(27*n+29,32)
    else:
        left = 2**(a+3)*scale-3**(a+1)
        right = 26*scale-18*offset-9
        bound = Fraction(3*n+3,4)
        rank_bound = Fraction(9*n+5,8)
    accepted = left*t > right
    assert accepted == (bound < data['seed'])
    assert accepted == (rank_bound < data['canonical_upper'])
    return dict(F_exponent=k, selected_partner=partner, scale=scale, offset=offset,
                slope_difference=left, intercept=right, accepted=accepted,
                bound=[bound.numerator,bound.denominator],
                rank_bound=[rank_bound.numerator,rank_bound.denominator])


def forward_plan(w):
    """Return an exact formal P(w) plan on the entire returning row.

    Acceptance is by the proved rational endpoint bound, retaining all signed
    coefficients. No search is made for the requested smaller pair currents.
    """
    data = parameters(w)
    upper_bridge, lower_bridge = NORMAL.bridge(3*w), NORMAL.bridge(w)
    assert upper_bridge['minimum'] == data['canonical_upper']
    lower = lower_bridge['minimum']
    assert lower < w
    high, low = INVERSE.absorption_five_plan(data['endpoint']), INVERSE.absorption_five_plan(lower)
    current = combine((1,upper_bridge['current']), (1,data['prefix']),
                      (-1,lower_bridge['current']), (1,high['current']), (-1,low['current']))
    coefficients = Counter(high['coefficients'])
    coefficients.subtract(low['coefficients'])
    coefficients = NINE.clean(coefficients)
    bound_data = absorption_bound(data['endpoint'])
    bound = bound_data['bound']
    rank_data = absorption_rank_bound(data['endpoint'])
    rank_bound = rank_data['bound']
    rank = rho(w)
    assert rank == data['canonical_upper']
    assert all(u <= bound for u in high['coefficients'])
    assert all(rho(u) <= rank_bound for u in high['coefficients'])
    assert all(u < lower for u in low['coefficients'])
    assert 4*lower <= w-1
    assert all(8*rho(u) <= 9*lower+5 < 8*rank for u in low['coefficients'])
    status = 'descending' if rank_bound < rank else 'unresolved'
    if status == 'descending':
        assert all(u % 8 == 5 and rho(u) < rank for u in coefficients)
    if data['a'] == 3 and not (NORMAL.canonical(data['endpoint']) and data['endpoint'] % 4 == 3):
        assert status == 'descending'
    if data['a'] == 4 and not NORMAL.canonical(data['endpoint']):
        assert status == 'descending'
    expected = TRIPLING.pair_source(w)
    for u,c in coefficients.items():
        expected = combine((1,expected),(-c,TRIPLING.pair_source(u)))
    assert divergence(current) == expected
    return dict(seed=w, rank=rank, status=status, current=current, coefficients=coefficients,
                parameters=data, lower_seed=lower, normalized_upper=bound_data['minimum'],
                bound_kind=bound_data['kind'], input_bound=[bound.numerator,bound.denominator],
                rank_bound_kind=rank_data['kind'],
                input_rank_bound=[rank_bound.numerator,rank_bound.denominator],
                index_status='descending' if bound < w else 'unresolved',
                uniform_stratum=stratum_inequality(data))


def compile_forward_plan(data, supplied):
    if data['status'] != 'descending':
        raise ValueError('Arithmetic descent criterion unresolved; no certificate claimed')
    assert all(rho(u) < rho(data['seed']) for u in data['coefficients'])
    return NINE.compile_five_plan(data,supplied)


def check_undo(w, length):
    """Verify either uniform undo mechanism, without claiming it progresses."""
    data = parameters(w)
    if not isinstance(length,int) or not 0 <= length <= data['a']-3:
        raise ValueError('The prefix must stay in the complementary part of the initial rising run')
    end, rows = NINE.prefix(data['canonical_upper'],length)
    start_plan = INVERSE.absorption_five_plan(data['canonical_upper'])
    end_plan = INVERSE.absorption_five_plan(end)
    assert start_plan['coefficients'] == end_plan['coefficients']
    assert combine((1,rows),(1,end_plan['current'])) == start_plan['current']
    inverse = INVERSE.phase_bridge(data['endpoint'])
    assert inverse['lower'] == data['canonical_upper']
    assert combine((1,data['prefix']),(1,inverse['current'])) == {}
    return dict(seed=w, prefix_length=length, endpoint=end,
                full_run_length=data['a']-1, restored=data['canonical_upper'])


def sibling_family(a, index=0, depth=None):
    """A complete nonempty CRT family with arbitrary first-run exponent a.

    The endpoint has at least depth sibling factors. The displayed uniform
    inequality ensures strict W5 descent for every positive member.
    """
    if not isinstance(a,int) or a < 3 or not isinstance(index,int) or index < 0:
        raise ValueError('Require a>=3 and a nonnegative family index')
    if depth is None:
        depth = 1
        while 4**depth*(2**(a+3)-20) <= 3**(a+1)-3:
            depth += 1
    if not isinstance(depth,int) or depth < 1:
        raise ValueError('Require a positive sibling depth')
    scale = 4**depth
    if scale*(2**(a+3)-20) <= 3**(a+1)-3:
        raise ValueError('This sibling depth does not give the uniform decreasing family')
    offset = (scale-1)//3
    binary = 4*scale
    t_binary = (2*offset+2*scale+1)*pow(3**(a-1),-1,binary) % binary
    t_ternary = 10*pow(2**a,-1,27) % 27
    first = t_binary+binary*((t_ternary-t_binary)*pow(binary,-1,27) % 27)
    period = 27*binary
    t = first+period*index
    w = (2**a*t-1)//3
    data = parameters(w)
    assert data['a'] == a and data['t'] == t
    r = data['endpoint']
    s = (r-offset)//scale
    assert s > 0 and s % 2 and r == scale*s+offset
    assert Fraction(3*s+3,4) < w
    assert Fraction(9*s+5,8) < rho(w)
    # Our more detailed canonical bound can only improve the generic bound.
    assert absorption_bound(r)['bound'] <= Fraction(3*s+3,4)
    assert absorption_rank_bound(r)['bound'] <= Fraction(9*s+5,8)
    return dict(seed=w,a=a,t=t,depth=depth,lowered_endpoint=s,endpoint=r,
                t_residue=first,t_period=period,
                seed_residue=(2**a*first-1)//3,seed_period=9*2**a*binary)
