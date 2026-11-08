"""Exact controls for the balanced third-period denominator law.

The README proves the unbounded claim. This certificate checks its formal
polynomial identities, exhaustive small-word track classification, a declared
six-block grid, and genuine reduced 3x+q cycles. No failure-to-find argument
is used. Checks remain active under python -O. By default the receipt must
match exactly; --write-receipt regenerates it.
"""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FIXTURES = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


def intercept(word):
    total = value = 0
    for letter in word:
        value = 3 * value + 2**total
        total += letter
    return value


def rotate(word, start):
    return word[start:] + word[:start]


def mismatches(word, shift):
    return sum(x != word[(i + shift) % len(word)] for i, x in enumerate(word))


def denominator(word):
    gap = 2**sum(word) - 3**len(word)
    need(gap > 0, "denominator requires a positive gap")
    return gap // gcd(gap, intercept(word))


def actual_cycle(word):
    gap = 2**sum(word) - 3**len(word)
    common = gcd(gap, intercept(word))
    q = gap // common
    state = intercept(word) // common
    first = state
    states = []
    for letter in word:
        need(state > 0 and state % 2 == 1, "positive odd reduced state")
        states.append(state)
        raw = 3 * state + q
        valuation = (raw & -raw).bit_length() - 1
        need(valuation == letter, "exact reduced valuation")
        state = raw >> letter
    need(state == first, "reduced cycle closure")
    return q, states


def classify(word):
    """Return the majority description of any third-period four-mismatch word."""
    need(len(word) % 3 == 0, "third-period length")
    g = len(word) // 3
    if mismatches(word, g) != 4:
        return None
    majority = []
    outliers = []
    track_counts = []
    for column in range(g):
        values = tuple(word[column + j * g] for j in range(3))
        count = sum(values[j] != values[(j + 1) % 3] for j in range(3))
        track_counts.append(count)
        need(count in (0, 2, 3), "three-track mismatch count")
        frequencies = Counter(values)
        base, frequency = frequencies.most_common(1)[0]
        need(frequency >= 2, "four total mismatches force a majority in every track")
        majority.append(base)
        for j, value in enumerate(values):
            if value != base:
                outliers.append((column + j * g, value - base))
    need(track_counts.count(2) == 2 and track_counts.count(3) == 0,
         "exactly two nonconstant majority tracks")
    need(len(outliers) == 2 and outliers[0][0] % g != outliers[1][0] % g,
         "two distinct exceptional columns")
    need(mismatches(word, 2 * g) == 4, "reverse third-period shift")
    template = tuple(majority)
    balanced = sum(change for _, change in outliers) == 0
    if not balanced:
        return {"balanced": False, "template": template}
    positive = next(position for position, change in outliers if change > 0)
    negative = next(position for position, change in outliers if change < 0)
    delta = next(change for _, change in outliers if change > 0)
    distance = (negative - positive) % len(word)
    need(distance not in (0, g, 2 * g), "distinct-column distance")
    need(sum(word) == 3 * sum(template), "balanced total")
    if distance < g or distance > 2 * g:
        start = positive if distance < g else negative
        oriented = rotate(word, start)
        phase = rotate(template, start % g)
        changed = oriented[:g]
        need(oriented == changed + phase + phase, "aligned exact reconstruction")
        need(changed != phase and sum(changed) == sum(phase), "aligned equal-total blocks")
        return {"balanced": True, "placement": "aligned", "template": template,
                "delta": delta, "start": start}
    length_a = 2 * g - distance
    start = (positive - length_a + 1) % len(word)
    phase = rotate(template, start % g)
    a_word, b_word = phase[:length_a], phase[length_a:]
    need(a_word and b_word and b_word[-1] > delta, "positive unaligned blocks")
    raised = a_word[:-1] + (a_word[-1] + delta,)
    lowered = b_word[:-1] + (b_word[-1] - delta,)
    need(rotate(word, start) == raised + b_word + a_word + lowered + a_word + b_word,
         "unaligned exact reconstruction")
    return {"balanced": True, "placement": "unaligned", "template": template,
            "delta": delta, "start": start, "A": a_word, "B": b_word}


