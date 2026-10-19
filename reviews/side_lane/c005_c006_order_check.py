"""Sidekick probe: independent checks of main's C005 and C006 (experiments/cycle_spectrum/C005, C006, main 1cb02fa).

Conventions: a rational 3x+1 cycle is given by odd numerators n_i with common reduced denominator q:
3 n_i + q = 2^(a_i) n_(i+1). L = min n_i, h_i = floor(log2(n_i/L)), z_i = n_i / 2^(h_i) in [L, 2L).
"Ordered" (C006's domain): sorting by z, the successor i -> i+1 shifts ranks by a constant mod m (circular order
preserved). J = 1 + number of adjacent height changes in z-sorted order; B = max h_i.

(1) C005 main theorem: for primitive mechanical v with coprime (A0, m0), 2^A0 > 3^m0, v != (2), every concatenation of
    rotations of v (2..6 blocks, random phases) has reduced denominator > 1. Small (A0, m0) exhaustively-phased.
(2) C005's q=1 lemma ingredient: for q = 1 an inversion needs height difference k >= 3, i.e. 3r < 2^k - 1 with r >= 1 odd.
(3) C005 controls from the census: q = 233 period 8 with gcd(C, D) = 7 and strict order (rank shift 5); q = 5 period 17
    with gcd 1,015,513 and strict order (rank shift 10); the q = 11 cycle with minimum numerator 13 has an inversion,
    H < 8L and gcd(A, m) = 2.
(4) C006 worked example: q = 233 cycle 1663, 2611, 4033, 3083, 4741, 1807, 2827, 4357 with valuations (1,1,2,1,3,1,1,3),
    B = 1, J = 3, and the stated rational bound q > 208768/14501.
(5) C006 bound on every ordered cycle in the census with q <= L: L > 2^(ceil(m/J) - 1 - B) and B + 1 <= J.
(6) C006 controls: ordered q = 13 cycle (227, 347, 527, 797, 601); the minimum odd part of the pairwise differences of
    the height-scaled numerators n 2^(B-h) is 15, main's "minimum odd gap"; q = 5 cycle (19, 31, 49).
Standard library. Run without -O.
"""
from fractions import Fraction as Fr
from math import gcd, ceil
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent


def CD(z):
    A, C, m = 0, 0, len(z)
    for j, a in enumerate(z):
        C += 3**(m - 1 - j) * 2**A
        A += a
    return C, 2**A - 3**m


