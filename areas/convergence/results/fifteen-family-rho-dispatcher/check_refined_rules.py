"""Bounded audit of fifteen-family strict-rho composition and exact supply."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import refined_rules as M

HERE = Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def absorb(seed):
    x, current = seed, {}
    for _ in range(10001):
        if x == 1:
            assert M.RANK.divergence(current) == M.RANK.atoms((1, seed))
            return current
        if x in current or len(current) == 10000 or x.bit_length() > 512:
            raise RuntimeError('Finite demonstration input reached its cap')
        current[x] = 1
        x = M.RANK.NORMAL.step(x)
    raise AssertionError('Unreachable')


def audit():
    counts, plans, old_count, old_plan_rows = Counter(), [], 0, []
    new_inputs = []
    for w in range(5, 8192, 8):
        old, plan = M.OLD.one_step(w), M.one_step(w)
        if old is not None:
            old_count += 1
            assert plan == old
            old_plan_rows.append([w, old['rule'], digest(old['current']), sorted(old['coefficients'].items())])
        if plan is None:
            counts['unresolved'] += 1
        else:
            M.RANK.validate_step(w, plan)
            counts[plan['rule']] += 1
            plans.append([w, plan['rule'], digest(plan['current']), sorted(plan['coefficients'].items())])
            if old is None:
                new_inputs.append(w)
                expected = None
                for module, name in M.ADDED:
                    candidate = module.one_step(w)
                    if candidate is not None:
                        expected = name
                        assert plan['current'] == candidate['current']
                        assert plan['coefficients'] == candidate['coefficients']
                        break
                assert plan['rule'] == expected
    assert old_count == 722
    old_receipt = json.loads((HERE.parent/'selected_rules/selected_rules_audit.json').read_text())
    assert digest(old_plan_rows) == old_receipt['plan_hash']

    # The inverse-cycle family overlaps deferred expansion in some witnesses.
    # Use a parameter-family member which really selects the final branch.
    cycle_family = M.CYCLE.parameter_family(1, 3, unit=2, index=0)
    assert cycle_family['seed'] == 11432437
    branch_witnesses = []
    for w, expected in ((4021, 'R58_exact_absorption_bound'),
                        (1301, 'R59_deferred_rank'),
                        (cycle_family['seed'], 'R60_cycle_inverse')):
        assert M.OLD.one_step(w) is None
        plan = M.one_step(w)
        assert plan['rule'] == expected
        M.RANK.validate_step(w, plan)
        branch_witnesses.append(dict(seed=w, rule=expected, current_hash=digest(plan['current']),
                                     coefficients=sorted(plan['coefficients'].items())))
    assert {x['rule'] for x in branch_witnesses} == {name for _, name in M.ADDED}
    overlap_seed = M.CYCLE.parameter_family(1, 3, avoidance_depth=0)['seed']
    assert overlap_seed == 284897820661
    assert M.OLD.one_step(overlap_seed) is None
    assert M.CYCLE.one_step(overlap_seed) is not None
    assert M.one_step(overlap_seed)['rule'] == 'R59_deferred_rank'

    examples, tables, all_supplied = [], [], {}
    for w in (221, 4021, 245, 1301, 787733, 11432437, overlap_seed):
        direct = M.one_step(w)
        assert direct is not None
        plan = M.close(w, max_nodes=10000)
        supplied = {}
        for u in plan['coefficients']:
            if u not in all_supplied:
                all_supplied[u] = M.RANK.combine((1, absorb(3*u)), (-1, absorb(u)))
            supplied[u] = all_supplied[u]
        current = M.compile_plan(plan, supplied)
        assert M.RANK.divergence(current) == M.RANK.T.pair_source(w)
        examples.append(dict(seed=w, direct_rule=direct['rule'], expanded=plan['expanded'],
                             coefficients=plan['coefficients'], rows=len(current),
                             current_hash=digest(current), supplied_hash=digest(supplied)))
        if w in (1301, 11432437):
            tables.append(dict(plan=plan, supplied=supplied, current=current))

    first_unresolved = next(w for w in range(5, 8192, 8) if M.one_step(w) is None)
    unfinished = M.close(first_unresolved, max_nodes=10000)
    assert unfinished['current'] == {} and unfinished['coefficients'] == {first_unresolved: 1}
    failures = 0
    for action in (lambda: M.one_step(1), lambda: M.one_step(-3),
                   lambda: M.close(221, max_nodes=0),
                   lambda: M.compile_plan(unfinished, {}),
                   lambda: M.compile_plan(unfinished, {first_unresolved: {}})):
        try:
            action()
        except (ValueError, RuntimeError):
            failures += 1
        else:
            raise AssertionError('Invalid or incomplete request was accepted')

    # R59 caps never become a certified missing premise or recurse into R60.
    macro = M.DEFERRED.OLD.FORWARD.forward_plan(1301)
    capped = M.DEFERRED.defer(macro, max_nodes=0)
    assert capped['status'] == 'capped' and capped['remaining_high']
    assert M.DEFERRED.one_step(1301, max_nodes=0) is None
    assert M.DEFERRED.OLD.__file__.endswith('/selected_rules/selected_rules.py')

    return dict(status='PASS',
                scope='Fifteen strict-rho families with old-twelve priority; fixed-twelve deferred resolver; sigma excluded; missing inputs retained',
                candidates=1024, old_accepted=old_count, accepted=len(plans),
                newly_accepted=len(new_inputs), categories=dict(sorted(counts.items())),
                plan_hash=digest(plans), old_plan_hash=digest(old_plan_rows), new_inputs_hash=digest(new_inputs),
                added_rule_witnesses=branch_witnesses, cycle_family=cycle_family,
                overlap_seed=overlap_seed, overlap_rule='R59_deferred_rank',
                actual_substitutions=examples, tables=tables,
                distinct_supplied_pairs=len(all_supplied), supplied_hash=digest(all_supplied),
                explicit_unresolved_example=unfinished, rejection_checks=failures,
                explicit_deferred_cap=capped,
                caps=dict(candidate_upper_bound=8192, closure_nodes=10000, deferred_nodes=10000,
                          input_steps=10000, input_bits=512),
                source_hashes={name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('refined_rules.py', 'check_refined_rules.py')})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result = json.loads(json.dumps(audit(), sort_keys=True))
    path = HERE/'refined_rules_audit.json'
    if args.write_receipt:
        path.write_text(json.dumps(result, sort_keys=True, indent=2)+'\n')
    else:
        assert json.loads(path.read_text()) == result, 'Receipt differs; inspect before regenerating'
    print('PASS: fifteen-family rho union, old-twelve priority, fixed deferred resolver and exact supplied-current conversions')


if __name__ == '__main__':
    main()
