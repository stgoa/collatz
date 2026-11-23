#!/usr/bin/env python3
"""Certificate for mismatch-chain-ridout-criterion.

Raw odd-only clock. For an actual cycle of 3x+d with states x_i, letters w_i (2^(w_i) x_(i+1) = 3 x_i + d) and a
shift H, write x'_i = x_(i+H), w'_i = w_(i+H). For positions i_0 <= i_r (n = i_r - i_0) and a run of a-1 matched
positions before i_0, the node's chain identity reads

    2^(w'_(i_0)) xi' - 2^(w_(i_0)) xi = 3^a G,
    3^(a+n) G = 2^(w'_(i_0)+sigma') U - 2^(w_(i_0)+sigma) zeta - d (2^(w'_(i_0)) C' - 2^(w_(i_0)) C).

Checks, in exact integer arithmetic:
V1  on a deterministic family of actual 3x+d cycles with distinct states (all words of length 2..6 over the
    letters 1..3 with positive denominator, and a fixed pseudo-random sample of longer words), for every shift,
    start, admissible run length and end: the divisibility by 3^a, the chain identity, the oddness of G/2^e at a
    mismatch, and, when every position strictly between i_0 and i_r has w' >= w, the intercept comparison
    C <= C' <= 2^(D') C and the two estimates of the node's section 3 (with d C in place of C);
V2  on actual 3x+d cycles with word A B A[p] B[q] and H = N: the two dictionaries of the node's section 4;
V3  receipt comparison.

Exit 1 on failure; --write-receipt regenerates check_chain_criterion.json. Standard library only; no floating
point; no assert statements (valid under python3 -O)."""
import json
import sys
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "check_chain_criterion.json"
failures = []


def fail(msg):
    failures.append(msg)
    if len(failures) <= 20:
        print("FAIL:", msg)


def need(cond, msg):
    if not cond:
        fail(msg)
    return cond


def intercept(word):
    n, c, pre = len(word), 0, 0
    for i, w in enumerate(word):
        c += 3 ** (n - 1 - i) * 2 ** pre
        pre += w
    return c


def cycle(word):
    """The actual 3x+d cycle with this valuation word, or None if D <= 0."""
    m, E = len(word), sum(word)
    D = 2 ** E - 3 ** m
    if D <= 0:
        return None
    C = intercept(word)
    g = gcd(C, D)
    d, cur, st = D // g, C // g, []
    for w in word:
        st.append(cur)
        num = 3 * cur + d
        if num % 2 ** w:
            return None
        cur = num >> w
    if cur != st[0]:
        return None
    return d, st


def check_cycle(w, d, x, stats):
    m = len(w)
    for H in range(1, m):
        wp = [w[(i + H) % m] for i in range(m)]
        xp = [x[(i + H) % m] for i in range(m)]
        for i0 in range(m):
            run = 0
            while run < m - 1 and w[(i0 - 1 - run) % m] == wp[(i0 - 1 - run) % m]:
                run += 1
            xi, xip = x[(i0 + 1) % m], xp[(i0 + 1) % m]
            base = 2 ** wp[i0] * xip - 2 ** w[i0] * xi
            for a in range(1, run + 2):
                if not need(base % 3 ** a == 0, f"V1 divisibility {w} H={H} i0={i0} a={a}"):
                    continue
                G = base // 3 ** a
                mism = w[i0] != wp[i0]
                if mism:
                    e = min(w[i0], wp[i0])
                    need(G % 2 ** e == 0 and (G >> e) % 2 == 1, f"V1 odd quotient {w} H={H} i0={i0} a={a}")
                for n in range(0, m - a + 1):
                    lw = [w[(i0 + 1 + k) % m] for k in range(n)]
                    hw = [wp[(i0 + 1 + k) % m] for k in range(n)]
                    C, Cp = (intercept(lw), intercept(hw)) if n else (0, 0)
                    s, sp = sum(lw), sum(hw)
                    zeta, U = x[(i0 + 1 + n) % m], xp[(i0 + 1 + n) % m]
                    need(2 ** s * zeta == 3 ** n * xi + d * C and 2 ** sp * U == 3 ** n * xip + d * Cp,
                         f"V1 track equations {w} H={H} i0={i0} n={n}")
                    need(3 ** (a + n) * G == 2 ** (wp[i0] + sp) * U - 2 ** (w[i0] + s) * zeta
                         - d * (2 ** wp[i0] * Cp - 2 ** w[i0] * C), f"V1 chain identity {w} H={H} i0={i0} a={a} n={n}")
                    stats["identities"] += 1
                    if not mism:
                        continue
                    inner = [hw[k] - lw[k] for k in range(n - 1)] if n >= 1 else []
                    if any(v < 0 for v in inner):
                        continue
                    Dp = sum(inner)
                    need(C <= Cp <= 2 ** Dp * C, f"V1 intercept comparison {w} H={H} i0={i0} n={n}")
                    e = min(w[i0], wp[i0])
                    delta = abs(wp[i0] - w[i0])
                    theta = (2 ** (w[i0] - e + s) * zeta + d * (2 ** (wp[i0] - e) * Cp - 2 ** (w[i0] - e) * C))
                    c = wp[i0] - e + sp
                    need(2 ** c * U - 3 ** (a + n) * (G >> e) == theta, f"V1 reduced identity {w} H={H} i0={i0}")
                    if wp[i0] > w[i0]:
                        stats["pattern_i"] += 1
                        # Theta < 2^sigma zeta (1 + 2^(delta + D')), and 2^sigma zeta = 3^n xi + d C
                        need(0 < theta < 2 ** s * zeta * (1 + 2 ** (delta + Dp)), f"V1 pattern (i) {w} H={H} i0={i0}")
                    elif n >= 1:
                        stats["pattern_ii"] += 1
                        # Theta = 2^delta 3^n xi + d C' <= 2^delta 3^n xi + 2^(D') d C
                        need(theta == 2 ** delta * 3 ** n * xi + d * Cp
                             and 0 < theta <= 2 ** delta * 3 ** n * xi + 2 ** Dp * d * C,
                             f"V1 pattern (ii) {w} H={H} i0={i0}")
    stats["cycles"] += 1


