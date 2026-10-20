"""R91: exact finite rational basin supporting an all-word precision bound.

The finite classification supplies no positive Collatz absorption premise.
See SHADOW_PRECISION.md for the first-hit reduction and positive transfer.
"""

from array import array
from fractions import Fraction
from math import gcd

D, B, A, M = 7153, 299947, 3**12, 2**19
ROOT = -3 * B
BOUND = 7277133  # Strict upper bound on the positive numerator u.
V0, VP = 67839005952677, 2**18 * 3**18
Q0, QP = 70506316836123, 3 * 2**45
BASES = {
    0: (("ray0", 8, 3), ("ray1", 16, 3)),
    1: (("ray0", 4, -1), ("ray1", 32, 19)),
    2: (("point", 2, -1), ("ray0", 64, 19), ("ray1", 128, 83)),
}


def valuation(n):
    if type(n) is not int or not n:
        raise ValueError("valuation needs a nonzero integer")
    n = abs(n)
    return (n & -n).bit_length() - 1


def _normalize(n):
    # D=1 mod8, so these signed numerator residues equal rational residues.
    e = 0
    while n % 8 == 5:
        n = (n - D) // 4
        e += 2
    if n % 4 == 3:
        a = valuation(n + D)
        if ((n + D) // 2**a) % 4 == pow(3, a, 4):
            n = (n - D) // 2
            e += 1
    return n, e


def normalize(n):
    if type(n) is not int or n >= -D or n % 2 == 0 or gcd(n, D) != 1:
        raise ValueError("expected primitive odd numerator n < -D")
    return _normalize(n)


def _step(n):
    a = valuation(3 * n + D)
    n = (3 * n + D) // 2**a
    if n >= -D:
        return n, a  # The complement of x<-1 cannot return to the target.
    n, b = _normalize(n)
    return n, a + b


def step(n):
    if normalize(n)[0] != n:
        raise ValueError("rational source must be canonical")
    return _step(n)


def inverse(n, kind, index=0):
    if normalize(n)[0] != n:
        raise ValueError("rational target must be canonical")
    if type(index) is not int or index < 0:
        raise ValueError("ray index must be a nonnegative integer")
    choices = {name: (a, b) for name, a, b in BASES[n % 3]}
    if kind not in choices or (kind == "point" and index):
        raise ValueError("illegal inverse branch")
    a, b = choices[kind]
    p = (a * n + b * D) // 3
    e = a.bit_length() - 1
    scale = 64**index
    p = scale * p + 7 * D * (scale - 1) // 9
    e += 6 * index
    assert _step(p) == (n, e)
    return p, e


def weight(depth, cost):
    if any(type(x) is not int or x < 0 for x in (depth, cost)):
        raise ValueError("depth and cost must be nonnegative integers")
    k = max(0, (depth + 6) // 12)
    return Fraction(2**cost * A**k, 3**depth * M**k)


def family(returns, index=0):
    """All starts with at least the given return count in the original cell."""
    if any(type(x) is not int or x < 0 for x in (returns, index)):
        raise ValueError("return count and cell index must be nonnegative integers")
    precision = 19 * returns + 18
    residue = (-B * pow(D, -1, 2**precision)) % 2**precision
    modulus = 2**(19 * returns)
    ell0 = ((residue - V0) // 2**18 * pow(3**18, -1, modulus)) % modulus
    ell = ell0 + modulus * index
    v0, q = V0 + VP * ell, Q0 + QP * ell
    numerator = A**returns * (D * v0 + B)
    assert numerator % M**returns == 0
    center = numerator // M**returns
    assert (center - B) % D == 0
    v = (center - B) // D
    return dict(returns=returns, index=index, ell=ell, Q=q, v0=v0, v=v,
                target=3*v, horizon=12*returns+5)


def classify():
    """Exhaust the finite first-hit universe; any cap aborts verification.

    Every unclassified path is followed to the known root, an already
    classified state, the invariant complement, or a detected finite cycle.
    The 100000-arrow guard is a resource limit, never a nonmembership verdict.
    """
    state = array("b", [0]) * (BOUND // 2 + 1)
    depth = array("i", [0]) * len(state)
    cost = array("i", [0]) * len(state)
    large = {}

    def lookup(n):
        u = -n
        if u < BOUND:
            return state[u//2], depth[u//2], cost[u//2]
        return large.get(n, (0, 0, 0))

    def save(n, result):
        u = -n
        if u < BOUND:
            state[u//2], depth[u//2], cost[u//2] = result
        else:
            large[n] = result

    save(ROOT, (1, 0, 0))
    hits = []
    candidates = escapes = cycles = 0
    max_u = 0
    fingerprint = 14695981039346656037
    mask = 2**64 - 1
    for origin in range(-D-2, -BOUND, -2):
        if gcd(origin, D) != 1 or _normalize(origin)[0] != origin:
            continue
        candidates += 1
        n, path, seen = origin, [], set()
        while True:
            max_u = max(max_u, -n)
            if n >= -D:
                result = (-1, 0, 0)
                escapes += 1
                break
            result = lookup(n)
            if result[0]:
                break
            if n in seen:
                result = (-1, 0, 0)
                cycles += 1
                break
            if len(path) >= 100000:
                raise RuntimeError("finite basin path reached the resource cap")
            seen.add(n)
            nxt, e = _step(n)
            path.append((n, e))
            n = nxt
        for n, e in reversed(path):
            if result[0] == 1:
                result = (1, result[1]+1, result[2]+e)
            save(n, result)
        s, d, e = lookup(origin)
        assert s in (-1, 1)
        if s == 1:
            hits.append([-origin, d, e])
        # Reproducibility fingerprint, not a substitute for the enumeration.
        for value in (-origin, s+1, d, e):
            fingerprint = ((fingerprint ^ value) * 1099511628211) & mask
    return dict(candidates=candidates, hits=hits, escape_trees=escapes,
                cycles=cycles, largest_u=max_u, large_cache=len(large),
                cap_hits=0, classification_fingerprint=f"{fingerprint:016x}")
