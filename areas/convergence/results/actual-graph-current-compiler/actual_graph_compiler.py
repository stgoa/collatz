"""Compile finite packet certificates into an integer convergence certificate.

The finite cone is conditional on its packet inputs. This demo discovers those
inputs with a capped historical search, verifies every divergence, constructs
an exact rational current with positive residual mass <1, then extracts an
integer current using only its already exposed arrows. No universal input
constructor or Collatz proof is supplied.
"""

import argparse
from collections import defaultdict
import csv
import hashlib
import importlib.util
import json
from math import lcm
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CONE = load("forcing_cone", HERE.parent / "duality/finite_cone.py")
GRAPH = load("forcing_graph", ROOT / "experiments/annular_construction/components/annular_components.py")
PACKETS = GRAPH.ANNULAR.PACKETS
CURRENT = GRAPH.CURRENT


def add(table, source, multiplier=1):
    for x, coefficient in source.items():
        table[x] += multiplier * coefficient


def counting(cutoff):
    return dict.fromkeys(range(3, cutoff + 1, 2), 1)


def hash_table(table):
    data = "".join(f"{x},{c}\n" for x, c in sorted(table.items()))
    return hashlib.sha256(data.encode()).hexdigest()


def absorption_current(measure, cap=1000):
    """Used only for the proved finite base/core, with a strict discovery cap."""
    current = defaultdict(int)
    for x, coefficient in measure.items():
        for _ in range(cap):
            if x == 1:
                break
            current[x] += coefficient
            x = PACKETS.step(x)
        else:
            raise RuntimeError("Finite base/core absorption cap reached")
    current = CURRENT.clean(current)
    assert CURRENT.divergence(current, PACKETS.step, 1) == measure
    return current


def discover_packet_input(N, cap=128):
    """Capped historical search; a cap is unresolved, never a nonexistence claim."""
    source, eta, _ = PACKETS.right_packets(N)
    components = GRAPH.Components(source, dict.fromkeys(source, 0))
    frontier, edges = list(source), {}
    for depth in range(cap + 1):
        good = all(components.absorbed[r] or components.masses[r][0] <= 0
                   for r in components.roots)
        if good:
            current, residual = GRAPH.current_for(source, edges, True)
            unknown_sources = sum(sum(components.counts[r]) for r in components.roots
                                  if not components.absorbed[r])
            return current, residual, dict(
                N=N, exposure_depth=depth, source_atoms=len(source),
                current_rows=len(current), residual_atoms=len(residual),
                sources_not_linked_to_1=unknown_sources,
                current_sha256=hash_table(current), residual_sha256=hash_table(residual))
        if depth == cap:
            break
        following = []
        for x in frontier:
            if x == 1:
                continue
            y = PACKETS.step(x)
            edges[x] = y
            if components.add(y):
                following.append(y)
            components.union(x, y)
        frontier = following
    raise RuntimeError(f"Packet input at N={N} unresolved at depth {cap}")


