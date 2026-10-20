"""Exact classification of the only above-seed request in formal absorption.

The returned plans remain conditional on every signed W5 input. No sigma
edge or unknown absorption history is used by this rho interface.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, relative):
    spec = spec_from_file_location(name, HERE.parent / relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


FORWARD = load('sharp_forward', 'nonselected_forward/nonselected_forward.py')
RANK = load('sharp_rank', 'critical_rank/rank_closure.py')
NORMAL = RANK.NORMAL


def absorption_bound(seed):
    """All requests have rho<=minimum, apart from the stated unique lead."""
    n = NORMAL.normal_form(seed)
    exception = None
    if n % 48 == 27 and NORMAL.valuation2(3*n-1) == 4:
        z = (3*n-1)//16
        if not NORMAL.canonical(3*z):
            u = 4*z+1
            assert u % 8 == 5 and RANK.rho(u) == (9*n+5)//8 > n
            exception = dict(index=u, coefficient=1, rank=RANK.rho(u), z=z)
    bound = (exception['rank'] if exception else n) if n > 1 else 0
    if n < seed:
        assert bound < seed
    return dict(seed=seed, minimum=n, bound=bound, exception=exception)


def absorption_plan(seed):
    data = RANK.absorption_plan(seed)
    bound = absorption_bound(seed)
    n, exception = bound['minimum'], bound['exception']
    above = {u:c for u,c in data['coefficients'].items() if RANK.rho(u)>n}
    expected = {exception['index']:1} if exception else {}
    assert above == expected
    assert all(RANK.rho(u)<=bound['bound'] for u in data['coefficients'])
    if exception:
        assert all(RANK.rho(u)<n for u in data['coefficients'] if u!=exception['index'])
    return dict(data, sharp_bound=bound)


def eligible(w):
    return isinstance(w,int) and w>0 and w%512==437


def fifth_plan(w):
    """Complete original-rho classification on w=437 modulo512."""
    if not eligible(w):
        raise ValueError('Require a positive input w=437 modulo512')
    data = FORWARD.forward_plan(w)
    par = data['parameters']
    assert (par['a'],par['d']) == (5,3)
    q, f = RANK.rho(w), par['endpoint']
    bound = absorption_bound(f)
    assert f < q
    m = (w-437)//512
    failure = False
    if m%16 == 7:
        z = 2147+4374*((m-7)//16)
        failure = not NORMAL.canonical(3*z)
    accepted = bound['bound'] < q
    assert accepted == (not failure)
    result = dict(data, status='descending' if accepted else 'unresolved',
                  sharp_bound=bound, family_index=m)
    if accepted:
        RANK.validate_step(w,result)
    else:
        high = {u:c for u,c in data['coefficients'].items() if RANK.rho(u)>=q}
        assert high == {bound['exception']['index']:1}
    return result


def one_step(w):
    if not eligible(w):
        return None
    plan = fifth_plan(w)
    return plan if plan['status']=='descending' else None


def fresh_family(index=0):
    if not isinstance(index,int) or index<0:
        raise ValueError('Require a nonnegative index')
    w = 4021+294912*index
    data = fifth_plan(w)
    assert data['status']=='descending'
    return dict(seed=w,index=index,residue=4021,period=294912)


def compile_plan(plan,supplied):
    if plan['status']!='descending':
        raise ValueError('Unresolved original-rho comparison')
    RANK.validate_step(plan['seed'],plan)
    return RANK.compile_plan(plan,supplied)
