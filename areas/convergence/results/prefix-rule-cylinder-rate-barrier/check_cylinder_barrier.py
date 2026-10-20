"""Exact prefix-rule checks and elementary survival-rate evidence.

The universal rate proof is in CYLINDER_RATES.md. Rates here concern binary
cylinder measure, not counts in a growing finite integer interval.
"""

import argparse
from collections import defaultdict
from fractions import Fraction
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent


def next_state(j, A, run, a, merger, halving, scale=1):
    j2, A2 = j + 1, A + a
    if scale * 3**(j2 + 1) < 2**(A2 + 1):
        return None
    if merger and a >= 3 and a % 2 and 3**j2 < 2**A2:
        return None
    if halving and run == 1 and a >= 3:
        return None
    if a == 1:
        run2 = run if run != -1 else int(3**(j + 1) < 2**(A + 2))
    else:
        run2 = -1
    return j2, A2, run2


def bit_survival(bits, merger=False, halving=False, partial_halving=False, scale=1):
    """Count equal-weight binary words; first valuation1 is conditioned on."""
    assert bits >= 2 and (not partial_halving or halving)
    states, unfinished = {(1, 1, 1): 1}, 0
    while states:
        following = defaultdict(int)
        for (j, A, run), count in states.items():
            for a in range(1, bits - A):
                state = next_state(j, A, run, a, merger, halving, scale)
                if state is not None:
                    following[state] += count
            # There is exactly one unfinished binary suffix per prefix.
            # An active halving run only needs a>=3, not its exact value.
            if not (partial_halving and run == 1 and bits - A >= 3):
                unfinished += count
        states = following
    return Fraction(unfinished, 2**(bits - 2))


def direct_bit_survival(bits, merger=False, halving=False, partial_halving=False):
    unfinished = 0
    for original in range(3, 2**bits, 4):
        x, j, A, run, accepted = original, 0, 0, -1, False
        while True:
            numerator = 3*x + 1
            a = (numerator & -numerator).bit_length() - 1
            if A + a >= bits:
                accepted = partial_halving and run == 1 and bits - A >= 3
                break
            j2, A2 = j + 1, A + a
            if 3**(j2 + 1) < 2**(A2 + 1):
                accepted = True
                break
            if merger and a >= 3 and a % 2 and 3**j2 < 2**A2:
                accepted = True
                break
            if halving and run == 1 and a >= 3:
                accepted = True
                break
            if a == 1:
                if run == -1:
                    run = int(3**(j + 1) < 2**(A + 2))
            else:
                run = -1
            x, j, A = numerator // 2**a, j2, A2
        unfinished += not accepted
    return Fraction(unfinished, 2**(bits - 2))


def odd_step_survival(steps, merger=False, halving=False):
    assert steps >= 1
    states = {(1, 1, 1): 1}
    for j in range(1, steps):
        following = defaultdict(int)
        # Above this total valuation, descent is already certified.
        largest_total = (3**(j + 2)).bit_length() - 2
        for (_, A, run), count in states.items():
            for a in range(1, largest_total - A + 1):
                state = next_state(j, A, run, a, merger, halving)
                if state is not None:
                    following[state] += count
        states = following
    return sum((Fraction(count, 2**(A - 1))
                for (_, A, _), count in states.items()), Fraction(0))


def nonnegative_compositions(length, total):
    """Count words with every 2^prefix_total <= 3^prefix_length."""
    counts = {0: 1}
    for j in range(1, length + 1):
        following = defaultdict(int)
        largest = min((3**j).bit_length() - 1, total - (length - j))
        for A, count in counts.items():
            for a in range(1, largest - A + 1):
                following[A + a] += count
        counts = following
    return counts.get(total, 0)


def step(x):
    numerator = 3*x + 1
    return numerator // (numerator & -numerator)


