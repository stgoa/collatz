"""A complete two-ray inverse interface on selected w=16 modulo27.

Finite formal plans retain every signed pair premise.  The two strict domains
do not cover this phase universally; failed plans retain their leading request.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('selected_inverse_rank', HERE.parent/'critical_rank/rank_closure.py')
RANK = module_from_spec(spec)
spec.loader.exec_module(RANK)
NINE, T, NORMAL = RANK.NINE, RANK.T, RANK.NORMAL
combine, atoms, divergence = RANK.combine, RANK.atoms, RANK.divergence


def eligible(w):
    NORMAL._odd(w)
    return w % 8 == 5 and w % 27 == 16 and NORMAL.selected(3*w)


def parameters(w, k):
    if not eligible(w) or k not in (4, 8):
        raise ValueError('Require selected3w, w=5 mod8 and16 mod27, k4 or8')
    q = (3*w-1)//2
    v = (16*w-13)//27
    p = 3*v
    h = RANK.INVERSE.valuation3(k*v+1)
    unit = (k*v+1)//3**h
    b, r = 2*k*v+1, 2**(h+1)*unit-1
    threshold = 3 if k == 4 else 5
    descending = h >= threshold
    assert q == (81*v+23)//32 and v % 128 == 121 and v >= 121
    assert p == (32*q-23)//27 and NORMAL.canonical(p)
    assert NORMAL.canonical(b) and NORMAL.canonical(r)
    assert (r < q) == descending
    assert r % 3 != 2 if h else True
    if h:
        assert NORMAL.valuation2(r+1) == h+1
    returning = h == 0 or (h == 1 and r % 3 == 0)
    return dict(seed=w, rank=q, first_inverse=p, nine_index=v, k=k, h=h,
                unit=unit, base=b, endpoint=r, threshold=threshold,
                descending=descending, returning=returning,
                word=[1]*h+([2,1,1,4] if k == 4 else [2,3,2,2]),
                ordinary_length=h+4, quotient_length=h+4)


def bridge(w, k):
    """Actual negative ordinary path [q]-[r], with exact length h+4."""
    data = parameters(w, k)
    x, path, current = data['endpoint'], [data['endpoint']], Counter()
    for a in data['word']:
        assert NORMAL.valuation2(3*x+1) == a
        if x != 1:
            current[x] -= 1
        x = NORMAL.step(x)
        path.append(x)
    assert x == data['rank']
    current = combine((1, current))
    assert divergence(current) == atoms((1, data['rank']), (-1, data['endpoint']))
    return dict(parameters=data, current=current, path=path)


def pair_plan(w, k):
    """Exact signed plan, retaining the leading request in every failed row."""
    inv = bridge(w, k)
    data, q, r = inv['parameters'], inv['parameters']['rank'], inv['parameters']['endpoint']
    z = NORMAL.normal_form(w)
    high, low = RANK.absorption_plan(r), RANK.absorption_plan(z)
    current = combine((1, NORMAL.bridge(3*w)['current']), (1, inv['current']),
                      (-1, NORMAL.bridge(w)['current']),
                      (1, high['current']), (-1, low['current']))
    coefficients = Counter(high['coefficients'])
    coefficients.subtract(low['coefficients'])
    coefficients = NINE.clean(coefficients)
    expected = T.pair_source(w)
    for u, c in coefficients.items():
        expected = combine((1, expected), (-c, T.pair_source(u)))
    assert divergence(current) == expected
    if data['descending']:
        status, leading = 'descending', None
        assert all(RANK.rho(u) < q for u in coefficients)
    elif data['returning']:
        status, leading = 'original_request', w
        assert coefficients[w] == 1
        assert all(RANK.rho(u) < q for u in coefficients if u != w)
    else:
        status, leading = 'higher_request', T.critical_inverse(r)
        assert leading % 8 == 5 and coefficients[leading] == 1 and RANK.rho(leading) == r > q
        assert all(RANK.rho(u) < r for u in coefficients if u != leading)
    result = dict(seed=w, rank=q, parameters=data, current=current,
                  coefficients=coefficients, status=status, leading=leading)
    if status == 'descending':
        RANK.validate_step(w, result)
    return result


def recognized(w):
    return eligible(w) and (w % 729 == 718 or w % 6561 == 4255)


def one_step(w):
    if not recognized(w):
        return None
    return pair_plan(w, 4 if w % 729 == 718 else 8)


def compile_plan(data, supplied):
    if data['status'] != 'descending':
        raise ValueError('The displayed plan retains a nondecreasing request')
    RANK.validate_step(data['seed'], data)
    return RANK.compile_plan(data, supplied)


def parameter_family(k, h, terminal_unit=1, index=0):
    """A full exact phase inside w3445mod3456, including both unit choices."""
    if k not in (4,8) or not isinstance(h,int) or h < 1 or terminal_unit not in (1,2):
        raise ValueError('Require k4/8, h>=1 and a nonzero ternary terminal unit')
    if not isinstance(index,int) or index < 0:
        raise ValueError('Require a nonnegative family index')
    modulus = 3**(h+1)
    residue = ((3**h*terminal_unit-1)*pow(k,-1,modulus)) % modulus
    first_v = 2041+2048*((residue-2041)*pow(2048,-1,modulus) % modulus)
    v = first_v+2048*modulus*index
    w = (27*v+13)//16
    data = parameters(w,k)
    assert data['h'] == h and data['unit'] % 3 == terminal_unit
    assert w % 3456 == 3445
    return dict(seed=w,k=k,h=h,terminal_unit=terminal_unit,index=index,
                v=v,v_residue=first_v,v_period=2048*modulus,
                seed_period=3456*modulus)


def avoidance_family(depth, k=4, h=None, terminal_unit=1, index=0):
    """Full CRT intersection with every prescribed R54 growing-prefix length."""
    if not isinstance(depth,int) or depth < 1 or k not in (4,8):
        raise ValueError('Require positive depth and k4/8')
    if h is None:
        h = 3 if k == 4 else 5
    if not isinstance(h,int) or h < (3 if k == 4 else 5) or terminal_unit not in (1,2):
        raise ValueError('Require an accepted exact h and terminal unit1/2')
    if not isinstance(index,int) or index < 0:
        raise ValueError('Require a nonnegative family index')
    K, modulus = 11*depth+6, 3**(h+1)
    residue = ((7*k-1+3**h*terminal_unit)*pow(k*2**(K+5),-1,modulus)) % modulus
    s = (residue or modulus)+modulus*index
    q = 81*2**K*s-17
    w = (2*q+1)//3
    data = parameters(w,k)
    assert data['h'] == h and data['descending'] and data['unit'] % 3 == terminal_unit
    return dict(seed=w,rank=q,depth=depth,k=k,h=h,terminal_unit=terminal_unit,
                s=s,s_residue=residue,s_period=modulus,binary_exponent=K,
                ordinary_inverse_length=h+4)
