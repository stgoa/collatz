"""An explicit shrinking coalescence family for the positive R_N residual.

Construction takes an absorption current through N as input.  It exposes only
the stated finite prefixes; it never searches for an outer seed's future.
"""

from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = spec_from_file_location("halving_transfer", HERE.parent / "complement_recursion/transfer.py")
TRANSFER = module_from_spec(spec)
spec.loader.exec_module(TRANSFER)
COMPLEMENT, LOCAL = TRANSFER.COMPLEMENT, TRANSFER.LOCAL
step, divergence, combine = TRANSFER.step, TRANSFER.divergence, TRANSFER.combine


def parameters(x):
    if not isinstance(x, int) or x <= 1 or x % 4 != 3:
        raise ValueError("The seed must be positive and 3 modulo4")
    a = ((x + 1) & -(x + 1)).bit_length() - 1
    t = (x + 1) >> a
    return a, t


def selected(x):
    if x <= 1 or x % 4 != 3:
        return False
    a, t = parameters(x)
    return t % 4 == pow(3, a, 4)


def path_current(path):
    # Absorption at1: self-loops used for algebra never become current rows.
    return dict(Counter(x for x in path[:-1] if x != 1))


def coalescence(x):
    """Return div D_x=delta_x-delta_((x-1)/2), with delta_1 killed."""
    a, t = parameters(x)
    if not selected(x):
        raise ValueError("Seed is in the complementary binary class")
    q = (x - 1) // 2
    left, right = [x], [q]
    for _ in range(a):
        left.append(step(left[-1]))
        right.append(step(right[-1]))
    assert left[-1] == right[-1]
    assert all(y == 3**j * 2**(a-j) * t - 1 for j, y in enumerate(left[:a]))
    assert all(y == 3**j * 2**(a-1-j) * t - 1 for j, y in enumerate(right[:a-1]))
    assert left[-2] == 4 * right[-2] + 1
    current = combine((1, path_current(left)), (-1, path_current(right)))
    expected = {x: 1}
    if q != 1:
        expected[q] = -1
    assert divergence(current) == expected
    return dict(root=x, smaller=q, a=a, t=t, left=left, right=right, current=current)


def selected_profile(N):
    _, _, residual = COMPLEMENT.residual_profile(N)
    return {x: c for x, c in residual.items() if selected(x)}


def binary_residue(a):
    """The complete class, not an exact valuation word beyond the first run."""
    return 2**a * (1 if a % 2 == 0 else 3) - 1, 2**(a+2)


def combined_residue(a, residue, modulus):
    """Combine the binary class with an R_N class modulo12 or36."""
    r, power = binary_residue(a)
    assert modulus in (12, 36) and residue % 4 == 3
    odd_modulus = modulus // 4
    index = ((residue - r) * pow(power, -1, odd_modulus)) % odd_modulus
    period = power * odd_modulus
    return (r + power * index) % period, period


def selected_mass_formula(N):
    """Exact O(log N) floor formula, without constructing R_N."""
    if not isinstance(N, int) or N < 8 or N % 8:
        raise ValueError("N must be a positive multiple of8")
    largest_a = (3 * N // 2).bit_length() - 1
    intervals = ((1, N, Fraction(3*N, 2), 3, 12),
                 (1, Fraction(9*N, 8), Fraction(3*N, 2), 7, 12),
                 (2, N, Fraction(9*N, 8), 7, 36),
                 (2, N, Fraction(9*N, 8), 19, 36))
    answer = 0
    for a in range(2, largest_a + 1):
        for weight, low, high, residue, modulus in intervals:
            r, period = combined_residue(a, residue, modulus)
            answer += weight * COMPLEMENT.strict_count(low, high, r, period)
    return answer


def certify_selected(N, lower_current):
    """Exact nonnegative current for the selected full-weight R_N atoms.

    The caller's finite current may be signed.  Its nonzero-row graph must
    absorb U_N by the finite component argument.  No higher absorption input
    or complete forward search is used by this conversion.
    """
    lower_current = {x: c for x, c in lower_current.items() if c}
    if divergence(lower_current) != LOCAL.count(N):
        raise ValueError("Supply an exact current for U_N")
    target = selected_profile(N)
    lower_edges = {x: step(x) for x in lower_current}
    smaller_source, bridge = {}, {}
    extra_edges = {}
    max_prefix = 0
    for x, c in target.items():
        data = coalescence(x)
        q = data["smaller"]
        assert q < N
        smaller_source[q] = smaller_source.get(q, 0) + c
        bridge = combine((1, bridge), (c, data["current"]))
        assert all(lower_edges.get(y) == z for y, z in zip(data["right"], data["right"][1:])
                   if y != 1)
        extra_edges.update({y: z for y, z in zip(data["left"], data["left"][1:]) if y != 1})
        max_prefix = max(max_prefix, data["a"])
    smaller_current = COMPLEMENT.extract_exact(smaller_source, lower_edges)
    signed_current = combine((1, bridge), (1, smaller_current))
    assert divergence(signed_current) == target
    assert all(c > 0 for c in signed_current.values())
    assert sum(signed_current.values()) == sum(smaller_current.values())
    signed_edges = {x: step(x) for x in signed_current}
    current = COMPLEMENT.extract_exact(target, signed_edges)
    assert set(current) <= set(lower_edges) | set(extra_edges)
    _, _, residual = COMPLEMENT.residual_profile(N)
    remaining = combine((1, residual), (-1, target))
    assert all(c > 0 for c in remaining.values())
    return dict(N=N, target=target, remaining=remaining, current=current,
                bridge=bridge, smaller_source=smaller_source,
                signed_current=signed_current, new_rows=sorted(set(extra_edges)-set(lower_edges)),
                largest_prefix_length=max_prefix)
