#!/usr/bin/env python3
"""Certificate for rho-four-census-letters-three.

Complete enumeration of the primitive positive words w with letters <= 3, 9 <= m <= MMAX, D = 2^A - 3^m > 0 and
rotation distance rho(w) <= 4, through the track structure of a rotation with at most four mismatches: for a shift h
with g = gcd(h, m), the letters along each of the g track-cycles are piecewise constant with c_k change points
(mismatches), sum c_k <= 4 and no c_k = 1.  For each word (one representative per rotation class): A, rho (exact),
G = gcd(C_w, D), e = gcd(A, m), g_prim = gcd(G, Phi_e(2^(A/e), 3^(m/e))), whether 2^A < 2 * 3^m (near-critical),
whether G^2 >= 2^A (a violation of the half bound) and whether g_prim^2 >= 2^A.
Q1  the enumeration for 9 <= m <= MMAX (= 16 in the certificate) with the per-m summary;
Q2  the eight violating words found by the same enumeration up to m = 20 (the m = 18, 20 part is exploration):
    each is primitive, has D > 0, rho = 4 with the listed witnesses, the listed G, e, g_prim, and is not near-critical;
Q3  receipt comparison.  Exit 1 on failure; --write-receipt regenerates rho4_census.json.  Standard library only."""
import itertools
import json
import math
import sys
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "rho4_census.json"
MMAX, LMAX = 16, 3
VIOLATIONS = [
    ([1, 1, 2, 2, 3, 1, 2, 2, 3, 3, 2, 2], 6475, 12, 1, [4, 8]),
    ([1, 1, 2, 2, 1, 3, 1, 2, 2, 2, 3, 3], 5921, 1, 5921, [6]),
    ([1, 1, 2, 1, 1, 3, 1, 2, 1, 3, 2, 3, 1, 3, 1, 2], 19415, 4, 1765, [8]),
    ([1, 1, 2, 2, 2, 1, 2, 3, 1, 2, 2, 2, 2, 1, 2, 2], 16591, 4, 353, [8]),
    ([1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2], 91595, 6, 7, [3, 15]),
    ([1, 2, 2, 3, 1, 3, 1, 3, 1, 3, 2, 2, 1, 3, 1, 3, 1, 3], 1697227, 18, 1, [8, 10]),
    ([1, 2, 2, 2, 2, 2, 2, 3, 1, 3, 2, 2, 2, 2, 2, 2, 1, 3], 3151993, 18, 1, [8, 10]),
    ([1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 2, 1, 1, 3, 2, 1, 1, 3, 2], 1257863, 1, 1257863, [4, 16]),
]
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


def rho(w):
    return min(mismatches(w, h) for h in range(1, len(w)))


def canon(w):
    m = len(w)
    return min(tuple(w[i:] + w[:i]) for i in range(m))


def is_primitive(w):
    m = len(w)
    return all(any(w[i] != w[(i + p) % m] for i in range(m)) for p in range(1, m) if m % p == 0)


def mobius(n):
    res, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            res = -res
        p += 1
    return -res if n > 1 else res


