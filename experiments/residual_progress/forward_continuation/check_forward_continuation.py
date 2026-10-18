"""Exact algebra, block clocks, strict signed plans and finite input fixtures."""
import argparse
from collections import Counter
from fractions import Fraction as F
import csv
import hashlib
import json
from pathlib import Path
import sys
import forward_continuation as M

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'double_inverse'))
import expanded_union as SEVEN


def digest(rows):
    return hashlib.sha256(json.dumps(sorted(rows.items()),separators=(',',':')).encode()).hexdigest()


def algebra_table():
    rows=[(3,2,0),(3,4,0),(4,2,0),(4,2,1),(4,4,0),(4,4,1),(4,6,0),(4,8,0)]
    result=[]
    for a,d,p in rows:
        A=3**(a-1+d//2);C=2**(a+d-1);B=A-2**a*3**(d//2)+C
        if p:B-=C;C*=2
        alpha,beta=F(A,C),F(B,C)
        qmin=39 if a==3 else 111
        odd_slope=1-F(81,256)*alpha
        odd_value=qmin*odd_slope-F(81*beta+133,256)
        assert odd_slope>0 and odd_value>0
        decisions=[]
        for e in(2,4,6,8,10):
            fa=F(3**(e//2+1),2**(e+1))*alpha
            fb=F(3**(e//2+1),2**(e+1))*beta+1-F(3**(e//2),2**(e+1))
            forms={'raw':(fa,fb),'selected1':(27*fa/64,(27*(fb-1)+58)/64),
                   'selected3':(9*fa/16,(9*(fb-1)+10)/16),'selected7':(fa/2,(fb-1)/2)}
            accepted=[]
            for kind,(ma,mb) in forms.items():
                slope,value=1-ma,qmin*(1-ma)-mb
                assert slope*value>0
                if value>0:accepted.append(kind)
            decisions.append([e,accepted])
        result.append(dict(row=[a,d,p],affine=[A,B,C],even_decisions=decisions))
    return result


def clocks(w,plan):
    data=plan['parameters']
    x=3*w
    for _ in range(data['quotient_length']):x=M.NORMAL.quotient_step(x)
    assert x==plan['minimum']
    if 'ordinary_clocks' in data:
        left,right=data['ordinary_clocks']
        assert M.NINE.prefix(3*w,left)[0]==M.NINE.prefix(plan['raw_endpoint'],right)[0]


def absorption(seed):
    x,rows=seed,{}
    for _ in range(10001):
        if x==1:
            assert M.divergence(rows)==M.atoms((1,seed))
            return rows
        if x in rows or len(rows)==10000 or x.bit_length()>512:
            raise RuntimeError('Finite fixture unresolved within caps')
        rows[x]=1;x=M.NORMAL.step(x)
    raise AssertionError('Unreachable')


def expect_error(action):
    try:action()
    except ValueError:return
    raise AssertionError('Expected rejection')


def audit():
    algebra=algebra_table()
    rows=Counter();decisions=[]
    for w in range(5,65536,8):
        try:table=M.low_first_table(w)
        except ValueError:continue
        plan=M.two_plan(w)
        assert (plan['status']=='descending')==table['accepted']
        clocks(w,plan)
        rows[str(tuple(table['row']))+','+str(table['accepted'])]+=1
        decisions.append([w,table['accepted'],digest(plan['current'])])
    exit_counts=Counter()
    for E in range(5,61):
        for unit in(1,3,5,9):
            x=2**E*unit-5
            data=M.low_run(x)
            assert data['length']==(E-2)//3
            assert data['endpoint']>x
            exit_counts[data['exit_exponent']]+=1
    families=[]
    for r in list(range(1,13))+[32,64]:
        for extra in(0,2):
            d=4*r+3+extra
            for index in(0,3):
                family=M.delayed_family(r,d,index)
                w=family['seed'];plan=M.delayed_plan(w)
                assert plan['status']=='descending'
                M.RANK.validate_step(w,plan);clocks(w,plan)
                assert SEVEN.one_step(w) is None
                assert plan['parameters']['low_endpoint']>3*w
                assert M.OLD.OLD.absorption_rank_bound(plan['parameters']['low_endpoint'])['bound']>3*w
                families.append(dict(r=r,d=d,index=index,w=w,period=family['seed_period'],
                                     original_rank=3*w,intermediate=plan['parameters']['low_endpoint'],
                                     endpoint=plan['raw_endpoint'],clocks=plan['parameters']['ordinary_clocks'],
                                     requests=len(plan['coefficients']),sha256=digest(plan['current'])))
    examples=[];fixture={}
    for w in(141,365,4258701):
        plan=M.delayed_plan(w) if w==4258701 else M.two_plan(w)
        supplied={v:M.combine((1,absorption(3*v)),(-1,absorption(v))) for v in plan['coefficients']}
        current=M.compile_plan(plan,supplied)
        assert M.divergence(current)==M.T.pair_source(w)
        examples.append(dict(seed=w,inputs=len(supplied),rows=len(current),sha256=digest(current)))
        if w==4258701:fixture=dict(seed=w,local_current=plan['current'],coefficients=plan['coefficients'],
                                 status=plan['status'],inputs=supplied,current=current)
    assert M.accepted_plan(4258701) is not None and M.accepted_plan(141) is not None
    assert M.accepted_plan(21) is None
    expect_error(lambda:M.compile_plan(M.two_plan(397),{}))
    expect_error(lambda:M.compile_plan(M.two_plan(365),{}))
    expect_error(lambda:M.low_run(31))
    expect_error(lambda:M.delayed_family(0))
    expect_error(lambda:M.delayed_family(1,2))
    return dict(status='PASS',scope='Partial original-rho continuation; universal macro closure open',
                algebra_table=algebra,W5_candidates=8192,whole_table_cases=len(decisions),
                table_rows=dict(sorted(rows.items())),table_digest=hashlib.sha256(json.dumps(decisions).encode()).hexdigest(),
                low_run_cases=224,exit_counts=dict(exit_counts),exact_families=families,
                actual_substitutions=examples,rejection_checks=5,
                caps=dict(input_steps=10000,input_bits=512)),fixture


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args();result,fixture=audit()
    receipt=HERE/'forward_continuation_audit.json'
    inputs=HERE/'w4258701_inputs.json';table=HERE/'w4258701_current.csv'
    metadata={k:v for k,v in fixture.items() if k!='current'}
    if args.write_receipt:
        receipt.write_text(json.dumps(result,indent=2)+'\n')
        inputs.write_text(json.dumps(metadata,indent=2)+'\n')
        with table.open('w',newline='') as stream:
            writer=csv.writer(stream,lineterminator='\n');writer.writerow(('state','current'))
            writer.writerows(sorted(fixture['current'].items()))
    else:
        assert json.loads(receipt.read_text())==json.loads(json.dumps(result))
        saved=json.loads(inputs.read_text());assert saved==json.loads(json.dumps(metadata))
        plan=dict(seed=saved['seed'],status=saved['status'],current={int(x):c for x,c in saved['local_current'].items()},
                  coefficients={int(v):c for v,c in saved['coefficients'].items()})
        supplied={int(v):{int(x):c for x,c in rows.items()} for v,rows in saved['inputs'].items()}
        replay=M.compile_plan(plan,supplied)
        with table.open() as stream:stored={int(row['state']):int(row['current']) for row in csv.DictReader(stream)}
        assert replay==stored==fixture['current']
    print(f'PASS: {result["whole_table_cases"]} complete table cases; 224 maximal low runs; '
          f'{len(result["exact_families"])} exact growing families; three supplied substitutions')


if __name__=='__main__':main()
