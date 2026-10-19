#!/usr/bin/env python3
"""Replay three actual-cycle obstructions to termwise defect divisibility."""
import argparse
from hashlib import sha256
import json
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = HERE.parent/'C001/actual_cycles.json'


def require(value, message):
    if not value:
        raise ValueError(message)


def data(word):
    p = [0]
    for a in word:
        require(type(a) is int and a > 0, 'invalid valuation')
        p.append(p[-1]+a)
    c = sum(3**(len(word)-1-j)*2**p[j] for j in range(len(word)))
    return p, c, 2**p[-1]-3**len(word)


def case(word, shift, expected_q, expected_g, expected_pieces):
    m = len(word)
    rotated = word[shift:]+word[:shift]
    p, c, d = data(word)
    v, other, other_d = data(rotated)
    g = gcd(c, d)
    require(d > 0 and other_d == d and g == expected_g and d//g == expected_q,
            'cycle arithmetic changed')
    terms = [3**(m-1-j)*(2**v[j]-2**p[j]) for j in range(m)]
    prefix_difference = [v[j]-p[j] for j in range(m)]
    groups, j = [], 0
    while j < m:
        end = j+1
        while end < m and prefix_difference[end] == prefix_difference[j]:
            end += 1
        if prefix_difference[j]:
            value = sum(terms[j:end])
            groups.append(dict(start=j, stop_exclusive=end,
                prefix_difference=prefix_difference[j], value=value, residue=value % g))
        j = end
    require([row['value'] for row in groups] == expected_pieces, 'plateau values changed')
    require(sum(terms) == other-c == sum(expected_pieces) and (other-c) % g == 0,
            'full difference is not divisible by the cycle gcd')
    require(all(row['residue'] != 0 for row in groups), 'termwise counterexample failed')
    intercepts = [data(word[j:]+word[:j])[1] for j in range(m)]
    require(all(c_i % g == 0 for c_i in intercepts), 'inexact numerator reduction')
    states = [c_i//g for c_i in intercepts]
    require(len(set(states)) == m and all(n > 0 and n % 2 for n in states),
            'cycle is not primitive positive odd')
    for j, n in enumerate(states):
        require(3*n+expected_q == 2**word[j]*states[(j+1) % m],
                'actual cycle arrow failed')
    source = json.loads(SOURCE.read_text())['cycles']
    require(any(raw['reduced_denominator'] == expected_q and
                any(raw['primitive_states'] == states[j:]+states[:j] for j in range(m))
                for raw in source), 'example missing from stored actual corpus')
    return dict(word=word, shift=shift, q=expected_q, g=g, C=c, D=d,
        states=states, mismatch_count=sum(a != b for a, b in zip(word, rotated)),
        prefix_difference=prefix_difference, plateaus=groups,
        intercept_difference=other-c, quotient=(other-c)//g)


def report():
    return dict(status='PASS', schema='C011-coupled-defects-v1',
        scope='Three exact actual-cycle counterexamples to termwise divisibility; no obstruction to coupled estimates is claimed.',
        source_sha256={str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                       for p in (Path(__file__), SOURCE)},
        cases=[case([2,4,3], 1, 97, 5, [36,64]),
               case([1,1,2,1,2,1,3,2], 3, 233, 7, [972,8352]),
               case([1,1,2,3,1,1,2,4], 1, 359, 73, [972,3888,1536,14336])])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = report()
    path = HERE/'coupled_defect_controls.json'
    if args.write:
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(json.loads(path.read_text()) == result, 'receipt mismatch')
    print(json.dumps(dict(status='PASS', mode='write' if args.write else 'replay',
        cases=[dict(q=r['q'], g=r['g'], mismatch_count=r['mismatch_count'],
                    residues=[x['residue'] for x in r['plateaus']]) for r in result['cases']])))


if __name__ == '__main__':
    main()
