"""Independent check of Lean C006-e (claude/lean-lane 6c42229): the C_c form of (G1).

On every ordered cycle -- the 33 actual ordered 3x+q cycles of s1a_integer_cycle_check.py and the 337
rational ordered cycles of jterm_gap_check.py -- read from its minimum, with heights h_j and normalised
letters c_j = a_j + h_(j+1) - h_j:
  P_j = A_j + h_j (prefix sums), C_h = sum 3^(m-1-j) 2^(A_j) <= C_c = sum 3^(m-1-j) 2^(P_j);
  the normalised word equals mech(A, m, 0) (phase 0) -- Lean proves this at q = 1, B <= 2 via three_band,
  here it is tested for every ordered cycle at any q; gcd(C_c, D) = 1 when gcd(A, m) = 1 (R71-a);
  D n_0 <= q C_c (actual cycles); and (G1) second form D 2^floor((m-1)/J) < 2^B q C_c (actual cycles).
"""
import itertools
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402
from s1b_run_start_gcd_check import data  # noqa: E402
from jterm_gap_check import ordered, CD, rot  # noqa: E402


def mech(A, m, l):
    return [((j + 1) * A + l) // m - (j * A + l) // m for j in range(m)]


def heights(states):
    L = states[0]
    h = []
    for x in states:
        k = 0
        while x >= 2**(k + 1) * L:
            k += 1
        h.append(k)
    return h


def check_word(a, states):
    m = len(a)
    A = sum(a)
    h = heights(states)
    c = [a[j] + h[(j + 1) % m] - h[j] for j in range(m)]
    Apre = [sum(a[:j]) for j in range(m)]
    Ppre = [sum(c[:j]) for j in range(m)]
    assert all(Ppre[j] == Apre[j] + h[j] for j in range(m))
    Ch = sum(3**(m - 1 - j) * 2**Apre[j] for j in range(m))
    Cc = sum(3**(m - 1 - j) * 2**Ppre[j] for j in range(m))
    assert Ch <= Cc
    assert c == mech(A, m, 0), (a, c)
    D = 2**A - 3**m
    if math.gcd(A, m) == 1:
        assert math.gcd(Cc, D) == 1
    return Ch, Cc, D, max(h)


def main():
    n_act = 0
    for q, N in [(5, 40001), (7, 40001), (13, 40001), (61, 40001), (11, 20001), (17, 20001),
                 (19, 20001), (23, 20001), (29, 20001), (233, 20001), (1201, 8001)]:
        for cyc in cycles(q, N):
            d = data(cyc, q)
            if d is None:
                continue
            m, s, B, n, gap, T = d
            a = [step(x, q)[1] for x in n]
            Ch, Cc, D, Bmax = check_word(a, n)
            assert D * n[0] <= q * Cc
            J = sum(1 for t in T if t != 0)
            assert D * 2**((m - 1) // J) < 2**B * q * Cc
            n_act += 1
    n_rat = 0
    for m in range(2, 10):
        for z in itertools.product(range(1, 5), repeat=m):
            d = ordered(list(z))
            if d is None:
                continue
            states = [CD(rot(list(z), i))[0] for i in range(m)]
            check_word(list(z), states)
            n_rat += 1
    out = {"probe": "c006e_cc_check", "lean": "claude/lean-lane 6c42229",
           "actual_ordered_cycles": n_act, "rational_ordered_cycles": n_rat,
           "normalised_word_is_mech_phase0_at_any_q": True, "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
