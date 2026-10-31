#!/usr/bin/env python3
"""Adversarial test of the primitive-cancellation conjecture at e = gcd(A, m) = 2.

Written at the 2026-10-28 batch (Claude, Fable 5.1). Standard library, exact integers; run from the
repository root:  python3 <this file> [--write-receipt].  Exits 1 on any failure. About a minute.

Setting. For A, m even put x = 2^(A/2), y = 3^(m/2), D = (x - y)(x + y) = Phi_1 * Phi_2. For a word
w = (u, v) with |u| = |v| = m/2 and S_u - S_v = Delta (even), C_w = 3^(m/2) C_u + 2^(S_u) C_v, hence
    Phi_1 | C_w  <=>  C_u = -2^(Delta/2) C_v (mod Phi_1),      Phi_2 | C_w  <=>  C_u = 2^(Delta/2) C_v (mod Phi_2).
Since Phi_2 < 2^(A/2 + 1) is odd, the primitive conjecture g_prim < 2^(A/2) at e = 2 is equivalent to Phi_2 not
dividing C_w. The near-doubled words are the natural adversaries with few mismatches:
  (T) v = u with two letters a = u_i, b = u_k swapped (rotation by m/2 has 4 mismatches):
      Phi_2 | C_w  <=>  Phi_2 | (2^(b-a) - 1) F(z),  z = u[i+1..k-1],  F(z) = sum_{t<=|z|} 3^(|z|-t) 2^(sigma_t);
  (O) v = u with one letter raised by 2j (rotation by m/2 has 2 mismatches): Phi_2 | C_w <=> 2^j C_u = C_v.
Checks (hard):
  N1  the reduction identities above hold on 2000 pseudo-random pairs (u, v) (fixed seed);
  N2  (T): every sub-word z with |z| <= n-2, sum z <= B-n+|z|-1, for n = 5..11, ceil(n log2 3) <= B <= 2.3n,
      and k = |b-a| <= 5: no F(z) = 0 mod Phi_2/gcd(Phi_2, 2^k-1) that extends to a primitive w with
      Phi_2 | C_w; the sub-word counts (and hence the uniform-heuristic expectations) are as recorded;
  N3  (O): n = 5..9, j in {1, 2}, every u and position: no hit; the condition counts are as recorded;
  N4  among the e = 2 words of the five few-arc censuses (few-arc-codings-denominator-census), the primitive
      part never reaches Phi_2: the recorded maximum of log2(g_prim) - A/2 is negative and reproduced.
"""
from __future__ import annotations

import itertools
import json
import math
import random
import sys
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "near_doubled.json"
LOG2_3 = math.log2(3)
KMAX = 5


def intercept(w):
    C = s = 0
    m = len(w)
    for j in range(m):
        C += 3 ** (m - 1 - j) << s
        s += w[j]
    return C, s


def primitive(w):
    m = len(w)
    return all(w != w[p:] + w[:p] for p in range(1, m) if m % p == 0)


def compositions(B, n):
    if n == 1:
        yield (B,)
        return
    for first in range(1, B - n + 2):
        for rest in compositions(B - first, n - 1):
            yield (first,) + rest


