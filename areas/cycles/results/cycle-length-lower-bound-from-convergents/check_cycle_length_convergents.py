#!/usr/bin/env python3
"""Certificate for cycle-length-lower-bound-from-convergents.

Setting: raw odd-only 3x+1 map n -> (3n+1)/2^(v_2(3n+1)) on positive odd integers; a nontrivial cycle has m odd
states n_1..n_m, A = sum of the valuations and minimum L >= 3, and satisfies 2^A = prod (3 + 1/n_i), hence
    (1)   0 < A - m*theta < m / (3 L ln 2) < 0.481 m / L,          theta = log_2 3.
Call a pair (m, A) of positive integers admissible for L if it satisfies (1). With the convergents p_k/q_k of theta,
e_k = |q_k theta - p_k|, and for q_k <= m < q_{k+1} the integers x, y with m = x q_k + y q_{k+1}, A = x p_k + y p_{k+1}
(determinant +-1), one has A - m theta = (-1)^(k+1) (x e_k - y e_{k+1}); admissibility forces y >= 1, x <= -1 when k
is even and x >= 1, y <= 0 when k is odd, with |x| e_k < 0.481 q_{k+1}/L and |y| e_{k+1} < 0.481 q_{k+1}/L. So the
admissible pairs below any q_K are a finite, exactly computable set, and its least m is a lower bound for the period.
V1  the continued fraction of theta from a two-sided enclosure (decimal ln is correctly rounded; two precisions), the
    convergents, and an exact integer cross-check 2^p_k > 3^q_k (k odd) / < (k even) for q_k <= 3000;
V2  0.481 > 1/(3 ln 2), checked against the decimal enclosure of ln 2;
V3  for L = 2^40, 2^60, 2^68, 2^71 (the last is the external input barina-2025-convergence-2-71): the admissible pairs
    with m < q_K (K large enough that at least three admissible m appear), each decided by interval arithmetic with the
    enclosure (an undecided pair fails the certificate), the least admissible m = M(L), and the least total length
    m + A over the admissible pairs;
V4  controls: on every cycle of actual-cycles-3x-d-corpus (3x+d, d <= 999), the exact identity 2^A prod n_i =
    prod (3 n_i + d) and the exact inequalities 3^m < 2^A <= (3 + d/L)^m, cleared of denominators;
V5  receipt comparison. Exit 1 on failure; --write-receipt regenerates cycle_length_convergents.json.
Standard library only; deterministic."""
import json
import sys
from decimal import Decimal, getcontext
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


def error_interval(k, conv, lo, hi):
    """Enclosure [e_lo, e_hi] of e_k = |q_k theta - p_k|."""
    p, q = conv[k]
    s_lo, s_hi = q * lo - p, q * hi - p
    if k % 2 == 0:            # p_k/q_k < theta
        return s_lo, s_hi
    return -s_hi, -s_lo


def admissible_pairs(L, conv, lo, hi, K):
    """All admissible (m, A) with m < q_K, as a sorted list, with the k and (x, y) that produced them."""
    out = []
    for k in range(K):
        pk, qk = conv[k]
        pk1, qk1 = conv[k + 1]
        if qk1 <= qk:            # empty range [q_k, q_{k+1})
            continue
        ek_lo, ek_hi = error_interval(k, conv, lo, hi)
        ek1_lo, ek1_hi = error_interval(k + 1, conv, lo, hi)
        if ek_lo <= 0 or ek1_lo <= 0:
            fail(f"V3: error enclosure not positive at k={k}")
            return out
        eps = C_UP * qk1 / L                           # every admissible pair in the range has gap < eps
        xmax = int(eps / ek_lo)                        # |x| e_k < eps
        ymax = int(eps / ek1_lo)                       # |y| e_{k+1} < eps
        if k % 2 == 0:
            cands = ((-ax, y) for y in range(1, ymax + 1) for ax in range(1, xmax + 1))
        else:
            cands = ((x, -ay) for x in range(1, xmax + 1) for ay in range(0, ymax + 1))
        for x, y in cands:
            m = x * qk + y * qk1
            if not (qk <= m < qk1):
                continue
            A = x * pk + y * pk1
            gap_lo = abs(x) * ek_lo + abs(y) * ek1_lo    # A - m theta = |x| e_k + |y| e_{k+1} in both parities
            gap_hi = abs(x) * ek_hi + abs(y) * ek1_hi
            bound = C_UP * m / L
            if gap_hi < bound:
                out.append((m, A, k, x, y))
            elif gap_lo >= bound:
                continue
            else:
                fail(f"V3: undecided pair m={m} at k={k}")
    out.sort()
    return out


