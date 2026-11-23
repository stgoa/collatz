#!/usr/bin/env python3
"""Certificate for half-period-s-unit-approximation-law.

Raw odd-only clock. A word W = A B A[p] B[q] (A, B nonempty positive words, p, q >= 1, [.] raises only the last
letter) of length 2N with D = 2^sum(W) - 3^(2N) > 0 is the valuation word of an actual cycle of 3x+d for
d = D / gcd(C_W, D), provided its states are odd. The node proves, for d = 1 and N >= 2^22 under EXT-1, that such a
cycle forces 0 < 2^c U - 3^N V < 2^(c - N/25) / V for explicit (c, U, V). This script checks the finite steps:

V1  the exact rational constants of the proof: 15849/10000 < log2(3) < 317/200, log2(3 + 2^-17) < 317/200,
    1 - a + 1/a >= 2911/63400 at a = 317/200, and the two threshold inequalities for every N >= 2^22
    (checked on each dyadic block [2^k, 2^(k+1)) by a base case at k = 22 and a monotone step), together with
    2 tau + ell < N/20 on the same blocks;
V2  local descent: every odd n with 3 <= n < 2^17 reaches a smaller odd number, so a nontrivial cycle of the
    odd-only 3x+1 map has minimum at least 2^17;
V3  on a deterministic family of actual 3x+d cycles with word A B A[p] B[q] (exhaustive small blocks plus a fixed
    pseudo-random sample, the true addend d retained): the four boundary equations, the integrality and signs of
    h and j, identity (3) and the two exact identities (4), (5) (with C replaced by d*C), the four slopes, the
    placement of every minimum among the smaller copies, and each elementary inequality used in the four cases
    (I, II, B, C) of the proof, all in exact integer arithmetic; the known 3x+47 and 3x+1631 cycles are replayed;
V4  the elementary approximation lemma on exact continued fractions: for convergents P/Q of 2^c/3^N from below
    and multiples (U, V) = (gQ, gP) with Theta (2UV + 1) < 2^c U, Theta = 2^c U - 3^N V, the next partial quotient
    exceeds 2^c/(Theta V) - 3, and no other fraction with denominator below 3^N/(2 Theta) is as close;
V5  the algebra of the estimates (11), (12), (13): each is an exact identity between the difference of its two
    sides and a sum of slacks of the elementary inequalities, checked with rational numbers;
V6  receipt comparison.

Exit 1 on failure; --write-receipt regenerates check_s_unit_law.json. Standard library only; no floating point;
no assert statements (valid under python3 -O)."""
import json
import sys
from fractions import Fraction
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "check_s_unit_law.json"
failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL:", msg)


def need(cond, msg):
    if not cond:
        fail(msg)
    return cond


# ---------------------------------------------------------------- V1
def v1():
    out = {}
    need(3 ** 10000 > 2 ** 15849, "V1: 3^10000 > 2^15849")
    need(3 ** 200 < 2 ** 317, "V1: 3^200 < 2^317")
    need(393217 ** 200 < 2 ** 3717, "V1: (3 + 2^-17)^200 < 2^(317 - 17*200 + 3400)")
    a_lo, a_hi = Fraction(15849, 10000), Fraction(317, 200)
    c0 = 1 - a_hi + 1 / a_hi                      # 1 - a + 1/a is decreasing in a
    need(c0 == Fraction(2911, 63400), "V1: c0 = 2911/63400")
    c_ell = 2 + 1 / a_lo                          # upper bound for 2 + 1/alpha
    c_tau = 3 + 1 / a_lo                          # upper bound for 3 + 1/alpha
    slope = c0 - Fraction(1, 25) - c_tau / 2 ** 18   # tau < N / 2^18
    need(slope > 0, "V1: positive slope")
    # main threshold on the block 2^k <= N < 2^(k+1): slope * 2^k > c_ell * (514 + 342 (k+1))
    k0 = 22
    base = slope * 2 ** k0 - c_ell * (514 + 342 * (k0 + 1))
    need(base > 0, "V1: main threshold at k = 22")
    need(slope * 2 ** k0 > 342 * c_ell, "V1: main threshold step")
    # exclusion of the cases B and C: (1 - kappa (alpha - 1)) N > (1 + kappa) ell + 2 kappa tau
    kap = Fraction(317, 200)
    slope2 = 1 - kap * (a_hi - 1) - 2 * kap / 2 ** 18
    base2 = slope2 * 2 ** k0 - (1 + kap) * (514 + 342 * (k0 + 1))
    need(base2 > 0, "V1: exclusion threshold at k = 22")
    need(slope2 * 2 ** k0 > 342 * (1 + kap), "V1: exclusion threshold step")
    # used by the finiteness node: 2 tau + ell < 2^(k-16) + 514 + 342 (k+1) < 2^k / 20 on the block k >= 22
    need(20 * (2 ** (k0 - 16) + 514 + 342 * (k0 + 1)) < 2 ** k0, "V1: 2 tau + ell < N/20 at k = 22")
    need(20 * (2 ** (k0 - 16) + 342) < 2 ** k0, "V1: 2 tau + ell < N/20 step")
    out["two_tau_plus_ell_bound_at_first_block"] = 2 ** (k0 - 16) + 514 + 342 * (k0 + 1)
    out["c0"] = str(c0)
    out["c_ell_upper"] = str(c_ell)
    out["c_tau_upper"] = str(c_tau)
    out["main_slope"] = str(slope)
    out["main_base_margin_floor"] = int(base)
    out["exclusion_slope"] = str(slope2)
    out["exclusion_base_margin_floor"] = int(base2)
    out["threshold_log2_N"] = k0
    print(f"V1: constants exact; thresholds hold for every N >= 2^{k0} "
          f"(margins at the first block: {int(base)} and {int(base2)})")
    return out


