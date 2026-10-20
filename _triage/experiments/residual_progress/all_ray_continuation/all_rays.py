"""Complete ray-index search for two specified cycle/point continuations.

The ray cutoff is proved from the original rank. Exhaustion rejects this
particular procedure, not a pair current or an unrestricted inverse search.
"""
from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('all_rays_previous',HERE.parent/'refined_obstruction/refined_obstruction.py')
PREVIOUS=module_from_spec(spec);spec.loader.exec_module(PREVIOUS)
OLD=PREVIOUS.OLD
RANK,NORMAL,T,NINE=PREVIOUS.RANK,PREVIOUS.NORMAL,PREVIOUS.T,PREVIOUS.NINE
combine,atoms,divergence,rho=PREVIOUS.combine,PREVIOUS.atoms,PREVIOUS.divergence,PREVIOUS.rho
WORDS={17:(1,1,1,2,1,1,4),25:(1,1,2,1,1,4,1)}


def eligible(w):
    return OLD.eligible(w)


def ray(v,L):
    if not isinstance(v,int) or v<=0 or not isinstance(L,int) or L<0:
        raise ValueError('Require positive v and nonnegative ray index')
    power=64**L
    return power*(8*v+1)+49*((power-1)//63)


def parameters(w,L):
    if not eligible(w) or not isinstance(L,int) or L<0:
        raise ValueError('Require the selected entry domain and nonnegative L')
    data=OLD.OLD.parameters(w,4)
    q,v=data['rank'],data['nine_index']
    b=ray(v,L)
    c=25 if L%3==1 else 17
    h=RANK.INVERSE.valuation3(b+c)
    k=h//7
    p=2**(11*k)*(b+c)//3**(7*k)-c
    j=RANK.INVERSE.valuation3(p+1)
    eta=2**j*(p+1)//3**j-1
    assert p>0 and eta>0 and NORMAL.canonical(p) and NORMAL.canonical(eta)
    assert b%3==(L+1)%3 and b%8==1
    if k:
        assert NORMAL.valuation2(p+c)==11*k+1
        order=4 if c==17 else 3
        assert NORMAL.valuation2(p+1)==order
        assert NORMAL.valuation2(eta+1)==order+j and eta%3!=2
    else:
        assert NORMAL.valuation2(eta+1)==j+1
        assert j==0 if L%3!=1 else j>=1
    self_return=(k==0 and (j==0 or (j==1 and eta%3==0)))
    if not self_return:
        lead=T.critical_inverse(eta)
        assert lead%8==5 and rho(lead)==eta
    else:
        lead=w
    descending=not self_return and eta<q
    word=[1]*j+list(WORDS[c])*k+[2,6*L+1,1,4]
    return dict(seed=w,rank=q,v=v,L=L,base=b,center=c,ternary_depth=h,
                cycles=k,remainder=h-7*k,point_depth=j,cycle_endpoint=p,
                endpoint=eta,self_return=self_return,descending=descending,
                leading=lead,word=word,ordinary_length=len(word),
                total_valuation=sum(word))


def bridge(w,L):
    data=parameters(w,L)
    x,path,current=data['endpoint'],[data['endpoint']],Counter()
    for a in data['word']:
        assert NORMAL.valuation2(3*x+1)==a
        current[x]-=1;x=NORMAL.step(x);path.append(x)
    current=combine((1,current))
    assert x==data['rank']
    assert divergence(current)==atoms((1,x),(-1,data['endpoint']))
    return dict(parameters=data,path=path,current=current)


def pair_plan(w,L):
    inv=bridge(w,L);data=inv['parameters'];q=data['rank'];eta=data['endpoint']
    z=NORMAL.normal_form(w)
    high,low=RANK.absorption_plan(eta),RANK.absorption_plan(z)
    current=combine((1,NORMAL.bridge(3*w)['current']),(1,inv['current']),
                    (-1,NORMAL.bridge(w)['current']),
                    (1,high['current']),(-1,low['current']))
    cs=Counter(high['coefficients']);cs.subtract(low['coefficients']);cs=NINE.clean(cs)
    expected=T.pair_source(w)
    for u,c in cs.items():expected=combine((1,expected),(-c,T.pair_source(u)))
    assert divergence(current)==expected
    if data['self_return']:
        original=OLD.OLD.pair_plan(w,4)
        assert current==original['current'] and cs==original['coefficients']
        assert cs[w]==1 and all(rho(u)<q for u in cs if u!=w)
        status='original_request'
    elif not data['descending']:
        lead=data['leading']
        assert cs[lead]==1 and all(rho(u)<eta for u in cs if u!=lead)
        status='nondecreasing_request'
    else:
        status='descending'
    result=dict(seed=w,rank=q,parameters=data,current=current,coefficients=cs,status=status)
    if data['descending']:RANK.validate_step(w,result)
    return result


def ray_bound(w):
    """Every accepted ray is <=limit; all formulas use exact integer bounds."""
    if not eligible(w):raise ValueError('Require the complete entry domain')
    data=OLD.OLD.parameters(w,4);q,v=data['rank'],data['nine_index']
    J=(q-1).bit_length()-2
    P=3**J*(q-1)//2**J
    K=max(0,((P+24).bit_length()-2)//11)
    B=2187**K*(P+24)//2048**K-17
    ratio=(9*B+7)//(9*(8*v+1)+7)
    limit=(ratio.bit_length()-1)//6 if ratio else -1
    assert limit <= q.bit_length()-1
    return dict(seed=w,rank=q,J=J,P=P,K=K,B=B,ratio=ratio,limit=limit)


def decide(w,max_rays=None):
    """Exhaust this infinite ray family using its proved finite rank cutoff."""
    if max_rays is not None and (not isinstance(max_rays,int) or max_rays<0):
        raise ValueError('Require nonnegative max_rays or None')
    bound=ray_bound(w);tested=[]
    for L in range(bound['limit']+1):
        if max_rays is not None and len(tested)>=max_rays:
            return dict(seed=w,status='capped',bound=bound,tested=tested)
        data=parameters(w,L);tested.append(data)
        if data['descending']:
            return dict(seed=w,status='descending',bound=bound,tested=tested,plan=pair_plan(w,L))
    return dict(seed=w,status='exhausted',bound=bound,tested=tested)


def one_step(w):
    if not eligible(w):return None
    data=decide(w)
    return data.get('plan')


def compile_plan(plan,supplied):
    if plan['status']!='descending':raise ValueError('The plan retains a nondecreasing request')
    RANK.validate_step(plan['seed'],plan)
    return RANK.compile_plan(plan,supplied)


def ray_congruence(v,target,H):
    """Unique L mod3^H with b_L=target mod3^H, without constructing64^L."""
    if not isinstance(v,int) or v<=0 or not isinstance(target,int) or not isinstance(H,int) or H<0:
        raise ValueError('Require positive v, integer target, nonnegative precision')
    C=9*(8*v+1)+7
    L,period=0,1
    for level in range(1,H+1):
        modulus=3**(level+2)
        candidates=[L+period*d for d in range(3)
                    if (pow(64,L+period*d,modulus)*C-7-9*target)%modulus==0]
        assert len(candidates)==1
        L=candidates[0];period*=3
    return dict(v=v,target=target,precision=H,residue=L,period=period)


def density_bound(N=None):
    """Uniform cylinder-count bound, not an assertion that density exists."""
    S=Fraction(1,729)+Fraction(3,3**8-1)/(1-Fraction(1,3**7))+Fraction(3,3**70-1)
    assert S<Fraction(1,500) and 2**124>3**78
    result=dict(limsup_acceptance=[S.numerator,S.denominator],
                liminf_failure=[S.denominator-S.numerator,S.denominator])
    if N is not None:
        if not isinstance(N,int) or N<1:raise ValueError('Require N>=1')
        Tn=(15552*N).bit_length()-1
        error=5*Tn*Tn+6*Tn+1
        upper=N*S+error
        result.update(N=N,ray_count_bound=Tn,error=error,
                      accepted_count_upper=[upper.numerator,upper.denominator])
    return result


def phase_family(L,k,j,unit=1,index=0):
    """Complete high-point CRT cells for both admissible ray residues.

    This supplies inputs to audit the all-ray constructor, not a universal
    arithmetic selection theorem. k0 uses the point branch atL1mod3.
    """
    if (not all(isinstance(x,int) for x in (L,k,j,unit,index)) or L<0 or k<0
            or j<2 or unit not in (1,2) or index<0 or L%3==2
            or (k==0 and L%3!=1)):
        raise ValueError('Require L0/1mod3,k>=0,j>=2,unit1/2,index>=0; k0 needsL1')
    c=25 if L%3==1 else 17
    power=64**L
    offset=power+49*((power-1)//63)
    modulus=3**(7*k+j+1)
    desired=3**(7*k)*pow(2**(11*k),-1,modulus)*((c-1)+3**j*unit)-c
    vr=(desired-offset)*pow(8*power,-1,modulus)%modulus
    v=2041+2048*((vr-2041)*pow(2048,-1,modulus)%modulus)+2048*modulus*index
    w=(27*v+13)//16
    data=parameters(w,L)
    assert (data['cycles'],data['point_depth'])==(k,j)
    return dict(seed=w,L=L,k=k,j=j,unit=unit,index=index,v=v,v_period=2048*modulus,
                parameters=data)
