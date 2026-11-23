#!/usr/bin/env python3
"""Independent referee test for
  half-period-s-unit-approximation-law  and  half-period-four-mismatch-finiteness.

Written from the README statements only.  It does not import, copy or read the
author's certificate.  Standard library only.

Parts
  P0  exact constants and the threshold arithmetic (Fractions, integers)
  P1  the normal form of section 1 (exhaustive on small words) and primitivity
  P2  actual 3x+d cycles built from words A B A[p] B[q]; every identity, sign,
      placement claim and elementary inequality in exact integers; the combined
      real inequalities (12), (13), (11) and the final gap in the d-agnostic form
      (actual tau, ell, kappa of the cycle), floats with an 80-digit Decimal
      fallback for small margins
  P3  controls found by brute-force iteration of 3x+d (not by word construction)
  P4  the approximation lemma of section 8 and the Legendre remark
  P5  the algebra of the Ridout step (file 2, section 2) on the same cycles
"""
import json
import math
import random
import sys
from decimal import Decimal, getcontext
from fractions import Fraction
from math import gcd
from pathlib import Path

getcontext().prec = 80
LN2 = Decimal(2).ln()


class FloatR:
    name = "float"
    alpha = math.log2(3)
    tol = 1e-7

    @staticmethod
    def lg(n):
        return math.log2(n)

    @staticmethod
    def num(v):
        try:
            return float(v)
        except OverflowError:
            return math.inf


class DecR:
    name = "decimal80"
    alpha = Decimal(3).ln() / LN2
    tol = Decimal(10) ** -60

    @staticmethod
    def lg(n):
        return Decimal(n).ln() / LN2

    @staticmethod
    def num(v):
        v = Fraction(v)
        return Decimal(v.numerator) / Decimal(v.denominator)


class Tally:
    def __init__(self):
        self.n = {}
        self.bad = {}
        self.minslack = {}
        self.examples = {}

    def exact(self, name, cond, ctx=None):
        self.n[name] = self.n.get(name, 0) + 1
        if not cond:
            self.bad[name] = self.bad.get(name, 0) + 1
            self.examples.setdefault(name, ctx)

    def slack(self, name, value, strict, ctx=None, tol=0):
        """value must be > 0 (strict) or >= 0 (non-strict, up to tol)."""
        self.n[name] = self.n.get(name, 0) + 1
        v = float(value)
        if name not in self.minslack or v < self.minslack[name]:
            self.minslack[name] = v
        ok = value > 0 if strict else value >= -tol
        if not ok:
            self.bad[name] = self.bad.get(name, 0) + 1
            self.examples.setdefault(name, ctx)


T = Tally()
MUT = {}
DISTINCT = {}


def mutant(name, value):
    """A deliberately WRONG variant of a proved inequality; count how often the corpus detects it."""
    rec = MUT.setdefault(name, [0, 0])
    rec[0] += 1
    if value < -1e-9:
        rec[1] += 1


def v2(n):
    return (n & -n).bit_length() - 1


def v3(n):
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def intercept(w):
    """C_w = sum_i 3^(len-1-i) 2^(w_0+..+w_(i-1))."""
    c, pre, L = 0, 0, len(w)
    for i, letter in enumerate(w):
        c += 3 ** (L - 1 - i) << pre
        pre += letter
    return c


# ------------------------------------------------------------------ P0
def part0():
    out = {}
    lo, hi = Fraction(15849, 10000), Fraction(317, 200)
    T.exact("P0 alpha > 15849/10000", 3 ** 10000 > 2 ** 15849)
    T.exact("P0 alpha < 317/200", 3 ** 200 < 2 ** 317)
    # kappa = log2(3 + 1/M) <= log2(3 + 2^-17) < 317/200
    T.exact("P0 kappa < 317/200", (3 * 2 ** 17 + 1) ** 200 < 2 ** (317 + 17 * 200))
    c0 = 1 - hi + 1 / hi
    T.exact("P0 c0 = 2911/63400", c0 == Fraction(2911, 63400))
    T.exact("P0 kappa(alpha-1) bound < 0.928", hi * (hi - 1) < Fraction(928, 1000))
    c_ell = 2 + 1 / lo      # >= 2 + 1/alpha
    c_tau = 3 + 1 / lo      # >= 3 + 1/alpha
    main_slope = c0 - Fraction(1, 25) - c_tau / 2 ** 18
    excl_slope = 1 - hi * (hi - 1) - 2 * hi / 2 ** 18

    def ell_ub(k):          # ell < 514 + 342 log2 N < 514 + 342 (k+1) on [2^k, 2^(k+1))
        return 514 + 342 * (k + 1)

    def main_margin(k):
        return main_slope * 2 ** k - c_ell * ell_ub(k)

    def excl_margin(k):
        return excl_slope * 2 ** k - (1 + hi) * ell_ub(k)

    T.exact("P0 main threshold on every block k=22..600", all(main_margin(k) > 0 for k in range(22, 601)))
    T.exact("P0 main threshold monotone step", main_slope * 2 ** 22 > 342 * c_ell)
    T.exact("P0 exclusion threshold on every block k=22..600", all(excl_margin(k) > 0 for k in range(22, 601)))
    T.exact("P0 exclusion threshold monotone step", excl_slope * 2 ** 22 > 342 * (1 + hi))
    out["main_margin_k22"] = float(main_margin(22))
    out["excl_margin_k22"] = float(excl_margin(22))
    out["main_first_block_ok"] = min(k for k in range(1, 40) if all(main_margin(m) > 0 for m in range(k, 60)))
    out["excl_first_block_ok"] = min(k for k in range(1, 40) if all(excl_margin(m) > 0 for m in range(k, 60)))
    # file 2: 2 tau + ell < N/20, with 2 tau < N/2^17
    def f2_margin(k):
        return (Fraction(1, 20) - Fraction(1, 2 ** 17)) * 2 ** k - ell_ub(k)
    T.exact("P0 file2: 2tau+ell < N/20 on blocks k=22..600", all(f2_margin(k) > 0 for k in range(22, 601)))
    T.exact("P0 file2: step", (Fraction(1, 20) - Fraction(1, 2 ** 17)) * 2 ** 22 > 342)
    T.exact("P0 file2: (2-alpha) - 1/20 > 1/3", 2 - hi - Fraction(1, 20) > Fraction(1, 3))
    T.exact("P0 file2: (alpha-1) + 1/20 < 1", hi - 1 + Fraction(1, 20) < 1)
    T.exact("P0 file2: eps=1/250: 5N/250 = N/50", Fraction(5, 250) == Fraction(1, 50))
    # local descent below 2^17 (odd-only map)
    worst = 0
    okd = True
    for n in range(3, 2 ** 17, 2):
        m, s = n, 0
        while m >= n and s < 5000:
            m = 3 * m + 1
            m >>= v2(m)
            s += 1
        if m >= n:
            okd = False
        worst = max(worst, s)
    T.exact("P0 descent below 2^17", okd)
    out["descent_max_steps"] = worst
    return out


