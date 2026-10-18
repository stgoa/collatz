"""Compose complete forward blocks before introducing missing pair currents.

The low-run interface is exact and finite. Acceptance is conditional on
strictly smaller critical-image inputs, not a claim of universal coverage.
"""
from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
def load(name,path):
    spec=spec_from_file_location(name,HERE.parent/path)
    module=module_from_spec(spec);spec.loader.exec_module(module)
    return module

OLD=load('continuation_old','nonselected_forward/nonselected_forward.py')
RANK=load('continuation_rank','critical_rank/rank_closure.py')
RUN,NORMAL,T,NINE=OLD.RUN,OLD.NORMAL,OLD.T,OLD.NINE
combine,atoms,divergence=OLD.combine,OLD.atoms,OLD.divergence


def finish(w,arithmetic,raw,metadata):
    """One final H request, retaining the original q=3w comparison rank."""
    z=NORMAL.normal_form(w)
    high,low=RANK.absorption_plan(raw),RANK.absorption_plan(z)
    current=combine((1,arithmetic),(-1,NORMAL.bridge(w)['current']),
                    (1,high['current']),(-1,low['current']))
    coefficients=Counter(high['coefficients'])
    coefficients.subtract(low['coefficients'])
    coefficients=NINE.clean(coefficients)
    bound=OLD.OLD.absorption_rank_bound(raw)['bound']
    expected=T.pair_source(w)
    for v,c in coefficients.items():expected=combine((1,expected),(-c,T.pair_source(v)))
    assert divergence(current)==expected
    result=dict(seed=w,current=current,coefficients=coefficients,parameters=metadata,
                raw_endpoint=raw,minimum=NORMAL.normal_form(raw),
                bound=[bound.numerator,bound.denominator],
                status='descending' if bound<3*w else 'unresolved')
    if result['status']=='descending':RANK.validate_step(w,result)
    return result


def two_plan(w):
    first=OLD.parameters(w)
    n=first['minimum']
    if n%4!=3:
        raise ValueError('Require a complementary canonical first endpoint')
    first_bridge=RUN.normalized_bridge(3*w)
    second=RUN.bridge(n)
    current=combine((1,first_bridge['current']),(1,second['current']))
    a,t,d,u=RUN.parameters(n)
    metadata=dict(first=first,second=dict(a=a,t=t,d=d,u=u),
                  first_selected=NORMAL.selected(first['endpoint']),
                  quotient_length=first['quotient_length']+a+d//2-1,
                  second_ordinary_clocks=[len(second['left'])-1,len(second['right'])-1])
    return finish(w,current,second['target'],metadata)


def low_first_table(w):
    """Complete two-block endpoint test on all eight stated low-first rows."""
    first=OLD.parameters(w)
    a,d,n=first['a'],first['d'],first['minimum']
    if a not in(3,4) or OLD.OLD.absorption_rank_bound(n)['bound']<3*w or n%4!=3:
        raise ValueError('Require an unresolved first block with a3 or4')
    aa,t,e,u=RUN.parameters(n)
    if aa!=2:raise ValueError('Require second first exponent2')
    partner=NORMAL.selected(first['endpoint'])
    row=(a,d,partner)
    f=RUN.target(n);m=NORMAL.normal_form(f);selected=NORMAL.selected(f)
    if e%2:accepted=True
    elif row==(3,2,False):accepted=e>=8 or(selected and(e>=4 or m%8!=3))
    elif row in((3,4,False),(4,2,True),(4,6,False)):accepted=e>=6 or selected
    elif row==(4,2,False):accepted=e>=10 or(selected and(e>=6 or(e==4 and m%8==1)))
    elif row==(4,4,False):accepted=e>=8 or(selected and(e>=4 or m%8==1))
    elif row in((4,4,True),(4,8,False)):accepted=e>=4 or selected
    else:raise AssertionError('The complete first-phase list was not exhausted')
    actual=OLD.OLD.absorption_rank_bound(m)['bound']<3*w
    assert accepted==actual
    return dict(seed=w,row=list(row),second_d=e,second_selected=selected,
                endpoint=m,endpoint_mod8=m%8,accepted=accepted)


