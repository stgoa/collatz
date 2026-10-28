#!/usr/bin/env python3
"""Certificate for two-marker-constant-background-exact-denominator.

Written at the 2026-10-28 batch (Claude, Fable 5.1). Standard library, exact integers. Run from the
repository root: python3 <this file>. Exits 1 on any failure.

For 1 <= n <= 200 and w_n = (1, 2^(n-1), 3, 2^(n-1)) (m = 2n, A = 4n) it checks:
  - the closed form C_w = 3^(2n-1) + 2*3^(n-1)*(4^n - 3^n) + 4^(n+1)*(4^(n-1) - 3^(n-1)) against the
    definition C_w = sum_j 3^(m-1-j) 2^(s_j);
  - D = 16^n - 9^n, gcd(C_w, D) = 4^n - 3^n and q = D/gcd = 4^n + 3^n;
  - the rotation by n differs from w_n in exactly the two positions 0 and n, and w_n is primitive;
  - the two natural-order arcs between the mismatches both have intercept 4^n - 3^n (the two-defect
    bound (5) is then attained within the factor 3 = 2^k - 1, k = 2).
"""
import sys
from math import gcd


def intercept(w):
    C = s = 0
    m = len(w)
    for j in range(m):
        C += 3 ** (m - 1 - j) << s
        s += w[j]
    return C


def main():
    for n in range(1, 201):
        w = [1] + [2] * (n - 1) + [3] + [2] * (n - 1)
        m = 2 * n
        A = sum(w)
        C = intercept(w)
        closed = 3 ** (2 * n - 1) + 2 * 3 ** (n - 1) * (4 ** n - 3 ** n) + 4 ** (n + 1) * (4 ** (n - 1) - 3 ** (n - 1))
        D = (1 << A) - 3 ** m
        G = gcd(C, D)
        mis = [i for i in range(m) if w[i] != w[(i + n) % m]]
        prim = all(w != w[p:] + w[:p] for p in range(1, m) if m % p == 0)
        arc_u = intercept(w[1:n + 1])          # positions 1..n (ends with the 3)
        arc_v = intercept(w[n + 1:] + w[:1])   # positions n+1..m-1 and 0 (ends with the 1)
        ok = (A == 4 * n and C == closed and D == 16 ** n - 9 ** n and G == 4 ** n - 3 ** n
              and D // G == 4 ** n + 3 ** n and mis == [0, n] and prim
              and arc_u == 4 ** n - 3 ** n and arc_v == 4 ** n - 3 ** n)
        if not ok:
            print(f"FAIL at n={n}: A={A} C==closed:{C == closed} G={G} q={D // G} mis={mis} prim={prim} "
                  f"arcs={arc_u},{arc_v}")
            return 1
    print("PASS: n = 1..200, gcd(C_w, D) = 4^n - 3^n, q = 4^n + 3^n, rotation by n has exactly two mismatches")
    return 0


if __name__ == "__main__":
    sys.exit(main())
