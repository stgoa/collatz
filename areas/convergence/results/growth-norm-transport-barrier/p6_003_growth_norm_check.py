"""Sidekick probe: independent check of main's P6-003 (S.2 barrier to first-half growth-norm contraction,
main 2e619a2), with this branch's own maps. Nothing is imported from main.

(1) Theorem 2's four paths: for d in {1,5,7,13,61} and every y = 5d (mod 18) up to 10^5, the sources
    n3=(8y-d)/3, n5=(32y-d)/3, n23=(32y-7d)/9, n15=(64y-5d)/9 are odd integers with exact valuation words
    (3), (5), (2,3), (1,5), first-half descent to y at times 1, 1, 2, 2, and all 4 families distinct.
(2) K(7/8) > 241/240 through the four integer inequalities (9), and K(alpha) evaluated on a grid.
(3) The exact count (5): #{y in A_(alpha,d) : y <= X} = floor(m^alpha), m = floor((X-5d)/18), for
    alpha = p/q in {1/2, 2/3, 7/8} and all X up to 2*10^4 (integer-root arithmetic).
(4) Theorem 3's mass bound: a dynamic program over valuation words gives the exact first-crossing mass
    p_B (s_i > 1/2 before the last arrow, s_l < 1/2 at it, total valuation <= B); for m = 9..15 and
    B = 5m + L - 1 <= 90 it satisfies p_B >= 1 - delta_m - 2^-L; p_B exceeds 2^(alpha-1) for alpha = 0.9
    at a modest B; and the identity 3^-l s^alpha = 2^-A s^(alpha-1) holds termwise.
Standard library. Run without -O.
"""
from fractions import Fraction as F
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def v2(n):
    return (n & -n).bit_length() - 1


def Sv(d, n):
    y = 3*n + d
    e = v2(y)
    return y >> e, e


def first_half(d, n):
    x, j = n, 0
    while True:
        x, _ = Sv(d, x)
        j += 1
        if 2*x <= n:
            return j, x
        assert j < 10**4


def part1():
    cnt = 0
    for d in (1, 5, 7, 13, 61):
        for y in range(5*d % 18 or 18, 10**5, 18):
            if y % 18 != (5*d) % 18 or y <= d:
                continue
            fams = {}
            for name, num, den, word in (("n3", 8*y - d, 3, [3]), ("n5", 32*y - d, 3, [5]),
                                         ("n23", 32*y - 7*d, 9, [2, 3]), ("n15", 64*y - 5*d, 9, [1, 5])):
                assert num % den == 0
                n = num // den
                assert n % 2 == 1 and n > 1
                x, w = n, []
                for _ in word:
                    x, e = Sv(d, x)
                    w.append(e)
                assert w == word and x == y
                assert first_half(d, n) == (len(word), y)
                fams[name] = n
            assert len(set(fams.values())) == 4
            cnt += 1
    return cnt


def part2():
    assert 3**7 * 5**8 > 2**29 and 3**7 > 2**11 and 3**14 > 8 * 5**8 and 3**22 > 2**34
    assert F(2, 5) + F(1, 8) + F(5, 16) + F(1, 6) == F(241, 240)
    K = lambda a: (3/8)**a + (3/32)**a + (9/32)**a + (9/64)**a
    return {str(a): round(K(a), 5) for a in (0.5, 0.75, 0.875, 0.9, 0.95)}


def iroot_floor(m, p, q):
    """floor(m^(p/q)) exactly: largest r with r^q <= m^p."""
    target = m**p
    lo, hi = 0, 1
    while hi**q <= target:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi)//2
        if mid**q <= target:
            lo = mid
        else:
            hi = mid
    return lo


def part3():
    checks = 0
    for (p, q) in ((1, 2), (2, 3), (7, 8)):
        for d in (1, 5):
            A = []
            j = 1
            while True:
                c = iroot_floor(j**q, 1, p)            # floor(j^(q/p)); adjust to ceil
                while c**p < j**q:
                    c += 1
                v = 18*c + 5*d
                if v > 2*10**4:
                    break
                A.append(v)
                j += 1
            assert all(b > a for a, b in zip(A, A[1:]))
            idx = 0
            for X in range(1, 2*10**4 + 1):
                while idx < len(A) and A[idx] <= X:
                    idx += 1
                m = max(0, (X - 5*d)//18)
                assert idx == iroot_floor(m, p, q)
                checks += 1
    return checks


def first_crossing_mass(B):
    """Exact p_B = sum over first-crossing words with total valuation <= B of 2^-A (Fractions).
    State: (length i, total A) with 3^i/2^A > 1/2 for all prefixes so far (i >= 1)."""
    total = F(0)
    frontier = {(0, 0): F(1)}           # empty word, weight 1 (bit 0 fixed)
    while frontier:
        nxt = {}
        for (i, A), wt in frontier.items():
            for a in range(1, B - A + 1):
                i2, A2 = i + 1, A + a
                w2 = wt / 2**a
                # s = 3^i2 / 2^A2 compared with 1/2:  2*3^i2 vs 2^A2
                if 2 * 3**i2 < 2**A2:
                    total += w2
                else:
                    nxt[(i2, A2)] = nxt.get((i2, A2), F(0)) + w2
        frontier = nxt
    return total


def part4():
    r = F(16807, 18432)
    rows = []
    p90 = first_crossing_mass(90)
    for m in range(9, 16):
        L = 90 - 5*m + 1
        if L < 1:
            continue
        B = 5*m + L - 1
        pB = p90
        bound = 1 - F(8, 7)*r**m - F(1, 2**L)
        assert pB >= bound
        rows.append([m, L, B, float(pB), float(bound)])
    # the identity behind (15), on a few words
    for l, A in ((1, 3), (2, 5), (5, 12)):
        s = F(3**l, 2**A)
        for alpha in (F(1, 2), F(9, 10)):
            lhs = F(1, 3**l) * float(s)**float(alpha)
            rhs = F(1, 2**A) * float(s)**float(alpha - 1)
            assert abs(float(lhs) - float(rhs)) < 1e-12
    # p_B passes 2^(alpha-1) for alpha = 0.9 at a modest B
    B = 10
    while float(first_crossing_mass(B)) <= 2**(0.9 - 1):
        B += 2
    return {"rows": rows, "B_for_alpha_0.9": B}


def main():
    out = {"probe": "p6_003_growth_norm_check", "main": "2e619a2", "four_path_targets": part1(),
           "K_alpha": part2(), "count_formula_checks": part3(), "first_crossing": part4(),
           "result": "PASS"}
    (HERE / "p6_003_growth_norm_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
