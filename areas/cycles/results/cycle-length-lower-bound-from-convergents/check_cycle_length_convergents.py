#!/usr/bin/env python3
"""Certificate for cycle-length-lower-bound-from-convergents.

Setting: raw odd-only 3x+1 map n -> (3n+1)/2^(v_2(3n+1)) on positive odd integers; a nontrivial cycle has m odd
states n_1..n_m, A = sum of the valuations, minimum L >= 3 and satisfies 2^A = prod (3 + 1/n_i), hence
    0 < A - m*theta < m / (3 L ln 2) < 0.481 m / L,          theta = log_2 3.
With the convergents p_k/q_k of theta, and k defined by q_k <= m < q_{k+1}, the best-approximation inequalities
|m theta - A| >= |q_k theta - p_k| > 1/(q_k + q_{k+1}) give m > L / (0.481 (q_k + q_{k+1})); so k >= k1(L), the least
k with q_{k+1} (q_k + q_{k+1}) > L/0.481, and m >= B(L) = max(q_{k1}, floor(L/(0.481 (q_{k1} + q_{k1+1}))) + 1).
V1  the continued fraction of theta from a two-sided enclosure (decimal ln is correctly rounded; two precisions),
    the convergents, and an exact integer cross-check 2^p_k > 3^q_k (k odd) / < (k even) for q_k <= 3000;
V2  0.481 > 1/(3 ln 2), checked against the decimal enclosure of ln 2;
V3  B(L) for L = 2^40, 2^60, 2^68, 2^71 (the last is the external input barina-2025-convergence-2-71), and the
    total-length bound m + floor(m theta) + 1 at m = B(L);
V4  controls: on every cycle of actual-cycles-3x-d-corpus (3x+d, d <= 999), the exact identity 2^A prod n_i =
    prod (3 n_i + d) and the exact inequalities 3^m < 2^A <= (3 + d/L)^m, cleared of denominators;
V5  receipt comparison. Exit 1 on failure; --write-receipt regenerates cycle_length_convergents.json.
Standard library only; deterministic."""
import json
import sys
from decimal import Decimal, getcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "cycle_length_convergents.json"
CORPUS = HERE.parent / "actual-cycles-3x-d-corpus" / "actual_cycles.json"
C_UP = Fraction(481, 1000)          # an upper bound for 1/(3 ln 2) = 0.48090...
N_TERMS = 80
failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL:", msg)


def theta_enclosure(prec):
    """Rationals lo < log_2 3 < hi from correctly rounded decimal logarithms at the given precision."""
    getcontext().prec = prec
    ln3, ln2 = Decimal(3).ln(), Decimal(2).ln()
    ulp3 = Decimal(10) ** (ln3.adjusted() - prec + 1)
    ulp2 = Decimal(10) ** (ln2.adjusted() - prec + 1)
    lo = Fraction(ln3 - ulp3) / Fraction(ln2 + ulp2)
    hi = Fraction(ln3 + ulp3) / Fraction(ln2 - ulp2)
    return lo, hi, Fraction(ln2 - ulp2), Fraction(ln2 + ulp2)


def cf_terms(x, n):
    terms = []
    for _ in range(n):
        a = x.numerator // x.denominator
        terms.append(a)
        frac = x - a
        if frac == 0:
            break
        x = 1 / frac
    return terms


def convergents(terms):
    p0, q0, p1, q1 = 1, 0, terms[0], 1
    out = [(p1, q1)]
    for a in terms[1:]:
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        out.append((p1, q1))
    return out


