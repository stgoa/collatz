#!/usr/bin/env python3
"""Finite certificate for L2/L3 (explicit valuation tail and one-round descent).

Exact rationals for probabilities and counts; floating point only for the
rate function I(theta), with an explicit relative tolerance. Writes
receipts/L2_receipt.json. Exit code 0 iff every check passes.
"""
import json
import math
import os
import random
import sys
from fractions import Fraction
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "receipts", "L2_receipt.json")
TOL = 1e-9  # relative slack allowed when comparing an exact probability to a float bound


def rate(theta: float) -> float:
    """I(theta) = theta*log(2(theta-1)/theta) - log(theta-1), 1 < theta < 2."""
    return theta * math.log(2 * (theta - 1) / theta) - math.log(theta - 1)


def chernoff_bound(n: int, t: float) -> float:
    """min_{u>1} u^t / (2u-1)^n, evaluated at u* = (t/n)/(2(t/n-1)); requires n < t < 2n."""
    theta = t / n
    assert 1 < theta < 2
    return math.exp(-n * rate(theta))


def exact_tail(n: int, t: float) -> Fraction:
    """P(A_n <= t) for iid geometric(1/2) on {1,2,...}: sum_{A=n}^{floor t} C(A-1,n-1)/2^A."""
    return sum(Fraction(comb(A - 1, n - 1), 2 ** A) for A in range(n, math.floor(t) + 1))


def v2(x: int) -> int:
    return (x & -x).bit_length() - 1


def syr(N: int, d: int):
    y = 3 * N + d
    a = v2(y)
    return y >> a, a


def word(N: int, n: int, d: int):
    ws = []
    for _ in range(n):
        N, a = syr(N, d)
        ws.append(a)
    return tuple(ws), N


