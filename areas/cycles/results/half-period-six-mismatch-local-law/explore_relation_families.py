#!/usr/bin/env python3
"""Exploration for half-period-six-mismatch-local-law (not a certificate; never run by CI).

Question explored: which families of exact relations force a small S-free product for a half-period word with
d changed positions? The model is the normalised one (everything divided by N, subexponential factors dropped,
minimum at height 0), so its numbers are indicative only. The certificate of the node proves the case d <= 3
of the family "basic" with explicit error terms and exact arithmetic.

Variables: b_k (block lengths, sum 1), e_k >= 0 (common total s_k = b_k + e_k), eps_k (signed change at the end
of block k, second half minus first half), X0, G_k = log|g_k| >= 0, dip_k in [0, e_k] (depth of the lowest state
of block k below its start). Cycle index K in Z/2d: Z_K is the height before block K of the cycle, ex(K) the
extra final letter of that block copy, Z_(K+1) = Z_K + alpha b_K - s_K - ex(K).

Relation families (K a mismatch, r >= 0 further blocks):
  basic3   3^B g_K = (2^nu' - 2^nu) xi + 2^c g_(K+1), three terms (xi either state after the mismatch);
  basic4   the same relation with the two terms 2^nu' xi and 2^nu xi kept apart, four terms;
  chain3   2^(..) U = 3^(B+n) g_K + [2^ex C + 3^n 2^ex z], U a state r >= 1 blocks later on the shifted track,
           C the intercept of that track segment, the bracket taken as one term;
  chain4   the same with the two terms of the bracket kept apart;
  gg       3^(B+n) g_K - 2^(..) g_(K+r+1) = (2^Ax - 2^Ay) U + 2^ex C_y - 2^ex C_x for r >= 1, right side as one
           term, with the alternative that the right side vanishes.
For each sign case the programme maximises t such that EVERY relation of the chosen families has
(sum of logs of its S-free parts) >= (log of its largest term) + t. A negative maximum in every case means that
some relation is forced to have a small S-free product, with margin |t| N bits in this model.

The minimum is placed in the first block of the first half; rotating by whole blocks permutes the cases.
Needs numpy and scipy (HiGHS). HiGHS presolve returned an infeasible point as "optimal" on one of these
programmes when variables were unbounded above; the variables are therefore boxed and every returned point is
re-checked against all rows.

    python3 areas/cycles/results/half-period-six-mismatch-local-law/explore_relation_families.py [--write-receipt]
"""
import itertools
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

ALPHA = float(np.log2(3.0))
BIGM = 30.0
HERE = Path(__file__).resolve().parent


def lin(*pairs):
    out = {}
    for c, v in pairs:
        for k, a in v.items():
            out[k] = out.get(k, 0.0) + c * a
    return out