def final_bound(word, template, delta):
    g = len(template)
    p, z = 3**g, 2**sum(template)
    q = denominator(word)
    phi = p * p + p * z + z * z
    d0 = gcd(2**delta - 1, phi)
    need((q * d0)**2 * p * p > 2**(2 * g + delta) * z, "sharpened denominator law")
    need(gcd(phi, 3) == 1, "Phi prime to three")
    if delta in (1, 2):
        need(d0 == 1 and q > 1, "delta one/two corollary")
    if q == 1:
        need(2**delta * 3**g > 4**g, "necessary large change for denominator one")
    return q, d0


def symbolic_identities():
    """Exact Laurent-polynomial composition, with S/k allowed symbolically."""
    names = ("alpha", "beta", "Q", "S", "C", "E", "k", "h", "t", "s")
    dimension = len(names)
    zero = (0,) * dimension

    def scalar(value):
        return {zero: value} if value else {}

    def variable(name, exponent=1):
        powers = [0] * dimension
        powers[names.index(name)] = exponent
        return {tuple(powers): 1}

    def add(*polynomials):
        result = {}
        for polynomial in polynomials:
            for monomial, coefficient in polynomial.items():
                result[monomial] = result.get(monomial, 0) + coefficient
        return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}

    def multiply(*polynomials):
        result = scalar(1)
        for polynomial in polynomials:
            following = {}
            for left, a in result.items():
                for right, b in polynomial.items():
                    monomial = tuple(x + y for x, y in zip(left, right))
                    following[monomial] = following.get(monomial, 0) + a * b
            result = {monomial: coefficient for monomial, coefficient in following.items() if coefficient}
        return result

    alpha, beta, q, s_power, c, e, k, h, t, s = map(variable, names)
    minus = scalar(-1)
    p, z = multiply(alpha, beta), multiply(q, s_power)
    x, y = multiply(beta, c), multiply(q, e)
    phi = add(multiply(p, p), multiply(p, z), multiply(z, z))
    residue = add(multiply(p, x), multiply(minus, z, y))
    blocks = ((alpha, multiply(q, k), c), (beta, s_power, e),
              (alpha, q, c), (beta, multiply(s_power, variable("k", -1)), e),
              (alpha, q, c), (beta, s_power, e))
    coefficient, binary = scalar(0), scalar(1)
    for ternary, block_binary, block_intercept in blocks:
        coefficient = add(multiply(ternary, coefficient), multiply(binary, block_intercept))
        binary = multiply(binary, block_binary)
    need(binary == multiply(z, z, z), "formal balanced total")
    rhs = add(multiply(add(x, multiply(k, y)), phi),
              multiply(add(k, minus), z, residue))
    need(coefficient == rhs, "formal six-block intercept identity")
    dc = add(multiply(h, alpha), multiply(z, t))
    de = add(multiply(minus, h, s_power), multiply(p, s))
    coupled = add(multiply(alpha, beta, beta, dc), multiply(minus, q, q, s_power, de),
                  multiply(minus, h, phi))
    need(coupled == multiply(p, z, add(multiply(beta, t), multiply(minus, q, s), multiply(minus, h))),
         "formal lattice coupling")
    h_value = add(multiply(beta, t), multiply(minus, q, s))
    dc = add(multiply(h_value, alpha), multiply(z, t))
    de = add(multiply(minus, h_value, s_power), multiply(p, s))
    need(add(multiply(beta, dc), multiply(q, de)) ==
         add(multiply(beta, p, t), multiply(q, z, s)), "formal AB lattice identity")
    need(add(multiply(alpha, de), multiply(s_power, dc)) ==
         add(multiply(alpha, p, s), multiply(s_power, z, t)), "formal BA lattice identity")
    return {"identities": 5, "ring": "integer Laurent polynomials in " + ",".join(names)}


