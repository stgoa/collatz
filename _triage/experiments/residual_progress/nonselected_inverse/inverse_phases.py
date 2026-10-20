"""Complete base-ray phase classification for nonselected critical-five inputs.

All returned plans retain their missing pair currents. Universal supply is not
claimed. Two base quotient inverse branches are examined; higher ray indices
and other inverse words are not excluded by a failed base-branch plan.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('nonselected_rank', HERE.parent/'critical_rank/rank_closure.py')
RANK = module_from_spec(spec)
spec.loader.exec_module(RANK)
OLD = RANK.INVERSE
NINE, T, NORMAL = OLD.NINE, OLD.T, OLD.NORMAL
combine, atoms, divergence = T.combine, T.atoms, T.divergence
GOOD_FOUR = {47, 101, 128, 182, 209}
GOOD_EIGHT = {91, 577}
GOOD_729 = {r+243*j for r in GOOD_FOUR for j in range(3)} | GOOD_EIGHT
critical_rank = RANK.rho


def eligible(w):
    NORMAL._odd(w)
    return w % 8 == 5 and not NORMAL.selected(3*w)


def decreasing_domain(w):
    return eligible(w) and (w % 27 == 20 or w % 243 == 91)


def index_decreasing_domain(w):
    return eligible(w) and w % 729 in GOOD_729


def parameters(w, k):
    if not eligible(w) or k not in (4, 8):
        raise ValueError('Require w=5 modulo8, nonselected3w, and k=4 or8')
    h = OLD.valuation3(k*w+1)
    C = (k*w+1)//3**h
    b = 2*k*w+1
    p = 2**(h+1)*C-1
    assert NORMAL.canonical(3*w) and NORMAL.canonical(b)
    if h == 0:
        assert p == b
        return dict(w=w, k=k, h=h, C=C, predecessor=b, lower=p,
                    child=None, residue=None, index_shrinking=False,
                    rank_shrinking=False, child_domain=None, parent_rank=3*w)
    assert NORMAL.canonical(p) and p % 4 == 3 and p % 3 in (0, 1)
    v = T.critical_inverse(p)
    residue = p % 3
    threshold = {(4, 0): 3, (4, 1): 5, (8, 0): 5, (8, 1): 6}[k, residue]
    index_shrinking = h >= threshold
    rank_shrinking = h >= (3 if k == 4 else 5)
    assert (v < w) == index_shrinking
    assert (p < 3*w) == rank_shrinking
    assert critical_rank(v) == p
    assert v != w
    domain = 'W9' if v % 16 == 9 else 'W5'
    assert (domain == 'W9') == (h == 1 and residue == 0)
    if rank_shrinking:
        assert domain == 'W5'
    return dict(w=w, k=k, h=h, C=C, predecessor=b, lower=p,
                child=v, residue=residue, index_shrinking=index_shrinking,
                rank_shrinking=rank_shrinking, child_domain=domain,
                index_threshold=threshold, parent_rank=3*w, child_rank=p)


def inverse_bridge(w, k):
    """Exact signed current delta_(3w)-delta_p; T^(h+1)(p)=3w."""
    data = parameters(w, k)
    q, b, p, h = 3*w, data['predecessor'], data['lower'], data['h']
    end, path = NINE.prefix(p, h)
    assert end == b
    successor = NORMAL.step(b)
    bridge = NORMAL.bridge(successor)
    assert bridge['minimum'] == q
    forward = combine((1, {b: 1}), (1, bridge['current']))
    assert divergence(forward) == atoms((1, b), (-1, q))
    current = combine((-1, path), (-1, forward))
    assert divergence(current) == atoms((1, q), (-1, p))
    return dict(parameters=data, current=current)


def pair_plan(w, k):
    """Retain the exact W5 dependency vector, whether decreasing or unresolved."""
    inv = inverse_bridge(w, k)
    data = inv['parameters']
    if data['h'] == 0:
        raise ValueError('This base ray has no valuation1 inverse continuation')
    v, z = data['child'], NORMAL.normal_form(w)
    local = combine((1, inv['current']), (-1, NORMAL.bridge(3*v)['current']),
                    (-1, NORMAL.bridge(w)['current']))
    expected = combine((1, T.pair_source(w)), (-1, T.pair_source(v)),
                       (-1, atoms((1, v), (-1, z))))
    assert divergence(local) == expected
    child = NINE.five_plan(v)
    high, low = RANK.absorption_plan(v), RANK.absorption_plan(z)
    current = combine((1, local), (1, child['current']),
                      (1, high['current']), (-1, low['current']))
    coefficients = Counter(child['coefficients'])
    for u, c in high['coefficients'].items():
        coefficients[u] += c
    for u, c in low['coefficients'].items():
        coefficients[u] -= c
    coefficients = NINE.clean(coefficients)
    expected = T.pair_source(w)
    for u, c in coefficients.items():
        expected = combine((1, expected), (-c, T.pair_source(u)))
    assert divergence(current) == expected
    if data['rank_shrinking']:
        assert all(critical_rank(u) < 3*w for u in coefficients)
        if data['index_shrinking']:
            assert all(u < w for u in coefficients)
    elif data['child_domain'] == 'W9':
        assert coefficients == {w: 1} and not current
    else:
        assert coefficients[v] == 1
        assert all(critical_rank(u) < data['lower'] for u in coefficients if u != v)
        assert critical_rank(v) > 3*w
    return dict(seed=w, parameters=data, current=current, coefficients=coefficients,
                status='descending' if all(critical_rank(u) < 3*w for u in coefficients) else 'unresolved',
                absorption_seeds=[v, z])


def compile_plan(data, supplied):
    if data['status'] != 'descending':
        raise ValueError('The plan has a nondecreasing critical-rank dependency')
    RANK.validate_step(data['seed'], data)
    return RANK.compile_plan(data, supplied)


def decreasing_plan(w):
    if not decreasing_domain(w):
        raise ValueError('The seed is outside the proved decreasing domain')
    k = 4 if w % 3 == 2 else 8
    data = pair_plan(w, k)
    assert data['status'] == 'descending'
    return data
