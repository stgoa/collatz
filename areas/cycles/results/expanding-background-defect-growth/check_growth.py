#!/usr/bin/env python3
"""Exact finite checks for the expanding-background defect-growth theorem."""

import argparse
import itertools
import json
from fractions import Fraction
from math import gcd, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
RECEIPT = HERE / "check_growth.json"


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def constant(value):
    return {(0,) * 6: value} if value else {}


def variable(index):
    powers = [0] * 6
    powers[index] = 1
    return {tuple(powers): 1}


def plus(*polynomials):
    result = {}
    for polynomial in polynomials:
        for powers, coefficient in polynomial.items():
            result[powers] = result.get(powers, 0) + coefficient
    return {p: c for p, c in result.items() if c}


def times(left, right):
    result = {}
    for lp, lc in left.items():
        for rp, rc in right.items():
            powers = tuple(a + b for a, b in zip(lp, rp))
            result[powers] = result.get(powers, 0) + lc * rc
    return {p: c for p, c in result.items() if c}


def negative(polynomial):
    return {p: -c for p, c in polynomial.items()}


def symbolic():
    pp, qq, cc, xx, ee, bb = [variable(i) for i in range(6)]
    difference = plus(pp, negative(qq))
    left = plus(times(difference, plus(times(pp, xx), cc)), times(cc, qq))
    right = times(pp, plus(times(difference, xx), cc))
    require(left == right, "one-block shifted-coordinate polynomial identity failed")
    # P and Q now stand for the k-th powers; B is independent.
    left = plus(times(bb, times(pp, xx)), times(cc, plus(pp, negative(qq))),
                times(cc, times(qq, ee)))
    right = plus(times(pp, plus(times(bb, xx), cc)),
                 times(cc, times(qq, plus(ee, constant(-1)))))
    require(left == right, "group shifted-coordinate polynomial identity failed")
    return {"identities": ["B(Px+C)+CQ=P(Bx+C), B=P-Q",
                           "BP^k*x+C(P^k-Q^k)+CQ^k*2^e=P^k(Bx+C)+CQ^k(2^e-1)"],
            "both_polynomial_differences_zero": True}


def intercept(word):
    value, denominator = 0, 1
    for letter in word:
        value, denominator = 3 * value + denominator, denominator * 2**letter
    return value


def actual_states(word):
    cw, dd = intercept(word), 2**sum(word) - 3**len(word)
    require(dd > 0, "nonpositive word denominator in actual-state constructor")
    divisor = gcd(cw, dd)
    q, start = dd // divisor, cw // divisor
    states, state = [], start
    for letter in word:
        states.append(state)
        numerator = 3 * state + q
        require(numerator % 2**letter == 0, "ordinary arrow is not integral")
        state = numerator // 2**letter
        require(state > 0 and state % 2 == 1, "ordinary valuation is not exact")
    require(state == start, "ordinary word did not close")
    return q, states


def general_backgrounds():
    backgrounds = [u for length in range(1, 5)
                   for u in itertools.product((1, 2, 3), repeat=length)
                   if 3**length > 2**sum(u)]
    require(len(backgrounds) == 23, "background enumeration changed")
    positive, groups, integer_words, adjacent_groups = 0, 0, 0, 0
    totals = set()
    for base in backgrounds:
        pp, qq, cc = 3**len(base), 2**sum(base), intercept(base)
        bb = pp - qq
        for number in range(1, 6):
            for increases in itertools.product((0, 1, 3), repeat=number):
                word = tuple(letter for e in increases for letter in (*base[:-1], base[-1] + e))
                dd = 2**sum(word) - 3**len(word)
                if dd <= 0:
                    continue
                positive += 1
                q, states = actual_states(word)
                block_states = states[::len(base)]
                require(len(block_states) == number, "block clock mismatch")
                if q == 1:
                    integer_words += 1
                    require(set(word) == {2}, "unexpected nontrivial integer sample")
                block_product = prod(Fraction(pp * x + q * cc, pp * x) for x in block_states)
                require(block_product == Fraction(2**sum(word), 3**len(word)),
                        "block drift product failed")
                endings = [i for i, e in enumerate(increases) if e]
                require(endings, "positive denominator with no modifications")
                start = (endings[-1] + 1) % number
                y_values, length = [], 0
                begin, reciprocals = start, Fraction(0)
                for offset in range(number):
                    index = (start + offset) % number
                    x0, x = block_states[begin], block_states[index]
                    require(bb * x * qq**length + q * cc * qq**length
                            == pp**length * (bb * x0 + q * cc),
                            "within-group shifted coordinate failed")
                    require(x * qq**length >= pp**length * x0, "within-group growth failed")
                    reciprocals += Fraction(1, x)
                    length += 1
                    if not increases[index]:
                        continue
                    xn = block_states[(index + 1) % number]
                    yi, yn = bb * x0 + q * cc, bb * xn + q * cc
                    require(pp**length * yi == qq**length * (bb * 2**increases[index] * xn + q * cc),
                            "exact integral group identity failed")
                    require(yi % qq**length == 0 and yi >= qq**length,
                            "divisibility lower bound failed")
                    require(yn * qq**length <= pp**length * yi,
                            "power-chain first inequality failed")
                    require(reciprocals < Fraction(pp, bb * x0), "reciprocal geometric bound failed")
                    y_values.append(yi)
                    groups += 1
                    adjacent_groups += length == 1
                    begin, length, reciprocals = (index + 1) % number, 0, Fraction(0)
                require(length == 0 and len(y_values) == len(endings)
                        and prod(y_values) >= qq**number, "group product lower bound failed")
                totals.add((len(base), sum(base)))
    return {"backgrounds": len(backgrounds), "background_length_range": [1, 4],
            "background_letter_set": [1, 2, 3], "block_count_range": [1, 5],
            "increase_set": [0, 1, 3], "positive_denominator_words": positive,
            "groups_checked": groups, "groups_with_one_block": adjacent_groups,
            "denominator_one_words_all_trivial": integer_words,
            "background_length_total_pairs": sorted(totals)}


