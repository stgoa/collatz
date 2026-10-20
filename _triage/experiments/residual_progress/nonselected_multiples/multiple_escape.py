"""Complete two-block interface for nonselected W5 multiples of three.

Plans retain every missing pair current.  The strict-rank subdomain is
arithmetic and unbounded; no universal coverage or orbit termination is used.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('multiple_phases', HERE.parent/'nonselected_inverse/inverse_phases.py')
PHASE = module_from_spec(spec)
spec.loader.exec_module(PHASE)
RANK, OLD, NINE, T, NORMAL = PHASE.RANK, PHASE.OLD, PHASE.NINE, PHASE.T, PHASE.NORMAL
spec = spec_from_file_location('multiple_spine', HERE.parent/'inverse_escape/inverse_escape.py')
SPINE = module_from_spec(spec)
spec.loader.exec_module(SPINE)
combine, atoms, divergence = PHASE.combine, PHASE.atoms, PHASE.divergence


def eligible(w):
    return PHASE.eligible(w) and w % 3 == 0


def parameters(w, k):
    if not eligible(w) or k not in (4, 8):
        raise ValueError('Require nonselected W5 with 3|w and k=4 or8')
    D = OLD.valuation3(w)
    u = w//3**D
    b = 2*k*w+1
    s = 2*k*4**D*u+1
    j = OLD.valuation3(k*4**D*u+1)
    C = (k*4**D*u+1)//3**j
    p = 2**(j+1)*C-1
    numerator, denominator = k*2**(2*D+j+1), 3**(D+j+1)
    descending = numerator < denominator
    assert NORMAL.canonical(p) and NORMAL.valuation2(p+1) == j+1
    assert (p < 3*w) == descending
    assert (j > 0) == (u % 3 == (2 if k == 4 else 1))
    child = T.critical_inverse(p) if j else None
    domain = None if child is None else ('W9' if child % 16 == 9 else 'W5')
    if j:
        assert p % 3 in (0, 1)
        assert (domain == 'W9') == (j == 1 and p % 3 == 0)
    if descending:
        assert j >= 4 and domain == 'W5'
    return dict(w=w,k=k,D=D,u=u,b=b,spine=s,j=j,C=C,p=p,
                slope=[numerator,denominator],descending=descending,
                child=child,child_domain=domain,parent_rank=3*w,
                index_shrinking=bool(child and child < w))


def inverse_bridge(w, k):
    data = parameters(w,k)
    spine = SPINE.spine_bridge(data['b'])
    assert spine['D'] == data['D'] and spine['j'] == data['j'] and spine['p'] == data['p']
    b, q = data['b'], 3*w
    successor = NORMAL.step(b)
    normalization = NORMAL.bridge(successor)
    assert normalization['minimum'] == q
    forward = combine((1,{b:1}),(1,normalization['current']))
    current = combine((1,spine['current']),(-1,forward))
    assert divergence(current) == atoms((1,q),(-1,data['p']))
    return dict(parameters=data,current=current,word=spine['word'],path=spine['path'])


def pair_plan(w, k):
    """Full conditional plan for either ray, including nondecreasing cases."""
    inv = inverse_bridge(w,k)
    data = inv['parameters']
    p, z = data['p'], NORMAL.normal_form(w)
    if not data['j']:
        high, low = RANK.absorption_plan(p), RANK.absorption_plan(z)
        current = combine((1,inv['current']),(-1,NORMAL.bridge(w)['current']),
                          (1,high['current']),(-1,low['current']))
        coefficients = Counter(high['coefficients'])
        for v,c in low['coefficients'].items():
            coefficients[v] -= c
        coefficients = NINE.clean(coefficients)
        assert not current and coefficients == {w:1}
    else:
        v = data['child']
        child = NINE.five_plan(v)
        high, low = RANK.absorption_plan(v), RANK.absorption_plan(z)
        current = combine((1,inv['current']),(-1,NORMAL.bridge(3*v)['current']),
                          (-1,NORMAL.bridge(w)['current']), (1,child['current']),
                          (1,high['current']),(-1,low['current']))
        coefficients = Counter(child['coefficients'])
        for a,c in high['coefficients'].items():
            coefficients[a] += c
        for a,c in low['coefficients'].items():
            coefficients[a] -= c
        coefficients = NINE.clean(coefficients)
        if data['child_domain'] == 'W5' and not data['descending']:
            assert coefficients[v] == 1 and RANK.rho(v) >= 3*w
            assert all(RANK.rho(a) < p for a in coefficients if a != v)
        elif data['child_domain'] == 'W9':
            C = data['C']
            lead = w if C < 3*w else (2*C+1)//3
            assert C != 3*w and coefficients[lead] == 1
            assert RANK.rho(lead) == max(C,3*w)
            assert all(RANK.rho(a)<RANK.rho(lead) for a in coefficients if a != lead)
    expected = T.pair_source(w)
    for v,c in coefficients.items():
        expected = combine((1,expected),(-c,T.pair_source(v)))
    assert divergence(current) == expected
    plan = dict(seed=w,parameters=data,current=current,coefficients=coefficients,
                status='descending' if all(RANK.rho(v)<3*w for v in coefficients) else 'unresolved')
    if data['descending']:
        RANK.validate_step(w,plan)
    assert (plan['status'] == 'descending') == data['descending']
    return plan


def decreasing_plan(w):
    """Return the strict-rank rule, or None if its integer slope test fails."""
    if not eligible(w):
        return None
    D = OLD.valuation3(w)
    k = 4 if (w//3**D) % 3 == 2 else 8
    if not parameters(w,k)['descending']:
        return None
    return pair_plan(w,k)


def return_defect(w,k):
    """Exact j=1,p=0mod3 return, as P(w) plus a formal forward defect."""
    data = parameters(w,k)
    if data['j'] != 1 or data['p'] % 3:
        raise ValueError('Require the W9 return case j=1,p=0 modulo3')
    C = data['C']
    successor = NORMAL.step(C)
    high, low = RANK.absorption_plan(C), RANK.absorption_plan(successor)
    current = combine((1,high['current']),(-1,{C:1}),(-1,low['current']))
    coefficients = Counter({w:1})
    for a,c in high['coefficients'].items():
        coefficients[a] += c
    for a,c in low['coefficients'].items():
        coefficients[a] -= c
    coefficients = NINE.clean(coefficients)
    full = pair_plan(w,k)
    assert current == full['current'] and coefficients == full['coefficients']
    d = NORMAL.valuation2(9*data['child']-1)
    assert d == 2*data['D']+(4 if k == 4 else 5)
    assert C % 16 == 11 and C % 3 == 1
    return dict(seed=w,k=k,C=C,successor=successor,d=d,current=current,
                coefficients=coefficients)


def parameter_witness(D,j,k=4,terminal=1,index=0):
    """Complete CRT cylinder with w=13mod32 and exact D,j,terminal unit."""
    if not isinstance(D,int) or D<1 or not isinstance(j,int) or j<1:
        raise ValueError('Require D,j positive integers')
    if k not in (4,8) or terminal not in (1,2) or not isinstance(index,int) or index<0:
        raise ValueError('Require k4/8, terminal1/2 and nonnegative index')
    modulus = 3**(j+1)
    u3 = ((terminal*3**j-1)*pow(k*4**D,-1,modulus))%modulus
    u2 = (13*pow(3**D,-1,32))%32
    u = u2+32*((u3-u2)*pow(32,-1,modulus)%modulus)+32*modulus*index
    w = 3**D*u
    data = parameters(w,k)
    assert w%32 == 13 and data['D']==D and data['j']==j and data['C']%3==terminal
    return dict(data,unit_period=32*modulus,w_period=32*3**(D+j+1),index=index,terminal=terminal)


def compile_plan(plan,supplied):
    RANK.validate_step(plan['seed'],plan)
    return RANK.compile_plan(plan,supplied)
