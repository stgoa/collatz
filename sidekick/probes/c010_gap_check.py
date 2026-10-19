"""Sidekick probe: independent checks of main's C010 (experiments/cycle_spectrum/C010, main cae57b0).

(1) Gap lattice: E shifts sorted coordinates by one place and doubles the wrapped coordinate, so E^m = 2I and
    U = E - I has the integer inverse I + E + ... + E^(m-1) (exact integer matrices, m <= 12).
(2) The q5 control 19 -> 31 -> 49 divided by 5: sorted normalized gaps 11/10, 13/10 and the seam 7/5.
(3) Mechanical complete seam: for primitive mechanical words (coprime (A, m), 2^A > 3^m) the sorted intercepts B_j of
    the rotations satisfy 2 B_0 - B_(m-1) = 3^(m-1), so the seam gap is 3^(m-1)/D.
Standard library. Run without -O.
"""
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def matmul(X, Y):
    n = len(X)
    return [[sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def part1():
    for m in range(1, 13):
        E = [[0] * m for _ in range(m)]
        for i in range(m - 1):
            E[i][i + 1] = 1
        E[m - 1][0] = 2
        I = [[int(i == j) for j in range(m)] for i in range(m)]
        P = I
        S = [[0] * m for _ in range(m)]
        for _ in range(m):
            S = [[S[i][j] + P[i][j] for j in range(m)] for i in range(m)]
            P = matmul(P, E)
        assert P == [[2 * I[i][j] for j in range(m)] for i in range(m)]          # E^m = 2I
        U = [[E[i][j] - I[i][j] for j in range(m)] for i in range(m)]
        assert matmul(U, S) == I and matmul(S, U) == I
    return {"m_checked": 12}


def part2():
    st = [Fr(19, 5), Fr(31, 5), Fr(49, 5)]
    L = min(st)
    h = [0 if s < 2 * L else (1 if s < 4 * L else 2) for s in st]
    z = sorted(s / 2**hi for s, hi in zip(st, h))
    gaps = [z[1] - z[0], z[2] - z[1], 2 * z[0] - z[2]]
    assert gaps == [Fr(11, 10), Fr(13, 10), Fr(7, 5)]
    return {"gaps": [str(g) for g in gaps]}


def CD(z):
    A, C, m = 0, 0, len(z)
    for j, a in enumerate(z):
        C += 3**(m - 1 - j) * 2**A
        A += a
    return C, 2**A - 3**m


def part3():
    n = 0
    for m in range(2, 30):
        for A in range(m, 3 * m):
            if gcd(A, m) != 1 or 2**A <= 3**m:
                continue
            w = tuple((j + 1) * A // m - j * A // m for j in range(m))
            Bs = sorted(CD(w[i:] + w[:i])[0] for i in range(m))
            assert 2 * Bs[0] - Bs[-1] == 3**(m - 1), (A, m)
            n += 1
    return {"mechanical_words_checked": n}


def main():
    out = {"probe": "c010_gap_check", "main": "cae57b0", "gap_lattice_inverse": part1(), "q5_gaps": part2(),
           "mechanical_seam": part3(), "result": "PASS"}
    (HERE / "c010_gap_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