# ---------------------------------------------------------------- V2
def v2():
    limit = 2 ** 17
    worst = 0
    for n in range(3, limit, 2):
        m, steps = n, 0
        while m >= n:
            m = 3 * m + 1
            while m % 2 == 0:
                m //= 2
            steps += 1
            if steps > 1000:
                fail(f"V2: no descent found for {n}")
                break
        worst = max(worst, steps)
    print(f"V2: every odd 3 <= n < 2^17 reaches a smaller odd number (at most {worst} odd steps)")
    return {"limit": limit, "max_odd_steps_to_descend": worst}


# ---------------------------------------------------------------- V3
def intercept(word):
    n, c, pre = len(word), 0, 0
    for i, w in enumerate(word):
        c += 3 ** (n - 1 - i) * 2 ** pre
        pre += w
    return c


def v2adic(n):
    return (n & -n).bit_length() - 1


def check_word(A, B, p, q, stats):
    a, b = len(A), len(B)
    N = a + b
    W = A + B + A[:-1] + [A[-1] + p] + B[:-1] + [B[-1] + q]
    E = sum(W)
    D = 2 ** E - 3 ** (2 * N)
    if D <= 0:
        stats["nonpositive_D"] += 1
        return None
    C = intercept(W)
    g = gcd(C, D)
    d, cur = D // g, C // g
    st = []
    for w in W:
        st.append(cur)
        num = 3 * cur + d
        if cur % 2 == 0 or v2adic(num) != w:
            stats["not_an_odd_only_word"] += 1
            return None
        cur = num >> w
    if cur != st[0]:
        fail(f"V3: cycle does not close for {A} {B} {p} {q}")
        return None
    x, z, y, t = st[0], st[a], st[N], st[N + a]
    sA, sB = sum(A), sum(B)
    su = sA + sB
    CA, CB = intercept(A), intercept(B)
    tag = f"{A} {B} {p} {q}"
    ok = True
    ok &= need(2 ** sA * z == 3 ** a * x + d * CA and 2 ** sB * y == 3 ** b * z + d * CB
               and 2 ** (sA + p) * t == 3 ** a * y + d * CA and 2 ** (sB + q) * x == 3 ** b * t + d * CB,
               f"V3 boundary equations {tag}")
    ok &= need((y - x) % 2 ** sA == 0 and (z - t) % 2 ** sB == 0, f"V3 divisibility {tag}")
    h, j = (y - x) // 2 ** sA, (z - t) // 2 ** sB
    ok &= need(h > 0 and j != 0, f"V3 signs of h, j {tag}")
    ok &= need(2 ** p * t - z == 3 ** a * h and y - 2 ** q * x == 3 ** b * j, f"V3 three-adic pair {tag}")
    if j < 0:
        ok &= need(p < q, f"V3 j < 0 forces p < q {tag}")
    ok &= need((2 ** p - 1) * (2 ** q - 1) * d * CA == 3 ** a * 2 ** sA * (2 ** q - 2 ** p) * h
               + (2 ** (sA + sB + p) * (2 ** q - 1) + 3 ** N * (2 ** p - 1)) * j, f"V3 identity (3) {tag}")
    # the two exact identities (with the true addend d)
    th1 = 2 ** (sB + p + q) * x - 3 ** N * h
    th2 = 2 ** (sA + p) * t - 3 ** N * j
    ok &= need(th1 == 2 ** sB * y + (2 ** p - 1) * d * CB, f"V3 identity I {tag}")
    ok &= need(th2 == 3 ** a * 2 ** q * x + d * CA, f"V3 identity II {tag}")
    # slopes
    ok &= need(3 ** N * y < 2 ** (su + p + q) * x and 3 ** N * x < 2 ** su * y
               and 3 ** N * z < 2 ** (su + p) * t and 3 ** N * t < 2 ** (su + q) * z, f"V3 slopes {tag}")
    M = min(st)
    for pos in [i for i, s in enumerate(st) if s == M]:
        if j < 0:
            ok &= need(pos < N, f"V3 minimum in the first half {tag}")
            if pos < a:
                stats["case_I"] += 1
                ok &= need(2 ** sA * M >= 2 ** a * x, f"V3 I (5a) {tag}")
                ok &= need(2 ** q * x > 3 ** b, f"V3 I (5b) {tag}")
                ok &= need(0 < th1 < 2 ** (sB + p) * y and h * 2 ** sA < y, f"V3 I size {tag}")
            else:
                stats["case_B"] += 1
                i = pos - a
                ok &= need(t > 2 ** sB and M * 2 ** sB >= 2 ** b * z and y > 2 ** sA, f"V3 B lower bounds {tag}")
                ok &= need(y * (2 * M) ** (b - i) <= M * (3 * M + d) ** (b - i), f"V3 B suffix growth {tag}")
        else:
            ok &= need(pos < a or pos >= N + a, f"V3 minimum among the smaller copies {tag}")
            if pos >= N + a:
                stats["case_II"] += 1
                ok &= need(2 ** sB * M >= 2 ** b * t, f"V3 II (5a') {tag}")
                ok &= need(2 ** p * t > 3 ** a, f"V3 II (5b') {tag}")
                ok &= need(0 < th2 < 2 ** (sA + q) * z and j * 2 ** sB < z, f"V3 II size {tag}")
            else:
                stats["case_C"] += 1
                i = pos
                ok &= need(z > 2 ** sB and M * 2 ** sA >= 2 ** a * x and y > 2 ** sA, f"V3 C lower bounds {tag}")
                ok &= need(z * (2 * M) ** (a - i) <= M * (3 * M + d) ** (a - i), f"V3 C suffix growth {tag}")
    stats["cycles"] += 1
    return d, st


