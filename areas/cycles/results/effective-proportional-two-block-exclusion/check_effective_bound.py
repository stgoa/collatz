"""Exact finite checks accompanying the uniform proof in README.md."""

from fractions import Fraction
from itertools import product
import json
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def data(word):
    c, total = 0, 0
    for letter in word:
        require(letter >= 1, "nonpositive valuation")
        c = 3 * c + (1 << total)
        total += letter
    return c, (1 << total) - 3 ** len(word)


def denominator(word):
    c, d = data(word)
    require(d > 0, "nonpositive cycle denominator")
    return d // gcd(c, d)


def integer_lemma():
    count = 0
    minimum = None
    witness = None
    for r in range(1, 33):
        for s in range(1, 33):
            if gcd(r, s) != 1:
                continue
            for k in range(2, 13):
                for ell in range(2, 13):
                    length = r * k + s * ell
                    h = gcd(r * k, s * ell)
                    t = length - h + 1
                    value = Fraction(8 * (t - r - s) - 3 * max(r, s), 8 * length)
                    require(value >= Fraction(7, 96), "uniform exponent")
                    if minimum is None or value < minimum:
                        minimum, witness = value, [r, s, k, ell]
                    count += 1
    return dict(checks=count, r_s_max=32, repetitions_max=12,
                smallest_tested_exponent=str(minimum), witness=witness)


def word_checks():
    words = [w for n in range(1, 4) for w in product(range(1, 5), repeat=n)]
    pairs, repetitions, commuting = 0, 0, 0
    for u in words:
        cu, du = data(u)
        if du <= 0:
            continue
        bu = (1 << (sum(u) - len(u))) * 3 ** len(u)
        require(cu < bu and 0 < du < (1 << sum(u)) < bu, "u intercept bound")
        for v in words:
            if sum(u) * len(v) != sum(v) * len(u):
                continue
            cv, dv = data(v)
            bv = (1 << (sum(v) - len(v))) * 3 ** len(v)
            require(cv < bv and 0 < dv < (1 << sum(v)) < bv, "v intercept bound")
            a, b = gcd(sum(u), sum(v)), gcd(len(u), len(v))
            r, s = len(u) // b, len(v) // b
            require(sum(u) == a * r and sum(v) == a * s and gcd(r, s) == 1,
                    "proportional parameterization")
            base, other = 1 << a, 3 ** b
            gap = base - other
            commutator = du * cv - dv * cu
            require(gap > 0 and commutator % gap == 0, "base-gap divisibility")
            if not commutator:
                commuting += 1
                require(Fraction(cu, du) == Fraction(cv, dv), "common fixed point")
                continue
            pairs += 1
            require(abs(commutator) < max(du * cv, dv * cu), "positive-difference bound")
            require(abs(commutator) ** 8 < base ** (8 * (r + s) + 3 * max(r, s)),
                    "rational commutator exponent")
            quotient = abs(commutator) // gap
            for prime in (2, 3):
                while quotient % prime == 0:
                    quotient //= prime
            for k, ell in product(range(2, 5), repeat=2):
                word = u * k + v * ell
                c, d = data(word)
                g = gcd(c, d)
                q = d // g
                length = r * k + s * ell
                h = gcd(r * k, s * ell)
                require((quotient * (base ** h - other ** h)) % g == 0,
                        "strong divisibility cancellation")
                require(q * abs(commutator) > gap * base ** (length - h),
                        "exact denominator lower bound")
                # EXT-1 is tested here only for these generated base exponents;
                # the proof uses the separately declared replayed source globally.
                require(gap * (1 << 172) * b ** 341 >= base, "finite gap check")
                exponent = 7 * sum(word) - 172 * 96
                if exponent >= 0:
                    require((q * b ** 341) ** 96 > (1 << exponent),
                            "cleared uniform bound")
                else:
                    require(q * b ** 341 >= 1, "small-exponent uniform bound")
                repetitions += 1
    return dict(generated_words=len(words), noncommuting_pairs=pairs,
                commuting_pairs=commuting, repeated_word_checks=repetitions)


def controls():
    path = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    fixtures = json.loads(path.read_text())["cycles"]
    rows = []
    for fixture in fixtures:
        word = tuple(fixture["valuations"])
        states, addend = fixture["states"], fixture["d"]
        require(len(states) == len(word), "fixture shape")
        for i, letter in enumerate(word):
            x, y = states[i], states[(i + 1) % len(states)]
            require(x > 0 and x % 2 == 1 and y % 2 == 1, "fixture odd domain")
            require(3 * x + addend == (1 << letter) * y, "fixture exact arrow")
        c, d = data(word)
        require(Fraction(c, d) == Fraction(states[0], addend), "fixture fixed point")
        u, v = word, word * 2
        cu, du = data(u)
        cv, dv = data(v)
        require(du * cv - dv * cu == 0, "actual control must retain K=0")
        q = denominator(word)
        require(addend % q == 0 and denominator(u * 2 + v * 3) == q,
                "common-word repetition preserves denominator")
        rows.append(dict(addend=addend, minimum=min(states), denominator=q,
                         commutator=0))
    require(len(rows) == 11, "shared fixture count changed")
    require(denominator((2,) * 8) == 1, "trivial cycle retained")
    return rows


def cutoff():
    a0 = 1 << 17
    logarithm = Fraction(7 * a0, 96) - 172 - 341 * 15
    require(logarithm == Fraction(12811, 3) > 0, "cutoff logarithm")
    slope = Fraction(7 * a0, 96) - 682
    require(slope > 0, "cutoff growth")
    require(2 ** 8 > 3 ** 5, "log_3(2)>5/8")
    # This is the stated consequence of the separately declared dependency;
    # its own certificate replays the continued-fraction derivation.
    primitive_period_lower = 72_057_431_991
    require(primitive_period_lower > a0, "remaining period contradiction")
    return dict(total_valuation_cutoff=a0, logarithm_at_cutoff=str(logarithm),
                positive_growth_coefficient=str(slope),
                declared_dependency_period_lower=primitive_period_lower)


def main():
    receipt = dict(integer_lemma=integer_lemma(), words=word_checks(),
                   cutoff=cutoff(), actual_cycle_controls=controls())
    target = HERE / "check_effective_bound.json"
    target.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: value for key, value in receipt.items()
                      if key != "actual_cycle_controls"}, sort_keys=True))
    print("All 11 actual-cycle controls retained.")


if __name__ == "__main__":
    main()
