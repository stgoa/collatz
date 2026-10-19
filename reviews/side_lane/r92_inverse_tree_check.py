"""Sidekick probe: independent checks related to R92 (main 61fd041), with this branch's own step/nu.

Part 1 (R25 inverse table, brute force): for every canonical x < 3000, the canonical y < 2*10^5 with
T(y) = x found by scanning all y equal exactly the table's predecessors below 2*10^5:
  x = 0 mod 3: rays from (8x+3)/3 and (16x+3)/3;  x = 1 mod 3: rays from (4x-1)/3 and (32x+19)/3;
  x = 2 mod 3: point (2x-1)/3 and rays from (64x+19)/3 and (128x+83)/3; each ray continues p -> 64p+49.
Part 2 (R92 at concrete sources, inverse-tree search): for ell = 0 (r = 0, depth <= 19) and the least
ell >= 1 with r = 1 (depth <= 31), every canonical p <= Q with T^d(p) = n_r, d <= 12r+19, is found by
expanding all inverse branches from n_r (every ray index), pruning only states whose every completion
exceeds Q (each inverse step gives y >= (2/3)x - 1). R92 says the only solution is p = Q at d = 12r+18.
Every generated predecessor is checked with this branch's T. Standard library. Run without -O.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step  # noqa: E402
from fibre_count_check import nu  # noqa: E402


def T(x):
    return nu(step(1, x))


def bases(x):
    r = x % 3
    if r == 0:
        return [], [(8*x + 3)//3, (16*x + 3)//3]
    if r == 1:
        return [], [(4*x - 1)//3, (32*x + 19)//3]
    return [(2*x - 1)//3], [(64*x + 19)//3, (128*x + 83)//3]


def table_preds(x, bound):
    pts, rays = bases(x)
    out = [p for p in pts if 0 < p <= bound]
    for p in rays:
        while p <= bound:
            if p > 0:
                out.append(p)
            p = 64*p + 49
    return sorted(out)


def part1():
    bound = 2*10**5
    preds = {}
    for y in range(3, bound, 2):
        if nu(y) == y:
            preds.setdefault(T(y), []).append(y)
    checked = 0
    for x in range(1, 3000, 2):
        if nu(x) != x:
            continue
        brute = sorted(p for p in preds.get(x, []) if p != x)
        assert brute == [p for p in table_preds(x, bound) if p != x], (x, brute[:5], table_preds(x, bound)[:5])
        checked += 1
    return checked


def search(target, Q, dmax):
    hits, nodes = [], 0
    frontier = [target]
    for depth in range(1, dmax + 1):
        rem = dmax - depth            # further steps allowed after this one
        nxt = []
        for x in frontier:
            pts, rays = bases(x)
            cands = list(pts)
            for p in rays:
                # every completion of p is >= (2/3)^rem * p - 3; stop extending the ray past that bound
                while 2**rem*p - 3*3**rem <= Q*3**rem:
                    cands.append(p)
                    p = 64*p + 49
            for y in cands:
                if y <= 0:
                    continue
                assert nu(y) == y and T(y) == x
                nodes += 1
                if y <= Q:
                    hits.append((y, depth))
                if rem > 0 and 2**rem*y - 3*3**rem <= Q*3**rem:
                    nxt.append(y)
        frontier = nxt
    return hits, nodes


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    checked = part1()
    A, M, B, D = 3**12, 2**19, 299947, 7153
    results = []
    # ell = 0, r = 0
    ells = [0]
    # least ell >= 1 with v2(L(v0)) >= 37 (r = 1)
    V0 = 67839005952677
    mod = 2**19
    ell1 = (-((D*V0 + B)//2**18)*pow(D*3**18, -1, mod)) % mod
    ells.append(ell1 if ell1 > 0 else mod)
    for ell in ells:
        v0 = V0 + 2**18*3**18*ell
        Q = 70506316836123 + 3*2**45*ell
        L = D*v0 + B
        vr = (L & -L).bit_length() - 1
        r = (vr - 18)//19
        v = v0
        for _ in range(r):
            assert (A*v + B) % M == 0
            v = (A*v + B)//M
        n_r = 3*v
        x = Q
        for _ in range(12*r + 18):
            x = T(x)
        assert x == n_r
        hits, nodes = search(n_r, Q, 12*r + 19)
        assert hits == [(Q, 12*r + 18)], (ell, r, hits[:5])
        results.append(dict(ell=ell, r=r, Q=Q, depth_limit=12*r + 19, nodes=nodes, hits=[list(h) for h in hits]))
    report = dict(scope="R25 inverse-table completeness (brute force) and R92 at two concrete sources (inverse-tree search).",
                  r25_table_checked_targets=checked, r92_cases=results, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
