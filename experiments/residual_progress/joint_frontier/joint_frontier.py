"""Exact unfinished frontiers for C(v)=delta_(18v+3)-delta_v.

Every loop is a prescribed finite prefix. No function searches for absorption
or treats an unresolved positive frontier as an absorption certificate.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('frontier_even_pairs', HERE.parent/'even_pair_closure/even_pairs.py')
E = module_from_spec(spec)
spec.loader.exec_module(E)
step, prefix, combine, divergence = E.step, E.prefix, E.combine, E.divergence
v2 = E.NORMAL.valuation2


def atom(x, weight=1):
    return {} if x == 1 or weight == 0 else {x: weight}


def _parameter(v):
    if not isinstance(v, int) or v <= 0 or v % 4 != 3:
        raise ValueError('Require a positive integer v=3 modulo4')


def interface(v):
    """Complete two-arrow arithmetic interface, retaining both sources."""
    _parameter(v)
    if v % 8 == 3:
        a = v2((9*v+5)//2)
        z = (9*v+5)//2**(a+1)
        y = 9*2**(a-1)*z-7
        kind, left_word, right_word = '3mod8', [2, 1], [1, a]
    else:
        z = (9*v+5)//4
        a = v2(9*z-7)
        y = (9*z-7)//2**a
        kind, left_word, right_word = '7mod8', [2, a+1], [1, 1]
    left, L = prefix(18*v+3, 2)
    right, R = prefix(v, 2)
    assert (left[-1], right[-1]) == (y, z)
    current = combine((1, L), (-1, R))
    residual = combine((1, atom(y)), (-1, atom(z)))
    source = {18*v+3: 1, v: -1}
    assert combine((1, divergence(current)), (1, residual)) == source
    return dict(v=v, kind=kind, exponent=a, upper=y, lower=z,
                upper_word=left_word, lower_word=right_word,
                current=current, residual=residual)


def shadow_frontier(v):
    """Exhaust the binary exponent for every v=3 modulo32."""
    _parameter(v)
    if v % 32 != 3:
        raise ValueError('Require v=3 modulo32')
    t = (3*v-1)//8
    h = v2(3*t+1)
    u = step(t)
    j = (h-2)//3
    s = h-1-3*j
    q = 2**s*3**(2*j+3)*u-5
    clock = 3+2*j
    left, L = prefix(18*v+3, clock)
    right, R = prefix(v, 2)
    assert left[-1] == q and right[-1] == u
    assert h >= 2 and s in (1, 2, 3) and 3*u <= v
    assert v == (2**(h+3)*u-5)//9 and 2**h*u % 9 == 4
    current = combine((1, L), (-1, R))
    residual = combine((1, atom(q)), (-1, atom(u)))
    assert combine((1, divergence(current)), (1, residual)) == {18*v+3: 1, v: -1}
    return dict(v=v, t=t, h=h, u=u, blocks=j, exponent=s, frontier=q,
                upper_clock=clock, lower_clock=2,
                upper_word=[2, 1, 2]+[1, 2]*j, lower_word=[1, h+2],
                current=current, residual=residual)


def expanding_family(r):
    if not isinstance(r, int) or r < 0:
        raise ValueError('Require an integer r>=0')
    v = (2**(6*r+5)-5)//9
    data = shadow_frontier(v)
    q = 2*3**(4*r+3)-5
    assert data['u'] == 1 and data['h'] == 6*r+2
    assert data['frontier'] == q and data['upper_clock'] == 4*r+3
    assert q % 8 == 1 and q % 27 == 22
    assert E.NORMAL.normal_form(q) == q
    return dict(r=r, **data)


def embedded_family(r):
    """Actual complementary d4 seed; its half has a four-arrow certificate."""
    if not isinstance(r, int) or r < 0 or r % 9:
        raise ValueError('Require an integer r>=0 divisible by9')
    data = expanding_family(r)
    v, h, q = data['v'], data['h'], data['frontier']
    assert v % 9 == 3
    w = 16*v//3+1
    t = (16*w+1)//3
    x = 4*t-1
    lower = (x-1)//2
    a0, t0, d0, w0 = E.RUN.parameters(x)
    assert (a0, t0, d0, w0) == (2, t, 4, w)
    assert t % 4 == 3 and w % 128 == 17 and w % 3 == 2
    clock = 4*r+7
    left, L = prefix(x, clock)
    right, R = prefix(lower, 4)
    assert left[-1] == q and right[-1] == 1
    assert right == [lower, w, E.NORMAL.F(v), step(v), 1]
    current = combine((1, L), (-1, R))
    residual = atom(q)
    assert combine((1, divergence(current)), (1, residual)) == {x: 1, lower: -1}
    assert divergence(R) == {lower: 1}
    return dict(r=r, v=v, h=h, w=w, t=t, root=x, lower=lower,
                frontier=q, clock=clock, lower_word=[5, 2, 3, h+2],
                upper_word=[1, 2, 2, 1, 3, 3, 2]+[1, 2]*(2*r),
                current=current, residual=residual, lower_current=R,
                upper_current=L)


def required_ray_family(r):
    """An actual weight1 R_N root, with an unresolved positive frontier."""
    if not isinstance(r, int) or r < 27 or r % 27:
        raise ValueError('Require a positive multiple of27')
    data = embedded_family(r)
    N = 12*2**(6*r+5)
    x = data['root']
    assert x == (2**(6*r+15)-3365)//81
    assert x % 12 == 3 and N < x and 8*x < 9*N
    assert E.RUN.H.TRANSFER.residual_coefficient(N, x) == 1
    assert data['lower'] < N < x < data['frontier']
    return dict(N=N, weight=1, **data)
