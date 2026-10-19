"""Sidekick probe: independent checks for main's V006 (experiments/viewpoints/V006/REPORT.md, main ceebb93).

(1) The quadratic theorem's worked example. With F the indicator of powers of 2 (1, 2, 4, ...), the sequences
    n -> F(t + s2(3^a n)), 0 <= a, t <= 7, are pairwise distinct on a finite prefix (prefix distinctness is a
    rigorous lower bound on the number of distinct whole sequences). The two arithmetic lemmas are also checked:
    s2(m (2^k - 1)) = k once 2^k >= m (odd m <= 999, k <= 40), and s2((2^K - 1)/3^r) = K/2 for K a multiple of
    2*3^(r-1) (r <= 6).
(2) Does the theorem's hypothesis ever hold for an actual invariant? For the 3x+d cycle labellings c_d
    (d = 5, 13, 61; genuine non-periodic invariants), test every section n -> c_d(2^K n + r), K <= 9, r odd, for
    being a function of s2(n) on n < 2^13 (necessary condition: equal digit counts give equal values).
(3) The 11-pair control z(n) = F(N_11(n)): doubling, z(8n+5) = z(2n+1), and the invariance failure z(3) != z(10).
Standard library. Run without -O.
"""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def s2(n):
    return bin(n).count("1")


def v2(n):
    return (n & -n).bit_length() - 1


def F(x):
    return 1 if x >= 1 and x & (x - 1) == 0 else 0


def part1():
    for m in range(1, 1000, 2):
        for k in range(1, 41):
            if 2**k >= m:
                assert s2(m * (2**k - 1)) == k, (m, k)
    for r in range(1, 7):
        per = 2 * 3**(r - 1)
        for mult in range(1, 4):
            K = per * mult
            assert (2**K - 1) % 3**r == 0 and s2((2**K - 1) // 3**r) == K // 2, (r, K)
    W = 400
    seqs = {}
    for a in range(8):
        for t in range(8):
            seqs[(a, t)] = tuple(F(t + s2(3**a * n)) for n in range(W))
    distinct = len(set(seqs.values()))
    assert distinct == 64, distinct
    return {"pairs_a_t_le_7": 64, "distinct_on_prefix_400": distinct}


def cycle_label(d, N):
    lab = {}
    def T(x):
        y = 3*x + d
        return y >> v2(y)
    out = [0]*(N + 1)
    for n in range(1, N + 1):
        x = n >> v2(n)
        path, seen = [], set()
        while x not in lab and x not in seen:
            seen.add(x)
            path.append(x)
            x = T(x)
        L = lab[x] if x in lab else min(path[path.index(x):])
        for y in path:
            lab[y] = L
        out[n] = lab[n >> v2(n)]
    return out


def part2():
    res = {}
    B = 2**13
    for d in (5, 13, 61):
        c = cycle_label(d, 2**9 * B + 2**9)
        found = []
        for K in range(1, 10):
            for r in range(1, 2**K, 2):
                vals = {}
                ok = True
                for n in range(B):
                    k = s2(n)
                    v = c[2**K * n + r]
                    if vals.setdefault(k, v) != v:
                        ok = False
                        break
                if ok and len(set(vals.values())) > 1:
                    found.append((K, r))
        res[f"d={d}"] = {"nonconstant_digit_count_sections_found": found[:5], "count": len(found)}
    return res


def part3():
    def N11(n):
        b = bin(n)[2:]
        return sum(1 for i in range(len(b) - 1) if b[i] == b[i + 1] == "1")
    z = lambda n: F(N11(n))
    for n in range(1, 5000):
        assert z(2*n) == z(n) and z(8*n + 5) == z(2*n + 1)
    return {"z(3)": z(3), "z(10)": z(10), "invariance_fails_at_3": z(3) != z(10)}


def main():
    out = {"probe": "v006_quadratic_check", "main": "ceebb93", "quadratic_example": part1(),
           "digit_count_sections_in_controls": part2(), "eleven_pair_control": part3(), "result": "PASS"}
    (HERE / "v006_quadratic_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
