"""Sidekick probe: independent check of main's R82 (history_frontier/HISTORY_FRONTIER.md, main 9190ccf)
with this branch's own T = nu o S. Nothing is imported from main; no anchor table is read.

(1) Anchor classification: every canonical c < 11547 is followed forward with T to 1 (memoised;
    every orbit is checked to terminate). Exactly one reaches Y = 17321 = T(11547): c = 11391, at
    depth 13, along the stated path, with inverse slope 2^20/3^13. No canonical c < 11547 reaches
    11547 itself.
(2) The lifted family q = 11547 + 16*3^D*t, y = (3q+1)/2: q and y canonical, T(q) = y, cutoff (1)
    equal to 11546, and by an independent inverse-tree search from y (all branches, every ray index,
    pruning only states whose every completion is >= q) the canonical a < q with T^d(a) = y,
    d <= D+1, are: none for D <= 11, and exactly p = 11391 + 2^23*3^(D-12)*t at d = 13 for D >= 12.
(3) The contracting control (6): T^6(q) = T(p) = y on the stated progressions, p < q, the inverse
    multipliers 32768/729 and 128/3, and the anchor bound 393216/729 with cutoff 538.
(4) The finite-anchor theorem on random instances: for random canonical anchors Y, horizons K,
    canonical lifts y = Y (mod 3^K) and thresholds q, the inverse-tree set of canonical a < q with
    T^d(a) = y (d <= K) equals the set of lifts c + lambda_c*(y - Y) of origins c <= n whose forward
    path visits Y within K steps (found by forward iteration), restricted to a < q.
Standard library. Run without -O.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent


def v2(n):
    return (n & -n).bit_length() - 1


def S(x):
    y = 3*x + 1
    return y >> v2(y)


def selected(x):
    if x % 4 != 3:
        return False
    a = v2(x + 1)
    return ((x + 1) >> a) % 4 == pow(3, a, 4)


def nu(x):
    while True:
        if x % 8 == 5:
            x = (x - 1)//4
        elif x > 1 and selected(x):
            x = (x - 1)//2
        else:
            return x


def T(x):
    return nu(S(x))


def canonical(x):
    return x % 2 == 1 and x > 0 and nu(x) == x


def inverse_preds(x, bound):
    """All canonical y <= bound with T(y) = x, y != x (R25 table, every ray index); checked by T."""
    r = x % 3
    if r == 0:
        pts, rays = [], [(8*x + 3)//3, (16*x + 3)//3]
    elif r == 1:
        pts, rays = [], [(4*x - 1)//3, (32*x + 19)//3]
    else:
        pts, rays = [(2*x - 1)//3], [(64*x + 19)//3, (128*x + 83)//3]
    out = [p for p in pts if 0 < p <= bound]
    for p in rays:
        while p <= bound:
            out.append(p)
            p = 64*p + 49
    out = [p for p in out if p != x]
    for p in out:
        assert canonical(p) and T(p) == x, (x, p)
    return out


def tree_search(y, q, K):
    """Canonical a < q with T^d(a) = y for some 0 <= d <= K, by inverse search with exact pruning:
    every inverse step has y' + 1 >= (2/3)(x + 1), so from a state x at depth d any origin a at
    depth <= K has 3^(K-d)(a+1) >= 2^(K-d)(x+1) ... we prune when even depth K stays >= q."""
    found, nodes = set(), 0
    frontier = [(y, 0)]
    while frontier:
        x, d = frontier.pop()
        nodes += 1
        if x < q:
            found.add((x, d))
        if d == K:
            continue
        # predecessors y' of x satisfy y'+1 >= (2/3)(x+1); deeper ones keep shrinking by <= 2/3
        bound = (3**(K - d) * q) // 2**(K - d) + 1   # any useful state x' has (2/3)^(K-d-1)(x'+1) < q
        for p in inverse_preds(x, bound):
            frontier.append((p, d + 1))
    return found, nodes


def forward_visit(c, Y, K):
    """Depth at which the T-path of c visits Y within K steps (or None), and the inverse slope."""
    x, d = c, 0
    while d <= K:
        if x == Y:
            return d
        if x == 1:
            return None
        x, d = T(x), d + 1
    return None


def part1():
    memo = {1: (False, None)}
    Y, b = 17321, 11547
    assert T(b) == Y and canonical(b) and canonical(Y)

    def reaches(c):
        path, x = [], c
        while x not in memo:
            path.append(x)
            x = T(x)
            assert len(path) < 10**5
        hitY, dY = memo[x]
        for z in reversed(path):
            if z == Y:
                hitY, dY = True, 0
            elif hitY:
                dY += 1
            memo[z] = (hitY, dY)
        return memo[c]

    hits, hit_b, count = [], [], 0
    for c in range(1, b, 2):
        if not canonical(c):
            continue
        count += 1
        h, d = reaches(c)
        if h:
            hits.append((c, d))
        x = c
        while x != 1:
            assert x != b
            x = T(x)
    assert hits == [(11391, 13)], hits
    path = [11391]
    for _ in range(13):
        path.append(T(path[-1]))
    assert path == [11391, 17087, 25631, 38447, 57671, 86507, 129761, 97321, 72991, 109487,
                    164231, 246347, 369521, 17321]
    # inverse slope: exponent of the quotient path (ordinary valuation plus normaliser exponents)
    E = 0
    for x in path[:-1]:
        y = 3*x + 1
        e = v2(y)
        z = y >> e
        E += e
        while True:
            if z % 8 == 5:
                z, E = (z - 1)//4, E + 2
            elif z > 1 and selected(z):
                z, E = (z - 1)//2, E + 1
            else:
                break
    assert E == 20
    lam = F(2**20, 3**13)
    return count, lam


def part2(lam):
    rows = []
    rng = random.Random(82)
    for D in range(1, 15):
        ts = [0, 1, 2, 5] + [rng.randrange(6, 10**6) for _ in range(2)]
        for t in ts:
            q = 11547 + 16*3**D*t
            y = (3*q + 1)//2
            assert canonical(q) and canonical(y) and T(q) == y and (q//3) % 16 == 9
            Cq = F((q + 1)*(17321 + 1), y + 1)
            n = -(-Cq.numerator // Cq.denominator) - 2
            assert n == 11546 and y - 17321 == 8*3**(D + 1)*t
            found, nodes = tree_search(y, q, D + 1)
            expect = set()
            if D >= 12:
                p = 11391 + 2**23 * 3**(D - 12) * t
                assert p == 11391 + lam*(y - 17321) and p < q
                expect.add((p, 13))
            assert found == expect, (D, t, found)
            rows.append(nodes)
    return len(rows), max(rows)


def part3():
    path = [465]
    for _ in range(6):
        path.append(T(path[-1]))
    assert path == [465, 43, 65, 49, 9, 7, 11] and T(497) == 11
    checked = 0
    for D in range(0, 7):
        for t in (1, 2, 3, 17):
            q = 465 + 2**19 * 3**D * t
            p = 497 + 2**11 * 3**(D + 5) * t
            y = 11 + 16 * 3**(D + 6) * t
            x = q
            for _ in range(6):
                x = T(x)
            assert x == y == T(p) and p < q and p - q == 32 - 26624 * 3**D * t
            assert canonical(q) and canonical(p) and canonical(y)
            checked += 1
    assert F(2**19, 3**6) == F(524288, 729) and F(2**11 * 3**5, 3**6) == F(2048, 3)
    # multipliers: lambda = (q-shift)/(y-shift) per unit t
    lq, lp = F(2**19, 16 * 3**6), F(2**11 * 3**5, 16 * 3**6)
    assert lq == F(32768, 729) and lp == F(128, 3) and lp / lq == F(243, 256)
    # anchor bound (5) with g = 1/lq on q >= 465, Y = 11
    g = 1 / lq
    h = 11 - g*465
    bnd = max(F(466), F(12) / g)
    assert bnd == F(393216, 729) and -(-bnd.numerator // bnd.denominator) - 2 == 538
    assert h + g*465 == 11
    return checked


def part4():
    rng = random.Random(4082)
    cases = nonempty = deep = maxd = 0
    while cases < 300:
        Y = rng.randrange(3, 3000, 2)
        if not canonical(Y) or Y == 1:
            continue
        K = rng.randrange(1, 7)
        s = rng.randrange(0, 40)
        y = Y + 3**K * s
        if not canonical(y):
            continue
        q = rng.randrange(3, 4000)
        Cq = F((q + 1)*(Y + 1), y + 1)
        n = -(-Cq.numerator // Cq.denominator) - 2
        if n > 20000:
            continue
        lifts = set()
        for c in range(1, max(n, 0) + 1, 2):
            if not canonical(c):
                continue
            d = forward_visit(c, Y, K)
            if d is None:
                continue
            # inverse slope of the T-path c -> Y: lambda = (dc/dY) from the exact affine word
            E, x = 0, c
            for _ in range(d):
                yy = 3*x + 1
                e = v2(yy)
                z = yy >> e
                E += e
                while True:
                    if z % 8 == 5:
                        z, E = (z - 1)//4, E + 2
                    elif z > 1 and selected(z):
                        z, E = (z - 1)//2, E + 1
                    else:
                        break
                x = z
            assert x == Y
            a = c + F(2**E, 3**d) * (y - Y)
            assert a.denominator == 1
            a = a.numerator
            if a < q:
                lifts.add((a, d))
        found, _ = tree_search(y, q, K)
        assert found == lifts, (Y, K, y, q, sorted(found)[:5], sorted(lifts)[:5])
        cases += 1
        nonempty += bool(found)
        deep += sum(1 for a, d in found if d >= 1)
        maxd = max([maxd] + [d for a, d in found])
    return cases, nonempty, deep, maxd


def main():
    out = {"probe": "r82_anchor_lift_check", "main": "9190ccf"}
    count, lam = part1()
    out["anchor_canonical_origins_below_11547"] = count
    out["only_origin_reaching_17321"] = [11391, 13, str(lam)]
    out["lifted_family_cases"], out["max_tree_nodes"] = part2(lam)
    out["contracting_control_cases"] = part3()
    (out["random_theorem_cases"], out["random_nonempty"], out["random_histories_depth_ge_1"],
     out["random_max_depth"]) = part4()
    out["result"] = "PASS"
    (HERE / "r82_anchor_lift_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
