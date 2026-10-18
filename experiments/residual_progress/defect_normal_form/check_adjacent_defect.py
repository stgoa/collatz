"""Bounded exact replay of the complete adjacent-defect reformulation."""
import argparse
import hashlib
import json
from pathlib import Path
import adjacent_defect as M

HERE = Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def expect_error(call, exception=ValueError):
    try:
        call()
    except exception:
        return
    raise AssertionError('Expected an explicit rejection')


def finite_absorption(seed):
    x, current = seed, {}
    while x != 1:
        if x in current or len(current) >= 10000 or x.bit_length() > 512:
            raise RuntimeError('Designated finite input unresolved within caps')
        current[x] = 1
        x = M.NORMAL.step(x)
    assert M.divergence(current) == M.atoms((1, seed))
    return current


def audit():
    rows = []
    for i in range(1024):
        q = 31+108*i
        if not M.NORMAL.canonical(q):
            continue
        w = (2*q+1)//3
        plan = M.defect_plan(w)
        n, z = plan['height'], plan['lower']
        assert M.EXACT.absorption_bound(n)['exception']['index'] == w
        assert M.NORMAL.valuation2(3*n+1) == 1
        middle = M.NORMAL.step(n)
        assert M.NORMAL.valuation2(3*middle+1) == 2 and M.NORMAL.step(middle) == q
        assert M.NORMAL.step(q+2) < n
        assert (5*q-83) >= 72
        assert q not in {M.NORMAL.normal_form(x) for x in (z, 3*z, 2*z+1, 6*z+3)}
        rows.append(dict(seed=w, rank=q, height=n, helpers=sorted(plan['coefficients'].items()),
                         current_hash=digest(plan['current'])))

    mixed = []
    for s in range(1, 2048, 2):
        data = M.mixed_absorption(s, max_nodes=1000)
        mixed.append(dict(seed=s, pairs=sorted(data['coefficients'].items()),
                          adjacent=sorted(data['adjacent'].items()), expanded=data['expanded'],
                          current_hash=digest(data['current'])))

    inverse = []
    good = 0
    for w in range(5, 32768, 8):
        q = M.RANK.rho(w)
        data = M.inverse_g(q)
        if data['count']:
            if M.eligible(w):
                assert data['count'] == 1 and data['minimum'] == 4*w//3-1
            else:
                assert w % 9 in (0,6)
                if data['count'] >= 2:
                    assert w % 9 == 6
                assert M.RANK.INVERSE.phase_pair_plan(w)['status'] == 'descending'
                good += 1
        elif not M.NORMAL.selected(3*w):
            assert q == 3*w
        inverse.append([w,q,data['minimum'],data['count'],digest(data['current'])])
    assert M.inverse_g(27)['minimum'] == M.inverse_g(31)['minimum'] == 27
    assert M.inverse_g(M.NORMAL.quotient_step(27))['minimum'] == 41
    assert M.inverse_g(M.NORMAL.quotient_step(31))['minimum'] == 47
    counterexample = M.transported_old_counterexample()

    examples, tables, all_supplied = [], [], {}
    for w in (21,93,4629):
        plan = M.defect_plan(w)
        q = plan['rank']
        supplied = {u:M.combine((1,finite_absorption(3*u)),(-1,finite_absorption(u)))
                    for u in plan['coefficients']}
        all_supplied.update(supplied)
        original_adjacent = M.combine((1,finite_absorption(q+2)),(-1,finite_absorption(q)))
        pair = M.compile_defect(plan, original_adjacent, supplied)
        assert M.compile_adjacent(plan, pair, supplied) == original_adjacent
        original_pair = M.combine((1,finite_absorption(3*w)),(-1,finite_absorption(w)))
        adjacent = M.compile_adjacent(plan, original_pair, supplied)
        assert M.compile_defect(plan, adjacent, supplied) == original_pair
        assert M.divergence(pair) == M.T.pair_source(w)
        assert M.divergence(adjacent) == M.adjacent_source(q)
        examples.append(dict(seed=w, helpers=len(supplied), pair_rows=len(pair),
                             adjacent_rows=len(adjacent), pair_hash=digest(pair),
                             adjacent_hash=digest(adjacent)))
        tables.append(dict(plan=plan, supplied=supplied, original_adjacent=original_adjacent,
                           compiled_pair=pair, original_pair=original_pair, compiled_adjacent=adjacent))

    valid = M.defect_plan(21)
    expect_error(lambda:M.parameters(5))
    expect_error(lambda:M.adjacent_source(139+2))
    expect_error(lambda:M.inverse_g(5))
    expect_error(lambda:M.compile_defect(valid,{},{}))
    expect_error(lambda:M.compile_adjacent(valid,{},{}))
    expect_error(lambda:M.compile_defect(valid,tables[0]['original_adjacent'],{}))
    expect_error(lambda:M.compile_adjacent(valid,tables[0]['original_pair'],{}))
    expect_error(lambda:M.mixed_absorption(27,max_nodes=0),RuntimeError)
    return dict(status='PASS',scope='Complete triangular source reformulation; no new accepted rule or adjacent-current supply',
                defect_plans=len(rows),defect_hash=digest(rows),mixed_absorption_plans=len(mixed),
                mixed_hash=digest(mixed),inverse_w5_cases=len(inverse),inverse_hash=digest(inverse),
                inverse_already_good_cases=good,rank_counterexample=counterexample,
                dynamic_counterexample=dict(equal_class=[27,31],next_minima=[41,47]),
                actual_bidirectional_conversions=examples,stored_tables=tables,
                distinct_supplied_helpers=len(all_supplied),rejection_checks=8,
                caps=dict(q_parameter_indices=[0,1023],mixed_seeds_below=2048,w5_below=32768,
                          mixed_nodes=1000,input_steps=10000,input_bits=512))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    result=audit()
    result['source_hashes']={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                             for name in ('adjacent_defect.py','check_adjacent_defect.py')}
    result=json.loads(json.dumps(result,sort_keys=True))
    path=HERE/'adjacent_defect_audit.json'
    if args.write_receipt:path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:assert json.loads(path.read_text()) == result,'Receipt differs; inspect before regenerating'
    print(f"PASS: {result['defect_plans']} complete defects, {result['mixed_absorption_plans']} mixed plans, "
          f"{result['inverse_w5_cases']} inverse-scope cases, three bidirectional conversions")


if __name__=='__main__':main()