# ------------------------------------------------------------------ P1
def mism(W, k):
    L = len(W)
    return sum(1 for i in range(L) if W[i] != W[(i + k) % L])


def normal_form(W):
    """Section 1 recipe, implemented literally.  Returns (A, B, p, q, Wrot)."""
    N = len(W) // 2
    u, v = W[:N], W[N:]
    diffs = [(i, v[i] - u[i]) for i in range(N) if v[i] != u[i]]
    if len(diffs) != 2:
        return None
    (i1, d1), (i2, d2) = diffs
    k = i2 + 1 if (d1 > 0) == (d2 > 0) else i1 + 1
    W2 = W[k:] + W[:k]
    u2, v2_ = W2[:N], W2[N:]
    dd = [(i, v2_[i] - u2[i]) for i in range(N) if v2_[i] != u2[i]]
    if all(x < 0 for _, x in dd):
        u2, v2_ = v2_, u2
        W2 = u2 + v2_
        dd = [(i, -x) for i, x in dd]
    if len(dd) != 2 or not all(x > 0 for _, x in dd) or dd[1][0] != N - 1:
        return None
    m, p = dd[0]
    q = dd[1][1]
    A, B = u2[:m + 1], u2[m + 1:]
    if not A or not B:
        return None
    if W2 != A + B + A[:-1] + [A[-1] + p] + B[:-1] + [B[-1] + q]:
        return None
    if {p, q} != {abs(d1), abs(d2)} and sorted([p, q]) != sorted([abs(d1), abs(d2)]):
        return None
    return A, B, p, q, W2


def all_words(length, letters):
    if length == 0:
        yield []
        return
    for w in all_words(length - 1, letters):
        for l in letters:
            yield w + [l]


