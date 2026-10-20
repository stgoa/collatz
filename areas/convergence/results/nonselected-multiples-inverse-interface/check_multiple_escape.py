"""Bounded exact audit of the whole two-block interface and supplied inputs."""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import multiple_escape as M

HERE = Path(__file__).resolve().parent


def digest(rows):
    return hashlib.sha256(json.dumps(sorted(rows.items()),separators=(',',':')).encode()).hexdigest()


def clocks(data):
    w,k,D,j,p = (data[a] for a in ('w','k','D','j','p'))
    x=p
    for a in [1]*j+[2]*D:
        assert M.NORMAL.valuation2(3*x+1)==a
        x=M.NORMAL.step(x)
    assert x==data['b']
    a=M.NORMAL.valuation2(3*w+1)
    left,right=(D+j+2,1) if k==8 else (D+j+a+2,a+1)
    assert M.NINE.prefix(p,left)[0]==M.NINE.prefix(3*w,right)[0]
    return [left,right]


def capped_absorption(seed,cap=10000):
    seen,rows,x=set(),Counter(),seed
    for _ in range(cap):
        if x==1:
            result=M.NINE.clean(rows)
            assert M.divergence(result)==M.atoms((1,seed))
            return result
        if x in seen:
            raise RuntimeError('Nonabsorbing cycle in fixture search')
        seen.add(x)
        rows[x]+=1
        x=M.NORMAL.step(x)
    raise RuntimeError('Fixture cap reached; no certificate')


def supplied_pair(w):
    return M.combine((1,capped_absorption(3*w)),(-1,capped_absorption(w)))


def expect_error(kind,action):
    try:
        action()
    except kind:
        return
    raise AssertionError('Expected explicit rejection')


def check_case(w,k):
    data=M.parameters(w,k)
    plan=M.pair_plan(w,k)
    ordinary=clocks(data)
    if data['j']==0:
        assert plan['current']=={} and plan['coefficients']=={w:1}
        kind='exact_zero_self_return'
    elif data['child_domain']=='W9':
        defect=M.return_defect(w,k)
        C=data['C']
        assert (C<3*w)==(k==4 and data['D'] in (1,2))
        end,prefix=M.NINE.prefix(defect['successor'],data['D'])
        assert end==(2*w+1 if k==4 else M.NORMAL.F(w))
        low=M.RANK.absorption_plan(defect['successor'])
        low_end=M.RANK.absorption_plan(end)
        assert low['current']==M.combine((1,prefix),(1,low_end['current']))
        assert low['coefficients']==low_end['coefficients']
        assert all(M.RANK.rho(a)<3*w for a in low['coefficients'])
        kind='W9_forward_defect'
    elif data['descending']:
        M.RANK.validate_step(w,plan)
        assert M.decreasing_plan(w)==plan
        kind='strict_rank_decrease'
    else:
        kind='uncancelled_largest_W5'
    assert (plan['status']=='descending')==data['descending']
    return data,plan,kind,ordinary


