"""Independent finite checks of the native-W9 composition and its failures."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from types import ModuleType
import native_nine as M

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def rows(x):
    return [[a, c] for a, c in sorted(x.items())]


def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def step(x):
    y = 3*x+1
    return y//(y & -y)


def div(current):
    out = Counter()
    for x, c in current.items():
        assert type(x) is int and x > 1 and x % 2 and type(c) is int
        out[x] += c
        y = step(x)
        if y != 1:
            out[y] -= c
    return {x: c for x, c in out.items() if c}


def check(plan):
    expected = {3*plan['seed']: 1, plan['seed']: -1}
    for w, c in plan['coefficients'].items():
        expected = M.combine((1, expected), (-c, {3*w: 1, w: -1}))
    assert div(plan['current']) == expected


def reject(action, error=ValueError):
    try:
        action()
    except error:
        return
    raise AssertionError('Expected rejection')


def sources():
    pending, seen, paths = [M], set(), {Path(__file__).resolve()}
    while pending:
        module = pending.pop()
        if id(module) in seen:
            continue
        seen.add(id(module))
        file = getattr(module, '__file__', None)
        if not file:
            continue
        p = Path(file).resolve()
        if not p.is_relative_to(ROOT):
            continue
        paths.add(p)
        pending.extend(v for v in vars(module).values() if isinstance(v, ModuleType))
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}


def finite_pair(w):
    def path(x):
        out = {}
        while x != 1:
            if x in out or len(out) >= 10000 or x.bit_length() > 4096:
                raise RuntimeError('Designated finite supply exceeded its caps')
            out[x] = 1
            x = step(x)
        return out
    answer = M.combine((1, path(3*w)), (-1, path(w)))
    assert div(answer) == {3*w: 1, w: -1}
    return answer


def demo(plan):
    supplied = {w: finite_pair(w) for w in plan['coefficients']}
    out = M.compile_plan(plan, supplied)
    assert div(out) == {3*plan['seed']: 1, plan['seed']: -1}
    reject(lambda: M.compile_plan(plan, {}))
    wrong = dict(supplied)
    wrong[next(iter(wrong))] = {}
    reject(lambda: M.compile_plan(plan, wrong))
    wrong = dict(supplied)
    wrong[next(iter(wrong))] = {3: True}
    reject(lambda: M.compile_plan(plan, wrong))
    return dict(seed=plan['seed'], rank=plan['rank'], current_rows=len(out),
                plan_current=rows(plan['current']), coefficients=rows(plan['coefficients']),
                supplied={str(w): rows(c) for w, c in sorted(supplied.items())},
                current=rows(out), current_hash=digest(rows(out)))


def affine_checks():
    checks = []
    for t in (191, 191+1728, 191+1728*2**64):
        n, m = Fraction(128*t-13, 9), Fraction(81*t-3, 4)
        cases = [
            (n-(9*m+5)/8, Fraction(-2465*t-353, 288), False),
            (n-(27*m+23)/32, Fraction(-3299*t-1763, 1152), False),
            (n-(81*m+101)/128, Fraction(6487*t-8105, 4608), True),
            (n-(9*m-3)/16, Fraction(1631*t-481, 576), True),
            (n-(81*m+53)/128, Fraction(6487*t-6377, 4608), True)]
        for left, right, positive in cases:
            assert left == right and (left > 0) == positive
            checks.append([str(left), positive])
    for q in (209935, 209935+59049*4, 209935+59049*4*2**64):
        n = Fraction(16384*q-29839, 19683)
        cases = [
            (n-Fraction(9*q-3,32),Fraction(347141*q-895799,629856),True),
            (n-Fraction(9*q+5,8),Fraction(-46075*q-337127,157464),False),
            (n-Fraction(27*q+23,32),Fraction(-7153*q-1407557,629856),False),
            (n-Fraction(81*q+101,128),Fraction(502829*q-5807375,2519424),True),
            (n-Fraction(9*q-3,16),Fraction(84997*q-418375,314928),True)]
        for left, right, positive in cases:
            assert left == right and (left > 0) == positive
            checks.append([str(left), positive])
    return checks


def audit():
    contraction = []
    for c in range(9, 8192, 16):
        plan = M.NINE.local_plan(c)
        if plan['d'] == 4 and not M.NORMAL.canonical(3*plan['z']):
            continue
        maximum = max(map(M.rho, plan['coefficients']), default=0)
        assert 32*maximum <= 81*c+23
        contraction.append([c, maximum, maximum*32 == 81*c+23])
    assert any(x[2] for x in contraction)

    native, branches = [], set()
    seeds = {905+8192*i for i in range(128)}
    for d in range(4, 33):
        for index in range(4):
            cell = M.native_cell(d, index)
            seeds.add(cell['seed'])
            assert M.native_cell(d, index+1)['seed']-cell['seed'] == cell['seed_period']
    for d in (64, 128, 256):
        for index in (0, 2**64):
            seeds.add(M.native_cell(d, index)['seed'])
    for b in sorted(seeds):
        plan = M.native_plan(b)
        check(plan)
        data = plan['parameters']
        expected = not (data['d'] in (4,6) and not data['upper_canonical'])
        assert (plan['status']=='descending') == expected
        first = M.BASIS.SIGMA.RETURN.forward_plan(data['returning'])
        second = M.SECOND.continuation_plan(data['returning'])
        assert first['status']=='unresolved'
        assert (second['status']=='descending') == expected
        assert all(M.rho(v)<plan['rank'] for v in second['coefficients']) == expected
        if expected:
            M.BASIS.validate(plan)
        else:
            reject(lambda: M.compile_plan(plan, {}))
            if data['d']==4:
                returned=M.d4_return(b);check(returned)
                reject(lambda:M.BASIS.validate(returned))
        native.append([b, data['d'], data['upper_canonical'], expected,
                       rows(plan['coefficients']), digest(rows(plan['current']))])
        branches.add((data['d'],data['upper_canonical']))

    d6_seeds = set()
    for d in range(2, 33):
        for index in range(4):
            cell = M.d6_A2_cell(d,index)
            d6_seeds.add(cell['seed'])
            assert M.d6_A2_cell(d,index+1)['seed']-cell['seed'] == cell['seed_period']
    for d in (64,128,256):
        for index in (0,2**64):
            d6_seeds.add(M.d6_A2_cell(d,index)['seed'])
    for j in range(64):
        b=58249+65536*j
        if M.NORMAL.selected(3*((19683*b+12677)//8192)):
            d6_seeds.add(b)
    inverses, forward_rows, other_A = [], [], []
    old_local_success_original_failure = None
    demo_seeds = []
    for b in sorted(d6_seeds):
        data=M.d6_parameters(b)
        four,eight=M.inverse_pair_plan(b,4),M.inverse_pair_plan(b,8)
        check(four);check(eight)
        assert four['inverse']['parameters']['h']==3
        assert eight['inverse']['parameters']['h']==0
        assert four['inverse']['parameters']['endpoint']==data['first_critical']
        end=M.prefix(data['first_critical'],(1,1,1,2))
        upper=M.prefix(data['child_rank'],(1,2,2))
        assert M.combine((1,end['current']),
                         (1,M.NORMAL.bridge(data['first_endpoint'])['current']),
                         (1,upper['current']),(1,four['inverse']['current'])) == {}
        undo,k8=M.d6_undo(b),M.d6_k8(b)
        check(undo);check(k8)
        reject(lambda:M.BASIS.validate(undo))
        reject(lambda:M.BASIS.validate(k8))
        inverses.append([b,rows(undo['coefficients']),digest(rows(undo['current'])),
                         rows(k8['coefficients']),digest(rows(k8['current']))])
        plan=M.d6_forward_plan(b);check(plan)
        fdata=plan['forward']['parameters'];f=fdata['endpoint']
        left,right=plan['upper_comparison_clocks']
        x,y=data['rank'],f
        for _ in range(left):x=step(x)
        for _ in range(right):y=step(y)
        assert x==y
        if plan['next_a']==2:
            expected=bool(plan['next_d']%2 or plan['next_d']>=6 or plan['next_selected'])
            assert (plan['status']=='descending')==expected
            assert plan['actual_rank_status']==expected
            if expected and len(demo_seeds)<2 and plan['next_d'] in(2,3):
                demo_seeds.append(b)
            if not expected:
                reject(lambda:M.compile_plan(plan,{}))
                assert plan['next_d'] in (2,4) and M.NORMAL.canonical(f)
                assert f % 3 == 1 and f % 4 == 3
                leader=(2*f+1)//3
                assert leader % 8 == 5 and M.rho(leader)==f>data['rank']
                assert plan['coefficients'][leader]==1
            old=M.FORWARD.forward_plan(data['higher_five'])
            if old['status']=='descending' and not expected:
                old_local_success_original_failure=dict(seed=b,higher_five=data['higher_five'],
                    original_rank=data['rank'],higher_rank=data['higher_rank'],next_d=plan['next_d'],
                    endpoint=f,old_status=old['status'],native_status=plan['status'])
            forward_rows.append([b,plan['next_d'],plan['next_selected'],expected,
                                 rows(plan['coefficients']),digest(rows(plan['current']))])
        else:
            assert plan['status']=='unresolved'
            other_A.append([b,plan['next_a'],plan['next_d'],plan['actual_rank_status']])
    assert old_local_success_original_failure is not None and other_A
    assert len(demo_seeds)==2
    demonstrations=[demo(M.native_plan(905))]+[demo(M.d6_forward_plan(b)) for b in demo_seeds]

    rejections=[lambda:M.parameters(True),lambda:M.parameters(9),lambda:M.parameters(-7287),
        lambda:M.d6_parameters(905),lambda:M.d6_parameters(58249),
        lambda:M.inverse_pair_plan(demo_seeds[0],True),
        lambda:M.native_cell(3),lambda:M.native_cell(4,-1),lambda:M.native_cell(True),
        lambda:M.d6_A2_cell(1),lambda:M.d6_A2_cell(2,True),
        lambda:M.substitute(M.native_plan(905),M.BASIS.returning_conversion(21))]
    for action in rejections:reject(action)
    bad=M.native_plan(905);bad=dict(bad,current={**bad['current'],3:True})
    reject(lambda:M.BASIS.check_boundary(bad))
    return dict(status='PASS',scope='Conditional native-W9 composition; universal supply remains open',
                caps=dict(supplied_arrows=10000,supplied_bits=4096),sources=sources(),
                contraction_cases=len(contraction),contraction_hash=digest(contraction),
                affine_checks=affine_checks(),native_cases=len(native),native_hash=digest(native),
                native_branches=sorted(branches),inverse_cases=len(inverses),inverse_hash=digest(inverses),
                next_A2_cases=len(forward_rows),next_A2_hash=digest(forward_rows),
                other_A_unresolved=other_A,old_local_success_original_failure=old_local_success_original_failure,
                supplied_demonstrations=demonstrations,general_rejections=len(rejections)+1)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true')
    args=parser.parse_args();receipt=HERE/'native_nine_audit.json';result=audit()
    if args.write:
        receipt.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else:
        assert json.loads(receipt.read_text())==json.loads(json.dumps(result))
    print('PASS: native W9; %d native cases; %d two-ray undos; %d complete next-A2 cases; %d supplied conversions' %
          (result['native_cases'],result['inverse_cases'],result['next_A2_cases'],len(result['supplied_demonstrations'])))


if __name__=='__main__':main()
