"""Conditional current compilation in the full W5 union W9 critical basis.

Old sigma-valid W5 plans are translated, not retained as high-rho edges.
Unknown terminal pair currents remain supplied premises. No dispatcher changes.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('critical_basis_sigma', HERE.parent/'phase_rank/sigma_rank.py')
SIGMA = module_from_spec(spec)
spec.loader.exec_module(SIGMA)
RANK, T, NORMAL = SIGMA.RANK, SIGMA.T, SIGMA.NORMAL
NINE = RANK.NINE
combine, atoms, divergence = T.combine, T.atoms, T.divergence


def rho(w):
    if not isinstance(w, int) or isinstance(w, bool) or w <= 0 or not T.critical_domain(w):
        raise ValueError('Require a positive W5 or W9 pair index')
    return T.critical_image(w)


def absorption_plan(seed):
    """The unchanged R37 plan, retaining both critical pair types."""
    data = T.plan(seed)
    coefficients = dict(Counter(data['pairs']))
    minimum = NORMAL.normal_form(seed)
    assert all(rho(w) <= minimum for w in coefficients)
    out = dict(seed=seed, minimum=minimum, current=data['current'],
               coefficients=coefficients)
    expected = atoms((1, seed))
    for w, c in coefficients.items():
        expected = combine((1, expected), (-c, T.pair_source(w)))
    assert divergence(out['current']) == expected
    return out


def check_boundary(data):
    w = data['seed']
    rho(w)
    expected = T.pair_source(w)
    for u, c in data['coefficients'].items():
        rho(u)
        if not isinstance(c, int) or isinstance(c, bool) or not c:
            raise ValueError('Require nonzero signed integer critical requests')
        expected = combine((1, expected), (-c, T.pair_source(u)))
    for x, c in data['current'].items():
        if (not isinstance(x, int) or isinstance(x, bool) or x <= 1 or x % 2 != 1
                or not isinstance(c, int) or isinstance(c, bool) or not c):
            raise ValueError('Require integer current rows at positive odd states above1')
    if divergence(data['current']) != expected:
        raise ValueError('Incorrect full conditional pair boundary')
    return data


def validate(data):
    check_boundary(data)
    rank = rho(data['seed'])
    if any(rho(u) >= rank for u in data['coefficients']):
        raise ValueError('The plan does not strictly decrease critical rho')
    return data


def returning_conversion(u):
    """Complete E_return conversion; the unique highest child is in W9."""
    rho(u)
    if u % 8 != 5 or not SIGMA.RETURN.returning(u):
        raise ValueError('Require an E_return W5 input')
    q, n, b = (3*u-1)//2, (4*u-3)//3, (4*u-3)//9
    assert 3*b == n == SIGMA.sigma(u) and b % 16 == 9
    assert NORMAL.canonical(n) and NORMAL.canonical(q)
    x, path = n, {}
    for valuation in (1, 2):
        assert NORMAL.valuation2(3*x+1) == valuation
        path[x] = 1
        x = NORMAL.step(x)
    assert x == q and divergence(path) == atoms((1, n), (-1, q))
    upper, lower = absorption_plan(b), absorption_plan(u)
    current = combine((1, NORMAL.bridge(3*u)['current']), (-1, path),
                      (1, upper['current']), (-1, lower['current']))
    coefficients = combine((1, {b: 1}), (1, upper['coefficients']),
                           (-1, lower['coefficients']))
    assert coefficients[b] == 1 and rho(b) == n < q == rho(u)
    assert all(rho(v) < n for v in coefficients if v != b)
    out = dict(seed=u, rank=q, native_height=n, leading=b, current=current,
               coefficients=coefficients, inverse_word=[1, 2],
               inverse_path=[n, (3*n+1)//2, q], status='descending',
               rule='E_return_to_critical_nine')
    validate(out)
    return out


def translate_sigma(data):
    """Translate any sigma-valid W5 plan, retaining every signed multiplier."""
    w = data['seed']
    check_boundary(data)
    SIGMA.validate(w, data)
    current, coefficients, converted = data['current'], {}, []
    for u, c in data['coefficients'].items():
        if SIGMA.RETURN.returning(u):
            child = returning_conversion(u)
            current = combine((1, current), (c, child['current']))
            coefficients = combine((1, coefficients), (c, child['coefficients']))
            converted.append(dict(seed=u, coefficient=c, leading=child['leading'],
                                  native_height=child['native_height']))
        else:
            assert rho(u) == SIGMA.sigma(u)
            coefficients = combine((1, coefficients), (c, {u: 1}))
    assert all(rho(u) < SIGMA.sigma(w) <= rho(w) for u in coefficients)
    out = dict(seed=w, rank=rho(w), original_sigma_rank=SIGMA.sigma(w),
               current=current, coefficients=coefficients, converted=converted,
               status='descending', rule='translated_sigma')
    validate(out)
    return out


def retain_rho(data):
    """Every old rho-valid W5 plan remains valid, with identical rows/requests."""
    RANK.validate_step(data['seed'], data)
    out = dict(data, current=dict(data['current']), coefficients=dict(data['coefficients']),
               rank=rho(data['seed']), status='descending', rule='retained_old_rho')
    validate(out)
    return out


def nine_candidate(b):
    """Keep R40's local critical requests; an expanding row is not accepted."""
    data = NINE.local_plan(b)
    out = dict(data, rank=rho(b), high={u: c for u, c in data['coefficients'].items()
                                     if rho(u) >= rho(b)})
    expected_high = {data['exception']: 1} if data['d'] == 4 and data['exception'] else {}
    assert out['high'] == expected_high
    out['status'] = 'unresolved' if out['high'] else 'descending'
    check_boundary(out)
    if not out['high']:
        validate(out)
    return out