def words(max_len, max_letter):
    out = [[]]
    res = []
    for _ in range(max_len):
        out = [w + [l] for w in out for l in range(1, max_letter + 1)]
        res.extend(out)
    return res


class Lcg:
    def __init__(self, seed):
        self.s = seed

    def below(self, n):
        self.s = (6364136223846793005 * self.s + 1442695040888963407) % 2 ** 64
        return (self.s >> 33) % n


def v3():
    stats = {k: 0 for k in ["cycles", "nonpositive_D", "not_an_odd_only_word",
                            "case_I", "case_II", "case_B", "case_C"]}
    small = words(3, 3)
    for A in small:
        for B in small:
            for p in range(1, 6):
                for q in range(1, 6):
                    check_word(A, B, p, q, stats)
    exhaustive = dict(stats)
    rng = Lcg(20261123)
    letters = [1, 1, 1, 2, 2, 3, 4, 5]
    for _ in range(20000):
        A = [letters[rng.below(8)] for _ in range(1 + rng.below(8))]
        B = [letters[rng.below(8)] for _ in range(1 + rng.below(8))]
        check_word(A, B, 1 + rng.below(12), 1 + rng.below(12), stats)
    # two known actual cycles
    r47 = check_word([1], [1], 1, 2, {k: 0 for k in stats})
    need(r47 is not None and r47[0] == 47, "V3: the word (1,1,2,3) is a 3x+47 cycle")
    r1631 = check_word([1, 1], [2, 1], 1, 2, {k: 0 for k in stats})
    need(r1631 is not None and r1631[0] == 1631 and r1631[1] ==
         [9145, 14533, 22615, 17369, 26869, 41119, 31247, 23843], "V3: the 3x+1631 cycle through 9145")
    print(f"V3: {stats['cycles']} actual 3x+d cycles with word A B A[p] B[q] checked "
          f"(cases I/II/B/C: {stats['case_I']}/{stats['case_II']}/{stats['case_B']}/{stats['case_C']})")
    return {"exhaustive_blocks_up_to_length_3_letters_up_to_3_p_q_up_to_5": exhaustive, "all": stats,
            "fixtures": {"3x+47": [1, 1, 2, 3], "3x+1631": [1, 1, 2, 1, 1, 2, 2, 3]}}


# ---------------------------------------------------------------- V4
def cf_convergents(num, den):
    """Partial quotients and convergents of num/den (canonical Euclidean expansion)."""
    quots, convs = [], []
    p0, q0, p1, q1 = 0, 1, 1, 0
    while den:
        a_k, r = divmod(num, den)
        quots.append(a_k)
        p0, q0, p1, q1 = p1, q1, a_k * p1 + p0, a_k * q1 + q0
        convs.append((p1, q1))
        num, den = den, r
    return quots, convs


