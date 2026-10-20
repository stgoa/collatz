"""Recompute the paired-run identities, cylinders and Mersenne mergers of paired_return_audit.json.

Written at the B10-residual-R25-R39 migration; the legacy scripts in this folder load
../complementary_bridge/run_bridge.py (paired_return.py) and
experiments/packet_currents/negative_controls/ (batch_64fff1d_check.py) by their
pre-migration paths and no longer run.

Everything below uses this file's own odd-only Syracuse step, 2-adic valuation and
canonical-set test (B = 1 mod 8, or 3 mod 4 and not selected). It checks:
  1. for every w = 3 mod 8 below 32768: the paired prefixes S^k(3w) = 4z+1,
     S^(k+1)(w) = 2z+1 when h = v2(3w-1) is even; for z = 101 mod 128 the child
     w' = (3z+1)/16 is 3 mod 8 with 0 < 4w' < w; the recognizer's accepted /
     terminal / recursive / unresolved counts against the receipt's seed_domain;
     and, for every accepted w, the prescribed merger S^l(3w) = S^(l+1)(w) by
     direct iteration;
  2. the 72 terminal cylinders (11), k = 1..24, offsets 0, 1, 7;
  3. the 56 recursive integer witnesses (depths 0..24, 32, 48, 64, offsets 0, 1):
     seed bit lengths against the receipt, exactly r recursive k = 1 layers then
     terminal w = 59 mod 128, and the clock S^(3r+3)(3w) = S^(3r+4)(w);
  4. the binary exponent lifts (15) for depths 0..64 and the five tabulated
     classes a_r (199 mod 256, 2887 mod 65536, ...), and the a = 39 mod 2^20 class
     with k word (3, 1);
  5. the eight actual Mersenne roots of the receipt (a = 39, 135, 199, 263, 423,
     455, 711, 2887): identities (1) and (2), k word, bit lengths and the
     same-clock merger S^(a+l)(2^a-1) = S^(a+l)(2^(a-1)-1) by direct iteration;
     and the unresolved a = 7, 23;
  6. the a = 39 conversion: N, x, q, w, f, the hashes of the supplied lower path
     (the orbit of q) and of the output current, and that mersenne_39_current.csv
     is exactly the orbit path of x to 1 (191 rows, coefficient 1, divergence
     delta_x with the row at 1 killed).
It does not rebuild the signed bridge currents and their hashes (legacy checker,
evidence only). Standard library; no files are written.
"""
from pathlib import Path
import csv
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
FAILURES = []


def need(condition, message):
    if not condition:
        FAILURES.append(message)


def v2(n):
    return (n & -n).bit_length() - 1


def S(x):
    if x == 1:
        return 1
    z = 3 * x + 1
    return z >> v2(z)


def it(x, n):
    for _ in range(n):
        x = S(x)
    return x


def selected(x):
    if x % 4 != 3:
        return False
    a = v2(x + 1)
    t = (x + 1) >> a
    return t % 4 == pow(3, a, 4)


def canonical(x):
    return x % 8 == 1 or (x % 4 == 3 and not selected(x))


def plan(w):
    """Return (accepted, layers) with layers = [(w, k, z, kind)]."""
    layers = []
    while True:
        h = v2(3 * w - 1)
        if h % 2:
            return False, layers
        k = h // 2 - 1
        z = 3**k * ((3 * w - 1) >> h)
        if canonical(z):
            layers.append((w, k, z, "terminal"))
            return True, layers
        if z % 128 != 101:
            return False, layers
        child = (3 * z + 1) // 16
        need(child % 8 == 3 and 0 < 4 * child < w, f"child bound at w={w}")
        layers.append((w, k, z, "recursive"))
        w = child


def clock(layers):
    _, k, z, _ = layers[-1]
    length = k + v2(2 * z + 2)
    for _, k, _, _ in layers[:-1]:
        length += k + 2
    return length


def digest(current):
    return hashlib.sha256("".join(f"{x},{c}\n" for x, c in sorted(current.items())).encode()).hexdigest()


