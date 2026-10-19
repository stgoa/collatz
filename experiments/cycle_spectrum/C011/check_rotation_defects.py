#!/usr/bin/env python3
"""Exact rotation defects on stored raw cycles and bounded generated controls.

No new seed census. Zero defects from repeated words remain explicit. A valid
divisibility bound is distinguished from an exact gcd formula throughout.
"""
import argparse
from collections import Counter
from hashlib import sha256
import importlib.util
import json
from math import gcd
from pathlib import Path
import sys

if sys.flags.optimize:
    raise SystemExit('FAIL: optimized Python is not supported')

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
C009 = HERE.parent/'C009/check_excursions.py'
spec = importlib.util.spec_from_file_location('c009_raw_cycle_helpers', C009)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
require = old.require


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def strip23(value):
    require(type(value) is int and value != 0, 'zero has no unit-stripped bound')
    value = abs(value)
    a = (value & -value).bit_length()-1
    value >>= a
    b = 0
    while value % 3 == 0:
        value //= 3
        b += 1
    return value, a, b


def direct_data(word):
    """Direct weighted sum, independently of the historical recurrence helper."""
    require(word and all(type(a) is int and a >= 1 for a in word),
            'positive valuation word required')
    P = [0]
    for a in word:
        P.append(P[-1]+a)
    m = len(word)
    C = sum(3**(m-1-j)*2**P[j] for j in range(m))
    D = 2**P[-1]-3**m
    return dict(m=m, A=P[-1], C=C, D=D, prefixes=P)


def rotate(word, k):
    return word[k:]+word[:k]


