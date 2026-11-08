#!/usr/bin/env python3
"""Exact finite remainder for the sparse four-arc classification.

The README proves r <= 37 for a near-critical full-plus cancellation.
This certificate checks its algebra, exact cutoff, and every remaining
tuple. It neither assumes convergence nor extends a finite census.
"""

import argparse
import json
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
RECEIPT = HERE / "check_classification.json"


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def intercept(word):
    result, denominator = 0, 1
    for letter in word:
        result = 3 * result + denominator
        denominator *= 2**letter
    return result


def word_of(r, a, b, c):
    return [1] * (2 * r - 4) + [a, 1, c] + [1] * (2 * r - 2) + [c, 1, b]


# Polynomials in V,Z,Q,R, represented as exponent tuples -> coefficients.
# V=3^(2r-4), Z=2^(2r-4); the other long block has weights 9V,4Z.
ZERO_EXP = (0, 0, 0, 0)


def constant(value):
    return {ZERO_EXP: value} if value else {}


def variable(index):
    exponents = [0] * 4
    exponents[index] = 1
    return {tuple(exponents): 1}


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for powers, coefficient in polynomial.items():
            result[powers] = result.get(powers, 0) + coefficient
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def scale(polynomial, value):
    return {powers: coefficient * value for powers, coefficient in polynomial.items()
            if coefficient * value}


def multiply(left, right):
    result = {}
    for powers1, coefficient1 in left.items():
        for powers2, coefficient2 in right.items():
            powers = tuple(a + b for a, b in zip(powers1, powers2))
            result[powers] = result.get(powers, 0) + coefficient1 * coefficient2
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def symbolic_intercept():
    v, z, q, rr = [variable(i) for i in range(4)]
    current = add(v, scale(z, -1))
    denominator = z

    def append_letter(current, denominator, weight):
        return add(scale(current, 3), denominator), multiply(denominator, weight)

    for weight in (q, constant(2), rr):
        current, denominator = append_letter(current, denominator, weight)
    current = add(multiply(scale(v, 9), current),
                  multiply(denominator, add(scale(v, 9), scale(z, -4))))
    denominator = multiply(denominator, scale(z, 4))
    for weight in (rr, constant(2)):
        current, denominator = append_letter(current, denominator, weight)
    # The last letter b changes the denominator but not the intercept.
    current = add(scale(current, 3), denominator)

    y2, x2 = scale(v, 81), scale(z, 16)
    expected = add(
        scale(multiply(y2, y2), 32),
        scale(multiply(multiply(add(multiply(q, add(constant(5), scale(rr, 2))),
                                     constant(-18)), x2), y2), 6),
        multiply(multiply(multiply(q, rr), add(scale(rr, 5), constant(-18))),
                 multiply(x2, x2)),
    )
    require(scale(current, 32) == expected, "symbolic intercept identity failed")
    return [{"powers_V_Z_Q_R": list(powers), "coefficient_in_32C": coefficient}
            for powers, coefficient in sorted(expected.items())]


