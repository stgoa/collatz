"""Exact exits from the R54 selected cycle, with conditional rho descent.

The prescribed finite blocks do not search for an unknown absorption current.
Every remaining signed W5 premise is retained and missing inputs are rejected.
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


CYCLE = load('exit_cycle', 'rule_avoidance/rule_avoidance.py')
RUN = load('exit_run', 'complementary_bridge/run_bridge.py')
OLD = load('exit_returning', 'returning_phase/returning_phase.py')
RANK, NORMAL, NINE, T = CYCLE.RANK, CYCLE.NORMAL, CYCLE.NINE, CYCLE.T
combine, atoms, divergence, rho = RANK.combine, RANK.atoms, RANK.divergence, RANK.rho


def phase(w):
    return isinstance(w, int) and w > 0 and w % 3456 == 3445


def maximal_cycles(q):
    """Maximum seven-T returns whose endpoints remain in the R54 entry phase."""
    CYCLE.entry(q)
    E = NORMAL.valuation2(q+17)
    repeats, offset = divmod(E-6, 11)
    e = offset+6
    u = (q+17)//2**E
    endpoint = 3**(7*repeats)*2**e*u-17
    return dict(q=q, exponent=E, repeats=repeats, exit_exponent=e,
                odd_part=u, endpoint=endpoint, exit_odd_part=3**(7*repeats)*u)


def ordinary_path(seed, steps):
    path = [seed]
    for _ in range(steps):
        path.append(NORMAL.step(path[-1]))
    current = Counter(path[:-1])
    current.pop(1, None)
    return path, dict(current)


def cycle_prefix(q):
    data = maximal_cycles(q)
    path, current = ordinary_path(q, 7*data['repeats'])
    assert path[-1] == data['endpoint']
    for i, x in enumerate(path[:-1]):
        assert NORMAL.valuation2(3*x+1) == (1,1,1,2,1,1,4)[i % 7]
    assert divergence(current) == atoms((1,q),(-1,path[-1]))
    return dict(data, path=path, current=current)


def next_block(q):
    """One complete R26 block, or the single canonical 1 mod8 arrow."""
    if q == 1:
        return dict(kind='absorber', root=q, target=q, current={}, quotient_length=0)
    if q % 8 == 1:
        return dict(kind='canonical_forward', root=q, target=NORMAL.step(q),
                    current={q:1}, quotient_length=1)
    result = dict(RUN.bridge(q), kind='complete_run')
    result['quotient_length'] = result['a']+result['d']//2-1
    return result


def exit_interface(q):
    """Complete eleven-row exit interface, with all variable-depth cases kept."""
    CYCLE.entry(q)
    e = NORMAL.valuation2(q+17)
    if not 6 <= e <= 16:
        raise ValueError('First strip the maximal guarded phase returns')
    U = (q+17)//2**e
    first = next_block(q)
    assert first['a'] == 4
    expected_d = 2+NORMAL.valuation2(27*2**(e-6)*U-7)
    assert first['d'] == expected_d
    if e == 6:
        assert expected_d >= 3
        endpoint = first['target']
        return dict(q=q, e=e, U=U, first=first, second=None, endpoint=endpoint,
                    current=first['current'], quotient_length=first['quotient_length'])
    assert expected_d == 2
    Y = 81*2**(e-5)*U-41
    assert first['target'] == Y
    normalization = NORMAL.bridge(Y)
    v = normalization['minimum']
    if e >= 10:
        assert v == 81*2**(e-6)*U-21
        assert NORMAL.selected(Y) and NORMAL.valuation2(v+1) == 2
    elif e == 9:
        assert v == Y and NORMAL.valuation2(Y+1) == 3
    elif e == 7:
        assert NORMAL.valuation2(Y+1) == 2
        assert NORMAL.selected(Y) == (U % 4 == 3)
    else:
        assert NORMAL.valuation2(Y+1) == 3+NORMAL.valuation2(81*U-5)
    second = next_block(v)
    if e >= 10:
        assert second['a'] == 2
        d = NORMAL.valuation2(243*2**(e-8)*U-16)
        assert second['d'] == d
        assert (e,d) in ((10,2),(11,3)) or (e == 12 and d >= 5) or (e >= 13 and d == 4)
    current = combine((1,first['current']),(1,normalization['current']),
                      (1,second['current']))
    endpoint = second['target']
    if e >= 13:
        assert endpoint == 2187*2**(e-11)*U-17
        if e in (13,14):
            assert NORMAL.selected(endpoint) == (U % 4 == 3)
        elif e == 15:
            assert NORMAL.valuation2(endpoint+1) == 4+NORMAL.valuation2(2187*U-1)
        else:
            assert NORMAL.selected(endpoint)
            assert NORMAL.normal_form(endpoint) == 34992*U-9
    assert divergence(current) == atoms((1,q),(-1,endpoint))
    return dict(q=q,e=e,U=U,first=first,normalization=normalization,second=second,
                endpoint=endpoint,current=current,
                quotient_length=first['quotient_length']+second['quotient_length'])


def parameters(w):
    if not phase(w):
        raise ValueError('Require w=3445 modulo3456')
    q = (3*w-1)//2
    prefix = cycle_prefix(q)
    tail = exit_interface(prefix['endpoint'])
    current = combine((1,prefix['current']),(1,tail['current']))
    f = tail['endpoint']
    bound = OLD.absorption_rank_bound(f)
    assert divergence(current) == atoms((1,q),(-1,f))
    return dict(seed=w,rank=q,prefix=prefix,exit=tail,endpoint=f,current=current,
                minimum=NORMAL.normal_form(f),rank_bound=bound['bound'],
                quotient_length=7*prefix['repeats']+tail['quotient_length'])


def exit_plan(w):
    data = parameters(w)
    upper, lower = NORMAL.bridge(3*w), NORMAL.bridge(w)
    z = lower['minimum']
    high, low = RANK.absorption_plan(data['endpoint']), RANK.absorption_plan(z)
    current = combine((1,upper['current']),(1,data['current']),(-1,lower['current']),
                      (1,high['current']),(-1,low['current']))
    coefficients = Counter(high['coefficients'])
    coefficients.subtract(low['coefficients'])
    coefficients = NINE.clean(coefficients)
    assert all(rho(u) <= data['rank_bound'] for u in high['coefficients'])
    assert all(8*rho(u) <= 9*z+5 < 8*data['rank'] for u in low['coefficients'])
    expected = T.pair_source(w)
    for u,c in coefficients.items():
        expected = combine((1,expected),(-c,T.pair_source(u)))
    assert divergence(current) == expected
    accepted = data['rank_bound'] < data['rank']
    result = dict(seed=w,rank=data['rank'],current=current,coefficients=coefficients,
                  status='descending' if accepted else 'unresolved',parameters=data)
    if accepted:
        RANK.validate_step(w,result)
    return result


def recognized(w):
    return phase(w) and parameters(w)['rank_bound'] < rho(w)


def one_step(w):
    return exit_plan(w) if recognized(w) else None


def family(repeats, index=0, depth=None, avoid_inverse=False):
    """Entire strict-rho families after any prescribed maximal cycle count."""
    if (not isinstance(repeats,int) or repeats < 0 or not isinstance(index,int) or index < 0):
        raise ValueError('Require nonnegative repeat count and progression index')
    d = 2*repeats+5 if depth is None else depth
    if not isinstance(d,int) or d % 2 != 1 or d < 2*repeats+5:
        raise ValueError('Require odd d>=2r+5')
    b = d//2
    period = 2**(d-3)
    residue = pow(3**(7*repeats+9),-1,period)*(1+2**(d-4)) % period
    if avoid_inverse:
        unit = pow(pow(2,11*repeats+17,3),-1,3)
        residue += period*((unit-residue)*pow(period,-1,3) % 3)
        period *= 3
    s = residue+period*index
    q = 81*2**(11*repeats+12)*s-17
    w = (2*q+1)//3
    f = 3**b*(3**(7*repeats+9)*s-1)//2**(d-4)
    assert s % 2 and (9*f+5) < 8*q
    assert 2**(d-4)*(3**4*2**(11*repeats+15)-141) > 3**(b+2)*(3**(7*repeats+9)-1)
    if avoid_inverse:
        assert (2**(11*repeats+17)*s-7) % 3 == 0
    return dict(seed=w,q=q,repeats=repeats,d=d,b=b,index=index,s=s,avoid_inverse=avoid_inverse,
                s_residue=residue,s_period=period,endpoint=f,
                seed_residue=54*2**(11*repeats+12)*residue-11,
                seed_period=(3 if avoid_inverse else 1)*27*2**(11*repeats+d+10),
                left_clock=7*repeats+b+6,right_clock=1,
                quotient_clock=7*repeats+b+5)


def compile_plan(plan,supplied):
    if plan['status'] != 'descending':
        raise ValueError('This exit still has an unresolved rank comparison')
    RANK.validate_step(plan['seed'],plan)
    return RANK.compile_plan(plan,supplied)
