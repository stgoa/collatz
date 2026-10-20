"""Exact bounded replay of the enlarged critical-basis compilation theorem."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from types import ModuleType
import critical_basis as M

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def rows(data):
    return [[x, c] for x, c in sorted(data.items())]


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def direct_divergence(current):
    result = Counter()
    for x, c in current.items():
        assert isinstance(x, int) and x > 1 and x % 2
        y = 3*x+1
        y //= y & -y
        result[x] += c
        if y != 1:
            result[y] -= c
    return {x: c for x, c in result.items() if c}


def check(data):
    source = {3*data['seed']: 1, data['seed']: -1}
    for u, c in data['coefficients'].items():
        source = M.combine((1, source), (-c, {3*u: 1, u: -1}))
    assert direct_divergence(data['current']) == source


def expect_error(action, error=ValueError):
    try:
        action()
    except error:
        return
    raise AssertionError('Expected rejection')


def finite_pair(w):
    def absorption(x):
        current = {}
        while x != 1:
            if x in current or len(current) >= 10000 or x.bit_length() > 4096:
                raise RuntimeError('Designated finite input exceeded supplied-path caps')
            current[x] = 1
            y = 3*x+1
            x = y//(y & -y)
        return current
    result = M.combine((1, absorption(3*w)), (-1, absorption(w)))
    assert direct_divergence(result) == {3*w: 1, w: -1}
    return result


def supplied_demo(data):
    supplied = {u: finite_pair(u) for u in data['coefficients']}
    current = M.compile_plan(data, supplied)
    assert direct_divergence(current) == {3*data['seed']: 1, data['seed']: -1}
    expect_error(lambda: M.compile_plan(data, {}))
    wrong = dict(supplied)
    wrong[next(iter(wrong))] = {}
    expect_error(lambda: M.compile_plan(data, wrong))
    return dict(seed=data['seed'], rank=M.rho(data['seed']),
                plan_current=rows(data['current']), coefficients=rows(data['coefficients']),
                supplied={str(w): rows(c) for w, c in sorted(supplied.items())},
                current=rows(current), current_rows=len(current), current_hash=digest(rows(current)))


def source_hashes():
    pending, seen, paths = [M], set(), {Path(__file__).resolve()}
    while pending:
        module = pending.pop()
        if id(module) in seen:
            continue
        seen.add(id(module))
        name = getattr(module, '__file__', None)
        if not name:
            continue
        path = Path(name).resolve()
        if not path.is_relative_to(ROOT):
            continue
        paths.add(path)
        pending.extend(x for x in vars(module).values() if isinstance(x, ModuleType))
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}


def audit():
    absorption = []
    for seed in range(1, 1024, 2):
        data = M.absorption_plan(seed)
        expected = {} if seed == 1 else {seed: 1}
        for w, c in data['coefficients'].items():
            expected = M.combine((1, expected), (-c, {3*w: 1, w: -1}))
        assert direct_divergence(data['current']) == expected
        assert all(M.rho(w) <= M.NORMAL.normal_form(seed) for w in data['coefficients'])
        absorption.append([seed, rows(data['coefficients']), digest(rows(data['current']))])

    returning, old_rho = [], []
    index = 0
    while len(returning) < 256:
        u = 21+72*index
        index += 1
        if not M.SIGMA.RETURN.returning(u):
            continue
        data = M.returning_conversion(u)
        check(data)
        b = data['leading']
        assert M.rho(b) == M.SIGMA.sigma(u) < M.rho(u)
        assert all(M.rho(v) < M.rho(b) for v in data['coefficients'] if v != b)
        undo = M.blocked_nine(u)
        check(undo)
        expect_error(lambda: M.validate(undo))
        returning.append(dict(seed=u, leading=b, native_height=data['native_height'],
                              coefficients=rows(data['coefficients']), current_hash=digest(rows(data['current'])),
                              undo_coefficients=rows(undo['coefficients']),
                              undo_current_hash=digest(rows(undo['current']))))
        candidate = M.SIGMA.RETURN.forward_plan(u)
        if candidate['status'] == 'descending' and len(old_rho) < 32:
            retained = M.retain_rho(candidate)
            assert retained['current'] == candidate['current']
            assert retained['coefficients'] == candidate['coefficients']
            check(retained)
            old_rho.append([u, rows(retained['coefficients']), digest(rows(retained['current']))])

    nines, branches = [], set()
    for b in range(9, 8192, 16):
        data = M.nine_candidate(b)
        check(data)
        expected = {data['exception']: 1} if data['d'] == 4 and data['exception'] else {}
        assert data['high'] == expected
        if expected:
            expect_error(lambda: M.validate(data))
        else:
            M.validate(data)
        branches.add((data['d'], data['branch']))
        nines.append([b, data['d'], data['branch'], rows(data['coefficients']), rows(data['high'])])

    sigma = []
    for w in range(5, 2053, 8):
        data = M.SIGMA.one_step(w)
        if data is None:
            continue
        imported = M.translate_sigma(data)
        check(imported)
        assert all(M.rho(u) < M.SIGMA.sigma(w) for u in imported['coefficients'])
        sigma.append(dict(seed=w, original=rows(data['coefficients']),
                          coefficients=rows(imported['coefficients']), converted=imported['converted'],
                          current_hash=digest(rows(imported['current']))))

    guarded = []
    for count in (1, 2, 4, 8):
        modulus = 2**(26+19*(count-1))
        residue = -311195*pow(7153, -1, modulus) % modulus
        for index in (0, 1):
            w = residue+index*modulus
            data = M.guarded_plan(w)
            check(data)
            imported = M.translate_sigma(M.SIGMA.forward_plan(w))
            check(imported)
            b, f = data['leading'], data['endpoint']
            assert imported['coefficients'][b] == 1
            assert all(M.rho(v) < f for v in imported['coefficients'] if v != b)
            q = 3*w
            for _ in range(6):
                q = M.NORMAL.step(q)
            assert q == M.NORMAL.step(f)
            q = 3*w
            for _ in range(5):
                q = M.NORMAL.quotient_step(q)
            assert q == f
            blocked = M.nine_candidate(b)
            assert blocked['high'] == {data['avoided_returning']: 1}
            assert M.rho(data['avoided_returning']) > M.rho(w)
            guarded.append(dict(seed=w, binary_depth=26+19*(count-1), rank=M.rho(w),
                                leading=b, leading_rank=f, avoided=data['avoided_returning'],
                                avoided_rank=M.rho(data['avoided_returning']),
                                coefficients=rows(data['coefficients']),
                                direct_current_hash=digest(rows(data['current'])),
                                translated_coefficients=rows(imported['coefficients']),
                                translated_current_hash=digest(rows(imported['current']))))

    # A genuinely negative E request: its known finite currents are fixture
    # construction data, never an assumption in the universal translation.
    original = dict(seed=93, current=M.combine((1, finite_pair(93)), (3, finite_pair(21))),
                    coefficients={21: -3})
    M.SIGMA.validate(93, original)
    negative = M.translate_sigma(original)
    assert negative['coefficients'][9] == -3
    check(negative)

    incompatible = M.SIGMA.RETURN.forward_plan(4629)
    kept = M.retain_rho(incompatible)
    assert kept['coefficients'][2197] == 1
    expect_error(lambda: M.translate_sigma(incompatible))
    zero = M.blocked_nine(21)
    assert zero['current'] == {} and zero['coefficients'] == {9: 1}
    nonzero = M.blocked_nine(453)
    assert nonzero['coefficients'] == {5: 1, 25: 1, 201: 1}
    assert len(nonzero['current']) == 14

    seed = 40529845
    def choose(w):
        if w == seed:
            return M.guarded_plan(w)
        if w % 8 == 5 and M.SIGMA.RETURN.returning(w):
            return M.returning_conversion(w)
        if w % 16 == 9:
            candidate = M.nine_candidate(w)
            return candidate if candidate['status'] == 'descending' else None
        return None
    closed = M.close_plan(seed, choose)
    check(closed)
    assert closed['coefficients'][M.guarded_plan(seed)['leading']] == 1
    expect_error(lambda: M.close_plan(seed, choose, max_nodes=1), RuntimeError)
    expect_error(lambda: M.close_plan(seed, choose, max_nodes=True))
    expect_error(lambda: M.close_plan(9, lambda w: M.nine_candidate(w)))

    demos = [supplied_demo(M.returning_conversion(21)),
             supplied_demo(M.guarded_plan(seed)), supplied_demo(negative)]
    bad_current = dict(original, current=dict(original['current']))
    bad_current['current'][next(iter(bad_current['current']))] = True
    self_request = dict(seed=5, current={}, coefficients={5: 1})
    bool_supplied = {u: finite_pair(u) for u in negative['coefficients']}
    first = next(iter(bool_supplied))
    bool_supplied[first][next(iter(bool_supplied[first]))] = True
    invalid = [lambda: M.rho(1), lambda: M.rho(True), lambda: M.returning_conversion(5),
               lambda: M.translate_sigma(bad_current), lambda: M.validate(self_request),
               lambda: M.guarded_plan(21), lambda: M.compile_plan(negative, bool_supplied),
               lambda: M.close_plan(5, lambda w: dict(seed=13, current={}, coefficients={13: 1}))]
    for action in invalid:
        expect_error(action)
    return json.loads(json.dumps(dict(
        status='PASS', scope='Enlarged critical source basis; sigma plans translated; no new W5-only dispatcher coverage or universal supply',
        absorption_cases=len(absorption), absorption_hash=digest(absorption),
        returning_conversions=returning, old_rho_plans=old_rho,
        nine_cases=len(nines), nine_hash=digest(nines), nine_branches=sorted(branches),
        sigma_translations=sigma, whole_guard_plans=guarded,
        negative_translation=dict(original_current=rows(original['current']), original_requests=rows(original['coefficients']),
                                  current=rows(negative['current']), requests=rows(negative['coefficients'])),
        retained_rho_4629=dict(current=rows(kept['current']), coefficients=rows(kept['coefficients'])),
        nonzero_undo_counterexample=dict(seed=201, returning=453, current=rows(nonzero['current']),
                                         coefficients=rows(nonzero['coefficients'])),
        conditional_closure=dict(seed=seed, expanded=closed['expanded'], coefficients=rows(closed['coefficients']),
                                 current_hash=digest(rows(closed['current']))),
        supplied_demonstrations=demos,
        general_rejections=len(invalid)+4+2*len(demos),
        returning_self_rejections=len(returning), nine_expansion_rejections=sum(bool(x[-1]) for x in nines),
        caps=dict(supplied_arrows=10000, supplied_bits=4096), sources=source_hashes())))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = audit()
    path = HERE/'critical_basis_audit.json'
    if args.write:
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        assert json.loads(path.read_text()) == result
    print('PASS: critical-basis compiler; '
          f"{result['absorption_cases']} absorption plans; {len(result['returning_conversions'])} returning conversions; "
          f"{result['nine_cases']} W9 rows; {len(result['sigma_translations'])} sigma translations; "
          f"{len(result['old_rho_plans'])} unchanged rho plans; {len(result['whole_guard_plans'])} whole-guard cases; "
          f"{len(result['supplied_demonstrations'])} supplied conversions")
