"""Independent check of Lean R71-d and C006-b (claude/lean-lane 3faa040).

R71-d: for k >= 3 and A = bit length of 3^k (3^k < 2^A < 2*3^k), den(mech A k l) > 1 for every phase;
       den = 1 exactly at k = 1, 2.
C006-b: on the actual ordered 3x+q cycles of s1a_integer_cycle_check.py, for every rank r0 and every
       zero-forcing stretch of length t starting at r0 (T = 0 at the first t orbit positions), with
       e_run = E(r0, t) the exponent sum, check 2^(e_run) divides the gap at r0 (so <= it) and
       2^(e_run) < 2^B n_0; count how often e_run > t (the refinement over 2^t is strict).
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402
from r71c_state_bound_check import C, mech  # noqa: E402


def main():
    den_one = []
    for k in range(1, 81):
        A = (3**k).bit_length()
        D = 2**A - 3**k
        for l in range(k):
            c = C(mech(A, k, l))
            den = D // math.gcd(c, D)
            if den == 1:
                den_one.append((k, l))
            if k >= 3:
                assert den > 1
    assert sorted(set(k for k, _ in den_one)) == [1, 2]

    n_runs = n_strict = n_cyc = 0
    for q, N in [(5, 40001), (7, 40001), (13, 40001), (61, 40001), (11, 20001), (17, 20001),
                 (19, 20001), (23, 20001), (29, 20001), (233, 20001), (1201, 8001)]:
        for cyc in cycles(q, N):
            i0 = cyc.index(min(cyc))
            n = cyc[i0:] + cyc[:i0]
            m = len(n)
            if m < 2:
                continue
            a = [step(x, q)[1] for x in n]
            A = sum(a)
            h = []
            for x in n:
                kk = 0
                while x >= 2**(kk + 1) * n[0]:
                    kk += 1
                h.append(kk)
            B = max(h)
            Z = [2**(B - t) * x for t, x in zip(h, n)]
            order = sorted(range(m), key=lambda i: Z[i])
            rank = {i: r for r, i in enumerate(order)}
            s = (rank[1] - rank[0]) % m
            if not all((rank[(i + 1) % m] - rank[i]) % m == s for i in range(m)):
                continue
            F = [3 * Z[i] + 2**(B - h[i]) * q for i in range(m)]
            if any(F[order[r + 1]] <= F[order[r]] for r in range(m - 1)):
                continue
            hs = [h[order[r]] for r in range(m)]
            Zs = [Z[order[r]] for r in range(m)]
            gap = [Zs[r + 1] - Zs[r] for r in range(m - 1)] + [2 * Zs[0] - Zs[m - 1]]
            off = [2**(B - hs[r]) * q for r in range(m)]
            T = [off[r + 1] - off[r] for r in range(m - 1)] + [2 * off[0] - off[m - 1]]
            e = [A // m + (1 if r >= m - s else 0) for r in range(m)]
            n_cyc += 1
            for r0 in range(m):
                E, r, t = 0, r0, 0
                while t < m and T[r] == 0:
                    E += e[r]
                    t += 1
                    r = (r + s) % m
                    assert gap[r0] % 2**E == 0 and 2**E <= gap[r0] and 2**E < 2**B * n[0]
                    n_runs += 1
                    n_strict += E > t
    out = {"probe": "c006b_erun_check", "lean": "claude/lean-lane 3faa040",
           "R71d_k_range": "3..80, every phase den > 1", "den_one_at_k": [1, 2],
           "ordered_cycles": n_cyc, "zero_forcing_stretches": n_runs,
           "stretches_with_e_run_gt_t": n_strict, "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
