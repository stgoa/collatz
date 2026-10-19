#!/usr/bin/env python3
"""C007 exact small-denominator discrimination of the candidate B<=q-1.

Default replay repeats the entire deterministic bounded seed census.
Only certified cycle basins are memoized. Capped and unprocessed seeds
remain unresolved; finite survival never proves the candidate.
"""

import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
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
FIXTURES = ROOT/'experiments/phase6/cycle_fixtures.json'
C006 = HERE.parent/'C006/order_rigidity_audit.json'
PATH_STEP_CAP = 20000
STATE_BIT_CAP = 512
ARROWS_PER_PARAMETER_CAP = 10000000


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def raw_step(n, d):
    require(type(n) is int and n > 0 and n % 2 and type(d) is int and
            d > 0 and gcd(d, 6) == 1, 'invalid raw positive odd input')
    value = 3*n+d
    a = (value & -value).bit_length()-1
    return value >> a, a


def canonical(states):
    require(states and len(set(states)) == len(states), 'cycle must be simple')
    start = states.index(min(states))
    return states[start:]+states[:start]


def word_data(word):
    require(word and all(type(a) is int and a >= 1 for a in word), 'invalid exact valuation word')
    A, C = 0, 0
    for a in word:
        C = 3*C+2**A
        A += a
    return A, C, 2**A-3**len(word)


@lru_cache(maxsize=None)
def denominator_arithmetic(q):
    require(q > 1 and gcd(q, 6) == 1, 'multiplicative-order domain failed')
    remaining, phi, prime = q, q, 2
    while prime*prime <= remaining:
        if remaining % prime == 0:
            phi = phi//prime*(prime-1)
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        phi = phi//remaining*(remaining-1)
    residue, order = 2 % q, 1
    while residue != 1:
        residue = 2*residue % q
        order += 1
        require(order <= phi, 'multiplicative-order computation failed')
    require(phi % order == 0, 'order does not divide Euler phi')
    return order, phi


