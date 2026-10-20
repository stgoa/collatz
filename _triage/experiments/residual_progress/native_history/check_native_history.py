"""Bounded exact replay of the native high-history family, with stored supplies."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from types import ModuleType
import native_history as M

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OLD = M.load('history_old_seventeen', 'resolved_rules/resolved_rules.py')


def rows(data):
    return [[x, c] for x, c in sorted(data.items())]


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def direct_divergence(current):
    result = Counter()
    for x, c in current.items():
        assert isinstance(x, int) and not isinstance(x, bool) and x > 1 and x % 2
        assert isinstance(c, int) and not isinstance(c, bool) and c
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
    M.BASIS.validate(data)


def expect_error(action):
    try:
        action()
    except ValueError:
        return
    raise AssertionError('Expected rejection')


def finite_pair(w):
    """Fixture generation only; never called by default replay."""
    def absorption(x):
        current = {}
        while x != 1:
            if x in current or len(current) >= 10000 or x.bit_length() > 4096:
                raise RuntimeError('Designated fixture exceeded finite search caps')
            current[x] = 1
            y = 3*x+1
            x = y//(y & -y)
        return current
    answer = M.combine((1, absorption(3*w)), (-1, absorption(w)))
    assert direct_divergence(answer) == {3*w: 1, w: -1}
    return answer


def demo(plan, stored=None):
    supplied = ({u: finite_pair(u) for u in plan['coefficients']} if stored is None else
                {int(u): dict(c) for u, c in stored['supplied'].items()})
    assert set(supplied) == set(plan['coefficients'])
    for u, current in supplied.items():
        assert direct_divergence(current) == {3*u: 1, u: -1}
    current = M.compile_plan(plan, supplied)
    assert direct_divergence(current) == {3*plan['seed']: 1, plan['seed']: -1}
    expect_error(lambda: M.compile_plan(plan, {}))
    bad = dict(supplied)
    bad[next(iter(bad))] = {}
    expect_error(lambda: M.compile_plan(plan, bad))
    return dict(seed=plan['seed'], plan_current=rows(plan['current']),
                coefficients=rows(plan['coefficients']),
                supplied={str(u): rows(c) for u, c in sorted(supplied.items())},
                current=rows(current), current_rows=len(current), current_hash=digest(rows(current)))


def source_hashes():
    pending, seen = [M, OLD], set()
    paths = {Path(__file__).resolve(), HERE/'HIGH_HISTORY.md', HERE/'anchor_certificate.json'}
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


def inverse_words(depth):
    def visit(shadow, word):
        if len(word) == depth:
            yield word
            return
        for kind in M.INVERSE.BASES[shadow % 3]:
            next_shadow, _, _ = M.INVERSE.inverse_step(shadow, kind, 0)
            yield from visit(next_shadow, word+[(kind, 0)])
    return visit(M.ANCHOR, [])


def audit(stored=None):
    anchor = M.verify_anchor()
    assert anchor == dict(anchor=11547, states=4892, maximum=3012713, origins=2887)
    a, c, e = 1, 0, 0
    for v in M.WORD:
        a, c, e = 3*a, 3*c+2**e, e+v
    assert (a, c, e) == (3**13, 1779283, 16)
    assert len(M.BASE_PATH) == len(M.WORD)+1
    for j, x in enumerate(M.BASE_PATH[:-1]):
        assert M.NORMAL.canonical(x)
        assert M.NORMAL.valuation2(3*x+1) == M.WORD[j]
        if j:
            assert x > M.ANCHOR and 3**j*2**(19-sum(M.WORD[:j])) > 3**12

    cases, failures, five_frontiers = [], [], []
    for depth in (12, 13, 17, 32, 64, 129):
        for index in (*range(8), 2**64-1):
            params = M.family(depth, index)
            plan = M.history_plan(params['seed'])
            check(plan)
            data = plan['parameters']
            q, p = params['root'], params['lower']
            assert direct_divergence(plan['bridge']) == {q: 1, p: -1}
            for j, x in enumerate(data['lower_path']['states']):
                expected = M.BASE_PATH[j]+3**j*2**(36-sum(M.WORD[:j]))*3**(depth-12)*index
                assert x == expected
            assert max(data['lower_path']['states']) == 32*q+17
            # Independently expose the actual two ordinary prefixes.
            for seed, length in ((q, 2), (p, 14)):
                x = seed
                for _ in range(length):
                    z = 3*x+1
                    x = z//(z & -z)
                assert x == (9*q+5)//8 > q
            cases.append(dict(parameters=params, current_hash=digest(rows(plan['current'])),
                              coefficients=rows(plan['coefficients']),
                              max_rank=max(map(M.rho, plan['coefficients']), default=0)))
            failures.append(dict(seed=params['seed'], **M.old_endpoint_failures(params['seed'])))
            five = M.five_frontier_plan(params['seed'])
            check(five)
            five_frontiers.append(dict(seed=params['seed'], coefficients=rows(five['coefficients']),
                                       current_hash=digest(rows(five['current']))))

    words = []
    q = M.family(12, 1)['root']
    for length in range(1, 6):
        for word in inverse_words(length):
            result = M.shadow_word(q, word)
            words.append([word, digest(result)])
    varied = []
    for depth in (12, 17, 32):
        for mode in range(6):
            q, shadow, word = M.family(depth, mode+1)['root'], M.ANCHOR, []
            for j in range(depth):
                kinds = list(M.INVERSE.BASES[shadow % 3])
                kind = kinds[(mode+j) % len(kinds)]
                index = 0 if kind == 'point' else (0, 1, 7, 31)[(mode+j) % 4]
                shadow, _, _ = M.INVERSE.inverse_step(shadow, kind, index)
                word.append((kind, index))
            varied.append(dict(depth=depth, mode=mode, word=word,
                               hash=digest(M.shadow_word(q, word))))

    old_samples = []
    for index in range(4):
        params = M.family(12, index)
        u = (3*params['root']+3)//4
        old = OLD.one_step(u)
        assert old is None
        old_samples.append(dict(returning=u, result='unresolved'))

    demos = []
    for i, index in enumerate((0, 1)):
        plan = M.history_plan(M.family(12, index)['seed'])
        demos.append(demo(plan, None if stored is None else stored['supplied_demonstrations'][i]))

    invalid = [lambda: M.family(11), lambda: M.family(True), lambda: M.family(12, -1),
               lambda: M.family(12, True), lambda: M.history_plan(9),
               lambda: M.history_plan(True), lambda: M.history_plan(3849+16),
               lambda: M.prefix(1, (1,)), lambda: M.prefix(11547, (2,)),
               lambda: M.shadow_word(11547, [('ray0', 0)]),
               lambda: M.shadow_word(M.family(12, 1)['root'], [('point', 0)])]
    for action in invalid:
        expect_error(action)
    return dict(schema=1, claim='conditional high-history family; no universal supply',
                anchor=anchor, affine=dict(a=a, c=c, e=e, word=list(M.WORD)),
                family_cases=cases, old_endpoint_failures=failures,
                five_frontier_plans=five_frontiers,
                base_inverse_word_count=len(words), base_inverse_words_hash=digest(words),
                varied_inverse_words=varied, old_dispatcher_samples=old_samples,
                supplied_demonstrations=demos, invalid_inputs=len(invalid),
                source_hashes=source_hashes())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='Regenerate receipt and bounded designated supplies')
    args = parser.parse_args()
    path = HERE/'native_history_audit.json'
    expected = None if args.write else json.loads(path.read_text())
    result = audit(expected)
    serialized = json.dumps(result, sort_keys=True, indent=2)+'\n'
    if args.write:
        path.write_text(serialized)
    else:
        assert serialized == path.read_text(), 'Receipt mismatch; investigate before rewriting'
    print('PASS:54 high-history families,54 W5-frontier variants,54 old endpoint failures,4892 anchor states, '
          +str(result['base_inverse_word_count'])+' base inverse words,18 varied words,2 supplied conversions')


if __name__ == '__main__':
    main()
