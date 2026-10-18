"""Sidekick probe: independent check of main's R42 (joint_frontier/JOINT_FRONTIER.md, main 9190ccf)
with this branch's own S and nu. Nothing is imported from main. The retained-graph residual weight
R_N(x_r)=1 in (12) uses the annular residual machinery and is NOT checked here.

(1) Two-case interface for C(v)=[18v+3]-[v], v=3 mod 4: on v=3 mod 8, S^2(v)=z=(9v+5)/2^(a+1) with
    a=v2((9v+5)/2) and S^2(18v+3)=9*2^(a-1)*z-7; on v=7 mod 8, S^2(v)=(9v+5)/4 and
    S^2(18v+3)=oddpart(9z-7).
(2) The v=3 mod 32 class: the parametrization (4) v=(2^(h+3)u-5)/9 (both directions), t=(3v-1)/8,
    h=v2(3t+1), u=S(t)=(9v+5)/2^(h+3) <= (9v+5)/32 <= v/3; the two exact arrows (5); the block (6)
    S^(3+2j)(18v+3)=q=2^s*3^(2j+3)*u-5, S^2(v)=u, q=22 mod 27.
(3) The expanding family v_r=(2^(6r+5)-5)/9: S^2(v_r)=1 with word (1,6r+4); 18v_r+3=2^(6r+6)-7;
    S^(4r+3)(18v_r+3)=q_r=2*3^(4r+3)-5 with word (2,1,2)(1,2)^(2r); q_r canonical, 1 mod 8, 1 mod 3;
    S(q_r)=(3^(4r+4)-7)/2.
(4) The d4 roots for 9|r: w, t0, x, p with w=17 mod 128, w=2 mod 3, a=v2(x+1)=2, t0=3 mod 4,
    v2(3t0-1)=4; the four-arrow certificate (9) p->w->F(v)->S(v)->1 with valuations 5,2,3,h+2; the
    upper prefix S^3..S^6 and (10) S^(4r+7)(x)=q_r with word (1,2,2,1,3,3,2)(1,2)^(2r); for 27|r,
    x=x_r=(2^(6r+15)-3365)/81, x_r=3 mod 12, N_r<x_r<9N_r/8, p<N_r; (13) q_r>x_r and the identity
    81(q_r-x_r)=4374*81^r-32768*64^r+2960.
Standard library. Run without -O.
"""
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent


def v2(n):
    n = abs(n)
    return (n & -n).bit_length() - 1


def Sv(x):
    y = 3*x + 1
    e = v2(y)
    return y >> e, e


def S(x):
    return Sv(x)[0]


def walk(x, k):
    vals = []
    for _ in range(k):
        x, e = Sv(x)
        vals.append(e)
    return x, vals


def oddpart(n):
    return n >> v2(n)


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


