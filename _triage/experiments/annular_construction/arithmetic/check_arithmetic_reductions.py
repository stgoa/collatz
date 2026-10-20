"""Finite checks for explicit arithmetic partial currents of annular measures.

No search for eventual absorption is performed. Run without -O.
"""

from argparse import ArgumentParser
from collections import defaultdict
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "experiments/current_construction/recursive/check_annular_recursion.py"
SPEC = importlib.util.spec_from_file_location("annular_source", SOURCE)
ANNULAR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ANNULAR)
PACKETS = ANNULAR.PACKETS

CATALOGUE = (
    ("E", 12, 16, (7,), (-3, 3), (-3,)),
    ("D", 16, 18, (23, 71), (-1, 0, 1), (-1, -1)),
    ("B", 24, 32, (7,), (-2, 1, 1), (-2, -1)),
    ("C", 32, 36, (23,), (-3, 1, 2), (-3, -2)),
    ("A", 48, 64, (7, 55), (-1, -1, 2), (-1, -2)),
)
EXPECTED_CHAIN_ROWS = (
    (0, 1, 2, 3, 1, -1, -3, -2, -1),
    (-1, 3, 1, 2, 0, 1, -1, -3, -2),
    (1, 2, -1, -2, -1, 2, 1, -1, -1),
    (0, 0, -3, -3, 0, 3, 3, 0, 0),
    (-1, 0, -2, -1, 0, 1, 2, 0, 1),
    (0, 0, -1, 0, 0, -1, 0, 0, 2),
)


def clean(measure):
    return {state: coefficient for state, coefficient in measure.items()
            if coefficient}


def subtract(left, right):
    answer = defaultdict(int, left)
    for state, coefficient in right.items():
        answer[state] -= coefficient
    return clean(answer)


def norm(measure):
    return sum(abs(coefficient) for coefficient in measure.values())


def positive_mass(measure):
    return sum(max(coefficient, 0) for coefficient in measure.values())


def f_root(state):
    while state % 8 == 5:
        state = (state - 1) // 4
    return state


def root_collapse(measure):
    residual = defaultdict(int)
    for state, coefficient in measure.items():
        root = f_root(state)
        if root != 1:
            residual[root] += coefficient
    residual = clean(residual)
    current = subtract(measure, residual)
    return current, residual


def annular_coefficient(cutoff, state):
    q = 9 * cutoff // 4
    for band, row in enumerate(ANNULAR.EXPECTED_ROWS):
        if (1 << band) * q < state < (1 << (band + 1)) * q:
            return dict(zip(ANNULAR.RESIDUES, row)).get(state % 18, 0)
    return 0


def absorbed_class_mass(cutoff):
    q = 9 * cutoff // 4
    state = 1
    while state <= q:
        state = 4 * state + 1
    result = 0
    while state < 64 * q:
        result += annular_coefficient(cutoff, state)
        state = 4 * state + 1
    return result


def chain_coefficient(band, state):
    answer = 0
    for next_band in range(band, 6, 2):
        row = dict(zip(ANNULAR.RESIDUES, ANNULAR.EXPECTED_ROWS[next_band]))
        answer += row.get(state % 18, 0)
        state = 4 * state + 1
    return answer


