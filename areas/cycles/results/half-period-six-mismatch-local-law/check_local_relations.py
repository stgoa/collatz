#!/usr/bin/env python3
"""Certificate for half-period-six-mismatch-local-law.

Standard library only, exact arithmetic for every decision, deterministic. Run from the repository root:

    python3 areas/cycles/results/half-period-six-mismatch-local-law/check_local_relations.py
    python3 areas/cycles/results/half-period-six-mismatch-local-law/check_local_relations.py --show 3 +++ +++

The second form prints the multipliers of one sign case (d, signs of the changes, signs of y_k - x_k) and
writes nothing. It exits with status 1 if any check fails and writes check_local_relations.json next to itself.

V1  constants: rational bounds for log_2(3), the bound lambda = 1/500 for the minimum, local descent below 2^17,
    and the size thresholds used in the text.
V2  the linear programmes: for d = 1, 2, 3 changed positions and every sign case, an exact rational Farkas
    certificate that the rows L1 to L7 together with "all 4d relations fail by N/50 bits" have no solution.
    The certificate is found by an exact simplex and then verified from scratch (nonnegative multipliers,
    nonnegative column sums, negative right-hand side). For d = 1 the size rows alone are certified infeasible.
V3  actual cycles of 3x+q with the true addend: the identities (R1), (U), (V), the integrality and nonvanishing
    of the quotients g_k, and every row of V2 that does not depend on the addend, evaluated with the same
    indexing code as V2.
V4  the normal form: a word whose halves differ in d positions can be rotated so that the differences sit at
    the ends of d blocks of each half and a chosen block comes first.
"""
import itertools
import json
import math
import random
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent

ALO = F(15849, 10000)          # < log_2(3)
AHI = F(158497, 100000)        # > log_2(3)
THETA = F(1, 2 ** 18)          # error of every height recursion and of the budget
LAM = F(1, 500)                # (log_2 of the minimum) / N for N >= 2^22
MU = F(1, 50)                  # the spare bits per unit of N
N0 = 2 ** 22

FAILED = []


def check(cond, msg):
    if not cond:
        FAILED.append(msg)
        print("FAIL:", msg)
    return cond


# ----------------------------------------------------------------------------------------------- V1

