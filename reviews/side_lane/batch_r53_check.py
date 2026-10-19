"""Sidekick probe: independent check of R53's delayed-exit family (main 8764158, Sections 3-5).

For r = 1..6, d = 4r+3, and the CRT progression (12) for s (first 3 positive members):
  w = (2^(3r+8) s - 11)/9 is in W5, w = 13 mod 32, w = 45 mod 81, 3w non-selected, q = 3w;
  the ordinary word from q is (1,1,2) to x0 = 9*2^(3r+4) s - 5, then (1,2)^r to
  xr = 16*9^(r+1) s - 5, with every boundary = 1 mod 3 and > q;
  at xr: a = v2(xr+1) = 2 and d = v2(3t - 1) = 4r+3 for t = (xr+1)/4;
  with b = floor(d/2), y = 3^b (3^(2r+3) s - 1)/2^(d-2) satisfies T^(a+b-1)(xr) = nu(y)
  (T = nu o S on this branch's own nu/step) and (9y+5)/8 < q.
Also: G(x) = (9x+5)/8 equals S^2 with valuations (1,2) on x = 27 mod 32, and the maximal
number of consecutive such steps from x is floor((v2(x+5)-2)/3).
Standard library. Run without -O.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402
from fibre_count_check import nu, selected  # noqa: E402


def v2(n):
    return (n & -n).bit_length() - 1


def walk(x, word):
    for v in word:
        assert valuation(1, x) == v, (x, v)
        x = step(1, x)
    return x


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    T = lambda y: nu(step(1, y))
    members = 0
    for r in range(1, 7):
        d = 4*r + 3
        m2, m3 = 2**(d - 1), 729
        s2 = pow(3, -(2*r + 3), m2)*(1 + 2**(d - 2)) % m2
        s3 = 416*pow(2, -(3*r + 8), m3) % m3
        s0 = (s2*m3*pow(m3, -1, m2) + s3*m2*pow(m2, -1, m3)) % (m2*m3)
        for k in range(3):
            s = s0 + k*m2*m3
            num = 2**(3*r + 8)*s - 11
            assert num % 9 == 0
            w = num//9
            q = 3*w
            assert w % 8 == 5 and w % 32 == 13 and w % 81 == 45 and not selected(q)
            x0 = 9*2**(3*r + 4)*s - 5
            xr = 16*9**(r + 1)*s - 5
            assert walk(q, (1, 1, 2)) == x0
            x = x0
            for _ in range(r):
                assert x % 3 == 1 and x > q and x % 32 == 27
                x = walk(x, (1, 2))
            assert x == xr and xr % 3 == 1 and xr > q
            a = v2(xr + 1)
            t = (xr + 1) >> a
            assert a == 2 and v2(3*t - 1) == d
            b = d//2
            y = 3**b*(3**(2*r + 3)*s - 1)//2**(d - 2)
            z = xr
            for _ in range(a + b - 1):
                z = T(z)
            assert z == nu(y) and 9*y + 5 < 8*q
            members += 1
    runs = 0
    for x in range(27, 27 + 32*4000, 32):
        assert step(1, step(1, x)) == (9*x + 5)//8 and valuation(1, x) == 1
        j, y = 0, x
        while y % 32 == 27:
            y, j = (9*y + 5)//8, j + 1
        assert j == (v2(x + 5) - 2)//3
        runs += 1
    report = dict(scope="Independent finite checks of R53 Sections 3-5 (main 8764158).",
                  delayed_family_members=members, low_run_starts=runs, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
