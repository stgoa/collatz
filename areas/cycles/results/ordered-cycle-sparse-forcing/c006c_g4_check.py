"""Independent check of Lean C006-c (claude/lean-lane b113413): C006's (G4) on actual cycles.

For every actual cycle of T_q (q in 1, 5, 7, 11, 13, 17, 19, 23, 29, 61, 233, 1201; cycles found by
iteration, ordered or not): the exact product identity 2^A prod n_i = prod (3 n_i + q) (integers), the
log identity A log 2 - m log 3 = sum log(1 + q/(3 n_i)) (floating, to 1e-12 relative), and
delta = A log 2 - m log 3 <= m q/(3 L); the looseness ratio (m q/(3L))/delta is reported.
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402


def main():
    n = 0
    ratios = []
    for q, N in [(1, 2001), (5, 40001), (7, 40001), (11, 20001), (13, 40001), (17, 20001),
                 (19, 20001), (23, 20001), (29, 20001), (61, 40001), (233, 20001), (1201, 8001)]:
        for cyc in cycles(q, N):
            m = len(cyc)
            a = [step(x, q)[1] for x in cyc]
            A = sum(a)
            lhs = 2**A * math.prod(cyc)
            rhs = math.prod(3 * x + q for x in cyc)
            assert lhs == rhs
            delta = A * math.log(2) - m * math.log(3)
            s = sum(math.log1p(q / (3 * x)) for x in cyc)
            assert abs(delta - s) <= 1e-12 * max(1.0, abs(delta))
            L = min(cyc)
            bound = m * q / (3 * L)
            assert delta <= bound * (1 + 1e-12)
            ratios.append(bound / delta)
            n += 1
    out = {"probe": "c006c_g4_check", "lean": "claude/lean-lane b113413", "actual_cycles": n,
           "looseness_(mq/3L)/delta": {"min": round(min(ratios), 4), "max": round(max(ratios), 2)},
           "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
