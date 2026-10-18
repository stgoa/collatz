"""Exact growing quotient prefixes avoiding the seven direct W5 rules.

The negative shadow is a residue device. All constructed states are positive.
Missing leading currents remain explicit; no orbit termination is inferred.
"""
from collections import Counter
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'double_inverse'))
import expanded_union as UNION

RANK=UNION.RANK
NINE,T,NORMAL=RANK.NINE,RANK.T,RANK.NORMAL
combine,atoms,divergence=RANK.combine,RANK.atoms,RANK.divergence
ESCAPE=UNION.OLD.ESCAPE
# Exact canonical T prefixes (numerator, offset, total binary denominator).
PREFIXES=((1,0,0),(3,1,1),(9,5,2),(27,19,3),(81,33,6),
          (243,163,7),(729,617,9),(2187,2363,11))
SHADOWS=(-17,-25,-37,-55,-21,-31,-23,-17)


def entry(q):
    if not isinstance(q,int) or q<=0 or (q+17)%(64*81):
        raise ValueError('Require positive q=-17 modulo5184')
    w=(2*q+1)//3
    assert w%3456==3445 and NORMAL.canonical(q) and T.critical(q)
    assert NORMAL.selected(3*w) and RANK.rho(w)==q and w%3==1
    parameters=ESCAPE.spine_parameters(q)
    assert parameters['D']==2 and parameters['j']==1
    assert UNION.one_step(w) is None
    return dict(q=q,w=w,D=2,j=1)


def family(repeats,index=1):
    if not isinstance(repeats,int) or repeats<1 or not isinstance(index,int) or index<1:
        raise ValueError('Require positive integer repeat count and family index')
    bits=11*repeats+6
    q=81*2**bits*index-17
    return dict(repeats=repeats,index=index,bits=bits,**entry(q))


