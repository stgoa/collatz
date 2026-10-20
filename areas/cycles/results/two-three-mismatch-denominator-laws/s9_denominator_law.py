"""S9: S6 and S7 as denominator laws in the whole 3x+q family (global-drift ceiling).

For a primitive word w (period m, total A, D = 2^A - 3^m > 0) its reduced integer cycle has parameter
q = den(w) = D / gcd(C_w, D) and odd states n_i = C(w_i)/gcd. Every step of S6/S7 holds at any odd q
once the per-step ceiling error is replaced by the global drift
    sum_(i<m) log2(1 + q/(3 n_i)) = log2(2^A / 3^m) =: delta_A     (the closing identity),
so  log2 n_k <= log2 L + k log2(3/2) - X_k + delta_A  for every k, and  L <= m q 2^A / (3D).
Consequences (Lam = log2 L + delta_A):
  s = 2:  log2 den(w) > Phi2(m) - delta_A - log2(m 2^A / (3D)),
          Phi2(m) = 1 + ceil((m-2)/2) log2 3 - (m-1) log2(3/2)              (~0.2075 m)
  s = 3:  log2 den(w) > Lam3(m) - delta_A - log2(m 2^A / (3D)),
          Lam3(m) = sup{Lam : S7's conditions W, A, P, F hold at ell = Lam, eps = 0} (~0.0144 m)
This probe computes Lam3, then checks both laws on (i) every primitive word over {1,2,3} up to length 12,
(ii) random two- and three-arc chain words up to m = 1600, (iii) main's C013 section-3 distance-three family, (iv) the words of actual 3x+q cycles, odd q < 2000.
A single violation would refute the derivation.
"""
import json
import math
import random
import sys
from functools import lru_cache
from itertools import product
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s7_three_mismatch import conditions, LOG2_3  # noqa: E402

LOG2_15 = math.log2(1.5)


