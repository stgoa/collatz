"""Exact later-target witness using R83's existing complete ray cutoff."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import sys
from types import ModuleType

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = spec_from_file_location('later_phi', HERE.parent/'phi_exit_control/phi_exit_control.py')
F = module_from_spec(spec)
spec.loader.exec_module(F)
B, N = F.R.B, F.R.B.NORMAL
spec = spec_from_file_location('later_dispatch', HERE.parent/'resolved_rules/resolved_rules.py')
DISPATCH = module_from_spec(spec)
spec.loader.exec_module(DISPATCH)


def rows(values):
    return [[x, c] for x, c in sorted(values.items())]


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def clean(values):
    return {x: c for x, c in values.items() if x != 1 and c}


def combine(*terms):
    answer = Counter()
    for coefficient, values in terms:
        for x, c in values.items():
            answer[x] += coefficient*c
    return clean(answer)


def v(n, prime):
    assert type(n) is int and n > 0
    answer = 0
    while n % prime == 0:
        answer += 1
        n //= prime
    return answer


def step(x):
    assert type(x) is int and x > 0 and x % 2
    return 1 if x == 1 else (3*x+1)//2**v(3*x+1, 2)


def prefix(x, count):
    current, word = Counter(), []
    for _ in range(count):
        assert x > 1
        word.append(v(3*x+1, 2))
        current[x] += 1
        x = step(x)
    return x, clean(current), word


def divergence(current):
    answer = Counter()
    for x, c in current.items():
        assert type(x) is int and x > 1 and x % 2
        assert type(c) is int and c
        answer[x] += c
        answer[step(x)] -= c
    return clean(answer)


def cutoffs(y, q):
    """R83's finite necessary cutoffs, valid for any canonical target y>1."""
    if type(y) is not int or y <= 1 or y % 2 != 1 or not N.canonical(y):
        raise ValueError('Require a positive nonabsorbing canonical target')
    if type(q) is not int or q < 3 or q % 2 != 1:
        raise ValueError('Require an odd original threshold at least3')
    j = (q-1).bit_length()-2
    pmax = (3**j*(q-1))//2**j
    bases = {0: ((8*y+3)//3, (16*y+3)//3),
             1: ((4*y-1)//3, (32*y+19)//3),
             2: ((64*y+19)//3, (128*y+83)//3)}[y % 3]
    result = []
    for base in bases:
        assert base % 8 == 1 and N.canonical(base)
        ratio = (9*pmax-2)//(9*base+7) if j >= 1 else 0
        index, power = 0, 1
        while power <= ratio:
            index += 1
            power *= 64
        result.append(dict(base=base, ratio=ratio, last_index=index-1,
                           first_excluded_power=power))
    return dict(point_bound=j, lifted_bound=pmax, rays=result)


def inspect_plan(b, q, comparison, p):
    hp, hb = B.absorption_plan(p), B.absorption_plan(b)
    assert all(B.rho(u) < q for u in hb['coefficients'])
    current = combine((1, comparison), (1, hp['current']), (-1, hb['current']))
    coefficients = combine((1, hp['coefficients']), (-1, hb['coefficients']))
    expected = Counter({3*b: 1, b: -1})
    for u, c in coefficients.items():
        expected[3*u] -= c
        expected[u] += c
    assert divergence(current) == clean(expected)
    high = {u: c for u, c in coefficients.items() if B.rho(u) >= q}
    assert all(c > 0 for c in high.values())
    return current, coefficients, dict(origin=p, current_rows=len(current),
        current_sha256=digest(rows(current)), requests=rows(coefficients),
        high=[[u, c, B.rho(u)] for u, c in sorted(high.items())],
        accepted=not high)


def source_hashes():
    pending, seen = [F, DISPATCH], set()
    files = {Path(__file__).resolve(), HERE/'LATER_TARGET_PROBE.md',
             HERE.parent/'native_growth_escape/NATIVE_GROWTH_ESCAPE.md'}
    while pending:
        module = pending.pop()
        if id(module) in seen:
            continue
        seen.add(id(module))
        filename = getattr(module, '__file__', None)
        if filename is None:
            continue
        path = Path(filename).resolve()
        if not path.is_relative_to(ROOT):
            continue
        files.add(path)
        pending.extend(value for value in vars(module).values() if isinstance(value, ModuleType))
    return {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(files)}


def unhandled_control():
    data = F.exit_parameters(4, 18, 3, 0)
    q, b = data['Q'], data['Q']//3
    y, upper, word = prefix(q, data['total_length'])
    normalizer = N.bridge(y)
    z = normalizer['minimum']
    assert q == 10700808724915244204246595675625106715
    assert y == 33053313160223488220607297455181106259
    assert z == 16526656580111744110303648727590553129
    assert len(word) == 78 and sum(word) == 122
    assert v(F.D*data['v']+F.B, 2) == 94
    assert v(F.D*data['exit_v']+F.B, 2) == 18
    assert F.maximum_reentries(data['v']) == 4
    assert divergence(normalizer['current']) == clean(Counter({y: 1, z: -1}))
    comparison = combine((1, upper), (1, normalizer['current']))
    assert divergence(comparison) == clean(Counter({q: 1, z: -1}))
    bc, ba, baseline = inspect_plan(b, q, comparison, z)
    original = F.exit_comparison(4, 18, 3)
    assert (bc, ba) == (original['current'], original['coefficients'])
    assert len(baseline['high']) == 1
    lead, coefficient, rank = baseline['high'][0]
    assert coefficient == 1 and lead % 8 == 5
    assert DISPATCH.one_step(lead) is None
    point = (2*z-1)//3
    assert v(z+1, 3) == 1 and point > q
    assert N.canonical(point) and step(point) == z
    pc, pa, direct = inspect_plan(b, q, combine((1, comparison), (-1, {point: 1})), point)
    assert direct['high'] and not direct['accepted']
    assert any(rr == point and c == 1 for _, c, rr in direct['high'])
    bounds = cutoffs(z, q)
    assert [item['last_index'] for item in bounds['rays']] == [11, 10]
    records, shorter = [], 0
    for ray, bound in enumerate(bounds['rays']):
        for index in range(bound['last_index']+1):
            a = (64**index*(9*bound['base']+7)-7)//9
            assert a+1 <= bounds['lifted_bound']
            bridge = N.quotient_bridge(a)
            assert bridge['minimum'] == z
            assert divergence(bridge['current']) == clean(Counter({a: 1, z: -1}))
            h = v(a+1, 3)
            p = 2**h*((a+1)//3**h)-1
            end, path, ones = prefix(p, h)
            assert N.canonical(p) and end == a and ones == [1]*h
            comp = combine((1, comparison), (-1, path), (-1, bridge['current']))
            current, coefficients, result = inspect_plan(b, q, comp, p)
            assert p > q and not result['accepted']
            if h:
                assert any(rr == p and c == 1 for _, c, rr in result['high'])
            else:
                assert (current, coefficients) == (bc, ba)
            for length in range(1, h):
                partial = 2**length*((a+1)//3**length)-1
                endpoint, pp, pw = prefix(partial, length)
                assert endpoint == a and pw == [1]*length
                cc, ca, _ = inspect_plan(b, q, combine((1, comparison), (-1, pp),
                                                       (-1, bridge['current'])), partial)
                assert (cc, ca) == (current, coefficients)
                shorter += 1
            records.append(dict(ray=ray, index=index, lifted=a, point_depth=h,
                normalized_origin=p, gap=p-q, plan=result))
        excluded = (bound['first_excluded_power']*(9*bound['base']+7)-7)//9
        assert excluded+1 > bounds['lifted_bound']
    assert len(records) == 23
    return dict(parameters=data, raw_target=y, canonical_target=z,
        ordinary_clock_to_raw_target=78, upper_word=word,
        normalizer_current=rows(normalizer['current']),
        comparison_sha256=digest(rows(comparison)), baseline=baseline,
        direct_point=direct, cutoffs=bounds, rays=records, ray_count=len(records),
        shorter_stops=shorter, fixed_seventeen_dispatcher_rule=None,
        scope='Native and one-ray/point failures; sole native W5 leader is unhandled by the fixed seventeen-family dispatcher. Further comparisons remain open.')


def audit():
    assert not sys.flags.optimize, 'Run without Python optimization'
    data = F.exit_parameters(8, 18, 3, 0)
    q, b = data['Q'], data['Q']//3
    y, upper, word = prefix(q, data['total_length'])
    assert q == 210065029006409577911756714191833302426696026205209908227355
    assert y == 685003375529270486518611195608212623248313116517585840060299
    assert len(word) == 126 and sum(word) == 198 and N.canonical(y)
    assert y > q and y == F.raw_test(data)['target']
    assert v(F.D*data['v']+F.B, 2) == 170
    assert v(F.D*data['exit_v']+F.B, 2) == 18
    assert F.maximum_reentries(data['v']) == 8
    base_current, base_coefficients, baseline = inspect_plan(b, q, upper, y)
    lead = 304445944679675771786049420270316721443694718452260373360133
    point = (2*y-1)//3
    assert baseline['high'] == [[lead, 1, point]] and point > q
    repair = DISPATCH.one_step(lead)
    assert repair['rule'] == 'R44_returning_forward'
    assert len(repair['coefficients']) == 26
    assert all(B.rho(u) < q for u in repair['coefficients'])
    repaired_current = combine((1, base_current), (1, repair['current']))
    repaired_coefficients = combine((1, base_coefficients), (-1, {lead: 1}),
                                    (1, repair['coefficients']))
    assert all(B.rho(u) < q for u in repaired_coefficients)
    expected = Counter({3*b: 1, b: -1})
    for u, c in repaired_coefficients.items():
        expected[3*u] -= c
        expected[u] += c
    assert divergence(repaired_current) == clean(expected)
    repaired = dict(rule=repair['rule'], expanded=lead, child_requests=rows(repair['coefficients']),
        requests=rows(repaired_coefficients), high=[],
        current_rows=len(repaired_current), current_sha256=digest(rows(repaired_current)),
        scope='Existing R44 original-rank repair; terminal inputs remain conditional.')
    assert N.canonical(point) and step(point) == y and v(point+1, 3) == 0
    pc, pa, point_record = inspect_plan(b, q, combine((1, upper), (-1, {point: 1})), point)
    assert (pc, pa) == (base_current, base_coefficients)

    bounds = cutoffs(y, q)
    assert bounds['point_bound'] == 196
    assert [row['last_index'] for row in bounds['rays']] == [18, 17]
    records, shorter_stops = [], 0
    for ray, bound in enumerate(bounds['rays']):
        for index in range(bound['last_index']+1):
            a = (64**index*(9*bound['base']+7)-7)//9
            assert a+1 <= bounds['lifted_bound']
            bridge = N.quotient_bridge(a)
            assert bridge['minimum'] == y
            assert divergence(bridge['current']) == clean(Counter({a: 1, y: -1}))
            h = v(a+1, 3)
            p = 2**h*((a+1)//3**h)-1
            assert N.canonical(p) and p > q
            end, path, ones = prefix(p, h)
            assert end == a and ones == [1]*h
            comparison = combine((1, upper), (-1, path), (-1, bridge['current']))
            current, coefficients, result = inspect_plan(b, q, comparison, p)
            if h:
                assert p % 4 == 3 and p % 3 != 2
                assert any(rank == p and c == 1 for _, c, rank in result['high'])
            else:
                assert (current, coefficients) == (base_current, base_coefficients)
            assert not result['accepted']
            for length in range(1, h):
                partial = 2**length*((a+1)//3**length)-1
                endpoint, partial_path, partial_word = prefix(partial, length)
                assert endpoint == a and partial_word == [1]*length
                comp = combine((1, upper), (-1, partial_path), (-1, bridge['current']))
                cc, ca, _ = inspect_plan(b, q, comp, partial)
                assert (cc, ca) == (current, coefficients)
                shorter_stops += 1
            records.append(dict(ray=ray, index=index, lifted=a, point_depth=h,
                normalized_origin=p, gap=p-q, plan=result))
        excluded = (bound['first_excluded_power']*(9*bound['base']+7)-7)//9
        assert excluded+1 > bounds['lifted_bound']
    assert len(records) == 37 and shorter_stops == 5
    assert sum(row['point_depth'] == 0 for row in records) == 25
    assert min(row['gap'] for row in records) == 12779628610659756684959685217341680145837611961091232688471660

    # General target controls check all three inverse-table residue cases.
    controls = []
    for target in (7, 9, 11, 27, 39, 43):
        assert N.canonical(target)
        for threshold in (3, 101):
            bound = cutoffs(target, threshold)
            for rb in bound['rays']:
                a = rb['base']
                for index in range(rb['last_index']+2):
                    assert N.quotient_step(a) == target
                    assert (a+1 <= bound['lifted_bound']) == (index <= rb['last_index'])
                    a = 64*a+49
            controls.append(dict(target=target, threshold=threshold, bounds=bound))
    invalid = [(True, q), (1, q), (5, q), (y, True), (y, 2), (y, 4)]
    for target, threshold in invalid:
        try:
            cutoffs(target, threshold)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid domain accepted')
    return dict(status='PASS', scope='Native absorption and one complete canonical inverse ray followed by points at the specified r4/r8 later targets; r8 has an existing R44 repair, and no other currents are excluded.',
        parameters=data, target=y, ordinary_clock=126, upper_word=word,
        upper_current_sha256=digest(rows(upper)), baseline=baseline,
        direct_point=point_record, existing_dispatcher_repair=repaired,
        cutoffs=bounds, rays=records,
        ray_count=len(records), shorter_stops=shorter_stops,
        general_target_controls=controls, invalid_rejections=len(invalid),
        unhandled_r4=unhandled_control(),
        source_sha256=source_hashes())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = audit()
    receipt = HERE/'later_target_probe_audit.json'
    if args.write:
        receipt.write_text(json.dumps(result, sort_keys=True, indent=2)+'\n')
    else:
        assert result == json.loads(receipt.read_text()), 'Receipt mismatch'
    print('PASS later-target probe: r4', result['unhandled_r4']['ray_count'],
          'complete ray candidates, fixed17 unhandled; r8', result['ray_count'],
          'ray candidates, repaired by existing R44')


if __name__ == '__main__':
    main()