def part1():
    tested = 0
    for N in range(2, 6):
        for u in all_words(N, [1, 2, 3]):
            for i1 in range(N):
                for i2 in range(i1 + 1, N):
                    for d1 in (-2, -1, 1, 2, 3):
                        for d2 in (-2, -1, 1, 2, 3):
                            v = list(u)
                            v[i1] += d1
                            v[i2] += d2
                            if v[i1] < 1 or v[i2] < 1:
                                continue
                            W = u + v
                            tested += 1
                            T.exact("P1 four mismatches at half rotation", mism(W, N) == 4, W)
                            nf = normal_form(W)
                            ok = nf is not None
                            if ok:
                                A, B, p, q, W2 = nf
                                ok = any(W2 == W[k:] + W[:k] for k in range(2 * N)) and p >= 1 and q >= 1
                            T.exact("P1 normal form recipe", ok, W)
    # converse scope: every word with exactly four mismatches at the half rotation is of the stated type
    conv = 0
    for N in range(2, 5):
        for W in all_words(2 * N, [1, 2, 3]):
            if mism(W, N) == 4:
                conv += 1
                T.exact("P1 every 4-mismatch word normalises", normal_form(W) is not None, W)
    # primitivity: a proper power never has exactly four mismatches at its half rotation
    powc = 0
    for L in range(1, 5):
        for w in all_words(L, [1, 2, 3]):
            for k in (2, 3, 4, 5, 6):
                W = w * k
                if len(W) % 2 == 0:
                    powc += 1
                    T.exact("P1 proper powers never have 4 half-mismatches", mism(W, len(W) // 2) != 4, W)
    return {"recipe_words": tested, "converse_words": conv, "power_words": powc}


# ------------------------------------------------------------------ P2
CASES = {"I": 0, "II": 0, "B": 0, "C": 0}
EXTRA = {"p_eq_q": 0, "p_gt_q_and_j_neg": 0, "p_lt_q_and_j_pos": 0, "min_at_block_start": 0,
         "gap_exponent_G_positive": 0, "N_over_25_gap_holds": 0, "N_over_25_gap_fails": 0,
         "d_equals_1": 0, "max_N": 0}


def build_cycle(W):
    """Return (d, states) for the reduced 3x+d cycle of the word W, or None."""
    E, L = sum(W), len(W)
    D = 2 ** E - 3 ** L
    if D <= 0:
        return None
    C = intercept(W)
    g = gcd(C, D)
    d, cur = D // g, C // g
    st = []
    for w in W:
        st.append(cur)
        num = 3 * cur + d
        if cur <= 0 or cur % 2 == 0 or v2(num) != w:
            raise RuntimeError(f"word {W} is not realised")
        cur = num >> w
    if cur != st[0]:
        raise RuntimeError(f"cycle of {W} does not close")
    return d, st


def reals(R, c):
    """All real-number slacks for one cycle (dict name -> (value, strict))."""
    a, b, N, p, q, sA, sB, E, d = c["a"], c["b"], c["N"], c["p"], c["q"], c["sA"], c["sB"], c["E"], c["d"]
    al = R.alpha
    lg = R.lg
    M = c["M"]
    ell = lg(M)
    tau = R.num(Fraction(E, 2)) - N * al
    kap = lg(3 * M + d) - ell
    out = {}
    out["(7) tau > 0"] = (tau, True)
    out["(7) tau <= N log2(1+d/(3M))"] = (N * (lg(3 * M + d) - lg(3 * M)) - tau, False)
    out["(7) tau < N d/(2M)"] = (N * R.num(Fraction(d, 2 * M)) - tau, True)
    X, Tt, lz = lg(c["x"]), lg(c["t"]), lg(c["z"])
    c0 = 1 - al + 1 / al
    case = c["case"]
    if case == "I":
        i = c["i"]
        out["I: b < (X+q)/alpha"] = ((X + q) / al - b, True)
        out["I: X <= (alpha-1)N+tau+ell-(p+q)/2"] = ((al - 1) * N + tau + ell - R.num(Fraction(p + q, 2)) - X, False)
        lhs = sA - 2 * X - p
        l1 = a - X - ell - p
        l2 = N - (1 + 1 / al) * X - q / al - ell - p
        rhs = c0 * N + (1 - 1 / al) * R.num(Fraction(q - p, 2)) - (1 + 1 / al) * tau - (2 + 1 / al) * ell
        out["(12) line 1 (>=)"] = (lhs - l1, False)
        out["(12) line 2 (>)"] = (l1 - l2, True)
        out["(12) line 3 (>=)"] = (l2 - rhs, False)
        out["(12) combined"] = (lhs - rhs, True)
        cc = sB + p + q
        lth = lg(c["th1"] * c["h"])
        out["I: Theta1*h < 2^(c+2tau-(sA-2X-p))"] = (cc + 2 * tau - lhs - lth, True)
        G = c0 * N + (1 - 1 / al) * R.num(Fraction(q - p, 2)) - (3 + 1 / al) * tau - (2 + 1 / al) * ell
        out["I: Theta1*h < 2^(c-G) (d-agnostic gap)"] = (cc - G - lth, True)
        out["file2 I: sA < X+(p+q)/2+tau"] = (X + R.num(Fraction(p + q, 2)) + tau - sA, True)
        out["file2 I: sA < (alpha-1)N+2tau+ell"] = ((al - 1) * N + 2 * tau + ell - sA, True)
        out["file2 I: b > (2-alpha)N-2tau-ell"] = (b - ((2 - al) * N - 2 * tau - ell), True)
        out["file2 I: log2 U <= (alpha-1)N+tau+ell-(p+q)/2"] = out["I: X <= (alpha-1)N+tau+ell-(p+q)/2"]
        c["G"] = float(G)
        c["gapN25"] = float(cc - R.num(Fraction(N, 25)) - lth)
    elif case == "II":
        out["II: a < (T+p)/alpha"] = ((Tt + p) / al - a, True)
        out["II: T <= (alpha-1)N+tau+ell-(p+q)/2"] = ((al - 1) * N + tau + ell - R.num(Fraction(p + q, 2)) - Tt, False)
        lhs = sB - 2 * Tt
        l1 = b - Tt - ell
        l2 = N - (1 + 1 / al) * Tt - p / al - ell
        rhs = (c0 * N + (1 - 1 / al) * R.num(Fraction(p, 2)) + (1 + 1 / al) * R.num(Fraction(q, 2))
               - (1 + 1 / al) * tau - (2 + 1 / al) * ell)
        out["(13) line 1 (>=)"] = (lhs - l1, False)
        out["(13) line 2 (>)"] = (l1 - l2, True)
        out["(13) line 3 (>=)"] = (l2 - rhs, False)
        out["(13) combined"] = (lhs - rhs, True)
        cc = sA + p
        lth = lg(c["th2"] * c["j"])
        out["II: Theta2*j < 2^(c'+2tau-(sB-2T))"] = (cc + 2 * tau - lhs - lth, True)
        G = rhs - 2 * tau
        out["II: Theta2*j < 2^(c'-G) (d-agnostic gap)"] = (cc - G - lth, True)
        out["file2 II: sB < T+(p-q)/2+tau"] = (Tt + R.num(Fraction(p - q, 2)) + tau - sB, True)
        out["file2 II: sB < (alpha-1)N+2tau+ell"] = ((al - 1) * N + 2 * tau + ell - sB, True)
        out["file2 II: a > (2-alpha)N-2tau-ell"] = (a - ((2 - al) * N - 2 * tau - ell), True)
        out["remark II: 3^a x >= 2^(sA-2tau) z"] = (a * al + lg(c["x"]) - sA + 2 * tau - lz, True)
        out["remark II: Theta2*j > 2^(q+sA-2tau) z"] = (lth - (q + sA - 2 * tau + lz), True)
        c["G"] = float(G)
        c["gapN25"] = float(cc - R.num(Fraction(N, 25)) - lth)
    elif case == "B":
        out["B: b < ell+(q-p)/2+tau"] = (ell + R.num(Fraction(q - p, 2)) + tau - b, True)
        out["B: a < ell+(kappa-1)b"] = (ell + (kap - 1) * b - a, True)
        out["(11) in case B"] = ((1 + kap) * ell + kap * (al - 1) * N + 2 * kap * tau - N, True)
    else:
        out["C: a < ell+(p+q)/2+tau"] = (ell + R.num(Fraction(p + q, 2)) + tau - a, True)
        out["C: b < ell+(kappa-1)a"] = (ell + (kap - 1) * a - b, True)
        out["(11) in case C"] = ((1 + kap) * ell + kap * (al - 1) * N + 2 * kap * tau - N, True)
    return out


def mutants(c):
    R = FloatR
    a, b, N, p, q, sA, sB, E, d = c["a"], c["b"], c["N"], c["p"], c["q"], c["sA"], c["sB"], c["E"], c["d"]
    al, lg, M = R.alpha, R.lg, c["M"]
    ell = lg(M)
    tau = E / 2 - N * al
    kap = lg(3 * M + d) - ell
    X, Tt, lz = lg(c["x"]), lg(c["t"]), lg(c["z"])
    c0 = 1 - al + 1 / al
    case = c["case"]
    rhs11 = (1 + kap) * ell + kap * (al - 1) * N + 2 * kap * tau
    if N >= rhs11:
        # the mechanism of section 5 is active: (11) fails, so the cycle must be in case I or II
        EXTRA["(11) fails, case " + case] = EXTRA.get("(11) fails, case " + case, 0) + 1
    mutant("placement: j<0 forces first A (wrong without large N)", -1 if case == "B" else 1)
    mutant("placement: j>0 forces B[q] (wrong without large N)", -1 if case == "C" else 1)
    mutant("sign: p<q forces j<0 (wrong for d>1)", -1 if (p < q and c["j"] > 0) else 1)
    if case == "I":
        lhs = sA - 2 * X - p
        rhs = c0 * N + (1 - 1 / al) * (q - p) / 2 - (1 + 1 / al) * tau - (2 + 1 / al) * ell
        lth = lg(c["th1"] * c["h"])
        cc = sB + p + q
        mutant("(12) with (q-p) instead of (q-p)/2", lhs - (rhs + (1 - 1 / al) * (q - p) / 2))
        mutant("(12) with (1+1/alpha) ell instead of (2+1/alpha) ell", lhs - (rhs + ell))
        mutant("(12) with the tau term dropped", lhs - (rhs + (1 + 1 / al) * tau))
        mutant("(12) with c0 + 0.02", lhs - (rhs + 0.02 * N))
        mutant("I gap with 2 tau forgotten", cc - lhs - lth)
        mutant("I: X bound with ell dropped", (al - 1) * N + tau - (p + q) / 2 - X)
        mutant("I: b < (X+p)/alpha instead of (X+q)/alpha", (X + p) / al - b)
        mutant("I: N/25 gap as if d-agnostic", cc - N / 25 - lth)
        mutant("I gap with c-1", cc - 1 - (rhs - 2 * tau) - lth)
    elif case == "II":
        lhs = sB - 2 * Tt
        rhs = c0 * N + (1 - 1 / al) * p / 2 + (1 + 1 / al) * q / 2 - (1 + 1 / al) * tau - (2 + 1 / al) * ell
        lth = lg(c["th2"] * c["j"])
        cc = sA + p
        mutant("(13) with p and q coefficients swapped", lhs - (c0 * N + (1 + 1 / al) * p / 2 + (1 - 1 / al) * q / 2
                                                                 - (1 + 1 / al) * tau - (2 + 1 / al) * ell))
        mutant("(13) with (1+1/alpha) ell instead of (2+1/alpha) ell", lhs - (rhs + ell))
        mutant("(13) with the tau term dropped", lhs - (rhs + (1 + 1 / al) * tau))
        mutant("II gap with c'-1", cc - 1 - (rhs - 2 * tau) - lth)
        mutant("II gap with 2 tau forgotten", cc - lhs - lth)
        mutant("II: a < (T+q)/alpha instead of (T+p)/alpha", (Tt + q) / al - a)
        mutant("II: slope z/t with (q-p)/2", Tt + (q - p) / 2 + tau - lz)
        mutant("II: N/25 gap as if d-agnostic", cc - N / 25 - lth)
    elif case == "B":
        mutant("B: b bound with tau dropped", ell + (q - p) / 2 - b)
        mutant("B: a bound with ell dropped", (kap - 1) * b - a)
        mutant("(11) B with kappa factor dropped on (alpha-1)N", (1 + kap) * ell + (al - 1) * N + 2 * kap * tau - N)
    else:
        mutant("C: a bound with |p-q|/2 instead of (p+q)/2", ell + abs(p - q) / 2 + tau - a)
        mutant("C: b bound with ell dropped", (kap - 1) * a - b)
        mutant("(11) C with kappa factor dropped on (alpha-1)N", (1 + kap) * ell + (al - 1) * N + 2 * kap * tau - N)


def check_cycle(A, B, p, q, d, st, tag, light=False):
    a, b = len(A), len(B)
    N = a + b
    sA, sB = sum(A), sum(B)
    E = 2 * sA + 2 * sB + p + q
    ctx = (tag, A, B, p, q, d)
    x, z, y, t = st[0], st[a], st[N], st[N + a]
    CA, CB = intercept(A), intercept(B)
    EXTRA["max_N"] = max(EXTRA["max_N"], N)
    if d == 1:
        EXTRA["d_equals_1"] += 1
    T.exact("states distinct (primitive)", len(set(st)) == 2 * N, ctx)
    T.exact("states odd, coprime to 3", all(s % 2 == 1 and s % 3 != 0 for s in st), ctx)
    # (1)
    T.exact("(1) block equations", 2 ** sA * z == 3 ** a * x + d * CA and 2 ** sB * y == 3 ** b * z + d * CB
            and 2 ** (sA + p) * t == 3 ** a * y + d * CA and 2 ** (sB + q) * x == 3 ** b * t + d * CB, ctx)
    T.exact("C of A[p] equals C of A", intercept(A[:-1] + [A[-1] + p]) == CA and intercept(B[:-1] + [B[-1] + q]) == CB, ctx)
    # (2)
    T.exact("(2) 2^sA | y-x and 2^sB | z-t", (y - x) % 2 ** sA == 0 and (z - t) % 2 ** sB == 0, ctx)
    h, j = (y - x) // 2 ** sA, (z - t) // 2 ** sB
    T.exact("(2) 2^p t - z = 3^a h, y - 2^q x = 3^b j", 2 ** p * t - z == 3 ** a * h and y - 2 ** q * x == 3 ** b * j, ctx)
    T.exact("h > 0", h > 0, ctx)
    T.exact("j != 0", j != 0, ctx)
    T.exact("h odd and j odd (file 2)", h % 2 == 1 and j % 2 == 1, ctx)
    T.exact("j < 0 implies p < q", (j > 0) or (p < q), ctx)
    if p == q:
        EXTRA["p_eq_q"] += 1
        T.exact("p = q implies j > 0", j > 0, ctx)
    if p > q and j < 0:
        EXTRA["p_gt_q_and_j_neg"] += 1
    if p < q and j > 0:
        EXTRA["p_lt_q_and_j_pos"] += 1
    # (3)
    T.exact("(3) identity", (2 ** p - 1) * (2 ** q - 1) * d * CA ==
            3 ** a * 2 ** sA * (2 ** q - 2 ** p) * h
            + (2 ** (sA + sB + p) * (2 ** q - 1) + 3 ** N * (2 ** p - 1)) * j, ctx)
    T.exact("(3) auxiliary", (2 ** q - 1) * x == 2 ** sA * h - 3 ** b * j
            and (2 ** p - 1) * z == 3 ** a * h + 2 ** (sB + p) * j, ctx)
    # (4), (5), (6)
    th1 = 2 ** (sB + p + q) * x - 3 ** N * h
    th2 = 2 ** (sA + p) * t - 3 ** N * j
    T.exact("(4) identity I", th1 == 2 ** sB * y + (2 ** p - 1) * d * CB, ctx)
    T.exact("(5) identity II", th2 == 3 ** a * 2 ** q * x + d * CA, ctx)
    T.exact("(6) 0 < Theta1 < 2^(sB+p) y", 0 < th1 < 2 ** (sB + p) * y, ctx)
    T.exact("(6) 0 < Theta2 < 2^(sA+q) z", 0 < th2 < 2 ** (sA + q) * z, ctx)
    # (8) slopes, exact
    su = sA + sB
    T.exact("(8) y/x", 3 ** N * y < 2 ** (su + p + q) * x, ctx)
    T.exact("(8) z/t", 3 ** N * z < 2 ** (su + p) * t, ctx)
    T.exact("(8) t/z", 3 ** N * t < 2 ** (su + q) * z, ctx)
    T.exact("(8) x/y", 3 ** N * x < 2 ** su * y, ctx)
    T.exact("(9) sA+sB >= N", su >= N, ctx)
    # minimum, eta and the step bound
    M = min(st)
    T.exact("eta < 2N d/(3M) (step of (10))", (2 ** E - 3 ** (2 * N)) * 3 * M < 2 * N * d * 2 ** E, ctx)
    T.exact("step bound x' <= x (3+d/M)/2", all(st[(k + 1) % (2 * N)] * 2 * M <= st[k] * (3 * M + d)
                                                 for k in range(2 * N)), ctx)
    # paired states
    ok_pair, ok_formula = True, True
    pre = 0
    for i in range(a):
        diff = st[N + i] - st[i]
        if diff <= 0:
            ok_pair = False
        if diff * 2 ** pre != 3 ** i * (y - x):
            ok_formula = False
        pre += A[i]
    pre = 0
    for i in range(b):
        diff = st[a + i] - st[N + a + i]
        if (diff > 0) != (j > 0) or diff == 0:
            ok_pair = False
        if diff * 2 ** pre != 3 ** i * (z - t):
            ok_formula = False
        pre += B[i]
    T.exact("section 5 paired signs", ok_pair, ctx)
    T.exact("section 5 paired formula", ok_formula, ctx)
    pos = [k for k, s in enumerate(st) if s == M]
    T.exact("unique minimum", len(pos) == 1, ctx)
    k = pos[0]
    if j < 0:
        T.exact("j<0: minimum in the first half", k < N, ctx)
        case, i = ("I", k) if k < a else ("B", k - a)
    else:
        T.exact("j>0: minimum in first A or in B[q]", k < a or k >= N + a, ctx)
        case, i = ("II", k - N - a) if k >= N + a else ("C", k)
    CASES[case] += 1
    key = (tuple(A), tuple(B), p, q, d)
    if key not in DISTINCT:
        DISTINCT[key] = case
    if i == 0:
        EXTRA["min_at_block_start"] += 1
    else:
        EXTRA["interior_min_" + case] = EXTRA.get("interior_min_" + case, 0) + 1
    if tag == "P3":
        EXTRA["P3_case_" + case] = EXTRA.get("P3_case_" + case, 0) + 1
        EXTRA["P3_max_N"] = max(EXTRA.get("P3_max_N", 0), N)
    if case == "I":
        preA = sum(A[:i])
        T.exact("I: 2^pre M >= 3^i x", 2 ** preA * M >= 3 ** i * x, ctx)
        T.exact("I: 2^sA M >= 2^a x", 2 ** sA * M >= 2 ** a * x, ctx)
        T.exact("I: 2^q x > 3^b", 2 ** q * x > 3 ** b, ctx)
        T.exact("I: h 2^sA < y", h * 2 ** sA < y, ctx)
        T.exact("I: Theta1 h 2^sA < 2^(sB+p) y^2", th1 * h * 2 ** sA < 2 ** (sB + p) * y * y, ctx)
        T.exact("I: sA+sB >= N + X - ell (exact form)", 2 ** su * M >= 2 ** N * x, ctx)
        T.exact("remark I: Theta1 > 2^(sA+sB)", th1 > 2 ** su, ctx)
        T.exact("file2 I: y > 2^sA", y > 2 ** sA, ctx)
        U, V, c_exp, th = x, h, sB + p + q, th1
    elif case == "II":
        preB = sum(B[:i])
        T.exact("II: 2^pre M >= 3^i t", 2 ** preB * M >= 3 ** i * t, ctx)
        T.exact("II: 2^sB M >= 2^b t", 2 ** sB * M >= 2 ** b * t, ctx)
        T.exact("II: 2^p t > 3^a", 2 ** p * t > 3 ** a, ctx)
        T.exact("II: j 2^sB < z", j * 2 ** sB < z, ctx)
        T.exact("II: Theta2 j 2^sB < 2^(sA+q) z^2", th2 * j * 2 ** sB < 2 ** (sA + q) * z * z, ctx)
        T.exact("II: sA+sB >= N + T - ell (exact form)", 2 ** su * M >= 2 ** N * t, ctx)
        T.exact("remark II: Theta2 > 3^a 2^q x", th2 > 3 ** a * 2 ** q * x, ctx)
        T.exact("file2 II: z > 2^sB", z > 2 ** sB, ctx)
        U, V, c_exp, th = t, j, sA + p, th2
    elif case == "B":
        T.exact("B: t > 2^sB", t > 2 ** sB, ctx)
        T.exact("B: M 2^sB >= 3^i 2^(b-i) z", M * 2 ** sB >= 3 ** i * 2 ** (b - i) * z, ctx)
        T.exact("B: y > 2^sA", y > 2 ** sA, ctx)
        U = V = None
    else:
        T.exact("C: z > 2^sB", z > 2 ** sB, ctx)
        T.exact("C: y > 2^sA", y > 2 ** sA, ctx)
        T.exact("C: M 2^sA >= 3^i 2^(a-i) x", M * 2 ** sA >= 3 ** i * 2 ** (a - i) * x, ctx)
        U = V = None
    # real-number inequalities
    c = dict(a=a, b=b, N=N, p=p, q=q, sA=sA, sB=sB, E=E, d=d, M=M, x=x, z=z, y=y, t=t, h=h, j=j,
             th1=th1, th2=th2, case=case, i=i)
    res = reals(FloatR, c)
    need_dec = [nm for nm, (val, strict) in res.items() if abs(val) < 1e-6]
    if need_dec:
        resd = reals(DecR, c)
        EXTRA["decimal_fallbacks"] = EXTRA.get("decimal_fallbacks", 0) + 1
    for nm, (val, strict) in res.items():
        if nm in need_dec:
            val = resd[nm][0]
            T.slack(nm, val, strict, ctx, tol=DecR.tol)
        else:
            T.slack(nm, val, strict, ctx, tol=0)
    mutants(c)
    if case in ("I", "II"):
        if c["G"] > 0:
            EXTRA["gap_exponent_G_positive"] += 1
        if c["gapN25"] > 0:
            EXTRA["N_over_25_gap_holds"] += 1
        else:
            EXTRA["N_over_25_gap_fails"] += 1
        # ---------------- P5: the algebra of the Ridout step
        g = gcd(U, V)
        P, Q = 3 ** N * V // g, 2 ** c_exp * U // g
        T.exact("P5 gcd(P,Q) = 1", gcd(P, Q) == 1, ctx)
        T.exact("P5 gcd(U,6) = 1 and V odd", gcd(U, 6) == 1 and V % 2 == 1, ctx)
        T.exact("P5 v2(Q) = c exactly", v2(Q) == c_exp, ctx)
        T.exact("P5 v3(P) >= N", v3(P) >= N, ctx)
        T.exact("P5 Q - P = Theta/g > 0", Q - P == th // g and th % g == 0 and th > 0, ctx)
        T.exact("P5 c <= E", c_exp <= E, ctx)
        # Q |Q-P| |Q|_2 |P|_3 <= U Theta / (g^2 3^N)
        lhs = Fraction(Q * (Q - P), 2 ** v2(Q) * 3 ** v3(P))
        T.exact("P5 product <= U Theta/(g^2 3^N)", lhs <= Fraction(U * th, g * g * 3 ** N), ctx)
        # section 8 identity and isolation (brute force, capped)
        T.exact("(8) 3^N/Theta = U(2^c/(Theta V) - 1/(UV))",
                Fraction(3 ** N, th) == U * (Fraction(2 ** c_exp, th * V) - Fraction(1, U * V)), ctx)
        if not light:
            lim = min(3 ** N // (2 * th), 200)
            for Qp in range(1, lim + 1):
                base = 2 ** c_exp * Qp // 3 ** N
                for Pp in (base - 1, base, base + 1, base + 2):
                    if Pp * U == V * Qp:
                        continue
                    T.exact("(8) isolation brute force", abs(2 ** c_exp * Qp - 3 ** N * Pp) * U > th * Qp, ctx)
    return case


def bracket(w, r):
    return w[:-1] + [w[-1] + r]


def run_word(A, B, p, q, tag, light=False):
    W = A + B + bracket(A, p) + bracket(B, q)
    r = build_cycle(W)
    if r is None:
        EXTRA["nonpositive_D"] = EXTRA.get("nonpositive_D", 0) + 1
        return None
    d, st = r
    # independent second construction of the states on small words: C of the rotations
    if len(W) <= 8:
        E, L = sum(W), len(W)
        g = gcd(intercept(W), 2 ** E - 3 ** L)
        T.exact("states = C(rotations)/g", all(st[k] * g == intercept(W[k:] + W[:k]) for k in range(L)), tag)
    T.exact("built word has exactly 4 half-mismatches", mism(W, len(W) // 2) == 4, tag)
    return check_cycle(A, B, p, q, d, st, tag, light)


def part2():
    counts = {}
    # F1a: exhaustive, letters 1..3, block lengths <= 3, p,q <= 8
    n = 0
    small = [w for L in (1, 2, 3) for w in all_words(L, [1, 2, 3])]
    for A in small:
        for B in small:
            for p in range(1, 9):
                for q in range(1, 9):
                    if run_word(A, B, p, q, "F1a") is not None:
                        n += 1
    counts["F1a exhaustive letters<=3 len<=3 p,q<=8"] = n
    # F1b: exhaustive, letters 1..5, block lengths <= 2, p,q <= 10
    n = 0
    small = [w for L in (1, 2) for w in all_words(L, [1, 2, 3, 4, 5])]
    for A in small:
        for B in small:
            for p in range(1, 11):
                for q in range(1, 11):
                    if run_word(A, B, p, q, "F1b") is not None:
                        n += 1
    counts["F1b exhaustive letters<=5 len<=2 p,q<=10"] = n
    rng = random.Random(987654321)

    def geo():
        k = 1
        while rng.random() < 0.5 and k < 12:
            k += 1
        return k

    def rand_block(L, style):
        if style == 0:
            return [geo() for _ in range(L)]
        if style == 1:
            return [rng.choice([1, 1, 1, 2]) for _ in range(L)]
        if style == 2:
            return [rng.choice([1, 2, 3]) for _ in range(L)]
        if style == 3:
            return [1] * L
        return [rng.choice([2, 3, 4, 5, 6]) for _ in range(L)]

    # F2: random medium
    n = 0
    for _ in range(40000):
        style = rng.randrange(5)
        A = rand_block(rng.randint(1, 12), style)
        B = rand_block(rng.randint(1, 12), rng.choice([style, rng.randrange(5)]))
        mode = rng.randrange(4)
        if mode == 0:
            p, q = rng.randint(1, 6), rng.randint(1, 6)
        elif mode == 1:
            p, q = rng.randint(1, 40), rng.randint(1, 40)
        elif mode == 2:
            p = q = rng.randint(1, 30)
        else:
            p, q = rng.randint(1, 4), rng.randint(10, 60)
            if rng.random() < 0.5:
                p, q = q, p
        if run_word(A, B, p, q, "F2") is not None:
            n += 1
    counts["F2 random medium"] = n
    # F3: long
    n = 0
    for _ in range(600):
        style = rng.randrange(5)
        a, b = rng.randint(1, 200), rng.randint(1, 200)
        if rng.random() < 0.2:
            a = 1
        elif rng.random() < 0.2:
            b = 1
        A, B = rand_block(a, style), rand_block(b, rng.randrange(5))
        Nn = a + b
        mode = rng.randrange(3)
        if mode == 0:
            p, q = rng.randint(1, 10), rng.randint(1, 10)
        elif mode == 1:
            p, q = rng.randint(1, 2 * Nn), rng.randint(1, 2 * Nn)
        else:
            p, q = rng.randint(1, 5), rng.randint(Nn // 2 + 1, 2 * Nn)
            if rng.random() < 0.5:
                p, q = q, p
        if run_word(A, B, p, q, "F3", light=True) is not None:
            n += 1
    counts["F3 random long (N up to 400)"] = n
    # F4: very long
    n = 0
    for _ in range(24):
        a, b = rng.randint(300, 1200), rng.randint(300, 1200)
        A, B = rand_block(a, rng.choice([0, 1, 2, 3])), rand_block(b, rng.choice([0, 1, 2, 3]))
        Nn = a + b
        p, q = rng.randint(1, Nn), rng.randint(1, Nn)
        if run_word(A, B, p, q, "F4", light=True) is not None:
            n += 1
    counts["F4 very long (N up to 2400)"] = n
    # F5: adversarial shapes
    n = 0
    for L in range(1, 9):
        for r in range(1, 40):
            for (A, B, p, q) in (([1] * L, [1] * L, r, r), ([1] * L, [1], r, 2 * r), ([1], [1] * L, 2 * r, r),
                                 ([2] * L, [2] * L, r, r), ([1] * L, [2] * L, 1, r), ([2] * L, [1] * L, r, 1),
                                 ([1, 2] * L, [1, 2] * L, r, r + 1), ([3] * L, [1] * L, r + 1, r),
                                 ([1] * L, [1] * (L + 1), r, 40 - r)):
                if run_word(A, B, p, q, "F5") is not None:
                    n += 1
    counts["F5 adversarial shapes"] = n
    # F6: blocks of small letters with one or two large interior letters, small p, q (interior minima)
    n = 0
    for _ in range(40000):
        a, b = rng.randint(2, 7), rng.randint(2, 7)
        A = [rng.choice([1, 1, 2]) for _ in range(a)]
        B = [rng.choice([1, 1, 2]) for _ in range(b)]
        where = rng.randrange(3)
        if where in (0, 2):
            A[rng.randrange(a - 1)] = rng.randint(5, 14)
        if where in (1, 2):
            B[rng.randrange(b - 1)] = rng.randint(5, 14)
        p, q = rng.randint(1, 5), rng.randint(1, 5)
        if run_word(A, B, p, q, "F6") is not None:
            n += 1
    counts["F6 spiked blocks (interior minima)"] = n
    return counts


# ------------------------------------------------------------------ P3
def part3():
    out = {}
    found = 0
    examples = []
    for d in range(1, 1000):
        if gcd(d, 6) != 1:
            continue
        seen = {}
        for seed in range(1, 3001, 2):
            path = []
            n = seed
            while n not in seen:
                seen[n] = (seed, len(path))
                path.append(n)
                n = 3 * n + d
                n >>= v2(n)
            s0, idx = seen[n]
            if s0 != seed:
                continue
            cyc = path[idx:]
            L = len(cyc)
            if L % 2 or L < 4:
                continue
            W = [v2(3 * s + d) for s in cyc]
            if mism(W, L // 2) != 4:
                continue
            nf = normal_form(W)
            T.exact("P3 control normalises", nf is not None, (d, cyc[:4]))
            if nf is None:
                continue
            A, B, p, q, W2 = nf
            k = next(k for k in range(L) if W2 == W[k:] + W[:k] and
                     all(v2(3 * cyc[(k + m) % L] + d) == W2[m] for m in range(L)))
            st = cyc[k:] + cyc[:k]
            case = check_cycle(A, B, p, q, d, st, "P3")
            found += 1
            if len(examples) < 6:
                examples.append((d, min(cyc), L, case))
    out["half_period_four_mismatch_cycles_found_by_iteration"] = found
    out["examples (d, min, length, case)"] = examples
    # the two named controls, by direct iteration
    def iterate(seed, d):
        cyc, n = [], seed
        while True:
            cyc.append(n)
            n = 3 * n + d
            n >>= v2(n)
            if n == seed:
                return cyc
    c47 = iterate(73, 47)
    W47 = [v2(3 * s + 47) for s in c47]
    T.exact("control 3x+47 word (1,1,2,3)", W47 == [1, 1, 2, 3], W47)
    out["3x+47"] = (c47, check_cycle([1], [1], 1, 2, 47, c47, "ctl47"))
    c1631 = iterate(9145, 1631)
    W1631 = [v2(3 * s + 1631) for s in c1631]
    T.exact("control 3x+1631 word", W1631 == [1, 1, 2, 1, 1, 2, 2, 3], W1631)
    out["3x+1631"] = (c1631, check_cycle([1, 1], [2, 1], 1, 2, 1631, c1631, "ctl1631"))
    return out


# ------------------------------------------------------------------ P4
def cf(num, den):
    q, conv = [], []
    p0, q0, p1, q1 = 0, 1, 1, 0
    while den:
        a, r = divmod(num, den)
        q.append(a)
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        conv.append((p1, q1))
        num, den = den, r
    return q, conv


def part4():
    rng = random.Random(4242)
    iso = leg = 0
    for N in range(3, 34):
        for c in range(max(1, int(1.2 * N)), 2 * N + 4):
            A3, A2 = 3 ** N, 2 ** c
            quots, conv = cf(A2, A3)
            cands = [(Q, P) for (P, Q) in conv[:-1] if P > 0]
            cands += [(Q * m, P * m) for (Q, P) in list(cands) for m in (2, 3, 5, 11)]
            for _ in range(6):
                U = rng.randint(1, 60)
                cands.append((U, A2 * U // A3))
            for (U, V) in cands:
                if V <= 0:
                    continue
                th = A2 * U - A3 * V
                if th <= 0:
                    continue
                # isolation: P'/Q' != V/U at least as close  =>  Q' >= 3^N/(2 Theta)
                lim = min(A3 // (2 * th), 300)
                for Qp in range(1, lim + 1):
                    base = A2 * Qp // A3
                    for Pp in (base - 1, base, base + 1, base + 2):
                        if Pp * U == V * Qp:
                            continue
                        iso += 1
                        T.exact("P4 isolation", abs(A2 * Qp - A3 * Pp) * U > th * Qp, (N, c, U, V, Pp, Qp))
                # Legendre remark: if R = 2^c/(Theta V) > 3 then V/U reduced is a convergent and the
                # next partial quotient exceeds R - 3
                R = Fraction(A2, th * V)
                if R > 3:
                    g = gcd(U, V)
                    red = (V // g, U // g)
                    idx = [k for k, pq in enumerate(conv) if pq == red]
                    leg += 1
                    T.exact("P4 Legendre: V/U is a convergent", len(idx) == 1 and idx[0] + 1 < len(quots), (N, c, U, V))
                    if len(idx) == 1 and idx[0] + 1 < len(quots):
                        T.exact("P4 next partial quotient > R - 3", quots[idx[0] + 1] > R - 3, (N, c, U, V))
    return {"isolation_competitors": iso, "legendre_cases": leg}


# ------------------------------------------------------------------ P6
def part6():
    """Exact slack decompositions behind (12), (13), (11), and the Ridout chain on synthetic data."""
    rng = random.Random(606)

    def rf(lo, hi):
        return Fraction(rng.randint(lo * 1000, hi * 1000), 1000)

    n_id = 0
    for _ in range(20000):
        al = Fraction(rng.randint(1010, 1990), 1000)
        a, b, sA, sB, X, ell, tau = rf(1, 50), rf(1, 50), rf(1, 200), rf(1, 200), rf(-50, 200), rf(0, 80), rf(0, 9)
        p, q, kap = rng.randint(1, 60), rng.randint(1, 60), rf(1, 2)
        N = a + b
        c0 = 1 - al + 1 / al
        xmax = (al - 1) * N + tau + ell - Fraction(p + q, 2)
        rhs12 = c0 * N + (1 - 1 / al) * Fraction(q - p, 2) - (1 + 1 / al) * tau - (2 + 1 / al) * ell
        T.exact("P6 (12) = slack(i) + slack(ii) + (1+1/alpha) slack(iii), exact identity",
                (sA - 2 * X - p) - rhs12 == (sA - (a + X - ell)) + ((X + q) / al - b) + (1 + 1 / al) * (xmax - X))
        rhs13 = (c0 * N + (1 - 1 / al) * Fraction(p, 2) + (1 + 1 / al) * Fraction(q, 2)
                 - (1 + 1 / al) * tau - (2 + 1 / al) * ell)
        T.exact("P6 (13) = slack(i') + slack(ii') + (1+1/alpha) slack(iii'), exact identity",
                (sB - 2 * X) - rhs13 == (sB - (b + X - ell)) + ((X + p) / al - a) + (1 + 1 / al) * (xmax - X))
        rhs11 = (1 + kap) * ell + kap * (al - 1) * N + 2 * kap * tau
        s3 = (al - 1) * N + tau - Fraction(p + q, 2)
        T.exact("P6 (11) case B decomposition",
                rhs11 - N == (ell + (kap - 1) * b - a) + kap * (ell + Fraction(q - p, 2) + tau - b) + kap * s3 + kap * p)
        T.exact("P6 (11) case C decomposition",
                rhs11 - N == (ell + (kap - 1) * a - b) + kap * (ell + Fraction(p + q, 2) + tau - a) + kap * s3)
        # final gap exponents
        T.exact("P6 exponent bookkeeping I", sB + p - sA + 2 * (Fraction(p + q, 2) + tau + X)
                == (sB + p + q) + 2 * tau - (sA - 2 * X - p))
        T.exact("P6 exponent bookkeeping II", sA + q - sB + 2 * (Fraction(p - q, 2) + tau + X)
                == (sA + p) + 2 * tau - (sB - 2 * X))
        n_id += 1
    # synthetic solutions of (1) in file 2: N multiple of 25, K = N/25
    hits = skipped = 0
    for N in range(75, 401, 25):
        K = N // 25
        for c in range(int(1.585 * N) - 40, int(1.585 * N) + 41):
            if not (3 * c > N and c < 4 * N):
                continue
            A3, A2 = 3 ** N, 2 ** c
            _, conv = cf(A2, A3)
            for (V, U) in conv[:-1]:
                if V <= 0 or U >= 2 ** N:
                    continue
                th = A2 * U - A3 * V
                if th <= 0 or th * V * 2 ** K >= A2:
                    continue
                if U % 2 == 0 or U % 3 == 0 or V % 2 == 0:
                    skipped += 1
                    continue
                hits += 1
                g = gcd(U, V)
                P, Q = A3 * V // g, A2 * U // g
                T.exact("P6 Ridout: gcd(P,Q)=1", gcd(P, Q) == 1)
                T.exact("P6 Ridout: Q/2 < P < Q", Q < 2 * P and P < Q)
                lhs = Fraction(Q * (Q - P), 2 ** v2(Q) * 3 ** v3(P))
                T.exact("P6 Ridout: chain (2) < 2^(1-N/25)", lhs <= Fraction(U * th, g * g * A3)
                        and Fraction(U * th, g * g * A3) < Fraction(Q, P) / 2 ** K and lhs * 2 ** K < 2)
                T.exact("P6 Ridout: Q < 2^(5N)", Q < 2 ** (5 * N))
                T.exact("P6 Ridout: (3) with eps = 1/250", lhs ** 250 * Q < 1)
                # Bilu's form: product of the three local factors times H^2 equals the left side of (3)
                bilu = Fraction(Q - P, Q) * Fraction(1, 2 ** v2(Q)) * Fraction(1, 3 ** v3(P))
                T.exact("P6 Ridout: Bilu product * H^2 = Waldschmidt left side", bilu * Q * Q == lhs)
    return {"identity_samples": n_id, "synthetic_ridout_solutions": hits, "synthetic_skipped_parity": skipped}


def main():
    out = {}
    out["P0"] = part0()
    out["P1"] = part1()
    out["P2"] = part2()
    out["P3"] = part3()
    out["P4"] = part4()
    out["P6"] = part6()
    total_cycles = sum(CASES.values())
    out["cycles_tested"] = total_cycles
    out["distinct_cycles_tested"] = len(DISTINCT)
    dc = {}
    for v in DISTINCT.values():
        dc[v] = dc.get(v, 0) + 1
    out["distinct_cases"] = dc
    out["cases"] = dict(CASES)
    out["extra"] = dict(EXTRA)
    out["checks"] = {k: {"n": T.n[k], "violations": T.bad.get(k, 0),
                         **({"min_slack": T.minslack[k]} if k in T.minslack else {})} for k in sorted(T.n)}
    out["violations_total"] = sum(T.bad.values())
    out["mutants (name: [evaluated, detected])"] = MUT
    out["violation_examples"] = {k: repr(v)[:300] for k, v in T.examples.items()}
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    print("cycles tested:", total_cycles, "cases:", CASES)
    print("distinct cycles:", len(DISTINCT), "distinct cases:", dc)
    print("extra:", EXTRA)
    print("P0:", out["P0"])
    print("P1:", out["P1"])
    print("P2:", out["P2"])
    print("P3:", {k: (v if k != "examples (d, min, length, case)" else v) for k, v in out["P3"].items()})
    print("P4:", out["P4"])
    print("P6:", out["P6"])
    print("distinct checks:", len(T.n), " total evaluations:", sum(T.n.values()))
    print("VIOLATIONS:", out["violations_total"])
    for k, v in T.bad.items():
        print("  FAIL", k, v, "of", T.n[k], "e.g.", repr(T.examples.get(k))[:200])
    print("mutation test (wrong variants; evaluated / detected):")
    for k, (n_, det) in sorted(MUT.items()):
        print(f"  {n_:>7} / {det:>7}  {k}")
    worst = sorted(((v, k) for k, v in T.minslack.items()))[:12]
    print("smallest real slacks:")
    for v, k in worst:
        print(f"  {v:.3e}  {k}")
    return 1 if out["violations_total"] else 0


if __name__ == "__main__":
    sys.exit(main())
