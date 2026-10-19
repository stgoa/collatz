"""Side-lane LEAD probe: sorted gaps of ordered cycles as signed sums over forced positions.

Setting (C005/C006): a primitive rational cycle of a positive word w (m letters, total A, D = 2^A - 3^m > 0)
listed from its minimal intercept; heights h_i relative to the minimum, band B = max h; D-scaled
normalised states Zh_i = 2^(B - h_i) C(w.rotate i). "Ordered": the ranks of Zh rotate by a fixed s and the
images Fh_i = 3 Zh_i + 2^(B - h_i) D are in the same order (no inversions). Sorted gaps G_r (seam last:
G_(m-1) = 2 Zh_[0] - Zh_[m-1]), forcing tau_r = 2^(B-h_[r+1]) - 2^(B-h_[r]) (r < m-1) and
tau_(m-1) = 2^(B+1) - 2^(B-h_[m-1]); exponents e_r = floor(A/m) + [r >= m - s]. J = #{r : tau_r != 0}.

Checks:
 (1) recurrence 2^(e_r) G_((r+s) mod m) = 3 G_r + D tau_r, and the closed form
     G_(r0) = sum_i 3^(m-1-i) 2^(E_i) tau_(r_i) over the orbit r_i = r0 + i s (only J nonzero terms);
     hence gcd(C, D) = gcd(D, the J run-start gaps). J = 1 is the narrow (mechanical) case.
 (2) band B = 1 in the Collatz range m < A < 2m never has J = 2 (a height rise on a non-wrapping
     step would need a zero letter); and the J = 2 identity gcd(C, D) = gcd(2^u1 - 3^v1, 2^u2 - 3^v2)
     with (u1 + u2, v1 + v2) = (A, m) where J = 2 occurs (A >= 2m).
 (3) the rotation to the adjacent-rank state differs from w in at most 2J positions.
"""
import itertools
import json
import math
import sys
from collections import Counter


def CD(z):
    A, C, m = 0, 0, len(z)
    for j, a in enumerate(z):
        C += 3**(m - 1 - j) * 2**A
        A += a
    return C, 2**A - 3**m


def rot(z, i):
    return z[i:] + z[:i]


def is_primitive(z):
    m = len(z)
    return all(not (m % p == 0 and z == z[p:] + z[:p]) for p in range(1, m))


def ordered(z):
    m = len(z)
    C, D = CD(z)
    if D <= 0 or not is_primitive(z):
        return None
    Cs = [CD(rot(z, i))[0] for i in range(m)]
    if min(Cs) != Cs[0]:
        return None
    L = Cs[0]
    h = []
    for c in Cs:
        k = 0
        while c >= 2**(k + 1) * L:
            k += 1
        h.append(k)
    B = max(h)
    Z = [2**(B - t) * c for c, t in zip(Cs, h)]
    if len(set(Z)) < m:
        return None
    order = sorted(range(m), key=lambda i: Z[i])
    rank = {i: r for r, i in enumerate(order)}
    s = (rank[1 % m] - rank[0]) % m
    if not all((rank[(i + 1) % m] - rank[i]) % m == s for i in range(m)):
        return None
    F = [3 * Z[i] + 2**(B - h[i]) * D for i in range(m)]
    if any(F[order[r + 1]] <= F[order[r]] for r in range(m - 1)):
        return None
    A = sum(z)
    qp = A // m
    hs = [h[order[r]] for r in range(m)]
    Zs = [Z[order[r]] for r in range(m)]
    G = [Zs[r + 1] - Zs[r] for r in range(m - 1)] + [2 * Zs[0] - Zs[m - 1]]
    tau = [2**(B - hs[r + 1]) - 2**(B - hs[r]) for r in range(m - 1)] + [2**(B + 1) - 2**(B - hs[m - 1])]
    e = [qp + (1 if r >= m - s else 0) for r in range(m)]
    return dict(m=m, A=A, B=B, s=s, C=C, D=D, G=G, tau=tau, e=e, rank=rank)


def check_closed_form(d):
    m, s, D, G, tau, e = d['m'], d['s'], d['D'], d['G'], d['tau'], d['e']
    for r in range(m):
        assert 2**e[r] * G[(r + s) % m] == 3 * G[r] + D * tau[r]
    for r0 in range(m):
        tot, E, r = 0, 0, r0
        for i in range(m):
            tot += 3**(m - 1 - i) * 2**E * tau[r]
            E += e[r]
            r = (r + s) % m
        assert tot == G[r0]
    g = math.gcd(d['C'], D)
    starts = [(r + s) % m for r in range(m) if tau[r] != 0]
    gg = D
    for r0 in starts:
        gg = math.gcd(gg, G[r0])
    assert gg == g
    return sum(1 for t in tau if t != 0)


def j2_identity(d):
    m, s, e, tau, A = d['m'], d['s'], d['e'], d['tau'], d['A']
    f = [r for r in range(m - 1) if tau[r] != 0][0]
    r, E1, t1 = (m - 1 + s) % m, 0, 0
    while r != f:
        E1 += e[r]; t1 += 1; r = (r + s) % m
    r, E2, t2 = (f + s) % m, 0, 0
    while r != m - 1:
        E2 += e[r]; t2 += 1; r = (r + s) % m
    u1, v1, u2, v2 = e[m - 1] + E1, t1 + 2, e[f] + E2, t2
    assert (u1 + u2, v1 + v2) == (A, m)
    assert math.gcd(2**u1 - 3**v1, 2**u2 - 3**v2) == math.gcd(d['C'], d['D'])


def main():
    out = {"probe": "jterm_gap_check"}
    # (1) and (2b): all ordered cycles, m <= 9, letters 1..4
    byBJ, j2, collatz_b1_j2 = Counter(), 0, 0
    for m in range(2, 10):
        for z in itertools.product(range(1, 5), repeat=m):
            d = ordered(list(z))
            if d is None:
                continue
            J = check_closed_form(d)
            byBJ[(d['B'], J)] += 1
            if d['B'] == 1 and J == 2:
                j2_identity(d)
                j2 += 1
                if d['A'] < 2 * m:
                    collatz_b1_j2 += 1
    assert collatz_b1_j2 == 0
    out["closed_form_ordered_cycles"] = sum(byBJ.values())
    out["by_band_and_J"] = {f"B={b},J={j}": n for (b, j), n in sorted(byBJ.items())}
    out["band1_J2_identity_cases"] = j2
    out["band1_J2_in_collatz_range"] = collatz_b1_j2
    # (3): Collatz range m < A < 2m, m <= 12, letters 1..3
    n3, worst = 0, 0
    for m in range(2, 13):
        for z in itertools.product(range(1, 4), repeat=m):
            z = list(z)
            if not (m < sum(z) < 2 * m):
                continue
            d = ordered(z)
            if d is None:
                continue
            J = sum(1 for t in d['tau'] if t != 0)
            if d['B'] == 1:
                assert J >= 3
            i1 = [i for i in range(m) if d['rank'][i] == 1][0]
            ham = sum(1 for x, y in zip(z, rot(z, i1)) if x != y)
            assert ham <= 2 * J
            worst = max(worst, ham - 2 * J)
            n3 += 1
    out["collatz_range_ordered_cycles"] = n3
    out["max(adjacent_mismatch - 2J)"] = worst
    out["result"] = "PASS"
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
