#!/usr/bin/env python3
"""Exact C008 Hall discrimination on actual cycles and targeted word profiles.

No seed census is run. Most generated words are screened out by their exact
reduced denominator; retained words are realized as strict raw odd cycles.
Proper-divisor matching is explicitly distinct from full-denominator matching.
"""

import argparse
from collections import Counter
from hashlib import sha256
import json
from math import comb, gcd
from pathlib import Path
import sys

if sys.flags.optimize:
    raise SystemExit('FAIL: optimized Python is not supported')

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ACTUAL = HERE.parent/'C001/actual_cycles.json'
C007 = HERE.parent/'C007/height_denominator_audit.json'
FIXTURES = ROOT/'experiments/phase6/cycle_fixtures.json'


def require(test, message):
    if not test:
        raise ValueError(message)


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def step(n, q):
    require(type(n) is int and n > 0 and n % 2 and type(q) is int and
            q > 0 and gcd(q, 6) == 1, 'invalid positive raw odd input')
    value = 3*n+q
    a = (value & -value).bit_length()-1
    return value >> a, a


def word_data(word):
    require(word and all(type(a) is int and a >= 1 for a in word), 'invalid positive valuations')
    A, C = 0, 0
    for a in word:
        C = 3*C+2**A
        A += a
    return A, C, 2**A-3**len(word)


