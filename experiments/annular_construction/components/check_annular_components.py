"""Reproduce bounded annular component experiments and stored finite currents."""

import argparse
import csv
import json
from pathlib import Path

from annular_components import ANNULAR, explore, step

HERE = Path(__file__).resolve().parent
CUTOFFS = (96, 112, 128, 144, 168, 384)


def write_or_check_table(path, data, write):
    rows = [(x, data[x]) for x in sorted(data)]
    if write:
        with path.open("w", newline="") as stream:
            writer = csv.writer(stream, lineterminator="\n")
            writer.writerow(["state", "weight"])
            writer.writerows(rows)
    else:
        with path.open(newline="") as stream:
            reader = csv.reader(stream)
            assert next(reader) == ["state", "weight"]
            assert [(int(x), int(c)) for x, c in reader] == rows


def check_exposure_equivalence():
    sources = ANNULAR.annular_measure(96)
    for depth in (1, 8, 28, 45):
        direct = {}
        for source in sources:
            x = source
            for _ in range(depth):
                if x == 1:
                    break
                direct[x] = step(x)
                x = direct[x]
        seen, frontier, incremental = set(sources), set(sources), {}
        for _ in range(depth):
            following = set()
            for x in frontier:
                if x == 1:
                    continue
                y = step(x)
                incremental[x] = y
                if y not in seen:
                    seen.add(y)
                    following.add(y)
            frontier = following
        assert direct == incremental


def work_at(N, horizon):
    residual, work = ANNULAR.annular_measure(N), 0
    for _ in range(horizon):
        work += sum(residual.values())
        residual = ANNULAR.PACKETS.push(residual)
    return work


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    check_exposure_equivalence()
    results = []
    for N in CUTOFFS:
        report, certificates = explore(N, max_depth=128, keep_certificates=True)
        assert report["status"] == "all_band_certificates"
        if N in (96, 168):
            label = "aggregate_one_sided" if N == 96 else "aggregate_exact"
            current, residual = certificates[label]
            write_or_check_table(HERE / f"annular_{N}_{label}.csv", current, args.write_receipt)
            write_or_check_table(HERE / f"annular_{N}_{label}_residual.csv", residual, args.write_receipt)
        results.append(report)
    assert work_at(96, 53) == 699
    assert work_at(384, 9) == 42
    result = dict(status="PASS", cutoff_cases=results,
                  exposure_equivalence_depths=[1, 8, 28, 45],
                  finite_positive_work_witnesses=[dict(N=96, horizon=53, work=699),
                                                  dict(N=384, horizon=9, work=42)],
                  universal_current_construction_proved=False)
    path = HERE / "annular_component_audit.json"
    if args.write_receipt:
        path.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == result
    print(json.dumps(dict(status="PASS", summaries=[dict(N=r["N"],
                     first_depths={label: info["depth"] for label, info in r["first"].items()})
                     for r in results], work_witnesses=result["finite_positive_work_witnesses"]), indent=2))


if __name__ == "__main__":
    main()
