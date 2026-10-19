#!/usr/bin/env python3
"""Independent exact C008 relation-lattice and sorted-residue replay.

Finite corroboration of written results, never universal cycle exclusion.
No imports from the C008 author checker; all arithmetic is exact.
"""
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd, lcm
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'C001/actual_cycles.json'
CENSUS = HERE.parent / 'C007/height_denominator_audit.json'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def order(x, modulus):
    value = x % modulus
    exponent = 1
    while value != 1:
        value = value*x % modulus
        exponent += 1
        require(exponent < modulus, 'unit order exceeded finite group size')
    return exponent


def relation(modulus):
    n = order(2, modulus)
    binary = {pow(2, j, modulus): j for j in range(n)}
    b, value = 1, 3 % modulus
    while value not in binary:
        b += 1
        value = value*3 % modulus
        require(b < modulus, 'quotient order failed')
    a = binary[value]
    e = gcd(gcd(n, a), b)
    ternary_order = order(3, modulus)
    require((e == 1) == (lcm(n, ternary_order) == n*b), 'Smith/cyclicity comparison')
    cells = 0
    for m in range(2*b):
        for A in range(2*n):
            residue_relation = pow(2, A, modulus) == pow(3, m, modulus)
            lattice_relation = m % b == 0 and (A-a*(m//b)) % n == 0
            require(residue_relation == lattice_relation, 'relation lattice membership')
            if residue_relation:
                require(A % e == 0 and m % e == 0, 'common coordinate divisor')
            cells += 1
    return dict(d=modulus, order_two=n, a=a, b=b, e=e,
                group_size=n*b, group_exponent=lcm(n, ternary_order), finite_cells=cells)


def bezout(x, y):
    a, b, u, v, r, s = x, y, 1, 0, 0, 1
    while b:
        k = a//b
        a, b, u, v, r, s = b, a-k*b, r, s, u-k*r, v-k*s
    require(a == 1 and u*x+v*y == 1, 'coprime Bezout')
    return u, v


def inspect(q, states, lattice):
    require(q > 0 and gcd(q, 6) == 1, 'parameter domain')
    n = tuple(states)
    require(n and n[0] == min(n) and len(set(n)) == len(n), 'primitive cycle orientation')
    a, C, A = [], 0, 0
    for x, y in zip(n, n[1:]+n[:1]):
        require(x > 0 and gcd(x, 6*q) == 1, 'odd reduced numerator')
        value, exponent = 3*x+q, 0
        while value % 2 == 0:
            value //= 2
            exponent += 1
        require(value == y and exponent >= 1, 'raw odd arrow')
        a.append(exponent)
        C = 3*C+2**A
        A += exponent
    m, L = len(n), n[0]
    D = 2**A-3**m
    require(D > 0 and q == D//gcd(C, D) and L == C//gcd(C, D), 'reduced denominator')
    heights = []
    for x in n:
        h = 0
        while 2**(h+1)*L <= x:
            h += 1
        heights.append(h)
    z = [Fraction(x, 2**h) for x, h in zip(n, heights)]
    indices = sorted(range(m), key=z.__getitem__)
    require(len(set(z)) == m, 'distinct normalized states')
    images = [3*z[i]+Fraction(q, 2**heights[i]) for i in range(m)]
    ordered = q <= L and all(images[i] < images[j] for i, j in zip(indices, indices[1:]))
    result = dict(q=q, L=L, m=m, A=A, B=max(heights), ordered=ordered,
                  totals_gcd=gcd(A, m), fixed=m == 1)
    if q > 1:
        e = lattice[q]['e']
        require(A % e == 0 and m % e == 0, 'actual-cycle lattice divisor')
        if gcd(A, m) == 1:
            u, v = bezout(m, A)
            t = pow(2, u, q)*pow(3, v, q) % q
            require(pow(t, m, q) == 2 % q and pow(t, A, q) == 3 % q, 'generator powers')
            require(e == 1 and order(t, q) == lattice[q]['group_size'], 'cyclicity conclusion')
            result.update(generator=t, generator_order=order(t, q))
        if ordered:
            require(gcd(A, m) == 1, 'ordered coprime totals')
            for j, i in enumerate(indices):
                residue = n[i]*pow(2, -heights[i], q) % q
                require(residue == L*pow(t, j, q) % q, 'sorted normalized progression')
                require(n[i] % q == L*pow(t, j+m*heights[i], q) % q, 'raw lifted rank')
            if m > 1:
                require(order(t, q) >= 4, 'short residue period')
            require(all(q % d for d in (35, 65, 91)), 'ordered forbidden divisor')
    else:
        require(all(x % q == 0 for x in n), 'sole q1 residue')
    return result


def report():
    require(not sys.flags.optimize, 'optimized Python unsupported')
    lattice = {d: relation(d) for d in range(5, 1001) if gcd(d, 6) == 1}
    for d, expected in {35: (12, 10, 2, 2), 65: (12, 4, 4, 4), 91: (12, 0, 6, 6)}.items():
        r = lattice[d]
        require(tuple(r[k] for k in ('order_two', 'a', 'b', 'e')) == expected, 'explicit forbidden modulus')
    raw = json.loads(SOURCE.read_text())['cycles']
    cycles = {(r['reduced_denominator'], tuple(r['primitive_states'])) for r in raw}
    additions = json.loads(CENSUS.read_text())['small_parameter_census']['new_normalized_cycles']
    cycles.update((r['q'], tuple(r['states'])) for r in additions)
    require(len(cycles) == 1185 and all(q == 1 or q in lattice for q, _ in cycles), 'source coverage')
    rows = [inspect(q, n, lattice) for q, n in sorted(cycles)]
    count = Counter()
    for r in rows:
        count['primitive_normalized_cycles'] += 1
        count['raw_odd_arrows'] += r['m']
        count['q_gt_one_states'] += r['m'] if r['q'] > 1 else 0
        count['q_gt_one_nonfixed_states'] += r['m'] if r['q'] > 1 and not r['fixed'] else 0
        count['ordered_including_fixed_point'] += r['ordered']
        count['ordered_nonfixed'] += r['ordered'] and not r['fixed']
        count['unordered_q_le_L_noncoprime_totals'] += not r['ordered'] and r['q'] <= r['L'] and r['totals_gcd'] > 1
        count['coprime_totals'] += r['totals_gcd'] == 1
    controls = {}
    for d in (35, 65, 91):
        controls[str(d)] = [r for r in rows if r['q'] % d == 0]
        require(controls[str(d)] and all(r['L'] < r['q'] for r in controls[str(d)]), 'forbidden-factor controls remain outside order domain')
    forbidden = [d for d, r in lattice.items() if r['e'] > 1]
    minimal = [d for d in forbidden if not any(d % c == 0 for c in forbidden if c < d)]
    return dict(status='PASS', scope='Finite independent replay of exact written lattice and progression claims; no Hall or q1 exclusion proof.',
        counts=dict(sorted(count.items())), moduli_checked=len(lattice), maximum_modulus=1000,
        finite_relation_cells=sum(r['finite_cells'] for r in lattice.values()),
        lattice_rows=list(lattice.values()), minimal_forbidden_moduli_through_1000=minimal,
        forbidden_factor_actual_cycles=controls,
        ordered_progression_cases=[r for r in rows if r['ordered']],
        source_sha256={str(p.relative_to(HERE.parents[2])): sha256(p.read_bytes()).hexdigest()
                       for p in (Path(__file__), SOURCE, CENSUS)})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = report()
    target = HERE/'residue_spectrum_audit.json'
    if args.write:
        target.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(json.loads(target.read_text()) == result, 'stored receipt mismatch')
    print(json.dumps({k: result[k] for k in ('status', 'counts', 'moduli_checked', 'finite_relation_cells', 'minimal_forbidden_moduli_through_1000')}))


if __name__ == '__main__':
    main()
