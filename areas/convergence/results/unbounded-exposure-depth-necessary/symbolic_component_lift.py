"""Prove complete exposed-chain closure for an infinite congruence family.

The parameter is N=N0*q, where q>=1 and q=1 modulo a proved power of 3.
Every branch decision is verified symbolically on that entire half-line.
This is a finite arithmetic verifier for its stated N0 and D, not a proof
that a suitable base exists for arbitrary D.
"""

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache

from inverse_exposure_probe import COEFFICIENTS


@dataclass(frozen=True, order=True)
class Affine:
    a: Fraction
    b: Fraction

    def at_one(self):
        value = self.a + self.b
        assert value.denominator == 1
        return value.numerator

    def scale(self, factor):
        return Affine(self.a * factor, self.b * factor)

    def shift(self, offset):
        return Affine(self.a, self.b + offset)

    def minus(self, other):
        return Affine(self.a - other.a, self.b - other.b)

    def row(self):
        return [self.a.numerator, self.a.denominator,
                self.b.numerator, self.b.denominator]


def power_of_three(denominator):
    exponent = 0
    while denominator % 3 == 0:
        denominator //= 3
        exponent += 1
    assert denominator == 1
    return exponent


class UnstableDecision(Exception):
    """A numerical branch cannot be proved unchanged for every q>=1."""