def words(length, max_letter):
    out = [[]]
    for _ in range(length):
        out = [u + [l] for u in out for l in range(1, max_letter + 1)]
    return out


class Lcg:
    def __init__(self, seed):
        self.s = seed

    def below(self, n):
        self.s = (6364136223846793005 * self.s + 1442695040888963407) % 2 ** 64
        return (self.s >> 33) % n


def v1():
    stats = {"cycles": 0, "identities": 0, "pattern_i": 0, "pattern_ii": 0, "skipped_words": 0}
    for length in range(2, 7):
        for w in words(length, 3):
            r = cycle(w)
            if r is None or len(set(r[1])) < length:
                stats["skipped_words"] += 1
                continue
            check_cycle(w, r[0], r[1], stats)
    rng = Lcg(20261123)
    letters = [1, 1, 1, 2, 2, 3, 4, 6]
    for _ in range(1500):
        w = [letters[rng.below(8)] for _ in range(7 + rng.below(5))]
        r = cycle(w)
        if r is None or len(set(r[1])) < len(w):
            stats["skipped_words"] += 1
            continue
        check_cycle(w, r[0], r[1], stats)
    print(f"V1: chain identity checked on {stats['identities']} configurations of {stats['cycles']} actual 3x+d "
          f"cycles (pattern (i): {stats['pattern_i']}, pattern (ii): {stats['pattern_ii']})")
    return stats


def v2():
    count = 0
    blocks = [u for length in (1, 2, 3) for u in words(length, 3)]
    for A in blocks:
        for B in blocks:
            for p in range(1, 4):
                for q in range(1, 4):
                    a, b = len(A), len(B)
                    N = a + b
                    W = A + B + A[:-1] + [A[-1] + p] + B[:-1] + [B[-1] + q]
                    r = cycle(W)
                    if r is None:
                        continue
                    d, st = r
                    x, z, y, t = st[0], st[a], st[N], st[N + a]
                    sA, sB = sum(A), sum(B)
                    CA, CB = intercept(A), intercept(B)
                    h, j = (y - x) // 2 ** sA, (z - t) // 2 ** sB
                    # Case I dictionary: i_0 = a-1, i_r = N-1, H = N
                    need(2 ** (sB + p + q) * x - 3 ** N * h == 2 ** sB * y + (2 ** p - 1) * d * CB,
                         f"V2 case I {A} {B} {p} {q}")
                    need(2 ** p * t - z == 3 ** a * h, f"V2 case I quotient {A} {B} {p} {q}")
                    # Case II dictionary: i_0 = 2N-1, i_r = 2N-1+a, H = N
                    need(2 ** (sA + p) * t - 3 ** N * j == 3 ** a * 2 ** q * x + d * CA,
                         f"V2 case II {A} {B} {p} {q}")
                    need(y - 2 ** q * x == 3 ** b * j, f"V2 case II quotient {A} {B} {p} {q}")
                    count += 1
    print(f"V2: both half-period dictionaries checked on {count} actual 3x+d cycles with word A B A[p] B[q]")
    return {"cycles": count}


def main():
    write = "--write-receipt" in sys.argv
    summary = {"V1": v1(), "V2": v2()}
    if write:
        RECEIPT.write_text(json.dumps(summary, indent=1, sort_keys=True) + "\n")
        print("receipt written")
    elif not RECEIPT.exists():
        fail("V3 receipt missing")
    elif json.loads(RECEIPT.read_text()) != summary:
        fail("V3 summary differs from the receipt")
    if failures:
        print(f"{len(failures)} failure(s)")
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()