def phi2(m):
    return 1 + -(-(m - 2) // 2) * LOG2_3 - (m - 1) * LOG2_15


@lru_cache(maxsize=None)
def lam3(m):
    """Largest Lam (to 1e-6) with W, A, P, F all >= 0 at ell = Lam, eps = 0; None if none for Lam >= -m."""
    def ok(L):
        r = conditions(m, L, 0.0)
        return min(r["W"], r["A"], r["P"], r["F"]) >= 0
    lo, hi = -float(m), float(m)
    if not ok(lo):
        return None
    for _ in range(80):
        mid = (lo + hi) / 2
        if ok(mid):
            lo = mid
        else:
            hi = mid
    return lo


def C_of(w):
    c = 0
    for k, a in enumerate(reversed(w)):
        c = 3**k + 2**a * c
    return c


def primitive(w):
    m = len(w)
    return all(w != w[p:] + w[:p] for p in range(1, m) if m % p == 0)


def mismatch_counts(w):
    m = len(w)
    return [sum(1 for i in range(m) if w[i] != w[(i + h) % m]) for h in range(1, m)]


def log2_int(x):
    return x.bit_length() - 1 + math.log2(x / (1 << (x.bit_length() - 1))) if x.bit_length() < 1000 else \
        (x.bit_length() - 53) + math.log2(x >> (x.bit_length() - 53))


def analyse(w):
    """Return (m, s_min_set, log2 q, bound2, bound3) for a primitive word with D > 0, else None."""
    m, A = len(w), sum(w)
    D = 2**A - 3**m
    if D <= 0 or not primitive(w):
        return None
    C = C_of(w)
    q = D // gcd(C, D)
    lq = log2_int(q) if q > 1 else 0.0
    delta_A = A - m * LOG2_3
    lterm = math.log2(m / 3) + (A - log2_int(D))          # log2(m 2^A / (3D))
    s_set = set(mismatch_counts(w))
    b2 = phi2(m) - delta_A - lterm
    L3 = lam3(m) if 3 in s_set else None
    b3 = (L3 - delta_A - lterm) if L3 is not None else None
    return {"m": m, "A": A, "s": sorted(s_set & {2, 3}), "log2q": lq, "b2": b2, "b3": b3}


def check(rec, stats, tag):
    if rec is None:
        return
    for s in rec["s"]:
        b = rec["b2"] if s == 2 else rec["b3"]
        if b is None:
            continue
        stats[f"{tag}_s{s}"] = stats.get(f"{tag}_s{s}", 0) + 1
        slack = rec["log2q"] - b
        key = f"{tag}_s{s}_min_slack"
        if key not in stats or slack < stats[key][0]:
            stats[key] = (round(slack, 3), rec["m"], round(b, 2), round(rec["log2q"], 2))
        if not slack > 0:
            stats.setdefault("violations", []).append((tag, s, rec["m"], rec["A"], round(slack, 4)))
        if b > 0:  # the law says something non-trivial here
            stats[f"{tag}_s{s}_nonvacuous"] = stats.get(f"{tag}_s{s}_nonvacuous", 0) + 1
            key2 = f"{tag}_s{s}_nonvacuous_min_slack"
            if key2 not in stats or slack < stats[key2][0]:
                stats[key2] = (round(slack, 3), rec["m"], round(b, 2), round(rec["log2q"], 2))


def chain_word(m, h, arcs):
    """arcs = [(value, length), ...] laid along the chain 0, h, 2h, ... (gcd(h, m) = 1)."""
    w = [0] * m
    k = 0
    for v, L in arcs:
        for _ in range(L):
            w[(k * h) % m] = v
            k += 1
    assert k == m
    return w


def main():
    random.seed(20261019)
    stats = {}
    # Lam3 table
    lam_table = {m: (round(lam3(m), 2) if lam3(m) is not None else None)
                 for m in (100, 300, 1000, 3000, 10000, 100000)}
    print("Lam3(m):", lam_table, " Phi2(m):", {m: round(phi2(m), 2) for m in (100, 1000, 10000)})
    # (i) exhaustive small words
    for m in range(3, 13):
        for w in product((1, 2, 3), repeat=m):
            w = list(w)
            if w != min(w[i:] + w[:i] for i in range(m)):
                continue
            check(analyse(w), stats, "exhaustive")
    # (ii) random chain words with 2 and 3 arcs
    for m in (30, 60, 100, 200, 400, 800, 1600):
        for _ in range(40 if m <= 400 else 12):
            h = random.randrange(1, m)
            while gcd(h, m) != 1:
                h = random.randrange(1, m)
            for k in (2, 3):
                cuts = sorted(random.sample(range(1, m), k - 1))
                lens = [b - a for a, b in zip([0] + cuts, cuts + [m])]
                vals = []
                for _ in range(k):
                    v = random.choice((1, 1, 1, 2, 2, 3, 4))
                    while vals and v == vals[-1]:
                        v = random.choice((1, 2, 3, 4))
                    vals.append(v)
                if k == 3 and vals[0] == vals[-1]:
                    vals[-1] = ({1, 2, 3, 4} - {vals[0], vals[1]}).pop()
                w = chain_word(m, h, list(zip(vals, lens)))
                # push the total to just above m log2 3 by raising the largest arc's value if needed
                if 2**sum(w) <= 3**m:
                    continue
                check(analyse(w), stats, f"chain{k}")
    # (ii') near-critical chain words (A = ceil(m log2 3), drift < 1), where the laws are non-vacuous
    for m in (200, 400, 800, 1600, 3200):
        A0 = math.ceil(m * LOG2_3)
        for _ in range(10):
            h = random.randrange(1, m)
            while gcd(h, m) != 1:
                h = random.randrange(1, m)
            w2 = chain_word(m, h, [(1, m - (A0 - m)), (2, A0 - m)])
            check(analyse(w2), stats, "nearcrit2")
            l3 = random.randrange(1, (A0 - m - 1) // 2)
            l2 = A0 - m - 2 * l3
            arcs = [(1, m - l2 - l3), (2, l2), (3, l3)]
            random.shuffle(arcs)
            w3 = chain_word(m, h, arcs)
            check(analyse(w3), stats, "nearcrit3")
    # (iii) C013 section-3 family: w = (3, U, 4, U, 5, U), U = 1^u 2^v, u = 2b+2-a, v = a-b-3
    fam = []
    for a, b in ((27, 17), (65, 41), (149, 94), (485, 306), (1539, 971)):
        if a * math.log(2) - b * math.log(3) <= 0:
            continue
        u, v = 2 * b + 2 - a, a - b - 3
        U = [1] * u + [2] * v
        w = [3] + U + [4] + U + [5] + U
        rec = analyse(w)
        check(rec, stats, "C013fam")
        fam.append({"a": a, "b": b, "m": rec["m"], "log2q": round(rec["log2q"], 1),
                    "log2q_over_m": round(rec["log2q"] / rec["m"], 3),
                    "b3": None if rec["b3"] is None else round(rec["b3"], 1)})
    print("C013 family:", fam)
    # (iv) actual 3x+q cycles with small q (the hardest cases: den(w) divides q)
    from s1a_integer_cycle_check import cycles, step
    for q in range(1, 2000, 2):
        if q % 3 == 0:
            continue
        for cyc in cycles(q, 1001):
            i0 = cyc.index(min(cyc))
            n = cyc[i0:] + cyc[:i0]
            if len(n) < 3:
                continue
            w = [step(x, q)[1] for x in n]
            check(analyse(w), stats, "actual_q_lt_2000")
    out = {"lam3": lam_table, "stats": stats, "C013_family": fam,
           "violations": stats.get("violations", [])}
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1, default=str))
    for k, v in stats.items():
        if k != "violations":
            print(" ", k, v)
    print("violations:", len(stats.get("violations", [])))
    return 0 if not stats.get("violations") else 1


if __name__ == "__main__":
    sys.exit(main())
