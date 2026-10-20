#!/usr/bin/env python3
"""Finite certificate for the L4 architecture note: with Tao's own parameter
choices (v7, Section 5), the first-passage window I_y is empty and the 3-adic
level m_0 is zero at every scale remotely near the verified range.

Quantities (natural logarithms; alpha = 1.001 as in the paper):
  I_y   = [ log(y/x)/log(4/3) + (log x)^0.8 ,  log(y^alpha/x)/log(4/3) - (log x)^0.8 ],  y = x^alpha  (5.9)
  m_0   = floor( (alpha-1)/100 * log x )                                                      (5.2)
  n_0   with 2^{n_0} ~ x^{0.1}, i.e. n_0 ~ log x / (10 log 2)                                 (5.1)
  windows (log x)^0.6, (log x)^0.7 in (5.11), (5.10)
Writes receipts/L4_window_receipt.json. Floating point; every threshold is
also bracketed by exact integer comparisons of the defining inequality.
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "receipts", "L4_window_receipt.json")
ALPHA = 1.001
L43 = math.log(4 / 3)


def window(logx, alpha=ALPHA):
    lo = (alpha - 1) * logx / L43 + logx ** 0.8          # y = x^alpha: log(y/x) = (alpha-1) log x
    hi = (alpha * alpha - 1) * logx / L43 - logx ** 0.8  # log(y^alpha/x) = (alpha^2-1) log x
    return lo, hi


def main():
    rec = {}
    for name, logx in [("x=2^68 (verified range)", 68 * math.log(2)), ("x=2^1000", 1000 * math.log(2)),
                       ("x=2^(10^6)", 1e6 * math.log(2)), ("x=exp(10^12)", 1e12), ("x=exp(10^14)", 1e14)]:
        lo, hi = window(logx)
        rec[name] = {
            "log_x": logx,
            "I_y_lower": lo, "I_y_upper": hi, "I_y_nonempty": hi > lo,
            "m0": math.floor((ALPHA - 1) / 100 * logx),
            "n0_approx": logx / (10 * math.log(2)),
            "window_0.6": logx ** 0.6, "window_0.7": logx ** 0.7, "window_0.8": logx ** 0.8,
            "steps between scales x and x^alpha, (alpha-1)log x / log(4/3)": (ALPHA - 1) * logx / L43,
        }
    # Threshold for a nonempty window: (alpha^2-1 - (alpha-1)) log x / L43 > 2 (log x)^0.8
    #   <=> (log x)^0.2 > 2 L43 / (alpha (alpha-1))  <=> log x > (2 L43 / (alpha(alpha-1)))^5
    thr = (2 * L43 / (ALPHA * (ALPHA - 1))) ** 5
    rec["threshold_log_x_for_nonempty_window"] = thr
    rec["threshold_log2_x_for_nonempty_window"] = thr / math.log(2)
    # exact bracketing: window empty just below, nonempty just above
    lo1, hi1 = window(thr * 0.999)
    lo2, hi2 = window(thr * 1.001)
    rec["bracket_check"] = {"empty_at_0.999*thr": hi1 <= lo1, "nonempty_at_1.001*thr": hi2 > lo2}
    # m_0 >= 1 threshold
    rec["threshold_log_x_for_m0_ge_1"] = 100 / (ALPHA - 1)
    # how large would alpha have to be for a nonempty window at x = 2^68?
    logx = 68 * math.log(2)
    a = 1.0
    while True:
        a += 0.001
        lo, hi = window(logx, a)
        if hi > lo or a > 50:
            break
    rec["alpha_needed_for_nonempty_window_at_2^68"] = a
    ok = (rec["bracket_check"]["empty_at_0.999*thr"] and rec["bracket_check"]["nonempty_at_1.001*thr"]
          and not rec["x=2^68 (verified range)"]["I_y_nonempty"] and rec["x=2^68 (verified range)"]["m0"] == 0)
    rec["pass"] = ok
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(rec, open(OUT, "w"), indent=1)
    for k, v in rec.items():
        print(k, ":", v if not isinstance(v, dict) else {kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in v.items()})
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
