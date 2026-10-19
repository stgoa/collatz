#!/usr/bin/env python3
"""Exact dyadic-order audit on actual positive raw 3x+d cycles.

This is finite evidence. It records counterexamples to extending C004's
mechanical denominator conclusion after dyadic normalization; it does not
prove that any search or any cycle family is exhausted beyond its domain.
"""

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import gcd
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
MAX_LENGTH = 7
MAX_VALUATION = 4


def require(test, message):
    if not test:
        raise ValueError(message)


def rational(value):
    value = Fraction(value)
    return dict(numerator=value.numerator, denominator=value.denominator)


def stream_add(hasher, value):
    hasher.update(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()+b'\n')


def raw_step(n, d):
    require(type(n) is int and n > 0 and n % 2 == 1 and
            type(d) is int and d > 0 and gcd(d, 6) == 1,
            'invalid raw positive odd input')
    value = 3*n+d
    a = (value & -value).bit_length()-1
    return value >> a, a


def direct(word):
    require(word and all(type(a) is int and a >= 1 for a in word),
            'invalid positive valuation word')
    C, A = 0, 0
    for a in word:
        C = 3*C+2**A
        A += a
    return C, 2**A-3**len(word), A


def mechanical_offset(word):
    A, m = sum(word), len(word)
    base = tuple((j+1)*A//m-j*A//m for j in range(m))
    return next((i for i in range(m) if tuple(word) == base[i:]+base[:i]), None)


def analyze(n, q, word):
    """Analyze one simple reduced cycle in its supplied chronological phase."""
    m = len(word)
    require(len(n) == m and len(set(n)) == m, 'cycle is not simple')
    require(all(gcd(x, q) == 1 for x in n), 'states are not reduced at q')
    C, D, A = direct(word)
    g = gcd(C, D)
    require(D > 0 and q == D//g and n[0] == C//g,
            'cycle/word denominator formula failed')
    for i, x in enumerate(n):
        require(raw_step(x, q) == (n[(i+1) % m], word[i]), 'normalized raw arrow failed')
    L = min(n)
    heights = [(x//L).bit_length()-1 for x in n]
    require(all(2**h*L <= x < 2**(h+1)*L for x, h in zip(n, heights)),
            'dyadic normalization interval failed')
    z = [Fraction(x, 2**h) for x, h in zip(n, heights)]
    F = [Fraction(3*x+q, 2**h) for x, h in zip(n, heights)]
    require(len(set(z)) == m, 'distinct odd numerators have equal mantissas')
    c = [word[i]+heights[(i+1) % m]-heights[i] for i in range(m)]
    require(sum(c) == A and min(c) >= 1, 'normalized exponent sum/positivity failed')
    require(all(F[i] == 2**c[i]*z[(i+1) % m] for i in range(m)),
            'normalized successor identity failed')
    if L >= q:
        require(set(c) <= {1, 2}, 'L>=q binary normalized-exponent bound failed')
    ordered = sorted(range(m), key=lambda i: z[i])
    rank = {i: j for j, i in enumerate(ordered)}
    permutation = [rank[(i+1) % m] for i in ordered]
    shifts = {(p-j) % m for j, p in enumerate(permutation)}
    rotation = len(shifts) == 1
    shift = next(iter(shifts)) if rotation else None
    if rotation:
        require(gcd(shift, m) == 1, 'simple successor rank rotation is not transitive')
    wraps = (0 if m == 1 else
             sum(permutation[j] > permutation[(j+1) % m] for j in range(m)))
    if m > 1:
        require(rotation == (wraps == 1), 'rank rotation/circular descent criterion failed')

    counts, inversion_heights = Counter(equal_scaled_images=0), Counter()
    pairs_digest = sha256()
    first_inversions = []
    for position, i in enumerate(ordered):
        for j in ordered[position+1:]:
            counts['pairs'] += 1
            require(z[i] < z[j], 'sorted mantissa pair not strict')
            delta = F[j]-F[i]
            require(delta != 0, 'equal scaled images inside a simple cycle')
            k, r, threshold = None, None, None
            if heights[j] > heights[i]:
                k = heights[j]-heights[i]
                r = n[j]-2**k*n[i]
                threshold = 3*r-q*(2**k-1)
                require(r > 0 and r % 2 == 1, 'dyadic pair offset not positive odd')
                require(delta == Fraction(threshold, 2**heights[j]),
                        'exact dyadic pair difference failed')
                require((delta < 0) == (3*r < q*(2**k-1)),
                        'exact inversion threshold failed')
                counts['height_increase_pair_identity_checks'] += 1
            else:
                require(delta > 0, 'nonincreasing height produced an inversion')
                counts['nonincreasing_height_order_checks'] += 1
            if delta < 0:
                require(k is not None, 'inversion did not increase height')
                if q == 1:
                    require(k >= 3, 'denominator1 inversion below height gap3')
                counts['inverted_pairs'] += 1
                inversion_heights[k] += 1
                if len(first_inversions) < 8:
                    first_inversions.append(dict(indices=[i, j], height_difference=k,
                        odd_offset=r, threshold=threshold, scaled_image_difference=rational(delta)))
            stream_add(pairs_digest, [i, j, k, r, threshold, delta.numerator, delta.denominator])
    monotone = counts['inverted_pairs'] == 0
    F_span_small = max(F) < 2*min(F)
    original_mechanical = mechanical_offset(word)
    normalized_mechanical = mechanical_offset(c)
    if monotone:
        require(F_span_small, 'monotone images exceed one dyadic range')
        require(rotation and normalized_mechanical is not None,
                'monotone normalized-image rotation/mechanical conclusion failed')
        require(gcd(A, m) == 1, 'monotone primitive normalized cycle totals not coprime')
        require(max(c)-min(c) <= 1, 'monotone image exponents not adjacent')
        require([c[i] for i in ordered] == sorted(c),
                'monotone image exponents not threshold ordered')
    narrow = max(n) < 2*L
    require(narrow == (original_mechanical is not None), 'C004 narrow classification failed')
    if narrow:
        require(g == 1, 'primitive narrow cycle has cancellation')
    return dict(denominator=q, primitive_states=list(n), word=list(word),
        m=m, A=A, C=C, D=D, common_rotation_gcd=g, minimum_numerator=L,
        maximum_minimum_ratio=rational(Fraction(max(n), L)), heights=heights,
        normalized_exponents=c, mantissas=[rational(x) for x in z],
        scaled_images=[rational(x) for x in F], sorted_indices=ordered,
        successor_ranks=permutation, successor_is_rank_rotation=rotation,
        rank_shift=shift, circular_successor_descents=wraps,
        F_is_strictly_increasing=monotone, F_span_less_than2=F_span_small,
        L_ge_denominator=L >= q, normalized_exponents_are_1_or_2=set(c) <= {1, 2},
        narrow=narrow, original_mechanical_offset=original_mechanical,
        normalized_mechanical_offset=normalized_mechanical,
        pair_counts=dict(sorted(counts.items())),
        inversion_height_histogram={str(k): v for k, v in sorted(inversion_heights.items())},
        first_inversions=first_inversions, all_pairs_sha256=pairs_digest.hexdigest())


def add_metrics(counts, row):
    counts['cycles'] += 1
    counts['raw_arrows'] += row['m']
    counts['fixed_cycles' if row['m'] == 1 else 'nontrivial_cycles'] += 1
    for field in ('narrow', 'successor_is_rank_rotation', 'F_is_strictly_increasing',
                  'F_span_less_than2', 'L_ge_denominator', 'normalized_exponents_are_1_or_2'):
        counts[field] += int(row[field])
    counts['wide_cycles'] += int(not row['narrow'])
    counts['gcd_greater_than1'] += int(row['common_rotation_gcd'] > 1)
    counts['denominator1_cycles'] += int(row['denominator'] == 1)
    counts['inverted_cycles'] += int(not row['F_is_strictly_increasing'])
    counts['wide_rank_rotations'] += int(not row['narrow'] and row['successor_is_rank_rotation'])
    counts['wide_monotone_images'] += int(not row['narrow'] and row['F_is_strictly_increasing'])
    counts['wide_monotone_with_gcd_greater_than1'] += int(
        not row['narrow'] and row['F_is_strictly_increasing'] and row['common_rotation_gcd'] > 1)
    counts['rank_rotation_with_inversion'] += int(
        row['successor_is_rank_rotation'] and not row['F_is_strictly_increasing'])
    counts['L_ge_q_rank_rotation_with_inversion'] += int(row['L_ge_denominator'] and
        row['successor_is_rank_rotation'] and not row['F_is_strictly_increasing'])
    counts['original_mechanical'] += int(row['original_mechanical_offset'] is not None)
    counts['normalized_mechanical'] += int(row['normalized_mechanical_offset'] is not None)
    for key, value in row['pair_counts'].items():
        counts[key] += value


def generated_words():
    counts, digest = Counter(), sha256()
    examples = {}
    monotone_cancellation_heights = Counter()
    for m in range(1, MAX_LENGTH+1):
        for word in product(range(1, MAX_VALUATION+1), repeat=m):
            C, D, A = direct(word)
            counts['words'] += 1
            if D < 0:
                counts['negative_D_skipped'] += 1
                stream_add(digest, [word, D, 'negative_D'])
                continue
            counts['positive_words'] += 1
            g = gcd(C, D)
            q, current = D//g, C//g
            states = []
            for a in word:
                states.append(current)
                current, actual_a = raw_step(current, q)
                require(actual_a == a, 'generated word exact valuation failed')
                counts['realization_raw_arrows'] += 1
            require(current == states[0], 'generated word cycle failed to close')
            if len(set(states)) < m:
                counts['proper_power_words'] += 1
                stream_add(digest, [word, q, states, 'proper_power'])
                continue
            counts['primitive_displayed_words'] += 1
            row = analyze(states, q, word)
            add_metrics(counts, row)
            stream_add(digest, row)
            if row['F_is_strictly_increasing'] and g > 1:
                monotone_cancellation_heights[max(row['heights'])] += 1
                if max(row['heights']) == 1:
                    examples.setdefault('two_band_monotone_with_cancellation', row)
            if row['F_is_strictly_increasing'] and g > 1 and 'monotone_with_cancellation' not in examples:
                examples['monotone_with_cancellation'] = row
            if row['L_ge_denominator'] and row['successor_is_rank_rotation'] and not row['F_is_strictly_increasing']:
                examples.setdefault('L_ge_q_rotation_with_inversion', row)
    require(counts['words'] == 21844, 'generated word domain changed')
    return dict(domain=dict(lengths=[1, MAX_LENGTH], valuations=[1, MAX_VALUATION]),
        counts=dict(sorted(counts.items())), examples=examples, verification_sha256=digest.hexdigest(),
        monotone_cancellation_max_height_histogram={str(k): v for k, v in sorted(monotone_cancellation_heights.items())},
        scope='All displayed positive words are realized exactly; repeated words are counted and excluded from simple-cycle order tests. Primitive rotations are counted separately in this generated grid, unlike the deduplicated actual census.')


def pair_controls():
    """Exercise inversion/equality thresholds at q1 without hypothetical cycles."""
    counts, digest = Counter(), sha256()
    witnesses = {}
    for q in (1, 5, 7, 13):
        for p in range(1, 16, 2):
            for k in range(1, 7):
                for r in range(1, min(16, 2**k*p), 2):
                    other = 2**k*p+r
                    delta = Fraction(3*other+q, 2**k)-(3*p+q)
                    threshold = 3*r-q*(2**k-1)
                    require(delta == Fraction(threshold, 2**k), 'generated pair identity failed')
                    counts['pairs'] += 1
                    if q == 1 and delta < 0:
                        require(k >= 3, 'unit-parameter pair inversion below gap3')
                        counts['unit_parameter_inversions'] += 1
                    if delta == 0:
                        require(k % 2 == 0, 'coprime-to3 equal images with odd height gap')
                        require(raw_step(p, q)[0] == raw_step(other, q)[0],
                                'equal scaled images did not have equal odd successors')
                        counts['equal_images_same_successor'] += 1
                    if q == 1 and p == 1 and r == 1 and k in (2, 3):
                        witnesses[str(k)] = dict(q=q, numerators=[p, other], height_difference=k,
                            odd_offset=r, image_difference=rational(delta),
                            odd_successors=[raw_step(p, q)[0], raw_step(other, q)[0]])
                    stream_add(digest, [q, p, k, r, delta.numerator, delta.denominator])
    return dict(domain=dict(q=[1, 5, 7, 13], p_odd=[1, 15], height_gap=[1, 6],
                           r='positive odd r<=15 and r<2^k*p'),
        counts=dict(sorted(counts.items())), unit_parameter_witnesses=witnesses,
        verification_sha256=digest.hexdigest(),
        scope='Pairs of actual odd inputs, not asserted to lie in one cycle. Equality pairs have the same odd successor and therefore cannot both be distinct states of a simple cycle. The q1 inversion restriction is exercised nonvacuously here.')


def report():
    source = json.loads(ACTUAL.read_text())
    fixtures = json.loads(FIXTURES.read_text())['cycles']
    require(source['schema'] == 'C001-actual-raw-cycles-v1', 'wrong source schema')
    require(source['sources']['scanner_sha256'] == sha256(SCANNER.read_bytes()).hexdigest(),
            'source scanner hash mismatch')
    require(source['sources']['fixture_sha256'] == sha256(FIXTURES.read_bytes()).hexdigest(),
            'source fixture hash mismatch')
    cycles = source['cycles']
    require(len(cycles) == 2459 and len({c['d'] for c in cycles}) == 333,
            'actual cycle domain changed')
    fixture_index = {(f['d'], tuple(f['states'])): i+1 for i, f in enumerate(fixtures)}
    require(len(fixture_index) == len(fixtures) == 11, 'fixture domain changed')
    counts, unique, fixture_keys = Counter(), {}, {}
    source_digest = sha256()
    for cycle in cycles:
        d, states, word = cycle['d'], cycle['states'], tuple(cycle['word'])
        n, q = cycle['primitive_states'], cycle['reduced_denominator']
        m = len(word)
        require(len(states) == len(n) == m and len(set(states)) == m,
                'actual cycle not simple')
        require(states[0] == min(states) and n[0] == min(n), 'source orientation not minimum')
        require(d % q == 0 and cycle['actual_scaling'] == d//q and
                states == [(d//q)*x for x in n], 'source normalization failed')
        C, D, A = direct(word)
        require((cycle['C'], cycle['D'], cycle['A'], cycle['m'], cycle['gcd_C_D']) ==
                (C, D, A, m, gcd(C, D)), 'source coefficient metadata mismatch')
        for i, x in enumerate(states):
            require(raw_step(x, d) == (states[(i+1) % m], word[i]), 'actual raw arrow failed')
            require(raw_step(n[i], q) == (n[(i+1) % m], word[i]), 'scaled raw arrow failed')
            counts['actual_raw_arrows'] += 1
            counts['scaled_raw_arrows'] += 1
        counts['actual_cycles'] += 1
        key = (q, tuple(n))
        reference = dict(actual_d=d, actual_minimum=states[0], scale=d//q)
        if key not in unique:
            row = analyze(n, q, word)
            row['source_instances'] = []
            unique[key] = row
        else:
            require(unique[key]['word'] == list(word), 'deduplicated word mismatch')
        unique[key]['source_instances'].append(reference)
        stream_add(source_digest, [d, states, word, q, n, reference])
        fixture_key = d, tuple(states)
        if fixture_key in fixture_index:
            identifier = fixture_index[fixture_key]
            require(tuple(fixtures[identifier-1]['valuations']) == word, 'fixture word mismatch')
            fixture_keys[identifier] = key
    require(set(fixture_keys) == set(range(1, 12)), 'not all historical fixtures exercised')
    require(counts['actual_raw_arrows'] == counts['scaled_raw_arrows'] == 36912,
            'actual arrow coverage changed')
    rows = sorted(unique.values(), key=lambda r: (r['denominator'], r['primitive_states'][0], r['m']))
    normalized_counts, inversion_heights, row_digest = Counter(), Counter(), sha256()
    for row in rows:
        add_metrics(normalized_counts, row)
        inversion_heights.update({int(k): v for k, v in row['inversion_height_histogram'].items()})
        stream_add(row_digest, row)
    require((len(rows), normalized_counts['nontrivial_cycles'], normalized_counts['wide_cycles']) ==
            (1184, 1176, 1165), 'normalized census changed')
    require((normalized_counts['pairs'], normalized_counts['height_increase_pair_identity_checks'],
             normalized_counts['inverted_pairs']) == (739757, 290441, 161213),
            'exact actual pair census changed')
    require((normalized_counts['successor_is_rank_rotation'], normalized_counts['F_is_strictly_increasing'],
             normalized_counts['wide_monotone_with_gcd_greater_than1']) == (162, 71, 26),
            'exact actual order census changed')
    cancellations = [r for r in rows if r['F_is_strictly_increasing'] and r['common_rotation_gcd'] > 1]
    cancellation_heights = Counter(max(r['heights']) for r in cancellations)
    require(dict(cancellation_heights) == {1: 4, 2: 7, 3: 11, 4: 3, 9: 1},
            'actual monotone cancellation height partition changed')
    shortest = min(cancellations, key=lambda r: (r['m'], r['denominator'], r['primitive_states'][0]))
    require((shortest['m'], shortest['denominator'], shortest['common_rotation_gcd']) == (7, 83, 23),
            'shortest actual monotone cancellation witness changed')
    named = {
        'wide_mechanical_inheritance_failure': unique[(5, (19, 31, 49))],
        'large_cancellation_with_monotone_images': unique[(5, (187, 283, 427, 643, 967, 1453,
             1091, 1639, 2461, 1847, 2773, 2081, 781, 587, 883, 1327, 1993))],
        'shortest_actual_monotone_cancellation': shortest,
        'two_band_monotone_cancellation': unique[(233, (1535, 2419, 3745, 2867, 4417, 3371, 5173, 1969))],
        'rank_rotation_with_inversion': unique[(7, (5, 11))],
        'rank_rotation_with_inversion_period4': unique[(35, (13, 37, 73, 127))],
        'L_ge_q_inversion': unique[(11, (13, 25, 43, 35, 29, 49, 79, 31))],
    }
    discrepancy_row = analyze([7, 11], 23, (2, 3))
    require(discrepancy_row['narrow'] and 2**5 > 2*3**2,
            'narrow full-period discrepancy control failed')
    return dict(schema='C005-dyadic-order-v1', baseline_commit=BASELINE,
        status='Exact finite audit; wide monotone rank-rotation cycles can have large numerator cancellation.',
        clock='Raw positive odd-only map; state1 is not absorbed.',
        normalization='Each actual cycle is reduced by its common odd scaling; normalized cycles are deduplicated by reduced denominator and the minimum-oriented numerator cycle. Mantissas z=n/2^h lie in [L,2L), with L=min n, and represent q times the rational mantissas.',
        source_sha256={'check_order.py': sha256(Path(__file__).read_bytes()).hexdigest(),
            'C001/actual_cycles.json': sha256(ACTUAL.read_bytes()).hexdigest(),
            'C001/scan_cycles.py': sha256(SCANNER.read_bytes()).hexdigest(),
            'phase6/cycle_fixtures.json': sha256(FIXTURES.read_bytes()).hexdigest()},
        actual_counts=dict(sorted(counts.items())), normalized_counts=dict(sorted(normalized_counts.items())),
        inversion_height_histogram={str(k): v for k, v in sorted(inversion_heights.items())},
        monotone_cancellation_max_height_histogram={str(k): v for k, v in sorted(cancellation_heights.items())},
        all_actual_sources_sha256=source_digest.hexdigest(), all_normalized_rows_sha256=row_digest.hexdigest(),
        fixture_ids_checked=sorted(fixture_keys),
        fixture_controls=[dict(fixture_id=i, actual_fixture=fixtures[i-1], normalized_cycle=unique[fixture_keys[i]])
                          for i in sorted(fixture_keys)],
        named_obstructions=named, generated_words=generated_words(), pair_controls=pair_controls(),
        narrow_full_period_discrepancy_control=dict(cycle=discrepancy_row,
            statement='A-m*log_2(3)>1 over the complete odd period although H<2L.',
            exact_comparison=dict(left_2_to_A=2**5, right_2_times_3_to_m=2*3**2),
            scope='One period has length2; this does not discard the m/L term in a valid discrepancy estimate.'),
        scope='Every actual arrow and each distinct normalized pair is checked exactly. Full rows, source associations and pair audits enter deterministic digests. The actual sample and generated grid are finite; zero observed cases are not universal exclusions. q1 only has its fixed cycle in these cycle samples; separate input-pair controls exercise the q1 inversion threshold. Written arguments are separate from this receipt.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='write the recomputed exact receipt')
    args = parser.parse_args()
    result = report()
    target = HERE/'order_audit.json'
    if args.write:
        target.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(target.exists(), 'missing receipt; explicit --write is required to create it')
        require(json.loads(target.read_text()) == result, 'saved receipt differs from exact recomputation')
    print(json.dumps(dict(status='PASS', mode='write' if args.write else 'replay',
        actual_counts=result['actual_counts'], normalized_counts=result['normalized_counts'],
        generated_counts=result['generated_words']['counts'], pair_controls=result['pair_controls']['counts']),
        sort_keys=True))


if __name__ == '__main__':
    main()
