"""Exact finite-cone weights for the five-ray conditional forcing theorem.

This supplies combinations of REQUIRED packet certificates. It does not construct
those input certificates or prove their universal existence. Standard library only.
"""

from collections import defaultdict
from fractions import Fraction


MANTISSAS = (12, 14, 16, 18, 21)
R = Fraction(35, 27)
FIRST = 15
TRANSITIONS = ((-10, Fraction(1)), (3, Fraction(1, 3)),
               (-2, Fraction(1, 3)))


def grid_cutoff(k):
    """Integer grid point for nonnegative ordinal k=5*b+i."""
    assert isinstance(k, int) and k >= 0
    b, i = divmod(k, 5)
    return MANTISSAS[i] << b


def target_index(m):
    """First allowed grid cutoff at least the positive integer m."""
    if not isinstance(m, int) or m < 1:
        raise ValueError("m must be a positive integer")
    k = FIRST
    while grid_cutoff(k) < m:
        k += 1
    return k


def contraction(r=R):
    return r ** -10 + (r ** 3 + r ** -2) / 3


def sufficient_exponent(m, r=R):
    """First B with all-grid tail bound 6*r**k*(2/r**5)**B < 1.

    Required packet cutoffs are all a_i*2**b for 3 <= b < B.
    """
    assert r > 1 and r ** 5 > 2 and contraction(r) < 1
    assert all(Fraction(a, 1) / r ** i <= 12
               for i, a in enumerate(MANTISSAS))
    k = target_index(m)
    B = max(4, k // 5 + 1)
    beta = 2 / r ** 5
    while 6 * r ** k * beta ** B >= 1:
        B += 1
    return B


def solve_exact(matrix, rhs):
    """Gauss-Jordan elimination over Q; callers provide a nonsingular matrix."""
    n = len(rhs)
    assert len(matrix) == n and all(len(row) == n for row in matrix)
    augmented = [[Fraction(x) for x in row] + [Fraction(y)]
                 for row, y in zip(matrix, rhs)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if augmented[i][j])
        augmented[j], augmented[pivot] = augmented[pivot], augmented[j]
        value = augmented[j][j]
        augmented[j] = [x / value for x in augmented[j]]
        for i in range(n):
            if i == j or not augmented[i][j]:
                continue
            value = augmented[i][j]
            augmented[i] = [x - value * y
                            for x, y in zip(augmented[i], augmented[j])]
    answer = [row[-1] for row in augmented]
    assert all(sum(a * x for a, x in zip(row, answer)) == y
               for row, y in zip(matrix, rhs))
    return answer


def finite_forcing_plan(m, B=None):
    """Return exact finite positive-cone coefficients for target U_g(m).

    Fractions remain Fraction objects. `packet_weights[N]` is w_N/3,
    `comparison_weights[N]` is w_N. Upper and lower boundary dictionaries
    map counting-measure cutoffs to their nonnegative rational coefficients.
    `upper_boundary_mass < 1` is the integer-component forcing condition.
    Optional B selects a finite block directly; it need not meet that condition.
    """
    target = target_index(m)
    if B is None:
        B = sufficient_exponent(m)
    if not isinstance(B, int) or B < 4 or target >= 5 * B:
        raise ValueError("B must include the target and satisfy B >= 4")
    last = 5 * B - 1
    indices = list(range(FIRST, last + 1))
    n = len(indices)
    # M = I-A. Solve M^T w=e_target, so sum w_k delta_k isolates U_target.
    matrix = [[Fraction(i == j) for j in range(n)] for i in range(n)]
    for k in indices:
        for shift, coefficient in TRANSITIONS:
            ell = k + shift
            if FIRST <= ell <= last:
                matrix[ell - FIRST][k - FIRST] -= coefficient
    rhs = [Fraction(k == target) for k in indices]
    weights = solve_exact(matrix, rhs)
    assert all(w >= 0 for w in weights)
    lower, upper = defaultdict(Fraction), defaultdict(Fraction)
    for k, w in zip(indices, weights):
        for shift, coefficient in TRANSITIONS:
            ell = k + shift
            if ell < FIRST:
                lower[grid_cutoff(ell)] += w * coefficient
            elif ell > last:
                upper[grid_cutoff(ell)] += w * coefficient
    lower = {N: c for N, c in sorted(lower.items()) if c}
    upper = {N: c for N, c in sorted(upper.items()) if c}
    upper_mass = sum(c * (N // 2 - 1) for N, c in upper.items())
    return {
        "m": m,
        "target_cutoff": grid_cutoff(target),
        "target_index": target,
        "B": B,
        "r": R,
        "contraction": contraction(),
        "cutoffs": [grid_cutoff(k) for k in indices],
        "comparison_weights": {grid_cutoff(k): w
                               for k, w in zip(indices, weights)},
        "packet_weights": {grid_cutoff(k): w / 3
                           for k, w in zip(indices, weights)},
        "lower_boundary": lower,
        "upper_boundary": upper,
        "upper_boundary_mass": upper_mass,
        "forces_target": upper_mass < 1,
    }
