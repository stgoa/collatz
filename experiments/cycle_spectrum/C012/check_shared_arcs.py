#!/usr/bin/env python3
"""Finite exact controls for the shared-background obstruction, not an S-unit theorem."""
import argparse
from hashlib import sha256
import importlib.util
from itertools import combinations
import json
from math import comb, gcd, lcm
from pathlib import Path
import sys

if sys.flags.optimize:
    raise SystemExit('FAIL: optimized Python is not supported')

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('c012_coupled', HERE/'check_coupled_system.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def order(a, p):
    return next(t for t in range(1, p) if pow(a, t, p) == 1)


def recover(intercept, length, total):
    answer = []
    while length > 1:
        rest = intercept-3**(length-1)
        c.require(rest > 0, 'positive remaining intercept required')
        a = (rest & -rest).bit_length()-1
        c.require(a >= 1, 'recovered valuation is not positive')
        answer.append(a)
        intercept = rest//2**a
        total -= a
        length -= 1
    c.require(intercept == 1 and total >= 1, 'last-letter recovery failed')
    return answer+[total]


def marker_control(background, markers=(1, 3, 4)):
    word = sum(([marker]+background for marker in markers), [])
    A, D, g, q, values, states = c.intercepts(word)
    k, m = len(background)+1, len(word)
    mismatches = [sum(x != y for x, y in zip(word, c.rotate(word, r)))
                  for r in range(1, m)]
    c.require(c.period(word) == m and min(mismatches) == 3 and
              mismatches[k-1] == 3, 'marker minimum rotation distance changed')
    return dict(word=word, A=A, D=D, g=g, q=q, period=m,
                raw_arrows=len(states), rotations=m-1,
                full_check_sha256=c.digest([word, values, mismatches]))


def report():
    families, admissible, rows, transcript = [], [], [], sha256()
    arrows = rotations = 0
    for n in (2, 4, 6, 8, 10):
        seen = set()
        for positions in combinations(range(n), n//2):
            u = [2]*n
            for j in positions:
                u[j] = 5
            A, C, _ = c.direct_data(u)
            c.require(A == 7*n//2 and C not in seen, 'fixed-total intercept collision')
            c.require(recover(C, n, A) == u, 'intercept recovery changed background')
            seen.add(C)
            case = marker_control(u)
            arrows += case['raw_arrows']
            rotations += case['rotations']
            c.feed(transcript, [u, C, case])
        c.require(len(seen) == comb(n, n//2), 'background count changed')
        families.append(dict(background_length=n, background_total=7*n//2,
                             distinct_intercepts=len(seen), expected=comb(n, n//2)))
    for t in (3, 4, 5):
        n = 3*t
        seen = set()
        for positions in combinations(range(n), t):
            u = [2]*n
            for j in positions:
                u[j] = 1
            A, C, _ = c.direct_data(u)
            c.require(A == 5*t and C not in seen and recover(C, n, A) == u,
                      'admissible-total intercept recovery/count failed')
            seen.add(C)
            case = marker_control(u, (3, 4, 5))
            c.require(case['period'] == 9*t+3 and case['A'] == 15*t+12 and
                      case['D'] > 0 and case['A'] < 2*case['period'],
                      'integer-cycle-admissible totals failed')
            arrows += case['raw_arrows']
            rotations += case['rotations']
            c.feed(transcript, [u, C, case])
        c.require(len(seen) == comb(n, t), 'admissible background count changed')
        admissible.append(dict(t=t, background_length=n, background_total=5*t,
                              distinct_intercepts=len(seen), expected=comb(n, t)))
    for primes in ([5], [5, 7], [5, 7, 11], [5, 7, 11, 13], [17], [19], [23]):
        t = lcm(*(order(a, p) for p in primes for a in (2, 3)))
        n, k = t, t*((5+t-1)//t)
        u = [k]+[2]*n
        A, C, _ = c.direct_data(u)
        c.require(k >= 5 and C == 3**n+2**k*(4**n-3**n), 'shared-arc formula failed')
        c.require(all(C % p == 1 for p in primes) and gcd(C, 6) == 1,
                  'specified-prime escape failed')
        c.require(C > 1, 'nontrivial numerator required')
        case = marker_control(u)
        arrows += case['raw_arrows']
        rotations += case['rotations']
        rows.append(dict(primes=primes, n=n, k=k, C=C,
                         residues=[C % p for p in primes], period=case['period'],
                         q_bits=case['q'].bit_length(), check_sha256=case['full_check_sha256']))
        c.feed(transcript, [u, C, case])
    return dict(status='PASS', scope='Bounded exact examples for the written arbitrary-background and fixed-coefficient, bounded-height expression-counting obstructions. No candidate denominator inequality is proved or refuted.',
        clock='raw positive odd-only; no absorbing state',
        source_sha256={p.name:sha256(p.read_bytes()).hexdigest()
                       for p in (Path(__file__), HERE/'check_coupled_system.py')},
        fixed_total_families=families, integer_cycle_admissible_total_families=admissible,
        prescribed_prime_sets=rows,
        counts=dict(backgrounds=sum(r['distinct_intercepts'] for r in families),
                    admissible_total_backgrounds=sum(r['distinct_intercepts'] for r in admissible),
                    prime_set_cases=len(rows), raw_arrows=arrows, rotations=rotations),
        all_checks_sha256=transcript.hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = report()
    path = HERE/'shared_arc_audit.json'
    if args.write:
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        c.require(json.loads(path.read_text()) == result, 'saved receipt differs')
    print(json.dumps(dict(status=result['status'], counts=result['counts'])))


if __name__ == '__main__':
    main()
