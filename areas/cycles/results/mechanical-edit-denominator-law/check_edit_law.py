#!/usr/bin/env python3
"""Exact closure and finite identity checks for mechanical signed edits."""

from __future__ import annotations

import hashlib
import json
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CUTOFF = 1 << 18
LOCAL_LIMIT = 1 << 18
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
    return all(word != word[h:] + word[:h] for h in range(1, len(word)))


def mechanical(m: int, total: int, phase: int) -> list[int]:
    return [((i + 1) * total + phase) // m - (i * total + phase) // m
            for i in range(m)]


def check_chunks(word: list[int], base: list[int], states: list[int], q: int, D: int) -> dict:
    m, A, F = len(word), sum(word), sum(base)
    edits = [i for i in range(m) if word[i] != base[i]]
    s = len(edits)
    if s == 0:
        return dict(chunks=0, empty_runs=0, raised_uniform_checks=0, mode="unedited",
                    minimum_at_start=0, minimum_at_end=0)
    low_index = states.index(min(states))
    runs = [((edits[j - 1] + 1) % m, edits[j],
             (edits[j] - edits[j - 1] - 1) % m) for j in range(s)]
    containing = [run for run in runs if (low_index - run[0]) % m <= run[2]]
    require(bool(containing), "minimum outside all clean runs")
    start, end, length = containing[0]
    for a, b, size in runs:
        require((a + size) % m == b, "clean run endpoints")
        require(all(word[(a + j) % m] == base[(a + j) % m] for j in range(size)),
                "edited letter inside clean run")
        N = states[a] + q * m
        require(1 << size < 1024 * N**5, "clean run length bound")
    expanding = 3**m > 1 << F
    cut = start if expanding else end
    if expanding:
        require(states[cut] < 2 * min(states), "expanding minimum-adjacent cut")
    else:
        require(3 * states[cut] < 6 * min(states) + 2 * m * q,
                "contracting minimum-adjacent cut")
    N0 = states[cut] + q * m
    require(3 * N0 * D < 7 * m * q * (1 << A), "initial shifted height")

    position, covered, visited = cut, 0, []
    for _ in range(s):
        if expanding:
            edit = min(edits, key=lambda e: (e - position) % m)
            size = (edit - position) % m + 1
            successor = (edit + 1) % m
        else:
            require(position in edits, "edit-first chunk starts at clean arrow")
            edit = position
            following = [e for e in edits if e != position]
            successor = min(following, key=lambda e: (e - position) % m) if following else position
            size = (successor - position) % m or m
        require(size >= 1, "empty chunk")
        chunk_edits = [e for e in edits if (e - position) % m < size]
        require(chunk_edits == [edit], "chunk does not contain exactly one edit")
        N, Nnext = states[position] + q * m, states[successor] + q * m
        require(1 << size < 32768 * N**5, "chunk length bound")
        require(Nnext < 512 * N**4, "chunk logarithmic growth")
        require((Nnext << size) <= 3**size * N, "generic shifted growth")
        covered += size
        visited.append(edit)
        position = successor
    require(covered == m and position == cut and sorted(visited) == edits, "exact s-chunk cover")
    K = 5 * (4**s - 1) // 3
    require(3 * K == 5 * (4**s - 1), "integer geometric coefficient")
    # Exact real-exponent comparison, after raising both sides to K.
    # Large-fixture edit counts would make this redundant power enormous;
    # their full cut/chunk chain and a weakened integer exponent are checked.
    raised = int(s <= 4)
    if raised:
        require((32 * m * q * (1 << A))**K > (D**K) << m,
                "unconditional all-slope denominator law")
    require(32 * m * q * (1 << A) > D << (m // K), "integer all-slope lower bound")
    return dict(chunks=s, empty_runs=sum(size == 0 for _, _, size in runs),
                raised_uniform_checks=raised, mode="expanding" if expanding else "contracting",
                minimum_at_start=int(low_index == start), minimum_at_end=int(low_index == end))


def check_pair(word: list[int], base: list[int]) -> dict:
    m, A, F = len(word), sum(word), sum(base)
    require(m >= 2 and len(base) == m and min(word) > 0, "word scope")
    require(primitive(word), "nonprimitive sample")
    two, three, base_two = 1 << A, 3**m, 1 << F
    D, C = two - three, intercept(word)
    require(D > 0, "nonpositive denominator")
    common = gcd(C, D)
    q = D // common
    current, states = C, []
    for i, letter in enumerate(word):
        require(current > 0 and current % 2 == 1, "positive odd state")
        require(gcd(current, D) == common, "rotation gcd")
        states.append(current // common)
        raw = 3 * current + D
        require(raw % (1 << letter) == 0, "nonintegral exact arrow")
        successor = raw >> letter
        require(successor % 2 == 1, "incorrect exact valuation")
        if i in (0, m - 1):
            require(successor == intercept(word[i + 1:] + word[:i + 1]),
                    "direct rotated intercept")
        current = successor
    require(current == C and len(set(states)) == m, "primitive closure")
    for i, letter in enumerate(word):
        require(3 * states[i] + q == (1 << letter) * states[(i + 1) % m],
                "actual reduced arrow")

    s = sum(x != y for x, y in zip(word, base))
    B = sum(max(y - x, 0) for x, y in zip(word, base))
    t = (m - 2) // (s + 1)
    doubled, doubled_base, doubled_states = word + word, base + base, states + states
    types = {tuple(doubled_base[i:i + t]) for i in range(m)}
    require(len(types) <= t + 1, "mechanical factor complexity")
    untouched = [i for i in range(m) if doubled[i:i + t] == doubled_base[i:i + t]]
    require(len(untouched) >= m - s * t >= t + 2, "unchanged-window count")
    seen: dict[tuple[int, ...], int] = {}
    repeat = None
    for j in untouched:
        factor = tuple(doubled[j:j + t])
        if factor in seen:
            repeat = seen[factor], j
            break
        seen[factor] = j
    require(repeat is not None, "missing repeated factor")
    i, j = repeat
    E = sum(doubled[i:i + t])
    z_start = states[j] - states[i]
    z_end = doubled_states[j + t] - doubled_states[i + t]
    require(z_start != 0 and z_end != 0, "zero state separation")
    require(z_start % (1 << (E + 1)) == 0, "dyadic repeat separation")
    require((1 << E) * z_end == 3**t * z_start, "run identity")
    require(z_end % (2 * 3**t) == 0, "ternary repeat separation")

    factor_checks = 0
    for start in range(m):
        actual_total = base_total = 0
        for length in range(1, m):
            actual_total += doubled[start + length - 1]
            base_total += doubled_base[start + length - 1]
            require(abs(m * base_total - F * length) < m, "mechanical balance")
            require(m * (actual_total + B + 1) > F * length, "signed factor balance")
            factor_checks += 1
    low, high = min(states), max(states)
    K, M = 1 << (B + 1), max(three, base_two)
    require(high > 2 * 3**t, "repeat maximum bound")
    require(3 * high * base_two <= K * M * (3 * low + m * q), "balanced growth bound")
    require(3 * low * D < m * q * two, "minimum from drift")
    require(q * K * m * M * two > 3**(t + 1) * base_two * D,
            "general denominator law")
    require(m * B <= s * F and m * A >= F * (m - s), "edit budget inequalities")
    if m >= 8 * s and 4 * A < 7 * m:
        require(F < 2 * m and B <= s, "denominator-one decrease-budget implication")
    if s <= 2:
        require(q > 1, "finite two-edit control has denominator one")
    chunks = check_chunks(word, base, states, q, D)
    return dict(m=m, A=A, F=F, s=s, B=B, q=q, minimum=low, maximum=high,
                factor_checks=factor_checks, repeat_length=t, chunk_checks=chunks)


def sample_words() -> dict:
    counts = dict(bases=0, edit_recipes=0, eligible=0, nonpositive_D=0,
                  nonprimitive=0, arrows=0, cyclic_factor_checks=0,
                  with_increases=0, with_decreases=0, mixed_signs=0,
                  unedited=0, two_edit_class=0, chunks=0, empty_runs=0,
                  expanding_cuts=0, contracting_cuts=0, minimum_at_start=0,
                  minimum_at_end=0, raised_uniform_checks=0)
    digest = hashlib.sha256()
    for m in range(2, 13):
        for F in list(range(m, 3 * m + 1)) + [5 * m - 1]:
            for phase in range(m):
                base = mechanical(m, F, phase)
                require(min(base) > 0 and sum(base) == F, "mechanical construction")
                h = (F + phase) % m
                require(base[h:] + base[:h] == mechanical(m, F, (phase + h * F) % m),
                        "phase rotation")
                counts["bases"] += 1
                for requested in range(min(4, m) + 1):
                    schedules = [0] if requested == 0 else [0, 1]
                    patterns = [0] if requested == 0 else range(6)
                    for schedule in schedules:
                        positions = [((phase + j) if schedule == 0 else
                                      (phase + j * m // requested)) % m
                                     for j in range(requested)]
                        require(len(set(positions)) == requested, "edit-position recipe")
                        for pattern in patterns:
                            word = base.copy()
                            for j, position in enumerate(positions):
                                x = base[position]
                                values = [x + 1, x + 17, max(1, x - 1), 1,
                                          x + 9 if j % 2 == 0 else 1,
                                          1 if j % 2 == 0 else 7]
                                word[position] = values[pattern]
                            counts["edit_recipes"] += 1
                            if (1 << sum(word)) <= 3**m:
                                counts["nonpositive_D"] += 1
                                continue
                            if not primitive(word):
                                counts["nonprimitive"] += 1
                                continue
                            result = check_pair(word, base)
                            counts["eligible"] += 1
                            counts["arrows"] += m
                            counts["cyclic_factor_checks"] += result["factor_checks"]
                            inc = any(x > y for x, y in zip(word, base))
                            dec = any(x < y for x, y in zip(word, base))
                            counts["with_increases"] += inc
                            counts["with_decreases"] += dec
                            counts["mixed_signs"] += inc and dec
                            counts["unedited"] += result["s"] == 0
                            counts["two_edit_class"] += result["s"] <= 2
                            chunk = result["chunk_checks"]
                            for key in ("chunks", "empty_runs", "minimum_at_start", "minimum_at_end",
                                        "raised_uniform_checks"):
                                counts[key] += chunk[key]
                            counts["expanding_cuts"] += chunk["mode"] == "expanding"
                            counts["contracting_cuts"] += chunk["mode"] == "contracting"
                            digest.update((str((word, base, result["q"])) + "\n").encode())
    require(all(counts[x] > 0 for x in ("mixed_signs", "unedited", "two_edit_class",
                                      "expanding_cuts", "contracting_cuts", "empty_runs",
                                      "minimum_at_start", "minimum_at_end")),
            "missing required sample regime")
    return dict(scope=dict(m=[2, 12], F="m through 3m, and 5m-1", phase="all 0 through m-1",
                           edited_positions="0 through min(4,m), cyclic consecutive or evenly spaced",
                           replacement_recipes=["+1", "+17", "max(1,x-1)", "1",
                                                "alternate +9 and 1", "alternate 1 and 7"]),
                counts=counts, denominator_sha256=digest.hexdigest())


def cutoffs_and_finite_closure() -> dict:
    require(3**2 > 2**3 and 3**5 < 2**8, "logarithm comparisons")
    require(10**4 < 2**7 * 3**4, "q1 average bound")
    require(174 + 342 * 32 == 11118 < 16384, "square-root base comparison")
    require(2**16 > 5472 and 2**32 - 2**16 > 8, "square-root derivative and tail")
    require(CUTOFF - 25 * (177 + 342 * 18) == 103819,
            "two-edit cutoff value")
    require(CUTOFF > 25 * 684, "two-edit cutoff derivative")
    three = 1
    comparisons = 0
    for m in range(1, CUTOFF):
        three *= 3
        if m < 560:
            continue
        A_min = three.bit_length()
        D_min = (1 << A_min) - three
        require(D_min << (m // 25) > (32 * m) << A_min,
                f"finite denominator comparison failed at length {m}")
        comparisons += 1
    products = 0
    for m in range(2, 560):
        A_min = (3**m).bit_length()
        require((3 * LOCAL_LIMIT + 1)**m < 1 << (A_min + 18 * m),
                f"finite product comparison failed at length {m}")
        products += 1
    K_ten = 5 * (4**10 - 1) // 3
    require(K_ten * (177 + 342 * 35) < 1 << 35, "ten-edit cutoff value")
    require(684 * K_ten < 1 << 35, "ten-edit cutoff derivative")
    period_path = ROOT / "areas/cycles/results/cycle-length-lower-bound-from-convergents/cycle_length_convergents.json"
    period_receipt = json.loads(period_path.read_text())
    period = int(period_receipt["V3"]["2^71"]["least_m"])
    require(period == 72057431991 > 1 << 35, "declared period lower bound")
    return dict(square_root_length_cutoff=2**32, square_root_base_left=11118,
                square_root_base_right=16384, two_edit_length_cutoff=CUTOFF,
                two_edit_cutoff_numerator=103819, two_edit_cutoff_denominator=25,
                denominator_length_range=[560, CUTOFF - 1], denominator_comparisons=comparisons,
                small_length_range=[2, 559], small_product_comparisons=products,
                ten_edit_K=K_ten, ten_edit_length_cutoff=2**35,
                ten_edit_cutoff_right=K_ten * (177 + 342 * 35),
                ten_edit_derivative_numerator=684 * K_ten,
                declared_period_lower_bound=period,
                ten_edit_extra_external_input="barina-2025-convergence-2-71")


def local_descent() -> dict:
    seeds = steps = maximum_steps = 0
    first_maximum_seed = peak_odd = peak_raw = 1
    for seed in range(3, LOCAL_LIMIT, 2):
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
            raise RuntimeError(f"descent guard exhausted for seed {seed}")
        seeds += 1
        steps += count
        if count > maximum_steps:
            maximum_steps, first_maximum_seed = count, seed
    require(seeds == LOCAL_LIMIT // 2 - 1, "incomplete local descent")
    return dict(odd_seed_range=[3, LOCAL_LIMIT - 1], odd_seeds=seeds, odd_steps=steps,
                maximum_local_steps=maximum_steps, first_seed_at_maximum=first_maximum_seed,
                peak_odd=peak_odd, peak_raw=peak_raw, per_seed_guard=DESCENT_GUARD)


def controls() -> dict:
    path = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    cycles = json.loads(path.read_text())["cycles"]
    arrows = comparisons = 0
    for cycle in cycles:
        d, states, word = cycle["d"], cycle["states"], cycle["valuations"]
        require(len(states) == len(word) and min(states) == cycle["minimum"], "control shape")
        for i, letter in enumerate(word):
            require(states[i] > 0 and states[i] % 2 == 1, "control oddness")
            require(3 * states[i] + d == (1 << letter) * states[(i + 1) % len(word)],
                    "actual control arrow")
            arrows += 1
        D = (1 << sum(word)) - 3**len(word)
        q = D // gcd(intercept(word), D)
        require(D > 0 and d % q == 0, "control denominator")
        if len(word) >= 2:
            for phase in range(len(word)):
                result = check_pair(word, mechanical(len(word), sum(word), phase))
                require(result["q"] == q, "control pair denominator")
                comparisons += 1
    mixed = check_pair([1, 1, 3], [1, 2, 2])
    require(mixed["q"] == 5 and mixed["s"] == 2 and mixed["B"] == 1,
            "mixed-sign inside-class control")
    word = [2] * 64
    D = (1 << 128) - 3**64
    q = D // gcd(intercept(word), D)
    require(not primitive(word) and q == 1, "nonprimitive control")
    require(q * 2 * 64 * (1 << 128) <= 3**63 * D,
            "nonprimitive control does not refute the unscoped law")
    base = mechanical(64, 127, 0)
    require(sum(x != y for x, y in zip(word, base)) == 1, "nonprimitive one-edit control")
    require((32 * 64 * q * (1 << 128))**5 <= (D**5) << 64,
            "nonprimitive control does not refute the all-slope law")
    require({x["d"] for x in cycles} == {5, 7, 13, 61}, "missing addend control")
    return dict(addends=[5, 7, 13, 61], actual_cycles=len(cycles), actual_arrows=arrows,
                same_total_mechanical_comparisons=comparisons, mixed_sign_two_edit=mixed,
                nonprimitive_countercontrol=dict(word="(2)^64", q=q,
                                                  unscoped_law_fails=True))


def main() -> None:
    receipt = dict(schema="mechanical-edit-denominator-law-v1", samples=sample_words(),
                   finite_closure=cutoffs_and_finite_closure(), local_descent=local_descent(),
                   controls=controls())
    (HERE / "check_edit_law.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print("PASS mechanical-edit denominator law: "
          f"{receipt['samples']['counts']['eligible']} word pairs; "
          f"{receipt['finite_closure']['denominator_comparisons']} length comparisons; "
          f"{receipt['local_descent']['odd_seeds']} odd descents; "
          f"{receipt['controls']['actual_cycles']} actual-cycle controls")


if __name__ == "__main__":
    main()
