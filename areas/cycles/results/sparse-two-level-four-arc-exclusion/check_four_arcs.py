#!/usr/bin/env python3
"""Exact finite certificate; no optimization package is imported here."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


# Affine points have coefficients (u, p, q, constant); epsilon appears only
# after conversion to an inequality row.
zero = (F(0), F(0), F(0), F(0))
one = (F(0), F(0), F(0), F(1))
h = (F(1), F(0), F(0), F(0))
p = (F(0), F(1), F(0), F(0))
q = (F(0), F(0), F(1), F(0))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul(k, a):
    return tuple(k * x for x in a)


def row(v, eps=0):
    """Return integers: first four dot (u,p,q,epsilon) <= the last.

    The input represents v(u,p,q)+eps*epsilon <= 0. Only positive
    scalings clear denominators and remove common integer factors.
    """
    values = list(v[:3]) + [F(eps), -v[3]]
    common = lcm(*(x.denominator for x in values))
    integers = [int(x * common) for x in values]
    factor = gcd(*integers)
    return [x // factor for x in integers] if factor else integers


def less(rows, left, right):
    rows.append(row(sub(left, right)))


def witness(rows, sequence, threshold, shift):
    previous = zero
    cut = next(i for i, (name, _) in enumerate(sequence) if name == threshold)
    for i, (_, endpoint) in enumerate(sequence):
        height = add(endpoint, shift) if i <= cut else endpoint
        gap = sub(endpoint, previous)
        rows.append(row(sub(gap, mul(F(3, 8), height)), -1))
        previous = endpoint


def cells():
    """Generate all cells in the canonical order used by the dual receipt.

    Thirty rows, indexed from zero: 0..5 box; 6 p<=q; 7..8 wraps;
    9..14 second-list order; 15..18 first-list order; 19..22 first
    witnesses; 23..28 second witnesses; 29 epsilon<=1/193. The order
    includes weak inequalities, empty cells and all boundary ties.
    """
    for wp, wq in itertools.product((0, 1), repeat=2):
        points = {
            'Q': sub(one, mul(2, h)),
            'p': p,
            'pm': add(sub(p, h), mul(wp, one)),
            'q': q,
            'qm': add(sub(q, h), mul(wq, one)),
        }
        for perm in itertools.permutations(points):
            for order1 in (('p', 'q', 'R'), ('p', 'R', 'q'), ('R', 'p', 'q')):
                rows = []
                for value, high in ((h, F(1, 2)), (p, F(1)), (q, F(1))):
                    less(rows, zero, value)
                    less(rows, value, mul(high, one))
                less(rows, p, q)
                if wp:
                    less(rows, p, h)
                else:
                    less(rows, h, p)
                if wq:
                    less(rows, q, h)
                else:
                    less(rows, h, q)
                sequence2 = [(name, points[name]) for name in perm] + [('X', one)]
                previous = zero
                for _, endpoint in sequence2:
                    less(rows, previous, endpoint)
                    previous = endpoint
                first = {'p': p, 'q': q, 'R': sub(one, h)}
                sequence1 = [(name, first[name]) for name in order1] + [('X', one)]
                previous = zero
                for _, endpoint in sequence1:
                    less(rows, previous, endpoint)
                    previous = endpoint
                witness(rows, sequence1, 'R', h)
                witness(rows, sequence2, 'Q', mul(2, h))
                rows.append([0, 0, 0, 193, 1])
                yield (wp, wq, perm, order1), rows


def verify_duals():
    path = HERE / 'explore_cells.json'
    data = json.loads(path.read_text())
    all_cells = list(cells())
    proofs = data['proofs']
    require(len(all_cells) == len(proofs) == 1440, 'cell coverage')
    gaps = []
    supports = []
    for number, ((key, rows), proof) in enumerate(zip(all_cells, proofs)):
        require(len(rows) == 30, ('row count', number))
        require(1 <= len(proof) <= 5, ('support size', number))
        require(len({item[0] for item in proof}) == len(proof), 'duplicate row')
        weighted = [F(0)] * 5
        total = F(0)
        for index, numerator, denominator in proof:
            require(0 <= index < len(rows), ('row index', number))
            require(numerator >= 0 and denominator > 0, 'multiplier sign')
            weight = F(numerator, denominator)
            total += weight
            for j in range(5):
                weighted[j] += weight * rows[index][j]
        require(total == 1, ('weight normalization', number))
        require(weighted[:4] == [0] * 4, ('uncancelled coefficient', number))
        require(weighted[4] < 0, ('no contradiction', number))
        gaps.append(-weighted[4])
        supports.append(len(proof))
    require(min(gaps) == F(1, 4824), 'minimum contradiction')
    require(data['minimum_contradiction'] == str(min(gaps)), 'dual metadata')
    require(data['max_support'] == max(supports), 'support metadata')
    return {
        'cells': len(all_cells),
        'rows_per_cell': 30,
        'maximum_support': max(supports),
        'minimum_contradiction': str(min(gaps)),
        'dual_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def verify_geometry():
    # This regression checks the discrete-to-continuous correspondence. The
    # universal cell exhaustion is the construction and exact dual replay above.
    cell_index = {key: rows for key, rows in cells()}
    words = intervals = ties = interior_positions = 0
    equality_witnesses = reversal_checks = 0
    for m in range(4, 25):
        for step in range(1, (m + 1) // 2):
            if gcd(step, m) != 1:
                continue
            x = m - 1
            for a in range(1, m - 2):
                for b in range(1, m - a - 1):
                    c = m - 1 - a - b
                    track = [3] + [1] * a + [2] * b + [1] * c
                    word = [0] * m
                    for j, letter in enumerate(track):
                        word[(x + j * step) % m] = letter
                    require([word[(x - j * step) % m] for j in range(m)]
                            == [3] + [1] * c + [2] * b + [1] * a,
                            'orientation reversal')
                    reversal_checks += 1
                    p1 = (x + a * step) % m
                    p2 = (x + (a + b) * step) % m
                    e1 = {x, (x - step) % m, p1, p2}
                    e2 = {x, (x - 2 * step) % m, p1, p2,
                          (p1 - step) % m, (p2 - step) % m}
                    mismatches1 = {i for i in range(m)
                                   if word[i] != word[(i + step) % m]}
                    mismatches2 = {i for i in range(m)
                                   if word[i] != word[(i + 2 * step) % m]}
                    require(mismatches1 == e1 and len(e1) == 4, 'first mismatch set')
                    require(mismatches2 <= e2, 'second mismatch superset')
                    require(word[(x - step) % m] == word[(x + step) % m] == 1,
                            'removed second-rotation point')
                    pp, qq = sorted((p1 + 1, p2 + 1))
                    uu = F(step, m)
                    pv, qv = F(pp, m), F(qq, m)
                    wp, wq = int(pv <= uu), int(qv <= uu)
                    points2 = {'Q': 1 - 2 * uu, 'p': pv, 'q': qv,
                               'pm': pv - uu + wp, 'qm': qv - uu + wq}
                    perm = tuple(sorted(points2, key=lambda label:
                                        (points2[label], label == 'Q', label)))
                    points1 = {'R': 1 - uu, 'p': pv, 'q': qv}
                    order1 = tuple(sorted(points1, key=lambda label:
                                          (points1[label], label == 'R', label)))
                    key = (wp, wq, perm, order1)
                    require(key in cell_index, ('missing weak-order cell', key))
                    values = (uu, pv, qv)
                    rows = cell_index[key]
                    require(all(sum(row[i] * values[i] for i in range(3)) <= row[4]
                                for row in rows[:19]), 'geometry cell inequalities')
                    for k, names, points, threshold in (
                            (1, order1, points1, 'R'), (2, perm, points2, 'Q')):
                        seq = [(name, points[name]) for name in names] + [('X', F(1))]
                        cut = names.index(threshold)
                        previous = 0
                        for pos, (name, endpoint) in enumerate(seq):
                            end = endpoint * m
                            require(end.denominator == 1, 'nonintegral boundary')
                            end = int(end)
                            gap = end - previous
                            require(gap >= 0, 'boundary order')
                            intervals += 1
                            if gap == 0:
                                ties += 1
                            else:
                                for i in range(previous, end - 1):
                                    require(word[i] == word[(i + k * step) % m],
                                            'artificial interval contains mismatch')
                                    interior_positions += 1
                                partner = F(((end - 1 + k * step) % m) + 1, m)
                                selected = endpoint + k * uu if pos <= cut else endpoint
                                require(selected == max(endpoint, partner),
                                        ('witness branch', key, name))
                                equality_witnesses += int(endpoint == 1 - k * uu)
                            previous = end
                    words += 1
    require(words == 9912 and intervals == 99120 and ties == 3567,
            'finite geometry coverage')
    return {'length_min': 4, 'length_max': 24, 'track_words': words,
            'reversal_checks': reversal_checks, 'artificial_intervals': intervals,
            'zero_length_ties': ties, 'agreeing_positions': interior_positions,
            'positive_gap_equality_witnesses': equality_witnesses}


def valuation_two(number):
    require(number > 0, 'valuation input')
    return (number & -number).bit_length() - 1


def verify_descent():
    seeds = steps = longest = 0
    for seed in range(3, 128, 2):
        state = seed
        local = 0
        while state >= seed:
            require(local < 10000, ('descent guard', seed))
            raw = 3 * state + 1
            state = raw >> valuation_two(raw)
            local += 1
        require(state > 0 and state % 2 == 1, 'descent endpoint')
        seeds += 1
        steps += local
        longest = max(longest, local)
    require((seeds, steps, longest) == (63, 357, 37), 'descent totals')
    return {'odd_seeds': seeds, 'seed_max': 127, 'odd_steps': steps,
            'maximum_first_descent_length': longest, 'guard_per_seed': 10000}


def verify_constants():
    left, right = 388**8, 27 * 256 * 129**8
    require(left < right, 'slope below 3/8')
    require(F(4, 3)**3 < 3, 'twos displacement')
    require(F(3, 2)**3 < 4, 'basic growth sanity')
    k = 22
    numerator = 173 + 342 * (k + 1)
    require(numerator > 342, 'dyadic decrease base')
    # The numerator increases with k, so numerator>342 persists; this makes
    # (numerator+342)/2 smaller than numerator at every later dyadic interval.
    error = F(numerator, 2**k) + F(1, 384)
    margin = F(1, 193) - error
    require(error == F(56885, 12582912) and margin > 0, 'finite error ceiling')
    require(margin == F(1604107, 2428502016), 'finite margin')
    require(3**2 > 2**3, 'alpha exceeds 3/2')
    require(F(4, 3) * F(1, 512) == F(1, 384),
            'expanding-template discrepancy uses the original error ceiling')
    contracting_margin = F(95 * 2**k, 256) - (172 + 342 * (k + 1))
    require(contracting_margin == 1548442 and contracting_margin > 0,
            'contracting-template cutoff')
    require(F(95 * 2**k, 256) > 342,
            'contracting dyadic margin increases at every subsequent index')
    return {'minimum_length': 2**k, 'maximum_twos_fraction': '1/128',
            'slope_power_left': left, 'slope_power_right': right,
            'dyadic_error_ceiling': str(error), 'margin_below_1_over_193': str(margin),
            'alternative_maximum_cf_sum_fraction': '1/512',
            'contracting_dyadic_base_margin': int(contracting_margin)}


def continued_fraction_sum(numerator, denominator):
    """Canonical [0; d1,...,dl] for a reduced fraction in (0,1)."""
    require(0 < numerator < denominator and gcd(numerator, denominator) == 1,
            'continued-fraction input')
    coefficients = []
    left, right = denominator, numerator
    while right:
        quotient, remainder = divmod(left, right)
        coefficients.append(quotient)
        left, right = right, remainder
    require(coefficients[-1] >= 2, 'canonical final coefficient')
    rebuilt = F(coefficients[-1])
    for coefficient in reversed(coefficients[:-1]):
        rebuilt = coefficient + 1 / rebuilt
    require(1 / rebuilt == F(numerator, denominator), 'continued-fraction reconstruction')
    return sum(coefficients)


def reduced_cycle(word):
    """Return the actual reduced 3x+q cycle for a positive-D word."""
    m = len(word)
    total = sum(word)
    denominator = 2**total - 3**m
    require(denominator > 0, 'template control needs positive D')
    intercept = prefix = 0
    for j, letter in enumerate(word):
        intercept += 3**(m - 1 - j) * 2**prefix
        prefix += letter
    common = gcd(intercept, denominator)
    addend = denominator // common
    state = intercept // common
    states = []
    for letter in word:
        states.append(state)
        raw = 3 * state + addend
        require(valuation_two(raw) == letter, 'reduced-cycle exact valuation')
        state = raw >> letter
    require(state == states[0], 'reduced-cycle closure')
    require(all(x > 0 and x % 2 == 1 for x in states), 'reduced odd states')
    require(len(set(states)) == m, 'unique spike gives distinct states')
    return addend, states


def verify_template_envelopes():
    templates = factors = inverse_checks = crossing_factors = 0
    expanding = contracting = 0
    expanding_cycles = contracting_cycles = 0
    maximum_k = 0
    for m in range(4, 25):
        spike = m - 1
        for step in range(1, m):
            if gcd(step, m) != 1:
                continue
            inverse = pow(step, -1, m)
            require(step * inverse % m == 1, 'chronological inverse')
            complexity = continued_fraction_sum(inverse, m)
            maximum_k = max(maximum_k, complexity)
            delta = 2 * (complexity - 1)
            inverse_checks += 1
            for a in range(1, m - 2):
                for b in range(1, m - a - 1):
                    c = m - 1 - a - b
                    track = [1] + [1] * a + [2] * b + [1] * c
                    template = [0] * m
                    for j, letter in enumerate(track):
                        template[(spike + j * step) % m] = letter
                    require(sum(abs(track[(j + 1) % m] - track[j])
                                for j in range(m)) == 2, 'binary track variation')
                    require(all(template[i] == track[((i - spike) * inverse) % m]
                                for i in range(m)), 'chronological coding')
                    template_total = m + b
                    require(sum(template) == template_total, 'template total')
                    for start in range(m):
                        running = 0
                        for length in range(1, m):
                            running += template[(start + length - 1) % m]
                            require(abs(m * running - template_total * length) <= m * delta,
                                    'all-factor template discrepancy')
                            factors += 1
                            crossing_factors += int(start + length > m)
                    is_expanding = 2**template_total < 3**m
                    expanding += int(is_expanding)
                    contracting += int(not is_expanding)
                    # Two edit amplitudes per template: the least positive-gap
                    # spike >=3, and two extra powers of two at that position.
                    least_spike = max(3, (3**m).bit_length() - template_total + 1)
                    for value in (least_spike, least_spike + 2):
                        word = template[:]
                        word[spike] = value
                        addend, states = reduced_cycle(word)
                        minimum, maximum = min(states), max(states)
                        if is_expanding:
                            require(states[0] <= 2**delta * minimum,
                                    'post-spike to minimum envelope')
                            expanding_cycles += 1
                        else:
                            require(3 * maximum <= 2**delta * (3 * minimum + m * addend),
                                    'contracting affine envelope retains q')
                            contracting_cycles += 1
                    templates += 1
    require((templates, factors, expanding, contracting)
            == (19824, 7646880, 17352, 2472), 'template coverage')
    require(expanding_cycles == 2 * expanding and contracting_cycles == 2 * contracting,
            'two amplitudes in both mean regimes')
    return {
        'length_min': 4, 'length_max': 24,
        'all_coprime_track_steps': True,
        'inverse_and_continued_fraction_checks': inverse_checks,
        'maximum_partial_quotient_sum': maximum_k,
        'binary_templates': templates,
        'proper_template_factors': factors,
        'factors_crossing_chronological_cut': crossing_factors,
        'expanding_templates': expanding, 'contracting_templates': contracting,
        'expanding_reduced_cycles': expanding_cycles,
        'contracting_reduced_cycles': contracting_cycles,
        'scope': 'Discrepancy and q-scaled envelopes; no finite-grid cycle exclusion is inferred.',
    }


def verify_controls():
    path = ROOT / 'areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json'
    fixtures = json.loads(path.read_text())['cycles']
    rows = []
    total_pairs = total_prefixes = 0
    for fixture in fixtures:
        d = fixture['d']
        states, word = fixture['states'], fixture['valuations']
        m = len(word)
        require(len(states) == m and len(set(states)) == m, 'fixture period')
        require(min(states) == fixture['minimum'], 'fixture minimum')
        for i, state in enumerate(states):
            require(state > 0 and state % 2 == 1, 'fixture odd state')
            raw = 3 * state + d
            require(valuation_two(raw) == word[i], 'fixture exact valuation')
            require(raw >> word[i] == states[(i + 1) % m], 'fixture arrow')
        pairs = prefixes = 0
        for shift in range(1, m):
            for start in range(m):
                pairs += 1
                common_total = 0
                start_difference = states[start] - states[(start + shift) % m]
                for length in range(m):
                    end = (start + length) % m
                    difference = states[end] - states[(end + shift) % m]
                    require(difference != 0, 'distinct paired states')
                    require(3**length * start_difference == 2**common_total * difference,
                            'paired affine identity')
                    require(difference % (2 * 3**length) == 0, 'paired endpoint divisibility')
                    require(max(states[end], states[(end + shift) % m]) > 2 * 3**length,
                            'paired run height')
                    prefixes += 1
                    if word[end] != word[(end + shift) % m]:
                        break
                    common_total += word[end]
                else:
                    raise RuntimeError('nonprimitive fixture')
        total_pairs += pairs
        total_prefixes += prefixes
        rows.append({'d': d, 'minimum': min(states), 'odd_period': m,
                     'paired_starts': pairs, 'agreeing_prefixes': prefixes})
    require(len(rows) == 11 and {row['d'] for row in rows} == {5, 7, 13, 61},
            'control coverage')
    return {'fixture_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'cycles': rows, 'paired_starts': total_pairs,
            'agreeing_prefixes': total_prefixes,
            'scope': 'Exact 3x+d arrows and addend-independent paired run bounds only.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result = {'schema': 'sparse-two-level-four-arc-v2',
              'exact_cells': verify_duals(), 'finite_geometry': verify_geometry(),
              'local_descent': verify_descent(), 'constants': verify_constants(),
              'actual_controls': verify_controls(),
              'binary_template_envelopes': verify_template_envelopes()}
    receipt = HERE / 'check_four_arcs.json'
    if args.write_receipt:
        receipt.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    else:
        require(json.loads(receipt.read_text()) == result, 'receipt mismatch; regenerate explicitly')
    print(json.dumps({'status': 'passed', 'exact_cells': result['exact_cells']['cells'],
                      'geometry_words': result['finite_geometry']['track_words'],
                      'local_descent_seeds': result['local_descent']['odd_seeds'],
                      'actual_cycles': len(result['actual_controls']['cycles']),
                      'binary_templates': result['binary_template_envelopes']['binary_templates']}, sort_keys=True))


if __name__ == '__main__':
    main()
