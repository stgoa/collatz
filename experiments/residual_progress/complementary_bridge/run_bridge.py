"""Complete arithmetic run-block bridges on R23's complementary family."""
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('run_halving',HERE.parent/'residual_return/halving_return.py')
H=module_from_spec(spec);spec.loader.exec_module(H)
spec=spec_from_file_location('run_normal_form',HERE.parent/'bridge_normal_form/normal_form.py')
NORMAL=module_from_spec(spec);spec.loader.exec_module(NORMAL)
step,combine,divergence=H.step,H.combine,H.divergence

def parameters(x):
    a,t=H.parameters(x)
    if H.selected(x):
        raise ValueError('Use the complementary R23 family')
    v=3**(a-1)*t-1
    d=(v&-v).bit_length()-1
    assert d>=2
    return a,t,d,v//2**d

def target(x):
    a,t,d,w=parameters(x)
    return 3**(d//2)*w if d%2 else 2*3**(d//2)*w+1

def bridge(x):
    a,t,d,w=parameters(x)
    left=[x]
    for _ in range(a):left.append(step(left[-1]))
    assert left[-1]==3*2**(d-1)*w+1
    extra=(d-3)//2 if d%2 else d//2-1
    for _ in range(extra):
        assert (3*left[-1]+1)%8==4
        left.append(step(left[-1]))
    z=target(x)
    if d%2:
        assert left[-1]==4*z+1
        left.append(step(left[-1]));right=[z,step(z)]
        assert left[-1]==right[-1]
    else:
        assert left[-1]==z and z%4==3
        right=[z]
    current=combine((1,H.path_current(left)),(-1,H.path_current(right)))
    expected=combine((1,{x:1}),(-1,{z:1}))
    assert divergence(current)==expected
    return dict(root=x,a=a,t=t,d=d,w=w,target=z,left=left,right=right,current=current)

def cylinder(a,d):
    assert a>=2 and d>=2
    modulus=2**(d+1)
    t=((1+2**d)*pow(3**(a-1),-1,modulus))%modulus
    return 2**a*t-1,2**(a+d+1)

def slope(a,d):
    return F((1 if d%2 else 2)*3**(a-1+d//2),2**(a+d))

def cutoff(N,a,d):
    c=3**(d//2);A=c*3**(a-1)
    if d%2:return F(2**(a+d)*N+2**a*c,A)-1
    return F(2**(a+d)*(N-1)+2**(a+1)*c,2*A)-1

def progression_count(N,a,d):
    binary,power=cylinder(a,d)
    high=cutoff(N,a,d)
    intervals=((1,F(N),F(3*N,2),3,12),
               (1,F(9*N,8),F(3*N,2),7,12),
               (2,F(N),F(9*N,8),7,36),
               (2,F(N),F(9*N,8),19,36))
    result=0
    for weight,low,top,r,m in intervals:
        top=min(top,high)
        if top<=low:continue
        odd=m//4
        index=((r-binary)*pow(power,-1,odd))%odd
        residue=(binary+power*index)%(power*odd)
        result+=weight*H.COMPLEMENT.strict_count(low,top,residue,power*odd)
    return result

def mass_formula(N):
    if not isinstance(N,int) or N<8 or N%8:raise ValueError('Require 8|N, N>=8')
    A=(3*N//2).bit_length()-1
    result=0
    for a in range(2,A+1):
        tmax=(3*N//2)//2**a
        dmax=(3**(a-1)*tmax-1).bit_length()-1
        for d in range(2,dmax+1):result+=progression_count(N,a,d)
    return result

def leading_interval(K=64):
    """Exact rational enclosure of the universal leading coefficient."""
    assert K>=4
    lower=F(0)
    for a in range(2,K-1):
        for d in range(2,K-a+1):
            h=1/slope(a,d)
            v=(F(7,9)*max(F(0),min(F(9,8),h)-1)
               +F(2,3)*max(F(0),min(F(3,2),h)-F(9,8)))
            lower+=v/2**(a+d+1)
    upper=lower+F(25*(K-1),72*2**(K+1))
    return lower,upper

def selected_profile(N):
    residual=H.COMPLEMENT.residual_profile(N)[2]
    return {x:c for x,c in residual.items() if not H.selected(x) and target(x)<N}

def certify(N,lower_current):
    if divergence(lower_current)!=H.LOCAL.count(N):raise ValueError('Supply exact U_N current')
    removed=selected_profile(N)
    lower_edges={x:step(x) for x,c in lower_current.items() if c}
    sources,arithmetic,extra={},{},set()
    for x,c in removed.items():
        data=bridge(x);z=data['target']
        assert z<N
        sources[z]=sources.get(z,0)+c
        arithmetic=combine((1,arithmetic),(c,data['current']))
        extra.update(data['left'][:-1])
        assert all(lower_edges.get(u)==v for u,v in zip(data['right'],data['right'][1:]))
    known=H.COMPLEMENT.extract_exact(sources,lower_edges)
    current=combine((1,known),(1,arithmetic))
    assert divergence(current)==removed and all(c>0 for c in current.values())
    assert set(current)<=set(lower_edges)|extra
    old=H.COMPLEMENT.residual_profile(N)[2]
    old_remaining={x:c for x,c in old.items() if not H.selected(x)}
    remaining=combine((1,old_remaining),(-1,removed))
    assert all(c>0 for c in remaining.values())
    return dict(N=N,removed=removed,remaining=remaining,current=current,
                target_source=sources,new_rows=sorted(extra-set(lower_edges)))

def normal_target(x):
    return NORMAL.normal_form(target(x))

def normalized_bridge(x):
    data=bridge(x)
    normalized=NORMAL.bridge(data['target'])
    current=combine((1,data['current']),(1,normalized['current']))
    minimum=normalized['minimum']
    expected={x:1}
    if minimum!=1:expected=combine((1,expected),(-1,{minimum:1}))
    assert divergence(current)==expected
    return dict(root=x,target=minimum,raw_target=data['target'],current=current,
                arithmetic=data,normalization=normalized)

def normalized_cell_count(N,a,d):
    """Exact count through canonical targets and their full arithmetic fibres."""
    x0,period=cylinder(a,d)
    f0=target(x0)
    g=2 if d%2 else 4
    A=3**(a-1+d//2)
    advance=g*A
    tmax=(3*N//2)//2**a
    fmax=((1 if d%2 else 2)*3**(d//2)*(3**(a-1)*tmax-1))//2**d+(0 if d%2 else 1)
    if fmax<1:return 0
    kmax=(fmax.bit_length()+1)//2 if d%2 else 0
    intervals=((1,F(N),F(3*N,2),3,12),
               (1,F(9*N,8),F(3*N,2),7,12),
               (2,F(N),F(9*N,8),7,36),
               (2,F(N),F(9*N,8),19,36))
    answer=0
    for k in range(kmax+1):
        for partner in (False,True):
            scale=4**k*(2 if partner else 1)
            offset=(4**(k+1)-1)//3 if partner else (4**k-1)//3
            for weight,low,high,r,m in intervals:
                qlow=(F(advance,period)*(low-x0)+f0-offset)/scale
                qhigh=min(F(N),(F(advance,period)*(high-x0)+f0-offset)/scale)
                if qhigh<=qlow:continue
                qlo=max(0,qlow.numerator//qlow.denominator)
                qhi=max(0,-((-qhigh.numerator)//qhigh.denominator)-1)
                if qhi<=qlo:continue
                odd=A*(m//4)
                residue=((A*(r-x0)-(period//g)*(offset-f0))
                         *pow((period//g)*scale,-1,odd))%odd
                count=(NORMAL.canonical_count(qhi,residue,odd)
                       -NORMAL.canonical_count(qlo,residue,odd))
                if not d%2 and not partner:
                    # The even return is3mod4; remove canonical1mod8 targets.
                    index=((residue-1)*pow(8,-1,odd))%odd
                    first=(1+8*index)%(8*odd)
                    count-=max(0,(qhi-first)//(8*odd)+1)-max(0,(qlo-first)//(8*odd)+1)
                answer+=weight*count
    return answer

def normalized_mass_formula(N):
    if not isinstance(N,int) or N<8 or N%8:raise ValueError('Require 8|N, N>=8')
    A=(3*N//2).bit_length()-1
    answer=0
    for a in range(2,A+1):
        tmax=(3*N//2)//2**a
        dmax=(3**(a-1)*tmax-1).bit_length()-1
        for d in range(2,dmax+1):answer+=normalized_cell_count(N,a,d)
    return answer

def normalized_leading_interval(K=64):
    assert K>=4
    def g(h):
        return (F(7,9)*max(F(0),min(F(9,8),h)-1)
                +F(2,3)*max(F(0),min(F(3,2),h)-F(9,8)))
    lower=F(0)
    for a in range(2,K-1):
        for d in range(2,K-a+1):
            L=slope(a,d)
            if d%2:
                k=0;value=F(0)
                while F(4**k)/L<F(3,2):
                    value+=(g(F(4**k)/L)/2+g(F(2*4**k)/L)/4)/4**k
                    k+=1
                value+=F(25,72*4**k)
            else:value=(g(1/L)+g(2/L))/2
            lower+=value/2**(a+d+1)
    return lower,lower+F(25*(K-1),72*2**(K+1))

def normalized_profile(N):
    residual=H.COMPLEMENT.residual_profile(N)[2]
    return {x:c for x,c in residual.items() if not H.selected(x) and normal_target(x)<N}

def certify_normalized(N,lower_current):
    if divergence(lower_current)!=H.LOCAL.count(N):raise ValueError('Supply exact U_N current')
    removed=normalized_profile(N)
    lower_edges={x:step(x) for x,c in lower_current.items() if c}
    targets,arithmetic,explicit={},{},set()
    for x,c in removed.items():
        data=normalized_bridge(x);z=data['target']
        assert z<N
        if z!=1:targets[z]=targets.get(z,0)+c
        arithmetic=combine((1,arithmetic),(c,data['current']))
        explicit.update(data['current'])
    known=H.COMPLEMENT.extract_exact(targets,lower_edges)
    signed=combine((1,known),(1,arithmetic))
    assert divergence(signed)==removed
    current=H.COMPLEMENT.extract_exact(removed,{x:step(x) for x in signed})
    assert set(current)<=set(lower_edges)|explicit
    old=H.COMPLEMENT.residual_profile(N)[2]
    old_remaining={x:c for x,c in old.items() if not H.selected(x)}
    remaining=combine((1,old_remaining),(-1,removed))
    assert all(c>0 for c in remaining.values())
    return dict(N=N,removed=removed,remaining=remaining,current=current,
                target_source=targets,new_rows=sorted(explicit-set(lower_edges)))
