"""Exact finite replay for the scoped all-ray theorem; no orbit assumption."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import all_rays as M

HERE=Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def rows(value):
    return [[x,c] for x,c in sorted(value.items())]


def expect_error(action):
    try:action()
    except ValueError:return
    raise AssertionError('Expected rejection')


def isometry_checks():
    pairs=[]
    for v in (4089,10233,16377):
        for L in range(25):
            for R in range(L):
                assert M.RANK.INVERSE.valuation3(M.ray(v,L)-M.ray(v,R))==M.RANK.INVERSE.valuation3(L-R)
                pairs.append([v,L,R])
        for H in range(1,6):
            modulus=3**H
            assert len({M.ray(v,L)%modulus for L in range(modulus)})==modulus
    lifts=[]
    for target in (-17,-25,-1,123):
        for H in (0,1,2,3,7,16,32):
            d=M.ray_congruence(4089,target,H)
            modulus=3**(H+2)
            C=9*M.ray(4089,0)+7
            assert (pow(64,d['residue'],modulus)*C-7-9*target)%modulus==0
            lifts.append(d)
    return dict(pair_cases=len(pairs),pair_hash=digest(pairs),permutation_cases=15,lifts=lifts)


def affine_checks():
    records=[]
    for L in range(1,17):
        for c in (17,25):
            for k in (0,10*L-1,10*L):
                for j in (0,8*L-1,8*L):
                    a,t=Fraction(2048,2187)**k,Fraction(2,3)**j
                    lam=Fraction(256,81)*64**L*a*t
                    for q in (10351,155520001):
                        b=Fraction(64**L*(256*q-40)-63,81)
                        eta=t*(a*(b+c)-(c-1))-1
                        assert eta==lam*(q-Fraction(5,32))+t*(a*(c-Fraction(7,9))-(c-1))-1
                        if k<10*L and j<8*L:
                            assert lam>3 and eta>q
                        records.append([L,c,k,j,q,eta.numerator,eta.denominator])
    d=M.density_bound(10**9)
    S=Fraction(*d['limsup_acceptance'])
    assert S<Fraction(1,500) and 2**124>3**78
    assert S==Fraction(1,729)+sum((Fraction(3,3**(70*L))+
           sum((Fraction(3,3**(7*k+8*L)) for k in range(10*L)),Fraction()))
           for L in range(1,8))+(
               Fraction(3,3**70-1)*Fraction(1,3**(70*7))+
               Fraction(3,3**8-1)/(1-Fraction(1,3**7))*Fraction(1,3**(8*7))+
               sum((Fraction(3,3**(8*L+70*L))/(1-Fraction(1,3**7)) for L in range(1,8)),Fraction()))
    return dict(cases=len(records),hash=digest(records),density=d)


def lifted_fixture(old,L):
    """Carry one exact maximality row to another compatible ray by CRT."""
    k,j=old['cycles'],old['point_depth']
    precision=old['ternary_depth']+j+2
    modulus=3**precision
    power=64**L
    offset=power+49*((power-1)//63)
    target=old['base']%modulus
    vr=(target-offset)*pow(8*power,-1,modulus)%modulus
    v=2041+2048*((vr-2041)*pow(2048,-1,modulus)%modulus)
    w=(27*v+13)//16
    new=M.parameters(w,L)
    assert (new['cycles'],new['point_depth'],new['remainder'])==(k,j,old['remainder'])
    return w


def full_plan(w,L,store=False):
    p=M.pair_plan(w,L);d=p['parameters'];path=M.bridge(w,L)['path']
    assert len(path)==d['ordinary_length']+1
    assert d['ordinary_length']==d['point_depth']+7*d['cycles']+4
    assert d['total_valuation']==d['point_depth']+11*d['cycles']+6*L+8
    assert all(M.rho(u)<d['rank'] for u in p['coefficients'])==d['descending']
    bound=M.ray_bound(w)
    if d['descending']:
        assert L<=bound['limit'] and d['cycles']<=bound['K'] and d['point_depth']<=bound['J']
        if L:assert d['cycles']>=10*L or d['point_depth']>=8*L
    else:expect_error(lambda:M.compile_plan(p,{}))
    out=dict(seed=w,L=L,cycles=d['cycles'],point_depth=d['point_depth'],remainder=d['remainder'],
             rank=d['rank'],endpoint=d['endpoint'],status=p['status'],word=d['word'],
             bound=bound,coefficients=rows(p['coefficients']),current_hash=digest(rows(p['current'])))
    if store:out['current']=rows(p['current'])
    return out


def finite_absorption(seed):
    x,current=seed,{}
    while x!=1:
        if x in current or len(current)>=10000 or x.bit_length()>4096:
            raise RuntimeError('Designated supplied input unresolved within stated caps')
        current[x]=1;x=M.NORMAL.step(x)
    assert M.divergence(current)==M.atoms((1,seed))
    return current


def supplied_demo(w,L,store=True):
    p=M.pair_plan(w,L)
    assert p['status']=='descending'
    supplied={u:M.combine((1,finite_absorption(3*u)),(-1,finite_absorption(u)))
              for u in p['coefficients']}
    out=M.compile_plan(p,supplied)
    assert M.divergence(out)==M.T.pair_source(w)
    d=dict(seed=w,L=L,supplied_pairs=len(supplied),current_rows=len(out),current_hash=digest(rows(out)))
    if store:d.update(plan_current=rows(p['current']),coefficients=rows(p['coefficients']),
                      supplied={str(u):rows(c) for u,c in sorted(supplied.items())},current=rows(out))
    expect_error(lambda:M.compile_plan(p,{}))
    bad=dict(supplied);bad[next(iter(bad))]={}
    expect_error(lambda:M.compile_plan(p,bad))
    return d


def audit():
    iso=isometry_checks();affine=affine_checks();full=[]
    for n in range(4):
        for L in range(10):full.append(full_plan(6901+10368*n,L,store=(n==0 and L==0)))
    # Every positive-cycle remainder, carried to higher ray indices.
    for remainder in range(7):
        old=M.OLD.parameters(M.OLD.parameter_family(1,0,remainder=remainder)['seed'])
        full.append(full_plan(lifted_fixture(old,3),3))
        j=0 if remainder==0 else 1
        old=M.PREVIOUS.parameters(M.PREVIOUS.parameter_family(1,j,remainder=remainder)['seed'])
        full.append(full_plan(lifted_fixture(old,4),4))
    for L,k,j in ((0,1,3),(1,0,14),(3,1,34),(4,0,45),(6,1,65),(7,1,77)):
        for unit in (1,2):
            f=M.phase_family(L,k,j,unit)
            full.append(full_plan(f['seed'],L))
    cases=[]
    for n in range(1024):
        w=6901+10368*n
        d=M.decide(w)
        limit=d['bound']['limit']
        # A bounded independent check beyond the proved bound; the proof, not
        # these extra checks, supplies all larger L.
        for L in range(max(0,limit+1),max(0,limit+1)+5):assert not M.parameters(w,L)['descending']
        cases.append(dict(seed=w,status=d['status'],limit=limit,
                          first_ray=d['tested'][-1]['L'] if d['status']=='descending' else None))
    witness=M.decide(6901)
    assert witness['status']=='exhausted' and witness['bound']['limit']==0
    assert witness['bound']==dict(seed=6901,rank=10351,J=12,P=1342874,K=1,B=1434024,ratio=43,limit=0)
    assert M.decide(6901,max_rays=0)['status']=='capped'
    assert M.decide(6901,max_rays=1)['status']=='exhausted'
    demos=[supplied_demo(36641534965,1),supplied_demo(M.phase_family(3,1,34)['seed'],3)]
    invalid=[lambda:M.parameters(3445,0),lambda:M.parameters(1,0),lambda:M.parameters(6901,-1),
             lambda:M.ray(0,1),lambda:M.ray(1,-1),lambda:M.ray_bound(1),
             lambda:M.decide(6901,-1),lambda:M.ray_congruence(1,0,-1),
             lambda:M.density_bound(0),lambda:M.phase_family(2,1,4),
             lambda:M.phase_family(0,0,4),lambda:M.phase_family(1,1,1)]
    for f in invalid:expect_error(f)
    paths=[HERE/'all_rays.py',HERE/'check_all_rays.py']
    paths += [HERE.parent/p for p in ('refined_obstruction/refined_obstruction.py',
        'cycle_inverse/cycle_inverse.py','selected_inverse/selected_inverse.py',
        'critical_rank/rank_closure.py','w9_closure/w9_closure.py')]
    result=dict(status='PASS',isometry=iso,affine=affine,full_plans=full,
                categories=dict(Counter(x['status'] for x in full)),
                finite_decisions=dict(count=len(cases),counts=dict(Counter(x['status'] for x in cases)),
                                      hash=digest(cases),accepted=[x for x in cases if x['status']=='descending']),
                all_ray_failure=witness,caps=dict(max_rays_zero='capped',fixture_arrow_limit=10000,fixture_bit_limit=4096),
                supplied_demos=demos,rejections=len(invalid)+2*len(demos),
                sources={str(p.relative_to(HERE.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
    return json.loads(json.dumps(result))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true')
    args=parser.parse_args();result=audit();path=HERE/'all_rays_audit.json'
    if args.write:path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else:assert json.loads(path.read_text())==result
    print('PASS: exhaustive named all-ray continuation; '
          f"{result['isometry']['pair_cases']} isometry cases; {result['affine']['cases']} affine cases; "
          f"{len(result['full_plans'])} full plans; {result['finite_decisions']['count']} complete decisions; "
          f"{len(result['supplied_demos'])} supplied conversions")
