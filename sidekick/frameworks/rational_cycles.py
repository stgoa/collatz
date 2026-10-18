"""Framework filter: positive rational cycles of the odd-only map S(x) = (3x+1)/2^v2(3x+1).

S is defined on 2-adic integers, so on rationals with odd denominators. A periodic valuation
word W = (v_1..v_k) with m = sum(v) has exactly one 2-adic point following W forever:
    x_W = B_W / (2^m - 3^k),   B_W = sum_i 3^(k-1-i) 2^(v_1+...+v_i).
It is positive iff 2^m > 3^k. The cycle {x_W and its rotations} is a cycle of 3x+d on
integers after multiplying by its reduced denominator d (T_d(d y) = d T_1(y)).

These points are test cases for any proposed global argument. Its key property must fail at
them (they never reach 1), so it cannot depend only on 2-adic or 3-adic residues and size.
This script enumerates primitive words with k <= KMAX and 3^k < 2^m <= 2^(ceil(k log2 3)+EXTRA),
verifies each cycle by exact iteration, and reports the catalogue. Standard library.
"""
from fractions import Fraction
from itertools import product
from math import ceil, log2
from pathlib import Path
import json
import sys

KMAX, EXTRA = 9, 2


def S(x):
    z = 3*x + 1
    v = 0
    while z.numerator % 2 == 0:
        z /= 2
        v += 1
    return z, v


def primitive(word):
    k = len(word)
    return all(word != word[p:] + word[:p] for p in range(1, k) if k % p == 0)


def canonical(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    seen, rows = set(), []
    for k in range(1, KMAX + 1):
        mlo = ceil(k*log2(3) + 1e-12)
        for m in range(mlo, mlo + EXTRA + 1):
            if 2**m <= 3**k:
                continue
            for word in product(range(1, m - k + 2), repeat=k):
                if sum(word) != m or not primitive(word):
                    continue
                cw = canonical(word)
                if cw in seen:
                    continue
                seen.add(cw)
                e, B = 0, 0
                for i, v in enumerate(word):
                    B += 3**(k - 1 - i)*2**e
                    e += v
                x = Fraction(B, 2**m - 3**k)
                pts, y = [], x
                for v in word:
                    pts.append(y)
                    y, vv = S(y)
                    assert vv == v
                assert y == x
                c = min(pts)
                rows.append(dict(k=k, m=m, word=list(cw), minimum=str(c), denominator=c.denominator,
                                 minimum_float=float(c), multiplier=3**k/2**m))
    integral = [r for r in rows if r["denominator"] == 1]
    assert [r["word"] for r in integral] == [[2]], integral
    top = sorted(rows, key=lambda r: -r["minimum_float"])[:12]
    report = dict(scope="Positive rational cycles of 3x+1 (odd-only), primitive words k<=%d, 3^k<2^m<=2^(ceil(k log2 3)+%d)." % (KMAX, EXTRA),
                  cycles=len(rows), integral_cycles=[r["minimum"] for r in integral],
                  largest_minima=[(r["minimum"], round(r["minimum_float"], 2), r["word"]) for r in top],
                  status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(dict(report, catalogue=rows), indent=1) + "\n")
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