def high_halving_examples():
    examples = []
    for a in (10, 14, 18, 22):
        x, N = 2**a - 1, 12 * 2**(a - 4)
        q = (x - 1) // 2
        assert x % 12 == 3 and N < x < 3*N//2 and q < N
        left, right = [x], [q]
        for _ in range(a):
            left.append(step(left[-1]))
            right.append(step(right[-1]))
        z = (3**a - 1) // 8
        assert 3**a % 16 == 9
        assert left[-1] == right[-1] == z
        assert all(y > N for y in left)
        examples.append(dict(a=a, N=N, x=x, q=q, common_state=z,
                             common_height_over_N=str(Fraction(z, N)),
                             x_prefix=left, q_prefix=right))
    return examples


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    modes = ((False, False, False), (True, False, False),
             (True, True, False), (True, True, True))
    for bits in range(2, 15):
        for merger, halving, partial in modes:
            value = bit_survival(bits, merger, halving, partial)
            assert value == direct_bit_survival(bits, merger, halving, partial)
            assert value >= Fraction(1, 2**(bits - 2))

    external = json.loads((HERE / "external_review.json").read_text())
    tables = []
    for bits in (4, 8, 16, 32, 64, 96, 128):
        values = [bit_survival(bits, *mode) for mode in modes]
        assert all(values[j + 1] <= values[j] for j in range(3))
        if bits in (16, 32, 64, 96):
            claimed = external["reproduced"]["coalescence_check"]["undecided_D_DM_DMH"][str(bits)]
            assert list(map(float, values[:3])) == claimed
        tables.append(dict(bits=bits,
                           exact_fractions=list(map(str, values)),
                           decimals=list(map(float, values))))
    assert bit_survival(4, True, True, False) > bit_survival(4, True, True, True)

    cyclic_checks = []
    for n in range(1, 33):
        total = (3**n).bit_length() - 1
        good = nonnegative_compositions(n, total)
        all_words = math.comb(total - 1, n - 1)
        assert n * good >= all_words
        cyclic_checks.append(dict(length=n, total=total, good=good,
                                  all_compositions=all_words))
    for total in range(1, 65):
        n = 1
        while 3**n < 2**total:
            n += 1
        assert n * nonnegative_compositions(n, total) >= math.comb(total - 1, n - 1)

    # A fixed prefix closes the low-origin pending halving run, then escapes.
    state = (0, 0, -1)
    for a in (1, 1, 1, 2):
        state = next_state(*state, a, True, True)
        assert state is not None
    assert state == (4, 5, -1) and Fraction(3**4, 2**5) > 2
    x = 47
    for a in (1, 1, 1, 2):
        assert ((3*x+1) & -(3*x+1)) == 2**a
        x = step(x)

    odd_tables = []
    for n in (8, 16, 32, 64):
        values = [odd_step_survival(n, *mode[:2]) for mode in modes[:3]]
        odd_tables.append(dict(odd_steps=n, exact_fractions=list(map(str, values)),
                               decimals=list(map(float, values))))
    height_fits = []
    for scale in (1, 4, 16, 64):
        p96, p128 = bit_survival(96, scale=scale), bit_survival(128, scale=scale)
        height_fits.append(dict(scale=scale, fraction96=str(p96), fraction128=str(p128),
                                finite_rate_96_to_128=float(p128/p96)**(1/32)))
    c = math.log2(3)
    q = 1/c
    rho = c**c / (2**c * (c - 1)**(c - 1))
    beta = math.exp(-q*math.log(q)-(1-q)*math.log(1-q))/2
    assert abs(beta - rho**(1/c)) < 1e-14
    result = dict(status="PASS", proof="CYLINDER_RATES.md",
                  external_commit=external["ref"],
                  modes=["D", "D+M", "D+M+exact-closing-H", "D+M+partial-closing-H"],
                  brute_force_bit_range=[2, 14], fixed_bit_tables=tables,
                  fixed_odd_step_tables=odd_tables,
                  finite_shifted_height_fits=height_fits,
                  cyclic_rotation_count_checks=cyclic_checks,
                  bit_lower_bound_composition_totals=[1, 64],
                  escape_prefix=dict(valuations=[1,1,1,2], cylinder_residue=47,
                                     cylinder_modulus=64, slope="81/32"),
                  exact_rate_formulas=dict(c="log_2(3)", q="1/c",
                      rho="c^c / (2^c (c-1)^(c-1))",
                      beta="exp(-q log(q)-(1-q) log(1-q))/2",
                      rho_decimal=rho, beta_decimal=beta),
                  arbitrarily_high_common_state_examples=high_halving_examples(),
                  same_exponential_rate_for_specified_rules_proved=True,
                  constant_factor_equivalence_proved=False,
                  growing_integer_interval_count_proved=False,
                  arbitrary_bridge_impossibility_proved=False,
                  universal_termination_proved=False)
    path = HERE / "cylinder_audit.json"
    if args.write_receipt:
        path.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == result
    print(json.dumps(dict(status="PASS", rho_per_odd_step=rho,
                          beta_per_bit=beta, exact_rules_rate_proved=True,
                          coalescence_bit_budget_undercount_detected=True,
                          brute_force_bit_range=[2,14],
                          no_finite_integer_asymptotic_claim=True), indent=2))


if __name__ == "__main__":
    main()
