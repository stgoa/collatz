"""Independent check of Lean C006-d (claude/lean-lane 818d1d6): (G2) from an explicit gap hypothesis.

On the actual ordered 3x+q cycles (same search as s1a_integer_cycle_check.py), take mu = 0 and the
tightest c with 2^A <= 2^c (2^A - 3^m), i.e. c = ceil(log2(2^A/(2^A - 3^m))), and check the conclusion
3 * 2^floor((m-1)/J) < 2^(B+c) * q * m^(mu+1), together with delta_ge_gap:
(2^A - 3^m)/2^A <= A log 2 - m log 3.
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402
from s1b_run_start_gcd_check import data  # noqa: E402


def main():
    n = 0
    slack = []
    for q, N in [(5, 40001), (7, 40001), (13, 40001), (61, 40001), (11, 20001), (17, 20001),
                 (19, 20001), (23, 20001), (29, 20001), (233, 20001), (1201, 8001)]:
        for cyc in cycles(q, N):
            d = data(cyc, q)
            if d is None:
                continue
            m, s, B, nn, gap, T = d
            A = sum(step(x, q)[1] for x in nn)
            D = 2**A - 3**m
            assert D > 0
            assert D / 2**A <= A * math.log(2) - m * math.log(3) + 1e-15
            c = 0
            while 2**A > 2**c * D:
                c += 1
            J = sum(1 for t in T if t != 0)
            lhs = 3 * 2**((m - 1) // J)
            rhs = 2**(B + c) * q * m
            assert lhs < rhs, (q, nn[0], m, J, B, c)
            slack.append(math.log2(rhs / lhs))
            n += 1
    out = {"probe": "c006d_g2_check", "lean": "claude/lean-lane 818d1d6", "ordered_cycles": n,
           "log2_slack_(rhs/lhs)": {"min": round(min(slack), 2), "max": round(max(slack), 2)},
           "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
