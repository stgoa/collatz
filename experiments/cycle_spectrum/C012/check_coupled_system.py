#!/usr/bin/env python3
"""Exact coupled rotation systems on the stored raw-cycle corpus.

Finite tests do not prove the proposed arbitrary-defect cancellation bound.
The historical cycle loader is reused; intercepts, block matrices and selected
determinants are recomputed here with integer arithmetic.
"""
import argparse
from collections import Counter
from hashlib import sha256
import importlib.util
from itertools import combinations
import json
from math import gcd
from pathlib import Path
import sys

if sys.flags.optimize:
    raise SystemExit('FAIL: optimized Python is not supported')

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
C009 = HERE.parent/'C009/check_excursions.py'
spec = importlib.util.spec_from_file_location('c012_raw_helpers', C009)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
require = old.require


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def feed(hasher, value):
    hasher.update(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()+b'\n')


def direct_data(word):
    require(word and all(type(a) is int and a >= 1 for a in word), 'positive word required')
    prefixes = [0]
    for a in word:
        prefixes.append(prefixes[-1]+a)
    m, A = len(word), prefixes[-1]
    C = sum(3**(m-1-j)*2**prefixes[j] for j in range(m))
    return A, C, 2**A-3**m


def rotate(word, k):
    return word[k:]+word[:k]


