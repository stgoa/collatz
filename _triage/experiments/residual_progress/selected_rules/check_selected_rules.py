"""Bounded audit of twelve-family strict-rho composition and exact supply."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import selected_rules as M

HERE = Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def absorb(seed):
    x, current = seed, {}
    for _ in range(10001):
        if x == 1:
            assert M.RANK.divergence(current) == M.RANK.atoms((1,seed))
            return current
        if x in current or len(current) == 10000 or x.bit_length() > 512:
            raise RuntimeError('Finite demonstration input reached its cap')
        current[x] = 1
        x = M.RANK.NORMAL.step(x)
    raise AssertionError('Unreachable')


def audit():
    counts, plans, old_count, old_plan_rows = Counter(), [], 0, []
    new_inputs = []
    for w in range(5,8192,8):
        old, plan = M.OLD.one_step(w), M.one_step(w)
        if old is not None:
            old_count += 1
            assert plan == old
            old_plan_rows.append([w,old['rule'],digest(old['current']),sorted(old['coefficients'].items())])
        if plan is None:
            counts['unresolved'] += 1
        else:
            M.RANK.validate_step(w,plan)
            counts[plan['rule']] += 1
            plans.append([w,plan['rule'],digest(plan['current']),sorted(plan['coefficients'].items())])
            if old is None:
                new_inputs.append(w)
                # Check the entire dispatch priority, including overlap.
                expected = None
                for module,name in ((M.FORWARD,'R55_selected_forward'),
                                    (M.INVERSE,'R56_selected_inverse'),
                                    (M.EXIT,'R57_selected_cycle_exit')):
                    candidate = module.one_step(w)
                    if candidate is not None:
                        expected = name
                        assert plan['current'] == candidate['current']
                        assert plan['coefficients'] == candidate['coefficients']
                        break
                assert plan['rule'] == expected
    assert old_count == 493
    old_receipt = json.loads((HERE.parent/'continued_rules/continued_rules_audit.json').read_text())
    assert digest(old_plan_rows) == old_receipt['plan_hash']

    # Larger witnesses exercise all three added branches despite priority
    # overlap in the small window and in some published demonstrations.
    branch_witnesses = []
    for w,expected in ((221,'R55_selected_forward'),
                       (382205941,'R56_selected_inverse'),
                       (11324620789,'R57_selected_cycle_exit')):
        plan = M.one_step(w)
        assert plan['rule'] == expected
        M.RANK.validate_step(w,plan)
        branch_witnesses.append(dict(seed=w,rule=expected,current_hash=digest(plan['current']),
                                     coefficients=sorted(plan['coefficients'].items())))
    assert {x['rule'] for x in branch_witnesses} == {
        'R55_selected_forward','R56_selected_inverse','R57_selected_cycle_exit'}

    examples, tables, all_supplied = [], [], {}
    for w in (221,2813,10357,5821,93301,1105909,11324620789):
        direct = M.one_step(w)
        assert direct is not None
        plan = M.close(w,max_nodes=10000)
        supplied = {}
        for u in plan['coefficients']:
            if u not in all_supplied:
                all_supplied[u] = M.RANK.combine((1,absorb(3*u)),(-1,absorb(u)))
            supplied[u] = all_supplied[u]
        current = M.compile_plan(plan,supplied)
        assert M.RANK.divergence(current) == M.RANK.T.pair_source(w)
        examples.append(dict(seed=w,direct_rule=direct['rule'],expanded=plan['expanded'],
                             coefficients=plan['coefficients'],rows=len(current),
                             current_hash=digest(current),supplied_hash=digest(supplied)))
        if w in (5821,1105909):
            tables.append(dict(plan=plan,supplied=supplied,current=current))

    # An unrecognized root is retained exactly, never silently discarded.
    first_unresolved = next(w for w in range(5,8192,8) if M.one_step(w) is None)
    unfinished = M.close(first_unresolved,max_nodes=10000)
    assert unfinished['current'] == {} and unfinished['coefficients'] == {first_unresolved:1}
    failures = 0
    for action in (lambda:M.one_step(1),lambda:M.one_step(-3),
                   lambda:M.close(221,max_nodes=0),
                   lambda:M.compile_plan(unfinished,{}),
                   lambda:M.compile_plan(unfinished,{first_unresolved:{}})):
        try:
            action()
        except (ValueError,RuntimeError):
            failures += 1
        else:
            raise AssertionError('Invalid or incomplete request was accepted')

    return dict(status='PASS',
                scope='Twelve strict-rho families with old-nine priority; sigma excluded; unresolved inputs retained',
                candidates=1024,old_accepted=old_count,accepted=len(plans),
                newly_accepted=len(new_inputs),categories=dict(sorted(counts.items())),
                plan_hash=digest(plans),old_plan_hash=digest(old_plan_rows),new_inputs_hash=digest(new_inputs),
                added_rule_witnesses=branch_witnesses,
                actual_substitutions=examples,tables=tables,
                distinct_supplied_pairs=len(all_supplied),supplied_hash=digest(all_supplied),
                explicit_unresolved_example=unfinished,rejection_checks=failures,
                caps=dict(candidate_upper_bound=8192,closure_nodes=10000,input_steps=10000,input_bits=512),
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('selected_rules.py','check_selected_rules.py')})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt',action='store_true')
    args = parser.parse_args()
    result = json.loads(json.dumps(audit(),sort_keys=True))
    path = HERE/'selected_rules_audit.json'
    if args.write_receipt:
        path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:
        assert json.loads(path.read_text()) == result,'Receipt differs; inspect before regenerating'
    print('PASS: twelve-family rho union, old-nine priority, exact supplied-current conversions and explicit unresolved inputs')


if __name__ == '__main__':main()
