#!/usr/bin/env python3
"""Exact checks for unequal-one-three-half-defect-exclusion."""

import argparse
import json
from itertools import combinations, product
from math import gcd
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def intercept(word, coefficients=None):
    c, total = 0, 0
    for i,a in enumerate(word):
        b = 1 if coefficients is None else coefficients[i]
        c = 3*c+b*(1 << total)
        total += a
    return c


def check_pair(original_u, original_v):
    u,v = tuple(original_u),tuple(original_v)
    n = len(u)
    require(min(u+v) >= 1, 'nonpositive letters')
    differences = [v[i]-u[i] for i in range(n) if u[i] != v[i]]
    require(sorted(abs(x) for x in differences) == [1,3], 'wrong amplitudes')
    combined = sum(u)+sum(v)
    require(combined % 2 == 0, 'odd total')
    S = combined//2
    P = (1 << S)+3**n
    initial_gcd = gcd(intercept(u+v),P)
    for cut_count in range(4):
        i,h = [t for t in range(n) if u[t] != v[t]]
        if abs(v[i]-u[i]) == 1 and v[h]-u[h] == 3:
            break
        r = i+1
        new_u,new_v = u[r:]+v[:r],v[r:]+u[:r]
        require(new_u+new_v == (u+v)[r:]+(u+v)[:r], 'incorrect cyclic cut')
        require(gcd(intercept(new_u+new_v),P) == initial_gcd, 'cut changed gcd')
        u,v = new_u,new_v
    else:
        raise RuntimeError('normalization did not terminate in four patterns')
    epsilon = v[i]-u[i]
    j = (epsilon+3)//2
    B = sum(u)
    require(S == B+j, 'wrong adjusted total')
    a,b = (2,3) if epsilon == -1 else (3,2)
    blocks = [0,0,0]
    prefix = 0
    for t,letter in enumerate(u):
        part = 0 if t <= i else 1 if t <= h else 2
        blocks[part] += 3**(n-1-t)*(1 << prefix)
        prefix += letter
    X,Y,Z = blocks
    difference = (1 << j)*intercept(u)-intercept(v)
    require((2 if epsilon == -1 else 1)*difference == a*X+b*Y-(1 << j)*a*Z,
            'cleared weighted difference identity')
    original_mask = tuple(b if i < t <= h else a for t in range(n))
    rotated = u[h+1:]+u[:h+1]
    mask = original_mask[h+1:]+original_mask[:h+1]
    M = intercept(rotated,mask)
    require(mask == (a,)*(n-h+i)+(b,)*(h-i), 'incorrect block ordering')
    p = sum(u[:h+1])
    require(3**(n-1-h)*(1 << p)*M == 3**n*a*Z+(1 << B)*(a*X+b*Y),
            'weighted rotation identity')
    require(gcd(M,P) == initial_gcd, 'weighted gcd identity')
    modified = rotated[:-1]+(rotated[-1]+j,)
    require(sum(modified) == S and intercept(modified,mask) == M,
            'last-valuation adjustment')
    require(modified[-1] >= j+1, 'last valuation too small')
    require(M % P != 0, 'plus factor divides masked intercept')
    if (1 << S) > 3**n:
        require(initial_gcd < (1 << S), 'half bound fails')
    return dict(original_u=list(original_u), original_v=list(original_v),
                normalized_u=list(u),normalized_v=list(v), epsilon=epsilon,
                j=j,mask=list(mask),n=n,S=S,plus_factor=P,plus_gcd=initial_gcd,
                near_critical=3**(2*n) < (1 << (2*S)) < 2*3**(2*n),
                cyclotomic_index=gcd(2*S,2*n))


def check_weighted_segments():
    tested,integral,zero_cuts = 0,0,0
    for n in range(2,6):
        for split in range(1,n):
            for a,b,j in ((2,3,1),(3,2,2)):
                mask = (a,)*split+(b,)*(n-split)
                for base_word in product((1,2,3),repeat=n):
                    word = base_word[:-1]+(base_word[-1]+j,)
                    C = intercept(word,mask)
                    denominator = 1 << sum(word)
                    for start in range(-16,0):
                        tested += 1
                        numerator = 3**n*start+C
                        if numerator % denominator:
                            continue
                        end = numerator//denominator
                        x = start
                        for letter,offset in zip(word,mask):
                            value = 3*x+offset
                            require(value % (1 << letter) == 0, 'nonintegral forced cut')
                            x = value//(1 << letter)
                            if x == 0:
                                zero_cuts += 1
                        require(x == end and end <= 0, 'forbidden signed crossing')
                        integral += 1
    x=-1
    control=[x]
    for offset in (3,2):
        require((3*x+offset) % 2 == 0, 'zero-interface control')
        x=(3*x+offset)//2
        control.append(x)
    require(control == [-1,0,1], 'wrong zero-interface control')
    require((3**2*(-1)+intercept((1,3),(3,2))) % (1 << 4) != 0,
            'adjusted zero-interface control became integral')
    return dict(tested_segments=tested,integral_segments=integral,
                zero_cuts=zero_cuts,unadjusted_control=control)


def compute():
    counts = {'epsilon_minus_one':0,'epsilon_plus_one':0}
    for n in range(2,6):
        for u in product((1,2,3,4),repeat=n):
            for i,h in combinations(range(n),2):
                for p,q in ((1,3),(3,1)):
                    for first,second in product((-1,1),repeat=2):
                        v = list(u)
                        v[i] += first*p
                        v[h] += second*q
                        if min(v) < 1:
                            continue
                        result = check_pair(u,v)
                        key = 'epsilon_minus_one' if result['epsilon'] == -1 else 'epsilon_plus_one'
                        counts[key] += 1
    examples = [check_pair((1,1,1,1,2),(2,1,1,4,2)),
                check_pair((2,1,1,1,2),(1,1,1,4,2))]
    require(all(row['near_critical'] and row['cyclotomic_index'] == 2 for row in examples),
            'named examples fail scope')
    controls = []
    for d in (5,7,13,61):
        numerator = -3+d
        v = (numerator & -numerator).bit_length()-1
        successor = numerator//(1 << v)
        require(successor > 0 and successor % 2 == 1 and v >= 1, 'sign-crossing control')
        controls.append(dict(d=d,start=-1,valuation=v,end=successor))
    return dict(scope=dict(length_min=2,length_max=5,alphabet=[1,2,3,4],amplitudes=[1,3]),
                pair_counts=counts,weighted_segments=check_weighted_segments(),
                examples=examples,controls=controls)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    result=compute()
    receipt=Path(__file__).with_suffix('.json')
    if args.write_receipt:
        receipt.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else:
        require(receipt.exists(),'Missing receipt.')
        require(json.loads(receipt.read_text()) == result,'Receipt mismatch.')
    print(json.dumps(result,sort_keys=True))


if __name__ == '__main__':
    main()
