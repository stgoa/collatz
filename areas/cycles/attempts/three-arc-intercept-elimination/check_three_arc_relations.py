#!/usr/bin/env python3
"""Certificate for three-arc-intercept-elimination: the two-term relations and the vacuous determinant.

Written at the 2026-10-28 batch (Claude, Fable 5.1). Standard library, exact rational arithmetic. Run from
the repository root: python3 <this file>. Exits 1 on any failure. About twenty seconds.

For every primitive three-arc word (coprime track step, all cuts, letters 1..3, m <= 16) with D > 0, with
mismatches e1 < e2 < e3 of the rotation h, signed differences d_r = a_(e_r + h) - a_(e_r), arcs
alpha = (e1, e2], beta = (e2, e3], gamma = (e3, e1 + m] and their intercepts C_alpha, C_beta, C_gamma:
  (1) C_(w') - C_w = 3^(m-1-e3) * 2^(s_(e1+1)) * Xi_1 with
      Xi_1 = (2^d1 - 1) 3^(l_beta) C_alpha + (2^(d1+d2) - 1) 2^(S_alpha) C_beta   (exact rationals);
  (2) G = gcd(C_w, D) divides the numerator of Xi_1 (G is odd), and Xi_1 != 0;
  (3) the cyclic 3x3 system of these relations has determinant -(2^d1 - 1)(2^d2 - 1)(2^d3 - 1) * D.
"""
import itertools
import sys
from fractions import Fraction as F
from math import gcd


def intercept(letters):
    C = s = 0
    for i, a in enumerate(letters):
        C += 3 ** (len(letters) - 1 - i) << s
        s += a
    return C, s


def primitive(w):
    m = len(w)
    return all(w != w[p:] + w[:p] for p in range(1, m) if m % p == 0)


def main():
    checked = 0
    for m in range(4, 17):
        for h in range(1, m):
            if gcd(h, m) != 1:
                continue
            hinv = pow(h, -1, m)
            for cuts in itertools.combinations(range(1, m), 2):
                bounds = (0,) + cuts + (m,)
                for vals in itertools.product((1, 2, 3), repeat=3):
                    if vals[0] == vals[1] or vals[1] == vals[2] or vals[2] == vals[0]:
                        continue
                    track = [vals[0]] * (bounds[1]) + [vals[1]] * (bounds[2] - bounds[1]) + [vals[2]] * (m - bounds[2])
                    w = [track[(j * hinv) % m] for j in range(m)]
                    if not primitive(w):
                        continue
                    C, A = intercept(w)
                    D = (1 << A) - 3 ** m
                    if D <= 0:
                        continue
                    G = gcd(C, D)
                    wp = [w[(j + h) % m] for j in range(m)]
                    Cp, _ = intercept(wp)
                    E = [i for i in range(m) if w[i] != w[(i + h) % m]]
                    if len(E) != 3:
                        return fail("mismatch count", m, h, bounds, vals, E)
                    e1, e2, e3 = E
                    d = [w[(e + h) % m] - w[e] for e in E]
                    if sum(d) != 0:
                        return fail("differences", m, h, bounds, vals, d)
                    s = [0] * (m + 1)
                    for j in range(m):
                        s[j + 1] = s[j] + w[j]
                    alpha, beta, gamma = w[e1 + 1:e2 + 1], w[e2 + 1:e3 + 1], w[e3 + 1:] + w[:e1 + 1]
                    Ca, Cb, Cg = intercept(alpha)[0], intercept(beta)[0], intercept(gamma)[0]
                    la, lb, lg = len(alpha), len(beta), len(gamma)
                    Sa, Sb, Sg = sum(alpha), sum(beta), sum(gamma)
                    if la + lb + lg != m or Sa + Sb + Sg != A:
                        return fail("arcs", m, h, bounds, vals)
                    xi1 = (F(2) ** d[0] - 1) * 3 ** lb * Ca + (F(2) ** (d[0] + d[1]) - 1) * 2 ** Sa * Cb
                    if F(Cp - C) != F(3) ** (m - 1 - e3) * F(2) ** s[e1 + 1] * xi1:
                        return fail("(1)", m, h, bounds, vals)
                    if xi1 == 0 or xi1.numerator % G:
                        return fail("(2)", m, h, bounds, vals, xi1, G)
                    M = [[(F(2) ** d[0] - 1) * 3 ** lb, (F(2) ** (-d[2]) - 1) * 2 ** Sa, 0],
                         [0, (F(2) ** d[1] - 1) * 3 ** lg, (F(2) ** (-d[0]) - 1) * 2 ** Sb],
                         [(F(2) ** (-d[1]) - 1) * 2 ** Sg, 0, (F(2) ** d[2] - 1) * 3 ** la]]
                    det = (M[0][0] * M[1][1] * M[2][2] + M[0][1] * M[1][2] * M[2][0] + M[0][2] * M[1][0] * M[2][1]
                           - M[0][2] * M[1][1] * M[2][0] - M[0][1] * M[1][0] * M[2][2] - M[0][0] * M[1][2] * M[2][1])
                    if det != -(F(2) ** d[0] - 1) * (F(2) ** d[1] - 1) * (F(2) ** d[2] - 1) * D:
                        return fail("(3)", m, h, bounds, vals, det)
                    checked += 1
    print(f"PASS: {checked} primitive three-arc words (m <= 16, letters 1-3): relation (1), divisibility (2) with "
          f"Xi_1 != 0, and the determinant identity (3) hold throughout")
    return 0


def fail(what, *info):
    print("FAIL", what, info)
    return 1


if __name__ == "__main__":
    sys.exit(main())
