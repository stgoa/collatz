"""Exact growing blocks made from one sigma and one rho comparison.

This is a conditional signed interface and a scoped rank obstruction.
It does not alter either dispatcher's priority or supply an unknown pair.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('mixed_growth_defect', HERE.parent/'defect_resolution/defect_resolution.py')
D = module_from_spec(spec)
spec.loader.exec_module(D)
RANK, NORMAL, SIGMA = D.RANK, D.NORMAL, D.SIGMA
combine, divergence, rho = D.combine, D.divergence, D.rho
A, B, DEN, DIFFERENCE = 531441, 311195, 524288, 7153
GUARD_BITS, CONSUMED_BITS = 26, 19
RESIDUE = 40529845
WORD = (1,1,1,1,2,3,2,1,1,1,1,2)


def eligible(w):
    return isinstance(w,int) and w>0 and w % 2**GUARD_BITS == RESIDUE


def lift(w):
    if not eligible(w):
        raise ValueError('Require positive w=40529845 modulo2^26')
    result, remainder = divmod(A*w+B,DEN)
    assert not remainder and result>w and result % 8 == 5
    assert NORMAL.canonical(3*result) and rho(result)==3*result
    return result


def parameters(w):
    v = lift(w)
    q,u,f = 3*w,(2187*w+1209)//1024,(729*w+147)//256
    R,t = (3*u-1)//2,(3*u+1)//64
    r,n = (243*t-1)//2,3*v
    assert w % 512 == 437 and u % 512 == 21 and u % 81 == 3
    assert f % 128 == 27 and f % 3 == 0
    assert r % 512 == 125 and n % 128 == 31
    assert r==4*n+1 and 3*u+1==64*t and t%4==1
    assert D.RETURN.returning(u) and not D.RETURN.returning(w)
    assert not D.RETURN.returning(v) and rho(w)==q and rho(u)==R
    assert SIGMA.sigma(u)==f and f<q<n<R
    return dict(seed=w,child=v,rank=q,child_rank=n,intermediate=u,
                intermediate_rank=R,intermediate_sigma=f,first_endpoint=f,
                returning_exponent=6,returning_unit=t,raw_endpoint=r,
                guard_valuation=NORMAL.valuation2(DIFFERENCE*w+B))


def path_current(seed,length):
    x,current,valuations=seed,Counter(),[]
    for _ in range(length):
        assert x>1
        current[x]+=1
        valuations.append(NORMAL.valuation2(3*x+1))
        x=NORMAL.step(x)
    current=combine((1,current))
    assert divergence(current)==RANK.atoms((1,seed),(-1,x))
    return x,current,valuations


def macro(w):
    """The two actual valid plan choices, including their full signed sum."""
    data=parameters(w)
    u,v,q,n=(data[x] for x in ('intermediate','child','rank','child_rank'))
    left=SIGMA.forward_plan(w)
    SIGMA.validate(w,left)
    assert left['status']=='descending' and left['coefficients'][u]==1
    assert {x:c for x,c in left['coefficients'].items() if rho(x)>=q}=={u:1}
    right=D.RETURN.forward_plan(u)
    assert right['status']=='descending'
    RANK.validate_step(u,right)
    assert right['coefficients'][v]==1 and SIGMA.sigma(v)>SIGMA.sigma(u)
    coefficients=Counter(left['coefficients']);assert coefficients.pop(u)==1
    coefficients.update(right['coefficients']);coefficients=RANK.NINE.clean(coefficients)
    current=combine((1,left['current']),(1,right['current']))
    h_v,h_w=RANK.absorption_plan(v),RANK.absorption_plan(w)
    expected=combine((1,{v:1}),(1,h_v['coefficients']),(-1,h_w['coefficients']))
    assert coefficients==expected and coefficients[v]==1
    assert all(rho(x)<q for x in coefficients if x!=v)
    endpoint,prefix,word=path_current(q,12)
    assert tuple(word)==WORD and endpoint==NORMAL.F(n)
    comparison=combine((1,prefix),(1,NORMAL.bridge(endpoint)['current']))
    assert divergence(comparison)==RANK.atoms((1,q),(-1,n))
    assert current==combine((1,comparison),(1,h_v['current']),(-1,h_w['current']))
    expected_boundary=RANK.T.pair_source(w)
    for x,c in coefficients.items():
        expected_boundary=combine((1,expected_boundary),(-c,RANK.T.pair_source(x)))
    assert divergence(current)==expected_boundary
    return dict(seed=w,rank=q,current=current,coefficients=coefficients,
                status='unresolved',parameters=data,leading=v,
                quotient_length=12,ordinary_common_tail_clocks=[13,1],
                sigma_plan=left,rho_plan=right)


def family(count,index=0):
    """At least count growing macros, retaining all binary guard bits."""
    if not isinstance(count,int) or count<1 or not isinstance(index,int) or index<0:
        raise ValueError('Require a positive count and nonnegative index')
    bits=GUARD_BITS+CONSUMED_BITS*(count-1)
    period=2**bits
    residue=-B*pow(DIFFERENCE,-1,period)%period
    w=residue+period*index
    assert eligible(w)
    states=[w]
    for _ in range(count):states.append(lift(states[-1]))
    assert all(a<b for a,b in zip(states,states[1:]))
    return dict(seed=w,count=count,index=index,bits=bits,residue=residue,
                period=period,states=states)


def maximum(w):
    """Exact maximal count for this guard, not over other plan choices."""
    if not eligible(w):raise ValueError('The mixed-block guard fails')
    order=NORMAL.valuation2(DIFFERENCE*w+B)
    count=1+(order-GUARD_BITS)//CONSUMED_BITS
    states=[w]
    for _ in range(count):states.append(lift(states[-1]))
    terminal=states[-1]
    assert not eligible(terminal)
    assert 7<=NORMAL.valuation2(DIFFERENCE*terminal+B)<=25
    return dict(seed=w,count=count,states=states,valuation=order,
                exit_valuation=NORMAL.valuation2(DIFFERENCE*terminal+B))


def repeated_plan(w,count):
    """Closed form of count full macro substitutions; no unknown supply."""
    if not isinstance(count,int) or count<1:
        raise ValueError('Require a positive repetition count')
    states=[w]
    for _ in range(count):states.append(lift(states[-1]))
    last=states[-1];q,n=3*w,3*last
    endpoint,prefix,word=path_current(q,12*count)
    expected_word=list(WORD)+([3]+list(WORD[1:]))*(count-1)
    assert word==expected_word and endpoint==NORMAL.F(n)
    comparison=combine((1,prefix),(1,NORMAL.bridge(endpoint)['current']))
    upper,lower=RANK.absorption_plan(last),RANK.absorption_plan(w)
    current=combine((1,comparison),(1,upper['current']),(-1,lower['current']))
    coefficients=combine((1,{last:1}),(1,upper['coefficients']),(-1,lower['coefficients']))
    assert coefficients[last]==1
    assert all(rho(x)<3*states[-2] for x in coefficients if x!=last)
    expected=RANK.T.pair_source(w)
    for x,c in coefficients.items():expected=combine((1,expected),(-c,RANK.T.pair_source(x)))
    assert divergence(current)==expected
    return dict(seed=w,rank=q,count=count,states=states,current=current,
                coefficients=coefficients,leading=last,status='unresolved',
                quotient_length=12*count,
                ordinary_common_tail_clocks=[12*count+1,1])


def substitute_leading(plan,child):
    leading=plan['leading']
    if child['seed']!=leading:raise ValueError('Wrong leading source')
    coefficients=Counter(plan['coefficients']);weight=coefficients.pop(leading)
    assert weight==1
    coefficients.update(child['coefficients'])
    return dict(seed=plan['seed'],current=combine((1,plan['current']),(1,child['current'])),
                coefficients=RANK.NINE.clean(coefficients),leading=child['leading'])


def compile_plan(plan,supplied):
    """An unresolved higher pair is mandatory; it is never supplied here."""
    return RANK.NINE.compile_five_plan(plan,supplied)
