"""Bounded exact replay for R61/refined15 and the lifted rotated-cycle rule."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import refined_obstruction as M

HERE=Path(__file__).resolve().parent


def digest(data):
    return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def rows(data):
    return [[x,c] for x,c in sorted(data.items())]


def expect_error(action):
    try:action()
    except ValueError:return
    raise AssertionError('Expected rejection')


def affine_checks():
    cases=[]
    for k in range(97):
        a=Fraction(2048,2187)**k
        for j in range(17):
            t=Fraction(2,3)**j
            for q in (5167,1000000001):
                lam=Fraction(16384,81)*a*t
                beta=-t*(Fraction(598,81)*a+24)-1
                eta=lam*q+beta
                D=3**(7*k+j)
                rhs=(16384*2**(11*k+j)-81*D)*q-598*2**(11*k+j)-1944*2**j*3**(7*k)-81*D
                assert 81*D*(eta-q)==rhs
                assert (eta<q)==(j>=M.point_threshold(k))
                cases.append([k,j,q,rhs])
    failures=[(0,13)]+[(end,j-1) for end,j in M.THRESHOLDS]
    starts=[0,1]+[end+1 for end,_ in M.THRESHOLDS]
    for k,j in failures:
        a,t=Fraction(2048,2187)**k,Fraction(2,3)**j
        assert (Fraction(16384,81)*a*t-1)*5167-t*(Fraction(598,81)*a+24)-1>0
    for k in starts:
        j=M.point_threshold(k)
        assert 16384*2**(11*k+j)<81*3**(7*k+j)
    return dict(cases=len(cases),hash=digest(cases),last_failures=[list(x) for x in failures],
                first_passes=[[k,M.point_threshold(k)] for k in starts])


def check_plan(family):
    w=family['seed'];plan=M.pair_plan(w);d=plan['parameters']
    path=M.bridge(w)['path']
    assert len(path)-1==d['ordinary_length']
    assert all(M.NORMAL.valuation2(3*x+1)==a for x,a in zip(path,d['word']))
    assert all(M.rho(u)<d['rank'] for u in plan['coefficients'])==d['descending']
    if not d['descending']:expect_error(lambda:M.compile_plan(plan,{}))
    return dict(seed=w,k=d['cycles'],j=d['point_depth'],remainder=d['remainder'],
                status=plan['status'],endpoint=d['endpoint'],leading=plan['leading'],
                current_hash=digest(rows(plan['current'])),coefficients=rows(plan['coefficients']))


def finite_absorption(seed):
    x,current=seed,{}
    while x!=1:
        if x in current or len(current)>=10000 or x.bit_length()>4096:
            raise RuntimeError('Designated supplied input unresolved within caps')
        current[x]=1;x=M.NORMAL.step(x)
    assert M.divergence(current)==M.atoms((1,seed))
    return current


def supplied_demo(w,store=False):
    plan=M.pair_plan(w)
    assert plan['status']=='descending'
    supplied={u:M.combine((1,finite_absorption(3*u)),(-1,finite_absorption(u)))
              for u in plan['coefficients']}
    out=M.compile_plan(plan,supplied)
    assert M.divergence(out)==M.T.pair_source(w)
    result=dict(seed=w,word=plan['parameters']['word'],supplied_pairs=len(supplied),
                current_rows=len(out),current_hash=digest(rows(out)))
    if store:
        result.update(plan_current=rows(plan['current']),coefficients=rows(plan['coefficients']),
                      supplied={str(u):rows(c) for u,c in sorted(supplied.items())},current=rows(out))
    expect_error(lambda:M.compile_plan(plan,{}))
    bad=dict(supplied);bad[next(iter(bad))]={}
    expect_error(lambda:M.compile_plan(plan,bad))
    return result


def audit():
    affine=affine_checks()
    full=[]
    for h in range(1,7):
        for unit in ((1,) if h==1 else (1,2)):
            full.append(check_plan(M.parameter_family(0,1,remainder=h,unit=unit)))
    for j in (2,13,14,32):
        for unit in (1,2):full.append(check_plan(M.parameter_family(0,j,remainder=1,unit=unit)))
    for k in (1,6,7,74,75,80,81):
        full.append(check_plan(M.parameter_family(k,0)))
        for j in sorted({max(1,M.point_threshold(k)-1),max(1,M.point_threshold(k))}):
            full.append(check_plan(M.parameter_family(k,j,remainder=1)))
    for d in range(2,7):
        full.append(check_plan(M.parameter_family(1,1,remainder=d)))
    full.append(check_plan(M.parameter_family(1,13,remainder=1,unit=2)))

    old_phase=[]
    for k,j,d in ((0,0,1),(0,0,6),(1,0,0),(1,2,0),(1,3,0),(1,0,6),
                  (6,2,0),(12,1,0),(18,0,0)):
        data=M.old_cycle_family(16,5,0,k,j,remainder=d)
        old_phase.append(dict(k=k,j=j,remainder=d,seed=data['seed'],
                              accepted=data['cycle_parameters']['descending']))
    crt=[]
    for r,A,K in ((16,5,0),(17,6,1),(32,8,8),(64,32,64)):
        for c in (0,1):
            for unit in (1,2):
                data=M.lifted_family(r,A,K,cycles=c,unit=unit)
                inv=M.bridge(data['seed'])
                assert inv['parameters']['endpoint']<data['rank']
                crt.append(dict(r=r,A=A,K=K,cycles=c,unit=unit,seed=data['seed'],
                                s_residue=data['s_residue'],s_period=data['s_period'],
                                ordinary_length=inv['parameters']['ordinary_length']))
    classifications=[]
    inputs=[M.old_cycle_family(16,5,0,1,3),M.old_cycle_family(16,5,0,0,0,remainder=1),
            M.lifted_family(16,5,0),M.lifted_family(17,6,1,cycles=1)]
    for data in inputs:
        result=M.classify_fifteen(data,check_dispatcher=True)
        assert result['accepted']==result['old_cycle_parameters']['descending']
        classifications.append(dict(seed=data['seed'],leading=data['leading'],accepted=result['accepted'],
                                    deferred=[dict(recipe=x['recipe'],leading=x['leading'],
                                                   current_hash=digest(rows(x['current'])),
                                                   coefficients=rows(x['coefficients']),
                                                   expanded=len(x['history'])) for x in result['deferred']]))
    undos=[]
    for i,data in enumerate((inputs[2],inputs[3])):
        result=M.leading_inverse(data)
        item=dict(seed=data['seed'],leading=data['leading'],rank=data['rank'],
                  leading_rank=data['endpoint'],quotient_length=result['quotient_length'],
                  clocks=result['ordinary_common_tail_clocks'],
                  current_hash=digest(rows(result['current'])),coefficients=rows(result['coefficients']),
                  composed_current=[],composed_coefficients=[[data['seed'],1]])
        if i==0:
            item.update(current=rows(result['current']),inverse_word=result['inverse_word'],
                        inverse_states=result['inverse_states'],
                        original_exit_current=rows(M.ELEVEN.EXIT.exit_plan(data['seed'])['current']))
        undos.append(item)
    fixture=M.parameter_family(0,14,remainder=1)['seed']
    assert fixture==36641534965 and M.FIFTEEN.one_step(fixture) is None
    demos=[supplied_demo(fixture,True),
           supplied_demo(M.parameter_family(1,13,remainder=1)['seed'],True),
           supplied_demo(inputs[2]['seed'],False)]
    invalid=[lambda:M.parameters(1),lambda:M.point_threshold(-1),
             lambda:M.parameter_family(0,0,remainder=1),
             lambda:M.parameter_family(1,0,remainder=1),
             lambda:M.parameter_family(1,2,remainder=2),
             lambda:M.old_cycle_family(16,5,0,1,1,remainder=1),
             lambda:M.lifted_family(15,5,0),
             lambda:M.lifted_family(16,5,0,cycles=2),
             lambda:M.eleven_from_s(16,5,0,1)]
    for action in invalid:expect_error(action)
    source_paths=[HERE/'refined_obstruction.py',HERE/'check_refined_obstruction.py']
    source_paths += [HERE.parent/p for p in ('exit_continuation/exit_continuation.py',
        'refined_rules/refined_rules.py','deferred_rank/deferred_rank.py',
        'cycle_inverse/cycle_inverse.py','selected_inverse/selected_inverse.py')]
    result=dict(status='PASS',affine=affine,full_plans=full,
                categories=dict(Counter(x['status'] for x in full)),old_cycle_rows=old_phase,
                new_crt_rows=crt,dispatcher_classifications=classifications,leading_undos=undos,
                supplied_demos=demos,rejections=len(invalid)+2*len(demos),
                sources={str(p.relative_to(HERE.parent)):hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in source_paths})
    return json.loads(json.dumps(result))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true')
    args=parser.parse_args();result=audit();path=HERE/'refined_obstruction_audit.json'
    if args.write:path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else:assert json.loads(path.read_text())==result
    print('PASS: refined fifteen obstruction and lifted cycle; '
          f"{result['affine']['cases']} affine cases; {len(result['full_plans'])} full plans; "
          f"{len(result['new_crt_rows'])} new CRT rows; {len(result['supplied_demos'])} supplied conversions")
