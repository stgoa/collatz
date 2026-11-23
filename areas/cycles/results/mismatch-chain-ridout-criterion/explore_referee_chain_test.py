#!/usr/bin/env python3
"""Referee test for the node mismatch-chain-ridout-criterion.

Written from the README statement only (the author's certificate was NOT read
before this file was written, and nothing is imported or copied from it).

Builds actual integer cycles of 3x+d from words and checks, in exact integer
(or exact rational) arithmetic, for every shift H, start i_0, admissible run
length a-1 and end i_r:

  T1  3^a divides 2^(w'_(i0)) xi' - 2^(w_(i0)) xi           (definition of G)
  T2  identity (1) with d*C, d*C' in place of C, C'
  T3  at a mismatch: 2^e | G, g = G/2^e odd, 2^c U - 3^(a+n) g = Theta
  T4  Theta = 2^(w-e) 3^n xi + 2^(w'-e) d C' > 0   (referee's own closed form)
  T5  comparison (4): C <= C' <= 2^(D') C when w' >= w strictly between
  T6  2^sigma zeta = 3^n xi Pi, with Pi = prod (1 + d/(3 x_l))
  T7  pattern (i) bound, T8 pattern (ii) bound (section 3), d-analogues
  T9  the arithmetic of part (b): sign of g, coprimality of P and Q, |Q|_2,
      |P|_3, Q - P = Theta/k, the exact rational part of the inequality chain
  T10 redundancy: U*Theta < 3^(a+n) forces c >= 1 and g >= 1
  T11 the exact form of the remark "Why the amplitudes on the way do not hurt"
  T12 the dictionary of section 4 for words A B A[p] B[q]
Everything exits non-zero on the first failed check.
"""
import itertools
import random
import sys
from fractions import Fraction
from math import gcd

FAILS = []
COUNT = {}


def bump(key, k=1):
    COUNT[key] = COUNT.get(key, 0) + k


def check(cond, label, info=None):
    bump(label)
    if not cond:
        FAILS.append((label, info))
        print("FAIL", label, info)
        if len(FAILS) > 5:
            sys.exit(1)


def intercept(word):
    """C_w = sum_i 3^(len-1-i) 2^(w_0+...+w_(i-1))."""
    n = len(word)
    total = 0
    pref = 0
    for i, letter in enumerate(word):
        total += 3 ** (n - 1 - i) * 2 ** pref
        pref += letter
    return total


def build_cycle(word):
    """Return (d, states) of the 3x+d cycle with valuation word `word`, or None."""
    m = len(word)
    big_d = 2 ** sum(word) - 3 ** m
    if big_d <= 0:
        return None
    c0 = intercept(word)
    gg = gcd(c0, big_d)
    d = big_d // gg
    x = c0 // gg
    states = []
    for letter in word:
        states.append(x)
        num = 3 * x + d
        if num % (2 ** letter) != 0:
            raise RuntimeError("word does not close as integers")
        x = num // 2 ** letter
        if x % 2 == 0:
            raise RuntimeError("even state")
    if x != states[0]:
        raise RuntimeError("cycle does not close")
    if len(set(states)) != m:
        return None  # states must be distinct (primitive)
    return d, states


