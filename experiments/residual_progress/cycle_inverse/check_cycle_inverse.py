"""Exact bounded replay of the maximal cycle/point inverse comparison."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import cycle_inverse as M

HERE = Path(__file__).resolve().parent


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, HERE.parent/relative)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


TWELVE = load('cycle_inverse_twelve', 'selected_rules/selected_rules.py')
EXIT = load('cycle_inverse_exit', 'selected_cycle_exit/selected_exit.py')


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def expect_error(action):
    try:
        action()
    except ValueError:
        return
    raise AssertionError('Expected rejection')


def finite_absorption(seed):
    x, current = seed, {}
    while x != 1:
        if x in current or len(current) >= 10000 or x.bit_length() > 512:
            raise RuntimeError('Designated supplied input unresolved within caps')
        current[x] = 1
        x = M.NORMAL.step(x)
    assert M.divergence(current) == M.atoms((1, seed))
    return current


def affine_audit():
    rows = []
    for k in range(1, 33):
        for j in range(8):
            for v in (2041, 1000001):
                q = Fraction(81*v+23, 32)
                p = Fraction(2**(11*k)*(8*v+18), 3**(7*k))-17
                eta = Fraction(2**j, 3**j)*(p+1)-1
                den = 3**(7*k+j)
                rhs = (256*2**(11*k+j)-81*den)*v+576*2**(11*k+j)-512*2**j*3**(7*k)-55*den
                assert 32*den*(eta-q) == rhs
                assert (rhs < 0) == (j >= M.point_threshold(k))
                rows.append([k, j, v, rhs])
    for k, j in ((5,2), (11,1), (17,0)):
        a, t = Fraction(2048,2187)**k, Fraction(2,3)**j
        lam = Fraction(256,81)*a*t
        beta = t*(Fraction(1274,81)*a-16)-1
        assert lam > 1 and lam*5167+beta > 5167
    for k, j in ((1,3), (6,2), (12,1), (18,0)):
        assert 256*2**(11*k+j) < 81*3**(7*k+j)
    return dict(cases=len(rows), hash=digest(rows), exact_boundary_checks=7)


def check_plan(w):
    plan = M.pair_plan(w)
    data = plan['parameters']
    path = M.bridge(w)['path']
    assert len(path)-1 == data['ordinary_length']
    if data['cycles']:
        p, eta, k, j = (data[x] for x in ('cycle_endpoint', 'endpoint', 'cycles', 'point_depth'))
        assert M.RANK.INVERSE.valuation3(p+17) == data['remainder']
        assert M.RANK.absorption_plan(p)['coefficients'] == M.RANK.absorption_plan(eta)['coefficients']
        assert data['ordinary_length'] == j+7*k+4
    else:
        old = M.OLD.pair_plan(w, 4)
        assert plan['current'] == old['current'] and plan['coefficients'] == old['coefficients']
    good = all(M.RANK.rho(u) < data['rank'] for u in plan['coefficients'])
    assert good == data['descending']
    if not good:
        expect_error(lambda: M.compile_plan(plan, {}))
    return dict(seed=w, cycles=data['cycles'], remainder=data['remainder'],
                point_depth=data['point_depth'], endpoint=data['endpoint'],
                status=plan['status'], leading=plan['leading'],
                coefficients=sorted(plan['coefficients'].items()), current_hash=digest(plan['current']))


def audit():
    rows, categories = [], Counter()
    for h in range(1, 7):
        for unit in (1, 2):
            r2 = -19*pow(3**h, -1, 8192) % 8192
            U = r2+8192*((unit-r2)*pow(8192, -1, 3) % 3)
            v = (3**h*U-9)//4
            w = (27*v+13)//16
            assert M.parameters(w)['ternary_depth'] == h
            rows.append(check_plan(w))
    for k in (1, 5, 6, 11, 12, 17, 18):
        for j in range(5):
            for unit in ((1,) if j == 0 else (1,2)):
                family = M.parameter_family(k,j,unit)
                rows.append(check_plan(family['seed']))
    for k in (1, 18):
        for remainder in range(1, 7):
            for unit in (1,2):
                family = M.parameter_family(k,0,unit,remainder=remainder)
                rows.append(check_plan(family['seed']))
    for row in rows:
        categories[row['status']] += 1

    avoiding = []
    for L in (0,1,2,3,4,8,16,32,64):
        family = M.parameter_family(1,3,avoidance_depth=L)
        w = family['seed']
        plan = M.pair_plan(w)
        q = plan['rank']
        assert plan['parameters']['ordinary_length'] == 14
        assert plan['status'] == 'descending'
        assert TWELVE.one_step(w) is None
        data = EXIT.parameters(w)
        assert data['prefix']['repeats'] == L and data['exit']['e'] == 13
        assert data['minimum'] == data['endpoint'] > q
        assert data['rank_bound'] == data['endpoint']
        assert M.OLD.parameters(w,4)['h'] == M.OLD.parameters(w,8)['h'] == 0
        avoiding.append(dict(family=family, endpoint=plan['parameters']['endpoint'],
                             old_exit=data['endpoint'], current_hash=digest(plan['current']),
                             requests=sorted(plan['coefficients'].items())))

    long_words = []
    for k,j in ((32,0),(64,0),(1,32),(1,64)):
        family = M.parameter_family(k,j)
        bridge = M.bridge(family['seed'])
        long_words.append(dict(k=k,j=j,seed=family['seed'],
                               arrows=len(bridge['path'])-1,hash=digest(bridge['current'])))

    examples, tables = [], []
    for family in (M.parameter_family(1,3), M.parameter_family(1,3,index=1),
                   M.parameter_family(1,3,avoidance_depth=0)):
        w = family['seed']
        plan = M.pair_plan(w)
        supplied = {u:M.combine((1,finite_absorption(3*u)),(-1,finite_absorption(u)))
                    for u in plan['coefficients']}
        current = M.compile_plan(plan,supplied)
        assert M.divergence(current) == M.T.pair_source(w)
        examples.append(dict(seed=w,inputs=len(supplied),rows=len(current),hash=digest(current)))
        if len(tables) < 2:
            tables.append(dict(seed=w,plan=plan,supplied=supplied,current=current))
    good = M.pair_plan(examples[0]['seed'])
    expect_error(lambda:M.parameters(5))
    expect_error(lambda:M.parameters(3445))
    expect_error(lambda:M.parameter_family(0,3))
    expect_error(lambda:M.parameter_family(1,-1))
    expect_error(lambda:M.parameter_family(1,1,remainder=1))
    expect_error(lambda:M.parameter_family(1,3,avoidance_depth=-1))
    expect_error(lambda:M.compile_plan(good,{}))
    expect_error(lambda:M.compile_plan(good,{u:{} for u in good['coefficients']}))
    return dict(status='PASS',scope='One complete inverse procedure; universal current supply remains open',
                affine=affine_audit(),full_plans=len(rows),categories=dict(categories),
                plan_hash=digest(rows),exact_plan_rows=rows,old_twelve_exclusions=avoiding,
                long_words=long_words,actual_substitutions=examples,stored_tables=tables,
                rejection_checks=8,caps=dict(input_steps=10000,input_bits=512))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt',action='store_true')
    args = parser.parse_args()
    result = audit()
    result['source_hashes'] = {name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('cycle_inverse.py','check_cycle_inverse.py')}
    path = HERE/'cycle_inverse_audit.json'
    normalized = json.loads(json.dumps(result))
    if args.write_receipt:
        path.write_text(json.dumps(normalized,indent=2,sort_keys=True)+'\n')
    else:
        assert json.loads(path.read_text()) == normalized
    print('PASS: maximal cycle/point inverse, complete failures, old-twelve exclusions and supplied currents')


if __name__ == '__main__':
    main()
