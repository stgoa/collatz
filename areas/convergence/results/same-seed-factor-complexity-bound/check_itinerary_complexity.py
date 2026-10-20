"""Bounded exact replay for the conditional itinerary-complexity theorem."""

from argparse import ArgumentParser
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from random import Random
import sys

import itinerary_complexity as subject


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = 40529845
GUARD = 2**26


def words(max_length):
    for length in range(1, max_length + 1):
        for letters in product("VR", repeat=length):
            yield "".join(letters)


def raw_affine(word):
    # Fractional composition is separate from the implementation's integer
    # numerator recurrence, including the extra R factor of two.
    slope, offset = Fraction(1), Fraction(0)
    bits = 0
    for letter in word:
        if letter == "V":
            alpha, beta, step_bits = Fraction(3**12, 2**19), Fraction(311195, 2**19), 19
        else:
            assert letter == "R"
            alpha = Fraction(3**24, 2**37)
            beta = Fraction(311195 * (3**12 + 2**19), 2**37)
            step_bits = 37
        slope, offset = alpha * slope, alpha * offset + beta
        bits += step_bits
    return int(slope * 2**bits), int(offset * 2**bits), bits


def raw_step(w, letter):
    assert type(w) is int and w > 0 and w % GUARD == BASE
    if letter == "V":
        result = Fraction(3**12 * w + 311195, 2**19)
    else:
        assert letter == "R"
        result = 2 * (Fraction(3**12, 2**19) *
                      Fraction(3**12 * w + 311195, 2**19) + Fraction(311195, 2**19))
    if result.denominator != 1 or int(result) % GUARD != BASE:
        return None
    return int(result)


def raw_trace(w, word):
    out = [w]
    for letter in word:
        value = raw_step(out[-1], letter)
        if value is None:
            return None
        out.append(value)
    return out


def raw_copies(w, word, cap=128):
    for copies in range(cap):
        states = raw_trace(w, word)
        if states is None:
            return copies
        w = states[-1]
    raise AssertionError("explicit copy cap reached; unresolved")


def valuation(n):
    assert type(n) is int and n != 0
    n = abs(n)
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count


def digest_rows(rows):
    data = "\n".join(json.dumps(row, sort_keys=True, separators=(",", ":")) for row in rows)
    return sha256(data.encode()).hexdigest()


def check_affines_and_copies():
    affine_cases = cylinder_cases = copy_cases = zero_cases = 0
    rows = []
    for word in words(5):
        a, c, e = raw_affine(word)
        assert subject.affine(word) == (a, c, e)
        assert a > 2**e and c > 0 and c % 2 == 1
        affine_cases += 1
        residue, modulus = subject.cylinder(word)
        assert modulus == 2**(26 + e)
        assert residue % GUARD == BASE
        assert (a * residue + c - 2**e * BASE) % modulus == 0
        for lift in (0, 1, 3):
            w = residue + lift * modulus
            assert raw_trace(w, word) == subject.trace(w, word)
            cylinder_cases += 1
    for word in words(4):
        for requested_copies in range(7):
            residue, modulus = subject.cylinder(word * requested_copies)
            for lift in (0, 1, 3):
                w = residue + lift * modulus
                exact = subject.maximal_copies(w, word)
                direct = raw_copies(w, word)
                assert direct == exact and exact >= requested_copies
                copy_cases += 1
                zero_cases += int(exact == 0)
                rows.append([word, requested_copies, lift, exact])

    # Complete V returns consume the endpoint guard. R67's final guarded
    # growing block can exit G and must not be counted as another V return.
    boundaries = []
    for order in (26, 27, 37, 44, 45, 46, 63, 64, 82, 83, 102, 121):
        modulus = 2**(order + 1)
        w = ((2**order - 311195) * pow(7153, -1, modulus)) % modulus
        assert w > 0 and w % GUARD == BASE
        assert valuation(7153 * w + 311195) == order
        exact = subject.maximal_copies(w, "V")
        assert exact == (order - 26) // 19 == raw_copies(w, "V")
        old_guarded_blocks = 1 + (order - 26) // 19
        assert old_guarded_blocks == exact + 1
        boundaries.append({"Y_order": order, "complete_V_returns": exact,
                           "R67_guarded_blocks": old_guarded_blocks})
    assert zero_cases > 0
    return {"affine_words": affine_cases, "complete_cylinder_lifts": cylinder_cases,
            "copy_count_cases": copy_cases, "zero_copy_cases": zero_cases,
            "copy_case_digest": digest_rows(rows), "V_guard_boundary_cases": boundaries}


