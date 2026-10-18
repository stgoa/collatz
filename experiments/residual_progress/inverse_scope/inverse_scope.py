"""Complete finite inverse exclusions and their all-ray affine lifts.

Stored forward-closed certificates, not a search cap, exclude all inverse
depths at their anchors. Forward witnesses are already covered by R48; they
illustrate why inverse-only completion is insufficient.
"""
from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name,path):
    spec = spec_from_file_location(name,HERE.parent/path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


RANK = load('scope_rank','critical_rank/rank_closure.py')
SAT = load('scope_saturation','known_saturation/saturation.py')
C, NORMAL = RANK.INVERSE, RANK.NORMAL
combine, atoms, divergence = C.combine, C.atoms, C.divergence


def table(rows):
    return [[x,c] for x,c in sorted(rows.items())]


def from_table(rows):
    if any(not isinstance(row,list) or len(row)!=2 or
           any(not isinstance(x,int) for x in row) for row in rows):
        raise ValueError('Require an exact integer two-column table')
    result = dict(rows)
    if len(result) != len(rows):
        raise ValueError('Duplicate table keys')
    return result


def verify_closed_exclusion(anchor, edges):
    """Finite proof of no smaller canonical ancestor, at any depth.

    Absorption is not required for this invariant-set exclusion itself.
    """
    if anchor <= 1 or not NORMAL.canonical(anchor):
        raise ValueError('Require a nontrivial canonical anchor')
    Q = set(edges)
    if anchor in Q or any(not NORMAL.canonical(q) for q in Q):
        raise ValueError('The closed set must be canonical and exclude the anchor')
    for q,y in edges.items():
        if y != NORMAL.quotient_step(q) or y not in Q:
            raise ValueError('The supplied table is not exactly T-forward-closed')
    smaller = {q for q in range(1,anchor,2) if NORMAL.canonical(q)}
    if not smaller <= Q:
        raise ValueError('A smaller canonical origin is missing')
    return dict(anchor=anchor,bases=Q,smaller=smaller,edges=edges)


def forward_witness(w):
    """Three quotient arrows in two complete R48-covered binary cylinders.

    The returned signed current has divergence[3w]-[target]; it is not an
    absorption current until its smaller target is supplied.
    """
    NORMAL._odd(w)
    if w % 256 == 13:
        kind='selected_endpoint'
    elif w % 128 == 45:
        kind='sibling_endpoint'
    else:
        raise ValueError('Require w13 modulo256 or w45 modulo128')
    q=3*w
    assert NORMAL.canonical(q) and not NORMAL.selected(q)
    path,current,x=[q],{},q
    for _ in range(3):
        bridge=NORMAL.quotient_bridge(x)
        current=combine((1,current),(1,bridge['current']))
        x=bridge['minimum']
        path.append(x)
    raw=(27*q+19)//16
    assert NORMAL.normal_form(raw)==x
    if kind=='selected_endpoint':
        assert q % 256==39 and NORMAL.selected(raw)
        assert x==(27*q+3)//32
    else:
        assert q % 128==7 and raw % 8==5
        assert x <= (27*q+3)//64
    assert x<q and 9*x+5<8*q
    assert divergence(current)==atoms((1,q),(-1,x))
    return dict(seed=w,rho=q,kind=kind,target=x,path=path,raw_endpoint=raw,current=current)


def forward_plan(w):
    """A strict-rho conditional plan, used as a barrier-resolution witness."""
    data=forward_witness(w)
    z=NORMAL.normal_form(w)
    high,low=RANK.absorption_plan(data['target']),RANK.absorption_plan(z)
    current=combine((1,data['current']),(-1,NORMAL.bridge(w)['current']),
                    (1,high['current']),(-1,low['current']))
    coefficients=Counter(high['coefficients'])
    coefficients.subtract(low['coefficients'])
    coefficients=C.NINE.clean(coefficients)
    result=dict(seed=w,rho=data['rho'],current=current,coefficients=coefficients,
                forward=data)
    RANK.validate_step(w,result)
    return result


def build_certificate(anchor, step_cap=1000, bit_cap=1024):
    """Capped discovery only for the two stored small demonstrations."""
    if anchor not in (39,135):
        raise ValueError('Discovery is restricted to the two declared anchors')
    Q={1}
    for seed in range(1,anchor,2):
        if not NORMAL.canonical(seed):
            continue
        x,seen=seed,set()
        for _ in range(step_cap+1):
            Q.add(x)
            if x==1:
                break
            if x in seen or len(seen)>=step_cap or x.bit_length()>bit_cap:
                raise RuntimeError('Unresolved capped lower-input discovery')
            seen.add(x)
            x=NORMAL.quotient_step(x)
        else:
            raise AssertionError('Unreachable')
    edges={q:NORMAL.quotient_step(q) for q in Q}
    verify_closed_exclusion(anchor,edges)
    core=SAT.compile_core(Q)
    lower=Counter()
    for seed in range(1,anchor,2):
        lower.update(SAT.certify_member(seed,core)['current'])
    lower=combine((1,lower))
    assert divergence(lower)==dict.fromkeys(range(3,anchor,2),1)
    data=forward_witness(anchor//3)
    upper_absorption=combine((1,data['current']),
                             (1,SAT.certify_member(data['target'],core)['current']))
    pair=combine((1,upper_absorption),(-1,SAT.certify_member(anchor//3,core)['current']))
    assert divergence(pair)==C.T.pair_source(anchor//3)
    return dict(anchor=anchor,quotient_edges=table(edges),lower_current=table(lower),
                forward_path=data['path'],forward_current=table(data['current']),
                pair_current=table(pair),discovery_caps=dict(steps=step_cap,bits=bit_cap))


def verify_certificate(data):
    anchor=data['anchor']
    edges=from_table(data['quotient_edges'])
    proof=verify_closed_exclusion(anchor,edges)
    # Verify that Q is exactly the supplied smaller-origin closure, not a
    # larger closed set chosen merely to make the exclusion true.
    reached=set()
    for seed in proof['smaller']:
        x=seed
        while x not in reached:
            reached.add(x)
            x=edges[x]
    if reached!=proof['bases']:
        raise ValueError('The table is not the complete smaller-origin closure')
    core=SAT.compile_core(proof['bases'])
    lower=from_table(data['lower_current'])
    if divergence(lower)!=dict.fromkeys(range(3,anchor,2),1):
        raise ValueError('Incorrect supplied lower absorption current')
    if any(c<=0 for c in lower.values()):
        raise ValueError('This stored input is required to be nonnegative')
    # Reconstruct each requested input path only in the already finite core.
    expected=Counter()
    for seed in range(1,anchor,2):
        expected.update(SAT.certify_member(seed,core)['current'])
    if lower!=combine((1,expected)):
        raise ValueError('Stored lower current does not match the finite core')
    forward=forward_witness(anchor//3)
    if data['forward_path']!=forward['path'] or from_table(data['forward_current'])!=forward['current']:
        raise ValueError('Incorrect stored forward escape')
    if any(q in proof['bases'] for q in forward['path'][:-1]) or forward['target'] not in proof['bases']:
        raise ValueError('The displayed first known-history entry is incorrect')
    pair=combine((1,forward['current']),
                 (1,SAT.certify_member(forward['target'],core)['current']),
                 (-1,SAT.certify_member(anchor//3,core)['current']))
    if from_table(data['pair_current'])!=pair or divergence(pair)!=C.T.pair_source(anchor//3):
        raise ValueError('Incorrect stored tripling current')
    return dict(proof,core=core,lower_current=lower,pair_current=pair,forward=forward)


def lifted_witness(anchor,D,index=1):
    minimum={39:2,135:4}
    if anchor not in minimum or not isinstance(D,int) or D<minimum[anchor]:
        raise ValueError('Require anchor39,D>=2 or anchor135,D>=4')
    if not isinstance(index,int) or index<1:
        raise ValueError('Require a positive family index')
    q=anchor+256*3**D*index
    w=q//3
    assert q%3==0 and NORMAL.canonical(q) and w%8==5
    assert C.valuation3(q)==C.valuation3(anchor)
    assert not NORMAL.selected(3*w)
    if anchor==39:
        assert w%256==13
    else:
        assert w%128==45 and w%9==0
    return dict(anchor=anchor,D=D,index=index,q=q,w=w,
                ternary_valuation=C.valuation3(q),forward=forward_witness(w))


def shadow_lift(anchor,edges,q,word):
    """Audit any complete inverse word against an all-depth excluded anchor.

    Every ray index is allowed. The finite source table proves c>=anchor
    for every possible shadow; no tree truncation is used in that argument.
    """
    verify_closed_exclusion(anchor,edges)
    D=len(word)
    if D<1 or q<=anchor or not NORMAL.canonical(q) or (q-anchor)%3**D:
        raise ValueError('Require q>anchor canonical and q=anchor modulo3^word_length')
    actual,shadow,slope=q,anchor,Fraction(1)
    states=[]
    for depth,(kind,index) in enumerate(word,1):
        assert actual%3==shadow%3
        old_gap=slope-Fraction(shadow+1,anchor+1)
        actual,alpha,beta=C.inverse_step(actual,kind,index)
        shadow,_,_=C.inverse_step(shadow,kind,index)
        slope*=alpha
        gap=slope-Fraction(shadow+1,anchor+1)
        assert shadow>=anchor and shadow not in edges
        assert gap==alpha*old_gap+(alpha-beta-1)/(anchor+1)>0
        assert slope>1 and actual==slope*(q-anchor)+shadow>q
        states.append(dict(depth=depth,state=actual,shadow=shadow,
                           slope=[slope.numerator,slope.denominator],
                           gap=[gap.numerator,gap.denominator]))
    return dict(anchor=anchor,q=q,word=[[kind,index] for kind,index in word],states=states)
