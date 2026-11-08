#!/usr/bin/env python3
"""Exact finite checks for the sparse-rotation coverage obstruction."""

from __future__ import annotations

import hashlib
import json
from math import gcd, isqrt
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MAX_PRIME = 601
MAX_PERIOD = 12


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def prime(n: int) -> bool:
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def intercept(word: list[int]) -> int:
    value, power = 0, 1
    for letter in word:
        value = 3 * value + power
        power <<= letter
    return value


def mismatch(word: list[int], shift: int) -> set[int]:
    m = len(word)
    return {i for i in range(m) if word[i] != word[(i + shift) % m]}


def construct(m: int) -> tuple[list[int], list[int], dict]:
    require(prime(m) and m >= 61, "construction parameter")
    three = 3**m
    total = three.bit_length()
    # floor(m*(log_2(3)-1/2)), using only integer comparisons.
    base_total = ((three * three).bit_length() - 1 - m) // 2
    require(1 << (2 * base_total + m) < three * three,
            "lower floor comparison")
    require(three * three < 1 << (2 * base_total + m + 2),
            "upper floor comparison")
    twos = base_total - m
    require(5 <= twos < m - 2 and gcd(twos, m) == 1, "two-arc sizes")
    base = [(i + 1) * base_total // m - i * base_total // m
            for i in range(m)]
    require(set(base) == {1, 2} and base.count(2) == twos,
            "mechanical letters")
    shift = pow(twos, -1, m)
    old_mismatches = mismatch(base, shift)
    require(len(old_mismatches) == 2, "base mismatch count")
    forbidden = old_mismatches | {(i + shift) % m for i in old_mismatches}
    choices = [i for i, letter in enumerate(base)
               if letter == 2 and i not in forbidden]
    require(bool(choices), "missing safe edit")
    position = choices[0]
    word = base.copy()
    word[position] = total - base_total + 2
    require(word[position] in ((m + 5) // 2, (m + 7) // 2), "marker size")
    require(word.count(word[position]) == 1, "unique marker")
    require(sum(word) == total, "new total")
    require(three < 1 << total < 2 * three, "near-critical total")
    require(mismatch(word, shift) == old_mismatches | {
        position, (position - shift) % m}, "exact edited mismatch set")
    require(base[(position - shift) % m] == base[(position + shift) % m] == 2,
            "marker is inside the two-arc")
    return word, base, dict(m=m, A=total, F=base_total, twos=twos,
                           h=shift, p=position, marker=word[position])


def check_word(word: list[int], base: list[int], data: dict) -> dict:
    m, total, base_total = data["m"], data["A"], data["F"]
    twos, shift, position = data["twos"], data["h"], data["p"]
    minimum = m
    for r in range(1, m):
        old = mismatch(base, r)
        new = mismatch(word, r)
        distance = (r * twos) % m
        expected = 2 * min(distance, m - distance, twos, m - twos)
        require(len(old) == expected, "two-arc spectrum")
        require(old <= new, "edit removed a mismatch")
        require(len(new) > 0, "nonprimitive word")
        minimum = min(minimum, len(new))
    require(minimum == 4, "rho is not four")
    track = [word[(j * shift) % m] for j in range(m)]
    require(len(mismatch(track, 1)) == 4, "four track arcs")

    doubled = base + base
    prefixes = [0]
    for letter in doubled:
        prefixes.append(prefixes[-1] + letter)
    balance_checks = 0
    for start in range(m):
        for length in range(1, m + 1):
            actual = prefixes[start + length] - prefixes[start]
            expected = ((start + length) * base_total // m
                        - start * base_total // m)
            require(actual == expected, "cyclic prefix telescoping")
            require(abs(actual * m - length * base_total) < m,
                    "mechanical balance")
            balance_checks += 1

    factor_checks = 0
    marker_factor_checks = 0
    maxima = []
    for period in range(1, MAX_PERIOD + 1):
        max_length = 0
        for start in range(m):
            length = period
            while length < m and (word[(start + length) % m]
                                  == word[(start + length - period) % m]):
                length += 1
            max_length = max(max_length, length)
            has_marker = (position - start) % m < length
            if has_marker:
                require(length < 2 * period, "unique marker repeated by period")
                marker_factor_checks += 1
            else:
                repeats = length // period
                first_total = prefixes[start + period] - prefixes[start]
                complete_total = prefixes[start + repeats * period] - prefixes[start]
                require(complete_total == repeats * first_total,
                        "period blocks have unequal totals")
                require(repeats * abs(first_total * m - period * base_total) < m,
                        "period-factor balance inequality")
            factor_checks += 1
        maxima.append(max_length)

    D = (1 << total) - 3**m
    C = intercept(word)
    common = gcd(C, D)
    q = D // common
    current = C
    seen = set()
    for i, letter in enumerate(word):
        require(current > 0 and current % 2 == 1, "positive odd intercept")
        require(gcd(current, D) == common, "rotation gcd")
        state = current // common
        require(state not in seen, "actual cycle is nonprimitive")
        seen.add(state)
        numerator = 3 * current + D
        require(numerator % (1 << letter) == 0, "rotated intercept division")
        successor = numerator >> letter
        require(successor % 2 == 1, "inexact valuation")
        require(3 * state + q == (1 << letter) * (successor // common),
                "actual reduced arrow")
        if i in (0, m // 2, m - 1):
            rotated = word[i + 1:] + word[:i + 1]
            require(successor == intercept(rotated), "direct rotation intercept")
        current = successor
    require(current == C, "cycle closure")
    require(q > 1, "finite example unexpectedly has denominator one")
    return dict(balance_checks=balance_checks, factor_checks=factor_checks,
                marker_factor_checks=marker_factor_checks,
                periodic_factor_maxima=maxima, denominator_bits=q.bit_length(),
                reduced_arrows=m)


def check_separation() -> int:
    require(3**12 > 2**19 and 3**3 < 2**5, "slope bracket")
    count = 0
    for cap in range(1, MAX_PERIOD + 1):
        for period in range(1, cap + 1):
            for value in range(period, 2 * period + 1):
                left, right = 1 << (2 * value + period), 3**(2 * period)
                require(left != right, "irrational separation")
                require(max(left, right) <= 1 << (5 * cap), "power size bound")
                require(abs(left - right) >= 1, "integer gap")
                count += 1
    return count


def check_controls() -> dict:
    path = (ROOT / "areas/convergence/results/baseline-obligation-transfer-controls"
            / "cycle_fixtures.json")
    fixtures = json.loads(path.read_text())["cycles"]
    arrows = 0
    parameters = set()
    for fixture in fixtures:
        d, states, word = fixture["d"], fixture["states"], fixture["valuations"]
        require(len(states) == len(word), "fixture length")
        parameters.add(d)
        D = (1 << sum(word)) - 3**len(word)
        C = intercept(word)
        require(states[0] * D == d * C, "fixture cycle equation")
        require(d % (D // gcd(C, D)) == 0, "fixture denominator")
        for i, letter in enumerate(word):
            x, y = states[i], states[(i + 1) % len(states)]
            require(x > 0 and x % 2 == y % 2 == 1, "fixture odd states")
            require(3 * x + d == (1 << letter) * y, "fixture raw arrow")
            arrows += 1
    require(parameters == {5, 7, 13, 61}, "fixture parameters")
    return dict(cycles=len(fixtures), arrows=arrows, parameters=sorted(parameters))


def main() -> None:
    digest = hashlib.sha256()
    rows = []
    totals = dict(rotations=0, balance_checks=0, factor_checks=0,
                  marker_factor_checks=0, reduced_arrows=0)
    maxima = [0] * MAX_PERIOD
    for m in range(61, MAX_PRIME + 1):
        if not prime(m):
            continue
        word, base, data = construct(m)
        checked = check_word(word, base, data)
        digest.update(json.dumps(word, separators=(",", ":")).encode())
        totals["rotations"] += m - 1
        for key in totals:
            if key != "rotations":
                totals[key] += checked[key]
        maxima = [max(a, b) for a, b in zip(maxima, checked["periodic_factor_maxima"])]
        rows.append(data | dict(denominator_bits=checked["denominator_bits"]))
    result = dict(
        scope="Finite checks only; the README proves the unbounded family and obstruction.",
        prime_range=[61, MAX_PRIME], primes_checked=len(rows),
        period_range=[1, MAX_PERIOD], counts=totals,
        maximal_periodic_factor_lengths=maxima,
        elementary_separation_pairs=check_separation(),
        word_digest_sha256=digest.hexdigest(),
        samples=rows[:5] + rows[-1:], controls=check_controls(),
    )
    (HERE / "check_obstruction.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(dict(status="PASS", primes=result["primes_checked"], **totals,
                         controls=result["controls"]), sort_keys=True))


if __name__ == "__main__":
    main()
