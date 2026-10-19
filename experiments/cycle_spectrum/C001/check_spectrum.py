#!/usr/bin/env python3
"""Reproduce the finite C001 word-family tests; print a deterministic receipt."""
import argparse
import hashlib
import json
import sys
from collections import Counter
from itertools import product
from math import gcd
from pathlib import Path

from repetition_spectrum import (data, exact_cycle, high_family_repetitions,
                                mechanical, modular_period,
                                prime_to_six_part, repeat_data)

HERE = Path(__file__).resolve().parent


def direct(word):
    # Independent explicit sum, rather than the concatenation recurrence.
    prefix = 0
    c = 0
    for i, a in enumerate(word):
        c += 3 ** (len(word)-1-i) * 2 ** prefix
        prefix += a
    return c, 2 ** prefix - 3 ** len(word)


def main():
    words = [w for n in range(1, 5) for w in product(range(1, 5), repeat=n)]
    tails = [w for w in words if len(w) <= 3]
    counts = Counter()
    denominators = set()
    repeated_controls = []
    period_controls = []
    for u in words:
        cu, q, p = data(u)
        if q <= p:
            continue
        for v in tails:
            counts['block_pairs'] += 1
            cv, s, r = data(v)
            determinant = (q-p)*cv-(s-r)*cu
            if determinant == 0:
                counts['common_fixed_point_pairs'] += 1
            modulus = prime_to_six_part(determinant) if determinant else None
            for k in (1, 2, 3, 4, 5, 6, 8, 12, 16):
                row = repeat_data(u, v, k)
                word = u*k + v
                c, d = direct(word)
                assert (row['C'], row['D']) == (c, d)
                if d <= 0:
                    counts['nonpositive_words'] += 1
                    continue
                parameter, states = exact_cycle(word)
                assert parameter == row['denominator']
                counts['positive_word_cycles'] += 1
                counts['exact_odd_arrows'] += len(states)
                denominators.add(parameter)
                g = row['cancellation']
                if determinant:
                    assert modulus % g == 0
                    assert gcd(c, d, modulus) == g
                    counts['noncommuting_bound_checks'] += 1
                    if gcd(q-p, s-r) == 1:
                        assert g == gcd(d, determinant)
                        counts['coprime_exact_checks'] += 1
                    if d > modulus:
                        assert parameter > 1
                        counts['nonintegrality_certificates'] += 1
                else:
                    assert c*(q-p) == cu*d
                    counts['common_fixed_point_checks'] += 1
            if (determinant and modulus <= 127
                    and len(period_controls) < 128):
                period = modular_period(u, v, cap=20000)
                if period is None:
                    counts['period_search_capped'] += 1
                    continue
                for k in range(32):
                    left, right = repeat_data(u, v, k), repeat_data(u, v, k+period)
                    assert left['cancellation'] == right['cancellation']
                period_controls.append(dict(u=list(u), v=list(v), modulus=modulus,
                                            period=period, tested_offsets=32))

    for k in range(1, 257):
        u, v = (1, 1, 3), (2,)
        row = repeat_data(u, v, k)
        g = 7 if k % 6 == 3 else 1
        assert row['cancellation'] == g
        d, states = exact_cycle(u*k+v)
        assert d == (4*32**k-3*27**k)//g
        assert min(states) > d
        minima = sum(states[i] < states[i-1] and states[i] < states[(i+1)%len(states)]
                     for i in range(len(states)))
        assert minima == k
        if k <= 6:
            repeated_controls.append(dict(k=k, denominator=d,
                                          cancellation=g, states=states))

    high_controls = []
    for m in list(range(13, 129)) + [256, 512]:
        u = mechanical(m)
        cu, q, p = data(u)
        assert u[:3] == (1, 2, 1) and u[-3:] == (1, 2, 2)
        k0 = high_family_repetitions(m)
        assert q**k0 >= 2*p**k0
        for k in sorted({2, k0, k0+1}):
            row = repeat_data(u, (2,), k)
            d, states = exact_cycle(u*k+(2,))
            assert row['K'] != 0 and row['D'] > abs(row['K'])
            assert d > 1
            # Strict denominator lower bound: den > 3*(3^m)^(k-1)/(2m).
            assert 2*m*d > 3*p**(k-1)
            separated = q**k >= 2*p**k
            minima = None
            if separated:
                assert 10*min(states) > m*d
                minima = sum(states[i] < states[i-1]
                             and states[i] < states[(i+1)%len(states)]
                             for i in range(len(states)))
                assert minima == k*(2*m-sum(u))
                # In the shortcut clock, every a>=2 contributes one descent run.
                assert sum(a >= 2 for a in u*k+(2,)) == k*(sum(u)-m)+1
            high_controls.append(dict(m=m, A=sum(u), k=k,
                                      odd_steps=len(states),
                                      denominator_bits=d.bit_length(),
                                      cancellation=row['cancellation'],
                                      separation_condition=separated,
                                      odd_only_local_minima=minima,
                                      shortcut_local_minima=k*(sum(u)-m)+1))

    # Removing the coprime-block assumption gives a false exact-gcd formula.
    bad = repeat_data((3,), (1, 5), 1)
    assert (bad['C'], bad['D'], bad['K'], bad['cancellation']) == (49, 485, -30, 1)
    assert gcd(bad['D'], bad['K']) == 5
    d, states = exact_cycle((3, 1, 5))
    assert (d, states) == (485, [49, 79, 361])

    return dict(
        status='PASS', schema='cycle-spectrum-C001-v1',
        scope='Finite tests of the stated repetition theorem; not exhaustive cycles at any d.',
        word_box=dict(u_length=[1,4], v_length=[1,3], valuations=[1,4],
                      u_condition='2^sum(u)>3^len(u)',
                      repetitions=[1,2,3,4,5,6,8,12,16]),
        counts=dict(counts), distinct_denominators=len(denominators),
        periodic_controls=period_controls,
        explicit_mod6_family=dict(checked_k=[1,256], examples=repeated_controls),
        high_family_controls=high_controls,
        false_exact_formula=dict(u=[3], v=[1,5], k=1, **bad,
                                 false_prediction=5, states=states),
        source_sha256={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                       for name in ['repetition_spectrum.py', 'check_spectrum.py']}
    )


if __name__ == '__main__':
    if sys.flags.optimize:
        raise SystemExit('Run without -O or PYTHONOPTIMIZE; exact checks use assertions.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='replace the finite receipt')
    args = parser.parse_args()
    receipt = main()
    target = HERE / 'spectrum_audit.json'
    if args.write:
        target.write_text(json.dumps(receipt, indent=2)+'\n')
    else:
        assert receipt == json.loads(target.read_text()), 'finite receipt changed'
    print(json.dumps(dict(status='PASS', counts=receipt['counts'],
                          distinct_denominators=receipt['distinct_denominators'],
                          periodic_controls=len(receipt['periodic_controls']),
                          high_family_controls=len(receipt['high_family_controls']))))