def main() -> int:
    ok = True
    receipt = {"checks": {}, "rate_table": [], "tradeoff_table": []}

    # 1. Chernoff bound vs exact tail distribution.
    thetas = [1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.95]
    worst = 0.0
    cases = 0
    for n in range(1, 61):
        for theta in thetas:
            t = theta * n
            if not (n < t < 2 * n):
                continue
            p = exact_tail(n, t)
            b = chernoff_bound(n, t)
            cases += 1
            ratio = float(p) / b if b > 0 else float("inf")
            worst = max(worst, ratio)
            if float(p) > b * (1 + TOL):
                ok = False
                print(f"FAIL chernoff n={n} theta={theta}: exact {float(p):.3e} > bound {b:.3e}")
    receipt["checks"]["chernoff_vs_exact"] = {"cases": cases, "worst_exact_over_bound": worst, "pass": worst <= 1 + TOL}
    for theta in thetas:
        receipt["rate_table"].append({"theta": theta, "I": rate(theta), "descent_factor_per_step": 3 / 2 ** theta})

    # Word-count identity: #words with A_n <= t equals C(floor t, n).
    wc_ok = True
    for n in range(1, 30):
        for T in range(n, 2 * n + 3):
            lhs = sum(comb(A - 1, n - 1) for A in range(n, T + 1))
            if lhs != comb(T, n):
                wc_ok = False
    receipt["checks"]["word_count_hockey_stick"] = {"pass": wc_ok}
    ok &= wc_ok

    # 2. L1 on actual integers: each word is one odd class mod 2^(A+1); counts within +-1.
    X = 2 ** 16
    for d in (1, 5):
        classes = {}
        counts = {}
        for N in range(1, X + 1, 2):
            for n in range(1, 7):
                w, _ = word(N, n, d)
                A = sum(w)
                if 2 ** (A + 1) > X:
                    break
                key = (n, w)
                classes.setdefault(key, set()).add(N % 2 ** (A + 1))
                counts[key] = counts.get(key, 0) + 1
        one_class = all(len(s) == 1 for s in classes.values())
        within = True
        for (n, w), c in counts.items():
            A = sum(w)
            expect = Fraction(X, 2 ** (A + 1))
            if abs(c - expect) > 1:
                within = False
        # every odd class mod 2^(A+1) that is realized must correspond to exactly one word: check injectivity
        inv = {}
        inj = True
        for (n, w), s in classes.items():
            r = next(iter(s))
            k = (n, sum(w), r)
            if k in inv and inv[k] != w:
                inj = False
            inv[k] = w
        receipt["checks"][f"cylinders_d{d}"] = {"X": X, "words": len(classes), "one_class_each": one_class,
                                                "counts_within_1": within, "class_determines_word": inj,
                                                "pass": one_class and within and inj}
        ok &= one_class and within and inj

    # 3. Affine formula S^n(N) = (3^n N + C_w)/2^A exactly, the bound C_w/2^A <= (3/2)^n - 1,
    #    and a record that the discarded multiplicative form C_w <= 3^n is false.
    rng = random.Random(20261018)
    aff_ok = True
    mult_form_violations = 0
    for _ in range(20000):
        N = rng.randrange(1, 2 ** 64) | 1
        n = rng.randrange(1, 41)
        w, Nn = word(N, n, 1)
        A = sum(w)
        Aj = 0
        Cw = 0
        for j, a in enumerate(w):
            Cw += 3 ** (n - 1 - j) * 2 ** Aj
            Aj += a
        if (3 ** n * N + Cw) % 2 ** A != 0 or (3 ** n * N + Cw) // 2 ** A != Nn:
            aff_ok = False
        if not (Fraction(Cw, 2 ** A) <= Fraction(3 ** n - 2 ** n, 2 ** n)):  # C_w/2^A <= (3/2)^n - 1
            aff_ok = False
        if Cw > 3 ** n:
            mult_form_violations += 1
    # explicit counterexample to the discarded form: word (10,1) has C_w = 3 + 2^10
    w_ex = (10, 1)
    Cw_ex = 3 ** 1 * 2 ** 0 + 3 ** 0 * 2 ** 10
    receipt["checks"]["affine_bound"] = {"samples": 20000, "pass": aff_ok,
                                         "discarded_multiplicative_form_violations": mult_form_violations,
                                         "counterexample_word": list(w_ex), "counterexample_Cw": Cw_ex,
                                         "counterexample_exceeds_3^n": Cw_ex > 3 ** 2}
    ok &= aff_ok and (Cw_ex > 3 ** 2)

    # 4. Integer tail counts (4) and descent (6) for X = 2^20.
    X = 2 ** 20
    tail_rows = []
    ns = (6, 8, 10)
    ths = (1.6, 1.7, 1.8)
    for d in (1, 5):
        acc = {(n, theta): [0, 0] for n in ns for theta in ths}
        for N in range(1, X + 1, 2):
            ws, its, M = [], {}, N
            for j in range(1, max(ns) + 1):
                M, a = syr(M, d)
                ws.append(a)
                its[j] = M
            for n in ns:
                A = sum(ws[:n])
                Nn = its[n]
                for theta in ths:
                    if A <= theta * n:
                        acc[(n, theta)][0] += 1
                    elif not (Nn < N * (3 / 2 ** theta) ** n + d * 1.5 ** n):  # (6), additive term scales with d
                        acc[(n, theta)][1] += 1
        for (n, theta), (bad, nondesc) in sorted(acc.items()):
            t = theta * n
            bound = (X / 2) * chernoff_bound(n, t) + comb(math.floor(t), n)
            row = {"d": d, "n": n, "theta": theta, "bad_count": bad, "bound_(4)": bound,
                   "descent_violations_off_bad_set": nondesc, "pass": bad <= bound * (1 + TOL) and nondesc == 0}
            tail_rows.append(row)
            ok &= row["pass"]
    receipt["checks"]["integer_tail_and_descent"] = tail_rows

    # 5. Trade-off table for one round from scale X with n = floor(kappa log2 X).
    for theta in (1.6, 1.65, 1.7, 1.75, 1.8, 1.9):
        H = lambda p: -p * math.log2(p) - (1 - p) * math.log2(1 - p)
        kappa_max = 1 / (theta * H(1 / theta))  # boundary term C(theta n, n) ~ 2^{theta n H(1/theta)} must stay below X
        I = rate(theta)
        receipt["tradeoff_table"].append({
            "theta": theta, "I": I, "descent_factor_per_step": 3 / 2 ** theta,
            "kappa_max_for_boundary_term": kappa_max,
            "exceptional_exponent_at_kappa_max": kappa_max * I / math.log(2),
            "landing_scale_exponent_at_kappa_max": 1 + kappa_max * math.log2(3 / 2 ** theta),
        })

    receipt["pass"] = bool(ok)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(receipt, f, indent=1)
    print(json.dumps({k: (v if not isinstance(v, list) else f"{len(v)} rows") for k, v in receipt["checks"].items()}, indent=1))
    print("tradeoff:")
    for r in receipt["tradeoff_table"]:
        print(f"  theta={r['theta']:.2f} I={r['I']:.5f} factor/step={r['descent_factor_per_step']:.4f} "
              f"kappa_max={r['kappa_max_for_boundary_term']:.3f} exc.exp={r['exceptional_exponent_at_kappa_max']:.4f} "
              f"landing exp={r['landing_scale_exponent_at_kappa_max']:.4f}")
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
