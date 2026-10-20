"""Recompute the mixed shrinking-pair recognizer, its cylinders and mergers against mixed_pairs_audit.json.

Written at the B10-residual-R25-R39 migration; the legacy scripts in this folder load
../second_return/paired_return.py (mixed_pairs.py) and
experiments/packet_currents/negative_controls/ plus fibre_count_check
(batch_r33_r36_check.py) by their pre-migration paths and no longer run.

Everything below uses this file's own odd-only Syracuse step, canonical-set test
and normal form nu. It checks:
  1. for every w = 3 mod 8 below 32768: the paired prefixes (2) and (3) for both
     parities of h; the three-branch recognizer (terminal, O, E1, E2) with every
     child 3 mod 8 and 0 < 2 child < w; the counts accepted / old_accepted (R30's
     terminal-or-E2 rule) / new_accepted / unresolved and the branch uses against
     the receipt; and, for every accepted w, the prescribed merger
     S^l(3w) = S^(l+1)(w) by direct iteration;
  2. the 510 short-word cylinders (all 85 words of length <= 3 over O_0, O_1,
     E1_1, E2_1; terminal k = 1, 2; offsets 0, 1, 7): backward inversion (16) gives
     a residue whose members follow exactly that word, with clock (17) checked by
     direct iteration, and the binary exponent lift (18) gives a = 7 mod 16;
  3. the 28 long words (depth up to 64): seed bit lengths against the receipt,
     the recursion depth and the clock;
  4. the exact binary-cylinder measures 1/6; 1/6, 1/96, 1/192; 32/157; 125/157,
     including the finite partial sums over k;
  5. the six exponent examples (a, period, additional clock) and the four actual
     Mersenne mergers S^t(2^a-1) = S^t(2^(a-1)-1) (a = 39, 631, 2679, 3655) with
     their words and times; the unresolved a = 7, 23;
  6. the rejected unrestricted odd rule at w = 19 (nu(43) = 43, nu(21) = 1);
  7. the a = 631 conversion hashes (the supplied lower path is the orbit of
     2^630 - 1, the output is the orbit of 2^631 - 1) and that pair_499_current.csv
     has divergence delta_1497 - delta_499 and the receipt's hash.
It does not rebuild the signed mixed currents of the long words and Mersenne roots
or their hashes (legacy checker, evidence only). Standard library; no files are
written.
"""
from fractions import Fraction as F
from itertools import product
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


def nu(x):
    while x % 8 == 5:
        x = (x - 1) // 4
    return (x - 1) // 2 if selected(x) else x


def affine(kind, k):
    if kind == "O":
        return 3**(k + 1), -3**k, 2 * k + 3
    return 3**(k + 2), 4**(k + 1) - 3**(k + 1), 2 * k + (5 if kind == "E1" else 6)


def reduction(w):
    h = v2(3 * w - 1)
    if h % 2:
        k = (h - 3) // 2
        z = 3**k * ((3 * w - 1) >> h)
        if z % 8 != 3:
            return ("unresolved", k, z, None)
        kind, child = "O", z
    else:
        k = h // 2 - 1
        z = 3**k * ((3 * w - 1) >> h)
        if canonical(z):
            return ("terminal", k, z, None)
        if z % 64 == 29:
            kind, child = "E1", (3 * z + 1) // 8
        elif z % 128 == 101:
            kind, child = "E2", (3 * z + 1) // 16
        else:
            return ("unresolved", k, z, None)
    A, B, p = affine(kind, k)
    need(child > 0 and 2 * child < w and child % 8 == 3 and A * w + B == 2**p * child, f"child at w={w}")
    return (kind, k, z, child)


def plan(w):
    layers = []
    while True:
        row = reduction(w)
        layers.append(row)
        if row[0] in ("terminal", "unresolved"):
            return row[0] == "terminal", layers
        w = row[3]


def clock(layers):
    _, k, z, _ = layers[-1]
    length = k + v2(2 * z + 2)
    for kind, k, _, _ in layers[:-1]:
        length += k + (1 if kind == "O" else 2)
    return length


def old_accepted(w):
    """R30's rule: terminal or E2 only."""
    while True:
        kind, _, _, child = reduction(w)
        if kind == "terminal":
            return True
        if kind != "E2":
            return False
        w = child


