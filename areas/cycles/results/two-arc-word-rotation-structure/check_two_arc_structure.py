#!/usr/bin/env python3
"""Certificate for two-arc-word-rotation-structure (brute force on every two-arc word up to m = 30).

Written at the 2026-10-28 batch (Claude, Fable 5.1). Standard library. Run from the repository root:
python3 <this file>. Exits 1 on any failure. About ten seconds.

For every m <= 30, every h coprime to m (alpha = h^(-1) mod m), every arc length t1 in 1..m-1 (t2 = m - t1)
and letters (a, b) in a fixed list, the word w_j = a if j*alpha mod m < t1 else b is built and checked:
  (i)   s(r) = 2 * min(||r*alpha||_m, t1, t2) for every rotation r (||.||_m the cyclic distance to 0);
  (ii)  the mismatches of h are the natural positions (t1 - 1) h and -h (mod m), at natural distance
        ell = t1 h mod m, and s(r h) = 2 r for 1 <= r <= min(t1, t2);
  (iii) if min(t1, t2) >= 2: [the two mismatches of h are adjacent]  <=>  [t1 = +-h^(-1) mod m]
        <=>  [the binary mask is a mechanical word], and in that case gcd(C_w, D) | 2^|b-a| - 1 when D > 0;
  (iv)  if min(t1, t2) = 1: every rotation has exactly two mismatches and the mask is mechanical.
"""
import sys
from math import gcd

LETTERS = ((1, 2), (1, 3), (2, 1), (3, 1), (2, 4), (1, 5))


def intercept(w):
    C = s = 0
    m = len(w)
    for j in range(m):
        C += 3 ** (m - 1 - j) << s
        s += w[j]
    return C, s


def mechanical(mask):
    m, t = len(mask), sum(mask)
    return any(all(mask[j] == ((j + 1) * t + phi) // m - (j * t + phi) // m for j in range(m)) for phi in range(m))


def main():
    tested = sturmian = singles = 0
    for m in range(3, 31):
        for h in range(1, m):
            if gcd(h, m) != 1:
                continue
            alpha = pow(h, -1, m)
            for t1 in range(1, m):
                t2 = m - t1
                for a, b in LETTERS:
                    w = [a if (j * alpha) % m < t1 else b for j in range(m)]
                    tested += 1

                    def s(r):
                        return sum(1 for i in range(m) if w[i] != w[(i + r) % m])

                    for r in range(1, m):
                        d = (r * alpha) % m
                        if s(r) != 2 * min(d, m - d, t1, t2):
                            return fail("(i)", m, h, t1, a, b, r)
                    mis = sorted(i for i in range(m) if w[i] != w[(i + h) % m])
                    if mis != sorted({((t1 - 1) * h) % m, (-h) % m}):
                        return fail("(ii) positions", m, h, t1, a, b, mis)
                    for r in range(1, min(t1, t2) + 1):
                        if s((r * h) % m) != 2 * r:
                            return fail("(ii) multiples", m, h, t1, a, b, r)
                    ell = (t1 * h) % m
                    mask = [1 if x == b else 0 for x in w]
                    mech = mechanical(mask)
                    if min(t1, t2) >= 2:
                        adjacent = ell in (1, m - 1)
                        sturm = t1 % m in (alpha, (m - alpha) % m)
                        if not (adjacent == sturm == mech):
                            return fail("(iii) equivalence", m, h, t1, a, b, adjacent, sturm, mech)
                        if adjacent:
                            sturmian += 1
                            C, A = intercept(w)
                            D = (1 << A) - 3 ** m
                            if D > 0 and (2 ** abs(b - a) - 1) % gcd(C, D):
                                return fail("(iii) divisibility", m, h, t1, a, b, gcd(C, D))
                    else:
                        singles += 1
                        if not mech or any(s(r) != 2 for r in range(1, m)):
                            return fail("(iv)", m, h, t1, a, b)
    print(f"PASS: {tested} two-arc words (m <= 30, 6 letter pairs), {sturmian} Sturmian with min arc >= 2, "
          f"{singles} with a single distinguished letter; (i)-(iv) hold throughout")
    return 0


def fail(what, *info):
    print("FAIL", what, info)
    return 1


if __name__ == "__main__":
    sys.exit(main())
