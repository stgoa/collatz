#!/usr/bin/env python3
"""Exact C004 rotation and geometry audit of the pinned C001 raw cycles.

The minimum-pair-gap proposal is tested, not assumed. A failed proposal is
recorded as a mathematical counterexample; a failed identity rejects replay.
The universal statements are proved separately in the written notes; these
finite data alone imply no general size bound. State1 remains raw throughout.
"""

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations,permutations,product
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
BASELINE = '7270d956e1f7037e48b92493024f4f1baefd61d8'
MODULI = (2,3,4,8,9,16)
MATRIX_MAX_LENGTH = 4
MATRIX_MAX_VALUATION = 4
MECHANICAL_LENGTHS = tuple(range(2,257))+(306,)
SPREAD_MAX_LENGTH = 8
SPREAD_MAX_VALUATION = 4


def require(test,message):
    if not test:
        raise ValueError(message)


def rational(n,d=1):
    f = Fraction(n,d)
    return dict(numerator=f.numerator,denominator=f.denominator)


def stream_add(hasher,value):
    hasher.update(json.dumps(value,sort_keys=True,separators=(',',':')).encode()+b'\n')


def raw_step(n,d):
    require(type(n) is int and n > 0 and n % 2 == 1 and
            type(d) is int and d > 0 and gcd(d,6) == 1,'invalid raw odd input')
    z = 3*n+d
    a = (z & -z).bit_length()-1
    return z >> a,a


def direct(word):
    require(word and all(type(a) is int and a >= 1 for a in word),'invalid valuation word')
    c,A = 0,0
    for a in word:
        c = 3*c+2**A
        A += a
    return c,2**A-3**len(word),A


