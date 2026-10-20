"""S13: the rise lemma -- along a climb, each agreeing run of a rotation can at most multiply the height by log2 3.

Setting: a primitive positive odd cycle n_0..n_(m-1) of 3x+q (q odd), 2^(a_p) n_(p+1) = 3 n_p + q, minimum L,
log-profile y_p = log2(n_p / L), sigma = log2 3 - 1, eta = q / (3 L ln 2), kappa = log2 3 + eta.
Fix a rotation 0 < h < m and an orientation o = +1 or -1 (partner p + o h). A position p is a mismatch when
a_p != a_(p + o h); there are s(h) of them in either orientation.

Rise lemma. For a forward stretch u -> v containing k mismatches (positions u <= e < v), with run starts
b_0 = u and b_j = e_j + 1, put Dplus = max_j (y_(b_j + o h) - y_(b_j))^+ and c = log2 L + 1 + Dplus. Then

        y_v + c <= kappa^(k+1) (y_u + c).

Proof ingredients (each checked separately below): (W) the 2-adic start witness -- if n_b and n_(b+oh) have the
same next valuations up to (not including) the next mismatch, with letter sum F, then n_b = n_(b+oh) mod 2^(F+1),
so max(n_b, n_(b+oh)) > 2^(F+1); (P) a run of t letters with sum F >= t, followed by its mismatch step, raises the
profile by at most (F + 1)(sigma + eta).

Corollary (u = argmin, v = argmax): s(h) >= k >= log_kappa(1 + B/c) - 1, B = max y, and Dplus <= (sigma + eta)|h|_m
in the better orientation.

Checks: (a) every actual 3x+q cycle, odd q < 2000 with 3 not dividing q (cycles from seeds <= 1001): the lemma for
every rotation, both orientations, every pair (u, v) when m <= 64 and the argmin -> argmax stretch for every m;
(W) at every run start; the corollary with Dplus and with (sigma + eta)|h|_m. (b) The word form on exhaustive
primitive words over {1,2,3} (m <= 9) and {1,...,4} (m <= 7) with D > 0, using the integer cycle of 3x + den(w).
Writes s13_rise_lemma.json.
"""
import json
import math
import sys
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402

LOG3 = math.log2(3)
SIG = LOG3 - 1


def lg(x):
    return math.log2(x)


def check_cycle(n, a, q, st, allpairs):
    """n: cycle elements (any rotation), a: valuations, q: parameter. Updates st."""
    m = len(n)
    L = min(n)
    ellp = lg(L)
    eta = q / (3 * L * math.log(2))
    kap = LOG3 + eta
    lkap = math.log(kap)
    y = [lg(x) - ellp for x in n]
    u0 = n.index(L)
    v0 = max(range(m), key=lambda p: n[p])
    B = y[v0]
    for h in range(1, m):
        for o in (1, -1):
            d = (o * h) % m
            mis = [a[p] != a[(p + d) % m] for p in range(m)]
            s = sum(mis)
            # (W) the start witness at every run start (and at the minimum)
            for b in range(m):
                if mis[b] or not (mis[(b - 1) % m] or b == u0):
                    continue
                F, p = 0, b
                while not mis[p % m]:
                    F += a[p % m]
                    p += 1
                st["W_checks"] += 1
                if not max(n[b], n[(b + d) % m]) > 2 ** (F + 1):
                    st["W_viol"] += 1
                if (n[b] - n[(b + d) % m]) % (2 ** (F + 1)) != 0:
                    st["W_cong_viol"] += 1
            starts = range(m) if (allpairs and m <= 64) else [u0]
            for u in starts:
                k = 0
                dplus = 0.0 if mis[u] else max(0.0, y[(u + d) % m] - y[u])   # b_0 = u, witness needed iff run nonempty
                for j in range(1, m):
                    v = (u + j) % m
                    newstart = mis[(v - 1) % m]
                    if newstart:
                        k += 1
                    # check (u, v): run starts b_0..b_k, the last one only if its run [b_k, v) is nonempty
                    c = ellp + 1 + dplus
                    lhs = y[v] + c
                    # compare in logs (kappa can be large when q/L is large)
                    st["lemma_checks"] += 1
                    if math.log(lhs) > (k + 1) * lkap + math.log(y[u] + c) + 1e-12:
                        st["lemma_viol"] += 1
                    if y[v] > y[u] + 1e-9:
                        sl = (k + 1) - math.log(lhs / (y[u] + c)) / lkap
                        st["min_slack"] = min(st["min_slack"], sl)
                    if newstart and not mis[v]:
                        dplus = max(dplus, y[(v + d) % m] - y[v])
            # corollary on the argmin -> argmax stretch, with the global Dplus and with (sigma+eta)|h|_m
            hm = min(h, m - h)
            dglob = max(0.0, max(y[(p + d) % m] - y[p] for p in range(m)))
            for tag, dp in (("cor_dplus", dglob), ("cor_hm", (SIG + eta) * hm)):
                c = ellp + 1 + dp
                bound = math.log(1 + B / c) / math.log(kap) - 1
                st[tag + "_checks"] += 1
                if s < bound - 1e-9:
                    st[tag + "_viol"] += 1
            if dglob > (SIG + eta) * d + 1e-9:
                st["dplus_hm_viol"] += 1


