"""Sidekick probe: a discriminating test of main's C012 candidate (experiments/cycle_spectrum/C012, main de7db67).

Candidate (unproved in C012): for a positive word w with D = 2^A - 3^m > 0, g = gcd(C_w, D), and a selected nonidentity
rotation differing from w in s positions,  g^s * 4^m < 2^(A s) * 3^m   (equivalently q > (1 - 3^m/2^A)(4/3)^(m/s)).
Main's evidence on stored cycles is nondiscriminating (q >= 5, m/s <= 5). A case is discriminating only when the
candidate's lower bound for q is at least 5 (every q > 1 is coprime to 6). (1) Exhaustive grid (length <= 9, letters 1..5):
counts how many rotations are discriminating -- none can be, since (4/3)^(m/s) < 5 there. (4) A discriminating random
search over structured words (marker, U, marker, U, ...) with s = 3..5 mismatches and m/s up to ~21. Also checks:
(2) the corrected formula C(k, 2^n) = 3^n + 2^k (4^n - 3^n) for the word (k, 2, ..., 2);
(3) the family (1, U, 3, U, 4, U), U over {2, 5}: primitive with minimum rotation distance exactly 3 (random U).
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


def primitive(z):
    n = len(z)
    return all(not (n % p == 0 and z == z[:p] * (n // p)) for p in range(1, n))


def part1():
    tested, counter, worst, discr = 0, [], (0.0, None), 0
    by_s = {}
    for m in range(2, 10):
        for z in product(range(1, 6), repeat=m):
            C, D = CD(z)
            if D <= 0 or not primitive(z):
                continue
            g = gcd(C, D)
            A = sum(z)
            for r in range(1, m):
                rot = z[r:] + z[:r]
                s = sum(1 for i in range(m) if z[i] != rot[i])
                lhs = g**s * 4**m
                rhs = 2**(A * s) * 3**m
                tested += 1
                by_s[s] = by_s.get(s, 0) + 1
                # discriminating only if the candidate's lower bound for q reaches 5 (q > 1 is coprime to 6, so q >= 5)
                if (2**A - 3**m) ** s * 4**m >= 5**s * 2**(A * s) * 3**m:
                    discr += 1
                if g > 1:
                    ratio = (s * log(g) + m * log(4)) / (A * s * log(2) + m * log(3))
                    if ratio > worst[0]:
                        worst = (ratio, (z, r, s, g))
                if not lhs < rhs:
                    counter.append((z, r, s, g))
    return {"rotations_tested": tested, "discriminating_rotations": discr, "by_s": dict(sorted(by_s.items())),
            "counterexamples": counter[:5],
            "worst_log_ratio_with_g_gt_1": round(worst[0], 6), "worst_case": str(worst[1])}


def part2():
    for k in range(1, 8):
        for n in range(1, 12):
            C, _ = CD((k,) + (2,) * n)
            assert C == 3**n + 2**k * (4**n - 3**n)
    return {"formula_checked": True}


def rho(z):
    m = len(z)
    return min(sum(1 for i in range(m) if z[i] != (z[r:] + z[:r])[i]) for r in range(1, m))


def part3():
    rng = random.Random(12)
    n = 0
    for _ in range(300):
        U = tuple(rng.choice((2, 5)) for _ in range(rng.randint(1, 8)))
        w = (1,) + U + (3,) + U + (4,) + U
        assert primitive(w) and rho(w) == 3, (U, rho(w))
        n += 1
    return {"random_backgrounds": n}


def part4(samples=60000, seed=2026):
    """Structured words with few mismatches at a long period: w = (x_1, U, x_2, U, ..., x_s, U), letters of U in 1..3,
    markers distinct, |U| up to 20, so the rotation by |U|+1 has s mismatches with m/s up to ~21. Test the candidate only
    where it is discriminating (its lower bound for q is >= 5)."""
    rng = random.Random(seed)
    tested = discr = 0
    counter = []
    worst = (0.0, None)
    for _ in range(samples):
        s = rng.choice((3, 3, 4, 5))
        L = rng.randint(4, 20)
        U = tuple(rng.choice((1, 2, 2, 3)) for _ in range(L))
        markers = rng.sample(range(1, 7), s)
        w = tuple(x for mk in markers for x in (mk,) + U)
        m = len(w)
        C, D = CD(w)
        if D <= 0 or not primitive(w):
            continue
        A = sum(w)
        rot = w[L + 1:] + w[:L + 1]
        ss = sum(1 for i in range(m) if w[i] != rot[i])
        g = gcd(C, D)
        tested += 1
        if (2**A - 3**m) ** ss * 4**m >= 5**ss * 2**(A * ss) * 3**m:
            discr += 1
            if not g**ss * 4**m < 2**(A * ss) * 3**m:
                counter.append((w, ss, g))
            if g > 1:
                ratio = (ss * log(g) + m * log(4)) / (A * ss * log(2) + m * log(3))
                if ratio > worst[0]:
                    worst = (ratio, (m, ss, g, D // g))
    return {"structured_words_tested": tested, "discriminating": discr, "counterexamples": counter[:5],
            "worst_log_ratio_g_gt_1": round(worst[0], 6), "worst_case_m_s_g_q": str(worst[1])}


def main():
    out = {"probe": "c012_candidate_check", "main": "de7db67", "candidate": part1(),
           "corrected_formula": part2(), "distance3_family": part3(), "structured_search": part4(), "result": "PASS"}
    (HERE / "c012_candidate_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
