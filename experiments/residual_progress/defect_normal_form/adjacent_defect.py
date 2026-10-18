"""Exact adjacent-source interface for the entire returning absorption defect.

This is a change of conditional source basis, not a new accepted pair domain.
No unknown orbit is searched. Adjacent sources and all missing helpers remain
explicit until exact currents are supplied.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, relative):
    spec = spec_from_file_location(name, HERE.parent / relative)
    result = module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


RANK = load('adjacent_rank', 'critical_rank/rank_closure.py')
EXACT = load('adjacent_exact', 'exact_absorption_bound/exact_bound.py')
RETURN = load('adjacent_return', 'returning_phase/returning_phase.py')
NORMAL, T = RANK.NORMAL, RANK.T
combine, atoms, divergence = RANK.combine, RANK.atoms, RANK.divergence


def eligible(w):
    return isinstance(w, int) and w > 0 and w % 8 == 5 and w % 9 == 3 and NORMAL.selected(3*w)


def adjacent_source(q):
    if not isinstance(q, int) or q <= 0 or q % 108 != 31 or not NORMAL.canonical(q):
        raise ValueError('Require a positive canonical q31 modulo108')
    return atoms((1, q+2), (-1, q))


def parameters(w):
    if not eligible(w):
        raise ValueError('Require the complete returning E row')
    q, n, z = RANK.rho(w), 4*w//3-1, (w-1)//4
    assert q % 108 == 31 and NORMAL.canonical(q)
    assert n % 96 == 27 and NORMAL.canonical(n)
    assert q == (9*n+5)//8 and z == (q-1)//6
    assert NORMAL.step(NORMAL.step(n)) == q
    assert not NORMAL.canonical(3*z)
    exception = EXACT.absorption_bound(n)['exception']
    assert exception and exception['index'] == w
    return dict(seed=w, rank=q, height=n, lower=z, adjacent_upper=q+2)


def defect_plan(w):
    """P(w)=div(current)-A(q)+sum coefficients[u] P(u), all rho(u)<height."""
    data = parameters(w)
    q, n = data['rank'], data['height']
    lower = NORMAL.normal_form(w)
    upper_plan, lower_plan = RANK.absorption_plan(q+2), RANK.absorption_plan(lower)
    current = combine((1, NORMAL.bridge(3*w)['current']),
                      (-1, NORMAL.bridge(w)['current']),
                      (1, upper_plan['current']), (-1, lower_plan['current']))
    coefficients = Counter(upper_plan['coefficients'])
    coefficients.subtract(lower_plan['coefficients'])
    coefficients = RANK.NINE.clean(coefficients)
    assert all(4*RANK.rho(u) <= 3*q+7 < 4*n for u in coefficients)
    expected = combine((1, T.pair_source(w)), (1, adjacent_source(q)))
    for u, c in coefficients.items():
        expected = combine((1, expected), (-c, T.pair_source(u)))
    assert divergence(current) == expected
    return dict(data, current=current, coefficients=coefficients, adjacent={q:-1})


def mixed_absorption(seed, max_nodes=None):
    """Eliminate all E-return requests; leave a height-bounded mixed source basis.

    This terminates by strict original-rho descent of each replacement. It
    does not supply any remaining P or adjacent current. A cap rejects an
    unfinished computation rather than discarding its missing inputs.
    """
    NORMAL._odd(seed)
    base = RANK.absorption_plan(seed)
    current, pairs, adjacent = base['current'], Counter(base['coefficients']), Counter()
    expanded = []
    while True:
        candidates = [u for u, c in pairs.items() if c and eligible(u)]
        if not candidates:
            break
        if max_nodes is not None and len(expanded) >= max_nodes:
            raise RuntimeError('Mixed-basis cap reached with unresolved requests')
        u = max(candidates, key=RANK.rho)
        c = pairs.pop(u)
        plan = defect_plan(u)
        current = combine((1, current), (c, plan['current']))
        adjacent[plan['rank']] -= c
        for v, coefficient in plan['coefficients'].items():
            pairs[v] += c*coefficient
        expanded.append([u, c])
    pairs, adjacent = RANK.NINE.clean(pairs), RANK.NINE.clean(adjacent)
    n = NORMAL.normal_form(seed)
    assert all(not eligible(u) and RANK.rho(u) <= n for u in pairs)
    assert all((8*q-5)//9 <= n for q in adjacent)
    expected = atoms((1, seed))
    for u, c in pairs.items():
        expected = combine((1, expected), (-c, T.pair_source(u)))
    for q, c in adjacent.items():
        expected = combine((1, expected), (-c, adjacent_source(q)))
    assert divergence(current) == expected
    return dict(seed=seed, height=n, current=current, coefficients=pairs,
                adjacent=adjacent, expanded=expanded)


def compile_defect(plan, adjacent_current, supplied):
    """Require the unresolved adjacent current and every exact smaller helper."""
    if any(not isinstance(x, int) or not isinstance(c, int) for x, c in adjacent_current.items()):
        raise ValueError('Require an integer adjacent current')
    if divergence(adjacent_current) != adjacent_source(plan['rank']):
        raise ValueError('Missing or incorrect adjacent-current boundary')
    result = dict(plan, current=combine((1, plan['current']), (-1, adjacent_current)))
    RANK.validate_step(plan['seed'], result)
    return RANK.compile_plan(result, supplied)


def compile_adjacent(plan, pair_current, supplied):
    """Inverse conversion: exact P(w) plus the same helpers supplies A(q)."""
    if any(not isinstance(x, int) or not isinstance(c, int) for x, c in pair_current.items()):
        raise ValueError('Require an integer pair current')
    if divergence(pair_current) != T.pair_source(plan['seed']):
        raise ValueError('Missing or incorrect original pair-current boundary')
    current = combine((1, plan['current']), (-1, pair_current))
    for u, c in plan['coefficients'].items():
        if u not in supplied or divergence(supplied[u]) != T.pair_source(u):
            raise ValueError('Missing or incorrect smaller pair current')
        if any(not isinstance(x, int) or not isinstance(v, int) for x, v in supplied[u].items()):
            raise ValueError('Require integer smaller pair currents')
        current = combine((1, current), (c, supplied[u]))
    assert divergence(current) == adjacent_source(plan['rank'])
    return current


def inverse_g(q):
    """For the scoped audit: maximal canonical inverses of ordinary word(1,2)."""
    NORMAL._odd(q)
    if not NORMAL.canonical(q):
        raise ValueError('Require a canonical input')
    x, current, k = q, Counter(), 0
    while (x+5) % 9 == 0:
        p = (8*x-5)//9
        middle = NORMAL.step(p)
        assert NORMAL.canonical(p) and p < x
        assert NORMAL.valuation2(3*p+1) == 1
        assert NORMAL.valuation2(3*middle+1) == 2
        assert NORMAL.step(middle) == x
        current[p] -= 1
        current[middle] -= 1
        x, k = p, k+1
    current = combine((1, current))
    assert x+5 == 8**k*(q+5)//9**k
    assert divergence(current) == atoms((1, q), (-1, x))
    return dict(seed=q, minimum=x, count=k, current=current)


def transported_old_counterexample():
    """The old accepted4629 rule still expands the new adjacent-source height."""
    old = RETURN.forward_plan(4629)
    new = defect_plan(4629)
    assert old['status'] == 'descending'
    current = combine((1, new['current']), (-1, old['current']))
    coefficients = Counter(new['coefficients'])
    coefficients.subtract(old['coefficients'])
    coefficients = RANK.NINE.clean(coefficients)
    assert coefficients[2197] == -1
    assert not eligible(2197)
    assert RANK.rho(2197) == 6591 > new['height'] == 6171
    expected = adjacent_source(new['rank'])
    for u, c in coefficients.items():
        expected = combine((1, expected), (-c, T.pair_source(u)))
    assert divergence(current) == expected
    return dict(parent_height=new['height'], adjacent_index=new['rank'],
                child=2197, child_rank=6591, coefficient=-1,
                current=current, coefficients=coefficients)
