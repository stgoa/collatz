"""Sidekick probe: independent checks of main's R68 (adjacent_recursion/NATIVE_HEIGHT_SEPARATION.md)
and R70 (mixed_exit/MIXED_EXIT_REENTRY.md), main 9190ccf, with this branch's own S, nu and T.
Nothing is imported from main.

R68: the six-state anchor certificate below 27 (canonical origins {1,7,9,11,17,25} and their T-edges),
     T^2(27)=31 via 41, the 35-arrow word 31 -> 23 (cost 56) with nu(23)=11; for D=3..12 and several
     t: q=31+2^57*3^D*t and n=27+2^60*3^(D-2)*t=(8q-5)/9 are canonical, q=31 (mod 108), and an
     inverse-tree search from q (every branch and ray index, exact pruning) finds that the only
     canonical a<q with T^d(a)=q, 1<=d<=D, is a=n at d=2; the word W from q ends at
     y=23+2*3^(D+35)*t and 8n-(9y+5)=4+2*3^(D-2)*t*(2^62-3^39)>0.
R70: guard w=40529845 (mod 2^26) <=> v2(7153w+311195)>=26, W5 and rho(w)=3w on it; the maximal-copy
     formula m=1+floor((H-26)/19), e=H-19m in 7..25, exit 3w=31 (mod 128), first R26 exponent 5 and the
     second-depth table (e=7: 2; e=8: 3+v2(243z-294023)>=4; e>=9: 3) on constructed inputs; the
     word (9) W=(1,1,1,1,2,3,2,1,1,1,1,2) with map q -> (Aq+1064657)/2^17; the re-entry theorem on
     w=8515171531530858421 (mod 2^63): v2(Y)=37 (one copy, exit 18), the 24-arrow ordinary word
     (W, then W with first entry 3) ending at 6R(w)+1, T^24(3w)=3R(w),
     S^30(3w)=S^6(3R(w)), R(w)>w back in the guard, inequality (17), the least input and its image;
     r-fold repetition on w=-C/E (mod 2^(63+37(r-1))) for r=1..6 with the exact maximal count
     1+floor((h-63)/37), terminal h in 26..62, and clocks T^(24r), (24r+6, 6).
Standard library. Run without -O.
"""
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent


def v2(n):
    n = abs(n)
    return (n & -n).bit_length() - 1


def S(x):
    y = 3*x + 1
    return y >> v2(y)


def Sv(x):
    y = 3*x + 1
    e = v2(y)
    return y >> e, e


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
    return x > 0 and x % 2 == 1 and nu(x) == x


def iterate(f, x, k):
    for _ in range(k):
        x = f(x)
    return x


def inverse_preds(x, bound):
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
        assert canonical(p) and T(p) == x
    return out


def tree_search(y, q, K):
    """(a, d) with a canonical, a < q, T^d(a) = y, 0 <= d <= K; inverse steps obey y'+1 >= (2/3)(x+1)."""
    found, nodes, frontier = set(), 0, [(y, 0)]
    while frontier:
        x, d = frontier.pop()
        nodes += 1
        if x < q:
            found.add((x, d))
        if d < K:
            bound = (3**(K - d) * q) // 2**(K - d) + 1
            frontier.extend((p, d + 1) for p in inverse_preds(x, bound))
    return found, nodes


W68 = (1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 3, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 3, 1, 1, 1, 4, 2, 2, 4, 3)


def r68():
    canon = [c for c in range(1, 27, 2) if canonical(c)]
    assert canon == [1, 7, 9, 11, 17, 25]
    assert {c: T(c) for c in canon} == {1: 1, 7: 11, 9: 7, 11: 17, 17: 1, 25: 9}
    assert canonical(27) and T(27) == 41 and T(41) == 31 and canonical(31)
    assert [c for c in range(27, 31, 2) if canonical(c)] == [27]
    x, vals = 31, []
    for _ in range(35):
        x, e = Sv(x)
        vals.append(e)
    assert tuple(vals) == W68 and sum(vals) == 56 and x == 23 and nu(23) == 11
    rng = random.Random(68)
    cases, maxnodes = 0, 0
    for D in range(3, 13):
        for t in [1, 2, 3, 7] + [rng.randrange(8, 10**9) for _ in range(2)]:
            q = 31 + 2**57 * 3**D * t
            n = 27 + 2**60 * 3**(D - 2) * t
            assert 9*n == 8*q - 5 and canonical(q) and canonical(n) and q % 108 == 31
            found, nodes = tree_search(q, q, D)
            assert found == {(n, 2)}, (D, t, sorted(found)[:4])
            maxnodes = max(maxnodes, nodes)
            x, vals = q, []
            for _ in range(35):
                x, e = Sv(x)
                vals.append(e)
            y = 23 + 2 * 3**(D + 35) * t
            assert tuple(vals) == W68 and x == y
            assert 8*n - (9*y + 5) == 4 + 2 * 3**(D - 2) * t * (2**62 - 3**39) > 0
            cases += 1
    return {"family_cases": cases, "max_tree_nodes": maxnodes}


