"""Sidekick probe: independent checks of main's C007 (experiments/cycle_spectrum/C007, main dddbe33).

(1) The new q29 cycle: from seed 5859, the raw 3x+29 odd-only orbit reaches a cycle with minimum 7055, maximum 1,051,393,
    odd period 41, total exponent 65, cancellation factor gcd(C, D) = 14,499,716,215,459,201, B = 7, J = 38; ordered?
(2) The candidate law B <= q - 1 on every normalized census cycle with q <= L (C001 census plus the new cycle), ordered
    or not; report the largest B/(q-1) among ordered cycles.
(3) The modular identity z_i = n_i / 2^(h_i) = L 3^i 2^(-P_i) (mod q), P_i = sum_(j<i) c_j, c_j = a_j + h_(j+1) - h_j,
    indexing from the minimum, on every normalized census cycle with q > 1.
(4) The ordered q5 cycle from 187: raw residues mod 5 at heights 0, 1, 2, 3.
Standard library. Run without -O.
"""
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent


def v2(n):
    return (n & -n).bit_length() - 1


def CD(z):
    A, C, m = 0, 0, len(z)
    for j, a in enumerate(z):
        C += 3**(m - 1 - j) * 2**A
        A += a
    return C, 2**A - 3**m


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


def find_cycle(q, seed):
    seen, x = {}, seed
    while x not in seen:
        seen[x] = 1
        y = 3 * x + q
        x = y >> v2(y)
    return cycle_from(q, min(cycle_from(q, x)[0]))


def profile(ns):
    m, L = len(ns), min(ns)
    h = [((n // L).bit_length() - 1) for n in ns]
    z = [Fr(n, 2**hi) for n, hi in zip(ns, h)]
    order = sorted(range(m), key=lambda i: z[i])
    rank = {i: r for r, i in enumerate(order)}
    shifts = {(rank[(i + 1) % m] - rank[i]) % m for i in range(m)}
    J = 1 + sum(1 for a, b in zip(order, order[1:]) if h[a] != h[b])
    return {"m": m, "L": L, "H": max(ns), "B": max(h), "J": J, "ordered": len(shifts) == 1, "h": h}


def part1():
    ns, vals = find_cycle(29, 5859)
    C, D = CD(tuple(vals))
    pr = profile(ns)
    assert (min(ns), max(ns), len(ns), sum(vals)) == (7055, 1051393, 41, 65)
    assert gcd(C, D) == 14499716215459201 and pr["B"] == 7 and pr["J"] == 38
    assert D // gcd(C, D) == 29
    return {"min": 7055, "max": 1051393, "period": 41, "A": 65, "gcd": gcd(C, D), "B": 7, "J": 38,
            "ordered": pr["ordered"], "den": 29}


def norm_cycles(path):
    data = json.load(open(path))
    out = {}
    for c in data["cycles"]:
        q, sc = c["reduced_denominator"], c["actual_scaling"]
        ns = [s // sc for s in c["states"]]
        out[(q, min(ns))] = (q, ns)
    ns, _ = find_cycle(29, 5859)
    out[(29, min(ns))] = (29, ns)
    return out


def part2(cyc):
    worst_ordered, n_checked, n_ordered = Fr(0), 0, 0
    for q, ns in cyc.values():
        if len(ns) < 2:
            continue
        pr = profile(ns)
        if q <= pr["L"]:
            n_checked += 1
            assert pr["B"] <= q - 1, (q, min(ns), pr["B"])
            if pr["ordered"]:
                n_ordered += 1
                worst_ordered = max(worst_ordered, Fr(pr["B"], q - 1))
    return {"cycles_with_q_le_L": n_checked, "ordered": n_ordered, "max_B_over_q_minus_1_ordered": str(worst_ordered)}


def part3(cyc):
    n = 0
    for q, ns in cyc.values():
        if q == 1 or len(ns) < 2:
            continue
        i0 = ns.index(min(ns))
        ns = ns[i0:] + ns[:i0]
        _, vals = cycle_from(q, ns[0])
        L = ns[0]
        pr = profile(ns)
        h = pr["h"]
        m = len(ns)
        P = 0
        for i in range(m):
            zi = Fr(ns[i], 2**h[i])
            lhs = (zi.numerator * pow(zi.denominator, -1, q)) % q
            rhs = (L * pow(3, i, q) * pow(pow(2, P, q), -1, q)) % q
            assert lhs == rhs, (q, ns[0], i)
            c = vals[i] + h[(i + 1) % m] - h[i]
            P += c
            n += 1
    return {"states_checked": n}


def part4(cyc):
    ns, _ = cycle_from(5, 187)
    pr = profile(ns)
    res = {}
    for n, hi in zip(ns, pr["h"]):
        res.setdefault(hi, set()).add(n % 5)
    return {"ordered": pr["ordered"], "B": pr["B"], "raw_residues_mod5_by_height": {k: sorted(v) for k, v in sorted(res.items())}}


def main():
    cyc = norm_cycles(sys.argv[1])
    out = {"probe": "c007_height_check", "main": "dddbe33", "new_q29_cycle": part1(), "B_le_q_minus_1": part2(cyc),
           "modular_identity": part3(cyc), "q5_from_187": part4(cyc), "result": "PASS"}
    (HERE / "c007_height_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
