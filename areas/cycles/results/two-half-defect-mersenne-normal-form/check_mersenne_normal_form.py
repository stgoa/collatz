#!/usr/bin/env python3
"""Exact identities and bidirectional checks for the signed-Mersenne normal form."""

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
    c, total = 0, 0
    for a, b in zip(word, coefficients):
        c = 3 * c + b * 2**total
        total += a
    return c


def change_last(word, amount):
    require(bool(word) and word[-1] + amount > 0, 'nonpositive reconstructed letter')
    return word[:-1] + (word[-1] + amount,)


def odd_segment(start, word, d):
    require(bool(word) and start % 2 and start != 0, 'invalid signed segment start')
    states = [start]
    for a in word:
        numerator = 3 * states[-1] + d
        require(numerator != 0 and a >= 1, 'zero numerator or invalid exponent')
        valuation = (abs(numerator) & -abs(numerator)).bit_length() - 1
        require(a == valuation, 'segment valuation is not exact')
        successor = numerator // 2**a
        require(successor != 0 and successor % 2, 'segment cut is not nonzero odd')
        states.append(successor)
    return states


def reconstruct(J, r, order, A, B):
    p = J - r
    require(J > r >= 1 and A and B, 'invalid normal-form parameters')
    if order == 'high-low':
        return change_last(A, -p) + change_last(B, -r), A + change_last(B, J)
    require(order == 'low-high', 'unknown segment order')
    return change_last(A, p) + change_last(B, -J), A + change_last(B, r)


def canonical_cut(u, v, p, q):
    n = len(u)
    for _ in range(4):
        changed = [i for i in range(n) if u[i] != v[i]]
        require(len(changed) == 2, 'not two half defects')
        i, h = changed
        if abs(v[i] - u[i]) == p and v[h] - u[h] == q:
            U, V = u[h + 1:] + u[:h + 1], v[h + 1:] + v[:h + 1]
            return U, V, n - h + i
        cut = i + 1
        w = u + v
        w = w[cut:] + w[:cut]
        u, v = w[:n], w[n:]
    raise RuntimeError('cyclic normalization failed')


