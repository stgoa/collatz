"""S13 corollaries 5-7: the low mismatch spectrum is sparse, a low-mismatch rotation forces a huge letter, and so\nrho -> infinity follows from a sublinear bound on the largest letter.

(5) Subadditivity: s(h1 - h2) <= s(h1) + s(h2) (if a_i != a_(i+h1-h2) then i is in mis(h1) or i+h1-h2 is in
    mis(h2)). With Corollary 3 (s <= S forces |h|_m >= H*(S)), any two rotations with at most S mismatches
    differ by a rotation with at most 2S mismatches, so the set E_S = {h != 0 : s(h) <= S} lies in the arc
    [H*(S), m - H*(S)] with pairwise cyclic distances >= H*(2S): |E_S| <= floor((m - 2 H*(S)) / H*(2S)) + 1.
(6) Huge letter: Delta+ <= max_p (y_(p+d) - y_p) <= Var(mu)/2 <= V_h/2 + delta (S12 (3), mean zero), so the
    lemma B + c <= kappa^(s+1) c with c = ell' + 1 + Delta+ gives V_h >= 2 (B/(kappa^(s+1) - 1) - ell' - 1 - delta),
    and some mismatch has |a_e - a_(e+h)| >= V_h / s, so some letter is >= 1 + V_h / s.
    At q = 1 with S5 (B > ceil((m - s)/s) log2 3 - ell' + 1) this is a letter linear in m.

Checks on actual 3x+q cycles (odd q < 2000, 3 not dividing q): subadditivity for every pair of rotations, and (6)
with the cycle's own B, ell', delta for every rotation. Tables for q = 1 from s13_short_rotations.F.
Writes s13_corollaries.json.
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402
from s13_short_rotations import F, ellmax, KAP, LOG3  # noqa: E402


def Hstar(m, S):
    """Smallest |h|_m compatible with s(h) <= S (0 if none forced)."""
    lo, hi = 0.0, m / 2
    if F(m, hi)[0] > S:
        return None             # no rotation at all can have <= S mismatches
    if F(m, lo)[0] <= S:
        return 0.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if F(m, mid)[0] <= S:
            hi = mid
        else:
            lo = mid
    return hi


def checks():
    st = {"cycles": 0, "subadd_checks": 0, "subadd_viol": 0, "letter_checks": 0, "letter_viol": 0,
          "letter_min_margin": float("inf")}
    for q in range(1, 2000, 2):
        if q % 3 == 0:
            continue
        for cyc in cycles(q, 1001):
            m = len(cyc)
            if m < 2:
                continue
            st["cycles"] += 1
            a = [step(x, q)[1] for x in cyc]
            s = [sum(a[i] != a[(i + h) % m] for i in range(m)) for h in range(m)]
            if m <= 120:
                for h1 in range(1, m):
                    for h2 in range(1, m):
                        st["subadd_checks"] += 1
                        if s[(h1 - h2) % m] > s[h1] + s[h2]:
                            st["subadd_viol"] += 1
            L = min(cyc)
            ell = math.log2(L)
            eta = q / (3 * L * math.log(2))
            kap = LOG3 + eta
            B = math.log2(max(cyc)) - ell
            delta = sum(a) - m * LOG3
            amax = max(a)
            for h in range(1, m):
                lk = (s[h] + 1) * math.log(kap)
                if lk > 700:
                    continue
                need = 1 + 2 * (B / math.expm1(lk) - ell - 1 - delta) / s[h]
                st["letter_checks"] += 1
                if amax < need - 1e-9:
                    st["letter_viol"] += 1
                st["letter_min_margin"] = min(st["letter_min_margin"], amax - need)
    st["letter_min_margin"] = round(st["letter_min_margin"], 3)
    return st


def tables():
    out = {"sparsity": [], "huge_letter": []}
    for m in (int(1.375e11), 10**15, 10**20):
        row = {"m": m}
        for S in range(4, 13):
            h1, h2 = Hstar(m, S), Hstar(m, 2 * S)
            if h1 is None:
                row[str(S)] = 0
            elif not h2:
                row[str(S)] = "unbounded"
            else:
                row[str(S)] = int((m - 2 * h1) // h2) + 1
        out["sparsity"].append(row)
        print("sparsity bound |E_S|", row)
    for m in (int(1.375e11), 10**15, 10**20):
        ell = ellmax(m)
        row = {"m": m}
        for S in range(4, 13):
            Bmin = math.ceil((m - S) / S) * LOG3 - ell + 1
            Vh = 2 * (Bmin / (KAP ** (S + 1) - 1) - ell - 1)
            row[str(S)] = round((1 + Vh / S) / m, 5)
        out["huge_letter"].append(row)
        print("forced letter / m", row)
    return out


def forced(m, S):
    """Corollary 6 at q = 1 with S5's height: a rotation with <= S mismatches forces a letter >= forced(m, S)."""
    ell = ellmax(m)
    Bmin = math.ceil((m - S) / S) * LOG3 - ell + 1
    return 1 + 2 * (Bmin / (KAP ** (S + 1) - 1) - ell - 1) / S


def rho_lower(m, amax):
    """Corollary 7: every rotation has >= S + 1 mismatches whenever forced(m, S) > amax (forced decreases in S)."""
    S = 2
    while forced(m, S + 1) > amax:
        S += 1
    return S + 1


def main():
    st = checks()
    print(json.dumps(st, indent=1))
    out = tables()
    out["rho_from_max_letter"] = {}
    for m in (int(1.375e11), 10**15, 10**20, 10**30):
        row = {lab: rho_lower(m, am) for lab, am in (("10", 10), ("1e3", 10**3), ("1e6", 10**6), ("sqrt_m", m**0.5),
                                                      ("m^0.75", m**0.75), ("m/1000", m / 1000), ("m/100", m / 100))}
        out["rho_from_max_letter"][str(m)] = row
        print("rho lower bound from a_max <=", m, row)
    out["checks"] = st
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1))
    return 0 if st["subadd_viol"] == st["letter_viol"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
