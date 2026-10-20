"""Replay the complete original-rank transition and finite supplied currents."""
import argparse
from collections import Counter
import hashlib
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import sys
from types import ModuleType
import history_transition as M

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = spec_from_file_location('transition_second', HERE.parent/'returning_continuation/returning_continuation.py')
SECOND = module_from_spec(spec)
spec.loader.exec_module(SECOND)
ARROW_CAP, BIT_CAP = 10000, 1024


def rows(current):
    return [[x, c] for x, c in sorted(current.items())]


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def step(x):
    value = 3*x+1
    return value//(value & -value)


def div(current):
    answer = Counter()
    for x, c in current.items():
        assert type(x) is int and x > 1 and x % 2 and type(c) is int and c
        answer[x] += c
        if step(x) != 1:
            answer[step(x)] -= c
    return {x: c for x, c in answer.items() if c}


def expected(plan):
    out = Counter({3*plan['seed']: 1, plan['seed']: -1})
    for v, c in plan['coefficients'].items():
        out[3*v] -= c
        out[v] += c
    return {x: c for x, c in out.items() if x != 1 and c}


def check(k):
    data = M.plan(k)
    assert div(data['current']) == expected(data)
    high, low = M.B.absorption_plan(data['raw']), M.B.absorption_plan(data['seed'])
    direct_current = M.combine((1, data['prefix']['current']),
                               (1, high['current']), (-1, low['current']))
    direct_coeff = M.combine((1, high['coefficients']), (-1, low['coefficients']))
    assert data['current'] == direct_current and data['coefficients'] == direct_coeff
    actual = all(M.B.rho(v) < data['rank'] for v in direct_coeff)
    assert actual == (data['status'] == 'descending')
    phase = M.initial_row(k)
    if phase['accepted'] is not None:
        assert phase['accepted'] == actual
    x = data['rank']
    for _ in range(data['quotient_length']):
        x = M.N.quotient_step(x)
    assert x == data['terminal']
    left, right = data['rank'], data['terminal']
    lrows, rrows = Counter(), Counter()
    for _ in range(data['ordinary_clocks'][0]):
        if left != 1:
            lrows[left] += 1
        left = step(left)
    for _ in range(data['ordinary_clocks'][1]):
        if right != 1:
            rrows[right] += 1
        right = step(right)
    assert left == right == data['ordinary_meeting']
    assert M.combine((1, lrows), (-1, rrows)) == data['comparison']
    return data


