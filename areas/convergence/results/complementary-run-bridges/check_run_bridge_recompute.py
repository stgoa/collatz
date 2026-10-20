"""Recompute the run-bridge branches, normalized counts and series enclosures of run_bridge_audit.json.

Written at the B10-residual-R25-R39 migration; the legacy scripts in this folder
load ../residual_return/halving_return.py and ../bridge_normal_form/normal_form.py
(and the side-lane probes load affine_controls, fibre_count_check and
residual_vs_induction) by their pre-migration paths and no longer run.

Everything is rebuilt here from the statements, with this script's own odd-only
Syracuse step (S(1) = 1), selected-climber test, complementary parameters
(a, t, d, w), return f(x), and normal form nu (strip (x-1)/4 while x = 5 mod 8,
then halve once if selected). It checks, against the legacy receipt in this folder:

1. every complementary x = 3 mod 4 below 32768 (the receipt's 4096 seeds): the
   exact first run S^a(x) = 3 2^(d-1) w + 1, the odd-d coalescence
   S^(a+(d-3)/2)(x) = 4z+1 and S^(a+(d-1)/2)(x) = S(z), the even-d return
   S^(a+d/2-1)(x) = r with r = 3 mod 4, the cylinder (10), and nu(f(x)) <= f(x);
2. the parameter domain 2 <= a, d <= 32 with offsets 0, 1, 7 (2883 cases): the
   cylinder representative has labels (a, d), the shrinking test (6) is
   equivalent to f(x) < x, and every odd-d branch with a <= 5 shrinks;
3. all 68 profile cases: from the weighted R_N classes of R17, the prior
   complementary mass, the raw removed mass (f(x) < N), the normalized removed
   mass (nu(f(x)) < N), the remainder and the number of weight-2 normalized
   roots; and the error bound (14) against the alpha enclosure;
4. the exact rational enclosures of alpha and beta at K = 64, of 25/576 - beta,
   and the nested beta enclosures at K = 4, 8, 16, 32, 64 (formulas (12), (16));
5. the six unbounded canonical returns (a = 7 mod 16), the label cycle
   27 -> 31 -> 91, and the coefficient-2 example at N = 168 with the stored
   current outer_187_double_current.csv (its divergence is 2 delta_187, its
   row count and SHA-256 match the receipt).

It does not rebuild the seven supplied-input current conversions or the packet
upgrades at N = 96, 768 (legacy checker, evidence only). Standard library;
deterministic; writes nothing.
"""
import csv
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent


def v2(n):
    return (n & -n).bit_length() - 1


def step(x):
    if x == 1:
        return 1
    z = 3 * x + 1
    return z >> v2(z)


def selected(x):
    if x % 4 != 3:
        return False
    a = v2(x + 1)
    return ((x + 1) >> a) % 4 == pow(3, a, 4)


def nu(x):
    while x % 8 == 5:
        x = (x - 1) // 4
    return (x - 1) // 2 if selected(x) else x


def params(x):
    a = v2(x + 1)
    t = (x + 1) >> a
    z = 3 ** (a - 1) * t - 1
    d = v2(z)
    return a, t, d, z >> d


