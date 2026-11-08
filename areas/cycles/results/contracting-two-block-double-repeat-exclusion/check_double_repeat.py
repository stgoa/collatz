"""Exact finite support for the contracting double-repeat denominator law.

The unbounded result is proved in README.md and assumes EXT-1 only above
the finite gap range. This certificate replays all short-length comparisons,
the exact dyadic cutoff, declared contracting-block controls, and true
3x+q cycles. Common fixed points and expanding blocks are kept as explicit
out-of-scope controls. Checks remain active under python -O.
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
    value = total = 0
    for letter in word:
        value = 3 * value + 2**total
        total += letter
    return value


def block_data(word):
    p, q, c = 3**len(word), 2**sum(word), intercept(word)
    return p, q, q - p, c


def reduced_cycle(word):
    p, binary, gap, c = block_data(word)
    need(gap > 0, "positive cycle gap")
    common = gcd(c, gap)
    q = gap // common
    first = c // common
    state = first
    states = []
    for letter in word:
        need(state > 0 and state % 2 == 1, "positive odd actual state")
        states.append(state)
        raw = 3 * state + q
        valuation = (raw & -raw).bit_length() - 1
        need(valuation == letter, "exact raw odd-only valuation")
        state = raw >> letter
    need(state == first, "exact reduced cycle closure")
    return q, states


def gap_comparisons():
    p = 1
    digest = sha256()
    minimum = None
    for length in range(1, 8192):
        p *= 3
        a_min = p.bit_length()
        binary = 1 << a_min
        need(binary // 2 <= p < binary, "least contracting binary total")
        left = (1 << (length + 1)) * (binary - p)
        need(left >= binary, "short-length relative-gap inequality")
        ratio = Fraction(left, binary)
        if minimum is None or ratio < minimum[0]:
            minimum = (ratio, length, a_min)
        digest.update(f"{length}:{a_min}:{left:x}:{binary:x}\n".encode())
    start = 2**13 - 171 - 341 * 14
    need(start == 3247 and start > 0, "large-length dyadic base case")
    need(2**13 > 341, "positive increments for every j>=13")
    # The difference of successive dyadic lower bounds is exactly 2^j-341.
    need((2**14 - 171 - 341 * 15) - start == 2**13 - 341,
         "dyadic increment identity at the smallest permitted exponent")
    return {"lengths": [1, 8191], "comparisons": 8191,
            "minimum_ratio": str(minimum[0]), "minimum_length": minimum[1],
            "minimum_total": minimum[2], "comparisons_sha256": digest.hexdigest(),
            "large_cutoff": 8192, "dyadic_exponent": 13, "dyadic_base_margin": start,
            "dyadic_increment_formula": "2^j-341, positive for every j>=13",
            "outside_input": "EXT-1 for all block lengths >=8192; not re-proved by this script"}


def check_pair(u, v, k, ell):
    """Reconstruct true states and independently check both repetition budgets."""
    pu, qu, du, cu = block_data(u)
    pv, qv, dv, cv = block_data(v)
    need(du > 0 and dv > 0, "both selected blocks contract")
    a, b = Fraction(cu, du), Fraction(cv, dv)
    commutator = du * cv - dv * cu
    maximum_length = max(len(u), len(v))
    need(a < 2 * 3**len(u) and b < 2 * 3**len(v), "finite-control fixed-point ceiling")
    need(cu * 2**len(u) < qu * pu and cv * 2**len(v) < qv * pv,
         "ordinary intercept upper bounds")
    word = u * k + v * ell
    q, states = reduced_cycle(word)
    if not commutator:
        need(a == b and Fraction(states[0], q) == a, "common fixed point retained")
        if len(u) == len(v):
            need(u == v, "equal-length common fixed points have identical words")
        return {"commutator_zero": True, "q": q, "arrows": len(states)}

    need(a != b, "nonzero commutator means different fixed points")
    alpha, beta = Fraction(pu, qu), Fraction(pv, qv)
    t, z = alpha**k, beta**ell
    factor = (1 - z) / (1 - t * z)
    need(0 < factor < 1, "strict contracting interpolation coefficient")
    need(Fraction(states[0], q) == a + (b - a) * factor, "exact fixed-point composition")
    lower, upper = sorted((a, b))
    boundary_indices = [i * len(u) for i in range(k + 1)]
    boundary_indices += [k * len(u) + i * len(v) for i in range(ell + 1)]
    for index in boundary_indices:
        need(lower < Fraction(states[index % len(word)], q) < upper,
             "all actual block starts lie strictly in the fixed-point interval")

    for p, binary, count, length, offset in (
        (pu, qu, k, len(u), 0),
        (pv, qv, ell, len(v), k * len(u)),
    ):
        boundaries = [states[(offset + i * length) % len(word)] for i in range(count + 1)]
        first_difference = boundaries[1] - boundaries[0]
        last_difference = boundaries[-1] - boundaries[-2]
        budget = binary**(count - 1)
        need(first_difference != 0, "nonzero repeated-block difference")
        need(p**(count - 1) * first_difference == budget * last_difference,
             "exact repeated affine difference")
        need(first_difference % (2 * budget) == 0, "even lattice divisibility")
        need(2 * budget <= abs(first_difference) < q * abs(a - b) < q * max(a, b),
             "strict interval and lattice chain")
        need(q * 3**maximum_length > budget, "uniform denominator law with true q")

    budget_u, budget_v = qu**(k - 1), qv**(ell - 1)
    if max(budget_u, budget_v) >= 3**maximum_length:
        need(q > 1, "repetition-budget exclusion")
    return {"commutator_zero": False, "q": q, "arrows": len(states),
            "budget_eligible": max(budget_u, budget_v) >= 3**maximum_length,
            "equal_length": len(u) == len(v),
            "unequal_totals": sum(u) != sum(v),
            "U": list(u), "V": list(v), "k": k, "ell": ell,
            "budget_u": budget_u, "budget_v": budget_v,
            "first_state": states[0]}


def grid_controls():
    words = [word for length in range(1, 4)
             for word in product(range(1, 5), repeat=length)
             if 2**sum(word) > 3**length]
    counts = Counter()
    digest = sha256()
    examples = {}
    for u in words:
        for v in words:
            for k in range(1, 4):
                for ell in range(1, 4):
                    row = check_pair(u, v, k, ell)
                    counts["pairs_with_counts"] += 1
                    counts["actual_arrows"] += row["arrows"]
                    if row["commutator_zero"]:
                        counts["common_fixed_point_cases"] += 1
                    else:
                        counts["nonzero_commutator_cases"] += 1
                        counts["budget_eligible_cases"] += int(row["budget_eligible"])
                        counts["equal_length_unequal_total_cases"] += int(
                            row["equal_length"] and row["unequal_totals"])
                        if row["equal_length"] and row["unequal_totals"] and k == 2 and ell == 1:
                            examples.setdefault("equal_length_unequal_totals", row)
                        if len(u) != len(v) and row["budget_eligible"] and k == 2 and ell == 1:
                            examples.setdefault("unequal_lengths_two_copies", row)
                    digest.update((json.dumps(row, sort_keys=True) + "\n").encode())
    return {"ranges": {"block_lengths": [1, 3], "letters": [1, 4],
                       "k": [1, 3], "ell": [1, 3], "filter": "both blocks contract"},
            "contracting_blocks": len(words), "counts": dict(sorted(counts.items())),
            "examples": examples, "cases_sha256": digest.hexdigest()}


def aligned_controls():
    counts = Counter()
    examples = {}
    digest = sha256()
    for length in range(2, 5):
        for u in product(range(1, 4), repeat=length):
            if 2**sum(u) <= 3**length:
                continue
            for first in range(length):
                for second in range(first + 1, length):
                    for change_a in (-2, -1, 1, 2):
                        for change_b in (-2, -1, 1, 2):
                            if change_a + change_b == 0:
                                continue
                            v = list(u)
                            v[first] += change_a
                            v[second] += change_b
                            if min(v) <= 0 or 2**sum(v) <= 3**length:
                                continue
                            v = tuple(v)
                            word = u + u + v
                            need(sum(word[i] != word[(i + length) % len(word)]
                                     for i in range(len(word))) == 4,
                                 "aligned third-period four-mismatch control")
                            row = check_pair(u, v, 2, 1)
                            need(not row["commutator_zero"] and row["budget_eligible"],
                                 "aligned unequal-total corollary hypotheses")
                            category = ("opposite_unequal" if change_a * change_b < 0 else
                                        "both_increased" if change_a > 0 else "both_decreased")
                            counts[category] += 1
                            counts["actual_arrows"] += row["arrows"]
                            row["changes"] = [change_a, change_b]
                            examples.setdefault(category, row)
                            digest.update((json.dumps(row, sort_keys=True) + "\n").encode())
    need(all(counts[key] > 0 for key in ("opposite_unequal", "both_increased", "both_decreased")),
         "all unequal signed-change categories exercised")
    return {"ranges": {"lengths": [2, 4], "template_letters": [1, 3],
                       "changes": [-2, -1, 1, 2], "net_change": "nonzero",
                       "filter": "positive distinct blocks, both contracting"},
            "counts": dict(sorted(counts.items())), "examples": examples,
            "cases_sha256": digest.hexdigest()}


def external_class_controls():
    raw = FIXTURES.read_bytes()
    fixtures = json.loads(raw)["cycles"]
    common = []
    fixture_arrows = 0
    for fixture in fixtures:
        word = tuple(fixture["valuations"])
        states, addend = fixture["states"], fixture["d"]
        need(addend in (5, 7, 13, 61), "standard control addend")
        for i, letter in enumerate(word):
            value = 3 * states[i] + addend
            need((value & -value).bit_length() - 1 == letter, "fixture exact valuation")
            need(value >> letter == states[(i + 1) % len(states)], "fixture exact arrow")
            fixture_arrows += 1
        row = check_pair(word * 2, word, 2, 1)
        need(row["commutator_zero"] and addend % row["q"] == 0,
             "true fixture repeated at a common fixed point")
        common.append({"addend": addend, "denominator": row["q"],
                       "original_length": len(word), "repeated_arrows": row["arrows"]})
    need(len(fixtures) == 11 and fixture_arrows == 106, "all standard fixture arrows retained")
    trivial = check_pair((2,), (2, 2), 2, 1)
    need(trivial["commutator_zero"] and trivial["q"] == 1, "trivial 3x+1 repetition retained")

    mixed = []
    for u, v, k, ell in (((1,), (1, 3), 4, 3), ((2, 2), (1, 1), 2, 1)):
        pu, qu, du, cu = block_data(u)
        pv, qv, dv, cv = block_data(v)
        need(du * dv < 0, "one expanding block in the mixed-direction control")
        word = u * k + v * ell
        q, states = reduced_cycle(word)
        fixed = sorted((Fraction(cu, du), Fraction(cv, dv)))
        initial = Fraction(states[0], q)
        need(not (fixed[0] < initial < fixed[1]), "contracting interval does not extend to mixed directions")
        mixed.append({"U": list(u), "V": list(v), "k": k, "ell": ell,
                      "q": q, "first_state": states[0],
                      "fixed_points": [str(value) for value in fixed],
                      "actual_arrows": len(states)})
    need(mixed[0]["q"] == 499 and mixed[0]["first_state"] == 6605,
         "existing expanding-block obstruction retained")
    return {"fixture_sha256": sha256(raw).hexdigest(), "fixture_arrows": fixture_arrows,
            "common_fixed_point_fixtures": common, "trivial_control": trivial,
            "mixed_direction_controls": mixed}


def run():
    return {"schema": "contracting-double-repeat-v1", "gap": gap_comparisons(),
            "grid": grid_controls(), "aligned_third_period": aligned_controls(),
            "controls": external_class_controls(),
            "scope": "Finite exact checks of the written argument; the large-length gap uses declared EXT-1."}


def main():
    need(sys.argv[1:] in ([], ["--write-receipt"]), "usage: check_double_repeat.py [--write-receipt]")
    data = run()
    output = json.dumps(data, sort_keys=True, indent=2) + "\n"
    receipt = HERE / "check_double_repeat.json"
    if sys.argv[1:]:
        receipt.write_text(output)
    else:
        need(receipt.read_text() == output, "receipt mismatch; regenerate deliberately")
    print(json.dumps({"gap_comparisons": data["gap"]["comparisons"],
                      "grid": data["grid"]["counts"],
                      "aligned": data["aligned_third_period"]["counts"],
                      "standard_cycles": len(data["controls"]["common_fixed_point_fixtures"])}, sort_keys=True))


if __name__ == "__main__":
    main()
