#!/usr/bin/env python3
"""Bounded independent replay for R85; the all-ray quantifiers use its proof."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('checked_history_barrier', HERE/'history_barrier.py')
B = module_from_spec(spec)
spec.loader.exec_module(B)
RECEIPT = HERE/'history_barrier_audit.json'


def v2(x):
    assert x > 0
    answer = 0
    while x % 2 == 0:
        x //= 2
        answer += 1
    return answer


def s(x):
    return 1 if x == 1 else (3*x+1)//2**v2(3*x+1)


def normal(x):
    while x % 8 == 5:
        x = (x-1)//4
    if x % 4 == 3:
        a = v2(x+1)
        if ((x+1)//2**a-3**a) % 4 == 0:
            x = (x-1)//2
    return x


def t(x):
    assert normal(x) == x
    return normal(s(x))


def encode(value):
    """Hex makes even very large exact rows independent of decimal limits."""
    if isinstance(value, dict):
        return {str(key): encode(item) for key, item in sorted(value.items(), key=lambda item: str(item[0]))}
    if isinstance(value, (list, tuple)):
        return [encode(item) for item in value]
    if type(value) is int:
        return hex(value)
    return value


def digest(value):
    return hashlib.sha256(json.dumps(encode(value), sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def complete_origins(quotient):
    records = []
    origin_checks = 0
    target_checks = 0
    noncanonical = 0
    step = t if quotient else s
    for q in range(3, 512, 6):
        if quotient and normal(q) != q:
            continue
        J = 0
        targets = [q]
        while J < 5 and v2(3*targets[-1]+1) == 1:
            nxt = s(targets[-1])
            if quotient and normal(nxt) != nxt:
                break
            targets.append(nxt)
            J += 1
        value, Dmax = q, 0
        while value % 3 == 0:
            value //= 3
            Dmax += 1
        for D in range(1, Dmax+1):
            data = B.certificate(q, D, J, quotient=quotient)
            assert data['targets'] == targets
            noncanonical += int(normal(q) != q)
            matches = []
            for p in range(1, q+1, 2):
                if quotient and normal(p) != p:
                    continue
                x = p
                origin_checks += 1
                for d in range(D+J+1):
                    for a, y in enumerate(targets):
                        if d <= D+a:
                            target_checks += 1
                            if x == y:
                                assert (p, d) == (q, a), (q, D, J, p, d, a)
                                matches.append([p, d, a])
                    x = step(x)
            assert matches == [[q, a, a] for a in range(J+1)]
            records.append([q, D, J, matches])
    return dict(cases=len(records), origins=origin_checks, target_comparisons=target_checks,
                noncanonical_sources=noncanonical, sha256=digest(records),
                examples=[row for row in records if row[0] in (3, 39, 135, 243)])


def crt_checks():
    records = []
    for D, J, extra, index in product((1, 2, 4, 8, 16, 32, 64), (0, 1, 2, 4, 8, 16, 32), (0, 1), (0, 1)):
        H = max(J+1, 3)+extra
        data = B.family(D, J, index, H)
        q = data['source']
        assert q % 3**D == 0 and v2(q+1) == H
        assert (q+1)//2**H % 4 == -3**H % 4
        assert normal(3*data['seed']) == q and data['seed'] % 8 == 5
        x = q
        for a, y in enumerate(data['targets']):
            assert x == y == normal(x)
            if a < J:
                assert v2(3*x+1) == 1
                x = s(x)
        records.append(data)
    h17 = []
    for D, r, index in product((1, 2, 4, 16, 64), (0, 1, 2, 8, 16, 32), (0, 1)):
        data = B.h17_family(D, r, index)
        b = data['seed']
        assert b % 8192 == 905 and v2(217*b+223) == 9*r+17
        assert data['source'] == 3*b and normal(3*b) == 3*b
        assert t(3*b) == (9*b+1)//2
        h17.append(data)
    return dict(critical_cases=len(records), critical_sha256=digest(records),
                H17_cases=len(h17), H17_sha256=digest(h17),
                first_critical=records[0], first_H17=h17[0])


def inverse_words():
    records = []
    rational = 0
    positive_integer = 0
    q = B.family(8, 16)['source']
    for a, initial_points, ray, L, pattern in product((0, 1, 4, 16), (0, 1, 3, 16), ('ray0', 'ray1'), (0, 1, 3, 17, 64), range(2)):
        if initial_points > a:
            continue
        word = [('point', 0)]*initial_points
        x = B.ordinary_targets(q, a)[a-initial_points]
        word.append((ray, L))
        alpha, beta = B.inverse_affine(x % 3, ray, L)
        x = int(alpha*x+beta)
        while len(word) < 8+a:
            if x % 3 == 2 and pattern == 0:
                symbol = ('point', 0)
            else:
                symbol = ('ray'+str((len(word)+pattern) % 2), (len(word)+pattern) % 3)
            alpha, beta = B.inverse_affine(x % 3, *symbol)
            x = int(alpha*x+beta)
            word.append(symbol)
        data = B.inverse_trace(q, 8, a, word)
        assert data['endpoint'] == x > q
        for row in data['trace']:
            shadow = Fraction(*row['shadow'])
            if row['off_spine']:
                rational += int(shadow.denominator > 1)
                positive_integer += int(shadow.denominator == 1)
                assert shadow > 0
        # Recheck every actual inverse arrow without using constructor formulas.
        y = data['endpoint']
        for depth in range(len(word)-1, -1, -1):
            y = t(y)
            expected = B.ordinary_targets(q, a)[a] if depth == 0 else data['trace'][depth-1]['state']
            assert y == expected
        records.append(data)
    # All exact equality paths, including a=0 and J=32, use only point undo.
    spine = []
    for D, a in product((1, 2, 8), (0, 1, 4, 16, 32)):
        q = B.family(D, a)['source']
        data = B.inverse_trace(q, D, a, [('point', 0)]*a)
        assert data['endpoint'] == q
        spine.append(data)
    assert rational > 0 and positive_integer > 0
    return dict(words=len(records), equality_spines=len(spine),
                positive_rational_shadow_rows=rational, positive_integer_shadow_rows=positive_integer,
                largest_ray_index=64, sha256=digest(records), spine_sha256=digest(spine))


def ordinary_words():
    records = []
    attempts = 0
    valid = 0
    for q, D, a in ((3, 1, 0), (3, 1, 1), (15, 1, 2), (39, 1, 2),
                    (27, 3, 1), (63, 2, 3), (135, 3, 2), (243, 5, 1)):
        # All valuation sequences within each listed finite box are included.
        for depth in range(min(D+a, 4)+1):
            for word in product(range(1, 5), repeat=depth):
                attempts += 1
                p = B.ordinary_candidate(q, D, a, word)
                if p is not None:
                    x = p
                    for e in word:
                        assert v2(3*x+1) == e
                        x = s(x)
                    assert x == B.ordinary_targets(q, a)[a]
                    valid += 1
                    records.append([q, D, a, list(word), p])
    # A negative integer may become positive after losing integrality.
    # This is why the written ordinary proof uses the remaining-halving budget.
    bad_shadow = [Fraction(-1)]
    for e in (3, 1):
        bad_shadow.append((3*bad_shadow[-1]+1)/2**e)
    assert bad_shadow == [Fraction(-1), Fraction(-1, 4), Fraction(1, 8)]
    return dict(attempted_words=attempts, valid_words=valid, sha256=digest(records),
                negative_shadow_control=[[x.numerator, x.denominator] for x in bad_shadow])


def supplied_control():
    words = {39: (1, 1, 2, 1, 4, 1, 3, 1, 2, 3, 4), 13: (3, 4)}
    paths = {}
    supplied = {}
    for seed, word in words.items():
        current = Counter()
        x, path = seed, [seed]
        for e in word:
            assert x != 1 and v2(3*x+1) == e
            current[x] += 1
            x = s(x)
            path.append(x)
        assert x == 1
        assert B.N.divergence(dict(current)) == {seed: 1}
        paths[seed], supplied[seed] = path, current
    output = Counter(supplied[39])
    output.subtract(supplied[13])
    output = {x: c for x, c in sorted(output.items()) if c}
    assert B.N.divergence(output) == {13: -1, 39: 1}
    assert t(t(t(39))) == 33 < 39
    assert B.certificate(39, 1, 2)['targets'] == [39, 59, 89]
    return dict(seed=13, rank=39, quotient_escape=[39, 59, 89, 33],
                supplied_words={str(x): list(w) for x, w in words.items()},
                supplied_paths={str(x): p for x, p in paths.items()},
                current=[[x, c] for x, c in output.items()], rows=len(output),
                divergence=[[13, -1], [39, 1]])


def rejects():
    q = B.family(2, 4)['source']
    checks = [
        lambda: B.certificate(0, 1, 0), lambda: B.certificate(2, 1, 0),
        lambda: B.certificate(39, 0, 2), lambda: B.certificate(39, 2, 2),
        lambda: B.certificate(39, 1, 3), lambda: B.certificate(3, 1, 0),
        lambda: B.certificate(39, 1, 2, quotient=1), lambda: B.family(1, 3, H=3),
        lambda: B.family(1, 0, index=-1), lambda: B.h17_family(1, -1),
        lambda: B.inverse_affine(0, 'point'), lambda: B.inverse_affine(2, 'point', 1),
        lambda: B.inverse_affine(1, [], 0), lambda: B.inverse_affine(1, 'ray0', -1),
        lambda: B.inverse_affine(1, 'ray0', 64, max_bits=64),
        lambda: B.inverse_trace(q, 2, 4, [('point', 0)]*7),
        lambda: B.inverse_trace(q, 2, 4, [('point',)]),
        lambda: B.inverse_trace(q, 2, 4, [('ray0', 0)], max_bits=8),
        lambda: B.ordinary_candidate(39, 1, 2, [1]*4),
        lambda: B.ordinary_candidate(39, 1, 2, [0]),
        lambda: B.ordinary_candidate(39, 1, 2, [True]),
        lambda: B.ordinary_candidate(39, 1, 2, [1000], max_bits=100),
        lambda: B.ordinary_candidate(39, 1, 2, [1], max_bits=0),
    ]
    for i, check in enumerate(checks):
        try:
            check()
        except ValueError:
            continue
        raise AssertionError(('invalid input accepted', i))
    return len(checks)


def build():
    files = [Path(__file__).resolve(), HERE/'history_barrier.py', HERE/'HISTORY_CLOCK_BARRIER.md', Path(B.N.__file__).resolve()]
    return dict(status='PASS', theorem='R85', scope='Clock-bounded history exclusion; sources vary with precision; no all-current or fixed-source nontermination claim',
                source_hashes={str(p.relative_to(HERE.parent)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
                quotient_origins=complete_origins(True), ordinary_origins=complete_origins(False),
                CRT=crt_checks(), inverse=inverse_words(), ordinary_words=ordinary_words(),
                supplied=supplied_control(), rejections=rejects())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result = build()
    if args.write_receipt:
        RECEIPT.write_text(json.dumps(result, sort_keys=True, indent=2)+'\n')
    else:
        assert result == json.loads(RECEIPT.read_text()), 'Stored receipt differs; inspect before regeneration'
    print('PASS: bounded-future all-ray history barrier '
          f"({result['quotient_origins']['cases']} quotient/{result['ordinary_origins']['cases']} ordinary domains; "
          f"{result['inverse']['words']} inverse words; {result['CRT']['critical_cases']} critical/{result['CRT']['H17_cases']} H17 cells; "
          f"{result['rejections']} rejections)")


if __name__ == '__main__':
    main()