def period(word):
    return next(p for p in range(1, len(word)+1)
                if len(word) % p == 0 and word == word[:p]*(len(word)//p))


def intercepts(word):
    A, C, D = direct_data(word)
    require(D > 0, 'positive D required')
    values = [C]
    for a in word:
        numerator = 3*values[-1]+D
        require(numerator % 2**a == 0, 'rotated intercept recurrence is not integral')
        values.append(numerator//2**a)
    require(values.pop() == C, 'intercept recurrence does not close')
    g = gcd(C, D)
    q = D//g
    states = [c//g for c in values]
    require(all(c % g == 0 for c in values), 'rotation changed cancellation')
    for i, n in enumerate(states):
        require(old.step(n, q) == (states[(i+1) % len(word)], word[i]), 'raw arrow failed')
    require(len(set(states)) == period(word), 'word and state primitive periods disagree')
    return A, D, g, q, values, states


def bareiss(matrix):
    """Independent determinant, without using the claimed product formula."""
    n = len(matrix)
    if n == 0:
        return 1
    a = [r[:] for r in matrix]
    sign, previous = 1, 1
    for k in range(n-1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        value = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = a[i][j]*value-a[i][k]*a[k][j]
                require(numerator % previous == 0, 'Bareiss division is not exact')
                a[i][j] = numerator//previous
            a[i][k] = 0
        previous = value
    return sign*a[-1][-1]


def valuation(n, p):
    require(n != 0, 'zero has no finite prime valuation')
    n, exponent = abs(n), 0
    while n % p == 0:
        n //= p
        exponent += 1
    return exponent


def local_profile(matrix, D, beta, other_beta, p):
    """Check the local Smith ingredients by actual minors, not factorization."""
    s, t = len(matrix), valuation(D, p)
    require(t >= 1 and all((bp-b) % p for b, bp in zip(beta, other_beta)),
            'prime-unit local Smith hypotheses failed')
    witness = None
    for rows in combinations(range(s), 2):
        for columns in combinations(range(s), 2):
            value = bareiss([[matrix[i][j] for j in columns] for i in rows])
            if value % p:
                witness = dict(rows=list(rows), columns=list(columns), minor=value)
                break
        if witness:
            break
    require(witness is not None, 'rank modulo p is below two')
    checked = 0
    for rows in combinations(range(s), 3):
        for columns in combinations(range(s), 3):
            value = bareiss([[matrix[i][j] for j in columns] for i in rows])
            require(value % p**t == 0, 'a three-minor lacks the full p^t factor')
            checked += 1
    determinant_valuation = valuation(bareiss(matrix), p)
    require(determinant_valuation == (s-2)*t, 'local determinant valuation failed')
    return dict(prime=p, D_valuation=t, size=s, unit_two_minor=witness,
        all_three_minors_checked=checked, determinant_valuation=determinant_valuation,
        inferred_local_smith_valuations=[0, 0]+[t]*(s-2))


def coupled_system(word, shift, values, D, g, determinant=False, local_primes=()):
    """Blocks end at each mismatch, so paired block intercepts agree."""
    m = len(word)
    alternate = rotate(word, shift)
    positions = [j for j in range(m) if word[j] != alternate[j]]
    s = len(positions)
    require(s >= 2, 'nonzero rotation needs at least two mismatches')
    starts, lengths, c, alpha, beta, other_beta, deltas = [], [], [], [], [], [], []
    for i, end in enumerate(positions):
        start = (positions[i-1]+1) % m
        length = (end-positions[i-1]) % m
        indices = [(start+j) % m for j in range(length)]
        block = [word[j] for j in indices]
        other = [alternate[j] for j in indices]
        B, C, _ = direct_data(block)
        B_other, C_other, _ = direct_data(other)
        require(block[:-1] == other[:-1] and block[-1] != other[-1] and C == C_other,
                'mismatch blocks do not have common interiors/intercepts')
        starts.append(start)
        lengths.append(length)
        c.append(C)
        alpha.append(3**length)
        beta.append(2**B)
        other_beta.append(2**B_other)
        deltas.append(B_other-B)
    require(sum(lengths) == m and sum(deltas) == 0, 'block totals changed')
    M, cut_differences, total_alpha = [], [], 3**m
    for i in range(s):
        row, weights, alternate_weights = [0]*s, [0]*s, [0]*s
        prefix, other_prefix, suffix = 1, 1, total_alpha//alpha[i]
        for distance in range(s):
            j = (i+distance) % s
            weights[j] = prefix*suffix
            alternate_weights[j] = other_prefix*suffix
            row[j] = alternate_weights[j]-weights[j]
            prefix *= beta[j]
            other_prefix *= other_beta[j]
            if distance+1 < s:
                suffix //= alpha[(j+1) % s]
        require(sum(x*y for x, y in zip(weights, c)) == values[starts[i]],
                'W times block intercepts is not the full cut intercept')
        require(sum(x*y for x, y in zip(alternate_weights, c)) == values[(starts[i]+shift) % m],
                'W-prime times block intercepts is not the rotated full cut intercept')
        difference = values[(starts[i]+shift) % m]-values[starts[i]]
        require(sum(x*y for x, y in zip(row, c)) == difference and difference % g == 0,
                'coupled system or common cancellation failed')
        require(row[i] == 0, 'difference matrix diagonal is nonzero')
        M.append(row)
        cut_differences.append(difference)
    result = dict(shift=shift, mismatch_count=s, mismatch_positions=positions,
        signed_amplitudes=deltas, block_lengths=lengths, block_intercepts=c,
        beta=beta, beta_prime=other_beta, cut_differences=cut_differences,
        matrix_sha256=digest(M))
    if determinant:
        calculated = abs(bareiss(M))
        expected = D**(s-2)
        for b, bp in zip(beta, other_beta):
            expected *= abs(bp-b)
        require(calculated == expected > 0, 'coupled determinant product failed')
        minor_checks = 0
        for k in range(2, min(s, 4)+1):
            subsets = list(combinations(range(s), k))
            selected = sorted(set((subsets[0], subsets[len(subsets)//2], subsets[-1])))
            for rows in selected:
                for columns in selected:
                    minor = bareiss([[M[i][j] for j in columns] for i in rows])
                    require(minor % D**(k-2) == 0, 'claimed minor D factor failed')
                    minor_checks += 1
        require(s == 2 or calculated % g == 0,
                'determinant divisibility should already follow from g dividing D')
        result.update(determinant=calculated, determinant_D_power=s-2,
            independent_minor_checks=minor_checks,
            determinant_divisibility_automatic_from_g_dividing_D=s >= 3)
        if s <= 4:
            result['matrix'] = M
    if local_primes:
        result['local_profiles'] = [local_profile(M, D, beta, other_beta, p) for p in local_primes]
    return result


def candidate(word, A, D, g, q, shift):
    s = sum(a != b for a, b in zip(word, rotate(word, shift)))
    if s == 0:
        return dict(shift=shift, mismatch_count=0, candidate_applicable=False)
    m = len(word)
    left, right = g**s*4**m, 2**(A*s)*3**m
    return dict(shift=shift, mismatch_count=s, candidate_applicable=True,
        candidate_pass=left < right, candidate_integer_margin=right-left,
        already_implied_by_q=4**m <= q**s*3**m,
        repetition_limit_could_fail=4**m > q**s*3**m)


def actual_corpus():
    source = json.loads(old.ACTUAL.read_text())['cycles']
    additions = json.loads(old.C007.read_text())['small_parameter_census']['new_normalized_cycles']
    fixtures = json.loads(old.FIXTURES.read_text())['cycles']
    require(len(source) == 2459 and len(additions) == 1 and len(fixtures) == 11, 'corpus changed')
    unique, source_index, raw_transcript = {}, {}, sha256()
    counts, all_transcript = Counter(), sha256()
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
        feed(raw_transcript, [d, q, raw['states'], row['word']])
        counts['raw_arrows'] += len(n)
        counts['scaled_instances'] += d//q > 1
    require(len(unique) == 1184 and counts['raw_arrows'] == 36912 and
            counts['scaled_instances'] == 1275, 'raw source coverage changed')
    for raw in additions:
        row = old.certificate(raw['q'], raw['states'])
        unique[row['q'], tuple(row['states'])] = row
    require(len(unique) == 1185, 'normalized coverage changed')
    determinant_counts, hamming_groups, selected, failures = Counter(), {}, [], []
    summary_index, max_ratio = {}, (0, 1)
    for row in sorted(unique.values(), key=lambda r: (r['q'], r['L'])):
        word, m = row['word'], row['m']
        A, D, g, q, values, states = intercepts(word)
        require(states == row['states'] and q == row['q'] and period(word) == m,
                'independent actual-cycle reconstruction failed')
        counts['normalized_arrows'] += m
        counts['normalized_cycles'] += 1
        counts['nonfixed_cycles'] += m > 1
        cases = []
        for shift in range(1, m):
            test = candidate(word, A, D, g, q, shift)
            s = test['mismatch_count']
            require(s >= 2, 'actual primitive cycle has zero/nonlegal mismatch count')
            do_det = s <= 8 and determinant_counts[s] < 4
            system = coupled_system(word, shift, values, D, g, determinant=do_det)
            counts['rotations'] += 1
            counts['all_cut_identities'] += 2*s
            counts['coupled_equations'] += s
            counts['matrix_entries'] += s*s
            counts['candidate_passes'] += test['candidate_pass']
            counts['candidate_passes_already_implied_by_q'] += test['already_implied_by_q']
            counts['repetition_limit_could_fail'] += test['repetition_limit_could_fail']
            if not test['candidate_pass']:
                failures.append(dict(q=q, L=row['L'], word=word, test=test))
            if do_det:
                determinant_counts[s] += 1
                counts['independent_determinants'] += 1
                counts['independent_minors'] += system['independent_minor_checks']
            if m*max_ratio[1] > max_ratio[0]*s:
                max_ratio = m, s
            feed(all_transcript, [q, row['L'], system, test])
            cases.append((s, shift))
        minimum_s, witness = min(cases) if cases else (None, None)
        summary = dict(q=q, L=row['L'], m=m, A=A, g=g, word=word,
            minimum_hamming=minimum_s, witness_shift=witness,
            chronological_runs=sum(word[i] != word[i-1] for i in range(m)))
        summary_index[q, row['L']] = summary
        if minimum_s is not None:
            group = hamming_groups.setdefault(str(minimum_s), dict(cycles=0, max_period=0, max_g=0))
            group['cycles'] += 1
            group['max_period'] = max(group['max_period'], m)
            group['max_g'] = max(group['max_g'], g)
        if (q, row['L']) in {(1, 1), (5, 19), (7, 5), (13, 283), (23, 41),
                              (29, 7055), (97, 13), (233, 1907), (359, 209), (499, 6605)}:
            selected.append(summary)
    require(counts['rotations'] == 27646 and counts['normalized_arrows'] == 28831,
            'normalized rotation coverage changed')
    require(not failures and counts['candidate_passes_already_implied_by_q'] == counts['rotations'],
            'candidate result changed; preserve and inspect new evidence')
    require(max_ratio[0] == 5*max_ratio[1], 'sample max period/defect ratio changed')
    controls = []
    for i, fixture in enumerate(fixtures):
        row = source_index[fixture['d'], tuple(fixture['states'])]
        require(row['word'] == fixture['valuations'], 'fixture valuation changed')
        controls.append(dict(fixture_id=i+1, d=fixture['d'], states=fixture['states'],
            q=row['q'], scale=fixture['d']//row['q'],
            normalized_summary_sha256=digest(summary_index[row['q'], row['L']])))
    return dict(source_cycles=len(source), source_parameters=len({r['d'] for r in source}),
        C007_added_cycles=1, counts=dict(sorted(counts.items())),
        determinant_counts_by_size={str(k): v for k, v in sorted(determinant_counts.items())},
        minimum_hamming_groups=hamming_groups, selected_controls=selected,
        fixture_controls=controls, candidate_failures=failures,
        maximum_period_to_defect_ratio=dict(numerator=max_ratio[0], denominator=max_ratio[1]),
        all_raw_source_checks_sha256=raw_transcript.hexdigest(),
        all_coupled_checks_sha256=all_transcript.hexdigest(),
        scope='All actual candidate successes follow already from their reduced q and m/s; they provide no discriminating support for the proposed universal bound. Matrix cut identities are tested for every shift. Determinants and minors are independently evaluated only at the declared bounded matrix sizes.')


def generated_controls():
    cases, transcript, counts = [], sha256(), Counter()
    prime_power_controls, modular_controls = [], []
    for r in (2, 3, 4):
        ts = (1, 2, 4, 6, 8, 16, 20, 23, 32) if r == 2 else (1, 2, 4, 6, 8, 16, 20, 32)
        for t in ts:
            word = ([1]*t+[2]*(2*t))*(r-1)+[1]*t+[2]*(3*t)
            A, D, g, q, values, states = intercepts(word)
            m = len(word)
            require(m == (3*r+1)*t and A == (5*r+2)*t and period(word) == m,
                    'primitive run family totals/period changed')
            tests = [candidate(word, A, D, g, q, k) for k in range(1, m)]
            require(all(test['candidate_pass'] for test in tests),
                    'generated candidate failure: preserve before extending receipt')
            local_primes = [p for p in (5, 7, 11, 13, 23) if D % (p*p) == 0]
            system = coupled_system(word, 1, values, D, g, determinant=True, local_primes=local_primes)
            require(system['mismatch_count'] == 2*r and
                    all(abs(a) == 1 for a in system['signed_amplitudes']),
                    'primitive run family defects changed')
            require(system['determinant'] == 2**(A-r)*D**(2*r-2),
                    'primitive run family explicit determinant formula failed')
            if (r, t) == (2, 1):
                require(values[0] == 5095 and D == q == 1909 and g == 1 and
                        states == [5095, 8597, 6925, 5671, 9461, 7573, 6157] and
                        system['block_intercepts'] == [1, 7, 1, 37] and
                        system['matrix'] == [[0, 162, 0, 64], [-1024, 0, -648, 0],
                                             [0, 256, 0, 54], [-864, 0, -1024, 0]],
                        'small published-in-this-batch matrix control changed')
            record = dict(r=r, t=t, m=m, A=A, g=g, q_bits=q.bit_length(),
                D_bits=D.bit_length(), minimum_numerator_bits=min(states).bit_length(),
                minimum_hamming=min(test['mismatch_count'] for test in tests),
                shift_one_defects=2*r, shift_one_max_amplitude=1,
                candidate_passes=len(tests), primitive=True,
                candidate_passes_already_implied_by_q=sum(test['already_implied_by_q'] for test in tests),
                coupled_system_sha256=digest(system), all_candidate_tests_sha256=digest(tests))
            cases.append(record)
            feed(transcript, [word, values, system, tests])
            counts['primitive_family_words'] += 1
            counts['raw_arrows'] += m
            counts['candidate_rotations'] += len(tests)
            counts['candidate_passes_already_implied_by_q'] += sum(test['already_implied_by_q'] for test in tests)
            counts['independent_determinants'] += 1
            counts['independent_minors'] += system['independent_minor_checks']
            for profile in system.get('local_profiles', []):
                prime_power_controls.append(dict(r=r, t=t, **profile))
                counts['prime_power_local_profiles'] += 1
                counts['prime_power_three_minors'] += profile['all_three_minors_checked']
            for modulus, exponent in ((5, 4), (7, 6), (25, 20)):
                if t == exponent:
                    require(pow(2, t, modulus) == pow(3, t, modulus) == 1 and g % modulus == 0,
                            'run-family prescribed cancellation modulus failed')
                    modular_controls.append(dict(r=r, t=t, modulus=modulus, g=g))
    repeated = []
    for base in ([2], [3], [1, 2, 2], [1, 1, 2, 3, 1, 1, 2, 4]):
        for repetitions in (2, 3, 4):
            word = base*repetitions
            A, D, g, q, values, states = intercepts(word)
            tests = [candidate(word, A, D, g, q, k) for k in range(1, len(word))]
            zero = [test['shift'] for test in tests if not test['candidate_applicable']]
            require(zero == list(range(len(base), len(word), len(base))), 'repetition zero shifts changed')
            require(all(test.get('candidate_pass', True) for test in tests), 'repeated control bound failed')
            repeated.append(dict(base_word=base, repetitions=repetitions, q=q, g=g,
                zero_shifts=zero, nonzero_candidate_checks=len(tests)-len(zero)))
            counts['repeated_word_controls'] += 1
            counts['raw_arrows'] += len(word)
            counts['candidate_rotations'] += len(tests)-len(zero)
            counts['candidate_passes_already_implied_by_q'] += sum(test.get('already_implied_by_q', False) for test in tests)
            counts['zero_rotations_kept_separate'] += len(zero)
            feed(transcript, [word, values, tests])
    require(any(c['prime'] == 5 and c['D_valuation'] >= 2 for c in prime_power_controls) and
            any(c['prime'] == 23 and c['D_valuation'] >= 2 for c in prime_power_controls),
            'declared prime-power coverage missing')
    return dict(counts=dict(sorted(counts.items())), primitive_run_family=cases,
        prime_power_controls=prime_power_controls, prescribed_modulus_controls=modular_controls,
        repetition_controls=repeated, all_generated_checks_sha256=transcript.hexdigest(),
        scope='A bounded generated family, not a seed census or proof of the candidate. Candidate successes already implied by q are counted separately and are nondiscriminating. The matrix/determinant tests exercise primitive words with 4, 6 and 8 unit defects at shift one, including long agreeing arcs and prime powers. Repetitions and constant words retain their zero-defect shifts; every repetition of (2) has denominator one.')


def explicit_coupling_controls():
    source = json.loads(old.ACTUAL.read_text())['cycles']
    actual = {(r['reduced_denominator'], tuple(r['primitive_states'])) for r in source}
    controls = []
    for word, shift, expected_q, expected_g in (
            ([2, 4, 3], 1, 97, 5),
            ([1, 1, 2, 1, 2, 1, 3, 2], 3, 233, 7),
            ([1, 1, 2, 3, 1, 1, 2, 4], 1, 359, 73)):
        A, D, g, q, values, states = intercepts(word)
        require((q, g) == (expected_q, expected_g), 'explicit control changed')
        start = states.index(min(states))
        require((q, tuple(rotate(states, start))) in actual, 'control missing from actual source')
        system = coupled_system(word, shift, values, D, g, determinant=True)
        controls.append(dict(word=word, shift=shift, states=states, A=A, D=D, g=g, q=q,
            system=system, determinant_D_factor_already_multiple_of_g=True))
    require(controls[0]['system']['matrix'] == [[0, 36, 64], [-96, 0, -24], [-12, 32, 0]] and
            controls[0]['system']['determinant'] == 186240,
            'small explicit three-defect matrix changed')
    return controls


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    dependencies = [C009, old.ACTUAL, old.C007, old.FIXTURES]
    receipt = dict(schema='C012-coupled-system-v1', status='PASS',
        clock='raw positive odd-only 3x+d; no absorbing state',
        source_sha256={str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in dependencies},
        checker_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        exact_candidate='g^s*4^m < 2^(A*s)*3^m for a nonzero rotation with s mismatches',
        actual=actual_corpus(), generated=generated_controls(),
        explicit_actual_coupling_controls=explicit_coupling_controls(),
        claim_scope='Exact finite identities and bounded independent determinants; no proof or refutation of the proposed arbitrary-defect inequality, no unrestricted q=1 exclusion, no novelty or formal-verification claim.')
    output = HERE/'coupled_system_audit.json'
    if args.write:
        output.write_text(json.dumps(receipt, indent=2, sort_keys=True)+'\n')
    require(output.exists(), 'receipt missing; author must write it first')
    require(json.loads(output.read_text()) == receipt, 'receipt differs from exact replay')
    print(json.dumps(dict(status='PASS', receipt=str(output.relative_to(ROOT)),
        actual_counts=receipt['actual']['counts'], generated_counts=receipt['generated']['counts']), sort_keys=True))


if __name__ == '__main__':
    main()
