"""S11: main's C013 q1 restriction with the replayed gap_all in place of Matveev.

C013 section 4 (13): a q = 1 cycle whose word is (U,a_0,U,a_1,...,U,a_(r-1)) with nonconstant markers,
background length n, marker total T, satisfies
    n < r + 4T + 2(r-1) log2 r + log2(1/eta),        eta = D/2^A,
where C013 bounds log2(1/eta) < (K/ln 2)(1 + ln(2m)), K = 6e8 (Matveev, imported). gap_all (replayed as EXT-1)
gives eta >= 2^-172 m^-341, i.e. log2(1/eta) <= 172 + 341 log2 m. With T <= H r and m = r(n+1), this probe
computes the smallest r compatible with each bound (C013's (14), made explicit), for a few (m, H).
"""
import json
import math
import sys
from pathlib import Path


def min_r(m, H, lam):
    """smallest r >= 2 with m/r - 1 < r + 4 H r + 2 (r-1) log2 r + lam, i.e. q = 1 still possible."""
    r = 2
    while True:
        n_plus_1 = m / r
        if n_plus_1 - 1 < r + 4 * H * r + 2 * (r - 1) * math.log2(r) + lam:
            return r
        r += 1 if r < 1000 else max(1, r // 1000)


def main():
    rows = []
    for m in (10**7, 137_500_000_000, 10**15):
        lam_gap = 172 + 341 * math.log2(m)
        lam_matveev = (6e8 / math.log(2)) * (1 + math.log(2 * m))
        for H in (1, 2, 4, 8):
            rows.append({"m": m, "H": H,
                         "min_r_gap_all": min_r(m, H, lam_gap),
                         "min_r_matveev": min_r(m, H, lam_matveev),
                         "log2(1/eta) bound: gap_all": round(lam_gap), "Matveev": f"{lam_matveev:.3g}"})
            print(rows[-1])
    Path(__file__).with_suffix(".json").write_text(json.dumps(rows, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
