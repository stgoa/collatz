#!/usr/bin/env python3
"""Exact first-return discrimination on all stored reduced positive odd cycles.

No seeds or new cycle words are searched. Every segment retains its complement,
exact valuation cylinder, and the full primitive cycle. Open q1 paths are
separate controls and are never counted as cycles.
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
C007 = HERE.parent/'C007/height_denominator_audit.json'
FIXTURES = ROOT/'experiments/phase6/cycle_fixtures.json'


def require(test, message):
    if not test:
        raise ValueError(message)


def fraction(value):
    return [value.numerator, value.denominator]


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def step(n, q):
    require(type(n) is int and n > 0 and n % 2 and type(q) is int and
            q > 0 and gcd(q, 6) == 1, 'invalid positive raw odd input')
    value = 3*n+q
    a = (value & -value).bit_length()-1
    return value >> a, a


def word_data(word):
    require(all(type(a) is int and a >= 1 for a in word), 'invalid positive valuations')
    A, C = 0, 0
    for a in word:
        C = 3*C+2**A
        A += a
    return A, C, 2**A-3**len(word)


def certificate(q, states):
    n = list(states)
    require(n and len(set(n)) == len(n), 'cycle must be nonempty and simple')
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
    shifts = sorted({(successor[j]-j) % m for j in range(m)})
    rotation = len(shifts) == 1
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
        normalized_successor=successor, normalized_shifts=shifts,
        normalized_images_increasing=monotone, q_at_most_L=L >= q,
        ordered_domain=domain, nontrivial=m > 1)


def cylinder(word, q, observed_start):
    """Check each prefix residue implied by the full exact valuation cylinder."""
    S, C, _ = word_data(word)
    modulus = 2**(S+1)
    residue = ((2**S-q*C)*pow(3**len(word), -1, modulus)) % modulus
    require(observed_start % modulus == residue, 'observed segment misses its cylinder')
    prefix = []
    for j in range(1, len(word)+1):
        Sj, Cj, _ = word_data(word[:j])
        value = 3**j*residue+q*Cj
        require(value % 2**(Sj+1) == 2**Sj, 'endpoint cylinder loses odd intermediate prefix')
        prefix.append(dict(length=j, A=Sj, C=Cj, odd_numerator_residue=2**Sj))
    return dict(modulus=modulus, residue=residue, checked_prefixes=len(prefix),
        all_prefix_checks_sha256=digest(prefix))


def segment_audit(row, i, k):
    n, h, a, q, m = (row[key] for key in ('states', 'heights', 'word', 'q', 'm'))
    j = (i+k) % m
    word = [a[(i+t) % m] for t in range(k)]
    S, C, D = word_data(word)
    require(2**S*n[j] == 3**k*n[i]+q*C, 'segment affine identity failed')
    complement = [a[(j+t) % m] for t in range(m-k)]
    T, E, _ = word_data(complement)
    _, Cr, Dr = word_data(word+complement)
    require(S+T == row['A'] and Dr == row['D'], 'complement totals failed')
    require(Cr == 3**(m-k)*C+2**S*E and Dr*n[i] == q*Cr,
            'segment/complement elimination failed')
    require(2**T*n[i] == 3**(m-k)*n[j]+q*E, 'complement affine identity failed')
    delta = n[j]-n[i]
    require(q*C-D*n[i] == 2**S*delta and delta % 2 == 0,
            'exact even displacement slack failed')
    cy = cylinder(word, q, n[i])
    direction = 'increase' if delta > 0 else 'decrease' if delta < 0 else 'fixed'
    return dict(start_index=i, end_index=j, start=n[i], end=n[j], length=k,
        word=word, A=S, C=C, D=D, slope=fraction(Fraction(3**k, 2**S)),
        intercept=fraction(Fraction(q*C, 2**S)), direction=direction,
        displacement=delta, even_displacement_units=delta//2,
        affine_contracting=D > 0, positive_height=k > 1,
        interior_heights=[h[(i+t) % m] for t in range(1,k)],
        cylinder=cy, complement=dict(length=m-k, A=T, C=E),
        rotated_full_intercept=Cr)


def excursions(row):
    n, h, m = row['states'], row['heights'], row['m']
    zeros = [i for i in range(m) if h[i] == 0]
    sorted_zeros = sorted(zeros, key=n.__getitem__)
    rank = {i:j for j,i in enumerate(sorted_zeros)}
    segments, permutation = [], [None]*len(zeros)
    composed_S, composed_C, composed_k = 0, 0, 0
    for t, i in enumerate(zeros):
        j = zeros[(t+1) % len(zeros)]
        k = (j-i) % m or m
        segment = segment_audit(row, i, k)
        require(all(value > 0 for value in segment['interior_heights']), 'not a first height-zero return')
        require(h[i] == h[j] == 0, 'return endpoints not height zero')
        segments.append(segment)
        permutation[rank[i]] = rank[j]
        composed_C = 3**k*composed_C+2**composed_S*segment['C']
        composed_S += segment['A']
        composed_k += k
    require((composed_k,composed_S,composed_C) == (m,row['A'],row['C']),
            'composing returns changes the full affine word')
    offsets = sorted({(v-j) % len(zeros) for j,v in enumerate(permutation)})
    current, seen = 0, set()
    while current not in seen:
        seen.add(current)
        current = permutation[current]
    require(current == 0 and len(seen) == len(zeros), 'induced return is not one cycle')
    return dict(cycle=row, chronological_zero_indices=zeros, sorted_zero_indices=sorted_zeros,
        sorted_zero_states=[n[i] for i in sorted_zeros], return_permutation=permutation,
        return_rank_offsets=offsets, return_is_rank_rotation=len(offsets) == 1,
        segments=segments, composed_intercept=composed_C)


def summarize(records):
    total, ordered, by_class = Counter(), Counter(), {}
    for record in records:
        row = record['cycle']
        label = 'ordered_q_at_most_L' if row['ordered_domain'] else 'q_at_most_L_unordered' if row['q_at_most_L'] else 'q_greater_than_L'
        local = by_class.setdefault(label, Counter())
        for target in (total, local, ordered if row['ordered_domain'] else None):
            if target is None:
                continue
            target['cycles'] += 1
            target['nontrivial_cycles'] += row['nontrivial']
            target['return_rank_rotation'] += record['return_is_rank_rotation']
            target['return_not_rank_rotation'] += not record['return_is_rank_rotation']
            target['wide_cycles'] += row['B'] > 0
            for seg in record['segments']:
                target['segments'] += 1
                target['segments_'+seg['direction']] += 1
                target['contracting_segments'] += seg['affine_contracting']
                target['expanding_segments'] += not seg['affine_contracting']
                target['positive_height_segments'] += seg['positive_height']
                target['prefix_cylinder_checks'] += seg['length']
                if seg['positive_height']:
                    target['positive_'+seg['direction']] += 1
                    target['positive_contracting'] += seg['affine_contracting']
                    target['positive_expanding'] += not seg['affine_contracting']
                    target['positive_contracting_increase'] += seg['affine_contracting'] and seg['direction']=='increase'
    return dict(all=dict(sorted(total.items())), ordered=dict(sorted(ordered.items())),
                domain_partition={k:dict(sorted(v.items())) for k,v in sorted(by_class.items())})


def existing_audit():
    source = json.loads(ACTUAL.read_text())
    c007 = json.loads(C007.read_text())
    fixtures = json.loads(FIXTURES.read_text())['cycles']
    require(len(source['cycles']) == 2459 and len(fixtures) == 11, 'source coverage changed')
    unique, source_index, arrows, scaled = {}, {}, 0, 0
    for raw in source['cycles']:
        q, n, d = raw['reduced_denominator'], raw['primitive_states'], raw['d']
        row = certificate(q,n)
        scale = d//q
        require(d % q == 0 and raw['states'] == [scale*x for x in n] and raw['word'] == row['word'],
                'source scaling or valuation failed')
        for i,x in enumerate(raw['states']):
            require(step(x,d) == (raw['states'][(i+1)%len(n)],row['word'][i]), 'source raw arrow failed')
        unique[q,tuple(n)] = row
        source_index[d,tuple(raw['states'])] = row
        arrows += len(n)
        scaled += scale > 1
    require(len(unique) == 1184 and arrows == 36912 and scaled == 1275, 'original source counts changed')
    additions = c007['small_parameter_census']['new_normalized_cycles']
    for raw in additions:
        row = certificate(raw['q'],raw['states'])
        unique[row['q'],tuple(row['states'])] = row
    require(len(additions)==1 and len(unique)==1185,'C007 addition changed')
    controls = []
    for i,fixture in enumerate(fixtures):
        row = source_index[fixture['d'],tuple(fixture['states'])]
        require(row['word'] == fixture['valuations'], 'fixture valuations changed')
        controls.append(dict(fixture_id=i+1,source_fixture=fixture,
            scale=fixture['d']//row['q'], normalized_cycle=excursions(row)))
    records = [excursions(row) for row in sorted(unique.values(),key=lambda r:(r['q'],r['L']))]
    metrics = summarize(records)
    require(metrics['ordered']['cycles']==52 and metrics['ordered']['return_not_rank_rotation']==12,
            'ordered core order counts changed')
    require(metrics['ordered']['segments']==177 and metrics['ordered']['positive_height_segments']==60,
            'ordered segment coverage changed')
    return dict(source_cycles=2459,source_parameters=len({r['d'] for r in source['cycles']}),
        scaled_source_instances=scaled,source_raw_arrows=arrows,normalized_replay_arrows=arrows,
        C007_new_distinct_cycles=1,counts=metrics,fixture_controls=controls,cycles=records)


def counterexamples(existing):
    index={(r['cycle']['q'],r['cycle']['L']):r for r in existing['cycles']}
    keys=[(13,283),(13,251),(5,19),(5,347),(233,1907),(83,157)]
    chosen=[index[key] for key in keys]
    core=chosen[0]
    require(core['sorted_zero_states']==[283,373,431,493] and
        core['return_permutation']==[2,0,3,1] and not core['return_is_rank_rotation'],
        'small core order-loss control changed')
    ordered_sorted=sorted([r for r in existing['cycles'] if r['cycle']['ordered_domain']],
        key=lambda r:(r['cycle']['m'],r['cycle']['q'],r['cycle']['L']))
    require(next(r for r in ordered_sorted if not r['return_is_rank_rotation'])==core,
        'minimality within the finite stored census changed')
    mixed=chosen[1]['segments']
    require(any(s['positive_height'] and not s['affine_contracting'] and s['direction']=='increase' for s in mixed)
        and any(s['positive_height'] and s['affine_contracting'] and s['direction']=='decrease' for s in mixed),
        'mixed positive excursion control changed')
    for r in (chosen[3],chosen[4]):
        require(r['cycle']['ordered_domain'] and not r['return_is_rank_rotation'], 'known core control changed')
    require(any(s['start']==277 and s['end']==283 and s['slope']==[27,32]
        and s['affine_contracting'] for s in chosen[5]['segments']),
        'contracting but increasing excursion control changed')
    return dict(cases=chosen,
        refuted=['Every positive-height excursion in an ordered actual cycle descends.',
                 'Every positive-height excursion in an ordered actual cycle has contracting affine slope.',
                 'Contracting affine slope forces the actual excursion endpoint to decrease.',
                 'The first-return permutation on sorted height-zero states remains a rank rotation.'],
        scope='Exact counterexamples concern the whole3x+q ordered class. Their q>1 denominators do not refute a q1-specific theorem. The first order-loss witness is minimal only by (period,q,L) within the stored cycle sample.')


def open_q1_controls():
    specs=[dict(L=7,states=[7,11,17,13],start=1,end=3),
           dict(L=11,states=[19,29,11],start=0,end=2)]
    result=[]
    for spec in specs:
        n,L=spec['states'],spec['L']
        require(min(n)>=L and L%2==1,'open path threshold invalid')
        word=[]
        for i in range(len(n)-1):
            nxt,a=step(n[i],1)
            require(nxt==n[i+1],'open q1 raw arrow failed')
            word.append(a)
        h=[(x//L).bit_length()-1 for x in n]
        i,j=spec['start'],spec['end']
        require(h[i]==h[j]==0 and all(t>0 for t in h[i+1:j]),'open first-return condition failed')
        S,C,D=word_data(word[i:j])
        require(2**S*n[j]==3**(j-i)*n[i]+C,'open segment affine equation failed')
        B=max(h)
        order=sorted(range(len(n)),key=lambda k:n[k]<<(B-h[k]))
        F=[(3*x+1)<<(B-k) for x,k in zip(n,h)]
        require(all(F[order[t]]<F[order[t+1]] for t in range(len(n)-1)),
                'open q1 pair order control failed')
        require(step(n[-1],1)[0]!=n[0],'open control accidentally closes')
        result.append(dict(**spec,q=1,word=word,heights=h,segment_word=word[i:j],
            length=j-i,A=S,C=C,D=D,slope=fraction(Fraction(3**(j-i),2**S)),
            displacement=n[j]-n[i],cylinder=cylinder(word[i:j],1,n[i]),
            all_listed_images_increasing_in_normalized_order=True,closed_cycle=False,
            next_state=step(n[-1],1)[0]))
    require(result[0]['displacement']==2 and result[1]['displacement']==-8,'open directions changed')
    return dict(cases=result,scope='These are finite q1 paths with positive-height first returns and exact valuation cylinders. They do not close and are not evidence for an extra cycle. They show that local excursion legality, pair image order and integer slack permit both directions; full cyclic compatibility remains necessary.')


def rejection_controls():
    probes=[lambda:certificate(1,[1,1]),lambda:certificate(1,[7,11,17,13]),
            lambda:certificate(5,[38,62,98]),lambda:certificate(3,[1]),
            lambda:word_data([0,2]),lambda:cylinder([1,2],1,13)]
    count=0
    for probe in probes:
        try:
            probe()
        except ValueError:
            count+=1
        else:
            raise ValueError('invalid control was accepted')
    return dict(rejected=count,scope='Repeated states, open paths mislabeled cycles, even scaling, unsupported q, nonpositive valuations and a wrong cylinder residue are rejected.')


def report():
    existing=existing_audit()
    return dict(schema='C009-excursions-v1',
        status='Exact first-return/complement identities and counterexamples to two compression shortcuts; no new denominator-one exclusion.',
        clock='Primitive positive raw odd-only cycles without an absorber. q is reduced; source scalings are checked separately.',
        source_sha256={'check_excursions.py':sha256(Path(__file__).read_bytes()).hexdigest(),
            'C001/actual_cycles.json':sha256(ACTUAL.read_bytes()).hexdigest(),
            'C007/height_denominator_audit.json':sha256(C007.read_bytes()).hexdigest(),
            'phase6/cycle_fixtures.json':sha256(FIXTURES.read_bytes()).hexdigest()},
        existing=existing,counterexamples=counterexamples(existing),
        open_q1_controls=open_q1_controls(),rejection_controls=rejection_controls(),
        scope='All1185 stored normalized cycles and all11 fixtures are replayed. No new seed census or profile grid is run. Finite counts are not universal classifications. Endpoint compression is exact and retains prefix valuation cylinders, but its elimination returns the original closure equation and its core need not preserve circular order.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    result=report()
    path=HERE/'excursions_audit.json'
    if args.write:
        path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else:
        require(path.exists() and json.loads(path.read_text())==result,'receipt differs from exact recomputation')
    print(json.dumps(dict(status='PASS',mode='write' if args.write else 'replay',
        counts=result['existing']['counts'],controls=len(result['existing']['fixture_controls']),
        rejection_controls=result['rejection_controls']['rejected']),sort_keys=True))


if __name__=='__main__':
    main()
