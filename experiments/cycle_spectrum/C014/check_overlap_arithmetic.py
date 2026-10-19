#!/usr/bin/env python3
"""Bounded exact rotation/resultant controls; no new seed census.

The C013 candidate arithmetic is preserved. Its use of an observed q to
classify every generated test as nondiscriminating is corrected here.
"""
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import importlib.util
import json
from math import gcd, isqrt
from pathlib import Path
import subprocess
import sys

if sys.flags.optimize:
    raise SystemExit('FAIL: optimized Python is not supported')
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
C013 = HERE.parent/'C013/check_overlap.py'
spec = importlib.util.spec_from_file_location('c014_pinned_helpers', C013)
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
base, old, require = prior.base, prior.old, prior.require
digest, feed = base.digest, base.feed
SIDE = '9a0e8dc68e3751cfe8917f3f12d3645023c85725'


def evaluate(poly, x):
    value = 0
    for coefficient in reversed(poly):
        value = value*x+coefficient
    return value


def trim(poly):
    poly = list(poly)
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def xp_minus_q(P, Q):
    result = [0]+list(P)
    require(len(result) == len(Q), 'unexpected polynomial degree')
    return trim([a-b for a, b in zip(result, Q)])


def rotation_identity(word, profile):
    """All phase polynomials built directly, divided by the original G.

    Coprimality after rotation follows algebraically from the displayed
    residual identity and Qbar(0)!=0; no extra polynomial gcd is claimed.
    """
    G, Q, Qbar = (profile[k] for k in ('G', 'Q', 'Qbar'))
    require(Qbar[0] != 0 and abs(Qbar[0]) & (abs(Qbar[0])-1) == 0,
            'residual constant is not a signed power of two')
    phases = [prior.marker_polynomials(base.rotate(word, j))[0] for j in range(len(word))]
    reduced = [prior.exact_quotient(P, G) for P in phases]
    for j, a in enumerate(word):
        following = (j+1) % len(word)
        require([2**a*c for c in phases[following]] == xp_minus_q(phases[j], Q),
                'direct whole-polynomial rotation identity failed')
        require([2**a*c for c in reduced[following]] == xp_minus_q(reduced[j], Qbar),
                'extracted polynomial rotation identity failed')
    return phases, reduced


