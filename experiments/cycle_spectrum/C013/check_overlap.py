#!/usr/bin/env python3
"""Exact actual-overlap, polynomial and denominator controls for C013.

No new seed census. The candidate stress grid is explicitly nondiscriminating.
Integer polynomial gcds, paired-state runs and homogeneous extraction retain
the original raw odd-only cycles and their reduced denominators.
"""
import argparse
from collections import Counter
from fractions import Fraction
from functools import reduce
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
C012 = HERE.parent/'C012/check_coupled_system.py'
spec = importlib.util.spec_from_file_location('c013_pinned_helpers', C012)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
old, require = base.old, base.require
digest, feed = base.digest, base.feed


def fraction(x):
    return [x.numerator, x.denominator]


def primitive_polynomial(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    if not p:
        return []
    content = abs(reduce(gcd, p))*(1 if p[-1] > 0 else -1)
    return [v//content for v in p]


def polynomial_remainder(a, b):
    """Primitive pseudo-remainders; normalization preserves the Q-gcd."""
    require(b, 'polynomial division by zero')
    a = list(a)
    while a and len(a) >= len(b):
        shift, lead, divisor_lead = len(a)-len(b), a[-1], b[-1]
        a = [v*divisor_lead for v in a]
        for j, v in enumerate(b):
            a[j+shift] -= lead*v
        a = primitive_polynomial(a)
    return a


def polynomial_gcd(a, b):
    while b:
        a, b = b, polynomial_remainder(a, b)
    result = primitive_polynomial(a)
    require(result and result[-1] == 1, 'expected monic integer gcd')
    return result


def exact_quotient(a, b):
    """Separate exact long division verifies the computed common factor."""
    a, answer = list(a), [0]*(len(a)-len(b)+1)
    require(b and b[-1] == 1, 'monic divisor required')
    while a and len(a) >= len(b):
        shift, value = len(a)-len(b), a[-1]
        answer[shift] = value
        for j, v in enumerate(b):
            a[j+shift] -= value*v
        while a and a[-1] == 0:
            a.pop()
    require(not a, 'polynomial quotient was not exact')
    return answer


def marker_polynomials(word):
    prefix, total = [], 0
    for a in word:
        prefix.append(2**total)
        total += a
    return prefix[::-1], [-2**total]+[0]*(len(word)-1)+[1]


def polynomial_profile(word):
    P, Q = marker_polynomials(word)
    G = polynomial_gcd(P, Q)
    Pbar, Qbar = exact_quotient(P, G), exact_quotient(Q, G)
    require(polynomial_gcd(Pbar, Qbar) == [1], 'residual polynomials are not coprime')
    r, T, d = len(word), sum(word), len(G)-1
    e = r-d
    if gcd(r, T) == 1:
        require(G == [1], 'coprime-total irreducibility control failed')
    require((e == 1) == (len(set(word)) == 1), 'residual-degree-one characterization failed')
    return dict(r=r, T=T, d=d, e=e, G=G, P=P, Q=Q, Pbar=Pbar, Qbar=Qbar)


def homogeneous(coefficients, alpha, u):
    degree = len(coefficients)-1
    return sum(c*alpha**j*u**(degree-j) for j, c in enumerate(coefficients))


def resultant(a, b):
    da, db = len(a)-1, len(b)-1
    if da == 0:
        return a[0]**db
    if db == 0:
        return b[0]**da
    aa, bb = a[::-1], b[::-1]
    rows = [[0]*i+aa+[0]*(db-1-i) for i in range(db)]
    rows += [[0]*i+bb+[0]*(da-1-i) for i in range(da)]
    return base.bareiss(rows)


def strip6(n):
    n = abs(n)
    require(n > 0, 'nonzero resultant required')
    for p in (2, 3):
        while n % p == 0:
            n //= p
    return n


def uniform_denominator(U, markers, compute_resultant=True, profile=None):
    require(len(markers) >= 2 and len(set(markers)) > 1, 'nonconstant marker word required')
    n, AU = len(U), sum(U)
    CU = base.direct_data(U)[1] if U else 0
    u, alpha, E = 2**AU, 3**(n+1), 3*CU+2**AU
    word = [a for marker in markers for a in U+[marker]]
    A, C, D = base.direct_data(word)
    require(D > 0, 'positive full denominator required')
    g, q = gcd(C, D), D//gcd(C, D)
    p = profile or polynomial_profile(markers)
    r, T, d, e = (p[k] for k in ('r', 'T', 'd', 'e'))
    require(e >= 2 and A == r*AU+T and len(word) == r*(n+1), 'common-background totals failed')
    Gh, Ph, Qh = (homogeneous(p[k], alpha, u) for k in ('G', 'Pbar', 'Qbar'))
    h = gcd(Qh, Ph)
    require(D == -Gh*Qh and C == E*Gh*Ph, 'homogeneous extraction failed')
    require(g == abs(Gh)*gcd(Qh, E*Ph), 'extracted numerical cancellation failed')
    require(gcd(Qh, E*Ph) == h*gcd(Qh//h, E), 'residual numerical gcd identity failed')
    Rbound = r**(e*(d+1))*2**(2*T*e)
    require(E*2**n < u*alpha, 'background intercept envelope failed')
    left = q*2**A*Rbound*2**d
    right = D*2**(n*(e-1))
    require(left > right, 'uniform quantitative denominator bound failed')
    result = dict(n=n, AU=AU, r=r, T=T, d=d, e=e, G=p['G'],
        q_bits=q.bit_length(), g_bits=g.bit_length(),
        homogeneous_G_bits=abs(Gh).bit_length(), residual_h=h,
        uniform_resultant_bound_bits=Rbound.bit_length(),
        certified_lower_bound_exceeds_one=right > 2**A*Rbound*2**d,
        certified_lower_bound_floor=right//(2**A*Rbound*2**d),
        full_arithmetic_sha256=digest([word, C, D, g, q, Gh, Ph, Qh, E, hex(left), hex(right)]))
    if compute_resultant:
        R = resultant(p['Pbar'], p['Qbar'])
        require(R != 0 and abs(R) <= Rbound and strip6(R) % h == 0,
                'resultant bound or its unit-stripped divisibility failed')
        require(q*E*abs(R) >= abs(Qh), 'exact resultant denominator bound failed')
        result.update(resultant=R, resultant_coprime_to_6_part=strip6(R),
            exact_q=q, exact_g=g, exact_homogeneous_G=Gh)
    return result


def shift_runs(word, states, q, A, D, shift):
    m, L, H = len(word), min(states), max(states)
    B, K = (H//L).bit_length()-1, 2**((H//L).bit_length())-1
    mismatches = [i for i in range(m) if word[i] != word[(i+shift) % m]]
    require(mismatches, 'primitive nonidentity rotation required')
    differences = [states[(i+shift) % m]-states[i] for i in range(m)]
    require(all(z and z % 2 == 0 for z in differences), 'state differences must be nonzero even integers')
    orbit_count = gcd(m, shift)
    for start in range(orbit_count):
        require(sum(differences[(start+j*shift) % m] for j in range(m//orbit_count)) == 0,
                'actual overlap orbit sum failed')
    runs = []
    for before, end in zip(mismatches, mismatches[1:]+mismatches[:1]):
        t, start = (end-before-1) % m, (before+1) % m
        E = sum(word[(start+j) % m] for j in range(t))
        z0, z1 = differences[start], differences[end]
        require(2**E*z1 == 3**t*z0 and z0 % 2**(E+1) == 0 and z1 % (2*3**t) == 0,
                'agreeing-run exact divisibility failed')
        multiplier = z0//2**(E+1)
        require(multiplier == z1//(2*3**t), 'run endpoint multipliers differ')
        size = max(2**E, 3**t)
        require(H-L >= 2*size and L*K > 2*size, 'diameter or height-conversion bound failed')
        require(6*D*size < m*q*2**A*K, 'rational all-height denominator bound failed')
        runs.append(dict(start=start, end=end, length=t, E=E,
            multiplier=multiplier, z_start=z0, z_end=z1,
            diameter_ratio=fraction(Fraction(H-L, 2*size)),
            q_lower=fraction(Fraction(6*D*size, m*2**A*K))))
    longest = max(r['length'] for r in runs)
    require(longest >= (m+len(mismatches)-1)//len(mismatches)-1,
            'pigeonhole longest-run bound failed')
    return dict(shift=shift, mismatch_count=len(mismatches), orbit_count=orbit_count,
        longest_run=longest, runs=runs, B=B)


def actual_corpus():
    source = json.loads(old.ACTUAL.read_text())['cycles']
    additions = json.loads(old.C007.read_text())['small_parameter_census']['new_normalized_cycles']
    fixtures = json.loads(old.FIXTURES.read_text())['cycles']
    require((len(source), len(additions), len(fixtures)) == (2459, 1, 11), 'corpus changed')
    unique, source_index, raw_digest = {}, {}, sha256()
    counts, transcript = Counter(), sha256()
    for raw in source:
        q, n, d = raw['reduced_denominator'], raw['primitive_states'], raw['d']
        row = old.certificate(q, n)
        require(d % q == 0 and raw['states'] == [d//q*x for x in n] and row['word'] == raw['word'],
                'source scaling changed')
        for i, x in enumerate(raw['states']):
            require(old.step(x, d) == (raw['states'][(i+1) % len(n)], row['word'][i]), 'raw source arrow failed')
        unique[q, tuple(n)] = row
        source_index[d, tuple(raw['states'])] = row
        counts['raw_arrows'] += len(n)
        counts['scaled_source_instances'] += d//q > 1
        feed(raw_digest, [d, q, raw['states'], row['word']])
    require(len(unique) == 1184, 'normalized source count changed')
    for raw in additions:
        row = old.certificate(raw['q'], raw['states'])
        unique[row['q'], tuple(row['states'])] = row
    require(len(unique) == 1185, 'combined normalized count changed')
    nontrivial_polynomials, selected, fixture_index = [], [], {}
    tightest, strongest, longest = None, None, None
    for row in sorted(unique.values(), key=lambda r: (r['q'], r['L'])):
        word, m = row['word'], row['m']
        A, D, g, q, values, states = base.intercepts(word)
        require(states == row['states'] and q == row['q'] and base.period(word) == m,
                'independent actual cycle reconstruction failed')
        p = polynomial_profile(word)
        counts['exact_polynomial_gcds'] += 1
        counts['coprime_total_polynomial_controls'] += gcd(A, m) == 1
        counts['nonconstant_polynomial_gcds'] += p['d'] > 0
        if p['d']:
            nontrivial_polynomials.append(dict(q=q, L=row['L'], m=m, A=A, G=p['G'], e=p['e']))
        if m > 1:
            uniform = uniform_denominator([], word, compute_resultant=False, profile=p)
            counts['empty_background_uniform_bounds'] += 1
            require(not uniform['certified_lower_bound_exceeds_one'], 'empty background unexpectedly excludes q1')
        else:
            uniform = None
            counts['fixed_points_outside_nonconstant_marker_theorem'] += 1
        min_s, best_run = m, 0
        for shift in range(1, m):
            record = shift_runs(word, states, q, A, D, shift)
            s = record['mismatch_count']
            require(s*p['e']*(p['e']-1) >= 2*m, 'Fourier/Wronskian complexity bound failed')
            counts['fourier_complexity_checks'] += 1
            counts['rotations'] += 1
            counts['overlap_orbit_sums'] += record['orbit_count']
            min_s, best_run = min(min_s, s), max(best_run, record['longest_run'])
            for run in record['runs']:
                counts['maximal_agreeing_runs'] += 1
                counts['positive_length_runs'] += run['length'] > 0
                counts['unit_difference_multipliers'] += abs(run['multiplier']) == 1
                counts['positive_run_unit_multipliers'] += run['length'] > 0 and abs(run['multiplier']) == 1
                control = dict(q=q, L=row['L'], m=m, A=A, shift=shift, B=record['B'], **run)
                if run['length']:
                    if tightest is None or Fraction(*run['diameter_ratio']) < Fraction(*tightest['diameter_ratio']):
                        tightest = control
                    if strongest is None or Fraction(*run['q_lower']) > Fraction(*strongest['q_lower']):
                        strongest = control
                if longest is None or run['length'] > longest['length']:
                    longest = control
            feed(transcript, [q, row['L'], p['e'], record])
        summary = dict(q=q, L=row['L'], H=row['H'], m=m, A=A, g=g,
            G=p['G'], e=p['e'], minimum_rotation_distance=None if m == 1 else min_s,
            longest_agreeing_run=best_run, word=word)
        fixture_index[q, row['L']] = summary
        if (q, row['L']) in {(1, 1), (5, 19), (5, 187), (5, 347), (7, 5),
                            (13, 283), (29, 7055), (131, 23), (509, 5), (755, 869), (929, 11)}:
            selected.append(summary)
        if q == 5 and m == 17:
            require(A == 27 and p['G'] == [1] and p['e'] == 17 and g == 1015513,
                    'polynomial versus numerical cancellation control failed')
        counts['normalized_cycles'] += 1
        counts['normalized_arrows'] += m
        feed(transcript, [summary, uniform])
    require(counts['rotations'] == 27646 and counts['maximal_agreeing_runs'] == 969102 and
            counts['positive_length_runs'] == 334590 and counts['raw_arrows'] == 36912,
            'all-run coverage changed')
    require(counts['nonconstant_polynomial_gcds'] == 20, 'polynomial-gcd controls changed')
    controls = []
    for i, fixture in enumerate(fixtures):
        row = source_index[fixture['d'], tuple(fixture['states'])]
        require(row['word'] == fixture['valuations'], 'fixture valuations changed')
        controls.append(dict(fixture_id=i+1, d=fixture['d'], states=fixture['states'],
            q=row['q'], scale=fixture['d']//row['q'],
            normalized_summary_sha256=digest(fixture_index[row['q'], row['L']])))
    return dict(source_instances=len(source), source_parameters=len({r['d'] for r in source}),
        C007_added_cycles=1, counts=dict(sorted(counts.items())), fixture_controls=controls,
        selected_actual_controls=selected, nontrivial_polynomial_factors=nontrivial_polynomials,
        tightest_positive_run_diameter=tightest, strongest_height_dependent_q_bound=strongest,
        longest_agreeing_run=longest, all_raw_source_checks_sha256=raw_digest.hexdigest(),
        all_actual_overlap_checks_sha256=transcript.hexdigest(),
        scope='Every actual polynomial gcd is computed exactly, including all 762 noncoprime-total cases. Fourier complexity is checked on every nonidentity rotation; this is polynomial cancellation, distinct from numerical gcd. Empty-background uniform bounds are algebraic controls and all have lower bound below one. The run bound retains B explicitly.')


def minimum_distance(word):
    distances = [sum(a != b for a, b in zip(word, base.rotate(word, k))) for k in range(1, len(word))]
    positive = [(s, k+1) for k, s in enumerate(distances) if s]
    return min(positive), distances


def structured_stress():
    bases = [[1, 2, 2], [1, 1, 3], [1, 3], [1, 1, 2, 2, 2], [1, 1, 2, 3, 1, 1, 2, 4]]
    words = {}
    for b, U in enumerate(bases):
        alternatives = [base.rotate(U, i) for i in range(1, min(3, len(U)))]+[U[:-1]+[U[-1]+1]]
        for j, V in enumerate(alternatives):
            for k in (1, 2, 4, 8, 16, 32):
                for ell in (k, k+1, 2*k):
                    words[tuple(U*k+V*ell)] = ['two_blocks', b, j, k, ell]
    for t in (3, 4, 8, 16, 32):
        U = [1]*t+[2]*(2*t)
        words[tuple([3]+U+[4]+U+[5]+U)] = ['marker_runs', t]
    counts, transcript, selected = Counter(), sha256(), []
    max_ratio = Fraction(0)
    for word_tuple, label in sorted(words.items()):
        word = list(word_tuple)
        A, D, g, q, values, states = base.intercepts(word)
        (s, shift), distances = minimum_distance(word)
        m = len(word)
        passed, implied = g**s*4**m < 2**(A*s)*3**m, q**s*3**m >= 4**m
        require(passed and implied, 'structured stress outcome changed; preserve new evidence')
        counts['words'] += 1
        counts['candidate_passes'] += passed
        counts['passes_already_implied_by_q'] += implied
        counts['minimum_distance_two_already_in_C011'] += s == 2
        counts['raw_arrows'] += m
        counts['all_rotation_distances'] += len(distances)
        counts['primitive_words'] += base.period(word) == m
        ratio = Fraction(m, s)
        record = dict(label=label, m=m, A=A, minimum_distance=s, witness_shift=shift,
            q_bits=q.bit_length(), g_bits=g.bit_length(),
            candidate_pass=passed, already_implied_by_q=implied)
        if ratio > max_ratio:
            max_ratio = ratio
            largest_ratio = record
        if label[0] == 'marker_runs':
            t = label[1]
            require(s == 3 and max(states)*2**t > min(states)*3**t,
                    'fixed-distance height obstruction failed')
            record.update(B=(max(states)//min(states)).bit_length()-1,
                normalized_minimum_floor=min(states)//q)
            selected.append(record)
        feed(transcript, [record, word, states, distances])
    require(counts['words'] == 243 and counts['passes_already_implied_by_q'] == 243,
            'declared bounded stress grid changed')
    return dict(counts=dict(sorted(counts.items())), marker_height_controls=selected,
        largest_period_over_distance=largest_ratio, maximum_period_over_distance=fraction(max_ratio),
        full_stress_sha256=transcript.hexdigest(),
        decision='Stopped this grid after all 243 strongest per-word tests proved already implied by q. They are not discriminating evidence for the candidate, despite period/distance reaching 384. No seed census or expansion of this nondiscriminating search was made.')


def near_critical_height_controls():
    cases, transcript = [], sha256()
    for a, b in ((27, 17), (65, 41), (485, 306)):
        u, v = 2*b+2-a, a-b-3
        P, Q = 3**b, 2**a
        require(u >= 1 and v >= 1 and Q > P and 2*P >= Q, 'upper-pair family domain failed')
        U = [1]*u+[2]*v
        word = [3]+U+[4]+U+[5]+U
        A, D, g, q, values, states = base.intercepts(word)
        (s, shift), distances = minimum_distance(word)
        require(s == 3 and base.period(word) == len(word) and len(word) == 3*b and A == 3*a,
                'near-critical primitive totals/distance failed')
        r = Fraction(P, Q)
        lam, tau = Fraction(16, 3)*r, Fraction(3, 4)**v
        beta = lam+1-2*tau
        AU, CU, _ = base.direct_data(U)
        require(lam == Fraction(3**len(U), 2**AU) and beta == Fraction(CU, 2**AU),
                'two-run exact affine formula failed')
        constants = [beta+lam/2**k for k in (3, 4, 5)]
        T = r*r*constants[0]/2+r*constants[1]/2+constants[2]
        X = [Fraction(states[j*b], q) for j in range(3)]
        require(X[0] == T/(1-r**3) and X[1] == 2*r*X[0]+constants[0] and
                X[2] == r*X[1]+constants[1] and X[0] == r*X[2]/2+constants[2],
                'exact marker-state affine solution failed')
        L, H = min(states), max(states)
        require(Fraction(L, q) == min((3*x+1)/2**k for x, k in zip(X, (3, 4, 5))),
                'minimum is not at a post-marker state')
        require(256*L*(Q**3-P**3) > 27*q*Q**3 and H*2**u > L*3**u,
                'near-critical exact finite minimum/height bounds failed')
        run = shift_runs(word, states, q, A, D, b)
        require(run['mismatch_count'] == 3 and all(x['length'] == b-1 for x in run['runs']),
                'near-critical shared-run length changed')
        uniform = uniform_denominator(U, [3, 4, 5])
        require(uniform['exact_q'] == q, 'orientation changed the reduced denominator')
        record = dict(a=a, b=b, ones=u, twos=v, m=len(word), A=A,
            minimum_distance=s, B=(H//L).bit_length()-1,
            normalized_minimum_floor=L//q, q_bits=q.bit_length(), g_bits=g.bit_length(),
            all_states_exceed_q=L > q, affine_and_run_sha256=digest([list(map(fraction, X)), run]),
            quantitative_uniform_bound=uniform)
        cases.append(record)
        feed(transcript, [word, states, distances, record])
    return dict(cases=cases, raw_arrows=sum(c['m'] for c in cases),
        all_rotation_distances=sum(c['m']-1 for c in cases),
        full_controls_sha256=transcript.hexdigest(),
        scope='Only the three declared upper pairs are checked. Exact affine identities and finite inequalities are verified; asymptotic limits, balanced subsequences and unboundedness are separately written arguments, not inferred from these three examples.')


def common_background_controls():
    primitive_marker = [3, 1, 3, 3, 1, 1]
    p = polynomial_profile(primitive_marker)
    require(p['G'] == [4, 1] and p['e'] == 5 and base.period(primitive_marker) == 6,
            'primitive nonconstant polynomial factor control failed')
    R = resultant(p['Pbar'], p['Qbar'])
    require(abs(R) == 2**41*3**4, 'primitive marker resultant changed')
    cases = []
    for U, expected_q, expected_G in (([2], 92833, 25), ([1, 2], 11632565, 59),
                                    ([1, 1, 2, 2, 2, 2], 734195049138649189, 6283)):
        row = uniform_denominator(U, primitive_marker, profile=p)
        word = [a for marker in primitive_marker for a in U+[marker]]
        _, _, _, q, _, states = base.intercepts(word)
        require(row['exact_q'] == q == expected_q and row['exact_homogeneous_G'] == expected_G and
                row['residual_h'] == 1, 'nonempty algebraic extraction control changed')
        cases.append(dict(background=U, markers=primitive_marker, states_sha256=digest(states), **row))
    exclusions = []
    for U in ([1], [1, 1]):
        word = [a for marker in primitive_marker for a in U+[marker]]
        _, _, D = base.direct_data(word)
        require(D < 0, 'expanding negative-full-D control changed')
        exclusions.append(dict(background=U, full_D=D, counted_as_positive_cycle=False))
    long_cases = []
    for markers in ([3, 4, 5], primitive_marker):
        for repetitions in (10, 20):
            U = [1, 1, 2, 2, 2]*repetitions
            row = uniform_denominator(U, list(markers))
            word = [a for marker in markers for a in U+[marker]]
            _, _, _, q, _, states = base.intercepts(word)
            require(row['certified_lower_bound_exceeds_one'] and q > 1,
                    'long common-background lower bound does not exclude q1')
            long_cases.append(dict(background_base=[1, 1, 2, 2, 2], repetitions=repetitions,
                markers=list(markers), all_states_exceed_q=min(states) > q,
                states_sha256=digest(states), **row))
    repeated = []
    for repetitions in (2, 3, 5):
        word = [2]*repetitions
        A, D, g, q, values, states = base.intercepts(word)
        pp = polynomial_profile(word)
        require(q == 1 and pp['e'] == 1 and all(x == 1 for x in states), 'trivial repetition changed')
        repeated.append(dict(word=word, q=q, e=1, G=pp['G'],
            outside_nonconstant_marker_bound=True, zero_rotations=repetitions-1))
    return dict(primitive_marker=primitive_marker, primitive_marker_profile=p,
        primitive_marker_resultant=R, exact_extraction_cases=cases,
        negative_full_D_controls=exclusions, long_background_exclusions=long_cases,
        trivial_repetition_controls=repeated,
        scope='Exact resultant extraction and numerical residual gcd remain separate. Four nonempty long backgrounds yield certified lower bounds greater than one. These calibrate the written common-background theorem; they do not show all arbitrary sparse-rotation words have this representation.')


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--check', action='store_true')
    args = parser.parse_args()
    dependencies = [C012, base.C009, old.ACTUAL, old.C007, old.FIXTURES]
    receipt = dict(schema='C013-actual-overlap-v1', status='PASS',
        clock='raw positive odd-only 3x+d, no absorber',
        checker_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        source_sha256={str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in dependencies},
        actual=actual_corpus(), structured_candidate_stress=structured_stress(),
        near_critical_height=near_critical_height_controls(), common_background=common_background_controls(),
        claim_scope='Exact finite controls of written overlap and polynomial laws, retaining numerical cancellation. No new seed census, unrestricted mismatch-growth theorem, Collatz proof, novelty or formal-verification claim.')
    path = HERE/'overlap_audit.json'
    if args.write:
        path.write_text(json.dumps(receipt, indent=2, sort_keys=True)+'\n')
    require(path.exists(), 'receipt missing; run author --write first')
    require(json.loads(path.read_text()) == receipt, 'saved receipt differs from exact replay')
    print(json.dumps(dict(status='PASS', actual_counts=receipt['actual']['counts'],
        stress_counts=receipt['structured_candidate_stress']['counts'],
        positive_nonempty_quantitative_controls=len(receipt['common_background']['long_background_exclusions']),
        receipt=str(path.relative_to(ROOT))), sort_keys=True))


if __name__ == '__main__':
    main()
