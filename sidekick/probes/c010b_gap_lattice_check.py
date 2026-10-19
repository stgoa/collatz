"""Independent check of Lean C010-b (claude/lean-lane 4a707e3): the complete dyadic gap lattice.

(a) Actual cycles of 3x+q (ordered AND unordered), sorted scaled states Z_j = 2^(B-H_j) n_[j]:
    Z_j = sum_i G_i + sum_(i<j) G_i for the complete gaps G (seam 2Z_0 - Z_(m-1)), gcd(Z) = gcd(G) = 1,
    and G > 0 (the order cone).
(b) Rational ordered cycles (m <= 9, letters 1..4) normalised to parameter 1 (states C_(i)/D):
    the least common denominator of the scaled sorted states Y_j = 2^(B-H_j) x_[j] and of their
    complete gaps are equal, and equal to the reduced denominator q = D/gcd(C, D).
"""
import itertools
import json
import math
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles  # noqa: E402
from jterm_gap_check import ordered, CD, rot  # noqa: E402


def cgap(Z):
    m = len(Z)
    return [Z[j + 1] - Z[j] for j in range(m - 1)] + [2 * Z[0] - Z[m - 1]]


def sorted_scaled(states):
    L = min(states)
    h = []
    for x in states:
        k = 0
        while x >= 2**(k + 1) * L:
            k += 1
        h.append(k)
    B = max(h)
    return sorted(2**(B - t) * x for t, x in zip(h, states))


def lcm_den(v):
    out = 1
    for x in v:
        out = out * x.denominator // math.gcd(out, x.denominator)
    return out


def main():
    n_act = 0
    for q, N in [(5, 40001), (7, 40001), (13, 40001), (61, 40001), (11, 20001), (17, 20001),
                 (19, 20001), (23, 20001), (29, 20001), (233, 20001), (1201, 8001)]:
        for cyc in cycles(q, N):
            Z = sorted_scaled(cyc)
            G = cgap(Z)
            m = len(Z)
            for j in range(m):
                assert Z[j] == sum(G) + sum(G[:j])
            assert math.gcd(*Z) == 1 if m > 1 else Z[0] % 2 == 1
            assert math.gcd(*G) == 1 if m > 1 else True
            assert all(g > 0 for g in G)
            n_act += 1
    n_rat = 0
    for m in range(2, 10):
        for z in itertools.product(range(1, 5), repeat=m):
            d = ordered(list(z))
            if d is None:
                continue
            Cs = [CD(rot(list(z), i))[0] for i in range(m)]
            D = d['D']
            Y = sorted_scaled([Fr(c, D) for c in Cs])
            G = cgap(Y)
            qred = D // math.gcd(d['C'], D)
            assert lcm_den(Y) == lcm_den(G) == qred
            n_rat += 1
    out = {"probe": "c010b_gap_lattice_check", "lean": "claude/lean-lane 4a707e3",
           "actual_cycles_all_orders": n_act, "rational_ordered_cycles_lcd_equal_q": n_rat,
           "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
