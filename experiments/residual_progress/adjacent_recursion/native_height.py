"""Scoped native-height inverse obstruction, with a fixed forward comparison.

All conditional currents keep their smaller W5 inputs. The complete inverse
claim is justified by the finite anchor plus the all-ray affine proof; finite
word probes are only implementation checks. No unknown orbit is searched here.
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


ADJ=load('native_adjacent','defect_normal_form/adjacent_defect.py')
RANK,NORMAL=ADJ.RANK,ADJ.NORMAL
C=RANK.INVERSE
combine,atoms,divergence=RANK.combine,RANK.atoms,RANK.divergence
ANCHOR_EDGES={1:1,7:11,9:7,11:17,17:1,25:9}
WORD=(1,1,1,1,2,2,1,2,1,1,2,1,1,1,2,3,1,1,
      2,1,2,1,1,1,1,1,3,1,1,1,4,2,2,4,3)


def prefix(seed,word):
    NORMAL._odd(seed)
    x,current,states=seed,Counter(),[seed]
    for a in word:
        if not isinstance(a,int) or a<1 or NORMAL.valuation2(3*x+1)!=a:
            raise ValueError('The prescribed exact valuation word fails')
        if x!=1:current[x]+=1
        x=NORMAL.step(x);states.append(x)
    current=combine((1,current))
    assert divergence(current)==atoms((1,seed),(-1,x))
    return dict(seed=seed,endpoint=x,word=list(word),states=states,current=current)


def verify_anchor():
    Q=set(ANCHOR_EDGES)
    assert Q=={x for x in range(1,27,2) if NORMAL.canonical(x)}
    assert {x for x in range(27,31,2) if NORMAL.canonical(x)}=={27}
    assert all(NORMAL.quotient_step(x)==y and y in Q for x,y in ANCHOR_EDGES.items())
    assert 27 not in Q and 31 not in Q
    assert NORMAL.quotient_step(27)==41 and NORMAL.quotient_step(41)==31
    path=prefix(31,WORD)
    assert len(WORD)==35 and sum(WORD)==56 and path['endpoint']==23
    assert NORMAL.normal_form(23)==11 and 11 in Q
    assert 31 not in path['states'][1:]
    return dict(quotient_edges=ANCHOR_EDGES,ordinary_prefix=path,
                unique_small_ancestor=dict(source=27,quotient_path=[27,41,31],
                                          ordinary_word=[1,2],slope=[8,9]))


def family(depth,index=1):
    if not isinstance(depth,int) or depth<3 or not isinstance(index,int) or index<1:
        raise ValueError('Require integer depth>=3 and positive index')
    q=31+2**57*3**depth*index
    n=(8*q-5)//9
    assert q%108==31 and NORMAL.canonical(q) and NORMAL.canonical(n)
    assert n==27+2**60*3**(depth-2)*index
    return dict(depth=depth,index=index,q=q,height=n)


def shadow_word(q,word):
    """Audit any supplied legal inverse word; all nonnegative ray indices work."""
    ADJ.adjacent_source(q)
    if q<=31 or (q-31)%3**len(word):
        raise ValueError('Require a lifted adjacent target at sufficient ternary precision')
    word=[(kind,index) for kind,index in word]
    actual,shadow,slope=q,31,Fraction(1)
    rows=[]
    for depth,(kind,index) in enumerate(word,1):
        old_gap=slope-Fraction(shadow+1,32)
        actual,alpha,beta=C.inverse_step(actual,kind,index)
        shadow,_,_=C.inverse_step(shadow,kind,index)
        slope*=alpha
        gap=slope-Fraction(shadow+1,32)
        assert gap==alpha*old_gap+(alpha-beta-1)/32>0
        assert actual==slope*(q-31)+shadow
        assert shadow==27 or shadow>=31
        if shadow==27:
            assert depth==2 and list(word[:depth])==[('ray0',0),('point',0)]
            assert slope==Fraction(8,9) and actual==(8*q-5)//9
        else:
            assert slope>1 and actual>q
        rows.append(dict(depth=depth,actual=actual,shadow=shadow,
                         slope=[slope.numerator,slope.denominator],
                         gap=[gap.numerator,gap.denominator]))
    return dict(q=q,height=(8*q-5)//9,word=[list(x) for x in word],rows=rows)


def paired_run(q):
    """The whole initial binary run; it does not close its signed residual."""
    ADJ.adjacent_source(q)
    a=NORMAL.valuation2(q+1);t=(q+1)//2**a
    assert a>=2 and t%4==(-3**a)%4 and (2**a*t)%27==5
    negative=prefix(q,[1]*(a-1)+[2])
    r=(3**a*t-1)//2
    assert negative['endpoint']==r
    m=a//2
    if a%2==0:
        z=3**(m-1)*t
        positive=prefix(q+2,[2]*(m-1))
        assert positive['endpoint']==4*z+1
        positive_current=combine((1,positive['current']),
                                 (1,atoms((1,4*z+1),(-1,z))))
        lower=z;clocks=[m,1]
    else:
        z=3**m*t
        positive=prefix(q+2,[2]*m)
        lower=2*z+1;clocks=[m,0]
        assert positive['endpoint']==lower
        positive_current=positive['current']
    current=combine((1,positive_current),(-1,negative['current']))
    residual=atoms((1,lower),(-1,r))
    assert divergence(current)==combine((1,ADJ.adjacent_source(q)),(-1,residual))
    return dict(q=q,a=a,t=t,lower=lower,upper=r,positive_clocks=clocks,
                negative_length=a,current=current,residual=residual)


def transported_undo(u):
    """Transporting R44 through R65 is exactly the old endpoint comparison."""
    adjacent=ADJ.defect_plan(u)
    old=ADJ.RETURN.forward_plan(u)
    q=adjacent['rank'];a=NORMAL.valuation2(q+1)
    G=prefix(q,[1]*(a-1)+[2])
    high=RANK.absorption_plan(q+2);low=RANK.absorption_plan(G['endpoint'])
    current=combine((1,adjacent['current']),(-1,old['current']))
    expected=combine((1,high['current']),(-1,G['current']),(-1,low['current']))
    coefficients=Counter(adjacent['coefficients']);coefficients.subtract(old['coefficients'])
    coefficients=RANK.NINE.clean(coefficients)
    target=Counter(high['coefficients']);target.subtract(low['coefficients'])
    assert current==expected and coefficients==RANK.NINE.clean(target)
    return dict(seed=u,q=q,current=current,coefficients=coefficients)


def forward_plan(q):
    """A strict-native-height plan on the full binary cylinder, including31."""
    ADJ.adjacent_source(q)
    if q<31 or (q-31)%2**57:
        raise ValueError('Require q=31 modulo2^57 in the adjacent domain')
    n=(8*q-5)//9
    negative=prefix(q,WORD)
    positive=prefix(q+2,[2]);s=positive['endpoint'];y=negative['endpoint']
    assert y==23+3**35*(q-31)//2**56
    assert 9*y+5<8*n and s==(3*q+7)//4 and s%3==1 and s<n
    upper=RANK.absorption_plan(s);lower=RANK.absorption_plan(y)
    assert all(RANK.rho(v)<=s for v in upper['coefficients'])
    assert all(RANK.rho(v)<n for v in lower['coefficients'])
    current=combine((1,positive['current']),(1,upper['current']),
                    (-1,negative['current']),(-1,lower['current']))
    coefficients=Counter(upper['coefficients']);coefficients.subtract(lower['coefficients'])
    result=dict(q=q,height=n,positive=positive,negative=negative,current=current,
                coefficients=RANK.NINE.clean(coefficients))
    return validate_plan(result)


def validate_plan(plan):
    q=plan['q'];source=ADJ.adjacent_source(q);n=(8*q-5)//9
    if plan.get('height')!=n:
        raise ValueError('Incorrect original native height')
    expected=source
    for u,c in plan['coefficients'].items():
        if not isinstance(u,int) or u<=0 or u%8!=5 or not isinstance(c,int) or not c:
            raise ValueError('Require signed nonzero W5 input coefficients')
        if RANK.rho(u)>=n:
            raise ValueError('A helper does not decrease the original native height')
        expected=combine((1,expected),(-c,RANK.T.pair_source(u)))
    if any(not isinstance(x,int) or not isinstance(c,int) for x,c in plan['current'].items()):
        raise ValueError('Require an integer current')
    if divergence(plan['current'])!=expected:
        raise ValueError('Incorrect conditional adjacent boundary')
    return plan


def compile_plan(plan,supplied):
    validate_plan(plan)
    current=plan['current']
    for u,c in plan['coefficients'].items():
        rows=supplied.get(u)
        if rows is None or any(not isinstance(x,int) or not isinstance(v,int) for x,v in rows.items()):
            raise ValueError('Missing integer supplied pair current')
        if divergence(rows)!=RANK.T.pair_source(u):
            raise ValueError('Incorrect supplied pair boundary')
        current=combine((1,current),(c,rows))
    assert divergence(current)==ADJ.adjacent_source(plan['q'])
    return current