def primitive_period(word):
    m = len(word)
    return next(p for p in range(1, m+1) if m % p == 0 and word == word[:p]*(m//p))


def two_arc_check(word, rotated, positions, g, D):
    require(len(positions) == 2, 'two mismatch positions required')
    first, second = positions
    require(word[first] == rotated[second] and word[second] == rotated[first],
            'two mismatches are not an exponent swap')
    arcs = []
    m = len(word)
    for start, end in ((first, second), (second, first)):
        base, alt = (word, rotated) if word[start] < rotated[start] else (rotated, word)
        base, alt = rotate(base, start), rotate(alt, start)
        ell = (end-start) % m
        a, r = base[0], alt[0]-base[0]
        require(r > 0 and base[ell] == a+r and alt[ell] == a,
                'oriented two-arc exponent pattern failed')
        interval = base[1:ell+1]
        C_arc = direct_data(interval)['C']
        adjusted = interval[:-1]+[a]
        require(direct_data(adjusted)['C'] == C_arc,
                'changing the last interval valuation changed its intercept')
        delta = direct_data(alt)['C']-direct_data(base)['C']
        exact = (2**r-1)*2**a*3**(m-1-ell)*C_arc
        require(delta == exact > 0, 'two-arc intercept identity failed')
        bound, v2, v3 = strip23(delta)
        stripped_product = strip23((2**r-1)*C_arc)[0]
        require(bound == stripped_product and bound % g == 0,
                'two-arc unit-stripped divisibility failed')
        arcs.append(dict(start=start, length=ell, first_exponent=a, amplitude=r,
            interval_word=interval, interval_intercept=C_arc, oriented_delta=delta,
            interval_total=sum(interval), adjusted_interval_total=sum(adjusted),
            stripped_bound=bound, stripped_v2=v2, stripped_v3=v3))
    combined = gcd(arcs[0]['stripped_bound'], arcs[1]['stripped_bound'])
    require(combined % g == 0, 'combined two-arc bound failed')
    adjacent = min(a['length'] for a in arcs) == 1
    amplitude = arcs[0]['amplitude']
    A = sum(word)
    kappa = 2**amplitude-1
    require(sum(a['interval_total'] for a in arcs) == A+amplitude and
            sum(a['adjusted_interval_total'] for a in arcs) == A-amplitude,
            'two-arc endpoint accounting failed')
    for arc in arcs:
        require(arc['interval_intercept'] <
                2**(arc['adjusted_interval_total']-arc['length'])*3**arc['length'],
                'adjusted interval intercept envelope failed')
    weak_quadratic = kappa**2*2**(A-m)*3**m
    strong_quadratic = kappa**2*2**(A-m-amplitude)*3**m
    amplitude_free_quadratic = 2**(2*A-2*m)*3**m
    require(g**2 < strong_quadratic <= weak_quadratic and
            D**2 < (D//g)**2*strong_quadratic,
            'two-arc quadratic cancellation or denominator bound failed')
    require(amplitude <= A-m and strong_quadratic < amplitude_free_quadratic and
            g**2 < amplitude_free_quadratic,
            'amplitude-free quadratic consequence failed')
    if adjacent:
        short_bound = strip23(2**amplitude-1)[0]
        require(short_bound % g == 0 and combined <= short_bound,
                'adjacent mismatch bound failed')
        if amplitude == 1:
            require(g == 1, 'adjacent unit swap should have no cancellation')
    return dict(arcs=arcs, combined_bound=combined, bound_to_g=combined//g,
        gcd_with_D=gcd(D, combined), adjacent=adjacent, amplitude=amplitude,
        kappa=kappa, weak_quadratic_upper_bound=weak_quadratic,
        adjusted_quadratic_upper_bound=strong_quadratic,
        amplitude_free_quadratic_upper_bound=amplitude_free_quadratic,
        strict_denominator_exclusion=D > combined)


def rotation_audit(word, states=None, raw_q=None):
    data = direct_data(word)
    m, A, C, D, P = (data[k] for k in ('m', 'A', 'C', 'D', 'prefixes'))
    require(D > 0, 'positive cycle denominator required')
    g, records = gcd(C, D), []
    q = D//g
    require(gcd(g, 6) == 1 and gcd(q, 6) == 1, 'unexpected nonunit factor')
    if raw_q is not None:
        require(raw_q == q, 'provided reduced denominator changed')
    prefix_C = [0]
    for j in range(m):
        prefix_C.append(3*prefix_C[-1]+2**P[j])
    require(prefix_C[-1] == C, 'independent intercept calculations disagree')
    intercepts = [C]
    for k in range(1, m):
        v = rotate(word, k)
        other = direct_data(v)
        require(other['A'] == A and other['D'] == D, 'rotation changed totals')
        delta_terms = [3**(m-1-j)*(2**other['prefixes'][j]-2**P[j]) for j in range(m)]
        delta = sum(delta_terms)
        require(delta == other['C']-C, 'direct signed prefix-power difference failed')
        require(2**P[k]*delta == D*prefix_C[k]-(2**P[k]-3**k)*C,
                'exact rotation cut identity failed')
        cut_gcd = gcd(q, 2**P[k]-3**k)
        require(gcd(D, delta) == g*cut_gcd, 'rotation cut gcd factor failed')
        positions = [j for j in range(m) if word[j] != v[j]]
        amplitudes = [v[j]-word[j] for j in positions]
        require(sum(amplitudes) == 0 and bool(positions) == bool(delta),
                'zero rotation differs from word repetition')
        record = dict(shift=k, mismatch_count=len(positions), mismatch_positions=positions,
            signed_amplitudes=amplitudes, amplitude_l1=sum(abs(a) for a in amplitudes),
            amplitude_max=max((abs(a) for a in amplitudes), default=0),
            prefix_discrepancy_support=sum(x != y for x, y in zip(P[:-1], other['prefixes'][:-1])),
            intercept_difference=delta, cut_gcd_factor=cut_gcd,
            difference_gcd_with_D=gcd(D, delta))
        if delta:
            bound, v2, v3 = strip23(delta)
            require(bound % g == 0 and gcd(D, bound) == g*cut_gcd,
                    'unit stripping changed the gcd obstruction')
            record.update(stripped_bound=bound, stripped_v2=v2, stripped_v3=v3,
                          bound_to_g=bound//g, strict_denominator_exclusion=D > bound)
            if len(positions) == 2:
                record['two_arc'] = two_arc_check(word, v, positions, g, D)
        records.append(record)
        intercepts.append(other['C'])
    generated_states = [value//g for value in intercepts]
    require(all(value % g == 0 for value in intercepts), 'rotation loses common cancellation')
    require(all(gcd(n, q) == 1 and n > 0 and n % 2 for n in generated_states),
            'generated rational-cycle numerator is not reduced positive odd')
    for j, n in enumerate(generated_states):
        require(old.step(n, q) == (generated_states[(j+1) % m], word[j]),
                'generated raw cycle arrow failed')
    if states is not None:
        require(generated_states == states, 'rotation intercepts differ from actual states')
    period = primitive_period(word)
    require(len(set(generated_states)) == period,
            'word repetition and distinct-state count disagree')
    nonzero = [r for r in records if r['mismatch_count']]
    h2 = [r for r in nonzero if r['mismatch_count'] == 2]
    best = min(nonzero, key=lambda r: (r['mismatch_count'], r['amplitude_max'], r['shift'])) if nonzero else None
    summary = dict(m=m, A=A, C=C, D=D, g=g, q=q, minimum=min(generated_states),
        primitive_period=period, repetition_count=m//period, word=word,
        states=generated_states, zero_rotations=sum(not r['mismatch_count'] for r in records),
        minimum_nonzero_hamming=None if best is None else best['mismatch_count'],
        minimum_defect_witness=best, two_defect_rotations=len(h2),
        smallest_stripped_difference=min((r['stripped_bound'] for r in nonzero), default=None),
        smallest_two_arc_bound=min((r['two_arc']['combined_bound'] for r in h2), default=None),
        all_rotation_records_sha256=digest(records))
    return summary, records


def actual_corpus():
    source = json.loads(old.ACTUAL.read_text())['cycles']
    additions = json.loads(old.C007.read_text())['small_parameter_census']['new_normalized_cycles']
    fixtures = json.loads(old.FIXTURES.read_text())['cycles']
    require(len(source) == 2459 and len(additions) == 1 and len(fixtures) == 11,
            'stored cycle corpus changed')
    unique, source_index, raw_records = {}, {}, []
    raw_arrows = scaled = 0
    for raw in source:
        q, n, d = raw['reduced_denominator'], raw['primitive_states'], raw['d']
        row = old.certificate(q, n)
        require(d % q == 0 and raw['states'] == [d//q*x for x in n] and raw['word'] == row['word'],
                'raw source scaling failed')
        for i, x in enumerate(raw['states']):
            require(old.step(x, d) == (raw['states'][(i+1) % len(n)], row['word'][i]),
                    'raw source arrow failed')
        unique[q, tuple(n)] = row
        source_index[d, tuple(raw['states'])] = row
        raw_records.append([d, q, raw['states'], raw['word']])
        raw_arrows += len(n)
        scaled += d//q > 1
    require(len(unique) == 1184 and raw_arrows == 36912 and scaled == 1275,
            'raw corpus coverage changed')
    for raw in additions:
        row = old.certificate(raw['q'], raw['states'])
        unique[row['q'], tuple(row['states'])] = row
    require(len(unique) == 1185, 'normalized corpus coverage changed')
    summaries, all_records_digest, counts, by_hamming = [], sha256(), Counter(), {}
    for row in sorted(unique.values(), key=lambda r: (r['q'], r['L'])):
        summary, records = rotation_audit(row['word'], row['states'], row['q'])
        require(summary['primitive_period'] == row['m'] and summary['zero_rotations'] == 0,
                'stored primitive cycle has a repeated word')
        summaries.append(summary)
        all_records_digest.update(json.dumps([row['q'], row['L'], records], sort_keys=True,
                                             separators=(',', ':')).encode()+b'\n')
        counts['normalized_cycles'] += 1
        counts['normalized_arrows'] += row['m']
        counts['nonfixed_cycles'] += row['m'] > 1
        counts['rotations'] += len(records)
        counts['word_positions_compared'] += row['m']*len(records)
        counts['cycles_with_two_defects'] += bool(summary['two_defect_rotations'])
        counts['cycles_with_unit_two_defects'] += any(r['mismatch_count'] == 2 and r['amplitude_max'] == 1 for r in records)
        counts['cycles_with_adjacent_unit_defects'] += any(r.get('two_arc', {}).get('adjacent') and r['amplitude_max'] == 1 for r in records)
        counts['cycles_with_difference_bound_below_D'] += any(r['strict_denominator_exclusion'] for r in records)
        counts['cycles_with_two_arc_bound_below_D'] += any(r.get('two_arc', {}).get('strict_denominator_exclusion') for r in records)
        for r in records:
            counts['zero_rotation_differences'] += r['intercept_difference'] == 0
            counts['difference_gcd_has_extra_factor'] += r['cut_gcd_factor'] > 1
            counts['two_defect_rotations'] += r['mismatch_count'] == 2
            if 'two_arc' in r:
                counts['two_arc_identities'] += 2
                counts['weak_quadratic_bounds'] += 1
                counts['adjusted_quadratic_bounds'] += 1
                counts['amplitude_free_quadratic_bounds'] += 1
                counts['two_arc_gcd_has_extra_factor'] += r['two_arc']['gcd_with_D'] > summary['g']
        h = summary['minimum_nonzero_hamming']
        if h is not None:
            group = by_hamming.setdefault(str(h), dict(cycles=0, max_g=0, max_g_example=None))
            group['cycles'] += 1
            if summary['g'] > group['max_g']:
                group['max_g'] = summary['g']
                group['max_g_example'] = dict(q=summary['q'], L=summary['minimum'], m=summary['m'])
    controls = []
    index = {(r['q'], r['minimum']): r for r in summaries}
    for i, fixture in enumerate(fixtures):
        row = source_index[fixture['d'], tuple(fixture['states'])]
        require(row['word'] == fixture['valuations'], 'fixture valuations changed')
        controls.append(dict(fixture_id=i+1, d=fixture['d'], states=fixture['states'],
            q=row['q'], scale=fixture['d']//row['q'],
            normalized_audit_sha256=digest(index[row['q'], row['L']])))
    selected = [index[key] for key in ((1, 1), (5, 19), (7, 5), (13, 283), (13, 259),
                                      (35, 13), (59, 221), (59, 217), (71, 2585),
                                      (233, 1907), (359, 209), (505, 59), (539, 31), (29, 7055))]
    h2 = [r for r in summaries if r['minimum_nonzero_hamming'] == 2]
    require(len(h2) == 108 and max(r['g'] for r in h2) == 485,
            'low-defect actual controls changed')
    require(index[359, 209]['g'] == 73 and index[59, 221]['g'] == 5,
            'unit-amplitude actual controls changed')
    return dict(source_cycles=2459, source_parameters=len({r['d'] for r in source}),
        source_raw_arrows=raw_arrows, scaled_source_instances=scaled,
        C007_added_cycles=1, counts=dict(sorted(counts.items())),
        minimum_hamming_groups=by_hamming, fixture_controls=controls, selected_controls=selected,
        all_source_checks_sha256=digest(raw_records), all_summaries_sha256=digest(summaries),
        all_rotation_records_sha256=all_records_digest.hexdigest(),
        scope='All stored actual raw cycles are retained. Maximum-g statements are only over this finite stored sample. The full all-rotation bounds are identities or necessary divisibility bounds, not a new universal cycle exclusion.')


def phi(n):
    result, remaining, p = n, n, 2
    while p*p <= remaining:
        if remaining % p == 0:
            result -= result//p
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        result -= result//remaining
    return result


def generated_controls():
    moduli = [5, 7, 11, 13, 25, 35, 49, 55, 65, 77, 91, 125]
    ts = sorted(set(range(1, 49)) | {phi(M) for M in moduli} | {100})
    family, selected, transcript, counts = [], [], sha256(), Counter()
    for t in ts:
        word = [1]*t+[2]*(2*t)
        summary, rotations = rotation_audit(word)
        C = 3**(3*t)-2**(t+1)*3**(2*t)+2**(5*t)
        D = 2**(5*t)-3**(3*t)
        g = gcd(3**t-2**t, 4**t-1)
        first = rotations[0]
        require(summary['C'] == C and summary['D'] == D and summary['g'] == g,
                'two-run family closed cancellation formula failed')
        require(summary['primitive_period'] == 3*t and summary['minimum'] == C//g and
                min(summary['states']) > summary['q'], 'two-run primitive minimum/domain failed')
        require(first['mismatch_count'] == 2 and first['amplitude_max'] == 1,
                'two-run shift-one defect changed')
        require(first['two_arc']['combined_bound'] % g == 0,
                'two-run arc bound failed')
        record = dict(t=t, m=3*t, A=5*t, g=g, D_bits=D.bit_length(), q_bits=(D//g).bit_length(),
            minimum_numerator_bits=(C//g).bit_length(), shift_one_defect_count=2,
            shift_one_amplitude=1, arc_combined_bound=first['two_arc']['combined_bound'],
            primitive=True, all_rational_states_greater_than_one=True,
            all_rotation_records_sha256=summary['all_rotation_records_sha256'])
        family.append(record)
        transcript.update(json.dumps([t, summary], sort_keys=True, separators=(',', ':')).encode()+b'\n')
        counts['family_words'] += 1
        counts['family_raw_arrows'] += 3*t
        counts['family_rotation_checks'] += len(rotations)
        if t in (1, 2, 4, 20, 100):
            selected.append(dict(**record, C=C, D=D, q=D//g,
                                 first_rotation=first))
    lookup = {r['t']: r for r in family}
    modular = []
    for M in moduli:
        t = phi(M)
        require(gcd(M, 6) == 1 and pow(2, t, M) == pow(3, t, M) == 1 and
                lookup[t]['g'] % M == 0, 'prescribed cancellation modulus failed')
        modular.append(dict(M=M, t=t, g=lookup[t]['g'], multiplier=lookup[t]['g']//M))
    repeated = []
    repeated_words = [[2]*k for k in range(1, 9)] + [[3]*k for k in range(1, 7)] + [[1, 2, 2]*k for k in range(2, 7)]
    for word in repeated_words:
        summary, rotations = rotation_audit(word)
        p = summary['primitive_period']
        zero_shifts = [r['shift'] for r in rotations if not r['mismatch_count']]
        require(zero_shifts == list(range(p, len(word), p)),
                'zero rotations do not match repetitions')
        repeated.append(dict(word=word, primitive_period=p, repetition_count=len(word)//p,
            q=summary['q'], g=summary['g'], zero_shifts=zero_shifts,
            all_rotation_records_sha256=summary['all_rotation_records_sha256']))
    extra_factor, _ = rotation_audit([3, 7])
    require(extra_factor['g'] == 1 and extra_factor['q'] == 1015 and
            extra_factor['minimum_defect_witness']['stripped_bound'] == 5 and
            extra_factor['minimum_defect_witness']['cut_gcd_factor'] == 5,
            'extra cut-factor control changed')
    return dict(family_cases=family, selected_family_cases=selected,
        prescribed_modulus_controls=modular, repeated_word_controls=repeated,
        extra_gcd_factor_control=extra_factor, counts=dict(sorted(counts.items())),
        full_generated_records_sha256=transcript.hexdigest(),
        scope='The bounded family checks are examples supporting the separately written all-M obstruction. The arbitrary-M proof is not inferred from these twelve moduli. Repetitions are kept separate, including every repetition of the trivial word(2). The two-defect word(3,7) retains an extra factor5 in the cut gcd, refuting an unqualified equality with g.')


def marker_family():
    cases, transcript, counts = [], sha256(), Counter()
    for r in range(1, 9):
        n = 2**r-1
        A0 = (3**n).bit_length()
        b = [(j+1)*A0//n-j*A0//n for j in range(n)]
        require(set(b) <= {1, 2} and sum(b) == A0 and 3**n < 2**A0 < 2*3**n,
                'lower mechanical base totals failed')
        base = direct_data(b)
        require(12*base['C'] > n*2**A0, 'mechanical affine-intercept lower bound failed')
        require(all(2*3**j > 2**base['prefixes'][j] for j in range(n+1)),
                'mechanical prefix slope lower bound failed')
        word = [3]+b+[4]+b
        summary, rotations = rotation_audit(word)
        m, A, D, g, q = (summary[k] for k in ('m', 'A', 'D', 'g', 'q'))
        require(m == 2*n+2 == 2**(r+1) and A == 2*A0+7 and gcd(A, m) == 1,
                'marker family coprime totals failed')
        require(word.count(3) == word.count(4) == 1 and summary['primitive_period'] == m,
                'unique marker primitivity failed')
        half = rotations[n]
        require(half['shift'] == n+1 and half['mismatch_count'] == 2 and half['amplitude_max'] == 1,
                'marker half-period unit defect failed')
        require(9*2**A > 128*3**m and 9*D > 119*3**m,
                'marker expansion ratio failed')
        require(D**2 > half['two_arc']['weak_quadratic_upper_bound'] and q > 1,
                'marker quadratic denominator exclusion failed')
        require(128*min(summary['states']) > n*q,
                'marker minimum rational state lower bound failed')
        shortcut_minima = sum(a >= 2 for a in word)
        require(shortcut_minima == 2*(A0-n)+2,
                'marker shortcut local minimum count failed')
        saved = dict(r=r, n=n, m=m, A0=A0, A=A, gcd_totals=1,
            primitive=True, unique_markers=[3, 4], shift=n+1,
            mismatch_count=2, mismatch_amplitude=1,
            reduced_denominator_greater_than_one=True,
            minimum_rational_state_strictly_greater_than_n_over_128=True,
            shortcut_local_minima=shortcut_minima,
            C_bits=summary['C'].bit_length(), D_bits=D.bit_length(),
            g_bits=g.bit_length(), q_bits=q.bit_length(),
            g_sha256=sha256(str(g).encode()).hexdigest(),
            word_sha256=digest(word), states_sha256=digest(summary['states']),
            full_rotation_records_sha256=summary['all_rotation_records_sha256'])
        if r == 1:
            saved['small_exact_control'] = dict(word=word, states=summary['states'],
                C=summary['C'], D=D, g=g, q=q, half_rotation=half)
        cases.append(saved)
        transcript.update(json.dumps(summary, sort_keys=True, separators=(',', ':')).encode()+b'\n')
        counts['cases'] += 1
        counts['raw_cycle_arrows'] += m
        counts['all_rotation_checks'] += len(rotations)
        counts['mechanical_prefix_bounds'] += n+1
        counts['half_period_two_arc_checks'] += 1
    return dict(cases=cases, counts=dict(sorted(counts.items())),
        full_audits_sha256=transcript.hexdigest(),
        scope='Eight bounded examples of the separately written marker family. Full raw arrows and all rotations were checked. The shortcut local-minimum count is separate from odd-only minima. No published lower bound or all-size analytic theorem is independently verified by these examples.')


def rejection_controls():
    probes = [lambda: rotation_audit([0, 3]), lambda: rotation_audit([1]),
              lambda: strip23(0), lambda: rotation_audit([2], states=[3], raw_q=1)]
    count = 0
    for probe in probes:
        try:
            probe()
        except ValueError:
            count += 1
        else:
            raise ValueError('invalid rotation control was accepted')
    return dict(rejected_inputs=count,
        scope='Reject nonpositive valuations, negative cycle denominator, zero unit-stripping and a wrong supplied raw state. Repeated words are analyzed, not rejected.')


def report():
    paths = [Path(__file__), C009, old.ACTUAL, old.C007, old.FIXTURES]
    return dict(schema='C011-rotation-defects-v1', status='PASS',
        clock='Raw positive odd-only cycles without an absorber. Primitive cycles, repeated words, source scalings and additive parameters are distinguished.',
        source_sha256={str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in paths},
        actual=actual_corpus(), generated=generated_controls(), marker_family=marker_family(),
        rejection_controls=rejection_controls(),
        scope='Exact rotation/intercept identities, unit-stripped divisibility bounds, finite actual controls and bounded examples of an unbounded-cancellation family. No unrestricted integer-cycle exclusion, formal proof, novelty claim or improvement to published cycle records is asserted.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = report()
    path = HERE/'rotation_defect_audit.json'
    if args.write:
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(path.exists() and json.loads(path.read_text()) == result,
                'rotation receipt differs from exact recomputation')
    print(json.dumps(dict(status='PASS', mode='write' if args.write else 'replay',
        actual=result['actual']['counts'], generated=result['generated']['counts'],
        marker_family=result['marker_family']['counts'],
        fixtures=len(result['actual']['fixture_controls']),
        rejection_controls=result['rejection_controls']['rejected_inputs']), sort_keys=True))


if __name__ == '__main__':
    main()
