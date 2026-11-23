#!/usr/bin/env python3
"""Exploration for few-mismatch-rotation-orders-sweep (not a certificate; never run by CI).

Large rotation order: a model with explicit heights. Standard library only, floating point. It supports no
proved claim.

Everything is divided by the full period m; time t runs over (0, 1] and the cycle minimum is at time 0.
The word has a bulk of constant excess density beta (letters average 1 + beta) and finitely many special
letters placed on orbit segments {q + i h} of the rotation number h: "visible" ones with an excess that is a
positive fraction of m, and "small" ones whose excess is negligible. The last letter (time 1) is visible and
brings the height back to 0. Heights: Z(t) = (alpha - 1 - beta) t minus the visible excesses before t.

For each multiple j of the rotation, the mismatches are the positions whose label differs from the label j
steps along the orbit. Between consecutive mismatches the paired quotient g satisfies
    G = log2|g| / m = (higher of the two starting heights) - (2-adic total of the run) >= 0,
which is a row. At each mismatch the two relations between consecutive quotients are read in three-term and
four-term form, as in half-period-six-mismatch-local-law; the margin of a relation is
(log of its largest term) - (sum of logs of the parts coprime to 6), divided by m.

A configuration is feasible if all rows hold for j <= J. For a feasible configuration the script reports the
best margin over the relations of the shifts j <= 3: a positive value means that some relation has a small
product, with that many bits per unit of m to spare.

    python3 areas/cycles/results/few-mismatch-rotation-orders-sweep/explore_large_order_model.py [--write-receipt]
    python3 areas/cycles/results/few-mismatch-rotation-orders-sweep/explore_large_order_model.py --orders 3 30 [--write-receipt]

The second form runs the same explicit model with an exact rational rotation a/M for every order in the range
(indices read modulo M, rows for every nonzero multiple), for the one family that is feasible, and merges its
entries into the receipt. It assumes a bulk of constant density, which Model 1 does not.
"""
import json
import math
import sys
from pathlib import Path

AL = math.log2(3.0)
A1 = AL - 1.0
HERE = Path(__file__).resolve().parent


def frac1(x):
    f = x - math.floor(x)
    return 1.0 if f < 1e-12 else f


def analyse(h, columns, amps, beta=0.0, J=10, Jcrit=3, order=None, tol=1e-9):
    """columns: list of (base time, {index: label}). Column 0 has base 1.0 and its index 0 carries the label "K";
    all letters labelled "K" share the excess that remains. amps gives the excess of the other visible labels;
    labels absent from amps are small. With order = M the indices are read modulo M (exact rational h = a/M)."""
    gamma = A1 - beta
    if gamma <= 0:
        return False, None
    red = (lambda i: i % order) if order else (lambda i: i)
    lab = {}
    for o, (base, d) in enumerate(columns):
        for i, l in d.items():
            lab[(o, red(i))] = l
    label = lambda o, i: lab.get((o, red(i)), "1")
    tm = lambda o, i: frac1(columns[o][0] + red(i) * h)
    other = sum(amps.get(l, 0.0) for l in lab.values() if l != "K")
    amp_k = (gamma - other) / sum(1 for l in lab.values() if l == "K")
    if amp_k <= tol:
        return False, None
    amp = lambda l: amp_k if l == "K" else amps.get(l, 0.0)
    specials = sorted((tm(o, i), l) for (o, i), l in lab.items())

    def after(t, l):
        return gamma * t - sum(amp(l2) for (ts, l2) in specials if ts < t - 1e-12) - amp(l)

    if any(after(ts, l) < -tol for ts, l in specials):
        return False, None
    best = -1e9
    for j in range(1, J + 1):
        if order and j % order == 0:
            continue
        cand = set()
        for (o, i) in lab:
            cand.add((o, i))
            cand.add((o, red(i - j)))
        cuts = sorted((tm(o, i), o, i, label(o, i), label(o, i + j)) for (o, i) in cand if label(o, i) != label(o, i + j))
        if not cuts:
            return False, None
        runs = []
        for a in range(len(cuts)):
            tv, o, i, la, lb = cuts[a]
            tu, ou, iu, lau, lbu = cuts[a - 1]
            wraps = not (a > 0 and tv > tu)
            ell = 1.0 if len(cuts) == 1 else (tv - tu + (1.0 if wraps else 0.0))
            if wraps:
                inside = sum(amp(l) for (ts, l) in specials if ts > tu + 1e-12 or ts < tv - 1e-12)
            else:
                inside = sum(amp(l) for (ts, l) in specials if tu + 1e-12 < ts < tv - 1e-12)
            total = (1 + beta) * ell + inside + min(amp(la), amp(lb))
            g = max(after(tu, lau), after(tm(ou, iu + j), lbu)) - total
            if g < -tol:
                return False, None
            runs.append((ell, total, g))
        if j <= Jcrit:
            for a in range(len(cuts)):
                tv, o, i, la, lb = cuts[a]
                ell, total, g = runs[a]
                _, total_n, g_n = runs[(a + 1) % len(cuts)]
                low = min(amp(la), amp(lb))
                nu, nup = amp(la) - low, amp(lb) - low
                p = nu + nup
                t1 = AL * ell + g
                for z_xi, cexp in ((after(tv, la), nup), (after(tm(o, i + j), lb), nu)):
                    t2 = cexp + total_n + g_n
                    best = max(best, max(t1, t2) - (g + g_n + p + z_xi), max(t1, t2, p + z_xi) - (g + g_n + 2 * z_xi))
    return True, best


