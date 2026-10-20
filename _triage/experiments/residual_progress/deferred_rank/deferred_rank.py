"""Exact signed expansion before testing the original critical-image rank.

The fixed twelve-family resolver is the only source of expanded rules.
The original request is protected; unresolved and capped frontiers remain
explicit. No unknown orbit is searched and no sigma rule is used.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('deferred_rank_twelve', HERE.parent/'selected_rules/selected_rules.py')
OLD = module_from_spec(spec)
spec.loader.exec_module(OLD)
RANK, NORMAL = OLD.RANK, OLD.RANK.NORMAL
combine, atoms, divergence, rho = RANK.combine, RANK.atoms, RANK.divergence, RANK.rho


def _validate_boundary(w, current, coefficients):
    if not isinstance(w,int) or w <= 0 or w % 8 != 5:
        raise ValueError('Require a positive W5 source')
    if any(not isinstance(u,int) or u <= 0 or u%8 != 5 or
           not isinstance(c,int) or not c for u,c in coefficients.items()):
        raise ValueError('Require nonzero signed integer W5 requests')
    if any(not isinstance(x,int) or not isinstance(c,int) for x,c in current.items()):
        raise ValueError('Require integer current rows')
    expected = RANK.T.pair_source(w)
    for u,c in coefficients.items():
        expected = combine((1,expected),(-c,RANK.T.pair_source(u)))
    if divergence(current) != expected:
        raise ValueError('Incorrect initial or expanded signed boundary')


def defer(plan, max_nodes=10000):
    """Expand only requests at/above the original rank, with exact signs.

    Each accepted resolver step decreases its own rank.  Nodes blocked by
    the fixed resolver or by source protection remain explicit requests.
    A resource cap returns an exact unfinished plan with status 'capped'.
    """
    if max_nodes is not None and (not isinstance(max_nodes,int) or max_nodes < 0):
        raise ValueError('Require a nonnegative cap or None')
    w = plan['seed']
    current, coefficients = dict(plan['current']), Counter(plan['coefficients'])
    _validate_boundary(w,current,coefficients)
    threshold = rho(w)
    blocked, history = {}, []
    while True:
        pending = [u for u,c in coefficients.items() if c and rho(u)>=threshold and u not in blocked]
        if not pending:
            status = 'unresolved' if blocked else 'descending'
            break
        if max_nodes is not None and len(history)+len(blocked) >= max_nodes:
            status = 'capped'
            break
        u = max(pending,key=rho)
        if u == w:
            blocked[u] = 'original_source'
            continue
        child = OLD.one_step(u)
        if child is None:
            blocked[u] = 'unrecognized_by_fixed_twelve'
            continue
        RANK.validate_step(u,child)
        c = coefficients.pop(u)
        current = combine((1,current),(c,child['current']))
        for v,a in child['coefficients'].items():
            coefficients[v] += c*a
        coefficients = Counter({v:a for v,a in coefficients.items() if a})
        history.append(dict(seed=u,coefficient=c,rank=rho(u),rule=child['rule'],
                            requests=sorted(child['coefficients'].items())))
    coefficients = dict(coefficients)
    _validate_boundary(w,current,coefficients)
    answer = dict(seed=w,rank=threshold,current=current,coefficients=coefficients,
                  status=status,history=history,blocked=blocked,
                  remaining_high=sorted(u for u in coefficients if rho(u)>=threshold),
                  initial_requests=sorted(plan['coefficients'].items()))
    if status == 'descending':
        RANK.validate_step(w,answer)
    return answer


def candidates(w):
    """The prescribed failed or successful R55/R56/R57 plans, retaining all rows."""
    NORMAL._odd(w)
    if w % 8 != 5:
        raise ValueError('Require a W5 input')
    if OLD.FORWARD.eligible(w):
        first = OLD.FORWARD.forward_plan(w)
        yield 'R55_first',first
        data = first['parameters']
        if (data['a'],data['d']) == (2,2) and NORMAL.canonical(data['endpoint']):
            yield 'R55_second',OLD.FORWARD.two_block_plan(w)
    if OLD.INVERSE.eligible(w):
        for k in (4,8):
            yield 'R56_ray'+str(k),OLD.INVERSE.pair_plan(w,k)
    if OLD.EXIT.phase(w):
        yield 'R57_exit',OLD.EXIT.exit_plan(w)


def one_step(w, max_nodes=10000):
    """First original-rho success under the bounded deferred test, else None."""
    for name,plan in candidates(w):
        result = defer(plan,max_nodes=max_nodes)
        if result['status'] == 'descending':
            return dict(result,recipe=name)
    return None


def first_family(index=0):
    """Entire w=245 mod1024: exact H requests already decrease rho."""
    if not isinstance(index,int) or index < 0:
        raise ValueError('Require a nonnegative integer index')
    w,q,m,s = 245+1024*index,367+1536*index,465+1944*index,349+1458*index
    plan = OLD.FORWARD.forward_plan(w)
    assert plan['status'] == 'unresolved' and plan['parameters']['minimum'] == m
    assert plan['rank'] == q and m%8 == 1 and NORMAL.step(m) == s and s%3 == 1 and s<q
    result = defer(plan)
    assert result['status'] == 'descending' and not result['history']
    return dict(index=index,seed=w,rank=q,first_minimum=m,successor=s,plan=result)


def macro_family(index=0):
    """Whole branch w=1301+32768*l whose endpoint g is selected."""
    if not isinstance(index,int) or index < 0:
        raise ValueError('Require a nonnegative integer index')
    l = index
    w,q,m,s,u,g = (1301+32768*l,1951+49152*l,3705+93312*l,
                   2779+69984*l,1853+46656*l,3127+78732*l)
    if not NORMAL.selected(g):
        raise ValueError('This complete branch requires selected g')
    r = (g-1)//2
    parent = OLD.FORWARD.forward_plan(w)
    assert parent['status'] == 'unresolved' and parent['input_rank_bound'] == [g,1]
    assert parent['parameters']['minimum'] == m and NORMAL.step(m) == s
    assert rho(u) == s > q and u%3 == 2 and NORMAL.canonical(s)
    child = OLD.one_step(u)
    assert child['rule'] == 'R55_selected_forward' and child['parameters']['endpoint'] == g
    assert child['parameters']['minimum'] == r and 8*q-(9*r+5) == 1536+38922*l > 0
    result = defer(parent)
    assert result['status'] == 'descending'
    assert result['history'] == [dict(seed=u,coefficient=1,rank=s,rule=child['rule'],
                                    requests=sorted(child['coefficients'].items()))]
    path,x = [q],q
    word = [1,1,1,1,2,1,3,2]
    rows = {}
    for a in word:
        assert NORMAL.valuation2(3*x+1) == a
        rows[x] = rows.get(x,0)+1
        x = NORMAL.step(x);path.append(x)
    assert x == g
    t = q
    for _ in range(8):t = NORMAL.quotient_step(t)
    assert t == r
    z = NORMAL.normal_form(w)
    high,low = RANK.absorption_plan(r),RANK.absorption_plan(z)
    direct = combine((1,NORMAL.bridge(3*w)['current']),(1,rows),
                     (1,NORMAL.bridge(g)['current']),(-1,NORMAL.bridge(w)['current']),
                     (1,high['current']),(-1,low['current']))
    c = Counter(high['coefficients']);c.subtract(low['coefficients'])
    assert result['current'] == direct and result['coefficients'] == RANK.NINE.clean(c)
    return dict(index=l,seed=w,rank=q,first_minimum=m,intermediate=s,child=u,
                endpoint=g,minimum=r,word=word,path=path,plan=result)


def compile_plan(plan,supplied):
    if plan['status'] != 'descending':
        raise ValueError('Deferred plan still has a high-rank or capped request')
    RANK.validate_step(plan['seed'],plan)
    return RANK.compile_plan(plan,supplied)
