#!/usr/bin/env python3
"""Independent C009 deletion-law and integer endpoint reconstruction checks."""
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent


def require(ok, message):
    if not ok:
        raise ValueError(message)


def word_data(word):
    A, C = 0, 0
    for a in word:
        require(type(a) is int and a > 0, 'positive valuation')
        C = 3*C+2**A
        A += a
    return A, C


def follow(x, q, word):
    states = [x]
    for a in word:
        value = 3*x+q
        require(value % 2**a == 0 and (value//2**a) % 2 == 1, 'exact odd valuation')
        x = value//2**a
        states.append(x)
    return states


def deletion_grid():
    cases, interior, nearest, arrows = 0, 0, 0, 0
    digest = sha256()
    for m in range(2, 81):
        for s in range(1, m):
            if gcd(m, s) != 1:
                continue
            for deleted in range(m):
                retained = [(deleted+j) % m for j in range(1, m)]
                rank = {v: j for j, v in enumerate(retained)}
                shifts = []
                for source in retained:
                    j = (source-deleted) % m
                    target = (source+s) % m
                    if target == deleted:
                        target = (target+s) % m
                    shift = (rank[target]-rank[source]) % (m-1)
                    expected = (s if j < m-s else s-1 if j > m-s else 2*s-1) % (m-1)
                    require(shift == expected, 'one-point deletion shift formula')
                    shifts.append(shift)
                    arrows += 1
                is_rotation = len(set(shifts)) == 1
                require(is_rotation == (s in (1, m-1)), 'deletion classification')
                expected_counts = Counter()
                expected_counts[s % (m-1)] += m-s-1
                expected_counts[(s-1) % (m-1)] += s-1
                expected_counts[(2*s-1) % (m-1)] += 1
                require(Counter(shifts) == +expected_counts, 'deletion shift multiplicities')
                cases += 1
                nearest += is_rotation
                interior += not is_rotation
                digest.update(json.dumps([m, s, deleted, shifts], separators=(',', ':')).encode())
    return dict(maximum_m=80, permutations=cases, checked_arrows=arrows,
                nearest_neighbor_rotations=nearest, interior_nonrotations=interior,
                exact_rows_sha256=digest.hexdigest())


def endpoint_grid():
    cases, arrows = 0, 0
    for length in range(1, 6):
        for word in product(range(1, 5), repeat=length):
            A, C = word_data(word)
            modulus = 2**(A+1)
            for q in (1, 5, 7, 13):
                residue = (2**A-q*C)*pow(3**length, -1, modulus) % modulus
                for lift in range(3):
                    x = residue+lift*modulus
                    require(x > 0 and x % 2, 'odd starting residue')
                    numerator = 3**length*x+q*C
                    require(numerator % 2**A == 0, 'endpoint divisibility')
                    y = numerator//2**A
                    require(y > 0 and y % 2, 'odd endpoint')
                    states = follow(x, q, word)
                    require(states[-1] == y, 'endpoint reconstruction')
                    cases += 1
                    arrows += length
    return dict(word_lengths=[1, 5], valuation_alphabet=[1, 4], parameters=[1, 5, 7, 13],
                lifts_per_word_parameter=3, positive_odd_endpoint_pairs=cases, exact_arrows=arrows,
                scope='Open positive paths constructed from endpoint congruences, not new cycles.')


def actual_control(q, n):
    require(n[0] == min(n) and len(n) == len(set(n)), 'primitive minimum phase')
    word = []
    for x, y in zip(n, n[1:]+n[:1]):
        value, a = 3*x+q, 0
        while value % 2 == 0:
            value //= 2
            a += 1
        require(value == y and a > 0, 'actual cycle arrow')
        word.append(a)
    A, C = word_data(word)
    D = 2**A-3**len(n)
    require(D > 0 and D//gcd(C, D) == q and C//gcd(C, D) == n[0], 'actual reduced denominator')
    h = [(x//n[0]).bit_length()-1 for x in n]
    z = [Fraction(x, 2**height) for x, height in zip(n, h)]
    full_order = sorted(range(len(n)), key=z.__getitem__)
    F = [3*z[i]+Fraction(q, 2**h[i]) for i in range(len(n))]
    require(q <= n[0] and all(F[i] < F[j] for i, j in zip(full_order, full_order[1:])), 'ordered domain')
    core = sorted((i for i in range(len(n)) if h[i] == 0), key=n.__getitem__)
    ranks = {i: j for j, i in enumerate(core)}
    returns = []
    for i in core:
        j = (i+1) % len(n)
        segment = [word[i]]
        while h[j] > 0:
            segment.append(word[j])
            j = (j+1) % len(n)
        exponent, intercept = word_data(segment)
        require(2**exponent*n[j] == 3**len(segment)*n[i]+q*intercept, 'return affine identity')
        returns.append(dict(source=n[i], target=n[j], target_rank=ranks[j], word=segment,
                            A=exponent, C=intercept, slope=[3**len(segment), 2**exponent]))
    shifts = {(r['target_rank']-j) % len(core) for j, r in enumerate(returns)}
    return dict(q=q, states=n, word=word, heights=h, core=[n[i] for i in core],
                returns=returns, first_return_is_rotation=len(shifts) == 1)


def report():
    controls = [actual_control(13, [283, 431, 653, 493, 373]),
                actual_control(83, [157, 277, 457, 727, 283, 233, 391])]
    require(not controls[0]['first_return_is_rotation'], 'exact order-loss control')
    r = next(r for r in controls[1]['returns'] if r['source'] == 277)
    require(r['target'] == 283 and r['slope'] == [27, 32] and r['C'] == 19,
            'contracting but increasing excursion')
    return dict(status='PASS', clock='raw odd-only; no absorber',
                scope='Finite checks of written reconstruction and deletion theorems and exact controls; no q1 cycle exclusion.',
                deletion=deletion_grid(), endpoints=endpoint_grid(), actual_controls=controls,
                source_sha256={p.name: sha256(p.read_bytes()).hexdigest()
                               for p in (Path(__file__), HERE/'FIRST_RETURN_ORDER.md')})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    r = report()
    p = HERE/'return_order_audit.json'
    if args.write:
        p.write_text(json.dumps(r, indent=2, sort_keys=True)+'\n')
    else:
        require(json.loads(p.read_text()) == r, 'receipt mismatch')
    print(json.dumps({k:r[k] for k in ('status', 'deletion', 'endpoints')}))


if __name__ == '__main__':
    main()
