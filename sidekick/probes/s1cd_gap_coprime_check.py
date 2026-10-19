"""Independent check of Lean S1-c/d (claude/lean-lane 9686831) on actual reduced 3x+q cycles.

S1-c: every sorted gap of a reduced ordered cycle is coprime to q.
S1-d: if the seam is the only forced position (J = 1), then D = 2^A - 3^m equals q.
Same cycle search and normalisation as s1b_run_start_gcd_check.py; also the rational ordered cycles
of jterm_gap_check.py (m <= 9, letters 1..4), where J = 1 must give gcd(C, D) = 1.
"""
import itertools
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402
from s1b_run_start_gcd_check import data  # noqa: E402
from jterm_gap_check import ordered  # noqa: E402


def main():
    n_cyc = n_j1 = 0
    j1_rows = []
    for q, N in [(5, 40001), (7, 40001), (13, 40001), (61, 40001), (11, 20001), (17, 20001),
                 (19, 20001), (23, 20001), (29, 20001), (233, 20001), (1201, 8001)]:
        for cyc in cycles(q, N):
            d = data(cyc, q)
            if d is None:
                continue
            m, s, B, n, gap, T = d
            assert all(math.gcd(q, x) == 1 for x in gap)
            J = sum(1 for t in T if t != 0)
            if J == 1:
                A = sum(step(x, q)[1] for x in n)
                assert 2**A - 3**m == q
                n_j1 += 1
                j1_rows.append((q, n[0], m))
            n_cyc += 1
    n_rat = n_rat_j1 = 0
    for m in range(2, 10):
        for z in itertools.product(range(1, 5), repeat=m):
            d = ordered(list(z))
            if d is None:
                continue
            n_rat += 1
            if sum(1 for t in d['tau'] if t != 0) == 1:
                assert math.gcd(d['C'], d['D']) == 1
                n_rat_j1 += 1
    out = {"probe": "s1cd_gap_coprime_check", "lean": "claude/lean-lane 9686831",
           "actual_ordered_cycles_every_gap_coprime_to_q": n_cyc,
           "actual_J1_cycles_with_D_eq_q": n_j1, "J1_examples_(q,min,m)": j1_rows,
           "rational_ordered_cycles": n_rat, "rational_J1_with_gcd_1": n_rat_j1, "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
