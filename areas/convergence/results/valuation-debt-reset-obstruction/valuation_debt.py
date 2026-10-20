"""Exact phase debt transport and a full-rule obstruction family.

The local leading-state potential is not a global rank. Every counterfamily
uses an actually accepted R44 plan and retains all signed pair requests.
"""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
from fractions import Fraction

HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('debt_mixed',HERE.parent/'mixed_rank_recursion/mixed_growth.py')
MIXED=module_from_spec(spec);spec.loader.exec_module(MIXED)
RETURN=MIXED.D.RETURN
RANK,NORMAL=MIXED.RANK,MIXED.NORMAL
D,B_W,B_E=7153,311195,656187


def phase(w):
    if not isinstance(w,int) or w<=0 or w%8!=5:
        raise ValueError('Require a positive W5 pair index')
    return 'E' if RETURN.returning(w) else 'W'


def debt(w):
    label=phase(w)
    form=D*w+(B_E if label=='E' else B_W)
    order=NORMAL.valuation2(form)
    return dict(seed=w,phase=label,form=form,order=order,integer_potential=form*2**order)


def leading_transport(w):
    macro=MIXED.macro(w)
    data=macro['parameters'];u,v=data['intermediate'],data['child']
    a,b,c=debt(w),debt(u),debt(v)
    assert (a['phase'],b['phase'],c['phase'])==('W','E','W')
    assert 1024*b['form']==2187*a['form']
    assert 512*c['form']==243*b['form']
    assert b['order']==a['order']-10 and c['order']==a['order']-19
    assert a['integer_potential']>b['integer_potential']>c['integer_potential']
    assert macro['sigma_plan']['coefficients'][u]==1
    assert macro['rho_plan']['coefficients'][v]==1
    return dict(seed=w,intermediate=u,child=v,states=[a,b,c],
                edge_ratios=[[2187,2**20],[243,2**18]],
                scope='Leading requests only; no claim about every helper or later exit')


def pole_family(H,index=0):
    """Every member has an exact child debt H and fixed parent debt3."""
    if not isinstance(H,int) or H<26 or not isinstance(index,int) or index<0:
        raise ValueError('Require exact child order H>=26 and index>=0')
    power=2**(H+1)
    binary=(2**H-B_W)*pow(D,-1,power)%power
    u0=binary+power*((13-binary)*pow(power,-1,81)%81)
    u=u0+81*power*index
    w=(64*u+5)//9
    assert u>0 and u%81==13 and MIXED.eligible(u)
    assert phase(u)=='W' and phase(w)=='E'
    parent,child=debt(w),debt(u)
    assert child['order']==H and parent['order']==3
    assert 9*parent['form']==64*child['form']-13975032
    assert 3*(21459*w+6626905)==64*child['form']
    assert NORMAL.valuation2(21459*w+6626905)==H+6
    ratio=Fraction(child['integer_potential'],parent['integer_potential'])
    assert ratio>Fraction(9,512)*2**H
    return dict(seed=w,child=u,H=H,index=index,child_residue=u0,
                child_period=81*power,parent=parent,child_debt=child,
                potential_ratio=[ratio.numerator,ratio.denominator])


def obstruction(H,index=0):
    data=pole_family(H,index);w,u=data['seed'],data['child']
    plan=RETURN.forward_plan(w)
    r=plan['parameters']['endpoint']
    assert plan['parameters']['a']==3 and r==12*u+1==NORMAL.F(3*u)
    assert plan['normalized_upper']==3*u and plan['status']=='descending'
    assert plan['coefficients'][u]==1
    assert all(RANK.rho(x)<3*u for x in plan['coefficients'] if x!=u)
    assert 3*plan['rank']==32*u+1 and RANK.rho(u)==3*u<plan['rank']
    assert data['child_debt']['integer_potential']>data['parent']['integer_potential']
    a,b=(u-13)//72,(32*u-11)//81
    assert a>0 and a%8==b%8==5 and a%9==0
    c=a//9
    assert b==256*c+5
    ha,hb,hu,hz=(RANK.absorption_plan(x) for x in (a,b,u,plan['lower_seed']))
    assert hu['coefficients']==RANK.combine((1,{a:1}),(1,ha['coefficients']))
    assert hz['coefficients']==RANK.combine((1,{b:1}),(1,hb['coefficients']))
    sibling=RANK.combine((1,{b:1,48*c+1:1,36*c+1:1}),(-1,{a:1}))
    assert RANK.divergence(sibling)==RANK.atoms((1,b),(-1,a))
    assert hb['current']==RANK.combine((1,sibling),(1,ha['current']))
    assert hb['coefficients']==ha['coefficients']
    assert plan['coefficients']=={u:1,a:1,b:-1}
    return dict(seed=w,rank=plan['rank'],current=plan['current'],coefficients=plan['coefficients'],
                family=data,small_positive=a,small_negative=b,status='rho_valid_debt_failure',ordinary_forward_word=[1,2],
                endpoint=r,normalized_endpoint=3*u,leading=u,
                quotient_length=2,ordinary_common_tail_clocks=[3,1])


def compile_plan(data,supplied):
    """Supply exact currents normally; the rejected debt adds no premise."""
    RANK.validate_step(data['seed'],data)
    return RANK.compile_plan(data,supplied)
