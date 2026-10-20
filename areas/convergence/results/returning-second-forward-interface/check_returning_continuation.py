"""Exact bounded replay of the prescribed second returning block."""
import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import returning_continuation as M

HERE = Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def finite_absorption(seed, cap=10000):
    current, x = {}, seed
    for _ in range(cap+1):
        if x == 1:
            assert M.divergence(current) == M.atoms((1, seed))
            return current
        if x in current or len(current) == cap or x.bit_length() > 512:
            raise RuntimeError('Designated finite input remains unresolved: '+str(seed))
        current[x] = 1
        x = M.NORMAL.step(x)
    raise AssertionError('Unreachable')


def affine_comparisons():
    rows = []
    for v in (1, 11, 37, 1001):
        for A, coefficient in ((2, 1319), (3, 1909), (4, 1631)):
            q = F(2**(A+3)*v-13, 9)
            f = F(3*(3**(A-1)*v-1), 8)
            assert q-F(9*f+5, 8) == F(coefficient*v-949, 576)
        def raw(A, d):
            return F(2*3**(d//2)*(3**(A-1)*v-1), 2**d)+1
        for A, d, c, intercept, denominator in (
                (2,2,-17,-17,18), (2,4,13,-95,72),
                (3,6,-139,-461,288), (3,8,1631,-2087,1152),
                (4,8,-3299,-2087,1152), (4,10,6487,-9077,4608)):
            q = F(2**(A+3)*v-13, 9)
            assert q-raw(A,d) == F(c*v+intercept,denominator)
        for A, d, c, intercept, denominator in (
                (2,2,295,-353,288), (3,4,1631,-1655,1152), (4,6,6487,-7349,4608)):
            q = F(2**(A+3)*v-13,9)
            n = (raw(A,d)-1)/2
            assert q-(9*n+5)/8 == F(c*v+intercept,denominator)
        for A, d, coefficients in (
                (3,2,((1631,-1979,1152),(-139,-353,288),(13,-25,36))),
                (4,4,((6487,-8645,4608),(-3299,-1655,1152),(-139,-127,144))),
                (4,2,((-3299,-1979,1152),(-2465,-353,288),(-217,-25,36)))):
            q = F(2**(A+3)*v-13,9)
            n = (raw(A,d)-1)/2
            actual = (q-(27*n+29)/32, q-(9*n+5)/8, q-n)
            assert actual == tuple(F(c*v+i,dn) for c,i,dn in coefficients)
            rows.append([v,A,d,[[x.numerator,x.denominator] for x in actual]])
    return rows


def check_clock(data):
    x = data['rank']
    for _ in range(data['quotient_length']):
        x = M.NORMAL.quotient_step(x)
    assert x == data['minimum']
    second = data['second']
    if second['kind'] == 'complete_run':
        A, d = second['a'], second['d']
        assert len(second['left'])-1 == (A+(d-1)//2 if d%2 else A+d//2-1)
        assert len(second['right'])-1 == (1 if d%2 else 0)
        assert second['left'][-1] == second['right'][-1]


def check_old_missing(data):
    assert data['first_rejected'] and M.OLD.returning(data['seed'])
    q, w = data['rank'], data['seed']
    assert q % 27 == 4 and w % 9 == 3
    assert M.INVERSE.valuation3(q-1) == 1
    assert M.INVERSE.valuation3(4*((q-1)//3)+2) == 1
    assert M.NORMAL.selected(3*w)


def audit():
    formulas = affine_comparisons()
    plans, categories, new, low, worsened = [], Counter(), [], [], []
    for w in range(5,131072,8):
        if not M.OLD.returning(w):
            continue
        plan = M.continuation_plan(w)
        data = plan['parameters']
        check_clock(data)
        categories[str((plan['status'], data['first_rejected'], data['second']['kind']))] += 1
        if plan['status'] == 'descending' and data['first_rejected']:
            check_old_missing(data)
            new.append(w)
        elif plan['status'] != 'descending' and not data['first_rejected']:
            worsened.append(w)
        if (data['first']['a'] == 3 and data['first_minimum'] == data['first']['endpoint']
                and data['first']['endpoint'] % 4 == 3):
            assert data['first']['endpoint'] % 243 == 157
            assert data['first']['endpoint'] > data['rank']
            if data['second']['a'] in (2,3,4):
                assert (plan['status'] == 'descending') == M.low_exponent_domain(data)
                low.append(w)
        plans.append([w,plan['status'],data['first_rejected'],data['endpoint'],data['minimum'],
                      plan['input_rank_bound'],sorted(plan['coefficients'].items()),digest(plan['current'])])

    cells, cell_categories = [], Counter()
    for A in (2,3,4):
        for d in range(2,18):
            for j in range(16):
                family = M.cell_family(3,A,d,j)
                data = M.parameters(family['seed'])
                accepted = data['rank_bound'] < data['rank']
                assert accepted == M.low_exponent_domain(data)
                assert data['first']['endpoint'] % 243 == 157
                assert data['second']['t'] >= 11
                check_old_missing(data)
                key = (A,d,M.NORMAL.selected(data['endpoint']) if d%2==0 else 'odd',
                       data['minimum']%8,accepted)
                cell_categories[str(key)] += 1
                cells.append([family['seed'],A,d,accepted,data['minimum']])

    families = []
    for a,A in [(a,A) for a in range(3,13) for A in (2,3,4,8)]+[(16,16),(32,16),(32,32),(64,64)]:
        for j in (0,1,7):
            family = M.long_family(a,A,j)
            plan = M.continuation_plan(family['seed'])
            assert plan['status'] == 'descending'
            check_clock(plan['parameters'])
            check_old_missing(plan['parameters'])
            assert family['seed'] == family['seed_residue']+j*family['seed_period']
            families.append(dict(family=family,rows=len(plan['current']),requests=len(plan['coefficients']),
                                 current_hash=digest(plan['current'])))

    supplied, actual, tables = {}, [], []
    for w in list(dict.fromkeys([1533,3837,5565]+new[:8])):
        plan = M.continuation_plan(w)
        for u in plan['coefficients']:
            if u not in supplied:
                supplied[u] = M.combine((1,finite_absorption(3*u)),(-1,finite_absorption(u)))
        current = M.compile_plan(plan,supplied)
        assert M.divergence(current) == M.T.pair_source(w)
        actual.append(dict(seed=w,rank=plan['rank'],requests=sorted(plan['coefficients'].items()),
                           rows=len(current),current_hash=digest(current)))
        if w in (1533,3837,5565):
            tables.append(dict(seed=w,current=sorted(current.items()),
                               supplied={u:sorted(supplied[u].items()) for u in plan['coefficients']}))

    failures = 0
    good = M.continuation_plan(1533)
    for action in (lambda:M.compile_plan(good,{}),
                   lambda:M.compile_plan(good,{u:{} for u in good['coefficients']}),
                   lambda:M.compile_plan(M.continuation_plan(21),{}),
                   lambda:M.continuation_plan(13),lambda:M.cell_family(2,2,2),
                   lambda:M.long_family(64,64,d=3),lambda:M.long_family(3,2,d=4)):
        try:
            action()
        except ValueError:
            failures += 1
        else:
            raise AssertionError('Invalid request was not rejected')

    return dict(status='PASS',scope='Conditional second returning block, complete low-exponent table and CRT families; universal supply open',
                returning_inputs=len(plans),plan_hash=digest(plans),categories=dict(sorted(categories.items())),
                newly_accepted=len(new),new_examples=new[:32],old_accepted_but_new_failed=len(worsened),
                low_exponent_checks=len(low),cell_checks=len(cells),cell_hash=digest(cells),
                cell_categories=dict(sorted(cell_categories.items())),affine_formula_checks=formulas,
                long_families=families,actual_substitutions=actual,actual_current_tables=tables,
                distinct_supplied_inputs=len(supplied),supplied_hash=digest(supplied),rejection_checks=failures,
                caps=dict(seed_upper_bound=131072,cell_a=3,cell_A=[2,3,4],cell_d=[2,17],
                          cell_indices=[0,15],largest_first_exponent=64,largest_second_exponent=64,
                          input_discovery_steps=10000,input_discovery_bits=512),
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('returning_continuation.py','check_returning_continuation.py')})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt',action='store_true')
    args = parser.parse_args()
    result = json.loads(json.dumps(audit(),sort_keys=True))
    path = HERE/'returning_continuation_audit.json'
    if args.write_receipt:
        path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:
        assert json.loads(path.read_text()) == result,'Receipt differs; inspect before regenerating'
    print('PASS: second returning blocks, complete low-exponent table, long CRT families and supplied-input conversions')


if __name__ == '__main__':
    main()
