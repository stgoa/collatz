"""Sidekick probe: independent checks of main's C004 (experiments/cycle_spectrum/C004, main 61cf54a).

(1) Narrow-cycle theorem: for primitive positive valuation words (D = 2^A - 3^m > 0), the rational cycle has
    H < 2L iff the word is a rotation of the mechanical word a_j = floor((j+1)A/m) - floor(jA/m); for narrow cycles
    with m > 1, gcd(A, m) = 1 and den = D (no cancellation). Grid: all words of length 1..7 with entries 1..5
    (different from main's 1..8 x 1..4 grid).
(2) Narrow spectrum law vs actual census: at each d <= 999 coprime to 6, the narrow primitive cycles are indexed by
    coprime (A, m) with 0 < 2^A - 3^m | d. Predicted cycles whose minimum is <= 5000 must appear in main's seed-bounded
    census (actual_cycles.json); narrow cycles in the census must be predicted.
(3) Cut formula gcd(D, K_i) = g * gcd(D/g, 2^(a_i) - 3) for one-letter cuts (random words).
(4) Controls: the d5 cycle 19 -> 31 -> 49 has normalized minimum gap 12/5 > 2; the d13 mechanical cycle has
    numerators 319, 367, 421, 485, 557 with ratio 557/319 < 2.
Standard library. Run without -O.
"""
from fractions import Fraction as Fr
from itertools import product
from math import gcd
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent


def CD(z):
    A, C, m = 0, 0, len(z)
    for j, a in enumerate(z):
        C += 3**(m - 1 - j) * 2**A
        A += a
    return C, 2**A - 3**m


def states(z):
    C, D = CD(z)
    x = Fr(C, D)
    out = []
    for a in z:
        out.append(x)
        x = (3 * x + 1) / 2**a
    assert x == out[0]
    return out


def mechanical(A, m):
    return tuple((j + 1) * A // m - j * A // m for j in range(m))


def rotations(z):
    return {z[i:] + z[:i] for i in range(len(z))}


def primitive(z):
    n = len(z)
    return all(not (n % p == 0 and z == z[:p] * (n // p)) for p in range(1, n))


def part1():
    n = narrow = 0
    for m in range(1, 8):
        for z in product(range(1, 6), repeat=m):
            C, D = CD(z)
            if D <= 0 or not primitive(z):
                continue
            n += 1
            st = states(z)
            is_narrow = max(st) < 2 * min(st)
            is_mech = z in rotations(mechanical(sum(z), m))
            assert is_narrow == is_mech, z
            if is_narrow:
                narrow += 1
                if m > 1:
                    assert gcd(sum(z), m) == 1 and gcd(C, D) == 1
    return {"primitive_positive_words": n, "narrow": narrow}


def part2(path):
    data = json.load(open(path))
    pairs = []
    for m in range(1, 40):
        for A in range(m, 80):
            D = 2**A - 3**m
            if 0 < D <= 999 and gcd(A, m) == 1:
                pairs.append((A, m, D))
    checked, missing, extra = 0, [], []
    census = {}
    for c in data["cycles"]:
        census.setdefault(c["d"], []).append(c)
    for d in range(1, 1000, 2):
        if d % 3 == 0:
            continue
        actual_narrow = set()
        for c in census.get(d, []):
            st = c["states"]
            if len(st) > 1 and max(st) < 2 * min(st) or len(st) == 1:
                actual_narrow.add(min(st))
        predicted = set()
        for A, m, D in pairs:
            if d % D == 0:
                st = [s * d for s in states(mechanical(A, m))]
                assert all(s.denominator == 1 for s in st)
                predicted.add(int(min(st)))
        for x in predicted:
            if x <= 5000:
                checked += 1
                if x not in actual_narrow:
                    missing.append((d, x))
        for x in actual_narrow:
            if x not in predicted:
                extra.append((d, x))
    assert not missing and not extra, (missing[:5], extra[:5])
    return {"coprime_pairs_with_D_le_999": len(pairs), "predicted_narrow_cycles_with_min_le_5000": checked}


def part3(trials=3000):
    rng = random.Random(4)
    n = 0
    while n < trials:
        z = tuple(rng.randint(1, 5) for _ in range(rng.randint(2, 8)))
        C, D = CD(z)
        if D <= 0:
            continue
        g = gcd(C, D)
        for i in range(len(z)):
            r = z[i:] + z[:i]
            u, v = r[:1], r[1:]
            Cu, Du = CD(u)
            Cv, Dv = CD(v)
            K = Du * Cv - Dv * Cu
            assert gcd(D, K) == g * gcd(D // g, 2**r[0] - 3)
        n += 1
    return {"random_words": n}


def part4():
    v2 = lambda n: (n & -n).bit_length() - 1
    T = lambda x, d: (3 * x + d) >> v2(3 * x + d)
    assert T(19, 5) == 31 and T(31, 5) == 49 and T(49, 5) == 19
    st = sorted(Fr(x, 5) for x in (19, 31, 49))
    gap = min(b - a for a, b in zip(st, st[1:]))
    w = mechanical(8, 5)
    s13 = sorted(int(13 * s) for s in states(w))
    return {"d5_min_gap": str(gap), "d13_mechanical_word": list(w), "d13_numerators": s13,
            "ratio_lt_2": s13[-1] < 2 * s13[0]}


def main():
    out = {"probe": "c004_narrow_check", "main": "61cf54a", "narrow_theorem": part1(),
           "spectrum_vs_census": part2(sys.argv[1]), "cut_formula": part3(), "controls": part4(), "result": "PASS"}
    assert out["controls"]["d5_min_gap"] == "12/5" and out["controls"]["d13_numerators"] == [319, 367, 421, 485, 557]
    (HERE / "c004_narrow_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
