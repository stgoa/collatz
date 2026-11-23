#!/usr/bin/env python3
"""Exploration for near-circuit-rotation-forced-relation (not a certificate; never run by CI).

Near-circuits in the normalised model: everything divided by the period m, time t in (0, 1], minimum at time 0,
heights Z(t) = (alpha - 1) t, one giant letter at time 1 that brings the height back to 0, all other excesses
negligible. A rotation with rotation number h in (0, 1/2] has s mismatches: the two of the giant, at times 1
and 1 - h, and s - 2 others at arbitrary times, with negligible letter differences.

Only the rows and the relations of this rotation are used:
  rows       for each run between consecutive mismatches, G = (higher starting height) - (run length) >= 0;
  relations  at each mismatch, 3^n g = (2^nu' - 2^nu) xi + 2^c g' for either choice of the state xi, in
             three-term and four-term form, as in half-period-six-mismatch-local-law.
The order type is the number of small mismatches before time 1 - h; given it, everything is linear in h and
the mismatch times. For each order type one linear programme maximises t such that every relation has
(sum of logs of parts coprime to 6) >= (log of the largest term) + t. A negative maximum means: some relation
is forced to have a small product, with -t bits per unit of m to spare. "None" means the rows have no solution.

Needs numpy and scipy, floating point.

    python3 areas/cycles/results/near-circuit-rotation-forced-relation/explore_near_circuit_lp.py [--write-receipt]
"""
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

AL = float(np.log2(3.0))
A1 = AL - 1.0
HERE = Path(__file__).resolve().parent


def lin(*pairs):
    out = {}
    for coef, v in pairs:
        for key, a in v.items():
            out[key] = out.get(key, 0.0) + coef * a
    return out


def solve(s, below):
    k = s - 2
    nv = k + 2
    ih, it = 0, k + 1
    one = {"const": 1.0}
    h = {ih: 1.0}
    p_time = lin((1, one), (-1, h))
    rows = []

    def le(c, rhs=0.0):
        rows.append((dict(c), rhs))

    cuts = [("s", {1 + i: 1.0}, True) for i in range(below)] + [("P", p_time, None)]
    cuts += [("s", {1 + i: 1.0}, False) for i in range(below, k)] + [("K", one, None)]
    le(lin((-1, cuts[0][1])))
    for i in range(len(cuts) - 1):
        le(lin((1, cuts[i][1]), (-1, cuts[i + 1][1])))
    le(h, 0.5)

    def after(cut):
        kind, pos, is_below = cut
        if kind == "K":
            return {}, lin((A1, h))
        if kind == "P":
            return lin((A1, pos)), {}
        if is_below:
            return lin((A1, pos)), lin((A1, pos), (A1, h))
        return lin((A1, pos)), lin((A1, pos), (A1, h), (-A1, one))

    def higher(cut):
        zx, zy = after(cut)
        if cut[0] == "K":
            return zy
        if cut[0] == "P":
            return zx
        return zy if cut[2] else zx

    n = len(cuts)
    runs = []
    for i in range(n):
        ell = lin((1, cuts[i][1]), (-1, cuts[i - 1][1])) if i > 0 else lin((1, cuts[i][1]))
        g = lin((1, higher(cuts[i - 1])), (-1, ell))
        le(lin((-1, g)))
        runs.append((ell, g))
    tvar = {it: 1.0}
    for i in range(n):
        ell, g = runs[i]
        ell_n, g_n = runs[(i + 1) % n]
        nu = lin((A1, one)) if cuts[i][0] == "K" else {}
        nup = lin((A1, one)) if cuts[i][0] == "P" else {}
        p = lin((1, nu), (1, nup))
        t1 = lin((AL, ell), (1, g))
        for z, cexp in zip(after(cuts[i]), (nup, nu)):
            t2 = lin((1, cexp), (1, ell_n), (1, g_n))
            cost3 = lin((1, g), (1, g_n), (1, p), (1, z))
            cost4 = lin((1, g), (1, g_n), (2, z))
            for main in (t1, t2):
                le(lin((1, main), (-1, cost3), (1, tvar)))
            for main in (t1, t2, lin((1, p), (1, z))):
                le(lin((1, main), (-1, cost4), (1, tvar)))
    A = np.zeros((len(rows), nv))
    b = np.zeros(len(rows))
    for r, (c, rhs) in enumerate(rows):
        b[r] = rhs
        for key, a in c.items():
            if key == "const":
                b[r] -= a
            else:
                A[r, key] += a
    obj = np.zeros(nv)
    obj[it] = -1.0
    res = linprog(obj, A_ub=A, b_ub=b, bounds=[(0, 1)] * (nv - 1) + [(-5, 5)], method="highs")
    if res.status != 0:
        return None
    return round(float(-res.fun), 4), [round(float(v), 4) for v in res.x[:nv - 1]]


def main():
    out = {}
    for s in range(3, 11):
        per_type = {}
        for below in range(0, s - 1):
            r = solve(s, below)
            per_type[f"small mismatches before 1-h: {below}"] = None if r is None else {"largest_t": r[0], "h_and_times": r[1]}
        vals = [v["largest_t"] for v in per_type.values() if v is not None]
        verdict = "empty" if not vals else ("forced" if max(vals) < -1e-9 else "not forced")
        out[f"s={s}"] = {"verdict": verdict, "largest_t": max(vals) if vals else None, "order_types": per_type}
        print(f"s={s}: {verdict}, largest t {max(vals) if vals else None}")
    if "--write-receipt" in sys.argv:
        (HERE / "explore_near_circuit_lp.json").write_text(json.dumps(out, indent=1) + "\n")
        print("receipt written")


if __name__ == "__main__":
    main()
