"""Sidekick probe: independent checks of the arithmetic parts of main's R15, R18, R21 and R29 (main 9190ccf)
with this branch's own S and nu. Statements that need the annular measure A_N (source masses, cluster
masses, residual profiles) are NOT checked here.

R15: for every odd y < 10^6, a strictly smaller ancestor within two Syracuse steps exists exactly when
     y = 5, 11, 13, 17 (mod 18); the stated moves (2y-1)/3, (8y-5)/9, (4y-5)/9 are such ancestors via
     exact one/two-arrow paths and lie below 8y/9.
R18: the graph E0 (valuation-1 arrows, and valuation-2 arrows from sources = 2 mod 3): in-degree and
     out-degree at most 1, no two consecutive valuation-2 arrows, two backward steps contract by < 8/9,
     finite backward roots, and no incoming E0 arrow exactly on the inactive residues {1,3,7,9,15} mod 18
     (all odd y < 10^6); the Mersenne family N=96*64^k, L=12+6k, x_j=3^j 2^(L-j)-1 is an E0 path, its
     first forbidden exit is w=(3^L-1)/2^(2+v2(L)), and for odd k, w = 1 (mod 18) is an inactive root
     (k <= 12).
R21: on E0, h(x)=x (x=1 mod 3), x/2 (x=2 mod 3): steps from type 1 multiply h by > 3/4, from type 2
     by > 3/2, shrinking steps are never consecutive; the separation arithmetic 58/63 from a height
     ratio below 32; the sharp path (1,2)^31,1 from x=3*2^95 t-5 (cost 94) inside E0 with both ends in
     (Q, 32Q), Q=18 floor(x/18); forbidden edges: valuation 2 lands on a smaller inactive root, valuation
     >= 3 lands in an E0 component whose root is below x/4 (all odd x < 2*10^5).
R29: for the T-closure Q of all canonical states below 3000: W_Q={S(q),3q+2} has |W_Q|=2|Q|,
     max W_Q=3maxQ+2, S(W_Q) in W_Q, S(x) in W_Q for every odd x < 2*10^6 with nu(x) in Q, every element
     of W_Q is attained, and such x reach 1 within 1+2|Q| arrows; S(x) <= 3nu(x)+2 for all odd x < 2*10^6;
     the 327/415/1579 example (S^4(327)=415, S^9(327)=1579).
Standard library. Run without -O.
"""
from pathlib import Path
import json
import math

HERE = Path(__file__).resolve().parent


def v2(n):
    return (n & -n).bit_length() - 1


def Sv(x):
    y = 3*x + 1
    e = v2(y)
    return y >> e, e


def S(x):
    return Sv(x)[0]


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


