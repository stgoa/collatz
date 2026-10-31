#!/usr/bin/env python3
"""Certificate for doubled-words-periodic-and-antiperiodic-points.

Raw odd-only clock. For a word w = (u, v) with |u| = |v| = n and even total A = 2S, D = Phi1 * Phi2 with
Phi1 = 2^S - 3^n and Phi2 = 2^S + 3^n. Writing j = (S_v - S_u)/2 (an integer of either sign), the node proves
    gcd(C_w, Phi1) = gcd(2^j C_u + C_v, Phi1),     gcd(C_w, Phi2) = gcd(2^j C_u - C_v, Phi2)
(for j < 0 read 2^j as the inverse of 2^(-j) modulo the odd factor), i.e. Phi1 | C_w iff 2^j x_u + x_v is an
integer for the periodic points x_z = C_z/Phi1, and Phi2 | C_w iff 2^j y_u - y_v is an integer for the
antiperiodic points y_z = C_z/Phi2.  Checks:
  H1  the identities, the gcd forms and the one-letter forms on pseudo-random pairs (fixed seed);
  H2  the two-marker family (1, 2^(n-1), 3, 2^(n-1)), n <= 40, through the theorem: G = 4^n - 3^n;
  H3  every rotation pair (u_r, u_s), r < s, of every distinct cycle word of actual-cycles-3x-d-corpus:
      Phi1 | C_w iff q | n_r + n_s; for the words where it holds, rho(w), g2 = gcd(C_w, Phi2), G = Phi1 * g2
      and the half bound G^2 < 2^A; no such word with rho <= 7 violates it, the smallest violating rho is 8;
  H4  the one-letter family built from fresh scans of 3x+q' (q' | 2^j + 1): Phi1 | C_w, rho = 2, g2 recorded;
  H5  receipt comparison.
Exit status 1 on any failure.  --write-receipt regenerates doubled_words.json.  Standard library only."""
import json
import math
import random
import sys
from fractions import Fraction
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "doubled_words.json"
CORPUS = HERE.parent / "actual-cycles-3x-d-corpus" / "actual_cycles.json"
SEED = 20261030
ONE_LETTER_Q = [5, 11, 13, 17, 41, 65, 257]
ONE_LETTER_SEEDMAX = 200_000
failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL:", msg)


def intercept(z):
    C = 0
    s = 0
    n = len(z)
    for t in range(n):
        C += 3 ** (n - 1 - t) * (1 << s)
        s += z[t]
    return C


def rho(w):
    m = len(w)
    best = m
    for h in range(1, m):
        c = 0
        for i in range(m):
            if w[i] != w[(i + h) % m]:
                c += 1
                if c >= best:
                    break
        best = min(best, c)
    return best


def shifted(j, a, b):
    """2^j a + b and 2^j a - b, with 2^j read as the inverse of 2^(-j) when j < 0 (so multiply b instead)."""
    if j >= 0:
        return (1 << j) * a + b, (1 << j) * a - b
    return a + (1 << -j) * b, a - (1 << -j) * b


def ord2(q):
    if q == 1:
        return 1
    k, x = 1, 2 % q
    while x != 1:
        x = (x * 2) % q
        k += 1
    return k


def small_prime_factors(n, bound=100_000):
    out = []
    p = 3
    while p <= bound and p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 2
    if 1 < n <= bound:
        out.append(n)
    return out


