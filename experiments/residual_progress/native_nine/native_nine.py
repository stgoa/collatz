"""Native-rank composition on a complete blocked W9 subdomain.

Uses established R52/R55 comparisons in the full critical basis. All terminal
requests remain supplied premises. Inverse alternatives retain their exact
self/higher frontiers; no local rank is substituted for the original rank.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = spec_from_file_location(name, HERE.parent/path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASIS = load('native_nine_basis', 'critical_basis/critical_basis.py')
INVERSE = load('native_nine_inverse', 'selected_inverse/selected_inverse.py')
FORWARD = load('native_nine_forward', 'selected_forward/selected_forward.py')
SECOND = load('native_nine_second', 'returning_continuation/returning_continuation.py')
NORMAL, T, NINE = BASIS.NORMAL, BASIS.T, BASIS.NINE
combine, atoms, divergence, rho = BASIS.combine, BASIS.atoms, BASIS.divergence, BASIS.rho


def integer(x, lower=0):
    return isinstance(x, int) and not isinstance(x, bool) and x >= lower


def eligible(b):
    return integer(b, 1) and b % 8192 == 905


def prefix(x, word):
    current, path = Counter(), [x]
    for a in word:
        assert NORMAL.valuation2(3*x+1) == a
        current[x] += 1
        x = NORMAL.step(x)
        path.append(x)
    return dict(current=dict(current), path=path, endpoint=x, word=list(word))


def parameters(b):
    if not eligible(b):
        raise ValueError('Require a positive W9 input b=905 modulo8192')
    t = (27*b+13)//128
    u, n = (32*t-1)//3, 3*b
    q, r = 16*t-1, (81*t-1)//2
    m, c = (r-1)//2, (27*t-1)//4
    assert t >= 191 and t % 1728 == 191
    assert BASIS.SIGMA.RETURN.returning(u)
    assert NORMAL.valuation2(3*u+1) == 5
    assert NORMAL.selected(r) and NORMAL.normal_form(r) == m == 3*c
    assert c % 16 == 9 and b < c < n < m
    first = prefix(n, (1, 2, 1, 1, 1, 2))
    assert first['endpoint'] == r
    local = NINE.local_plan(c)
    upper_canonical = NORMAL.canonical(3*local['z'])
    accepted = not (local['d'] in (4, 6) and not upper_canonical)
    return dict(seed=b, rank=n, t=t, returning=u, first_critical=q,
                first_endpoint=r, child_rank=m, child_nine=c, prefix=first,
                local=local, d=local['d'], upper_canonical=upper_canonical,
                accepted=accepted)


def native_plan(b):
    data = parameters(b)
    c, r, n = data['child_nine'], data['first_endpoint'], data['rank']
    local = data['local']
    high, low = BASIS.absorption_plan(c), BASIS.absorption_plan(b)
    current = combine((1, data['prefix']['current']), (1, NORMAL.bridge(r)['current']),
                      (1, local['current']), (1, high['current']), (-1, low['current']))
    coefficients = combine((1, local['coefficients']), (1, high['coefficients']),
                           (-1, low['coefficients']))
    leading = None if data['accepted'] else 4*local['z']+1
    out = dict(seed=b, rank=n, current=current, coefficients=coefficients,
               parameters=data, status='descending' if data['accepted'] else 'unresolved',
               leading=leading, rule='native_a5_W9_continuation')
    BASIS.check_boundary(out)
    assert all(rho(v) < n for v in coefficients) == data['accepted']
    if leading is not None:
        assert coefficients[leading] == 1 and rho(leading) > n
        assert all(rho(v) < n for v in coefficients if v != leading)
    else:
        BASIS.validate(out)
    return out


def d6_parameters(b):
    data = parameters(b)
    if data['d'] != 6 or data['upper_canonical']:
        raise ValueError('Require the noncanonical-upper D6 failure')
    t, c = data['t'], data['child_nine']
    p, Q = (729*t+25)//64, (2187*t+11)//128
    assert b % 65536 == 58249 and p % 19683 == 2176
    assert p == 4*data['local']['z']+1 and rho(p) == Q
    assert INVERSE.eligible(p) and (16*p-13)//27 == c
    assert INVERSE.parameters(p, 4)['h'] == 3
    assert INVERSE.parameters(p, 8)['h'] == 0
    assert c % 3 == 2 and data['rank'] == (16384*Q-29839)//19683
    return dict(data, higher_five=p, higher_rank=Q, lower_endpoint=(Q+2)//3)


def inverse_pair_plan(b, k):
    if k not in (4, 8) or isinstance(k, bool):
        raise ValueError('Require inverse choice4 or8')
    data = d6_parameters(b)
    p = data['higher_five']
    inverse = INVERSE.bridge(p, k)
    eta, z = inverse['parameters']['endpoint'], NORMAL.normal_form(p)
    high, low = BASIS.absorption_plan(eta), BASIS.absorption_plan(z)
    current = combine((1, NORMAL.bridge(3*p)['current']), (1, inverse['current']),
                      (-1, NORMAL.bridge(p)['current']), (1, high['current']),
                      (-1, low['current']))
    coefficients = combine((1, high['coefficients']), (-1, low['coefficients']))
    leading = data['returning'] if k == 4 else data['child_nine']
    assert coefficients[leading] == 1 and rho(leading) > data['rank']
    assert all(rho(v) < data['rank'] for v in coefficients if v != leading)
    out = dict(seed=p, rank=rho(p), original_rank=data['rank'], current=current,
               coefficients=coefficients, leading=leading, inverse=inverse,
               status='unresolved_at_original_rank')
    BASIS.check_boundary(out)
    return out


def substitute(plan, child):
    BASIS.check_boundary(plan)
    BASIS.check_boundary(child)
    v = child['seed']
    if v not in plan['coefficients']:
        raise ValueError('The supplied formal child is not requested')
    a = plan['coefficients'][v]
    out = dict(seed=plan['seed'], rank=rho(plan['seed']),
               current=combine((1, plan['current']), (a, child['current'])),
               coefficients=combine((1, plan['coefficients']), (-a, {v: 1}),
                                    (a, child['coefficients'])))
    BASIS.check_boundary(out)
    return out


def d4_return(b):
    plan = native_plan(b)
    data = plan['parameters']
    if data['d'] != 4 or data['upper_canonical']:
        raise ValueError('Require the noncanonical-upper D4 failure')
    result = substitute(plan, BASIS.returning_conversion(plan['leading']))
    c = data['child_nine']
    assert c == (729*b+223)//512
    assert result['coefficients'][c] == 1 and rho(c) > data['rank']
    assert all(rho(v) < data['rank'] for v in result['coefficients'] if v != c)
    return dict(result, parameters=data, leading=c, status='higher_nine_request')


def d6_undo(b):
    data = d6_parameters(b)
    inverse = inverse_pair_plan(b, 4)
    result = substitute(substitute(native_plan(b), inverse),
                        BASIS.returning_conversion(data['returning']))
    c, ell = data['child_nine'], data['lower_endpoint']
    lower = prefix(c, (2, 1, 2))
    assert lower['endpoint'] == ell
    hc, he = BASIS.absorption_plan(c), BASIS.absorption_plan(ell)
    assert result['current'] == combine((1, hc['current']), (-1, lower['current']),
                                        (-1, he['current']))
    assert result['coefficients'] == combine((1, {b: 1}), (1, hc['coefficients']),
                                             (-1, he['coefficients']))
    assert result['coefficients'][b] == 1
    assert all(rho(v) < data['rank'] for v in result['coefficients'] if v != b)
    return dict(result, parameters=data, status='self_request', leading=b)


def d6_k8(b):
    data = d6_parameters(b)
    result = substitute(native_plan(b), inverse_pair_plan(b, 8))
    c = data['child_nine']
    assert result['coefficients'][c] == 1 and rho(c) > data['rank']
    assert all(rho(v) < data['rank'] for v in result['coefficients'] if v != c)
    return dict(result, parameters=data, status='higher_nine_request', leading=c)


def d6_forward_plan(b):
    data = d6_parameters(b)
    p, Q = data['higher_five'], data['higher_rank']
    fdata = FORWARD.parameters(p)
    bridge = FORWARD.RUN.bridge(Q)
    f = bridge['target']
    hf, hp = BASIS.absorption_plan(f), BASIS.absorption_plan(p)
    forward = dict(seed=p, parameters=fdata, bridge=bridge,
                   current=combine((1, NORMAL.bridge(3*p)['current']),
                                   (1, bridge['current']), (1, hf['current']),
                                   (-1, hp['current'])),
                   coefficients=combine((1, hf['coefficients']), (-1, hp['coefficients'])))
    BASIS.check_boundary(forward)
    result = substitute(native_plan(b), forward)
    c, ell = data['child_nine'], data['lower_endpoint']
    initial = prefix(data['rank'], (1, 2, 1, 1, 1, 2, 1, 1, 4))
    lower = prefix(c, (2, 1, 2))
    assert initial['endpoint'] == Q and lower['endpoint'] == ell
    hc, he, hb = (BASIS.absorption_plan(x) for x in (c, ell, b))
    assert result['current'] == combine((1, initial['current']), (1, bridge['current']),
                                        (1, hf['current']), (-1, lower['current']),
                                        (1, hc['current']), (-1, he['current']),
                                        (-1, hb['current']))
    assert result['coefficients'] == combine((1, hf['coefficients']), (1, hc['coefficients']),
                                             (-1, he['coefficients']), (-1, hb['coefficients']))
    A, d = fdata['a'], fdata['d']
    selected = NORMAL.selected(f)
    actual = all(rho(v) < data['rank'] for v in result['coefficients'])
    accepted = A == 2 and (bool(d % 2) or d >= 6 or selected)
    if A == 2:
        assert actual == accepted
    if accepted:
        BASIS.validate(result)
    clocks = (9+fdata['ordinary_left_length'], fdata['ordinary_right_length'])
    return dict(result, parameters=data, forward=forward, next_a=A, next_d=d,
                next_selected=selected, actual_rank_status=actual,
                upper_comparison_clocks=list(clocks),
                status='descending' if accepted else 'unresolved',
                rule='native_D6_selected_A2_continuation')


def one_step(b):
    if not eligible(b):
        return None
    plan = native_plan(b)
    if plan['status'] == 'descending':
        return plan
    if plan['parameters']['d'] == 6:
        result = d6_forward_plan(b)
        if result['status'] == 'descending':
            return result
    return None


def compile_plan(plan, supplied):
    if plan.get('status') != 'descending':
        raise ValueError('Require a descending native-rank plan')
    BASIS.validate(plan)
    return BASIS.compile_plan(plan, supplied)


def native_cell(d, index=0):
    if not integer(d, 4) or not integer(index):
        raise ValueError('Require d>=4 and a nonnegative index')
    binary = 2**(d+3)
    residue = (13+2**(d+2))*pow(243, -1, binary) % binary
    t = residue+binary*((2-residue)*pow(binary, -1, 27) % 27)
    period = 27*binary
    while t < 191:
        t += period
    t += index*period
    b = (128*t-13)//27
    assert parameters(b)['d'] == d
    return dict(seed=b, t=t, d=d, index=index, t_period=period,
                seed_period=2**(d+10))


def d6_A2_cell(d, index=0):
    if not integer(d, 2) or not integer(index):
        raise ValueError('Require d>=2 and a nonnegative index')
    binary = 2**(d+3)
    residue = (1+2**(d+2))*pow(3, -1, binary) % binary
    Q = residue+binary*((32788-residue)*pow(binary, -1, 59049) % 59049)
    period = binary*59049
    while Q < 209935:
        Q += period
    Q += index*period
    t = (128*Q-11)//2187
    assert 2187*t == 128*Q-11
    b = (128*t-13)//27
    data = d6_parameters(b)
    forward = FORWARD.parameters(data['higher_five'])
    assert forward['a'] == 2 and forward['d'] == d
    return dict(seed=b, t=t, Q=Q, next_d=d, index=index, Q_period=period,
                seed_period=2**(d+17))