def comb(start, length, label, step=1):
    return {start + step * k: label for k in range(length)}


def merge(*ds):
    out = {}
    for d in ds:
        out.update(d)
    return out


def families(limit):
    """Five-mismatch patterns. Each item: name, whether a second orbit is used, builder(q, gamma) -> (columns, amps)."""
    for n in range(0, limit + 1):
        for dr in ((1, -1) if n else (1,)):
            for n2 in range(1, limit + 1):
                yield ("A giant with adjacent small run, separate small run", True,
                       lambda q, gm, n=n, dr=dr, n2=n2: ([(1.0, merge({0: "K"}, comb(dr, n, "s", dr))), (q, comb(0, n2, "r"))], {}))
    for a in range(1, limit + 1):
        for b in range(1, limit + 1):
            yield ("B giant alone, separate run with two small letters", True,
                   lambda q, gm, a=a, b=b: ([(1.0, {0: "K"}), (q, merge(comb(0, a, "s"), comb(a, b, "r")))], {}))
    for dr in (1, -1):
        for n2 in range(1, limit):
            for fr in (0.1, 0.25, 0.4, 0.5, 0.6, 0.75, 0.9):
                yield ("C two adjacent visible letters, separate small run", True,
                       lambda q, gm, dr=dr, n2=n2, fr=fr: ([(1.0, {0: "K", dr: "V"}), (q, comb(0, n2, "r"))], {"V": fr * gm}))
    for n in range(1, limit):
        for dr in (1, -1):
            for kv in range(1, 4):
                for fr in (0.1, 0.25, 0.5, 0.75):
                    yield ("C2 giant with adjacent small run, separate run of visible letters", True,
                           lambda q, gm, n=n, dr=dr, kv=kv, fr=fr: ([(1.0, merge({0: "K"}, comb(dr, n, "s", dr))), (q, comb(0, kv, "V"))],
                                                                    {"V": fr * gm / kv}))
    for k in range(2, 5):
        for a in range(1, 5):
            for b in range(1, 5):
                yield ("D run of equal visible letters, separate run with two small letters", True,
                       lambda q, gm, k=k, a=a, b=b: ([(1.0, comb(0, k, "K", -1)), (q, merge(comb(0, a, "s"), comb(a, b, "r")))], {}))
    for a in range(1, limit + 1):
        for gap in range(1, limit + 1):
            for b in range(1, limit + 1):
                for dr in (1, -1):
                    yield ("E one orbit: giant, small run, gap, small run", False,
                           lambda q, gm, a=a, gap=gap, b=b, dr=dr: ([(1.0, merge({0: "K"}, comb(dr, a, "s", dr),
                                                                                comb(dr * (a + gap + 1), b, "r", dr)))], {}))
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                for dr in (1, -1):
                    yield ("E3 one orbit: giant followed by three different small runs", False,
                           lambda q, gm, a=a, b=b, c=c, dr=dr: ([(1.0, merge({0: "K"}, comb(dr, a, "s", dr), comb(dr * (a + 1), b, "r", dr),
                                                                             comb(dr * (a + b + 1), c, "u", dr)))], {}))