def v1_constants():
    out = {}
    check(2 ** 15849 < 3 ** 10000, "15849/10000 < log_2 3")
    check(3 ** 100000 < 2 ** 158497, "log_2 3 < 158497/100000")
    out["alpha_bounds"] = [str(ALO), str(AHI)]
    # local descent: every odd 3 <= n < 2^17 reaches a smaller odd number
    worst = 0
    for n in range(3, 2 ** 17, 2):
        x = n
        steps = 0
        while x >= n:
            x = 3 * x + 1
            while x % 2 == 0:
                x //= 2
            steps += 1
            if steps > 10000:
                check(False, f"no descent found for {n}")
                break
        worst = max(worst, steps)
    out["descent_below_2^17_max_odd_steps"] = worst
    # lambda: (514 + 342 log_2 N)/N <= 1/500 at N = 2^22 (the left side decreases for N >= 3)
    lam_at_n0 = F(514 + 342 * 22, N0)
    check(lam_at_n0 <= LAM, "(514 + 342*22)/2^22 <= 1/500")
    out["lambda_at_2^22"] = str(lam_at_n0)
    # the function N -> (514 + 342 log_2 N)/N is decreasing once 342/ln 2 < 514 + 342 log_2 N, true for N >= 1
    check(342 * 1000 < 693 * 514, "342/ln 2 < 514 (so the bound on the minimum decreases in N)")
    # 1/N <= THETA and the error of a block: B/(2M) <= N/2^18 with M >= 2^17
    check(F(1, N0) <= THETA, "1/N <= 2^-18 for N >= 2^22")
    # sizes for the finiteness node: 3p < 2^(N/100) with p < 2N + 2, and every term below 2^(5N)
    check(6 * N0 + 6 < 2 ** (N0 // 100), "3(2N+2) < 2^(N/100) at N = 2^22")
    out["mu"] = str(MU)
    return out


# ----------------------------------------------------------------------------------------------- V2

def indexers(d):
    ib = lambda k: k % d
    ie = lambda k: d + k % d
    ip = lambda k: 2 * d + k % d
    ig = lambda k: 3 * d + k % d
    iz = lambda K: 4 * d + K % (2 * d)
    return ib, ie, ip, ig, iz


def build_rows(d, eps_sign, rho, with_failure=True):
    """Rows (name, coefficient list, right-hand side) meaning sum coef * x <= rhs, with all variables >= 0.

    Variables, all divided by N: b_k (block length), e_k (common total minus length), pi_k (size of the change),
    G_k (log_2 |g_k|), for k < d; Z_K (log_2 of the state before block K of the cycle), K in Z/2d.
    eps_sign[k] = +1 if the second half carries the larger final letter of block k, -1 otherwise.
    rho[k] = +1 if y_k > x_k, -1 otherwise.
    """
    n = 6 * d
    ib, ie, ip, ig, iz = indexers(d)
    rows = []

    def le(name, coef, rhs):
        v = [F(0)] * n
        for i, a in coef:
            v[i] += F(a)
        rows.append((name, v, F(rhs)))

    def ex(K):
        K %= 2 * d
        k = K % d
        return [(ip(k), 1)] if ((eps_sign[k] < 0) == (K < d)) else []

    le("L1+", [(ib(k), 1) for k in range(d)], 1)
    le("L1-", [(ib(k), -1) for k in range(d)], -1)
    bud = [(ib(k), 1) for k in range(d)] + [(ie(k), 1) for k in range(d)] + [(ip(k), F(1, 2)) for k in range(d)]
    le("L2+", bud, AHI + THETA)
    le("L2-", [(i, -a) for i, a in bud], -ALO)
    for K in range(2 * d):
        base = [(iz(K + 1), 1), (iz(K), -1), (ie(K), 1)] + ex(K)
        le(f"L3lo[{K}]", [(i, -a) for i, a in base] + [(ib(K), -(1 - ALO))], 0)
        le(f"L3hi[{K}]", base + [(ib(K), 1 - AHI)], THETA)
    le("L5", [(iz(0), 1), (ie(0), -1)], LAM)
    for k in range(d):
        if rho[k] > 0:
            le(f"rho[{k}]", [(iz(k), 1), (iz(k + d), -1)], 0)
            le(f"L6[{k}]", [(ig(k), 1), (ib(k), 1), (ie(k), 1), (iz(k + d), -1)], 0)
        else:
            le(f"rho[{k}]", [(iz(k + d), 1), (iz(k), -1)], 0)
            le(f"L6[{k}]", [(ig(k), 1), (ib(k), 1), (ie(k), 1), (iz(k), -1)], 0)
    if with_failure:
        for k in range(d):
            for track, U in (("U", iz(k + 1)), ("V", iz(k + 1 + d))):
                withp = (eps_sign[k] > 0) == (track == "U")
                t1 = [(ib(k), ALO), (ig(k), 1)]
                t2 = [(ib(k + 1), 1), (ie(k + 1), 1), (ig(k + 1), 1)] + ([(ip(k), 1)] if withp else [])
                cost3 = [(ig(k), 1), (ig(k + 1), 1), (ip(k), 1), (U, 1)]
                for nm, t in (("T1", t1), ("T2", t2)):
                    le(f"F3{track}[{k}].{nm}", t + [(i, -a) for i, a in cost3], MU)
                cost4 = [(ig(k), 1), (ig(k + 1), 1), (U, 2)]
                for nm, t in (("T1", t1), ("T2", t2), ("T3", [(ip(k), 1), (U, 1)])):
                    le(f"F4{track}[{k}].{nm}", t + [(i, -a) for i, a in cost4], MU)
    return n, rows


def farkas_search(n, rows):
    """Exact simplex (Bland's rule) for: minimise sum y_i b_i subject to sum_i y_i a_ij >= 0 for every column j,
    sum y_i <= 1, y >= 0. Returns the multipliers y. Nothing is trusted from this function: see farkas_verify."""
    m = len(rows)
    ncol = m + n + 1
    tab = []
    for j in range(n):
        tab.append([-rows[i][1][j] for i in range(m)] + [F(1) if jj == j else F(0) for jj in range(n)] + [F(0), F(0)])
    tab.append([F(1)] * m + [F(0)] * n + [F(1), F(1)])
    basis = [m + j for j in range(n)] + [m + n]
    obj = [rows[i][2] for i in range(m)] + [F(0)] * (n + 2)
    pivots = 0
    while True:
        enter = -1
        for c in range(ncol):
            if obj[c] < 0:
                enter = c
                break
        if enter < 0:
            break
        best = None
        leave = -1
        for r in range(n + 1):
            a = tab[r][enter]
            if a > 0:
                ratio = tab[r][-1] / a
                if best is None or ratio < best or (ratio == best and basis[r] < basis[leave]):
                    best = ratio
                    leave = r
        if leave < 0:
            return None, pivots
        piv = tab[leave][enter]
        tab[leave] = [v / piv for v in tab[leave]]
        rowl = tab[leave]
        for r in range(n + 1):
            f = tab[r][enter]
            if r != leave and f != 0:
                tab[r] = [v - f * w for v, w in zip(tab[r], rowl)]
        f = obj[enter]
        if f != 0:
            obj = [v - f * w for v, w in zip(obj, rowl)]
        basis[leave] = enter
        pivots += 1
    y = [F(0)] * m
    for r, bv in enumerate(basis):
        if bv < m:
            y[bv] = tab[r][-1]
    return y, pivots


def farkas_verify(n, rows, y):
    """The rows say A x <= b with x >= 0. If y >= 0, y^T A >= 0 in every column and y^T b < 0, there is no such x:
    0 <= (y^T A) x <= y^T b < 0."""
    if y is None or len(y) != len(rows) or any(v < 0 for v in y):
        return None
    for j in range(n):
        if sum(y[i] * rows[i][1][j] for i in range(len(rows))) < 0:
            return None
    value = sum(y[i] * rows[i][2] for i in range(len(rows)))
    return value if value < 0 else None


def v2_programmes():
    out = {}
    for d in (1, 2, 3):
        cases = 0
        max_support = 0
        weakest = None
        used = {}
        for eps_sign in itertools.product([1, -1], repeat=d):
            for rho in itertools.product([1, -1], repeat=d):
                n, rows = build_rows(d, eps_sign, rho)
                y, _ = farkas_search(n, rows)
                value = farkas_verify(n, rows, y)
                cases += 1
                if not check(value is not None, f"no certificate for d={d}, eps={eps_sign}, rho={rho}"):
                    continue
                support = [rows[i][0] for i in range(len(rows)) if y[i] != 0]
                max_support = max(max_support, len(support))
                for nm in support:
                    key = nm.split("[")[0] if nm[0] != "F" else nm.split("[")[0]
                    used[key] = used.get(key, 0) + 1
                if weakest is None or value > weakest[0]:
                    weakest = (value, eps_sign, rho)
        out[f"d={d}"] = {
            "cases_certified": cases,
            "largest_support": max_support,
            "weakest_value": str(weakest[0]) if weakest else None,
            "weakest_case": [list(weakest[1]), list(weakest[2])] if weakest else None,
            "rows_used": dict(sorted(used.items())),
        }
        print(f"V2 d={d}: {cases} sign cases certified; largest support {max_support}")
    # d = 1: the size rows alone
    cases = 0
    for eps_sign in itertools.product([1, -1], repeat=1):
        for rho in itertools.product([1, -1], repeat=1):
            n, rows = build_rows(1, eps_sign, rho, with_failure=False)
            y, _ = farkas_search(n, rows)
            cases += 1
            check(farkas_verify(n, rows, y) is not None, f"size rows feasible for d=1, eps={eps_sign}, rho={rho}")
    out["d=1 size rows only"] = {"cases_certified": cases}
    # d = 2 with three-term relations only (Ridout's theorem suffices there): rows F4 removed
    cases = 0
    for eps_sign in itertools.product([1, -1], repeat=2):
        for rho in itertools.product([1, -1], repeat=2):
            n, rows = build_rows(2, eps_sign, rho)
            rows = [r for r in rows if not r[0].startswith("F4")]
            y, _ = farkas_search(n, rows)
            cases += 1
            check(farkas_verify(n, rows, y) is not None, f"three-term rows feasible for d=2, eps={eps_sign}, rho={rho}")
    out["d=2 three-term relations only"] = {"cases_certified": cases}
    return out


# ----------------------------------------------------------------------------------------------- V3

def intercept(word):
    c = 0
    s = 0
    m = len(word)
    for i, w in enumerate(word):
        c += 3 ** (m - 1 - i) * 2 ** s
        s += w
    return c


def cycle_states(word):
    """States of the cycle of 3x+q with q = 2^sum - 3^len (true addend), or None if q <= 0."""
    m = len(word)
    q = 2 ** sum(word) - 3 ** m
    if q <= 0:
        return None, None
    z = intercept(word)
    states = []
    for w in word:
        states.append(z)
        num = 3 * z + q
        if num % (2 ** w) != 0:
            return None, None
        z = num // 2 ** w
    if z != states[0]:
        return None, None
    return q, states


def random_instance(rng, d):
    blocks = []
    for _ in range(d):
        length = rng.randint(1, 7)
        letters = [rng.choice([1, 1, 1, 2, 2, 3, 5]) for _ in range(length - 1)]
        kappa = rng.choice([1, 1, 2, 3])
        p = rng.choice([1, 1, 2, 3, 4, 7, 11])
        side = rng.choice([1, -1])
        blocks.append((letters, kappa, p, side))
    first = []
    second = []
    for letters, kappa, p, side in blocks:
        first += letters + [kappa + (p if side < 0 else 0)]
        second += letters + [kappa + (p if side > 0 else 0)]
    return blocks, first + second


def v3_controls():
    rng = random.Random(20261123)
    tested = {1: 0, 2: 0, 3: 0}
    rows_checked = 0
    min_ratio = None
    for d in (1, 2, 3):
        attempts = 0
        while tested[d] < 4000 and attempts < 200000:
            attempts += 1
            blocks, word = random_instance(rng, d)
            q, states = cycle_states(word)
            if q is None:
                continue
            n_half = len(word) // 2
            lengths = [len(b[0]) + 1 for b in blocks]
            s = [sum(b[0]) + b[1] for b in blocks]
            nu = [b[2] if b[3] < 0 else 0 for b in blocks]        # extra final letter of the first half
            nup = [b[2] if b[3] > 0 else 0 for b in blocks]       # extra final letter of the second half
            starts = [sum(lengths[:k]) for k in range(d + 1)]
            x = [states[starts[k]] for k in range(d)] + [states[n_half]]
            y = [states[n_half + starts[k]] for k in range(d)] + [states[0]]
            ok = True
            g = []
            for k in range(d):
                diff = y[k] - x[k]
                ok &= check(diff % 2 ** s[k] == 0, "2^s_k divides y_k - x_k")
                g.append(diff // 2 ** s[k])
                ok &= check(g[k] != 0, "g_k is not zero")
            if not ok:
                continue
            g.append(-g[0])
            s_ext = s + [s[0]]
            for k in range(d):
                lhs = 3 ** lengths[k] * g[k]
                check(lhs == 2 ** nup[k] * y[k + 1] - 2 ** nu[k] * x[k + 1], "identity (R1)")
                check(lhs == (2 ** nup[k] - 2 ** nu[k]) * x[k + 1] + 2 ** (nup[k] + s_ext[k + 1]) * g[k + 1],
                      "identity (U)")
                check(lhs == (2 ** nup[k] - 2 ** nu[k]) * y[k + 1] + 2 ** (nu[k] + s_ext[k + 1]) * g[k + 1],
                      "identity (V)")
                check(2 ** s[k] * abs(g[k]) < max(x[k], y[k]), "2^s_k |g_k| < max(x_k, y_k)")
            # block equations with the true addend, and the addend-free rows through the indexing of V2
            eps_sign = tuple(b[3] for b in blocks)
            rho = tuple(1 if y[k] > x[k] else -1 for k in range(d))
            ib, ie, ip, ig, iz = indexers(d)
            val = [0.0] * (6 * d)
            for k in range(d):
                val[ib(k)] = lengths[k] / n_half
                val[ie(k)] = (s[k] - lengths[k]) / n_half
                val[ip(k)] = blocks[k][2] / n_half
                val[ig(k)] = math.log2(abs(g[k])) / n_half
                val[iz(k)] = math.log2(x[k]) / n_half
                val[iz(k + d)] = math.log2(y[k]) / n_half
            _, rows = build_rows(d, eps_sign, rho, with_failure=False)
            for name, coef, rhs in rows:
                if name.startswith(("L1", "L3lo", "rho", "L6")):
                    lhs = sum(float(a) * v for a, v in zip(coef, val))
                    # L3lo is stated with the lower bound ALO of log_2 3; allow its rounding
                    check(lhs <= float(rhs) + 1e-9, f"row {name} on an actual cycle (d={d})")
                    rows_checked += 1
            # the block containing a minimum starts at most 2^(s - B) above it
            mn = min(states)
            pos = states.index(mn)
            cyc_starts = [starts[k] for k in range(d)] + [n_half + starts[k] for k in range(d)] + [2 * n_half]
            K = max(i for i in range(2 * d) if cyc_starts[i] <= pos)
            check(states[cyc_starts[K]] <= mn * 2 ** (s[K % d] - lengths[K % d]),
                  "the block of the minimum starts at most 2^(s-B) above it")
            ratio = math.log2(mn) / n_half
            min_ratio = ratio if min_ratio is None else min(min_ratio, ratio)
            tested[d] += 1
        check(tested[d] == 4000, f"4000 actual cycles for d={d}")
    return {"actual_cycles": tested, "addend_free_rows_checked": rows_checked,
            "smallest_log2_minimum_over_N": round(min_ratio, 6)}


# ----------------------------------------------------------------------------------------------- V4

def v4_normal_form():
    rng = random.Random(7)
    tested = 0
    for _ in range(3000):
        n_half = rng.randint(3, 14)
        d = rng.randint(1, min(3, n_half))
        first = [rng.randint(1, 4) for _ in range(n_half)]
        second = list(first)
        pos = sorted(rng.sample(range(n_half), d))
        for i in pos:
            if rng.random() < 0.5:
                second[i] += rng.randint(1, 5)
            else:
                first[i] += rng.randint(1, 5)
        word = first + second
        # rotate so that the last difference is at the end of a half
        r = pos[-1] + 1
        w = word[r:] + word[:r]
        diffs = [i for i in range(n_half) if w[i] != w[i + n_half]]
        ok = check(len(diffs) == d and diffs[-1] == n_half - 1, "normal form: last difference at the end of a half")
        if not ok:
            continue
        ends = diffs
        starts = [0] + [e + 1 for e in ends[:-1]]
        # rotating by the start of any block of the cycle keeps the form
        for K in range(2 * d):
            shift = (starts[K % d] + (n_half if K >= d else 0)) % (2 * n_half)
            w2 = w[shift:] + w[:shift]
            diffs2 = [i for i in range(n_half) if w2[i] != w2[i + n_half]]
            lengths = [ends[k] - starts[k] + 1 for k in range(d)]
            rot_lengths = [lengths[(K + i) % d] for i in range(d)]
            expected = [sum(rot_lengths[:i + 1]) - 1 for i in range(d)]
            check(diffs2 == expected, "normal form: rotation by a block start")
        tested += 1
    return {"words_tested": tested}


def show_case(d, eps_sign, rho):
    """Print the multipliers of one sign case, for a reader who wants to follow a certificate by hand."""
    n, rows = build_rows(d, eps_sign, rho)
    y, _ = farkas_search(n, rows)
    value = farkas_verify(n, rows, y)
    print(f"d={d} eps={eps_sign} rho={rho}: verified={value is not None}")
    for (name, _, rhs), v in zip(rows, y):
        if v != 0:
            print(f"   {str(v):>40}  x  {name}   (right-hand side {rhs})")
    print(f"   combination of the right-hand sides: {value}")


def main():
    if len(sys.argv) == 5 and sys.argv[1] == "--show":
        sign = lambda t: tuple(1 if ch == "+" else -1 for ch in t)
        show_case(int(sys.argv[2]), sign(sys.argv[3]), sign(sys.argv[4]))
        return
    receipt = {
        "V1_constants": v1_constants(),
        "V2_linear_programmes": v2_programmes(),
        "V3_actual_cycles": v3_controls(),
        "V4_normal_form": v4_normal_form(),
    }
    if FAILED:
        print(f"{len(FAILED)} check(s) failed")
        sys.exit(1)
    (HERE / "check_local_relations.json").write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n")
    print("all checks passed; receipt written")


if __name__ == "__main__":
    main()
