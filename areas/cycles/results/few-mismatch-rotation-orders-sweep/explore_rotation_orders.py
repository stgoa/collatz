#!/usr/bin/env python3
"""Exploration for few-mismatch-rotation-orders-sweep (not a certificate; never run by CI).

Rotations of order M with few mismatches, in a normalised linear model. Needs numpy and scipy (HiGHS),
floating point. It supports no proved claim.

The word is M copies of a base period, read in time order. A period is cut into d blocks; the last letter of
block k in copy j exceeds the smallest of the M last letters by lam[j][k] >= 0. A pattern fixes, for every
block, the weak ordering of these M excesses (rank 0 means excess 0, equal ranks mean equal letters). The
hypothesised rotation shifts the copies by h, gcd(h, M) = 1; its mismatches are the block ends where the
ranks of copies j and j + h differ.

Unknowns, per unit of period length: block lengths b_k (sum 1), common totals s_k = b_k + e_k, the excesses,
the height Z_K = log2(state)/P before each of the M d block copies, and G = log2|g| for the paired quotient of
every maximal agreeing run of every shift t <= M/2.

Rows: the valuation budget; Z_K >= 0; a minimum in the first block copy (Z_0 <= e_0); for every shift t and
every agreeing run, G + (2-adic total of the run) <= the higher of its two starting heights.

Relations: at every mismatch of every shift, the two relations between consecutive quotients,
3^n g = (2^nu' - 2^nu) xi + 2^c g', in three-term and four-term form (as in half-period-six-mismatch-local-law).
The programme maximises t such that every relation has (sum of logs of S-free parts) >= (log of its largest
term) + t. Outcomes for a pattern:
  empty   the rows alone are contradictory;
  forced  the maximum is negative: some relation has a small S-free product;
  free    the maximum is nonnegative: nothing is forced by these relations;
  invariant  some shift fixes the pattern (the true order is smaller).

    python3 areas/cycles/results/few-mismatch-rotation-orders-sweep/explore_rotation_orders.py --run M s [h]
    python3 areas/cycles/results/few-mismatch-rotation-orders-sweep/explore_rotation_orders.py --run M s [h] --write-receipt

With --write-receipt the entries are merged into explore_rotation_orders.json.
With --rotation-only the rows and the relations are those of the hypothesised rotation alone, not of its
multiples; such entries are stored with the suffix "rotation only".
"""
import itertools
import json
import sys
from math import gcd
from pathlib import Path

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

ALPHA = float(np.log2(3.0))
BIGM = 40.0
HERE = Path(__file__).resolve().parent


def lin(*pairs):
    out = {}
    for c, v in pairs:
        for k, a in v.items():
            out[k] = out.get(k, 0.0) + c * a
    return out


def weak_orderings(M):
    out = set()
    for tup in itertools.product(range(M), repeat=M):
        used = sorted(set(tup))
        if used == list(range(len(used))):
            out.add(tup)
    return sorted(out)


def changes(rank, t):
    M = len(rank)
    return sum(1 for j in range(M) if rank[j] != rank[(j + t) % M])


def compositions(s, parts_min=2):
    if s == 0:
        yield []
        return
    for first in range(parts_min, s + 1):
        for rest in compositions(s - first, parts_min):
            yield [first] + rest


