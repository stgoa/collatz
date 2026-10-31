#!/usr/bin/env python3
"""Certificate for half-cancellation-counterexample-rotation-pair.

K1  Direct verification of the word w = (1,1,1,1,6,1,5,1,1,2,1,5,1,1,2,1,1,1,1,6): m = 20, A = 40, D = 2^40 - 3^20 > 0,
    w primitive, rho(w) = 4 (witness: the rotation by 5; the rotation by 10 has 8), G = gcd(C_w, D) = 5 * (2^20 - 3^10),
    G^2 > 2^A;
    w is the valuation word of an actual 3x+q cycle with q = D/G; its primitive part gcd(G, Phi_20(4, 3)) = 5.
K2  The construction: rotations 3 and 8 of the 3x+1267 cycle through 197; the two states sum to 0 mod 1267.
K3  Scan: every cycle of 3x+d, d <= 20000 coprime to 6, from odd seeds <= 5000; every rotation pair (r < s) with
    d | n_r + n_s; among the resulting words with rho <= 4 (exact), count the violations of G^2 < 2^A (m >= 9),
    their cycle classes, their primitive parts, and the largest 3^n/2^S among them; no violating word is
    near-critical (3^n/2^S > 1/sqrt 2).
K4  Receipt comparison.  Exit 1 on failure; --write-receipt regenerates counterexample.json.  Standard library only."""
import json
import math
import sys
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "counterexample.json"
W = (1, 1, 1, 1, 6, 1, 5, 1, 1, 2, 1, 5, 1, 1, 2, 1, 1, 1, 1, 6)
DMAX, SEEDMAX = 20000, 5000
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


def mismatches(w, h):
    m = len(w)
    return sum(1 for i in range(m) if w[i] != w[(i + h) % m])


def rho_full(w):
    return min(mismatches(w, h) for h in range(1, len(w)))


def rho_le(w, k):
    """exact rho(w) if it is <= k, else None"""
    m = len(w)
    best = None
    for h in range(1, m):
        c = 0
        for i in range(m):
            if w[i] != w[(i + h) % m]:
                c += 1
                if c > k:
                    break
        if c <= k and (best is None or c < best):
            best = c
    return best


def is_primitive(w):
    m = len(w)
    return all(any(w[i] != w[(i + p) % m] for i in range(m)) for p in range(1, m) if m % p == 0)


