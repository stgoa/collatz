"""Replay finite anchor classification and exact supplied history currents."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import random
import sys
from types import ModuleType
import history_frontier as M

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ANCHOR_PATH = HERE.parent/'native_history/anchor_certificate.json'
INPUT_PATH = HERE.parent/'native_history/native_history_audit.json'


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def rows(data):
    return [[x, c] for x, c in sorted(data.items())]


def div(current):
    out = Counter()
    for x, c in current.items():
        assert isinstance(x, int) and not isinstance(x, bool) and x > 1 and x % 2
        assert isinstance(c, int) and not isinstance(c, bool) and c
        y = 3*x+1
        y //= y & -y
        out[x] += c
        if y != 1:
            out[y] -= c
    return {x: c for x, c in out.items() if c}


def inverse(y, kind, j):
    # Independent integer implementation of the complete branch formulas.
    bases = {0: {'ray0': (8, 3), 'ray1': (16, 3)},
             1: {'ray0': (4, -1), 'ray1': (32, 19)},
             2: {'point': (2, -1), 'ray0': (64, 19), 'ray1': (128, 83)}}
    a, b = bases[y % 3][kind]
    assert (a*y+b) % 3 == 0 and (kind != 'point' or j == 0)
    p = (a*y+b)//3
    p = 64**j*p+49*(64**j-1)//63
    return p, Fraction(64**j*a, 3)


def finite_inverse_tree(y, depth, max_ray=2):
    out, frontier = {(y, 0)}, [y]
    for d in range(1, depth+1):
        following = []
        for x in frontier:
            kinds = ('point', 'ray0', 'ray1') if x % 3 == 2 else ('ray0', 'ray1')
            for kind in kinds:
                for j in (range(1) if kind == 'point' else range(max_ray+1)):
                    p, _ = inverse(x, kind, j)
                    out.add((p, d))
                    following.append(p)
        frontier = following
    return out


def reject(action):
    try:
        action()
    except ValueError:
        return
    raise AssertionError('Expected rejection')


def source_hashes():
    paths = {Path(__file__).resolve(), HERE/'HISTORY_FRONTIER.md', ANCHOR_PATH, INPUT_PATH}
    pending, seen = [M], set()
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
        pending.extend(v for v in vars(module).values() if isinstance(v, ModuleType))
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}


def audit():
    stored = json.loads(ANCHOR_PATH.read_text())
    history = M.FiniteHistory(stored['edges'], 11546)
    assert len(history.edges) == 4892 and len(history.origins) == 2887
    assert 11547 not in history.edges
    cat = history.catalogue(17321)
    assert len(cat) == 1
    row = cat[0]
    assert (row['origin'], row['depth'], row['slope']) == (11391, 13, Fraction(2**20, 3**13))
    assert history.catalogue(11547) == ()
    catalogue = dict(origin=row['origin'], depth=row['depth'],
                     slope=[row['slope'].numerator, row['slope'].denominator],
                     inverse_word=row['word'], forward_path=row['path'])

    family = []
    for d in (1, 2, 3, 8, 11, 12, 13, 16, 32, 64, 128):
        for t in (0, 1, 2, 19):
            q = 11547+16*3**d*t
            y = (3*q+1)//2
            assert M.N.canonical(q) and M.N.canonical(y) and q//3 % 16 == 9
            direct = history.classify(q, q, 11547, d)
            assert not direct['hits'] and direct['shadow_cutoff'] == 11546
            found = history.classify(q, y, 17321, d+1)
            assert found['shadow_cutoff'] == 11546
            if d < 12:
                assert not found['hits']
                family.append([d, t, 0])
                continue
            assert len(found['hits']) == 1
            hit = found['hits'][0]
            p = 11391+2**23*3**(d-12)*t
            assert (hit['lower'], hit['depth']) == (p, 13) and p < q
            plan = M.native_plan(q//3, (q, y), hit)
            expected = {q: 1, q//3: -1}
            for v, c in plan['coefficients'].items():
                expected = M.combine((1, expected), (-c, {3*v: 1, v: -1}))
            assert div(plan['current']) == expected
            assert all(M.B.rho(v) < q for v in plan['coefficients'])
            family.append([d, t, p, len(plan['current']), rows(plan['coefficients'])])

    # Finite direct enumeration cross-check; the theorem supplies completeness
    # for arbitrary rays, not this deliberately bounded enumeration.
    trees = []
    for target in (7, 11, 17, 49, 121):
        assert M.N.canonical(target)
        for depth in (0, 1, 2, 3):
            result = history.classify(700, target, target, depth)
            actual = {(r['lower'], r['depth']) for r in result['hits']}
            bounded = {(a, d) for a, d in finite_inverse_tree(target, depth) if a < 700}
            assert actual == bounded
            trees.append([target, depth, len(actual)])
    for t in (1, 2, 7):
        target = 11+16*3**3*t
        threshold = 1000+16*3**3*t
        result = history.classify(threshold, target, 11, 3)
        actual = {(r['lower'], r['depth']) for r in result['hits']}
        bounded = {(a, d) for a, d in finite_inverse_tree(target, 3) if a < threshold}
        assert actual == bounded
        trees.append([target, 3, len(actual)])

    # General shadow inequality at larger ray indices and varying depth.
    rng = random.Random(82013)
    gaps = []
    for trial in range(36):
        length = 1+trial % 18
        anchor = rng.choice((7, 11, 17, 17321))
        target = anchor+32*3**length*(trial+1)
        assert M.N.canonical(target)
        a, c, slope = target, anchor, Fraction(1)
        for depth in range(length):
            choices = ('point', 'ray0', 'ray1') if c % 3 == 2 else ('ray0', 'ray1')
            kind = rng.choice(choices)
            j = 0 if kind == 'point' else rng.choice((0, 1, 7, 31))
            a, alpha = inverse(a, kind, j)
            c, _ = inverse(c, kind, j)
            slope *= alpha
            assert M.N.canonical(a) and M.N.canonical(c)
            assert a == c+slope*(target-anchor)
            assert slope >= Fraction(c+1, anchor+1)
            assert Fraction(a+1, target+1) >= Fraction(c+1, anchor+1)
        gaps.append([length, anchor, a.bit_length(), c.bit_length(),
                     slope.numerator, slope.denominator])

    # A larger anchor origin can become a smaller actual origin when the
    # target prefix contracts: the exact cutoff must be retained.
    cutoffs = []
    qpath = (465, 43, 65, 49, 9, 7, 11)
    for d in (0, 1, 2, 8, 32):
        for t in (1, 2):
            q = 465+2**19*3**d*t
            p = 497+2**11*3**(d+5)*t
            y = 11+16*3**(d+6)*t
            x = q
            for _ in range(6):
                x = M.N.quotient_step(x)
            assert x == y and M.N.quotient_step(p) == y and p < q
            found = history.classify(q, y, 11, d+6)
            assert any(r['origin'] == 497 and r['lower'] == p and r['depth'] == 1
                       for r in found['hits'])
            assert 497 > 465 and found['shadow_cutoff'] == 538
            cutoffs.append([d, t, q, p, y, found['shadow_cutoff']])
    assert M.quotient_current(qpath)

    demos = []
    inputs = json.loads(INPUT_PATH.read_text())['supplied_demonstrations']
    for item in inputs:
        w = item['seed']
        q, y = 3*w, (9*w+1)//2
        found = history.classify(q, y, 17321, 13)
        assert len(found['hits']) == 1
        plan = M.native_plan(w, (q, y), found['hits'][0])
        assert rows(plan['current']) == item['plan_current']
        assert rows(plan['coefficients']) == item['coefficients']
        supplied = {int(u): dict(v) for u, v in item['supplied'].items()}
        for u, current in supplied.items():
            assert div(current) == {3*u: 1, u: -1}
        result = M.B.compile_plan(plan, supplied)
        assert rows(result) == item['current'] and div(result) == {q: 1, w: -1}
        reject(lambda: M.B.compile_plan(plan, {}))
        demos.append(dict(seed=w, rows=len(result), current_hash=digest(rows(result))))

    wrong = [list(r) for r in stored['edges']]
    wrong[1][1] = 1
    invalid = [lambda: M.FiniteHistory(wrong, 11546),
               lambda: M.FiniteHistory(stored['edges']+stored['edges'][:1], 11546),
               lambda: M.FiniteHistory(stored['edges'][1:], 11546),
               lambda: M.FiniteHistory([(1, 1)], 7),
               lambda: M.FiniteHistory(stored['edges'], True),
               lambda: history.catalogue(1), lambda: history.catalogue(True),
               lambda: history.classify(True, 17321, 17321, 13),
               lambda: history.classify(11547, 17321, 17321, -1),
               lambda: history.classify(11547, 17321, 1, 13),
               lambda: history.classify(11547, 17321, 17353, 13),
               lambda: history.classify(11547, 17353, 17321, 13),
               lambda: history.classify(100000, 17321, 17321, 13),
               lambda: M.edge_branch(11391, 17321),
               lambda: M.quotient_current((7, 17)),
               lambda: M.native_plan(1, (), {})]
    for action in invalid:
        reject(action)
    return dict(schema=1, status='PASS', anchor_states=len(history.edges),
                covered_origins=len(history.origins), unique_catalogue=catalogue,
                family_cases=len(family), family_hash=digest(family),
                finite_tree_cases=trees, shadow_cases=len(gaps), shadow_hash=digest(gaps),
                cutoff_controls=cutoffs, supplied_demos=demos,
                rejected_inputs=len(invalid), source_hashes=source_hashes())


def main():
    assert not sys.flags.optimize, 'Run without -O'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result = audit()
    text = json.dumps(result, sort_keys=True, indent=2)+'\n'
    path = HERE/'history_frontier_audit.json'
    if args.write_receipt:
        path.write_text(text)
    else:
        assert path.read_text() == text, 'Receipt mismatch; investigate before refreshing'
    print('PASS: complete4892-state anchor,44 lifted histories,23 finite trees,36 shadow words,10 cutoff controls,2 supplied currents')


if __name__ == '__main__':
    main()
