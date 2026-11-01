#!/usr/bin/env python3
"""Certificate for inverse-syracuse-binary-coding.

Raw odd-only map S(n) = (3n+1)/2^v, v = v_2(3n+1), on positive odd integers. On U = {n odd, 3 does not divide n}:
    G_b(n) = (2^(a_b(n mod 9)) n - 1)/3,   b in {0, 1},
with the exponent table A below; Gamma(empty) = 1, Gamma(b w) = G_b(Gamma(w)).
V1  the table: for every residue r in {1,2,4,5,7,8} mod 9 and b in {0,1}, 2^a r mod 9 is 4 or 7; exponents for b = 0 lie in
    [3, 6] and for b = 1 in [7, 10] (disjoint bands, both disjoint from the valuation 2 of S at 1);
V2  for every n in U below N_TABLE and b: G_b(n) is an odd integer, not divisible by 3, G_b(n) > 2n, and S(G_b(n)) = n with
    valuation exactly a_b(n mod 9);
V3  for every binary word of length <= L_MAX: Gamma(w) is decoded back to w by the forward orbit (valuation band gives the
    bit, the table at the successor confirms it), reaches 1 after exactly |w| odd steps, satisfies 2^|w| < Gamma(w) < 2^(10|w|)
    for |w| >= 1, and all Gamma(w) are distinct;
V4  the decoder rejects every odd x < N_DECODE that is not a codeword, and accepts exactly the codewords below N_DECODE;
V5  the PCP equivalence on random instances: for random lists of pairs of binary words and every index sequence of length
    <= T_MAX, Gamma(u_i1...u_it) = Gamma(v_i1...v_it) iff u_i1...u_it = v_i1...v_it;
V6  receipt comparison. Exit 1 on failure; --write-receipt regenerates binary_coding.json. Standard library only;
    deterministic (fixed seed)."""
import itertools
import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "binary_coding.json"
A = {0: {1: 4, 2: 3, 4: 6, 5: 3, 7: 4, 8: 5},
     1: {1: 8, 2: 7, 4: 8, 5: 9, 7: 10, 8: 7}}
N_TABLE, L_MAX, N_DECODE, T_MAX = 200000, 14, 2 ** 22, 5
failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL:", msg)


def v2(n):
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def G(b, n):
    return (2 ** A[b][n % 9] * n - 1) // 3


def gamma(word):
    x = 1
    for bit in reversed(word):
        x = G(bit, x)
    return x


def decode(x):
    """The word w with Gamma(w) = x, or None. Each step at least halves x, so it terminates."""
    word = []
    while x != 1:
        if x % 2 == 0 or x % 3 == 0:
            return None
        v = v2(3 * x + 1)
        n = (3 * x + 1) >> v
        if n % 3 == 0:
            return None
        if 3 <= v <= 6:
            b = 0
        elif 7 <= v <= 10:
            b = 1
        else:
            return None
        if A[b][n % 9] != v:
            return None
        word.append(b)
        x = n
    return word