A, M, B, D7 = 3**12, 2**19, 311195, 7153
P, L = A*A, 2**37
C = B*(A + M)
E = P - L
W70 = (1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 2)   # R70 (9)


def V(w):
    assert (A*w + B) % M == 0
    return (A*w + B)//M


def Y(w):
    return D7*w + B


def R(w):
    assert (P*w + C) % L == 0
    return (P*w + C)//L


def r70():
    assert (P, C, E) == (282429536481, 328537586155, 144990583009) and P == 3**24
    c, Ew = 0, 0
    for e in W70:   # twelve affine odd steps of (9): q -> (A q + 1064657) / 2^17
        c, Ew = 3*c + (1 << Ew), Ew + e
    assert (c, Ew) == (1064657, 17)
    g = 40529845
    assert v2(Y(g)) >= 26 and (-B * pow(D7, -1, 2**26)) % 2**26 == g and g % 8 == 5
    rng = random.Random(70)
    # guard members: W5, canonical 3w, rho(w) = nu(3w) = 3w
    for _ in range(200):
        w = g + 2**26 * rng.randrange(0, 2**40)
        assert w % 8 == 5 and nu(3*w) == 3*w
    # maximal copies, exit valuations, first R26 exponent and the second-depth table
    exits = 0
    for m in range(1, 5):
        for e in range(7, 26):
            H = 19*m + e
            base = ((2**H - B) * pow(D7, -1, 2**(H + 1))) % 2**(H + 1)
            for k in (0, 1, rng.randrange(2, 2**30)):
                w0 = base + k * 2**(H + 1)
                assert v2(Y(w0)) == H and m == 1 + (H - 26)//19
                w = w0
                for _ in range(m):
                    w = V(w)
                assert v2(Y(w)) == e and (3*w) % 128 == 31 and v2(3*w + 1) == 5
                z = Y(w) >> e
                t = (3*w + 1)//32
                d = v2(81*t - 1)
                if e == 7:
                    assert d == 2
                elif e == 8:
                    assert d == 3 + v2(243*z - 294023) and d >= 4
                else:
                    assert d == 3
                exits += 1
    # re-entry theorem on w = 8515171531530858421 (mod 2^63)
    w63 = 8515171531530858421
    assert (-C * pow(E, -1, 2**63)) % 2**63 == w63
    assert R(w63) == 17498212027614261173
    reentry = 0
    for w in [w63, w63 + 2**63, w63 + 3 * 2**63] + [w63 + 2**63 * rng.randrange(4, 2**80) for _ in range(20)]:
        assert v2(Y(w)) == 37 and 1 + (37 - 26)//19 == 1 and 37 - 19 == 18
        x, vals = 3*w, []
        for _ in range(24):
            x, e = Sv(x)
            vals.append(e)
        assert tuple(vals[:12]) == W70 and tuple(vals[12:]) == (3,) + W70[1:]
        Rw = R(w)
        v = V(w)   # exit with v2(Y(v)) = 18; R(w) = 2V^2(w) = (Av+B)/2^18, an odd integer (10)
        assert v2(Y(v)) == 18 and (A*v + B) % 2**18 == 0 and Rw == (A*v + B) // 2**18 and Rw % 2 == 1
        assert x == 6*Rw + 1 and nu(x) == 3*Rw
        assert iterate(T, 3*w, 24) == 3*Rw and iterate(S, 3*w, 30) == iterate(S, 3*Rw, 6)
        assert Rw > w and Rw % 2**26 == g and 756669054999*w > 3644033042755
        assert 8*(3*w) > 9*Rw + 5
        reentry += 1
    # r-fold repetition and the exact maximal count
    reps = 0
    for r in range(1, 7):
        mod = 2**(63 + 37*(r - 1))
        base = (-C * pow(E, -1, mod)) % mod
        for w0 in [base, base + mod, base + mod * rng.randrange(2, 2**20)]:
            h = v2(E*w0 + C)
            rmax = 1 + (h - 63)//37
            assert rmax >= r
            ws = [w0]
            while v2(E*ws[-1] + C) >= 63:
                assert v2(Y(ws[-1])) == 37
                ws.append(R(ws[-1]))
            assert len(ws) - 1 == rmax and all(b > a for a, b in zip(ws, ws[1:]))
            hT = v2(E*ws[-1] + C)
            assert 26 <= hT <= 62 and v2(Y(ws[-1])) >= 26
            for j in range(1, r + 1):
                assert E*ws[j] + C == (P * (E*ws[j - 1] + C)) // L
            assert iterate(T, 3*w0, 24*r) == 3*ws[r]
            assert iterate(S, 3*w0, 24*r + 6) == iterate(S, 3*ws[r], 6)
            reps += 1
    return {"exit_cases": exits, "reentry_cases": reentry, "repetition_cases": reps}


def main():
    out = {"probe": "batch_r68_r70_check", "main": "9190ccf", "r68": r68(), "r70": r70(), "result": "PASS"}
    (HERE / "batch_r68_r70_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