def check_finite_repeats():
    rng = Random(74018)
    cases = ["V" * 64, "R" * 64, "VR" * 32, "VVR" * 21,
             "VRRV" * 16, "VVVRR" * 12]
    cases += ["".join(rng.choice("VR") for _ in range(64)) for _ in range(10)]
    rows = []
    trace_cases = growth_checks = 0
    overlapping = 0
    for word in cases:
        residue, modulus = subject.cylinder(word)
        for lift in (0, 1):
            w = residue + lift * modulus
            states = subject.trace(w, word)
            assert states == raw_trace(w, word)
            trace_cases += 1
            for j, state in enumerate(states):
                assert (7153 * state + 311195) * 2**(37 * j) <= (7153 * w + 311195) * 3**(24 * j)
                if j:
                    assert states[j - 1] < state
                growth_checks += 1
            for length in range(1, 9):
                first = {}
                for j in range(len(word) - length + 1):
                    factor = word[j:j + length]
                    if factor not in first:
                        first[factor] = j
                        continue
                    i = first[factor]
                    row = subject.repeated_factor(w, word, i, j, length)
                    e = 19 * factor.count("V") + 37 * factor.count("R")
                    gap = states[j] - states[i]
                    assert gap >= 2**(26 + e) and gap % 2**(26 + e) == 0
                    assert (7153 * w + 311195) * 3**(24 * j) > 7153 * 2**(26 + e + 37 * j)
                    overlapping += int(j - i < length)
                    rows.append(row)
    assert overlapping > 0
    return {"positive_finite_traces": trace_cases, "maximum_symbols": 64,
            "exact_growth_checks": growth_checks, "repeated_factor_checks": len(rows),
            "overlapping_factor_checks": overlapping, "repeat_digest": digest_rows(rows)}