def residue_count(cutoff, lower, upper, residue):
    return ((upper * cutoff - 1 - residue) // 72
            - (lower * cutoff - residue) // 72)


def catalogue_current(cutoff, measure):
    submeasure, current = {}, defaultdict(int)
    families = {}
    for name, lower, upper, residues, weights, currents in CATALOGUE:
        count = 0
        for residue in residues:
            first = lower * cutoff + 1
            first += (residue - first) % 72
            for state in range(first, upper * cutoff, 72):
                points = [state, (3 * state + 1) // 2,
                          (9 * state + 5) // 4]
                assert state % 8 == 7
                assert PACKETS.step(points[0]) == points[1]
                assert PACKETS.step(points[1]) == points[2]
                for point, weight in zip(points, weights):
                    assert measure.get(point, 0) == weight
                    if weight:
                        assert point not in submeasure, (name, point)
                        submeasure[point] = weight
                for point, weight in zip(points, currents):
                    current[point] += weight
                count += 1
        assert count == sum(residue_count(cutoff, lower, upper, residue)
                            for residue in residues)
        families[name] = count
    current = clean(current)
    assert all(coefficient < 0 for coefficient in current.values())
    assert subtract(current, PACKETS.push(current)) == submeasure
    residual = subtract(measure, submeasure)
    assert all(residual.get(state, 0) == 0 for state in submeasure)
    expected_removed = sum(
        sum(max(weight, 0) for weight in weights)
        * sum(residue_count(cutoff, lower, upper, residue) for residue in residues)
        for _, lower, upper, residues, weights, _ in CATALOGUE
    )
    assert positive_mass(submeasure) == expected_removed
    assert positive_mass(residual) == 99 * cutoff // 4 - expected_removed
    if cutoff % 72 == 0:
        assert expected_removed == 3 * cutoff // 2
    return current, residual, families, expected_removed


def check_cutoff(cutoff):
    measure = ANNULAR.annular_measure(cutoff)
    current, residual = root_collapse(measure)
    assert not PACKETS.push(current)
    assert subtract(measure, residual) == subtract(current, PACKETS.push(current))
    pushed = PACKETS.push(measure)
    assert PACKETS.push(residual) == pushed
    correction = absorbed_class_mass(cutoff)
    assert abs(correction) <= 3
    assert norm(residual) == norm(pushed) == 171 * cutoff // 4 - abs(correction)
    q = 9 * cutoff // 4
    witnesses = list(range(32 * q + 35, 64 * q, 36))
    assert len(witnesses) == 2 * cutoff
    assert all(residual[state] == 2 for state in witnesses)
    cat_current, cat_residual, counts, removed = catalogue_current(cutoff, measure)
    assert subtract(measure, cat_residual) == subtract(cat_current, PACKETS.push(cat_current))
    return {
        "N": cutoff, "initial_norm": norm(measure), "root_residual_norm": norm(residual),
        "absorbed_class_signed_mass": correction, "catalogue_family_counts": counts,
        "catalogue_positive_mass_removed": removed,
        "catalogue_positive_mass_remaining": positive_mass(cat_residual),
        "catalogue_current_rows": len(cat_current),
    }


def check_outer_profile(cutoff, depth_cap):
    measure = ANNULAR.annular_measure(cutoff)
    q = 9 * cutoff // 4
    for depth in range(depth_cap + 1):
        power2, power3 = 1 << depth, 3 ** depth
        lower = power3 * (96 * q + 1) // (3 * power2) - 1
        upper = 64 * power3 * q // power2 - 1
        seen_positive = False
        for state in range(max(3, lower - 2) | 1, upper + 1, 2):
            if not (3 * power2 * (state + 1) > power3 * (96 * q + 1)
                    and power2 * (state + 1) <= 64 * power3 * q):
                continue
            expected = 0
            if (state + 1) % (3 ** (depth + 1)) == 0:
                expected = 3 * int((state + 1) % (3 ** (depth + 2)) == 0) - 1
            assert measure.get(state, 0) == expected, (cutoff, depth, state)
            seen_positive |= expected == 2
        assert seen_positive
        if depth < depth_cap:
            measure = PACKETS.push(measure)


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    for band, expected in enumerate(EXPECTED_CHAIN_ROWS):
        assert tuple(chain_coefficient(band, residue)
                     for residue in range(1, 18, 2)) == expected
    absolute_sums = []
    for band in range(6):
        period = 18 if band < 2 else 72
        absolute_sums.append(sum(abs(chain_coefficient(band, state))
                                 for state in range(1, period, 2)
                                 if band < 2 or state % 8 != 5))
    assert absolute_sums == [14, 14, 36, 36, 24, 12]
    cases = [check_cutoff(cutoff) for cutoff in range(8, 513, 8)]
    cases.extend(check_cutoff(cutoff) for cutoff in (768, 1536))
    assert absorbed_class_mass(80000) == 0
    for cutoff in (8, 24, 96, 128):
        check_outer_profile(cutoff, 4)
    corrections = [case["catalogue_positive_mass_removed"] - 3 * case["N"] // 2
                   for case in cases[:9]]
    for case in cases[:64]:
        assert (case["catalogue_positive_mass_removed"] - 3 * case["N"] // 2
                == corrections[(case["N"] // 8 - 1) % 9])
    receipt = {
        "status": "PASS", "cutoff_multiples_of_8": [8, 512],
        "additional_cutoffs": [768, 1536], "cases": len(cases),
        "outer_profile_cutoffs": [8, 24, 96, 128], "outer_profile_depths": [0, 4],
        "catalogue_boundary_correction_N_8_through_72": corrections,
        "root_norm_formula": "171*N/4 - abs(c_N)",
        "root_bulk_contraction": "19/22", "zero_absorbed_correction_example": 80000,
        "selected_results": [cases[0], cases[8], cases[11], *cases[-2:]],
        "universal_partial_current_construction_proved": True,
        "universal_complete_current_construction_proved": False,
        "eventual_absorption_search_used": False,
    }
    serialized = json.dumps(receipt, indent=2) + "\n"
    if args.write_receipt:
        Path(__file__).with_name("arithmetic_audit.json").write_text(serialized)
    print(serialized, end="")


if __name__ == "__main__":
    main()
