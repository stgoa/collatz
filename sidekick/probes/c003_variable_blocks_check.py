"""Sidekick probe: independent checks of main's C003 (experiments/cycle_spectrum/C003, main 7270d95).

(1) Effective contracting theorem (Section 2): u, v nonempty positive words with D_u, D_v > 0 and K != 0; let
    Q* = max(2^sum(u), 2^sum(v)), m* = max(len u, len v). If a block attaining Q* occurs t* >= 3 times and the other
    at least once, then den(u^k v^ell) > 2^m* * Q*^(t*-3). Exhaustive over words of length <= 3 with entries <= 4
    (contracting ones) and counts up to 6, plus random larger words.
(2) Worked example (1,2,2)^3 (2): C = 213341, D = 72023, gcd 1, bound 8.
(3) The d499 obstruction: w = (1)^4 (1,3)^3, D_u = -1, C_u = 1, D_v = 7, C_v = 5, K = -12, C_w = 85865, D_w = 6487,
    gcd 13, den 499, and the actual 3x+499 cycle through 6605 with exactly these valuations.
(4) The coprime integer lemma 5(Rk + S ell - gcd(Rk, S ell) + 1) >= 7(R + S) for coprime R, S and k, ell >= 2
    (R, S <= 40, k, ell <= 14), and eta = (5 log_3 2 - 3)/14.
Standard library. Run without -O.
"""
from itertools import product
from math import gcd, log
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent


def CD(z):
    A, C, m = 0, 0, len(z)
    for j, a in enumerate(z):
        C += 3**(m - 1 - j) * 2**A
        A += a
    return C, 2**A - 3**m


def check(u, v, k, ell):
    Cu, Du = CD(u)
    Cv, Dv = CD(v)
    if Du <= 0 or Dv <= 0:
        return None
    K = Du * Cv - Dv * Cu
    if K == 0:
        return None
    Qu, Qv = 2**sum(u), 2**sum(v)
    Qs, ms = max(Qu, Qv), max(len(u), len(v))
    counts = []
    if Qu == Qs:
        counts.append((k, ell))
    if Qv == Qs:
        counts.append((ell, k))
    ok_cases = [(ts, other) for ts, other in counts if ts >= 3 and other >= 1]
    if not ok_cases:
        return None
    ts = max(t for t, _ in ok_cases)
    C, D = CD(u * k + v * ell)
    assert D > 0
    den = D // gcd(C, D)
    assert den > 2**ms * Qs**(ts - 3), (u, v, k, ell, den)
    return True


def part1():
    words = [z for L in (1, 2, 3) for z in product(range(1, 5), repeat=L) if CD(z)[1] > 0]
    n = 0
    for u in words:
        for v in words:
            for k in range(1, 7):
                for ell in range(1, 7):
                    if check(u, v, k, ell):
                        n += 1
    rng = random.Random(3)
    r = 0
    while r < 3000:
        u = tuple(rng.randint(1, 5) for _ in range(rng.randint(1, 7)))
        v = tuple(rng.randint(1, 5) for _ in range(rng.randint(1, 7)))
        if check(u, v, rng.randint(1, 7), rng.randint(1, 7)):
            r += 1
    return {"contracting_words_len_le_3": len(words), "exhaustive_eligible_cases": n, "random_eligible_cases": r}


def part2():
    C, D = CD((1, 2, 2) * 3 + (2,))
    assert (C, D, gcd(C, D)) == (213341, 72023, 1)
    return {"C": C, "D": D, "gcd": 1, "bound": 2**3}


def part3():
    u, v = (1,), (1, 3)
    Cu, Du = CD(u)
    Cv, Dv = CD(v)
    K = Du * Cv - Dv * Cu
    w = u * 4 + v * 3
    C, D = CD(w)
    g = gcd(C, D)
    assert (Du, Cu, Dv, Cv, K, C, D, g, D // g) == (-1, 1, 7, 5, -12, 85865, 6487, 13, 499)
    v2 = lambda n: (n & -n).bit_length() - 1
    x, vals = 6605, []
    for _ in range(len(w)):
        y = 3 * x + 499
        e = v2(y)
        vals.append(e)
        x = y >> e
    assert x == 6605 and tuple(vals) == w
    assert 6605 * D == 499 * C * 1 or 6605 * (D // g) == 499 * (C // g)
    return {"word": list(w), "C": C, "D": D, "gcd": g, "den": D // g, "start": 6605}


def part4():
    n = 0
    for R in range(1, 41):
        for S in range(1, 41):
            if gcd(R, S) != 1:
                continue
            for k in range(2, 15):
                for ell in range(2, 15):
                    assert 5 * (R * k + S * ell - gcd(R * k, S * ell) + 1) >= 7 * (R + S), (R, S, k, ell)
                    n += 1
    eta = (5 * log(2) / log(3) - 3) / 14
    return {"cases": n, "eta": round(eta, 10)}


def main():
    out = {"probe": "c003_variable_blocks_check", "main": "7270d95", "contracting_theorem": part1(),
           "example_122_2": part2(), "d499_obstruction": part3(), "integer_lemma": part4(), "result": "PASS"}
    (HERE / "c003_variable_blocks_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