def check_complexity_thresholds():
    rows = []
    for w in (BASE, BASE + GUARD, BASE + 12345 * GUARD,
              BASE + 2**64 * GUARD, BASE + 2**256 * GUARD):
        for length in (1, 2, 4, 5, 8, 16, 32, 64, 128):
            count = subject.distinct_initial_positions(w, length)
            # A separate linear recurrence finds exactly the same integer
            # threshold as the implementation's binary search.
            left, right = 7153 * w + 311195, 7153 * 2**(26 + 19 * length)
            direct = 0
            while left <= right:
                direct += 1
                left *= 3**24
                right *= 2**37
            assert count == direct
            if count:
                j = count - 1
                assert (7153 * w + 311195) * 3**(24 * j) <= 7153 * 2**(26 + 19 * length + 37 * j)
            j = count
            assert (7153 * w + 311195) * 3**(24 * j) > 7153 * 2**(26 + 19 * length + 37 * j)
            rows.append([w, length, count])

    assert 3**432 < 2**685
    cutoff_rows = []
    for length in range(1, 9):
        cutoff, horizon = subject.pigeonhole_cutoff(length)
        exact = Fraction(2**(26 + 19 * length), 1) / subject.MAX_GROWTH**(2**length) - Fraction(311195, 7153)
        assert cutoff == max(0, exact.numerator // exact.denominator)
        assert horizon == 2**length + length
        if cutoff:
            assert (Fraction(cutoff) + subject.SHIFT) * subject.MAX_GROWTH**(2**length) <= 2**(26 + 19 * length)
            assert (Fraction(cutoff + 1) + subject.SHIFT) * subject.MAX_GROWTH**(2**length) > 2**(26 + 19 * length)
            # Largest guard member below the cutoff inherits at least
            # 2**length+1 pairwise distinct factor positions conditionally.
            guard_member = BASE + ((cutoff - BASE) // GUARD) * GUARD
            if guard_member > 0:
                assert subject.distinct_initial_positions(guard_member, length) >= 2**length + 1
        cutoff_rows.append({"factor_length": length, "positive_seed_cutoff": cutoff,
                            "forbidden_return_prefix_length": horizon})
    assert subject.pigeonhole_cutoff(5) == (260028359941009900571662033, 37)
    return {"threshold_cases": len(rows), "threshold_digest": digest_rows(rows),
            "strict_lower_constant_test": "3^432 < 2^685",
            "conditional_complexity_lower_slope": "19/log2(3^24/2^37)",
            "pigeonhole_cutoffs": cutoff_rows,
            "scope": "Conditional threshold tests and arithmetic cutoffs; no survivor is supplied."}


def check_negative_periodic_and_completion_controls():
    rows = []
    periodic_states = 0
    for word in words(5):
        a, c, e = raw_affine(word)
        x = subject.rational_periodic_point(word)
        assert x == Fraction(-c, a - 2**e) < 0
        assert x.denominator % 2 == 1
        assert (x.numerator - BASE * x.denominator) % GUARD == 0
        y = x
        for _ in range(3):
            for letter in word:
                if letter == "V":
                    y = (3**12 * y + 311195) / 2**19
                else:
                    y = (3**24 * y + 311195 * (3**12 + 2**19)) / 2**37
                assert y < 0 and y.denominator % 2 == 1
                assert (y.numerator - BASE * y.denominator) % GUARD == 0
                periodic_states += 1
            assert y == x  # Equal states invalidate the positive gap argument.
        rows.append([word, x.numerator, x.denominator])
        try:
            subject.trace(x, word)
        except ValueError:
            pass
        else:
            raise AssertionError("a negative rational point entered the positive interface")

    completion_rows = []
    for n in range(1, 81):
        den, modulus = 3**(12 * n), 2**(19 * n)
        residue = den % modulus
        z = Fraction(residue, den)
        assert 0 < z < Fraction(modulus, den)
        diff = z - 1
        assert diff.denominator % 2 == 1
        assert valuation(diff.numerator) >= 19 * n
        completion_rows.append([n, valuation(diff.numerator), z.numerator, z.denominator])
    return {"negative_rational_periodic_words": len(rows),
            "periodic_guarded_rational_steps": periodic_states,
            "periodic_control_digest": digest_rows(rows),
            "different_completion_limit_cases": len(completion_rows),
            "completion_control_digest": digest_rows(completion_rows),
            "scope": "Negative rational controls and a limit-inference counterexample, not positive survivors."}


def check_invalid_inputs():
    calls = [
        lambda: subject.trace(1, "V"),
        lambda: subject.trace(0, "V"),
        lambda: subject.trace(-BASE, "V"),
        lambda: subject.trace(Fraction(BASE), "V"),
        lambda: subject.trace(BASE, "X"),
        lambda: subject.step(BASE, "VR"),
        lambda: subject.maximal_copies(BASE, ""),
        lambda: subject.distinct_initial_positions(BASE, 0),
        lambda: subject.pigeonhole_cutoff(0),
        lambda: subject.trace(BASE, "V"),
        lambda: subject.repeated_factor(BASE, "VR", 0, 1, 1),
        lambda: subject.repeated_factor(BASE, "VV", 0, 0, 1),
    ]
    for call in calls:
        try:
            call()
        except ValueError:
            pass
        else:
            raise AssertionError("invalid input was accepted")
    assert subject.trace(BASE, "") == [BASE]
    return {"rejected_cases": len(calls), "empty_finite_trace_accepted": True,
            "absorbing_one_rejected_outside_guard": True}


def source_hashes():
    paths = [HERE / "itinerary_complexity.py", Path(__file__).resolve(),
             HERE / "ITINERARY_COMPLEXITY.md",
             HERE.parent / "integer_prefix/INTEGER_PREFIXES.md"]
    return {str(path.relative_to(ROOT)): sha256(path.read_bytes()).hexdigest() for path in paths}


def main():
    assert not sys.flags.optimize, "run without Python optimization"
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    receipt = {
        "status": "PASS", "affine_and_repetition": check_affines_and_copies(),
        "finite_repeats": check_finite_repeats(),
        "complexity_and_finite_cutoffs": check_complexity_thresholds(),
        "negative_and_completion_controls": check_negative_periodic_and_completion_controls(),
        "invalid_inputs": check_invalid_inputs(), "source_hashes": source_hashes(),
        "positive_infinite_survivor_constructed": False,
        "all_positive_survivors_excluded": False,
        "new_current_or_dispatcher_rule": False,
    }
    path = HERE / "itinerary_complexity_audit.json"
    if args.write_receipt:
        path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    else:
        assert json.loads(path.read_text()) == receipt, "receipt mismatch"
    print(json.dumps({"status": "PASS", "repeat_checks": receipt["finite_repeats"]["repeated_factor_checks"],
                      "positive_seed_cutoff_for_37_return_exclusion": subject.pigeonhole_cutoff(5)[0],
                      "scope": "Exact necessary constraints; global positive termination remains open."}, indent=2))


if __name__ == "__main__":
    main()
