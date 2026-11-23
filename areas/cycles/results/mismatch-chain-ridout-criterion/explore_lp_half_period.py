#!/usr/bin/env python3
"""Exploration for mismatch-chain-ridout-criterion (not a certificate; never run by CI).

Question explored: for a half-period word whose halves differ in d positions, do the elementary size
constraints force one of the chain criteria (patterns (i), (ii) of the node) to hold with a fixed margin?

Model, in variables normalised by the half length N, with the minimum at height 0 and tau = 0:
  b_k >= 0 (block lengths, sum 1), e_k >= 0 (excess of the ordinary total s_k = b_k + e_k of block k),
  eps_k (signed amplitude of the change at the end of block k, second half minus first half), X_0 >= 0.
Heights: X_(k+1) = X_k + alpha b_k - s_k - max(-eps_k, 0), ratio R_k = (sum eps)/2 - eps_0 - ... - eps_(k-1),
Y_k = X_k + R_k. Constraints:
  budget          sum_k (s_k + |eps_k|/2) = alpha;
  positivity      every block-start height is >= 0;
  two-adic        the higher of the two paired block starts is >= s_k;
  three-adic      the state after the block on the higher track, times 2^(its extra letter), is >= 3^(b_k);
  minimum         the block copy containing the minimum has excess e_k >= its start height;
  chains          every chain criterion of pattern (i) or (ii), with cost |delta_0| + D', is violated up to MARGIN.
Each sign pattern of (eps_k), each sign pattern of (R_k) and each admissible block copy for the minimum is one
linear program. A relaxation that is infeasible in every case means: some chain criterion is forced.

This script needs numpy and scipy (a linear-programming solver) and uses floating point. Its output is a count of
feasible cases. It supports no claim of the node; it illustrates where the method applies.

    python3 areas/cycles/results/mismatch-chain-ridout-criterion/explore_lp_half_period.py [--write-receipt]
"""
import itertools
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

ALPHA = float(np.log2(3.0))
HERE = Path(__file__).resolve().parent


def explore(d, margin, slack=1e-6):
    nv = 3 * d + 1

    def ib(k):
        return k

    def ie(k):
        return d + k

    def ieps(k):
        return 2 * d + k

    def vec():
        return np.zeros(nv)

    feasible = total = 0
    for sgn_eps in itertools.product([1, -1], repeat=d):
        def epsvec(k):
            v = vec()
            v[ieps(k)] = 1
            return v

        def pos(k):
            return epsvec(k) if sgn_eps[k] > 0 else vec()

        def neg(k):
            return -epsvec(k) if sgn_eps[k] < 0 else vec()

        def sord(k):
            v = vec()
            v[ib(k)] = 1
            v[ie(k)] = 1
            return v

        def xk(k):
            v = vec()
            v[3 * d] = 1
            for i in range(k):
                v[ib(i)] += ALPHA
                v = v - sord(i) - neg(i)
            return v

        def rk(k):
            v = vec()
            for i in range(d):
                v[ieps(i)] += 0.5
            for i in range(k):
                v[ieps(i)] -= 1
            return v

        def xfull(K):
            K %= 2 * d
            return xk(K) if K < d else xk(K - d) + rk(K - d)

        def epsfull(K):
            K %= 2 * d
            return epsvec(K) if K < d else -epsvec(K - d)

        def sgnfull(K):
            K %= 2 * d
            return sgn_eps[K] if K < d else -sgn_eps[K - d]

        for sgn_r in itertools.product([1, -1], repeat=d):
            for kstar in range(2 * d):
                if sgn_r[kstar % d] * (1 if kstar < d else -1) < 0:
                    continue
                a_ub, b_ub, a_eq, b_eq = [], [], [], []

                def ge(v, c=0.0):
                    a_ub.append(-v)
                    b_ub.append(-c)

                v = vec()
                for i in range(d):
                    v[ib(i)] = 1
                a_eq.append(v)
                b_eq.append(1.0)
                v = vec()
                for i in range(d):
                    v = v + sord(i) + 0.5 * sgn_eps[i] * epsvec(i)
                a_eq.append(v)
                b_eq.append(ALPHA)
                for k in range(d):
                    ge(sgn_eps[k] * epsvec(k), slack)
                    ge(sgn_r[k] * rk(k), 0.0)
                    ge(np.eye(nv)[ib(k)], slack)
                for K in range(2 * d):
                    ge(xfull(K), 0.0)
                for k in range(d):
                    ab = vec()
                    ab[ib(k)] = ALPHA
                    if sgn_r[k] > 0:
                        ge(xfull(k + d) - sord(k), 0.0)
                        ge(xfull(k + 1 + d) + pos(k) - ab, 0.0)
                    else:
                        ge(xfull(k) - sord(k), 0.0)
                        ge(xfull(k + 1) + neg(k) - ab, 0.0)
                v = vec()
                v[ie(kstar % d)] = 1
                ge(v - xfull(kstar), 0.0)
                for k0 in range(2 * d):
                    s0 = sgnfull(k0)
                    ab = vec()
                    ab[ib(k0 % d)] = ALPHA
                    for r in range(0, 2 * d - 1):
                        inner = [k0 + i for i in range(1, r)]
                        if not all(sgnfull(K) > 0 for K in inner):
                            break
                        if s0 < 0 and r == 0:
                            continue
                        cost = s0 * epsfull(k0)
                        for K in inner:
                            cost = cost + epsfull(K)
                        ge(cost + xfull(k0 + r + 1 + d) + xfull(k0 + 1) - ab, -margin)
                res = linprog(np.zeros(nv), A_ub=np.array(a_ub), b_ub=np.array(b_ub), A_eq=np.array(a_eq),
                              b_eq=np.array(b_eq),
                              bounds=[(0, None)] * (2 * d) + [(None, None)] * d + [(0, None)], method="highs")
                total += 1
                if res.status == 0:
                    feasible += 1
    return total, feasible


def main():
    out = {}
    for d in (1, 2, 3):
        for margin in (0.0, 0.03):
            total, feasible = explore(d, margin)
            out[f"defects={d}, margin={margin}"] = {"cases": total, "feasible": feasible}
            print(f"defects = {d}, margin = {margin}: {feasible} of {total} cases feasible with every chain "
                  f"criterion violated")
    if "--write-receipt" in sys.argv:
        (HERE / "explore_lp_half_period.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
        print("receipt written")


if __name__ == "__main__":
    main()
