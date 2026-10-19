#!/usr/bin/env python3
"""Replay exact integer gap coordinates and local odd rounding on stored cycles.

No new cycle search. Rational additive-one rescalings are relaxation controls,
not integer cycles. The compact receipt stores summaries, full-record digests,
and selected exact witnesses instead of every intermediate vector.
"""
import argparse
from collections import Counter
from fractions import Fraction
from functools import reduce
from hashlib import sha256
import importlib.util
import itertools
import json
from math import gcd, lcm
from pathlib import Path
import sys

if sys.flags.optimize:
    raise SystemExit('FAIL: optimized Python is not supported')

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
C009 = HERE.parent/'C009/check_excursions.py'
spec = importlib.util.spec_from_file_location('c009_cycle_certificates', C009)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
require = old.require


def pair(value):
    value = Fraction(value)
    return [value.numerator, value.denominator]


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def vector_gcd(v):
    return reduce(gcd, v, 0)


def common_denominator(v):
    return reduce(lcm, (Fraction(x).denominator for x in v), 1)


def E(v, power=1):
    m = len(v)
    return [2**((j+power)//m)*v[(j+power) % m] for j in range(m)]


def U(v):
    return [a-b for a, b in zip(E(v), v)]


def inverse_U(g):
    total = sum(g)
    result, prefix = [], 0
    for value in g:
        result.append(total+prefix)
        prefix += value
    return result


def M(v, s):
    return [2*a-3*b for a, b in zip(E(v, s), v)]


def sharp_bound(q, a, b):
    """Necessary adjacent normalized gap, including seam height b=-1."""
    require(q > 0 and gcd(q, 6) == 1 and a >= 0 and b >= -1,
            'invalid adjacent-bound domain')
    if a == b:
        return Fraction(2, 2**a)
    if b < a:
        return Fraction(1, 2**a)
    k = b-a
    eta = 6 if k % 2 == 0 else 2 if q % 6 == 1 else 4
    result = Fraction(q*(2**k-1)+eta, 3*2**b)
    r = result*2**b
    require(r.denominator == 1 and r.numerator % 2 == 1 and r > 0,
            'sharp bound does not have an odd numerator')
    require(3*r > q*(2**k-1) and (r == 1 or 3*(r-2) <= q*(2**k-1)),
            'sharp adjacent bound is not the least admissible odd integer')
    return result


def odd_ceiling(value):
    value = Fraction(value)
    ceiling = -(-value.numerator//value.denominator)
    return ceiling if ceiling % 2 else ceiling+1


def gap_audit(row):
    n, h, B, order, q = (row[k] for k in ('states', 'heights', 'B', 'sorted_indices', 'q'))
    H = [h[i] for i in order]
    W = [2**(B-a) for a in H]
    Z = [n[i]*w for i, w in zip(order, W)]
    G = U(Z)
    m = len(n)
    require(all(g > 0 for g in G) and sum(G) == Z[0] == row['L']*2**B,
            'positive gap or seam sum failed')
    require(inverse_U(G) == Z and U(inverse_U(G)) == G, 'integer inverse failed')
    require(E(Z, m) == [2*z for z in Z], 'dyadic extension failed')
    require(vector_gcd(G) == vector_gcd(Z) == 1, 'reduced integer coordinate gcd failed')
    require([z & -z for z in Z] == W, 'exact dyadic valuations failed')
    require(common_denominator([Fraction(g, q) for g in G]) == q,
            'gap rescaling loses the reduced denominator')
    require(common_denominator([Fraction(z, q) for z in Z]) == q,
            'state rescaling loses the reduced denominator')
    detail = dict(q=q, L=row['L'], m=m, A=row['A'], B=B, states=n,
        word=row['word'], sorted_heights=H, scaled_states=Z, scaled_gaps=G,
        coordinate_gcd=1, additive_one_common_denominator=q,
        ordered_domain=row['ordered_domain'])
    if row['ordered_domain']:
        s = row['A']-m
        require(1 <= s <= m and (s < m or m == 1), 'rank shift convention failed')
        T = U(W)
        require(M(Z, s) == [q*w for w in W], 'sorted state recurrence failed')
        require(M(G, s) == [q*t for t in T], 'full gap recurrence failed')
        require(U(M(Z, s)) == M(U(Z), s), 'rank operator commutation failed')
        identity_left = 2*sum(G[:s])-sum(G)
        require(identity_left == q*2**B == q*sum(T), 'exact linear sum identity failed')
        gaps = [Fraction(g, 2**B) for g in G]
        bounds = [sharp_bound(q, a, b) for a, b in zip(H, H[1:]+[-1])]
        slacks = [g-b for g, b in zip(gaps, bounds)]
        require(all(x >= 0 for x in slacks), 'actual odd lattice rounding failed')
        V = sum((Fraction(1, 2**a)-Fraction(1, 2**b)
                 for a, b in zip(H, H[1:]+[-1]) if b > a), Fraction(0))
        R = sum(bounds)
        gamma = R-Fraction(q, 3)*V
        require(sum(gaps) == row['L'] and row['L'] >= R and
                row['L'] >= odd_ceiling(R) and
                Fraction(q)*(Fraction(row['L'], q)-V/3) >= gamma,
                'summed local rounding identity failed')
        one_bounds = [sharp_bound(1, a, b) for a, b in zip(H, H[1:]+[-1])]
        one_slacks = [g/q-b for g, b in zip(gaps, one_bounds)]
        pair_checks, one_pair_checks = [], []
        for j in range(m):
            for length in range(1, m):
                k = j+length
                target_height = H[k % m]-k//m
                delta = Fraction(2**(k//m)*Z[k % m]-Z[j], 2**B)
                require(delta > 0 and
                        3*delta+q*(Fraction(2**(k//m)*W[k % m]-W[j], 2**B)) > 0,
                        'circular pair lost geometric or image order')
                bound = sharp_bound(q, H[j], target_height)
                one_bound = sharp_bound(1, H[j], target_height)
                require(delta >= bound, 'actual circular pair rounded bound failed')
                pair_checks.append([j, k, pair(delta), pair(bound)])
                one_pair_checks.append(delta/q >= one_bound)
        detail.update(rank_shift=s, forcing_without_q=T,
            linear_sum_identity=identity_left, normalized_gaps=[pair(x) for x in gaps],
            actual_rounding_bounds=[pair(x) for x in bounds],
            actual_rounding_slacks=[pair(x) for x in slacks],
            upward_variation=pair(V), summed_bound=pair(R), odd_ceiled_sum_bound=odd_ceiling(R),
            gamma=pair(gamma), circular_pair_checks=len(pair_checks),
            circular_pair_checks_sha256=digest(pair_checks),
            additive_one_minimum=pair(Fraction(row['L'], q)),
            additive_one_rounding_bounds=[pair(x) for x in one_bounds],
            additive_one_rounding_slacks=[pair(x) for x in one_slacks],
            additive_one_all_local_bounds_pass=all(x >= 0 for x in one_slacks),
            additive_one_sum_bound_pass=Fraction(row['L'], q) >= sum(one_bounds),
            additive_one_odd_ceiled_sum_bound=odd_ceiling(sum(one_bounds)),
            additive_one_odd_ceiled_sum_pass=Fraction(row['L'], q) >= odd_ceiling(sum(one_bounds)),
            additive_one_all_circular_pairs_pass=all(one_pair_checks),
            additive_one_circular_pair_failures=sum(not x for x in one_pair_checks))
    return detail


def load_cycles():
    source = json.loads(old.ACTUAL.read_text())
    additions = json.loads(old.C007.read_text())['small_parameter_census']['new_normalized_cycles']
    fixtures = json.loads(old.FIXTURES.read_text())['cycles']
    require(len(source['cycles']) == 2459 and len(fixtures) == 11 and len(additions) == 1,
            'stored corpus sizes changed')
    unique, source_index = {}, {}
    raw_arrows, scaled = 0, 0
    source_records = []
    for raw in source['cycles']:
        q, n, d = raw['reduced_denominator'], raw['primitive_states'], raw['d']
        row = old.certificate(q, n)
        require(d % q == 0, 'source scale is not an integer')
        scale = d//q
        require(raw['states'] == [scale*x for x in n] and raw['word'] == row['word'],
                'source scaling or valuation failed')
        for i, x in enumerate(raw['states']):
            require(old.step(x, d) == (raw['states'][(i+1) % len(n)], row['word'][i]),
                    'raw source arrow failed')
        unique[q, tuple(n)] = row
        source_index[d, tuple(raw['states'])] = row
        source_records.append([d, q, n, raw['states'], row['word']])
        raw_arrows += len(n)
        scaled += scale > 1
    require(len(unique) == 1184 and raw_arrows == 36912 and scaled == 1275,
            'source cycle coverage changed')
    for raw in additions:
        row = old.certificate(raw['q'], raw['states'])
        unique[row['q'], tuple(row['states'])] = row
    require(len(unique) == 1185, 'combined normalized corpus changed')
    records = [gap_audit(row) for row in sorted(unique.values(), key=lambda r: (r['q'], r['L']))]
    controls = []
    for i, fixture in enumerate(fixtures):
        row = source_index[fixture['d'], tuple(fixture['states'])]
        require(row['word'] == fixture['valuations'], 'fixture valuations changed')
        controls.append(dict(fixture_id=i+1, d=fixture['d'], states=fixture['states'],
            reduced_q=row['q'], scale=fixture['d']//row['q'],
            gap_record_sha256=digest(gap_audit(row))))
    counts = Counter()
    for r in records:
        counts['normalized_cycles'] += 1
        counts['normalized_arrows'] += r['m']
        counts['coordinate_gcd_one'] += r['coordinate_gcd'] == 1
        if r['ordered_domain']:
            counts['ordered_cycles'] += 1
            counts['ordered_nonfixed_cycles'] += r['m'] > 1
            counts['ordered_arrows'] += r['m']
            counts['ordered_wide_cycles'] += r['B'] > 0
            counts['actual_sharp_local_rounding_checks'] += r['m']
            counts['actual_sharp_circular_pair_checks'] += r['circular_pair_checks']
            counts['actual_sharp_rounding_equalities'] += sum(x == [0, 1] for x in r['actual_rounding_slacks'])
            counts['rescaled_additive_one_local_pass'] += r['additive_one_all_local_bounds_pass']
            counts['rescaled_additive_one_local_fail'] += not r['additive_one_all_local_bounds_pass']
            counts['rescaled_additive_one_sum_pass'] += r['additive_one_sum_bound_pass']
            counts['rescaled_additive_one_sum_fail'] += not r['additive_one_sum_bound_pass']
            counts['rescaled_additive_one_odd_ceiled_sum_pass'] += r['additive_one_odd_ceiled_sum_pass']
            counts['rescaled_additive_one_all_circular_pairs_pass'] += r['additive_one_all_circular_pairs_pass']
            counts['rescaled_additive_one_circular_pair_failures'] += r['additive_one_circular_pair_failures']
            if r['q'] > 1:
                counts['noninteger_rescaled_additive_one_local_pass'] += r['additive_one_all_local_bounds_pass']
    require(counts['ordered_cycles'] == 52 and counts['ordered_nonfixed_cycles'] == 51,
            'ordered domain count changed')
    index = {(r['q'], r['L']): r for r in records}
    chosen = [index[k] for k in [(1, 1), (5, 19), (5, 347), (7, 5), (13, 283), (83, 157), (233, 1907), (29, 7055)]]
    require(index[5, 19]['additive_one_all_local_bounds_pass'] and
            index[13, 283]['additive_one_all_local_bounds_pass'] and
            not index[83, 157]['additive_one_all_local_bounds_pass'],
            'sharp relaxation controls changed')
    require(index[5, 19]['additive_one_all_circular_pairs_pass'] and
            index[5, 19]['additive_one_odd_ceiled_sum_pass'],
            'global rounded relaxation control changed')
    return dict(source_cycles=2459, source_parameters=len({r['d'] for r in source['cycles']}),
        scaled_source_instances=scaled, source_raw_arrows=raw_arrows,
        C007_new_distinct_cycles=1, counts=dict(sorted(counts.items())),
        all_source_checks_sha256=digest(source_records), all_gap_records_sha256=digest(records),
        fixture_controls=controls, selected_controls=chosen,
        scope='Every stored raw source instance and every reduced normalized cycle was checked. All eleven raw fixture controls retain their own parameter and scaling. The additive-one rescalings with q>1 remain rational cycles with common denominator q, even when every local and summed rounding inequality passes.')


def determinant(a):
    """Fraction-based Gaussian determinant; independent of special matrix forms."""
    a = [[Fraction(x) for x in row] for row in a]
    result = Fraction(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        value = a[j][j]
        result *= value
        for i in range(j+1, len(a)):
            multiplier = a[i][j]/value
            for k in range(j+1, len(a)):
                a[i][k] -= multiplier*a[j][k]
    require(result.denominator == 1, 'integer determinant became nonintegral')
    return result.numerator


def matrix_of(fn, m):
    columns = [fn([int(i == j) for i in range(m)]) for j in range(m)]
    return [[columns[j][i] for j in range(m)] for i in range(m)]


def independent_grid():
    counts = Counter()
    transcript = sha256()
    for m in range(1, 7):
        for raw in itertools.product(range(-2, 3), repeat=m):
            v = list(raw)
            g = U(v)
            require(inverse_U(g) == v and U(inverse_U(v)) == v, 'signed-grid inverse failed')
            require(vector_gcd(g) == vector_gcd(v), 'signed-grid gcd failed')
            powers = [E(v, k) for k in range(m)]
            require([sum(values) for values in zip(*powers)] == inverse_U(v),
                    'geometric inverse identity failed')
            require(E(v, m) == [2*x for x in v], 'signed-grid E^m failed')
            counts['integer_vectors'] += 1
            for s in range(m+1):
                require(U(M(v, s)) == M(U(v), s), 'grid commutation failed')
                counts['rank_operator_commutations'] += 1
            for d in (1, 3, 5, 7):
                rational = [Fraction(x, d) for x in v]
                transformed = U(rational)
                require(inverse_U(transformed) == rational and
                        common_denominator(transformed) == common_denominator(rational),
                        'rational common-denominator invariant failed')
                counts['rational_vectors'] += 1
            transcript.update(json.dumps([v, g], separators=(',', ':')).encode()+b'\n')
    matrices = []
    for m in range(1, 13):
        det_u = determinant(matrix_of(U, m))
        require(abs(det_u) == 1, 'U determinant is not a unit')
        counts['unimodular_determinants'] += 1
        for s in range(1, m+1):
            if gcd(s, m) != 1:
                continue
            det_m = determinant(matrix_of(lambda v: M(v, s), m))
            require(abs(det_m) == abs(2**(m+s)-3**m), 'rank matrix determinant failed')
            matrices.append(dict(m=m, s=s, det_U=det_u, det_M=det_m,
                                 D=2**(m+s)-3**m))
            counts['coprime_rank_determinants'] += 1
    rounding = []
    for q in range(1, 102, 2):
        if q % 3 == 0:
            continue
        for a in range(6):
            for b in range(-1, 6):
                value = sharp_bound(q, a, b)
                rounding.append([q, a, b, pair(value)])
    counts['independent_sharp_bound_checks'] = len(rounding)
    return dict(counts=dict(sorted(counts.items())), integer_grid={'dimensions': [1, 6], 'entries': [-2, 2]},
        rational_denominators=[1, 3, 5, 7], all_integer_vectors_sha256=transcript.hexdigest(),
        matrix_controls=matrices, rounding_checks_sha256=digest(rounding),
        scope='Signed vectors verify the exact linear coordinate identities without positivity or cycle assumptions. Common denominator is the least common denominator, including unreduced test inputs. The determinant grid is finite evidence, not a substitute for the written unimodularity and rank-matrix proofs.')


def mechanical_complete_gaps():
    """Four exact examples of the written all-size mechanical obstruction."""
    summaries, transcript, counts = [], sha256(), Counter()
    for A, m in ((5, 3), (8, 5), (65, 41), (485, 306)):
        require(gcd(A, m) == 1 and A >= m, 'mechanical totals are not legal coprime totals')
        D = 2**A-3**m
        require(D > 0, 'mechanical cycle is not positive')
        phases = []
        for ell in range(m):
            terms = [3**(m-1-j)*2**((j*A+ell)//m) for j in range(m)]
            require(all(2*t > 3**(m-1) for t in terms),
                    'mechanical term lower bound failed')
            phases.append(sum(terms))
            counts['phase_intercept_summands'] += len(terms)
        chronological = [phases[(i*A) % m] for i in range(m)]
        row = old.certificate(D, chronological)
        require(row['A'] == A and row['C'] == phases[0] and row['D'] == D and
                row['q'] == D and row['B'] == 0 and row['ordered_domain'] and
                row['states'] == chronological, 'mechanical exact-cycle classification failed')
        require(row['word'] == [(i+1)*A//m-i*A//m for i in range(m)],
                'mechanical word changed')
        require(row['sorted_indices'] == sorted(range(m), key=chronological.__getitem__) and
                [chronological[i] for i in row['sorted_indices']] == phases,
                'mechanical phase order failed')
        gaps = U(phases)
        monomials = []
        for ell in range(m-1):
            j = ((m-1-ell)*pow(A, -1, m)) % m
            require(1 <= j < m and (j*A+ell) % m == m-1,
                    'unique jumping summand index failed')
            monomial = 3**(m-1-j)*2**((j*A+ell)//m)
            require(gaps[ell] == monomial, 'exact interior gap monomial failed')
            monomials.append([ell, j, monomial])
        require(gaps[-1] == 2*phases[0]-phases[-1] == 3**(m-1),
                'exact mechanical seam failed')
        require(all(2*g > 3**(m-1) for g in gaps),
                'complete-gap lower bound failed')
        require(vector_gcd(gaps) == vector_gcd(phases) == 1 and
                common_denominator([Fraction(g, D) for g in gaps]) == D,
                'mechanical full-gap denominator failed')
        require(all(g >= (2 if j < m-1 else 1) for j, g in enumerate(gaps)),
                'actual mechanical rounded bound failed')
        lower = Fraction(3**(m-1), 2*D)
        minimum = Fraction(min(gaps), D)
        require(minimum > lower and Fraction(phases[0], D) > m*lower,
                'exact rational lower comparison failed')
        pair_failures = 0
        pair_transcript = sha256()
        for j in range(m):
            for length in range(1, m):
                k = j+length
                delta = 2**(k//m)*phases[k % m]-phases[j]
                bound = 2 if k < m else 1
                require(Fraction(bound) == sharp_bound(1, 0, -(k//m)),
                        'mechanical proper-pair bound changed')
                require(delta >= min(gaps), 'proper circular gap below minimum adjacent gap')
                pair_failures += delta < bound*D
                pair_transcript.update(json.dumps([j, k, delta, bound], separators=(',', ':')).encode()+b'\n')
                counts['proper_circular_pair_checks'] += 1
        if minimum > 2:
            require(pair_failures == 0 and Fraction(phases[0], D) >= 2*m-1,
                    'large-gap mechanical relaxation should pass all bounds')
        complete_record = dict(A=A, m=m, D=D, phases=phases, gaps=gaps, word=row['word'],
                               chronological_states=chronological, interior_monomials=monomials)
        record_hash = digest(complete_record)
        transcript.update(record_hash.encode()+b'\n')
        summaries.append(dict(A=A, m=m, q=D, reduced_denominator=D, all_heights_zero=True,
            complete_gap_record_sha256=record_hash, minimum_rational_gap=pair(minimum),
            strict_gap_lower_bound=pair(lower), minimum_rational_state=pair(Fraction(phases[0], D)),
            seam_gap_numerator=gaps[-1], seam_gap_formula='3^(m-1)',
            additive_one_minimum_gap_greater_than_two=minimum > 2,
            additive_one_all_circular_pairs_pass=pair_failures == 0,
            additive_one_circular_pair_failures=pair_failures,
            additive_one_rounded_sum=2*m-1,
            pair_checks_sha256=pair_transcript.hexdigest()))
        counts['cycles'] += 1
        counts['raw_cycle_arrows'] += m
        counts['interior_monomials'] += m-1
        counts['exact_seam_checks'] += 1
        counts['noninteger_shapes_passing_all_pair_bounds'] += pair_failures == 0
    return dict(cases=summaries, counts=dict(sorted(counts.items())),
        complete_records_sha256=transcript.hexdigest(),
        scope='Four generated exact primitive mechanical cycles with reduced denominator D, not new census discoveries. All phases, raw arrows, interior monomials and exact seams were checked. The written upper-approximation argument proves arbitrarily large full gaps; these four finite cases do not establish that limit by themselves. Additive-one rescaling keeps denominator D and is never labeled an integer cycle.')


def rejection_controls():
    probes = [lambda: old.certificate(1, [1, 1]), lambda: old.certificate(1, [7, 11, 17, 13]),
              lambda: old.certificate(5, [38, 62, 98]), lambda: old.certificate(3, [1]),
              lambda: old.word_data([0, 2])]
    count = 0
    for probe in probes:
        try:
            probe()
        except ValueError:
            count += 1
        else:
            raise ValueError('invalid raw-cycle control accepted')
    Z, W = [8, 10, 13], [2, 2, 1]
    require(M(Z, 2) == W and [x & -x for x in Z] != W,
            'zero-valuation affine control changed')
    return dict(rejected_inputs=count, zero_valuation_affine_control=dict(
        raw_states=[4, 13, 5], chronological_valuations=[0, 3, 2],
        sorted_scaled_states=Z, prescribed_powers=W,
        observed_lowbits=[x & -x for x in Z],
        scope='The affine loop has valuation zero and even states; its integral sorted-gap solution is not an odd-only cycle. Positive valuation hypotheses are required before deriving the exact lowbits from integrality.'))


def report():
    paths = [Path(__file__), C009, old.ACTUAL, old.C007, old.FIXTURES,
             HERE.parent/'C004/SIZE_PROBE.md']
    return dict(schema='C010-integer-gaps-v1', status='PASS',
        clock='Primitive positive raw odd-only cycles without an absorber. q is the reduced denominator; d-scalings are checked separately.',
        source_sha256={str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in paths},
        existing=load_cycles(), independent_grid=independent_grid(),
        mechanical_complete_gaps=mechanical_complete_gaps(), rejection_controls=rejection_controls(),
        scope='Integer gap coordinates are an invertible integer change of variables retaining the exact denominator obstruction. Local odd rounding and its sum are necessary inequalities; rational additive-one controls can pass them. No new denominator-one exclusion, universal cycle classification, novelty claim, or formal verification is asserted.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = report()
    path = HERE/'integer_gap_audit.json'
    if args.write:
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(path.exists() and json.loads(path.read_text()) == result,
                'receipt differs from exact recomputation')
    print(json.dumps(dict(status='PASS', mode='write' if args.write else 'replay',
        counts=result['existing']['counts'], grid=result['independent_grid']['counts'],
        mechanical=result['mechanical_complete_gaps']['counts'],
        fixtures=len(result['existing']['fixture_controls'])), sort_keys=True))


if __name__ == '__main__':
    main()
