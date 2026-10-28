#!/usr/bin/env python3
"""Exact census of cancellation and reduced denominators in few-arc rotation codings.

Written at the 2026-10-28 batch (Claude, Fable 5.1). Standard library, exact integers; run from the
repository root:  python3 <this file> [--write-receipt].  Exits 1 on any failure.

Objects. A positive valuation word w of length m with a rotation h, gcd(h, m) = 1, having exactly s
mismatches is the coding of the circle rotation k -> k+1 along the h-track into s arcs of constant letter:
position j carries the letter of the arc containing j*h^(-1) mod m, and consecutive arcs carry different
letters. For gcd(h, m) = g > 1 with two mismatches, one residue class mod g is such a two-arc track and the
other classes carry constant letters (two-defect-cancellation-bound, part 1). Every such word is enumerated
(primitive words only, one representative per rotation class) in the five censuses below, and for each word
we record A, D = 2^A - 3^m > 0, gcd(C_w, D) = G, q = D/G, the candidate ratio
    log2 R = s*log2 G + 2m - A s - m log2 3        (rotation-defect-denominator-candidate: R < 1),
and the half-cancellation excess  log2 G - A/2.

Checks (all hard; any failure exits 1):
  C1  R < 1 for every word of every census (the candidate holds throughout).
  C2  log2 G < A/2 for every word with m >= 9 (and the full list of exceptions with m <= 8 is as recorded).
  C3  the per-m minima of log2 q / m are as recorded; in particular the recorded floor for m >= 9 holds.
  C4  the marker family (1, 2^(n-1), 3, 2^(n-1)), m = 2n, has G = 4^n - 3^n and q = 4^n + 3^n exactly, and
      its rotation by n has exactly two mismatches, for 1 <= n <= 60.
  C5  the receipt (summary per census and per m) is reproduced exactly.
  C6  for m = 12, 16, ..., 40 the two-arc word with letters (1, 3) on two equal arcs along the track of
      h = m/2 - 1 has G = (2^m - 3^(m/2))/7 (an observed exact identity; no proof is claimed).
"""
from __future__ import annotations

import itertools
import json
import math
import sys
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "few_arc_census.json"
LOG2_3 = math.log2(3)

CENSUSES = [
    # name, s, mmax, vmax, gcd range, const-track letters
    ("s2_v4", 2, 40, 4, (1,), 0),
    ("s2_v8", 2, 36, 8, (1,), 0),
    ("s2_gcd", 2, 30, 4, (2, 3), 4),
    ("s3_v4", 3, 30, 4, (1,), 0),
    ("s4_v3", 4, 22, 3, (1,), 0),
]


def intercept(w):
    m = len(w)
    C = 0
    sj = 0
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


def mismatches(w, h):
    m = len(w)
    return sum(1 for i in range(m) if w[i] != w[(i + h) % m])


def coded_words(m, s, vmax, g, cmax):
    """Yield the words of length m that are s-arc codings along a track of gcd g (constant other tracks)."""
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
                    yield w, hh * g


