#!/usr/bin/env python3
"""Certificate for rotation-pair-words-exact-cancellation.

For the valuation word u of an actual 3x+d cycle (length n, total S, states n_0..n_(n-1), reduced denominator d,
G_u = gcd(C_u, D_u) = (2^S - 3^n)/d) and 0 <= r < s < n, the word w = (R_r u, R_s u) has
    gcd(C_w, D_w) = G_u * gcd(n_r + n_s, d) * gcd(n_r - n_s, 2^S + 3^n),
    D_w / gcd(C_w, D_w) = d * (2^S + 3^n) / (gcd(n_r + n_s, d) * gcd(n_r - n_s, 2^S + 3^n)).
R1  every rotation pair of every distinct cycle word (n >= 2) of actual-cycles-3x-d-corpus: both formulas, directly;
    also C_(R_r u) = n_r * G_u for every r, and the bound gcd(C_w, D_w) <= (2^S - 3^n) * |n_r - n_s|.
R2  every rotation pair of every cycle of 3x+d, d <= 3000 coprime to 6, from odd seeds <= 5000 (cycles found by
    iteration, states coprime to d): both formulas; counts recorded.
R3  the counterexample of half-cancellation-counterexample-rotation-pair: d = 1267, states 1837 and 697.
R4  receipt comparison.  Exit 1 on failure; --write-receipt regenerates rotation_pairs.json.  Standard library only."""
import json
import math
import sys
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "rotation_pairs.json"
CORPUS = HERE.parent / "actual-cycles-3x-d-corpus" / "actual_cycles.json"
DMAX, SEEDMAX = 3000, 5000
failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL:", msg)


def intercept(z):
    C, s, n = 0, 0, len(z)
    for t in range(n):
        C += 3 ** (n - 1 - t) * (1 << s)
        s += z[t]
    return C


def check_word(wd, label, stats):
    """all rotation pairs of one primitive cycle word wd; returns False on a formula failure"""
    n, S = len(wd), sum(wd)
    D = (1 << S) - 3 ** n
    Phi2 = (1 << S) + 3 ** n
    Cs = [intercept(wd[r:] + wd[:r]) for r in range(n)]
    Gu = gcd(Cs[0], D)
    d = D // Gu
    states = []
    for Cr in Cs:
        if Cr % Gu:
            fail(f"{label}: C_(R_r u) is not a multiple of G_u")
            return
        states.append(Cr // Gu)
    if len(set(states)) != n:
        stats["nonprimitive"] += 1
        return
    for r in range(n):
        for s in range(r + 1, n):
            Cw = 3 ** n * Cs[r] + (1 << S) * Cs[s]
            G = gcd(Cw, D * Phi2)
            g1 = gcd(states[r] + states[s], d)
            g2 = gcd(abs(states[r] - states[s]), Phi2)
            stats["pairs"] += 1
            if G != Gu * g1 * g2:
                fail(f"{label}: gcd formula fails at r={r}, s={s}")
                return
            if (D * Phi2) // G != d * Phi2 // (g1 * g2):
                fail(f"{label}: denominator formula fails at r={r}, s={s}")
                return
            if G > D * abs(states[r] - states[s]):
                fail(f"{label}: bound fails at r={r}, s={s}")
                return
            stats["max_g2"] = max(stats["max_g2"], g2)
            stats["g1_full"] += g1 == d
            stats["g2_gt_1"] += g2 > 1
            if G * G >= (1 << (2 * S)):
                stats["violations"] += 1
                stats["violations_with_g1_full"] += g1 == d


def r1():
    corpus = json.load(open(CORPUS))
    words = {}
    for c in corpus["cycles"]:
        wd = tuple(c["word"])
        if len(wd) >= 2:
            words.setdefault(wd, c["d"])
    stats = dict(words=len(words), pairs=0, nonprimitive=0, max_g2=0, g1_full=0, g2_gt_1=0, violations=0, violations_with_g1_full=0)
    for wd, d in words.items():
        check_word(wd, f"corpus d={d}", stats)
    return stats


def cycles_3xd(d, seedmax):
    seen, out = set(), {}
    for n0 in range(1, seedmax, 2):
        if n0 in seen:
            continue
        path, pos, n = [], {}, n0
        while n not in pos and n not in seen and len(path) < 3000 and n < 1 << 120:
            pos[n] = len(path)
            path.append(n)
            x, a = 3 * n + d, 0
            while x % 2 == 0:
                x //= 2
                a += 1
            n = x
        if n in pos:
            cyc = path[pos[n]:]
            k = cyc.index(min(cyc))
            cyc = cyc[k:] + cyc[:k]
            if gcd(cyc[0], d) == 1 and cyc[0] not in out:
                word = []
                for x in cyc:
                    y, a = 3 * x + d, 0
                    while y % 2 == 0:
                        y //= 2
                        a += 1
                    word.append(a)
                out[cyc[0]] = tuple(word)
        seen.update(path)
    return out


def r2():
    stats = dict(d_max=DMAX, seed_max=SEEDMAX, words=0, pairs=0, nonprimitive=0, max_g2=0, g1_full=0, g2_gt_1=0, violations=0, violations_with_g1_full=0)
    for d in range(1, DMAX + 1):
        if d % 2 == 0 or d % 3 == 0:
            continue
        for mn, wd in cycles_3xd(d, SEEDMAX).items():
            if len(wd) < 2:
                continue
            stats["words"] += 1
            check_word(wd, f"d={d} min={mn}", stats)
    return stats


def r3():
    d, n_r, n_s = 1267, 1837, 697
    S, n = 20, 10
    Phi1, Phi2 = (1 << S) - 3 ** n, (1 << S) + 3 ** n
    g1, g2 = gcd(n_r + n_s, d), gcd(n_r - n_s, Phi2)
    Gu = Phi1 // d
    if Phi1 % d or g1 != 1267 or g2 != 5 or Gu * g1 * g2 != 4947635 or d * Phi2 // (g1 * g2) != 221525:
        fail("R3 counterexample numbers")
    return {"d": d, "n_r": n_r, "n_s": n_s, "G_u": Gu, "g1": g1, "g2": g2, "G": Gu * g1 * g2, "q": d * Phi2 // (g1 * g2)}


def main():
    write = "--write-receipt" in sys.argv
    summary = {"R1": r1(), "R2": r2(), "R3": r3()}
    if write:
        RECEIPT.write_text(json.dumps(summary, indent=1) + "\n")
        print("receipt written")
    elif not RECEIPT.exists():
        fail("R4 receipt missing")
    elif json.loads(RECEIPT.read_text()) != summary:
        fail("R4 summary differs from the receipt")
    for k in ("R1", "R2"):
        s = summary[k]
        print(f"{k}: words {s['words']} pairs {s['pairs']} nonprimitive {s['nonprimitive']} max g2 {s['max_g2']} g1=d in {s['g1_full']} "
              f"g2>1 in {s['g2_gt_1']} violations {s['violations']} (with g1=d: {s['violations_with_g1_full']})")
    if failures:
        print(f"{len(failures)} failure(s)")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
