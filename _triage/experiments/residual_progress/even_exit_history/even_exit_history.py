"""Exact even-exit history cone; all terminal currents remain premises."""
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('even_exit_basis', HERE.parent/'critical_basis/critical_basis.py')
B = module_from_spec(spec)
spec.loader.exec_module(B)
N = B.NORMAL
combine, atoms, divergence = B.combine, B.atoms, B.divergence


def integer(x, minimum=0):
    if type(x) is not int or x < minimum:
        raise ValueError('Require an integer at least '+str(minimum))


def least_closing_half(H, max_bits=50000):
    integer(H, 4); integer(max_bits, 1)
    if 5*H+8 > max_bits:
        raise ValueError('Exponent comparison cap exceeded')
    low, high = 1, 2*H
    assert 3**(H+high) < 2**(H+2*high+2)
    while low < high:
        middle = (low+high)//2
        if 3**(H+middle) < 2**(H+2*middle+2):
            high = middle
        else:
            low = middle+1
    return low


def parameters(H, b, t, max_bits=50000):
    integer(H, 3); integer(b, 1); integer(t, 1); integer(max_bits, 1)
    if t % 2 == 0 or H+2*b+t.bit_length()+8 > max_bits:
        raise ValueError('Require odd t within the materialization cap')
    q = 2**H*t-1
    numerator = 3**(H-1)*t-1
    if q % 3 or numerator % 4**b:
        raise ValueError('The source or even-exit congruence fails')
    u = numerator//4**b
    n = 3**b*u
    if u <= 0 or u % 2 == 0 or n % 8 != 1:
        raise ValueError('Require exact even depth and canonical one-modulo-eight half')
    f, y = 2*n+1, (3*n+1)//4
    if max(q,n,f,y).bit_length() > max_bits:
        raise ValueError('State materialization cap exceeded')
    w = q//3
    assert N.canonical(q) and w % 8 == 5 and B.rho(w) == q
    assert N.valuation2(q+1) == H and N.valuation2(numerator) == 2*b
    assert N.selected(f) and N.normal_form(f) == n and N.step(n) == y
    assert y % 3 == 1 and q % 3 == 0
    slope = Fraction(3**(H+b),2**(H+2*b+2))
    assert (y < q) == (slope < 1) and y != q
    return dict(seed=w, rank=q, H=H, b=b, t=t, u=u, n=n, f=f, y=y,
                slope=[slope.numerator,slope.denominator], raw_descending=y<q,
                quotient_length=H+b, ordinary_clocks=[H+b+1,1])


def family(H, b, D, unit=1, index=0, max_bits=50000):
    integer(H, 3); integer(b, 1); integer(D, 1); integer(index); integer(max_bits, 1)
    if type(unit) is not int or unit not in (1,2):
        raise ValueError('Require the exact ternary terminal unit1 or2')
    if H+2*b+2*D+index.bit_length()+12 > max_bits:
        raise ValueError('CRT materialization cap exceeded')
    m2, m3 = 2**(2*b+3), 3**(D+1)
    residue2 = ((1+4**b*pow(3,-b,8))*pow(3,1-H,m2)) % m2
    residue3 = ((1+unit*3**D)*pow(2,-H,m3)) % m3
    residue = residue2+m2*((residue3-residue2)*pow(m2,-1,m3) % m3)
    t = residue+index*m2*m3
    data = parameters(H,b,t,max_bits)
    assert data['rank'] % 3**D == 0 and data['rank']//3**D % 3 == unit
    return dict(data, D=D, ternary_unit=unit, index=index,
                t_residue=residue,t_period=m2*m3,seed_period=2**H*m2*3**D)


def minimal_family(H, D, unit=1, index=0, max_bits=50000):
    b = least_closing_half(H, max_bits)
    data = family(H,b,D,unit,index,max_bits)
    assert data['n'] > data['rank'] > data['y']
    return dict(data, minimal_closing_half=True)


def comparison(H,b,t,max_bits=50000):
    data = parameters(H,b,t,max_bits)
    x, current, path = data['rank'], {}, [data['rank']]
    word = [1]*(H-1)+[2]*b
    for e in word:
        assert N.valuation2(3*x+1) == e and N.canonical(x)
        current = combine((1,current),(1,atoms((1,x))))
        x = N.step(x); path.append(x)
    assert x == data['f']
    for _ in range(2):
        current = combine((1,current),(1,atoms((1,x))))
        x = N.step(x); path.append(x)
    assert path[-2] == N.F(data['y']) and x == N.step(data['y'])
    current = combine((1,current),(-1,atoms((1,data['y']))))
    assert divergence(current) == atoms((1,data['rank']),(-1,data['y']))
    qx = data['rank']
    for _ in range(data['quotient_length']):
        qx = N.quotient_step(qx)
    assert qx == N.normal_form(data['y'])
    actual_word = [N.valuation2(3*x+1) for x in path[:-1]]
    assert actual_word[:-2] == word and actual_word[-2] == 1
    assert actual_word[-1] == N.valuation2(3*data['y']+1)+2
    return dict(data, comparison=current, ordinary_path=path,
                ordinary_word=actual_word, ordinary_meeting=x,
                terminal=N.normal_form(data['y']))


def plan(H,b,t,max_bits=50000):
    data = comparison(H,b,t,max_bits)
    high, low = B.absorption_plan(data['y']), B.absorption_plan(data['seed'])
    current = combine((1,data['comparison']),(1,high['current']),(-1,low['current']))
    coefficients = combine((1,high['coefficients']),(-1,low['coefficients']))
    answer = dict(data,current=current,coefficients=coefficients,
                  status='descending' if data['raw_descending'] else 'outside_raw_cone',
                  rule='even_exit_history_cone')
    B.check_boundary(answer)
    if data['raw_descending']:
        B.validate(answer)
    return answer


def compile_plan(data,supplied):
    if data.get('status') != 'descending' or not data.get('raw_descending'):
        raise ValueError('This constructor accepts only its proved raw-target cone')
    B.validate(data)
    return B.compile_plan(data,supplied)


def old_unrecognized_family(index=0):
    integer(index)
    w = 293+4608*index
    data = plan(4,1,(3*w+1)//16)
    assert data['seed'] == w and data['n'] == 1113+17496*index
    assert data['y'] == 835+13122*index and data['rank'] == 879+13824*index
    assert w % 9 == 5 and N.valuation2(data['n']+1) == 1
    assert Fraction(27*data['n']+29,32) > data['rank']
    return dict(data, progression_index=index,old_seventeen_unrecognized=True)
