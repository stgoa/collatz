"""Bounded seventeen-family priority and exact-supply audit."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import resolved_rules as M

HERE=Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def absorb(seed):
    x,current=seed,{}
    for _ in range(10001):
        if x==1:
            assert M.RANK.divergence(current)==M.RANK.atoms((1,seed))
            return current
        if x in current or len(current)==10000 or x.bit_length()>512:
            raise RuntimeError('Finite supplied fixture reached its cap')
        current[x]=1;x=M.RANK.NORMAL.step(x)
    raise AssertionError('Unreachable')


def audit():
    categories,plans,old_rows=Counter(),[],[]
    for w in range(5,8192,8):
        old,plan=M.OLD.one_step(w),M.one_step(w)
        if old is not None:
            assert plan==old
            old_rows.append([w,old['rule'],digest(old['current']),sorted(old['coefficients'].items())])
        if plan is None:
            categories['unresolved']+=1
            continue
        M.RANK.validate_step(w,plan)
        categories[plan['rule']]+=1
        plans.append([w,plan['rule'],digest(plan['current']),sorted(plan['coefficients'].items())])
        if old is None:
            for module,name in M.ADDED:
                candidate=module.one_step(w)
                if candidate is not None:
                    assert plan['rule']==name
                    assert plan['current']==candidate['current']
                    assert plan['coefficients']==candidate['coefficients']
                    break
            else:raise AssertionError('No dispatch rule found')
    old_receipt=json.loads((HERE.parent/'refined_rules/refined_rules_audit.json').read_text())
    assert len(old_rows)==747 and digest(old_rows)==old_receipt['plan_hash']

    family=M.LIFTED.parameter_family(0,14,remainder=1)
    assert family['seed']==36641534965
    witnesses=[]
    for w,name in ((53173,'R62_defect_resolution'),(family['seed'],'R64_lifted_inverse')):
        assert M.OLD.one_step(w) is None
        plan=M.one_step(w)
        assert plan['rule']==name
        M.RANK.validate_step(w,plan)
        witnesses.append(dict(seed=w,rule=name,current_hash=digest(plan['current']),
                              coefficients=sorted(plan['coefficients'].items())))
    assert {x['rule'] for x in witnesses}=={name for _,name in M.ADDED}
    # Both new formulas may also recognize inputs with higher-priority rules.
    overlap=20405
    assert M.DEFECT.one_step(overlap) is not None
    assert M.one_step(overlap)==M.OLD.one_step(overlap)
    assert M.one_step(overlap)['rule']=='R45_nonselected_base'

    examples,tables,supply_cache=[],[],{}
    for w in (221,53173,85941,15224757,11432437,family['seed']):
        direct=M.one_step(w)
        assert direct is not None
        plan=M.close(w,max_nodes=10000)
        supplied={}
        for u in plan['coefficients']:
            if u not in supply_cache:
                supply_cache[u]=M.RANK.combine((1,absorb(3*u)),(-1,absorb(u)))
            supplied[u]=supply_cache[u]
        current=M.compile_plan(plan,supplied)
        assert M.RANK.divergence(current)==M.RANK.T.pair_source(w)
        examples.append(dict(seed=w,direct_rule=direct['rule'],expanded=plan['expanded'],
                             coefficients=plan['coefficients'],rows=len(current),
                             current_hash=digest(current),supplied_hash=digest(supplied)))
        if w in (15224757,family['seed']):
            tables.append(dict(plan=plan,supplied=supplied,current=current))

    assert M.DEFECT.FIXED.__file__.endswith('/refined_rules/refined_rules.py')
    assert M.OLD.DEFERRED.OLD.__file__.endswith('/selected_rules/selected_rules.py')
    first_unresolved=next(w for w in range(5,8192,8) if M.one_step(w) is None)
    unfinished=M.close(first_unresolved,max_nodes=10000)
    assert unfinished['current']=={} and unfinished['coefficients']=={first_unresolved:1}
    rejections=0
    for action in (lambda:M.one_step(1),lambda:M.one_step(-3),
                   lambda:M.close(53173,max_nodes=0),
                   lambda:M.compile_plan(unfinished,{}),
                   lambda:M.compile_plan(unfinished,{first_unresolved:{}})):
        try:action()
        except (ValueError,RuntimeError):rejections+=1
        else:raise AssertionError('Invalid or incomplete request accepted')

    return dict(status='PASS',scope='Seventeen conditional rho families, old-fifteen priority and frozen inner resolvers; universal supply open',
                candidates=1024,old_accepted=len(old_rows),accepted=len(plans),
                newly_accepted=len(plans)-len(old_rows),categories=dict(sorted(categories.items())),
                old_plan_hash=digest(old_rows),plan_hash=digest(plans),
                added_rule_witnesses=witnesses,lifted_family=family,
                old_priority_overlap=overlap,actual_substitutions=examples,stored_tables=tables,
                distinct_supplied_pairs=len(supply_cache),supplied_hash=digest(supply_cache),
                explicit_unresolved_example=unfinished,rejection_checks=rejections,
                caps=dict(candidate_upper_bound=8192,closure_nodes=10000,input_steps=10000,input_bits=512),
                fixed_resolvers={'R62':str(Path(M.DEFECT.FIXED.__file__).relative_to(HERE.parent)),
                                 'R59':str(Path(M.OLD.DEFERRED.OLD.__file__).relative_to(HERE.parent))},
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('resolved_rules.py','check_resolved_rules.py')})


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args();result=json.loads(json.dumps(audit(),sort_keys=True))
    path=HERE/'resolved_rules_audit.json'
    if args.write_receipt:path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:assert json.loads(path.read_text())==result,'Receipt differs; inspect before regenerating'
    print('PASS: seventeen-family rho union, old-fifteen priority and exact supplied-current conversions')


if __name__=='__main__':main()
