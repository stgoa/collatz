#!/usr/bin/env python3
"""Exact C006 tests of weighted order, height profiles and lattice bounds.

The arithmetic packing bound is checked on all cycles, without an order
hypothesis. Ordered-cycle diagnostics and speculative height bounds have
separate scopes. A finite successful test never promotes a candidate to a
universal theorem; explicit failed strengthenings are saved as controls.
"""

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
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
PROFILE_MAX_HEIGHT = 6


def require(test, message):
    if not test:
        raise ValueError(message)


def ceil_div(a, b):
    require(a >= 0 and b > 0, 'invalid positive ceiling division')
    return (a+b-1)//b


def rational(x):
    x = Fraction(x)
    return dict(numerator=x.numerator, denominator=x.denominator)


def stream_add(hasher, value):
    hasher.update(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()+b'\n')


def oddpart(n):
    require(type(n) is int and n > 0, 'oddpart needs a positive integer')
    return n//(n & -n)


def raw_step(n, q):
    require(type(n) is int and n > 0 and n % 2 == 1 and
            type(q) is int and q > 0 and gcd(q, 6) == 1, 'invalid positive raw odd input')
    value = 3*n+q
    a = (value & -value).bit_length()-1
    return value >> a, a


def direct(word):
    require(word and all(type(a) is int and a >= 1 for a in word), 'invalid positive valuation word')
    C, A = 0, 0
    for a in word:
        C = 3*C+2**A
        A += a
    return C, 2**A-3**len(word), A


