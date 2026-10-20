"""Sidekick probe: independent checks of main's C011 (experiments/cycle_spectrum/C011, main b896512).

(1) Two-rotation-defect theorem: for every primitive positive word w with D = 2^A - 3^m > 0 (length <= 9, letters 1..5)
    and every nonidentity rotation differing from w in exactly two positions: den(w) > 1,
    g^2 < (2^k - 1)^2 2^(A-m-k) 3^m (k = the mismatch amplitude), and den(w) > (1 - 3^m/2^A)(2/sqrt 3)^m.
(2) The marker family (3, b_n, 4, b_n), n = 2^r - 1, b_n the lower mechanical block of length n and total
    ceil(n log2 3): its half-period rotation has two unit mismatches, every rational state exceeds n/128, den > 1.
(3) The cancellation family 1^t 2^(2t): gcd(C, D) = gcd(4^t - 1, 3^t - 2^t), and powers of 5 divide it at suitable t.
Standard library. Run without -O.
"""
from fractions import Fraction as Fr
from itertools import product
from math import gcd, isqrt
from pathlib import Path
import json

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
    n_words = n_rot = 0
    for m in range(2, 10):
        for z in product(range(1, 6), repeat=m):
            C, D = CD(z)
            if D <= 0 or not primitive(z):
                continue
            A = sum(z)
            g = gcd(C, D)
            den = D // g
            hit = False
            for s in range(1, m):
                r = z[s:] + z[:s]
                diff = [i for i in range(m) if z[i] != r[i]]
                if len(diff) != 2:
                    continue
                i, j = diff
                vals = sorted([z[i], z[j]])
                assert sorted([r[i], r[j]]) == vals            # swapped valuations a, a+k
                k = vals[1] - vals[0]
                assert den > 1
                assert g * g < (2**k - 1)**2 * 2**(A - m - k) * 3**m
                # den > (1 - 3^m/2^A) (2/sqrt3)^m  <=>  den^2 * 3^m * 2^(2A) > (2^A - 3^m)^2 * 4^m
                assert den * den * 3**m * 2**(2 * A) > (2**A - 3**m)**2 * 4**m
                n_rot += 1
                hit = True
            n_words += hit
    return {"words_with_two_defect_rotation": n_words, "two_defect_rotations": n_rot}


def mech(n):
    A = (3**n).bit_length()                       # ceil(n log2 3) since 3^n is not a power of 2
    return tuple((j + 1) * A // n - j * A // n for j in range(n))


def states(z):
    C, D = CD(z)
    x = Fr(C, D)
    out = []
    for a in z:
        out.append(x)
        x = (3 * x + 1) / 2**a
    assert x == out[0]
    return out


def part2():
    rows = []
    for r in range(2, 7):
        n = 2**r - 1
        b = mech(n)
        w = (3,) + b + (4,) + b
        m = len(w)
        rot = w[m // 2:] + w[:m // 2]
        diff = [i for i in range(m) if w[i] != rot[i]]
        assert len(diff) == 2 and all(abs(w[i] - rot[i]) == 1 for i in diff)
        C, D = CD(w)
        assert D > 0 and D // gcd(C, D) > 1 and primitive(w)
        assert min(states(w)) > Fr(n, 128)
        rows.append({"n": n, "m": m, "den_gt_1": True})
    return rows


def part3():
    hits5 = {}
    for t in range(1, 61):
        w = (1,) * t + (2,) * (2 * t)
        C, D = CD(w)
        g = gcd(C, D)
        assert g == gcd(4**t - 1, 3**t - 2**t), t
        e = 0
        while g % 5**(e + 1) == 0:
            e += 1
        if e >= 1:
            hits5.setdefault(e, t)
    return {"t_checked": 60, "first_t_with_5^e": hits5}


def main():
    out = {"probe": "c011_two_defect_check", "main": "b896512", "two_defect_theorem": part1(),
           "marker_family": part2(), "cancellation_family": part3(), "result": "PASS"}
    (HERE / "c011_two_defect_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
