#!/usr/bin/env python3
"""Exact closure and affine-bound certificate for two/four half defects."""

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations, product
from math import gcd
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def intercept(word, coefficients=None):
    coefficients = (1,) * len(word) if coefficients is None else coefficients
    require(len(word) == len(coefficients), 'coefficient length mismatch')
    value, total = 0, 0
    for a, b in zip(word, coefficients):
        value = 3 * value + b * 2**total
        total += a
    return value


def arrows(x, b):
    numerator = 3 * x + b
    require(numerator != 0, 'zero numerator needs a separate argument')
    v = (abs(numerator) & -abs(numerator)).bit_length() - 1
    return [(a, numerator // 2**a) for a in range(1, v + 1)]


def segment(x, word, coefficients):
    states = [x]
    for a, b in zip(word, coefficients):
        numerator = 3 * states[-1] + b
        require(numerator % 2**a == 0, 'nonintegral cut')
        states.append(numerator // 2**a)
    return states


def affine(word, x):
    for a in word:
        x = (3 * x + 1) / 2**a
    return x


def check_closure():
    expected = {2: [(1, 5)],
                4: [(1, 8), (2, 4), (3, 2), (4, 1)],
                8: [(1, 14), (2, 7)],
                10: [(1, 17)],
                14: [(1, 23)],
                16: [(1, 26), (2, 13)],
                20: [(1, 32), (2, 16), (3, 8), (4, 4), (5, 2), (6, 1)],
                26: [(1, 41)],
                32: [(1, 50), (2, 25)],
                50: [(1, 77)]}
    reached = {2, 10, 20}
    pending = list(reached)
    while pending:
        x = pending.pop()
        outgoing = arrows(x, 4)
        require(x in expected and outgoing == expected[x], 'four-block closure mismatch')
        for _, y in outgoing:
            if y % 2 == 0 and y not in reached:
                reached.add(y)
                pending.append(y)
    require(reached == set(expected), 'closure states mismatch')
    terminals = sorted((x, a, y) for x in reached for a, y in arrows(x, 4)
                       if y % 2 and a >= 4)
    require(terminals == [(4, 4, 1), (20, 6, 1)], 'high odd terminal mismatch')
    # Backward accessibility inside the closed even graph establishes both tail shapes.
    relevant = {x for x, _, _ in terminals}
    while True:
        enlarged = relevant | {x for x in reached if any(y in relevant and y % 2 == 0
                                                        for _, y in arrows(x, 4))}
        if enlarged == relevant:
            break
        relevant = enlarged
    require(relevant == {4, 20}, 'unexpected predecessor branch to a high terminal')
    require(arrows(-10, 4) == [(1, -13)], 'negative boundary obstruction')
    odd_orbit = {1: (1, 5), 5: (1, 11), 11: (3, 5)}
    for x, expected_arrow in odd_orbit.items():
        require([(a, y) for a, y in arrows(x, 7) if y % 2] == [expected_arrow],
                'seven-block positive odd orbit')
    exits = [(x, a, y) for x in (-1, 1, 5, 11) for a, y in arrows(x, 7)
             if y > 0 and y % 2 == 0]
    require(exits == [(-1, 1, 2), (11, 1, 20), (11, 2, 10)], 'even interfaces')
    return dict(four_closure={str(x): expected[x] for x in sorted(expected)},
                high_terminals=terminals, relevant_predecessors=sorted(relevant),
                seven_odd_orbit=odd_orbit, seven_even_exits=exits,
                negative_boundary=dict(start=-10, exponent=1, end=-13))


def check_intervals():
    low, high = Fraction(11, 7), Fraction(7, 2)
    require(affine((2, 1, 1), Fraction(1)) == high, 'shared prefix bound')
    require(affine((3, 1), low) == low, 'loop fixed point')
    require(low <= affine((3, 1), high) <= high, 'loop interval invariance')
    following_one = affine((1,), high)
    direct_bound = affine((3,), following_one)
    four_bound = affine((4,), following_one)
    require(following_one == Fraction(23, 4), 'post-loop bound')
    require(direct_bound == Fraction(73, 32) < 9, 'direct final bound')
    require(four_bound == Fraction(73, 64), 'second-family prefix bound')
    require(Fraction(0) <= affine((2,), Fraction(0)) <= four_bound,
            'letter-two lower endpoint')
    require(Fraction(0) <= affine((2,), four_bound) <= four_bound,
            'letter-two upper endpoint')
    second_bound = affine((1,), four_bound)
    require(second_bound == Fraction(283, 128) < 9, 'second final bound')
    # All maps are increasing, so the endpoint checks certify the entire intervals.
    return {key: str(value) for key, value in dict(loop_low=low, loop_high=high,
            following_one=following_one, direct_bound=direct_bound,
            four_bound=four_bound, repeated_two_upper=affine((2,), four_bound),
            second_bound=second_bound).items()}


def normalize(u, v):
    n = len(u)
    for _ in range(4):
        changed = [i for i in range(n) if u[i] != v[i]]
        require(len(changed) == 2, 'not two half defects')
        i, h = changed
        if abs(v[i] - u[i]) == 2 and v[h] - u[h] == 4:
            return u, v, i, h
        cut = i + 1
        w = u + v
        w = w[cut:] + w[:cut]
        u, v = w[:n], w[n:]
    raise RuntimeError('normalization failed')


def family(t, k=None):
    prefix = (2, 1, 1) + (3, 1) * t
    if k is None:
        return prefix + (1, 3), prefix + (3, 7)
    return prefix + (1, 4) + (2,) * k + (1,), prefix + (3, 4) + (2,) * k + (5,)


def check_identities():
    checked, full_hits = 0, 0
    patterns = set()
    for n in range(2, 6):
        for u in product((1, 2, 3, 5), repeat=n):
            for i, h in combinations(range(n), 2):
                for amplitudes in ((2, 4), (4, 2)):
                    for s1, s2 in product((-1, 1), repeat=2):
                        v = list(u)
                        v[i] += s1 * amplitudes[0]
                        v[h] += s2 * amplitudes[1]
                        if min(v) <= 0:
                            continue
                        patterns.add((amplitudes, s1, s2))
                        v = tuple(v)
                        S = (sum(u) + sum(v)) // 2
                        P = 2**S + 3**n
                        original_gcd = gcd(intercept(u + v), P)
                        p, q, i0, h0 = normalize(u, v)
                        epsilon = q[i0] - p[i0]
                        j = (epsilon + 4) // 2
                        a, b = (4, 7) if epsilon == -2 else (7, 4)
                        B = sum(p)
                        require(S == B + j, 'changed total in normalization')
                        require(gcd(intercept(p + q), P) == original_gcd, 'rotation gcd')
                        terms = [3**(n - 1 - z) * 2**sum(p[:z]) for z in range(n)]
                        X, Y, Z = sum(terms[:i0 + 1]), sum(terms[i0 + 1:h0 + 1]), sum(terms[h0 + 1:])
                        lhs = (2**j * intercept(p) - intercept(q)) * (4 if epsilon == -2 else 1)
                        require(lhs == a * X + b * Y - 2**j * a * Z, 'weighted split')
                        r = p[h0 + 1:] + p[:h0 + 1]
                        first_block = n - h0 + i0
                        coefficients = (a,) * first_block + (b,) * (n - first_block)
                        M = intercept(r, coefficients)
                        require(3**(n - 1 - h0) * 2**sum(p[:h0 + 1]) * M
                                == 3**n * a * Z + 2**B * (a * X + b * Y), 'weighted rotation')
                        require(gcd(M, P) == original_gcd, 'weighted gcd')
                        require(M % 2 == a % 2, 'initial parity')
                        if epsilon == -2:
                            require(r[first_block - 1] >= 3, 'decreased-letter boundary')
                        if M % P == 0:
                            require(n == 5 and epsilon == 2 and r == family(0)[0] and M == P,
                                    'unexpected finite full-cancellation word')
                            raised = r[:-1] + (r[-1] + j,)
                            require(segment(-1, raised, coefficients)[-1] == 1, 'finite endpoint')
                            full_hits += 1
                        checked += 1
    require(len(patterns) == 8 and full_hits > 0, 'missing sign cases or exceptional controls')
    return dict(pairs=checked, sign_order_patterns=len(patterns), full_cancellation_hits=full_hits)


def check_families():
    parameters = [(t, None) for t in (0, 1, 2, 3, 8, 32)]
    parameters += [(t, k) for t, k in product((0, 1, 2, 5), (0, 1, 2, 5))]
    records = []
    for t, k in parameters:
        u, v = family(t, k)
        w = u + v
        n, S = len(u), (sum(u) + sum(v)) // 2
        P, D = 2**S + 3**n, 2**(2 * S) - 3**(2 * n)
        C = intercept(w)
        G = gcd(C, D)
        require(n == (5 + 2 * t if k is None else 6 + 2 * t + k), 'family length')
        require(S == 2 * n + 1 and gcd(2 * S, 2 * n) == 2, 'family total and index')
        require(2**(2 * S) > 2 * 3**(2 * n), 'family far-criticality')
        require(w.count(7 if k is None else 5) == 1, 'family primitivity')
        first_block = 4 + 2 * t
        coefficients = (7,) * first_block + (4,) * (n - first_block)
        raised = u[:-1] + (u[-1] + 3,)
        states = segment(-1, raised, coefficients)
        require(states[-1] == 1 and intercept(u, coefficients) == P, 'family weighted endpoint')
        alpha, beta = 3**n, 2**sum(u)
        Cu, Cv = intercept(u), intercept(v)
        require(Cv == 8 * Cu - P and C == P * (Cu - beta), 'family intercept quotient')
        require(Fraction(C, D) == Fraction(Cu - beta, 8 * beta - alpha), 'rational state identity')
        bound = Fraction(73, 32) if k is None else Fraction(283, 128)
        require(affine(u, Fraction(1)) == Fraction(alpha + Cu, beta) <= bound < 9,
                'uniform affine bound')
        require(0 < C < D and D // G > 1 and gcd(G, P) == P, 'denominator/primitive factor')
        for h in range(len(w)):
            rotated = w[h:] + w[:h]
            require(gcd(intercept(rotated), D) == G, 'denominator rotation invariance')
            differences = [abs(y - x) for x, y in zip(rotated[:n], rotated[n:]) if x != y]
            require(sorted(differences) == [2, 4], 'rotation defect class')
        record = dict(t=t, k=k, n=n, S=S, P=P, C=C, D=D, G=G,
                      denominator=D // G, primitive_cancellation=P, word=list(w),
                      signed_states=states, rational_state=str(Fraction(C, D)),
                      affine_at_one=str(affine(u, Fraction(1))))
        if t == 0 and k is None:
            require((C, D, P, G, D // G) == (194735, 4135255, 2291, 11455, 361),
                    'base arithmetic')
            cycle = [intercept(w[h:] + w[:h]) // G for h in range(len(w))]
            require(min(cycle) == 17 and len(set(cycle)) == len(w), 'base cycle minimum/period')
            for h, x in enumerate(cycle):
                y = cycle[(h + 1) % len(w)]
                require(x > 0 and x % 2 and y % 2 and 3 * x + 361 == 2**w[h] * y,
                        'base exact positive cycle')
            record['positive_cycle'] = cycle
        records.append(record)
    return records


def check_actual_controls():
    relative = Path('areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json')
    fixture = Path(__file__).resolve().parents[4] / relative
    raw = fixture.read_bytes()
    cycles = json.loads(raw)['cycles']
    require(len(cycles) == 11 and {row['d'] for row in cycles} == {5, 7, 13, 61},
            'standard fixture scope changed')
    records = []
    for row in cycles:
        d, states, word = row['d'], row['states'], tuple(row['valuations'])
        require(len(word) == len(states) > 0 and min(word) >= 1, 'fixture lengths/valuations')
        require(len(set(states)) == len(states) and min(states) == row['minimum'],
                'fixture period/minimum')
        for i, x in enumerate(states):
            y = states[(i + 1) % len(states)]
            require(x > 0 and x % 2 and y % 2 and 3 * x + d == 2**word[i] * y,
                    'fixture exact cycle arrow')
        in_class = False
        if len(word) % 2 == 0:
            n = len(word) // 2
            for h in range(len(word)):
                rotated = word[h:] + word[:h]
                differences = sorted(abs(y - x) for x, y in zip(rotated[:n], rotated[n:]) if x != y)
                in_class |= differences == [2, 4]
        require(not in_class, 'actual control unexpectedly belongs to the two/four class')
        records.append(dict(d=d, minimum=min(states), period=len(word), states=states,
                            valuations=list(word), in_two_four_class=False))
    return dict(fixture=str(relative), sha256=hashlib.sha256(raw).hexdigest(), cycles=records)


def compute():
    controls = {}
    for d in (5, 7, 13, 61):
        states = segment(-1, (1,), (d,))
        require(states[-1] == (d - 3) // 2 > 0, '3x+d crossing control')
        controls[str(d)] = states
    result = dict(closure=check_closure(), affine_intervals=check_intervals(),
                  identity_checks=check_identities(), family_checks=check_families(),
                  crossing_controls=controls, actual_cycle_controls=check_actual_controls())
    return json.loads(json.dumps(result))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result = compute()
    receipt = Path(__file__).with_suffix('.json')
    if args.write_receipt:
        receipt.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    else:
        require(receipt.exists(), 'missing receipt')
        require(json.loads(receipt.read_text()) == result, 'receipt mismatch')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
