"""Reproduce local extension identities and the scoped positive-cone barrier."""

from argparse import ArgumentParser
import csv
import json
from pathlib import Path

from local_extension import (CURRENT, FORCING, automatic_packet, combine,
                             extend_packet, geometry, inspect_exposed)


HERE = Path(__file__).resolve().parent


def pointwise_scale(N, x):
    return (3 * (x <= N) - 3 * (x <= N // 4)
            - (x <= 3 * N // 2) - (x <= 3 * N // 4))


def run():
    point_checks = 0
    for N in range(8, 513, 8):
        geo = geometry(N)
        for x in range(3, 2 * N + 2, 2):
            coefficient = pointwise_scale(N, x)
            assert coefficient == geo["scale"].get(x, 0)
            assert (coefficient > 0) == (x <= N < 4 * x)
            if N < x:
                assert coefficient <= 0
            point_checks += 1
        # This raw top atom is removed by the explicit K divergence; it is
        # not an intrinsic state-height requirement for constructing inputs.
        top = 9 * N // 4 - 1
        assert geo["packet"][top] == 2
        assert geo["scale"].get(top, 0) == 0

    automatic = []
    for N in (8, 24, 96):
        geo = geometry(N)
        H = FORCING.absorption_current(geo["inner"])
        J, residual, _ = automatic_packet(geo, H)
        extension = extend_packet(geo, H, J, residual)
        assert not extension["current"]
        assert extension["complement_residual"] == geo["complement"]
        assert extension["outer_residual"] == geo["outer"]
        automatic.append(dict(N=N, inner_source_mass=sum(geo["inner"].values()),
                              packet_current_rows=len(J),
                              negative_residual_mass=-sum(residual.values()),
                              feedback_current_rows=0,
                              feedback_outer_mass=sum(geo["outer"].values())))

    examples, exact_outer = [], None
    for N in (24, 96, 384):
        geo = geometry(N)
        H = FORCING.absorption_current(geo["inner"])
        J, residual, metadata = FORCING.discover_packet_input(N)
        extension = extend_packet(geo, H, J, residual)
        inspection = inspect_exposed(geo, extension)
        output = dict(N=N, input_discovery_depth=metadata["exposure_depth"],
                      input_current_sha256=FORCING.hash_table(J),
                      input_residual={str(x): c for x, c in sorted(residual.items())},
                      inner_current_rows=len(H),
                      inner_current_sha256=FORCING.hash_table(H),
                      extension_current_rows=len(extension["current"]),
                      extension_current_sha256=FORCING.hash_table(extension["current"]),
                      complement_mass=sum(geo["complement"].values()),
                      complement_positive_budget=extension["complement_positive_budget"],
                      outer_positive_budget=extension["outer_positive_budget"],
                      missed_low=inspection["missed_low"],
                      missed_outer=inspection["missed_outer"],
                      actual_weighted_unabsorbed=inspection["actual_weighted_unabsorbed"],
                      unabsorbed_exit_mass=inspection["unabsorbed_exit_mass"],
                      no_outer_trajectory_search_during_conversion=True)
        if N == 96:
            exact_outer, zero = inspection["outer_certificate"]
            assert not zero
            output.update(extracted_outer_current_rows=len(exact_outer),
                          extracted_outer_current_sha256=FORCING.hash_table(exact_outer))
        examples.append(output)
    assert examples[0]["missed_outer"] == [27, 31]
    assert examples[0]["actual_weighted_unabsorbed"] == 2
    assert examples[1]["actual_weighted_unabsorbed"] == 0
    assert examples[2]["missed_outer"] == [447, 495, 511, 559]
    assert examples[2]["actual_weighted_unabsorbed"] == 4
    result = dict(status="PASS", full_scale_cutoffs=[8, 512, 8],
                  pointwise_checks=point_checks,
                  automatic_input_feedback=automatic, actual_examples=examples,
                  universal_inner_absorption_assumed=False,
                  universal_packet_constructor_proved=False)
    return result, exact_outer


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    result, exact_outer = run()
    receipt = HERE / "local_extension_audit.json"
    table = HERE / "outer_96_current.csv"
    if args.write_receipt:
        receipt.write_text(json.dumps(result, indent=2) + "\n")
        with table.open("w", newline="") as out:
            writer = csv.writer(out, lineterminator="\n")
            writer.writerow(("state", "weight"))
            writer.writerows(sorted(exact_outer.items()))
    else:
        assert json.loads(receipt.read_text()) == result
        with table.open(newline="") as inp:
            saved = {int(row["state"]): int(row["weight"]) for row in csv.DictReader(inp)}
        assert saved == exact_outer
    print(json.dumps(dict(status="PASS", pointwise_checks=result["pointwise_checks"],
                          exact_outer_current_rows=len(exact_outer),
                          missed_outer={str(x["N"]): x["missed_outer"]
                                        for x in result["actual_examples"]})))


if __name__ == "__main__":
    main()
