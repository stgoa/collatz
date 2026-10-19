"""S13: what the rise lemma and S5 give together for q = 1 cycles, as a function of m and |h|_m.

Inputs (all upper bounds on ell' = log2 L, which weakens both bounds when larger):
  L <= m 2^A / (3D) (drift bound) and gap_all 2^A <= 2^172 m^341 D (mmusson, replayed EXT-1),
  so ell' <= 172 + 342 log2 m - log2 3.  eta = 1/(3 L ln 2) with the standing hypothesis L >= 2^20.
For a rotation h with s mismatches and the cycle's log-height B (real):
  (S5, end witness)  the longest agreeing run t >= ceil((m - s)/s) satisfies 1 + t log2 3 < ell' + B;
  (rise, S13)        s >= k >= ceil(log_kappa(1 + B/c)) - 1,  c = ell' + 1 + (sigma + eta)|h|_m.
The guaranteed count is F(m, H0) = min over B >= 0 of max(S5(B), rise(B)) for |h|_m <= H0.
Also: the smallest |h|_m compatible with s(h) <= S (localization).
Writes s13_short_rotations.json.
"""
import json
import math
from pathlib import Path

LOG3 = math.log2(3)
SIG = LOG3 - 1
ETA = 1 / (3 * 2**20 * math.log(2))
KAP = LOG3 + ETA


def ellmax(m):
    return 172 + 342 * math.log2(m) - LOG3


def s5_min(m, B, ell):
    """Smallest s >= 2 allowed by the end witness at height B."""
    lim = (ell + B - 1) / LOG3          # t must be < lim
    lo, hi = 2, m
    if math.ceil((m - hi) / hi) >= lim:
        return m
    while lo < hi:                       # ceil((m - s)/s) is nonincreasing in s
        mid = (lo + hi) // 2
        if math.ceil((m - mid) / mid) < lim:
            hi = mid
        else:
            lo = mid + 1
    return lo


def rise_min(B, c):
    x = math.log(1 + B / c) / math.log(KAP)
    return max(0, math.ceil(x - 1e-12) - 1)


def F(m, H0):
    """min over B in [0, sigma m] of max(S5(B), rise(B)); S5 is nonincreasing and rise nondecreasing in B."""
    ell = ellmax(m)
    c = ell + 1 + (SIG + ETA) * H0
    f = lambda B: s5_min(m, B, ell)
    g = lambda B: rise_min(B, c)
    lo, hi = 0.0, SIG * m
    if g(hi) < f(hi):
        return f(hi), hi
    if g(lo) >= f(lo):
        return g(lo), lo
    for _ in range(200):
        mid = (lo + hi) / 2
        if mid in (lo, hi):
            break
        if g(mid) < f(mid):
            lo = mid
        else:
            hi = mid
    return (f(lo), lo) if f(lo) <= g(hi) else (g(hi), hi)


def F_grid(m, H0, n=3000):
    """Brute-force check of F on a log grid (used for a sanity comparison only)."""
    ell = ellmax(m)
    c = ell + 1 + (SIG + ETA) * H0
    Bmax = SIG * m
    grid = [0.0] + [Bmax * 10 ** (-k * 12 / n) for k in range(n, -1, -1)]
    return min(max(s5_min(m, B, ell), rise_min(B, c)) for B in grid)


def main():
    out = {"ell_bound": "172 + 342 log2 m - log2 3", "eta": ETA, "table": [], "localization": [], "asymptotic": []}
    ms = [2**19, 10**7, 1.375e11, 10**15, 10**20, 10**30]
    for m, H0 in ((10**7, 1), (10**7, 10**4), (int(1.375e11), 1), (int(1.375e11), 10**9), (10**20, 10**10)):
        assert F_grid(m, H0) >= F(m, H0)[0], (m, H0)   # bisection value is attained, grid cannot beat it
    for m in ms:
        m = int(m)
        row = {"m": m, "ell_max": round(ellmax(m), 1)}
        for label, H0 in (("1", 1), ("ell", ellmax(m)), ("10ell", 10 * ellmax(m)), ("sqrt_m", m**0.5),
                          ("m^0.75", m**0.75), ("m/1000", m / 1000), ("m/100", m / 100), ("m/10", m / 10),
                          ("m/3", m / 3), ("m/2", m / 2)):
            v, B = F(m, H0)
            row[label] = v
        out["table"].append(row)
        print(row)
    for m in (2**19, 10**7, int(1.375e11), 10**15):
        loc = {"m": m}
        for S in range(3, 16):
            lo, hi = 0.0, m / 2
            if F(m, hi)[0] > S:
                loc[str(S)] = "none"      # even |h|_m = m/2 forces more than S mismatches
                continue
            if F(m, lo)[0] <= S:
                loc[str(S)] = 0.0
                continue
            for _ in range(60):
                mid = (lo + hi) / 2
                if F(m, mid)[0] <= S:
                    hi = mid
                else:
                    lo = mid
            loc[str(S)] = round(hi / m, 6)
        out["localization"].append(loc)
        print(loc)
    for m in (10**12, 10**18, 10**24, 10**36, 10**48):
        r = {"m": m}
        for th in (0.25, 0.5, 0.75, 1.0):
            r["theta=%s" % th] = F(m, m ** (1 - th))[0]
        out["asymptotic"].append(r)
        print(r)
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