# ---------------------------------------------------------------- H1: identities on random pairs
def h1():
    rng = random.Random(SEED)
    trials = 0
    while trials < 2000:
        n = rng.randint(2, 14)
        u = [rng.randint(1, 6) for _ in range(n)]
        v = [rng.randint(1, 6) for _ in range(n)]
        if (sum(u) + sum(v)) % 2:
            v[-1] += 1
        S = (sum(u) + sum(v)) // 2
        Phi1, Phi2 = (1 << S) - 3 ** n, (1 << S) + 3 ** n
        if Phi1 <= 0:
            continue
        trials += 1
        Cu, Cv = intercept(u), intercept(v)
        w = u + v
        Cw = intercept(w)
        if Cw != 3 ** n * Cu + (1 << sum(u)) * Cv:
            fail(f"H1 concatenation identity {u} {v}")
        j = (sum(v) - sum(u)) // 2
        X, Y = shifted(j, Cu, Cv)
        if gcd(Cw, Phi1) != gcd(X, Phi1):
            fail(f"H1 Phi1 gcd form {u} {v}")
        if gcd(Cw, Phi2) != gcd(Y, Phi2):
            fail(f"H1 Phi2 gcd form {u} {v}")
        # periodic and antiperiodic points
        xu, xv = Fraction(Cu, Phi1), Fraction(Cv, Phi1)
        yu, yv = Fraction(Cu, Phi2), Fraction(Cv, Phi2)
        if j >= 0:
            per = (2 ** j) * xu + xv
            anti = (2 ** j) * yu - yv
        else:
            per = xu + (2 ** -j) * xv
            anti = yu - (2 ** -j) * yv
        if (per.denominator == 1) != (Cw % Phi1 == 0):
            fail(f"H1 periodic-point criterion {u} {v}")
        if (anti.denominator == 1) != (Cw % Phi2 == 0):
            fail(f"H1 antiperiodic-point criterion {u} {v}")
        # the affine map of u recut to total S fixes x_u and sends -y_u to y_u
        T = lambda x: (3 ** n * x + Cu) / Fraction(1 << S)
        if T(xu) != xu or T(-yu) != yu:
            fail(f"H1 fixed/antifixed point {u}")
    # one-letter forms
    for _ in range(1000):
        n = rng.randint(2, 12)
        j = rng.randint(1, 4)
        u = [rng.randint(1, 6) for _ in range(n)]
        i = rng.randrange(n)
        v = u[:]
        v[i] += 2 * j
        up = u[:]
        up[i] += j
        w = u + v
        S = sum(up)
        Phi1, Phi2 = (1 << S) - 3 ** n, (1 << S) + 3 ** n
        if Phi1 <= 0:
            continue
        Cw = intercept(w)
        if Phi1 != (1 << sum(up)) - 3 ** n or gcd(Cw, Phi1) != gcd(((1 << j) + 1) * intercept(up), Phi1):
            fail(f"H1 one-letter Phi1 form {u} i={i} j={j}")
        urot = u[i + 1:] + u[:i + 1]
        if gcd(Cw, Phi2) != gcd(((1 << j) - 1) * intercept(urot), Phi2):
            fail(f"H1 one-letter Phi2 form {u} i={i} j={j}")
    return {"random_pairs": trials, "one_letter_trials": 1000}


# ---------------------------------------------------------------- H2: the two-marker family
def h2():
    for n in range(2, 41):
        u = [1] + [2] * (n - 1)
        v = [3] + [2] * (n - 1)
        w = u + v
        A = sum(w)
        D = (1 << A) - 3 ** (2 * n)
        G = gcd(intercept(w), D)
        trivial = [2] * n
        Dt = (1 << (2 * n)) - 3 ** n
        g1 = gcd(3 * intercept(trivial), Dt)             # the theorem's Phi1 part: u' = (2)^n, j = 1
        g2 = gcd(intercept([2] * (n - 1) + [1]), (1 << (2 * n)) + 3 ** n)   # u° = rotation after position 0
        if not (G == 4 ** n - 3 ** n == g1 and g2 == 1 and Dt == 4 ** n - 3 ** n):
            fail(f"H2 two-marker n={n}: G={G}, g1={g1}, g2={g2}")
    return {"n_max": 40}