def cutoff():
    ratio = Fraction(271, 256)
    hs = sum(ratio**j for j in range(4))
    coefficient = 3 / hs
    margin = coefficient * 7120 - (178 + 341 * Fraction(69, 5))
    require(9**256 < 8**271 and hs == Fraction(73240879, 16777216),
            "rational gamma bound failed")
    require(7 * (4 + 1) < 64 and 172 + 6 == 178, "cutoff coefficient failed")
    require(7120**5 < 2**64 and margin == Fraction(3337644499, 366204395) and margin > 0,
            "cutoff base inequality failed")
    require(coefficient > Fraction(682, 7120), "cutoff persistence slope failed")
    return {"gamma_upper_bound": str(ratio), "H4_upper_bound": str(hs),
            "coefficient": str(coefficient), "N0": 7120, "positive_margin": str(margin),
            "maximum_blocks": 7119, "maximum_odd_word_length": 14238,
            "integer_power_comparisons": {"9^256<8^271": True, "7120^5<2^64": True}}


def arbitrary_substitutions():
    backgrounds = [u for length in range(1, 5)
                   for u in itertools.product((1, 2, 3), repeat=length)
                   if 3**length > 2**sum(u)]
    checked, groups, negative_changes, mixed_words = 0, 0, 0, 0
    for base in backgrounds:
        t, a = len(base), sum(base)
        pp, qq, kk = 3**t, 2**a, 2**(max(base) - 1)
        bb = pp - qq
        phase_intercepts = [intercept(base[j:] + base[:j]) for j in range(t)]
        sums = []
        for j in range(t):
            require(2**base[j] * phase_intercepts[(j + 1) % t] == 3 * phase_intercepts[j] - bb,
                    "phase intercept rotation failed")
            prefix, reciprocal = 0, Fraction(0)
            for r in range(t):
                reciprocal += Fraction(2**prefix, 3**r)
                prefix += base[(j + r) % t]
            sums.append(reciprocal)
        bound_s = max(sums) / (1 - Fraction(qq, pp))
        for number in range(1, 4):
            periodic = base * number
            for changed_count in (1, 2):
                for positions in itertools.combinations(range(len(periodic)), changed_count):
                    choices = [tuple(v for v in range(1, 5) if v != periodic[p]) for p in positions]
                    for replacements in itertools.product(*choices):
                        word = list(periodic)
                        for p, v in zip(positions, replacements):
                            word[p] = v
                        if 2**sum(word) <= 3**len(word):
                            continue
                        q, states = actual_states(word)
                        changes = [word[i] - periodic[i] for i in positions]
                        negative_changes += sum(e < 0 for e in changes)
                        mixed_words += min(changes) < 0 < max(changes)
                        start = (positions[-1] + 1) % len(word)
                        begin, length, total, reciprocal = start, 0, 0, Fraction(0)
                        y_values = []
                        for offset in range(len(word)):
                            index = (start + offset) % len(word)
                            x0, x = states[begin], states[index]
                            yi = bb * x0 + q * phase_intercepts[begin % t]
                            current_y = bb * x + q * phase_intercepts[index % t]
                            require(current_y * 2**total == 3**length * yi,
                                    "arbitrary-phase unchanged stretch failed")
                            require(x * 2**total >= 3**length * x0,
                                    "arbitrary-phase state lower bound failed")
                            reciprocal += Fraction(1, x)
                            length += 1
                            total += periodic[index]
                            e = word[index] - periodic[index]
                            if e == 0:
                                continue
                            next_index = (index + 1) % len(word)
                            xn, cn = states[next_index], q * phase_intercepts[next_index % t]
                            negative_part = max(-e, 0)
                            require(3**length * yi * 2**negative_part
                                    == 2**total * (bb * 2**(e + negative_part) * xn
                                                    + cn * 2**negative_part),
                                    "arbitrary-substitution group identity failed")
                            require(total > negative_part and 2**negative_part <= kk
                                    and yi % 2**(total - negative_part) == 0,
                                    "negative-change divisibility loss failed")
                            require(yi * kk >= 2**total
                                    and (bb * xn + cn) * 2**total <= kk * 3**length * yi,
                                    "arbitrary-substitution chain bound failed")
                            require(reciprocal < bound_s / x0, "phase reciprocal bound failed")
                            y_values.append(yi)
                            groups += 1
                            begin, length, total, reciprocal = next_index, 0, 0, Fraction(0)
                        require(length == 0 and len(y_values) == changed_count
                                and prod(y_values) * kk**changed_count >= qq**number,
                                "arbitrary-substitution product lower bound failed")
                        checked += 1
    require(negative_changes > 0 and mixed_words > 0, "decreasing or mixed-sign controls missing")
    return {"backgrounds": len(backgrounds), "copies_range": [1, 3],
            "changed_positions": [1, 2], "replacement_letters": [1, 4],
            "positive_denominator_words": checked, "groups_checked": groups,
            "decreased_positions_checked": negative_changes, "mixed_sign_words": mixed_words}


