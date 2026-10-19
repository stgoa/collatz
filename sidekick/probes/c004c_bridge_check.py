"""Independent check of Lean C004-c (claude/lean-lane 9f73b54): the bridge from an actual odd cycle
to its valuation word, and the integer corollary of C004 (narrow + q = 1 => the fixed point 1).

Actual cycles of the odd map T_q(n) = (3n + q) / 2^v2(3n + q) are found by direct iteration
(q = 1 and the controls q = 5, 7, 13, 61), listed from their minimum n_0 as in Lean's OddCycle.
For each cycle (word w = (a_0, ..., a_{m-1}), D = 2^A - 3^m) it checks:
  (1) the cycle identity D n_0 = q C(w) and the rotated form q C(w.rotate i) = D n_i
      (Lean's C_word_rotate is its q = 1 case);
  (2) narrow (every n_i < 2 n_0, i.e. B = 0) <=> w is a rotation of the mechanical word of
      (A, m) with gcd(A, m) = 1 or m = 1 (C004-b + R71's primitive case);
  (3) at q = 1 the only narrow cycle is the fixed point 1 (C004-c); the controls show that the
      conclusion needs q = 1: narrow cycles with m >= 2, and m = 1 cycles other than n_0 = 1;
  (4) primitivity is needed for "m = 1": the doubled fixed point (2, 2) satisfies every other
      hypothesis at q = 1.
"""
import json
import math
import sys


def C(z):
    c = 0
    for k, a in enumerate(reversed(z)):
        c = 3**k + 2**a * c
    return c


def mech(A, m, l):
    return [((j + 1) * A + l) // m - (j * A + l) // m for j in range(m)]


def step(n, q):
    x = 3 * n + q
    a = (x & -x).bit_length() - 1
    return x >> a, a


def cycles(q, N, max_steps=20000, max_val=10**40):
    found, known = [], set()
    for s in range(1, N + 1, 2):
        path, n = {}, s
        for _ in range(max_steps):
            if n in known or n > max_val:
                break
            if n in path:
                # extract the cycle through n
                cyc, x = [], n
                while True:
                    cyc.append(x)
                    x, _ = step(x, q)
                    if x == n:
                        break
                known.update(cyc)
                found.append(cyc)
                break
            path[n] = True
            n, _ = step(n, q)
    out = []
    for cyc in found:
        i0 = cyc.index(min(cyc))
        cyc = cyc[i0:] + cyc[:i0]
        word = [step(x, q)[1] for x in cyc]
        out.append((cyc, word))
    return out


def main():
    res = {"probe": "c004c_bridge_check", "lean": "claude/lean-lane 9f73b54"}
    N = {1: 200001, 5: 40001, 7: 40001, 13: 40001, 61: 40001}
    for q, bound in N.items():
        rows = []
        for cyc, w in cycles(q, bound):
            m, A = len(w), sum(w)
            Dv = 2**A - 3**m
            assert Dv * cyc[0] == q * C(w)
            for i in range(m):
                assert q * C(w[i:] + w[:i]) == Dv * cyc[i]
            narrow = max(cyc) < 2 * cyc[0]
            rot_of_mech = any(w == mech(A, m, l) for l in range(m))
            mech_ok = rot_of_mech and math.gcd(A, m) == 1
            assert narrow == mech_ok, (q, cyc, w)
            rows.append({"min": cyc[0], "m": m, "A": A, "D": Dv, "narrow": narrow})
        narrow_rows = [r for r in rows if r["narrow"]]
        if q == 1:
            assert [(r["min"], r["m"]) for r in rows] == [(1, 1)]
        res[f"q={q}"] = {"starts_up_to": bound, "cycles": len(rows),
                         "narrow": [(r["min"], r["m"], r["A"], r["D"]) for r in narrow_rows]}
    # (4) the doubled fixed point at q = 1: m = 2, word (2, 2), n_0 = n_1 = 1
    w = [2, 2]
    assert (2**4 - 3**2) * 1 == C(w) and C(w[1:] + w[:1]) == (2**4 - 3**2) * 1
    res["doubled_fixed_point"] = {"word": w, "D": 7, "C": C(w), "states": [1, 1]}
    res["result"] = "PASS"
    js = json.dumps(res, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