def reduced_certificate(n, q):
    """An exact simple raw cycle at its common reduced denominator."""
    require(n == canonical(n), 'reduced cycle not in minimum-state orientation')
    word = []
    for i, x in enumerate(n):
        target, a = raw_step(x, q)
        require(target == n[(i+1) % len(n)], 'raw cycle arrow failed')
        require(gcd(x, q) == 1, 'cycle is not reduced')
        word.append(a)
    A, C, D = word_data(word)
    g = gcd(C, D)
    require(D > 0 and C//g == n[0] and D//g == q, 'cycle denominator identity failed')
    m, L, H = len(n), n[0], max(n)
    h = [(x//L).bit_length()-1 for x in n]
    B = max(h)
    require(all(2**t*L <= x < 2**(t+1)*L for x, t in zip(n, h)), 'dyadic height failed')
    Z = [x << (B-t) for x, t in zip(n, h)]
    F = [(3*x+q) << (B-t) for x, t in zip(n, h)]
    require(len(set(Z)) == m, 'distinct odd states have equal mantissas')
    order = sorted(range(m), key=Z.__getitem__)
    ranks = {i: j for j, i in enumerate(order)}
    successor = [ranks[(i+1) % m] for i in order]
    monotone = all(F[order[j]] < F[order[j+1]] for j in range(m-1))
    rotation = len({(successor[j]-j) % m for j in range(m)}) == 1
    J = 1+sum(h[i] != h[j] for i, j in zip(order, order[1:]))
    c = [word[i]+h[(i+1) % m]-h[i] for i in range(m)]
    require(sum(c) == A, 'coboundary sum failed')
    if L >= q:
        require(all(x in (1, 2) for x in c), 'normalized valuation outside one/two')
        require(monotone == rotation, 'order/rank-rotation equivalence failed')
    domain = m > 1 and L >= q and monotone
    if domain:
        require(c == [(i+1)*A//m-i*A//m for i in range(m)], 'ordered canonical code not mechanical')
        require(gcd(A, m) == 1 and J >= B+1, 'ordered primitive totals or height coverage failed')
    top_comparisons = []
    if B:
        for x, height in zip(n, h):
            if height == B:
                r = x-2**B*L
                slack = 3*r-q*(2**B-1)
                require(r > 0 and r % 2 == 1, 'odd top-height remainder failed')
                require(slack == 3*x+q-2**B*(3*L+q), 'top/minimum image identity failed')
                if domain:
                    require(slack > 0, 'ordered top/minimum comparison is inverted')
                top_comparisons.append(dict(top_state=x, remainder=r, image_difference_numerator=slack,
                    image_difference_denominator=2**B))
    order2, phi = denominator_arithmetic(q) if q > 1 else (None, None)
    return dict(q=q, m=m, A=A, C=C, D=D, numerator_gcd=g, L=L, H=H,
        B=B, J=J, word=word, states=n, heights=h, normalized_word=c,
        sorted_indices=order, monotone_images=monotone, successor_rank_rotation=rotation,
        L_ge_q=L >= q, candidate_domain=domain, candidate_holds=B <= q-1,
        candidate_margin=q-1-B, ratio_B_over_q_minus1=([B, q-1] if q > 1 else None),
        stronger_logarithmic_bound_holds=B <= q.bit_length()-1,
        stronger_half_linear_bound_holds=2*B <= q-1,
        order_of_2_mod_q=order2, euler_phi_q=phi,
        stronger_multiplicative_order_bound_holds=(B < order2 if q > 1 else None),
        stronger_euler_phi_bound_holds=(B < phi if q > 1 else None),
        top_height_minimum_comparisons=top_comparisons)


def source_certificate(d, states):
    states = canonical(list(states))
    word = []
    for i, x in enumerate(states):
        target, a = raw_step(x, d)
        require(target == states[(i+1) % len(states)], 'source raw arrow failed')
        word.append(a)
    A, C, D = word_data(word)
    g = gcd(C, D)
    q = D//g
    require(D > 0 and d % q == 0, 'source denominator does not divide d')
    scale = d//q
    require(all(x % scale == 0 for x in states), 'source scaling not integral')
    reduced = reduced_certificate([x//scale for x in states], q)
    require(reduced['word'] == word and reduced['A'] == A, 'scaling changed exact valuations')
    return reduced, scale


def key(row):
    return row['q'], tuple(row['states'])


def summarize(rows):
    rows = sorted(rows, key=lambda r: (r['q'], r['L']))
    domain = [r for r in rows if r['candidate_domain']]
    near = sorted(domain, key=lambda r: (r['q'] == 1,
        Fraction(r['B'], r['q']-1) if r['q'] > 1 else Fraction(0), -r['q'], -r['L']), reverse=True)
    comparable = [r for r in domain if r['B'] > 0 and 4*r['B'] >= r['q']-1]
    maximum_by_q = {}
    for r in domain:
        if str(r['q']) not in maximum_by_q or r['B'] > maximum_by_q[str(r['q'])]['B']:
            maximum_by_q[str(r['q'])] = r
    wide = [r for r in domain if r['B'] > 0]
    closest_top = min(wide, key=lambda r: min(x['image_difference_numerator']
                      for x in r['top_height_minimum_comparisons']), default=None)
    return dict(counts=dict(normalized_cycles=len(rows), nontrivial=sum(r['m'] > 1 for r in rows),
        ordered_domain=len(domain), wide_ordered=sum(r['B'] > 0 for r in domain),
        comparable_height_denominator=len(comparable),
        candidate_failures=sum(not r['candidate_holds'] for r in domain),
        outside_order_candidate_failures=sum(not r['candidate_holds'] and not r['candidate_domain'] for r in rows)),
        near_boundary=near[:12], comparable_cases=comparable,
        maximum_height_by_denominator=maximum_by_q,
        candidate_failures=[r for r in domain if not r['candidate_holds']],
        outside_order_candidate_failures=[r for r in rows if not r['candidate_holds'] and not r['candidate_domain']],
        stronger_logarithmic_failures=[r for r in domain if not r['stronger_logarithmic_bound_holds']],
        stronger_half_linear_failures=[r for r in domain if not r['stronger_half_linear_bound_holds']],
        stronger_multiplicative_order_failures=[r for r in domain if r['stronger_multiplicative_order_bound_holds'] is False],
        outside_domain_multiplicative_order_failures=[r for r in rows if not r['candidate_domain']
            and r['stronger_multiplicative_order_bound_holds'] is False],
        stronger_euler_phi_failures=[r for r in domain if r['stronger_euler_phi_bound_holds'] is False],
        all_domain_euler_phi_failures=[r for r in rows if r['stronger_euler_phi_bound_holds'] is False],
        closest_top_height_minimum_comparison=closest_top,
        all_rows_sha256=digest(rows),
        scope='Comparable means B>0 and B/(q-1)>=1/4. It is a descriptive stratum, not a theorem hypothesis or evidence that other cases cannot violate the conjecture.')


def existing_audit():
    source = json.loads(ACTUAL.read_text())
    fixtures = json.loads(FIXTURES.read_text())['cycles']
    require(source['schema'] == 'C001-actual-raw-cycles-v1' and len(source['cycles']) == 2459,
            'unexpected actual source')
    require(source['sources']['fixture_sha256'] == sha256(FIXTURES.read_bytes()).hexdigest(),
            'fixture hash changed')
    require(source['sources']['scanner_sha256'] == sha256((HERE.parent/'C001/scan_cycles.py').read_bytes()).hexdigest(),
            'stored actual scanner dependency changed')
    unique, source_index, arrows = {}, {}, 0
    source_scales = Counter()
    for row in source['cycles']:
        reduced, scale = source_certificate(row['d'], row['states'])
        require(reduced['states'] == row['primitive_states'] and reduced['q'] == row['reduced_denominator']
                and reduced['word'] == row['word'], 'stored reduction disagrees with recomputation')
        unique[key(reduced)] = reduced
        source_index[row['d'], tuple(row['states'])] = reduced
        source_scales[scale] += 1
        arrows += reduced['m']
    require(len(unique) == 1184 and arrows == 36912, 'existing audit coverage changed')
    controls = []
    for i, fixture in enumerate(fixtures):
        reduced = source_index[fixture['d'], tuple(fixture['states'])]
        require(fixture['valuations'] == reduced['word'], 'fixture exact valuations changed')
        controls.append(dict(fixture_id=i+1, fixture=fixture, reduced_cycle=reduced))
    require(len(controls) == 11, 'eleven fixture controls required')
    result = summarize(unique.values())
    previous = json.loads(C006.read_text())
    old_ordered = {(r['universal']['denominator'], tuple(r['primitive_states'])) for r in previous['actual']['ordered_cases']}
    require(old_ordered == {key(r) for r in unique.values() if r['candidate_domain']},
            'C006 ordered domain changed')
    result.update(source_cycles=2459, parameter_count=len({r['d'] for r in source['cycles']}),
        source_raw_arrows=arrows, reduced_raw_arrows=arrows, fixture_controls=controls,
        scaling_counts={str(k): v for k, v in sorted(source_scales.items())},
        spectrum=[{k: r[k] for k in ('q', 'm', 'A', 'L', 'H', 'B', 'J', 'candidate_domain', 'candidate_holds')}
                  for r in sorted(unique.values(), key=lambda r: (r['q'], r['L']))])
    return result, unique


def census_domain():
    params = {d: 200001 for d in range(1, 98, 2) if d % 3}
    params[5] = 4000001
    for d in (7, 11, 13, 29):
        params[d] = 2000001
    return params


def scan_parameter(d, seed_max):
    """Only exact certified basins enter memo; no cap implies convergence."""
    memo, discovered, caps, outcomes = set(), {}, [], Counter()
    arrows, peak_bits = 0, 0
    requested = (seed_max+1)//2
    for seed in range(1, seed_max+1, 2):
        if arrows >= ARROWS_PER_PARAMETER_CAP:
            break
        if seed in memo:
            outcomes['certified_cycle_basin'] += 1
            continue
        path, positions, n = [], {}, seed
        while True:
            if n in memo:
                reason = 'certified_cycle_basin'
                break
            if n in positions:
                cycle = canonical(path[positions[n]:])
                cycle_key = tuple(cycle)
                if cycle_key not in discovered:
                    reduced, scale = source_certificate(d, cycle)
                    discovered[cycle_key] = dict(d=d, states=cycle, scale=scale, reduced_cycle=reduced,
                        first_seed=seed, first_seed_preperiod=positions[n], path_length=len(path))
                reason = 'certified_cycle_basin'
                break
            peak_bits = max(peak_bits, n.bit_length())
            if n.bit_length() > STATE_BIT_CAP:
                reason = 'state_bit_cap'
                break
            if len(path) >= PATH_STEP_CAP:
                reason = 'path_step_cap'
                break
            if arrows >= ARROWS_PER_PARAMETER_CAP:
                reason = 'parameter_arrow_cap'
                break
            positions[n] = len(path)
            path.append(n)
            value = 3*n+d
            n = value//(value & -value)
            arrows += 1
        outcomes[reason] += 1
        if reason == 'certified_cycle_basin':
            memo.update(path)
        else:
            caps.append(dict(seed=seed, reason=reason, new_path_arrows=len(path),
                last_state=n, last_state_bits=n.bit_length(), path_sha256=digest(path)))
    processed = sum(outcomes.values())
    rows = sorted(discovered.values(), key=lambda r: r['states'][0])
    # Independently replay the first-seed connection for every discovered cycle.
    for row in rows:
        n = row['first_seed']
        for unused in range(row['first_seed_preperiod']):
            n = raw_step(n, d)[0]
        require(n in row['states'], 'first discovery seed does not reach its recorded cycle')
    return dict(d=d, seed_max=seed_max, requested_seeds=requested, processed_seeds=processed,
        unprocessed_seeds=requested-processed, outcomes=dict(sorted(outcomes.items())),
        new_arrows=arrows, memoized_certified_states=len(memo), peak_state_bits=peak_bits,
        capped_paths=caps, discovered_cycles=rows)


def targeted_census(previous):
    reports = [scan_parameter(d, limit) for d, limit in census_domain().items()]
    unique, counts = {}, Counter()
    for report in reports:
        for row in report['discovered_cycles']:
            reduced = row['reduced_cycle']
            unique[key(reduced)] = reduced
        for name in ('requested_seeds', 'processed_seeds', 'unprocessed_seeds', 'new_arrows'):
            counts[name] += report[name]
        counts['capped_paths'] += len(report['capped_paths'])
        counts['source_cycles'] += len(report['discovered_cycles'])
    new = [r for k, r in unique.items() if k not in previous]
    result = summarize(unique.values())
    result.update(parameters=dict(seed_max_by_d={str(d): limit for d, limit in census_domain().items()},
        path_step_cap=PATH_STEP_CAP, state_bit_cap=STATE_BIT_CAP,
        new_arrows_per_parameter_cap=ARROWS_PER_PARAMETER_CAP,
        memoization='Only paths already connected to an exactly closed cycle are memoized; capped paths are never memoized.'),
        census_counts=dict(sorted(counts.items())), reports=reports,
        new_normalized_cycles=new, new_normalized_summary=summarize(new),
        interpretation='A deterministic bounded seed census at small additive parameters, with deeper scans at d5,7,11,13,29. Reduced denominators divide d. Every capped or unprocessed seed is unresolved; cycles outside the seed range may exist. Default replay reruns every processed seed, not only stored cycles.')
    return result, unique


def report():
    old, previous = existing_audit()
    census, discovered = targeted_census(previous)
    combined = dict(previous)
    combined.update(discovered)
    return dict(schema='C007-height-denominator-v1',
        conjecture='For every simple positive raw odd cycle with reduced denominator q, q<=L and circular normalized successor order, B<=q-1.',
        status='Finite discrimination only. The conjecture remains unproved unless a separately checked counterexample is present.',
        clock='Raw positive odd-only map, no absorber; exact valuations and reduced denominators retained.',
        source_sha256={'check_height_denominator.py': sha256(Path(__file__).read_bytes()).hexdigest(),
            'C001/actual_cycles.json': sha256(ACTUAL.read_bytes()).hexdigest(),
            'C001/scan_cycles.py': sha256((HERE.parent/'C001/scan_cycles.py').read_bytes()).hexdigest(),
            'phase6/cycle_fixtures.json': sha256(FIXTURES.read_bytes()).hexdigest(),
            'C006/order_rigidity_audit.json': sha256(C006.read_bytes()).hexdigest()},
        existing=old, small_parameter_census=census, combined=summarize(combined.values()),
        scope='The finite test deliberately separates small-denominator near-bound cases from large-q passes. Logarithmic, half-linear, multiplicative-order and Euler-phi strengthenings are separate diagnostics, not adopted theorems. No scan establishes the absence of further cycles or any convergence claim.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = report()
    target = HERE/'height_denominator_audit.json'
    if args.write:
        target.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(target.exists(), 'missing receipt; explicit --write is required')
        require(json.loads(target.read_text()) == result, 'receipt differs from exact bounded recomputation')
    print(json.dumps(dict(status='PASS', mode='write' if args.write else 'replay',
        existing=result['existing']['counts'], combined=result['combined']['counts'],
        census=result['small_parameter_census']['census_counts'],
        new_cycles=result['small_parameter_census']['new_normalized_summary']['counts']), sort_keys=True))


if __name__ == '__main__':
    main()
