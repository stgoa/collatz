"""Finite signed composition of all seven strict-rank rule domains."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import expanded_union as U
from check_double_inverse import absorption

HERE=Path(__file__).resolve().parent
M=U.RANK


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def audit():
    counts=Counter();mixed=closed=old=0;plans=[]
    for w in range(5,8192,8):
        before=U.OLD.one_step(w)
        data=U.one_step(w)
        if before is not None:
            old+=1
            assert data['rule']==before['rule'] and data['coefficients']==before['coefficients']
        if data is None:
            counts['unresolved']+=1
            continue
        counts[data['rule']]+=1
        plan=U.close(w,max_nodes=10000)
        assert all(U.one_step(v) is None for v in plan['coefficients'])
        rules=sorted({U.one_step(v)['rule'] for v in plan['expanded']})
        mixed+=len(rules)>1
        closed+=not plan['coefficients']
        plans.append([w,rules,plan['expanded'],sorted(plan['coefficients'].items()),digest(plan['current'])])
    examples=[];tables=[];all_inputs={}
    for w in(37,45,53,101,741,957,1821,16653):
        plan=U.close(w,max_nodes=10000)
        supplied={}
        for v in plan['coefficients']:
            if v not in all_inputs:
                all_inputs[v]=M.combine((1,absorption(3*v)),(-1,absorption(v)))
            supplied[v]=all_inputs[v]
        current=M.compile_plan(plan,supplied)
        assert M.divergence(current)==M.T.pair_source(w)
        if w==1821:assert not supplied
        examples.append(dict(seed=w,expanded=plan['expanded'],coefficients=plan['coefficients'],
                             current_rows=len(current),sha256=digest(current)))
        if w in(957,1821,16653):tables.append(dict(seed=w,plan=plan,inputs=supplied,current=current))
    assert U.one_step(21) is None and U.close(21)['coefficients']=={21:1}
    return dict(status='PASS',scope='Finite seven-rule composition; unresolved domain not supplied',
                candidates=1024,old_accepted=old,categories=dict(sorted(counts.items())),
                accepted_plans=len(plans),mixed_closures=mixed,closed_without_inputs=closed,
                plan_hash=digest(plans),actual_substitutions=examples,
                distinct_supplied_inputs=len(all_inputs),tables=tables,
                caps=dict(union_upper_bound=8192,closure_nodes=10000,input_steps=10000,input_bits=512))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args();result=audit();path=HERE/'expanded_union_audit.json'
    if args.write_receipt:path.write_text(json.dumps(result,indent=2)+'\n')
    else:assert json.loads(path.read_text())==json.loads(json.dumps(result))
    print(f'PASS: {result["candidates"]} candidates; {result["accepted_plans"]} strict rules; '
          f'{result["mixed_closures"]} mixed closures; eight actual substitutions')


if __name__=='__main__':main()
