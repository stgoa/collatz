"""Exact finite checks for the written 64-scale annular packet identity.

Standard library only. This does not construct universal currents or search
for convergence. Run without -O. The proof is in annular_recursion.md.
"""

from argparse import ArgumentParser
from collections import defaultdict
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "experiments" / "packet_currents" / "right_aligned_packets.py"
SPEC = importlib.util.spec_from_file_location("right_aligned_packets", SOURCE)
PACKETS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACKETS)

RESIDUES = (1, 5, 7, 11, 13, 17)
EXPECTED_ROWS = (
    (1, 0, 1, 0, -2, 0),
    (2, 1, -1, 1, -1, -2),
    (3, -1, -3, 2, 0, -1),
    (1, -3, -2, 3, 1, 0),
    (-1, -2, -1, 1, 2, 1),
    (0, -1, 0, -1, 0, 2),
)


def derived_coefficient(band, endpoint):
    """Use source lifts directly, rather than the saved row table."""
    last_outer = 6 - band
    answer = 0
    for valuation in range(1, last_outer + 1):
        numerator = (1 << valuation) * endpoint - 1
        if numerator % 3:
            continue
        source = numerator // 3
        answer += 3 * int(source % 3 == 2) - 1
        if valuation < last_outer:
            answer += 3 * int(source % 3 == 1) - 1
    return answer


def annular_measure(cutoff):
    assert cutoff > 0 and cutoff % 8 == 0
    q = 9 * cutoff // 4
    answer = {}
    for band, row in enumerate(EXPECTED_ROWS):
        start, end = (1 << band) * q, (1 << (band + 1)) * q
        coefficients = dict(zip(RESIDUES, row))
        for endpoint in range(start + 1, end, 2):
            coefficient = coefficients.get(endpoint % 18, 0)
            if coefficient:
                answer[endpoint] = coefficient
    return answer


def difference(first, second):
    answer = defaultdict(int, first)
    for endpoint, coefficient in second.items():
        answer[endpoint] -= coefficient
    return {endpoint: coefficient for endpoint, coefficient in answer.items()
            if coefficient}


def explicit_source_annulus(cutoff):
    answer = {}
    lower, middle, inner_upper, outer_upper = (
        3 * cutoff // 4, 3 * cutoff // 2, 48 * cutoff, 96 * cutoff
    )
    for source in range(lower + 1, outer_upper, 2):
        if source <= middle:
            coefficient = 3 * int(source % 3 == 1) - 1
        elif source <= inner_upper:
            coefficient = 1 - 3 * int(source % 3 == 0)
        else:
            coefficient = 3 * int(source % 3 == 2) - 1
        if coefficient:
            answer[source] = coefficient
    return answer


def check_cutoff(cutoff):
    small, core_small, _ = PACKETS.right_packets(cutoff)
    large, core_large, _ = PACKETS.right_packets(64 * cutoff)
    annulus = annular_measure(cutoff)
    q = 9 * cutoff // 4
    assert difference(large, small) == annulus
    assert core_large == core_small
    assert all(1 < endpoint < q for endpoint in small)
    assert all(q < endpoint < 64 * q for endpoint in annulus)
    assert not small.keys() & annulus.keys()
    assert sum(annulus.values()) == 0
    assert sum(abs(coefficient) for coefficient in annulus.values()) == 99 * cutoff // 2
    assert sum(max(coefficient, 0) for coefficient in annulus.values()) == 99 * cutoff // 4
    assert len(annulus) == 267 * cutoff // 8
    assert (sum(abs(coefficient) for coefficient in large.values())
            == sum(abs(coefficient) for coefficient in small.values()) + 99 * cutoff // 2)
    assert len(large) == len(small) + 267 * cutoff // 8
    assert sum(endpoint * coefficient
               for endpoint, coefficient in annulus.items()) == 63 * q
    for band in range(6):
        start, end = (1 << band) * q, (1 << (band + 1)) * q
        assert sum(coefficient for endpoint, coefficient in annulus.items()
                   if start < endpoint < end) == 0
    source_annulus = difference(PACKETS.initial(64 * cutoff),
                               PACKETS.initial(cutoff))
    assert source_annulus == explicit_source_annulus(cutoff)
    assert PACKETS.push(source_annulus) == annulus
    return {"N": cutoff, "small_atoms": len(small),
            "annular_atoms": len(annulus), "annular_norm": 99 * cutoff // 2,
            "first_moment": 63 * q}


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    for band, expected in enumerate(EXPECTED_ROWS):
        assert tuple(derived_coefficient(band, residue)
                     for residue in RESIDUES) == expected
        assert sum(expected) == 0
        for residue in range(1, 18, 2):
            assert derived_coefficient(band, residue) == (
                dict(zip(RESIDUES, expected)).get(residue, 0)
            )
    cases = [check_cutoff(cutoff) for cutoff in range(8, 513, 8)]
    cases.extend(check_cutoff(cutoff) for cutoff in (1000, 4096))
    receipt = {
        "status": "PASS", "cutoff_multiples_of_8": [8, 512],
        "additional_cutoffs": [1000, 4096], "cases": len(cases),
        "largest_expanded_cutoff": 262144,
        "selected_results": [cases[0], *cases[-2:]],
        "residues": RESIDUES, "annular_rows": EXPECTED_ROWS,
        "trajectory_search_used": False,
        "universal_current_construction_proved": False,
    }
    serialized = json.dumps(receipt, indent=2) + "\n"
    if args.write_receipt:
        Path(__file__).with_name("annular_audit.json").write_text(serialized)
    print(serialized, end="")


if __name__ == "__main__":
    main()
