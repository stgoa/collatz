"""S2 exploration: the run-compressed cycle of an ordered cycle (Lean normalisation, integer units).

For an ordered reduced 3x+q cycle (sorted scaled states Z = 2^(B-h) n, gaps Delta_r with seam,
forcing T_r = q (2^(B-h_[r+1]) - 2^(B-h_[r])) and seam T = q (2^(B+1) - 2^(B-h_[m-1])), rank shift s,
exponents e_r = q' + [r >= m-s]):
  run starts r_k = ranks whose orbit predecessor is forced; t_k = number of unforced steps after r_k;
  E_k = exponent total over those t_k steps; f_k = the forced rank ending the run (T_(f_k) != 0).
  u_k := Delta_(r_k) / 2^(E_k)  (an integer by the run lemma), v_k := v2(Delta_(r_k)) - E_k >= 0.
Checks: identity 2^(e_(f_k) + E_(k+1)) u_(k+1) = 3^(t_k+1) u_k + T_(f_k); product bookkeeping
sum (e_f + E) = A, sum (t + 1) = m. Statistics: v_k pattern (interior-ending vs seam-ending runs), by band B
and q; spread max u / min u; J. Sources: the actual ordered 3x+q cycles and the rational ordered cycles
(m <= 9, letters 1..4) through their reduced integer cycles (n_i = C_i/g, q = D/g).
"""
import itertools
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402
from jterm_gap_check import CD, rot, is_primitive  # noqa: E402


def v2(x):
    x = abs(x)
    return (x & -x).bit_length() - 1 if x else 10**9


def ordered_integer(n, a, q):
    """n listed from its minimum, a its letters; return run data or None if not ordered."""
    m = len(n)
    if m < 2:
        return None
    A = sum(a)
    L = n[0]
    h = []
    for x in n:
        k = 0
        while x >= 2**(k + 1) * L:
            k += 1
        h.append(k)
    B = max(h)
    Z = [2**(B - t) * x for t, x in zip(h, n)]
    if len(set(Z)) < m:
        return None
    order = sorted(range(m), key=lambda i: Z[i])
    rank = {i: r for r, i in enumerate(order)}
    s = (rank[1] - rank[0]) % m
    if not all((rank[(i + 1) % m] - rank[i]) % m == s for i in range(m)):
        return None
    F = [3 * Z[i] + 2**(B - h[i]) * q for i in range(m)]
    if any(F[order[r + 1]] <= F[order[r]] for r in range(m - 1)):
        return None
    hs = [h[order[r]] for r in range(m)]
    Zs = [Z[order[r]] for r in range(m)]
    gap = [Zs[r + 1] - Zs[r] for r in range(m - 1)] + [2 * Zs[0] - Zs[m - 1]]
    off = [2**(B - hs[r]) * q for r in range(m)]
    T = [off[r + 1] - off[r] for r in range(m - 1)] + [2 * off[0] - off[m - 1]]
    qp = A // m
    e = [qp + (1 if r >= m - s else 0) for r in range(m)]
    for r in range(m):
        assert 2**e[r] * gap[(r + s) % m] == 3 * gap[r] + T[r]
    forced = [r for r in range(m) if T[r] != 0]
    J = len(forced)
    # run starts in orbit order, starting from the image of the seam
    runs = []
    r0 = (m - 1 + s) % m
    r = r0
    while True:
        start, t, E = r, 0, 0
        while T[r] == 0:
            E += e[r]
            t += 1
            r = (r + s) % m
        f = r
        runs.append(dict(start=start, t=t, E=E, f=f, ef=e[f], T=T[f], seam=(f == m - 1)))
        r = (r + s) % m
        if r == r0:
            break
    assert len(runs) == J
    for R in runs:
        g = gap[R['start']]
        assert g % 2**R['E'] == 0
        R['u'] = g // 2**R['E']
        R['v'] = v2(g) - R['E']
    for k, R in enumerate(runs):
        Rn = runs[(k + 1) % J]
        assert 2**(R['ef'] + Rn['E']) * Rn['u'] == 3**(R['t'] + 1) * R['u'] + R['T']
    assert sum(R['ef'] + R['E'] for R in runs) == A and sum(R['t'] + 1 for R in runs) == m
    return dict(m=m, A=A, B=B, q=q, J=J, runs=runs, L=L)