def preds(y, bound):
    """Odd x <= bound with S(x) = y."""
    out, e = [], 1
    while True:
        num = (y << e) - 1
        if num // 3 > bound:
            return out
        if num % 3 == 0 and (num // 3) % 2 == 1 and num // 3 > 0:
            out.append(num // 3)
        e += 1


def r15(limit=10**6):
    cnt = {True: 0, False: 0}
    for y in range(3, limit, 2):
        anc = [p for p in preds(y, y - 1)]
        for m in preds(y, (3*y + 1)//2):
            anc += [p for p in preds(m, y - 1)]
        has = bool([p for p in anc if p < y])
        assert has == (y % 18 in (5, 11, 13, 17)), y
        cnt[has] += 1
        r = y % 18
        if r in (5, 11):
            p = (2*y - 1)//3
            assert 3*p == 2*y - 1 and Sv(p) == (y, 1)
        elif r == 13:
            p = (8*y - 5)//9
            assert 9*p == 8*y - 5 and S(S(p)) == y
        elif r == 17:
            p = (4*y - 5)//9
            assert 9*p == 4*y - 5 and S(S(p)) == y
        else:
            continue
        assert 9*p < 8*y
    return {"with_short_ancestor": cnt[True], "without": cnt[False]}


INACTIVE = (1, 3, 7, 9, 15)   # R18: residues mod 18 with no incoming E0 arrow


def e0_allowed(x):
    e = v2(3*x + 1)
    return e == 1 or (e == 2 and x % 3 == 2)


def e0_pred(y):
    out = []
    if y % 3 == 2:
        x = (2*y - 1)//3
        if x > 0 and e0_allowed(x) and S(x) == y:
            out.append(x)
    if y % 3 == 1:
        x = (4*y - 1)//3
        if x % 3 == 2 and e0_allowed(x) and S(x) == y:
            out.append(x)
    return out


def e0_root(y):
    while True:
        p = e0_pred(y)
        if not p:
            return y
        y = p[0]


def r18(limit=10**6):
    for y in range(1, limit, 2):
        p = e0_pred(y)
        assert len(p) <= 1 and (not p) == (y % 18 in INACTIVE)
        # brute-force: every odd x < 2y with an allowed arrow to y is the listed predecessor
        if y < 3000:
            assert sorted(x for x in range(1, 2*y + 2, 2) if S(x) == y and e0_allowed(x) and x != y) == p
        if p:
            x = p[0]
            pp = e0_pred(x)
            if pp:
                z = pp[0]
                assert not (v2(3*z + 1) == 2 and v2(3*x + 1) == 2)   # no two consecutive valuation-2
                assert 9*z < 8*y                                      # two backward steps contract < 8/9
    roots = sum(1 for y in range(1, 20001, 2) if e0_root(y) <= y)
    mers = 0
    for k in range(0, 13):
        L = 12 + 6*k
        xs = [3**j * 2**(L - j) - 1 for j in range(L)]
        for a, b in zip(xs, xs[1:]):
            assert Sv(a) == (b, 1) and e0_allowed(a)
        w, e = Sv(xs[-1])
        assert e == 3 + v2(L) and w == (3**L - 1) // 2**(2 + v2(L)) and not e0_allowed(xs[-1])
        if k % 2:
            assert w % 18 == 1 and not e0_pred(w)        # inactive root: no E0 predecessor
        mers += 1
    return {"vertices": limit // 2, "roots_checked": roots, "mersenne_k": mers}


def h(x):
    return F_(x) if x % 3 == 1 else F_(x, 2)


def F_(a, b=1):
    from fractions import Fraction
    return Fraction(a, b)


def r21(limit=2*10**5):
    from fractions import Fraction as Fr
    steps = 0
    for x in range(1, limit, 2):
        if x % 3 == 0 or not e0_allowed(x):
            continue
        y = S(x)
        ratio = h(y) / h(x)
        if x % 3 == 1:
            assert ratio > Fr(3, 4) and y % 3 == 2           # a shrinking step lands on type 2
        else:
            assert ratio > Fr(3, 2)
        steps += 1
    # separation arithmetic from (9/8)^(m/2) and (3/4)(9/8)^k below 32
    assert max(m for m in range(0, 200, 2) if Fr(9, 8)**(m//2) < 32) == 58
    assert max(2*k + 1 for k in range(0, 100) if Fr(3, 4) * Fr(9, 8)**k < 32) == 63
    sharp = 0
    for t in range(1, 6):
        x = 3 * 2**95 * t - 5
        y, vals = x, []
        for _ in range(63):
            assert e0_allowed(y)
            y, e = Sv(y)
            vals.append(e)
        assert vals == [1, 2]*31 + [1] and sum(vals) == 94
        Q = 18 * (x // 18)
        assert Q < h(x) < 32*Q and Q < h(y) < 32*Q
        sharp += 1
    forb2 = forb3 = 0
    for x in range(1, limit, 2):
        if x == 1 or e0_allowed(x):
            continue
        y, e = Sv(x)
        if e == 2:
            assert y < x and y % 18 in INACTIVE and not e0_pred(y)
            forb2 += 1
        else:
            assert 4*e0_root(y) < x
            forb3 += 1
    return {"e0_steps": steps, "sharp_t": sharp, "forbidden_val2": forb2, "forbidden_val_ge3": forb3}


def r29(M=3000, X=2*10**6):
    Q = set()
    for c in range(1, M, 2):
        if nu(c) == c:
            x = c
            while x not in Q:
                Q.add(x)
                x = T(x)
    W = {S(q) for q in Q} | {3*q + 2 for q in Q}
    assert len(W) == 2*len(Q) and max(W) == 3*max(Q) + 2
    assert all(S(w) in W for w in W)
    hit, nuQ, maxsteps = set(), 0, 0
    for x in range(1, X, 2):
        n = nu(x)
        assert S(x) <= 3*n + 2
        if n in Q:
            nuQ += 1
            assert S(x) in W
            hit.add(S(x))
            if nuQ % 50 == 0:
                y, k = x, 0
                while y != 1:
                    y, k = S(y), k + 1
                maxsteps = max(maxsteps, k)
                assert k <= 1 + 2*len(Q)
    missing = W - hit
    for w in list(missing):          # attain the rest through larger preimages
        e = 1
        while True:
            num = (w << e) - 1
            if num % 3 == 0 and nu(num // 3) in Q:
                missing.discard(w)
                break
            e += 1
            assert e < 200
    assert not missing
    x = 327
    orbit = [x]
    for _ in range(9):
        orbit.append(S(orbit[-1]))
    assert orbit[4] == 415 and orbit[9] == 1579
    return {"Q_size": len(Q), "max_Q": max(Q), "nu_preimages_checked": nuQ, "max_steps_to_1": maxsteps}


def main():
    out = {"probe": "batch_r15_r18_r21_r29_check", "main": "9190ccf",
           "r15": r15(), "r18": r18(), "r21": r21(), "r29": r29(), "result": "PASS"}
    (HERE / "batch_r15_r18_r21_r29_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