def prove_chain_lift(N0, depth, query_cap=100000):
    """Verify all incoming/outgoing edges of the proposed depth-D component.

    Returns the complete query table and a compact exact receipt. Assertions
    check identities; UnstableDecision denotes a failed proposed lift, and
    RuntimeError denotes the explicit query cap. Neither means no lift exists.
    """
    assert N0 > 0 and N0 % 8 == 0 and depth >= 1
    assert (64 * N0) % (2 ** (depth + 3)) == 0
    max_denominator_power = 0
    congruence_power = 0
    inequality_count = 0
    constant_inequality_count = 0
    minimum_positive_slope = None
    minimum_positive_margin = None
    query_results = {}
    comparison_rows = []

    def sign_stable(expression, strict, label):
        """Require f(q)>=0 (or >0), for every real q>=1."""
        nonlocal inequality_count, constant_inequality_count
        nonlocal minimum_positive_slope, minimum_positive_margin
        value = expression.a + expression.b
        if expression.a < 0 or value < 0 or (strict and value == 0):
            raise UnstableDecision((label, expression.row(), str(value), strict))
        inequality_count += 1
        constant_inequality_count += expression.a == 0
        if expression.a > 0:
            minimum_positive_slope = (expression.a if minimum_positive_slope is None
                                      else min(minimum_positive_slope, expression.a))
        if value > 0:
            minimum_positive_margin = (value if minimum_positive_margin is None
                                       else min(minimum_positive_margin, value))
        comparison_rows.append([*expression.row(), bool(strict), label])

    def register_state(x):
        nonlocal max_denominator_power, congruence_power
        # The affine slope is even in the localization Z[1/3]. Thus q=1
        # modulo 3^(k+2) preserves the entire residue modulo 18.
        k = max(power_of_three(x.a.denominator), power_of_three(x.b.denominator))
        assert x.a > 0
        assert x.a.numerator % 2 == 0
        assert x.at_one() > 0 and x.at_one() % 2
        max_denominator_power = max(max_denominator_power, k)
        congruence_power = max(congruence_power, k + 2)

    zero = Affine(Fraction(0), Fraction(0))
    one = zero.shift(1)
    qbound = Affine(Fraction(9 * N0, 4), Fraction(0))
    bounds = []
    for r in range(depth + 1):
        slope = Fraction(3**r * 144 * N0, 2**r)
        assert slope.denominator == 1
        bounds.append(Affine(slope, Fraction(-1)))

    def coefficient_stable(x):
        register_state(x)
        value = x.at_one()
        if value <= 9 * N0 // 4:
            sign_stable(qbound.minus(x), False, "below_source_support")
            return 0
        if value >= 144 * N0:
            sign_stable(x.minus(qbound.scale(64)), False, "above_source_support")
            return 0
        band = (value // (9 * N0 // 4)).bit_length() - 1
        assert 0 <= band <= 5
        sign_stable(x.minus(qbound.scale(2**band)), True, "source_band_lower")
        sign_stable(qbound.scale(2 ** (band + 1)).minus(x), True, "source_band_upper")
        return COEFFICIENTS[band].get(value % 18, 0)

    def predecessors_stable(y, bound):
        register_state(y)
        residue = y.at_one() % 3
        if residue == 0:
            return
        power = 2 if residue == 2 else 4
        while True:
            test = bound.scale(3).shift(1).minus(y.scale(power))
            if test.a + test.b < 0:
                sign_stable(test.scale(-1), True, "first_excluded_predecessor")
                return
            sign_stable(test, False, "included_predecessor")
            p = y.scale(power).shift(-1).scale(Fraction(1, 3))
            register_state(p)
            # None of this witness's bounded ancestors is the absorber.
            sign_stable(p.minus(one), True, "predecessor_above_absorber")
            assert p.at_one() > 1
            yield p
            power *= 4

    @lru_cache(maxsize=None)
    def reachable(x, remaining):
        if len(query_results) >= query_cap:
            raise RuntimeError("symbolic reachability query cap")
        query_results[(x, remaining)] = None
        if coefficient_stable(x):
            answer = True
        elif remaining == 0:
            answer = False
        else:
            difference = x.minus(bounds[remaining])
            if difference.a + difference.b > 0:
                sign_stable(difference, True, "beyond_reachability_height")
                answer = False
            else:
                sign_stable(difference.scale(-1), False, "within_reachability_height")
                answer = any(reachable(p, remaining - 1)
                             for p in predecessors_stable(x, bounds[remaining - 1]))
        query_results[(x, remaining)] = answer
        return answer

    chain = [Affine(Fraction(64 * N0 * 3**j, 2**j), Fraction(-1))
             for j in range(depth + 3)]
    for x in chain:
        assert x.a.denominator == 1 and x.a.numerator % 2 == 0
        register_state(x)
    source_coefficients = [coefficient_stable(x) for x in chain]
    assert source_coefficients == [-2, 2, 2] + [0] * depth
    assert all(x.at_one() > 1 for x in chain)
    incoming = []
    for j, x in enumerate(chain):
        outgoing = reachable(x, depth - 1)
        assert outgoing == (j < len(chain) - 1)
        if outgoing:
            # Exact valuation one for every integer parameter q: the next
            # affine state has even slope and odd constant term.
            assert x.scale(3).shift(1) == chain[j + 1].scale(2)
        actual = [p for p in predecessors_stable(x, bounds[depth - 1])
                  if reachable(p, depth - 1)]
        expected = [] if j == 0 else [chain[j - 1]]
        assert actual == expected, (j, [p.row() for p in actual])
        incoming.append([p.row() for p in actual])

    queries = [[*x.row(), r, answer]
               for (x, r), answer in sorted(query_results.items())]
    assert all(row[-1] is not None for row in queries)
    assert congruence_power <= depth + 2
    receipt = dict(N0=N0, depth=depth, parameter="N=N0*q; q>=1; q=1 mod 3^K",
                   K=congruence_power,
                   maximal_denominator_power=max_denominator_power,
                   vertices=len(chain), arrows=len(chain) - 1,
                   source_coefficients=source_coefficients,
                   signed_source_mass=sum(source_coefficients), linked_to_1=False,
                   queries=len(queries), comparisons=inequality_count,
                   constant_comparisons=constant_inequality_count,
                   minimum_positive_slope=str(minimum_positive_slope),
                   minimum_positive_margin=str(minimum_positive_margin),
                   chain=[x.row() for x in chain],
                   dyadic_exponent_period=2 * 3 ** (congruence_power - 1),
                   all_comparisons_proved_for_every_real_q_at_least_1=True)
    return dict(receipt=receipt, queries=queries, comparisons=comparison_rows)
