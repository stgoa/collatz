"""Bounded replay of selected inverse words, complete failures and CRT escapes."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import selected_inverse as M

HERE = Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def direct_words(data):
    q,p,b,r = data['rank'],data['first_inverse'],data['base'],data['endpoint']
    x = p
    for a in (1,2,2):
        assert M.NORMAL.valuation2(3*x+1) == a
        x = M.NORMAL.step(x)
    assert x == q and p > q
    x = r
    for a in data['word']:
        assert M.NORMAL.valuation2(3*x+1) == a
        x = M.NORMAL.step(x)
    assert x == q and len(data['word']) == data['ordinary_length']
    x = r
    for _ in range(data['quotient_length']):
        x = M.NORMAL.quotient_step(x)
    assert x == q and M.NORMAL.quotient_step(b) == p


def failed_vectors(data):
    """Independently check the complete H-vector decomposition in failed rows."""
    v,p,q,r,k,h = (data[t] for t in ('nine_index','first_inverse','rank','endpoint','k','h'))
    A = lambda x: M.RANK.absorption_plan(x)['coefficients']
    ell = (q+2)//3
    assert M.NORMAL.valuation2(9*v-1) == 6
    assert A(p) == M.combine((1,A(q)),(-1,A(ell)),(1,A(v)))
    if h == 0:
        assert A(r) == A(p)
    elif h == 1 and r % 3 == 0:
        c = r//3
        assert M.NORMAL.valuation2(9*c-1) == (4 if k == 4 else 5)
        assert A(r) == M.combine((1,A(q)),(-1,A(ell)),(1,A(c)))
        if k == 8:
            assert M.NORMAL.normal_form(M.NORMAL.step(c)) == (4*v-1)//3


def exact_affine_checks():
    cases = []
    for k in (4,8):
        for h in range(17):
            for v in (121,2041,1000001):
                q = Fraction(81*v+23,32)
                r = Fraction(2**(h+1)*(k*v+1),3**h)-1
                rhs = (k*2**(h+6)-3**(h+4))*v+2**(h+6)-55*3**h
                assert 32*3**h*(r-q) == rhs
                assert (rhs < 0) == (h >= (3 if k == 4 else 5))
                cases.append([k,h,v,rhs])
    return cases


def finite_absorption(seed, cap=10000):
    x,current = seed,{}
    for _ in range(cap+1):
        if x == 1:
            assert M.divergence(current) == M.atoms((1,seed))
            return current
        if x in current or len(current) == cap or x.bit_length() > 512:
            raise RuntimeError('Designated finite input unresolved')
        current[x] = 1
        x = M.NORMAL.step(x)
    raise AssertionError('Unreachable')


def expect_error(action):
    try:
        action()
    except ValueError:
        return
    raise AssertionError('Expected invalid request to be rejected')


def audit():
    formulas = exact_affine_checks()
    rows,categories,accepted = [],Counter(),[]
    for w in range(5,131072,8):
        if not M.eligible(w):
            continue
        successes = []
        for k in (4,8):
            plan = M.pair_plan(w,k)
            data = plan['parameters']
            direct_words(data)
            failed_vectors(data)
            categories[f'k{k}:{plan["status"]}'] += 1
            good = all(M.RANK.rho(u) < data['rank'] for u in plan['coefficients'])
            assert good == data['descending']
            successes.append(good)
            if good:
                accepted.append(w)
                M.RANK.validate_step(w,plan)
            else:
                expect_error(lambda: M.compile_plan(plan,{}))
            rows.append([w,k,data['h'],data['endpoint'],plan['status'],
                         sorted(plan['coefficients'].items()),digest(plan['current'])])
        assert M.recognized(w) == any(successes)

    families = []
    for k in (4,8):
        for h in list(range(1,13))+[16,32,64,128]:
            for e in (1,2):
                for index in (0,1,7):
                    family = M.parameter_family(k,h,e,index)
                    data = M.parameters(family['seed'],k)
                    direct_words(data)
                    assert family['seed'] % 3456 == 3445
                    plan = M.pair_plan(family['seed'],k)
                    families.append([k,h,e,index,family['seed'],data['endpoint'],
                                     plan['status'],digest(plan['current'])])

    avoiding = []
    for depth in (1,2,3,4,8,16,32,64,128):
        for k in (4,8):
            for e in (1,2):
                family = M.avoidance_family(depth,k,terminal_unit=e)
                data = M.parameters(family['seed'],k)
                direct_words(data)
                q0,x = family['rank'],family['rank']
                for cycle in range(depth):
                    start = x
                    for _ in range(7):
                        x = M.NORMAL.quotient_step(x)
                        assert x > q0
                    assert 2048*(x+17) == 2187*(start+17)
                    assert x % 5184 == 5167
                assert data['endpoint'] < q0 and data['ordinary_length'] == (7 if k == 4 else 9)
                avoiding.append(dict(family=family,final_forward=x,inverse_endpoint=data['endpoint']))

    examples,tables = [],[]
    seeds = [(min(accepted),4),(93301,4),(148597,8),
             (M.avoidance_family(1)['seed'],4)]
    for w,k in seeds:
        plan = M.pair_plan(w,k)
        supplied = {u:M.combine((1,finite_absorption(3*u)),(-1,finite_absorption(u)))
                    for u in plan['coefficients']}
        current = M.compile_plan(plan,supplied)
        assert M.divergence(current) == M.T.pair_source(w)
        examples.append(dict(seed=w,k=k,inputs=len(supplied),rows=len(current),current_hash=digest(current)))
        if w in (93301,148597):
            tables.append(dict(seed=w,plan=plan,inputs=supplied,current=current))

    good = M.pair_plan(93301,4)
    expect_error(lambda: M.parameters(3445,2))
    expect_error(lambda: M.parameters(5,4))
    expect_error(lambda: M.compile_plan(good,{}))
    expect_error(lambda: M.compile_plan(good,{u:{} for u in good['coefficients']}))
    expect_error(lambda: M.compile_plan(M.pair_plan(3445,8),{}))
    expect_error(lambda: M.parameter_family(4,0))
    expect_error(lambda: M.avoidance_family(0))
    expect_error(lambda: M.avoidance_family(1,8,h=4))

    return dict(status='PASS',scope='Complete prescribed inverse interface; two strict domains, universal complement open',
                candidates=16384,eligible_inputs=len(rows)//2,two_choice_plans=len(rows),
                categories=dict(sorted(categories.items())),plans_hash=digest(rows),
                affine_checks=len(formulas),affine_hash=digest(formulas),
                exact_phase_examples=families,forward_avoidance_intersections=avoiding,
                actual_substitutions=examples,stored_tables=tables,rejection_checks=8,
                caps=dict(candidate_upper=131072,input_steps=10000,input_bits=512))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt',action='store_true')
    args = parser.parse_args()
    result = audit()
    path = HERE/'selected_inverse_audit.json'
    if args.write_receipt:
        path.write_text(json.dumps(result,indent=2)+'\n')
    else:
        assert json.loads(path.read_text()) == json.loads(json.dumps(result))
    print(f'PASS: {result["eligible_inputs"]} selected inputs; {result["two_choice_plans"]} exact plans; '
          f'{len(result["exact_phase_examples"])} phase examples; '
          f'{len(result["forward_avoidance_intersections"])} growing-prefix intersections; four substitutions')


if __name__ == '__main__':
    main()
