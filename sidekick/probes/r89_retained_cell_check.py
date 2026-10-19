"""Sidekick probe: independent check of the arithmetic in main's R89 (retained_history/RETAINED_HISTORY.md,
main 9190ccf) with this branch's own S and nu. Nothing is imported from main. The formal absorption
planner (J_s, A_s, the dispatcher) is NOT rebuilt here, so statements about which plans pass are not
checked; only the ordinary paths, normal forms, cells, congruences and inequalities are.

Section 1: for random W9 pairs (C, Q) in window (1): d=v2(9C-1)>=4, z, the actual (h+2)-arrow prefix
  from 3C ends at F=4(3z)+1 (odd d) or 6z+1 (even d); S(C)=(3C+1)/4<Q; (4) 16z<9C and 4z<3Q; (5) for
  even d. The three-node family C=585+4096j, Q=441+3072j (j>=4): d=4 twice, z1, z2, all 9 mod 16,
  3z2-Q=114+816j; the j=4 chain 16969 -> 9545 -> 5369 at Q=12729 with third depth 6; the boundary
  C=15401, Q=11551 has S(C)=Q and 3C+1=4Q.
Section 2: the cell k=85+256j: S^18(Q)=r=(81z0+23)/8 with cost 26 ending (1,1,3,1,2), r-1<6(Q-1); on
  j=64m: v, Q, r=6v+1, nu(r)=3v, E=(81v+11)/64=162818633+3^22 m, v=37 mod 64, v<Q<3v, R26 first exponent
  v2(3v+1)=4 of the state 3v; for every d=2..48, the progression (8) has v2(E)=d-2 and the run targets (9) with the
  ordinary clocks (4+b,1) for d=2b+1 and (3+b,0) for d=2b; (10) for all m; the d=2 leader E is odd,
  2 mod 3, 3E+1<4Q, and in W9 exactly when m=0 mod 16.
Section 3: the subcell m=2736+4096l: C=E=121 mod 128, beta=5 mod 64 and 8 mod 9, s=3 mod 9; S^4(3v)=6C+1
  with (1,1,1,2) and nu(6C+1)=3C; S^3(3C)=X with (1,2,2), S^3(C)=Y with (2,1,2); a=61, b=21 mod 128;
  (2Y+1)/3=b; S^7(3v)=X, S^23(Q)=S^5(3v), S^25(Q)=X, S^27(Q)=Z with last valuations (1,2); the l=0 values
  and ranks rho(a), rho(b); section 5: s odd -> Z selected, nu(Z)=3c, c=(27beta+1)/8 in W9 with
  23Q/40<c<7Q/12; s even -> Z canonical with R26 first exponent v2(Z+1)=3; the identities for g.
Standard library. Run without -O.
"""
from fractions import Fraction as F
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


def canonical(x):
    return x > 0 and x % 2 == 1 and nu(x) == x


def W9(x):
    return x > 0 and x % 16 == 9


def local(C):
    d = v2(9*C - 1)
    h = (d - 5)//2 if d % 2 else (d - 4)//2
    assert (9*C - 1) % 2**d == 0
    z = 3**h * (9*C - 1) // 2**d
    return d, h, z


