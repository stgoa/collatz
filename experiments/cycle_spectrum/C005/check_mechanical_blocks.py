#!/usr/bin/env python3
"""Exact C005 checks for concatenations of rotations of one mechanical base.

The finite phase grid, actual-cycle recognition and growing-base examples
verify their declared domains. The universal exclusion relies on the written
proof; no bounded enumeration proves it by itself.
"""

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import gcd, isqrt
from pathlib import Path
import sys

if sys.flags.optimize:
    raise SystemExit('FAIL: optimized Python is not supported')

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ACTUAL = HERE.parent/'C001/actual_cycles.json'
SCANNER = HERE.parent/'C001/scan_cycles.py'
FIXTURES = ROOT/'experiments/phase6/cycle_fixtures.json'
BASELINE = '61cf54ad52df1caa5cc250b0d1464432ed90b162'
HIGH_PRIMES = (13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
               67, 71, 73, 79, 83, 89, 97)
HIGH_PHASES = (0, 0, 1, 0, 1, 1)


def require(test, message):
    if not test:
        raise ValueError(message)


def rational(value):
    value = Fraction(value)
    return dict(numerator=value.numerator, denominator=value.denominator)


def stream_add(hasher, value):
    hasher.update(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()+b'\n')


def direct(word):
    require(word and all(type(a) is int and a >= 1 for a in word), 'invalid valuation word')
    C, A = 0, 0
    for a in word:
        C = 3*C+2**A
        A += a
    return C, 2**A-3**len(word), A


def raw_step(n, q):
    require(type(n) is int and n > 0 and n % 2 == 1 and
            type(q) is int and q > 0 and gcd(q, 6) == 1, 'invalid raw input')
    value = 3*n+q
    a = (value & -value).bit_length()-1
    return value >> a, a


def primitive_length(word):
    """Length of the shortest repeating block, using the prefix function."""
    prefix = [0]*len(word)
    for i in range(1, len(word)):
        j = prefix[i-1]
        while j and word[i] != word[j]:
            j = prefix[j-1]
        if word[i] == word[j]:
            j += 1
        prefix[i] = j
    period = len(word)-prefix[-1]
    return period if len(word) % period == 0 else len(word)


