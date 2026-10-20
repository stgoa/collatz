"""Finite signed composition with the original rho rank on every edge."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import continued_rules as M

HERE=Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def absorb(seed):
    x,rows=seed,{}
    for _ in range(10001):
        if x==1:return rows
        if x in rows or len(rows)==10000 or x.bit_length()>512:
            raise RuntimeError('Finite demonstration input reached its cap')
        rows[x]=1;x=M.RANK.NORMAL.step(x)
    raise AssertionError('Unreachable')


def audit():
    counts=Counter();plans=[];old_count=0
    for w in range(5,8192,8):
        old=M.OLD.one_step(w);p=M.one_step(w)
        old_count+=old is not None
        if old is not None:assert p==old
        if p is None:counts['unresolved']+=1
        else:
            M.RANK.validate_step(w,p);counts[p['rule']]+=1
            plans.append([w,p['rule'],digest(p['current']),sorted(p['coefficients'].items())])
    examples=[];tables=[]
    for w in (141,365,1533,3837,5565,4258701):
        plan=M.close(w,max_nodes=10000)
        supplied={u:M.RANK.combine((1,absorb(3*u)),(-1,absorb(u))) for u in plan['coefficients']}
        current=M.RANK.compile_plan(plan,supplied)
        assert M.RANK.divergence(current)==M.RANK.T.pair_source(w)
        examples.append(dict(seed=w,expanded=plan['expanded'],coefficients=plan['coefficients'],
                             rows=len(current),current_hash=digest(current)))
        if w in (1533,4258701):tables.append(dict(plan=plan,supplied=supplied,current=current))
    for i in range(64):assert M.one_step(3445+3456*i) is None
    return dict(status='PASS',scope='Nine rho rule families; sigma rules are separate and universal coverage remains open',
                candidates=1024,old_accepted=old_count,accepted=len(plans),categories=dict(sorted(counts.items())),
                plan_hash=digest(plans),actual_substitutions=examples,tables=tables,
                untouched_phase_examples=64,caps=dict(candidate_upper_bound=8192,closure_nodes=10000,
                                                     input_steps=10000,input_bits=512))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args();result=json.loads(json.dumps(audit()))
    path=HERE/'continued_rules_audit.json'
    if args.write_receipt:path.write_text(json.dumps(result,indent=2)+'\n')
    else:assert json.loads(path.read_text())==result
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
