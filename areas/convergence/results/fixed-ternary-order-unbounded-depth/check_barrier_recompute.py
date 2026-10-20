"""Self-contained recomputation of the finite barrier certificate of the fixed-h theorem.

Written at the B09-residual-R11-R24 migration; the legacy checker in this folder
imports inverse_exposure_probe from ../templates/ by its pre-migration path and
no longer runs. Standard library, exact integers.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

It recomputes, and compares with finite_barrier_certificate in fixed_h_audit.json:
  - the union of the Syracuse orbits of the odd integers 1..33 (each reaches 1),
    the stated 54-element set;
  - every triple (z0, u0, c0) with z0 in that set, u0 = 2^s 3^r >= 4, 9u0 < z0 < 10u0,
    c0 = 10u0 - z0: exactly the 22 stored candidates;
  - for each candidate with c0 > 1, the orbit of c0 under T_-(c) = (3c-1)/2^v2(3c-1)
    enters the cycle {5, 7} or {17, 25, 37, 55, 41, 61, 91} and never meets 1
    (the stored negative orbits, path and cycle);
  - for every depth D = 1..64, an exponent e with 2^e = 10 mod 3^(D+2) exists,
    is divisible by 6, and X = 2^e has v3(X-1) = 2 (the required-ladder realization).
It does not recompute the complete exposed components (they need the inverse oracle).
"""

import json
import sys
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


def T_minus(c):
    z = 3 * c - 1
    return z >> v2(z)


def v3(n):
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def negative_orbit(c):
    path, seen = [], {}
    x = c
    while x not in seen:
        if x == 1:
            return None
        seen[x] = len(path)
        path.append(x)
        x = T_minus(x)
        if len(path) > 1000:
            return None
    start = seen[x]
    return dict(c=c, path=path, repeat=x, cycle=path[start:])


def main():
    stored = json.loads((HERE / "fixed_h_audit.json").read_text())["finite_barrier_certificate"]
    union = set()
    for s in range(1, 34, 2):
        x, steps = s, 0
        union.add(x)
        while x != 1:
            x = S(x)
            union.add(x)
            steps += 1
            require(steps < 1000, f"orbit of {s} did not reach 1")
            if steps >= 1000:
                break
    require(sorted(union) == stored["positive_orbit_union"] and len(union) == 54, "positive orbit union")
    candidates = []
    for z in sorted(union):
        for s in range(0, 20):
            for r in range(0, 13):
                u = 2 ** s * 3 ** r
                if u >= 4 and 9 * u < z < 10 * u:
                    candidates.append((z, u, 10 * u - z))
    candidates.sort()
    require(candidates == sorted((c["z"], c["u"], c["c"]) for c in stored["candidates"]) and len(candidates) == 22,
            "candidate triples")
    cycles = ({5, 7}, {17, 25, 37, 55, 41, 61, 91})
    orbits = {o["c"]: o for o in stored["negative_orbits"]}
    for c in sorted({c for _, _, c in candidates if c > 1}):
        o = negative_orbit(c)
        require(o is not None and set(o["cycle"]) in cycles, f"c0={c} must cycle away from 1")
        require(o == orbits.get(c), f"c0={c}: negative orbit differs from the receipt")
    require(len(orbits) == 12, "twelve distinct c0 > 1")
    for D in range(1, 65):
        mod = 3 ** (D + 2)
        e = next(e for e in range(0, 2 * 3 ** (D + 1)) if pow(2, e, mod) == 10 % mod) if D <= 8 else None
        if e is None:  # lift one ternary digit at a time, as in the README
            e, order, m = 0, 2, 3
            while m < mod:
                m *= 3
                e = next(c for c in (e, e + order, e + 2 * order) if pow(2, c, m) == 10 % m)
                order *= 3
        require(pow(2, e, mod) == 10 % mod and e % 6 == 0, f"D={D}: ladder exponent")
        # X = 10 mod 27 means X - 1 = 9 mod 27, so v3(X - 1) = 2 exactly
        require(pow(2, e, 27) == 10 and v3(10 - 1) == 2, f"D={D}: v3(X-1) = 2")
    if failures:
        print("FAIL: " + "; ".join(failures[:10]))
        sys.exit(1)
    print("PASS: 54-state positive orbit union, 22 candidates, 12 negative-map orbits away from 1, "
          "ladder exponents for D = 1..64")


if __name__ == "__main__":
    main()
