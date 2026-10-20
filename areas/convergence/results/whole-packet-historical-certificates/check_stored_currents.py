"""Check the two stored whole-packet currents against freshly built packets.

Written at the B08 migration; the legacy whole_packet_demo.py no longer runs at
this path. For N = 65536 (exact) and N = 2053 (one-sided) it rebuilds the
right-aligned packet measure with the constructor of the node
right-aligned-fixed-core-remainder and checks, in exact integer arithmetic,

    Pi_N = (I - P) J + Z,   P = one odd-only Syracuse step, mass at 1 discarded,

with Z = 0 for the exact table and Z <= 0 (total mass -5) for the one-sided one.
It also checks the row counts and positive costs quoted in the node.
Run from the repository root: python3 <this file>. Exits 1 on any failure.
"""

import csv
import importlib.util
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PACKETS_PATH = HERE.parent / "right-aligned-fixed-core-remainder" / "right_aligned_packets.py"
spec = importlib.util.spec_from_file_location("right_aligned_packets", PACKETS_PATH)
packets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(packets)

# (N, current table, residual table, rows, positive cost, residual rows, residual mass, one-sided)
CASES = (
    (65536, "exact_65536.csv", "exact_residual_65536.csv", 53621, 74725, 0, 0, False),
    (2053, "one_sided_2053.csv", "one_sided_residual_2053.csv", 1532, 1950, 4, -5, True),
)


def read_table(name):
    with (HERE / name).open(newline="") as f:
        reader = csv.reader(f)
        if next(reader) != ["state", "weight"]:
            raise ValueError(f"{name}: unexpected header")
        rows = [(int(x), int(c)) for x, c in reader]
    table = dict(rows)
    if len(table) != len(rows) or any(c == 0 for c in table.values()):
        raise ValueError(f"{name}: repeated state or zero weight")
    return table


def divergence(current):
    out = defaultdict(int)
    for x, c in current.items():
        if x == 1 or x % 2 == 0 or x < 1:
            raise ValueError(f"current row at invalid state {x}")
        out[x] += c
        y = packets.step(x)
        if y != 1:
            out[y] -= c
    return out


def check(case):
    N, cur_name, res_name, rows, cost, res_rows, res_mass, one_sided = case
    mu, _, _ = packets.right_packets(N)
    current, residual = read_table(cur_name), read_table(res_name)
    total = divergence(current)
    for x, c in residual.items():
        total[x] += c
    total = {x: c for x, c in total.items() if c}
    failures = []
    if total != {x: c for x, c in mu.items() if c}:
        failures.append("identity Pi_N = (I-P)J + Z fails")
    if len(current) != rows:
        failures.append(f"{len(current)} current rows, expected {rows}")
    if sum(max(c, 0) for c in current.values()) != cost:
        failures.append("positive current cost differs")
    if len(residual) != res_rows or sum(residual.values()) != res_mass:
        failures.append("residual size or mass differs")
    if one_sided and any(c > 0 for c in residual.values()):
        failures.append("one-sided residual has a positive atom")
    return N, len(mu), failures


def main():
    bad = False
    for case in CASES:
        N, atoms, failures = check(case)
        print(f"N={N}: {atoms} packet atoms, " + ("PASS" if not failures else "FAIL: " + "; ".join(failures)))
        bad = bad or bool(failures)
    if bad:
        sys.exit(1)
    print("PASS: both stored whole-packet currents verified")


if __name__ == "__main__":
    main()
