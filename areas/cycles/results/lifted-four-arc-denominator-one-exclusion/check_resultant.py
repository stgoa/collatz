#!/usr/bin/env python3
"""Exact algebra and finite controls for the lifted four-arc exclusion."""

import argparse
import json
from fractions import Fraction
from math import gcd, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
RECEIPT = HERE / "check_resultant.json"


def require(condition, message):
    if not condition:
        raise SystemExit(message)


# Sparse rational polynomials. Each exponent tuple records a monomial.
def const(value, n=4):
    return {(0,) * n: Fraction(value)} if value else {}


def var(index, n=4):
    powers = [0] * n
    powers[index] = 1
    return {tuple(powers): Fraction(1)}


def add(*items):
    result = {}
    for item in items:
        for powers, coefficient in item.items():
            result[powers] = result.get(powers, 0) + coefficient
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def scale(item, factor):
    return {powers: coefficient * factor for powers, coefficient in item.items()
            if coefficient * factor}


def mul(left, right):
    result = {}
    for lp, lc in left.items():
        for rp, rc in right.items():
            powers = tuple(a + b for a, b in zip(lp, rp))
            result[powers] = result.get(powers, 0) + lc * rc
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def square(item):
    return mul(item, item)


def terms(item):
    return [{"powers": list(p), "numerator": c.numerator, "denominator": c.denominator}
            for p, c in sorted(item.items())]


def symbolic_checks():
    # V=9^(2r-4), Z=8^(2r-4), with independent marker powers Q,R.
    vv, zz, qq, rr = [var(i) for i in range(4)]
    current, denominator = add(vv, scale(zz, -1)), zz
    for weight in (scale(qq, 4), const(8), scale(rr, 4)):
        current, denominator = add(scale(current, 9), denominator), mul(denominator, weight)
    current = add(mul(scale(vv, 81), current),
                  mul(denominator, add(scale(vv, 81), scale(zz, -64))))
    denominator = mul(denominator, scale(zz, 64))
    for weight in (scale(rr, 4), const(8)):
        current, denominator = add(scale(current, 9), denominator), mul(denominator, weight)
    current = add(scale(current, 9), denominator)  # Final b changes no intercept.
    xx2, yy2 = scale(zz, 4096), scale(vv, 6561)
    nn = scale(add(mul(qq, add(const(17), scale(rr, 32))), const(-162)), 18)
    zcoef = scale(mul(mul(qq, rr), add(scale(rr, 17), const(-162))), 4)
    expected = add(scale(square(yy2), 2048), mul(nn, mul(xx2, yy2)),
                   mul(zcoef, square(xx2)))
    require(scale(current, 2048) == expected, "symbolic block intercept failed")

    # Independent symbolic resultant in Q,T,R (fourth variable unused).
    qq, tt, rr = [var(i) for i in range(3)]
    kk = scale(mul(mul(qq, tt), square(rr)), Fraction(1, 16))
    aa = add(mul(add(scale(tt, 32), const(17)), rr), const(-162))
    bb = add(mul(qq, add(const(17), scale(rr, 32))), const(-162))
    ll = scale(mul(mul(qq, rr), aa), 4)
    nn = scale(bb, 18)
    ff = add(scale(mul(qq, square(aa)), 64), scale(mul(tt, square(bb)), -81))
    ee = add(square(ll), scale(mul(kk, square(nn)), -1))
    require(ee == mul(scale(mul(qq, square(rr)), Fraction(1, 4)), ff),
            "symbolic resultant factorization failed")

    # The polynomial equations used in the square-K branches.
    uu, rr = var(0), var(1)
    numerator = add(scale(square(uu), 2048), scale(uu, 2916))
    bracket = add(scale(mul(rr, add(scale(rr, 17), const(-162))), 4),
                  scale(mul(add(const(17), scale(rr, 32)), uu), -18))
    first_cleared = add(scale(mul(rr, numerator), 2), mul(uu, bracket))
    first_expected = scale(mul(uu, add(mul(add(scale(rr, 1760), const(-153)), uu),
                                        mul(rr, add(const(2592), scale(rr, 34))))), 2)
    require(first_cleared == first_expected, "first zero branch failed")
    second = add(scale(square(uu), 256), mul(add(const(288), scale(rr, -144)), uu),
                 scale(square(rr), 17), scale(rr, -162))
    require(add(numerator, scale(bracket, 2)) == scale(second, 8),
            "second zero branch failed")
    ratio_coefficients = []
    for ratio, quadratic, linear in [(Fraction(1, 2), Fraction(753, 4), 207),
                                     (Fraction(1), Fraction(129), 126),
                                     (Fraction(2), Fraction(36), -36)]:
        require(256 - 144 * ratio + 17 * ratio**2 == quadratic
                and 288 - 162 * ratio == linear, "dyadic-ratio substitution failed")
        ratio_coefficients.append({"ratio": str(ratio), "quadratic": str(quadratic),
                                   "linear": linear})
    # At R=U/4 the denominator in Q's quotient is U(559U+1872)/4.
    case_den = add(scale(mul(add(const(17), scale(uu, 8)), uu), 18),
                   scale(mul(uu, add(scale(uu, Fraction(17, 4)), const(-162))), -1))
    require(case_den == scale(mul(uu, add(scale(uu, 559), const(1872))), Fraction(1, 4)),
            "equal-valuation zero branch failed")
    require(16 * 512 - 8 * 559 == 3720 and 16 * 729 - 8 * 1872 == -3312,
            "lower power-of-two comparison failed")
    require(3720 * 2 - 3312 > 0 and 16 * 559 - 16 * 512 > 0
            and 16 * 1872 - 16 * 729 > 0, "strict quotient bounds failed")
    return {"intercept_variables": ["V", "Z", "Q", "R"],
            "intercept_terms": terms(expected), "resultant_variables": ["Q", "T", "R", "unused"],
            "reduced_resultant_terms": terms(ff), "square_K_ratio_substitutions": ratio_coefficients}