def ret(x):
    a, t, d, w = params(x)
    return 3 ** ((d - 1) // 2) * w if d % 2 else 2 * 3 ** (d // 2) * w + 1


def cylinder(a, d):
    m = 2 ** (d + 1)
    t = ((1 + 2 ** d) * pow(3 ** (a - 1), -1, m)) % m
    return 2 ** a * t - 1, 2 ** (a + d + 1)


def iterate(x, n):
    for _ in range(n):
        x = step(x)
    return x


def residual_roots(N):
    """R'_N candidates: the weighted R_N of R17, restricted to complementary roots."""
    roots = {}
    for x in range(N + 1, (3 * N) // 2 + 1, 2):
        if 2 * x >= 3 * N:
            continue
        if x % 12 == 3:
            w = 1
        elif x % 12 == 7 and 8 * x > 9 * N:
            w = 1
        elif x % 36 in (7, 19) and 8 * x < 9 * N:
            w = 2
        else:
            continue
        if not selected(x):
            roots[x] = w
    return roots


def g(h):
    return (F(7, 9) * max(F(0), min(F(9, 8), h) - 1)
            + F(2, 3) * max(F(0), min(F(3, 2), h) - F(9, 8)))


def slope(a, d):
    return F((1 if d % 2 else 2) * 3 ** (a - 1 + d // 2), 2 ** (a + d))


def enclosures(K):
    alpha = beta = F(0)
    for a in range(2, K - 1):
        for d in range(2, K - a + 1):
            L = slope(a, d)
            alpha += g(1 / L) / 2 ** (a + d + 1)
            if d % 2:
                k, h = 0, F(0)
                while F(4 ** k) / L < F(3, 2):
                    h += (g(F(4 ** k) / L) / 2 + g(F(2 * 4 ** k) / L) / 4) / 4 ** k
                    k += 1
                h += F(25, 72 * 4 ** k)
            else:
                h = (g(1 / L) + g(2 / L)) / 2
            beta += h / 2 ** (a + d + 1)
    tail = F(25 * (K - 1), 72 * 2 ** (K + 1))
    return (alpha, alpha + tail), (beta, beta + tail)


def main():
    receipt = json.loads((HERE / "run_bridge_audit.json").read_text())
    fails = []

    def need(ok, msg):
        if not ok:
            fails.append(msg)

    seeds = 0
    for x in range(3, 32768, 4):
        if selected(x):
            continue
        seeds += 1
        a, t, d, w = params(x)
        need(d >= 2 and w % 2 == 1, f"params {x}")
        need(iterate(x, a) == 3 * 2 ** (d - 1) * w + 1, f"first run {x}")
        f = ret(x)
        if d % 2:
            need(iterate(x, a + (d - 3) // 2) == 4 * f + 1, f"odd run {x}")
            need(iterate(x, a + (d - 1) // 2) == step(f), f"odd coalescence {x}")
        else:
            need(iterate(x, a + d // 2 - 1) == f and f % 4 == 3, f"even return {x}")
        r, p = cylinder(a, d)
        need(x % p == r, f"cylinder {x}")
        need(nu(f) <= f, f"normal form {x}")
    need(seeds == receipt["complementary_seeds_checked"], "seed count")
    need(receipt["complementary_seed_range"] == [3, 32767, 4], "seed range")

    cases = 0
    for a in range(2, 33):
        for d in range(2, 33):
            r, p = cylinder(a, d)
            for off in (0, 1, 7):
                x = r + p * off
                aa, t, dd, w = params(x)
                need((aa, dd) == (a, d) and not selected(x), f"labels {a},{d},{off}")
                C = 3 ** (d // 2)
                A = C * 3 ** (a - 1)
                left = (2 ** (a + d) - (A if d % 2 else 2 * A)) * t
                right = 2 ** d - C if d % 2 else 2 ** (d + 1) - 2 * C
                need((ret(x) < x) == (left > right), f"shrink test {a},{d},{off}")
                if d % 2 and a <= 5:
                    need(ret(x) < x, f"odd a<=5 shrink {a},{d},{off}")
                cases += 1
    need(cases == receipt["parameter_domain"]["cases"], "parameter case count")

    (al, ah), (bl, bh) = enclosures(64)
    need([str(al), str(ah)] == receipt["raw_leading_bounds"], "alpha enclosure")
    need([str(bl), str(bh)] == receipt["normalized_leading_bounds"], "beta enclosure")
    need([str(F(25, 576) - bh), str(F(25, 576) - bl)] == receipt["normalized_remaining_bounds"],
         "remaining enclosure")
    need(0 < al < ah < bl < bh < F(25, 576), "enclosure order")
    for row in receipt["nested_series_enclosures"]:
        if row["K"] == 64:
            lo, hi = bl, bh
        else:
            lo, hi = enclosures(row["K"])[1]
        need([str(lo), str(hi)] == [row["lower"], row["upper"]], f"nested K={row['K']}")

    for row in receipt["profile_cases"]:
        N = row["N"]
        roots = residual_roots(N)
        prior = sum(roots.values())
        raw = sum(c for x, c in roots.items() if ret(x) < N)
        norm = {x: c for x, c in roots.items() if nu(ret(x)) < N}
        got = dict(N=N, prior_complement_mass=prior, raw_removed=raw,
                   normalized_removed=sum(norm.values()),
                   remaining=prior - sum(norm.values()),
                   normalized_weight2_roots=sum(c == 2 for c in norm.values()))
        need(got == row, f"profile N={N}: {got} vs {row}")
        K = 3 * ((3 * N // 2).bit_length() - 1)
        err = F(7 * (K - 3) * (K - 2), 2) + 1
        need(al * N - err <= raw <= ah * N + err, f"bound (14) N={N}")
    need(len(receipt["profile_cases"]) == 68, "profile case count")

    for row in receipt["normalized_unbounded_returns"]:
        a = row["a"]
        x, N = 2 ** a - 1, 12 * 2 ** (a - 4)
        f = ret(x)
        need(a % 16 == 7 and row["root"] == x and row["N"] == N, f"escape labels a={a}")
        need(x % 12 == 7 and 9 * N < 8 * x < 12 * N and not selected(x), f"escape root a={a}")
        need(params(x)[2] == 3 and f == (3 ** a - 3) // 8 and f % 8 == 1, f"escape return a={a}")
        need(nu(f) == f == row["canonical_return"] and f > x, f"escape canonical a={a}")
    for row in receipt["parameter_label_cycle"]:
        x = row["root"]
        a, t, d, w = params(x)
        need(dict(root=x, a=a, d=d, raw_return=ret(x), canonical_return=nu(ret(x))) == row,
             f"label cycle {x}")
    need([r["canonical_return"] for r in receipt["parameter_label_cycle"][:2]] == [31, 91], "27->31->91")
    ex = receipt["coefficient_two_example"]
    need(residual_roots(168).get(187) == 2 and ret(187) == 211 and nu(211) == 105, "root 187")
    need(ex["arithmetic_prefix"] == [187, step(187), iterate(187, 2)] == [187, 281, 211], "prefix 187")
    need(ex["normalization_left"] == [211, step(211), iterate(211, 2)], "normalization left")
    need(ex["normalization_right"] == [105, step(105), iterate(105, 2)], "normalization right")
    need(ex["normalization_left"][-1] == ex["normalization_right"][-1], "normalization coalescence")
    with (HERE / "outer_187_double_current.csv").open(newline="") as src:
        current = {int(r["state"]): int(r["current"]) for r in csv.DictReader(src)}
    div = {}
    for x, c in current.items():
        if x == 1:
            continue
        div[x] = div.get(x, 0) + c
        y = step(x)
        if y != 1:
            div[y] = div.get(y, 0) - c
    need({x: c for x, c in div.items() if c} == {187: 2}, "stored current divergence")
    sha = hashlib.sha256("".join(f"{x},{c}\n" for x, c in sorted(current.items())).encode()).hexdigest()
    need(len(current) == ex["current_rows"] and sha == ex["current_sha256"], "stored current hash")

    if fails:
        print(f"FAIL: {len(fails)} mismatches; first: {fails[0]}")
        sys.exit(1)
    print(f"PASS: {seeds} complementary seeds, {cases} parameter cases, "
          f"{len(receipt['profile_cases'])} normalized profile counts, K=64 enclosures, "
          f"{len(receipt['normalized_unbounded_returns'])} unbounded returns, stored 187 current")


if __name__ == "__main__":
    main()