def audit():
    eligible=0
    kinds=Counter()
    accepted=[]
    for w in range(5,32768,8):
        if not M.eligible(w):
            continue
        eligible+=1
        active=0
        for k in (4,8):
            data,plan,kind,ordinary=check_case(w,k)
            kinds[kind]+=1
            active+=data['j']>0
            if data['descending']:
                accepted.append(dict(w=w,k=k,D=data['D'],j=data['j'],p=data['p'],
                                     child=data['child'],clocks=ordinary,
                                     coefficients=plan['coefficients']))
                assert not M.PHASE.decreasing_domain(w)
                assert not M.OLD.eligible(w)
                assert not M.SPINE.recognized(w)
        assert active==1
    synthetic=[]
    for D in range(1,13):
        for k in (4,8):
            threshold=next(j for j in range(1,2*D+7)
                           if k*2**(2*D+j+1)<3**(D+j+1))
            for j in sorted({1,2,threshold-1,threshold,2*D+6}):
                for terminal in (1,2):
                    data=M.parameter_witness(D,j,k,terminal)
                    checked,plan,kind,ordinary=check_case(data['w'],k)
                    assert checked['D']==D and checked['j']==j
                    synthetic.append(dict(D=D,k=k,j=j,terminal=terminal,w=data['w'],
                                          period=data['w_period'],kind=kind,clocks=ordinary,
                                          sha256=digest(plan['current'])))
            far=M.parameter_witness(D,2*D+6,k,2,7)
            assert far['descending']
            check_case(far['w'],k)
    fixture={}
    conversions=[]
    for w in (2445,16653,17325,17997):
        plan=M.decreasing_plan(w)
        supplied={u:supplied_pair(u) for u in plan['coefficients']}
        current=M.compile_plan(plan,supplied)
        assert M.divergence(current)==M.T.pair_source(w)
        conversions.append(dict(w=w,inputs=len(supplied),rows=len(current),sha256=digest(current)))
        if w==16653:
            assert plan['parameters']['child']>w
            assert plan['coefficients']=={93:-1,325:1,31189:1}
            fixture=dict(seed=w,local_current=plan['current'],coefficients=plan['coefficients'],
                         inputs=supplied,current=current)
    closures=[]
    for w in (2445,16653,17325,17997):
        closed=M.RANK.close_plan(w,M.decreasing_plan,max_nodes=1000)
        assert all(M.decreasing_plan(v) is None for v in closed['coefficients'])
        closures.append(dict(w=w,expanded=closed['expanded'],leaves=closed['coefficients']))
    assert M.decreasing_plan(101) is None and M.decreasing_plan(45) is None
    expect_error(ValueError,lambda:M.parameters(101,4))
    expect_error(ValueError,lambda:M.parameters(2445,16))
    expect_error(ValueError,lambda:M.return_defect(2445,4))
    expect_error(ValueError,lambda:M.compile_plan(M.pair_plan(45,4),{}))
    expect_error(ValueError,lambda:M.compile_plan(M.decreasing_plan(2445),{}))
    return dict(status='PASS',scope='Complete prescribed two-block interface; universal remaining inputs open',
                W5_candidates=4096,eligible_inputs=eligible,complete_plans=2*eligible,
                cases=dict(kinds),decreasing_examples=accepted,synthetic_cases=synthetic,
                far_CRT_checks=24,actual_substitutions=conversions,
                fixture_absorption_cap=10000,formal_closures=closures,rejection_checks=5),fixture


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    result,fixture=audit()
    receipt=HERE/'nonselected_multiples_audit.json'
    inputs=HERE/'w16653_inputs.json'
    table=HERE/'w16653_current.csv'
    metadata={k:v for k,v in fixture.items() if k!='current'}
    if args.write_receipt:
        receipt.write_text(json.dumps(result,indent=2)+'\n')
        inputs.write_text(json.dumps(metadata,indent=2)+'\n')
        with table.open('w',newline='') as stream:
            writer=csv.writer(stream,lineterminator='\n')
            writer.writerow(('state','current'))
            writer.writerows(sorted(fixture['current'].items()))
    else:
        assert json.loads(receipt.read_text())==json.loads(json.dumps(result))
        saved=json.loads(inputs.read_text())
        assert saved==json.loads(json.dumps(metadata))
        supplied={int(u):{int(x):c for x,c in rows.items()} for u,rows in saved['inputs'].items()}
        plan=dict(seed=saved['seed'],current={int(x):c for x,c in saved['local_current'].items()},
                  coefficients={int(x):c for x,c in saved['coefficients'].items()})
        replay=M.compile_plan(plan,supplied)
        with table.open() as stream:
            stored={int(row['state']):int(row['current']) for row in csv.DictReader(stream)}
        assert replay==stored==fixture['current']
    print(f'PASS: {result["eligible_inputs"]} inputs; {result["complete_plans"]} complete plans; '
          f'{len(result["synthetic_cases"])} exact CRT cases; four supplied substitutions')


if __name__=='__main__':
    main()
