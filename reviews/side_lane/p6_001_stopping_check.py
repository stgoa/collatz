"""Sidekick probe: independent check of main's P6-001 (S.1 stopping calibration, main 546e891), with
this branch's own maps. Nothing is imported from main.

(a) Parity lemma: for the shortcut map C_d (n/2 or (3n+d)/2), length-k parity words are a bijection
    on residues mod 2^k, and on odd residues p-1 = (#odd steps)-1 is Binomial(k-1, 1/2) exactly
    (k <= 14, d in {1,5,7,13,61}).
(b) The exact bad-class share delta = B/2^(k-1), k = 5m, B = sum_{j>=3m} binom(k-1,j), obeys
    delta <= (8/7)(16807/18432)^m for m = 9..120 (exact rationals); the least m with
    (8/7)r^m <= eps/2 is 34 for eps = 1/10 and 59 for eps = 1/100 (horizons 170 and 295).
(c) Good words half-descend: for m = 9 (k = 45) and d in {1,5,61}, random odd n >= Z = ceil(4d 3^k/2^k)
    whose 45-step shortcut word has p <= 27 satisfy C^45(n) < n/2, and the p-th odd-map iterate equals
    oddpart(C^45(n)).
(d) W5 pullback (d = 1): q = nu(3w) is 3w or (3w-1)/2 on W5, q >= 7, w -> q is injective, and
    half-descent S^j(q) <= q/2 implies 9T^j(q)+5 < 8q with T^j(q) = nu(S^j(q)) (w < 2*10^5).
(e) Sanity check of the cited fixed-k density (Borovkov-Pfeifer): for large n, the share of
    {n : C^k(n) < n/2} over a full residue system equals 2^-k sum_{j<(k-1)/log2 3} binom(k,j).
Standard library. Run without -O.
"""
from fractions import Fraction as F
from math import comb, log2
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent


def v2(n):
    return (n & -n).bit_length() - 1


def C(d, n):
    return n // 2 if n % 2 == 0 else (3*n + d) // 2


def S(d, n):
    y = 3*n + d
    return y >> v2(y)


def selected(x):
    if x % 4 != 3:
        return False
    a = v2(x + 1)
    return ((x + 1) >> a) % 4 == pow(3, a, 4)


def nu(x):
    while True:
        if x % 8 == 5:
            x = (x - 1)//4
        elif x > 1 and selected(x):
            x = (x - 1)//2
        else:
            return x


def part_a():
    checked = 0
    for d in (1, 5, 7, 13, 61):
        for k in range(1, 15):
            words, odd_p = {}, {}
            for r in range(2**k):
                n = r + 2**k * 7          # a positive representative of the class
                w, x = [], n
                for _ in range(k):
                    w.append(x % 2)
                    x = C(d, x)
                words[tuple(w)] = r
                if r % 2:
                    p = sum(w)
                    odd_p[p] = odd_p.get(p, 0) + 1
            assert len(words) == 2**k
            for p, cnt in odd_p.items():
                assert cnt == comb(k - 1, p - 1)
            checked += 1
    return checked


def part_b():
    r = F(16807, 18432)
    assert r == F(7, 6)**5 / F(4, 3)**3
    for m in range(9, 121):
        k = 5*m
        B = sum(comb(k - 1, j) for j in range(3*m, k))
        delta = F(B, 2**(k - 1))
        assert delta <= F(8, 7) * r**m
    least = {}
    for eps in (F(1, 10), F(1, 100)):
        m = 9
        while F(8, 7) * r**m > eps/2:
            m += 1
        least[str(eps)] = (m, 5*m)
    assert least == {"1/10": (34, 170), "1/100": (59, 295)}
    return least


def part_c():
    rng = random.Random(6001)
    m, k = 9, 45
    good = 0
    for d in (1, 5, 61):
        Z = -(-4*d*3**k // 2**k)
        tried = 0
        while tried < 400:
            n = rng.randrange(Z, Z * 10**6) | 1
            x, p = n, 0
            for _ in range(k):
                p += x % 2
                x = C(d, x)
            tried += 1
            if p > 3*m:
                continue
            assert 2*x < n
            y = n
            for _ in range(p):
                y = S(d, y)
            assert y == x >> v2(x) if x else y == 0
            good += 1
    return good


def part_d(limit=2*10**5):
    seen = {}
    checks = 0
    for w in range(5, limit, 8):
        q = nu(3*w)
        assert q in (3*w, (3*w - 1)//2) and q >= 7 and w < q <= 3*w
        assert (q == 3*w) == (not selected(3*w))
        assert q not in seen
        seen[q] = w
        x, t = q, q
        for j in range(1, 25):
            x = S(1, x) if x != 1 else 1
            t = nu(S(1, t)) if t != 1 else 1
            assert t == nu(x)
            if 2*x <= q:
                assert 9*t + 5 < 8*q
                checks += 1
                break
    return {"w_count": len(seen), "implications": checks}


def part_e():
    rows = []
    for k in range(6, 17):
        base = 2**40
        hits = 0
        for r in range(2**k):
            n = base + r
            x = n
            for _ in range(k):
                x = C(1, x)
            hits += 2*x < n
        pred = F(sum(comb(k, j) for j in range(k + 1) if j < (k - 1)/log2(3)), 2**k)
        assert F(hits, 2**k) == pred, (k, hits, pred)
        rows.append([k, str(pred)])
    return rows


def main():
    out = {"probe": "p6_001_stopping_check", "main": "546e891",
           "parity_bijection_cases": part_a(), "least_m": part_b(),
           "good_word_half_descents": part_c(), "w5_pullback": part_d(),
           "fixed_k_density": part_e(), "result": "PASS"}
    (HERE / "p6_001_stopping_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