def one_cycle(q):
    entry(q)
    if (q+17)%2**17:
        raise ValueError('One full cycle needs q=-17 modulo2^17')
    states=[]
    for A,C,B in PREFIXES:
        numerator=A*q+C
        assert numerator%2**B==0
        states.append(numerator//2**B)
    current={}
    for i,x in enumerate(states[:-1]):
        row=NORMAL.quotient_bridge(x)
        assert row['minimum']==states[i+1]
        assert states[i+1]>q and NORMAL.canonical(states[i+1])
        current=combine((1,current),(1,row['current']))
    assert states[4]==(81*q+33)//64
    assert NORMAL.step(states[3])==(81*q+65)//32
    assert NORMAL.selected(NORMAL.step(states[3]))
    assert (states[-1]+17)*2048==2187*(q+17)
    assert divergence(current)==atoms((1,q),(-1,states[-1]))
    critical=[(i,T.critical_inverse(x)) for i,x in enumerate(states) if T.critical(x)]
    assert [i for i,_ in critical]==[0,4,7]
    assert critical[1][1]%16==9
    assert critical[0][1]%8==critical[2][1]%8==5
    entry(states[-1])
    return dict(q=q,endpoint=states[-1],states=states,current=current,
                critical=[[i,w] for i,w in critical])


def nine_frontier(q):
    """Full W9 elimination retains the next unaccepted W5 frontier at +1."""
    cycle=one_cycle(q)
    v=cycle['states'][4]//3
    data=NINE.five_plan(v)
    local=data['local_plans'][v]
    endpoint=cycle['endpoint']
    lead=entry(endpoint)['w']
    lower=(729*q+2153)//2048
    assert local['d']==6 and local['endpoints']==[endpoint,lower]
    assert endpoint==3*lower-2
    assert data['coefficients'][lead]==1
    assert all(RANK.rho(w)<endpoint for w in data['coefficients'] if w!=lead)
    assert endpoint>q and UNION.one_step(lead) is None
    return dict(seed=v,q=q,endpoint=endpoint,lead=lead,lower=lower,
                current=data['current'],coefficients=data['coefficients'])


def forward_plan(q):
    """One exact increasing comparison; deliberately not a strict-rank rule."""
    cycle=one_cycle(q)
    w,child=entry(q)['w'],entry(cycle['endpoint'])['w']
    z=NORMAL.normal_form(w)
    high,low=RANK.absorption_plan(child),RANK.absorption_plan(z)
    current=combine((1,NORMAL.bridge(3*w)['current']), (1,cycle['current']),
                    (-1,NORMAL.bridge(3*child)['current']),
                    (-1,NORMAL.bridge(w)['current']),
                    (1,high['current']),(-1,low['current']))
    coefficients=Counter(high['coefficients']);coefficients.subtract(low['coefficients'])
    coefficients[child]+=1
    coefficients=NINE.clean(coefficients)
    assert 3*cycle['endpoint']+4<4*q
    assert coefficients[child]==1
    assert all(RANK.rho(v)<q for v in coefficients if v!=child)
    expected=T.pair_source(w)
    for v,c in coefficients.items():
        expected=combine((1,expected),(-c,T.pair_source(v)))
    assert divergence(current)==expected
    return dict(seed=w,rank=q,endpoint=cycle['endpoint'],lead=child,
                current=current,coefficients=coefficients)


def witness(repeats,index=1,with_plans=False):
    data=family(repeats,index)
    q=data['q'];states=[q];current={};cycles=[]
    for i in range(repeats):
        block=one_cycle(q)
        if with_plans:
            block['pair_plan']=forward_plan(q)
            block['nine_plan']=nine_frontier(q)
        current=combine((1,current),(1,block['current']))
        states.extend(block['states'][1:]);cycles.append(block)
        q=block['endpoint']
        assert (q+17)*2**(11*(i+1))==3**(7*(i+1))*(data['q']+17)
    assert all(x>data['q'] for x in states[1:])
    assert divergence(current)==atoms((1,data['q']),(-1,q))
    return dict(data,endpoint=q,states=states,current=current,cycles=cycles)


def repeat_plan(repeats,index=1):
    """Retain the largest unaccepted +1 request after prescribed repetitions."""
    data=family(repeats,index)
    coefficients={data['w']:1};current={};q=data['q']
    for _ in range(repeats):
        plan=forward_plan(q)
        w=plan['seed'];assert coefficients[w]==1
        coefficients=Counter(coefficients);del coefficients[w]
        coefficients.update(plan['coefficients']);coefficients=NINE.clean(coefficients)
        current=combine((1,current),(1,plan['current']))
        q=plan['endpoint']
    lead=entry(q)['w']
    assert coefficients[lead]==1
    assert all(RANK.rho(v)<q for v in coefficients if v!=lead)
    expected=T.pair_source(data['w'])
    for v,c in coefficients.items():expected=combine((1,expected),(-c,T.pair_source(v)))
    assert divergence(current)==expected
    return dict(seed=data['w'],rank=data['q'],repeats=repeats,index=index,
                endpoint=q,lead=lead,current=current,coefficients=coefficients)


def lookahead_plan(repeats,steps,index=1):
    """Any prescribed quotient prefix followed by the full deterministic H.

    The nondecreasing +1 leading request survives every seven-rule expansion
    of the strictly lower requests. This is a scoped failure certificate.
    """
    if not isinstance(steps,int) or steps<0 or steps>7*repeats:
        raise ValueError('Require 0<=steps<=7*repeats')
    trajectory=witness(repeats,index)
    w,q=trajectory['w'],trajectory['q']
    current=NORMAL.bridge(3*w)['current']
    for x in trajectory['states'][:steps]:
        current=combine((1,current),(1,NORMAL.quotient_bridge(x)['current']))
    endpoint=trajectory['states'][steps]
    z=NORMAL.normal_form(w)
    high,low=RANK.absorption_plan(endpoint),RANK.absorption_plan(z)
    current=combine((1,current),(-1,NORMAL.bridge(w)['current']),
                    (1,high['current']),(-1,low['current']))
    coefficients=Counter(high['coefficients']);coefficients.subtract(low['coefficients'])
    coefficients=NINE.clean(coefficients)
    block,offset=divmod(steps,7)
    leading_block=block+(offset>=3)
    lead=entry(trajectory['states'][7*leading_block])['w']
    assert coefficients[lead]==1 and RANK.rho(lead)>=q
    assert all(RANK.rho(v)<RANK.rho(lead) for v in coefficients if v!=lead)
    expected=T.pair_source(w)
    for v,c in coefficients.items():expected=combine((1,expected),(-c,T.pair_source(v)))
    assert divergence(current)==expected
    return dict(seed=w,rank=q,repeats=repeats,index=index,steps=steps,
                endpoint=endpoint,lead=lead,leading_rank=RANK.rho(lead),
                current=current,coefficients=coefficients)