def census(name, s, mmax, vmax, gs, cmax):
    per_m = {}
    exceptions_c2 = []
    for m in range(3, mmax + 1):
        seen = set()
        n_words = n_disc = n_g1 = 0
        min_logq = None
        min_word = None
        max_excess = None
        max_logR = None
        nc_min_logq = None
        nc_min_margin = None
        nc_count = 0
        for g in gs:
            if m % g:
                continue
            for w, h in coded_words(m, s, vmax, g, cmax):
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
                q = D // G
                logq = math.log2(q)
                logG = math.log2(G)
                logR = s * logG + 2 * m - A * s - m * LOG2_3
                excess = logG - A / 2
                n_words += 1
                n_disc += (m >= 6 * s)
                n_g1 += (G > 1)
                if min_logq is None or q < min_word[0]:
                    min_logq, min_word = logq, (q, h, w, A, G)
                if max_excess is None or excess > max_excess:
                    max_excess = excess
                if max_logR is None or logR > max_logR:
                    max_logR = logR
                if logR >= 0:
                    raise SystemExit(f"C1 FAIL: candidate violated at {name} m={m} w={w} h={h} G={G}")
                if excess >= 0:
                    exceptions_c2.append((m, w, h, A, G, q))
                    if m >= 9:
                        raise SystemExit(f"C2 FAIL: G >= 2^(A/2) at {name} m={m} w={w} G={G} A={A}")
                if A <= m * LOG2_3 + 1:
                    nc_count += 1
                    if nc_min_logq is None or logq < nc_min_logq:
                        nc_min_logq = logq
                    if s == 2:
                        # the proved two-defect bound (7): q > (1 - 3^m/2^A) (2/sqrt3)^m
                        bound = math.log2(D) - A + m * (1 - LOG2_3 / 2)
                        margin = logq - bound
                        if nc_min_margin is None or margin < nc_min_margin:
                            nc_min_margin = margin
        if n_words == 0:
            continue
        per_m[str(m)] = {
            "words": n_words, "discriminating": n_disc, "with_cancellation": n_g1,
            "min_log2q": round(min_logq, 4), "min_log2q_over_m": round(min_logq / m, 4),
            "min_q_word": {"q": min_word[0], "h": min_word[1], "w": min_word[2], "A": min_word[3], "G": min_word[4]},
            "max_log2G_minus_half_A": round(max_excess, 4), "max_log2R": round(max_logR, 4),
            "near_critical_words": nc_count,
            "near_critical_min_log2q": None if nc_min_logq is None else round(nc_min_logq, 4),
            "near_critical_min_margin_over_bound7": None if nc_min_margin is None else round(nc_min_margin, 4),
        }
    floor9 = min(v["min_log2q_over_m"] for k, v in per_m.items() if int(k) >= 9)
    return {"s": s, "mmax": mmax, "letters": vmax, "gcd": list(gs), "const_letters": cmax,
            "total_words": sum(v["words"] for v in per_m.values()),
            "total_discriminating": sum(v["discriminating"] for v in per_m.values()),
            "max_log2R": max(v["max_log2R"] for v in per_m.values()),
            "max_log2G_minus_half_A_m_ge_9": max(v["max_log2G_minus_half_A"] for k, v in per_m.items() if int(k) >= 9),
            "min_log2q_over_m_m_ge_9": floor9,
            "half_cancellation_exceptions": [{"m": e[0], "w": e[1], "h": e[2], "A": e[3], "G": e[4], "q": e[5]} for e in exceptions_c2],
            "per_m": per_m}


def marker_family(nmax=60):
    out = []
    for n in range(1, nmax + 1):
        w = [1] + [2] * (n - 1) + [3] + [2] * (n - 1)
        C, A = intercept(w)
        m = 2 * n
        D = (1 << A) - 3 ** m
        G = gcd(C, D)
        if A != 4 * n or G != 4 ** n - 3 ** n or D // G != 4 ** n + 3 ** n or mismatches(w, n) != 2 or not primitive(w):
            raise SystemExit(f"C4 FAIL at n={n}: G={G} q={D // G}")
        out.append({"n": n, "m": m, "A": A, "G": G, "q": D // G})
    return out


def half_swap_identity():
    out = []
    for m in range(12, 41, 4):
        h = m // 2 - 1
        hinv = pow(h, -1, m)
        w = [1 if (j * hinv) % m < m // 2 else 3 for j in range(m)]
        C, A = intercept(w)
        D = (1 << A) - 3 ** m
        G = gcd(C, D)
        P = (1 << m) - 3 ** (m // 2)
        if A != 2 * m or P % 7 or G != P // 7:
            raise SystemExit(f"C6 FAIL at m={m}: G={G}, (2^m-3^(m/2))/7={P / 7}")
        out.append({"m": m, "h": h, "G": G})
    return out


def main(argv):
    result = {"schema": 1, "censuses": {}, "marker_family_checked_up_to_n": 60}
    for name, s, mmax, vmax, gs, cmax in CENSUSES:
        result["censuses"][name] = census(name, s, mmax, vmax, gs, cmax)
    result["marker_family_first_rows"] = marker_family()[:8]
    result["half_swap_identity"] = half_swap_identity()
    text = json.dumps(result, indent=1, sort_keys=True) + "\n"
    if "--write-receipt" in argv:
        RECEIPT.write_text(text, encoding="utf-8")
        print("receipt written")
    else:
        if not RECEIPT.exists() or RECEIPT.read_text(encoding="utf-8") != text:
            raise SystemExit("C5 FAIL: receipt mismatch (run with --write-receipt only after reviewing the diff)")
    for name, c in result["censuses"].items():
        print(f"PASS {name}: {c['total_words']} words, {c['total_discriminating']} discriminating, "
              f"max log2 R = {c['max_log2R']}, max log2 G - A/2 (m>=9) = {c['max_log2G_minus_half_A_m_ge_9']}, "
              f"min log2 q / m (m>=9) = {c['min_log2q_over_m_m_ge_9']}, exceptions = {len(c['half_cancellation_exceptions'])}")
    print("PASS marker family n <= 60: G = 4^n - 3^n, q = 4^n + 3^n, two mismatches")
    print("PASS half-swap (1,3) words, m = 12..40 step 4: G = (2^m - 3^(m/2))/7")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
