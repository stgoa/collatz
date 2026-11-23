#!/usr/bin/env python3
"""Exploration for near-circuit-rotation-forced-relation (not a certificate; never run by CI).

Near-circuits whose small defects form two long runs along the rotation: a run of n defects right after the
giant letter in the order of the rotation, and a separate run of n' defects starting at time q. For a
multiple j of the rotation smaller than both run lengths, the mismatches are at the times
    1,   1 - k h and q - k h (k = 1..j),   theta - k h and theta' - k h (k = 0..j-1),
where theta = frac(n h) and theta' = frac(q + (n'-1) h) are the ends of the two runs. So the configuration is
a point (h, q, theta, theta') of a four-dimensional family, whatever the order of the rotation.

Part 1: random search, with local improvement, for points where every run of every multiple j <= J has
G = (higher starting height) - (run length) >= 0, with heights (alpha - 1) t.
Part 2: each point found is realised with explicit run lengths and passed to the explicit model, which
re-checks the rows and computes the best margin of the three- and four-term relations of the multiples
j <= 3 (positive margin: some relation has a small product of parts coprime to 6).

Standard library only, floating point, fixed seed.

    python3 areas/cycles/results/near-circuit-rotation-forced-relation/explore_long_runs.py [--write-receipt]
"""
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path

AL = math.log2(3.0)
A1 = AL - 1.0
HERE = Path(__file__).resolve().parent


def frac1(x):
    f = x - math.floor(x)
    return 1.0 if f < 1e-12 else f


def slack(h, q, th, thp, J, stop_below=None):
    worst = 1e9
    for j in range(1, J + 1):
        cuts = [(1.0, 0)]
        for k in range(1, j + 1):
            cuts.append((frac1(1.0 - k * h), 1 if k == j else 0))
            cuts.append((frac1(q - k * h), 0))
        for k in range(j):
            cuts.append((frac1(th - k * h), 0))
            cuts.append((frac1(thp - k * h), 0))
        cuts.sort()
        for a in range(len(cuts)):
            u, flag = cuts[a - 1]
            v = cuts[a][0]
            ell = v - u if a > 0 else v - u + 1.0
            if ell < 1e-12:
                continue
            g = max(0.0 if u == 1.0 else A1 * u, 0.0 if flag else A1 * frac1(u + j * h)) - ell
            if g < worst:
                worst = g
                if stop_below is not None and worst < stop_below:
                    return worst
    return worst


def analyse(h, n, q, n2, J, Jcrit=3, tol=1e-9):
    """Explicit model: giant at index 0 of the orbit through time 1, defects at its indices 1..n, defects at
    indices 0..n2-1 of the orbit through q. Returns (rows hold for j <= J, best margin for j <= Jcrit)."""
    lab = {(0, 0): "K"}
    for i in range(1, n + 1):
        lab[(0, i)] = "s"
    for i in range(n2):
        lab[(1, i)] = "r"
    base = (1.0, q)
    label = lambda o, i: lab.get((o, i), "1")
    tm = lambda o, i: frac1(base[o] + i * h)
    after = lambda t, l: 0.0 if l == "K" else A1 * t
    best = -1e9
    for j in range(1, J + 1):
        cand = set()
        for (o, i) in lab:
            cand.add((o, i))
            cand.add((o, i - j))
        cuts = sorted((tm(o, i), o, i, label(o, i), label(o, i + j)) for (o, i) in cand if label(o, i) != label(o, i + j))
        runs = []
        for a in range(len(cuts)):
            tv = cuts[a][0]
            tu, ou, iu, lau, lbu = cuts[a - 1]
            ell = tv - tu + (0.0 if (a > 0 and tv > tu) else 1.0)
            g = max(after(tu, lau), after(tm(ou, iu + j), lbu)) - ell
            if g < -tol:
                return False, None
            runs.append((ell, g))
        if j <= Jcrit:
            for a in range(len(cuts)):
                tv, o, i, la, lb = cuts[a]
                ell, g = runs[a]
                ell_n, g_n = runs[(a + 1) % len(cuts)]
                nu = A1 if la == "K" else 0.0
                nup = A1 if lb == "K" else 0.0
                p = nu + nup
                t1 = AL * ell + g
                for z, cexp in ((after(tv, la), nup), (after(tm(o, i + j), lb), nu)):
                    t2 = cexp + ell_n + g_n
                    best = max(best, max(t1, t2) - (g + g_n + p + z), max(t1, t2, p + z) - (g + g_n + 2 * z))
    return True, best


def realise(h, q, th, thp, nmin=40, nmax=3000):
    dist = lambda x: abs(((x + 0.5) % 1.0) - 0.5)
    n = min(range(nmin, nmax), key=lambda k: dist(k * h - th))
    n2 = min(range(nmin, nmax), key=lambda k: dist(q + (k - 1) * h - thp))
    return n, n2


def main():
    rng = random.Random(11)
    trials, J = 150000, 12
    pool = []
    for _ in range(trials):
        p = (rng.uniform(0.02, 0.5), rng.random(), rng.random(), rng.random())
        if slack(*p, J=4, stop_below=-0.01) > -0.01:
            pool.append(p)
    found = []
    for p in pool:
        cur, cs = p, slack(*p, J=J)
        step = 0.01
        for it in range(150):
            cand = tuple(min(0.9999, max(0.0001, c + rng.gauss(0, step))) for c in cur)
            cand = (min(0.5, max(0.01, cand[0])),) + cand[1:]
            s2 = slack(*cand, J=J, stop_below=cs)
            if s2 > cs:
                cur, cs = cand, s2
            if cs >= 0.002 and it > 30:
                break
        if cs >= 0.0:
            found.append(cur)
    margins, rotation, survive24, margins24 = [], [], 0, []
    for (h, q, th, thp) in found:
        n, n2 = realise(h, q, th, thp)
        ok, best = analyse(h, n, q, n2, J)
        if ok:
            margins.append(best)
            rotation.append(round(h, 2))
            ok24, best24 = analyse(h, n, q, n2, 24)
            if ok24:
                survive24 += 1
                margins24.append(best24)
    receipt = {
        "random_points": trials,
        "pass_first_4_multiples_within_0.01": len(pool),
        "rows_of_12_multiples_hold_after_local_search": len(found),
        "confirmed_by_explicit_model_with_12_multiples": len(margins),
        "smallest_best_margin": round(min(margins), 4) if margins else None,
        "largest_best_margin": round(max(margins), 4) if margins else None,
        "rotation_numbers_rounded": {str(k): v for k, v in sorted(Counter(rotation).items())},
        "of_these_rows_of_24_multiples_hold": survive24,
        "smallest_best_margin_with_24_multiples": round(min(margins24), 4) if margins24 else None,
    }
    print(json.dumps(receipt, indent=1))
    if "--write-receipt" in sys.argv:
        (HERE / "explore_long_runs.json").write_text(json.dumps(receipt, indent=1) + "\n")
        print("receipt written")


if __name__ == "__main__":
    main()
