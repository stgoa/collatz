"""Two exact inverse phases, allowing growth between their endpoints.

Only the final pair requests must decrease in critical-image rank. Missing
currents remain explicit; the constructor never discovers unknown orbits.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('double_base', HERE.parent/'nonselected_inverse/inverse_phases.py')
BASE = module_from_spec(spec)
spec.loader.exec_module(BASE)
RANK, OLD = BASE.RANK, BASE.OLD
NINE, T, NORMAL = RANK.NINE, RANK.T, RANK.NORMAL
combine, atoms, divergence = RANK.combine, RANK.atoms, RANK.divergence


def parameters(w):
    if not BASE.eligible(w) or w % 3 == 0:
        raise ValueError('Require nonselected W5 with3 not dividing w')
    k = 4 if w % 3 == 2 else 8
    first = BASE.parameters(w,k)
    h, C, r = first['h'], first['C'], first['lower']
    assert h >= 1
    L = OLD.valuation3(2*r+1)
    if L < 3:
        raise ValueError('Require second inverse phase L>=3')
    p = 2**L*((2*r+1)//3**L)-1
    threshold = 5 if k == 4 else 6
    shrinking = h+L >= threshold
    assert (p < 3*w) == shrinking
    assert NORMAL.canonical(p) and p % 8 == 7 and p % 3 in (0,1)
    v = T.critical_inverse(p)
    assert v % 8 == 5 and RANK.rho(v) == p
    return dict(seed=w,k=k,h=h,C=C,L=L,intermediate=r,endpoint=p,
                child=v,parent_rank=3*w,rank_shrinking=shrinking,
                threshold=threshold,intermediate_grows=r>3*w)


def recognized(w):
    try:
        return parameters(w)['rank_shrinking']
    except ValueError:
        return False


def bridge(w):
    data = parameters(w)
    first = BASE.inverse_bridge(w,data['k'])
    second = OLD.phase_bridge(data['intermediate'])
    assert second['lower'] == data['endpoint'] and second['h'] == data['L']
    current = combine((1,first['current']),(1,second['current']))
    assert divergence(current) == atoms((1,3*w),(-1,data['endpoint']))
    return dict(parameters=data,current=current)


def pair_plan(w):
    data = bridge(w)
    par = data['parameters']
    if not par['rank_shrinking']:
        raise ValueError('The complete two-phase endpoint does not decrease')
    local = T.critical_step(par['endpoint'])
    v,z = par['child'],NORMAL.normal_form(w)
    assert local['pair'] == v and local['lower'] == v
    high,low = RANK.absorption_plan(v),RANK.absorption_plan(z)
    current = combine((1,data['current']),(1,local['current']),
                      (-1,NORMAL.bridge(w)['current']),
                      (1,high['current']),(-1,low['current']))
    coefficients = Counter({v:1})
    coefficients.update(high['coefficients'])
    coefficients.subtract(low['coefficients'])
    result = dict(seed=w,rank=3*w,parameters=par,current=current,
                  coefficients=NINE.clean(coefficients),status='descending')
    RANK.validate_step(w,result)
    return result


def compile_plan(data,supplied):
    RANK.validate_step(data['seed'],data)
    return RANK.compile_plan(data,supplied)


def parameter_family(k,h,L,index=0):
    """Exact h,L and nonselected w13mod32, for all positive family members."""
    if k not in (4,8) or h<1 or L<3 or index<0:
        raise ValueError('Require k4/8,h>=1,L>=3,index>=0')
    binary = 32*k
    C_binary = (1+13*k)*pow(3**h,-1,binary) % binary
    ternary = 3**(L+1)
    C_ternary = (1+3**L)*pow(2**(h+2),-1,ternary) % ternary
    first = C_binary+binary*((C_ternary-C_binary)*pow(binary,-1,ternary) % ternary)
    C = first+binary*ternary*index
    w = (3**h*C-1)//k
    data = parameters(w)
    assert (data['k'],data['h'],data['L']) == (k,h,L)
    assert w % 32 == 13
    return dict(seed=w,k=k,h=h,L=L,C=C,C_residue=first,C_period=binary*ternary,
                seed_period=3**h*binary*ternary//k)