def intercept(word):
    value, denominator = 0, 1
    for letter in word:
        value, denominator = 3 * value + denominator, denominator * 2**letter
    return value


def family(r, a, b, c):
    base = [1] * (2 * r - 4) + [a, 1, c] + [1] * (2 * r - 2) + [c, 1, b]
    return base, [entry for letter in base for entry in (2, letter)]


def samples():
    count, positive, parity, branches, seven_control = 0, 0, [0, 0], [0, 0, 0], None
    for r in range(2, 9):
        xx, yy = 8**r, 9**r
        for a in range(1, 9):
            for b in range(1, 9):
                for c in range(2, 9):
                    base, word = family(r, a, b, c)
                    qq, tt, rr = 2**a, 2**b, 2**c
                    ss = a + b + 2 * c - 4
                    kk = 2**ss
                    nn = 18 * (qq * (17 + 32 * rr) - 162)
                    zz = 4 * qq * rr * (17 * rr - 162)
                    ll = 2048 * kk + zz
                    ff = (64 * qq * ((32 * tt + 17) * rr - 162)**2
                          - 81 * tt * (qq * (17 + 32 * rr) - 162)**2)
                    ee = ll**2 - kk * nn**2
                    cw, dd = intercept(word), 2**sum(word) - 3**len(word)
                    require(len(word) == 8 * r and sum(word) == 12 * r + ss,
                            "lift length or total failed")
                    require(16 * kk == qq * tt * rr**2 and dd == kk * xx**4 - yy**4,
                            "lift denominator identity failed")
                    require(2048 * cw == 7 * (2048 * yy**4 + nn * xx**2 * yy**2 + zz * xx**4),
                            "direct ordinary-word intercept failed")
                    require(ee == (qq * rr**2 // 4) * ff and ee != 0,
                            "sample resultant failed")
                    require(ll > 0 and nn > 0 and 2 * abs(ff) <= 1703025 * kk**2,
                            "positivity or uniform resultant bound failed")
                    expected = sum((a != 1, a != c, b != 1, b != c))
                    shift = 4 * r - 2
                    require(gcd(shift, len(word)) == 2 and
                            sum(word[i] != word[(i + shift) % len(word)] for i in range(len(word))) == expected,
                            "lift mismatch formula failed")
                    require(sum(letter >= 2 for letter in word) == 4 * r + 2 + (a >= 2) + (b >= 2),
                            "shortcut minima count failed")
                    if ss % 2 == 0:
                        tt_exp = ss // 2
                        branches[(c + 2 > tt_exp) - (c + 2 < tt_exp) + 1] += 1
                    if dd > 0:
                        gg = gcd(cw, dd)
                        require(49 * ff % gg == 0, "general cancellation divisor failed")
                        require(dd // gg > 1, "sample denominator-one word found")
                        positive += 1
                        if ff % gg and seven_control is None:
                            seven_control = {"r": r, "a": a, "b": b, "c": c,
                                             "C": cw, "D": dd, "gcd_C_D": gg,
                                             "gcd_F_g": gcd(ff, gg)}
                    count += 1
                    parity[ss % 2] += 1
    require(seven_control is not None, "missing nonunit-seven control")
    return {"ranges": {"r": [2, 8], "a": [1, 8], "b": [1, 8], "c": [2, 8]},
            "tuples": count, "positive_D_tuples": positive,
            "even_and_odd_totals": parity, "square_K_branch_counts_less_equal_greater": branches,
            "nonunit_seven_control": seven_control}


def structure_checks():
    examples = []
    require(3**16 > 2**25, "near-critical construction lower bound failed")
    for r in (16, 24, 32, 64):
        aa = (3 ** (8 * r)).bit_length()
        b = aa - 12 * r - 3
        _, word = family(r, 3, b, 2)
        require(b >= 6 and word.count(b) == 1, "unique-marker primitivity failed")
        require(sum(word) == aa and 3**len(word) < 2**aa < 2 * 3**len(word),
                "near-critical construction failed")
        minima = sum(letter >= 2 for letter in word)
        require(minima == 4 * r + 4, "growing minima construction failed")
        examples.append({"r": r, "a": 3, "b": b, "c": 2,
                         "m": len(word), "A": aa, "shortcut_minima": minima})
    _, word = family(3, 3, 5, 2)
    equal_total, backgrounds = [], set()
    for cut in range(len(word)):
        rotated = word[cut:] + word[:cut]
        for width in range(1, len(word) + 1):
            if len(word) % width:
                continue
            blocks = [tuple(rotated[i:i + width]) for i in range(0, len(word), width)]
            number = len(blocks)
            if number >= 3:
                for k in range(1, number):
                    left, right = blocks[0], blocks[k]
                    if left != right and sum(left) == sum(right) and blocks == [left] * k + [right] * (number - k):
                        equal_total.append((cut, width, k))
            if number >= 2 and len({b[:-1] for b in blocks}) == 1 and len({b[-1] for b in blocks}) > 1:
                backgrounds.add((width - 1, number))
    require(not equal_total and backgrounds == {(0, 24), (1, 12)}, "coverage comparison failed")
    return {"primitive_near_critical_examples": examples,
            "coverage_example": {"r": 3, "a": 3, "b": 5, "c": 2,
                                 "equal_total_two_block_representations": equal_total,
                                 "shared_background_length_and_copies": sorted(backgrounds)}}


def controls():
    path = REPO / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    fixtures = json.loads(path.read_text())["cycles"]
    require(len(fixtures) == 11 and {entry["d"] for entry in fixtures} == {5, 7, 13, 61},
            "control fixture coverage failed")
    result = []
    for entry in fixtures:
        d, states, word = entry["d"], entry["states"], entry["valuations"]
        require(len(states) == len(word) and len(set(states)) == len(states), "control period failed")
        for i, (state, letter) in enumerate(zip(states, word)):
            target = states[(i + 1) % len(states)]
            require(state > 0 and state % 2 == 1 and target % 2 == 1
                    and 3 * state + d == 2**letter * target, "control exact arrow failed")
        require(2**sum(word) * prod(states) == prod(3 * state + d for state in states),
                "general-d product identity failed")
        cw, dd = intercept(word), 2**sum(word) - 3**len(word)
        denominator = dd // gcd(cw, dd)
        require(dd > 0 and d % denominator == 0 and denominator > 1,
                "control denominator failed")
        result.append({"d": d, "minimum": min(states), "length": len(word),
                       "denominator": denominator, "q1_product_specialization_applied": False})
    return result


def finite_period_exclusion():
    limit = 2**21
    maximum_word_length = 4088
    step_guard = 10000
    total_steps, maximum_steps, longest_seed, maximum_odd, maximum_raw = 0, 0, None, 1, 4
    seeds = 0
    for seed in range(3, limit, 2):
        state, steps = seed, 0
        while state >= seed:
            require(steps < step_guard, f"descent guard exceeded for seed {seed}")
            raw = 3 * state + 1
            maximum_raw = max(maximum_raw, raw)
            state = raw // (raw & -raw)
            require(state > 0 and state % 2 == 1, "odd-step descent failed")
            maximum_odd = max(maximum_odd, state)
            steps += 1
        total_steps += steps
        seeds += 1
        if steps > maximum_steps:
            maximum_steps, longest_seed = steps, seed
    require(seeds == (limit - 2) // 2, "descent seed range incomplete")
    three_power, product_numerator = 1, 1
    for length in range(1, maximum_word_length + 1):
        three_power *= 3
        product_numerator *= 3 * limit + 1
        least_total = three_power.bit_length()
        require(product_numerator < 1 << (least_total + 21 * length),
                f"finite product inequality failed at length {length}")
    return {"L": limit, "odd_seeds": seeds, "total_odd_steps": total_steps,
            "maximum_local_steps": maximum_steps, "longest_descent_seed": longest_seed,
            "maximum_odd_state": maximum_odd, "maximum_raw_3x_plus_1": maximum_raw,
            "per_seed_step_guard": step_guard,
            "product_inequality_lengths": [1, maximum_word_length],
            "product_inequalities_checked": maximum_word_length,
            "last_least_total": least_total}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    require(64 * Fraction(81, 2)**2 * 16 == 1679616, "first coefficient bound failed")
    require(81 * Fraction(145, 4)**2 * 16 == 1703025, "second coefficient bound failed")
    require(1703025 < 2 * 2**20 and 49 < 2**6, "power-of-two bounds failed")
    require(172 + 26 + 3 * 341 == 1221, "gap exponent bookkeeping failed")
    require(12**8 > 2**10 * 5**8 and 10 * 2**9 > 1221 + 341 * 10,
            "exact exponential cutoff failed")
    require(10 * 2**9 > 341 and 8 * 511 == 4088,
            "dyadic induction or length bound failed")
    receipt = {"status": "PASS", "symbolic": symbolic_checks(), "samples": samples(),
               "structure": structure_checks(), "controls": controls(),
               "finite_period_exclusion": finite_period_exclusion(),
               "cutoff": {"base_left": 12**8, "base_right": 2**10 * 5**8,
                          "dyadic_left": 10 * 2**9, "dyadic_right": 1221 + 341 * 10,
                          "maximum_r": 511, "maximum_odd_word_length": 4088}}
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.write_receipt:
        RECEIPT.write_text(rendered)
    else:
        require(RECEIPT.exists() and RECEIPT.read_text() == rendered,
                "receipt differs; review changes before using --write-receipt")
    print(f"PASS: symbolic identities and cutoff, {receipt['samples']['tuples']} parameter tuples, "
          "1,048,575 descent seeds, 4,088 exact product inequalities, "
          "near-critical growing-minima examples, coverage comparison, 11 controls")


if __name__ == "__main__":
    main()