def solve_case(d, sgn_eps, sgn_r, families, time_limit):
    ib = lambda k: k % d
    ie = lambda k: d + k % d
    ieps = lambda k: 2 * d + k % d
    ix0 = 3 * d
    ig = lambda k: 3 * d + 1 + k % d
    idip = lambda k: 4 * d + 1 + k % d
    it = 5 * d + 1
    ncont = 5 * d + 2
    rows = []
    nbin = [0]

    def newbin():
        nbin[0] += 1
        return ncont + nbin[0] - 1

    var = lambda i: {i: 1.0}
    B = lambda k: var(ib(k))
    E = lambda k: var(ie(k))
    S = lambda k: lin((1, B(k)), (1, E(k)))
    eps = lambda k: var(ieps(k))
    pos = lambda k: eps(k) if sgn_eps[k % d] > 0 else {}
    neg = lambda k: lin((-1, eps(k))) if sgn_eps[k % d] < 0 else {}
    G = lambda k: var(ig(k))
    dip = lambda k: var(idip(k))
    tvar = var(it)

    def ex(K):
        K %= 2 * d
        return neg(K) if K < d else pos(K - d)

    def Z(K):
        K %= 2 * d
        v = dict(var(ix0))
        for i in range(K):
            v = lin((1, v), (ALPHA, B(i)), (-1, S(i)), (-1, ex(i)))
        return v

    def ge(expr, c=0.0):
        rows.append((expr, c, np.inf))

    def eq(expr, c=0.0):
        rows.append((expr, c, c))

    eq(lin(*[(1, B(k)) for k in range(d)]), 1.0)
    eq(lin(*[(1, S(k)) for k in range(d)], *[(0.5 * sgn_eps[k], eps(k)) for k in range(d)]), ALPHA)
    for k in range(d):
        ge(lin((sgn_eps[k], eps(k))))
        ge(lin((sgn_r[k], Z(k + d)), (-sgn_r[k], Z(k))))
        ge(lin((1, E(k)), (-1, dip(k))))
        hi = Z(k + d) if sgn_r[k] > 0 else Z(k)
        ge(lin((1, hi), (-1, S(k)), (-1, G(k))))
    for K in range(2 * d):
        ge(lin((1, Z(K)), (-1, dip(K))))
    eq(lin((1, Z(0)), (-1, dip(0))))

    def violate(small, thetas, mains, alternative=None):
        zs = []
        for th in thetas:
            z = newbin()
            zs.append(z)
            for mt in mains:
                ge(lin((1, small), (1, th), (-1, mt), (-1, tvar), (-BIGM, {z: 1.0})), -BIGM)
        if alternative is not None:
            z = newbin()
            zs.append(z)
            for expr in alternative:
                ge(lin((1, expr), (-BIGM, {z: 1.0})), -BIGM)
        rows.append(({z: 1.0 for z in zs}, 1.0, np.inf))

    rmax = 2 * d - 1
    for K in range(2 * d):
        a_k = lin((ALPHA, B(K)))
        for r in range(0, rmax + 1):
            n = lin(*[(ALPHA, B(K + i)) for i in range(1, r + 1)])
            sig_y = lin(*[(1, S(K + i)) for i in range(1, r + 1)], *[(1, ex(K + d + i)) for i in range(1, r + 1)])
            sig_x = lin(*[(1, S(K + i)) for i in range(1, r + 1)], *[(1, ex(K + i)) for i in range(1, r + 1)])
            c_y = [lin((1, n), (1, Z(K + d + 1)), (-1, Z(K + d + i)), (1, dip(K + i))) for i in range(1, r + 1)]
            c_x = [lin((1, n), (1, Z(K + 1)), (-1, Z(K + i)), (1, dip(K + i))) for i in range(1, r + 1)]
            if r >= 1 and ("chain3" in families or "chain4" in families):
                U = Z(K + d + r + 1)
                mains = [lin((1, a_k), (1, n), (1, G(K))), lin((1, ex(K + d)), (1, sig_y), (1, U))]
                if "chain3" in families:
                    thetas = [lin((1, n), (1, ex(K)), (1, Z(K + 1)))] + [lin((1, ex(K + d)), (1, c)) for c in c_y]
                    violate(lin((1, U), (1, G(K))), thetas, mains)
                if "chain4" in families:
                    violate(lin((1, U), (1, G(K)), (1, Z(K + 1))), c_y,
                            mains + [lin((1, n), (1, ex(K)), (1, Z(K + 1)))])
            if K >= d:
                continue
            a_x = lin((1, ex(K)), (1, sig_x))
            a_y = lin((1, ex(K + d)), (1, sig_y))
            s_next = S(K + r + 1)
            g_next = G(K + r + 1)
            small = lin((1, G(K)), (1, g_next))
            for (U, a_main) in ((Z(K + r + 1), a_y), (Z(K + d + r + 1), a_x)):
                mains = [lin((1, a_k), (1, n), (1, G(K))), lin((1, a_main), (1, s_next), (1, g_next))]
                if r == 0:
                    if "basic3" in families:
                        violate(small, [lin((1, a_x), (1, U)), lin((1, a_y), (1, U))], mains)
                    if "basic4" in families:
                        violate(lin((1, small), (2, U)), [{}],
                                mains + [lin((1, a_x), (1, U)), lin((1, a_y), (1, U))])
                elif "gg" in families:
                    thetas = [lin((1, a_x), (1, U)), lin((1, a_y), (1, U))]
                    thetas += [lin((1, ex(K + d)), (1, c)) for c in c_y] + [lin((1, ex(K)), (1, c)) for c in c_x]
                    vanish = [lin((1, G(K)), (-1, a_main), (-1, s_next)), lin((1, g_next), (-1, a_k), (-1, n))]
                    violate(small, thetas, mains, alternative=vanish)

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
    up_b = np.full(nvar, 10.0)
    for k in range(d):
        lo_b[ieps(k)] = -10.0
    lo_b[it] = -5.0
    up_b[it] = 5.0
    up_b[ncont:] = 1.0
    integrality = np.zeros(nvar)
    integrality[ncont:] = 1
    for presolve in (True, False):
        res = milp(c, constraints=LinearConstraint(A, lb, ub), integrality=integrality, bounds=Bounds(lo_b, up_b),
                   options={"time_limit": time_limit, "presolve": presolve})
        if res.x is None:
            return None if res.status == 2 else "unsolved"
        x = res.x
        slack = min((x - lo_b).min(), (up_b - x).min(), (A @ x - lb).min(), (ub - A @ x).min())
        if res.status == 0 and slack > -1e-6:
            return float(x[it])
    return "unsolved"


def explore(d, families, time_limit=120):
    best = None
    nonempty = unsolved = 0
    for sgn_eps in itertools.product([1, -1], repeat=d):
        for sgn_r in itertools.product([1, -1], repeat=d):
            t = solve_case(d, sgn_eps, sgn_r, families, time_limit)
            if t == "unsolved":
                unsolved += 1
            elif t is not None:
                nonempty += 1
                best = t if best is None else max(best, t)
    return {"sign_cases": 4 ** d, "cases_with_a_point": nonempty, "unsolved": unsolved,
            "largest_t": None if best is None else round(best, 4),
            "forced": bool(best is not None and best < -1e-6 and unsolved == 0)}


def main():
    plan = [
        (2, ["basic3"]), (2, ["basic3", "basic4"]),
        (3, ["basic3"]), (3, ["basic3", "basic4"]), (3, ["basic3", "chain3", "gg"]),
        (3, ["basic3", "basic4", "chain3", "chain4", "gg"]),
        (4, ["basic3", "basic4"]), (4, ["basic3", "basic4", "chain3", "chain4", "gg"]),
    ]
    out = {}
    for d, families in plan:
        res = explore(d, families)
        key = f"d={d}: " + "+".join(families)
        out[key] = res
        print(key, res, flush=True)
    if "--write-receipt" in sys.argv:
        (HERE / "explore_relation_families.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
        print("receipt written")


if __name__ == "__main__":
    main()
