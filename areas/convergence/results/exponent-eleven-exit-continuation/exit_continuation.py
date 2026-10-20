"""A complete e11 exit and a scoped obstruction to appended full blocks.

Every current and every missing signed input is retained.  The construction
does not search for absorption or exclude unrelated comparisons.
"""
from collections import Counter
from pathlib import Path
from importlib.util import module_from_spec,spec_from_file_location

HERE=Path(__file__).resolve().parent


def load(name,path):
    spec=spec_from_file_location(name,HERE.parent/path)
    module=module_from_spec(spec);spec.loader.exec_module(module)
    return module


EXIT=load('continuation_exit','selected_cycle_exit/selected_exit.py')
UNION=load('continuation_union','selected_rules/selected_rules.py')
RANK,NORMAL,RUN,NINE,T=EXIT.RANK,EXIT.NORMAL,EXIT.RUN,EXIT.NINE,EXIT.T
combine,atoms,divergence,rho=EXIT.combine,EXIT.atoms,EXIT.divergence,EXIT.rho


def eleven(r,s):
    """Entire exit-exponent11 stratum, with its exact original-rank comparison."""
    if not isinstance(r,int) or r<0 or not isinstance(s,int) or s<1 or s%2==0:
        raise ValueError('Require r>=0 and positive odd s')
    q=81*2**(11*r+11)*s-17
    w=(2*q+1)//3
    f=3**(7*r+10)*s-6
    path,current=EXIT.ordinary_path(q,7*r+7)
    assert path[-1]==NORMAL.step(f)
    current=combine((1,current),(-1,{f:1}))
    assert divergence(current)==atoms((1,q),(-1,f))
    assert (f>q)==(r>=16)
    data=EXIT.maximal_cycles(q)
    assert data['repeats']==r and data['exit_exponent']==11
    return dict(seed=w,rank=q,repeats=r,index=s,endpoint=f,current=current,
                ordinary_clocks=[7*r+7,1],quotient_clock=7*r+6)


def family(r,A,K,index=0):
    """Complete CRT family with K appended low blocks after one long block."""
    if (not all(isinstance(x,int) for x in (r,A,K,index))
            or r<16 or A<5 or K<0 or index<0):
        raise ValueError('Require r>=16,A>=5,K>=0,index>=0')
    M=7*r+10
    binary=2**(3*K+6)
    ternary=3**(M+1)
    t2=-9*pow(3**A,-1,binary)%binary
    unit=pow(2,r,3)
    t3=(3**M*unit-5)*pow(2**A,-1,ternary)%ternary
    residue=t2+binary*((t3-t2)*pow(binary,-1,ternary)%ternary)
    period=binary*ternary
    t=residue+period*index
    f=2**A*t-1
    assert (f+6)%3**M==0
    s=(f+6)//3**M
    data=eleven(r,s)
    assert data['endpoint']==f and s%3==unit and s%2
    assert NORMAL.canonical(f) and RUN.parameters(f)[:3]==(A,t,2)
    v=f//3
    assert v%8==5 and v%3==1 and rho(v)==f
    g=(3**A*t-1)//2
    assert RUN.target(f)==g and (g+5)%2**(3*K+5)==0
    assert (2**(11*r+16)*s-7)%3==0
    return dict(data,A=A,K=K,progression_index=index,M=M,t=t,t_residue=residue,t_period=period,
                s=s,s_period=3*2**(A+3*K+6),leading=v,first_extended_endpoint=g,
                seed_period=81*2**(11*r+A+3*K+18))


def continued_plan(data,low_blocks):
    """The e11 current followed by a specified long block and low-block prefix."""
    if not isinstance(low_blocks,int) or not 0<=low_blocks<=data['K']:
        raise ValueError('Require a low-block prefix between zero and K')
    f,w=data['endpoint'],data['seed']
    first=RUN.bridge(f)
    assert first['a']==data['A'] and first['d']==2
    extension=first['current'];states=[first['target']]
    for _ in range(low_blocks):
        block=RUN.bridge(states[-1])
        assert block['a']==block['d']==2 and NORMAL.canonical(block['target'])
        extension=combine((1,extension),(1,block['current']))
        states.append(block['target'])
    z=NORMAL.normal_form(w)
    high,low=RANK.absorption_plan(states[-1]),RANK.absorption_plan(z)
    current=combine((1,NORMAL.bridge(3*w)['current']),(1,data['current']),
                    (1,extension),(-1,NORMAL.bridge(w)['current']),
                    (1,high['current']),(-1,low['current']))
    coefficients=Counter(high['coefficients']);coefficients.subtract(low['coefficients'])
    coefficients=NINE.clean(coefficients)
    expected=T.pair_source(w)
    for u,c in coefficients.items():expected=combine((1,expected),(-c,T.pair_source(u)))
    assert divergence(current)==expected
    return dict(seed=w,rank=data['rank'],current=current,coefficients=coefficients,
                states=states,low_blocks=low_blocks,endpoint=states[-1],
                quotient_clock=data['quotient_clock']+data['A']+2*low_blocks,
                ordinary_clocks=[data['ordinary_clocks'][0]+data['A']-1+2*low_blocks,0])


def undo_plan(data,plan):
    """Apply exactly the leading R41 inverses; all auxiliary rows cancel."""
    current=plan['current'];coefficients=Counter(plan['coefficients']);undos=[]
    for g in reversed(plan['states']):
        u=(2*g+1)//3
        assert coefficients[u]==1 and max(coefficients,key=rho)==u
        local=RANK.INVERSE.phase_pair_plan(u)
        assert local['status']=='descending'
        RANK.validate_step(u,local)
        del coefficients[u]
        coefficients.update(local['coefficients'])
        coefficients=Counter(NINE.clean(coefficients))
        current=combine((1,current),(1,local['current']))
        undos.append(dict(seed=u,rank=g,child=local['parameters']['p']))
    original=EXIT.exit_plan(data['seed'])
    assert original['parameters']['endpoint']==data['endpoint']
    assert current==original['current']
    assert dict(coefficients)==original['coefficients']
    v=data['leading']
    assert coefficients[v]==1 and max(coefficients,key=rho)==v
    assert all(rho(u)<data['endpoint'] for u in coefficients if u!=v)
    return dict(seed=data['seed'],rank=data['rank'],current=current,
                coefficients=dict(coefficients),leading=v,leading_rank=data['endpoint'],undos=undos)


def rejection_parameters(data):
    """Arithmetic reasons for the unchanged leading input's twelve-rule failure."""
    v,f=data['leading'],data['endpoint']
    inverse=load('continuation_nonselected','nonselected_inverse/inverse_phases.py')
    double=load('continuation_double','double_inverse/double_inverse.py')
    four,eight=inverse.parameters(v,4),inverse.parameters(v,8)
    assert four['h']==0 and eight['h']==1 and eight['residue']==0
    assert eight['child_domain']=='W9'
    assert RANK.INVERSE.valuation3(2*eight['lower']+1)==0
    assert RUN.parameters(f)[0]==data['A']>=5 and RUN.parameters(f)[2]==2
    g=RUN.target(f)
    assert NORMAL.canonical(g) and g%3==1 and g>f
    assert EXIT.OLD.absorption_rank_bound(g)['bound']==g
    assert not inverse.decreasing_domain(v) and not double.recognized(v)
    assert UNION.one_step(v) is None and UNION.one_step(data['seed']) is None
    return dict(nonselected_base_h=[four['h'],eight['h']],double_second_depth=0,
                first_a=data['A'],first_d=2,first_return=g,rank=f,
                initial_rank=data['rank'])
