"""Exact odd-only rational cycles and the specified mechanical-word family.

Finite constructors/checks only; the universal statements are proved in
BALANCED_DENOMINATORS.md. No claim about all integer Collatz orbits.
"""
from fractions import Fraction
from math import gcd


def valuation2(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError('positive integer required')
    return (n & -n).bit_length() - 1


def word_data(word):
    word = tuple(word)
    if not word or any(type(a) is not int or a < 1 for a in word):
        raise ValueError('nonempty positive integer valuation word required')
    a_sum = 0
    intercept = 0
    for a in word:
        intercept = 3 * intercept + 2 ** a_sum
        a_sum += a
    denominator = 2 ** a_sum - 3 ** len(word)
    if denominator <= 0:
        raise ValueError('word has no positive rational cycle')
    return intercept, denominator


def rational_step(value):
    value = Fraction(value)
    p, q = value.numerator, value.denominator
    if p <= 0 or p % 2 == 0 or q % 2 == 0 or q % 3 == 0:
        raise ValueError('positive odd rational with denominator coprime to6 required')
    a = valuation2(3 * p + q)
    return Fraction(3 * p + q, q * 2 ** a), a


def cycle(word):
    word = tuple(word)
    b, denominator = word_data(word)
    first = Fraction(b, denominator)
    value = first
    states = []
    for a in word:
        states.append(value)
        value, actual = rational_step(value)
        if actual != a:
            raise AssertionError('affine fixed point has wrong exact valuation')
    if value != first:
        raise AssertionError('cycle did not close')
    return tuple(states)


def mechanical_word(k, total, intercept=0):
    if (type(k) is not int or type(total) is not int or k < 1 or total < k
            or type(intercept) is not int or not 0 <= intercept < k):
        raise ValueError('require integers total>=k>=1 and0<=intercept<k')
    return tuple(((j + 1) * total + intercept) // k
                 - (j * total + intercept) // k for j in range(k))


def reduced_denominator(k, total):
    mechanical_word(k, total)
    if 2 ** total <= 3 ** k:
        raise ValueError('positive cycle required')
    g = gcd(k, total)
    return 2 ** (total // g) - 3 ** (k // g)


def high_control(k):
    if type(k) is not int or k < 1:
        raise ValueError('positive integer length required')
    total = (3 ** k).bit_length()
    word = mechanical_word(k, total)
    states = cycle(word)
    d = reduced_denominator(k, total)
    if any(x.denominator != d for x in states):
        raise AssertionError('unexpected reduced denominator')
    return dict(length=k, total=total, primitive_length=k // gcd(k, total),
                word=word, denominator=d,
                integer_states=tuple(x.numerator for x in states),
                minimum=min(states))
