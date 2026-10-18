"""Sidekick probe: independent check of R57's descending exit family (main working copy, 23:30).

For r = 0..4, odd d in {2r+5, 2r+7, 2r+9}, and the first 3 positive odd s in progression (7):
  q = 81*2^(11r+12) s - 17, w = (2q+1)/3: w = 3445 mod 3456 and nu(3w) = q;
  v2(q+17) = 11r+12; each of the r guarded copies is the ordinary word (1,1,1,2,1,1,4)
  with S^7(x) = Psi(x) = (2187x+2363)/2048, and T^7 gives the same point;
  exit: Y = S^4(Q), V = nu(Y) = 3^(7r+8)*64 s - 21, a(V) = 2, v2(3t-1) = d (t = (V+1)/4);
  f = 3^b (3^(7r+9) s - 1)/2^(d-4), b = (d-1)/2, equals 3^b (3t-1)/2^d;
  T^(7r+b+5)(q) = nu(f); S^(7r+b+6)(q) = S(f); (9f+5)/8 < q.
Also the avoid-inverse subprogression (16): v = (32q-23)/81 = 0 mod 3.
Uses this branch's own nu/step only. Standard library. Run without -O.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402
from fibre_count_check import nu  # noqa: E402


def v2(n):
    return (n & -n).bit_length() - 1


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    T = lambda y: nu(step(1, y))
    Psi = lambda x: (2187*x + 2363)//2048
    n_members = n_avoid = 0
    for r in range(0, 5):
        for d in (2*r + 5, 2*r + 7, 2*r + 9):
            m = 2**(d - 3)
            s0 = pow(3, -(7*r + 9), m)*(1 + 2**(d - 4)) % m
            members = [s0 + k*m for k in range(3)]
            for s in members:
                assert s % 2 == 1
                q = 81*2**(11*r + 12)*s - 17
                w = (2*q + 1)//3
                assert 3*w == 2*q + 1 and w % 3456 == 3445 and nu(3*w) == q
                assert v2(q + 17) == 11*r + 12
                x = q
                for _ in range(r):
                    y = x
                    for a in (1, 1, 1, 2, 1, 1, 4):
                        assert valuation(1, y) == a
                        y = step(1, y)
                    z = x
                    for _ in range(7):
                        z = T(z)
                    assert y == z == Psi(x)
                    x = y
                Q = x
                Y = Q
                for _ in range(4):
                    Y = step(1, Y)
                V = nu(Y)
                assert V == 3**(7*r + 8)*64*s - 21 and v2(V + 1) == 2
                t = (V + 1)//4
                assert v2(3*t - 1) == d
                b = (d - 1)//2
                f = 3**b*(3**(7*r + 9)*s - 1)//2**(d - 4)
                assert f == 3**b*((3*t - 1) >> d)
                z = q
                for _ in range(7*r + b + 5):
                    z = T(z)
                assert z == nu(f)
                z = q
                for _ in range(7*r + b + 6):
                    z = step(1, z)
                assert z == step(1, f) and 9*f + 5 < 8*q
                n_members += 1
                if (2**(11*r + 17)*s) % 3 == 1:
                    assert ((32*q - 23)//81) % 3 == 0
                    n_avoid += 1
    report = dict(scope="Independent finite checks of R57 Sections 1-3 (main working copy at 23:30).",
                  family_members=n_members, avoid_inverse_members=n_avoid, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