def word_cylinder(word, j=1):
    mod = 2**(2 * j + 5)
    res = ((3**j + 2**(2 * j + 2)) * pow(3**(j + 1), -1, mod)) % mod
    for kind, k in reversed(word):
        A, B, p = affine(kind, k)
        mod *= 2**p
        res = ((2**p * res - B) * pow(A, -1, mod)) % mod
        need(res % 8 == 3, "cylinder residue not 3 mod 8")
    return res, mod


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


def digest(current):
    return hashlib.sha256("".join(f"{x},{c}\n" for x, c in sorted(current.items())).encode()).hexdigest()


def orbit_current(x):
    current = {}
    while x != 1:
        current[x] = current.get(x, 0) + 1
        x = S(x)
    return current


def main():
    receipt = json.loads((HERE / "mixed_pairs_audit.json").read_text())

    # 1. Domain.
    counts = dict(accepted=0, old_accepted=0, new_accepted=0, unresolved=0)
    kinds = dict(O=0, E1=0, E2=0)
    for w in range(3, 32768, 8):
        h = v2(3 * w - 1)
        k = (h - 3) // 2 if h % 2 else h // 2 - 1
        z = 3**k * ((3 * w - 1) >> h)
        need(it(3 * w, k) == (8 * z + 1 if h % 2 else 4 * z + 1), f"left prefix w={w}")
        need(it(w, k + 1) == (4 * z + 1 if h % 2 else 2 * z + 1), f"right prefix w={w}")
        old = old_accepted(w)
        ok, layers = plan(w)
        need(ok or not old, f"old rule accepted but new did not, w={w}")
        counts["old_accepted"] += old
        if not ok:
            counts["unresolved"] += 1
            continue
        counts["accepted"] += 1
        counts["new_accepted"] += not old
        for row in layers[:-1]:
            kinds[row[0]] += 1
        l = clock(layers)
        need(it(3 * w, l) == it(w, l + 1), f"merger clock w={w}")
    dom = receipt["w_domain"]
    need(all(dom[key] == counts[key] for key in counts) and dom["cases"] == 4096, f"domain counts {counts}")
    need(receipt["branch_uses"] == kinds, f"branch uses {kinds}")

    # 2. Short-word cylinders.
    alphabet = (("O", 0), ("O", 1), ("E1", 1), ("E2", 1))
    words = [word for size in range(4) for word in product(alphabet, repeat=size)]
    cases = 0
    for word in words:
        for j in (1, 2):
            res, mod = word_cylinder(word, j)
            a, period = exponent_lift(res, mod)
            need(a % 16 == 7 and period == 2 * mod and pow(3, a - 1, 8 * mod) == 1 + 8 * res, f"lift {word}")
            for offset in (0, 1, 7):
                w = res + offset * mod
                ok, layers = plan(w)
                need(ok and [(r[0], r[1]) for r in layers[:-1]] == list(word), f"word {word}")
                need(ok and layers[-1][1] == j and layers[-1][2] % 8 == 1, f"terminal {word}")
                length = j + 2 + sum(k + (1 if kind == "O" else 2) for kind, k in word)
                need(ok and clock(layers) == length and it(3 * w, length) == it(w, length + 1), f"clock {word}")
                cases += 1
    short = receipt["short_word_cylinders"]
    need((short["words"], short["cases"]) == (len(words), cases) == (85, 510), "short-word counts")

    # 3. Long words.
    long_rows = receipt["long_word_cases"]
    expected = [(d, p) for d in (1, 2, 4, 8, 16, 32, 64)
                for p in ((("O", 0),), (("E1", 1),), (("E2", 1),), alphabet)]
    need(len(long_rows) == 28, "long-word count")
    for row, (depth, pattern) in zip(long_rows, expected):
        need(row["depth"] == depth and [tuple(x) for x in row["pattern"]] == list(pattern), "long-word list")
        word = tuple(pattern[i % len(pattern)] for i in range(depth))
        res, mod = word_cylinder(word)
        ok, layers = plan(res)
        need(ok and len(layers) == depth + 1 and res.bit_length() == row["seed_bits"], f"long word depth {depth}")
        l = clock(layers)
        need(it(3 * res, l) == it(res, l + 1), f"long-word clock depth {depth}")
        a, period = exponent_lift(res, mod)
        need(pow(3, a - 1, 8 * mod) == 1 + 8 * res, f"long-word lift depth {depth}")

    # 4. Exact measures.
    t = F(1, 6)
    masses = dict(O=F(1, 6), E1=F(1, 96), E2=F(1, 192))
    r = sum(masses.values())
    need(r == F(35, 192) and t / (1 - r) == F(32, 157), "measure 32/157")
    for K in (1, 2, 4, 8, 16):
        need(sum(F(1, 2**affine("O", k)[2]) for k in range(K)) == masses["O"] * (1 - F(1, 4**K)), "O partial sum")
        for kind in ("E1", "E2"):
            part = sum(F(1, 2**affine(kind, k)[2]) for k in range(1, K + 1))
            need(part == masses[kind] * (1 - F(1, 4**K)), f"{kind} partial sum")
    need(sum(F(1, 2) * F(1, 4**k) for k in range(1, 40)) == F(1, 6) * (1 - F(1, 4**39)), "terminal mass")
    meas = receipt["exact_relative_binary_measures"]
    need(meas == dict(terminal="1/6", recursive=dict(O="1/6", E1="1/96", E2="1/192"),
                      accepted=str(t / (1 - r)), unresolved=str(1 - t / (1 - r))), "measure strings")

    # 5. Exponent examples and Mersenne mergers.
    for row in receipt["exponent_examples"]:
        word = tuple(tuple(x) for x in row["word"])
        a, period = exponent_lift(*word_cylinder(word))
        extra = 3 + sum(k + (1 if kind == "O" else 2) for kind, k in word)
        need((a, period, extra) == (row["a"], row["period"], row["additional_clock"]), f"exponent example {word}")
    for row in receipt["actual_mersenne_bridges"]:
        a = row["a"]
        x, q, N = 2**a - 1, 2**(a - 1) - 1, 12 * 2**(a - 4)
        w = (3**(a - 1) - 1) // 8
        need(q < N < x < 3 * N // 2 and it(q, a - 1) == w and it(x, a) == 12 * w + 1, f"Mersenne identities a={a}")
        ok, layers = plan(w)
        need(ok and [[r[0], r[1]] for r in layers] == row["word"], f"Mersenne word a={a}")
        tm = a + clock(layers)
        need(tm == row["clock"] and it(x, tm) == it(q, tm), f"Mersenne merger a={a}")
    need([row["a"] for row in receipt["actual_mersenne_bridges"]] == [39, 631, 2679, 3655], "Mersenne list")
    need(receipt["unresolved_exponents"] == [7, 23], "unresolved list")
    for a in (7, 23):
        need(not plan((3**(a - 1) - 1) // 8)[0], f"a={a} should stay unresolved")

    # 6. Rejected unrestricted odd rule.
    kind, k, z, _ = reduction(19)
    need(kind == "unresolved" and v2(3 * 19 - 1) == 3 and z == 7 and nu(43) == 43 and nu(21) == 1, "w = 19")
    need(receipt["rejected_unrestricted_odd_rule"] == dict(w=19, z=7, left_normal=43, right_normal=1), "w = 19 row")

    # 7. Conversion hashes and the stored P(499) current.
    conv = receipt["supplied_conversion"]
    a = conv["a"]
    lower, out = orbit_current(2**(a - 1) - 1), orbit_current(2**a - 1)
    need(a == 631 and len(lower) == conv["input_rows"] and digest(lower) == conv["input_sha256"], "lower input")
    need(len(out) == conv["output_rows"] and digest(out) == conv["output_sha256"], "output current")
    known = {1} | {nu(v) for v in lower}
    need(2**a - 1 not in known and (3**a - 3) // 8 not in known, "root and old return outside supplied saturation")
    with (HERE / "pair_499_current.csv").open(newline="") as handle:
        stored = {int(row["state"]): int(row["current"]) for row in csv.DictReader(handle)}
    div = {}
    for s, c in stored.items():
        div[s] = div.get(s, 0) + c
        if S(s) != 1:
            div[S(s)] = div.get(S(s), 0) - c
    need({s: c for s, c in div.items() if c} == {1497: 1, 499: -1}, "P(499) divergence")
    small = receipt["small_current"]
    need(small["w"] == 499 and small["rows"] == len(stored) and small["sha256"] == digest(stored), "P(499) hash")
    need(plan(499)[0], "P(499) accepted")

    if FAILURES:
        print(f"FAIL: {len(FAILURES)} checks failed; first: {FAILURES[0]}")
        sys.exit(1)
    print("PASS: 4096 pairs, 510 mixed cylinders, 28 long words, measure 32/157, 4 Mersenne mergers, "
          "conversion hashes and P(499) recomputed against mixed_pairs_audit.json")


if __name__ == "__main__":
    main()
