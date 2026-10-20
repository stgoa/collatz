#!/usr/bin/env python3
"""Independent exact replay of C007's arithmetic obstruction examples."""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def inspect(q, states):
    n = tuple(states)
    require(n[0] == min(n) and len(set(n)) == len(n), 'orientation or simplicity')
    require(q > 0 and gcd(q, 6) == 1, 'denominator domain')
    a = []
    for x, y in zip(n, n[1:]+n[:1]):
        require(x > 0 and gcd(x, 6*q) == 1, 'numerator unit lemma')
        value = 3*x+q
        exponent = 0
        while value % 2 == 0:
            value //= 2
            exponent += 1
        require(value == y and exponent >= 1, 'exact raw odd arrow')
        a.append(exponent)
    L = n[0]
    h = []
    for x in n:
        height = 0
        while L*2**(height+1) <= x:
            height += 1
        h.append(height)
    z = [Fraction(x, 2**height) for x, height in zip(n, h)]
    c = [a[i]+h[(i+1) % len(n)]-h[i] for i in range(len(n))]
    P, C = 0, 0
    modular_arrows = 0
    for i, (x, height) in enumerate(zip(n, h)):
        require(P-height == sum(a[:i]), 'height telescoping')
        C += 3**(len(n)-1-i)*2**(P-height)
        if q > 1:
            mantissa = x*pow(pow(2, height, q), -1, q) % q
            expected = L*pow(3, i, q)*pow(pow(2, P, q), -1, q) % q
            require(mantissa == expected, 'normalized modular orbit')
            modular_arrows += 1
        P += c[i]
    D = 2**P-3**len(n)
    require(D > 0 and D*L == q*C and D//gcd(C, D) == q, 'weighted intercept')
    order = sorted(range(len(n)), key=z.__getitem__)
    F = [3*z[i]+Fraction(q, 2**h[i]) for i in range(len(n))]
    ordered = all(F[i] < F[j] for i, j in zip(order, order[1:]))
    if ordered and q <= L:
        for x, height in zip(n, h):
            if height:
                require(3*(x-2**height*L) > q*(2**height-1), 'min-height inequality')
    return dict(q=q, L=L, B=max(h), m=len(n), ordered=ordered,
                heights=h, normalized=z, sorted_indices=order,
                modular_arrows=modular_arrows)


def report():
    source_path = HERE.parent/'C001/actual_cycles.json'
    census_path = HERE/'height_denominator_audit.json'
    source = json.loads(source_path.read_text())
    census = json.loads(census_path.read_text())
    cycles = {(r['reduced_denominator'], tuple(r['primitive_states']))
              for r in source['cycles']}
    cycles.update((r['q'], tuple(r['states'])) for r in
                  census['small_parameter_census']['new_normalized_cycles'])
    records = [inspect(q, n) for q, n in sorted(cycles)]
    require(len(records) == 1185, 'combined coverage')
    witness = next(n for q, n in cycles if q == 5 and n[0] == 187)
    detail = inspect(5, witness)
    raw_sets, normalized_sets = {}, {}
    for n, h in zip(witness, detail['heights']):
        raw_sets.setdefault(h, set()).add(n % 5)
        normalized_sets.setdefault(h, set()).add(n*pow(pow(2, h, 5), -1, 5) % 5)
    require(detail['ordered'] and detail['B'] == 3, 'ordered residue witness')
    require(all(2 in raw_sets[h] for h in range(4)), 'reused raw residue')
    require(normalized_sets[0] & normalized_sets[2], 'reused normalized residues')
    second = next(n for q, n in cycles if q == 5 and n[0] == 347)
    second_detail = inspect(5, second)
    indices = second_detail['sorted_indices']
    first_gap = 2**second_detail['B']*(second_detail['normalized'][indices[1]]-
                                    second_detail['normalized'][indices[0]])/5
    require(second_detail['ordered'] and first_gap == Fraction(96, 5), 'rational rescaling')
    pair_checks = 0
    for q in range(1, 101, 2):
        if q % 3 == 0:
            continue
        for B in (q, q+1, q+20):
            L = 2*q+1
            r = q*2**B+1
            N = 2**B*L+r
            require(N % 2 and 0 < r < 2**B*L, 'relaxed top-height pair')
            require(3*r > q*(2**B-1), 'relaxed pair order')
            pair_checks += 1
    return dict(status='PASS', scope='Finite checks of written identities and exact obstructions; no proof of the height-denominator conjecture.',
        normalized_cycles=len(records), modular_arrows=sum(r['modular_arrows'] for r in records),
        residue_control=dict(q=5, L=187, B=3,
            raw_residues={str(h): sorted(s) for h, s in raw_sets.items()},
            normalized_residues={str(h): sorted(s) for h, s in normalized_sets.items()}),
        rational_rescaling_control=dict(reduced_q=5, L=347, B=3,
            additive_term_after_rescaling=1, first_scaled_gap=[96, 5],
            warning='Rational coordinates are not an integer denominator-one cycle.'),
        relaxed_pair_checks=pair_checks,
        relaxation_scope='Only the min/top pair inequalities; these pairs are not claimed to lie in cycles.',
        source_sha256={p.name: sha256(p.read_bytes()).hexdigest() for p in
            (Path(__file__), source_path, census_path, HERE/'HEIGHT_DENOMINATOR.md',
             HERE/'INDEPENDENT_ARITHMETIC.md')})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = report()
    target = HERE/'arithmetic_obstructions.json'
    if args.write:
        target.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(json.loads(target.read_text()) == result, 'receipt mismatch')
    print(json.dumps({k: result[k] for k in ('status', 'normalized_cycles', 'modular_arrows', 'relaxed_pair_checks')}))


if __name__ == '__main__':
    main()