def low_run(x):
    """Maximal consecutive (a,d)=(2,2) raw run, including its exact exit."""
    NORMAL._odd(x)
    if x%32!=27:raise ValueError('Require canonical x27 modulo32')
    e=NORMAL.valuation2(x+5)
    r=(e-2)//3
    y=x;current=Counter();path=[x]
    for _ in range(r):
        assert y%32==27 and RUN.parameters(y)[:1]==(2,)
        assert RUN.parameters(y)[2]==2
        for a in(1,2):
            assert NORMAL.valuation2(3*y+1)==a
            current[y]+=1;y=NORMAL.step(y);path.append(y)
    assert y+5==9**r*((x+5)//8**r)
    exit_exponent=e-3*r
    assert exit_exponent in(2,3,4) and y%32!=27
    assert divergence(current)==atoms((1,x),(-1,y))
    if exit_exponent==3:
        assert NORMAL.selected(y) and NORMAL.normal_form(y)%8==1
    elif exit_exponent==4:
        assert NORMAL.canonical(y) and y%32==11
        assert RUN.parameters(y)[0]==2 and RUN.parameters(y)[2]>=3
    return dict(seed=x,length=r,exponent=e,exit_exponent=exit_exponent,
                endpoint=y,current=dict(current),path=path)


def delayed_parameters(w):
    first=OLD.parameters(w)
    x=first['minimum']
    if (first['a'],first['d'])!=(3,2) or first['endpoint']!=x or x%32!=27:
        raise ValueError('Require first(3,2), canonical endpoint27mod32')
    run=low_run(x)
    if run['exit_exponent']!=4:
        raise ValueError('Require the complete exit-exponent4 stratum')
    r=run['length'];s=(x+5)//(9*2**(3*r+4))
    assert s>0 and s%2 and x+5==9*2**(3*r+4)*s
    assert w==(2**(3*r+8)*s-11)//9
    a,t,d,u=RUN.parameters(run['endpoint'])
    assert a==2 and d==2+NORMAL.valuation2(3**(2*r+3)*s-1)
    return dict(seed=w,r=r,s=s,d=d,first_endpoint=x,low_endpoint=run['endpoint'],
                quotient_length=3+2*r+1+d//2,run=run)


def delayed_plan(w):
    data=delayed_parameters(w)
    first=RUN.bridge(3*w)
    assert first['target']==data['first_endpoint'] and not first['right'][1:]
    last=RUN.bridge(data['low_endpoint'])
    current=combine((1,first['current']),(1,data['run']['current']),(1,last['current']))
    metadata={k:v for k,v in data.items() if k!='run'}
    metadata['ordinary_clocks']=[3+2*data['r']+len(last['left'])-1,len(last['right'])-1]
    if data['d']%2:
        b=data['d']//2
        lhs=(2**(3*data['r']+data['d']+9)-3**(2*data['r']+b+6))*data['s']
        rhs=103*2**(data['d']-2)-3**(b+3)
        assert (lhs>rhs)==(Fraction(9*last['target']+5,8)<3*w)
        metadata['generic_test']=[lhs,rhs]
    return finish(w,current,last['target'],metadata)


def uniform_odd_test(r,d):
    if r<1 or d<3 or d%2!=1:return False
    return 2**(d-2)*(2**(3*r+11)-103)>3**(d//2+3)*(3**(2*r+3)-1)


def delayed_family(r,d=None,index=0):
    """Full new CRT families outside all seven earlier direct rule domains."""
    if not isinstance(r,int) or r<1 or not isinstance(index,int) or index<0:
        raise ValueError('Require positive integer r and nonnegative index')
    if d is None:d=4*r+3
    if not isinstance(d,int) or not uniform_odd_test(r,d):
        raise ValueError('Require odd d passing the proved uniform inequality')
    binary=2**(d-1)
    s2=(1+2**(d-2))*pow(3**(2*r+3),-1,binary)%binary
    s3=416*pow(2**(3*r+8),-1,729)%729
    first=s2+binary*((s3-s2)*pow(binary,-1,729)%729)
    s=first+729*binary*index
    w=(2**(3*r+8)*s-11)//9
    data=delayed_parameters(w)
    assert data['r']==r and data['d']==d and data['s']==s and w%81==45
    return dict(seed=w,r=r,d=d,s=s,s_residue=first,s_period=729*binary,
                seed_period=81*2**(3*r+d+7),index=index)


def accepted_plan(w):
    """Bounded arithmetic recognizer, prioritizing the delayed complete stratum."""
    if not OLD.eligible(w):return None
    try:data=delayed_plan(w)
    except ValueError:data=None
    if data is not None and data['status']=='descending':return data
    try:
        table=low_first_table(w)
        if table['accepted']:return two_plan(w)
    except ValueError:pass
    return None


def one_step(w):
    """Ordinary w-based R43 dispatcher API; no family parameters are needed."""
    return accepted_plan(w)


def recognized(w):
    return one_step(w) is not None


def compile_plan(plan,supplied):
    if plan['status']!='descending':raise ValueError('Endpoint bound does not decrease original rank')
    RANK.validate_step(plan['seed'],plan)
    return RANK.compile_plan(plan,supplied)
