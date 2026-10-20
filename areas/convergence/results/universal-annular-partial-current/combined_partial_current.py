"""Construct and verify the combined universal partial current for A_N.

The finite arithmetic construction combines the five short-chain families with
all admissible copies of the compiled five-source template. It returns the full
current and exact residual; remaining positive mass is retained. No search for
eventual absorption or a complete current is performed.
"""

from argparse import ArgumentParser
from collections import defaultdict
from functools import lru_cache
import csv
import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
COMPONENTS = HERE.parent / "components"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ARITHMETIC = load_module("combined_annular_arithmetic",
                         HERE / "check_arithmetic_reductions.py")
# The compiler uses its sibling annular_components module. Restrict the path
# change to loading that existing repository module, then restore sys.path.
sys.path.insert(0, str(COMPONENTS))
try:
    COMPILER = load_module("combined_annular_affine_compiler",
                          COMPONENTS / "affine_template_compiler.py")
finally:
    sys.path.pop(0)


@lru_cache(maxsize=1)
def five_source_template():
    """Read the stored finite tree and verify its base identity, without search."""
    receipt = json.loads((COMPONENTS / "affine_templates.json").read_text())
    template = next(item["template"] for item in receipt["templates"]
                    if item["name"] == "five_source_cross_band")
    source, _, residual = COMPILER.instantiate(template, 0)
    assert source == {4591: -1, 6121: -1, 6887: 1, 10331: 2, 13775: -1}
    assert not residual and template["source_mass"] == 0
    assert template["generic_positive_current_cost"] == 3
    return template


def build_combined_partial_current(cutoff):
    """Return (current, residual, summary) for every positive cutoff divisible by8.

    The first two return values are full integer dictionaries keyed by actual
    odd states. They satisfy A_N=(I-P)current+residual. All deleted source
    coefficients are used once, and the residual's positive coefficients are
    explicitly retained. Construction terminates by bounded arithmetic loops.
    """
    if not isinstance(cutoff, int) or cutoff <= 0 or cutoff % 8:
        raise ValueError("cutoff must be a positive integer divisible by 8")
    measure = ARITHMETIC.ANNULAR.annular_measure(cutoff)
    short_current, short_residual, family_counts, removed_short_positive = (
        ARITHMETIC.catalogue_current(cutoff, measure)
    )
    removed = ARITHMETIC.subtract(measure, short_residual)
    short_source_count = len(removed)
    current = defaultdict(int, short_current)
    template = five_source_template()
    copy_counts = {}
    for residue in (0, 3):
        indices = COMPILER.family_indices(cutoff, residue)
        copy_counts[str(residue)] = len(indices)
        for index in indices:
            source, copy_current, copy_residual = COMPILER.instantiate(
                template, 9 * index + residue
            )
            assert not copy_residual
            assert not removed.keys() & source.keys(), "Source capacity reused"
            assert all(measure.get(state, 0) == coefficient
                       for state, coefficient in source.items())
            removed.update(source)
            for state, coefficient in copy_current.items():
                current[state] += coefficient
    copies = sum(copy_counts.values())
    current = ARITHMETIC.clean(current)
    residual = ARITHMETIC.subtract(measure, removed)

    # Independently verify the complete returned dictionaries by exact one-step
    # divergence and by deletion from the original signed source measure.
    divergence = ARITHMETIC.subtract(current, ARITHMETIC.PACKETS.push(current))
    assert divergence == removed
    assert ARITHMETIC.subtract(measure, divergence) == residual
    assert residual == {state: coefficient for state, coefficient in measure.items()
                        if state not in removed}
    assert len(removed) == short_source_count + 5 * copies
    assert ARITHMETIC.positive_mass(removed) == removed_short_positive + 3 * copies
    expected_positive = 99 * cutoff // 4 - removed_short_positive - 3 * copies
    assert ARITHMETIC.positive_mass(residual) == expected_positive
    assert ARITHMETIC.norm(residual) == 99 * cutoff // 2 - 2 * (
        removed_short_positive + 3 * copies
    )
    positive_cost = ARITHMETIC.positive_mass(current)
    assert positive_cost <= 3 * copies

    summary = {
        "N": cutoff,
        "initial_source_atoms": len(measure),
        "short_family_counts": family_counts,
        "short_positive_mass_removed_D": removed_short_positive,
        "five_source_copy_counts": copy_counts,
        "five_source_copies_C": copies,
        "removed_source_atoms": len(removed),
        "removed_positive_mass": removed_short_positive + 3 * copies,
        "current_rows": len(current),
        "positive_current_cost": positive_cost,
        "positive_current_cost_upper_bound": 3 * copies,
        "residual_atoms": len(residual),
        "residual_positive_mass": expected_positive,
        "residual_norm": ARITHMETIC.norm(residual),
        "residual_is_nonpositive": all(coefficient <= 0
                                       for coefficient in residual.values()),
        "exact_divergence_verified": True,
        "source_capacity_verified": True,
    }
    return current, residual, summary


def write_table(path, table):
    with path.open("w", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(("state", "weight"))
        writer.writerows(sorted(table.items()))


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--cutoff", type=int,
                        help="Construct one cutoff instead of running the audit cases")
    parser.add_argument("--write-tables", action="store_true",
                        help="With --cutoff, save both full CSV tables beside this script")
    parser.add_argument("--write-receipt", action="store_true",
                        help="Refresh combined_audit.json for the default audit cases")
    args = parser.parse_args()
    if args.cutoff is not None:
        if args.write_receipt:
            parser.error("--write-receipt applies only to the default audit cases")
        current, residual, summary = build_combined_partial_current(args.cutoff)
        if args.write_tables:
            write_table(HERE / f"combined_{args.cutoff}_current.csv", current)
            write_table(HERE / f"combined_{args.cutoff}_residual.csv", residual)
        print(json.dumps(summary, indent=2))
        return
    if args.write_tables:
        parser.error("--write-tables requires --cutoff")
    cutoffs = (8, 72, 96, 160, 168, 384, 768, 6144)
    cases = [build_combined_partial_current(cutoff)[2] for cutoff in cutoffs]
    receipt = {
        "status": "PASS", "cutoffs": cutoffs, "cases": cases,
        "residual_positive_mass_formula": "99*N/4-D(N)-3*C(N)",
        "positive_current_cost_bound": "3*C(N)",
        "source_supports_deleted_exactly_once": True,
        "universal_partial_constructor_proved": True,
        "universal_complete_constructor_proved": False,
        "trajectory_search_used": False,
    }
    serialized = json.dumps(receipt, indent=2) + "\n"
    path = HERE / "combined_audit.json"
    if args.write_receipt:
        path.write_text(serialized)
    else:
        assert json.loads(path.read_text()) == json.loads(serialized)
    print(serialized, end="")


if __name__ == "__main__":
    main()
