#!/usr/bin/env python3
"""Finite formula checks for antiperiodic-intercept-nondivisibility."""

import argparse
import json
from math import gcd
from pathlib import Path


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def intercept(word):
    value, total = 0, 0
    for letter in word:
        value = 3 * value + (1 << total)
        total += letter
    return value


def words(prefix=(), remaining=14):
    if prefix:
        yield prefix
    if len(prefix) < 6:
        for letter in range(1, remaining + 1):
            yield from words(prefix + (letter,), remaining - letter)


def compute():
    counts = dict(words=0, nondivisibility_checks=0, integral_segments=0,
                  one_letter_identities=0, coprime_exclusions=0,
                  primitive_half_bounds=0, transposition_identities=0,
                  transposition_coprime_exclusions=0)
    for word in words():
        counts['words'] += 1
        n, total, c = len(word), sum(word), intercept(word)
        two, three = 1 << total, 3 ** n
        for s in range(1, 17):
            for t in range(1, 17):
                require(c % (two * t + three * s) != 0, ('divisibility', word, s, t))
                counts['nondivisibility_checks'] += 1
        for start in range(-9, 10):
            numerator = three * start + c
            if numerator % two:
                continue
            end = numerator // two
            x = start
            for a in word:
                require((3*x+1) % (1 << a) == 0, ('nonintegral cut', word, start))
                x = (3*x+1) // (1 << a)
                if start < 0:
                    require(x < 0, ('sign crossing', word, start))
            require(x == end, ('composition', word, start))
            counts['integral_segments'] += 1
        for i in range(n):
            rotated = word[i+1:] + word[:i+1]
            for j in range(1, 7):
                changed = word[:i] + (word[i] + 2*j,) + word[i+1:]
                joined = word + changed
                modulus = (1 << (total+j)) + three
                factor = (1 << j)-1
                actual = gcd(intercept(joined), modulus)
                expected = gcd(factor * intercept(rotated), modulus)
                require(actual == expected, ('one-letter gcd', word, i, j))
                counts['one_letter_identities'] += 1
                if gcd(factor, modulus) == 1:
                    require(actual != modulus, ('coprime exclusion', word, i, j))
                    counts['coprime_exclusions'] += 1
                    if (1 << (total+j)) > three and gcd(total+j, n) == 1:
                        require(actual < (1 << (total+j)), ('half bound', word, i, j))
                        counts['primitive_half_bounds'] += 1
        for i in range(n):
            for h in range(i+1, n):
                if word[i] == word[h]:
                    continue
                v = list(word)
                v[i], v[h] = v[h], v[i]
                gap = abs(word[i]-word[h])
                middle = word[i+1:h]
                appended = middle + (total-sum(middle),)
                f = intercept(appended)
                modulus = two + three
                actual = gcd(intercept(word+tuple(v)), modulus)
                expected = gcd(((1 << gap)-1) * f, modulus)
                require(actual == expected, ('transposition gcd', word, i, h))
                require(f % modulus != 0, ('middle-word exclusion', word, i, h))
                counts['transposition_identities'] += 1
                if gcd((1 << gap)-1, modulus) == 1:
                    require(actual != modulus, ('transposition exclusion', word, i, h))
                    counts['transposition_coprime_exclusions'] += 1
    controls = []
    for d in (5, 7, 13, 61):
        t = (d-3)//2
        require((3*(-1)+d)//2 == t and t > 0, ('control segment', d))
        require(d * intercept((1,)) % (2*t+3) == 0, ('control divisibility', d))
        controls.append(dict(d=d, start=-1, word=[1], end=t, divisor=2*t+3))
    diagnostic = dict(u=[1], v=[9], j=4, modulus=35,
                      actual_gcd=gcd(intercept((1,9)),35),
                      dropped_factor_gcd=gcd(intercept((1,)),35))
    require(diagnostic['actual_gcd'] == 5 and diagnostic['dropped_factor_gcd'] == 1,
            'Dropped-factor diagnostic failed.')
    return dict(scope=dict(max_length=6, max_total=14, s_min=1, s_max=16, t_min=1, t_max=16,
                           start_min=-9, start_max=9, j_min=1, j_max=6),
                counts=counts, controls=controls, dropped_factor_diagnostic=diagnostic)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    receipt = Path(__file__).with_suffix('.json')
    result = compute()
    if args.write_receipt:
        receipt.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(receipt.exists(), 'Missing receipt; run --write-receipt.')
        require(json.loads(receipt.read_text()) == result, 'Receipt mismatch.')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
