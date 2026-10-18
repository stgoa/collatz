"""Exact first/second comparisons for the unique fifth-family rank defect.

All signed requests remain explicit. The optional fixed-rule expansion uses
only the frozen fifteen-family dispatcher, never this module.
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


FIXED = load('defect_fixed', 'refined_rules/refined_rules.py')
SIGMA = load('defect_sigma', 'phase_rank/sigma_rank.py')
RETURN = load('defect_return', 'returning_phase/returning_phase.py')
CONTINUE = load('defect_continue', 'returning_continuation/returning_continuation.py')
RANK, NORMAL, EXACT = FIXED.RANK, FIXED.RANK.NORMAL, FIXED.EXACT
combine, divergence, rho = RANK.combine, RANK.divergence, RANK.rho


def sigma_frontier(plan):
    """Complete rank-mismatch classification for a supplied sigma-valid plan."""
    w = plan['seed']
    SIGMA.validate(w, plan)
    Q = rho(w)
    high = {u:c for u,c in plan['coefficients'].items() if rho(u)>=Q}
    for u in high:
        assert RETURN.returning(u) and 8*rho(u) == 9*SIGMA.sigma(u)+5
        assert 9*SIGMA.sigma(u) >= 8*Q-5
        assert SIGMA.sigma(u) < SIGMA.sigma(w)
    if RETURN.returning(w):
        assert not high
    return dict(seed=w, rank=Q, sigma=SIGMA.sigma(w),
                parent_returning=RETURN.returning(w), high=high,
                lower_sigma=(8*Q+3)//9)


def _finish(w, current, coefficients, **metadata):
    coefficients = RANK.NINE.clean(coefficients)
    expected = RANK.T.pair_source(w)
    for u,c in coefficients.items():
        expected = combine((1, expected), (-c, RANK.T.pair_source(u)))
    assert divergence(current) == expected
    high = {u:c for u,c in coefficients.items() if rho(u)>=rho(w)}
    answer = dict(seed=w, rank=rho(w), current=current,
                  coefficients=coefficients, high=high,
                  status='unresolved' if high else 'descending', **metadata)
    if not high:
        RANK.validate_step(w, answer)
    return answer


def parameters(w):
    initial = EXACT.fifth_plan(w)
    if initial['status'] != 'unresolved':
        raise ValueError('Require a failed fifth-exponent comparison')
    j = (w-4021)//8192
    u, Q = 8589+17496*j, 12063+24576*j
    assert w == 4021+8192*j and j >= 0 and Q == rho(w)
    high = {v:c for v,c in initial['coefficients'].items() if rho(v)>=Q}
    assert high == {u:1} and RETURN.returning(u) and u%81 == 3
    data = RETURN.parameters(u)
    a,t,r = data['a'],data['t'],data['endpoint']
    assert Q == (2**(a+10)*t-4651)//2187
    assert 2187*Q == 2**(a+10)*t-4651
    assert SIGMA.sigma(u) == initial['parameters']['endpoint'] < Q < rho(u)
    return dict(seed=w,index=j,rank=Q,defect=u,defect_rank=rho(u),
                a=a,t=t,endpoint=r,initial=initial,first=data)


def substitute(initial, u, child):
    """Substitute an exact comparison even if its local rank test failed."""
    assert child['seed'] == u
    coefficients = Counter(initial['coefficients'])
    weight = coefficients.pop(u)
    current = combine((1,initial['current']),(weight,child['current']))
    for v,c in child['coefficients'].items():
        coefficients[v] += weight*c
    return _finish(initial['seed'],current,coefficients)


def first_plan(w):
    data = parameters(w)
    child = RETURN.forward_plan(data['defect'])
    result = substitute(data['initial'],data['defect'],child)
    result['parameters'] = data
    result['stage'] = 'first_return'
    # All other initial and lower absorption requests are below original Q.
    high = RANK.absorption_plan(data['endpoint'])
    assert result['high'] == {u:c for u,c in high['coefficients'].items() if rho(u)>=data['rank']}
    return result


def second_plan(w):
    """Entire second interface, including arbitrary second exponents."""
    data = parameters(w)
    child = CONTINUE.continuation_plan(data['defect'])
    result = substitute(data['initial'],data['defect'],child)
    result['parameters'] = data
    result['continuation'] = child['parameters']
    result['stage'] = 'second_block'
    high = RANK.absorption_plan(child['parameters']['endpoint'])
    assert result['high'] == {u:c for u,c in high['coefficients'].items() if rho(u)>=data['rank']}
    return result


def a3_first_decision(w):
    plan = first_plan(w)
    data = plan['parameters']
    if data['a'] != 3:
        raise ValueError('Require defect first exponent a=3')
    r = data['endpoint']
    accepted = not NORMAL.canonical(r) or r%8 == 1
    assert (plan['status']=='descending') == accepted
    return dict(plan, arithmetic_decision=accepted)


def a3_second_decision(w):
    plan = second_plan(w)
    data,cont = plan['parameters'],plan['continuation']
    r = data['endpoint']
    if data['a'] != 3 or not NORMAL.canonical(r) or r%4 != 3:
        raise ValueError('Require the failed a=3 first-return branch')
    second = cont['second']
    A,d,f,n = second['a'],second['d'],cont['endpoint'],cont['minimum']
    if A not in (2,3):
        raise ValueError('The complete low-exponent table has A=2 or3')
    selected = NORMAL.selected(f)
    if A == 2:
        accepted = bool(d%2 or d>=6 or selected)
    else:
        accepted = bool(d%2 or d>=8 or (selected and (d>=4 or n%8==1 or
                        (n%8==3 and EXACT.absorption_bound(n)['exception'] is None))))
    assert (plan['status']=='descending') == accepted
    return dict(plan, arithmetic_decision=accepted)


def fixed_resolution(w, max_nodes=10000):
    """Expand the initial defect through fixed refined15 above original rho."""
    data = parameters(w)
    Q = data['rank']
    def resolver(v):
        if v == w or rho(v)<Q:
            return None
        return FIXED.one_step(v)
    child = RANK.close_plan(data['defect'],resolver,max_nodes=max_nodes)
    result = substitute(data['initial'],data['defect'],child)
    return dict(result,parameters=data,expanded=child['expanded'],stage='fixed_fifteen')


def one_step(w):
    """Only exact final-rho successes; no unresolved current is supplied."""
    if not EXACT.eligible(w):
        return None
    old = EXACT.fifth_plan(w)
    if old['status'] == 'descending':
        return old
    for constructor in (first_plan,second_plan):
        plan = constructor(w)
        if plan['status'] == 'descending':
            return plan
    return None


def successful_family(index=0):
    if not isinstance(index,int) or index<0:
        raise ValueError('Require a nonnegative index')
    w = 53173+65536*index
    plan = a3_first_decision(w)
    assert plan['status'] == 'descending'
    return dict(seed=w,index=index,plan=plan)


def surviving_family(index=0, exclude_parent=False):
    if not isinstance(index,int) or index<0:
        raise ValueError('Require a nonnegative index')
    k = 81*index if exclude_parent else index
    w,u = 44981+2**24*k,96069+35831808*k
    data = parameters(w)
    assert data['defect']==u and data['a']==4
    assert FIXED.one_step(u) is None
    undo = FIXED.DEFERRED.defer(FIXED.DEFERRED.OLD.FORWARD.forward_plan(u))
    assert undo['current']=={} and undo['coefficients']=={u:1}
    if exclude_parent:
        assert w%81==26 and FIXED.one_step(w) is None
    result = fixed_resolution(w)
    assert result['high']=={u:1} and not result['expanded']
    return dict(seed=w,defect=u,index=index,exclude_parent=exclude_parent,plan=result)


def second_cell(A,d,index=0):
    """Complete CRT cylinder on every failed a3 second-run cell."""
    if not all(isinstance(x,int) for x in (A,d,index)) or A<2 or d<2 or index<0:
        raise ValueError('Require A,d>=2 and a nonnegative index')
    binary,ternary = 2**(d+1),59049
    vb = (1+2**d)*pow(3**(A-1),-1,binary)%binary
    vt = 14495*pow(2**A,-1,ternary)%ternary
    residue = vb+binary*((vt-vb)*pow(binary,-1,ternary)%ternary)
    period = binary*ternary
    first = max(0,(73544-2**A*residue+2**A*period-1)//(2**A*period))
    v = residue+period*(first+index)
    r = 2**A*v-1
    j = (2*r-28988)//59049
    w = 4021+8192*j
    data = second_plan(w)
    assert data['parameters']['a']==3 and data['parameters']['endpoint']==r
    assert (data['continuation']['second']['a'],data['continuation']['second']['d'])==(A,d)
    return dict(seed=w,A=A,d=d,index=index,v=v,v_residue=residue,
                v_period=period,first_index=first,plan=data)


def compile_plan(plan,supplied):
    if plan.get('status')!='descending':
        raise ValueError('A high request remains; no original-rho certificate')
    RANK.validate_step(plan['seed'],plan)
    return RANK.compile_plan(plan,supplied)
