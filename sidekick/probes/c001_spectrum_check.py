"""Sidekick probe: independent checks of main's C001 (experiments/cycle_spectrum/C001, main 14441c0), the first batch
of the cycle-spectrum goal.

Conventions as in C001: a positive valuation word z = (a_0..a_(m-1)), A_j partial sums, A = A_m,
C_z = sum_j 3^(m-1-j) 2^(A_j), D_z = 2^A - 3^m; for D_z > 0 the cycle point is C_z/D_z and
den(z) = D_z / gcd(C_z, D_z).

(1) Identities (1)-(3) for w_k = u^k v, the divisibility g_k | K_0 (prime-to-6 part of K = D_u C_v - D_v C_u),
    the exact formula g_k = gcd(D_k, K) when gcd(D_u, D_v) = 1, the two-sided bound (7), and periodicity of g_k with
    the stated period T = lcm(ord_L(Q), ord_L(P)), L = K_0 |D_u| -- random u, v, k.
(2) The worked law den((1,1,3)^k 2) = (4*32^k - 3*27^k)/(7 if k = 3 mod 6 else 1), k <= 80.
(3) The killed strengthening u=(3), v=(1,5), k=1 and its actual 3x+485 cycle 49 -> 79 -> 361 -> 49.
(4) The perturbed mechanical family w = u_m^k 2 (u_m lower mechanical word, length m, total A = bitlength(3^m)):
    den(w) > 3*(3^m)^(k-1)/(2m), primitivity, for 13 <= m <= 60, 2 <= k <= 5.
(5) Independent raw cycle scan of 3x+d (state 1 not absorbing), d <= 199 coprime to 6, odd seeds <= 5000, compared
    with main's actual_cycles.json (per-d cycle sets as sets of minimum states).
Standard library. Run without -O.
"""
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
    return C, 2**A - 3**m, A, m