def main():
    write = "--write-receipt" in sys.argv
    summary = {}
    # V1
    lo1, hi1, ln2lo, ln2hi = theta_enclosure(160)
    lo2, hi2, _, _ = theta_enclosure(220)
    t = [cf_terms(x, N_TERMS) for x in (lo1, hi1, lo2, hi2)]
    agree = 0
    while agree < N_TERMS and len({tt[agree] for tt in t}) == 1:
        agree += 1
    terms = t[0][:agree]
    conv = convergents(terms)
    if agree < 60:
        fail(f"V1: only {agree} continued-fraction terms certified")
    checked = 0
    for k, (p, q) in enumerate(conv):
        if q > 3000:
            break
        if (2 ** p > 3 ** q) != (k % 2 == 1):
            fail(f"V1: convergent {p}/{q} (k={k}) on the wrong side of theta")
        checked += 1
    summary["V1"] = {"terms_certified": agree, "terms": terms, "convergents_checked_exactly": checked,
                     "q_values": [str(q) for _, q in conv]}
    print(f"V1: {agree} terms of the continued fraction of log2(3) certified; {checked} convergents checked exactly")
    print("    terms:", terms[:40], "...")
    # V2
    ok2 = 3 * ln2lo * C_UP > 1
    if not ok2:
        fail("V2: 0.481 is not an upper bound for 1/(3 ln 2)")
    summary["V2"] = {"c_up": "481/1000", "three_ln2_c_up_minus_one": str(float(3 * ln2lo * C_UP - 1))}
    print(f"V2: 0.481 > 1/(3 ln 2): {ok2}")
    # V3
    summary["V3"] = {}
    for e in (40, 60, 68, 71):
        L = 2 ** e
        K = 1
        pairs = []
        while K < len(conv) - 1:
            pairs = admissible_pairs(L, conv, lo1, hi1, K)
            if len({m for m, *_ in pairs}) >= 3:
                break
            K += 1
        if len(pairs) < 3:
            fail(f"V3: fewer than three admissible pairs found for L = 2^{e}")
            continue
        M = pairs[0][0]
        least_total = min(m + A for m, A, *_ in pairs)
        first = [{"m": str(m), "A": str(A), "total": str(m + A), "k": k, "x": x, "y": y} for m, A, k, x, y in pairs[:6]]
        summary["V3"][f"2^{e}"] = {"searched_below_q_K_with_K": K, "q_K": str(conv[K][1]), "admissible_pairs_found": len(pairs),
                                   "least_m": str(M), "least_total_length": str(least_total), "first_pairs": first}
        print(f"V3: L = 2^{e}: admissible pairs below q_{K} = {conv[K][1]}: {len(pairs)}; least m = {M} ({M:.4e}), "
              f"least total length = {least_total} ({least_total:.4e})")
        for d in first[:4]:
            print(f"      m = {d['m']}, A = {d['A']}, total = {d['total']}  (k = {d['k']}, x = {d['x']}, y = {d['y']})")
    # V4
    data = json.loads(CORPUS.read_text())
    n_cycles, n_d = 0, set()
    for cyc in data["cycles"]:
        d, states, A, m = cyc["d"], cyc["states"], cyc["A"], cyc["m"]
        L = min(states)
        lhs, rhs = 2 ** A, 1
        for n in states:
            lhs *= n
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
