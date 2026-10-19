"""Sidekick probe: independent checks of main's C013 (experiments/cycle_spectrum/C013, main 1c5c19d).

Words w = (U, a_0, U, a_1, ..., U, a_(r-1)) with an arbitrary background U (length n, total A_U) and nonconstant markers.
u = 2^A_U, alpha = 3^(n+1), E = 3 C_U + u, T = sum a_i, P(X) = sum_j 2^(a_0+...+a_(j-1)) X^(r-1-j), Q(X) = X^r - 2^T,
G = monic gcd(P, Q), d = deg G, e = r - d, Pbar = P/G, Qbar = Q/G, R = Res(Pbar, Qbar), eta = D/2^A.
(1) C_w = E * P_h(alpha, u) and D = -Q_h(alpha, u) (homogeneous evaluations);
(2) the exact denominator law q = |Qbar_h| / gcd(Qbar_h, E Pbar_h);
(3) q >= |Qbar_h| / (E |R|);
(4) q > eta 2^(n(e-1)-d) / |R|  and the weaker  q > eta 2^(n(e-1)-d) / (r^(e(d+1)) 2^(2Te));
(5) support uncertainty: every marker rotation with s > 0 mismatches has s * binom(e, 2) >= r;
(6) control: markers (3,1,3,3,1,1) give G = X + 4.
Random words with n <= 8 (U letters 1..4), r = 2..6, nonconstant markers 1..5, D > 0. Standard library. Run without -O.
"""
from fractions import Fraction as Fr
from math import gcd, comb
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


# polynomials as lists of Fractions, index = power
def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pdivmod(a, b):
    a, b = trim(a), trim(b)
    q = [Fr(0)] * max(1, len(a) - len(b) + 1)
    r = a[:]
    while len(r) >= len(b) and any(r):
        c = r[-1] / b[-1]
        k = len(r) - len(b)
        q[k] = c
        for i, bc in enumerate(b):
            r[i + k] -= c * bc
        r = trim(r)
        if len(r) < len(b) or (len(r) == 1 and r[0] == 0):
            break
    return trim(q), trim(r)


def pgcd(a, b):
    a, b = trim(a), trim(b)
    while any(b):
        _, r = pdivmod(a, b)
        a, b = b, r
        if len(b) == 1 and b[0] == 0:
            break
    return [c / a[-1] for c in a]


def homog(p, x, y):
    k = len(p) - 1
    return sum(c * x**i * y**(k - i) for i, c in enumerate(p))


def det(M):
    M = [row[:] for row in M]
    n = len(M)
    dval = Fr(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            dval = -dval
        dval *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n):
                M[r][k] -= f * M[c][k]
    return dval


def resultant(p, q):
    p, q = trim(p), trim(q)
    dp, dq = len(p) - 1, len(q) - 1
    if dp == 0:
        return p[0]**dq
    if dq == 0:
        return q[0]**dp
    n = dp + dq
    S = []
    for i in range(dq):
        row = [Fr(0)] * n
        for j, c in enumerate(reversed(p)):
            row[i + j] = c
        S.append(row)
    for i in range(dp):
        row = [Fr(0)] * n
        for j, c in enumerate(reversed(q)):
            row[i + j] = c
        S.append(row)
    return det(S)


def analyse(U, markers):
    r = len(markers)
    n = len(U)
    w = tuple(x for a in markers for x in U + (a,))
    C, D = CD(w)
    if D <= 0:
        return None
    A, m = sum(w), len(w)
    q = D // gcd(C, D)
    AU = sum(U)
    u = 2**AU
    alpha = 3**(n + 1)
    CU = CD(U)[0] if U else 0
    E = 3 * CU + u
    T = sum(markers)
    pref = [sum(markers[:j]) for j in range(r)]
    P = [Fr(0)] * r
    for j in range(r):
        P[r - 1 - j] = Fr(2**pref[j])
    Q = [Fr(-2**T)] + [Fr(0)] * (r - 1) + [Fr(1)]
    assert C == E * homog(P, alpha, u) and -D == homog(Q, alpha, u)          # (1)
    G = pgcd(Q, P)
    d = len(G) - 1
    e = r - d
    Pbar, rem1 = pdivmod(P, G)
    Qbar, rem2 = pdivmod(Q, G)
    assert all(c == 0 for c in rem1) and all(c == 0 for c in rem2)
    assert all(c.denominator == 1 for c in Pbar + Qbar + G)
    Qh = int(homog(Qbar, alpha, u))
    Ph = int(homog(Pbar, alpha, u))
    assert q == abs(Qh) // gcd(Qh, E * Ph) and abs(Qh) % gcd(Qh, E * Ph) == 0     # (2)
    R = int(resultant(Pbar, Qbar))
    assert R != 0
    assert Fr(q) >= Fr(abs(Qh), E * abs(R))                                    # (3)
    eta = Fr(D, 2**A)
    assert Fr(q) > eta * Fr(2)**(n * (e - 1) - d) / abs(R)                      # (4)
    assert Fr(q) > eta * Fr(2)**(n * (e - 1) - d) / (r**(e * (d + 1)) * 2**(2 * T * e))
    for k in range(1, r):                                                      # (5)
        rot = markers[k:] + markers[:k]
        s = sum(1 for i in range(r) if markers[i] != rot[i])
        if s > 0:
            assert s * comb(e, 2) >= r, (markers, k, s, e)
    return {"d": d, "e": e}


def main():
    rng = random.Random(13)
    n_ok, by_d = 0, {}
    while n_ok < 4000:
        n = rng.randint(0, 8)
        U = tuple(rng.randint(1, 4) for _ in range(n))
        r = rng.randint(2, 6)
        markers = tuple(rng.randint(1, 5) for _ in range(r))
        if len(set(markers)) == 1:
            continue
        res = analyse(U, markers)
        if res is None:
            continue
        n_ok += 1
        by_d[res["d"]] = by_d.get(res["d"], 0) + 1
    # (6) control
    P = [Fr(2**s) for s in reversed([0, 3, 4, 7, 10, 11])]
    Q = [Fr(-4096)] + [Fr(0)] * 5 + [Fr(1)]
    G = pgcd(Q, P)
    assert G == [Fr(4), Fr(1)]
    out = {"probe": "c013_background_check", "main": "1c5c19d", "random_words_checked": n_ok,
           "count_by_deg_G": dict(sorted(by_d.items())), "control_313311_G": "X + 4", "result": "PASS"}
    (HERE / "c013_background_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
