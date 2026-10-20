#!/usr/bin/env python3
"""Exact bounded V003 examples; no frozen imports or all-input inference.

Default replay compares verification.json without modifying it.
Use --write-receipt only to replace the selected receipt deliberately.
"""

import argparse
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
DS = (1, 5, 7, 13, 61)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def v2(n):
    require(isinstance(n, int) and n > 0, "v2 requires a positive integer")
    return (n & -n).bit_length() - 1


def oddpart(n):
    return n >> v2(n)


def popcount(n):
    require(n >= 0, "popcount requires a nonnegative integer")
    return bin(n).count("1")


def validate_d(d):
    require(isinstance(d, int) and d > 0 and d % 2 == 1 and d % 3 != 0,
            "d must be positive odd and coprime to3")


def odd_step(n, d=1):
    validate_d(d)
    require(n > 0 and n % 2 == 1, "odd source required")
    if n == 1:
        return 1, None
    a = v2(3 * n + d)
    return (3 * n + d) >> a, a


def raw_shortcut(n, d):
    require(n >= 0, "raw parity template requires nonnegative input")
    return (3 * n + d) // 2 if n % 2 else n // 2


def digest(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return sha256(raw).hexdigest()


def check_digit_sum():
    family = []
    for k in range(2, 129):
        n = 32 * (2**k - 1) + 9
        y = 3 * n + 1
        require(n > 1 and n % 2 == 1, "digit-sum source domain failed")
        require(y == 32 * (3 * 2**k - 3) + 28, "digit blocks do not compose")
        require(popcount(3 * 2**k - 3) == k, "upper digit count failed")
        require((popcount(n), popcount(y)) == (k + 2, k + 3),
                "adjacent digit weights failed")
        endpoint, a = odd_step(n)
        require(endpoint == oddpart(y) and a == v2(y), "actual digit-family odd arrow failed")
        family.append([k, n, y, a])
    bridges = []
    for n, y, left, right in [(5, 16, 2, 1), (13, 40, 3, 2), (23, 70, 4, 3)]:
        require(3 * n + 1 == y and (popcount(n), popcount(y)) == (left, right),
                "small digit-weight bridge failed")
        require(odd_step(n)[0] == oddpart(y), "bridge odd-arrow normalization failed")
        bridges.append([n, y, left, right])
    # This tests the displayed nonperiod argument, not arbitrary automaticity.
    thue_witnesses = []
    for period in range(1, 65):
        L = period.bit_length() + 8
        witnesses = []
        for power in (L, L + 1):
            n = 2**power - period
            require(popcount(n) == power - popcount(period - 1),
                    "digit-complement formula failed")
            if popcount(n) % 2 != popcount(n + period) % 2:
                witnesses.append(n)
        require(witnesses, "Thue-Morse candidate period was not separated")
        thue_witnesses.append([period, witnesses[0]])
    require(popcount(3) == popcount(5) == 2 and 3 % 5 != 0 and 5 % 5 == 0,
            "d5 digit-count control failed")
    require(popcount(31) == popcount(61) == 5 and 31 % 61 != 0,
            "d61 digit-count control failed")
    return {"k_range": [2, 128], "family_count": len(family),
            "family_sha256": digest(family), "bridges": bridges,
            "Thue_Morse_periods_separated": len(thue_witnesses),
            "Thue_Morse_witness_sha256": digest(thue_witnesses)}


def parity_template(r, K, d):
    x, multiplier, intercept = r, 1, 0
    bits = []
    for i in range(K):
        bit = x % 2
        bits.append(bit)
        if bit:
            multiplier *= 3
            intercept = 3 * intercept + d * 2**i
        x = raw_shortcut(x, d)
    j = sum(bits)
    positions = [i for i, bit in enumerate(bits) if bit]
    independent_b = d * sum(3**(j - index - 1) * 2**position
                            for index, position in enumerate(positions))
    require(multiplier == 3**j and intercept == independent_b, "shortcut affine composition failed")
    require(multiplier * r + intercept == 2**K * x, "template endpoint failed")
    require((multiplier * r + intercept) % 2**K == 0, "template residue failed")
    require(j == 0 or intercept % 3 != 0, "intercept must be a ternary unit")
    return bits, j, intercept


def check_cylinders():
    targets = (1, 5, 7, 19, 61, 235)
    primitive_orders = []
    for j in range(1, 6):
        modulus, order = 3**j, 2 * 3**(j - 1)
        powers = {pow(2, i, modulus) for i in range(order)}
        require(powers == {i for i in range(modulus) if i % 3}, "powers2 miss a ternary unit")
        require(pow(2, order, modulus) == 1, "ternary unit period failed")
        primitive_orders.append(order)
    rows, shortcut_arrows, odd_arrows, max_clock, max_bits = [], 0, 0, 0, 0
    parity_classes = 0
    for d in DS:
        for K in range(6):
            words = set()
            for r in range(2**K):
                bits, j, b = parity_template(r, K, d)
                words.add(tuple(bits))
                parity_classes += 1
                for target in targets:
                    require(target % 2 == 1 and gcd(target, 3) == 1, "target domain failed")
                    if j:
                        modulus, period = 3**j, 2 * 3**(j - 1)
                        candidates = [s for s in range(period)
                                      if pow(2, K + s, modulus) * target % modulus == b % modulus]
                        require(len(candidates) == 1, "unit congruence did not have one period solution")
                        s0 = candidates[0]
                    else:
                        require(r == 0 and b == 0, "all-even class is wrong")
                        period, s0 = 1, 0
                    # A direct sufficient height threshold; no unbounded search.
                    required_s = max(0, (b + 3**j * 2**K).bit_length() - K)
                    repeats = max(0, (required_s - s0 + period - 1) // period)
                    s0 += period * repeats
                    previous_n = 0
                    for lift in (0, 1):
                        s = s0 + lift * period
                        numerator = 2**(K + s) * target - b
                        require(numerator % 3**j == 0, "inverse source is not integral")
                        n = numerator // 3**j
                        require(n > 2**K and n > previous_n and n % 2**K == r,
                                "inverse source height, growth or residue failed")
                        previous_n = n
                        x, states, actual_bits = n, [n], []
                        for _ in range(K):
                            require(x > 1, "raw template touched absorber before endpoint")
                            actual_bits.append(x % 2)
                            x = raw_shortcut(x, d)
                            states.append(x)
                        require(actual_bits == bits and x == 2**s * target,
                                "actual parity cylinder or endpoint failed")
                        for _ in range(s):
                            require(x > 1 and x % 2 == 0, "claimed final halving was not legal")
                            x //= 2
                            states.append(x)
                        require(x == target and all(y > 1 for y in states[:-1]),
                                "constructed path violates absorption at1")
                        odd_states = [y for y in states if y % 2]
                        require(odd_states[0] == oddpart(n) and odd_states[-1] == target,
                                "odd-clock compression endpoints failed")
                        for left, right in zip(odd_states, odd_states[1:]):
                            require(odd_step(left, d)[0] == right, "compressed path is not actual Syracuse")
                        shortcut_arrows += K + s
                        odd_arrows += len(odd_states) - 1
                        max_clock = max(max_clock, K + s)
                        max_bits = max(max_bits, n.bit_length())
                        rows.append([d, K, r, target, lift, s, n, j])
            require(len(words) == 2**K, "parity words are not a complete finite bijection")
    return {"d": list(DS), "K_range": [0, 5], "targets": list(targets),
            "parity_classes": parity_classes, "predecessor_paths": len(rows),
            "lifts_per_class_and_target": 2, "shortcut_arrows": shortcut_arrows,
            "odd_arrows_after_initial_halvings": odd_arrows, "largest_shortcut_clock": max_clock,
            "largest_source_bits": max_bits, "unit_orders": primitive_orders,
            "paths_sha256": digest(rows),
            "scope": "Two explicit lifts per case; unbounded predecessor supply is a separate written proof."}


def check_kernel_arithmetic():
    rows, nonsingular, divisible = [], 0, 0
    for a in range(7):
        for r in range(2**a):
            for j in range(3):
                c = 2**a * j + r
                if c % 3:
                    exponent = 1 if c % 3 == 2 else 2
                    offset = (2**exponent * c - 1) // 3
                    require(offset % 2 == 1 and 0 <= offset < 2**(a + exponent),
                            "binary-kernel inverse offset is outside its domain")
                    for n in range(6):
                        source = 2**(a + exponent) * n + offset
                        target = 3 * 2**a * n + c
                        require(3 * source + 1 == 2**exponent * target,
                                "kernel affine branch failed")
                        endpoint, actual_a = odd_step(source)
                        require(endpoint == oddpart(target), "kernel branch has wrong actual odd endpoint")
                        if source != 1:
                            require(actual_a == exponent + v2(target), "missing additional target valuation")
                        nonsingular += 1
                        rows.append([a, r, j, n, source, target])
                else:
                    offset = c // 3
                    require(0 <= offset < 2**a, "divisible kernel offset failed")
                    for n in range(6):
                        inner = 2**a * n + offset
                        require(3 * 2**a * n + c == 3 * inner, "f1 section index failed")
                        if offset:
                            removed = v2(offset)
                            u = offset >> removed
                            odd_inner = 2**(a - removed) * n + u
                            require(inner == 2**removed * odd_inner and odd_inner % 2,
                                    "f1 binary section reduction failed")
                            origin, lifted = 3 * odd_inner, 16 * odd_inner + 1
                            lifted_next = odd_step(lifted)[0]
                            require(lifted_next == 12 * odd_inner + 1
                                    and odd_step(lifted_next)[0] == odd_step(origin)[0],
                                    "f1 common endpoint at clocks1,2 failed")
                        elif n:
                            require(oddpart(3 * inner) == oddpart(3 * n), "f1 zero section failed")
                        divisible += 1
                        rows.append([a, r, j, n, inner])
    pure_paths, pure_arrows = [], 0
    for t in range(13):
        for u in range(1, 18, 2):
            origin, lifted = 3**t * u, 4**(t + 1) * u + 1
            x = lifted
            for i in range(t + 1):
                x, _ = odd_step(x)
                if i < t:
                    require(x == 4**(t - i) * 3**(i + 1) * u + 1,
                            "pure-zero intermediate merger state failed")
            require(x == odd_step(origin)[0], "pure-zero odd-section merger failed")
            pure_paths.append([t, u, origin, lifted, x])
            pure_arrows += t + 2
    pair_checks = 0
    for t in range(13):
        for n in range(9):
            pairs = [(3**t * (6 * n + 1), 3**t * (2 * (3 * n) + 1)),
                     (3**t * (6 * n + 4), 2 * 3**t * (3 * n + 2)),
                     (3**t * (6 * n + 2), 2 * 3**t * (3 * n + 1)),
                     (3**t * (6 * n + 5), 3**t * (2 * (3 * n + 2) + 1))]
            require(all(left == right for left, right in pairs), "mixed-section argument identity failed")
            pair_checks += 4
    return {"binary_depth_range": [0, 6], "index_samples": [0, 5],
            "nondivisible_actual_branches": nonsingular, "divisible_index_checks": divisible,
            "affine_samples_sha256": digest(rows), "pure_zero_t_range": [0, 12],
            "pure_zero_mergers": len(pure_paths), "pure_zero_arrow_or_absorber_steps": pure_arrows,
            "pure_zero_sha256": digest(pure_paths), "mixed_pair_index_equalities": pair_checks,
            "scope": "Arithmetic identities and actual common endpoints; no sampled constant coloring and no finite-kernel theorem inferred."}


def chi(odd):
    require(odd % 2 != 0, "chi requires an odd residue, possibly negative")
    return 1 if odd % 8 in (1, 3) else -1


def scaling_color(n):
    return chi(oddpart(n))


def check_scaling_counterexample():
    for n in range(1, 513):
        require(scaling_color(2 * n) == scaling_color(n)
                and scaling_color(3 * n) == scaling_color(n), "scaling invariance failed")
    require(odd_step(3)[0] == 5 and scaling_color(3) != scaling_color(5),
            "scaling control must fail actual Collatz invariance")
    mixed = []
    for t in range(1, 10):
        for s in range(1, 10):
            if t == s:
                continue
            delta = 3**t - 3**s
            a = v2(abs(delta))
            D = delta // 2**a
            K, modulus = a + 4, 3**t
            v_mod8 = 1 if chi(D) == -1 else 5
            if modulus == 1:
                v = v_mod8
            else:
                residue = pow(2**K, -1, modulus)
                v = v_mod8 + 8 * ((residue - v_mod8) * pow(8, -1, modulus) % modulus)
            numerator = 2**K * v - 1
            require(v > 0 and v % 2 and numerator % modulus == 0, "mixed witness CRT failed")
            n = numerator // modulus
            left, right = 3**t * n + 1, 3**s * n + 1
            parenthesis = 3**s * 2**(K - a) * v + D
            require(n > 0 and parenthesis > 0 and parenthesis % 2,
                    "mixed witness positivity or exact valuation failed")
            require(3**t * right == 2**a * parenthesis and parenthesis % 8 == D % 8,
                    "mixed witness affine separation failed")
            require(scaling_color(left) == chi(v) != chi(D) == scaling_color(right),
                    "mixed ternary sections were not separated")
            mixed.append([t, s, n, left, right, scaling_color(left), scaling_color(right)])
    nonperiod = []
    for period in range(1, 129):
        a, m = v2(period), oddpart(period)
        u = 1 if chi(m) == -1 else 5
        for threshold in (1, 10**6):
            k = max(4, threshold.bit_length() + 1)
            n = 2**(a + k) * u
            require(n > threshold and oddpart(n + period) == 2**k * u + m,
                    "nonperiod witness normalization failed")
            require(scaling_color(n) != scaling_color(n + period), "candidate period was not separated")
            nonperiod.append([period, threshold, n])
    return {"scaling_inputs": 512, "scaling_equalities": 1024,
            "actual_invariance_failure": [3, 5], "mixed_t_s_range": [1, 9],
            "ordered_mixed_pairs": len(mixed), "mixed_witness_sha256": digest(mixed),
            "mixed_examples": [row for row in mixed if row[:2] in ([1, 2], [2, 1], [8, 9], [9, 8])],
            "candidate_period_range": [1, 128], "thresholds": [1, 10**6],
            "nonperiod_witnesses": len(nonperiod), "nonperiod_sha256": digest(nonperiod)}


def base3_value(states):
    value = 0
    for state in states:
        value = 3 * value + sum(state)
    return value


def check_carry_patch():
    columns, remainders = {0: [(1, 0), (1, 1)]}, {}
    vertical = []
    for x in range(-1, -6, -1):
        incoming, remainder = columns[x + 1], 0
        outgoing = []
        for state in incoming:
            old_remainder = remainder
            total = remainder + sum(state)
            completed = (remainder, total // 2)
            remainder = total % 2
            require(sum(completed) == (3 * old_remainder + sum(state)) // 2,
                    "vertical base3 division digit failed")
            outgoing.append(completed)
            vertical.append([x, list(state), old_remainder, list(completed), remainder])
        require(base3_value(incoming) == 2 * base3_value(outgoing) + remainder,
                "vertical whole-number division failed")
        columns[x], remainders[x] = outgoing, remainder
    require([columns[x] for x in (-1, -2, -3)]
            == [[(0, 0), (1, 1)], [(0, 0), (0, 1)], [(0, 0), (0, 0)]],
            "vertical conversion states differ from the displayed patch")
    binary_input = sum(remainders[x] * 2**(-x - 1) for x in range(-1, -6, -1))
    require(binary_input == 5, "conversion bottom bits do not encode5")
    row, emitted, horizontal = {0: (0, 1)}, {}, []
    for x in range(-1, -7, -1):
        current_sum = remainders.get(x, 0)
        east = row[x + 1]
        total = current_sum + sum(east)
        row[x], emitted[x] = (current_sum, total // 2), total % 2
        horizontal.append([x, current_sum, list(east), total, list(row[x]), emitted[x]])
    require([row[x] for x in range(-1, -6, -1)]
            == [(1, 1), (0, 1), (1, 1), (0, 1), (0, 0)], "horizontal carry states failed")
    require(row[-6] == (0, 0) and emitted[-6] == 0, "constant west-tail rule failed")
    binary_output = sum(bit * 2**(-x - 1) for x, bit in emitted.items())
    require(binary_output == 16 == 3 * binary_input + 1, "carry flush output failed")
    require(row[-4] == (0, 1) and (remainders[-5] + sum((0, 0))) % 2 == 0
            and emitted[-5] == 1, "discarded-carry counterexample failed")
    rectangle = [[list(columns[x][0]) for x in range(-5, 1)],
                 [list(columns[x][1]) for x in range(-5, 1)],
                 [list(row[x]) for x in range(-5, 1)]]
    expected = [[[0, 0]] * 5 + [[1, 0]],
                [[0, 0], [0, 0], [0, 0], [0, 1], [1, 1], [1, 1]],
                [[0, 0], [0, 1], [1, 1], [0, 1], [1, 1], [0, 1]]]
    require(rectangle == expected, "complete carry rectangle failed")
    column_values = [base3_value(columns[x] + [row[x]]) for x in (-1, -2, -3, -4)]
    require(column_values == [8, 4, 2, 1], "column shortcut readings failed")
    x = 5
    for expected_value in column_values:
        x = raw_shortcut(x, 1)
        require(x == expected_value, "actual shortcut trajectory disagrees with columns")
    require(odd_step(5) == (1, 4), "odd-only diagram clock failed")
    for t in range(17):
        require(odd_step(5 + 32 * t) == (1 + 6 * t, 4), "exact low-bit arrow cylinder failed")
    for B in range(5, 17):
        n = 5 + 2**B
        require(n % 2**B == 5 and odd_step(n) == (1 + 3 * 2**(B - 4), 4),
                "finite low-bit boundary ambiguity failed")
    return {"rectangle_rows_y2_y1_y0": rectangle, "vertical_divisions": [[5, 2, 1], [2, 1, 0], [1, 0, 1]],
            "nonzero_conversion_digit_transitions": 6, "zero_column_digit_transitions": 4,
            "horizontal_nonzero_transitions": 5, "horizontal_zero_tail_transition": 1,
            "transition_sha256": digest([vertical, horizontal]), "binary_input": binary_input,
            "binary_output": binary_output, "column_values": column_values,
            "shortcut_arrows": 4, "odd_arrows": 1, "odd_valuation": 4,
            "exact_cylinder_samples": 17, "boundary_ambiguity_samples": 12,
            "boundary_scope": "Bootstrap and entire zero/undefined rays are supplied data; finite replay does not infer them.",
            "parallel_update_count": "not asserted"}


def check_controls():
    cycles = []
    for d, start, length, total in [(5, 19, 3, 5), (61, 235, 41, 66)]:
        states, valuations, x = [start], [], start
        for _ in range(length):
            x, a = odd_step(x, d)
            states.append(x)
            valuations.append(a)
        require(states[-1] == start and len(set(states[:-1])) == length
                and min(states) == start and 1 not in states,
                "known nonabsorbing cycle failed under absorber1")
        require(sum(valuations) == total, "cycle valuation total failed")
        cycles.append({"d": d, "states": states, "valuations": valuations,
                       "length": length, "total_valuation": total,
                       "absorber": 1, "status": "nonabsorbing cycle"})
    for d in DS:
        require(odd_step(1, d) == (1, None), "absorber must not use raw odd arithmetic")
    require(raw_shortcut(1, 7) == 5 and odd_step(1, 7) == (1, None),
            "d7 raw/absorbed distinction failed")
    require(odd_step(5, 5)[0] == 5 and odd_step(61, 61)[0] == 61,
            "multiples-of-d fixed-point controls failed")
    doubling_checks, odd_checks, ordinary_checks = 0, 0, 0
    affine_failures = []
    for d, m in ((5, 1), (61, 15)):
        color = lambda n: int(n % d == 0)
        require(color(1) == 0 and color(d) == 1, "divisibility coloring is not nonconstant")
        for n in range(1, 2 * d + 1):
            require(color(2 * n) == color(n) == color(oddpart(n)),
                    "divisibility coloring failed doubling/oddpart invariance")
            doubling_checks += 1
            if n % 2:
                require(color(odd_step(n, d)[0]) == color(n),
                        "divisibility coloring failed actual absorbed Syracuse invariance")
                odd_checks += 1
                if n > 1:
                    require(color(3 * n + d) == color(n),
                            "divisibility coloring failed its ordinary odd-source identity")
                    ordinary_checks += 1
        left, right = 3 * m + 1, 4 * m + 1
        require(color(left) == 0 and color(right) == 1,
                "the d1 affine section identity must fail for this d-control")
        affine_failures.append({"d": d, "m": m, "left": left, "right": right,
                                "left_color": color(left), "right_color": color(right),
                                "refuted_transfer": "h(3m+1)=h(4m+1)"})
    # Each binary class contains both colors; finite CRT examples exercise the control hypothesis.
    crt_examples = 0
    for d in (5, 61):
        for K in range(6):
            for r in range(2**K):
                for residue in (0, 1):
                    n = r + 2**K * ((residue - r) * pow(2**K, -1, d) % d)
                    n += d * 2**K
                    require(n > 0 and n % 2**K == r and n % d == residue,
                            "cycle-control binary CRT failed")
                    crt_examples += 1
    return {"cycles": cycles, "fixed_points_outside_absorber": [5, 61],
            "divisibility_color_doubling_and_oddpart_checks": doubling_checks,
            "divisibility_color_actual_odd_checks": odd_checks,
            "divisibility_color_ordinary_odd_checks": ordinary_checks,
            "d1_affine_identity_transfer_failures": affine_failures,
            "binary_CRT_color_examples": crt_examples, "d7_raw_at1": 5, "d7_absorbed_at1": 1}


def report():
    return {"schema": 1, "status": "PASS",
            "verifier_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
            "scope": "Bounded exact arithmetic examples only. Written all-input proofs, external theorems and automatic-coloring closure are not established by this replay.",
            "digit_sum": check_digit_sum(), "cylinders": check_cylinders(),
            "kernel_arithmetic": check_kernel_arithmetic(), "scaling_control": check_scaling_counterexample(),
            "carry_patch": check_carry_patch(), "cycle_controls": check_controls()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    parser.add_argument("--receipt", type=Path, default=HERE / "verification.json")
    args = parser.parse_args()
    try:
        actual = report()
        if args.write_receipt:
            args.receipt.write_text(json.dumps(actual, indent=2, sort_keys=True) + "\n")
        else:
            require(json.loads(args.receipt.read_text()) == actual,
                    "receipt mismatch; no evidence was modified")
    except (OSError, ValueError, TypeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: V003 bounded digit, cylinder, kernel, scaling, carry and cycle examples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