def local_exclusion():
    bits, max_length, guard = 25, 14238, 10000
    limit = 1 << bits
    total, count, longest, longest_seed, peak = 0, 0, 0, None, 1
    for seed in range(3, limit, 2):
        state, steps = seed, 0
        while state >= seed:
            require(steps < guard, f"descent guard exceeded for seed {seed}")
            raw = 3 * state + 1
            state = raw // (raw & -raw)
            steps += 1
            peak = max(peak, state)
        total += steps
        count += 1
        if steps > longest:
            longest, longest_seed = steps, seed
    require(count == (limit - 2) // 2, "descent seed range incomplete")
    require(total == 58580426 and longest == 188, "documented descent counts changed")
    three_power, numerator = 1, 1
    for length in range(1, max_length + 1):
        three_power *= 3
        numerator *= 3 * limit + 1
        require(numerator < 1 << (three_power.bit_length() + bits * length),
                f"exact product inequality failed at length {length}")
    return {"L": limit, "odd_seeds": count, "total_odd_steps": total,
            "maximum_local_steps": longest, "longest_descent_seed": longest_seed,
            "maximum_odd_state": peak, "per_seed_step_guard": guard,
            "product_inequality_lengths": [1, max_length],
            "product_inequalities_checked": max_length,
            "final_minimum_total": three_power.bit_length()}


def controls():
    fixture_path = REPO / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    fixtures = json.loads(fixture_path.read_text())["cycles"]
    require(len(fixtures) == 11 and {f["d"] for f in fixtures} == {5, 7, 13, 61},
            "standard control coverage failed")
    rows = []
    for fixture in fixtures:
        q, states, word = fixture["d"], fixture["states"], fixture["valuations"]
        require(len(states) == len(word), "standard control length failed")
        for i, (x, letter) in enumerate(zip(states, word)):
            require(x > 0 and x % 2 == 1
                    and 3 * x + q == 2**letter * states[(i + 1) % len(states)],
                    "standard control exact arrow failed")
        denominator = (2**sum(word) - 3**len(word)) // gcd(intercept(word), 2**sum(word) - 3**len(word))
        require(denominator > 1 and q % denominator == 0, "standard control denominator failed")
        rows.append({"q": q, "minimum": min(states), "odd_length": len(word),
                     "denominator": denominator})
    direct = []
    for word, expected_q, expected_states in [((2, 3), 23, [7, 11]), ((2, 5), 17, [1, 5])]:
        q, states = actual_states(word)
        require(q == expected_q and states == expected_states, "direct block control failed")
        require((states[0] + 7 * q) % 8 == 0, "direct q-coordinate divisibility failed")
        direct.append({"word": word, "q": q, "states": states, "q1_exclusion_applied": False})
    return {"standard_fixtures": rows, "direct_modified_block_controls": direct}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    receipt = {"status": "PASS", "symbolic": symbolic(), "general_backgrounds": general_backgrounds(),
               "arbitrary_substitutions": arbitrary_substitutions(),
               "cutoff": cutoff(), "local_exclusion": local_exclusion(), "controls": controls()}
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.write_receipt:
        RECEIPT.write_text(rendered)
    else:
        require(RECEIPT.exists() and RECEIPT.read_text() == rendered,
                "receipt differs; review changes before using --write-receipt")
    print(f"PASS: {receipt['general_backgrounds']['positive_denominator_words']} general-background words, "
          f"{receipt['arbitrary_substitutions']['positive_denominator_words']} arbitrary-substitution words, "
          "symbolic identities and cutoff, 16,777,215 descent seeds, "
          "14,238 product inequalities, 11 standard and 2 direct controls")


if __name__ == "__main__":
    main()