def check_pair(u, v, J, r):
    p, q = J - r, J + r
    n = len(u)
    require(n == len(v) and n >= 2 and min(u + v) > 0, 'invalid positive half pair')
    S = (sum(u) + sum(v)) // 2
    P = 2**S + 3**n
    original = u + v
    U, V, cut = canonical_cut(u, v, p, q)
    require(U + V in [original[i:] + original[:i] for i in range(2 * n)],
            'canonical cut is not a full-word rotation')
    require(0 < cut < n and V[-1] - U[-1] == q, 'canonical boundary')
    positive = V[cut - 1] - U[cut - 1] == p
    s = J if positive else r
    K = 2**p
    Cu, Cv = intercept(U), intercept(V)
    require(sum(U) + s == S, 'canonical total')
    M0 = 2**s * Cu - Cv
    require(M0 > 0 and M0 % 2, 'normalized quotient numerator is not positive odd')
    coefficients = ((2**J - 1,) * cut + (K * (2**r - 1),) * (n - cut)
                    if positive else (K * (2**r - 1),) * cut + (2**J - 1,) * (n - cut))
    require(intercept(U, coefficients) == (M0 if positive else K * M0), 'weighted formula')
    require(gcd(intercept(original), P) == gcd(intercept(U + V), P) == gcd(M0, P),
            'rotation/plus-factor gcd identity')
    if M0 % P:
        return None
    h = M0 // P
    require(h > 0 and h % 2, 'endpoint h is not positive odd')
    first, second = U[:cut], U[cut:]
    if positive:
        A, B = change_last(first, p), change_last(second, r)
        order, d1, d2 = 'high-low', 2**J - 1, 2**r - 1
        require(A[-1] > p and B[-1] > r, 'high-low terminal conditions')
    else:
        A, B = change_last(first, -p), change_last(second, J)
        order, d1, d2 = 'low-high', 2**r - 1, 2**J - 1
        require(B[-1] > J, 'low-high terminal condition')
    first_states = odd_segment(-h, A, d1)
    second_states = odd_segment(first_states[-1], B, d2)
    require(second_states[-1] == h, 'ordinary signed endpoint')
    require(reconstruct(J, r, order, A, B) == (U, V), 'inverse reconstruction')
    require(sum(A) + sum(B) == S, 'segment total is not S')
    # Independently check the integral weighted cuts and the exact even-block level.
    H = h if positive else K * h
    weighted_states = [-H]
    raised = change_last(U, s)
    for a, b in zip(raised, coefficients):
        numerator = 3 * weighted_states[-1] + b
        require(numerator % 2**a == 0, 'weighted cut not integral')
        weighted_states.append(numerator // 2**a)
    require(weighted_states[-1] == H, 'weighted endpoint')
    even_inputs = weighted_states[cut:n] if positive else weighted_states[:cut]
    require(all(x != 0 and x % K == 0 and (x // K) % 2 for x in even_inputs),
            'even block does not have exact valuation p')
    alpha, beta = 3**n, 2**sum(U)
    C, D = intercept(U + V), 2**(2 * S) - 3**(2 * n)
    require(Cv == 2**s * Cu - h * P and C == P * (Cu - h * beta), 'cycle-state identities')
    state = None
    criterion = None
    if D > 0:
        x = Fraction(C, D)
        Fu1 = Fraction(alpha + Cu, beta)
        require(x == Fraction(Cu - h * beta, 2**s * beta - alpha) > 0, 'rational cycle state')
        criterion = Fu1 < 2**s + h
        require((x < 1) == criterion, 'affine-state criterion equivalence')
        if criterion:
            require(D // gcd(C, D) > 1, 'denominator consequence')
        state = str(x)
    return dict(J=J, r=r, p=p, q=q, order=order, h=h, S=S,
                A=list(A), B=list(B), u=list(U), v=list(V),
                first_states=first_states, second_states=second_states,
                rational_state=state, affine_criterion=criterion)


def symbolic_identities():
    # Laurent polynomials in K,L,X,Y,alpha,beta,h,C; negative powers allow C_v=X+Y/K.
    zero = (0,) * 8
    def constant(c):
        return {} if c == 0 else {zero: c}
    def variable(i, exponent=1):
        m = list(zero)
        m[i] = exponent
        return {tuple(m): 1}
    def add(*polynomials):
        out = {}
        for polynomial in polynomials:
            for m, c in polynomial.items():
                out[m] = out.get(m, 0) + c
        return {m: c for m, c in out.items() if c}
    def scale(poly, c):
        return {m: c * v for m, v in poly.items() if c * v}
    def mul(a, b):
        out = {}
        for m, c in a.items():
            for n, d in b.items():
                exponent = tuple(x + y for x, y in zip(m, n))
                out[exponent] = out.get(exponent, 0) + c * d
        return {m: c for m, c in out.items() if c}
    K, L, X, Y, alpha, beta, h, C = [variable(i) for i in range(8)]
    one = constant(1)
    E = mul(K, L)
    Cu = add(X, Y)
    positive_Cv = add(X, mul(K, Y))
    require(add(mul(E, Cu), scale(positive_Cv, -1))
            == add(mul(add(E, scale(one, -1)), X), mul(mul(K, add(L, scale(one, -1))), Y)),
            'symbolic positive coefficient identity')
    negative_Cv = add(X, mul(variable(0, -1), Y))
    require(mul(K, add(mul(L, Cu), scale(negative_Cv, -1)))
            == add(mul(mul(K, add(L, scale(one, -1))), X), mul(add(E, scale(one, -1)), Y)),
            'symbolic negative coefficient identity')
    for slope in (E, L):
        P = add(alpha, mul(slope, beta))
        Cv = add(mul(slope, C), scale(mul(h, P), -1))
        require(add(mul(alpha, C), mul(beta, Cv))
                == mul(P, add(C, scale(mul(h, beta), -1))), 'symbolic cycle quotient')
    return ['positive weighted identity', 'negative weighted identity',
            'cycle quotient for both normalized totals']


def bounded_forward_checks():
    count, hits = 0, []
    patterns = set()
    for n in range(2, 5):
        for u in product((1, 5, 11), repeat=n):
            for i, h in combinations(range(n), 2):
                for J in range(2, 6):
                    for r in range(1, J):
                        p, q = J - r, J + r
                        for amplitudes in ((p, q), (q, p)):
                            for s1, s2 in product((-1, 1), repeat=2):
                                v = list(u)
                                v[i] += s1 * amplitudes[0]
                                v[h] += s2 * amplitudes[1]
                                if min(v) <= 0:
                                    continue
                                patterns.add((J, r, amplitudes, s1, s2))
                                result = check_pair(u, tuple(v), J, r)
                                if result:
                                    hits.append(result)
                                count += 1
    require(len(patterns) == 80 and hits, 'missing grid parameters/sign patterns/hits')
    return dict(scope=dict(half_lengths=[2, 3, 4], base_letters=[1, 5, 11],
                           J=[2, 3, 4, 5], r='every integer 1<=r<J'),
                pairs=count, sign_order_patterns_per_parameter=8,
                parameter_pairs=10, full_cancellation_hits=hits)


def reverse_controls():
    examples = []
    # Existing one/five family: signed +7 followed by signed +3.
    for t in range(5):
        examples.append((3, 2, 'high-low', 3,
                         (1, 2, 1, 1) + (3, 1) * t + (3,), (1, 1, 4)))
    # Existing two/four families: signed +7 followed by signed +1.
    for t in range(4):
        A = (2, 1, 1) + (3, 1) * t + (3,)
        examples.append((3, 1, 'high-low', 1, A, (4,)))
        for k in range(4):
            examples.append((3, 1, 'high-low', 1, A, (4,) + (2,) * k + (2,)))
    examples += [(4, 3, 'high-low', 1, (2,), (4,)),
                 (5, 3, 'low-high', 1, (2, 1, 1), (6,))]
    records = []
    for J, r, order, h, A, B in examples:
        d1, d2 = (2**J - 1, 2**r - 1) if order == 'high-low' else (2**r - 1, 2**J - 1)
        first = odd_segment(-h, A, d1)
        require(odd_segment(first[-1], B, d2)[-1] == h, 'reverse control endpoints')
        u, v = reconstruct(J, r, order, A, B)
        record = check_pair(u, v, J, r)
        require(record is not None and record['A'] == list(A) and record['B'] == list(B),
                'reverse/forward reconstruction mismatch')
        # Every full cyclic cut remains in the same class and retains cancellation.
        w, n = u + v, len(u)
        for shift in range(len(w)):
            rotated = w[shift:] + w[:shift]
            require(check_pair(rotated[:n], rotated[n:], J, r) is not None,
                    'cyclic-cut reconstruction failed')
        records.append(record)
    # Previously excluded one/three cases, in both normalized signs.
    no_one_three = [((1, 1, 1, 1, 2), (2, 1, 1, 4, 2)),
                    ((2, 1, 1, 1, 2), (1, 1, 1, 4, 2))]
    for u, v in no_one_three:
        require(check_pair(u, v, 2, 1) is None, 'one/three control unexpectedly cancels')
    try:
        odd_segment(-1, (1,), 3)
    except RuntimeError:
        zero_rejected = True
    else:
        zero_rejected = False
    require(zero_rejected, 'zero cannot be an ordinary signed odd step')
    return dict(segment_pairs=records, one_three_noncancellation_controls=len(no_one_three),
                zero_numerator_rejected=zero_rejected)


def actual_controls():
    relative = Path('areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json')
    raw = (Path(__file__).resolve().parents[4] / relative).read_bytes()
    fixtures = json.loads(raw)['cycles']
    require(len(fixtures) == 11, 'fixture count changed')
    records = []
    for row in fixtures:
        states, word, d = row['states'], tuple(row['valuations']), row['d']
        require(len(word) == len(states) and len(set(states)) == len(states), 'fixture period')
        require(min(states) == row['minimum'], 'fixture minimum')
        require(odd_segment(states[0], word, d) == states + states[:1], 'actual cycle replay')
        records.append(dict(d=d, minimum=min(states), period=len(states), states=states, valuations=list(word)))
    crossings = {str(d): odd_segment(-1, (1,), d) for d in (5, 13, 61)}
    # +7 crosses with exact valuation 2; division by only 2 would leave an even state.
    crossings['7'] = odd_segment(-1, (2,), 7)
    return dict(fixture=str(relative), sha256=hashlib.sha256(raw).hexdigest(),
                cycles=records, signed_crossings=crossings)


def compute():
    return dict(symbolic_identities=symbolic_identities(), forward_grid=bounded_forward_checks(),
                reverse_controls=reverse_controls(), actual_controls=actual_controls())


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
