"""Complete R67 exit interface and a growing natural re-entry comparison.

The exit comparison is conditional: its leading higher-rank pair is retained.
In particular, the second returning plan at the re-entry is not accepted by
the rho dispatcher.  No missing current or universal termination is supplied.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('mixed_exit_growth', HERE.parent/'mixed_rank_recursion/mixed_growth.py')
M = module_from_spec(spec)
spec.loader.exec_module(M)
RANK, NORMAL = M.RANK, M.NORMAL
FORWARD = M.SIGMA.FORWARD
RUN = FORWARD.RUN
combine, divergence, rho = M.combine, M.divergence, M.rho
A, B, DEN, DIFFERENCE = M.A, M.B, M.DEN, M.DIFFERENCE
P, C, L = A*A, B*(A+DEN), 2**37
E = P-L
REENTRY_BITS, CONSUMED_BITS = 63, 37
RESIDUE = 8515171531530858421


def exit_family(count, valuation, index=0):
    """Every positive initial seed with exactly count macros and exit e."""
    if not isinstance(count, int) or count < 1 or valuation not in range(7,26):
        raise ValueError('Require count>=1 and exit valuation7..25')
    if not isinstance(index, int) or index < 0:
        raise ValueError('Require a nonnegative progression index')
    order = 19*count+valuation
    period = 2**(order+1)
    residue = (2**order-B)*pow(DIFFERENCE,-1,period)%period
    seed = residue+period*index
    actual = M.maximum(seed)
    assert actual['count']==count and actual['exit_valuation']==valuation
    terminal = actual['states'][-1]
    unit = (DIFFERENCE*terminal+B)//2**valuation
    assert unit%2 and unit == A**count*((DIFFERENCE*seed+B)//2**order)
    return dict(seed=seed,count=count,exit_valuation=valuation,index=index,
                residue=residue,period=period,states=actual['states'],
                exit=terminal,exit_unit=unit)


def exit_parameters(seed):
    data = M.maximum(seed)
    w, e = data['states'][-1],data['exit_valuation']
    z = (DIFFERENCE*w+B)//2**e
    a,t,d,unit = RUN.parameters(3*w)
    assert a==5 and z%2
    if e==7:
        assert d==2
    elif e==8:
        assert d==3+NORMAL.valuation2(243*z-294023) and d>=4
    else:
        assert d==3
    f = RUN.target(3*w)
    if e==7:assert f==(729*w+211)//64
    if e>=9:assert f==(729*w+147)//256
    return dict(seed=seed,rank=3*seed,count=data['count'],states=data['states'],
                exit=w,exit_valuation=e,exit_unit=z,a=a,t=t,d=d,unit=unit,
                endpoint=f,minimum=NORMAL.normal_form(f))


def _validate(seed,current,coefficients):
    expected = RANK.T.pair_source(seed)
    for w,c in coefficients.items():
        assert w%8==5 and isinstance(c,int) and c
        expected = combine((1,expected),(-c,RANK.T.pair_source(w)))
    assert divergence(current)==expected


def exit_plan(seed):
    """One complete next R26 block, still measured against original rho."""
    data = exit_parameters(seed)
    first = M.repeated_plan(seed,data['count'])
    child = FORWARD.forward_plan(data['exit'])
    coefficients = Counter(first['coefficients'])
    assert coefficients.pop(data['exit'])==1
    coefficients.update(child['coefficients'])
    coefficients = RANK.NINE.clean(coefficients)
    current = combine((1,first['current']),(1,child['current']))
    upper,lower = RANK.absorption_plan(data['endpoint']),RANK.absorption_plan(seed)
    assert coefficients==combine((1,upper['coefficients']),(-1,lower['coefficients']))
    high = {w:c for w,c in coefficients.items() if rho(w)>=3*seed}
    assert high=={w:c for w,c in upper['coefficients'].items() if rho(w)>=3*seed}
    _validate(seed,current,coefficients)
    d,m = data['d'],data['count']
    return dict(seed=seed,rank=3*seed,current=current,coefficients=coefficients,
                high=high,status='unresolved' if high else 'descending',parameters=data,
                quotient_length=12*m+4+d//2,
                ordinary_common_tail_clocks=[12*m+5+(d-1)//2,1] if d%2
                                             else [12*m+4+d//2,0])


def general_reentry_family(count,index=0):
    """Exactly count old macros, exit18, and re-entry after the next block."""
    if not isinstance(count,int) or count<1 or not isinstance(index,int) or index<0:
        raise ValueError('Require a positive old count and nonnegative index')
    k=count+1
    multiplier=A**k
    offset=B*((A**k-DEN**k)//DIFFERENCE)
    denominator=2**(19*k-1)
    period=denominator*2**26
    residue=(M.RESIDUE*denominator-offset)*pow(multiplier,-1,period)%period
    seed=residue+period*index
    target,remainder=divmod(multiplier*seed+offset,denominator)
    assert not remainder and M.eligible(target)
    old=M.maximum(seed)
    assert old['count']==count and old['exit_valuation']==18
    assert DEN*target==2*(A*old['states'][-1]+B)
    return dict(seed=seed,count=count,index=index,period=period,residue=residue,
                leading=target,exit=old['states'][-1],multiplier=multiplier,
                offset=offset,denominator=denominator)


def general_reentry_plan(seed):
    """Full comparison on the entire exit18-to-guard subdomain, at any depth."""
    old=M.maximum(seed)
    v=old['states'][-1]
    if old['exit_valuation']!=18:
        raise ValueError('Require maximal old exit18')
    target,remainder=divmod(A*v+B,2**18)
    if remainder or not M.eligible(target):
        raise ValueError('The natural continuation does not re-enter the guard')
    length=12*(old['count']+1)
    endpoint,prefix,_=M.path_current(3*seed,length)
    assert endpoint==6*target+1
    norm=NORMAL.bridge(endpoint)
    assert norm['minimum']==3*target and len(norm['left_prefix'])==len(norm['right_prefix'])==7
    upper,lower=RANK.absorption_plan(target),RANK.absorption_plan(seed)
    current=combine((1,prefix),(1,norm['current']),
                    (1,upper['current']),(-1,lower['current']))
    coefficients=combine((1,{target:1}),(1,upper['coefficients']),(-1,lower['coefficients']))
    assert coefficients[target]==1 and all(rho(x)<3*target for x in coefficients if x!=target)
    _validate(seed,current,coefficients)
    return dict(seed=seed,rank=3*seed,old_count=old['count'],current=current,
                coefficients=coefficients,leading=target,status='unresolved',
                high={x:c for x,c in coefficients.items() if rho(x)>=3*seed},
                quotient_length=length,ordinary_common_tail_clocks=[length+6,6])


def eligible(w):
    return isinstance(w,int) and w>0 and w%2**REENTRY_BITS==RESIDUE


def lift(w):
    if not eligible(w):
        raise ValueError('Require the complete63-bit re-entry cylinder')
    result,remainder = divmod(P*w+C,L)
    assert not remainder and result>w and M.eligible(result)
    assert NORMAL.valuation2(DIFFERENCE*w+B)==37
    return result


def parameters(w):
    target = lift(w)
    previous = M.maximum(w)
    assert previous['count']==1 and previous['exit_valuation']==18
    v = previous['states'][-1]
    f,u = (729*v+147)//256,(2187*v+1209)//1024
    raw = 6*target+1
    assert target*DEN==2*(A*v+B) and raw==(243*((3*u+1)//64)-1)//2
    assert f%128==27 and u%81==3 and M.D.RETURN.returning(u)
    assert NORMAL.selected(raw) and NORMAL.normal_form(raw)==3*target
    assert NORMAL.valuation2(raw+1)==6 and rho(target)==3*target
    assert rho(u)<rho(target)
    return dict(seed=w,rank=3*w,exit=v,exit_valuation=18,first_endpoint=f,
                intermediate=u,intermediate_rank=rho(u),raw_endpoint=raw,
                leading=target,leading_rank=3*target,
                guard_valuation=NORMAL.valuation2(E*w+C))


def comparison(w):
    """Exactly24 ordinary arrows followed by the six/six halving bridge."""
    data = parameters(w)
    endpoint,path,word = M.path_current(3*w,24)
    assert endpoint==data['raw_endpoint']
    assert word==list(M.WORD)+[3]+list(M.WORD[1:])
    norm = NORMAL.bridge(endpoint)
    assert norm['minimum']==3*data['leading']
    assert len(norm['left_prefix'])==len(norm['right_prefix'])==7
    current = combine((1,path),(1,norm['current']))
    assert divergence(current)==RANK.atoms((1,3*w),(-1,3*data['leading']))
    return dict(parameters=data,current=current,word=word,
                quotient_length=24,ordinary_common_tail_clocks=[30,6])


def plan(w, audit_composition=False):
    data = comparison(w)
    v = data['parameters']['leading']
    upper,lower = RANK.absorption_plan(v),RANK.absorption_plan(w)
    current = combine((1,data['current']),(1,upper['current']),(-1,lower['current']))
    coefficients = combine((1,{v:1}),(1,upper['coefficients']),(-1,lower['coefficients']))
    assert coefficients[v]==1
    assert all(rho(x)<3*w for x in coefficients if x!=v)
    _validate(w,current,coefficients)
    if audit_composition:
        old = M.macro(w)
        p = data['parameters']
        first = M.SIGMA.forward_plan(p['exit'])
        M.SIGMA.validate(p['exit'],first)
        assert first['status']=='descending' and first['coefficients'][p['intermediate']]==1
        second = M.D.RETURN.forward_plan(p['intermediate'])
        assert second['status']=='unresolved'
        assert {x:c for x,c in second['coefficients'].items()
                if rho(x)>=p['intermediate_rank']}=={v:1}
        requested = combine((1,old['coefficients']),(-1,{p['exit']:1}),
                            (1,first['coefficients']),(-1,{p['intermediate']:1}),
                            (1,second['coefficients']))
        assert requested==coefficients
        assert current==combine((1,old['current']),(1,first['current']),(1,second['current']))
    return dict(seed=w,rank=3*w,current=current,coefficients=coefficients,
                leading=v,high={v:1},status='unresolved',parameters=data['parameters'],
                quotient_length=24,ordinary_common_tail_clocks=[30,6])


def family(count,index=0):
    if not isinstance(count,int) or count<1 or not isinstance(index,int) or index<0:
        raise ValueError('Require a positive count and nonnegative index')
    bits = REENTRY_BITS+CONSUMED_BITS*(count-1)
    period = 2**bits
    residue = -C*pow(E,-1,period)%period
    w = residue+period*index
    states = [w]
    for _ in range(count):states.append(lift(states[-1]))
    return dict(seed=w,count=count,index=index,bits=bits,period=period,
                residue=residue,states=states)


def maximum(w):
    if not eligible(w):raise ValueError('The re-entry guard fails')
    valuation = NORMAL.valuation2(E*w+C)
    count = 1+(valuation-REENTRY_BITS)//CONSUMED_BITS
    states = [w]
    for _ in range(count):states.append(lift(states[-1]))
    last = states[-1]
    assert not eligible(last) and M.eligible(last)
    assert 26<=NORMAL.valuation2(E*last+C)<=62
    return dict(seed=w,count=count,valuation=valuation,states=states,
                terminal_valuation=NORMAL.valuation2(E*last+C))


def repeated_plan(w,count):
    if not isinstance(count,int) or count<1:
        raise ValueError('Require a positive repeat count')
    states,current = [w],{}
    for _ in range(count):
        data = comparison(states[-1])
        current = combine((1,current),(1,data['current']))
        states.append(data['parameters']['leading'])
    upper,lower = RANK.absorption_plan(states[-1]),RANK.absorption_plan(w)
    current = combine((1,current),(1,upper['current']),(-1,lower['current']))
    coefficients = combine((1,{states[-1]:1}),(1,upper['coefficients']),(-1,lower['coefficients']))
    assert coefficients[states[-1]]==1
    assert all(rho(x)<3*states[-2] for x in coefficients if x!=states[-1])
    _validate(w,current,coefficients)
    return dict(seed=w,rank=3*w,count=count,states=states,current=current,
                coefficients=coefficients,leading=states[-1],status='unresolved',
                quotient_length=24*count,ordinary_common_tail_clocks=[24*count+6,6],
                high={x:c for x,c in coefficients.items() if rho(x)>=3*w})


def compile_plan(data,supplied):
    """Require every missing pair, including the larger re-entered input."""
    return RANK.NINE.compile_five_plan(data,supplied)
