"""Verify an infinite complete-component family by exact affine decisions."""

import argparse
import hashlib
import json
from pathlib import Path

from inverse_exposure_probe import component
from symbolic_component_lift import prove_chain_lift

HERE = Path(__file__).resolve().parent


def digest(rows):
    data = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(data).hexdigest()


def check_numeric(N0, depth, q, expected_queries):
    report, graph = component(N0 * q, depth, state_cap=10000, query_cap=20000)
    assert report["status"] == "complete_component"
    chain = [(64 * N0 * q * 3**j) // 2**j - 1 for j in range(depth + 3)]
    assert graph["nodes"] == set(chain)
    assert graph["edges"] == dict(zip(chain, chain[1:]))
    assert graph["sources"] == dict(zip(chain[:3], (-2, 2, 2)))
    assert report["positive_component_obstruction"]
    assert report["reachability_queries"] == expected_queries
    return dict(q=q, N=N0 * q, depth=depth, vertices=len(chain),
                queries=report["reachability_queries"], signed_source_mass=2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    proof = prove_chain_lift(96 * 2**24, 32, query_cap=20000)
    receipt = proof["receipt"]
    assert receipt["K"] == 22
    assert receipt["maximal_denominator_power"] == 20
    assert receipt["queries"] == 9171 and receipt["comparisons"] == 42487
    modulus = 3 ** receipt["K"]
    period = receipt["dyadic_exponent_period"]
    assert modulus == 31381059609 and period == 20920706406
    assert pow(2, period, modulus) == 1
    samples = [check_numeric(receipt["N0"], receipt["depth"], q, receipt["queries"])
               for q in (1, 1 + modulus, 1 + 2 * modulus)]
    assert samples[1]["q"] % 2 == 0

    # The main family's first nontrivial dyadic multiplier has over twenty
    # billion bits. Verify its modular condition without allocating it.
    # A smaller independent proof has a numerical nontrivial dyadic sample.
    small = prove_chain_lift(384, 2, query_cap=100)
    small_receipt = small["receipt"]
    assert small_receipt["K"] == 2
    assert small_receipt["dyadic_exponent_period"] == 6
    small_sample = check_numeric(384, 2, 2**6, small_receipt["queries"])

    result = dict(status="PASS", theorem=receipt,
                  query_table_sha256=digest(proof["queries"]),
                  comparison_table_sha256=digest(proof["comparisons"]),
                  exact_numeric_samples=samples,
                  main_dyadic_congruence_verified_modulo=modulus,
                  main_dyadic_nontrivial_multiplier_materialized=False,
                  small_depth_symbolic_theorem=small_receipt,
                  nontrivial_small_depth_dyadic_sample=small_sample,
                  obstruction_at_every_exposure_depth_proved=False,
                  universal_current_construction_proved=False)
    path = HERE / "symbolic_lift_audit.json"
    if args.write_receipt:
        path.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == result
    print(json.dumps(dict(status="PASS", N0=receipt["N0"], depth=32, modulus=modulus,
                          dyadic_exponent_period=period, queries=receipt["queries"],
                          inequalities=receipt["comparisons"], numeric_samples=len(samples),
                          nontrivial_small_depth_dyadic_sample=small_sample,
                          obstruction_at_every_exposure_depth_proved=False), indent=2))


if __name__ == "__main__":
    main()
