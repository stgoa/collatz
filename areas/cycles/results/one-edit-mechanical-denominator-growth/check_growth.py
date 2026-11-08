#!/usr/bin/env python3
"""Exact finite closure and samples for the one-edit mechanical law."""

from __future__ import annotations

import hashlib
import json
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LENGTH_CUTOFF = 32768
DESCENT_LIMIT = 1 << 18
DESCENT_GUARD = 10000


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def intercept(word: list[int]) -> int:
    value, power = 0, 1
    for letter in word:
        value = 3 * value + power
        power <<= letter
    return value


def primitive(word: list[int]) -> bool:
    m = len(word)
    return all(word != word[h:] + word[:h] for h in range(1, m))


def mechanical(m: int, total: int, phase: int) -> list[int]:
    return [((i + 1) * total + phase) // m - (i * total + phase) // m
            for i in range(m)]


def check_word(word: list[int], base: list[int]) -> dict:
    """The edited position is last; reconstruct all actual reduced arrows."""
    m, total = len(word), sum(word)
    require(m >= 2 and min(word) > 0, "word scope")
    require(word[:-1] == base[:-1], "unchanged mechanical prefix")
    require(primitive(word), "nonprimitive word supplied")
    two, three = 1 << total, 3**m
    D = two - three
    require(D > 0, "nonpositive cycle denominator")
    C = intercept(word)
    common = gcd(C, D)
    q = D // common
    states = []
    current = C
    for i, letter in enumerate(word):
        require(current > 0 and current % 2 == 1, "positive odd intercept")
        require(gcd(current, D) == common, "rotation gcd changed")
        states.append(current // common)
        numerator = 3 * current + D
        require(numerator % (1 << letter) == 0, "nonintegral arrow")
        successor = numerator >> letter
        require(successor % 2 == 1, "valuation not exact")
        if i in (0, m // 2, m - 1):
            require(successor == intercept(word[i + 1:] + word[:i + 1]),
                    "direct rotated intercept disagrees")
        current = successor
    require(current == C and len(set(states)) == m, "primitive cycle closure")
    for i, letter in enumerate(word):
        require(3 * states[i] + q == (1 << letter) * states[(i + 1) % m],
                "reduced actual arrow")

    t, k = (m - 2) // 2, m // 2
    require(2 * t + 1 <= m - 1, "repeat windows exceed unchanged prefix")
    windows: dict[tuple[int, ...], int] = {}
    repeated = None
    for j in range(t + 2):
        factor = tuple(word[j:j + t])
        if factor in windows:
            repeated = (windows[factor], j)
            break
        windows[factor] = j
    require(repeated is not None, "missing repeated factor")
    i, j = repeated
    E = sum(word[i:i + t])
    start_difference = states[j] - states[i]
    end_difference = states[j + t] - states[i + t]
    require(start_difference != 0 and end_difference != 0, "zero separation")
    require(start_difference % (1 << (E + 1)) == 0, "dyadic separation")
    require((1 << E) * end_difference == 3**t * start_difference,
            "paired-state run identity")
    require(end_difference % (2 * 3**t) == 0, "endpoint separation")
    low, high = min(states), max(states)
    require(high > 2 * 3**t, "repeat maximum bound")
    require(3 * low * D < m * q * two, "minimum from product drift")
    require((high + q) * (1 << (m - 1)) <= 3**(m - 1) * (low + q),
            "maximum from minimum growth")
    require(q * (m + 3) * 3**k * two > 2 * 4**k * D,
            "unconditional denominator law")
    require(q > 1, "finite sample unexpectedly has denominator one")
    return dict(m=m, A=total, gcd=common, q=q, minimum=low, maximum=high,
                repeat_start=i, repeat_other_start=j, repeat_length=t)


def finite_mechanical_checks() -> dict:
    counts = dict(bases=0, factor_checks=0, replacements=0, eligible_words=0,
                  nonpositive_D=0, nonprimitive=0, increases=0, decreases=0,
                  unchanged=0, noncoprime_base_words=0, actual_arrows=0)
    digest = hashlib.sha256()
    replacements = list(range(1, 9)) + [32, 65]
    for m in range(2, 25):
        t = (m - 2) // 2
        for total in range(m, 3 * m + 1):
            for phase in range(m):
                base = mechanical(m, total, phase)
                require(sum(base) == total and min(base) > 0, "mechanical total")
                doubled = base + base
                factors = {tuple(doubled[i:i + t]) for i in range(m)}
                require(len(factors) <= t + 1, "mechanical factor complexity")
                # The rotation law covers arbitrary locations of the substitution.
                h = (m + phase) // 2 % m
                require(base[h:] + base[:h] == mechanical(m, total, (phase + h * total) % m),
                        "mechanical phase rotation")
                counts["bases"] += 1
                counts["factor_checks"] += m
                for replacement in replacements:
                    counts["replacements"] += 1
                    word = base[:-1] + [replacement]
                    if (1 << sum(word)) <= 3**m:
                        counts["nonpositive_D"] += 1
                        continue
                    if not primitive(word):
                        counts["nonprimitive"] += 1
                        continue
                    result = check_word(word, base)
                    counts["eligible_words"] += 1
                    counts["actual_arrows"] += m
                    counts["noncoprime_base_words"] += int(gcd(total, m) > 1)
                    kind = ("increases" if replacement > base[-1] else
                            "decreases" if replacement < base[-1] else "unchanged")
                    counts[kind] += 1
                    digest.update((str((m, total, phase, replacement, result["q"])) + "\n").encode())
    require(all(counts[key] > 0 for key in ("increases", "decreases", "unchanged",
                                          "noncoprime_base_words")), "missing sample class")
    return dict(scope=dict(m=[2, 24], F="m through 3m", phase="0 through m-1",
                           last_letter=replacements), counts=counts,
                denominator_sha256=digest.hexdigest())


def prime_family_samples() -> list[dict]:
    samples = []
    for m in (61, 101, 139, 601):
        three = 3**m
        total = three.bit_length()
        F = ((three * three).bit_length() - 1 - m) // 2
        base = mechanical(m, F, 0)
        h = pow(F - m, -1, m)
        edges = {i for i in range(m) if base[i] != base[(i + h) % m]}
        forbidden = edges | {(i + h) % m for i in edges}
        p = next(i for i, letter in enumerate(base) if letter == 2 and i not in forbidden)
        word = base.copy()
        word[p] = total - F + 2
        cut = p + 1
        result = check_word(word[cut:] + word[:cut], base[cut:] + base[:cut])
        result.update(F=F, edited_position=p, marker=word[p])
        samples.append(result)
    return samples


def finite_closure() -> dict:
    require(2**8 > 3**5, "logarithm lower bound")
    require(LENGTH_CUTOFF == 2**15, "cutoff power")
    require(LENGTH_CUTOFF - 2 - 5 * (172 + 342 * 15) == 6256,
            "cutoff numerator")
    require(LENGTH_CUTOFF > 5 * 684, "cutoff derivative")
    three, three_half = 1, 1
    comparisons = 0
    for m in range(1, LENGTH_CUTOFF):
        three *= 3
        if m % 2 == 0:
            three_half *= 3
        if m < 42:
            continue
        A_min = three.bit_length()
        D_min = (1 << A_min) - three
        k = m // 2
        require(2 * (D_min << (2 * k)) > ((m + 3) * three_half) << A_min,
                f"finite denominator comparison failed at length {m}")
        comparisons += 1
    small_comparisons = 0
    for m in range(2, 42):
        A_min = (3**m).bit_length()
        require((3 * DESCENT_LIMIT + 1)**m < 1 << (A_min + 18 * m),
                f"small-period product comparison failed at length {m}")
        small_comparisons += 1
    return dict(cutoff=LENGTH_CUTOFF, cutoff_value_numerator=6256,
                cutoff_value_denominator=5, intermediate_lengths=[42, LENGTH_CUTOFF - 1],
                intermediate_comparisons=comparisons, small_lengths=[2, 41],
                small_product_comparisons=small_comparisons)


def local_descent() -> dict:
    seeds = steps = max_steps = 0
    max_steps_seed = peak_odd = peak_raw = 1
    for seed in range(3, DESCENT_LIMIT, 2):
        current = seed
        for count in range(1, DESCENT_GUARD + 1):
            raw = 3 * current + 1
            peak_raw = max(peak_raw, raw)
            current = raw >> ((raw & -raw).bit_length() - 1)
            peak_odd = max(peak_odd, current, seed)
            require(current > 0 and current % 2 == 1, "descent left positive odd states")
            if current < seed:
                break
        else:
            raise RuntimeError(f"local descent guard exhausted for seed {seed}")
        seeds += 1
        steps += count
        if count > max_steps:
            max_steps, max_steps_seed = count, seed
    require(seeds == DESCENT_LIMIT // 2 - 1, "incomplete descent coverage")
    return dict(odd_seed_minimum=3, odd_seed_maximum=DESCENT_LIMIT - 1,
                odd_seeds=seeds, odd_steps=steps, maximum_local_steps=max_steps,
                first_seed_at_maximum=max_steps_seed, peak_odd=peak_odd,
                peak_raw=peak_raw, per_seed_guard=DESCENT_GUARD)


def controls() -> dict:
    fixture = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    cycles = json.loads(fixture.read_text())["cycles"]
    arrows = 0
    for cycle in cycles:
        d, states, word = cycle["d"], cycle["states"], cycle["valuations"]
        require(len(states) == len(word) and min(states) == cycle["minimum"], "control shape")
        for i, letter in enumerate(word):
            require(states[i] > 0 and states[i] % 2 == 1, "control positive odd state")
            require(3 * states[i] + d == (1 << letter) * states[(i + 1) % len(states)],
                    "actual control arrow")
            arrows += 1
        D = (1 << sum(word)) - 3**len(word)
        q = D // gcd(intercept(word), D)
        require(D > 0 and d % q == 0, "actual control denominator")
    inside = []
    for word, expected_q in (([1, 1, 3], 5), ([1, 3], 7), ([1, 1, 1, 1, 4], 13)):
        result = check_word(word, [1] * len(word))
        require(result["q"] == expected_q, "inside-class denominator control")
        inside.append(dict(word=word, **result))
    repeated = [2] * 64
    D = (1 << sum(repeated)) - 3**len(repeated)
    q = D // gcd(intercept(repeated), D)
    require(q == 1 and not primitive(repeated), "nonprimitive control")
    require(q * 67 * 3**32 * (1 << 128) <= 2 * 4**32 * D,
            "nonprimitive control does not violate the proposed unscoped law")
    require({cycle["d"] for cycle in cycles} == {5, 7, 13, 61}, "missing standard addend")
    return dict(actual_cycles=len(cycles), actual_arrows=arrows, addends=[5, 7, 13, 61],
                inside_class=inside, nonprimitive_control=dict(word="(2)^64", q=q,
                unscoped_denominator_inequality_fails=True))


def main() -> None:
    receipt = dict(schema="one-edit-mechanical-growth-v1",
                   finite_samples=finite_mechanical_checks(),
                   prime_four_mismatch_samples=prime_family_samples(),
                   finite_closure=finite_closure(), local_descent=local_descent(),
                   controls=controls())
    (HERE / "check_growth.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print("PASS one-edit mechanical denominator growth: "
          f"{receipt['finite_samples']['counts']['eligible_words']} word samples; "
          f"{receipt['finite_closure']['intermediate_comparisons']} length comparisons; "
          f"{receipt['local_descent']['odd_seeds']} odd descents; "
          f"{receipt['controls']['actual_cycles']} actual-cycle controls")


if __name__ == "__main__":
    main()