def cyclotomic(e, x, y):
    num = den = 1
    for d in range(1, e + 1):
        if e % d == 0:
            v = x ** d - y ** d
            mu = mobius(e // d)
            if mu == 1:
                num *= v
            elif mu == -1:
                den *= v
    if num % den:
        fail("cyclotomic value not an integer")
    return num // den


def arc_colourings(c, letters):
    if c == 0:
        for a in letters:
            yield (a,)
        return
    for seq in itertools.product(letters, repeat=c):
        if all(seq[i] != seq[(i + 1) % c] for i in range(c)):
            yield seq


def words_for_shift(m, h, letters, smax=4):
    g = gcd(h, m)
    L = m // g
    cycles = [[(k + j * h) % m for j in range(L)] for k in range(g)]

    def dists(k, remaining):
        if k == g:
            yield []
            return
        for c in [0] + list(range(2, remaining + 1)):
            if c > L:
                continue
            for rest in dists(k + 1, remaining - c):
                yield [c] + rest

    for dist in dists(0, smax):
        if sum(dist) == 0:
            continue
        per_cycle = []
        for c in dist:
            opts = []
            if c == 0:
                for a in letters:
                    opts.append(((), (a,)))
            else:
                for pos in itertools.combinations(range(L), c):
                    for cols in arc_colourings(c, letters):
                        opts.append((pos, cols))
            per_cycle.append(opts)
        for choice in itertools.product(*per_cycle):
            w = [0] * m
            for k, (pos, cols) in enumerate(choice):
                cyc = cycles[k]
                if not pos:
                    for i in cyc:
                        w[i] = cols[0]
                else:
                    c = len(pos)
                    for a in range(c):
                        start, end = pos[a] + 1, pos[(a + 1) % c]
                        j = start % L
                        while True:
                            w[cyc[j]] = cols[a]
                            if j == end % L:
                                break
                            j = (j + 1) % L
            yield tuple(w)


def analyse(cw):
    m, A = len(cw), sum(cw)
    D = (1 << A) - 3 ** m
    C = intercept(cw)
    G = gcd(C, D)
    e = gcd(A, m)
    gp = gcd(G, cyclotomic(e, 1 << (A // e), 3 ** (m // e)))
    return dict(A=A, rho=rho(cw), G=G, e=e, gprim=gp, near=(1 << A) < 2 * 3 ** m,
                plain=G * G >= (1 << A), prim=gp * gp >= (1 << A))


def q1():
    letters = list(range(1, LMAX + 1))
    summary = {}
    for m in range(9, MMAX + 1):
        seen, rows = set(), []
        for h in range(1, m):
            for w in words_for_shift(m, h, letters):
                cw = canon(list(w))
                if cw in seen:
                    continue
                seen.add(cw)
                if (1 << sum(cw)) - 3 ** m <= 0 or not is_primitive(cw):
                    continue
                r = analyse(cw)
                if r["rho"] > 4:
                    fail(f"Q1 construction gave rho > 4 at m={m}")
                rows.append((cw, r))
        plain = [(cw, r) for cw, r in rows if r["plain"]]
        summary[str(m)] = dict(
            words=len(rows), near_critical=sum(1 for _, r in rows if r["near"]),
            by_rho={str(k): sum(1 for _, r in rows if r["rho"] == k) for k in (2, 3, 4)},
            plain_violations=len(plain), near_critical_plain_violations=sum(1 for _, r in plain if r["near"]),
            primitive_violations=sum(1 for _, r in rows if r["prim"]),
            max_log2_gprim_minus_half_A=round(max(math.log2(r["gprim"]) - r["A"] / 2 for _, r in rows), 3),
            max_log2_G_minus_half_A_near_critical=round(max((math.log2(r["G"]) - r["A"] / 2 for _, r in rows if r["near"]), default=-99), 3),
            violations=[dict(w=list(cw), A=r["A"], G=r["G"], e=r["e"], gprim=r["gprim"]) for cw, r in plain])
    return summary


def q2():
    out = []
    for w, G, e, gp, hs in VIOLATIONS:
        m, A = len(w), sum(w)
        D = (1 << A) - 3 ** m
        r = analyse(tuple(w))
        wit = [h for h in range(1, m) if mismatches(w, h) <= 4]
        ok = (D > 0 and is_primitive(w) and r["rho"] == 4 and wit == hs and r["G"] == G and r["e"] == e
              and r["gprim"] == gp and r["plain"] and not r["near"])
        if not ok:
            fail(f"Q2 violation word {w}: {r}, witnesses {wit}")
        out.append(dict(w=w, m=m, A=A, G=G, q=D // G, e=e, gprim=gp, witnesses=hs, gcd_h_m=[gcd(h, m) for h in hs],
                        log2_G_minus_half_A=round(math.log2(G) - A / 2, 3), ratio_2A_over_3m=round(2 ** A / 3 ** m, 3),
                        primitive_violation=r["prim"]))
    return out


def main():
    write = "--write-receipt" in sys.argv
    summary = {"Q1": q1(), "Q2": q2()}
    if write:
        RECEIPT.write_text(json.dumps(summary, indent=1) + "\n")
        print("receipt written")
    elif not RECEIPT.exists():
        fail("Q3 receipt missing")
    elif json.loads(RECEIPT.read_text()) != summary:
        fail("Q3 summary differs from the receipt")
    tot = sum(v["words"] for v in summary["Q1"].values())
    near = sum(v["near_critical"] for v in summary["Q1"].values())
    pv = sum(v["plain_violations"] for v in summary["Q1"].values())
    npv = sum(v["near_critical_plain_violations"] for v in summary["Q1"].values())
    print(f"Q1 m=9..{MMAX}: {tot} words, {near} near-critical, {pv} plain violations ({npv} near-critical), "
          f"{sum(v['primitive_violations'] for v in summary['Q1'].values())} primitive violations")
    print(f"Q2 {len(summary['Q2'])} violating words verified")
    if failures:
        print(f"{len(failures)} failure(s)")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
