"""Self-contained recomputation of the two 1-mod-8 entry branches and their actual Mersenne mergers (pair_one_audit.json).

Written at the B10-residual-R25-R39 migration; the legacy scripts in this folder
load ../paired_completion/mixed_pairs.py (and through it the R30, R26, R25 and
R23 code) by their pre-migration paths and no longer run. Standard library,
exact integers. Run from the repository root: python3 <this file>. Exits 1 on
any failure; writes nothing.

Checks, with its own odd-only Syracuse step S and canonical test:
  - over the 4096 odd w = 1 mod 8 below 32768: branch A (w = 17 mod 128) has
    exactly 256 inputs and branch B (w = 105 mod 256) exactly 128, the rest
    (3712) are parent-unresolved, as in the receipt's direct_domains; for every
    A input, with w = 16u + 1 and v = 3u: S(3w) = 4(18u+1) + 1, S(w) = 4(3u) + 1,
    9u canonical and 1 mod 8 (so 18u+1 is its selected partner), v = 3 mod 8 and
    0 < v < w; for every B input, with v = (9w-1)/16: S^2(3w) = 2(3v) + 1,
    S^2(w) = 2v + 1 with valuations (1,2) and (2,1), v = 11 mod 16, v and 3v
    canonical, 0 < v < w;
  - the binary exponent lift (5) for the two terminal parent cylinders:
    w = 1681 mod 2048 gives a = 1699 mod 4096 and w = 105 mod 2048 gives
    a = 659 mod 4096, matching the receipt's empty-word exponent_lifts;
  - the four actual Mersenne bridges of the receipt (a = 659, 1699, 4755, 5795):
    each a lies in its class, (3^(a-1)-1)/8 is in the A or B parent domain, and
    S^t(2^a - 1) = S^t(2^(a-1) - 1) at the receipt's clock t = a + 4 (A) or
    a + 5 (B), by direct iteration;
  - the stored current pair_315_current.csv: 11 rows of coefficient 1 forming
    the actual path of 315 to 1 (divergence delta_315 with the row at 1 killed).
It does not rebuild the mixed-word acceptances, the current hashes or the
supplied a = 659 conversion (legacy checker, evidence only).
"""

import csv
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
    if x == 1:
        return 1
    y = 3 * x + 1
    return y >> v2(y)


def selected(x):
    a = v2(x + 1)
    t = (x + 1) >> a
    return x % 4 == 3 and t % 4 == pow(3, a, 4)


def canonical(q):
    return q % 8 == 1 or (q % 4 == 3 and not selected(q))


def lift(c, m):
    """All a = 3 mod 16 modulo 2^(m+1) with 3^(a-1) = 1 + 8c mod 2^(m+3), by exhaustion."""
    return [a for a in range(3, 2 ** (m + 1), 16) if pow(3, a - 1, 2 ** (m + 3)) == (1 + 8 * c) % 2 ** (m + 3)]


def main():
    receipt = json.loads((HERE / "pair_one_audit.json").read_text())
    count_a = count_b = 0
    for w in range(1, 32768, 8):
        if w % 128 == 17:
            count_a += 1
            u = (w - 1) // 16
            v = 3 * u
            ok = (S(3 * w) == 4 * (18 * u + 1) + 1 and S(w) == 4 * v + 1 and canonical(9 * u)
                  and (9 * u) % 8 == 1 and v % 8 == 3 and 0 < v < w)
            require(ok, f"branch A at w={w}")
        elif w % 256 == 105:
            count_b += 1
            v = (9 * w - 1) // 16
            ok = (S(S(3 * w)) == 2 * (3 * v) + 1 and S(S(w)) == 2 * v + 1
                  and v2(9 * w + 1) == 1 and v2(3 * S(3 * w) + 1) == 2
                  and v2(3 * w + 1) == 2 and v2(3 * S(w) + 1) == 1
                  and v % 16 == 11 and canonical(v) and canonical(3 * v) and 0 < v < w)
            require(ok, f"branch B at w={w}")
    dom = receipt["direct_domains"]
    require(dom["inputs"] == 4096 and dom["A"] == count_a == 256 and dom["B"] == count_b == 128
            and dom["parent_unresolved"] == 4096 - count_a - count_b, "direct domains")

    lifts = {(r["kind"], r["a"], r["period"]) for r in receipt["exponent_lifts"] if not r["word"]}
    require(lift(1681, 11) == [1699] and lift(105, 11) == [659]
            and lifts == {("A", 1699, 4096), ("B", 659, 4096)}, "terminal exponent lifts")

    for row in receipt["actual_mersenne_bridges"]:
        a, t = row["a"], row["clock"]
        w = (3 ** (a - 1) - 1) // 8
        kind = "A" if a % 4096 == 1699 else "B" if a % 4096 == 659 else None
        good = kind is not None and ((kind == "A" and w % 128 == 17 and t == a + 4)
                                     or (kind == "B" and w % 256 == 105 and t == a + 5))
        x, q = 2 ** a - 1, 2 ** (a - 1) - 1
        for _ in range(t):
            x, q = S(x), S(q)
        require(good and x == q, f"Mersenne bridge a={a}")

    with (HERE / "pair_315_current.csv").open(newline="") as source:
        table = {int(r["state"]): int(r["current"]) for r in csv.DictReader(source)}
    path, y = [], 315
    while y != 1:
        path.append(y)
        y = S(y)
    small = receipt["small_current"]
    require(table == {s: 1 for s in path} and len(table) == small["rows"] == 11
            and small["root"] == 315 and small["lower"] == 105, "stored current at 315")

    if failures:
        print("FAIL: " + "; ".join(failures[:10]))
        sys.exit(1)
    print(f"PASS: branch A on {count_a} and branch B on {count_b} of 4096 inputs; terminal lifts 1699, 659 "
          "mod 4096; four Mersenne mergers; stored current at 315")


if __name__ == "__main__":
    main()
