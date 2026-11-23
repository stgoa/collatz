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
    start, admissible run length a-1 and every end with n <= m: the divisibility by 3^a, the chain identity,
    and at a mismatched start the oddness of g = G/2^e, the reduced identity 2^c U - 3^(a+n) g = Theta and the
    closed form Theta = 2^(w-e) 3^n xi + 2^(w'-e) d C' > 0; when every position strictly between i_0 and i_r has
    w' >= w, the intercept comparison C <= C' <= 2^(D') C and the two estimates of the node's section 3 (with
    d C in place of C);
V2  on actual 3x+d cycles with word A B A[p] B[q] and H = N: the two configurations of the node's section 4
    are recomputed from the general definitions and compared with the quantities of the approximation law;
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


def configuration(w, x, d, H, i0, a, n):
    """The quantities of the node for the shift H, start i0, run length a-1 and end i0+n (positions mod m)."""
    m = len(w)
    wi, wpi = w[i0 % m], w[(i0 + H) % m]
    xi, xip = x[(i0 + 1) % m], x[(i0 + 1 + H) % m]
    base = 2 ** wpi * xip - 2 ** wi * xi
    lw = [w[(i0 + 1 + k) % m] for k in range(n)]
    hw = [w[(i0 + 1 + k + H) % m] for k in range(n)]
    C, Cp = (intercept(lw), intercept(hw)) if n else (0, 0)
    out = {"wi": wi, "wpi": wpi, "xi": xi, "xip": xip, "base": base, "lw": lw, "hw": hw, "C": C, "Cp": Cp,
           "s": sum(lw), "sp": sum(hw), "zeta": x[(i0 + 1 + n) % m], "U": x[(i0 + 1 + n + H) % m]}
    if base % 3 ** a == 0:
        G = base // 3 ** a
        out["G"] = G
        if wi != wpi:
            e = min(wi, wpi)
            out["e"] = e
            out["g_ok"] = G % 2 ** e == 0 and (G >> e) % 2 == 1
            out["g"] = G >> e
            out["c"] = wpi - e + out["sp"]
            out["theta"] = 2 ** (wi - e + out["s"]) * out["zeta"] + d * (2 ** (wpi - e) * Cp - 2 ** (wi - e) * C)
    return out


def check_cycle(w, d, x, stats):
    m = len(w)
    for H in range(1, m):
        for i0 in range(m):
            run = 0
            while run < m - 1 and w[(i0 - 1 - run) % m] == w[(i0 - 1 - run + H) % m]:
                run += 1
            for a in range(1, run + 2):
                for n in range(0, m + 1):
                    q = configuration(w, x, d, H, i0, a, n)
                    tag = f"{w} H={H} i0={i0} a={a} n={n}"
                    if not need("G" in q, f"V1 divisibility {tag}"):
                        continue
                    xi, xip, zeta, U, C, Cp, s, sp = (q[k] for k in ("xi", "xip", "zeta", "U", "C", "Cp", "s", "sp"))
                    need(2 ** s * zeta == 3 ** n * xi + d * C and 2 ** sp * U == 3 ** n * xip + d * Cp,
                         f"V1 track equations {tag}")
                    need(3 ** (a + n) * q["G"] == 2 ** (q["wpi"] + sp) * U - 2 ** (q["wi"] + s) * zeta
                         - d * (2 ** q["wpi"] * Cp - 2 ** q["wi"] * C), f"V1 chain identity {tag}")
                    stats["identities"] += 1
                    if q["wi"] == q["wpi"]:
                        continue
                    e, theta, c = q["e"], q["theta"], q["c"]
                    need(q["g_ok"], f"V1 odd quotient {tag}")
                    need(2 ** c * U - 3 ** (a + n) * q["g"] == theta, f"V1 reduced identity {tag}")
                    need(theta == 2 ** (q["wi"] - e) * 3 ** n * xi + 2 ** (q["wpi"] - e) * d * Cp and theta > 0,
                         f"V1 closed form of Theta {tag}")
                    stats["mismatched_starts"] += 1
                    inner = [q["hw"][k] - q["lw"][k] for k in range(n - 1)] if n >= 1 else []
                    if any(v < 0 for v in inner):
                        continue
                    Dp = sum(inner)
                    need(C <= Cp <= 2 ** Dp * C, f"V1 intercept comparison {tag}")
                    delta = abs(q["wpi"] - q["wi"])
                    if q["wpi"] > q["wi"]:
                        stats["pattern_i"] += 1
                        # Theta = 3^n xi + 2^delta d C' <= 3^n xi + 2^(delta + D') d C
                        need(theta == 3 ** n * xi + 2 ** delta * d * Cp
                             and theta <= 3 ** n * xi + 2 ** (delta + Dp) * d * C, f"V1 pattern (i) {tag}")
                    elif n >= 1:
                        stats["pattern_ii"] += 1
                        # Theta = 2^delta 3^n xi + d C' <= 2^delta 3^n xi + 2^(D') d C
                        need(theta == 2 ** delta * 3 ** n * xi + d * Cp
                             and theta <= 2 ** delta * 3 ** n * xi + 2 ** Dp * d * C, f"V1 pattern (ii) {tag}")
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
    stats = {"cycles": 0, "identities": 0, "mismatched_starts": 0, "pattern_i": 0, "pattern_ii": 0,
             "skipped_words": 0}
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
          f"cycles ({stats['mismatched_starts']} with a mismatched start; pattern (i): {stats['pattern_i']}, "
          f"pattern (ii): {stats['pattern_ii']})")
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
                    tag = f"{A} {B} {p} {q}"
                    # Case I: H = N, i_0 = a-1, run length a-1, end N-1 (n = b); pattern (i)
                    c1 = configuration(W, st, d, N, a - 1, a, b)
                    need(c1.get("g") == h and c1.get("c") == sB + p + q and c1["U"] == x and c1["xi"] == z
                         and c1["xip"] == t and c1["zeta"] == y
                         and c1.get("theta") == 2 ** sB * y + (2 ** p - 1) * d * CB, f"V2 case I {tag}")
                    # Case II: H = N, i_0 = 2N-1, run length b-1, end 2N-1+a (n = a); pattern (ii)
                    c2 = configuration(W, st, d, N, 2 * N - 1, b, a)
                    need(c2.get("g") == j and c2.get("c") == sA + p and c2["U"] == t and c2["xi"] == x
                         and c2["xip"] == y and c2["zeta"] == z
                         and c2.get("theta") == 3 ** a * 2 ** q * x + d * CA, f"V2 case II {tag}")
                    count += 1
    print(f"V2: both half-period configurations recomputed on {count} actual 3x+d cycles with word A B A[p] B[q]")
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
