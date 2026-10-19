"""Sidekick probe: independent check of the concrete claims in main's V001 viewpoint survey (main 77ce821):
the lifting probe (V2/V3) and the potential probe (V6), with this branch's own maps.

Lifting: F1=(3x+1)/2 on x=3 mod 4 then F2=(3y+1)/16 on y=5 mod 32 compose to (9x+5)/32 exactly on
x=3 mod 64 (all x<10^5); the reversed composition is (9x+19)/32; x=35 has word (1,5), not (1,4); the inverse
shortcut path 1->2->4->8->5->3; the d=5 word (1,1,3) composes to (27x+95)/32 on x=19 mod 64, fixes 19, and
for general d has affine fixed point 19d/5; Applegate-Lagarias row 7 mod 64: C^6(5x)=(45x+5)/64<x for
x=7 mod 64, x>=7 (first 2000 members); 7->11->17->13->5 and 35->53->5 merge at 5.
Potential: with conductance 1/n on actual arrows, u(3)=u(5)=1/(1+5T), T=sum_{j>=1} 3/(10*4^j-1), and
9/14 <= u <= 13/18; every inverse neighbour of 5 is (10*4^j-1)/3.
Sublattice control (side-lane addition): for every d coprime to 6, x = d*y gives S_d(dy) = d*S_1(y), so the
multiples of d form an invariant copy of ordinary 3x+1 that never reaches 1 (checked for y < 10^4).
Standard library. Run without -O.
"""
from fractions import Fraction as F
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def v2(n):
    return (n & -n).bit_length() - 1


def S(d, x):
    y = 3*x + d
    return y >> v2(y), v2(y)


def C(d, n):
    return n // 2 if n % 2 == 0 else (3*n + d)//2


def word(d, x, k):
    w = []
    for _ in range(k):
        x, e = S(d, x)
        w.append(e)
    return x, w


def lifting():
    hits = 0
    for x in range(1, 10**5, 2):
        y, w = word(1, x, 2)
        follows = (x % 4 == 3) and ((3*x + 1)//2) % 32 == 5
        assert follows == (x % 64 == 3)
        if follows:
            assert w == [1, 4] and y == (9*x + 5)//32
            hits += 1
    # reversed composition as affine maps
    a = lambda t: (3*t + 1)/2
    b = lambda t: (3*t + 1)/16
    for t in (F(0), F(1)):
        assert a(b(t)) == (9*t + 19)/32 and b(a(t)) == (9*t + 5)/32
    y, w = word(1, 35, 2)
    assert w == [1, 5] and y == 5 and (9*35 + 5) % 32 == 0
    path = [1, 2, 4, 8, 5, 3]
    for i in range(len(path) - 1):
        assert C(1, path[i + 1]) == path[i]
    # d = 5 control
    for x in range(19, 10**5, 64):
        y, w = word(5, x, 3)
        assert w == [1, 1, 3] and y == (27*x + 95)//32
    assert word(5, 19, 3)[0] == 19
    c, E = 0, 0
    for e in (1, 1, 3):
        c, E = 3*c + 2**E, E + e
    assert (c, E) == (19, 5)
    for d in (1, 5, 7):
        fp = F(19*d, 5)
        assert (27*fp + 19*d) / 32 == fp
    al = 0
    for x in range(7, 7 + 64*2000, 64):
        z = 5*x
        for _ in range(6):
            z = C(1, z)
        assert z == (45*x + 5)//64 and 64*z == 45*x + 5 and z < x
        al += 1
    a7, _ = word(1, 7, 4)
    a35, _ = word(1, 35, 2)
    assert a7 == 5 and a35 == 5
    return {"lifting_cylinder_hits": hits, "applegate_lagarias_rows": al}


def potential():
    preds = []
    for a in range(1, 40):
        num = 5 * 2**a - 1
        if num % 3 == 0 and (num // 3) % 2 == 1:
            preds.append(num // 3)
    assert preds[:6] == [(10 * 4**j - 1)//3 for j in range(6)] and preds[0] == 3
    T = sum(F(3, 10 * 4**j - 1) for j in range(1, 60))
    Tlo, Thi = T, T + F(1, 9 * 4**59)
    assert F(1, 13) <= Tlo and Thi <= F(1, 9)
    u_lo, u_hi = 1/(1 + 5*Thi), 1/(1 + 5*Tlo)
    assert F(9, 14) <= u_lo and u_hi <= F(13, 18)
    # harmonic equations at 5 with u(3) = u(5)
    u = 1/(1 + 5*Tlo)
    assert (F(1, 5) + F(1, 3) + Tlo) * u == F(1, 5) + F(1, 3) * u
    return {"T_approx": float(T), "u_approx": float(u)}


def sublattice():
    for d in (5, 7, 13, 61):
        for y in range(1, 10**4, 2):
            if y % 3 == 0:
                continue
            assert S(d, d*y)[0] == d * S(1, y)[0]
    return True


def main():
    out = {"probe": "viewpoint_v001_check", "main": "77ce821", "lifting": lifting(),
           "potential": potential(), "sublattice_copy": sublattice(), "result": "PASS"}
    (HERE / "viewpoint_v001_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