def certificate(q, states):
    n = list(states)
    require(n and len(set(n)) == len(n), 'cycle must be simple')
    start = n.index(min(n))
    n = n[start:]+n[:start]
    word = []
    for i, x in enumerate(n):
        target, a = step(x, q)
        require(target == n[(i+1) % len(n)] and gcd(x, q) == 1, 'reduced cycle arrow failed')
        word.append(a)
    A, C, D = word_data(word)
    g = gcd(C, D)
    require(D > 0 and D//g == q and C//g == n[0], 'exact reduced denominator failed')
    L, m = n[0], len(n)
    h = [(x//L).bit_length()-1 for x in n]
    B = max(h)
    Z = [x << (B-k) for x, k in zip(n, h)]
    F = [(3*x+q) << (B-k) for x, k in zip(n, h)]
    require(len(set(Z)) == m, 'mantissas not distinct')
    order = sorted(range(m), key=Z.__getitem__)
    rank = {i: j for j, i in enumerate(order)}
    successor = [rank[(i+1) % m] for i in order]
    monotone = all(F[order[j]] < F[order[j+1]] for j in range(m-1))
    rotation = len({(successor[j]-j) % m for j in range(m)}) == 1
    domain = L >= q and monotone
    if L >= q:
        require(monotone == rotation, 'image/rank order equivalence failed')
    c = [word[i]+h[(i+1) % m]-h[i] for i in range(m)]
    if domain:
        require(set(h) == set(range(B+1)), 'ordered cycle misses an intermediate height')
        require(gcd(A, m) == 1 and c == [(i+1)*A//m-i*A//m for i in range(m)],
                'ordered canonical mechanical code failed')
    return dict(q=q, m=m, A=A, C=C, D=D, numerator_gcd=g, states=n, word=word,
        L=L, H=max(n), B=B, heights=h, sorted_indices=order, normalized_word=c,
        ordered_domain=domain, nontrivial=m > 1, numerical_height_bound=B <= q-1,
        missing_intermediate_heights=sorted(set(range(B+1))-set(h)))


def realize(word):
    A, C, D = word_data(word)
    require(D > 0, 'word does not have a positive cycle')
    g = gcd(C, D)
    q, current = D//g, C//g
    n = []
    for a in word:
        n.append(current)
        current, actual_a = step(current, q)
        require(actual_a == a, 'realization lost exact valuation')
    require(current == n[0], 'realization did not close')
    return certificate(q, n)


def matching_audit(row, mode, modulus=None):
    q = row['q'] if modulus is None else modulus
    require(q > 0 and row['q'] % q == 0 and mode in ('raw', 'normalized'), 'invalid residue projection')
    graph = {h: set() for h in row['heights']}
    for n, h in zip(row['states'], row['heights']):
        residue = n % q if mode == 'raw' or q == 1 else n*pow(pow(2, h, q), -1, q) % q
        graph[h].add(residue)
        require(q == 1 or gcd(residue, q) == 1, 'residue is not a unit')
    owner = {}

    def augment(h, seen):
        for residue in sorted(graph[h]):
            if residue in seen:
                continue
            seen.add(residue)
            if residue not in owner or augment(owner[residue], seen):
                owner[residue] = h
                return True
        return False

    for h in sorted(graph):
        augment(h, set())
    require(len(set(owner.values())) == len(owner) and all(r in graph[h] for r, h in owner.items()),
            'matching assignment is invalid')
    complete = len(owner) == len(graph)
    S, T = set(graph)-set(owner.values()), set()
    todo = list(S)
    while todo:
        h = todo.pop()
        for residue in graph[h]:
            if residue in T:
                continue
            T.add(residue)
            if residue in owner and owner[residue] not in S:
                S.add(owner[residue])
                todo.append(owner[residue])
    hall = None
    if not complete:
        require(len(S) > len(T) and T == set().union(*(graph[h] for h in S)), 'invalid Hall deficit witness')
        hall = dict(heights=sorted(S), residues=sorted(T), deficit=len(S)-len(T))
    support = {}
    for h, residues in graph.items():
        for r in residues:
            support.setdefault(r, set()).add(h)
    overlap = any(len(levels) > 1 for levels in support.values())
    near = None
    if overlap and len(graph) <= 10:
        labels = sorted(graph)
        for mask in range(1, 1 << len(labels)):
            subset = [labels[j] for j in range(len(labels)) if mask >> j & 1]
            if len(subset) < 2:
                continue
            neighbors = set().union(*(graph[h] for h in subset))
            slack = len(neighbors)-len(subset)
            if near is None or slack < near['slack']:
                near = dict(heights=subset, residues=sorted(neighbors), slack=slack)
    return dict(mode=mode, modulus=q, full_reduced_denominator=q == row['q'],
        graph={str(h): sorted(rs) for h, rs in sorted(graph.items())}, complete=complete,
        assignment=[[h, r] for r, h in sorted(owner.items(), key=lambda pair: pair[1])],
        hall_deficit=hall, height_sets_overlap=overlap, disjoint_sets_make_matching_automatic=not overlap,
        near_subset=near, near_subset_scope='All subsets with at least two labels are inspected only when height sets overlap and there are at most ten labels; matching itself has no such cutoff.')


def bezout(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        quotient = old_r//r
        old_r, r = r, old_r-quotient*r
        old_s, s = s, old_s-quotient*s
        old_t, t = t, old_t-quotient*t
    require(old_r == 1, 'Bezout totals not coprime')
    return old_s, old_t


def progression_audit(row):
    require(row['ordered_domain'], 'progression audit requires order')
    q, m, A, L = row['q'], row['m'], row['A'], row['L']
    if q == 1:
        return dict(residue=0, scope='Modulus1 retains its one residue0; the fixed point is tested, not omitted.')
    u, v = bezout(m, A)
    t = pow(2, u, q)*pow(3, v, q) % q
    require(pow(t, m, q) == 2 % q and pow(t, A, q) == 3 % q, 'residue generator powers failed')
    for j, i in enumerate(row['sorted_indices']):
        n, h = row['states'][i], row['heights'][i]
        require(n*pow(pow(2, h, q), -1, q) % q == L*pow(t, j, q) % q,
                'normalized sorted residue progression failed')
        require(n % q == L*pow(t, j+m*h, q) % q, 'raw lifted-rank residue progression failed')
    period = next((k for k in range(1, m*(row['B']+1)+1) if pow(t, k, q) == 1), None)
    return dict(generator=t, bezout_m=u, bezout_A=v, period_within_lifted_rank_range=period,
        normalized_repeats=period is not None and period < m,
        scope='A null period means no return was found through m(B+1), not that the finite multiplicative order does not exist.')


def audit_rows(rows):
    counts, all_rows, nonautomatic, failures = Counter(), [], [], []
    for row in sorted(rows, key=lambda r: (r['q'], r['L'])):
        counts['primitive_cycles'] += 1
        counts['ordered_cycles_including_fixed_point'] += row['ordered_domain']
        counts['ordered_nontrivial_cycles'] += row['ordered_domain'] and row['nontrivial']
        counts['missing_intermediate_height_cycles'] += bool(row['missing_intermediate_heights'])
        matches = [matching_audit(row, mode) for mode in ('raw', 'normalized')]
        record = dict(cycle=row, matching=matches)
        if row['ordered_domain']:
            record['residue_progression'] = progression_audit(row)
        for match in matches:
            mode = match['mode']
            counts[mode+'_matching_passes'] += match['complete']
            counts[mode+'_overlap_cases'] += match['height_sets_overlap']
            counts[mode+'_ordered_overlap_cases'] += match['height_sets_overlap'] and row['ordered_domain']
            if match['near_subset'] and match['near_subset']['slack'] == 0:
                counts[mode+'_tight_subset_cases'] += 1
            if not match['complete']:
                failures.append(dict(cycle=row, matching=match))
        if any(x['height_sets_overlap'] for x in matches):
            nonautomatic.append(record)
        all_rows.append(record)
    return dict(counts=dict(sorted(counts.items())), nonautomatic_cases=nonautomatic,
        full_denominator_failures=failures, all_checked_rows_sha256=digest(all_rows))


def existing_audit():
    source = json.loads(ACTUAL.read_text())
    c007 = json.loads(C007.read_text())
    fixtures = json.loads(FIXTURES.read_text())['cycles']
    require(len(source['cycles']) == 2459 and len(fixtures) == 11, 'source coverage changed')
    unique, source_index, arrows, scaled = {}, {}, 0, 0
    for raw in source['cycles']:
        q, n, d = raw['reduced_denominator'], raw['primitive_states'], raw['d']
        row = certificate(q, n)
        scale = d//q
        require(d % q == 0 and raw['states'] == [scale*x for x in n] and raw['word'] == row['word'],
                'source scaling or valuation failed')
        for i, x in enumerate(raw['states']):
            require(step(x, d) == (raw['states'][(i+1) % len(n)], row['word'][i]), 'source raw arrow failed')
        unique[q, tuple(n)] = row
        source_index[d, tuple(raw['states'])] = row
        arrows += len(n)
        scaled += scale > 1
    require(len(unique) == 1184 and arrows == 36912, 'original distinct/arrow counts changed')
    additions = c007['small_parameter_census']['new_normalized_cycles']
    for raw in additions:
        row = certificate(raw['q'], raw['states'])
        unique[row['q'], tuple(row['states'])] = row
    require(len(additions) == 1 and len(unique) == 1185, 'C007 addition changed')
    controls = []
    for i, fixture in enumerate(fixtures):
        row = source_index[fixture['d'], tuple(fixture['states'])]
        require(row['word'] == fixture['valuations'], 'fixture valuations changed')
        controls.append(dict(fixture_id=i+1, fixture=fixture, cycle=row,
            matching=[matching_audit(row, mode) for mode in ('raw', 'normalized')]))
    result = audit_rows(unique.values())
    result.update(source_cycles=2459, source_parameters=len({r['d'] for r in source['cycles']}),
        scaled_source_instances=scaled, source_raw_arrows=arrows, normalized_replay_arrows=arrows,
        C007_new_distinct_cycles=1, fixture_controls=controls)
    return result, unique


def profile_totals():
    result = []
    small_q = [q for q in range(5, 32, 2) if q % 3]
    for m in range(2, 18):
        for A in range((3**m).bit_length(), 2*m):
            if gcd(A, m) != 1:
                continue
            D = 2**A-3**m
            divisors = [q for q in small_q if D % q == 0]
            anticipated = comb(A-1, m-1)//m
            if divisors and anticipated <= 500000:
                result.append(dict(m=m, A=A, D=D, small_divisors=divisors, anticipated_profiles=anticipated))
    return result


def height_profiles(c):
    h = [0]
    def visit():
        if len(h) == len(c):
            yield tuple(h)
            return
        for value in range(h[-1]+c[len(h)-1]):
            h.append(value)
            yield from visit()
            h.pop()
    yield from visit()


def targeted_profiles(previous):
    counts, summaries, retained = Counter(), [], {}
    stream = sha256()
    for spec in profile_totals():
        A, m = spec['A'], spec['m']
        c = [(i+1)*A//m-i*A//m for i in range(m)]
        local, actual_count = Counter(), 0
        for h in height_profiles(c):
            word = [c[i]+h[i]-h[(i+1) % m] for i in range(m)]
            actual_A, C, D = word_data(word)
            require(actual_A == A and D == spec['D'], 'profile totals changed')
            q = D//gcd(C, D)
            actual_count += 1
            stream.update(json.dumps([A, m, h, C, q], separators=(',', ':')).encode()+b'\n')
            if q > 31:
                local['screened_out_reduced_q_gt31'] += 1
                continue
            row = realize(word)
            require(row['q'] == q and row['m'] == m, 'retained profile reduction failed')
            k = q, tuple(row['states'])
            require(k not in retained, 'different canonical profiles duplicated a primitive cycle')
            retained[k] = row
            local['retained_primitive_actual_cycles'] += 1
            local['retained_raw_arrow_checks'] += m
            local['retained_ordered_cycles'] += row['ordered_domain']
        require(actual_count == spec['anticipated_profiles'], 'canonical profile count mismatch')
        local['profiles'] = actual_count
        counts.update(local)
        summaries.append(dict(**spec, counts=dict(sorted(local.items()))))
    require(counts['profiles'] == 946001 and len(summaries) == 17, 'targeted grid changed')
    result = audit_rows(retained.values())
    result.update(construction_counts=dict(sorted(counts.items())), totals=summaries,
        all_intercepts_sha256=stream.hexdigest(), retained_cycles=list(retained.values()),
        cycles_absent_from_existing=[r for k, r in retained.items() if k not in previous],
        scope='Enumerate legal positive canonical height profiles with no additional height cap. Instantiate and test only words whose exact reduced denominator is at most31. Words screened out by larger q are not counted as matching evidence. Coprime totals ensure primitive words; every retained raw arrow is checked. This finite construction does not classify untested totals.')
    return result


def projected_controls():
    words = [[1]*16+[11], [1,2,1,2,1,2,2,1,2,1,1,1,1,1,4,2,2],
             [1,1,1,3,1,1,1,3,1,1,1,3,1,3,1,1,3]]
    results = []
    for word in words:
        row = realize(word)
        require(row['q'] == 5077565 and row['ordered_domain'] and row['m'] == 17 and row['A'] == 27,
                'projected control domain failed')
        full = [matching_audit(row, mode) for mode in ('raw', 'normalized')]
        projected = [matching_audit(row, mode, 5) for mode in ('raw', 'normalized')]
        require(all(x['complete'] for x in full) and not projected[0]['complete'],
                'proper-divisor raw Hall obstruction failed')
        require(projected[1]['complete'] == (len(results) == 2),
                'proper-divisor normalized Hall control failed')
        results.append(dict(cycle=row, full_denominator_matching=full,
            proper_divisor_5_matching=projected, residue_progression=progression_audit(row)))
    require(results[0]['cycle']['L'] == 129009091 and results[0]['cycle']['B'] == 9,
            'ten-height control changed')
    second = results[1]['cycle']
    require(second['L'] == 446400719 and second['B'] == 3 and second['numerator_gcd'] == 1,
            'four-height control changed')
    require(second['heights'] == [0,0,0,0,0,0,0,0,0,0,0,1,2,2,3,0,0], 'four-height geometry changed')
    third = results[2]['cycle']
    require(third['L'] == 365289811 and third['B'] == 2 and third['numerator_gcd'] == 1,
            'three-height raw control changed')
    require(third['heights'] == [0,0,1,1,0,0,1,2,0,1,1,2,1,1,0,0,1],
            'three-height raw control geometry changed')
    require(results[2]['proper_divisor_5_matching'][0]['graph'] == {'0': [1,4], '1': [1,4], '2': [1,4]},
            'three-height raw Hall graph changed')
    return dict(cases=results, scope='These are actual primitive ordered cycles. Both full-q graphs match in all three cases. Projection to the proper divisor5 fails in both graphs for the first two controls; the four-height second case has a subset Hall deficit despite four available units. The third control has only three heights: its raw projected graph fails, while its normalized projected graph matches. These refute prime-projection shortcuts, not full-denominator matching or the normalized B<=2 theorem.')


def report():
    existing, previous = existing_audit()
    return dict(schema='C008-height-matching-v1',
        status='Finite Hall tests and exact proper-divisor counterexamples; full-denominator matching remains an open mechanism.',
        clock='Simple positive raw odd-only cycles without an absorber, at their reduced denominator. Modulus1 has residue0 and is included.',
        source_sha256={'check_height_matching.py': sha256(Path(__file__).read_bytes()).hexdigest(),
            'C001/actual_cycles.json': sha256(ACTUAL.read_bytes()).hexdigest(),
            'C007/height_denominator_audit.json': sha256(C007.read_bytes()).hexdigest(),
            'phase6/cycle_fixtures.json': sha256(FIXTURES.read_bytes()).hexdigest()},
        existing=existing, targeted_profiles=targeted_profiles(previous), projected_controls=projected_controls(),
        scope='Complete matchings are independently checked assignments; failures include exact Hall subsets. Disjoint height residue sets are separated as automatic passes. No finite pass proves full matching, the numerical height bound, or the exclusion of nontrivial denominator1 cycles.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = report()
    path = HERE/'height_matching_audit.json'
    if args.write:
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(path.exists() and json.loads(path.read_text()) == result, 'receipt differs from exact recomputation')
    print(json.dumps(dict(status='PASS', mode='write' if args.write else 'replay',
        existing=result['existing']['counts'], construction=result['targeted_profiles']['construction_counts'],
        retained=result['targeted_profiles']['counts'],
        new_retained=len(result['targeted_profiles']['cycles_absent_from_existing'])), sort_keys=True))


if __name__ == '__main__':
    main()