def section1():
    rng = random.Random(891)
    cases = {"odd": 0, "even": 0}
    while sum(cases.values()) < 4000:
        C = 9 + 16*rng.randrange(700, 10**9)
        Q = rng.randrange(max(11547, (3*C + 1)//4 + 1), 3*C + 1)
        if Q % 2 == 0 or not (Q <= 3*C and 3*C + 1 < 4*Q) or Q < 11547:
            continue
        d, h, z = local(C)
        assert d >= 4 and C % 8 == 1 and (3*C + 1) % 4 == 0 and S(C) == (3*C + 1)//4 < Q
        Fend, _ = walk(3*C, h + 2)
        if d % 2:
            assert Fend == 4*(3*z) + 1 and 32*z < 9*C and 8*(3*z) < 9*Q
            cases["odd"] += 1
        else:
            assert Fend == 6*z + 1 and 16*z <= 9*C - 1 and 9*C - 1 < 4*(3*Q - 1) and 3*Q - 1 < 4*Q  # (5)
            cases["even"] += 1
        assert 16*z < 9*C and 4*z < 3*Q
    fam = 0
    for j in range(4, 400):
        C, Q = 585 + 4096*j, 441 + 3072*j
        assert Q % 2 == 1 and Q >= 11547 and Q <= 3*C and 3*C + 1 < 4*Q
        d1, _, z1 = local(C)
        d2, _, z2 = local(z1)
        assert (d1, z1, d2, z2) == (4, 329 + 2304*j, 4, 185 + 1296*j)
        assert W9(C) and W9(z1) and W9(z2) and 3*z2 - Q == 114 + 816*j > 0
        fam += 1
    assert (585 + 4096*4, 329 + 2304*4, 185 + 1296*4, 441 + 3072*4) == (16969, 9545, 5369, 12729)
    assert local(5369)[0] == 6 and 3*9545 > 12729 and 3*5369 > 12729
    assert S(15401) == 11551 and 3*15401 + 1 == 4*11551
    return {"window_cases": cases, "family_j": [4, 399], "family_cases": fam}


def section2():
    rng = random.Random(892)
    cell = 0
    for j in [0, 1, 2, 63, 64] + [rng.randrange(65, 2**40) for _ in range(30)]:
        Q = 133704987 + 3 * 2**27 * j
        z0 = 76235153 + 16 * 3**15 * j
        assert (81*z0 + 23) % 8 == 0
        r = (81*z0 + 23)//8
        x, vals = walk(Q, 18)
        assert x == r and sum(vals) == 26 and tuple(vals[-5:]) == (1, 1, 3, 1, 2) and r - 1 < 6*(Q - 1)
        assert canonical(Q)
        cell += 1
    # the subcell j = 64m
    sub = 0
    for m in [0, 1, 2, 10, 16, 2736] + [rng.randrange(17, 2**50) for _ in range(30)]:
        v = 128646821 + 64 * 3**18 * m
        Q = 133704987 + 3 * 2**33 * m
        z0 = 76235153 + 16 * 3**15 * 64 * m
        r = (81*z0 + 23)//8
        E = 162818633 + 3**22 * m
        assert r == 6*v + 1 and nu(r) == 3*v and 64*E == 81*v + 11 and v % 64 == 37 and v < Q < 3*v
        assert walk(Q, 18)[0] == r and v2(3*v + 1) == 4   # R26 first exponent of the state 3v: v2(3v+1)
        sub += 1
    # (10): 32E < 39(Q-1) for every m >= 0 (affine in m: constant and slope)
    assert 32*162818633 < 39*(133704987 - 1) and 32 * 3**22 < 39 * 3 * 2**33
    # the depth progression (8) and run targets (9), with ordinary clocks
    runs = 0
    for d in range(2, 49):
        mod = 2**(d - 1)
        base = ((2**(d - 2) - 162818633) * pow(3**22, -1, mod)) % mod
        for m in [base, base + mod, base + mod*rng.randrange(2, 2**30)]:
            v = 128646821 + 64 * 3**18 * m
            E = 162818633 + 3**22 * m
            assert v2(E) == d - 2
            b = d // 2
            if d % 2:
                fq = 2 * F(3, 4)**b * E
                assert fq.denominator == 1
                f = fq.numerator
                assert walk(3*v, 4 + b)[0] == S(f)
            else:
                fq = 8 * F(3, 4)**b * E + 1
                assert fq.denominator == 1
                f = fq.numerator
                assert walk(3*v, 3 + b)[0] == f
            runs += 1
    # the d = 2 leader
    lead = 0
    for m in range(0, 4096, 2):
        E = 162818633 + 3**22 * m
        Q = 133704987 + 3 * 2**33 * m
        assert E % 2 == 1 and E % 3 == 2 and 3*E + 1 < 4*Q
        assert W9(E) == (m % 16 == 0)
        lead += 1
    return {"cell_cases": cell, "subcell_cases": sub, "depth_runs": runs, "d2_leaders": lead}


def section3():
    rng = random.Random(893)
    out = {"cases": 0, "s_odd": 0, "s_even": 0}
    for l in [0, 1, 2, 3, 4, 13] + [rng.randrange(14, 2**40) for _ in range(40)]:
        m = 2736 + 4096*l
        v = 128646821 + 64 * 3**18 * m
        Q = 133704987 + 3 * 2**33 * m
        C = 162818633 + 3**22 * m
        assert (9*C - 1) % 64 == 0
        beta = (9*C - 1)//64
        assert (beta - 5) % 64 == 0 and (81*beta + 7) % 4 == 0
        s = (beta - 5)//64
        a, b = 12*beta + 1, 4*beta + 1
        X, Y, Z = 18*beta + 1, 6*beta + 1, (81*beta + 7)//4
        assert C % 128 == 121 and beta % 64 == 5 and beta % 9 == 8 and s % 9 == 3
        x, vals = walk(3*v, 4)
        assert x == 6*C + 1 and vals == [1, 1, 1, 2] and nu(6*C + 1) == 3*C
        x, vals = walk(3*C, 3)
        assert x == X and vals == [1, 2, 2]
        x, vals = walk(C, 3)
        assert x == Y and vals == [2, 1, 2]
        assert a % 128 == 61 and b % 128 == 21 and 2*Y + 1 == 3*b and beta < Q
        assert walk(3*v, 7)[0] == X and walk(Q, 23)[0] == walk(3*v, 5)[0]
        x, vals = walk(Q, 27)
        assert walk(Q, 25)[0] == X and x == Z and vals[-2:] == [1, 2]
        if s % 2:
            assert selected(Z) and (27*beta + 1) % 8 == 0
            c = (27*beta + 1)//8
            assert nu(Z) == 3*c and W9(c) and 40*c > 23*Q and 12*c < 7*Q
            out["s_odd"] += 1
        else:
            assert canonical(Z) and v2(Z + 1) == 3   # R26 first exponent v2(Z+1)
            out["s_even"] += 1
        # identities on the canonical-Z d'=2 branch formula for g (as rationals)
        g = F(2187*beta + 265, 64)
        assert g == F(3**13 * v + 1161985, 2**18) and 8*(2*g + 1)/27 - 1 == Z
        num = (2*g + 1) * 64
        assert num.denominator == 1 and num.numerator % 27 == 0 and (num.numerator // 27) % 3 != 0
        if l == 0:
            assert (Q, v, beta, a, b) == (70506316836123, 67839005952677, 12073885580933,
                                          144886626971197, 48295542323733)
            assert nu(3*a) == 217329940456795 and nu(3*b) == 72443313485599
        out["cases"] += 1
    return out


def main():
    out = {"probe": "r89_retained_cell_check", "main": "9190ccf",
           "section1": section1(), "section2": section2(), "section3": section3(), "result": "PASS"}
    (HERE / "r89_retained_cell_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
