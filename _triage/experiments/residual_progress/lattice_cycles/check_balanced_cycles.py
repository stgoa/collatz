#!/usr/bin/env python3
"""Replay exact finite evidence for the balanced-word denominator proof."""
import argparse
from fractions import Fraction
import hashlib
from itertools import product
import json
from math import gcd
from pathlib import Path

import balanced_cycles as B

HERE = Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def audit():
    arbitrary = []
    for k in range(1, 6):
        for word in product(range(1, 5), repeat=k):
            if 2 ** sum(word) <= 3 ** k:
                continue
            states = B.cycle(word)
            constant, denominator = B.word_data(word)
            d = denominator // gcd(constant, denominator)
            for i, x in enumerate(states):
                assert x.denominator == d
                rotation = word[i:] + word[:i]
                c, e = B.word_data(rotation)
                assert x == Fraction(c, e)
                numerator = x.numerator
                a = B.valuation2(3 * numerator + d)
                assert a == word[i]
                assert (3 * numerator + d) // 2 ** a == states[(i + 1) % k].numerator
            arbitrary.append([word, d, min(states).numerator])

    families = []
    primitive = 0
    intercepts = 0
    for k in range(1, 49):
        least = (3 ** k).bit_length()
        for total in range(least, least + 7):
            d = B.reduced_denominator(k, total)
            word = B.mechanical_word(k, total)
            states = B.cycle(word)
            assert all(x.denominator == d for x in states)
            assert (d == 1) == (total == 2 * k)
            g = gcd(k, total)
            base = B.mechanical_word(k // g, total // g)
            assert word == base * g
            full_d = 2 ** total - 3 ** k
            constants = []
            for l in range(k):
                w = B.mechanical_word(k, total, l)
                c, e = B.word_data(w)
                assert e == full_d
                assert e // gcd(c, e) == d
                next_l = (l + total) % k
                c_next, _ = B.word_data(B.mechanical_word(k, total, next_l))
                assert 3 * c + e == 2 ** w[0] * c_next
                assert c % 2 == 1
                constants.append(c)
                intercepts += 1
            if g == 1:
                primitive += 1
                assert all(gcd(c, full_d) == 1 for c in constants)
                for shift in range(k):
                    assert B.mechanical_word(k, total, shift * total % k) == word[shift:] + word[:shift]
                if k > 1:
                    j = next(j for j in range(1, k) if j * total % k == k - 1)
                    assert constants[1] - constants[0] == 3 ** (k - 1 - j) * 2 ** (j * total // k)
            families.append([k, total, g, d, digest(constants)])

    controls = []
    stored = []
    for k in list(range(1, 129)) + [256, 512]:
        c = B.high_control(k)
        assert 6 * c['minimum'] > k
        assert all(a in (1, 2) for a in c['word'])
        d = c['denominator']
        for i, x in enumerate(c['integer_states']):
            a = B.valuation2(3 * x + d)
            assert a == c['word'][i]
            assert (3 * x + d) // 2 ** a == c['integer_states'][(i + 1) % k]
        if k > 6:
            assert d > 1 and min(c['integer_states']) > d
        controls.append([k, c['total'], c['primitive_length'], d,
                         c['minimum'].numerator, c['minimum'].denominator])
        if k in (3, 5, 7, 64, 128, 512):
            stored.append(c)

    # The unreduced denominator is wrong for repetitions, and the gcd=1
    # theorem is not an assertion about arbitrary valuation words.
    assert B.reduced_denominator(6, 10) == 5
    assert 2 ** 10 - 3 ** 6 == 295
    counter = next((list(w), B.word_data(w)) for w, d, _ in arbitrary
                   if gcd(*B.word_data(w)) > 1 and len(set(w)) > 1)

    rejected = 0
    for action in (lambda: B.cycle([]), lambda: B.cycle([0, 2]),
                   lambda: B.cycle([1]), lambda: B.mechanical_word(0, 2),
                   lambda: B.mechanical_word(3, 2), lambda: B.mechanical_word(3, 5, 3),
                   lambda: B.reduced_denominator(3, 4), lambda: B.high_control(0),
                   lambda: B.rational_step(Fraction(1, 3)),
                   lambda: B.rational_step(Fraction(2, 5)), lambda: B.valuation2(0)):
        try:
            action()
        except ValueError:
            rejected += 1
        else:
            raise AssertionError('invalid domain accepted')
    return dict(status='PASS',
                scope='Exact denominator for specified mechanical words and varying-d rational cycle controls; no universal integer convergence claim',
                arbitrary_words=len(arbitrary), arbitrary_hash=digest(arbitrary),
                mechanical_families=len(families), primitive_families=primitive,
                intercept_checks=intercepts, family_hash=digest(families),
                high_controls=controls, stored_controls=stored,
                general_word_gcd_counterexample=counter, rejection_checks=rejected,
                source_hashes={name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                               for name in ('balanced_cycles.py', 'check_balanced_cycles.py')})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    data = json.loads(json.dumps(audit(), sort_keys=True,
                                default=lambda x: dict(numerator=x.numerator, denominator=x.denominator)))
    path = HERE / 'balanced_cycles_audit.json'
    if args.write_receipt:
        path.write_text(json.dumps(data, sort_keys=True, indent=2) + '\n')
    else:
        assert json.loads(path.read_text()) == data, 'Receipt differs; inspect before regenerating'
    print(f"PASS: {data['arbitrary_words']} rational words, {data['mechanical_families']} mechanical families, "
          f"{data['intercept_checks']} intercepts and {len(data['high_controls'])} high controls")


if __name__ == '__main__':
    main()