def finite_remainder():
    count, hits, pair_counts = 0, [], []
    branch_counts = {"a_le_b": 0, "large_R": 0, "small_R": 0}
    for r in range(2, 38):
        for t in range(1, 2 * r + 1):
            power3, power2 = 3 ** (4 * r), 2 ** (4 * r + 2 * t)
            if not power3 < power2 < 2 * power3:
                continue
            tuple_count = 0
            u, x, y = 2**t, 2**r, 3**r
            require(u >= 8, "near-critical lower bound on U failed")
            plus = y * y + u * x * x
            for c in range(2, t + 2):
                rr = 2**c
                total_ab = 2 * t - 2 * c + 4
                for a in range(1, total_ab):
                    b = total_ab - a
                    q, tt = 2**a, 2**b
                    word = word_of(r, a, b, c)
                    require(len(word) == 4 * r and sum(word) == 4 * r + 2 * t,
                            "word length or total failed")
                    require(q * tt * rr**2 == 16 * u**2, "letter-product identity failed")
                    require(rr <= 2 * u and q * rr**2 <= 8 * u**2
                            and tt * rr**2 <= 8 * u**2, "positivity bounds failed")
                    shift = 2 * r - 1
                    require(gcd(shift, len(word)) == 1, "track is not coprime")
                    track = [word[(len(word) - 1 + i * shift) % len(word)]
                             for i in range(len(word))]
                    require(track == [b, c, c, a] + [1] * (4 * r - 4),
                            "four-arc track identity failed")
                    cw = intercept(word)
                    polynomial = (32 * y**4 + 6 * (q * (5 + 2 * rr) - 18) * x**2 * y**2
                                  + q * rr * (5 * rr - 18) * x**4)
                    require(32 * cw == polynomial, "direct intercept identity failed")
                    a0 = 4 * u * (8 * u + 27)
                    b0 = rr * (5 * rr - 18) - 6 * (5 + 2 * rr) * u
                    hh = a0 + q * b0
                    require(a0 <= 59 * u**2 and abs(b0) <= 34 * rr * u,
                            "coefficient size bound failed")
                    require((32 * cw - x**4 * hh) % plus == 0, "residue identity failed")
                    if a <= b:
                        jj = hh
                        branch_counts["a_le_b"] += 1
                        require(abs(jj) <= 195 * u**2, "first residue bound failed")
                    elif rr**2 >= u:
                        jj = hh
                        branch_counts["large_R"] += 1
                    else:
                        jj = rr**2 * tt * (8 * u + 27) + 4 * u * b0
                        branch_counts["small_R"] += 1
                        require(4 * u * jj == rr**2 * tt * hh,
                                "cleared residue transformation failed")
                        require(abs(jj) <= 195 * rr * u**2, "third residue bound failed")
                    require(jj * jj <= 331**2 * u**5, "uniform residue bound failed")
                    require((cw % plus == 0) == (hh % plus == 0) == (jj % plus == 0),
                            "divisibility equivalence failed")
                    require((jj == 0) == (hh == 0), "zero equivalence failed")
                    require((hh == 0) == ((t, a, b, c) == (4, 3, 5, 2)),
                            "finite zero classification failed")
                    if cw % plus == 0:
                        dd = power2 - power3
                        cancellation = gcd(cw, dd)
                        hits.append({"r": r, "t": t, "a": a, "b": b, "c": c,
                                     "word": word, "length": len(word), "total": sum(word),
                                     "intercept": cw, "D": dd, "plus": plus, "H": hh,
                                     "minus": u * x * x - y * y,
                                     "gcd": cancellation, "denominator": dd // cancellation,
                                     "reduced_numerator": cw // cancellation,
                                     "mismatches": [sum(word[i] != word[(i + h) % len(word)]
                                                        for i in range(len(word)))
                                                    for h in range(1, len(word))]})
                    count += 1
                    tuple_count += 1
            require(tuple_count == t * t, "finite range count failed")
            pair_counts.append({"r": r, "t": t, "tuples": tuple_count})
    require(count == 11697, "unexpected finite tuple count")
    require(len(hits) == 1, "unexpected number of full-plus cancellations")
    hit = hits[0]
    require(tuple(hit[key] for key in ("r", "t", "a", "b", "c")) == (3, 4, 3, 5, 2),
            "unexpected cancellation tuple")
    require(hit["denominator"] == 295 and hit["gcd"] == 1753
            and hit["reduced_numerator"] == 737, "surviving denominator failed")
    require(gcd(hit["minus"], hit["reduced_numerator"]) == 1,
            "the other denominator factor did not survive")
    return {"parameter_pairs": pair_counts, "tuple_count": count,
            "residue_branches": branch_counts, "full_plus_cancellations": hits}


def controls():
    path = REPO / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    fixtures = json.loads(path.read_text())["cycles"]
    require(len(fixtures) == 11, "unexpected standard control count")
    require({item["d"] for item in fixtures} == {5, 7, 13, 61}, "control coverage failed")
    result = []
    for item in fixtures:
        d, states, word = item["d"], item["states"], item["valuations"]
        require(len(states) == len(word) and len(set(states)) == len(states),
                "control period failed")
        for i, (state, letter) in enumerate(zip(states, word)):
            target = states[(i + 1) % len(states)]
            require(state > 0 and state % 2 == 1 and target > 0 and target % 2 == 1,
                    "control odd positivity failed")
            require(3 * state + d == 2**letter * target, "control arrow failed")
        cw, dd = intercept(word), 2**sum(word) - 3**len(word)
        require(dd > 0 and states[0] * dd == d * cw, "control cycle equation failed")
        denominator = dd // gcd(cw, dd)
        require(d % denominator == 0, "control reduced denominator failed")
        require(len(word) % 4 != 0, "control unexpectedly inside the length class")
        result.append({"d": d, "minimum": min(states), "length": len(word),
                       "total": sum(word), "denominator": denominator,
                       "failed_hypothesis": "length divisible by 4"})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    left, right = 8 * 331**4 * 27**152, 32**152
    require(left < right, "large-r cutoff inequality failed")
    require(3**16 > 2**24, "zero-family near-critical exclusion base failed")
    receipt = {
        "status": "PASS",
        "scope": "All even-total near-critical words in the specified sparse four-arc family; no general four-arc classification.",
        "symbolic_identity": {"variables": ["V", "Z", "Q", "R"],
                              "terms": symbolic_intercept()},
        "large_r_cutoff": {"r": 38, "fourth_power_left": left, "fourth_power_right": right,
                           "zero_family_exclusion_base_r": 4,
                           "zero_family_base_power3": 3**16,
                           "zero_family_base_power2": 2**24},
        "finite_remainder": finite_remainder(),
        "controls": controls(),
    }
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.write_receipt:
        RECEIPT.write_text(rendered)
    else:
        require(RECEIPT.exists() and RECEIPT.read_text() == rendered,
                "receipt differs; use --write-receipt to regenerate after reviewing the change")
    print("PASS: symbolic identity, r>=38 cutoff, 11697 finite tuples, one cancellation with denominator 295, 11 controls")


if __name__ == "__main__":
    main()
