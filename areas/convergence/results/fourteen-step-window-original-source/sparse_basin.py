"""Independent signed classification of every relevant R92 boundary origin.

The congruence and individual height bounds reduce the larger origin universe
without assuming a bound on any intermediate state. Every resource cap aborts.
This module uses only the standard library and imports no other orbit code.
"""
from fractions import Fraction
import hashlib
from math import gcd

D, B, A, M = 7153, 299947, 3**12, 2**19
ROOT = -3*B
T0 = -ROOT-D
COSTS = tuple(range(8, 15))


def integer(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError('expected an integer at least '+str(minimum))


def valuation(n):
    if type(n) is not int or n == 0:
        raise ValueError('valuation requires a nonzero integer')
    n = abs(n)
    return (n & -n).bit_length()-1


def _normalize(n):
    extra = 0
    while n % 8 == 5:
        n = (n-D)//4
        extra += 2
    if n % 4 == 3:
        a = valuation(n+D)
        if ((n+D)//2**a) % 4 == (3 if a % 2 else 1):
            n = (n-D)//2
            extra += 1
    return n, extra


def normalize(n):
    if type(n) is not int or n >= -D or n % 2 == 0 or gcd(n, D) != 1:
        raise ValueError('expected a primitive odd signed numerator below -D')
    return _normalize(n)


def step(n):
    """One signed quotient arrow, with its full inverse binary exponent."""
    if normalize(n)[0] != n:
        raise ValueError('the source must be signed canonical')
    raw = 3*n+D
    exponent = valuation(raw)
    nxt = raw//2**exponent
    if nxt >= -D:
        # This invariant interval cannot reach the negative target cycle.
        return nxt, exponent
    nxt, extra = _normalize(nxt)
    return nxt, exponent+extra


def candidate_classes():
    """The exact seven congruence classes and strict individual bounds."""
    answer = []
    for m in COSTS:
        bound = Fraction(D)+Fraction(2**m, 243)*(T0+12*A)
        residue = (-ROOT*pow(2, m, D)*pow(243, -1, D)) % D
        first = residue
        if first <= D:
            first += ((D-first)//D+1)*D
        if first % 2 == 0:
            first += D
        count = canonical = 0
        for u in range(first, (bound.numerator+bound.denominator-1)//bound.denominator, 2*D):
            assert D < u < bound and u % 2 and gcd(u, D) == 1
            count += 1
            canonical += _normalize(-u)[0] == -u
        answer.append(dict(m=m, residue=residue, first=first, period=2*D,
                           strict_bound=[bound.numerator, bound.denominator],
                           odd_rows=count, canonical_rows=canonical))
    return answer


def candidates():
    """Yield (m,u,is_canonical) for every odd candidate, in fixed order."""
    for cell in candidate_classes():
        top = Fraction(*cell['strict_bound'])
        stop = (top.numerator+top.denominator-1)//top.denominator
        for u in range(cell['first'], stop, cell['period']):
            yield cell['m'], u, _normalize(-u)[0] == -u


def row_bytes(m, u, status, depth, cost):
    """Digest format: status0 noncanonical,1 nonhit,2 target hit."""
    return f'{m},{u},{status},{depth},{cost}\n'.encode('ascii')


def classify(max_path=100000, max_states=5000000, max_bits=256):
    """Completely classify the sparse finite universe; never hide a cap.

    A nonhit is certified by a path into the invariant interval, an actual
    detected non-target cycle, or an already classified state. The deterministic
    receipt stores complete first-hit paths and a digest of every candidate row.
    """
    for value in (max_path, max_states, max_bits):
        integer(value, 1)
    memo = {ROOT: (True, 0, 0)}
    largest = abs(ROOT)
    longest = transitions = interval_exits = other_cycles = 0

    def classify_one(origin):
        nonlocal largest, longest, transitions, interval_exits, other_cycles
        n, path, positions = origin, [], {}
        while n not in memo:
            if n >= -D:
                interval_exits += 1
                result = (False, 0, 0)
                break
            if n in positions:
                other_cycles += 1
                result = (False, 0, 0)
                break
            if len(path) >= max_path:
                raise RuntimeError('path cap reached: unresolved origin')
            if len(memo)+len(path) >= max_states:
                raise RuntimeError('state cap reached: unresolved origin')
            if abs(n).bit_length() > max_bits:
                raise RuntimeError('arithmetic-size cap reached: unresolved origin')
            positions[n] = len(path)
            nxt, exponent = step(n)
            if abs(nxt).bit_length() > max_bits:
                raise RuntimeError('arithmetic-size cap reached: unresolved successor')
            path.append((n, exponent))
            largest = max(largest, abs(n), abs(nxt))
            transitions += 1
            n = nxt
        else:
            result = memo[n]
        longest = max(longest, len(path))
        for n, exponent in reversed(path):
            if result[0]:
                result = (True, result[1]+1, result[2]+exponent)
            memo[n] = result
        return memo[origin]

    fingerprint = hashlib.sha256()
    total = canonical = 0
    hits, relevant, hit_details = [], [], []
    for m, u, admitted in candidates():
        total += 1
        if not admitted:
            fingerprint.update(row_bytes(m, u, 0, 0, 0))
            continue
        canonical += 1
        hit, depth, cost = classify_one(-u)
        fingerprint.update(row_bytes(m, u, 2 if hit else 1, depth, cost))
        if hit:
            hits.append([u, depth, cost])
            matches = depth % 12 == 5 and cost-19*((depth-5)//12) == m
            if matches:
                relevant.append([u, depth, cost])
            hit_details.append([m, u, depth, cost, matches])

    paths = []
    for u, depth, cost in hits:
        n, numerators, exponents = -u, [-u], []
        for _ in range(depth):
            assert n != ROOT
            n, e = step(n)
            numerators.append(n)
            exponents.append(e)
        assert n == ROOT and sum(exponents) == cost
        paths.append(dict(origin=u, depth=depth, cost=cost,
                          signed_numerators=numerators, exponents=exponents))
    return dict(candidate_classes=candidate_classes(), candidates=total,
                canonical_count=canonical, classified_states=len(memo),
                largest_numerator=largest, longest_new_path=longest,
                transitions=transitions, invariant_exits=interval_exits,
                other_cycles=other_cycles, cap_hits=0,
                caps=dict(path=max_path, states=max_states, integer_bits=max_bits),
                classification_sha256=fingerprint.hexdigest(), hits=hits,
                relevant_hits=relevant, hit_details=hit_details,
                first_hit_paths=paths)
