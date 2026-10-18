"""Maximal negative-cycle inverse comparison on the R56 zero-depth row.

All returned currents are conditional. Failed plans retain an original or
strictly higher critical request; the constructor never searches an orbit.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('cycle_inverse_old', HERE.parent/'selected_inverse/selected_inverse.py')
OLD = module_from_spec(spec)
spec.loader.exec_module(OLD)
RANK, NORMAL, T, NINE = OLD.RANK, OLD.NORMAL, OLD.T, OLD.NINE
combine, atoms, divergence = OLD.combine, OLD.atoms, OLD.divergence
WORD = (1, 1, 1, 2, 1, 1, 4)


def eligible(w):
    return isinstance(w, int) and w > 0 and w % 3456 == 3445 and OLD.parameters(w, 4)['nine_index'] % 3 == 0


def point_threshold(k):
    if not isinstance(k, int) or k < 1:
        raise ValueError('Require a positive cycle count')
    return 3 if k <= 5 else 2 if k <= 11 else 1 if k <= 17 else 0


def parameters(w):
    if not eligible(w):
        raise ValueError('Require w3445mod3456 and v=(16w-13)/27 divisible by3')
    initial = OLD.parameters(w, 4)
    q, v = initial['rank'], initial['nine_index']
    b = 8*v+1
    h = RANK.INVERSE.valuation3(b+17)
    k, remainder = divmod(h, 7)
    if k == 0:
        return dict(seed=w, rank=q, v=v, base=b, ternary_depth=h,
                    cycles=0, remainder=remainder, endpoint=b, point_depth=0,
                    cycle_endpoint=b, descending=False, ordinary_length=4,
                    word=[2, 1, 1, 4])
    p = 2**(11*k)*(b+17)//3**(7*k)-17
    j = RANK.INVERSE.valuation3(p+1)
    eta = 2**j*(p+1)//3**j-1
    assert p > 0 and eta > 0 and NORMAL.canonical(p) and NORMAL.canonical(eta)
    assert NORMAL.valuation2(p+1) == 4
    assert NORMAL.valuation2(eta+1) == 4+j and eta % 3 != 2
    descending = j >= point_threshold(k)
    assert (eta < q) == descending and eta != q
    word = [1]*j + list(WORD)*k + [2, 1, 1, 4]
    return dict(seed=w, rank=q, v=v, base=b, ternary_depth=h,
                cycles=k, remainder=remainder, cycle_endpoint=p, point_depth=j,
                endpoint=eta, descending=descending, ordinary_length=len(word),
                word=word)


def bridge(w):
    data = parameters(w)
    x, path, current = data['endpoint'], [data['endpoint']], Counter()
    for a in data['word']:
        assert NORMAL.valuation2(3*x+1) == a
        current[x] -= 1
        x = NORMAL.step(x)
        path.append(x)
    assert x == data['rank']
    current = combine((1, current))
    assert divergence(current) == atoms((1, data['rank']), (-1, data['endpoint']))
    return dict(parameters=data, current=current, path=path)


def pair_plan(w):
    inv = bridge(w)
    data, eta, q = inv['parameters'], inv['parameters']['endpoint'], inv['parameters']['rank']
    z = NORMAL.normal_form(w)
    high, low = RANK.absorption_plan(eta), RANK.absorption_plan(z)
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
    elif data['cycles'] == 0:
        status, leading = 'original_request', w
        assert coefficients[w] == 1
        assert all(RANK.rho(u) < q for u in coefficients if u != w)
    else:
        status, leading = 'higher_request', T.critical_inverse(eta)
        assert leading % 8 == 5 and coefficients[leading] == 1
        assert RANK.rho(leading) == eta > q
        assert all(RANK.rho(u) < eta for u in coefficients if u != leading)
    result = dict(seed=w, rank=q, parameters=data, current=current,
                  coefficients=coefficients, status=status, leading=leading)
    if status == 'descending':
        RANK.validate_step(w, result)
    return result


def one_step(w):
    if not eligible(w) or not parameters(w)['descending']:
        return None
    return pair_plan(w)


def compile_plan(data, supplied):
    if data['status'] != 'descending':
        raise ValueError('The displayed plan retains a nondecreasing request')
    RANK.validate_step(data['seed'], data)
    return RANK.compile_plan(data, supplied)


def parameter_family(k, j, unit=1, index=0, avoidance_depth=None, remainder=0):
    """Full exact h=7k+remainder family; optional old-twelve exclusion."""
    if not isinstance(k, int) or k < 1 or not isinstance(j, int) or j < 0:
        raise ValueError('Require k>=1 and j>=0')
    if unit not in (1, 2) or not isinstance(index, int) or index < 0:
        raise ValueError('Require terminal unit1/2 and nonnegative index')
    if not isinstance(remainder, int) or not 0 <= remainder <= 6 or (remainder and j):
        raise ValueError('Require remainder0..6, and point-depth0 for a nonzero remainder')
    modulus3 = 3**(j+1)
    if remainder:
        modulus3 = 3**(remainder+1)
        residue3 = 3**remainder*unit
    elif j:
        residue3 = ((1+3**j*unit)*pow(2**(11*k-3), -1, modulus3)) % modulus3
    else:
        # The unique nonzero unit giving point-depth zero and exact h=7k.
        residue3 = (2*pow(2**(11*k-3), -1, 3)) % 3
    if avoidance_depth is None:
        bits, numerator = 13, -19
    else:
        if not isinstance(avoidance_depth, int) or avoidance_depth < 0:
            raise ValueError('Require nonnegative prescribed growth depth')
        L = avoidance_depth
        bits = 11*L+22
        numerator = 2**(11*L+20)*(1 if L % 2 == 0 else 3)-19
    modulus2 = 2**bits
    residue2 = numerator*pow(3**(7*k), -1, modulus2) % modulus2
    U0 = residue2+modulus2*((residue3-residue2)*pow(modulus2, -1, modulus3) % modulus3)
    U = (U0 or modulus2*modulus3)+modulus2*modulus3*index
    v = (3**(7*k)*U-9)//4
    w = (27*v+13)//16
    data = parameters(w)
    assert data['cycles'] == k and data['remainder'] == remainder and data['point_depth'] == j
    assert eligible(w)
    return dict(seed=w, k=k, j=j, unit=unit, index=index, U=U,
                U_residue=U0, U_period=modulus2*modulus3,
                avoidance_depth=avoidance_depth, remainder=remainder)