def part1():
    rng = random.Random(421)
    vs = list(range(3, 200000, 4)) + [rng.randrange(1, 2**120)*4 + 3 for _ in range(5000)]
    n3 = n7 = 0
    for v in vs:
        lo = S(S(v))
        up = S(S(18*v + 3))
        if v % 8 == 3:
            a = v2((9*v + 5)//2)
            z = (9*v + 5) >> (a + 1)
            assert a >= 1 and lo == z and up == 9 * 2**(a - 1) * z - 7
            n3 += 1
        else:
            z = (9*v + 5)//4
            assert (9*v + 5) % 4 == 0 and lo == z and up == oddpart(9*z - 7)
            n7 += 1
    return {"v3mod8": n3, "v7mod8": n7}


def part2():
    rng = random.Random(422)
    blocks, params, arrows = 0, 0, 0
    # (5): two exact arrows from A*2^m*u - 5
    for _ in range(3000):
        A_, u, m = rng.randrange(1, 10**6, 2), rng.randrange(1, 10**6, 2), rng.randrange(4, 60)
        x0 = A_ * 2**m * u - 5
        x1, e1 = Sv(x0)
        x2, e2 = Sv(x1)
        assert (e1, x1, e2, x2) == (1, 3*A_ * 2**(m - 1) * u - 7, 2, 9*A_ * 2**(m - 3) * u - 5)
        arrows += 1
    vs = list(range(3, 400000, 32)) + [rng.randrange(1, 2**100)*32 + 3 for _ in range(3000)]
    for v in vs:
        t = (3*v - 1)//8
        assert (3*v - 1) % 8 == 0
        h = v2(3*t + 1)
        u = S(t)
        assert h >= 2 and u == (9*v + 5) >> (h + 3) and (9*v + 5) % 2**(h + 3) == 0
        assert 32*u <= 9*v + 5 and 3*(9*v + 5) <= 32*v
        assert (2**h * u) % 9 == 4 and 9*v == 2**(h + 3)*u - 5
        j = (h - 2)//3
        s = h - 1 - 3*j
        q = 2**s * 3**(2*j + 3) * u - 5
        assert s in (1, 2, 3) and walk(18*v + 3, 3 + 2*j)[0] == q and S(S(v)) == u and q % 27 == 22
        blocks += 1
    # converse of (4): every admissible (h, u) gives v = 3 mod 32 with exact valuation h
    for h in range(2, 40):
        cnt = 0
        for u in range(1, 4000, 2):
            if (2**h * u) % 9 != 4:
                continue
            v = (2**(h + 3)*u - 5)//9
            assert 9*v == 2**(h + 3)*u - 5 and v > 0 and v % 32 == 3
            t = (3*v - 1)//8
            assert v2(3*t + 1) == h and S(t) == u
            cnt += 1
        params += cnt
    return {"arrow_pairs": arrows, "block_cases": blocks, "parameter_pairs": params}


def part3():
    out = 0
    for r in range(0, 13):
        assert (2**(6*r + 5) - 5) % 9 == 0
        v = (2**(6*r + 5) - 5)//9
        x, vals = walk(v, 2)
        assert x == 1 and vals == [1, 6*r + 4]
        assert 18*v + 3 == 2**(6*r + 6) - 7
        q = 2 * 3**(4*r + 3) - 5
        x, vals = walk(18*v + 3, 4*r + 3)
        assert x == q and vals == [2, 1, 2] + [1, 2]*(2*r)
        assert q % 8 == 1 and q % 3 == 1 and nu(q) == q and S(q) == (3**(4*r + 4) - 7)//2
        out += 1
    return out


def part4():
    out = {"d4_roots": 0, "required_ray": 0}
    for r in (9, 18, 27, 36, 54, 81, 108):
        v = (2**(6*r + 5) - 5)//9
        h = 6*r + 2
        assert v % 9 == 3 and (16*v) % 3 == 0
        w = 16*v//3 + 1
        assert (16*w + 1) % 3 == 0
        t0 = (16*w + 1)//3
        x = 4*t0 - 1
        p = (x - 1)//2
        assert 3*p == 32*w - 1 and w % 128 == 17 and w % 3 == 2
        assert v2(x + 1) == 2 and t0 % 4 == 3 and v2(3*t0 - 1) == 4
        y, e = Sv(p)
        assert (y, e) == (w, 5)
        y, e = Sv(w)
        assert (y, e) == (4*v + 1, 2)
        y, e = Sv(4*v + 1)
        assert (y, e) == (S(v), 3)
        y, e = Sv(S(v))
        assert (y, e) == (1, h + 2)
        assert walk(x, 3)[0] == 18*w + 1 and walk(x, 4)[0] == 4*(2*(18*v + 3) + 1) + 1
        assert walk(x, 5)[0] == 4*S(18*v + 3) + 1 and walk(x, 6)[0] == S(S(18*v + 3))
        q = 2 * 3**(4*r + 3) - 5
        y, vals = walk(x, 4*r + 7)
        assert y == q and vals == [1, 2, 2, 1, 3, 3, 2] + [1, 2]*(2*r)
        assert 81*(q - x) == 4374 * 81**r - 32768 * 64**r + 2960 and q > x
        out["d4_roots"] += 1
        if r % 27 == 0:
            N = 12 * 2**(6*r + 5)
            assert 81*x == 2**(6*r + 15) - 3365 and x % 12 == 3
            assert N < x and 8*x < 9*N and p < N
            out["required_ray"] += 1
    assert 4374 * 81**9 > 32768 * 64**9 and (2**15 - 3365) == 243*121 and pow(2, 162, 243) == 1
    return out


def main():
    out = {"probe": "r42_joint_frontier_check", "main": "9190ccf", "interface": part1(),
           "class_3_mod_32": part2(), "expanding_family_r": part3(), "embedding": part4(), "result": "PASS"}
    (HERE / "r42_joint_frontier_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