# ---------------------------------------------------------------- H3: rotation pairs of actual cycles
def h3():
    corpus = json.load(open(CORPUS))
    words = {}
    for c in corpus["cycles"]:
        wd = tuple(c["word"])
        if len(wd) >= 2:
            words.setdefault(wd, c)
    pairs = 0
    hits = []
    q_mismatch = 0
    for wd, c in words.items():
        n, S = len(wd), sum(wd)
        D = (1 << S) - 3 ** n
        Phi1, Phi2 = D, (1 << S) + 3 ** n
        Cs = [intercept(wd[r:] + wd[:r]) for r in range(n)]
        gs = [gcd(Cr, D) for Cr in Cs]
        q = D // gs[0]
        if any(D // g != q for g in gs):
            fail(f"H3 denominator varies along the cycle {wd}")
        if q != c["reduced_denominator"]:
            q_mismatch += 1
        nums = [Cr // g for Cr, g in zip(Cs, gs)]
        for r in range(n):
            for s in range(r + 1, n):
                pairs += 1
                Cw = 3 ** n * Cs[r] + (1 << S) * Cs[s]      # concatenation identity (checked in H1)
                hit = (nums[r] + nums[s]) % q == 0
                if (Cw % Phi1 == 0) != hit:
                    fail(f"H3 iff fails: d={c['d']} r={r} s={s}")
                if not hit:
                    continue
                w = wd[r:] + wd[:r] + wd[s:] + wd[:s]
                G = gcd(Cw, Phi1 * Phi2)
                g2 = gcd(Cw, Phi2)
                if G != Phi1 * g2:
                    fail(f"H3 G != Phi1*g2: d={c['d']} r={r} s={s}")
                ham = sum(1 for a, b in zip(wd[r:] + wd[:r], wd[s:] + wd[:s]) if a != b)
                hits.append(dict(d=c["d"], q=q, minimum=c["minimum"], r=r, s=s, n=n, S=S, m=2 * n, ham=ham,
                                 rho=rho(w), g2=g2, excess=round(math.log2(G) - S, 4),
                                 violation=G * G >= (1 << (2 * S)), ratio=round(3 ** n / 2 ** S, 4), w=list(w)))
    by_rho = {}
    for h in hits:
        e = by_rho.setdefault(h["rho"], {"words": 0, "violations": 0, "max_excess": -1e9, "g2_gt_1": 0})
        e["words"] += 1
        e["violations"] += h["violation"]
        e["max_excess"] = max(e["max_excess"], h["excess"])
        e["g2_gt_1"] += h["g2"] > 1
    small = [h for h in hits if h["rho"] <= 7]
    if any(h["violation"] for h in small):
        fail("H3 a word with rho <= 7 violates the half bound")
    if any(h["g2"] not in (1, 5) for h in small):
        fail("H3 a word with rho <= 7 has g2 outside {1, 5}")
    viol = sorted([h for h in hits if h["violation"]], key=lambda h: (h["rho"], h["m"]))
    if not viol or viol[0]["rho"] != 8:
        fail(f"H3 smallest violating rho is not 8: {viol[:1]}")
    # labelled heuristic: expected number of rho <= 7 words with a small prime of Phi2 dividing C_w
    expect = 0.0
    for h in small:
        Phi2 = (1 << h["S"]) + 3 ** h["n"]
        expect += sum(1 / p for p in small_prime_factors(Phi2))
    near = max(small, key=lambda h: h["excess"])
    return {"distinct_words": len(words), "pairs": pairs, "hits": len(hits), "reduced_denominator_mismatches": q_mismatch,
            "by_rho": {str(k): by_rho[k] for k in sorted(by_rho)},
            "rho_le_7_words": len(small), "rho_le_7_violations": sum(h["violation"] for h in small),
            "rho_le_7_g2_gt_1": sum(h["g2"] > 1 for h in small), "rho_le_7_g2_values": sorted(set(h["g2"] for h in small)),
            "heuristic_expected_rho_le_7_words_with_small_g2": round(expect, 3),
            "violations": len(viol), "min_violating_rho": viol[0]["rho"], "min_violating_m": min(h["m"] for h in viol),
            "max_excess": max(h["excess"] for h in hits),
            "smallest_violations": [{k: h[k] for k in ("d", "q", "minimum", "r", "s", "m", "ham", "rho", "g2", "excess", "ratio", "w")}
                                    for h in viol if h["m"] <= 36],
            "closest_rho_le_7": {k: near[k] for k in ("d", "q", "minimum", "r", "s", "m", "ham", "rho", "g2", "excess", "ratio", "w")}}


# ---------------------------------------------------------------- H4: one-letter family from fresh scans
def cycles_3xq(q, seedmax):
    seen = set()
    out = {}
    for n0 in range(1, seedmax, 2):
        if n0 in seen:
            continue
        path, pos, n = [], {}, n0
        while n not in pos and n not in seen and len(path) < 5000 and n < 1 << 200:
            pos[n] = len(path)
            path.append(n)
            x, a = 3 * n + q, 0
            while x % 2 == 0:
                x //= 2
                a += 1
            n = x
        if n in pos:
            cyc = path[pos[n]:]
            k = cyc.index(min(cyc))
            cyc = cyc[k:] + cyc[:k]
            if gcd(cyc[0], q) == 1 and cyc[0] not in out:
                word = []
                for x in cyc:
                    y, a = 3 * x + q, 0
                    while y % 2 == 0:
                        y //= 2
                        a += 1
                    word.append(a)
                out[cyc[0]] = tuple(word)
        seen.update(path)
    return out


def h4():
    rows = []
    cycles_found = {}
    for q in ONE_LETTER_Q:
        o = ord2(q)
        if o % 2 or pow(2, o // 2, q) != q - 1:
            fail(f"H4 q={q} has no j with 2^j = -1")
            continue
        cyc = cycles_3xq(q, ONE_LETTER_SEEDMAX)
        cycles_found[str(q)] = sorted(cyc)
        for mn, wd in sorted(cyc.items()):
            n, Sp = len(wd), sum(wd)
            D = (1 << Sp) - 3 ** n
            if D // gcd(intercept(wd), D) != q:
                fail(f"H4 q={q} cycle at {mn} has the wrong reduced denominator")
            for j in range(o // 2, max(wd), o):
                for i, a in enumerate(wd):
                    if a <= j:
                        continue
                    u = list(wd)
                    u[i] -= j
                    v = list(wd)
                    v[i] += j
                    w = tuple(u + v)
                    Phi1, Phi2 = (1 << Sp) - 3 ** n, (1 << Sp) + 3 ** n
                    Cw = intercept(w)
                    if Cw % Phi1:
                        fail(f"H4 Phi1 does not divide C_w: q={q} min={mn} i={i} j={j}")
                    G, g2 = gcd(Cw, Phi1 * Phi2), gcd(Cw, Phi2)
                    if G != Phi1 * g2 or rho(w) != 2:
                        fail(f"H4 structure: q={q} min={mn} i={i} j={j}")
                    rows.append(dict(q=q, minimum=mn, n=n, m=2 * n, S=Sp, i=i, j=j, letter=a, g2=g2,
                                     excess=round(math.log2(G) - Sp, 6), ratio=round(3 ** n / 2 ** Sp, 4),
                                     violation=G * G >= (1 << (2 * Sp)), u_prime=list(wd)))
    return {"q_values": ONE_LETTER_Q, "seed_max": ONE_LETTER_SEEDMAX, "cycle_minima": cycles_found,
            "words": len(rows), "all_g2_one": all(r["g2"] == 1 for r in rows), "violations": sum(r["violation"] for r in rows),
            "max_excess": max(r["excess"] for r in rows) if rows else None, "rows": rows}


def main():
    write = "--write-receipt" in sys.argv
    summary = {"H1": h1(), "H2": h2(), "H3": h3(), "H4": h4()}
    if write:
        RECEIPT.write_text(json.dumps(summary, indent=1) + "\n")
        print("receipt written")
    elif not RECEIPT.exists():
        fail("H5 receipt missing")
    else:
        old = json.loads(RECEIPT.read_text())
        if old != summary:
            fail("H5 summary differs from the receipt")
    h3s, h4s = summary["H3"], summary["H4"]
    print(f"H1 {summary['H1']}")
    print(f"H3 words {h3s['distinct_words']} pairs {h3s['pairs']} hits {h3s['hits']} violations {h3s['violations']} "
          f"min violating rho {h3s['min_violating_rho']} (m={h3s['min_violating_m']}); rho<=7 words {h3s['rho_le_7_words']}, "
          f"g2>1 in {h3s['rho_le_7_g2_gt_1']} of them (heuristic expectation {h3s['heuristic_expected_rho_le_7_words_with_small_g2']}), "
          f"closest excess {h3s['closest_rho_le_7']['excess']}")
    print(f"H4 words {h4s['words']} all g2=1 {h4s['all_g2_one']} violations {h4s['violations']} max excess {h4s['max_excess']}")
    if failures:
        print(f"{len(failures)} failure(s)")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