def mechanical_word(A,m):
    require(type(A) is int and type(m) is int and A >= m >= 1,'invalid mechanical totals')
    return tuple((j+1)*A//m-j*A//m for j in range(m))


def mechanical_rotation(word):
    base = mechanical_word(sum(word),len(word))
    for offset in range(len(word)):
        if tuple(word) == base[offset:]+base[:offset]:
            return offset
    return None


def short_spread_checks():
    counts = Counter()
    digest = sha256()
    examples = []
    for m in range(1,SPREAD_MAX_LENGTH+1):
        for word in product(range(1,SPREAD_MAX_VALUATION+1),repeat=m):
            C,D,A = direct(word)
            counts['words'] += 1
            if D < 0:
                counts['negative_D'] += 1
                stream_add(digest,[word,C,D,'negative_D'])
                continue
            counts['positive_realizations'] += 1
            g = gcd(C,D)
            n,den = C//g,D//g
            states = []
            for a in word:
                states.append(n)
                n,actual = raw_step(n,den)
                require(actual == a,'short spread realization valuation failed')
                counts['raw_arrows'] += 1
            require(n == states[0],'short spread realization did not close')
            primitive = len(set(states)) == m
            counts['primitive_displayed_words'] += int(primitive)
            counts['proper_power_words'] += int(not primitive)
            small_spread = max(states) < 2*min(states)
            offset = mechanical_rotation(word)
            require(small_spread == (offset is not None),
                    'short-word small-spread/mechanical equivalence counterexample')
            counts['spread_equivalence_checks'] += 1
            counts['mechanical_words'] += int(offset is not None)
            if not primitive:
                counts['proper_power_mechanical_words'] += int(offset is not None)
            if m == 1:
                counts['fixed_points'] += 1
            if primitive and m > 1 and small_spread:
                require(gcd(A,m) == 1,'primitive mechanical totals are not coprime')
                require(g == 1,'primitive small-spread coefficient cancellation is nontrivial')
                counts['nontrivial_primitive_spread_checks'] += 1
                if len(examples) < 12:
                    examples.append(dict(word=list(word),denominator=den,states=states,
                                         mechanical_rotation_offset=offset))
            require(max(states) != 2*min(states),'odd numerator spread equals2')
            stream_add(digest,[word,C,D,g,primitive,small_spread,offset])
    require((counts['words'],counts['positive_realizations'],counts['primitive_displayed_words'],
             counts['nontrivial_primitive_spread_checks']) == (87380,86442,86106,297),
            'short spread exact census changed')
    return dict(domain=dict(lengths=[1,SPREAD_MAX_LENGTH],valuations=[1,SPREAD_MAX_VALUATION]),
                counts=dict(sorted(counts.items())),examples=examples,
                verification_sha256=digest.hexdigest(),
                scope='Finite exact tests of both directions max/min<2 iff mechanical rotation, with proper powers and fixed points counted separately. Coprime totals and gcd(C,D)=1 are checked on nontrivial primitive narrow words. No universal inference without the written classification proof; all positive raw arrows are exercised.')


def mechanical_gap_checks():
    counts = Counter()
    rows = []
    digest = sha256()
    for m in MECHANICAL_LENGTHS:
        A = (3**m).bit_length()
        require(2**(A-1) < 3**m < 2**A,'exact upper binary approximant failed')
        if gcd(A,m) != 1:
            counts['noncoprime_totals_skipped'] += 1
            continue
        word = mechanical_word(A,m)
        C,D,_ = direct(word)
        Cs = [direct(word[i:]+word[:i])[0] for i in range(m)]
        g = gcd(C,D)
        require(g == 1,'primitive mechanical coefficient gcd is not1')
        require(D > 0 and len(set(Cs)) == m,'mechanical cycle is not positive and primitive')
        require(all(gcd(c,D) == g for c in Cs),'mechanical common denominator failed')
        require(all(2*c > m*3**(m-1) for c in Cs),'mechanical point lower bound failed')
        ordered = sorted(Cs)
        differences = [b-a for a,b in zip(ordered,ordered[1:])]
        require(all(2*delta > 3**(m-1) for delta in differences),
                'mechanical adjacent pair gap lower bound failed')
        den = D//g
        for i,c in enumerate(Cs):
            require(raw_step(c//g,den) == (Cs[(i+1)%m]//g,word[i]),
                    'mechanical raw arrow or exact valuation failed')
            counts['raw_arrows'] += 1
        counts['cases'] += 1
        counts['point_lower_bounds'] += m
        counts['adjacent_gap_lower_bounds'] += m-1
        row = dict(m=m,A=A,D=D,common_gcd=g,reduced_denominator=den,
                   minimum=rational(ordered[0],D),maximum=rational(ordered[-1],D),
                   minimum_pair_gap=rational(min(differences),D),
                   point_lower_bound=rational(m*3**(m-1),2*D),
                   gap_lower_bound=rational(3**(m-1),2*D))
        if m == 306:
            require(3**305 > 200*D,'m306 gap lower bound is not above100')
            row['gap_lower_bound_exceeds100'] = True
            row['gap_over100_integer_comparison'] = dict(left=3**305,right=200*D)
        rows.append(row)
        stream_add(digest,[word,Cs,row])
    return dict(domain=dict(m=list(MECHANICAL_LENGTHS),A='bit_length(3^m)',
                            eligibility='gcd(A,m)=1'),counts=dict(sorted(counts.items())),
                cases=rows,verification_sha256=digest.hexdigest(),
                scope='Finite exact upper mechanical approximants. Point and sorted-neighbor gap bounds are checked by integer products. The existence of arbitrarily close upper approximants and unbounded gaps requires the separate written proof.')


def residues(values,den):
    result = {}
    for modulus in MODULI:
        require(gcd(den,modulus) == 1,'noninvertible denominator in declared residue domain')
        inverse = pow(den,-1,modulus)
        nums = Counter(n % modulus for n in values)
        rats = Counter(n*inverse % modulus for n in values)
        result[str(modulus)] = dict(
            primitive_numerator_counts={str(k):v for k,v in sorted(nums.items())},
            rational_state_counts={str(k):v for k,v in sorted(rats.items())})
    return result


def determinant(matrix):
    """Small independent Leibniz determinant; no floating or symbolic runtime."""
    n = len(matrix)
    require(n > 0 and all(len(row) == n for row in matrix),'nonsquare determinant input')
    total = 0
    for perm in permutations(range(n)):
        value = 1
        for i,j in enumerate(perm):
            value *= matrix[i][j]
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n))
        total += (-1 if inversions % 2 else 1)*value
    return total


