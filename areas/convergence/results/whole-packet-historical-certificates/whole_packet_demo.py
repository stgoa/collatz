"""Capped historical-current experiments on entire right-packet measures.

Run normally to reproduce and compare the persisted receipt. Use
--write-receipts to save the deterministic report and selected certificates.
No finite experiment proves a uniform depth bound or universal termination.
"""

import argparse
from collections import defaultdict
import csv
from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path

from verify_obstructions import capped_search, clean, divergence

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location(
    "right_packet_source", ROOT / "experiments/packet_currents/right_aligned_packets.py")
packet_source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(packet_source)
step, push = packet_source.step, packet_source.push
MANTISSAS = [8192, 8467, 8751, 9045, 9348, 9662, 9986, 10321,
             10668, 11026, 11396, 11778, 12173, 12582, 13004,
             13440, 13891, 14358, 14839, 15337, 15852]
CUTOFFS = [120, 236, 480, 517, 1984, 2053, 3008, 8197, 15104, 65536]
HISTORICAL_CAP = 96
SYNCHRONOUS_CAP = 512
SOURCE_HITTING_CAP = 1000


def audit_ray_constants():
    alpha = F(10337, 10000)
    ratios = [F(y, x) for x, y in zip(MANTISSAS, MANTISSAS[1:] + [16384])]
    assert max(ratios) == F(10668, 10321) < alpha
    args = [alpha / 4, 3 * alpha / 2, 3 * alpha / 4]
    upper = [F(n, 10000) for n in (5821, 11918, 9032)]
    assert all(x * x < u**5 for x, u in zip(args, upper))
    q = args[0] * upper[0] + (args[1] * upper[1] + args[2] * upper[2]) / 3
    assert q == F(399928193, 400000000) < 1
    return dict(rays=21, maximum_gap=str(max(ratios)), mesh_upper=str(alpha),
                comparison_power="7/5", contraction_upper=str(q),
                finite_base_check="delegated to frontier/check_sparse_criteria.py")


def exposed_components(mu, depth):
    adjacency = defaultdict(set)
    for source in mu:
        adjacency[source]
        x = source
        for _ in range(depth):
            if x == 1:
                break
            y = step(x)
            adjacency[x].add(y)
            adjacency[y].add(x)
            x = y
    unseen, unresolved, absorbed_sources = set(adjacency), [], 0
    while unseen:
        anchor = min(unseen)
        stack, component = [anchor], {anchor}
        unseen.remove(anchor)
        while stack:
            x = stack.pop()
            for y in adjacency[x]:
                if y in unseen:
                    unseen.remove(y)
                    component.add(y)
                    stack.append(y)
        sources = sorted(x for x in component if x in mu)
        if 1 in component:
            absorbed_sources += len(sources)
        else:
            unresolved.append(dict(minimum_state=min(component),
                                   source_count=len(sources),
                                   signed_source_mass=sum(mu[x] for x in sources),
                                   source_states=sources))
    return dict(sources_linked_to_1=absorbed_sources,
                sources_not_linked_to_1=len(mu) - absorbed_sources,
                unresolved_components=unresolved)


def synchronous_certificate(mu):
    current, residual, first_nonpositive = defaultdict(int), dict(mu), None
    for depth in range(SYNCHRONOUS_CAP + 1):
        if first_nonpositive is None and all(c < 0 for c in residual.values()):
            first_nonpositive = depth
        if not residual:
            return dict(status="certificate", depth=depth,
                        first_nonpositive_depth=first_nonpositive,
                        current=clean(current))
        if depth == SYNCHRONOUS_CAP:
            break
        for x, c in residual.items():
            current[x] += c
        residual = push(residual)
    return dict(status="unresolved", depth=SYNCHRONOUS_CAP,
                first_nonpositive_depth=first_nonpositive)


def bounded_source_hitting_times(mu):
    times = {}
    for source in mu:
        x, seen = source, set()
        for t in range(SOURCE_HITTING_CAP + 1):
            if x == 1:
                times[source] = t
                break
            if t == SOURCE_HITTING_CAP or x in seen:
                return dict(status="unresolved", source=source, steps=t)
            seen.add(x)
            x = step(x)
    return dict(status="all_absorbed", maximum_time=max(times.values(), default=0))


def certificate_metrics(result, mu):
    metrics = {k: v for k, v in result.items() if k not in ("current", "residual")}
    if result["status"] == "certificate":
        current, residual = result["current"], result["residual"]
        check = defaultdict(int, divergence(current, step, 1))
        for x, c in residual.items():
            check[x] += c
        assert clean(check) == mu
        assert all(c < 0 for c in residual.values())
        metrics.update(current_rows=len(current),
                       positive_current_cost=sum(c for c in current.values() if c > 0),
                       residual_rows=len(residual), residual_mass=sum(residual.values()),
                       exposure=exposed_components(mu, result["depth"]))
    return metrics


def write_or_check_table(path, table, write):
    rows = [(x, table[x]) for x in sorted(table)]
    if write:
        with path.open("w", newline="") as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow(["state", "weight"])
            writer.writerows(rows)
    else:
        with path.open(newline="") as f:
            reader = csv.reader(f)
            assert next(reader) == ["state", "weight"]
            assert [(int(x), int(c)) for x, c in reader] == rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-receipts", action="store_true")
    args = parser.parse_args()
    samples = []
    for N in CUTOFFS:
        mu, _, _ = packet_source.right_packets(N)
        exact = capped_search(mu, step, 1, HISTORICAL_CAP)
        one_sided = capped_search(mu, step, 1, HISTORICAL_CAP, one_sided=True)
        synchronous = synchronous_certificate(mu)
        sample = dict(N=N, packet_atoms=len(mu),
                      historical_exact=certificate_metrics(exact, mu),
                      historical_one_sided=certificate_metrics(one_sided, mu),
                      synchronous={k: v for k, v in synchronous.items() if k != "current"},
                      source_hitting_times=bounded_source_hitting_times(mu))
        if exact["status"] == synchronous["status"] == "certificate":
            assert exact["current"] == synchronous["current"]
            sample["historical_and_synchronous_exact_currents_identical"] = True
        if N in (2053, 65536):
            stored = [("exact", exact)] if N == 65536 else [("one_sided", one_sided)]
            for label, result in stored:
                assert result["status"] == "certificate", result
                write_or_check_table(HERE / f"{label}_{N}.csv", result["current"], args.write_receipts)
                write_or_check_table(HERE / f"{label}_residual_{N}.csv", result["residual"], args.write_receipts)
        samples.append(sample)
        print(json.dumps(dict(N=N, exact_depth=exact["depth"],
                              one_sided_depth=one_sided["depth"],
                              synchronous_depth=synchronous["depth"])), flush=True)
    report = dict(status="PASS", ray_constants=audit_ray_constants(),
                  caps=dict(historical_depth=HISTORICAL_CAP,
                            synchronous_depth=SYNCHRONOUS_CAP,
                            per_source_hitting_time=SOURCE_HITTING_CAP),
                  samples=samples, universal_current_existence_proved=False,
                  uniform_exposure_depth_proved=False)
    path = HERE / "whole_packet_audit.json"
    if args.write_receipts:
        path.write_text(json.dumps(report, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == report
    print("PASS: finite historical-current certificates and sparse-ray constants")


if __name__ == "__main__":
    main()