def solve(M, ranks, time_limit=60, only_shift=None):
    d = len(ranks)
    n_k = M * d
    shifts = list(range(1, M // 2 + 1)) if only_shift is None else [only_shift]
    idx = {}

    def new(name):
        idx[name] = len(idx)
        return idx[name]

    for k in range(d):
        new(("b", k))
    for k in range(d):
        new(("e", k))
    for k in range(d):
        for r in range(1, max(ranks[k]) + 1):
            new(("inc", k, r))
    new("Z0")
    var = lambda name: {idx[name]: 1.0}
    B = lambda K: var(("b", K % d))
    E = lambda K: var(("e", K % d))
    S = lambda K: lin((1, B(K)), (1, E(K)))

    def lam(K):
        K %= n_k
        j, k = divmod(K, d)
        return lin(*[(1, var(("inc", k, r))) for r in range(1, ranks[k][j] + 1)])

    def rk(K):
        K %= n_k
        j, k = divmod(K, d)
        return ranks[k][j]

    def Z(K):
        K %= n_k
        v = dict(var("Z0"))
        for i in range(K):
            v = lin((1, v), (ALPHA, B(i)), (-1, S(i)), (-1, lam(i)))
        return v

    rows = []

    def ge(expr, c=0.0):
        rows.append((expr, c, np.inf))

    def eq(expr, c=0.0):
        rows.append((expr, c, c))

    eq(lin(*[(1, B(k)) for k in range(d)]), 1.0)
    eq(lin(*[(M, S(k)) for k in range(d)], *[(1, lam(K)) for K in range(n_k)]), M * ALPHA)
    for K in range(n_k):
        ge(Z(K))
    ge(lin((1, E(0)), (-1, Z(0))))
    runs = {}
    gvar = {}
    for t in shifts:
        mism = [K for K in range(n_k) if rk(K) != rk(K + t * d)]
        if not mism:
            return "invariant", None
        for a in range(len(mism)):
            k1 = mism[a]
            k0 = (mism[a - 1] + 1) % n_k
            blocks = [(k0 + i) % n_k for i in range((k1 - k0) % n_k + 1)]
            if rk(k1) > rk(k1 + t * d):
                minlam, nu, nup = lam(k1 + t * d), lin((1, lam(k1)), (-1, lam(k1 + t * d))), {}
            else:
                minlam, nu, nup = lam(k1), {}, lin((1, lam(k1 + t * d)), (-1, lam(k1)))
            total = lin(*[(1, S(K)) for K in blocks], *[(1, lam(K)) for K in blocks[:-1]], (1, minlam))
            length = lin(*[(ALPHA, B(K)) for K in blocks])
            gvar[(t, a)] = new(("G", t, a))
            runs[(t, a)] = dict(k0=k0, k1=k1, S=total, n=length, nu=nu, nup=nup, p=lin((1, nu), (1, nup)))
    it = new("t")
    ncont = len(idx)
    nbin = [0]

    def newbin():
        nbin[0] += 1
        return ncont + nbin[0] - 1

    tvar = {it: 1.0}
    for (t, a), info in runs.items():
        G = {gvar[(t, a)]: 1.0}
        z = newbin()
        ge(lin((1, Z(info["k0"])), (-1, G), (-1, info["S"]), (BIGM, {z: 1.0})))
        ge(lin((1, Z(info["k0"] + t * d)), (-1, G), (-1, info["S"]), (-BIGM, {z: 1.0})), -BIGM)
    for t in shifts:
        count = len([1 for (tt, a) in runs if tt == t])
        for a in range(count):
            info = runs[(t, a)]
            nxt = runs[(t, (a + 1) % count)]
            G = {gvar[(t, a)]: 1.0}
            Gn = {gvar[(t, (a + 1) % count)]: 1.0}
            k1 = info["k1"]
            for (U, cexp) in ((Z(k1 + 1), info["nup"]), (Z(k1 + 1 + t * d), info["nu"])):
                mains = [lin((1, info["n"]), (1, G)), lin((1, cexp), (1, nxt["S"]), (1, Gn))]
                cost3 = lin((1, G), (1, Gn), (1, info["p"]), (1, U))
                for mt in mains:
                    ge(lin((1, cost3), (-1, mt), (-1, tvar)))
                cost4 = lin((1, G), (1, Gn), (2, U))
                for mt in mains + [lin((1, info["p"]), (1, U))]:
                    ge(lin((1, cost4), (-1, mt), (-1, tvar)))
    nvar = ncont + nbin[0]
    A = np.zeros((len(rows), nvar))
    lb = np.zeros(len(rows))
    ub = np.zeros(len(rows))
    for i, (coef, lo, up) in enumerate(rows):
        for k, a in coef.items():
            A[i, k] += a
        lb[i] = lo
        ub[i] = up
    c = np.zeros(nvar)
    c[it] = -1.0
    lo_b = np.zeros(nvar)
    up_b = np.full(nvar, 12.0)
    lo_b[it] = -6.0
    up_b[it] = 6.0
    up_b[ncont:] = 1.0
    integ = np.zeros(nvar)
    integ[ncont:] = 1
    for presolve in (True, False):
        res = milp(c, constraints=LinearConstraint(A, lb, ub), integrality=integ, bounds=Bounds(lo_b, up_b),
                   options={"time_limit": time_limit, "presolve": presolve})
        if res.x is None:
            return ("empty", None) if res.status == 2 else ("unsolved", None)
        x = res.x
        slack = min((x - lo_b).min(), (up_b - x).min(), (A @ x - lb).min(), (ub - A @ x).min())
        if res.status == 0 and slack > -1e-6:
            tval = float(x[it])
            return ("forced" if tval < -1e-6 else "free"), tval
    return "unsolved", None


def sweep(M, s, only_h=None, rotation_only=False):
    out = {}
    orderings = weak_orderings(M)
    for h in range(1, M // 2 + 1):
        if gcd(h, M) != 1 or (only_h is not None and h != only_h):
            continue
        by_changes = {}
        for r in orderings:
            c = changes(r, h)
            if c > 0:
                by_changes.setdefault(c, []).append(r)
        counts = {"empty": 0, "forced": 0, "free": 0, "invariant": 0, "unsolved": 0}
        weakest = largest = None
        cases = 0
        for comp in compositions(s):
            pools = [by_changes.get(c, []) for c in comp]
            if any(len(p) == 0 for p in pools):
                continue
            for ranks in itertools.product(*pools):
                cases += 1
                status, t = solve(M, list(ranks), only_shift=h if rotation_only else None)
                counts[status] += 1
                if status == "forced":
                    weakest = t if weakest is None else max(weakest, t)
                if status == "free":
                    largest = t if largest is None else max(largest, t)
        entry = dict(counts, patterns=cases,
                     weakest_forced=None if weakest is None else round(weakest, 3),
                     largest_free=None if largest is None else round(largest, 3))
        name = f"M={M} h={h} s={s}" + (" rotation only" if rotation_only else "")
        out[name] = entry
        print(f"{name}: {entry}", flush=True)
    return out


def main():
    if "--run" not in sys.argv:
        print(__doc__)
        return
    i = sys.argv.index("--run")
    args = [a for a in sys.argv[i + 1:] if not a.startswith("--")]
    M, s = int(args[0]), int(args[1])
    only_h = int(args[2]) if len(args) > 2 else None
    out = sweep(M, s, only_h, rotation_only="--rotation-only" in sys.argv)
    if "--write-receipt" in sys.argv:
        path = HERE / "explore_rotation_orders.json"
        data = json.loads(path.read_text()) if path.exists() else {}
        data.update(out)
        key = lambda k: [int(part.split("=")[1]) for part in k.split()[:3]]
        ordered = {k: data[k] for k in sorted(data, key=lambda k: ("rotation only" in k, key(k)[2], key(k)[0], key(k)[1]))}
        path.write_text(json.dumps(ordered, indent=1) + "\n")
        print("receipt updated")


if __name__ == "__main__":
    main()