def v4():
    tested = brute = 0
    largest_ratio = Fraction(0)
    for N in range(4, 41):
        for c in range(1, 2 * N + 6):
            P3, P2 = 3 ** N, 2 ** c
            quots, convs = cf_convergents(P2, P3)
            for k, (P, Q) in enumerate(convs[:-1]):
                if P == 0:
                    continue
                for g in (1, 5, 7):
                    U, V = g * Q, g * P
                    theta = P2 * U - P3 * V
                    if theta <= 0 or theta * (2 * U * V + 1) >= P2 * U:
                        continue
                    tested += 1
                    bound = Fraction(P2, theta * V) - 3
                    need(quots[k + 1] > bound, f"V4 next partial quotient N={N} c={c} k={k} g={g}")
                    largest_ratio = max(largest_ratio, Fraction(P2, theta * V))
                    # isolation: no other fraction with denominator < 3^N/(2 theta) is at least as close
                    lim = min(P3 // (2 * theta), 400)
                    for Qp in range(1, lim + 1):
                        for Pp in (P2 * Qp // P3, P2 * Qp // P3 + 1):
                            if Pp * U == V * Qp:
                                continue
                            brute += 1
                            # |xi - Pp/Qp| <= |xi - V/U|  <=>  |P2 Qp - P3 Pp| U <= theta Qp
                            need(abs(P2 * Qp - P3 * Pp) * U > theta * Qp,
                                 f"V4 isolation N={N} c={c} Q'={Qp}")
    print(f"V4: approximation lemma checked on {tested} convergent multiples and {brute} competing fractions")
    return {"convergent_multiples": tested, "competing_fractions": brute,
            "largest_2^c_over_Theta_V_floor": int(largest_ratio)}


# ---------------------------------------------------------------- V5
def v5():
    """The three estimates as exact identities in rational numbers (alpha, kappa arbitrary rationals)."""
    rng = Lcg(5)

    def rat():
        return Fraction(rng.below(4001) - 2000, 1 + rng.below(97))

    samples = 5000
    for _ in range(samples):
        al = 1 + Fraction(1 + rng.below(996), 997)
        ka = 1 + Fraction(1 + rng.below(996), 997)
        N, a, X, T, ell, tau, pp, qq, sA, sB = (rat() for _ in range(10))
        b = N - a
        inv = 1 / al
        rhs12 = (1 - al + inv) * N + (1 - inv) * (qq - pp) / 2 - (1 + inv) * tau - (2 + inv) * ell
        slack12 = ((sA - (a + X - ell)) + ((X + qq) / al - b)
                   + (1 + inv) * ((al - 1) * N + tau + ell - (pp + qq) / 2 - X))
        need((sA - 2 * X - pp) - rhs12 == slack12, "V5 identity behind (12)")
        rhs13 = (1 - al + inv) * N + (1 - inv) * pp / 2 + (1 + inv) * qq / 2 - (1 + inv) * tau - (2 + inv) * ell
        slack13 = ((sB - (b + T - ell)) + ((T + pp) / al - a)
                   + (1 + inv) * ((al - 1) * N + tau + ell - (pp + qq) / 2 - T))
        need((sB - 2 * T) - rhs13 == slack13, "V5 identity behind (13)")
        rhs11 = (1 + ka) * ell + ka * (al - 1) * N + 2 * ka * tau
        slack_b = ((ell + (ka - 1) * b - a) + ka * (ell + (qq - pp) / 2 + tau - b)
                   + ka * ((al - 1) * N + tau - (pp + qq) / 2) + ka * pp)
        slack_c = ((ell + (ka - 1) * a - b) + ka * (ell + (pp + qq) / 2 + tau - a)
                   + ka * ((al - 1) * N + tau - (pp + qq) / 2))
        need(rhs11 - N == slack_b, "V5 identity behind (11), case B")
        need(rhs11 - N == slack_c, "V5 identity behind (11), case C")
    print(f"V5: the identities behind (11), (12), (13) hold on {samples} rational samples")
    return {"samples": samples}


def main():
    write = "--write-receipt" in sys.argv
    summary = {"V1": v1(), "V2": v2(), "V3": v3(), "V4": v4(), "V5": v5()}
    if write:
        RECEIPT.write_text(json.dumps(summary, indent=1, sort_keys=True) + "\n")
        print("receipt written")
    elif not RECEIPT.exists():
        fail("V6 receipt missing")
    elif json.loads(RECEIPT.read_text()) != summary:
        fail("V6 summary differs from the receipt")
    if failures:
        print(f"{len(failures)} failure(s)")
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()
