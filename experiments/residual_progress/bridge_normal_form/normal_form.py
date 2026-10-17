"""Exact normal form for one-step sibling and R23 halving bridges.

This normalizes known identities.  It does not search for absorption or claim
that iteration of the induced Syracuse map terminates.
"""

from collections import Counter


def _odd(x):
    if not isinstance(x, int) or x <= 0 or x % 2 != 1:
        raise ValueError("Expected a positive odd integer")


def valuation2(x):
    if x <= 0:
        raise ValueError("Expected a positive integer")
    return (x & -x).bit_length() - 1


def step(x):
    _odd(x)
    if x == 1:
        return 1
    z = 3 * x + 1
    return z >> valuation2(z)


def F(x):
    _odd(x)
    return 4 * x + 1


def F_power(x, k):
    _odd(x)
    if not isinstance(k, int) or k < 0:
        raise ValueError("Expected a nonnegative integer exponent")
    return (4**k * (3*x + 1) - 1) // 3


def selected(x):
    _odd(x)
    if x % 4 != 3:
        return False
    a = valuation2(x + 1)
    t = (x + 1) >> a
    return t % 4 == (1 if a % 2 == 0 else 3)


def canonical(x):
    _odd(x)
    return x % 8 == 1 or (x % 4 == 3 and not selected(x))


def normalization(x):
    """Return the unique minimum of the complete elementary bridge class."""
    _odd(x)
    base, exponent = x, 0
    while base % 8 == 5:
        base = (base - 1) // 4
        exponent += 1
    partner = selected(base)
    minimum = (base - 1) // 2 if partner else base
    assert canonical(minimum)
    assert base == minimum or base == 2*minimum + 1
    return dict(seed=x, minimum=minimum, base=base, F_exponent=exponent,
                selected_partner=partner)


def normal_form(x):
    return normalization(x)["minimum"]


def canonical_count(limit, residue=0, odd_modulus=1):
    """Exact O(log limit) count of canonical q<=limit in an odd progression."""
    if not isinstance(limit, int) or limit < 0:
        raise ValueError("Expected a nonnegative integer cutoff")
    if not isinstance(odd_modulus, int) or odd_modulus <= 0 or odd_modulus % 2 == 0:
        raise ValueError("Expected a positive odd modulus")
    if limit == 0:
        return 0

    def count_class(b, power):
        index = ((residue-b) * pow(power, -1, odd_modulus)) % odd_modulus
        first = (b + power*index) % (power*odd_modulus)
        assert first > 0 and first % 2 == 1
        return max(0, (limit-first)//(power*odd_modulus) + 1)

    answer = count_class(1, 8)
    for a in range(2, (limit+1).bit_length()):
        b = (3 if a % 2 == 0 else 1) * 2**a - 1
        answer += count_class(b, 2**(a+2))
    return answer


def stratum_count(limit, k, partner, residue=0, odd_modulus=1):
    """Exact count x<=limit in one normal-form stratum and odd progression."""
    if not isinstance(k, int) or k < 0 or partner not in (False, True):
        raise ValueError("Expected a nonnegative depth and Boolean partner flag")
    factor = 4**k * (2 if partner else 1)
    offset = (4**(k+1)-1)//3 if partner else (4**k-1)//3
    q_limit = max(0, (limit-offset)//factor)
    q_residue = ((residue-offset) * pow(factor, -1, odd_modulus)) % odd_modulus
    return canonical_count(q_limit, q_residue, odd_modulus)


def _clean(counter):
    return {x: c for x, c in sorted(counter.items()) if x != 1 and c}


def divergence(current):
    answer = Counter()
    for x, c in current.items():
        _odd(x)
        if x == 1 or not c:
            continue
        answer[x] += c
        y = step(x)
        if y != 1:
            answer[y] -= c
    return _clean(answer)


def bridge(x):
    """Return an exact integer current with div J=delta_x-delta_nu(x).

    Only the explicit R23 prefixes are exposed, with known length a.  No
    unrestricted orbit search is used; delta1 and its current row are killed.
    """
    data = normalization(x)
    base, q = data["base"], data["minimum"]
    current = Counter()
    if x != base:
        current[x] += 1
        current[base] -= 1
    left, right = [base], [q]
    if data["selected_partner"]:
        a = valuation2(base + 1)
        for _ in range(a):
            if left[-1] != 1:
                current[left[-1]] += 1
            if right[-1] != 1:
                current[right[-1]] -= 1
            left.append(step(left[-1]))
            right.append(step(right[-1]))
        assert left[-1] == right[-1]
    result = _clean(current)
    expected = Counter({x: 1})
    expected[q] -= 1
    assert divergence(result) == _clean(expected)
    data.update(current=result, left_prefix=left, right_prefix=right)
    return data


def quotient_step(q):
    """The genuine induced map T=nu S on canonical minima."""
    if not canonical(q):
        raise ValueError("The quotient state must be canonical")
    return normal_form(step(q))


def quotient_bridge(q):
    """Exact finite bridge delta_q-delta_T(q), retaining all signed rows."""
    if not canonical(q):
        raise ValueError("The quotient state must be canonical")
    successor = step(q)
    data = bridge(successor)
    current = Counter(data["current"])
    if q != 1:
        current[q] += 1
    result = _clean(current)
    expected = Counter({q: 1})
    expected[data["minimum"]] -= 1
    assert divergence(result) == _clean(expected)
    return dict(seed=q, successor=successor, minimum=data["minimum"],
                current=result)


def predecessor_families(y):
    """All canonical T-predecessors: one optional point and two affine rays.

    Each returned ray starts at p and continues under p -> 64*p+49.
    """
    if not canonical(y):
        raise ValueError("The quotient state must be canonical")
    residue = y % 3
    if residue == 0:
        point = None
        rays = ((8*y + 3)//3, (16*y + 3)//3)
    elif residue == 1:
        point = None
        rays = ((4*y - 1)//3, (32*y + 19)//3)
    else:
        point = (2*y - 1)//3
        rays = ((64*y + 19)//3, (128*y + 83)//3)
    for p in rays + (() if point is None else (point,)):
        assert canonical(p) and quotient_step(p) == y
    return point, rays


def predecessors_up_to(y, bound):
    """Finite exact enumeration with an explicit integer height bound."""
    if not isinstance(bound, int) or bound < 1:
        raise ValueError("Expected a positive integer height bound")
    point, rays = predecessor_families(y)
    answer = []
    if point is not None and point <= bound:
        answer.append(point)
    for start in rays:
        p = start
        while p <= bound:
            answer.append(p)
            p = 64*p + 49
    return sorted(answer)


def least_predecessor(y):
    point, rays = predecessor_families(y)
    return min(rays) if point is None else point


def least_two_step_predecessor(y):
    """An exact finite search; greedy inverse minimization need not work.

    The greedy two-step predecessor is a valid upper bound B.  Since
    T(q)<=(3q+1)/2, any better q has intermediate state <=(3B+1)/2.
    """
    bound = least_predecessor(least_predecessor(y))
    middle = predecessors_up_to(y, (3*bound + 1)//2)
    return min(least_predecessor(p) for p in middle)