def base_data(A, m):
    require(A >= m >= 1 and 2**A > 3**m, 'invalid positive base totals')
    c = tuple((j+1)*A//m-j*A//m for j in range(m))
    Cc, D, unused = direct(c)
    coefficients, current = [], Cc
    prefix, monomials = 0, []
    for j, a in enumerate(c):
        coefficients.append(current)
        monomials.append(3**(m-1-j)*2**prefix)
        require((3*current+D) % 2**a == 0, 'mechanical coefficient recurrence not integral')
        current = (3*current+D)//2**a
        prefix += a
    require(current == Cc and sum(monomials) == Cc and min(coefficients) == Cc,
            'mechanical reference coefficient failed')
    return dict(A=A, m=m, c=c, Cc=Cc, D=D, coefficients=coefficients, monomials=monomials)


def realize(word):
    C, D, A = direct(word)
    require(D > 0, 'word does not have a positive cycle')
    g = gcd(C, D)
    q, current = D//g, C//g
    states = []
    for a in word:
        states.append(current)
        current, actual_a = raw_step(current, q)
        require(actual_a == a, 'word realization has the wrong exact valuation')
    require(current == states[0], 'word realization does not close')
    return states, q, C, g, A


def universal_metrics(n, q, word, base, g):
    """Packing and extremal-rotation bounds: no normalized-order premise."""
    m, A, D, Cc = len(word), base['A'], base['D'], base['Cc']
    require(len(n) == m and len(set(n)) == m and all(x > 0 and x % 2 for x in n),
            'universal audit needs a simple positive odd cycle')
    require(q == D//g and all(gcd(x, q) == 1 for x in n), 'incorrect reduced denominator')
    prefix, scores = 0, []
    for j, a in enumerate(word):
        scores.append(m*prefix-j*A)
        prefix += a
    require(prefix == A, 'word total changed')
    start = max(range(m), key=lambda j: scores[j])
    rotated = word[start:]+word[:start]
    total = 0
    for j in range(m+1):
        require(total <= j*A//m, 'maximal-deviation rotation violates prefix majorization')
        if j < m:
            total += rotated[j]
    Crot, rotated_D, unused = direct(rotated)
    require(rotated_D == D and Crot == g*n[start], 'rotated coefficient/state identity failed')
    mechanical = tuple(rotated) == base['c']
    require((Crot == Cc) == mechanical, 'strict prefix majorization criterion failed')
    L, H = min(n), max(n)
    require(g*L <= Crot <= Cc, 'universal mechanical-minimum bound failed')
    heights = [(x//L).bit_length()-1 for x in n]
    B, histogram = max(heights), Counter(heights)
    require(all(2**h*L <= x < 2**(h+1)*L for x, h in zip(n, heights)),
            'actual height interval failed')
    require(histogram[0] <= (L+1)//2, 'height0 odd-lattice capacity failed')
    for h, count in histogram.items():
        if h:
            require(count <= 2**(h-1)*L, 'positive-height odd-lattice capacity failed')
    aggregate = ceil_div(2*m-1, 2**(B+1)-1)
    P = max([2*histogram[0]-1]+[ceil_div(count, 2**(h-1))
                              for h, count in histogram.items() if h])
    P_odd = P if P % 2 else P+1
    require(L >= P_odd >= P >= aggregate, 'packing lower-bound comparison failed')
    lower_aggregate = ceil_div(aggregate*D, Cc)
    lower_P = ceil_div(P*D, Cc)
    lower_odd = ceil_div(P_odd*D, Cc)
    require(q >= lower_odd >= lower_P >= lower_aggregate,
            'universal packing/Green denominator bound failed')
    return dict(m=m, A=A, denominator=q, C_mechanical=Cc, D=D, numerator_gcd=g,
        minimum_numerator=L, maximum_numerator=H, maximum_height=B,
        heights=heights, height_histogram={str(h): count for h, count in sorted(histogram.items())},
        maximal_deviation_rotation=start, rotated_coefficient=Crot,
        mechanical_original_word=mechanical, wide=H >= 2*L,
        aggregate_minimum_bound=aggregate, P=P, P_odd=P_odd,
        denominator_lower_aggregate=lower_aggregate, denominator_lower_P=lower_P,
        denominator_lower_P_odd=lower_odd)


def count_universal(counts, row):
    counts['cycles'] += 1
    counts['nontrivial_cycles'] += int(row['m'] > 1)
    counts['prefix_majorization_checks'] += row['m']+1
    counts['mechanical_cycles'] += int(row['mechanical_original_word'])
    counts['wide_cycles'] += int(row['wide'])
    for suffix in ('aggregate', 'P', 'P_odd'):
        bound = row['denominator_lower_'+suffix]
        counts[suffix+'_bound_greater_than1'] += int(bound > 1)
        counts[suffix+'_nonmechanical_bound_greater_than1'] += int(bound > 1 and not row['mechanical_original_word'])
        counts[suffix+'_nontrivial_bound_greater_than1'] += int(bound > 1 and row['m'] > 1)


def normalized_order(n, q, heights):
    m, B = len(n), max(heights)
    Z = [x << (B-h) for x, h in zip(n, heights)]
    F = [(3*x+q) << (B-h) for x, h in zip(n, heights)]
    require(len(set(Z)) == m, 'distinct odd numerators have equal mantissas')
    order = sorted(range(m), key=lambda i: Z[i])
    rank = {i: j for j, i in enumerate(order)}
    successor = [rank[(i+1) % m] for i in order]
    monotone = all(F[order[j]] < F[order[j+1]] for j in range(m-1))
    is_rotation = len({(successor[j]-j) % m for j in range(m)}) == 1
    if min(n) >= q:
        require(monotone == is_rotation, 'q<=L order/rank equivalence failed')
    return Z, F, order, successor, monotone, is_rotation


def weighted_checks(n, q, proposed_heights, word, base, g):
    """Exact algebra valid even before the proposed heights are geometric."""
    m, Cc = len(n), base['Cc']
    c = tuple(word[i]+proposed_heights[(i+1) % m]-proposed_heights[i] for i in range(m))
    require(c == base['c'], 'weighted normalized word not the declared lower mechanical word')
    prefix, weighted = 0, 0
    for j, (a, h) in enumerate(zip(c, proposed_heights)):
        require(prefix >= h and base['monomials'][j] % 2**h == 0,
                'weighted mechanical monomial is not integral')
        weighted += base['monomials'][j]//2**h
        prefix += a
    require(weighted == g*n[0], 'weighted intercept differs from the original intercept')
    wide_label = max(proposed_heights) > 0
    for x, h, Cref in zip(n, proposed_heights, base['coefficients']):
        gap = 2**h*Cref-g*x
        require(gap >= 0 and (gap > 0) == wide_label, 'positive Green comparison failed')
    deficit = Cc-weighted
    positive_heights = sum(h > 0 for h in proposed_heights)
    require(2*deficit >= positive_heights*min(base['monomials']),
            'positive-height monomial loss bound failed')
    return weighted, deficit, positive_heights


def gap_recurrence(n, q, heights, Z, order, successor):
    m, B = len(n), max(heights)
    sorted_Z = [Z[i] for i in order]
    eps = [2**(B-heights[i]) for i in order]+[2**(B+1)]
    gaps = [sorted_Z[j+1]-sorted_Z[j] for j in range(m-1)]+[2*sorted_Z[0]-sorted_Z[-1]]
    shift = successor[0]
    require(gcd(shift, m) == 1 and shift != 0, 'ordered nontrivial rank shift not primitive')
    for j in range(m):
        target = j+shift
        factor = 2 if target < m else 4
        require(factor*gaps[target % m] == 3*gaps[j]+q*(eps[j+1]-eps[j]),
                'dyadic circular-gap recurrence failed')
    require(sum(gaps) == 2**B*min(n), 'dyadic circular gaps do not sum to L')
    return gaps, eps, shift


def zero_run_metrics(gaps, eps, shift, B, L, q, base):
    """Retain the dyadic wrap defect and follow zero runs along rank shift."""
    m = len(gaps)
    defects = [eps[j+1]-eps[j] for j in range(m)]
    nonzero = [j for j, value in enumerate(defects) if value]
    J = len(nonzero)
    require(J >= 1 and sum(defects) == 2**B, 'missing dyadic wrap defect')
    # With c in {1,2} and a>=1, chronological height rises by at most1.
    # Hence every height0..B occurs; sorting retains B changes plus wrap.
    require(J >= B+1, 'height coverage requires at least B+1 circular defects')
    require(gcd(shift, m) == 1, 'zero-run permutation is not a single cycle')
    require(shift == base['A']-m, 'ordered rank shift differs from A-m')
    runs = []
    for previous in nonzero:
        start = (previous+shift) % m
        current, length, exponent = start, 0, 0
        while defects[current] == 0:
            exponent += 1+int(current+shift >= m)
            length += 1
            require(length < m, 'zero-defect run did not terminate')
            current = (current+shift) % m
        require(gaps[start] % 2**exponent == 0, 'zero-run dyadic divisibility failed')
        require(L*2**B > 2**exponent, 'strict positive-gap packing bound failed')
        runs.append(dict(start=start, length=length, valuation_sum=exponent,
                         terminal_defect=current, starting_integer_gap=gaps[start]))
    require(sum(run['length'] for run in runs) == m-J, 'zero runs do not partition zero defects')
    longest = max(runs, key=lambda run: (run['length'], run['valuation_sum'], -run['start']))
    strongest = max(runs, key=lambda run: (run['valuation_sum'], run['length'], -run['start']))
    length_bound = ceil_div(m, J)-1
    require(longest['length'] >= length_bound and longest['valuation_sum'] >= longest['length'],
            'longest zero-run lower bound failed')
    D, Cc = base['D'], base['Cc']
    exact_numerator = D*2**strongest['valuation_sum']
    uniform_numerator = D*2**length_bound
    denominator = Cc*2**B
    require(q*denominator > exact_numerator >= uniform_numerator,
            'strict zero-run denominator inequality failed')
    exact_bound = exact_numerator//denominator+1
    uniform_bound = uniform_numerator//denominator+1
    require(q >= exact_bound >= uniform_bound, 'integer zero-run denominator bound failed')
    return dict(nonzero_defects=J, integer_defects=defects, runs=runs,
        longest_run=longest, strongest_run=strongest, pigeonhole_length_lower_bound=length_bound,
        strict_denominator_threshold=rational(Fraction(exact_numerator, denominator)),
        strict_uniform_threshold=rational(Fraction(uniform_numerator, denominator)),
        denominator_lower_exact_run=exact_bound, denominator_lower_uniform_run=uniform_bound)


def ordered_metrics(n, q, word, base, universal):
    heights, m, B = universal['heights'], len(n), universal['maximum_height']
    require(m > 1 and min(n) >= q, 'ordered metric domain failed')
    Z, F, order, successor, monotone, rotation = normalized_order(n, q, heights)
    require(monotone and rotation, 'ordered metrics called on an unordered cycle')
    weighted, deficit, K = weighted_checks(n, q, heights, word, base, universal['numerator_gcd'])
    gaps, eps, shift = gap_recurrence(n, q, heights, Z, order, successor)
    zero_runs = zero_run_metrics(gaps, eps, shift, B, min(n), q, base)
    minima = {name: None for name in ('all_pairs_oddpart', 'all_pairs_gap_over_pair_gcd',
                                     'adjacent_oddpart', 'circular_oddpart')}
    witnesses = {}
    pair_digest, pair_count = sha256(), 0
    for position, i in enumerate(order):
        for j in order[position+1:]:
            delta = Z[j]-Z[i]
            values = {'all_pairs_oddpart': oddpart(delta),
                      'all_pairs_gap_over_pair_gcd': delta//gcd(Z[i], Z[j])}
            for name, value in values.items():
                if minima[name] is None or value < minima[name]:
                    minima[name], witnesses[name] = value, [i, j]
            stream_add(pair_digest, [i, j, delta, values])
            pair_count += 1
    for j, delta in enumerate(gaps):
        names = ['circular_oddpart']+(['adjacent_oddpart'] if j < m-1 else [])
        for name in names:
            value = oddpart(delta)
            if minima[name] is None or value < minima[name]:
                minima[name], witnesses[name] = value, [order[j], order[(j+1) % m]]
    sorted_base = sorted(base['coefficients'])
    base_gap = min(b-a for a, b in zip(sorted_base, sorted_base[1:]))
    return dict(primitive_states=list(n), word=list(word), universal=universal,
        normalized_word=list(base['c']), sorted_indices=order, sorted_heights=[heights[i] for i in order],
        mantissas=[rational(Fraction(z, 2**B)) for z in Z],
        scaled_images=[rational(Fraction(f, 2**B)) for f in F],
        successor_ranks=successor, rank_shift=shift, weighted_intercept=weighted,
        unweighted_intercept=base['Cc'], intercept_deficit=deficit,
        normalized_minimum_loss=rational(Fraction(deficit, base['D'])),
        normalized_reference_minimum=rational(Fraction(base['Cc'], base['D'])),
        smallest_reference_neighbor_gap=rational(Fraction(base_gap, base['D'])),
        positive_height_count=K, height_weight_sum=rational(sum(Fraction(1, 2**h) for h in heights)),
        circular_gaps=[rational(Fraction(delta, 2**B)) for delta in gaps],
        extended_epsilon=[rational(Fraction(value, 2**B)) for value in eps],
        gap_minima=minima, gap_minimum_pairs=witnesses,
        all_pairs_sha256=pair_digest.hexdigest(), pair_count=pair_count,
        zero_defect_runs=zero_runs,
        candidate_height_bound_holds=B <= q-1,
        candidate_height_ratio=rational(Fraction(B, q-1)) if q > 1 else None,
        scope='Gap oddpart removes only powers of2 from the positive difference. Gap/pair-gcd instead divides by the rational gcd of the two mantissas. The circular statistic includes the final gap to2L. These conventions are distinct.')


def height_profiles(c, B):
    h = [0]
    def visit():
        if len(h) == len(c):
            yield tuple(h)
            return
        for next_height in range(min(B, h[-1]+c[len(h)-1]-1)+1):
            h.append(next_height)
            yield from visit()
            h.pop()
    yield from visit()


def profile_domain():
    specs = []
    for m in range(2, 12):
        for A in range((3**m).bit_length(), 2*m):
            if gcd(A, m) == 1:
                specs.append((A, m))
    specs += [((3**m).bit_length(), m) for m in (13, 17)]
    return specs


def profile_grid():
    counts, universal_counts, digest = Counter(), Counter(), sha256()
    examples, minima_by_height = {}, {}
    largest_bound, largest_wide_bound, largest_height_ratio = None, None, None
    largest_zero_bound, largest_wide_zero_bound = None, None
    candidate_failures = []
    for A, m in profile_domain():
        base = base_data(A, m)
        require(gcd(A, m) == 1, 'profile totals must be coprime')
        counts['base_totals'] += 1
        for h in height_profiles(base['c'], PROFILE_MAX_HEIGHT):
            word = tuple(base['c'][i]+h[i]-h[(i+1) % m] for i in range(m))
            n, q, C, g, unused = realize(word)
            require(len(set(n)) == m, 'coprime profile totals did not produce a primitive cycle')
            universal = universal_metrics(n, q, word, base, g)
            count_universal(universal_counts, universal)
            weighted_checks(n, q, h, word, base, g)
            counts['profiles'] += 1
            counts['raw_arrows'] += m
            counts['weighted_green_checks'] += m
            counts['numerator_cancellation'] += int(g > 1)
            counts['denominator1_profiles'] += int(q == 1)
            if n[0] != min(n):
                classification = 'minimum_phase_failure'
            elif tuple(universal['heights']) != h:
                classification = 'height_consistency_failure'
            else:
                counts['geometrically_consistent_profiles'] += 1
                require(n[0] > q, 'consistent canonical profile should have L>q')
                Z, F, order, successor, monotone, rotation = normalized_order(n, q, h)
                if not monotone:
                    classification = 'order_failure'
                else:
                    classification = 'ordered'
                    gaps, eps, shift = gap_recurrence(n, q, h, Z, order, successor)
                    counts['ordered_gap_recurrence_checks'] += m
                    B = max(h)
                    zero_runs = zero_run_metrics(gaps, eps, shift, B, min(n), q, base)
                    zero_bound = zero_runs['denominator_lower_exact_run']
                    histogram_bound = universal['denominator_lower_P_odd']
                    counts['zero_run_divisibility_checks'] += zero_runs['nonzero_defects']
                    counts['zero_run_edges'] += m-zero_runs['nonzero_defects']
                    counts['zero_run_bound_greater_than1'] += int(zero_bound > 1)
                    counts['wide_zero_run_bound_greater_than1'] += int(B > 0 and zero_bound > 1)
                    counts['uniform_zero_run_bound_greater_than1'] += int(zero_runs['denominator_lower_uniform_run'] > 1)
                    counts['zero_run_bound_stronger_than_histogram'] += int(zero_bound > histogram_bound)
                    counts['histogram_bound_stronger_than_zero_run'] += int(histogram_bound > zero_bound)
                    counts['wide_ordered_profiles'] += int(B > 0)
                    counts['ordered_bound_greater_than1'] += int(universal['denominator_lower_P_odd'] > 1)
                    counts['wide_ordered_bound_greater_than1'] += int(B > 0 and universal['denominator_lower_P_odd'] > 1)
                    if B > q-1:
                        candidate_failures.append(dict(A=A, m=m, q=q, h=list(h), word=list(word), states=n))
                    ref = dict(A=A, m=m, q=q, h=list(h), word=list(word), states=n, universal=universal)
                    if largest_zero_bound is None or zero_bound > largest_zero_bound['zero_defect_runs']['denominator_lower_exact_run']:
                        largest_zero_bound = dict(**ref, zero_defect_runs=zero_runs)
                    if B > 0 and (largest_wide_zero_bound is None or zero_bound > largest_wide_zero_bound['zero_defect_runs']['denominator_lower_exact_run']):
                        largest_wide_zero_bound = dict(**ref, zero_defect_runs=zero_runs)
                    if B > 0 and zero_bound > histogram_bound and 'zero_run_stronger_than_histogram' not in examples:
                        examples['zero_run_stronger_than_histogram'] = dict(**ref, zero_defect_runs=zero_runs)
                    if B not in minima_by_height or q < minima_by_height[B]['q']:
                        minima_by_height[B] = ref
                    if largest_height_ratio is None or B*(largest_height_ratio['q']-1) > max(largest_height_ratio['h'])*(q-1):
                        largest_height_ratio = ref
            counts[classification] += 1
            if classification != 'ordered' and classification not in examples:
                examples[classification] = dict(A=A, m=m, c=list(base['c']), proposed_heights=list(h),
                    word=list(word), states=n, C=C, D=base['D'], q=q, g=g, universal=universal)
            reference = dict(A=A, m=m, q=q, h=list(h), word=list(word), states=n,
                             classification=classification, universal=universal)
            if largest_bound is None or universal['denominator_lower_P_odd'] > largest_bound['universal']['denominator_lower_P_odd']:
                largest_bound = reference
            if universal['wide'] and (largest_wide_bound is None or universal['denominator_lower_P_odd'] > largest_wide_bound['universal']['denominator_lower_P_odd']):
                largest_wide_bound = reference
            stream_add(digest, [A, m, h, word, n, C, g, q, classification, universal])
            if classification == 'ordered':
                stream_add(digest, ['zero_runs', zero_runs])
    require(counts['profiles'] == 360618, 'profile domain count changed')
    require((counts['minimum_phase_failure'], counts['height_consistency_failure'],
             counts['order_failure'], counts['ordered']) == (11532, 27044, 4583, 317459),
            'profile consistency partition changed')
    require(counts['profiles'] == sum(counts[k] for k in
            ('minimum_phase_failure', 'height_consistency_failure', 'order_failure', 'ordered')),
            'profile classification is not exhaustive')
    return dict(domain=dict(height_bound=PROFILE_MAX_HEIGHT,
        totals=[dict(A=A, m=m) for A, m in profile_domain()],
        construction='Canonical lower mechanical c; h0=0; all 0<=h_i<=6 with a_i=c_i+h_i-h_(i+1)>=1, cyclic h_m=h0. All m<=11 and ceil(m log2 3)<=A<2m with gcd1; nearest-upper totals additionally at m13,17.'),
        counts=dict(sorted(counts.items())), universal_bound_counts=dict(sorted(universal_counts.items())),
        first_consistency_failures=examples, minimum_q_by_maximum_height={str(k): v for k, v in sorted(minima_by_height.items())},
        largest_universal_bound=largest_bound, largest_wide_universal_bound=largest_wide_bound,
        largest_zero_run_bound=largest_zero_bound, largest_wide_zero_run_bound=largest_wide_zero_bound,
        height_bound_candidate=dict(statement='B<=q-1 on geometrically consistent ordered cycles',
            status='finite diagnostic only; no theorem inferred', failures=candidate_failures,
            largest_observed_ratio=(rational(Fraction(max(largest_height_ratio['h']), largest_height_ratio['q']-1))
                                    if largest_height_ratio['q'] > 1 else None),
            ratio_witness=largest_height_ratio), verification_sha256=digest.hexdigest(),
        scope='All profiles produce legal positive primitive odd cycles, and all receive the universal prefix/packing checks. The prescribed height labels may fail geometric consistency or order; these failure classes are retained. Full rows including all numerator states enter the digest. No conclusion about untested periods, heights or arbitrary q1 words is inferred.')


def actual_audit():
    source = json.loads(ACTUAL.read_text())
    fixtures = json.loads(FIXTURES.read_text())['cycles']
    require(source['schema'] == 'C001-actual-raw-cycles-v1', 'wrong actual source schema')
    require(source['sources']['scanner_sha256'] == sha256(SCANNER.read_bytes()).hexdigest() and
            source['sources']['fixture_sha256'] == sha256(FIXTURES.read_bytes()).hexdigest(),
            'actual source dependency hash changed')
    cycles = source['cycles']
    require(len(cycles) == 2459 and len({c['d'] for c in cycles}) == 333, 'actual domain changed')
    fixture_index = {(f['d'], tuple(f['states'])): i+1 for i, f in enumerate(fixtures)}
    require(len(fixture_index) == len(fixtures) == 11, 'fixture domain changed')
    counts, bound_counts, order_counts = Counter(), Counter(), Counter()
    unique, fixture_keys, bases = {}, {}, {}
    all_digest, source_digest = sha256(), sha256()
    ordered_rows, gap_failures, bound_witnesses = [], {}, []
    max_bound, max_wide_bound = None, None
    for cycle in cycles:
        d, states, word = cycle['d'], cycle['states'], tuple(cycle['word'])
        n, q = cycle['primitive_states'], cycle['reduced_denominator']
        require(len(states) == len(n) == len(word) and len(set(states)) == len(states),
                'actual source cycle not simple')
        require(states[0] == min(states) and n[0] == min(n) and d % q == 0 and
                states == [(d//q)*x for x in n], 'source orientation/scaling failed')
        C, D, A = direct(word)
        g = gcd(C, D)
        require(D > 0 and D//g == q and C//g == n[0], 'actual denominator identity failed')
        for i, x in enumerate(states):
            require(raw_step(x, d) == (states[(i+1) % len(word)], word[i]), 'actual raw arrow failed')
            require(raw_step(n[i], q) == (n[(i+1) % len(word)], word[i]), 'reduced raw arrow failed')
            counts['actual_raw_arrows'] += 1
            counts['reduced_raw_arrows'] += 1
        counts['actual_cycles'] += 1
        stream_add(source_digest, [d, states, word, q, n])
        key = q, tuple(n)
        if key not in unique:
            base = bases.setdefault((A, len(word)), base_data(A, len(word)))
            universal = universal_metrics(n, q, word, base, g)
            count_universal(bound_counts, universal)
            Z, F, order, successor, monotone, rotation = normalized_order(n, q, universal['heights'])
            target = len(word) > 1 and n[0] >= q and monotone
            row = dict(primitive_states=n, word=list(word), universal=universal,
                       L_ge_q=n[0] >= q, monotone_images=monotone, rank_rotation=rotation,
                       ordered_diagnostic_domain=target)
            if target:
                full = ordered_metrics(n, q, word, base, universal)
                ordered_rows.append(full)
                order_counts['cycles'] += 1
                order_counts['wide_cycles'] += int(universal['wide'])
                order_counts['green_comparisons'] += len(word)
                order_counts['circular_gap_recurrence_checks'] += len(word)
                order_counts['all_pairs'] += full['pair_count']
                zero_runs = full['zero_defect_runs']
                zero_bound = zero_runs['denominator_lower_exact_run']
                histogram_bound = universal['denominator_lower_P_odd']
                order_counts['zero_run_divisibility_checks'] += zero_runs['nonzero_defects']
                order_counts['zero_run_edges'] += len(word)-zero_runs['nonzero_defects']
                order_counts['zero_run_bound_greater_than1'] += int(zero_bound > 1)
                order_counts['wide_zero_run_bound_greater_than1'] += int(universal['wide'] and zero_bound > 1)
                order_counts['uniform_zero_run_bound_greater_than1'] += int(zero_runs['denominator_lower_uniform_run'] > 1)
                order_counts['zero_run_bound_stronger_than_histogram'] += int(zero_bound > histogram_bound)
                order_counts['histogram_bound_stronger_than_zero_run'] += int(histogram_bound > zero_bound)
                for suffix in ('aggregate', 'P', 'P_odd'):
                    value = universal['denominator_lower_'+suffix]
                    order_counts[suffix+'_bound_greater_than1'] += int(value > 1)
                    order_counts[suffix+'_wide_bound_greater_than1'] += int(value > 1 and universal['wide'])
                for name, value in full['gap_minima'].items():
                    if value > q:
                        order_counts[name+'_bound_le_q_failures'] += 1
                        gap_failures.setdefault(name, full)
                order_counts['height_candidate_failures'] += int(not full['candidate_height_bound_holds'])
                if universal['wide'] and full['intercept_deficit'] < D:
                    gap_failures.setdefault('minimum_loss_at_least1', full)
                if universal['wide'] and Fraction(**full['normalized_minimum_loss']) < Fraction(**full['smallest_reference_neighbor_gap']):
                    gap_failures.setdefault('minimum_loss_at_least_reference_gap', full)
            if max_bound is None or universal['denominator_lower_P_odd'] > max_bound['universal']['denominator_lower_P_odd']:
                max_bound = row
            if universal['wide'] and (max_wide_bound is None or universal['denominator_lower_P_odd'] > max_wide_bound['universal']['denominator_lower_P_odd']):
                max_wide_bound = row
            if universal['wide'] and universal['denominator_lower_P_odd'] > 1 and len(bound_witnesses) < 12:
                bound_witnesses.append(row)
            unique[key] = row
            stream_add(all_digest, row)
        fixture_key = d, tuple(states)
        if fixture_key in fixture_index:
            identifier = fixture_index[fixture_key]
            require(tuple(fixtures[identifier-1]['valuations']) == word, 'fixture valuation mismatch')
            fixture_keys[identifier] = key
    require(set(fixture_keys) == set(range(1, 12)), 'not all fixtures exercised')
    require(counts['actual_raw_arrows'] == counts['reduced_raw_arrows'] == 36912 and len(unique) == 1184,
            'actual audit coverage changed')
    require(order_counts['cycles'] == 50 and order_counts['wide_cycles'] == 46,
            'ordered actual domain changed')
    single_defect = next(row for row in ordered_rows if row['universal']['denominator'] == 233 and
                         row['primitive_states'][0] == 1907)
    require(single_defect['weighted_intercept'] == 13349 and single_defect['positive_height_count'] == 1 and
            single_defect['universal']['numerator_gcd'] == 7, 'single-defect control mismatch')
    return dict(source_counts=dict(sorted(counts.items())), universal_bound_counts=dict(sorted(bound_counts.items())),
        ordered_counts=dict(sorted(order_counts.items())), all_source_rows_sha256=source_digest.hexdigest(),
        all_normalized_rows_sha256=all_digest.hexdigest(), ordered_cases=ordered_rows,
        gap_and_loss_counterexamples=gap_failures, single_defect_cancellation=single_defect,
        largest_universal_bound=max_bound, largest_wide_universal_bound=max_wide_bound,
        largest_zero_run_bound=max(ordered_rows, key=lambda row: row['zero_defect_runs']['denominator_lower_exact_run']),
        largest_wide_zero_run_bound=max((row for row in ordered_rows if row['universal']['wide']),
            key=lambda row: row['zero_defect_runs']['denominator_lower_exact_run']),
        first_wide_bound_witnesses=bound_witnesses,
        fixture_controls=[dict(fixture_id=i, fixture=fixtures[i-1], normalized_cycle=unique[fixture_keys[i]])
                          for i in sorted(fixture_keys)],
        scope='All1184 distinct normalized cycles receive the universal bounds, regardless of order. Fifty nontrivial cycles with L>=q and increasing normalized images receive the separate weighted and gap diagnostics. Scaling copies and all eleven raw fixtures remain explicit source controls.')


def relaxed_control():
    n, q, a, h, c = (4, 13, 5), 1, (0, 3, 2), (0, 1, 0), (1, 2, 2)
    require(all(3*n[i]+q == 2**a[i]*n[(i+1) % 3] for i in range(3)),
            'relaxed affine control does not satisfy its equations')
    require(tuple(a[i]+h[(i+1) % 3]-h[i] for i in range(3)) == c,
            'relaxed normalized exponent identity failed')
    z = [Fraction(n[i], 2**h[i]) for i in range(3)]
    F = [Fraction(3*n[i]+q, 2**h[i]) for i in range(3)]
    order = sorted(range(3), key=lambda i: z[i])
    require(all(F[order[i]] < F[order[i+1]] for i in range(2)), 'relaxed control lost order')
    rejected = {}
    for name, operation in [('positive_valuation_word', lambda: direct(a)),
                            ('odd_input_4', lambda: raw_step(4, 1))]:
        try:
            operation()
        except ValueError as error:
            rejected[name] = str(error)
        else:
            raise ValueError('strict validator accepted the relaxed control')
    require(raw_step(5, 1) == (1, 4), 'strict final arrow control failed')
    return dict(states=list(n), q=q, declared_valuations=list(a), heights=list(h), normalized_word=list(c),
        mantissas=[rational(x) for x in z], scaled_images=[rational(x) for x in F],
        strict_rejections=rejected, declared_last_arrow=[5, 4, 2], actual_last_arrow=[5, 1, 4],
        scope='A periodic affine control, not a raw odd-only cycle. It has an even state, a zero valuation and a final division that is not exact valuation. Ordered weighted equations alone would admit it; the strict declared domain rejects it.')


def report():
    return dict(schema='C006-order-rigidity-v1', baseline_commit=BASELINE,
        status='Exact finite discrimination and universal-bound checks; circular-order q1 exclusion and the speculative height bound remain unproved.',
        clock='Positive raw odd-only cycles, no absorber. The explicitly invalid affine control is isolated and rejected.',
        source_sha256={'check_order_rigidity.py': sha256(Path(__file__).read_bytes()).hexdigest(),
            'C001/actual_cycles.json': sha256(ACTUAL.read_bytes()).hexdigest(),
            'C001/scan_cycles.py': sha256(SCANNER.read_bytes()).hexdigest(),
            'phase6/cycle_fixtures.json': sha256(FIXTURES.read_bytes()).hexdigest(),
            'C005/check_order.py': sha256((HERE.parent/'C005/check_order.py').read_bytes()).hexdigest(),
            'C005/order_audit.json': sha256((HERE.parent/'C005/order_audit.json').read_bytes()).hexdigest()},
        actual=actual_audit(), profiles=profile_grid(), relaxed_affine_control=relaxed_control(),
        scope='The packing/minimum denominator law is universal and is not claimed as order-specific progress or novel. Height/order profile failures and gap counterexamples expose missing hypotheses. Every success of B<=q-1 is finite evidence only; no unrestricted word or cycle conclusion follows.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='write the recomputed exact receipt')
    args = parser.parse_args()
    result = report()
    target = HERE/'order_rigidity_audit.json'
    if args.write:
        target.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(target.exists(), 'missing receipt; explicit --write is required')
        require(json.loads(target.read_text()) == result, 'saved receipt differs from exact recomputation')
    print(json.dumps(dict(status='PASS', mode='write' if args.write else 'replay',
        actual_sources=result['actual']['source_counts'],
        actual_universal=result['actual']['universal_bound_counts'],
        actual_ordered=result['actual']['ordered_counts'],
        profiles=result['profiles']['counts'], profile_universal=result['profiles']['universal_bound_counts']),
        sort_keys=True))


if __name__ == '__main__':
    main()
