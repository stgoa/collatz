"""Recompute the inverse-ancestry identities, counts and witnesses of inverse_ancestry_audit.json.

Written at the B10-residual-R25-R39 migration; the legacy scripts in this folder
load ../complementary_bridge/run_bridge.py (and through it the R25 normal form)
by their pre-migration paths and no longer run.

Everything is rebuilt here from first principles (own odd-only Syracuse step S,
own elementary normal form nu, own R26 return f, own residual profile R_N) and
compared with the legacy receipt and stored currents in this folder:

1. For every canonical q < 16384 (the receipt's 4096 cases): eta(q) is canonical,
   3 does not divide eta(q)+1, eta is idempotent, the chain q_j = 2^j(q+1)/3^j - 1
   has S(q_j) = q_(j-1) with valuation 1, and the only canonical predecessor
   smaller than q among the six ray minima and L(q) = (2q-1)/3 is L(q), present
   exactly when q = 2 mod 3 (each ray minimum m is canonical with nu(S(m)) = q).
   Inverse depths 1..128 on the legacy test family.
2. For every complementary x < 16384 (2048 branches, 1364 with even d): even d
   gives depth 0; odd d satisfies h = v3(V) - 1 with V of formula (7), and
   h = min(b, e) whenever b != e.
3. The 32 members x = 19199 + 65536 j: q = (6561x+3745)/8192, p = (2187x-117)/4096,
   the words (1^7,2,6) and (1,2), S^9(x) = S^2(p), and old_target/target as stored.
4. For h = 2..7 and weights 1, 2: the family parameters a, d, k, the binary
   modulus bits K, the ray-witness root bit length and the weighted source count
   (own CRT count, with |count - 25N/(72 2^K)| <= 6); p = lambda x + beta exactly
   with -5/9 < beta < -7/192, q > x, the words of (17) and S^(a+b)(x) = S^(h+1)(p).
5. Old (R26) and extended weighted masses and the extra roots at the eight
   cutoffs N = 8 .. 65536, by explicit enumeration of R_N.
6. The two stored new-root currents (84735 and the h = 2 weight-2 witness):
   divergence equal to weight * delta_root under the own step, positive rows,
   and the stored N, target and old_target values.
7. The 33 nongreedy counterfamily cases u = 27 + 131072 j, q = 91 + 419904 j.

It does not rebuild the full-profile conversions from supplied U_N currents or
the bridge-current hashes (legacy checker, evidence only).
"""
import csv
import json
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
FAILURES = []


def need(condition, message):
    if not condition:
        FAILURES.append(message)


def v2(n):
    return (n & -n).bit_length() - 1


def v3(n):
    e = 0
    while n % 3 == 0:
        n //= 3
        e += 1
    return e


def S(x):
    if x == 1:
        return 1
    z = 3 * x + 1
    return z >> v2(z)


def letter(x):
    return v2(3 * x + 1)


def selected(x):
    if x % 4 != 3:
        return False
    a = v2(x + 1)
    t = (x + 1) >> a
    return t % 4 == (1 if a % 2 == 0 else 3)


def canonical(x):
    return x % 8 == 1 or (x % 4 == 3 and not selected(x))


def normalize(x):
    """Return (nu(x), F-exponent) for the elementary bridge class of x."""
    k = 0
    while x % 8 == 5:
        x = (x - 1) // 4
        k += 1
    if selected(x):
        x = (x - 1) // 2
    return x, k


