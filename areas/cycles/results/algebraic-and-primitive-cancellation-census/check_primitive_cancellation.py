#!/usr/bin/env python3
"""Algebraic versus primitive cancellation in few-arc rotation codings (exact census).

Written at the 2026-10-28 batch (Claude, Fable 5.1). Standard library, exact integers; run from the
repository root:  python3 <this file> [--write-receipt].  Exits 1 on any failure. About a minute.

For a positive word w (length m, total A, D = 2^A - 3^m > 0) put e = gcd(A, m), x = 2^(A/e), y = 3^(m/e).
Then D = x^e - y^e = prod_{d | e} Phi_d(x, y) with Phi_d the homogenised cyclotomic polynomials. The
PRIMITIVE factor is Phi_e(x, y) (for e = 1 it is D itself); the other factors are the ALGEBRAIC part, which
exists only when gcd(A, m) > 1. For G = gcd(C_w, D) we record the primitive cancellation
    g_prim = gcd(G, Phi_e(x, y)).
The five censuses are those of few-arc-codings-denominator-census (same enumeration, primitive words, one
per rotation class). Checks (hard):
  P1  the recorded maximum of g_prim in each census is reproduced, and g_prim < 2^17 everywhere;
  P2  every word with gcd(A, m) = 1 has G = g_prim < 2^17;
  P3  the per-census summary (counts of g_prim = 1, tail counts #{g_prim >= 2^k}, maxima, the words with
      log2 G >= A/4 and how many of them have gcd(A, m) > 1, per-m maxima) is reproduced exactly.
"""
from __future__ import annotations

import itertools
import json
import math
import sys
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "primitive_cancellation.json"
LOG2_3 = math.log2(3)
TAIL_KS = (2, 4, 6, 8, 10, 12, 14, 16)

CENSUSES = [
    ("s2_v4", 2, 40, 4, (1,), 0),
    ("s2_v8", 2, 36, 8, (1,), 0),
    ("s2_gcd", 2, 30, 4, (2, 3), 4),
    ("s3_v4", 3, 30, 4, (1,), 0),
    ("s4_v3", 4, 22, 3, (1,), 0),
]


def intercept(w):
    C = sj = 0
    m = len(w)
    for j in range(m):
        C += 3 ** (m - 1 - j) << sj
        sj += w[j]
    return C, sj


def primitive(w):
    m = len(w)
    return all(w != w[p:] + w[:p] for p in range(1, m) if m % p == 0)


def canonical(w):
    m = len(w)
    return min(tuple(w[i:] + w[:i]) for i in range(m))


def mobius(n):
    r, p, nn = 1, 2, n
    while p * p <= nn:
        if nn % p == 0:
            nn //= p
            if nn % p == 0:
                return 0
            r = -r
        p += 1
    if nn > 1:
        r = -r
    return r