def invariant_cuts(word, shift):
    m = len(word)
    mismatches = [j for j in range(m) if word[j] != word[(j+shift) % m]]
    require(mismatches, 'nonidentity primitive rotation required')
    cuts = {(j+1) % m for j in mismatches}
    closure, queue = set(cuts), list(cuts)
    while queue:
        target = (queue.pop()+shift) % m
        if target not in closure:
            closure.add(target)
            queue.append(target)
    d = gcd(m, shift)
    k = len({j % d for j in cuts})
    require(len(closure) == m//d*k and 2*k <= len(mismatches), 'invariant cut formula failed')
    return [shift, len(mismatches), d, k, len(closure)]


def determinant_control(word, profile, all_phases=False):
    """Sylvester/Bareiss, independent of the resultant rotation formula."""
    phases, reduced = rotation_identity(word, profile)
    e, Qbar = profile['e'], profile['Qbar']
    indices = list(range(len(word))) if all_phases else list(range(min(2, len(word))))
    values = {j: abs(prior.resultant(reduced[j], Qbar)) for j in indices}
    require(all(values.values()), 'residual resultant vanished')
    for j in indices:
        following = (j+1) % len(word)
        if following in values:
            require(values[following]*2**(word[j]*e) == values[j]*abs(Qbar[0]),
                    'independent resultant phase ratio failed')
        require(prior.strip6(values[j]) == prior.strip6(values[0]),
                'phase resultants have different prime-to-six parts')
    C, D = evaluate(profile['P'], 3), -evaluate(profile['Q'], 3)
    Gh = evaluate(profile['G'], 3)
    Ph, Qh = evaluate(profile['Pbar'], 3), evaluate(Qbar, 3)
    h = gcd(Ph, Qh)
    R, R6 = values[0], prior.strip6(values[0])
    require(C == Gh*Ph and -D == Gh*Qh and gcd(C, D) == abs(Gh)*h,
            'whole-word numerical factor extraction failed')
    require(R6 % h == 0 and gcd(D, 6) == 1 and gcd(h, 6) == 1,
            'residual resultant does not contain numerical gcd')
    return dict(resultant_bits=R.bit_length(), resultant_v2=base.valuation(R, 2),
        resultant_v3=base.valuation(R, 3), prime_to_six_part_bits=R6.bit_length(),
        evaluated_G=Gh, residual_evaluation_gcd=h,
        residual_denominator_resultant_gcd=gcd(Qh, R6),
        determinant_evaluations=len(indices), determinant_degree=e,
        phase_sha256=digest([[j, values[j]] for j in indices]),
        arithmetic_sha256=digest([word, profile, C, D, Gh, Ph, Qh, R, R6]))


def actual_corpus():
    source = json.loads(old.ACTUAL.read_text())['cycles']
    addition = json.loads(old.C007.read_text())['small_parameter_census']['new_normalized_cycles']
    fixtures = json.loads(old.FIXTURES.read_text())['cycles']
    require((len(source), len(addition), len(fixtures)) == (2459, 1, 11), 'corpus changed')
    unique, source_index, counts, transcript = {}, {}, Counter(), sha256()
    for raw in source:
        q, d, n = raw['reduced_denominator'], raw['d'], raw['primitive_states']
        row = old.certificate(q, n)
        require(raw['word'] == row['word'] and d % q == 0 and
                raw['states'] == [d//q*x for x in n], 'raw scaling changed')
        for j, x in enumerate(raw['states']):
            require(old.step(x, d) == (raw['states'][(j+1) % len(n)], row['word'][j]),
                    'raw source arrow failed')
        counts['raw_source_arrows'] += len(n)
        counts['scaled_source_instances'] += d//q > 1
        unique[q, tuple(n)] = row
        source_index[d, tuple(raw['states'])] = row
        feed(transcript, [d, q, raw['states'], row['word']])
    require(len(unique) == 1184, 'base normalized count changed')
    for raw in addition:
        row = old.certificate(raw['q'], raw['states'])
        unique[row['q'], tuple(row['states'])] = row
    require(len(unique) == 1185, 'combined normalized count changed')
    determinant_cases, factor_cases, q5_cases = [], [], []
    for row in sorted(unique.values(), key=lambda r: (r['q'], r['L'])):
        word, m = row['word'], row['m']
        A, D, g, q, values, states = base.intercepts(word)
        require(states == row['states'] and q == row['q'], 'actual reconstruction failed')
        profile = prior.polynomial_profile(word)
        phases, reduced = rotation_identity(word, profile)
        counts['original_exact_polynomial_gcds'] += 1
        counts['coprime_totals'] += gcd(A, m) == 1
        counts['nonconstant_G'] += profile['d'] > 0
        counts['cyclic_polynomial_and_residual_identities'] += m
        counts['nonidentity_rotation_phases'] += m-1
        counts['normalized_raw_arrows'] += m
        for j, P in enumerate(phases):
            require(evaluate(P, 3) == values[j] and gcd(evaluate(P, 3), D) == g,
                    'evaluation at three changed the original gcd obstruction')
            for p in (5, 7, 11, 13, 17, 19, 23, 31):
                if D % p == 0:
                    t = base.valuation(D, p)
                    require(min(t, base.valuation(values[j], p)) == base.valuation(g, p),
                            'truncated local evaluation valuation changed under rotation')
                    counts['truncated_prime_valuation_controls'] += 1
            if j:
                cut = invariant_cuts(word, j)
                counts['direct_invariant_cut_closures'] += 1
                counts['singleton_cut_refinements'] += cut[-1] == m
                feed(transcript, cut)
        bounded = m <= 10 or profile['d'] > 0 or (q == 5 and m == 17)
        if bounded:
            item = dict(q=q, L=min(states), m=m, A=A, g=g, G=profile['G'], e=profile['e'],
                        **determinant_control(word, profile, all_phases=(q == 5 and m == 17)))
            determinant_cases.append(item)
            counts['direct_resultant_cycles'] += 1
            counts['direct_resultant_evaluations'] += item['determinant_evaluations']
            if profile['d']:
                factor_cases.append(item)
            if q == 5 and m == 17:
                require(profile['G'] == [1] and g == 1015513, 'q5 numerical cancellation control changed')
                q5_cases.append(item)
        else:
            counts['cycles_outside_direct_resultant_scope'] += 1
        if m > 1:
            (s, _), _ = prior.minimum_distance(word)
            require(q >= 5 and m <= 5*s and D**s*4**m < 5**s*2**(A*s)*3**m,
                    'stored-cycle independent floor screen changed')
            counts['nonfixed_floor_screen_ineligible'] += 1
        feed(transcript, [q, states, word, profile, phases, reduced])
    fixture_records = []
    for fixture in fixtures:
        # Fixtures contain raw states at the named d, possibly a scaled copy.
        d, states = fixture['d'], fixture['states']
        row = source_index.get((d, tuple(states)))
        if row is None:
            n = states.index(min(states))
            states = states[n:]+states[:n]
            row = source_index[d, tuple(states)]
        for j, x in enumerate(states):
            require(old.step(x, d) == (states[(j+1) % len(states)], row['word'][j]),
                    'raw fixture arrow failed')
        fixture_records.append(dict(d=d, states=states, q=row['q'], word=row['word']))
    require(len(q5_cases) == 2 and len(factor_cases) == 20, 'declared resultant controls changed')
    return dict(counts=dict(sorted(counts.items())), raw_instances=len(source),
        source_parameters=len({x['d'] for x in source}), normalized_cycles=len(unique),
        fixtures=fixture_records, all_nonconstant_G_controls=factor_cases,
        q5_polynomial_coprime_numerical_cancellation=q5_cases,
        determinant_scope='Every original cycle with m<=10, every nonconstant G, and both q5 period17 controls. First two phases directly evaluated, or every phase for q5. All other phases use exact polynomial identities, not independent determinants.',
        maximum_direct_resultant_degree=max(x['e'] for x in determinant_cases),
        determinant_cases_sha256=digest(determinant_cases), full_corpus_sha256=transcript.hexdigest())


def c013_stress_correction():
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
    counts, by, transcript, examples = Counter(), defaultdict(Counter), sha256(), []
    for w, label in sorted(words.items()):
        word, m = list(w), len(w)
        A, D, g, q, values, states = base.intercepts(word)
        require(base.period(word) == m, 'stress word lost primitivity')
        (s, shift), distances = prior.minimum_distance(word)
        eligible = D**s*4**m >= 5**s*2**(A*s)*3**m
        passes = g**s*4**m < 2**(A*s)*3**m
        observed = q**s*3**m >= 4**m
        require(passes and observed, 'historical stress arithmetic changed')
        counts['words'] += 1
        counts['candidate_passes'] += passes
        counts['observed_q_stronger_inequality'] += observed
        counts['floor_screen_eligible'] += eligible
        counts['raw_arrows'] += m
        counts['rotation_distances'] += len(distances)
        category = 's2_already_proved_C011' if s == 2 else 's_at_least3'
        for key in (category, label[0]):
            by[key]['words'] += 1
            by[key]['floor_screen_eligible'] += eligible
        row = dict(label=label, m=m, A=A, s=s, shift=shift, g_bits=g.bit_length(),
                   q_bits=q.bit_length(), floor_screen_eligible=eligible)
        if eligible and s >= 3 and len(examples) < 4:
            examples.append(dict(row, g=g, q=q))
        feed(transcript, [row, word, D, g, q, distances])
    require(counts['words'] == 243 and counts['floor_screen_eligible'] == 178 and
            by['s_at_least3']['floor_screen_eligible'] == 96 and
            by['s2_already_proved_C011']['floor_screen_eligible'] == 82, 'corrected coverage changed')
    return dict(counts=dict(counts), by={k: dict(v) for k, v in sorted(by.items())},
        selected_eligible_examples=examples, transcript_sha256=transcript.hexdigest(),
        correction='The observed-q test contains g through q=D/g. Thus all243 measured-q successes are not independent reasons to call the generated tests nondiscriminating. 178 exceed the q>1 universal floor screen, including96 with s>=3; these are successful finite evidence, not a theorem. The actual corpus remains floor-screen ineligible. Historical arithmetic and files are unchanged.',
        floor_scope='The floor q>=5 applies only after q>1 is known. No q1 hypothetical cycle is discarded by this screen.')


def c012_stress_correction():
    words = []
    for r in (2, 3, 4):
        ts = (1, 2, 4, 6, 8, 16, 20, 23, 32) if r == 2 else (1, 2, 4, 6, 8, 16, 20, 32)
        for t in ts:
            words.append((['primitive', r, t], ([1]*t+[2]*(2*t))*(r-1)+[1]*t+[2]*(3*t)))
    for background in ([2], [3], [1, 2, 2], [1, 1, 2, 3, 1, 1, 2, 4]):
        for repetitions in (2, 3, 4):
            words.append((['repeated', background, repetitions], background*repetitions))
    counts, transcript = Counter(), sha256()
    for label, word in words:
        A, D, g, q, values, states = base.intercepts(word)
        m = len(word)
        counts['words'] += 1
        for shift in range(1, m):
            s = sum(a != b for a, b in zip(word, base.rotate(word, shift)))
            if s == 0:
                counts['zero_shifts_kept_separate'] += 1
                continue
            eligible = D**s*4**m >= 5**s*2**(A*s)*3**m
            require(g**s*4**m < 2**(A*s)*3**m and q**s*3**m >= 4**m,
                    'C012 generated arithmetic changed')
            counts['nonzero_rotations'] += 1
            counts['floor_screen_eligible'] += eligible
            counts[label[0]+'_eligible'] += eligible
            counts['s2_eligible'] += eligible and s == 2
            counts['s_at_least3_eligible'] += eligible and s >= 3
            feed(transcript, [label, word, shift, s, D, g, q, eligible])
    require(counts['words'] == 37 and counts['nonzero_rotations'] == 2887 and
            counts['zero_shifts_kept_separate'] == 24 and counts['floor_screen_eligible'] == 178 and
            counts['s_at_least3_eligible'] == 178 and counts['repeated_eligible'] == 0,
            'C012 corrected coverage changed')
    return dict(counts=dict(counts), transcript_sha256=transcript.hexdigest(),
        correction='The same measured-q interpretation error also affects C012 generated controls:178 of its2887 nonzero rotations exceed the q>1 floor screen. Historical exact arithmetic, determinant controls and zero-shift exclusions are unchanged. These counts concern rotations, unlike C013 counts of one strongest shift per word.')


def two_run_controls():
    records = []
    for t in (1, 2, 3, 6, 12, 18, 24):
        word = [1]*t+[2]*(2*t+1)
        A, D, g, q, values, states = base.intercepts(word)
        m = len(word)
        require((m, A) == (3*t+1, 5*t+2) and gcd(A, m) == 1 and A < 2*m and
                base.period(word) == m and prior.minimum_distance(word)[0][0] == 2,
                'two-run domain changed')
        numerator, denominator = 2**(t*(2*t+1))-1, (2**t-1)*(2**(2*t+1)-1)
        require(numerator % denominator == 0, 'two-run resultant quotient not integral')
        quotient = numerator//denominator
        predicted = 2**(13*t*t+5*t)*quotient
        if t <= 6:
            p = prior.polynomial_profile(word)
            require(p['G'] == [1] and abs(prior.resultant(p['P'], p['Q'])) == predicted,
                    'two-run independently computed resultant disagrees')
            # All phases in these bounded examples exercise invariance separately.
            determinant = determinant_control(word, p, all_phases=True)
        else:
            determinant = None
        R6 = prior.strip6(predicted)
        require(R6 % g == 0, 'family resultant missed numerical cancellation')
        ell = 2*t+1
        require(values[0] == 2**(t+1)*(4**ell-3**ell)-D and
                g == gcd(3**t-2**t, 4**ell-3**ell) == gcd(3**t-2**t, 4**(t+1)-3),
                'independent evaluated two-arc gcd formula failed')
        if t % 6 == 0:
            require(gcd(quotient, 6) == 1 and R6 == quotient and R6 > D,
                    'declared finite large-height control failed')
        records.append(dict(t=t, m=m, A=A, D=D, g=g, q=q,
            resultant_bits=predicted.bit_length(), prime_to_six_part=R6,
            denominator_resultant_gcd=gcd(D, R6), direct_determinant=determinant,
            raw_states_sha256=digest(states)))
    p = prior.polynomial_profile([1]*3+[2]*7)
    roots = [x for x in range(7) if evaluate(p['P'], x) % 7 == evaluate(p['Q'], x) % 7 == 0]
    require(roots == [4] and evaluate(p['Q'], 3) % 7 == 0 and evaluate(p['P'], 3) % 7 == 2,
            'extraneous evaluation-prime control changed')
    return dict(cases=records, spurious_prime_control=dict(t=3, prime=7,
        common_roots_mod_prime=roots, evaluation_point=3, P_at_3_mod_prime=2,
        actual_g=1, denominator_resultant_gcd=7),
        scope='Direct Sylvester determinants only at t1,2,3,6. Larger selected t use the separately written resultant formula, with exact arrows and gcd checks. Large R6 refutes its use as a useful uniform height bound here; it does not refute exact gcd(D,R6) information, which equals1 at t6,12,18,24.')


def coverage_controls():
    result = []
    for p in (5, 7, 19, 41, 101):
        require(all(p % d for d in range(2, isqrt(p)+1)), 'declared prime is composite')
        A0 = (3**p).bit_length()
        mechanical = [(j+1)*A0//p-j*A0//p for j in range(p)]
        require(mechanical[-1] == 2 and set(mechanical) <= {1, 2}, 'mechanical control changed')
        word = mechanical[:-1]+[3]
        A, D, g, q, values, states = base.intercepts(word)
        (s, shift), distances = prior.minimum_distance(word)
        phase_shift = pow(A0, -1, p)
        j = p-phase_shift
        phase_mismatches = [i for i in range(p) if word[i] != word[(i+phase_shift) % p]]
        require(phase_mismatches == [j-1, j, p-1], 'prime mechanical-phase mismatch set changed')
        require(A == A0+1 and A < 2*p and base.period(word) == p and s == 3 and
                base.direct_data(mechanical)[1] == values[0] and 18*min(values) > p*D,
                'prime-period obstruction control failed')
        if p >= 19:
            require(min(states) > q, 'q<=L prime-period control failed')
        closures = []
        for h in range(1, p):
            cut = invariant_cuts(word, h)
            require(cut[-1] == p, 'invariant mismatch-cut closure did not fill prime period')
            closures.append(cut)
        # Every repetition and representation is handled by the written
        # prime-period argument, not inferred from this finite cut test.
        result.append(dict(prime_period=p, mechanical_A=A0, A=A, g=g, q=q,
            minimum_distance=s, witness_shift=shift, normalized_minimum_floor=min(states)//q,
            mechanical_phase_shift=phase_shift, phase_mismatch_positions=phase_mismatches,
            raw_arrows=p, invariant_cut_closures=len(closures),
            all_states_exceed_q=min(states) > q, states_sha256=digest(states),
            cuts_sha256=digest(closures)))
    return dict(cases=result, scope='Finite arrows, minimum bound, mismatch distances and invariant-cut closures. The assertion about every repetition and every common-background representation is a separate written prime-period theorem, not an exhaustive finite enumeration.')


def side_source_audit():
    paths = ['sidekick/DIRECTIONS.md', 'sidekick/FEED.md',
             'sidekick/probes/c012_candidate_check.py', 'sidekick/probes/c012_candidate_check.json']
    contents = {p: subprocess.check_output(['git', 'show', SIDE+':'+p], cwd=ROOT) for p in paths}
    receipt = json.loads(contents[paths[-1]])
    require(receipt['structured_search']['structured_words_tested'] == 59759 and
            receipt['structured_search']['discriminating'] == 56150, 'side reported receipt changed')
    return dict(reviewed_commit=SIDE, file_sha256={p: sha256(b).hexdigest() for p, b in contents.items()},
        reported_structured_words=59759, reported_floor_screen_eligible=56150,
        reported_failures=receipt['structured_search']['counterexamples'],
        independent_replay=False,
        scope='Read-only source and receipt audit. The exact threshold matches C014. The side sample and exhaustive grid were not rerun; counts are externally reported. Eligible means beyond the q>1 floor, not a proof or a near-failure.')


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--check', action='store_true')
    args = parser.parse_args()
    dependencies = [C013, C013.parent/'overlap_audit.json', prior.C012,
                    prior.C012.parent/'coupled_system_audit.json', base.C009,
                    old.ACTUAL, old.C007, old.FIXTURES]
    receipt = dict(schema='C014-overlap-arithmetic-v1', status='PASS',
        clock='raw positive odd-only 3x+d, no absorber',
        checker_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        source_sha256={str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in dependencies},
        actual=actual_corpus(), c013_stress_correction=c013_stress_correction(),
        c012_stress_correction=c012_stress_correction(),
        two_run_resultant=two_run_controls(), prime_period_coverage=coverage_controls(),
        side_source_audit=side_source_audit(),
        scope='Finite checks, explicit interpretation correction and scoped obstructions only. No new census, universal mismatch law, Collatz exclusion, novelty or formal-verification claim.')
    path = HERE/'overlap_arithmetic_audit.json'
    if args.write:
        path.write_text(json.dumps(receipt, indent=2, sort_keys=True)+'\n')
    require(path.exists() and json.loads(path.read_text()) == receipt, 'saved receipt differs from exact replay')
    print(json.dumps(dict(status='PASS', actual_counts=receipt['actual']['counts'],
        candidate_counts=receipt['c013_stress_correction']['counts'], receipt=str(path.relative_to(ROOT))), sort_keys=True))


if __name__ == '__main__':
    main()
