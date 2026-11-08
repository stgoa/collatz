#!/usr/bin/env python3
"""Exact finite closure and identity checks for the one/five classification."""

import argparse
import json
from itertools import combinations, product
from math import gcd
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def intercept(word, coefficients=None):
    if coefficients is None:
        coefficients = (1,) * len(word)
    require(len(word) == len(coefficients), 'coefficient length mismatch')
    value, total = 0, 0
    for letter, coefficient in zip(word, coefficients):
        value = 3 * value + coefficient * 2**total
        total += letter
    return value


def integral_arrows(state, coefficient):
    numerator = 3 * state + coefficient
    require(numerator != 0, 'zero numerator needs a separate symbolic argument')
    valuation = (abs(numerator) & -abs(numerator)).bit_length() - 1
    return [(a, numerator // 2**a) for a in range(1, valuation + 1)]


def segment(start, word, coefficients):
    states = [start]
    for a, coefficient in zip(word, coefficients):
        numerator = 3 * states[-1] + coefficient
        require(numerator % 2**a == 0, 'nonintegral cut')
        states.append(numerator // 2**a)
    return states


def check_closure():
    expected = {2: [(1, 6), (2, 3)],
                6: [(1, 12), (2, 6), (3, 3)],
                10: [(1, 18), (2, 9)],
                12: [(1, 21)],
                18: [(1, 30), (2, 15)],
                20: [(1, 33)],
                24: [(1, 39)],
                30: [(1, 48), (2, 24), (3, 12), (4, 6), (5, 3)],
                48: [(1, 75)]}
    reached = {2, 10, 20}
    pending = list(reached)
    while pending:
        state = pending.pop()
        arrows = integral_arrows(state, 6)
        require(state in expected and arrows == expected[state], 'closure table mismatch')
        for _, successor in arrows:
            if successor % 2 == 0 and successor not in reached:
                reached.add(successor)
                pending.append(successor)
    require(reached == set(expected), 'closure states mismatch')
    terminals = [(x, a, y) for x in reached for a, y in integral_arrows(x, 6)
                 if y % 2 and a >= 4]
    require(terminals == [(30, 5, 3)], 'high terminal classification fails')
    positive_odd = {1: (1, 5), 5: (1, 11), 11: (3, 5)}
    for x, arrow in positive_odd.items():
        odd = [(a, y) for a, y in integral_arrows(x, 7) if y % 2]
        require(odd == [arrow], 'positive odd seven-orbit mismatch')
    even_exits = [(x, a, y) for x in (-1, 1, 5, 11)
                  for a, y in integral_arrows(x, 7) if y > 0 and y % 2 == 0]
    require(even_exits == [(-1, 1, 2), (11, 1, 20), (11, 2, 10)],
            'seven-block even exits mismatch')
    require(segment(-2, (1, 1, 3), (6, 6, 7)) == [-2, 0, 3, 2],
            'boundary necessity control failed')
    return dict(six_closure={str(x): expected[x] for x in sorted(expected)},
                high_odd_terminal=terminals, seven_odd_orbit=positive_odd,
                seven_even_exits=even_exits,
                boundary_control=dict(states=[-2, 0, 3, 2], coefficients=[6, 6, 7],
                                      exponents=[1, 1, 3]))


def normalize(u, v):
    n = len(u)
    for turns in range(4):
        changed = [i for i in range(n) if u[i] != v[i]]
        require(len(changed) == 2, 'not two half defects')
        i, h = changed
        delta = (v[i] - u[i], v[h] - u[h])
        if abs(delta[0]) == 1 and delta[1] == 5:
            return u, v, i, h, turns
        cut = i + 1
        w = u + v
        w = w[cut:] + w[:cut]
        u, v = w[:n], w[n:]
    raise RuntimeError('sign/order normalization failed')


def check_identities():
    checked = 0
    signs = set()
    original_patterns = set()
    for n in range(2, 6):
        for u in product((1, 2, 6), repeat=n):
            for i, h in combinations(range(n), 2):
                for amplitudes in ((1, 5), (5, 1)):
                    for first_sign, second_sign in product((-1, 1), repeat=2):
                        v = list(u)
                        v[i] += first_sign * amplitudes[0]
                        v[h] += second_sign * amplitudes[1]
                        if min(v) <= 0:
                            continue
                        original_patterns.add((amplitudes, first_sign, second_sign))
                        v = tuple(v)
                        S = (sum(u) + sum(v)) // 2
                        P = 2**S + 3**n
                        original_gcd = gcd(intercept(u + v), P)
                        p, q, i0, h0, _ = normalize(u, v)
                        epsilon = q[i0] - p[i0]
                        signs.add(epsilon)
                        j = (epsilon + 5) // 2
                        a, b = (6, 7) if epsilon == -1 else (7, 6)
                        B = sum(p)
                        require(S == B + j, 'normalization changes total')
                        require(gcd(intercept(p + q), P) == original_gcd,
                                'rotation changes gcd')
                        terms = [3**(n - 1 - k) * 2**sum(p[:k]) for k in range(n)]
                        X, Y, Z = sum(terms[:i0 + 1]), sum(terms[i0 + 1:h0 + 1]), sum(terms[h0 + 1:])
                        left = 2**j * intercept(p) - intercept(q)
                        if epsilon == -1:
                            left *= 2
                        require(left == a * X + b * Y - 2**j * a * Z,
                                'weighted split identity')
                        r = p[h0 + 1:] + p[:h0 + 1]
                        first_block = n - h0 + i0
                        coefficients = (a,) * first_block + (b,) * (n - first_block)
                        M = intercept(r, coefficients)
                        require(3**(n - 1 - h0) * 2**sum(p[:h0 + 1]) * M
                                == 3**n * a * Z + 2**B * (a * X + b * Y),
                                'weighted rotation identity')
                        require(gcd(M, P) == original_gcd, 'weighted gcd identity')
                        require(M % 2 == a % 2, 'endpoint parity identity')
                        if epsilon == -1:
                            require(r[first_block - 1] >= 2, 'lost decreased-letter positivity')
                        require(M % P != 0, 'unexpected cancellation below minimum family length')
                        checked += 1
    require(signs == {-1, 1}, 'missing normalized sign case')
    require(len(original_patterns) == 8, 'missing original sign/amplitude-order case')
    return checked


def family(t):
    stem = (1, 2, 1, 1) + (3, 1) * t
    return stem + (2, 1, 1, 2), stem + (3, 1, 1, 7)


def check_family():
    records = []
    for t in (*range(9), 32):
        u, v = family(t)
        w = u + v
        n, S = len(u), (sum(u) + sum(v)) // 2
        P = 2**S + 3**n
        require((n, S) == (8 + 2 * t, 14 + 4 * t), 'family totals')
        require(gcd(2 * S, 2 * n) == 4, 'family index is not four')
        require(w.count(7) == 1, 'unique-letter primitivity fails')
        require(2**(2 * S) > 2 * 3**(2 * n), 'family is not far from critical')
        coefficients = (7,) * (5 + 2 * t) + (6,) * 3
        raised = u[:-1] + (u[-1] + 3,)
        states = segment(-3, raised, coefficients)
        require(states[-1] == 3, 'family endpoint failed')
        require(intercept(u, coefficients) == 3 * P, 'family weighted quotient')
        C, D = intercept(w), 2**(2 * S) - 3**(2 * n)
        G = gcd(C, D)
        require(C % P == 0 and G % P == 0, 'family does not cancel plus factor')
        L, K = 16**t, 9**t
        require(7 * intercept(u) == 19683 * K + 51584 * L, 'closed half intercept')
        require(intercept(v) == 8 * intercept(u) - 3 * P, 'second half intercept')
        numerator = 19683 * K + 8576 * L
        denominator = 7 * (16384 * L - 6561 * K)
        require(7 * C == P * numerator, 'closed full intercept')
        require(C * denominator == D * numerator, 'closed rational state')
        require(0 < numerator < denominator and D // G > 1, 'integer-cycle exclusion fails')
        # Every cyclic cut retains full plus divisibility, including all sign/orders.
        for h in range(len(w)):
            rotation = w[h:] + w[:h]
            require(intercept(rotation) % P == 0, 'rotation loses cancellation')
            left, right = rotation[:n], rotation[n:]
            defects = [abs(y - x) for x, y in zip(left, right) if x != y]
            require(sorted(defects) == [1, 5], 'rotation changes defect amplitudes')
        record = dict(t=t, n=n, S=S, P=P, C=C, D=D, G=G, denominator=D // G,
                      index=4, word=list(w), weighted_states=states,
                      rational_state=dict(numerator=numerator, denominator=denominator))
        if t == 0:
            cycle = [intercept(w[h:] + w[:h]) // G for h in range(len(w))]
            require((C, D, P, G, D // G) == (92628965, 225388735, 22945, 252395, 893),
                    'base arithmetic mismatch')
            require(min(cycle) == 367 and len(set(cycle)) == len(w), 'base cycle minimum/period')
            for h, x in enumerate(cycle):
                y = cycle[(h + 1) % len(w)]
                require(x > 0 and x % 2 and y % 2 and 3 * x + 893 == 2**w[h] * y,
                        'base exact positive cycle arrow')
            record['positive_cycle'] = cycle
        records.append(record)
    return records


def compute():
    Cp, Cl, Cz = intercept((1, 2, 1, 1)), intercept((3, 1)), intercept((2, 1, 1, 2))
    require((Cp, Cl, Cz) == (85, 11, 103), 'block intercept constants')
    # Coefficients of K and L after clearing the denominator 16-9=7.
    half_coefficients = (7 * 81 * Cp - 32 * 81 * Cl, 32 * 81 * Cl + 7 * 32 * Cz)
    require(half_coefficients == (19683, 51584), 'symbolic concatenation coefficients')
    quotient_coefficients = (half_coefficients[0], half_coefficients[1] - 7 * 3 * 2048)
    require(quotient_coefficients == (19683, 8576), 'symbolic quotient coefficients')
    gap_coefficients = (7 * 16384 - quotient_coefficients[1], -7 * 6561 - quotient_coefficients[0])
    require(gap_coefficients == (106112, -65610), 'symbolic state-gap coefficients')
    require(gap_coefficients[0] > -gap_coefficients[1] > 0, 'state-gap positivity for L>=K>0')
    controls = {}
    for d in (5, 7, 13, 61):
        states = segment(-1, (1,), (d,))
        require(states[-1] == (d - 3) // 2 > 0, '3x+d crossing control')
        controls[str(d)] = states
    result = dict(closure=check_closure(), normalized_pairs_checked=check_identities(),
                  family_checks=check_family(), crossing_controls=controls,
                  symbolic_coefficients=dict(half_K_L=half_coefficients,
                                             quotient_K_L=quotient_coefficients,
                                             denominator_minus_numerator_L_K=gap_coefficients),
                  far_critical_base=dict(two_power=2**28, twice_three_power=2 * 3**16),
                  far_critical_step=dict(numerator=256, denominator=81))
    # Normalize tuple and integer-key representations before receipt comparison.
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
