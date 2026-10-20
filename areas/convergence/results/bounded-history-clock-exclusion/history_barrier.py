"""Exact bounded-future/all-ray smaller-history barriers.

The theorem bounds two clocks; it does not deny deeper histories or absorption.
No unknown orbit search is used by the arithmetic certificate constructor.
"""
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = spec_from_file_location('history_barrier_normal', HERE.parent/'bridge_normal_form/normal_form.py')
N = module_from_spec(_spec)
_spec.loader.exec_module(N)
BASES = {0: {'ray0': (8, 3), 'ray1': (16, 3)},
         1: {'ray0': (4, -1), 'ray1': (32, 19)},
         2: {'point': (2, -1), 'ray0': (64, 19), 'ray1': (128, 83)}}


def integer(x, minimum=0):
    return type(x) is int and x >= minimum


def ordinary_targets(q, J):
    if not integer(q, 1) or q % 2 == 0 or not integer(J):
        raise ValueError('Require a positive odd source and nonnegative horizon')
    out = [q]
    for _ in range(J):
        if N.valuation2(3*out[-1]+1) != 1:
            raise ValueError('The prescribed valuation-one prefix fails')
        out.append(N.step(out[-1]))
    assert out[-1]+1 == Fraction(3, 2)**J*(q+1)
    return out


def certificate(q, D, J, quotient=True):
    if type(quotient) is not bool or not integer(D, 1):
        raise ValueError('Require a positive ternary depth and a Boolean clock choice')
    targets = ordinary_targets(q, J)
    if q % 3**D:
        raise ValueError('Insufficient ternary divisibility')
    if quotient and any(not N.canonical(x) for x in targets):
        raise ValueError('The quotient version requires the full canonical prefix')
    return dict(source=q, ternary_depth=D, future_horizon=J, targets=targets,
                inverse_horizons=[D+a for a in range(J+1)],
                clock='quotient' if quotient else 'ordinary',
                conclusion='The only origins at most q are q itself, at depth a for target a')


def family(D, J, index=0, H=None):
    if not integer(D, 1) or not integer(J) or not integer(index):
        raise ValueError('Require D>=1,J>=0 and a nonnegative progression index')
    if H is None:
        H = max(J+1, 3)
    if not integer(H, max(J+1, 3)):
        raise ValueError('Require H>=max(J+1,3)')
    modulus2 = 2**(H+2)
    residue2 = (1 if H % 2 else 3)*2**H-1
    modulus3 = 3**D
    residue = residue2+modulus2*((-residue2)*pow(modulus2, -1, modulus3) % modulus3)
    q = residue+index*modulus2*modulus3
    out = certificate(q, D, J)
    assert N.valuation2(q+1) == H and q//3 % 8 == 5
    return dict(out, seed=q//3, binary_order=H, residue=residue,
                modulus=modulus2*modulus3, index=index)


def h17_family(D, r, index=0):
    if not integer(D, 1) or not integer(r) or not integer(index):
        raise ValueError('Require D>=1,r>=0 and a nonnegative progression index')
    modulus2 = 2**(9*r+18)
    residue2 = ((2**(9*r+17)-223)*pow(217, -1, modulus2)) % modulus2
    modulus3 = 3**(D-1)
    residue = residue2+modulus2*((-residue2)*pow(modulus2, -1, modulus3) % modulus3)
    b = residue+index*modulus2*modulus3
    out = certificate(3*b, D, 1)
    assert N.valuation2(217*b+223) == 9*r+17 and b % 16 == 9
    return dict(out, seed=b, returns=r, residue=residue,
                modulus=modulus2*modulus3, index=index)


def inverse_affine(residue, kind, L=0, max_bits=50000):
    if not integer(residue) or residue not in BASES or not isinstance(kind, str) or kind not in BASES[residue]:
        raise ValueError('Invalid inverse branch')
    if not integer(L) or (kind == 'point' and L) or not integer(max_bits, 1):
        raise ValueError('Invalid ray index or bit cap')
    if 6*L+8 > max_bits:
        raise ValueError('Ray materialization cap exceeded')
    A, B = BASES[residue][kind]
    factor = 64**L
    alpha = Fraction(factor*A, 3)
    beta = Fraction(factor*B, 3)+49*((factor-1)//63)
    assert alpha-beta >= 1 and alpha >= Fraction(2, 3)
    return alpha, beta


def inverse_trace(q, D, a, word, max_bits=50000):
    data = certificate(q, D, a)
    if not isinstance(word, (tuple, list)) or len(word) > D+a:
        raise ValueError('Inverse word exceeds the stated ternary horizon')
    x = data['targets'][a]
    slope, shadow = Fraction(3, 2)**a, Fraction(3, 2)**a-1
    off_spine = False
    trace = []
    for depth, symbol in enumerate(word, 1):
        if not isinstance(symbol, (tuple, list)) or len(symbol) != 2:
            raise ValueError('Require (branch,ray_index) symbols')
        kind, L = symbol
        alpha, beta = inverse_affine(x % 3, kind, L, max_bits)
        previous = x
        value = alpha*x+beta
        if value.denominator != 1:
            raise ValueError('Nonintegral inverse state')
        x = value.numerator
        if x.bit_length() > max_bits:
            raise ValueError('Inverse state materialization cap exceeded')
        assert N.canonical(x) and N.quotient_step(x) == previous
        slope, shadow = alpha*slope, alpha*shadow+beta
        assert x == slope*q+shadow and slope-shadow >= 1
        if kind != 'point':
            off_spine = True
        if off_spine:
            assert shadow > 0 and x > q
        else:
            assert depth <= a and x == data['targets'][a-depth]
        assert x >= q and (x == q) == (not off_spine and depth == a)
        trace.append(dict(depth=depth, state=x, slope=[slope.numerator,slope.denominator],
                          shadow=[shadow.numerator,shadow.denominator], off_spine=off_spine))
    return dict(source=q, future=a, word=[list(s) for s in word], endpoint=x, trace=trace)


def ordinary_candidate(q, D, a, word, max_bits=50000):
    data = certificate(q, D, a, quotient=False)
    if not isinstance(word, (list, tuple)) or any(not integer(e, 1) for e in word):
        raise ValueError('Require a finite positive valuation word')
    if len(word) > D+a:
        raise ValueError('Ordinary inverse word exceeds the clock bound')
    if not integer(max_bits, 1):
        raise ValueError('Require a positive materialization cap')
    x = data['targets'][a]
    for e in reversed(word):
        if x.bit_length()+e > max_bits:
            raise ValueError('Ordinary inverse state materialization cap exceeded')
        numerator = 2**e*x-1
        if numerator % 3:
            return None
        p = numerator//3
        if p <= 0 or p % 2 == 0 or N.valuation2(3*p+1) != e:
            return None
        x = p
    assert x >= q and (x == q) == (len(word) == a and all(e == 1 for e in word))
    return x
