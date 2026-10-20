"""Exact variable-depth inverse descent and a complete fixed-phase barrier.

Conditional W5 plans retain their missing inputs.  The barrier uses the
canonical quotient clock; every actual current uses ordinary Syracuse arrows.
"""
from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('escape_critical', HERE.parent/'critical_inverse/critical_inverse.py')
C = module_from_spec(spec)
spec.loader.exec_module(C)
T, NORMAL = C.T, C.NORMAL
combine, atoms, divergence = C.combine, C.atoms, C.divergence


def spine_parameters(q):
    """Complete arithmetic data for D inverse-2 steps, then j inverse-1 steps.

    D and j are the maximal initial block lengths.  Descent is equivalent to
    the exact integer slope test; no search or real logarithm is used.
    """
    NORMAL._odd(q)
    if q <= 1 or not NORMAL.canonical(q) or q % 3 != 1:
        raise ValueError('Require canonical q>1 with q=1 modulo3')
    D = C.valuation3(q-1)
    unit = (q-1)//3**D
    spine = 4**D*unit+1
    j = C.valuation3(spine+1)
    p = 2**j*((spine+1)//3**j)-1
    numerator, denominator = 2**(2*D+j), 3**(D+j)
    assert q == 1+3**D*unit and unit % 2 == 0
    assert spine % 8 == 1 and NORMAL.canonical(spine)
    assert NORMAL.canonical(p)
    assert NORMAL.valuation2(p+1) == j+1
    assert (p < q) == (numerator < denominator)
    return dict(q=q, D=D, unit=unit, j=j, spine=spine, p=p,
                slope=[numerator,denominator], descending=p<q)


def spine_bridge(q):
    """Exact ordinary current [q]-[p] with word 1^j,2^D, whether or not p<q."""
    data = spine_parameters(q)
    word = [1]*data['j']+[2]*data['D']
    x, path, current = data['p'], [data['p']], Counter()
    for a in word:
        assert NORMAL.valuation2(3*x+1) == a
        if x != 1:
            current[x] -= 1
        x = NORMAL.step(x)
        path.append(x)
        assert NORMAL.canonical(x)
    assert x == q
    current = combine((1,current))
    assert divergence(current) == atoms((1,q),(-1,data['p']))
    return dict(data, word=word, path=path, current=current)


def pair_parameters(w):
    NORMAL._odd(w)
    if w % 8 != 5 or not NORMAL.selected(3*w):
        raise ValueError('Require w=5 modulo8 and selected3w')
    q = (3*w-1)//2
    data = spine_parameters(q)
    if data['j'] < 2 or not data['descending']:
        raise ValueError('Require j>=2 and 2^(2D+j)<3^(D+j)')
    assert data['p'] % 8 == 7 and C.T.critical(q)
    data.update(w=w)
    return data


def recognized(w):
    try:
        pair_parameters(w)
    except ValueError:
        return False
    return True


def pair_plan(w):
    """Exact P(w) plan with every missing input in W5 and strictly below w."""
    data = pair_parameters(w)
    bridge = spine_bridge(data['q'])
    step = T.critical_step(data['p'])
    lower, child = step['lower'], step['pair']
    assert lower < w and (child is None or child % 8 == 5)
    z = NORMAL.normal_form(w)
    assert z < w
    high, low = C.absorption_five_plan(lower), C.absorption_five_plan(z)
    current = combine((1,NORMAL.bridge(3*w)['current']), (1,bridge['current']),
                      (1,step['current']), (-1,NORMAL.bridge(w)['current']),
                      (1,high['current']), (-1,low['current']))
    coefficients = Counter(high['coefficients'])
    for v,c in low['coefficients'].items():
        coefficients[v] -= c
    if child is not None:
        coefficients[child] += 1
    coefficients = C.NINE.clean(coefficients)
    assert all(v % 8 == 5 and v < w for v in coefficients)
    assert all(T.critical_image(v) < data['q'] for v in coefficients)
    expected = T.pair_source(w)
    for v,c in coefficients.items():
        expected = combine((1,expected),(-c,T.pair_source(v)))
    assert divergence(current) == expected
    return dict(seed=w,rho=data['q'],current=current,coefficients=coefficients,parameters=data,
                lower=lower,child=child,other_absorption=z)


def compile_plan(plan, supplied):
    if any(v % 8 != 5 or v >= plan['seed'] for v in plan['coefficients']):
        raise ValueError('Every requested W5 input must be strictly smaller')
    if plan['rho'] != T.critical_image(plan['seed']) or any(
            T.critical_image(v) >= plan['rho'] for v in plan['coefficients']):
        raise ValueError('Every requested critical image must be strictly smaller')
    return C.NINE.compile_five_plan(plan,supplied)


def parameter_witness(D,j,index=0):
    """An infinite CRT class with exact block lengths and fixed q=7 modulo32."""
    if not isinstance(D,int) or D < 1 or not isinstance(j,int) or j < 1:
        raise ValueError('Require positive block lengths')
    if not isinstance(index,int) or index < 0:
        raise ValueError('Require a nonnegative family index')
    # 4^D*u+2 = 3^j modulo3^(j+1) forces exact j and u=1 modulo3.
    ternary = 3**(j+1)
    u3 = ((3**j-2)*pow(4**D,-1,ternary)) % ternary
    u2 = (6*pow(3**D,-1,32)) % 32
    unit = u2+32*((u3-u2)*pow(32,-1,ternary) % ternary)
    unit += 32*ternary*index
    q = 1+3**D*unit
    w = (2*q+1)//3
    data = spine_parameters(q)
    assert data['D'] == D and data['j'] == j and q % 32 == 7
    assert w % 64 == 5 and NORMAL.selected(3*w)
    return dict(D=D,j=j,index=index,q=q,w=w,unit=unit,
                q_period=32*3**(D+j+1),descending=data['descending'])


def anchor_witness(D,index=1):
    """Fixed v3(q-1)=1, with arbitrary precision around canonical7."""
    if not isinstance(D,int) or D < 2 or not isinstance(index,int) or index < 1:
        raise ValueError('Require D>=2 and a positive family index')
    q = 7+32*3**D*index
    w = (2*q+1)//3
    assert C.valuation3(q-1) == 1 and q % 32 == 7 and T.critical(q)
    assert w % 64 == 5 and w % 3 == 2 and NORMAL.selected(3*w)
    first, second = (3*q+1)//2, (9*q+5)//4
    assert NORMAL.quotient_step(q) == first and NORMAL.quotient_step(first) == second
    return dict(D=D,index=index,q=q,w=w,forward=[q,first,second])


def anchor_inverse_lift(D,index,k,word):
    """Audit an arbitrary all-ray inverse word after k=0,1,2 forward steps.

    Legal up to D+k quotient inverse steps.  Returns full exact states; no
    enumeration is represented as exhaustion of the unbounded inverse rays.
    """
    data = anchor_witness(D,index)
    if k not in (0,1,2) or not 1 <= len(word) <= D+k:
        raise ValueError('Require k=0,1,2 and 1<=word length<=D+k')
    anchor = (7,11,17)[k]
    actual, shadow, slope = data['forward'][k], anchor, Fraction(1)
    scale = Fraction(3,2)**k
    states = []
    for depth,(kind,ray_index) in enumerate(word,1):
        assert actual % 3 == shadow % 3
        old_gap = slope-Fraction(shadow+1,anchor+1)
        actual,alpha,beta = C.inverse_step(actual,kind,ray_index)
        shadow,_,_ = C.inverse_step(shadow,kind,ray_index)
        slope *= alpha
        gap = slope-Fraction(shadow+1,anchor+1)
        assert gap == alpha*old_gap+(alpha-beta-1)/(anchor+1)
        assert shadow >= 7 and gap >= 0
        effective = scale*slope
        assert effective >= Fraction(shadow+1,8) >= 1
        assert actual == effective*(data['q']-7)+shadow >= data['q']
        equality = depth == k and all(kind0 == 'point' for kind0,_ in word[:depth])
        assert (actual == data['q']) == equality
        states.append(dict(depth=depth,state=actual,shadow=shadow,
                           slope=[slope.numerator,slope.denominator],
                           gap=[gap.numerator,gap.denominator]))
    return dict(D=D,index=index,k=k,q=data['q'],target=data['forward'][k],
                word=[[kind,j] for kind,j in word],states=states)