def orbit_current(x):
    current = {}
    while x != 1:
        current[x] = current.get(x, 0) + 1
        x = S(x)
    return current


def recursive_cylinder(r):
    mod = 2**(8 * r + 7)
    res = ((7 + 256**r * (229 * 59 - 7) * pow(27**r, -1, mod)) * pow(229, -1, mod)) % mod
    return res, mod


def synthetic(r, offset):
    odd = 27**r
    if odd == 1:
        v = 59 + 128 * offset
    else:
        fixed = (7 * pow(229, -1, odd)) % odd
        index = ((fixed - 59) * pow(128, -1, odd)) % odd
        v = 59 + 128 * (index + offset * odd)
    for _ in range(r):
        need((256 * v - 7) % 27 == 0, f"inverse not integral at depth {r}")
        v = (256 * v - 7) // 27
    return v


def exponent_lift(res, mod):
    bits = mod.bit_length() - 1
    target = 1 + 8 * res
    e = 6
    for j in range(4, bits + 1):
        m = 2**(j + 3)
        if pow(3, e, m) != target % m:
            e += 2**j
        need(pow(3, e, m) == target % m, f"lift failed at bit {j}")
    return e + 1, 2**(bits + 1)


def main():
    receipt = json.loads((HERE / "paired_return_audit.json").read_text())

    # 1. Domain w = 3 mod 8 below 32768.
    counts = dict(accepted=0, terminal=0, recursive=0, unresolved=0)
    for w in range(3, 32768, 8):
        h = v2(3 * w - 1)
        if h % 2 == 0:
            k = h // 2 - 1
            z = 3**k * ((3 * w - 1) >> h)
            need(it(3 * w, k) == 4 * z + 1 and it(w, k + 1) == 2 * z + 1, f"identity (3) at w={w}")
        ok, layers = plan(w)
        if not ok:
            counts["unresolved"] += 1
            continue
        counts["accepted"] += 1
        counts["recursive" if len(layers) > 1 else "terminal"] += 1
        l = clock(layers)
        need(it(3 * w, l) == it(w, l + 1), f"merger clock at w={w}")
    dom = receipt["seed_domain"]
    need(all(dom[key] == counts[key] for key in counts) and dom["cases"] == 4096, f"domain counts {counts}")

    # 2. Terminal cylinders.
    cases = 0
    for k in range(1, 25):
        mod = 2**(2 * k + 5)
        res = ((3**k + 2**(2 * k + 2)) * pow(3**(k + 1), -1, mod)) % mod
        for offset in (0, 1, 7):
            ok, layers = plan(res + offset * mod)
            need(ok and len(layers) == 1 and layers[0][1] == k and layers[0][2] % 8 == 1, f"terminal cylinder k={k}")
            cases += 1
    need(cases == receipt["terminal_cylinders"]["cases"] == 72, "terminal cylinder count")

    # 3. Recursive witnesses.
    rows = receipt["recursive_integer_cases"]
    expected = [(r, o) for r in [*range(25), 32, 48, 64] for o in (0, 1)]
    need([(row["depth"], row["offset"]) for row in rows] == expected, "recursive case list")
    for row in rows:
        r, o = row["depth"], row["offset"]
        res, mod = recursive_cylinder(r)
        w = synthetic(r, o)
        need(w % mod == res and w.bit_length() == row["seed_bits"], f"recursive seed depth {r}")
        ok, layers = plan(w)
        need(ok and len(layers) == r + 1 and all(L[1] == 1 for L in layers), f"recursive word depth {r}")
        need(ok and layers[-1][0] % 128 == 59 and clock(layers) == 3 * r + 3, f"recursive clock depth {r}")
        need(it(3 * w, 3 * r + 3) == it(w, 3 * r + 4), f"recursive merger depth {r}")

    # 4. Exponent lifts.
    table = receipt["first_exponent_cylinders"]
    for r in range(65):
        res, mod = recursive_cylinder(r)
        a, period = exponent_lift(res, mod)
        need(a % 16 == 7 and period == 2 * mod and pow(3, a - 1, 8 * mod) == 1 + 8 * res, f"lift depth {r}")
        if r < 5:
            need(table[r] == dict(depth=r, w_residue=res, w_period=mod, a_residue=a, a_period=period), f"lift row {r}")
    mod = 2**19
    res = ((59 * 4096 - 175) * pow(243, -1, mod)) % mod
    need(exponent_lift(res, mod) == (39, 2**20), "a = 39 class")
    ok, layers = plan(res)
    need(ok and [L[1] for L in layers] == [3, 1], "a = 39 class word")
    sec = receipt["secondary_exponent_cylinder"]
    need((sec["a_residue"], sec["a_period"], sec["k_word"]) == (39, 2**20, [3, 1]), "secondary class row")

    # 5. Actual Mersenne roots.
    for row in receipt["actual_mersenne_bridges"]:
        a = row["a"]
        x, q, N = 2**a - 1, 2**(a - 1) - 1, 12 * 2**(a - 4)
        w = (3**(a - 1) - 1) // 8
        f = 3 * w
        need(q < N < x < 3 * N // 2 and x % 12 == 7, f"root range a={a}")
        need(it(q, a - 1) == w and it(x, a) == 4 * f + 1, f"identity (2) a={a}")
        need(f % 8 == 1 and v2(3 * f + 1) == 2 and S(f) == (3**(a + 1) - 1) // 32, f"identity (1) a={a}")
        ok, layers = plan(w)
        need(ok and [L[1] for L in layers] == row["pair_k_word"], f"k word a={a}")
        t = a + clock(layers)
        need(t == row["equal_prefix_clock"] and it(x, t) == it(q, t), f"merger a={a}")
        need(x.bit_length() == row["root_bits"] and f.bit_length() == row["old_return_bits"], f"bits a={a}")
    need([row["a"] for row in receipt["actual_mersenne_bridges"]] == [39, 135, 199, 263, 423, 455, 711, 2887], "root list")
    for a in receipt["unresolved_mersenne_examples"]:
        need(not plan((3**(a - 1) - 1) // 8)[0], f"a={a} should stay unresolved")
    need(receipt["unresolved_mersenne_examples"] == [7, 23], "unresolved list")

    # 6. The a = 39 conversion.
    conv = receipt["actual_conversion"]
    a = 39
    x, q = 2**a - 1, 2**(a - 1) - 1
    w = (3**(a - 1) - 1) // 8
    need((conv["N"], conv["root"], conv["lower_seed"], conv["known_later_state"], conv["old_canonical_return"])
         == (12 * 2**(a - 4), x, q, w, 3 * w), "conversion values")
    lower, out = orbit_current(q), orbit_current(x)
    need(len(lower) == conv["lower_input_rows"] and digest(lower) == conv["lower_input_sha256"], "lower input hash")
    need(len(out) == conv["output_rows"] and digest(out) == conv["output_sha256"], "output hash")
    with (HERE / "mersenne_39_current.csv").open(newline="") as handle:
        stored = {int(r["state"]): int(r["current"]) for r in csv.DictReader(handle)}
    need(stored == out, "mersenne_39_current.csv is the orbit path of x")
    div = {}
    for s, c in stored.items():
        div[s] = div.get(s, 0) + c
        if S(s) != 1:
            div[S(s)] = div.get(S(s), 0) - c
    need({s: c for s, c in div.items() if c} == {x: 1}, "stored current divergence")

    if FAILURES:
        print(f"FAIL: {len(FAILURES)} checks failed; first: {FAILURES[0]}")
        sys.exit(1)
    print("PASS: 4096 pairs, 72 terminal cylinders, 56 recursive witnesses, 65 exponent lifts, "
          "8 Mersenne mergers and the a = 39 conversion recomputed against paired_return_audit.json")


if __name__ == "__main__":
    main()
