#!/usr/bin/env python3
"""Exact finite counterexample to unrestricted transposition plus exclusion."""

import argparse
import json
from math import gcd
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def intercept(word):
    c, total = 0, 0
    for letter in word:
        c = 3*c + (1 << total)
        total += letter
    return c


def compute():
    d = (1 << 14)-1
    x = -63
    path, middle = [], []
    for index in range(187):
        require(x != 453291, ('target reached too early', index))
        require(x % 2 == 1, ('even path state', index, x))
        value = 3*x+d
        require(value != 0, ('zero on path', index))
        a = (abs(value) & -abs(value)).bit_length()-1
        y = value // (1 << a)
        require(a >= 1 and y % 2 == 1 and (1 << a)*y == value,
                ('illegal signed arrow', index))
        path.append(dict(start=x, valuation=a, end=y))
        middle.append(a)
        x = y
    require(x == 453291, ('wrong terminal source', x))
    require(3*x+d == (1 << 16)*21, 'wrong last arrow')
    path.append(dict(start=x, valuation=16, end=21))
    require(len(middle) == 187 and sum(middle) == 320, 'wrong middle word')

    u = [1] + middle + [15]
    v = [15] + middle + [1]
    w = u+v
    n, total = len(u), sum(u)
    require(n == 189 and total == 336 and sum(v) == total, 'wrong half dimensions')
    plus = (1 << total) + 3**n
    minus = (1 << total) - 3**n
    full_denominator = (1 << (2*total))-3**(2*n)
    c = intercept(w)
    f = intercept(middle+[16])
    require(d*f == 21*plus, 'signed path intercept identity')
    require(intercept(v)-intercept(u) == 2*d*f, 'transposition intercept identity')
    require(c == 3**n*intercept(u)+(1 << total)*intercept(v), 'concatenation identity')
    require(full_denominator == plus*minus and minus > 0, 'factorization')
    require(gcd(c,plus) == plus, 'plus factor does not cancel fully')
    require(gcd(c,minus) == 1, 'unexpected minus cancellation')
    require(gcd(c,full_denominator) == plus, 'wrong total cancellation')
    require(plus*plus > (1 << (2*total)), 'half bound not violated')
    require((1 << (2*total)) >= 2*3**(2*n), 'counterexample is near-critical')
    require(gcd(2*total,2*n) == 42, 'wrong cyclotomic index')

    mismatch_counts = [sum(w[i] != w[(i+shift) % len(w)] for i in range(len(w)))
                       for shift in range(1,len(w))]
    require(min(mismatch_counts) == 4, 'wrong rotation distance')
    require(all(count > 0 for count in mismatch_counts), 'word is not primitive')
    minimizing_shifts = [shift for shift,count in enumerate(mismatch_counts,1) if count == 4]
    require(minimizing_shifts == [189], 'unexpected minimizing shift')

    states = []
    for phase in range(len(w)):
        rotated = w[phase:]+w[:phase]
        phase_intercept = intercept(rotated)
        require(phase_intercept % plus == 0, ('nonintegral cycle state',phase))
        states.append(phase_intercept // plus)
    require(len(set(states)) == len(w), 'actual cycle is not primitive')
    for i,state in enumerate(states):
        successor = states[(i+1) % len(states)]
        require(state > 0 and state % 2 == 1, ('invalid positive cycle state',i))
        require(3*state+minus == (1 << w[i])*successor,
                ('wrong positive cycle arrow',i))
    return dict(signed_map_parameter=d, signed_path=path, middle_word=middle,
                half_u=u, half_v=v, word=w, n=n, B=total, m=len(w), A=sum(w),
                C=c, D=full_denominator, plus_factor=plus, minus_factor=minus,
                G=plus, reduced_denominator=minus, cyclotomic_index=42,
                rotation_distance=4, minimizing_shifts=minimizing_shifts,
                mismatch_counts=mismatch_counts, primitive=True,
                half_bound_violated=True, near_critical=False,
                positive_cycle_states=states)


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
    print(json.dumps({key:result[key] for key in
                      ('m','A','G','reduced_denominator','cyclotomic_index',
                       'rotation_distance','minimizing_shifts','primitive',
                       'half_bound_violated','near_critical')},sort_keys=True))


if __name__ == '__main__':
    main()