def structural_controls():
    counts = Counter()
    digest = sha256()

    def check(word, rotate_all):
        counts["words"] += 1
        description = classify(word)
        if description is None:
            return
        counts["four_mismatch_words"] += 1
        if not description["balanced"]:
            counts["unbalanced_words"] += 1
            return
        counts[description["placement"]] += 1
        template, delta = description["template"], description["delta"]
        positive = 2**sum(template) > 3**len(template)
        if positive:
            q, d0 = final_bound(word, template, delta)
            if description["placement"] == "aligned":
                need(q * 3**len(template) > 2**(len(template) + sum(template)),
                     "existing aligned two-block bound")
            counts["positive_balanced_words"] += 1
            if rotate_all:
                for start in range(len(word)):
                    rotated = rotate(word, start)
                    other = classify(rotated)
                    need(other is not None and other["balanced"], "rotation classification")
                    need(other["placement"] == description["placement"], "rotation placement")
                    need(denominator(rotated) == q, "rotation denominator")
                    counts["rotation_checks"] += 1
            digest.update((repr((word, q, d0)) + "\n").encode())

    for g in range(1, 4):
        for word in product(range(1, 4), repeat=3 * g):
            check(word, True)
    exhaustive = counts["words"]
    for g in range(4, 9):
        template = tuple(3 + i % 3 for i in range(g))
        for positive in range(3 * g):
            for negative in range(3 * g):
                if positive % g == negative % g:
                    continue
                for delta in (1, 2):
                    word = list(template * 3)
                    word[positive] += delta
                    word[negative] -= delta
                    check(tuple(word), False)
    return {"counts": dict(sorted(counts.items())),
            "exhaustive_words": exhaustive,
            "ranges": {"exhaustive_g": [1, 3], "exhaustive_letters": [1, 3],
                       "generated_g": [4, 8], "generated_template": "U_i=3+(i mod 3)",
                       "generated_delta": [1, 2], "generated_positions": "all pairs in distinct columns"},
            "positive_cases_sha256": digest.hexdigest()}


def words(max_length, alphabet):
    return [word for length in range(1, max_length + 1) for word in product(alphabet, repeat=length)]


def lattice_controls():
    identities = positives = arrows = 0
    signs = {"negative": 0, "zero": 0, "positive": 0}
    digest = sha256()
    smallest = None
    examples = {}
    for a_word in words(3, range(1, 5)):
        alpha, q_power, c = 3**len(a_word), 2**sum(a_word), intercept(a_word)
        for b_word in words(3, range(1, 6)):
            beta, s_power, e = 3**len(b_word), 2**sum(b_word), intercept(b_word)
            g = len(a_word) + len(b_word)
            p, z, x, y = alpha * beta, q_power * s_power, beta * c, q_power * e
            phi = p * p + p * z + z * z
            residue = p * x - z * y
            need(gcd(p, z) == 1 and gcd(phi, 6 * z) == 1, "basic coprimality")
            for delta in range(1, b_word[-1]):
                k = 2**delta
                raised = a_word[:-1] + (a_word[-1] + delta,)
                lowered = b_word[:-1] + (b_word[-1] - delta,)
                word = raised + b_word + a_word + lowered + a_word + b_word
                cw = intercept(word)
                need(sum(word) == 3 * (sum(a_word) + sum(b_word)), "balanced six-block total")
                need(cw == (x + k * y) * phi + (k - 1) * z * residue, "six-block identity")
                need(mismatches(word, g) == 4, "six-block mismatch count")
                description = classify(word)
                need(description["placement"] == "unaligned", "six-block placement")
                need(description["A"] == a_word and description["B"] == b_word,
                     "six-block canonical reconstruction")
                identities += 1
                if z <= p:
                    continue
                q, d0 = final_bound(word, a_word + b_word, delta)
                d1 = gcd(q * (k - 1), phi)
                need((d1 * residue) % phi == 0, "extracted cubic divisibility")
                h = d1 * residue // phi
                need((d1 * c - h * alpha) % z == 0 and (d1 * e + h * s_power) % p == 0,
                     "two coupled congruences")
                t, s = (d1 * c - h * alpha) // z, (d1 * e + h * s_power) // p
                need(t > 0 and s > 0 and beta * t - q_power * s == h, "positive lattice parameters")
                cab, cba = intercept(a_word + b_word), intercept(b_word + a_word)
                need(d1 * cab == beta * p * t + q_power * z * s, "AB intercept identity")
                need(d1 * cba == alpha * p * s + s_power * z * t, "BA intercept identity")
                need(cab == intercept(a_word + lowered), "final-letter intercept invariance")
                need(cab * 2**(g + delta) < z * p and cba * 2**g < z * p,
                     "sharpened and ordinary intercept bounds")
                need(q_power * 2**(g + delta) < d1 * p and s_power * 2**g < d1 * p,
                     "two binary-clock bounds")
                need(d1 <= q * d0 and d1**2 * p * p > 2**(2 * g + delta) * z,
                     "gcd extraction and sharpened product")
                actual_q, states = actual_cycle(word)
                need(actual_q == q, "actual cycle retains denominator")
                arrows += len(states)
                positives += 1
                sign = "positive" if h > 0 else "negative" if h < 0 else "zero"
                signs[sign] += 1
                row = {"A": list(a_word), "B": list(b_word), "delta": delta,
                       "q": q, "d0": d0, "h": h, "t": t, "s": s, "word": list(word)}
                if sign not in examples:
                    examples[sign] = row
                ratio = Fraction((q * d0)**2 * p * p, 2**(2 * g + delta) * z)
                if smallest is None or ratio < smallest[0]:
                    smallest = (ratio, row)
                digest.update((json.dumps(row, sort_keys=True) + "\n").encode())
    need(signs["negative"] > 0 and signs["positive"] > 0, "both residue signs exercised")
    return {"ranges": {"A_length": [1, 3], "A_letters": [1, 4],
                       "B_length": [1, 3], "B_letters": [1, 5], "delta": "1 through last(B)-1"},
            "identities": identities, "positive_words": positives, "actual_arrows": arrows,
            "lattice_signs": signs, "examples": examples,
            "smallest_law_ratio": str(smallest[0]), "smallest_ratio_example": smallest[1],
            "cases_sha256": digest.hexdigest()}


