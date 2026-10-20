"""Finite checks of the common rank, mixed signed closure and actual inputs."""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import rules_union as U

M = U.RANK
HERE = Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def expect_error(kind, action):
    try:
        action()
    except kind:
        return
    raise AssertionError('Required rejection did not occur')


def finite_absorption(seed, cap=10000):
    x, rows = seed, {}
    for _ in range(cap+1):
        if x == 1:
            assert M.divergence(rows) == M.atoms((1, seed))
            return rows
        if x in rows or len(rows) == cap or x.bit_length() > 512:
            raise RuntimeError('Unresolved finite demonstration input')
        rows[x] = 1
        x = M.NORMAL.step(x)
    raise AssertionError('Unreachable')


def audit():
    nine, absorption = [], []
    for w in range(9,32768,16):
        data = M.nine_plan(w)
        nine.append([w,sorted(data['coefficients'].items()),digest(data['current'])])
    for s in range(1,8192,2):
        data = M.absorption_plan(s)
        absorption.append([s,sorted(data['coefficients'].items()),digest(data['current'])])
    exceptional = []
    for d,w,u in ((4,9,21),(6,377,637),(8,825,1045)):
        assert M.NORMAL.valuation2(9*w-1) == d
        assert u in M.NINE.local_plan(w)['coefficients']
        numerator,denominator = {4:(27*w+5,8),6:(81*w+23,32),8:(243*w+101,128)}[d]
        assert denominator*M.rho(u) == numerator
        exceptional.append(dict(d=d,w=w,u=u,rank=M.rho(w),child_rank=M.rho(u)))

    counts, closed, mixed = Counter(), [], []
    recognized = 0
    for w in range(5,8192,8):
        step = U.one_step(w)
        if step is None:
            counts['unresolved'] += 1
            continue
        recognized += 1
        counts[step['rule']] += 1
        data = U.close(w,max_nodes=10000)
        assert all(U.one_step(u) is None for u in data['coefficients'])
        rules = sorted({U.one_step(u)['rule'] for u in data['expanded']})
        if len(rules)>1:
            mixed.append([w,rules,len(data['expanded']),len(data['coefficients'])])
        if not data['coefficients']:
            closed.append(w)
    data = U.close(1029,max_nodes=10000)
    assert not data['coefficients'] and len(data['expanded'])>1
    assert M.divergence(M.compile_plan(data,{})) == M.T.pair_source(1029)
    # This is a finite closure through signed cancellation, not universal supply.
    closed_fixture = dict(seed=1029,current=data['current'],expanded=data['expanded'])
    increasing = U.BASE.decreasing_plan(1613)
    assert increasing['coefficients'][2549] == 1
    assert 2549>1613 and M.rho(2549)==3823<4839==M.rho(1613)

    tables, supplied_all, substitutions = [], {}, []
    for w in (61,69,749,1029,1245,1613,1821):
        plan = U.close(w,max_nodes=10000)
        supplied = {}
        for u in plan['coefficients']:
            if u not in supplied_all:
                supplied_all[u] = M.combine((1,finite_absorption(3*u)),(-1,finite_absorption(u)))
            supplied[u] = supplied_all[u]
        current = M.compile_plan(plan,supplied)
        assert M.divergence(current) == M.T.pair_source(w)
        substitutions.append(dict(w=w,expanded=plan['expanded'],coefficients=plan['coefficients'],
                                  rows=len(current),sha256=digest(current)))
        if w == 749:
            tables = dict(seed=w,plan=plan,inputs=supplied,current=current)

    assert U.close(21)['coefficients']=={21:1}
    expect_error(ValueError,lambda:M.validate_step(21,M.INVERSE.phase_pair_plan(21)))
    expect_error(ValueError,lambda:M.validate_step(61,dict(seed=61,current={},coefficients={})))
    expect_error(ValueError,lambda:M.compile_plan(U.close(61),{}))
    expect_error(ValueError,lambda:M.compile_plan(U.close(61),{5:{},21:{}}))
    expect_error(RuntimeError,lambda:U.close(749,max_nodes=1))
    expect_error(ValueError,lambda:U.close(9))
    expect_error(ValueError,lambda:M.validate_step(61,dict(seed=61,current={},coefficients={9:1})))
    return dict(status='PASS',scope='Finite rank and mixed-rule checks; universal leaf supply remains open',
                nine_plans=len(nine),nine_hash=digest(nine),absorption_plans=len(absorption),
                absorption_hash=digest(absorption),exceptional_rows=exceptional,
                union_candidates=1024,union_recognized=recognized,categories=dict(sorted(counts.items())),
                closed_without_inputs=closed,mixed_rule_examples=mixed,
                actual_substitutions=substitutions,distinct_supplied_inputs=len(supplied_all),
                closed_fixture=closed_fixture,rejection_checks=7,
                caps=dict(union_bound=8192,closure_nodes=10000,absorption_steps=10000,absorption_bits=512)),tables


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    result,fixture=audit()
    receipt=HERE/'critical_rank_audit.json'
    if args.write_receipt:
        receipt.write_text(json.dumps(result,indent=2)+'\n')
        (HERE/'w749_inputs.json').write_text(json.dumps(fixture,indent=2)+'\n')
        with (HERE/'w749_current.csv').open('w',newline='') as target:
            writer=csv.writer(target,lineterminator='\n')
            writer.writerow(('state','current'))
            writer.writerows(sorted(fixture['current'].items()))
    else:
        assert json.loads(receipt.read_text())==json.loads(json.dumps(result))
        assert json.loads((HERE/'w749_inputs.json').read_text())==json.loads(json.dumps(fixture))
        with (HERE/'w749_current.csv').open() as source:
            stored={int(r['state']):int(r['current']) for r in csv.DictReader(source)}
        assert stored==fixture['current']
    print(f'PASS: {result["nine_plans"]} W9 ranks; {result["absorption_plans"]} absorption bounds; '
          f'{result["union_recognized"]} union rules; {len(result["mixed_rule_examples"])} mixed closures; '
          'seven actual substitutions')


if __name__=='__main__':
    main()