def level2_order(n, a, q):
    """The gap cycle of an ordered cycle, in orbit order from rank 0, normalised by its own minimum:
    return 'ordered' / 'unordered' / 'tied' (rank rotation test) and its band."""
    m = len(n)
    L = n[0]
    h = []
    for x in n:
        k = 0
        while x >= 2**(k + 1) * L:
            k += 1
        h.append(k)
    B = max(h)
    Z = [2**(B - t) * x for t, x in zip(h, n)]
    order = sorted(range(m), key=lambda i: Z[i])
    rank = {i: r for r, i in enumerate(order)}
    s = (rank[1] - rank[0]) % m
    Zs = [Z[order[r]] for r in range(m)]
    gap = [Zs[r + 1] - Zs[r] for r in range(m - 1)] + [2 * Zs[0] - Zs[m - 1]]
    seq = [gap[(k * s) % m] for k in range(m)]
    i0 = seq.index(min(seq))
    seq = seq[i0:] + seq[:i0]
    Lg = seq[0]
    hg = []
    for x in seq:
        k = 0
        while x >= 2**(k + 1) * Lg:
            k += 1
        hg.append(k)
    zg = [x / 2**t for x, t in zip(seq, hg)]
    if len(set(zg)) < m:
        return 'tied', max(hg)
    o2 = sorted(range(m), key=lambda i: zg[i])
    rk = {i: r for r, i in enumerate(o2)}
    s2 = (rk[1] - rk[0]) % m
    ok = all((rk[(i + 1) % m] - rk[i]) % m == s2 for i in range(m))
    return ('ordered' if ok else 'unordered'), max(hg)


def main():
    stats = defaultdict(Counter)
    spreads = defaultdict(list)
    samples = []
    def record(d, src):
        B = d['B']
        for R in d['runs']:
            kind = 'seam' if R['seam'] else 'interior'
            stats[(src, B, kind)]['runs'] += 1
            stats[(src, B, kind)]['u_odd'] += R['u'] % 2
        us = [R['u'] for R in d['runs']]
        spreads[(src, B)].append(max(us) / min(us))
        if src == 'actual' and len(samples) < 6:
            samples.append(dict(q=d['q'], L=d['L'], m=d['m'], B=B, J=d['J'],
                                u=[R['u'] for R in d['runs']], t=[R['t'] for R in d['runs']],
                                T=[R['T'] for R in d['runs']], v=[R['v'] for R in d['runs']]))
    lvl2 = Counter()
    max_band2 = 0
    n_act = 0
    for q, N in [(5, 40001), (7, 40001), (13, 40001), (61, 40001), (11, 20001), (17, 20001),
                 (19, 20001), (23, 20001), (29, 20001), (233, 20001), (1201, 8001)]:
        for cyc in cycles(q, N):
            i0 = cyc.index(min(cyc))
            n = cyc[i0:] + cyc[:i0]
            a = [step(x, q)[1] for x in n]
            d = ordered_integer(n, a, q)
            if d is None:
                continue
            record(d, 'actual')
            if len(n) >= 3:
                o, bg = level2_order(n, a, q)
                lvl2[('actual', o)] += 1
                max_band2 = max(max_band2, bg)
            n_act += 1
    n_rat = 0
    for m in range(2, 10):
        for z in itertools.product(range(1, 5), repeat=m):
            z = list(z)
            C, D = CD(z)
            if D <= 0 or not is_primitive(z):
                continue
            Cs = [CD(rot(z, i))[0] for i in range(m)]
            if min(Cs) != Cs[0]:
                continue
            g = math.gcd(Cs[0], D)
            n = [c // g for c in Cs]
            d = ordered_integer(n, z, D // g)
            if d is None:
                continue
            record(d, 'rational')
            if m >= 3:
                o, bg = level2_order(n, z, D // g)
                lvl2[('rational', o)] += 1
                max_band2 = max(max_band2, bg)
            n_rat += 1
    out = {"probe": "s2_ucycle_explore", "actual_ordered": n_act, "rational_ordered": n_rat,
           "u_odd_by_(source,B,run_kind)": {f"{k[0]},B={k[1]},{k[2]}": dict(v) for k, v in sorted(stats.items())},
           "u_spread_max_over_min": {f"{k[0]},B={k[1]}": [round(min(v), 2), round(max(v), 2)] for k, v in sorted(spreads.items())},
           "level2_gap_cycle_order_(m>=3)": {f"{k[0]},{k[1]}": v for k, v in sorted(lvl2.items())},
           "level2_max_band": max_band2,
           "samples_actual": samples, "result": "PASS (identities)"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