def compile_inputs(plan, provider):
    """Verify supplied packet currents and compile one exact integer U_g current.

    provider(N) returns (integer current, everywhere nonpositive residual, meta).
    It may load previously stored certificates; discovery is not required here.
    All rational arithmetic is represented over one exact common denominator.
    """
    assert plan["forces_target"] and plan["upper_boundary_mass"] < 1
    coefficients = [*plan["packet_weights"].values(),
                    *plan["lower_boundary"].values(), *plan["upper_boundary"].values()]
    denominator = lcm(*(c.denominator for c in coefficients))
    current_num, residual_num = defaultdict(int), defaultdict(int)
    input_receipts = []
    for N, weight in plan["packet_weights"].items():
        numerator = int(weight * denominator)
        assert numerator == weight * denominator and numerator >= 0
        source, eta, _ = PACKETS.right_packets(N)
        current, residual, meta = provider(N)
        assert all(isinstance(x, int) and x > 1 and x % 2 == 1
                   and isinstance(c, int) for table in (current, residual)
                   for x, c in table.items())
        assert all(c <= 0 for c in residual.values())
        check = defaultdict(int, CURRENT.divergence(current, PACKETS.step, 1))
        add(check, residual)
        assert CURRENT.clean(check) == source
        input_receipts.append(meta)

        # D_N = Pi_N + eta_N + (I-P)K_N, at the exact integer cutoffs.
        K = defaultdict(int, PACKETS.initial(N))
        for x in range(N // 4 + 1, N + 1, 2):
            assert x % 2 == 1
            K[x] += 3
        K = CURRENT.clean(K)
        eta_current = absorption_current(eta)
        add(current_num, current, numerator)
        add(current_num, K, numerator)
        add(current_num, eta_current, numerator)
        add(residual_num, residual, numerator)

        ordinal = next(k for k in range(CONE.FIRST, 5 * plan["B"])
                       if CONE.grid_cutoff(k) == N)
        rounded = CONE.grid_cutoff(ordinal + 3)
        # The rounding shells are nonnegative and enter with a minus sign.
        for low, high in ((3 * N // 2, rounded), (3 * N // 4, rounded // 2)):
            assert low <= high and low % 2 == high % 2 == 0
            for x in range(low + 1, high + 1, 2):
                residual_num[x] -= numerator

    for N, weight in plan["lower_boundary"].items():
        assert N < 96
        add(current_num, absorption_current(counting(N)), int(weight * denominator))
    for N, weight in plan["upper_boundary"].items():
        add(residual_num, counting(N), int(weight * denominator))

    current_num, residual_num = CURRENT.clean(current_num), CURRENT.clean(residual_num)
    target = counting(plan["target_cutoff"])
    check = defaultdict(int, CURRENT.divergence(current_num, PACKETS.step, 1))
    add(check, residual_num)
    assert CURRENT.clean(check) == {x: denominator for x in target}
    positive_numerator = sum(c for c in residual_num.values() if c > 0)
    assert positive_numerator <= plan["upper_boundary_mass"] * denominator
    assert positive_numerator < denominator

    # Integer component masses force absorption on this graph. The extraction
    # below adds no arrows and does not follow any previously unexposed future.
    edges = {x: PACKETS.step(x) for x in current_num}
    certificate = CURRENT.finite_certificate(target, edges, 1, False)
    assert certificate is not None, "Integrality forcing failed on verified input"
    integral_current, final_residual = certificate
    assert not final_residual and set(integral_current) <= set(edges)
    assert all(isinstance(c, int) and c > 0 for c in integral_current.values())
    assert CURRENT.divergence(integral_current, PACKETS.step, 1) == target
    receipt = dict(
        m=plan["m"], target_cutoff=plan["target_cutoff"], B=plan["B"],
        input_packet_count=len(input_receipts), largest_input_cutoff=max(plan["cutoffs"]),
        exact_upper_boundary_mass=str(plan["upper_boundary_mass"]),
        rational_denominator=denominator, rational_current_rows=len(current_num),
        rational_current_numerator_sha256=hash_table(current_num),
        rational_residual_atoms=len(residual_num),
        rational_residual_numerator_sha256=hash_table(residual_num),
        positive_residual_numerator=positive_numerator,
        exact_positive_residual_mass=str(CONE.Fraction(positive_numerator, denominator)),
        integer_target_mass=len(target), integral_current_rows=len(integral_current),
        integral_current_sha256=hash_table(integral_current),
        no_new_arrows_during_extraction=True, inputs=input_receipts)
    return integral_current, receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    plan = CONE.finite_forcing_plan(97, B=9)
    current, receipt = compile_inputs(plan, discover_packet_input)
    receipt = dict(status="PASS", finite_demo=receipt,
                   universal_input_certificate_construction_proved=False)
    path = HERE / "forcing_demo_audit.json"
    table = HERE / "forced_U112_current.csv"
    if args.write_receipt:
        path.write_text(json.dumps(receipt, indent=2) + "\n")
        with table.open("w", newline="") as out:
            writer = csv.writer(out, lineterminator="\n")
            writer.writerow(("state", "weight"))
            writer.writerows(sorted(current.items()))
    else:
        assert json.loads(path.read_text()) == receipt
        with table.open(newline="") as inp:
            saved = {int(row["state"]): int(row["weight"]) for row in csv.DictReader(inp)}
        assert saved == current
    print(json.dumps({k: v for k, v in receipt["finite_demo"].items() if k != "inputs"}, indent=2))


if __name__ == "__main__":
    main()
