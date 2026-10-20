"""Exact parameters for the S.1 fixed-factor stopping calibration.

No orbit search is used to construct the constants. The proof is in
STOPPING_CALIBRATION.md; all densities concern stopping below half the seed,
not absorption at 1. Raw shortcut and absorbed odd clocks stay separate.
"""
from fractions import Fraction
from math import comb, gcd


RATE = Fraction(16807, 18432)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, name, minimum=0):
    require(type(value) is int and value >= minimum, f"invalid {name}")


def check_d(d):
    integer(d, "d", 1)
    require(gcd(d, 6) == 1, "d must be positive and coprime to 6")


def check_epsilon(epsilon):
    require(type(epsilon) in (int, Fraction), "epsilon must be exact rational")
    epsilon = Fraction(epsilon)
    require(0 < epsilon <= 1, "epsilon must lie in (0,1]")
    return epsilon


def ceiling(value):
    value = Fraction(value)
    return -((-value.numerator) // value.denominator)


def mgf_bound(m):
    integer(m, "m", 1)
    return Fraction(8, 7) * RATE**m


def choose_m(epsilon, max_m=None):
    epsilon = check_epsilon(epsilon)
    # (1/RATE)^m >= 1 + m*(1/RATE-1), so this explicit finite bound
    # guarantees mgf_bound(m) <= epsilon/2. It is not a search cap premise.
    proved_limit = max(9, ceiling((Fraction(16, 7) / epsilon - 1)
                                  / (1 / RATE - 1)))
    limit = proved_limit
    if max_m is not None:
        integer(max_m, "m computation cap")
        limit = min(limit, max_m)
    for m in range(9, limit + 1):
        if mgf_bound(m) <= epsilon / 2:
            return m, proved_limit
    raise ValueError("m computation cap exhausted; constants not constructed")


def parameters(d, epsilon, max_m=None):
    check_d(d)
    epsilon = check_epsilon(epsilon)
    m, proved_limit = choose_m(epsilon, max_m)
    k = 5 * m
    bad_residues = sum(comb(k - 1, j) for j in range(3 * m, k))
    odd_period = 2**(k - 1)
    delta = Fraction(bad_residues, odd_period)
    Z = ceiling(Fraction(4 * d * 3**k, 2**k))
    E = bad_residues + (Z + 1) // 2
    M0 = ceiling(2 * E / epsilon)
    X0 = 2 * M0 - 1
    require(m >= 9 and Fraction(27, 32)**m < Fraction(1, 4),
            "insufficient contraction exponent")
    require(delta <= mgf_bound(m) <= epsilon / 2, "incorrect tail bound")
    return dict(d=d, epsilon=epsilon, m=m, proved_m_search_limit=proved_limit,
                shortcut_horizon=k, odd_horizon=k, integer_modulus=2**k,
                odd_residue_period=odd_period, bad_residues=bad_residues,
                delta=delta, mgf_bound=mgf_bound(m), Z=Z, E=E, M0=M0, X0=X0)


def failure_bound(plan, X):
    integer(X, "cutoff")
    return plan["delta"] * ((X + 1) // 2) + plan["E"]


def w5_parameters(epsilon, max_m=None):
    epsilon = check_epsilon(epsilon)
    ordinary = parameters(1, epsilon / 18, max_m)
    return dict(epsilon=epsilon, ordinary=ordinary,
                odd_horizon=ordinary["odd_horizon"],
                quotient_horizon=ordinary["odd_horizon"],
                X0=max(5, (ordinary["X0"] + 2) // 3),
                counting_ratio_bound=18)


def raw_shortcut(d, n):
    check_d(d)
    integer(n, "state", 1)
    return (3 * n + d) // 2 if n % 2 else n // 2


def raw_odd(d, n):
    check_d(d)
    integer(n, "odd state", 1)
    require(n % 2 == 1, "state must be odd")
    value = 3 * n + d
    return value // (value & -value)


def absorbed_odd(d, n):
    check_d(d)
    integer(n, "odd state", 1)
    require(n % 2 == 1, "state must be odd")
    return 1 if n == 1 else raw_odd(d, n)


def half_descent(d, n, horizon):
    """Exact finite-horizon predicate, with no claim about later times."""
    check_d(d)
    integer(n, "odd seed", 1)
    require(n % 2 == 1, "seed must be odd")
    integer(horizon, "odd horizon")
    x = n
    for j in range(horizon + 1):
        if 2 * x <= n:
            return dict(found=True, time=j, endpoint=x)
        if j < horizon:
            x = absorbed_odd(d, x)
    return dict(found=False, time=None, endpoint=x)


def json_exact(value):
    if isinstance(value, Fraction):
        return dict(numerator=value.numerator, denominator=value.denominator)
    if isinstance(value, dict):
        return {key: json_exact(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_exact(item) for item in value]
    return value