def mechanical_base(A, m):
    require(A >= m >= 1 and gcd(A, m) == 1 and 2**A > 3**m, 'invalid base totals')
    word = tuple((i+1)*A//m-i*A//m for i in range(m))
    rotations = tuple(word[i:]+word[:i] for i in range(m))
    require(len(set(rotations)) == m and primitive_length(word) == m, 'base is not primitive')
    D = 2**A-3**m
    coefficients = [direct(w)[0] for w in rotations]
    require(all(gcd(C, D) == 1 for C in coefficients), 'mechanical base has cancellation')
    values = [Fraction(C, D) for C in coefficients]
    low, high = min(values), max(values)
    require(high < 2*low, 'mechanical base is not narrow')
    for i, C in enumerate(coefficients):
        require(raw_step(C, D) == (coefficients[(i+1) % m], word[i]),
                'base raw rotation arrow failed')
    return dict(A=A, m=m, D=D, word=word, rotations=rotations,
                values=values, low=low, high=high)


def check_concatenation(base, phases, keep_states=False):
    require(phases and all(type(p) is int and 0 <= p < base['m'] for p in phases),
            'invalid phase sequence')
    b, r = base['m'], len(phases)
    word = sum((base['rotations'][p] for p in phases), ())
    C, D, A = direct(word)
    g = gcd(C, D)
    q, current = D//g, C//g
    low, high = base['low'], base['high']
    lower, upper = low*low/high, high*high/low
    states, boundaries = [], []
    for i, a in enumerate(word):
        value = Fraction(current, q)
        if i % b == 0:
            require(low <= value <= high, 'block boundary outside the fixed-point interval')
            boundaries.append(value)
        require(lower <= value <= upper, 'state outside the prefix envelope')
        states.append(current)
        current, actual_a = raw_step(current, q)
        require(actual_a == a, 'full concatenation exact valuation failed')
    require(current == states[0], 'concatenation did not close')
    L, H = Fraction(min(states), q), Fraction(max(states), q)
    R = high/low
    require(H/L <= R**3 < 8, 'cubic spread bound failed')
    m = len(word)
    period = primitive_length(word)
    repetitions = m//period
    require(r % repetitions == 0 and period % b == 0, 'whole-word period incompatible with base totals')
    require(primitive_length(phases) == period//b, 'phase and valuation primitive periods disagree')
    primitive_word = word[:period]
    Cp, Dp, Ap = direct(primitive_word)
    require(Dp//gcd(Cp, Dp) == q, 'repetition changed the reduced denominator')
    require(gcd(A, m) == r and gcd(Ap, period) == r//repetitions,
            'primitive gcd/repetition identity failed')
    require(len(set(states)) == period, 'raw state period and word period differ')
    exceptional_base = base['word'] == (2,)
    require((q == 1) == exceptional_base, 'denominator1 exclusion or its fixed-point exception failed')
    if q == 1:
        require(primitive_word == (2,) and gcd(Ap, period) == 1,
                'unit denominator did not reduce to the fixed point')
    result = dict(base_A=base['A'], base_m=b, base_D=base['D'], base_word=list(base['word']),
        phases=list(phases), blocks=r, word=list(word), A=A, m=m, C=C, D=D,
        numerator_gcd=g, denominator=q, primitive_period=period, repetitions=repetitions,
        primitive_totals_gcd=gcd(Ap, period), base_low=rational(low), base_high=rational(high),
        base_ratio=rational(R), boundary_states=[rational(x) for x in boundaries],
        state_lower_envelope=rational(lower), state_upper_envelope=rational(upper),
        minimum=rational(L), maximum=rational(H), ratio=rational(H/L),
        cubic_ratio_bound=rational(R**3), fixed_point_exception=exceptional_base)
    states_digest = sha256()
    stream_add(states_digest, states)
    result['raw_numerator_states_sha256'] = states_digest.hexdigest()
    if keep_states:
        result['raw_numerator_states'] = states
    return result


def count_row(counts, row):
    counts['concatenations'] += 1
    counts['raw_arrows'] += row['m']
    counts['boundary_checks'] += row['blocks']
    counts['envelope_checks'] += row['m']
    counts['primitive_words'] += int(row['repetitions'] == 1)
    counts['proper_powers'] += int(row['repetitions'] > 1)
    counts['mixed_phases'] += int(len(set(row['phases'])) > 1)
    counts['at_least_three_distinct_phases'] += int(len(set(row['phases'])) >= 3)
    counts['denominator1_exceptions'] += int(row['denominator'] == 1)
    counts['nontrivial_cancellation'] += int(row['numerator_gcd'] > 1)


def phase_grid():
    counts, digest = Counter(), sha256()
    bases, examples, gcd_histogram = [], {}, Counter()
    for m in range(2, 8):
        for extra in range(3):
            A = (3**m).bit_length()+extra
            if gcd(A, m) != 1:
                counts['noncoprime_base_candidates_skipped'] += 1
                continue
            base = mechanical_base(A, m)
            bases.append(dict(A=A, m=m, D=base['D'], word=list(base['word']),
                              low=rational(base['low']), high=rational(base['high'])))
            counts['bases'] += 1
            for r in range(1, 5):
                for phases in product(range(m), repeat=r):
                    row = check_concatenation(base, phases)
                    count_row(counts, row)
                    gcd_histogram[row['primitive_totals_gcd']] += 1
                    stream_add(digest, row)
                    if len(set(phases)) >= 3:
                        examples.setdefault('three_distinct_phases', check_concatenation(base, phases, True))
    for A in range(2, 8):
        base = mechanical_base(A, 1)
        for r in range(1, 9):
            row = check_concatenation(base, (0,)*r)
            counts['fixed_base_controls'] += 1
            counts['fixed_base_unit_controls'] += int(row['denominator'] == 1)
            stream_add(digest, ['fixed_base_control', row])
    require(counts['concatenations'] == 9664 and counts['raw_arrows'] == 227860,
            'phase grid coverage changed')
    require(counts['denominator1_exceptions'] == 0 and counts['fixed_base_unit_controls'] == 8,
            'fixed-point exception coverage changed')
    examples['two_block_q59'] = check_concatenation(mechanical_base(5, 3), (0, 1), True)
    return dict(domain=dict(base_lengths=[2, 7], base_totals='bit_length(3^m)+e, e=0,1,2; gcd(A,m)=1',
        block_counts=[1, 4], phases='every element of {0,...,m-1}^r',
        fixed_base_controls='base(A), A=2,...,7, each repeated r=1,...,8'),
        bases=bases, counts=dict(sorted(counts.items())),
        primitive_gcd_histogram={str(k): v for k, v in sorted(gcd_histogram.items())},
        examples=examples, verification_sha256=digest.hexdigest(),
        scope='Exhaustive displayed phase words in this finite grid, including repeated whole words. Rotations and powers are counted explicitly and do not represent additional primitive cycles.')


def high_family():
    counts, rows, digest = Counter(), [], sha256()
    for m in HIGH_PRIMES:
        require(m >= 13 and all(m % d for d in range(2, isqrt(m)+1)), 'declared m not prime')
        A = (3**m).bit_length()
        require(2**(A-1) < 3**m < 2**A and gcd(A, m) == 1, 'upper prime approximation failed')
        base = mechanical_base(A, m)
        require(set(base['word']) <= {1, 2} and base['low'] > Fraction(m, 6),
                'nearest-upper mechanical minimum or valuation bound failed')
        row = check_concatenation(base, HIGH_PHASES, True)
        require(row['repetitions'] == 1 and row['primitive_totals_gcd'] == 6,
                'six-phase word is not primitive with gcd6')
        require(Fraction(**row['minimum']) > Fraction(m, 12), 'growing minimum bound failed')
        states, q = row['raw_numerator_states'], row['denominator']
        shortcut = []
        for n, a in zip(states, row['word']):
            shortcut.append(n)
            value = (3*n+q)//2
            for unused in range(a-1):
                shortcut.append(value)
                require(value % 2 == 0, 'shortcut intermediate state not even')
                value //= 2
        require(len(shortcut) == row['A'] and len(set(shortcut)) == len(shortcut),
                'primitive shortcut expansion length or distinctness failed')
        minima = sum(shortcut[i] < shortcut[i-1] and shortcut[i] < shortcut[(i+1) % len(shortcut)]
                     for i in range(len(shortcut)))
        require(minima == sum(a >= 2 for a in row['word']) == 6*(A-m),
                'shortcut local-minimum formula failed')
        for i, n in enumerate(shortcut):
            successor = (3*n+q)//2 if n % 2 else n//2
            require(successor == shortcut[(i+1) % len(shortcut)], 'shortcut raw arrow failed')
        row['shortcut_local_minima'] = minima
        row['shortcut_period'] = len(shortcut)
        row['minimum_lower_bound'] = rational(Fraction(m, 12))
        shortcut_digest = sha256()
        stream_add(shortcut_digest, shortcut)
        row['shortcut_states_sha256'] = shortcut_digest.hexdigest()
        count_row(counts, row)
        counts['shortcut_arrows'] += len(shortcut)
        counts['shortcut_local_minima'] += minima
        stream_add(digest, row)
        if m != HIGH_PRIMES[0]:
            del row['raw_numerator_states']
        rows.append(row)
    return dict(domain=dict(base_prime_lengths=list(HIGH_PRIMES),
        base_total='bit_length(3^m)', phase_word=list(HIGH_PHASES)), counts=dict(sorted(counts.items())),
        cases=rows, verification_sha256=digest.hexdigest(),
        scope='Twenty finite examples of the written all-prime family. Every displayed six-block word is primitive; odd-only period6m and shortcut period6A are distinguished. Local minima are counted on the actual expanded shortcut cycle. Every full row including all odd states enters the verification digest; only the smallest case stores its full state array, and every case stores the reconstructible word, numerator, denominator and state digests. No literature comparison follows from the counts alone.')


def actual_cycles():
    source = json.loads(ACTUAL.read_text())
    fixtures = json.loads(FIXTURES.read_text())['cycles']
    require(source['schema'] == 'C001-actual-raw-cycles-v1', 'wrong actual source schema')
    require(source['sources']['scanner_sha256'] == sha256(SCANNER.read_bytes()).hexdigest() and
            source['sources']['fixture_sha256'] == sha256(FIXTURES.read_bytes()).hexdigest(),
            'actual source dependencies changed')
    cycles = source['cycles']
    require(len(cycles) == 2459 and len({c['d'] for c in cycles}) == 333, 'actual source domain changed')
    fixture_index = {(f['d'], tuple(f['states'])): i+1 for i, f in enumerate(fixtures)}
    require(len(fixture_index) == len(fixtures) == 11, 'fixture domain changed')
    source_counts, counts, seen, fixture_rows = Counter(), Counter(), {}, {}
    digest, matches = sha256(), []
    for cycle in cycles:
        d, states, word = cycle['d'], cycle['states'], tuple(cycle['word'])
        q, n = cycle['reduced_denominator'], cycle['primitive_states']
        require(len(set(states)) == len(states) == len(word) == len(n), 'source not primitive simple')
        require(states[0] == min(states) and d % q == 0 and
                states == [(d//q)*x for x in n], 'source orientation/scaling failed')
        C, D, A = direct(word)
        require(D > 0 and D//gcd(C, D) == q and C//gcd(C, D) == n[0],
                'actual source denominator formula failed')
        for i, x in enumerate(states):
            require(raw_step(x, d) == (states[(i+1) % len(word)], word[i]), 'actual raw arrow failed')
            require(raw_step(n[i], q) == (n[(i+1) % len(word)], word[i]), 'reduced raw arrow failed')
            source_counts['actual_raw_arrows'] += 1
            source_counts['reduced_raw_arrows'] += 1
        source_counts['actual_cycles'] += 1
        key = q, tuple(n)
        if key not in seen:
            m = len(word)
            r = gcd(A, m)
            base = mechanical_base(A//r, m//r)
            phase_lookup = {w: i for i, w in enumerate(base['rotations'])}
            recognized = []
            for offset in range(base['m']):
                rotated = word[offset:]+word[:offset]
                phases = [phase_lookup.get(rotated[i*base['m']:(i+1)*base['m']]) for i in range(r)]
                counts['alignment_tests'] += 1
                if all(p is not None for p in phases):
                    row = check_concatenation(base, phases, True)
                    expected = n[offset:]+n[:offset]
                    require(row['raw_numerator_states'] == expected and row['denominator'] == q,
                            'recognized actual word does not reproduce actual states')
                    recognized.append(dict(offset=offset, phases=phases))
                    counts['recognized_alignments'] += 1
            matched = bool(recognized)
            counts['normalized_cycles'] += 1
            counts['recognized_cycles'] += int(matched)
            counts['recognized_nontrivial_cycles'] += int(matched and m > 1)
            counts['recognized_multiblock_cycles'] += int(matched and r > 1)
            item = dict(denominator=q, primitive_states=n, word=list(word),
                        recognized=matched, base_m=base['m'], base_A=base['A'], blocks=r,
                        successful_alignments=recognized)
            if matched:
                first = recognized[0]
                item['checked_concatenation'] = check_concatenation(base, first['phases'], True)
                matches.append(item)
            seen[key] = item
            stream_add(digest, item)
        if seen[key]['recognized']:
            source_counts['recognized_source_instances'] += 1
        fixture_key = d, tuple(states)
        if fixture_key in fixture_index:
            identifier = fixture_index[fixture_key]
            require(tuple(fixtures[identifier-1]['valuations']) == word, 'fixture valuation mismatch')
            fixture_rows[identifier] = dict(fixture=fixtures[identifier-1], normalized=seen[key])
    require(set(fixture_rows) == set(range(1, 12)), 'not all fixtures exercised')
    require(source_counts['actual_raw_arrows'] == 36912 and len(seen) == 1184,
            'actual census coverage changed')
    require((counts['recognized_cycles'], counts['recognized_nontrivial_cycles'],
             counts['recognized_multiblock_cycles']) == (22, 14, 3), 'mechanical-block recognition census changed')
    return dict(source_counts=dict(sorted(source_counts.items())), normalized_counts=dict(sorted(counts.items())),
        recognized_cycles=matches,
        fixture_controls=[dict(fixture_id=i, **fixture_rows[i]) for i in sorted(fixture_rows)],
        verification_sha256=digest.hexdigest(),
        scope='Every actual source and all eleven raw fixtures are replayed. On each distinct normalized cycle, all alignment offsets modulo the only possible primitive base length m/gcd(A,m) are tested; shifts by a whole base block merely rotate the phase sequence. Nonmembers remain valid cycles and are not excluded.')


def report():
    return dict(schema='C005-mechanical-rotation-blocks-v1', baseline_commit=BASELINE,
        status='Exact finite checks of the written arbitrary-concatenation theorem; no universal inference from the census alone.',
        clock='Positive raw odd-only cycles, with separately expanded shortcut clocks for the high family; state1 is not absorbed.',
        source_sha256={'check_mechanical_blocks.py': sha256(Path(__file__).read_bytes()).hexdigest(),
            'C001/actual_cycles.json': sha256(ACTUAL.read_bytes()).hexdigest(),
            'C001/scan_cycles.py': sha256(SCANNER.read_bytes()).hexdigest(),
            'phase6/cycle_fixtures.json': sha256(FIXTURES.read_bytes()).hexdigest(),
            'C005/check_order.py': sha256((HERE/'check_order.py').read_bytes()).hexdigest(),
            'C005/order_audit.json': sha256((HERE/'order_audit.json').read_bytes()).hexdigest()},
        phase_grid=phase_grid(), high_family=high_family(), actual_cycles=actual_cycles(),
        scope='One primitive positive mechanical base, all blocks rotations of that same base. Different base totals or arbitrary nonmechanical blocks are outside this theorem. Repetitions reduce to their primitive word. The base(2) gives denominator1 and must survive. The written q1 spread<8 rigidity step is not proved by this script.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='write the recomputed exact receipt')
    args = parser.parse_args()
    result = report()
    target = HERE/'mechanical_blocks_audit.json'
    if args.write:
        target.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(target.exists(), 'missing receipt; explicit --write is required')
        require(json.loads(target.read_text()) == result, 'saved receipt differs from exact recomputation')
    print(json.dumps(dict(status='PASS', mode='write' if args.write else 'replay',
        phase_grid=result['phase_grid']['counts'], high_family=result['high_family']['counts'],
        actual_sources=result['actual_cycles']['source_counts'],
        actual_normalized=result['actual_cycles']['normalized_counts']), sort_keys=True))


if __name__ == '__main__':
    main()