# ---------------------------------------------------------------- N1: the reduction identities
def check_reduction():
    rng = random.Random(20261028)
    tested = 0
    for _ in range(2000):
        n = rng.randint(2, 9)
        u = [rng.randint(1, 4) for _ in range(n)]
        v = [rng.randint(1, 4) for _ in range(n)]
        if (sum(u) - sum(v)) % 2:
            v[0] += 1
        w = u + v
        C, A = intercept(w)
        Cu, Su = intercept(u)
        Cv, Sv = intercept(v)
        x, y = 1 << (A // 2), 3 ** n
        P1, P2 = x - y, x + y
        if P1 <= 0:
            continue
        half = (Su - Sv) // 2
        for P, sign in ((P1, -1), (P2, 1)):
            t = pow(2, half, P) if half >= 0 else pow(pow(2, -half, P), -1, P)
            lhs = C % P == 0
            rhs = (Cu - sign * t * Cv) % P == 0
            if lhs != rhs:
                raise SystemExit(f"N1 FAIL: reduction identity fails for u={u} v={v}")
        tested += 1
    return tested


# ---------------------------------------------------------------- N2: transpositions via sub-words
def transposition_search(n, B):
    P = (1 << B) + 3 ** n
    mods = {k: P // gcd(P, (1 << k) - 1) for k in range(1, KMAX + 1)}
    nodes = 0
    hits = []
    stack = [([], 1 % P, 0)]
    while stack:
        z, F, sig = stack.pop()
        nodes += 1
        L = len(z)
        for k, M in mods.items():
            if F % M:
                continue
            rem = n - L - 2
            for a in range(1, 9):
                for b in (a + k, a - k):
                    if b < 1:
                        continue
                    rest = B - sig - a - b
                    if (rem == 0 and rest != 0) or (rem > 0 and rest < rem):
                        continue
                    tail = [1] * rem
                    if rem:
                        tail[-1] += rest - rem
                    for split in range(rem + 1):
                        u = tail[:split] + [a] + z + [b] + tail[split:]
                        v = list(u)
                        i = split
                        kk = i + 1 + L
                        v[i], v[kk] = v[kk], v[i]
                        w = u + v
                        if not primitive(w):
                            continue
                        C, A = intercept(w)
                        D = (1 << A) - 3 ** len(w)
                        if D > 0 and C % ((1 << (A // 2)) + 3 ** n) == 0:
                            hits.append({"u": u, "v": v})
        if L < n - 2:
            c = 1
            while sig + c <= B - n + L:
                stack.append((z + [c], (3 * F + pow(2, sig + c, P)) % P, sig + c))
                c += 1
    return nodes, hits


# ---------------------------------------------------------------- N3: one letter raised by 2j
def one_letter_search(n, B, j):
    P = (1 << (B + j)) + 3 ** n
    if (1 << (B + j)) <= 3 ** n:
        return 0, []
    pow3 = [pow(3, n - 1 - l, P) for l in range(n)]
    f = (1 << (2 * j)) - 1
    conditions = 0
    hits = []
    for u in compositions(B, n):
        s = 0
        terms = []
        for l in range(n):
            terms.append(pow3[l] * pow(2, s, P) % P)
            s += u[l]
        Cu = sum(terms) % P
        target = Cu * pow(2, j, P) % P
        suf = 0
        sufs = [0] * (n + 1)
        for l in range(n - 1, -1, -1):
            suf = (suf + terms[l]) % P
            sufs[l] = suf
        for i in range(n):
            conditions += 1
            if (Cu + f * sufs[i + 1]) % P == target:
                v = list(u)
                v[i] += 2 * j
                w = list(u) + v
                if primitive(w):
                    C, A = intercept(w)
                    if (1 << A) - 3 ** len(w) > 0 and C % P == 0:
                        hits.append({"u": list(u), "v": v})
    return conditions, hits


# ---------------------------------------------------------------- N4: e = 2 words of the censuses
CENSUSES = [("s2_v4", 2, 40, 4, (1,), 0), ("s2_v8", 2, 36, 8, (1,), 0), ("s2_gcd", 2, 30, 4, (2, 3), 4),
            ("s3_v4", 3, 30, 4, (1,), 0), ("s4_v3", 4, 22, 3, (1,), 0)]


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


def census_e2():
    count = with_gp = 0
    best = (-1e9, None)
    for name, s, mmax, vmax, gs, cmax in CENSUSES:
        for m in range(3, mmax + 1):
            seen = set()
            for g in gs:
                if m % g:
                    continue
                for w in coded_words(m, s, vmax, g, cmax):
                    if not primitive(w):
                        continue
                    key = min(tuple(w[i:] + w[:i]) for i in range(m))
                    if key in seen:
                        continue
                    seen.add(key)
                    C, A = intercept(w)
                    D = (1 << A) - 3 ** m
                    if D <= 0 or gcd(A, m) != 2:
                        continue
                    count += 1
                    P2 = (1 << (A // 2)) + 3 ** (m // 2)
                    gp = gcd(gcd(C, D), P2)
                    if gp > 1:
                        with_gp += 1
                        ex = math.log2(gp) - A / 2
                        if ex > best[0]:
                            best = (ex, {"census": name, "m": m, "A": A, "w": w, "g_prim": gp, "Phi2": P2})
                    if gp == P2:
                        raise SystemExit(f"N4 FAIL: Phi_2 divides C_w for the census word {w}")
    return {"e2_words": count, "with_primitive_part": with_gp,
            "max_log2_gprim_minus_half_A": round(best[0], 3), "attained_by": best[1]}


def main(argv):
    result = {"schema": 1}
    result["reduction_identity_pairs"] = check_reduction()
    trans = {}
    total_nodes = 0.0
    total_expected = 0.0
    for n in range(5, 12):
        for B in range(math.ceil(n * LOG2_3), int(2.3 * n) + 1):
            if (1 << B) <= 3 ** n:
                continue
            nodes, hits = transposition_search(n, B)
            if hits:
                raise SystemExit(f"N2 FAIL: transposition hit at n={n} B={B}: {hits[0]}")
            P = (1 << B) + 3 ** n
            trans[f"{n},{B}"] = {"sub_words": nodes, "uniform_expectation": round(2 * nodes / P, 4)}
            total_nodes += nodes
            total_expected += 2 * nodes / P
    result["transpositions"] = {"per_nB": trans, "total_sub_words": int(total_nodes),
                                "total_uniform_expectation": round(total_expected, 3), "hits": 0}
    one = {}
    total_c = 0
    total_e = 0.0
    for n in range(5, 10):
        for B in range(math.ceil(n * LOG2_3) - 2, int(2.3 * n) + 1):
            for j in (1, 2):
                conditions, hits = one_letter_search(n, B, j)
                if hits:
                    raise SystemExit(f"N3 FAIL: one-letter hit at n={n} B={B} j={j}: {hits[0]}")
                if conditions:
                    P = (1 << (B + j)) + 3 ** n
                    one[f"{n},{B},{j}"] = {"conditions": conditions, "uniform_expectation": round(conditions / P, 4)}
                    total_c += conditions
                    total_e += conditions / P
    result["one_letter"] = {"per_nBj": one, "total_conditions": total_c,
                            "total_uniform_expectation": round(total_e, 3), "hits": 0}
    result["census_e2"] = census_e2()
    text = json.dumps(result, indent=1, sort_keys=True) + "\n"
    if "--write-receipt" in argv:
        RECEIPT.write_text(text, encoding="utf-8")
        print("receipt written")
    elif not RECEIPT.exists() or RECEIPT.read_text(encoding="utf-8") != text:
        raise SystemExit("receipt mismatch")
    print(f"PASS N1: reduction identities on {result['reduction_identity_pairs']} pairs")
    print(f"PASS N2: transpositions, {result['transpositions']['total_sub_words']} sub-words, uniform expectation "
          f"{result['transpositions']['total_uniform_expectation']}, 0 hits")
    print(f"PASS N3: one letter, {total_c} conditions, uniform expectation {result['one_letter']['total_uniform_expectation']}, 0 hits")
    c = result["census_e2"]
    print(f"PASS N4: {c['e2_words']} census words with gcd(A,m)=2, max log2 g_prim - A/2 = {c['max_log2_gprim_minus_half_A']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