def template_index(word, index):
    """Solve all exact binary guards independently, including final A guard."""
    a, c, exponent = 1, 0, 0
    residue, modulus = 1, 2
    rules = {'A': (1, 3, 1, 2), 'B': (3, 4, -1, 3), 'C': (5, 5, 1, 4)}
    for position, letter in enumerate(word+'A'):
        target, bits, sign, power = rules[letter]
        new_modulus = 2**(exponent+bits)
        new_residue = ((target*2**exponent-c)*pow(a, -1, new_modulus)) % new_modulus
        assert new_residue % modulus == residue
        residue, modulus = new_residue, new_modulus
        if position < len(word):
            a, c, exponent = 3*a, 3*c+sign*2**exponent, exponent+power
    period = modulus//2
    k = (((residue-70237)//2)*pow(3**14, -1, period)) % period
    return k+period*index


def absorption(x):
    current = {}
    while x != 1:
        if len(current) >= ARROW_CAP or x.bit_length() > BIT_CAP or x in current:
            raise RuntimeError('Designated finite input supply exceeded its caps')
        current[x] = 1
        x = step(x)
    return current


def pair_supply(w):
    current = M.combine((1, absorption(3*w)), (-1, absorption(w)))
    assert div(current) == {3*w: 1, w: -1}
    return current


def reject(call):
    try:
        call()
    except ValueError:
        return
    raise AssertionError('Expected rejection')


def sources():
    pending, seen = [M, SECOND], set()
    files = {Path(__file__).resolve(), HERE/'HISTORY_TRANSITION.md'}
    while pending:
        module = pending.pop()
        if id(module) in seen:
            continue
        seen.add(id(module))
        filename = getattr(module, '__file__', None)
        if not filename:
            continue
        path = Path(filename).resolve()
        if not path.is_relative_to(ROOT):
            continue
        files.add(path)
        pending.extend(value for value in vars(module).values() if isinstance(value, ModuleType))
    return {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(files)}


def audit(stored=None):
    cases = []
    for k in range(1024):
        data = check(k)
        cases.append([k, data['status'], data['word'], data['terminal'],
                      data['ordinary_clocks'], digest(rows(data['current'])),
                      rows(data['coefficients'])])
    assert len(M.TEMPLATES) == len(set(M.TEMPLATES)) == 14
    templates = []
    for word in M.TEMPLATES:
        for index in (0, 1, 2, 17, 2**64):
            k = template_index(word, index)
            data = check(k)
            assert data['word'].startswith(word)
            x = data['raw']
            for letter in word:
                x = M.transition(x, letter)['target']
            assert x % 8 == 1 and x > data['rank']
            templates.append([word, index, k, data['word'], data['status']])

    progressions = []
    for index in list(range(32))+[2**32, 2**64, 2**128, 2**256]:
        for residue, modulus, accepted in ((12, 16, True), (20, 32, True),
                                           (1, 4, False), (7, 8, False)):
            k = residue+modulus*index
            data = check(k)
            assert (data['status'] == 'descending') == accepted
            progressions.append([k, data['word'], data['status']])

    sharp = []
    for index in list(range(16))+[2**32, 2**64, 2**128, 2**256]:
        data = M.sharp_family(index)
        checked = check(data['k'])
        assert checked['word'] == 'A'*7 and checked['quotient_length'] == 20
        sharp.append([index, data['k'], checked['ordinary_clocks'], checked['terminal']])

    old = []
    for k in list(range(64))+[2**64+12, 2**128+20]:
        data = M.old_failure(k)
        a, b = SECOND.OLD.forward_plan(data['returning']), SECOND.continuation_plan(data['returning'])
        for plan in (a, b):
            assert plan['coefficients'][data['leading']] == 1
            assert div(plan['current']) == expected(plan)
        old.append([k, data['leading'], len(a['current']), len(b['current'])])

    demonstrations = []
    for i, k in enumerate((12, 20, 9954)):
        data = check(k)
        assert k % 3**11 and data['status'] == 'descending'
        if stored is None:
            supplied = {v: pair_supply(v) for v in data['coefficients']}
        else:
            supplied = {int(v): dict(table) for v, table in stored['demonstrations'][i]['supplied'].items()}
        assert set(supplied) == set(data['coefficients'])
        for v, table in supplied.items():
            assert div(table) == {3*v: 1, v: -1}
        compiled = M.compile_plan(data, supplied)
        assert div(compiled) == {3*data['seed']: 1, data['seed']: -1}
        reject(lambda: M.compile_plan(data, {}))
        reject(lambda: M.compile_plan(data, {**supplied, next(iter(supplied)): {}}))
        reject(lambda: M.compile_plan(data, {**supplied, next(iter(supplied)): {3: True}}))
        demonstrations.append(dict(k=k, seed=data['seed'], word=data['word'],
                                   quotient_length=data['quotient_length'],
                                   ordinary_clocks=data['ordinary_clocks'],
                                   plan_current=rows(data['current']),
                                   coefficients=rows(data['coefficients']),
                                   supplied={str(v): rows(table) for v, table in sorted(supplied.items())},
                                   output=rows(compiled), output_rows=len(compiled)))

    failed = check(1)
    invalid = [lambda: M.parameters(-1), lambda: M.parameters(True),
               lambda: M.parameters(1.0), lambda: M.prefix(True, 1),
               lambda: M.prefix(2, 1), lambda: M.prefix(3, -1),
               lambda: M.prefix(3, 1, [2]), lambda: M.prefix(3, 1, [1, 2]),
               lambda: M.transition(7, 'A'), lambda: M.transition(13, 'B'),
               lambda: M.transition(7, 'C'), lambda: M.transition(True, 'A'),
               lambda: M.transition(25, 'D'), lambda: M.sharp_family(-1),
               lambda: M.sharp_family(True), lambda: M.compile_plan(failed, {}),
               lambda: M.compile_plan(dict(M.plan(12), current={3: True}), {})]
    for call in invalid:
        reject(call)
    return dict(schema=1, status='PASS', scope='Complete fixed comparison only; all terminal inputs retained.',
                full_cases=len(cases), full_hash=digest(cases),
                template_cases=templates, progression_cases=len(progressions),
                progression_hash=digest(progressions), sharp_cases=sharp,
                old_failure_cases=old,
                unresolved_fixture=dict(k=1, seed=failed['seed'], terminal=failed['terminal'],
                                        leading=failed['leading'], current=rows(failed['current']),
                                        coefficients=rows(failed['coefficients'])),
                demonstrations=demonstrations, rejections=len(invalid)+9,
                supply_caps=dict(ordinary_arrows=ARROW_CAP, state_bits=BIT_CAP),
                source_hashes=sources())


def main():
    assert not sys.flags.optimize, 'Run without -O'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    path = HERE/'history_transition_audit.json'
    stored = None if args.write_receipt else json.loads(path.read_text())
    data = audit(stored)
    serialized = json.dumps(data, indent=2, sort_keys=True)+'\n'
    if args.write_receipt:
        path.write_text(serialized)
    else:
        assert json.loads(serialized) == stored, 'Receipt mismatch; investigate before refreshing'
    print('PASS: history transition; '+json.dumps(dict(
        full_cases=data['full_cases'], template_cases=len(data['template_cases']),
        progressions=data['progression_cases'], sharp_cases=len(data['sharp_cases']),
        old_failure_cases=len(data['old_failure_cases']),
        supplied_rows=[d['output_rows'] for d in data['demonstrations']],
        rejections=data['rejections']), sort_keys=True))


if __name__ == '__main__':
    main()
