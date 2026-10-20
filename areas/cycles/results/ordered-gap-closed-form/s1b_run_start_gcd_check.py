"""Independent check of Lean S1-b (claude/lean-lane 82bd72f) on actual reduced 3x+q cycles.

For each ordered actual cycle (same search and normalisation as s1a_integer_cycle_check.py):
run starts are the ranks r whose orbit predecessor (r - s mod m) is forced (T != 0); check
gcd(q, gaps at run starts) = 1 (run_start_gaps_coprime), that every rank is reached from a run start
along a zero-forcing run, and that sum of all gaps = 2^B n_0. In the word normalisation
(g = gcd(C_w, D_w), D_w = g q, G_r = g gap_r) check gcd(D_w, run-start G) = g, and count the
cycles where a single run-start gap shares a factor with q (so the joint statement is needed).
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402


def data(cyc, q):
    i0 = cyc.index(min(cyc))
    n = cyc[i0:] + cyc[:i0]
    m = len(n)
    if m < 2:
        return None
    a = [step(x, q)[1] for x in n]
    A = sum(a)
    h = []
    for x in n:
        k = 0
        while x >= 2**(k + 1) * n[0]:
            k += 1
        h.append(k)
    B = max(h)
    Z = [2**(B - t) * x for t, x in zip(h, n)]
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
    return m, s, B, n, gap, T


def main():
    n_cyc = n_single_shares = n_g_gt_1 = 0
    for q, N in [(5, 40001), (7, 40001), (13, 40001), (61, 40001), (11, 20001), (17, 20001),
                 (19, 20001), (23, 20001), (29, 20001), (233, 20001), (1201, 8001)]:
        for cyc in cycles(q, N):
            d = data(cyc, q)
            if d is None:
                continue
            m, s, B, n, gap, T = d
            assert math.gcd(q, n[0]) == 1 and q % 2 == 1
            assert sum(gap) == 2**B * n[0]
            starts = [r for r in range(m) if T[(r - s) % m] != 0]
            g = q
            for r in starts:
                g = math.gcd(g, gap[r])
            assert g == 1, (q, n[0], starts)
            reached = set()
            for r0 in starts:
                r = r0
                while True:
                    reached.add(r)
                    if T[r] != 0:
                        break
                    r = (r + s) % m
            assert reached == set(range(m))
            # word normalisation: g = gcd(C_w, D_w), D = g q, G_r = g * gap_r
            w = [step(x, q)[1] for x in n]
            Cw = 0
            for k, a in enumerate(reversed(w)):
                Cw = 3**k + 2**a * Cw
            Dw = 2**sum(w) - 3**len(w)
            gw = math.gcd(Cw, Dw)
            assert Dw == gw * q
            gG = Dw
            for r in starts:
                gG = math.gcd(gG, gw * gap[r])
            assert gG == gw
            if any(math.gcd(q, gap[r]) > 1 for r in starts):
                n_single_shares += 1
            if gw > 1:
                n_g_gt_1 += 1
            n_cyc += 1
    out = {"probe": "s1b_run_start_gcd_check", "lean": "claude/lean-lane 82bd72f",
           "ordered_reduced_cycles": n_cyc,
           "word_normalisation_gcd(D, run-start G) == gcd(C, D)": n_cyc,
           "cycles_with_g_gt_1": n_g_gt_1,
           "cycles_where_a_single_run_start_gap_shares_a_factor_with_q": n_single_shares,
           "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
