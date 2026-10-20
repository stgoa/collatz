"""Bounded replay of exact two-phase words, thresholds and signed currents."""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import double_inverse as M

HERE = Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def direct_word(data):
    x=data['endpoint']
    for a in [1]*(data['L']-1)+[2]+[1]*data['h']:
        assert M.NORMAL.valuation2(3*x+1)==a
        x=M.NORMAL.step(x)
    assert x==2*data['k']*data['seed']+1
    assert M.NORMAL.quotient_step(x)==3*data['seed']
    x=data['endpoint']
    for _ in range(data['h']+data['L']+1):
        x=M.NORMAL.quotient_step(x)
    assert x==3*data['seed']


def absorption(seed):
    x,rows=seed,{}
    for _ in range(10001):
        if x==1:
            assert M.divergence(rows)==M.atoms((1,seed))
            return rows
        if x in rows or len(rows)==10000 or x.bit_length()>512:
            raise RuntimeError('Bounded demonstration input unresolved')
        rows[x]=1
        x=M.NORMAL.step(x)
    raise AssertionError('Unreachable')


def expect_error(action):
    try:action()
    except ValueError:return
    raise AssertionError('Expected rejection')


def audit():
    cases,rows=Counter(),[]
    for w in range(5,65536,8):
        try:data=M.parameters(w)
        except ValueError:continue
        direct_word(data)
        accepted=data['endpoint']<3*w
        assert M.recognized(w)==accepted
        label=f'k{data["k"]},accepted{accepted},intermediate_grows{data["intermediate_grows"]}'
        cases[label]+=1
        if accepted:
            plan=M.pair_plan(w)
            M.RANK.validate_step(w,plan)
            rows.append([w,sorted(plan['coefficients'].items()),digest(plan['current'])])
        else:
            expect_error(lambda:M.pair_plan(w))
    families=[]
    phases=[(k,h,L) for k in(4,8) for h in range(1,9) for L in range(3,11)]
    phases += [(k,h,L) for k in(4,8) for h,L in((1,32),(2,64),(64,3),(128,128))]
    for k,h,L in phases:
        for index in(0,1,7):
            witness=M.parameter_family(k,h,L,index)
            data=M.parameters(witness['seed'])
            direct_word(data)
            if data['rank_shrinking']:
                M.RANK.validate_step(data['seed'],M.pair_plan(data['seed']))
            families.append([k,h,L,index,data['seed'],data['endpoint'],data['rank_shrinking']])
    examples=[];fixture={}
    for w in(37,53,877,1325):
        plan=M.pair_plan(w)
        supplied={u:M.combine((1,absorption(3*u)),(-1,absorption(u))) for u in plan['coefficients']}
        current=M.compile_plan(plan,supplied)
        assert M.divergence(current)==M.T.pair_source(w)
        examples.append(dict(w=w,parameters=plan['parameters'],inputs=len(supplied),rows=len(current),sha256=digest(current)))
        if w==53:fixture=dict(seed=w,plan=plan,inputs=supplied,current=current)
    expect_error(lambda:M.pair_plan(13))
    expect_error(lambda:M.pair_plan(45))
    expect_error(lambda:M.compile_plan(M.pair_plan(53),{}))
    bad={u:{} for u in M.pair_plan(53)['coefficients']}
    expect_error(lambda:M.compile_plan(M.pair_plan(53),bad))
    return dict(status='PASS',scope='Exact two-phase rules on the specified L>=3 domain; universal completion open',
                W5_candidates=8192,parameter_classes=dict(sorted(cases.items())),
                accepted_plans=len(rows),accepted_hash=digest(rows),families=families,
                actual_substitutions=examples,rejection_checks=4,
                caps=dict(pair_upper_bound=65536,input_steps=10000,input_bits=512)),fixture


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args();result,fixture=audit();path=HERE/'double_inverse_audit.json'
    if args.write_receipt:
        path.write_text(json.dumps(result,indent=2)+'\n')
        (HERE/'w53_inputs.json').write_text(json.dumps(fixture,indent=2)+'\n')
        with (HERE/'w53_current.csv').open('w',newline='') as target:
            writer=csv.writer(target,lineterminator='\n');writer.writerow(('state','current'))
            writer.writerows(sorted(fixture['current'].items()))
    else:
        assert json.loads(path.read_text())==json.loads(json.dumps(result))
        assert json.loads((HERE/'w53_inputs.json').read_text())==json.loads(json.dumps(fixture))
        with (HERE/'w53_current.csv').open() as source:
            stored={int(row['state']):int(row['current']) for row in csv.DictReader(source)}
        assert stored==fixture['current']
    print(f'PASS: {sum(result["parameter_classes"].values())} two-phase inputs; '
          f'{result["accepted_plans"]} strict plans; {len(result["families"])} exact families; four substitutions')


if __name__=='__main__':main()