def primitive_factor(A, m):
    """Phi_e(2^(A/e), 3^(m/e)) for e = gcd(A, m), via Phi_e(x,y) = prod_{d|e} (x^d - y^d)^{mu(e/d)}."""
    e = gcd(A, m)
    x, y = 2 ** (A // e), 3 ** (m // e)
    num = den = 1
    for d in range(1, e + 1):
        if e % d == 0:
            mu = mobius(e // d)
            if mu == 1:
                num *= x ** d - y ** d
            elif mu == -1:
                den *= x ** d - y ** d
    if num % den:
        raise SystemExit("internal: cyclotomic quotient not integral")
    return num // den, e


def coded_words(m, s, vmax, g, cmax):
    n = m // g
    if n <= s:
        return
    for hh in range(1, n):
        if gcd(hh, n) != 1:
            continue
        hinv = pow(hh, -1, n)
        for cuts in itertools.combinations(range(1, n), s - 1):
            bounds = (0,) + cuts + (n,)
            for vals in itertools.product(range(1, vmax + 1), repeat=s):
                if any(vals[r] == vals[(r + 1) % s] for r in range(s)):
                    continue
                track = [0] * n
                for r in range(s):
                    for k in range(bounds[r], bounds[r + 1]):
                        track[k] = vals[r]
                active = [track[(j * hinv) % n] for j in range(n)]
                consts = itertools.product(range(1, cmax + 1), repeat=g - 1) if g > 1 else [()]
                for cs in consts:
                    w = [0] * m
                    for j in range(n):
                        w[j * g] = active[j]
                    for r in range(1, g):
                        for j in range(n):
                            w[j * g + r] = cs[r - 1]
                    yield w


def census(name, s, mmax, vmax, gs, cmax):
    N = n_one = n_e1 = 0
    tails = {k: 0 for k in TAIL_KS}
    max_gp = (0, None)          # (g_prim, word info)
    max_ratio = (0.0, None)     # log2(g_prim)/A
    max_g_e1 = (0, None)        # largest G among gcd(A,m)=1 words
    big = big_alg = 0           # words with log2 G >= A/4, and those with e > 1
    big_max_gp = 0
    per_m = {}
    for m in range(3, mmax + 1):
        seen = set()
        pm_max = 0
        for g in gs:
            if m % g:
                continue
            for w in coded_words(m, s, vmax, g, cmax):
                if not primitive(w):
                    continue
                key = canonical(w)
                if key in seen:
                    continue
                seen.add(key)
                C, A = intercept(w)
                D = (1 << A) - 3 ** m
                if D <= 0:
                    continue
                G = gcd(C, D)
                Phi, e = primitive_factor(A, m)
                gp = gcd(G, Phi)
                N += 1
                n_one += (gp == 1)
                for k in TAIL_KS:
                    tails[k] += (gp >= 1 << k)
                if gp > max_gp[0]:
                    max_gp = (gp, {"m": m, "A": A, "e": e, "G": G, "w": w})
                if gp > 1 and math.log2(gp) / A > max_ratio[0]:
                    max_ratio = (round(math.log2(gp) / A, 4), {"m": m, "A": A, "e": e, "G": G, "w": w})
                if e == 1:
                    n_e1 += 1
                    if G != gp:
                        raise SystemExit("internal: e = 1 but G != g_prim")
                    if G > max_g_e1[0]:
                        max_g_e1 = (G, {"m": m, "A": A, "w": w})
                    if G >= 1 << 17:
                        raise SystemExit(f"P2 FAIL: gcd(A,m)=1 word with G = {G} >= 2^17: m={m} w={w}")
                if gp >= 1 << 17:
                    raise SystemExit(f"P1 FAIL: g_prim = {gp} >= 2^17 at m={m} w={w}")
                if G > 1 and math.log2(G) >= A / 4:
                    big += 1
                    big_alg += (e > 1)
                    big_max_gp = max(big_max_gp, gp)
                pm_max = max(pm_max, gp)
        if seen:
            per_m[str(m)] = {"max_g_prim": pm_max, "max_log2_g_prim": round(math.log2(pm_max), 2) if pm_max > 1 else 0.0}
    return {"s": s, "mmax": mmax, "letters": vmax, "gcd": list(gs), "const_letters": cmax,
            "words": N, "g_prim_equals_1": n_one, "tail_counts": {str(k): tails[k] for k in TAIL_KS},
            "tail_ratio_to_N_over_x": {str(k): round(tails[k] * (1 << k) / N, 3) for k in TAIL_KS},
            "max_g_prim": max_gp[0], "max_log2_g_prim": round(math.log2(max_gp[0]), 2), "max_g_prim_word": max_gp[1],
            "max_log2_g_prim_over_A": max_ratio[0], "max_log2_g_prim_over_A_word": max_ratio[1],
            "gcd_A_m_equals_1_words": n_e1, "max_G_among_gcd1_words": max_g_e1[0],
            "max_log2_G_among_gcd1_words": round(math.log2(max_g_e1[0]), 2), "max_G_among_gcd1_word": max_g_e1[1],
            "words_with_log2G_ge_A_over_4": big, "of_which_gcd_A_m_gt_1": big_alg,
            "max_g_prim_among_them": big_max_gp, "per_m": per_m}


def main(argv):
    result = {"schema": 1, "censuses": {}}
    for row in CENSUSES:
        result["censuses"][row[0]] = census(*row)
    text = json.dumps(result, indent=1, sort_keys=True) + "\n"
    if "--write-receipt" in argv:
        RECEIPT.write_text(text, encoding="utf-8")
        print("receipt written")
    elif not RECEIPT.exists() or RECEIPT.read_text(encoding="utf-8") != text:
        raise SystemExit("P3 FAIL: receipt mismatch")
    for name, c in result["censuses"].items():
        print(f"PASS {name}: {c['words']} words, g_prim = 1 for {c['g_prim_equals_1']}, max g_prim = {c['max_g_prim']} "
              f"(2^{c['max_log2_g_prim']}), max log2 g_prim / A = {c['max_log2_g_prim_over_A']}, "
              f"gcd(A,m)=1 words {c['gcd_A_m_equals_1_words']} with max G = {c['max_G_among_gcd1_words']}, "
              f"log2 G >= A/4: {c['words_with_log2G_ge_A_over_4']} words ({c['of_which_gcd_A_m_gt_1']} with gcd(A,m) > 1)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
