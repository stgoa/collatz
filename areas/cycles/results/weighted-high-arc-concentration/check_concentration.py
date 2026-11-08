"""Exact checks for the unequal weighted high-arc concentration theorem.

The manuscript proves the unbounded convexity and localization arguments.
The finite profile grid checks their formulas, including collisions and
unequal positive weights; it is not an absence census. Existing exact
logarithm, descent, and period arithmetic is rerun after source/receipt
hash checks. The imported period comparison alone uses Barina's input.
"""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
import importlib.util
from itertools import permutations, product
import json
from math import gcd, prod
from pathlib import Path
import sys


sys.dont_write_bytecode = True
F = Fraction
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
COMMON_DIR = ROOT / "areas/cycles/results/contiguous-maximum-four-arc-exclusion"
COMMON_SOURCE_HASH = "53c9c0c3576ccf8a1ffdf37d3ab1576aef265bf7f69ebf69387242f552c2052f"
COMMON_RECEIPT_HASH = "6648f377249a5ef745fd835c592d335f5345019cf4a13ac18e9415906a4d1391"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_common():
    source = COMMON_DIR / "check_maximum_arc.py"
    receipt = COMMON_DIR / "check_maximum_arc.json"
    require(sha256(source.read_bytes()).hexdigest() == COMMON_SOURCE_HASH,
            "pinned common arithmetic source")
    require(sha256(receipt.read_bytes()).hexdigest() == COMMON_RECEIPT_HASH,
            "pinned common arithmetic receipt")
    spec = importlib.util.spec_from_file_location("weighted_arc_common", source)
    require(spec is not None and spec.loader is not None, "common loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    expected = json.loads(receipt.read_text())
    replay = {}
    for name in ("constants", "exact_gap", "local_descent", "standard_controls"):
        value = getattr(module, name)()
        require(value == expected[name], "common arithmetic replay: " + name)
        replay[name] = value
    replay["source_sha256"] = COMMON_SOURCE_HASH
    replay["receipt_sha256"] = COMMON_RECEIPT_HASH
    replay["scope"] = (
        "Only constants, exact_gap, local_descent and standard_controls are rerun. "
        "The rational gap and local descent are independent of Barina; its "
        "external input supplies only the separately labelled period comparison."
    )
    return module, replay


def exact_constants(common):
    rise = F(8, 5) ** 5 - 1
    require(rise == F(29643, 3125), "exact four-mismatch rise factor")
    require(3 ** 12 > 2 ** 19, "alpha greater than 19/12")
    coefficient = F(19, 48) - rise / 25
    require(coefficient == F(61511, 3750000) > 0,
            "positive short-rotation coefficient")
    ell_coefficient = 1 + rise
    require(ell_coefficient == F(32768, 3125), "minimum coefficient")
    base = coefficient * 2 ** 23 - (
        ell_coefficient * (172 + 342 * 24) + rise + F(7, 12)
    )
    require(base == F(46609724897, 937500) > 0, "localization base")
    increment = ell_coefficient * 342
    require(coefficient * 2 ** 23 > increment, "localization dyadic induction")
    require(3 * F(1, 15) * (6 - 1) == 1, "six high positions imply cone")
    final = F(common["constants"]["post_gap_full_period_upper"])
    require(final == F(32760462311424, 30625), "cone cutoff")
    integer_bound = final.numerator // final.denominator
    require(integer_bound == 1069729381 and 2 ** 23 < integer_bound < 2 ** 30,
            "common integer bound, including small periods")
    require(common["constants"]["imported_odd_period_lower"] > 2 ** 30,
            "separately sourced all-length exclusion")
    spread_margin = F(1, 4) - F(2, 3) * F(6103, 16383)
    require(spread_margin == F(325, 196596) > F(1, 1216),
            "unequal weighted cone margin")
    return {
        "rise_factor": str(rise),
        "short_rotation_coefficient": str(coefficient),
        "minimum_coefficient": str(ell_coefficient),
        "localization_cutoff_bits": 23,
        "localization_base_margin": str(base),
        "localization_linear_increment": str(increment),
        "cone_obstruction_margin": str(spread_margin),
        "cone_integer_period_upper": integer_bound,
        "large_multiplicity_threshold": 6,
        "surviving_high_multiplicity_upper": 5,
        "clock": "full primitive odd-only period",
    }


def residue_one(value):
    return value % 1 or F(1)


def weighted_profile(points):
    """Return the range of slope=sum(weights), with pre/post jump extremes."""
    total = sum(points.values())
    consumed = 0
    low = high = F(0)
    for point, weight in sorted(points.items()):
        require(0 < point <= 1 and weight > 0, "profile point domain")
        before = total * point - consumed
        after = before - weight
        low = min(low, after)
        high = max(high, before)
        consumed += weight
    require(consumed == total, "all weighted drops counted")
    return low, high


def arc_points(length, step, origin=F(1)):
    return Counter(residue_one(origin - j * step) for j in range(length))


def single_arc_checks():
    endpoints = interiors = clustered = spread = cone = 0
    checksum = sha256()
    for length in range(2, 49):
        threshold = F(1, 3 * (length - 1))
        cuts = {threshold, F(1, length), F(1, 2)}
        for denominator in range(2, length):
            for numerator in range(1, denominator // 2 + 1):
                step = F(numerator, denominator)
                if threshold <= step <= F(1, 2):
                    cuts.add(step)
        ordered = sorted(cuts)
        values = []
        for step in ordered:
            low, high = weighted_profile(arc_points(length, step))
            oscillation = high - low
            if length * step <= 1:
                require(oscillation == length * (1 - (length - 1) * step),
                        "exact cluster oscillation")
                clustered += 1
            if length * step >= 1:
                q = step.denominator
                if q <= length:
                    copies, tail = divmod(length, q)
                    require(copies >= 1 and 2 <= q <= length, "collision denominator")
                    require(tail <= q - 1 <= copies * (2 * q - 3),
                            "general rational endpoint inequality")
                    require(oscillation <= copies + tail <= F(2 * length, 3),
                            "uniform grids and remainder")
                require(oscillation <= F(2 * length, 3), "spread oscillation")
                spread += 1
            require(oscillation <= F(2 * length, 3), "cone endpoint bound")
            cone += 1
            values.append(oscillation)
            checksum.update(f"{length}:{step}:{low}:{high}\n".encode())
            endpoints += 1
        for index in range(len(ordered) - 1):
            for ratio in (F(1, 3), F(1, 2), F(2, 3)):
                step = (1 - ratio) * ordered[index] + ratio * ordered[index + 1]
                low, high = weighted_profile(arc_points(length, step))
                oscillation = high - low
                chord = (1 - ratio) * values[index] + ratio * values[index + 1]
                require(oscillation <= chord <= F(2 * length, 3),
                        "ordering-cell convexity control")
                if length * step <= 1:
                    require(oscillation == length * (1 - (length - 1) * step),
                            "cluster interior formula")
                interiors += 1
    return {
        "arc_lengths": [2, 48],
        "complete_collision_and_cone_endpoints": endpoints,
        "interior_convexity_controls": interiors,
        "cluster_formula_endpoints": clustered,
        "spread_endpoints": spread,
        "cone_endpoints": cone,
        "profile_sha256": checksum.hexdigest(),
        "scope": "All ordering-cell endpoints in the stated bounded lengths; manuscript convexity proves the unbounded claim.",
    }


def weighted_cone_checks():
    steps = sorted({F(p, q) for q in range(2, 21) for p in range(1, q // 2 + 1)})
    count = overlaps = 0
    checksum = sha256()
    for c, d in product(range(2, 9), repeat=2):
        for step in steps:
            if 3 * step * (min(c, d) - 1) < 1:
                continue
            first = arc_points(c, step)
            first_low, first_high = weighted_profile(first)
            for origin in (F(1, 7), F(3, 5), F(1)):
                second = arc_points(d, step, origin)
                second_low, second_high = weighted_profile(second)
                for A, B in ((1, 2), (2, 7), (17, 1)):
                    weighted = Counter({point: A * weight for point, weight in first.items()})
                    weighted.update({point: B * weight for point, weight in second.items()})
                    low, high = weighted_profile(weighted)
                    upper = A * (first_high - first_low) + B * (second_high - second_low)
                    require(high - low <= upper <= F(2 * (A * c + B * d), 3),
                            "unequal weighted subadditivity")
                    overlaps += bool(set(first) & set(second))
                    checksum.update(f"{c}:{d}:{step}:{origin}:{A}:{B}:{high-low}\n".encode())
                    count += 1
    require(count > 0 and overlaps > 0, "weighted and coincident controls present")
    return {
        "arc_lengths": [2, 8],
        "step_denominators_up_to": 20,
        "translations": ["1/7", "3/5", "1"],
        "positive_weight_pairs": [[1, 2], [2, 7], [17, 1]],
        "weighted_profiles": count,
        "profiles_with_shared_points": overlaps,
        "profile_sha256": checksum.hexdigest(),
        "scope": "Continuous profile controls may overlap; actual word controls below keep all four arcs disjoint.",
    }


def actual_family_checks(common):
    words = cycles = arrows = factors = cone_words = cone_cycles = runs = 0
    adjacent = separated = 0
    orders_seen = set()
    checksum = sha256()
    examples = {}
    label_sets = ((1, 2, 3, 5), (1, 2, 5, 9), (1, 5, 6, 8))
    extra_lengths = ((1, 1, 6, 6), (1, 2, 6, 7), (2, 3, 8, 6))
    length_cases = list(product(range(1, 4), repeat=4)) + list(extra_lengths)
    large_multiplicity_controls = 0
    for lengths in length_cases:
        m = sum(lengths)
        for high_order in permutations((1, 2, 3)):
            order = (0,) + high_order
            high_adjacent = ((order.index(2) - order.index(3)) % 4) in (1, 3)
            for h in range(1, (m + 1) // 2):
                if gcd(h, m) != 1:
                    continue
                step = F(h, m)
                k = pow(h, -1, m)
                K = common.continued_fraction_sum(k, m)
                c, d = lengths[2], lengths[3]
                cone = c >= 2 and d >= 2 and 3 * h * (min(c, d) - 1) >= m
                for labels in label_sets:
                    t, U, V = labels[1:]
                    A, B = U - t, V - t
                    W = c * A + d * B
                    track = [labels[index] for index in order for _ in range(lengths[index])]
                    word = [0] * m
                    for index, letter in enumerate(track):
                        word[(index * h) % m] = letter
                    boundaries = {index for index in range(m) if word[index] != word[(index + h) % m]}
                    require(len(boundaries) == 4, "all four exact boundaries")
                    require(all(any(word[index] != word[(index + shift) % m] for index in range(m))
                                for shift in range(1, m)), "four-label word is primitive")
                    template = [t if letter in (U, V) else letter for letter in word]
                    require(sum(abs(template[index] - template[(index + h) % m])
                                for index in range(m)) == 2 * (t - 1),
                            "low template variation for every cyclic order")
                    require(sum(word) == sum(template) + W, "weighted edit total")
                    high_weights = {index + 1: (A if letter == U else B)
                                    for index, letter in enumerate(word) if letter in (U, V)}
                    scaled = [W * (index + 1) - m * sum(weight for point, weight in high_weights.items()
                                                      if point < index + 1)
                              for index in range(m)]
                    low, high = weighted_profile(Counter({F(point, m): weight
                                                         for point, weight in high_weights.items()}))
                    oscillation = high - low
                    require(oscillation * m == int(oscillation * m), "integral scaled oscillation")
                    if cone:
                        require(oscillation <= F(2 * W, 3), "actual two-arc cone")
                        cone_words += 1
                    Delta = 2 * (t - 1) * (K - 1)
                    for start in range(m):
                        template_total = actual_total = high_total = 0
                        for length in range(1, m):
                            index = (start + length - 1) % m
                            end = (start + length) % m
                            template_total += template[index]
                            actual_total += word[index]
                            high_total += word[index] - template[index]
                            difference = scaled[end] - scaled[start]
                            deviation = m * template_total - sum(template) * length
                            require(difference == W * length - m * high_total,
                                    "pre-drop profile increment including wrap")
                            require(abs(deviation) <= m * Delta, "every proper template factor")
                            require(m * actual_total + difference == sum(word) * length + deviation,
                                    "exact weighted affine/log-profile decomposition")
                            factors += 1
                    words += 1
                    large_multiplicity_controls += min(c, d) >= 6
                    orders_seen.add(order)
                    adjacent += high_adjacent
                    separated += not high_adjacent
                    cycle = common.reduced_cycle(word)
                    if cycle is None:
                        continue
                    q, states = cycle
                    L, H = min(states), max(states)
                    E = sum(word)
                    require(2 ** E * prod(states) == prod(3 * state + q for state in states),
                            "actual addend-aware product")
                    require((H * 3 ** m) ** m <= L ** m * 2 ** (m * (E + Delta) + int(m * oscillation)),
                            "weighted height envelope retains true drift")
                    ordered = sorted(boundaries)
                    for index, end in enumerate(ordered):
                        previous = ordered[index - 1]
                        length = (end - previous) % m - 1
                        start = (previous + 1) % m
                        require(all(word[(start + offset) % m] == word[(start + offset + h) % m]
                                    for offset in range(length)), "actual agreeing positions")
                        initial_difference = states[(start + h) % m] - states[start]
                        final_difference = states[(end + h) % m] - states[end]
                        valuation_total = sum(word[(start + offset) % m] for offset in range(length))
                        require(initial_difference != 0 and initial_difference % 2 ** (valuation_total + 1) == 0,
                                "integer odd-state start separation")
                        require(final_difference == 2 * 3 ** length * (initial_difference // 2 ** (valuation_total + 1)),
                                "exact agreeing-run endpoint")
                        require(H > 2 * 3 ** length, "actual end witness")
                    runs += common.addend_runs(word, states, q)
                    cycles += 1
                    arrows += m
                    cone_cycles += cone
                    key = "adjacent" if high_adjacent else "separated"
                    if cone and key not in examples:
                        examples[key] = dict(track_order=list(order), lengths=list(lengths), h=h,
                                             word=word, q=q, states=states, minimum=L,
                                             normalized_minimum=str(F(L, q)))
                    checksum.update(f"{lengths}:{order}:{h}:{labels}:{q}:{states}\n".encode())
    require(len(orders_seen) == 6 and adjacent and separated and cone_cycles,
            "all orders and genuine cone cycles covered")
    require(set(examples) == {"adjacent", "separated"}, "two genuine cone examples")
    return {
        "label_sets": [list(labels) for labels in label_sets],
        "each_label_multiplicity": [1, 3],
        "additional_multiplicity_tuples": [list(lengths) for lengths in extra_lengths],
        "both_high_multiplicities_at_least_six": large_multiplicity_controls,
        "cyclic_orders_after_fixing_label_one": [list(order) for order in sorted(orders_seen)],
        "track_steps": "all coprime 0<h<m/2",
        "geometry_words": words,
        "adjacent_high_words": adjacent,
        "separated_high_words": separated,
        "cone_words": cone_words,
        "proper_factor_checks": factors,
        "actual_reduced_cycles": cycles,
        "actual_cone_cycles": cone_cycles,
        "exact_odd_arrows": arrows,
        "addend_ones_runs": runs,
        "genuine_examples": examples,
        "control_sha256": checksum.hexdigest(),
        "scope": "Actual positive odd 3x+q arrows retain q; these finite controls do not prove absence or the q=1-only minimum estimate.",
    }


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: checker [--write-receipt]")
    common, replay = load_common()
    result = {
        "schema": "weighted-high-arc-concentration-v1",
        "constants": exact_constants(replay),
        "single_arc_profiles": single_arc_checks(),
        "weighted_cone_profiles": weighted_cone_checks(),
        "family_controls": actual_family_checks(common),
        "pinned_arithmetic_replay": replay,
    }
    encoded = json.dumps(result, sort_keys=True, indent=2) + "\n"
    destination = HERE / "check_concentration.json"
    if sys.argv[1:]:
        destination.write_text(encoded)
    else:
        require(destination.read_text() == encoded, "receipt differs; inspect before regenerating")
    print(json.dumps({
        "status": "passed",
        "profile_endpoints": result["single_arc_profiles"]["complete_collision_and_cone_endpoints"],
        "weighted_profiles": result["weighted_cone_profiles"]["weighted_profiles"],
        "geometry_words": result["family_controls"]["geometry_words"],
        "actual_cycles": result["family_controls"]["actual_reduced_cycles"],
        "actual_cone_cycles": result["family_controls"]["actual_cone_cycles"],
        "local_seeds": replay["local_descent"]["seeds"],
        "standard_cycles": replay["standard_controls"]["cycles"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