def mech(A, m, l=0):
    return tuple(((j + 1) * A + l) // m - (j * A + l) // m for j in range(m))


def v2(n):
    return (n & -n).bit_length() - 1


def part1():
    n = 0
    rng = random.Random(9)
    bases = [(A, m) for m in range(1, 7) for A in range(m, 3 * m + 1) if gcd(A, m) == 1 and 2**A > 3**m]
    for A0, m0 in bases:
        v = mech(A0, m0)
        if v == (2,):
            continue
        rots = [v[i:] + v[:i] for i in range(m0)]
        for _ in range(60):
            blocks = [rng.choice(rots) for _ in range(rng.randint(2, 6))]
            w = tuple(x for b in blocks for x in b)
            C, D = CD(w)
            assert D > 0 and D // gcd(C, D) > 1, (A0, m0, blocks)
            n += 1
    return {"bases": len(bases) - 1, "concatenations": n}


def part2():
    bad = [(k, r) for k in range(1, 3) for r in range(1, 50, 2) if 3 * r - (2**k - 1) < 0]
    assert not bad
    assert 3 * 1 - (2**3 - 1) < 0
    return {"no_q1_inversion_for_k_le_2": True, "first_possible_k": 3}


def cycle_from(q, n0):
    ns, vals, x = [], [], n0
    while True:
        y = 3 * x + q
        e = v2(y)
        ns.append(x)
        vals.append(e)
        x = y >> e
        if x == n0:
            return ns, vals
        assert len(ns) < 10**4


def profile(ns, q):
    m = len(ns)
    L = min(ns)
    h = [((n // L).bit_length() - 1) for n in ns]
    for n, hi in zip(ns, h):
        assert 2**hi * L <= n < 2**(hi + 1) * L
    z = [Fr(n, 2**hi) for n, hi in zip(ns, h)]
    order = sorted(range(m), key=lambda i: z[i])
    rank = {i: r for r, i in enumerate(order)}
    shifts = {(rank[(i + 1) % m] - rank[i]) % m for i in range(m)}
    ordered = len(shifts) == 1
    J = 1 + sum(1 for a, b in zip(order, order[1:]) if h[a] != h[b])
    return {"m": m, "L": L, "B": max(h), "J": J, "ordered": ordered,
            "shift": next(iter(shifts)) if ordered else None, "H_lt_8L": max(ns) < 8 * L}


def part3_4_5(path):
    data = json.load(open(path))
    norm = {}
    for c in data["cycles"]:
        q = c["reduced_denominator"]
        sc = c["actual_scaling"]
        ns = tuple(s // sc for s in c["states"])
        assert all(s % sc == 0 for s in c["states"])
        key = (q, min(ns))
        norm[key] = (q, ns)
    checked5 = 0
    for (q, ns) in norm.values():
        if len(ns) < 2:
            continue
        pr = profile(list(ns), q)
        if pr["ordered"] and q <= pr["L"]:
            assert pr["L"] > Fr(2)**(ceil(pr["m"] / pr["J"]) - 1 - pr["B"]), (q, ns[:3], pr)
            assert pr["B"] + 1 <= pr["J"]
            checked5 += 1
    # (3) controls
    def find(q, m):
        return [ns for (qq, ns) in norm.values() if qq == q and len(ns) == m]
    c233 = find(233, 8)
    assert c233, "q233 period-8 cycle missing"
    r233 = []
    for ns in c233:
        ns2, vals = cycle_from(233, min(ns))
        C, D = CD(tuple(vals))
        pr = profile(ns2, 233)
        r233.append({"min": min(ns), "gcd": gcd(C, D), "ordered": pr["ordered"], "shift": pr["shift"]})
    assert any(r["gcd"] == 7 and r["ordered"] and r["shift"] == 5 for r in r233)
    c5 = find(5, 17)
    r5 = []
    for ns in c5:
        ns2, vals = cycle_from(5, min(ns))
        C, D = CD(tuple(vals))
        pr = profile(ns2, 5)
        r5.append({"min": min(ns), "gcd": gcd(C, D), "ordered": pr["ordered"], "shift": pr["shift"]})
    assert any(r["gcd"] == 1015513 and r["ordered"] and r["shift"] == 10 for r in r5)
    c11 = [ns for (qq, ns) in norm.values() if qq == 11 and min(ns) == 13]
    assert c11
    ns11, vals11 = cycle_from(11, 13)
    pr11 = profile(ns11, 11)
    assert not pr11["ordered"] and pr11["H_lt_8L"] and gcd(sum(vals11), len(vals11)) == 2
    # (4) C006 worked example
    ns, vals = cycle_from(233, 1663)
    assert ns == [1663, 2611, 4033, 3083, 4741, 1807, 2827, 4357] and vals == [1, 1, 2, 1, 3, 1, 1, 3]
    pr = profile(ns, 233)
    assert pr["B"] == 1 and pr["J"] == 3
    assert Fr(208768, 14501) < 233 and 15 > Fr(208768, 14501) > 14
    return {"normalized_cycles": len(norm), "ordered_cycles_checked_for_C006_bound": checked5,
            "q233_controls": r233, "q5_period17_controls": r5,
            "q11_min13": {"ordered": pr11["ordered"], "H_lt_8L": pr11["H_lt_8L"], "gcd_A_m": 2},
            "c006_example": {"B": pr["B"], "J": pr["J"]}}


def part6():
    ns, vals = cycle_from(13, 227)
    assert sorted(ns) == [227, 347, 527, 601, 797]
    pr = profile(ns, 13)
    L = min(ns)
    h = [((n // L).bit_length() - 1) for n in ns]
    B = max(h)
    scaled = sorted(n * 2**(B - hi) for n, hi in zip(ns, h))
    def odd_part(x):
        return x >> v2(x)
    min_odd_gap = min(odd_part(b - a) for i, a in enumerate(scaled) for b in scaled[i + 1:])
    assert pr["ordered"] and min_odd_gap == 15
    ns5, _ = cycle_from(5, 19)
    assert ns5 == [19, 31, 49]
    return {"q13_min_odd_part_of_scaled_pair_gaps": min_odd_gap, "q13_ordered": pr["ordered"]}


def main():
    out = {"probe": "c005_c006_order_check", "main": "1cb02fa", "c005_rotation_blocks": part1(),
           "c005_q1_inversion": part2(), "census_checks": part3_4_5(sys.argv[1]), "c006_controls": part6(),
           "result": "PASS"}
    (HERE / "c005_c006_order_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