def actual_cycles(st):
    per_q = {}
    for q in range(1, 2000, 2):
        if q % 3 == 0:
            continue
        for cyc in cycles(q, 1001):
            m = len(cyc)
            if m < 2:
                continue
            a = [step(x, q)[1] for x in cyc]
            before = st["lemma_viol"] + st["W_viol"] + st["cor_dplus_viol"] + st["cor_hm_viol"]
            check_cycle(cyc, a, q, st, allpairs=True)
            st["cycles"] += 1
            st["rotations"] += m - 1
            if q in (5, 7, 13, 61):
                after = st["lemma_viol"] + st["W_viol"] + st["cor_dplus_viol"] + st["cor_hm_viol"]
                per_q.setdefault(q, [0, 0])
                per_q[q][0] += 1
                per_q[q][1] += after - before
    st["controls_d5_7_13_61"] = {str(k): {"cycles": v[0], "violations": v[1]} for k, v in sorted(per_q.items())}


def word_cycle(w):
    """Integer cycle of 3x + den(w) for a positive word w with D > 0; None if not primitive."""
    m, A = len(w), sum(w)
    D = 2**A - 3**m
    if D <= 0:
        return None
    for per in range(1, m):
        if m % per == 0 and w == w[per:] + w[:per]:
            return None
    Cs = []
    for p in range(m):
        u = w[p:] + w[:p]
        C, S = 0, 0
        for j in range(m):
            C += 3 ** (m - 1 - j) * 2**S
            S += u[j]
        Cs.append(C)
    g = gcd(Cs[0], D)
    den = D // g
    n = [den * C // D for C in Cs]
    assert all(den * C % D == 0 for C in Cs)
    return n, den, D


def exhaustive(st):
    seen = set()
    for alph, mmax in (((1, 2, 3), 9), ((1, 2, 3, 4), 7)):
        for m in range(2, mmax + 1):
            for w in product(alph, repeat=m):
                w = list(w)
                key = min(tuple(w[p:] + w[:p]) for p in range(m))
                if key in seen:
                    continue
                seen.add(key)
                r = word_cycle(w)
                if r is None:
                    continue
                n, den, D = r
                for p in range(m):
                    assert step(n[p], den) == (n[(p + 1) % m], w[p])
                check_cycle(n, w, den, st, allpairs=(m <= 7))
                st["words"] += 1
                # word form: log2 den >= B/(kappa^(s+1) - 1) - 1 - Dplus_hm - lambda(w), lambda = log2(m 2^A/(3D))
                L = min(n)
                xmin = Fraction(L, den)
                eta = float(1 / (3 * xmin)) / math.log(2)
                kap = LOG3 + eta
                B = lg(max(n)) - lg(L)
                lam = lg(m) + sum(w) - LOG3 - lg(D)
                for h in range(1, m):
                    s = sum(w[p] != w[(p + h) % m] for p in range(m))
                    hm = min(h, m - h)
                    law = B / math.expm1((s + 1) * math.log(kap)) - 1 - (SIG + eta) * hm - lam if (s + 1) * math.log(kap) < 700 else -1 - (SIG + eta) * hm - lam
                    st["word_law_checks"] += 1
                    if lg(den) < law - 1e-9:
                        st["word_law_viol"] += 1
                    st["word_law_min_margin"] = min(st["word_law_min_margin"], lg(den) - law)


def main():
    st = {k: 0 for k in ("cycles", "rotations", "W_checks", "W_viol", "W_cong_viol", "lemma_checks",
                         "lemma_viol", "cor_dplus_checks", "cor_dplus_viol", "cor_hm_checks", "cor_hm_viol",
                         "dplus_hm_viol", "words", "word_law_checks", "word_law_viol")}
    st["min_slack"] = float("inf")
    st["word_law_min_margin"] = float("inf")
    actual_cycles(st)
    st["min_slack_actual"] = round(st["min_slack"], 4)
    st["min_slack"] = float("inf")
    exhaustive(st)
    st["min_slack_words"] = round(st["min_slack"], 4)
    del st["min_slack"]
    st["word_law_min_margin"] = round(st["word_law_min_margin"], 4)
    print(json.dumps(st, indent=1))
    Path(__file__).with_suffix(".json").write_text(json.dumps(st, indent=1))
    bad = sum(st[k] for k in st if k.endswith("viol"))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
