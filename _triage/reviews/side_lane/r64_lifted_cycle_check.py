"""Sidekick probe: independent check of R64's lifted inverse ray and its acceptance table
(main refined_obstruction/LIFTED_CYCLE.md), with this branch's own step.

Domain: w = 3445 mod 3456, v0 = (16w-13)/27 = 0 mod 3, q = (81 v0 + 23)/32, b = 512 v0 + 113.
The word b -> q is (2,7,1,4). h = v3(b+25), k = floor(h/7), p = (2048/2187)^k (b+25) - 25, j = v3(p+1),
eta = 2^j (p+1)/3^j - 1; the word eta -> q is 1^j, C^k, 2,7,1,4 with C = (1,1,2,1,1,4,1); and
eta < q iff j >= J(k), with J = 14 (k=0), 13 (1-6), 12 (7-12), 11 (13-19), 10 (20-25), 9 (26-31),
8 (32-37), 7 (38-43), 6 (44-49), 5 (50-56), 4 (57-62), 3 (63-68), 2 (69-74), 1 (75-80), 0 (>= 81).
Inputs are built by CRT at every threshold boundary k in {0,1,6,7,...,80,81,85} with j in
{J-1, J, J+1} (feasible values only: k >= 1 uses h = 7k+1, any j >= 1, or h = 7k for j = 0).
Standard library. Run without -O.
"""
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "experiments" / "packet_currents" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402

BOUNDS = [(0, 0, 14), (1, 6, 13), (7, 12, 12), (13, 19, 11), (20, 25, 10), (26, 31, 9), (32, 37, 8),
          (38, 43, 7), (44, 49, 6), (50, 56, 5), (57, 62, 4), (63, 68, 3), (69, 74, 2), (75, 80, 1)]
C = (1, 1, 2, 1, 1, 4, 1)


def J(k):
    for lo, hi, t in BOUNDS:
        if lo <= k <= hi:
            return t
    return 0


def v3(n):
    h = 0
    while n % 3 == 0:
        n //= 3
        h += 1
    return h


def crt(r1, m1, r2, m2):
    return (r1*m2*pow(m2, -1, m1) + r2*m1*pow(m1, -1, m2)) % (m1*m2)


def build(k, j, rng):
    """Return v0 with the prescribed (k, j), or None."""
    two = 2**20
    for _ in range(400):
        if k == 0:
            # Z = 256 v0 + 57 = 0 mod 3^j exactly (j >= 2), v0 = -7 mod 2048, v0 = 0 mod 3
            m3 = 3**(j + 1)
            r3 = (-57*pow(256, -1, m3)) % m3
            r3 = (r3 + 3**j*rng.randrange(1, 3)) % m3 if j >= 1 else r3   # exact order j
            v0 = crt(2048 - 7, 2048, r3 % m3, m3) + 2048*m3*rng.randrange(1, 2**12)
        else:
            h = 7*k + (1 if j >= 1 else 0)
            m3 = 3**(max(j, 1) + 1)
            # b + 25 = 3^h * m, m != 0 mod 3; j = 1 + v3(2^(11k-3) m - 1) when h = 7k+1; j = 0 when h = 7k
            if j >= 1:
                base = pow(2**(11*k - 3), -1, 3**j) if j >= 2 else 1
                r3 = (base + 3**(j - 1)*rng.randrange(0, 3)) % 3**j if j >= 2 else rng.randrange(1, 3)
                mod3 = 3**j
            else:
                r3, mod3 = rng.randrange(1, 3), 3
            r2 = (-3446*pow(3**h, -1, two)) % two
            m = crt(r2, two, r3 % mod3, mod3) + two*mod3*rng.randrange(1, 2**12)
            b = 3**h*m - 25
            if (b - 113) % 512:
                continue
            v0 = (b - 113)//512
        if v0 % 2048 != 2041 or v0 % 3:
            continue
        b = 512*v0 + 113
        h = v3(b + 25)
        kk = h//7
        p = (2048**kk*(b + 25))//3**(7*kk) - 25
        jj = v3(p + 1)
        if kk == k and jj == j:
            return v0
    return None


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(64)
    ks = sorted({0, 85} | {lo for lo, hi, t in BOUNDS} | {hi for lo, hi, t in BOUNDS} | {81})
    tested, skipped = 0, []
    for k in ks:
        for j in sorted({J(k) - 1, J(k), J(k) + 1}):
            if j < 0 or (k == 0 and j < 2) or (k >= 1 and j == 0 and k < 1):
                continue
            v0 = build(k, j, rng)
            if v0 is None:
                skipped.append((k, j))
                continue
            w = (27*v0 + 13)//16
            assert (27*v0 + 13) % 16 == 0 and w % 3456 == 3445
            q = (81*v0 + 23)//32
            b = 512*v0 + 113
            x = b
            for a in (2, 7, 1, 4):
                assert valuation(1, x) == a
                x = step(1, x)
            assert x == q
            p = (2048**k*(b + 25))//3**(7*k) - 25
            eta = (2**j*(p + 1))//3**j - 1
            x = eta
            for a in [1]*j + list(C)*k + [2, 7, 1, 4]:
                assert valuation(1, x) == a
                x = step(1, x)
            assert x == q
            assert (eta < q) == (j >= J(k)), (k, j, eta < q)
            tested += 1
    assert not skipped and tested == 85, (tested, skipped)   # PASS only if every boundary cell was built
    report = dict(scope="Independent check of R64's lifted ray words and acceptance table at every boundary.",
                  boundary_cells_tested=tested, infeasible_or_skipped=skipped, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
