"""Independent check of Lean S1-a (claude/lean-lane d69137e) in its own normalisation, on actual cycles.

Lean's OrdCycle is an integer odd cycle of 3x+q: states n_i, heights h_i, B = max h, scaled states
Z_i = 2^(B-h_i) n_i, sorted gaps Delta_r (seam 2 Z_[0] - Z_[m-1]), offsets off_r = 2^(B-h_[r]) q,
T_r = off_(r+1) - off_r (seam: 2 off_0 - off_(m-1)), e_r = floor(A/m) + [r >= m - s].
gap_closed_form: (2^A - 3^m) Delta_(r0) = sum_(i<m) 3^(m-1-i) 2^(E_i) T_(r_i), r_i = r0 + i s mod m,
E_i = e_(r_0) + ... + e_(r_(i-1)).
Actual cycles of T_q(n) = (3n + q)/2^v2 are found by iteration (q = 5, 7, 13, 61 and a few others),
kept when ordered (rank rotation, no image inversion), and checked for every start r0.
"""
import json
import sys


def step(n, q):
    x = 3 * n + q
    a = (x & -x).bit_length() - 1
    return x >> a, a


def cycles(q, N, max_steps=20000):
    found, known = [], set()
    for s0 in range(1, N + 1, 2):
        path, n = set(), s0
        for _ in range(max_steps):
            if n in known:
                break
            if n in path:
                cyc, x = [], n
                while True:
                    cyc.append(x)
                    x, _ = step(x, q)
                    if x == n:
                        break
                known.update(cyc)
                found.append(cyc)
                break
            path.add(n)
            n, _ = step(n, q)
    return found


def check(cyc, q):
    i0 = cyc.index(min(cyc))
    n = cyc[i0:] + cyc[:i0]
    m = len(n)
    if m < 2:
        return None
    a = [step(x, q)[1] for x in n]
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
    order = sorted(range(m), key=lambda i: Z[i])
    rank = {i: r for r, i in enumerate(order)}
    s = (rank[1] - rank[0]) % m
    if not all((rank[(i + 1) % m] - rank[i]) % m == s for i in range(m)):
        return False
    F = [3 * Z[i] + 2**(B - h[i]) * q for i in range(m)]
    if any(F[order[r + 1]] <= F[order[r]] for r in range(m - 1)):
        return False
    hs = [h[order[r]] for r in range(m)]
    Zs = [Z[order[r]] for r in range(m)]
    gap = [Zs[r + 1] - Zs[r] for r in range(m - 1)] + [2 * Zs[0] - Zs[m - 1]]
    off = [2**(B - hs[r]) * q for r in range(m)]
    T = [off[r + 1] - off[r] for r in range(m - 1)] + [2 * off[0] - off[m - 1]]
    e = [A // m + (1 if r >= m - s else 0) for r in range(m)]
    D = 2**A - 3**m
    for r0 in range(m):
        tot, E, r = 0, 0, r0
        for i in range(m):
            tot += 3**(m - 1 - i) * 2**E * T[r]
            E += e[r]
            r = (r + s) % m
        assert D * gap[r0] == tot, (q, n, r0)
    return True


def main():
    rows, n_ord, n_unord = [], 0, 0
    for q, N in [(5, 40001), (7, 40001), (13, 40001), (61, 40001), (11, 20001), (17, 20001),
                 (19, 20001), (23, 20001), (29, 20001), (233, 20001), (1201, 8001)]:
        for cyc in cycles(q, N):
            r = check(cyc, q)
            if r is None:
                continue
            if r:
                n_ord += 1
                rows.append((q, min(cyc), len(cyc)))
            else:
                n_unord += 1
    out = {"probe": "s1a_integer_cycle_check", "lean": "claude/lean-lane d69137e",
           "ordered_actual_cycles_checked": n_ord, "unordered_skipped": n_unord,
           "examples_(q,min,m)": rows[:12], "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
