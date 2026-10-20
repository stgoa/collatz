"""Check retained-graph extension; default mode never updates stored evidence."""

import argparse
import csv
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from complement_constructor import (LOCAL, cutoff_components, divergence,
                                   improve_packet, residual_mass_formula,
                                   residual_profile, step)


HERE = Path(__file__).resolve().parent


def digest(table):
    data = "".join(f"{x},{c}\n" for x, c in sorted(table.items()))
    return hashlib.sha256(data.encode()).hexdigest()


def unabsorbed_outer(N, edges):
    vertices = set(edges) | set(edges.values()) | set(range(N + 1, 3 * N // 2, 2)) | {1}
    parents = dict(zip(vertices, vertices))
    def find(x):
        while x != parents[x]:
            parents[x] = parents[parents[x]]
            x = parents[x]
        return x
    for x, y in edges.items():
        parents[find(x)] = find(y)
    absorbed = find(1)
    return [x for x in range(N + 1, 3 * N // 2, 2) if find(x) != absorbed]


def run():
    graph_cases = [*range(8, 1025, 8), 1536, 2048, 6144]
    total_arrows, total_components = 0, 0
    for N in graph_cases:
        geo = LOCAL.geometry(N)
        edges, components, actual_bad = cutoff_components(N)
        assert set(geo["K"]) == set(edges)
        bad, transport, profile = residual_profile(N)
        assert set(bad) == actual_bad
        expected = []
        for x, c in profile.items():
            group = {x, step(x)}
            assert c in (1, 2)
            if c == 2:
                group.add((4 * x - 1) // 3)
            expected.append(tuple(sorted(group)))
        assert components == sorted(expected)
        assert sum(profile.values()) == residual_mass_formula(N)
        assert sum(profile.values()) == len(actual_bad)
        assert set(transport) <= set(edges)
        total_arrows += len(edges)
        total_components += len(components)

    phases = [residual_mass_formula(N) for N in range(8, 289, 8)]
    assert phases == [0, 1, 2, 2, 4, 4, 4, 4, 7, 6, 8, 7, 9, 10, 11, 9, 11, 13,
                      13, 13, 14, 15, 17, 16, 16, 17, 20, 18, 20, 20, 22, 22,
                      23, 22, 24, 25]
    for N in range(8, 289, 8):
        for periods in (1, 2, 10, 10 ** 12):
            assert residual_mass_formula(N + 288 * periods) == phases[N // 8 - 1] + 25 * periods
    errors = [Fraction(phases[N // 8 - 1]) - Fraction(25 * N, 288)
              for N in range(8, 289, 8)]
    assert min(errors) == Fraction(-19, 9) and max(errors) == Fraction(5, 4)
    for k in range(10):
        N = 96 * 64 ** k
        assert residual_mass_formula(N) == Fraction(25 * N, 288) - Fraction(4, 3)

    cases, saved_current = [], None
    for N in (8, 16, 24, 96, 168, 384, 768, 1536):
        geo = LOCAL.geometry(N)
        # Capped discovery is used only to supply these finite demonstration inputs.
        H = LOCAL.FORCING.absorption_current(geo["inner"], cap=1000)
        result = improve_packet(N, H)
        G = result["supplied_edges"]
        actual_missing = unabsorbed_outer(N, G)
        assert set(actual_missing) <= set(result["unresolved_outer"])
        assert divergence(result["lower_current"]) == LOCAL.count(N)
        assert all(c > 0 for c in result["lower_current"].values())
        assert len(result["guaranteed_outer"]) + len(result["unresolved_outer"]) == N // 4
        cases.append(dict(
            N=N, input_inner_current_rows=len(H), input_inner_current_sha256=digest(H),
            explicit_K_rows=len(geo["K"]), retained_graph_rows=len(G),
            automatic_negative_residual_mass=N // 2 - 2,
            guaranteed_outer_seeds=len(result["guaranteed_outer"]),
            improved_negative_residual_mass=sum(result["residual_profile"].values()),
            improved_current_rows=len(result["packet_current"]),
            improved_current_sha256=digest(result["packet_current"]),
            improved_residual=[[x, c] for x, c in sorted(result["packet_residual"].items())],
            lower_current_sha256=digest(result["lower_current"]),
            actual_unabsorbed_outer_in_retained_graph=actual_missing,
            no_new_arrows=True))
        if N == 24:
            saved_current = result["packet_current"]
    receipt = dict(
        claim="Conditional retained-graph packet improvement; not universal input supply",
        cutoff_graph_checks=dict(cases=len(graph_cases), first_N=8, regular_last_N=1024,
                                 extra_cutoffs=[1536, 2048, 6144],
                                 total_arrows=total_arrows,
                                 complete_components_disjoint_from_lower=total_components),
        mass_formula=dict(period=288, mass_increment=25, N_8_through_288=phases,
                          lower_error="-19/9", upper_error="5/4", huge_periods_tested=10 ** 12),
        absorption_discovery_cap=1000, finite_construction_cases=cases)
    return receipt, saved_current


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    receipt, current = run()
    receipt_path = HERE / "complement_audit.json"
    table_path = HERE / "improved_packet_24_current.csv"
    if args.write_receipt:
        receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
        with table_path.open("w", newline="") as out:
            writer = csv.writer(out, lineterminator="\n")
            writer.writerow(("state", "current"))
            writer.writerows(sorted(current.items()))
    else:
        assert json.loads(receipt_path.read_text()) == receipt
        with table_path.open(newline="") as inp:
            saved = {int(row["state"]): int(row["current"]) for row in csv.DictReader(inp)}
        assert saved == current
    print("PASS: 131 complete cutoff graphs, 36 exact mass phases, 8 retained-graph constructions")


if __name__ == "__main__":
    main()
