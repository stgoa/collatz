"""Portable bounded exact audit; the universal finite-list argument is written."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from types import ModuleType
import finite_centres as F

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def rows(data):
    return [[x, c] for x, c in sorted(data.items())]


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def direct_divergence(current):
    out = Counter()
    for x, c in current.items():
        assert isinstance(x, int) and x > 1 and x % 2
        assert isinstance(c, int) and c
        y = 3*x+1
        y //= y & -y
        out[x] += c
        if y != 1:
            out[y] -= c
    return {x: c for x, c in out.items() if c}


def source(seed):
    return {3*seed: 1, seed: -1}


def iterate(seed, count, quotient=False):
    step = F.NORMAL.quotient_step if quotient else F.NORMAL.step
    for _ in range(count):
        seed = step(seed)
    return seed


def expect_error(action):
    try:
        action()
    except ValueError:
        return
    raise AssertionError('Expected rejection')


def supplied_absorption(seed):
    x, current = seed, {}
    while x != 1:
        if x in current or len(current) >= 10000 or x.bit_length() > 4096:
            raise RuntimeError('Designated finite supplied path unresolved within caps')
        current[x] = 1
        x = F.NORMAL.step(x)
    assert direct_divergence(current) == {seed: 1}
    return current


def supplied_demo(L, H):
    data = F.comparison(L, H)
    supplied = {u: F.RANK.combine((1, supplied_absorption(3*u)),
                                 (-1, supplied_absorption(u)))
                for u in data['coefficients']}
    for u, current in supplied.items():
        assert direct_divergence(current) == source(u)
    output = F.compile_plan(data, supplied)
    assert direct_divergence(output) == source(data['seed'])
    expect_error(lambda: F.compile_plan(data, {}))
    bad = dict(supplied)
    bad[next(iter(bad))] = {}
    expect_error(lambda: F.compile_plan(data, bad))
    return dict(L=L, H=H, seed=data['seed'], leading=data['leading'],
                supplied_pairs=len(supplied), output_rows=len(output),
                plan_current=rows(data['current']), coefficients=rows(data['coefficients']),
                supplied={str(u): rows(c) for u, c in sorted(supplied.items())},
                output=rows(output), output_hash=digest(rows(output)))


def audit():
    # Integer inequalities used for all positive members, including offsets.
    assert Fraction(8, 27)-Fraction(1, 3) == -Fraction(1, 27)
    assert Fraction(4, 9)-Fraction(1, 3)+Fraction(2**3, 3**4) < 1
    assert Fraction(36+11, 32) < 3
    assert 5587204 < 3**15 and 4 < 3**2 and Fraction(3, 2)**3 < 4

    arithmetic = []
    for L in range(1, 73, 3):
        for H in (26, 27, 64, 256):
            for index in (0, 2**32):
                f = F.family(L, H, index)
                assert f['seed'] == (2**f['a']*f['t']-1)//3
                assert f['child'] % 2**(H+1) == f['binary_residue']
                assert f['child'] % 3**(f['a']+1) == f['ternary_residue']
                arithmetic.append(f)

    plans = []
    for L in (1, 4, 7, 10, 13, 16, 19, 22):
        for H in (26, 64, 128):
            for index in (0, 1):
                data = F.comparison(L, H, index)
                w, u, q, a, r = (data['seed'], data['leading'], data['rank'],
                                 data['family']['a'], data['family']['endpoint'])
                expected = Counter(source(w))
                for x, c in data['coefficients'].items():
                    expected[3*x] -= c
                    expected[x] += c
                expected = {x: c for x, c in expected.items() if c and x != 1}
                assert direct_divergence(data['current']) == expected
                x = q
                for valuation in [1]*(a-2)+[2]:
                    raw = 3*x+1
                    assert (raw & -raw).bit_length()-1 == valuation
                    x = raw >> valuation
                assert x == r
                assert iterate(q, a) == iterate(3*u, 1)
                assert iterate(3*w, a) == iterate(3*u, 1)
                assert iterate(q, a-1, True) == 3*u
                assert data['coefficients'][u] == 1
                assert all(F.RANK.rho(x) < 3*u for x in data['coefficients'] if x != u)
                plans.append(dict(family=data['family'], current_rows=len(data['current']),
                                  coefficients=rows(data['coefficients']),
                                  current_hash=digest(rows(data['current'])),
                                  helper_rank=max((F.RANK.rho(x) for x in data['coefficients']
                                                   if x != u), default=0),
                                  ordinary_clocks=[a, 1], quotient_length=a-1))

    centres = []
    for L in range(4, 4+9*24, 9):
        p = F.parameters(L)
        assert p['centre_denominator_order'] == p['a']-1
        centres.append(dict(L=L, a=p['a'], centre=[p['centre'].numerator, p['centre'].denominator],
                            denominator_order=p['centre_denominator_order']))
    assert all(x['a'] < y['a'] for x, y in zip(centres, centres[1:]))
    assert len({tuple(x['centre']) for x in centres}) == len(centres)

    # A finite-list illustration of the universal pole argument.  The proof
    # handles arbitrary finite lists and real weights; these are exact examples.
    w_centres = [F.THETA, Fraction(-1), Fraction(-5), Fraction(-17)]
    e_centres = [Fraction(-F.DEBT.B_E, F.D)]
    e_centres += [F.parameters(L)['centre'] for L in (4, 13, 22)]
    new_L = 31
    assert F.parameters(new_L)['centre'] not in e_centres
    poles = []
    for H in (512, 768, 1024):
        f = F.family(new_L, H)
        child_orders = [F.affine_order(c, f['child']) for c in w_centres]
        parent_orders = [F.affine_order(c, f['seed']) for c in e_centres]
        assert child_orders[0] == H
        # Representative equal height powers and arbitrary signed weights.
        weight_child = child_orders[0]-3*child_orders[1]+2*child_orders[2]-child_orders[3]
        weight_parent = sum(parent_orders)
        ratio = Fraction(f['child']+7, 2*f['seed']+1)**2*Fraction(2)**(weight_child-weight_parent)
        assert ratio > 1
        poles.append(dict(H=H, seed=f['seed'], child=f['child'], child_orders=child_orders,
                          parent_orders=parent_orders, log2_valuation_difference=weight_child-weight_parent,
                          ratio=[ratio.numerator, ratio.denominator]))
    assert all(x['parent_orders'] == poles[0]['parent_orders'] for x in poles)
    assert all(x['child_orders'][1:] == poles[0]['child_orders'][1:] for x in poles)
    assert all(x['log2_valuation_difference']-x['H'] ==
               poles[0]['log2_valuation_difference']-poles[0]['H'] for x in poles)

    # The arbitrary-list necessity proof fixes a sufficiently deep exact H,
    # then varies ordinary height.  These checks preserve both operations.
    mixed = []
    for H, index in ((128, 0), (128, 2**64), (192, 0), (256, 0)):
        modulus = 2**(H+1)
        w = (2**H-F.B)*pow(F.D, -1, modulus) % modulus+modulus*index
        data = F.DEBT.MIXED.parameters(w)
        u, v = data['intermediate'], data['child']
        assert (F.DEBT.phase(w), F.DEBT.phase(u), F.DEBT.phase(v)) == ('W', 'E', 'W')
        orders_w = [F.affine_order(c, w) for c in w_centres]
        orders_v = [F.affine_order(c, v) for c in w_centres]
        orders_e = [F.affine_order(c, u) for c in e_centres]
        assert orders_w[0]-orders_v[0] == 19
        assert orders_w[1:] == orders_v[1:]
        assert orders_e[0] == H-10
        mixed.append(dict(H=H, index=index, input_orders=orders_w,
                          intermediate_orders=orders_e, output_orders=orders_v,
                          seed=w, intermediate=u, child=v))
    assert mixed[0]['input_orders'] == mixed[1]['input_orders']
    assert mixed[0]['intermediate_orders'] == mixed[1]['intermediate_orders']
    assert mixed[0]['output_orders'] == mixed[1]['output_orders']

    demos = [supplied_demo(1, 26), supplied_demo(4, 26)]
    invalid = [lambda: F.parameters(0), lambda: F.parameters(2),
               lambda: F.parameters(4.0), lambda: F.family(4, 25),
               lambda: F.family(4, 26, -1), lambda: F.family(4, 26.0),
               lambda: F.valuation3(0), lambda: F.affine_order(Fraction(5), 5)]
    for action in invalid:
        expect_error(action)
    # Dynamic exec_module imports need not enter sys.modules.  Follow module
    # objects themselves as well as normally registered imports, with cycles
    # guarded by object identity.  Store portable repository-relative paths.
    paths = {Path(__file__).resolve(), (HERE/'finite_centres.py').resolve()}
    pending = [F, *tuple(sys.modules.values())]
    seen = set()
    while pending:
        module = pending.pop()
        if not isinstance(module, ModuleType) or id(module) in seen:
            continue
        seen.add(id(module))
        name = getattr(module, '__file__', None)
        if name:
            path = Path(name).resolve()
            if path.suffix == '.py' and path.is_relative_to(ROOT/'experiments/residual_progress'):
                paths.add(path)
                pending.extend(x for x in vars(module).values() if isinstance(x, ModuleType))
    required = ['arithmetic_progress/valuation_debt.py', 'returning_phase/returning_phase.py',
                'mixed_rank_recursion/mixed_growth.py', 'critical_rank/rank_closure.py',
                'phase_rank/sigma_rank.py', 'critical_inverse/critical_inverse.py',
                'w9_closure/w9_closure.py', 'tripling_equivalence/tripling.py']
    assert all((HERE.parent/p).resolve() in paths for p in required)
    result = dict(status='PASS',
                  scope='Two fixed W/E phases and finite affine valuation lists with nonnegative affine-height powers; conditional currents only, no dispatcher or universal supply',
                  arithmetic_cases=len(arithmetic), arithmetic_hash=digest(arithmetic),
                  full_comparisons=plans, distinct_centres=centres,
                  finite_list_examples=poles, mixed_stabilization=mixed,
                  supplied_demonstrations=demos, rejections=len(invalid)+2*len(demos),
                  caps=dict(ordinary_arrow_limit=10000, supplied_bit_limit=4096,
                            largest_full_ray=22, largest_arithmetic_ray=70,
                            largest_centre_ray=211, largest_checked_order=1024),
                  source_hashes={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                                 for p in sorted(paths)})
    return json.loads(json.dumps(result))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = audit()
    receipt = HERE/'finite_centres_audit.json'
    if args.write:
        receipt.write_text(json.dumps(result, sort_keys=True, indent=2)+'\n')
    else:
        assert json.loads(receipt.read_text()) == result, 'Receipt differs; inspect before regenerating'
    print('PASS: finite affine-centre obstruction; '
          f"{result['arithmetic_cases']} CRT cases; {len(result['full_comparisons'])} full comparisons; "
          f"{len(result['distinct_centres'])} distinct poles; "
          f"{len(result['supplied_demonstrations'])} supplied conversions")
