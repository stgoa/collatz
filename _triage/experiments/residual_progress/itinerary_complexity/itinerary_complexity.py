"""Exact repeated-factor constraints for the two R74 returns.

No function supplies or assumes an infinite positive survivor.  The trace
interface checks a supplied finite word, and the complexity bound is a
necessary condition if one fixed positive integer survives indefinitely.
"""

from fractions import Fraction


A = 3**12
M = 2**19
B = 311195
D = A - M
P = A * A
C = B * (A + M)
Q = 2**37
GUARD_BITS = 26
GUARD_MODULUS = 2**GUARD_BITS
GUARD_RESIDUE = 40529845
SHIFT = Fraction(B, D)
MAX_GROWTH = Fraction(P, Q)
ROWS = {"V": (A, B, 19), "R": (P, C, 37)}


def _word(word, *, allow_empty=False):
    if not isinstance(word, str) or any(symbol not in ROWS for symbol in word):
        raise ValueError("a word must be a string over V and R")
    if not allow_empty and not word:
        raise ValueError("a nonempty word is required")
    return word


def _positive_guard(w):
    if type(w) is not int or w <= 0 or w % GUARD_MODULUS != GUARD_RESIDUE:
        raise ValueError("a positive integer in the 26-bit guard is required")


def affine(word):
    """Return (a,c,e) for F_word(w)=(a*w+c)/2**e, in time order."""
    _word(word, allow_empty=True)
    a, c, e = 1, 0, 0
    for symbol in word:
        alpha, beta, bits = ROWS[symbol]
        a, c, e = alpha * a, alpha * c + beta * 2**e, e + bits
    return a, c, e


def cylinder(word):
    """The complete positive R74 cylinder; return (least residue, modulus)."""
    a, c, e = affine(word)
    modulus = 2**(GUARD_BITS + e)
    return ((2**e * GUARD_RESIDUE - c) * pow(a, -1, modulus)) % modulus, modulus


def step(w, symbol):
    """One checked positive return, with its endpoint in the guard."""
    _positive_guard(w)
    _word(symbol)
    if len(symbol) != 1:
        raise ValueError("step requires one symbol")
    alpha, beta, bits = ROWS[symbol]
    numerator = alpha * w + beta
    target, remainder = divmod(numerator, 2**bits)
    if remainder or target % GUARD_MODULUS != GUARD_RESIDUE:
        raise ValueError("the stated return is outside its complete domain")
    assert target > w
    return target


def trace(w, word):
    """Check a finite itinerary; leaving this subsystem raises ValueError."""
    _positive_guard(w)
    _word(word, allow_empty=True)
    states = [w]
    for symbol in word:
        states.append(step(states[-1], symbol))
    return states


def rational_periodic_point(word):
    """Negative rational point of a periodic word, as a scope control."""
    _word(word)
    a, c, e = affine(word)
    return Fraction(-c, a - 2**e)


def maximal_copies(w, word):
    """Exact number of consecutive complete copies of this fixed word.

    An unhandled next copy is only an exit from this particular repeated
    word, not absorption or an exit from every available return itinerary.
    """
    _positive_guard(w)
    _word(word)
    a, c, e = affine(word)
    defect = (a - 2**e) * w + c
    assert defect > 0
    order = (defect & -defect).bit_length() - 1
    assert order >= GUARD_BITS
    return (order - GUARD_BITS) // e


def distinct_initial_positions(w, length):
    """Exact lower bound on length-L factor complexity of a survivor.

    Return the count of j>=0 satisfying
       (D*w+B)*P**j <= D*2**(26+19*length+37*j).
    If an infinite positive itinerary exists, its factors beginning at
    precisely those initial positions are all different.  The returned
    integer is a conditional bound, never an existence assertion.
    """
    _positive_guard(w)
    if type(length) is not int or length < 1:
        raise ValueError("factor length must be a positive integer")

    def small_enough(j):
        return (D * w + B) * P**j <= D * 2**(GUARD_BITS + 19 * length + 37 * j)

    if not small_enough(0):
        return 0
    low, high = 0, 1
    while small_enough(high):
        low, high = high, 2 * high
    while high - low > 1:
        mid = (low + high) // 2
        if small_enough(mid):
            low = mid
        else:
            high = mid
    return low + 1


def pigeonhole_cutoff(length):
    """Return (cutoff, forbidden_prefix_length) for the binary-word test.

    No positive seed <= cutoff can make that many consecutive returns in
    this subsystem. Off-guard seeds have no such return at all. A zero
    cutoff means this particular inequality excludes no positive seed.
    This is not a Collatz stopping-time bound.
    """
    if type(length) is not int or length < 1:
        raise ValueError("factor length must be a positive integer")
    positions = 2**length
    numerator = D * 2**(GUARD_BITS + 19 * length + 37 * positions) - B * P**positions
    denominator = D * P**positions
    return max(0, numerator // denominator), positions + length


def repeated_factor(w, word, i, j, length):
    """Check one repeated factor in an actual supplied finite itinerary."""
    _word(word)
    if any(type(value) is not int for value in (i, j, length)):
        raise ValueError("factor positions and length must be integers")
    if not (0 <= i < j and length >= 1 and j + length <= len(word)):
        raise ValueError("invalid repeated-factor positions")
    factor = word[i:i + length]
    if factor != word[j:j + length]:
        raise ValueError("the two factors are different")
    states = trace(w, word)
    a, c, e = affine(factor)
    gap = states[j] - states[i]
    modulus = 2**(GUARD_BITS + e)
    assert gap > 0 and gap % modulus == 0
    # The comparison is exact and uses the initial seed, not a new lift.
    assert (D * states[j] + B) * Q**j <= (D * w + B) * P**j
    assert D * modulus * Q**j < (D * w + B) * P**j
    return {
        "factor": factor, "first_position": i, "second_position": j,
        "length": length, "consumed_bits": e,
        "gap_multiple": gap // modulus,
        "fixed_seed_integer_inequality_verified": True,
    }