def eta(q):
    h = v3(q + 1)
    return 2**h * ((q + 1) // 3**h) - 1, h


def r26(x):
    """Complementary parameters and the R26 raw return f(x)."""
    a = v2(x + 1)
    t = (x + 1) >> a
    v = 3**(a - 1) * t - 1
    d = v2(v)
    w = v >> d
    f = 3**(d // 2) * w if d % 2 else 2 * 3**(d // 2) * w + 1
    return a, t, d, w, f


def word(x, n):
    out = []
    for _ in range(n):
        out.append(letter(x))
        x = S(x)
    return out, x


def weight(N, x):
    if x % 12 == 3 and N < x < F(3 * N, 2):
        return 1
    if x % 12 == 7 and F(9 * N, 8) < x < F(3 * N, 2):
        return 1
    if x % 36 in (7, 19) and N < x < F(9 * N, 8):
        return 2
    return 0


def strict_count(low, high, r, m):
    """Integers strictly between rationals low < high that are r mod m."""
    if high <= low:
        return 0
    top = -((-(high - r)) // m)          # ceil((high-r)/m)
    bottom = (low - r) // m              # floor((low-r)/m)
    return max(0, int(top) - int(bottom) - 1)


def divergence(current):
    div = {}
    for y, c in current.items():
        div[y] = div.get(y, 0) + c
        z = S(y)
        div[z] = div.get(z, 0) - c
    div.pop(1, None)
    return {y: c for y, c in div.items() if c}


def main():
    receipt = json.loads((HERE / "inverse_ancestry_audit.json").read_text())

    # 1. canonical targets and the decreasing chain
    cases = 0
    for q in range(1, 16384, 2):
        if not canonical(q):
            continue
        cases += 1
        p, h = eta(q)
        need(canonical(p) and (p + 1) % 3 and eta(p)[0] == p, f"eta at {q}")
        y = q
        for j in range(1, h + 1):
            z = 2**j * ((q + 1) // 3**j) - 1
            need(z < y and canonical(z) and S(z) == y and letter(z) == 1, f"chain {q},{j}")
            y = z
        need(y == p, f"chain end {q}")
        numerators = {0: (8 * q + 3, 16 * q + 3), 1: (4 * q - 1, 32 * q + 19),
                      2: (64 * q + 19, 128 * q + 83)}[q % 3]
        for n in numerators:
            m = n // 3
            need(n % 3 == 0 and canonical(m) and normalize(S(m))[0] == q, f"ray minimum at {q}")
            need(m > q or (q == 1 and m == 1), f"ray minimum above {q}")
        if q % 3 == 2:
            L = (2 * q - 1) // 3
            need(S(L) == q and letter(L) == 1 and canonical(L) and L < q, f"L(q) at {q}")
    need(cases == receipt["canonical_targets"]["cases"], "canonical case count")
    need(receipt["long_inverse_depths"] == [1, 128], "depth range")
    for h in range(1, 129):
        t = 1 if h % 2 == 0 else 7
        p, q = 2**(h + 1) * t - 1, 2 * 3**h * t - 1
        need(canonical(q) and eta(q) == (p, h), f"long depth {h}")

    # 2. return branches
    branches = evens = 0
    for x in range(3, 16384, 4):
        if selected(x):
            continue
        a, t, d, w, f = r26(x)
        q, k = normalize(f)
        h = v3(q + 1)
        branches += 1
        if d % 2 == 0:
            evens += 1
            need(k == 0 and h == 0, f"even branch {x}")
        else:
            b = d // 2
            V = 3**(a + b) * t - 3**(b + 1) + 2**d * (2**(2 * k + 1) + 1)
            need(h == v3(V) - 1, f"formula (7) at {x}")
            e = v3(2 * k + 1)
            if e != b:
                need(h == min(e, b), f"formula (8) at {x}")
    need(branches == receipt["branch_cases"] and evens == receipt["even_branch_cases"], "branch counts")

    # 3. the small cylinder
    small = receipt["small_cylinder"]
    need(len(small) == 32, "small cylinder size")
    for j, row in enumerate(small):
        x = 19199 + 65536 * j
        a, t, d, w, f = r26(x)
        q, k = normalize(f)
        p, h = eta(q)
        need((a, d, k, h) == (8, 3, 1, 1) and f == 4 * q + 1, f"cylinder parameters {x}")
        need(8192 * q == 6561 * x + 3745 and 4096 * p == 2187 * x - 117, f"numerators {x}")
        lw, end_x = word(x, 9)
        rw, end_p = word(p, 2)
        need(lw == [1] * 7 + [2, 6] and rw == [1, 2] and end_x == end_p, f"merger {x}")
        need((row["root"], row["target"], row["old_target"]) == (x, p, q), f"stored row {x}")

    # 4. large-return families and ray witnesses
    fam_rows = receipt["large_return_families"]
    need(len(fam_rows) == 12, "family row count")
    for row in fam_rows:
        h, wt = row["h"], row["weight"]
        k, b, d = (3**h - 1) // 2, h + 1, 2 * h + 3
        M = h + 2 + 3**h
        a = next(a for a in range(2, 3 * M) if F(4, 9) <= F(3**a, 2**(a + M)) < F(2, 3))
        lam = F(3**a, 2**(a + M))
        bits_t = d + 2 * k + 3
        rt = ((3**(b + 1) + 2**d * (4**(k + 1) - 1)) * pow(3**(a + b), -1, 2**bits_t)) % 2**bits_t
        K = a + bits_t
        P, r = 2**K, 2**a * rt - 1
        need((row["a"], row["d"], row["k"], row["binary_bits"]) == (a, d, k, K), f"family h={h}")
        N = 12 * P * (8 if wt == 2 else 1)
        odd, rowres = (9, 7) if wt == 2 else (3, 3)
        comb = (r + P * ((rowres - r) * pow(P, -1, odd) % odd)) % (P * odd)
        x = comb + P * odd * ((N - comb) // (P * odd) + 1)
        need(weight(N, x) == wt and x.bit_length() == row["root_bits"], f"witness h={h} w={wt}")
        count = 0
        for wgt, lo, hi, rr, od in ((1, F(N), F(3 * N, 2), 3, 3), (1, F(9 * N, 8), F(3 * N, 2), 7, 3),
                                    (2, F(N), F(9 * N, 8), 7, 9), (2, F(N), F(9 * N, 8), 19, 9)):
            c = (r + P * ((rr - r) * pow(P, -1, od) % od)) % (P * od)
            count += wgt * strict_count(lo, hi, c, P * od)
        need(count == row["source_count"] and abs(count - F(25 * N, 72 * P)) <= 6, f"source count h={h} w={wt}")
        ax, tx, dx, wx, f = r26(x)
        q, kx = normalize(f)
        p, hx = eta(q)
        c0 = F(1, 3) - F(3**(h + 1), 2**d)
        beta = lam + F(2, 3)**h * (F(2, 3) + c0 / 4**k) - 1
        need((ax, dx, kx, hx) == (a, d, k, h), f"witness parameters h={h}")
        need(p == lam * x + beta and -F(5, 9) < beta < -F(7, 192), f"affine lower seed h={h}")
        need(p < N < x < q, f"order h={h}")
        need(q == F(3, 2)**h * lam * x + F(3, 2)**h * lam - F(1, 3) + c0 / 4**k, f"old return h={h}")
        lw, end_x = word(x, a + b)
        rw, end_p = word(p, h + 1)
        need(lw == [1] * (a - 1) + [2] * b + [2 * k + 4] and rw == [1] * h + [2] and end_x == end_p,
             f"merger (17) h={h}")
        need(sum(lw) + 1 == K, f"cylinder bits h={h}")

    # 5. exact profile counts
    stored = {row["N"]: row for row in receipt["exact_profile_counts"]}
    need(sorted(stored) == [8, 32, 96, 384, 1536, 6144, 24576, 65536], "profile cutoffs")
    for N, row in stored.items():
        old = new = 0
        extra = []
        for x in range(N + 1, (3 * N) // 2, 2):
            c = weight(N, x)
            if not c or selected(x):
                continue
            q = normalize(r26(x)[4])[0]
            p = eta(q)[0]
            if q < N:
                old += c
            if p < N:
                new += c
                if q >= N:
                    extra.append([x, c])
        need((old, new, extra) == (row["old_mass"], row["new_mass"], row["extra_roots"]), f"profile N={N}")

    # 6. stored currents of the two new roots
    for row in receipt["actual_new_root_conversions"]:
        x, N, wt = row["root"], row["N"], row["weight"]
        q = normalize(r26(x)[4])[0]
        p = eta(q)[0]
        need(weight(N, x) == wt and (p, q) == (row["target"], row["old_target"]) and p < N < x < F(3 * N, 2) and q > N,
             f"new root {x}")
        name = "root84735_current.csv" if x == 84735 else "large_h2_weight2_current.csv"
        with (HERE / name).open(newline="") as handle:
            current = {int(r["state"]): int(r["current"]) for r in csv.DictReader(handle)}
        need(len(current) == row["output_rows"] and all(c > 0 for c in current.values()), f"rows {name}")
        need(divergence(current) == {x: wt}, f"divergence {name}")

    # 7. nongreedy counterfamily
    need(receipt["nongreedy_ancestor_counterfamily_cases"] == 33, "counterfamily count")
    for j in range(33):
        u, q = 27 + 131072 * j, 91 + 419904 * j
        y, ok = u, canonical(u)
        for _ in range(8):
            y = S(y)
            ok = ok and canonical(y)
        need(ok and y == q and eta(q)[0] == q > u, f"counterfamily {j}")
    need(eta(normalize(S(7))[0])[0] == 7 and eta(normalize(S(17))[0])[0] == 1, "eta T examples")

    if FAILURES:
        print(f"FAIL: {len(FAILURES)} checks failed; first: {FAILURES[0]}")
        sys.exit(1)
    print(f"PASS: {cases} canonical targets, {branches} return branches, 32 cylinder members, "
          f"{len(fam_rows)} large-return witnesses, {len(stored)} profile counts, two stored currents")


if __name__ == "__main__":
    main()