def test_cycle(word, d, x, extra_n=0):
    m = len(word)
    for H in range(1, m):
        xp = [x[(i + H) % m] for i in range(m)]
        wp = [word[(i + H) % m] for i in range(m)]
        check(all(xp[i] != x[i] for i in range(m)), "states differ under shift")
        matched = [word[i] == wp[i] for i in range(m)]
        for i0 in range(m):
            # maximal common run before i0
            run = 0
            while run < m and matched[(i0 - 1 - run) % m]:
                run += 1
            check(run <= m - 1, "run below period")
            xi = x[(i0 + 1) % m]
            xip = xp[(i0 + 1) % m]
            w0, w0p = word[i0], wp[i0]
            lhs0 = 2 ** w0p * xip - 2 ** w0 * xi
            for a in range(1, run + 2):
                check(lhs0 % 3 ** a == 0, "T1 divisibility by 3^a", (word, H, i0, a))
                G = lhs0 // 3 ** a
                for n in range(0, m + extra_n):
                    bump("configurations")
                    ir = i0 + n
                    zeta = x[(ir + 1) % m]
                    U = xp[(ir + 1) % m]
                    v = [word[(i0 + 1 + k) % m] for k in range(n)]
                    vp = [wp[(i0 + 1 + k) % m] for k in range(n)]
                    sig, sigp = sum(v), sum(vp)
                    C, Cp = intercept(v), intercept(vp)
                    # track equations
                    check(2 ** sig * zeta == 3 ** n * xi + d * C, "track unprimed")
                    check(2 ** sigp * U == 3 ** n * xip + d * Cp, "track primed")
                    rhs = (2 ** (w0p + sigp) * U - 2 ** (w0 + sig) * zeta
                           - d * (2 ** w0p * Cp - 2 ** w0 * C))
                    check(3 ** (a + n) * G == rhs, "T2 identity (1)", (word, H, i0, a, n))
                    if w0 == w0p:
                        continue
                    bump("mismatched-start configurations")
                    e = min(w0, w0p)
                    check(G % 2 ** e == 0, "T3 2^e divides G")
                    g = G // 2 ** e
                    check(g % 2 != 0, "T3 g odd", (word, H, i0, a, n))
                    c = w0p - e + sigp
                    Theta = (2 ** (w0 - e + sig) * zeta
                             + d * (2 ** (w0p - e) * Cp - 2 ** (w0 - e) * C))
                    check(2 ** c * U - 3 ** (a + n) * g == Theta, "T3 reduced identity")
                    check(Theta == 2 ** (w0 - e) * 3 ** n * xi + 2 ** (w0p - e) * d * Cp,
                          "T4 closed form of Theta")
                    check(Theta > 0, "T4 Theta > 0")
                    # ---- arithmetic of part (b)
                    if g <= -1:
                        check(Theta >= 2 ** c * U + 3 ** (a + n), "T9 g<0 forces Theta > 3^(a+n)")
                        check(U * Theta > 3 ** (a + n), "T9 g<0 forces U Theta > 3^(a+n)")
                    else:
                        bump("configurations with g >= 1")
                        k = gcd(U, g)
                        P = 3 ** (a + n) * g // k
                        Q = 2 ** c * U // k
                        check(gcd(P, Q) == 1, "T9 gcd(P,Q)=1")
                        check(0 < P < Q, "T9 0<P<Q")
                        check(Q % 2 ** c == 0 and (Q // 2 ** c) % 2 == 1, "T9 v_2(Q)=c")
                        check(P % 3 ** (a + n) == 0, "T9 v_3(P)>=a+n")
                        check((Q - P) * k == Theta, "T9 Q-P=Theta/k")
                        v3 = 0
                        t = P
                        while t % 3 == 0:
                            t //= 3
                            v3 += 1
                        lhs = Fraction(Q * (Q - P), 2 ** c * 3 ** v3)
                        check(lhs <= Fraction(U * Theta, 3 ** (a + n)), "T9 chain left part")
                        check(max(P, Q) <= 2 ** c * U, "T9 max(P,Q) <= 2^c U")
                    if U * Theta < 3 ** (a + n):
                        bump("configurations with U Theta < 3^(a+n)")
                        check(c >= 1 and g >= 1, "T10 small U Theta forces c>=1, g>=1")
                    if c == 0:
                        check(U * Theta >= 3 ** (a + n) or g <= -1, "T10 c=0 never small")
                    if n == 0 and w0p > w0:
                        check(Theta == xi and U == xip and c == w0p - w0, "Reading: n=0 gives Theta=xi")
                    # ---- part (c)
                    if n >= m:
                        continue  # the README restricts n < m
                    between = [(i0 + 1 + k) % m for k in range(n - 1)]
                    if any(wp[l] < word[l] for l in between):
                        continue
                    Dp = sum(wp[l] - word[l] for l in between)
                    check(C <= Cp <= 2 ** Dp * C, "T5 comparison (4)", (word, H, i0, n))
                    Pi = Fraction(1)
                    for kk in range(n):
                        Pi *= 1 + Fraction(d, 3 * x[(i0 + 1 + kk) % m])
                    check(Fraction(2 ** sig * zeta) == 3 ** n * xi * Pi, "T6 product formula")
                    check(Fraction(d * C) == 3 ** n * xi * (Pi - 1), "T6 d C = 3^n xi (Pi-1)")
                    if w0p > w0:
                        bump("pattern (i) configurations")
                        delta = w0p - w0
                        check(c == delta + sigp and c >= 1, "T7 c in pattern (i)")
                        check(Theta == 2 ** sig * zeta + d * (2 ** delta * Cp - C), "T7 Theta form (i)")
                        check(0 < Theta < 2 ** sig * zeta * (1 + 2 ** (delta + Dp)), "T7 bound on Theta (i)")
                        check(Fraction(U * Theta) < 3 ** n * 2 ** (delta + Dp + 1) * Pi * U * xi,
                              "T7 U Theta bound (i)")
                        # referee's sharper bound
                        check(Fraction(Theta) <= 3 ** n * xi * (1 + 2 ** (delta + Dp) * (Pi - 1)),
                              "T7' sharper bound (i)")
                        if n >= 1:
                            # exact form of the remark on amplitudes
                            dl = wp[ir % m] - word[ir % m]
                            Pif = Fraction(1)
                            for kk in range(n + 1):
                                Pif *= 1 + Fraction(d, 3 * xp[(i0 + kk) % m])
                            left = 2 ** (delta + Dp + 1) * Pi * U * xi
                            right = (2 * xi * zeta * Fraction(xp[i0], x[i0]) * Fraction(1, 1) / Fraction(2) ** dl
                                     * Pif / (1 + Fraction(d, 3 * x[i0])))
                            check(left == right, "T11 exact form of the amplitude remark")
                    elif n >= 1:
                        bump("pattern (ii) configurations")
                        delta = w0 - w0p
                        check(c == sigp and c >= 1, "T8 c in pattern (ii)")
                        check(Theta == 2 ** delta * 3 ** n * xi + d * Cp, "T8 Theta form (ii)")
                        bound = 3 ** n * xi * (2 ** delta + 2 ** Dp * (Pi - 1))
                        check(0 < Theta <= bound, "T8 bound on Theta (ii)")
                        if Fraction(Theta) == bound:
                            bump("pattern (ii) bound attained with equality")
                            check(Dp == 0, "T8 equality only when D'=0")
                        else:
                            check(Dp >= 1, "T8 strict only when D'>=1")
                    else:
                        bump("pattern (ii) with n = 0 (c = 0)")
                        check(c == 0, "c = 0 exactly when w'<w and n=0")


def test_half_period(A, B, p, q):
    a, b = len(A), len(B)
    N = a + b
    Ap = A[:-1] + [A[-1] + p]
    Bq = B[:-1] + [B[-1] + q]
    W = A + B + Ap + Bq
    built = build_cycle(W)
    if built is None:
        return False
    d, st = built
    m = 2 * N
    H = N
    xs, z, y, t = st[0], st[a], st[N], st[N + a]
    sA, sB = sum(A), sum(B)
    CA, CB = intercept(A), intercept(B)
    check(intercept(Ap) == CA and intercept(Bq) == CB, "T12 intercept ignores last letter")
    check((y - xs) % 2 ** sA == 0 and (z - t) % 2 ** sB == 0, "T12 h, j integers")
    h = (y - xs) // 2 ** sA
    j = (z - t) // 2 ** sB
    wp = [W[(i + H) % m] for i in range(m)]
    xp = [st[(i + H) % m] for i in range(m)]
    mism = [i for i in range(m) if W[i] != wp[i]]
    check(mism == [a - 1, N - 1, N + a - 1, 2 * N - 1], "T12 four mismatches")

    def config(i0, n, arun):
        # returns the quantities of the criterion for start i0, n, and a = arun
        run_ok = all(W[(i0 - k) % m] == wp[(i0 - k) % m] for k in range(1, arun))
        xi, xip = st[(i0 + 1) % m], xp[(i0 + 1) % m]
        zeta, U = st[(i0 + n + 1) % m], xp[(i0 + n + 1) % m]
        v = [W[(i0 + 1 + k) % m] for k in range(n)]
        vp = [wp[(i0 + 1 + k) % m] for k in range(n)]
        w0, w0p = W[i0 % m], wp[i0 % m]
        e = min(w0, w0p)
        num = 2 ** w0p * xip - 2 ** w0 * xi
        ok = run_ok and num % (3 ** arun * 2 ** e) == 0
        g = num // (3 ** arun * 2 ** e) if ok else None
        c = w0p - e + sum(vp)
        Theta = 2 ** (w0 - e + sum(v)) * zeta + d * (2 ** (w0p - e) * intercept(vp) - 2 ** (w0 - e) * intercept(v))
        between = [(i0 + 1 + k) % m for k in range(n - 1)]
        Dp = sum(wp[l] - W[l] for l in between)
        allge = all(wp[l] >= W[l] for l in between)
        return dict(ok=ok, xi=xi, xip=xip, zeta=zeta, U=U, sig=sum(v), sigp=sum(vp),
                    C=intercept(v), Cp=intercept(vp), w0=w0, w0p=w0p, g=g, c=c, Theta=Theta,
                    Dp=Dp, allge=allge)

    # Case I
    c1 = config(a - 1, N - 1 - (a - 1), a)
    check(c1["ok"], "T12 I run of a-1 matched, divisibility")
    check(not (W[(a - 1 - a) % m] == wp[(a - 1 - a) % m]), "T12 I run is maximal")
    check(c1["w0p"] - c1["w0"] == p and c1["allge"] and c1["Dp"] == 0, "T12 I pattern (i), delta=p, D'=0")
    check((c1["xi"], c1["xip"], c1["zeta"], c1["U"]) == (z, t, y, xs), "T12 I states")
    check((c1["sig"], c1["sigp"], c1["C"], c1["Cp"]) == (sB, sB + q, CB, CB), "T12 I totals, intercepts")
    check(c1["c"] == sB + p + q and c1["g"] == h, "T12 I c and g=h")
    check(c1["Theta"] == 2 ** sB * y + (2 ** p - 1) * d * CB, "T12 I Theta")
    check(2 ** (sB + p + q) * xs - 3 ** N * h == 2 ** sB * y + (2 ** p - 1) * d * CB, "T12 I identity (4) of the law")
    check(W[N - 1] != wp[N - 1] and wp[N - 1] - W[N - 1] == q, "T12 I further mismatch at i_r")
    # Case II
    c2 = config(2 * N - 1, a, b)
    check(c2["ok"], "T12 II run of b-1 matched, divisibility")
    check(not (W[(2 * N - 1 - b) % m] == wp[(2 * N - 1 - b) % m]), "T12 II run is maximal")
    check(c2["w0"] - c2["w0p"] == q and c2["allge"] and c2["Dp"] == 0, "T12 II pattern (ii), delta=q, D'=0")
    check((c2["xi"], c2["xip"], c2["zeta"], c2["U"]) == (xs, y, z, t), "T12 II states")
    check((c2["sig"], c2["sigp"], c2["C"], c2["Cp"]) == (sA, sA + p, CA, CA), "T12 II totals, intercepts")
    check(c2["c"] == sA + p and c2["g"] == j, "T12 II c and g=j")
    check(c2["Theta"] == 3 ** a * 2 ** q * xs + d * CA, "T12 II Theta")
    check(2 ** (sA + p) * t - 3 ** N * j == 3 ** a * 2 ** q * xs + d * CA, "T12 II identity (5) of the law")
    check(wp[(2 * N - 1 + a) % m] - W[(2 * N - 1 + a) % m] == p, "T12 II further mismatch at i_r")
    check(h > 0 and j != 0, "T12 h>0, j!=0")
    return True


def canonical(word):
    m = len(word)
    return min(tuple(word[i:] + word[:i]) for i in range(m))


def main():
    rng = random.Random(20261123)
    seen = set()
    n_cycles = 0
    d_one = 0
    # exhaustive small words, one representative per rotation class
    for m in range(2, 7):
        for word in itertools.product(range(1, 5), repeat=m):
            word = list(word)
            if tuple(word) != canonical(word):
                continue
            built = build_cycle(word)
            if built is None:
                continue
            d, st = built
            seen.add(tuple(word))
            n_cycles += 1
            d_one += (d == 1)
            test_cycle(word, d, st, extra_n=m)  # also n in [m, 2m) for identity (1), (b) arithmetic
    # random longer words, including large amplitudes
    target = n_cycles + 1500
    while n_cycles < target:
        m = rng.randint(7, 12)
        word = [rng.choice([1, 1, 1, 2, 2, 3, 4, 6, 9]) for _ in range(m)]
        cw = canonical(word)
        if cw in seen:
            continue
        built = build_cycle(word)
        if built is None:
            continue
        seen.add(cw)
        d, st = built
        n_cycles += 1
        d_one += (d == 1)
        test_cycle(word, d, st)
    bump("cycles (general family)", n_cycles)
    bump("cycles with d = 1", d_one)
    # half-period words
    hp = 0
    tries = 0
    while hp < 1500 and tries < 200000:
        tries += 1
        a = rng.randint(1, 5)
        b = rng.randint(1, 5)
        A = [rng.choice([1, 1, 2, 2, 3, 5]) for _ in range(a)]
        B = [rng.choice([1, 1, 2, 2, 3, 5]) for _ in range(b)]
        p = rng.randint(1, 6)
        q = rng.randint(1, 6)
        if test_half_period(A, B, p, q):
            hp += 1
    bump("half-period cycles", hp)
    for key in sorted(COUNT):
        print(f"{COUNT[key]:>10}  {key}")
    if FAILS:
        print("FAILED", len(FAILS))
        sys.exit(1)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