def cyclotomic_value(e, x, y):
    """Phi_e(x, y) homogenised, by the Moebius product prod_{d|e} (x^d - y^d)^mu(e/d)."""
    def mu(n):
        res, p = 1, 2
        while p * p <= n:
            if n % p == 0:
                n //= p
                if n % p == 0:
                    return 0
                res = -res
            p += 1
        return -res if n > 1 else res
    num, den = 1, 1
    for d in range(1, e + 1):
        if e % d == 0:
            v = x ** d - y ** d
            if mu(e // d) == 1:
                num *= v
            elif mu(e // d) == -1:
                den *= v
    if num % den:
        fail("cyclotomic value is not an integer")
    return num // den


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
                out[cyc[0]] = (tuple(word), cyc)
        seen.update(path)
    return out


def k1():
    m, A = len(W), sum(W)
    D = (1 << A) - 3 ** m
    C = intercept(W)
    G = gcd(C, D)
    n, S = m // 2, A // 2
    Phi1, Phi2 = (1 << S) - 3 ** n, (1 << S) + 3 ** n
    ok = (m == 20 and A == 40 and D > 0 and is_primitive(W) and rho_full(W) == 4 and mismatches(W, 5) == 4
          and mismatches(W, 10) == 8 and G == 5 * Phi1 and G * G > (1 << A) and D == Phi1 * Phi2
          and W[:5] == W[15:] and W[5:10] == W[10:15])          # w = a b b a
    if not ok:
        fail("K1 direct verification")
    q = D // G
    x0 = C // G                                   # the cycle's first state as a 3x+q cycle
    # replay the orbit of x0 under 3x+q and read off the word
    states, word, x = [], [], x0
    for _ in range(m):
        states.append(x)
        y, a = 3 * x + q, 0
        while y % 2 == 0:
            y //= 2
            a += 1
        word.append(a)
        x = y
    if x != x0 or tuple(word) != W:
        fail("K1 w is not the word of the 3x+q cycle through C_w/G")
    e = gcd(A, m)
    phi_e = cyclotomic_value(e, 1 << (A // e), 3 ** (m // e))
    gprim = gcd(G, phi_e)
    if e != 20 or gprim != 5:
        fail(f"K1 primitive part: e={e}, gprim={gprim}")
    return {"m": m, "A": A, "D": D, "C_w": C, "G": G, "q": q, "G_over_Phi1": G // Phi1, "Phi1": Phi1, "Phi2": Phi2,
            "Phi2_factorisation": "5^3 * 8861" if Phi2 == 125 * 8861 else "?", "rho": 4, "witness_rotation": 5,
            "mismatches_rotation_10": mismatches(W, 10), "block_a": list(W[:5]), "block_b": list(W[5:10]),
            "log2_G_squared_over_2A": round(2 * math.log2(G) - A, 4), "cycle_min_state": min(states), "cycle_states": states,
            "e": e, "Phi_e": phi_e, "g_prim": gprim, "ratio_3n_over_2S": round(3 ** n / 2 ** S, 6)}


def k2():
    cyc = cycles_3xd(1267, SEEDMAX)
    if 197 not in cyc:
        fail("K2 the 3x+1267 cycle through 197 was not found")
        return {}
    word, states = cyc[197]
    r, s = 3, 8
    w = word[r:] + word[:r] + word[s:] + word[:s]
    if w != W or (states[r] + states[s]) % 1267:
        fail("K2 construction does not reproduce w")
    return {"d": 1267, "cycle_word": list(word), "cycle_states": states, "r": r, "s": s,
            "state_sum": states[r] + states[s], "state_sum_over_d": (states[r] + states[s]) // 1267}


def k3():
    n_words = n_hits = 0
    small, viol = [], []
    for d in range(1, DMAX + 1):
        if d % 2 == 0 or d % 3 == 0:
            continue
        for mn, (wd, states) in cycles_3xd(d, SEEDMAX).items():
            n = len(wd)
            if n < 2:
                continue
            n_words += 1
            S = sum(wd)
            Phi1, Phi2 = (1 << S) - 3 ** n, (1 << S) + 3 ** n
            for r in range(n):
                for s in range(r + 1, n):
                    if (states[r] + states[s]) % d:
                        continue
                    n_hits += 1
                    w = wd[r:] + wd[:r] + wd[s:] + wd[:s]
                    rh = rho_le(w, 4)
                    if rh is None:
                        continue
                    Cw = intercept(w)
                    if Cw % Phi1:
                        fail(f"K3 Phi1 does not divide C_w for d={d}, min={mn}, r={r}, s={s}")
                    G = gcd(Cw, Phi1 * Phi2)
                    g2 = gcd(Cw, Phi2)
                    rec = dict(d=d, minimum=mn, r=r, s=s, m=2 * n, rho=rh, g2=g2, excess=round(math.log2(G) - S, 4),
                               ratio=round(3 ** n / 2 ** S, 6), violation=bool(G * G >= (1 << (2 * S))))
                    small.append(rec)
                    if rec["violation"] and rec["m"] >= 9:
                        viol.append(rec)
    classes = sorted({(v["d"], v["minimum"]) for v in viol})
    if any(2 * (v["s"] - v["r"]) != v["m"] // 2 for v in viol):
        fail("K3 a violating pair is not at distance n/2")
    near = [x for x in small if x["ratio"] > 1 / math.sqrt(2)]
    if not viol or any(v["g2"] != 5 for v in viol) or any(v["ratio"] > 1 / math.sqrt(2) for v in viol):
        fail("K3 violation structure differs from the claim")
    if len(classes) != 3 or sorted(v["m"] for v in viol) != [20, 20, 28, 28, 28, 28, 36, 36, 36, 36, 36, 36]:
        fail(f"K3 classes {classes}, m values {sorted(v['m'] for v in viol)}")
    return {"d_max": DMAX, "seed_max": SEEDMAX, "cycle_words": n_words, "pair_hits": n_hits, "rho_le_4_words": len(small),
            "violations": len(viol), "violating_classes": [list(c) for c in classes],
            "violating_m": sorted(v["m"] for v in viol), "violating_g2": sorted(set(v["g2"] for v in viol)),
            "all_violating_pairs_at_distance_n_over_2": all(2 * (v["s"] - v["r"]) == v["m"] // 2 for v in viol),
            "max_violating_ratio": max(v["ratio"] for v in viol), "max_violating_excess": max(v["excess"] for v in viol),
            "g2_values_rho_le_4": sorted(set(x["g2"] for x in small)),
            "near_critical_rho_le_4_words": len(near), "near_critical_max_excess": max((x["excess"] for x in near), default=None),
            "violations_detail": viol}


def main():
    write = "--write-receipt" in sys.argv
    summary = {"K1": k1(), "K2": k2(), "K3": k3()}
    if write:
        RECEIPT.write_text(json.dumps(summary, indent=1) + "\n")
        print("receipt written")
    elif not RECEIPT.exists():
        fail("K4 receipt missing")
    elif json.loads(RECEIPT.read_text()) != summary:
        fail("K4 summary differs from the receipt")
    k1s, k3s = summary["K1"], summary["K3"]
    print(f"K1 G={k1s['G']} = {k1s['G_over_Phi1']}*Phi1, q={k1s['q']}, log2(G^2/2^A)={k1s['log2_G_squared_over_2A']}, "
          f"g_prim={k1s['g_prim']}, cycle min {k1s['cycle_min_state']}")
    print(f"K3 words {k3s['cycle_words']} hits {k3s['pair_hits']} rho<=4 {k3s['rho_le_4_words']} violations {k3s['violations']} "
          f"classes {k3s['violating_classes']} max ratio {k3s['max_violating_ratio']} near-critical words {k3s['near_critical_rho_le_4_words']} "
          f"(max excess {k3s['near_critical_max_excess']})")
    if failures:
        print(f"{len(failures)} failure(s)")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