def part1(trials=3000, seed=1):
    rng = random.Random(seed)
    n_exact = n_two_sided = n_periodic = 0
    for _ in range(trials):
        u = tuple(rng.randint(1, 5) for _ in range(rng.randint(1, 5)))
        v = tuple(rng.randint(1, 5) for _ in range(rng.randint(1, 5)))
        Cu, Du, Au, mu = CD(u)
        Cv, Dv, Av, mv = CD(v)
        Q, P, S, R = 2**Au, 3**mu, 2**Av, 3**mv
        K = Du * Cv - Dv * Cu
        K0 = abs(K)
        while K0 and K0 % 2 == 0:
            K0 //= 2
        while K0 and K0 % 3 == 0:
            K0 //= 3
        gs = {}
        for k in range(1, 13):
            Ck, Dk, _, _ = CD(u * k + v)
            Gk = (Q**k - P**k) // (Q - P)
            assert Ck == R * Cu * Gk + Q**k * Cv and Dk == S * Q**k - R * P**k
            assert Du * Ck - Cu * Dk == Q**k * K
            if Dk <= 0:
                continue
            g = gcd(Ck, Dk)
            gs[k] = g
            if K != 0:
                assert K0 % g == 0
                H = gcd(Dk, K)
                assert H % g == 0 and g % (H // gcd(H, Du)) == 0
                n_two_sided += 1
                if gcd(Du, Dv) == 1:
                    assert g == H
                    n_exact += 1
        if K != 0 and K0 > 1 and Du > 0:
            L = K0 * abs(Du)
            def order(a, n, cap=40):
                a %= n
                e, x = 1, a
                while x != 1:
                    if e >= cap:
                        return None
                    x = x * a % n
                    e += 1
                return e
            oQ, oP = order(Q, L), order(P, L)
            T = oQ * oP // gcd(oQ, oP) if oQ and oP else None
            if T is not None and T <= 40:
                for k in range(1, 13):
                    Ck, Dk, _, _ = CD(u * k + v)
                    Ck2, Dk2, _, _ = CD(u * (k + T) + v)
                    if Dk > 0 and Dk2 > 0:
                        assert gcd(Ck, Dk) == gcd(Ck2, Dk2)
                        n_periodic += 1
    return {"trials": trials, "two_sided_checks": n_two_sided, "exact_formula_checks": n_exact,
            "periodicity_checks": n_periodic}


def part2():
    for k in range(1, 81):
        C, D, _, _ = CD((1, 1, 3) * k + (2,))
        den = D // gcd(C, D)
        assert den == (4 * 32**k - 3 * 27**k) // (7 if k % 6 == 3 else 1), k
    return {"k_checked": 80, "first_den": CD((1, 1, 3, 2))[1] // gcd(*CD((1, 1, 3, 2))[:2])}


def part3():
    Cu, Du, _, _ = CD((3,))
    Cv, Dv, _, _ = CD((1, 5))
    K = Du * Cv - Dv * Cu
    C, D, _, _ = CD((3, 1, 5))
    T = lambda x: (3 * x + 485) // 2**(((3 * x + 485) & -(3 * x + 485)).bit_length() - 1)
    orbit = [49, T(49), T(T(49)), T(T(T(49)))]
    assert (Du, Dv, K, C, D) == (5, 55, -30, 49, 485) and gcd(C, D) == 1 and gcd(D, K) == 5
    assert orbit == [49, 79, 361, 49]
    return {"D_u": Du, "D_v": Dv, "K": K, "C_w": C, "D_w": D, "gcd(C,D)": 1, "gcd(D,K)": 5, "orbit": orbit}


def lower_mechanical(m, A):
    return tuple((j + 1) * A // m - j * A // m for j in range(m))


def primitive(z):
    n = len(z)
    return all(not (n % p == 0 and z == z[:p] * (n // p)) for p in range(1, n))


def part4():
    checked = 0
    for m in range(13, 61):
        A = (3**m).bit_length()
        u = lower_mechanical(m, A)
        assert len(u) == m and sum(u) == A
        for k in range(2, 6):
            w = u * k + (2,)
            C, D, _, _ = CD(w)
            assert D > 0 and primitive(w)
            den = D // gcd(C, D)
            assert 2 * m * den > 3 * 3**(m * (k - 1)), (m, k)
            checked += 1
    return {"pairs_m_k": checked}


def v2(n):
    return (n & -n).bit_length() - 1


def scan(d, seed_max=5000):
    T = lambda x: (3 * x + d) >> v2(3 * x + d)
    cyc_min = set()
    known = {}
    for s in range(1, seed_max + 1, 2):
        x, path, seen = s, [], {}
        while x not in known and x not in seen and len(path) < 10**5:
            seen[x] = len(path)
            path.append(x)
            x = T(x)
        if x in known:
            label = known[x]
        elif x in seen:
            label = min(path[seen[x]:])
            cyc_min.add(label)
        else:
            raise RuntimeError("cap")
        for y in path:
            known[y] = label
    return cyc_min


def part5(dmax=199):
    data = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else None
    rows, mismatches = 0, []
    for d in range(1, dmax + 1, 2):
        if d % 3 == 0:
            continue
        mine = scan(d)
        if data is not None:
            theirs = {c["minimum"] for c in data["cycles"] if c["d"] == d and c["discovery"]["discovery_d"] == d}
            if mine != theirs:
                mismatches.append((d, sorted(mine)[:5], sorted(theirs)[:5]))
        rows += 1
    return {"d_values": rows, "compared_with_main": data is not None, "mismatches": mismatches[:10]}


def main():
    out = {"probe": "c001_spectrum_check", "main": "14441c0", "identities_and_gcd": part1(),
           "law_113_2": part2(), "killed_strengthening": part3(), "mechanical_family": part4(),
           "cycle_scan_vs_main": part5(), "result": "PASS"}
    assert not out["cycle_scan_vs_main"]["mismatches"], out["cycle_scan_vs_main"]
    (HERE / "c001_spectrum_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