def minor(matrix,rows,cols):
    return [[matrix[i][j] for j in cols] for i in rows]


def compact_cycle(row):
    """Keep exact witnesses while the full metric/residue rows enter a digest."""
    result = {k:v for k,v in row.items() if k not in ('residue_histograms','source_instances')}
    result['source_instance_count'] = len(row['source_instances'])
    result['first_source_instance'] = row['source_instances'][0]
    return result


def matrix_checks():
    counts = Counter()
    digest = sha256()
    examples = []
    for m in range(1,MATRIX_MAX_LENGTH+1):
        for word in product(range(1,MATRIX_MAX_VALUATION+1),repeat=m):
            C,D,A = direct(word)
            Cs = [direct(word[i:]+word[:i])[0] for i in range(m)]
            g = gcd(C,D)
            B = [[0]*m for _ in range(m)]
            for i,a in enumerate(word):
                B[i][i] -= 3
                B[i][(i+1)%m] += 2**a
            require(abs(determinant(B)) == abs(D),'cycle matrix determinant failed')
            divisors = []
            for size in range(1,m+1):
                divisor = 0
                for rows in combinations(range(m),size):
                    for cols in combinations(range(m),size):
                        divisor = gcd(divisor,determinant(minor(B,rows,cols)))
                        counts['square_minors'] += 1
                require(divisor == (1 if size < m else abs(D)),
                        'cycle matrix Smith determinantal divisor failed')
                divisors.append(divisor)
            augmented = [row+[-1] for row in B]
            maximal_gcd = 0
            maximal_minors = []
            for removed in range(m+1):
                cols = [j for j in range(m+1) if j != removed]
                value = determinant(minor(augmented,range(m),cols))
                require(abs(value) == (abs(D) if removed == m else Cs[removed]),
                        'augmented maximal minor coefficient failed')
                maximal_minors.append(value)
                maximal_gcd = gcd(maximal_gcd,value)
                counts['augmented_maximal_minors'] += 1
            require(maximal_gcd == g,'augmented maximal-minor gcd failed')
            vector = [c//g for c in Cs]+[D//g]
            require(all(sum(row[j]*vector[j] for j in range(m+1)) == 0 for row in augmented),
                    'augmented integer kernel equation failed')
            vg = 0
            for n in vector:
                vg = gcd(vg,n)
            require(vg == 1,'augmented kernel vector not primitive')
            counts['matrices'] += 1
            if D > 0:
                n,den = vector[0],vector[-1]
                for a in word:
                    n,actual = raw_step(n,den)
                    require(actual == a,'small positive matrix cycle valuation failed')
                    counts['positive_raw_arrows'] += 1
                require(n == vector[0],'small positive matrix cycle did not close')
                counts['positive_matrices'] += 1
            else:
                counts['negative_D_matrices'] += 1
            row = dict(word=list(word),D=D,Cs=Cs,smith_determinantal_divisors=divisors,
                       augmented_maximal_minors=maximal_minors,augmented_gcd=g,
                       primitive_integer_kernel=vector)
            stream_add(digest,row)
            if word in ((2,),(1,3),(1,1,3),(1,2,2),(4,),(1,1,1,1)):
                examples.append(row)
    return dict(domain=dict(lengths=[1,MATRIX_MAX_LENGTH],valuations=[1,MATRIX_MAX_VALUATION]),
                counts=dict(sorted(counts.items())),verification_sha256=digest.hexdigest(),
                examples=examples,
                scope='Exact finite determinant/minor evidence for the separate written Smith-form theorem. Negative D cases test integer matrix algebra only; positive cases also exercise every raw arrow.')


def report():
    source = json.loads(ACTUAL.read_text())
    fixtures = json.loads(FIXTURES.read_text())['cycles']
    require(source['schema'] == 'C001-actual-raw-cycles-v1','wrong source schema')
    require(source['sources']['scanner_sha256'] == sha256(SCANNER.read_bytes()).hexdigest(),
            'source scanner hash mismatch')
    require(source['sources']['fixture_sha256'] == sha256(FIXTURES.read_bytes()).hexdigest(),
            'source fixture hash mismatch')
    cycles = source['cycles']
    require(len(cycles) == 2459 and len({c['d'] for c in cycles}) == 333,
            'source cycle domain changed')
    fixture_index = {(f['d'],tuple(f['states'])):i+1 for i,f in enumerate(fixtures)}
    require(len(fixture_index) == len(fixtures) == 11,'fixture domain mismatch')
    seen_fixtures = set()
    fixture_keys = {}
    unique = {}
    counts = Counter()
    rotation_digest = sha256()
    for cycle in cycles:
        actual_d,states,word = cycle['d'],cycle['states'],tuple(cycle['word'])
        primitive,den = cycle['primitive_states'],cycle['reduced_denominator']
        m = len(word)
        require(len(states) == len(primitive) == m and len(set(states)) == m,
                'source cycle must have distinct states')
        require(states[0] == min(states) and primitive[0] == min(primitive),
                'source cycle must use minimum orientation')
        require(actual_d % den == 0 and cycle['actual_scaling'] == actual_d//den,
                'incorrect actual/normalized scaling')
        scale = actual_d//den
        require(states == [scale*n for n in primitive], 'primitive states do not rescale to source')
        primitive_gcd = den
        for n in primitive:
            primitive_gcd = gcd(primitive_gcd,n)
        require(primitive_gcd == 1,'normalized state/parameter kernel vector is not primitive')
        counts['primitive_kernel_vector_gcd_checks'] += 1
        for i,n in enumerate(states):
            require(raw_step(n,actual_d) == (states[(i+1)%m],word[i]),'actual raw arrow failed')
            require(raw_step(primitive[i],den) == (primitive[(i+1)%m],word[i]),
                    'primitive raw arrow failed')
            require(gcd(primitive[i],den) == 1,'primitive state is not reduced')
            counts['source_raw_arrows'] += 1
            counts['normalized_raw_arrows'] += 1
        C,D,A = direct(word)
        g = gcd(C,D)
        require(D > 0 and den == D//g and primitive[0] == C//g,
                'normalized source fixed-point equation failed')
        require((cycle['C'],cycle['D'],cycle['A'],cycle['m'],cycle['gcd_C_D'])
                == (C,D,A,m,g),'source coefficient metadata mismatch')
        Cs = []
        for i in range(m):
            c,dr,ar = direct(word[i:]+word[:i])
            require((dr,ar) == (D,A),'rotated total changed')
            require(c == g*primitive[i] and gcd(c,D) == g,'rotated gcd or state formula failed')
            Cs.append(c)
            counts['direct_rotation_checks'] += 1
        all_gcd,coefficient_gcd = D,0
        for i,c in enumerate(Cs):
            require(2**word[i]*Cs[(i+1)%m] == 3*c+D,'adjacent rotation identity failed')
            all_gcd = gcd(all_gcd,c)
            coefficient_gcd = gcd(coefficient_gcd,c)
            stream_add(rotation_digest,[actual_d,states[0],i,word[i],c,D,g])
            counts['adjacent_rotation_checks'] += 1
            if m > 1:
                rotated = word[i:]+word[:i]
                cv,dv,_ = direct(rotated[1:])
                K = (2**word[i]-3)*cv-dv
                require(2**word[i]*K == (2**word[i]-3)*c-D,
                        'one-letter cut elimination failed')
                require(K % g == 0,'common gcd missing from one-letter commutator')
                require(gcd(D,K) == g*gcd(den,2**word[i]-3),
                        'general one-letter cut exact gcd formula failed')
                counts['one_letter_cut_checks'] += 1
                counts['general_one_letter_cut_exact_gcd_checks'] += 1
                if word[i] in (1,2):
                    require(gcd(D,K) == g,'unit one-letter cut exact gcd failed')
                    counts['unit_one_letter_cut_exact_gcd_checks'] += 1
        require(all_gcd == g,'all-rotation common gcd failed')
        require(coefficient_gcd == g,'rotation coefficients alone have the wrong gcd')
        counts['all_rotation_gcd_checks'] += 1
        counts['rotation_coefficients_gcd_checks'] += 1
        counts['source_cycles'] += 1
        counts['source_fixed_cycles' if m == 1 else 'source_nontrivial_cycles'] += 1
        spread_small = max(primitive) < 2*min(primitive)
        mechanical_offset = mechanical_rotation(word)
        require(spread_small == (mechanical_offset is not None),
                'actual spread/mechanical equivalence counterexample')
        counts['source_spread_equivalence_checks'] += 1
        if m > 1 and spread_small:
            require(gcd(A,m) == 1,'actual primitive mechanical totals not coprime')
            require(g == 1,'actual narrow cycle has nontrivial coefficient cancellation')
            counts['source_nontrivial_spread_mechanical_checks'] += 1
        ordered = sorted(primitive)
        min_gap = None
        pair = None
        if m > 1:
            min_gap,pair = min((b-a,(a,b)) for a,b in zip(ordered,ordered[1:]))
            require(min_gap > 0 and min_gap % 2 == 0 and min_gap >= 2,
                    'odd integer lattice gap failed')
            require(Fraction(den) >= Fraction(2*den,min_gap),'den>=2/min-gap failed')
            counts['odd_lattice_gap_checks'] += 1
            counts['source_gap_at_least2'] += int(min_gap >= 2*den)
            counts['source_gap_equal2'] += int(min_gap == 2*den)
        key = (den,tuple(primitive))
        source_ref = dict(actual_d=actual_d,actual_minimum=states[0],scaling=scale)
        if key in unique:
            unique[key]['source_instances'].append(source_ref)
        else:
            unique[key] = dict(
                denominator=den,primitive_states=primitive,word=list(word),m=m,A=A,C=C,D=D,
                common_rotation_gcd=g,all_rotations_and_D_gcd=all_gcd,
                rotation_coefficients_gcd=coefficient_gcd,
                minimum=rational(ordered[0],den),maximum=rational(ordered[-1],den),
                range=rational(ordered[-1]-ordered[0],den),sum=rational(sum(primitive),den),
                minimum_pair_gap=None if min_gap is None else rational(min_gap,den),
                nearest_pair=None if pair is None else dict(primitive_numerators=list(pair),
                    normalized_states=[rational(n,den) for n in pair]),
                gap_less_than2=None if min_gap is None else min_gap < 2*den,
                lattice_denominator_lower_bound=None if min_gap is None else rational(2*den,min_gap),
                residue_histograms=residues(primitive,den),source_instances=[source_ref])
            unique[key]['maximum_minimum_ratio'] = rational(ordered[-1],ordered[0])
            unique[key]['spread_less_than2'] = spread_small
            unique[key]['mechanical_rotation_offset'] = mechanical_offset
        fixture_key = (actual_d,tuple(states))
        if fixture_key in fixture_index:
            i = fixture_index[fixture_key]
            require(tuple(fixtures[i-1]['valuations']) == word,'fixture word mismatch')
            seen_fixtures.add(i)
            fixture_keys[i] = key
    require(seen_fixtures == set(range(1,12)),'not all exact fixture cycles were exercised')
    require(counts['source_raw_arrows'] == counts['direct_rotation_checks'] == 36912,
            'rotation coverage changed')
    rows = sorted(unique.values(),key=lambda r:(r['denominator'],r['primitive_states'][0],r['m']))
    nontrivial = [r for r in rows if r['m'] > 1]
    failures = [r for r in nontrivial if not r['gap_less_than2']]
    counts['distinct_normalized_cycles'] = len(rows)
    counts['distinct_normalized_fixed_cycles'] = len(rows)-len(nontrivial)
    counts['distinct_normalized_nontrivial_cycles'] = len(nontrivial)
    counts['distinct_gap_at_least2'] = len(failures)
    counts['distinct_nontrivial_spread_mechanical_checks'] = sum(r['spread_less_than2'] for r in nontrivial)
    require((len(rows),len(nontrivial),len(failures)) == (1184,1176,28),
            'independent normalized census changed')
    first = failures[0]
    require(first['denominator'] == 5 and first['primitive_states'] == [19,31,49]
            and first['minimum_pair_gap'] == rational(12,5),'named gap counterexample missing')
    largest = max(nontrivial,key=lambda r:Fraction(**{
        'numerator':r['minimum_pair_gap']['numerator'],
        'denominator':r['minimum_pair_gap']['denominator']}))
    metric_digest = sha256()
    for row in rows:
        stream_add(metric_digest,row)
    narrow_rows = [r for r in rows if r['spread_less_than2']]
    return dict(
        schema='C004-rotation-geometry-v1',baseline_commit=BASELINE,
        status='exact finite audit; minimum-pair-gap<2 proposal refuted',
        clock='raw positive odd-only recurrence; state1 is not absorbing',
        normalization='actual states/actual d = primitive_states/reduced_denominator; scaled source instances and rotations are not additional normalized primitive cycles',
        scope='Every stored actual raw cycle, all its rotations, exact normalized fractions and declared residue moduli. Fixed points have no pair-gap statistic. No all-cycle size bound or asymptotic theorem is inferred.',
        source_sha256={
            'check_rotations.py':sha256(Path(__file__).read_bytes()).hexdigest(),
            'C001/actual_cycles.json':sha256(ACTUAL.read_bytes()).hexdigest(),
            'C001/scan_cycles.py':sha256(SCANNER.read_bytes()).hexdigest(),
            'phase6/cycle_fixtures.json':sha256(FIXTURES.read_bytes()).hexdigest()},
        counts=dict(sorted(counts.items())),residue_moduli=list(MODULI),
        fixture_ids_checked=sorted(seen_fixtures),rotation_sha256=rotation_digest.hexdigest(),
        full_normalized_metrics_and_residues_sha256=metric_digest.hexdigest(),
        full_metrics_scope='All1184 normalized cycle metric rows, all original scaled-source associations and all declared residue histograms are recomputed and hashed; selected exact witnesses are stored below.',
        counterexamples=[compact_cycle(r) for r in failures],
        narrow_classification_cycles=[compact_cycle(r) for r in narrow_rows],
        fixture_controls=[dict(fixture_id=i,**compact_cycle(unique[fixture_keys[i]]))
                          for i in sorted(seen_fixtures)],
        largest_observed_minimum_gap=dict(denominator=largest['denominator'],
            minimum=largest['minimum'],m=largest['m'],gap=largest['minimum_pair_gap']),
        small_generated_matrices=matrix_checks(),
        short_word_spread=short_spread_checks(),mechanical_gap_family=mechanical_gap_checks())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--receipt',type=Path,default=HERE/'rotation_audit.json')
    args = parser.parse_args()
    try:
        result = json.loads(json.dumps(report()))
        if args.write:
            args.receipt.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
        else:
            require(result == json.loads(args.receipt.read_text()),'saved receipt mismatch')
    except (OSError,ValueError,KeyError,TypeError,ZeroDivisionError) as error:
        print(f'FAIL: {error}',file=sys.stderr)
        return 1
    print(json.dumps(dict(status='PASS',counts=result['counts'],
                         largest_gap=result['largest_observed_minimum_gap']),sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