def scan(nh, nq, limit, betas, J):
    out = {}
    for beta in betas:
        gamma = A1 - beta
        for name, uses_q, build in families(limit):
            key = f"{name}; beta={beta}; J={J}"
            r = out.setdefault(key, {"tested": 0, "feasible": 0, "weakest_best_margin": None})
            for ih in range(1, nh):
                h = 0.5 * ih / nh
                for iq in (range(nq) if uses_q else range(1)):
                    cols, amps = build((iq + 0.37) / nq, gamma)
                    ok, best = analyse(h, cols, amps, beta=beta, J=J)
                    r["tested"] += 1
                    if ok:
                        r["feasible"] += 1
                        if r["weakest_best_margin"] is None or best < r["weakest_best_margin"]:
                            r["weakest_best_margin"] = round(best, 4)
    return out


def escalate(nh, nq, limit, levels):
    """Family A only: the feasible grid points for the first level, re-tested with more multiples."""
    points = []
    for n in range(0, limit + 1):
        for dr in ((1, -1) if n else (1,)):
            for n2 in range(1, limit + 1):
                for ih in range(1, nh):
                    for iq in range(nq):
                        h, q = 0.5 * ih / nh, (iq + 0.37) / nq
                        cols = [(1.0, merge({0: "K"}, comb(dr, n, "s", dr))), (q, comb(0, n2, "r"))]
                        ok, best = analyse(h, cols, {}, J=levels[0])
                        if ok:
                            points.append((h, cols, best))
    out = {f"J={levels[0]}": {"feasible": len(points),
                              "weakest_best_margin": round(min(p[2] for p in points), 4) if points else None}}
    for J in levels[1:]:
        kept = []
        for h, cols, _ in points:
            ok, best = analyse(h, cols, {}, J=J)
            if ok:
                kept.append((h, cols, best))
        points = kept
        out[f"J={J}"] = {"feasible": len(points),
                         "weakest_best_margin": round(min(p[2] for p in points), 4) if points else None,
                         "rotation_numbers": sorted({round(p[0], 4) for p in points})[:40]}
    return out


def exact_orders(lo, hi, nq):
    """Family A with an exact rational rotation a/M, indices modulo M, rows for every nonzero multiple."""
    out = {}
    for order in range(lo, hi + 1):
        feasible = 0
        weakest = None
        numerators = set()
        limit = min(8, order - 2)
        for a in range(1, order // 2 + 1):
            if math.gcd(a, order) != 1:
                continue
            for n in range(0, limit + 1):
                for dr in ((1, -1) if n else (1,)):
                    for n2 in range(1, limit + 1):
                        for iq in range(nq):
                            cols = [(1.0, merge({0: "K"}, comb(dr, n, "s", dr))), ((iq + 0.37) / nq, comb(0, n2, "r"))]
                            ok, best = analyse(a / order, cols, {}, J=order // 2, Jcrit=min(3, order // 2), order=order)
                            if ok:
                                feasible += 1
                                numerators.add(a)
                                weakest = best if weakest is None else min(weakest, best)
        out[f"M={order}"] = {"feasible": feasible, "numerators": sorted(numerators),
                             "weakest_best_margin": None if weakest is None else round(weakest, 4)}
        print(f"M={order}: {out[f'M={order}']}", flush=True)
    return out


def main():
    if "--orders" in sys.argv:
        i = sys.argv.index("--orders")
        res = exact_orders(int(sys.argv[i + 1]), int(sys.argv[i + 2]), 300)
        if "--write-receipt" in sys.argv:
            path = HERE / "explore_large_order_model.json"
            data = json.loads(path.read_text()) if path.exists() else {}
            data.setdefault("family_A_exact_orders", {}).update(res)
            path.write_text(json.dumps(data, indent=1) + "\n")
            print("receipt updated")
        return
    receipt = {
        "validation_order_7": {
            "note": "the order-7 survivor of explore_rotation_orders.py, with indices read modulo 7; "
                    "its margin there is 2.354 per period, that is 0.3363 per unit of m",
            "result": analyse(3 / 7, [(1.0, {0: "K", 1: "s", 2: "s", 3: "s"}), ((1 + 0.524) / 7, {0: "r"})], {},
                              order=7, J=6, Jcrit=6),
        },
        "five_mismatch_families": scan(120, 120, 7, [0.0, 0.05, 0.15], 10),
        "family_A_with_more_multiples": escalate(200, 200, 8, [8, 12, 16, 24, 32, 48]),
    }
    print(json.dumps(receipt, indent=1))
    if "--write-receipt" in sys.argv:
        path = HERE / "explore_large_order_model.json"
        old = json.loads(path.read_text()) if path.exists() else {}
        if "family_A_exact_orders" in old:
            receipt["family_A_exact_orders"] = old["family_A_exact_orders"]
        path.write_text(json.dumps(receipt, indent=1) + "\n")
        print("receipt written")


if __name__ == "__main__":
    main()
