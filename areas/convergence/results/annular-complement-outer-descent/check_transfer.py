"""Exact finite audits of annular-to-complement transfer and shrinking branches."""

import argparse
import csv
import hashlib
import json
from pathlib import Path

import transfer as T


HERE = Path(__file__).resolve().parent


def digest(table):
    return hashlib.sha256("".join(f"{x},{c}\n" for x, c in sorted(table.items())).encode()).hexdigest()


def run():
    cutoffs = [*range(8, 513, 8), 768, 6144]
    positive_atoms, higher_positives, roots_checked = 0, 0, 0
    for M in cutoffs:
        N = 64 * M
        annulus = T.PACKING.OLD.ARITHMETIC.ANNULAR.annular_measure(M)
        for y, coefficient in annulus.items():
            if coefficient > 0:
                path = T.positive_ancestor(N, y)
                positive_atoms += 1
                higher_positives += len(path) > 1
        current, residual, summary = T.PACKING.build_extended_partial_current(M)
        source = T.combine((1, annulus), (-1, residual))
        roots = []
        for y, c in source.items():
            if c < 0 and y % 3 == 2:
                x = (2 * y - 1) // 3
                if T.residual_coefficient(N, x):
                    assert T.residual_coefficient(N, x) == 1
                    roots.append(x)
        assert sorted(roots) == T.old_packing_roots(M)
        roots_checked += len(roots)
    conversions, stored_current = [], None
    for M in (8, 96, 168, 384, 768):
        N = 64 * M
        current, residual, _ = T.PACKING.build_extended_partial_current(M)
        annulus = T.PACKING.OLD.ARITHMETIC.ANNULAR.annular_measure(M)
        source = T.combine((1, annulus), (-1, residual))
        # This is finite demonstration input discovery; the theorem takes H supplied.
        H = T.LOCAL.FORCING.absorption_current(T.LOCAL.count(N), cap=1000)
        result = T.transfer_block(M, source, current, H)
        assert sorted(result["target"]) == T.old_packing_roots(M)
        conversions.append(dict(M=M, N=N, lower_input_rows=len(H),
                                lower_input_sha256=digest(H),
                                exact_outer_target=sorted(map(list, result["target"].items())),
                                outer_current_rows=len(result["current"]),
                                outer_current_sha256=digest(result["current"]),
                                signed_negative_current_sha256=digest(result["signed_negative_current"])))
        if M == 96:
            stored_current = result["current"]
            geo = T.LOCAL.geometry(N)
            lower_edges = {x: T.step(x) for x in H}
            H_inner = T.COMPLEMENT.extract_exact(geo["inner"], lower_edges)
            old = T.COMPLEMENT.improve_packet(N, H_inner)
            new_current = T.combine((1, old["packet_current"]), (-1, result["current"]))
            remaining = T.combine((1, old["residual_profile"]), (-1, result["target"]))
            assert all(c > 0 for c in remaining.values())
            assert T.combine((1, T.divergence(new_current)), (-1, remaining)) == geo["packet"]
            conversions[-1]["full_packet_upgrade_verified"] = True
            conversions[-1]["remaining_packet_negative_mass"] = sum(remaining.values())
    branches = []
    for h in range(2, 33):
        for residue in (47, 155):
            params = T.RELEASE.family_parameters(h, residue)
            if params is None:
                continue
            for period in (0, 1):
                X = params["first_X"] + period * params["X_period"]
                for name, branch in (("designated", T.delayed_descent(params, X)),
                                     ("companion", T.delayed_companion(params, X))):
                    if branch is None:
                        continue
                    branches.append(dict(name=name, h=h, r=params["r"], residue=residue,
                                         X=X, N=branch["N"], root=branch["root"],
                                         residual_weight=branch["residual_weight"],
                                         first_descent_length=branch["first_descent_length"],
                                         peak=max(branch["path"]),
                                         current_sha256=digest(branch["current"])))
    p = T.RELEASE.family_parameters(3, 155)
    doubled = T.delayed_companion(p, p["first_X"])
    assert doubled["residual_weight"] == 2
    duplicate_check = dict(h=3, residue=155, X=p["first_X"], N=doubled["N"],
                           root=doubled["root"], endpoint=doubled["endpoint"],
                           current_rows=sorted(map(list, doubled["current"].items())),
                           positive_source_weight=2, endpoint_weight=-2,
                           first_descent_length=doubled["first_descent_length"])
    return dict(status="PASS", scope="Conditional partial residual recursion; universal coverage open",
                arithmetic_cutoffs=cutoffs, positive_atoms_checked=positive_atoms,
                positive_atoms_above_known_cutoff=higher_positives,
                exact_catalogue_roots_checked=roots_checked,
                finite_absorption_discovery_cap=1000, conversions=conversions,
                delayed_branches=branches, coefficient_two_branch=duplicate_check), stored_current


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    receipt, current = run()
    receipt_path = HERE / "transfer_audit.json"
    table_path = HERE / "outer_9183_current.csv"
    if args.write_receipt:
        receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
        with table_path.open("w", newline="") as output:
            writer = csv.writer(output, lineterminator="\n")
            writer.writerow(("state", "current"))
            writer.writerows(sorted(current.items()))
    else:
        assert json.loads(receipt_path.read_text()) == receipt
        with table_path.open(newline="") as source:
            saved = {int(row["state"]): int(row["current"]) for row in csv.DictReader(source)}
        assert saved == current
    print(f"PASS: {len(receipt['arithmetic_cutoffs'])} ancestor/capacity cases; "
          f"{len(receipt['conversions'])} actual conversions; "
          f"{len(receipt['delayed_branches'])} exact shrinking branches")


if __name__ == "__main__":
    main()