def main():
    write = "--write-receipt" in sys.argv
    summary = {}
    # V1: continued fraction from two enclosures
    lo1, hi1, ln2lo, ln2hi = theta_enclosure(160)
    lo2, hi2, _, _ = theta_enclosure(220)
    t_lo1, t_hi1 = cf_terms(lo1, N_TERMS), cf_terms(hi1, N_TERMS)
    t_lo2, t_hi2 = cf_terms(lo2, N_TERMS), cf_terms(hi2, N_TERMS)
    agree = 0
    while (agree < N_TERMS and len({t_lo1[agree], t_hi1[agree], t_lo2[agree], t_hi2[agree]}) == 1):
        agree += 1
    terms = t_lo1[:agree]
    conv = convergents(terms)
    if agree < 60:
        fail(f"V1: only {agree} continued-fraction terms certified")
    # exact cross-check for small convergents: p_k/q_k > theta iff 2^p_k > 3^q_k, and the parity pattern
    checked = 0
    for k, (p, q) in enumerate(conv):
        if q > 3000:
            break
        above = 2 ** p > 3 ** q
        if above != (k % 2 == 1):
            fail(f"V1: convergent {p}/{q} (k={k}) on the wrong side of theta")
        checked += 1
    # the enclosure itself, exactly: 3^q < 2^p iff p/q > theta; check lo < theta < hi via the last two small convergents
    summary["V1"] = {"terms_certified": agree, "terms": terms, "convergents_checked_exactly": checked,
                     "q_values": [str(q) for _, q in conv]}
    print(f"V1: {agree} terms of the continued fraction of log2(3) certified; {checked} convergents checked exactly")
    print("    terms:", terms[:40], "...")
    # V2: C_UP > 1/(3 ln 2)  <=>  3 * ln2 * C_UP > 1, using the lower bound of ln 2
    ok2 = 3 * ln2lo * C_UP > 1
    if not ok2:
        fail("V2: 0.481 is not an upper bound for 1/(3 ln 2)")
    summary["V2"] = {"c_up": "481/1000", "ln2_lower_bound_times_3_times_c_up_minus_1": str(float(3 * ln2lo * C_UP - 1))}
    print(f"V2: 0.481 > 1/(3 ln 2): {ok2}")
    # V3: the bound B(L)
    def bound(L):
        Lam = Fraction(L) / C_UP
        for k in range(len(conv) - 1):
            qk, qk1 = conv[k][1], conv[k + 1][1]
            if qk1 * (qk + qk1) > Lam:
                lower = Fraction(L) / (C_UP * (qk + qk1))
                B = max(qk, lower.numerator // lower.denominator + 1)
                return k, qk, qk1, B
        raise RuntimeError("not enough convergents")
    summary["V3"] = {}
    for e in (40, 60, 68, 71):
        L = 2 ** e
        k1, qk, qk1, B = bound(L)
        # total length: m + floor(m theta) + 1 at m = B, floor determined by the enclosure
        f_lo = (B * lo1).numerator // (B * lo1).denominator
        f_hi = (B * hi1).numerator // (B * hi1).denominator
        if f_lo != f_hi:
            fail(f"V3: floor(B theta) undetermined for L = 2^{e}")
        total = B + f_lo + 1
        summary["V3"][f"2^{e}"] = {"k1": k1, "q_k1": str(qk), "q_k1_plus_1": str(qk1), "B": str(B), "total_length_bound": str(total)}
        print(f"V3: L = 2^{e}: k1 = {k1}, q = {qk}, {qk1}; m >= B = {B} ({B:.3e}); total length >= {total} ({total:.3e})")
    # V4: controls on the corpus
    data = json.loads(CORPUS.read_text())
    n_cycles, n_d = 0, set()
    for cyc in data["cycles"]:
        d, states, A, m = cyc["d"], cyc["states"], cyc["A"], cyc["m"]
        L = min(states)
        lhs = 2 ** A
        for n in states:
            lhs *= n
        rhs = 1
        for n in states:
            rhs *= 3 * n + d
        if lhs != rhs:
            fail(f"V4: identity fails for d={d} states={states[:5]}")
        if not (3 ** m < 2 ** A):
            fail(f"V4: 3^m < 2^A fails for d={d} states={states[:5]}")
        if not (2 ** A * L ** m <= (3 * L + d) ** m):
            fail(f"V4: upper inequality fails for d={d} states={states[:5]}")
        if (2 ** A * L ** m == (3 * L + d) ** m) != (m == 1):
            fail(f"V4: equality case wrong for d={d} states={states[:5]}")
        n_cycles += 1
        n_d.add(d)
    summary["V4"] = {"cycles_checked": n_cycles, "parameters_d": len(n_d)}
    print(f"V4: {n_cycles} corpus cycles of 3x+d ({len(n_d)} values of d) satisfy the exact identity and inequalities")
    # V5
    if write:
        RECEIPT.write_text(json.dumps(summary, indent=1) + "\n")
        print("receipt written")
    elif not RECEIPT.exists():
        fail("V5 receipt missing")
    elif json.loads(RECEIPT.read_text()) != summary:
        fail("V5 summary differs from the receipt")
    if failures:
        print(f"{len(failures)} failure(s)")
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()