def fixture_controls():
    raw = FIXTURES.read_bytes()
    fixtures = json.loads(raw)["cycles"]
    rows = []
    arrows = 0
    for fixture in fixtures:
        word = tuple(fixture["valuations"])
        states, d = fixture["states"], fixture["d"]
        need(d in (5, 7, 13, 61), "standard fixture addend")
        for i, letter in enumerate(word):
            value = 3 * states[i] + d
            need((value & -value).bit_length() - 1 == letter, "fixture exact valuation")
            need(value >> letter == states[(i + 1) % len(states)], "fixture exact arrow")
            arrows += 1
        q = denominator(word)
        need(d % q == 0, "fixture denominator divides actual addend")
        description = classify(word) if len(word) % 3 == 0 else None
        eligible = description is not None and description["balanced"]
        if eligible:
            final_bound(word, description["template"], description["delta"])
        rows.append({"d": d, "word": list(word), "denominator": q,
                     "balanced_third_period": eligible})
    need(len(rows) == 11 and arrows == 106, "all eleven standard cycles")
    return {"fixture_sha256": sha256(raw).hexdigest(), "cycles": rows, "arrows": arrows}


def run():
    return {"schema": "balanced-third-period-denominator-law-v1",
            "symbolic": symbolic_identities(),
            "structure": structural_controls(),
            "lattice": lattice_controls(),
            "fixtures": fixture_controls(),
            "scope": "Exact polynomial identities and finite controls; the README supplies the unbounded proof."}


def main():
    need(sys.argv[1:] in ([], ["--write-receipt"]), "usage: check_third_period.py [--write-receipt]")
    data = run()
    output = json.dumps(data, sort_keys=True, indent=2) + "\n"
    receipt = HERE / "check_third_period.json"
    if sys.argv[1:]:
        receipt.write_text(output)
    else:
        need(receipt.read_text() == output, "receipt mismatch; regenerate deliberately with --write-receipt")
    print(json.dumps({"symbolic_identities": data["symbolic"]["identities"],
                      "structure": data["structure"]["counts"],
                      "lattice_words": data["lattice"]["positive_words"],
                      "actual_arrows": data["lattice"]["actual_arrows"],
                      "standard_cycles": len(data["fixtures"]["cycles"])}, sort_keys=True))


if __name__ == "__main__":
    main()
