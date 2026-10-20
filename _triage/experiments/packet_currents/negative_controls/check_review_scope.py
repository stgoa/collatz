"""Bounded exact counterexamples to uniqueness of cheapest one-sided currents.

The reviewed minimality lemma is not refuted. These examples refute its
stronger prose interpretation that no alternative certificates exist.
"""

from argparse import ArgumentParser
from collections import defaultdict
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "review_arithmetic",
    ROOT / "experiments/annular_construction/arithmetic/check_arithmetic_reductions.py")
ARITH = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ARITH)
P = ARITH.PACKETS.push


def divergence(current):
    return ARITH.subtract(current, P(current))


def check_small_example():
    source = {21: 1, 3: -1}
    exact = {21: 1, 3: -1, 5: -1}
    alternative = {21: 1, 3: -1}
    residual = {5: -1}
    assert ARITH.PACKETS.step(21) == ARITH.PACKETS.step(5) == 1
    assert ARITH.PACKETS.step(3) == 5
    assert divergence(exact) == source
    assert ARITH.subtract(source, divergence(alternative)) == residual
    assert ARITH.positive_mass(exact) == ARITH.positive_mass(alternative) == 1
    assert sum(source.values()) == 0
    return {
        "source_rows": [[3, -1], [21, 1]],
        "exact_current_rows": [[3, -1], [5, -1], [21, 1]],
        "alternative_current_rows": [[3, -1], [21, 1]],
        "alternative_residual_rows": [[5, -1]],
        "both_positive_costs": 1,
        "minimality_argument": "The indicator of hitting21 forces every admissible J(21)>=1.",
    }


def check_annulus(cutoff=768, depth_cap=256):
    source = ARITH.ANNULAR.annular_measure(cutoff)
    alive = set(source)
    for absorption_depth in range(1, depth_cap + 1):
        alive = {ARITH.PACKETS.step(state) for state in alive}
        alive.discard(1)
        if not alive:
            break
    assert not alive, "raw support absorption exceeded the explicit cap"
    pushed = source
    exact = defaultdict(int)
    for depth in range(depth_cap):
        for state, coefficient in pushed.items():
            exact[state] += coefficient
        pushed = P(pushed)
        if not pushed:
            break
    assert not pushed, "capped annular transport did not finish"
    exact = ARITH.clean(exact)
    assert divergence(exact) == source
    assert exact[5] == -55
    alternative = dict(exact)
    alternative[5] += 55
    alternative = ARITH.clean(alternative)
    residual = ARITH.subtract(source, divergence(alternative))
    assert residual == {5: -55}
    assert 5 not in alternative
    assert ARITH.positive_mass(exact) == ARITH.positive_mass(alternative) == 53758
    assert len(exact) == 40106 and len(alternative) == 40105
    return {
        "N": cutoff, "transport_cap": depth_cap, "extinction_depth": depth + 1,
        "exact_current_at_5": -55,
        "exact_current_rows": len(exact), "alternative_current_rows": len(alternative),
        "alternative_residual_rows": [[5, -55]], "both_positive_costs": 53758,
        "full_divergence_verified": True,
        "full_source_support_absorption_verified": True,
        "raw_support_absorption_depth": absorption_depth,
        "scope": "Raw source absorption, signed extinction and the complete current identity are checked.",
    }


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    receipt = {
        "status": "PASS", "reviewed_remote_commit": "ba6b337",
        "small_balanced_example": check_small_example(),
        "actual_annular_example": check_annulus(),
        "minimality_lemma_refuted": False,
        "unique_cheapest_one_sided_certificate_claim_refuted": True,
        "universal_collatz_statement_proved": False,
    }
    path = Path(__file__).with_name("review_scope_audit.json")
    if args.write_receipt:
        path.write_text(json.dumps(receipt, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == receipt
    print(json.dumps({"status": "PASS", "annular_cutoff": 768,
                      "same_positive_cost": 53758,
                      "one_current_row_removed": 5}, indent=2))


if __name__ == "__main__":
    main()
