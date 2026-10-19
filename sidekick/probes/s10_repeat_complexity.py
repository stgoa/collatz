"""S10: the run bound as a statement about repeated factors and factor complexity.

Two occurrences, at cyclic offset h, of the same factor of length t form an agreeing run of the rotation
by h, so the run law gives max(n_e, n_(e+h)) > 2*3^t at its end. With the global-drift ceiling (S9):
    t < T(m, Lam) := (Lam + (m-1) log2(3/2) - 1) / log2 3,      Lam = log2 L + delta(w).
So every factor of length >= T occurs at most once in the cyclic word: the factor complexity p_w(n) = m for
n >= T. At q = 1 with gap_all, T ~ 0.369 m + O(log m). Any word class with p(T) < m is therefore excluded for
large m: Sturmian/Christoffel words (p(n) = n + 1), codings of 2-interval rotations (p(n) <= 2n) and of
3-interval exchanges (p(n) = 2n + 1), since 2T + 1 < m. Codings of a rotation by k >= 3 intervals only satisfy
p(n) <= k n, so counting alone does not exclude them (three-mismatch chain words need S7).
This probe (i) checks the repeat inequality 2*3^t < H on every actual 3x+q cycle (q < 2000), and
(ii) on random k-interval rotation codings (k = 2, 3, 4), measures the longest repeated factor against
T(m, ell*). Generic codings repeat far beyond T because the rotation number has good rational approximations;
only badly approximable rotation numbers (as in S8's survivors) keep the longest repeat short.
"""
import json
import math
import random
import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402

LOG2_3 = math.log2(3)


def longest_repeat(w):
    """Longest t such that some factor of length t occurs at two distinct cyclic positions (binary search + hashing)."""
    m = len(w)
    ww = w + w

    def has_repeat(t):
        if t == 0:
            return True
        seen = set()
        base, mod = 1_000_003, (1 << 61) - 1
        hsh, pw = 0, pow(base, t, mod)
        for i in range(t):
            hsh = (hsh * base + ww[i]) % mod
        for i in range(m):
            if hsh in seen:
                return True
            seen.add(hsh)
            hsh = (hsh * base - ww[i] * pw + ww[i + t]) % mod
        return False

    lo, hi = 0, m - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if has_repeat(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


def T_bound(m, Lam):
    return (Lam + (m - 1) * math.log2(1.5) - 1) / LOG2_3


def coding(m, h, cuts, vals):
    """k-interval coding of the rotation by h on Z/m: letter at position i is vals[j] where (i*h mod m) in [cuts[j], cuts[j+1])."""
    w = []
    for i in range(m):
        x = (i * h) % m
        j = max(k for k in range(len(cuts)) if cuts[k] <= x)
        w.append(vals[j])
    return w


def main():
    out = {}
    # (i) actual cycles: the longest repeat t satisfies 2*3^t < H
    bad, tested, worst = 0, 0, None
    for q in range(1, 2000, 2):
        if q % 3 == 0:
            continue
        for cyc in cycles(q, 1001):
            m = len(cyc)
            if m < 3:
                continue
            w = [step(x, q)[1] for x in cyc]
            t = longest_repeat(w)
            H = max(cyc)
            tested += 1
            if not 2 * 3**t < H:
                bad += 1
            ratio = (1 + t * LOG2_3) / math.log2(H)
            if worst is None or ratio > worst[0]:
                worst = (round(ratio, 3), q, m, t, H)
    out["actual_cycles"] = {"tested": tested, "violations": bad, "max (1+t log2 3)/log2 H": worst}
    print("actual cycles:", out["actual_cycles"])
    # (ii) random k-interval codings at A = ceil(m log2 3)
    random.seed(7)
    rows = []
    for m in (2_000, 10_000, 40_000):
        ell = 172 + 342 * math.log2(m) - LOG2_3
        T = T_bound(m, ell)
        for k in (2, 3, 4):
            reps = []
            for _ in range(6):
                h = random.randrange(1, m)
                while gcd(h, m) != 1:
                    h = random.randrange(1, m)
                cuts = [0] + sorted(random.sample(range(1, m), k - 1))
                vals = random.sample([1, 1, 2, 2, 3][: max(k, 2) + 1], k) if k > 2 else [1, 2]
                w = coding(m, h, cuts, vals)
                reps.append(longest_repeat(w))
            rows.append({"m": m, "k": k, "T": round(T), "longest_repeats": reps,
                         "all_beyond_T": all(r >= T for r in reps)})
            print(rows[-1])
    out["codings"] = rows
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1, default=str))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