def blocked_nine(u):
    """The entire d4/E returning correspondence keeps a positive self-request.

    The residual lower current need not be zero; u453,b201 is a counterexample.
    """
    conversion = returning_conversion(u)
    b = conversion['leading']
    old = nine_candidate(b)
    assert old['d'] == 4 and old['exception'] == u and old['high'] == {u: 1}
    current = combine((1, old['current']), (1, conversion['current']))
    coefficients = combine((1, old['coefficients']), (-1, {u: 1}),
                           (1, conversion['coefficients']))
    assert coefficients[b] == 1
    assert all(rho(v) < rho(b) for v in coefficients if v != b)
    out = dict(seed=b, rank=rho(b), returning_index=u, current=current,
               coefficients=coefficients, high={b: 1}, status='unresolved')
    check_boundary(out)
    return out


def guarded_plan(w):
    """Entire R67 guard: retain the smaller critical-nine request, not its lift."""
    rho(w)
    if w % 2**26 != 40529845:
        raise ValueError('Require the complete R67 binary guard')
    q, f = 3*w, (729*w+147)//256
    b, u = f//3, (3*f+3)//4
    assert 3*b == f and b % 16 == 9 and SIGMA.RETURN.returning(u)
    assert rho(w) == q and w < f < q < rho(u)
    x, prefix = q, {}
    for valuation in (1, 1, 1, 1, 2):
        assert NORMAL.valuation2(3*x+1) == valuation
        prefix[x] = 1
        x = NORMAL.step(x)
    assert x == NORMAL.F(f)
    comparison = combine((1, prefix), (1, {x: 1}), (-1, {f: 1}))
    assert divergence(comparison) == atoms((1, q), (-1, f))
    upper, lower = absorption_plan(f), absorption_plan(w)
    current = combine((1, comparison), (1, upper['current']), (-1, lower['current']))
    coefficients = combine((1, upper['coefficients']), (-1, lower['coefficients']))
    assert coefficients[b] == 1 and rho(b) == f
    assert all(rho(v) < f for v in coefficients if v != b)
    out = dict(seed=w, rank=q, current=current, coefficients=coefficients,
               endpoint=f, leading=b, avoided_returning=u, status='descending',
               ordinary_common_tail_clocks=[6, 1], quotient_length=5,
               rule='whole_R67_guard_in_critical_basis')
    validate(out)
    return out


def close_plan(seed, choose, max_nodes=None):
    """Finite strict-rho expansion, ending with explicit conditional inputs.

    choose(w) returns a validated decreasing plan or None. It must never
    return an unresolved candidate. The resource cap rejects rather than
    certifying a missing leaf.
    """
    rho(seed)
    if max_nodes is not None and (not isinstance(max_nodes, int) or isinstance(max_nodes, bool)
                                  or max_nodes < 1):
        raise ValueError('Require a positive node cap or None')
    memo, active, expanded = {}, set(), set()

    def visit(w):
        if w in memo:
            return memo[w]
        if max_nodes is not None and len(memo)+len(active) >= max_nodes:
            raise RuntimeError('Conditional compiler node cap reached')
        active.add(w)
        data = choose(w)
        if data is None:
            answer = dict(current={}, coefficients={w: 1})
        else:
            if data.get('seed') != w:
                raise ValueError('Rule returned the wrong parent source')
            validate(data)
            expanded.add(w)
            current, coefficients = data['current'], {}
            for v, c in data['coefficients'].items():
                child = visit(v)
                current = combine((1, current), (c, child['current']))
                coefficients = combine((1, coefficients), (c, child['coefficients']))
            answer = dict(current=current, coefficients=coefficients)
        active.remove(w)
        memo[w] = answer
        return answer

    out = dict(visit(seed), seed=seed, rank=rho(seed), expanded=sorted(expanded),
               status='conditional', rule='critical_basis_closure')
    check_boundary(out)
    if expanded:
        validate(out)
    return out


def compile_plan(data, supplied):
    """Substitute every exact terminal current; unknown supply is never searched."""
    check_boundary(data)
    current = data['current']
    for w, c in data['coefficients'].items():
        if w not in supplied:
            raise ValueError('Missing exact critical pair current')
        rows = supplied[w]
        if any(not isinstance(x, int) or isinstance(x, bool) or x <= 1 or x % 2 != 1
               or not isinstance(v, int) or isinstance(v, bool) or not v for x, v in rows.items()):
            raise ValueError('Require integer supplied current rows')
        if divergence(rows) != T.pair_source(w):
            raise ValueError('Incorrect exact supplied pair current')
        current = combine((1, current), (c, rows))
    assert divergence(current) == T.pair_source(data['seed'])
    return current
