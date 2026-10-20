"""Self-contained recomputation of the halving identity and its exact residual count.

Written at the B09-residual-R11-R24 migration; the legacy scripts in this folder
load ../complement_recursion/transfer.py (and through it R14, R16, R17 code) by
their pre-migration paths and no longer run. Standard library, exact integers.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

Checks:
  - identity (1): S^a(x) = S^a((x-1)/2) for every selected x = 2^a t - 1
    (a = v2(x+1) >= 2, t odd, t = 3^a mod 4) with x < 2^16, and for x > 3 neither
    prefix reaches 1 before step a; the selected classes are exactly (3);
  - the selected and remaining masses of R_N: explicit enumeration of the
    profile R_N agrees with the CRT floor formula (7) for every N divisible by 8
    up to 4096, |R'_N - 25N/576| <= 6A with A = floor(log2(3N/2)), and the
    formula reproduces every large_exact_formula_cases row of the legacy receipt
    halving_return_audit.json (cutoffs up to about 3.3*10^238);
  - N = 6144: 263 of the 532 residual units are selected;
  - the complementary counterexample x = 27 (S^2(27) = 31, S^2(13) = 1), the
    coefficient-2 example at N = 72, root 79, and the seven required-ray
    excursions x = 2^a - 1 (peak and common state) of the receipt.
"""

import json
import sys
from fractions import Fraction
from math import ceil, floor
from pathlib import Path

HERE = Path(__file__).resolve().parent
failures = []


def require(ok, message):
    if not ok:
        failures.append(message)


def v2(n):
    return (n & -n).bit_length() - 1


def S(x):
    z = 3 * x + 1
    return z >> v2(z)


def selected(x):
    a = v2(x + 1)
    t = (x + 1) >> a
    return a >= 2 and t % 4 == pow(3, a, 4)


def C(L, H, r, m):
    L, H = Fraction(L), Fraction(H)
    return ceil((H - r) / m) - floor((L - r) / m) - 1


def profile(N):
    R = {}
    for x in range(N + 1, 3 * N // 2, 2):
        if x % 12 == 3 or (x % 12 == 7 and 8 * x > 9 * N):
            R[x] = 1
        elif x % 36 in (7, 19) and 8 * x < 9 * N:
            R[x] = 2
    return R


def profile_mass(N):
    return (C(N, Fraction(3 * N, 2), 3, 12) + C(Fraction(9 * N, 8), Fraction(3 * N, 2), 7, 12)
            + 2 * C(N, Fraction(9 * N, 8), 7, 36) + 2 * C(N, Fraction(9 * N, 8), 19, 36))


def selected_mass(N):
    """Formula (7)."""
    A = (3 * N // 2).bit_length() - 1
    total = 0
    for a in range(2, A + 1):
        b = (2 ** a - 1) if a % 2 == 0 else (3 * 2 ** a - 1)
        p = 2 ** (a + 2)
        b %= p
        terms = ((N, Fraction(3 * N, 2), 3, 12, 1), (Fraction(9 * N, 8), Fraction(3 * N, 2), 7, 12, 1),
                 (N, Fraction(9 * N, 8), 7, 36, 2), (N, Fraction(9 * N, 8), 19, 36, 2))
        for L, H, r, m, w in terms:
            q = m // 4
            k = ((r - b) * pow(p, -1, q)) % q
            total += w * C(L, H, b + p * k, p * q)
    return total


def main():
    for x in range(3, 2 ** 16, 4):
        a = v2(x + 1)
        cls = (2 ** a - 1) if a % 2 == 0 else (3 * 2 ** a - 1)
        require(selected(x) == (x % 2 ** (a + 2) == cls % 2 ** (a + 2)), f"class (3) at x={x}")
        if not selected(x):
            continue
        u, q = x, (x - 1) // 2
        for j in range(a):
            if x > 3:
                require(u != 1 and q != 1, f"x={x}: a prefix reached 1 early")
            u, q = S(u), S(q)
        require(u == q, f"x={x}: S^a(x) != S^a((x-1)/2)")
    for N in range(8, 4097, 8):
        R = profile(N)
        G = sum(c for x, c in R.items() if selected(x))
        total = sum(R.values())
        require(total == profile_mass(N), f"N={N}: profile mass")
        require(G == selected_mass(N), f"N={N}: selected mass {G} != formula {selected_mass(N)}")
        A = (3 * N // 2).bit_length() - 1
        require(abs(Fraction(total - G) - Fraction(25 * N, 576)) <= 6 * A, f"N={N}: remaining-mass bound")
    receipt = json.loads((HERE / "halving_return_audit.json").read_text())
    for row in receipt["large_exact_formula_cases"]:
        N = row["N"]
        g = selected_mass(N)
        require((g, profile_mass(N) - g) == (row["selected_mass"], row["remaining_mass"]), f"receipt row N={N}")
    R = profile(6144)
    require((sum(c for x, c in R.items() if selected(x)), sum(R.values())) == (263, 532), "N=6144: 263 of 532")
    cc = receipt["complementary_counterexample"]
    require(profile(24).get(27) == 1 and not selected(27) and S(S(27)) == 31 and S(S(13)) == 1
            and (cc["root_two_steps"], cc["smaller_two_steps"]) == (31, 1), "complementary counterexample")
    ex = receipt["coefficient_two_example"]
    left, right = [79], [39]
    for _ in range(4):
        left.append(S(left[-1]))
        right.append(S(right[-1]))
    require(profile(72).get(79) == 2 and selected(79) and left == ex["left"] and right == ex["right"],
            "coefficient-2 example at N = 72")
    for row in receipt["required_ray_excursions"]:
        a = row["a"]
        x, N = 2 ** a - 1, 12 * 2 ** (a - 4)
        orbit = [x]
        for _ in range(a):
            orbit.append(S(orbit[-1]))
        require(N == row["N"] and profile(N).get(x) == 1 if a <= 16 else N == row["N"], f"excursion a={a}: root")
        require(selected(x) and orbit[a - 1] == 2 * 3 ** (a - 1) - 1 == row["peak_before_coalescence"]
                and orbit[a] == row["common_state"] and all(y > x for y in orbit[1:a]), f"excursion a={a}")
    if failures:
        print("FAIL: " + "; ".join(failures[:10]))
        sys.exit(1)
    print(f"PASS: halving identity for selected x < 2^16; formula (7) = enumeration for 512 cutoffs; "
          f"{len(receipt['large_exact_formula_cases'])} receipt rows; 263 of 532 at N = 6144; examples")


if __name__ == "__main__":
    main()
