"""Sidekick probe: independent checks of main's C002 (experiments/cycle_spectrum/C002, main e14a4e3).

(1) Uniform theorem: u != v of equal length m and total A with 2^A > 3^m, k + ell >= 3 =>
    den(u^k v^ell) > 2^m * 2^A / 3^m. Tested on all such pairs with m <= 4, A <= 2m+2 and k, ell <= 6, plus random
    pairs with m <= 9. Also the ingredients: 0 < C_z <= 2^(A-m) (3^m - 2^m); equal-shape words with equal C coincide;
    the intermediate bound den >= G_n / (|J| G_h) > U^(n-h)/|J| (J = C_v - C_u, n = k+ell, h = gcd(k,ell)).
(2) Exact examples: den((1,1,3)^t (1,2,2)^t) = 5(32^t + 27^t) with cancellation (32^t - 27^t)/5;
    den((1,3)^t (3,1)^t) = 7(16^t + 9^t); t <= 40.
(3) The d=59 cycle from 221 with word (1)^2 (2)^4: C = 1105, D = 295, gcd 5 > |K| = 2.
(4) Rotating mechanical family: u_m lower mechanical (length m, total bitlength(3^m)), v_m its one-letter left rotation;
    every rational cycle state of u_m^k v_m^ell exceeds m/12 (13 <= m <= 30, k, ell <= 3), the word is primitive, and
    for k+ell >= 3 the reduced denominator exceeds 1.
Standard library. Run without -O.
"""
from fractions import Fraction as Fr
from itertools import product
from math import gcd
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


def den(z):
    C, D = CD(z)
    return D // gcd(C, D)


def compositions(A, m):
    if m == 1:
        if A >= 1:
            yield (A,)
        return
    for a in range(1, A - m + 2):
        for rest in compositions(A - a, m - 1):
            yield (a,) + rest


def check_pair(u, v, k, ell):
    m, A = len(u), sum(u)
    U, V = 2**A, 3**m
    w = u * k + v * ell
    C, D = CD(w)
    g = gcd(C, D)
    d = D // g
    assert d * 3**m > 2**m * 2**A, (u, v, k, ell)
    J = CD(v)[0] - CD(u)[0]
    n, h = k + ell, gcd(k, ell)
    Gn, Gh = (U**n - V**n) // (U - V), (U**h - V**h) // (U - V)
    assert J != 0 and Fr(d) >= Fr(Gn, abs(J) * Gh) and Fr(Gn, abs(J) * Gh) > Fr(U**(n - h), abs(J))
    return d


def part1():
    exhaustive = 0
    for m in range(1, 5):
        for A in range(1, 2 * m + 3):
            if 2**A <= 3**m:
                continue
            words = list(compositions(A, m))
            for z in words:
                C, _ = CD(z)
                assert 0 < C <= 2**(A - m) * (3**m - 2**m)
            Cs = [CD(z)[0] for z in words]
            assert len(set(Cs)) == len(Cs)            # equal-shape words have distinct C
            for u, v in product(words, repeat=2):
                if u == v:
                    continue
                for k in range(1, 7):
                    for ell in range(1, 7):
                        if k + ell >= 3:
                            check_pair(u, v, k, ell)
                            exhaustive += 1
    rng = random.Random(7)
    rand = 0
    for _ in range(4000):
        m = rng.randint(2, 9)
        A = rng.randint(int(m * 1.585) + 1, 3 * m)
        words = []
        while len(words) < 2:
            cuts = sorted(rng.sample(range(1, A), m - 1))
            z = tuple(b - a for a, b in zip([0] + cuts, cuts + [A]))
            if z not in words:
                words.append(z)
        u, v = words
        k, ell = rng.randint(1, 6), rng.randint(1, 6)
        if k + ell >= 3:
            check_pair(u, v, k, ell)
            rand += 1
    return {"exhaustive_cases_m_le_4": exhaustive, "random_cases_m_le_9": rand}


def part2():
    for t in range(1, 41):
        w = (1, 1, 3) * t + (1, 2, 2) * t
        C, D = CD(w)
        assert gcd(C, D) == (32**t - 27**t) // 5 and D // gcd(C, D) == 5 * (32**t + 27**t)
        w2 = (1, 3) * t + (3, 1) * t
        assert den(w2) == 7 * (16**t + 9**t)
    return {"t_checked": 40}


def part3():
    v2 = lambda n: (n & -n).bit_length() - 1
    x, states, vals = 221, [], []
    for _ in range(6):
        y = 3 * x + 59
        e = v2(y)
        states.append(x)
        vals.append(e)
        x = y >> e
    assert x == 221 and tuple(vals) == (1, 1, 2, 2, 2, 2)
    C, D = CD(tuple(vals))
    Cu, Du = CD((1,))
    Cv, Dv = CD((2,))
    K = Du * Cv - Dv * Cu
    assert (C, D, gcd(C, D), K) == (1105, 295, 5, -2) or (C, D, gcd(C, D), abs(K)) == (1105, 295, 5, 2)
    return {"states": states, "valuations": vals, "C": C, "D": D, "gcd": gcd(C, D), "K": K}


def lower_mechanical(m, A):
    return tuple((j + 1) * A // m - j * A // m for j in range(m))


def cycle_states(z):
    C, D = CD(z)
    x = Fr(C, D)
    out = []
    for a in z:
        out.append(x)
        x = (3 * x + 1) / 2**a
    assert x == out[0]
    return out


def primitive(z):
    n = len(z)
    return all(not (n % p == 0 and z == z[:p] * (n // p)) for p in range(1, n))


def part4():
    cnt = 0
    for m in range(13, 31):
        A = (3**m).bit_length()
        u = lower_mechanical(m, A)
        v = u[1:] + u[:1]
        assert u != v
        for k in range(1, 4):
            for ell in range(1, 4):
                w = u * k + v * ell
                assert primitive(w)
                assert min(cycle_states(w)) > Fr(m, 12)
                if k + ell >= 3:
                    assert den(w) > 1
                cnt += 1
    return {"m_k_ell_cases": cnt}


def main():
    out = {"probe": "c002_two_block_check", "main": "e14a4e3", "uniform_theorem": part1(),
           "exact_examples": part2(), "d59_cycle": part3(), "rotating_mechanical": part4(), "result": "PASS"}
    (HERE / "c002_two_block_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