def main():
    write = "--write-receipt" in sys.argv
    s = {}
    # V1
    for b in (0, 1):
        for r, a in A[b].items():
            if pow(2, a, 9) * r % 9 not in (4, 7):
                fail(f"V1: 2^{a}*{r} mod 9 not in {{4,7}} (b={b})")
    bands = (sorted(set(A[0].values())), sorted(set(A[1].values())))
    if not (max(bands[0]) <= 6 and min(bands[0]) >= 3 and min(bands[1]) >= 7 and max(bands[1]) <= 10):
        fail("V1: bands not [3,6] and [7,10]")
    s["V1"] = {"table": {str(b): {str(r): a for r, a in A[b].items()} for b in (0, 1)}, "bands": [list(x) for x in bands]}
    print("V1: table entries give 2^a r = 4 or 7 (mod 9); bands", bands)
    # V2
    count = 0
    for n in range(1, N_TABLE, 2):
        if n % 3 == 0:
            continue
        for b in (0, 1):
            g = G(b, n)
            if (2 ** A[b][n % 9] * n - 1) % 3 or g % 2 == 0 or g % 3 == 0 or g <= 2 * n:
                fail(f"V2: G_{b}({n}) = {g} fails integrality, oddness, 3-freeness or growth")
            if v2(3 * g + 1) != A[b][n % 9] or (3 * g + 1) >> A[b][n % 9] != n:
                fail(f"V2: S(G_{b}({n})) != {n} with valuation {A[b][n % 9]}")
            count += 1
    s["V2"] = {"pairs_checked": count, "n_below": N_TABLE}
    print(f"V2: {count} pairs (n, b) with n < {N_TABLE}: integral, odd, prime to 3, > 2n, one Syracuse step back with the table valuation")
    # V3
    seen, words = {}, 0
    for m in range(L_MAX + 1):
        for w in itertools.product((0, 1), repeat=m):
            w = list(w)
            x = gamma(w)
            if decode(x) != w:
                fail(f"V3: decoding fails for {w}")
            y, steps = x, 0
            while y != 1:
                y = (3 * y + 1) >> v2(3 * y + 1)
                steps += 1
            if steps != m:
                fail(f"V3: {w} reaches 1 after {steps} odd steps, not {m}")
            if m >= 1 and not (2 ** m < x < 2 ** (10 * m)):
                fail(f"V3: size bound fails for {w}")
            if x in seen:
                fail(f"V3: collision {w} and {seen[x]}")
            seen[x] = w
            words += 1
    s["V3"] = {"words": words, "max_length": L_MAX, "distinct_codewords": len(seen)}
    print(f"V3: {words} words of length <= {L_MAX}: decoded, reach 1 in |w| odd steps, 2^|w| < Gamma < 2^(10|w|), all distinct")
    # V4
    small_codes = {x for x in seen if x < N_DECODE}
    accepted = set()
    for x in range(1, N_DECODE, 2):
        if decode(x) is not None:
            accepted.add(x)
    if accepted != small_codes:
        extra = sorted(accepted - small_codes)[:5]
        missing = sorted(small_codes - accepted)[:5]
        # codewords of length > L_MAX below N_DECODE are impossible since Gamma > 2^m and ... check explicitly
        fail(f"V4: decoder acceptances differ from codewords: extra {extra}, missing {missing}")
    s["V4"] = {"odd_x_below": N_DECODE, "codewords_found": len(accepted)}
    print(f"V4: below {N_DECODE} the decoder accepts exactly the {len(accepted)} codewords")
    # V5
    rng = random.Random(20261101)
    instances, sequences, solutions = 0, 0, 0
    for _ in range(300):
        k = rng.randint(2, 4)
        pairs = [([rng.randint(0, 1) for _ in range(rng.randint(1, 3))],
                  [rng.randint(0, 1) for _ in range(rng.randint(1, 3))]) for _ in range(k)]
        instances += 1
        for t in range(1, T_MAX + 1):
            for idx in itertools.product(range(k), repeat=t):
                u = [bit for i in idx for bit in pairs[i][0]]
                v = [bit for i in idx for bit in pairs[i][1]]
                eq_codes = gamma(u) == gamma(v)
                if eq_codes != (u == v):
                    fail(f"V5: equivalence fails for {pairs}, {idx}")
                sequences += 1
                solutions += eq_codes
    s["V5"] = {"instances": instances, "index_sequences": sequences, "solutions_found": solutions, "seed": 20261101}
    print(f"V5: {instances} random PCP instances, {sequences} index sequences of length <= {T_MAX}: "
          f"codeword equality iff word equality ({solutions} solutions)")
    if write:
        RECEIPT.write_text(json.dumps(s, indent=1) + "\n")
        print("receipt written")
    elif not RECEIPT.exists():
        fail("V6 receipt missing")
    elif json.loads(RECEIPT.read_text()) != s:
        fail("V6 summary differs from the receipt")
    if failures:
        print(f"{len(failures)} failure(s)")
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()
