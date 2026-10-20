"""Two exact annular cancellation families, with disjoint source capacity.

The optional combined constructor extends the existing partial catalogue.
All loops are finite arithmetic loops; no absorption search is used.
"""

from argparse import ArgumentParser
from collections import defaultdict
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OLD_PATH = HERE.parents[1] / "annular_construction" / "arithmetic" / "combined_partial_current.py"
spec = importlib.util.spec_from_file_location("release_old_partial", OLD_PATH)
OLD = importlib.util.module_from_spec(spec)
spec.loader.exec_module(OLD)


def progression(N, low, high, residue, modulus):
    """All integers low*N < q < high*N in the given residue class."""
    first = low * N + 1
    first += (residue - first) % modulus
    return range(first, high * N, modulus)


def count(N, low, high, residue, modulus):
    return ((high * N - 1 - residue) // modulus
            - (low * N - residue) // modulus)


def release_families(N):
    if not isinstance(N, int) or N <= 0 or N % 8:
        raise ValueError("N must be a positive multiple of 8")
    source, current = {}, defaultdict(int)
    counts = {"pairs": 0, "triples": 0}

    def add(block, rows):
        assert not source.keys() & block.keys(), "Source coefficient reused"
        assert all(OLD.COMPILER.coefficient_at(N, x) == c for x, c in block.items())
        source.update(block)
        for x, c in rows.items():
            current[x] += c

    for q in progression(N, 36, 54, 31, 54):
        u = (4 * q - 1) // 3
        assert 4 * q - 1 == 3 * u and OLD.COMPILER.step(u) == q
        add({u: -2, q: 2}, {u: -2})
        counts["pairs"] += 1
    for residue in (31, 103):
        for q in progression(N, 64, 72, residue, 108):
            u, v = (4 * q - 1) // 3, (3 * q + 1) // 2
            assert 4 * q - 1 == 3 * u and 3 * q + 1 == 2 * v
            assert OLD.COMPILER.step(u) == q and OLD.COMPILER.step(q) == v
            add({u: -1, q: 2, v: -1}, {u: -1, q: 1})
            counts["triples"] += 1
    assert counts["pairs"] == count(N, 36, 54, 31, 54)
    assert counts["triples"] == sum(count(N, 64, 72, r, 108) for r in (31, 103))
    current = OLD.ARITHMETIC.clean(current)
    assert OLD.COMPILER.CURRENT.divergence(current, OLD.COMPILER.step, 1) == source
    assert OLD.ARITHMETIC.positive_mass(source) == 2 * sum(counts.values())
    assert OLD.ARITHMETIC.positive_mass(current) == counts["triples"]
    return source, current, counts


def build_extended_partial_current(N):
    old_current, old_residual, old_summary = OLD.build_combined_partial_current(N)
    removed, added_current, counts = release_families(N)
    assert all(old_residual.get(x) == c for x, c in removed.items()), "Old source capacity reused"
    residual = {x: c for x, c in old_residual.items() if x not in removed}
    current = defaultdict(int, old_current)
    for x, c in added_current.items():
        current[x] += c
    current = OLD.ARITHMETIC.clean(current)
    measure = OLD.ARITHMETIC.ANNULAR.annular_measure(N)
    div = OLD.COMPILER.CURRENT.divergence(current, OLD.COMPILER.step, 1)
    assert OLD.ARITHMETIC.subtract(measure, div) == residual
    removed_positive = old_summary["removed_positive_mass"] + 2 * sum(counts.values())
    assert OLD.ARITHMETIC.positive_mass(residual) == 99 * N // 4 - removed_positive
    cost = OLD.ARITHMETIC.positive_mass(current)
    bound = old_summary["positive_current_cost_upper_bound"] + counts["triples"]
    assert cost <= bound
    summary = dict(N=N, **counts, old_removed_positive_mass=old_summary["removed_positive_mass"],
                   additional_removed_positive_mass=2 * sum(counts.values()),
                   total_removed_positive_mass=removed_positive,
                   residual_positive_mass=OLD.ARITHMETIC.positive_mass(residual),
                   current_rows=len(current), positive_current_cost=cost,
                   positive_current_cost_bound=bound, exact_divergence_verified=True,
                   source_capacity_verified=True)
    return current, residual, summary


def audit():
    cases = [build_extended_partial_current(N)[2] for N in range(8, 1025, 8)]
    cases.append(build_extended_partial_current(6144)[2])
    # Exact floor formulas give the asymptotic constants with bounded error.
    # A shift of 216 preserves all three residue/boundary phases.
    phases = []
    for N in range(8, 217, 8):
        pair = count(N, 36, 54, 31, 54)
        triple = sum(count(N, 64, 72, r, 108) for r in (31, 103))
        assert count(N + 216, 36, 54, 31, 54) - pair == 72
        assert sum(count(N + 216, 64, 72, r, 108) for r in (31, 103)) - triple == 32
        phases.append(dict(N=N, pairs=pair, triples=triple))
    # Witness the three exact phases used in the cross-family capacity proof.
    assert all((91 + 96 * t) % 72 in (19, 43, 67) for t in range(3))
    assert all((13775 + 1152 * t) % 144 == 95 for t in range(3))
    return dict(status="PASS", cutoffs="8..1024 by8, plus6144", cases=cases,
                phase_period=216, phases=phases,
                additional_removed_positive_mass="26*N/27+O(1)",
                combined_removed_positive_mass="1073*N/432+O(1)",
                combined_positive_cost_upper_bound="73*N/432+O(1)",
                arithmetic_construction_only=True,
                universal_partial_construction_written_proof=True,
                universal_complete_construction_proved=False)


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    result = audit()
    receipt = HERE / "release_packing_audit.json"
    if args.write_receipt:
        receipt.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert json.loads(receipt.read_text()) == result
    print(json.dumps({k: v for k, v in result.items() if k not in ("cases", "phases")}, indent=2))


if __name__ == "__main__":
    main()
