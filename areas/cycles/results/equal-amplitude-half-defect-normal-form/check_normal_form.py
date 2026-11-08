#!/usr/bin/env python3
"""Exact finite checks of equal-amplitude half-defect normalization."""

import argparse
import json
from itertools import combinations, product
from math import gcd
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def intercept(word):
    value, total = 0, 0
    for a in word:
        value = 3*value+(1 << total)
        total += a
    return value


def check_pair(u, v):
    u, v = tuple(u), tuple(v)
    n = len(u)
    changed = [i for i in range(n) if u[i] != v[i]]
    require(len(changed) == 2, 'expected two changes')
    i, h = changed
    k = abs(v[i]-u[i])
    require(abs(v[h]-u[h]) == k and 1 <= k <= 12, 'wrong amplitude')
    require(min(u+v) >= 1, 'nonpositive letter')
    full_word = u+v
    total = sum(full_word)
    require(total % 2 == 0, 'odd combined total')
    S = total//2
    P = (1 << S)+3**n
    g = gcd(intercept(full_word), P)
    offset = 0
    if (v[i]-u[i])*(v[h]-u[h]) > 0:
        if v[i] < u[i]:
            u, v = v, u
            offset += n
        r = i+1
        U, V = u[r:]+v[:r], v[r:]+u[:r]
        offset += r
    else:
        U, V = u, v
    rotated = full_word[offset:]+full_word[:offset]
    require(U+V == rotated, 'normalization is not a rotation')
    require(sum(U) == sum(V) == S, 'normalization is not balanced')
    require(gcd(intercept(U+V), P) == g, 'rotation changed gcd')
    a, b = [i for i in range(n) if U[i] != V[i]]
    if V[a] < U[a]:
        U, V = V, U
    require(V[a] == U[a]+k and V[b] == U[b]-k, 'incorrect transfer')
    middle = U[a+1:b]
    c = S-sum(middle)
    r = n-len(middle)-1
    require(r >= 1 and c >= k+r+1, 'fillability failure')
    F = intercept(middle+(c,))
    prefix = sum(U[:a+1])
    difference = ((1 << k)-1)*(1 << prefix)*3**(n-1-b)*F
    require(intercept(V)-intercept(U) == difference, 'plateau identity')
    require(g == gcd(((1 << k)-1)*F, P), 'middle-intercept gcd')
    require(g != P, 'claimed full-factor exclusion failed')
    if (1 << S) > 3**n:
        require(g < (1 << S), 'half bound failed')
    return dict(u=list(u), v=list(v), normalized_U=list(U), normalized_V=list(V),
                k=k, n=n, S=S, plus_factor=P, plus_gcd=g,
                near_critical=(1 << (2*S)) > 3**(2*n)
                    and (1 << (2*S)) < 2*3**(2*n),
                cyclotomic_index=gcd(2*S,2*n))


def compute():
    counts = dict(exhaustive_pairs=0, additional_balanced_pairs=0,
                  equal_sign_pairs=0, opposite_sign_pairs=0)
    per_k = {str(k):0 for k in range(1,13)}
    for n in range(2,6):
        for u in product((1,2,3), repeat=n):
            for i,h in combinations(range(n),2):
                for k in range(1,13):
                    for first,second in product((-1,1), repeat=2):
                        v = list(u)
                        v[i] += first*k
                        v[h] += second*k
                        if min(v) < 1:
                            continue
                        check_pair(u,v)
                        counts['exhaustive_pairs'] += 1
                        counts['equal_sign_pairs' if first == second else 'opposite_sign_pairs'] += 1
                        per_k[str(k)] += 1
    for k in range(1,13):
        for a,b in product(range(1,4), repeat=2):
            for middle in ((),(1,),(2,1),(3,1,2)):
                u = (a,)+middle+(k+b,)
                v = (a+k,)+middle+(b,)
                check_pair(u,v)
                counts['additional_balanced_pairs'] += 1
                per_k[str(k)] += 1
    examples = [check_pair((1,1,1,1,4),(2,1,1,1,3)),
                check_pair((1,1,1,1,3),(2,1,1,2,3))]
    require(all(row['near_critical'] and row['cyclotomic_index'] == 2 for row in examples),
            'named examples are not near-critical index-2 words')
    require(examples[0]['v'][0] != examples[0]['u'][-1]
            and examples[0]['v'][-1] != examples[0]['u'][0],
            'balanced example accidentally swaps endpoint letters')
    require(all(b-a == 1 for a,b in zip(examples[1]['u'],examples[1]['v']) if a != b),
            'second example is not two equal increases')
    return dict(scope=dict(length_min=2, length_max=5, alphabet=[1,2,3],
                           amplitude_min=1, amplitude_max=12),
                counts=counts, checked_pairs_per_amplitude=per_k, examples=examples)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result = compute()
    receipt = Path(__file__).with_suffix('.json')
    if args.write_receipt:
        receipt.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else:
        require(receipt.exists(), 'Missing receipt.')
        require(json.loads(receipt.read_text()) == result, 'Receipt mismatch.')
    print(json.dumps(result,sort_keys=True))


if __name__ == '__main__':
    main()
