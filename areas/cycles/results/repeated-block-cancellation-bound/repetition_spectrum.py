"""Exact bounded-cancellation spectrum for valuation words u^k v.

The theorem is in REPETITION_SPECTRUM.md. These are finite constructors,
not a decision procedure for all cycles or for Collatz convergence.
"""
from math import gcd


def data(word):
    word = tuple(word)
    if not word or any(type(a) is not int or a < 1 for a in word):
        raise ValueError("nonempty positive integer valuation word required")
    c = a_sum = 0
    for a in word:
        c = 3 * c + (1 << a_sum)
        a_sum += a
    return c, 1 << a_sum, 3 ** len(word)


def prime_to_six_part(value):
    value = abs(value)
    if value == 0:
        raise ValueError("zero has no finite prime-to-six part")
    for p in (2, 3):
        while value % p == 0:
            value //= p
    return value


def repeat_data(u, v, k):
    if type(k) is not int or k < 0:
        raise ValueError("nonnegative integer repetition count required")
    cu, q, p = data(u)
    cv, s, r = data(v)
    du, dv = q - p, s - r
    qk, pk = q ** k, p ** k
    geometric = (qk - pk) // du
    c = r * cu * geometric + qk * cv
    d = s * qk - r * pk
    determinant = du * cv - dv * cu
    if du * c - cu * d != qk * determinant:
        raise AssertionError("commutator identity failed")
    g = gcd(c, d)
    return dict(C=c, D=d, cancellation=g,
                denominator=abs(d) // g, K=determinant,
                positive=d > 0, coprime_blocks=gcd(du, dv) == 1)


def exact_cycle(word):
    """Return the primitive-denominator integer realization, retaining repeats."""
    word = tuple(word)
    c, q, p = data(word)
    d = q - p
    if d <= 0:
        raise ValueError("positive rational cycle required")
    g = gcd(c, d)
    parameter, x = d // g, c // g
    first = x
    states = []
    for a in word:
        states.append(x)
        z = 3 * x + parameter
        actual = (z & -z).bit_length() - 1
        if actual != a:
            raise AssertionError("valuation mismatch")
        x = z >> a
        if gcd(x, parameter) != 1:
            raise AssertionError("reduced denominator changed")
    if x != first:
        raise AssertionError("cycle did not close")
    return parameter, states


def modular_period(u, v, cap=20000):
    """A certified period of g(k), or None if this finite search is capped.

    Track (Q^k,P^k,(Q^k-P^k)/(Q-P)) modulo M. The update is an
    invertible linear map, so a return to the initial triple is a period.
    It need not be the least period of the gcd sequence.
    """
    cu, q, p = data(u)
    cv, s, r = data(v)
    determinant = (q-p)*cv - (s-r)*cu
    if determinant == 0:
        raise ValueError("common-fixed-point case has no such modulus")
    modulus = prime_to_six_part(determinant)
    if modulus == 1:
        return 1
    initial = (1, 1, 0)
    qp, pp, geometric = initial
    for period in range(1, cap+1):
        qp, pp, geometric = (q*qp % modulus, p*pp % modulus,
                             (p*geometric+qp) % modulus)
        if (qp, pp, geometric) == initial:
            return period
    return None


def mechanical(m):
    if type(m) is not int or m < 1:
        raise ValueError("positive integer length required")
    a = (3 ** m).bit_length()
    return tuple(((i+1)*a)//m - (i*a)//m for i in range(m))


def high_family_repetitions(m):
    """A sufficient k>=2 for Q^k>=2P^k, using Bernoulli's inequality."""
    _, q, p = data(mechanical(m))
    return max(2, (p + (q-p) - 1) // (q-p))
