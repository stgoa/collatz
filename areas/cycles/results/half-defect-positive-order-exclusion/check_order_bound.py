"""Exact algebra and actual-cycle controls for the paired-order exclusion.

The README proves the unbounded result. This standard-library certificate
checks polynomial identities, the finite arithmetic used in that proof, and
explicitly bounded actual-cycle controls. No absence in the grid is used as
a general exclusion. Default execution compares a deterministic receipt;
--write-receipt regenerates it. Checks remain active under Python -O.
"""

from collections import Counter
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FIXTURES = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
RECEIPT = HERE / "check_order_bound.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def intercept(word):
    total = value = 0
    for letter in word:
        value = 3 * value + 2**total
        total += letter
    return value


def rotate(word, offset):
    return word[offset:] + word[:offset]


def raise_last(word, extra):
    return word[:-1] + (word[-1] + extra,)


def replay(word, d, states):
    require(len(word) == len(states) and len(word) > 0, "cycle length")
    require(d > 0 and d % 2 == 1, "positive odd addend")
    for i, (letter, state) in enumerate(zip(word, states)):
        require(letter > 0 and state > 0 and state % 2 == 1, "positive odd state and letter")
        raw = 3 * state + d
        valuation = (raw & -raw).bit_length() - 1
        require(valuation == letter, "exact actual valuation")
        require(raw == 2**letter * states[(i + 1) % len(word)], "closed actual arrow")
    return len(word)


def actual_cycle(word):
    gap = 2**sum(word) - 3**len(word)
    require(gap > 0, "positive word gap")
    common = gcd(gap, intercept(word))
    d = gap // common
    state = intercept(word) // common
    states = []
    for letter in word:
        states.append(state)
        raw = 3 * state + d
        require(raw % 2**letter == 0, "integral constructed arrow")
        state = raw // 2**letter
    require(state == states[0], "constructed closure")
    replay(word, d, states)
    for i, current in enumerate(states):
        ci = intercept(rotate(word, i))
        cn = intercept(rotate(word, (i + 1) % len(word)))
        require(ci == common * current, "independent rotated-intercept reconstruction")
        require(2**word[i] * cn == 3 * ci + gap, "rotation identity")
        require(ci % 2 == 1 and gcd(ci, gap) == common, "oddness and rotation-invariant gcd")
    return gap, d, states


# Sparse integer polynomials in P,R,Q,S,k,l,H,L. They certify algebraic
# equalities, not positivity assumptions or finite-sample extrapolations.
ZERO_MONOMIAL = (0,) * 8


def const(value):
    return {ZERO_MONOMIAL: value} if value else {}


def variable(index):
    powers = [0] * 8
    powers[index] = 1
    return {tuple(powers): 1}


def add(*polys):
    out = Counter()
    for poly in polys:
        for powers, coefficient in poly.items():
            out[powers] += coefficient
    return {powers: coefficient for powers, coefficient in out.items() if coefficient}


def scale(poly, value):
    return {powers: value * coefficient for powers, coefficient in poly.items() if value * coefficient}


def sub(left, right):
    return add(left, scale(right, -1))


def mul(*polys):
    out = const(1)
    for poly in polys:
        nxt = Counter()
        for p, cp in out.items():
            for q, cq in poly.items():
                nxt[tuple(x + y for x, y in zip(p, q))] += cp * cq
        out = {powers: coefficient for powers, coefficient in nxt.items() if coefficient}
    return out


def polynomial_identities():
    P, R, Q, S, k, l, H, L = (variable(i) for i in range(8))
    one = const(1)
    km = sub(k, one)
    lm = sub(l, one)
    factor = mul(km, lm)
    xn = mul(sub(mul(Q, H), mul(R, L)), km)
    tn = mul(add(mul(S, L), mul(P, H)), lm)
    yn = add(xn, mul(Q, H, factor))
    zn = add(tn, mul(S, L, factor))
    first = add(mul(add(mul(k, Q, S, lm), mul(P, R, km)), L),
                mul(P, Q, sub(l, k), H))
    second = sub(mul(sub(mul(l, Q, S, km), mul(P, R, lm)), H),
                 mul(R, S, sub(mul(k, l), one), L))
    identities = {
        "first_difference": sub(mul(Q, sub(zn, mul(k, tn))), mul(P, sub(xn, yn))),
        "second_difference": sub(mul(S, sub(yn, mul(l, xn))), mul(R, sub(zn, tn))),
        "retained_first_intercept": sub(sub(mul(Q, zn), mul(P, xn)), first),
        "retained_second_intercept": sub(sub(mul(S, yn), mul(R, zn)), second),
    }
    # Q,S stand for the independent X,Y in the norm expansion.
    norm = sub(mul(k, l, add(Q, S), add(Q, S)),
               mul(add(Q, mul(k, S)), add(Q, mul(k, S))))
    expanded = add(mul(sub(mul(k, l), one), Q, Q),
                   scale(mul(k, lm, Q, S), 2), mul(k, sub(l, k), S, S))
    identities["quadratic_norm"] = sub(norm, expanded)
    # L stands for a nonnegative scalar slack in each universal comparison.
    l2 = add(scale(k, 2), L)
    gap2 = sub(scale(mul(k, sub(l2, k)), 2), mul(km, sub(l2, one)))
    identities["dyadic_ratio_slack"] = sub(gap2, add(mul(add(k, one), L), scale(k, 3), const(-1)))
    lsquare = add(mul(k, k), L)
    gapsquare = sub(mul(k, sub(lsquare, k)), mul(km, sub(lsquare, one)))
    identities["strong_ratio_slack"] = sub(gapsquare, add(L, k, const(-1)))
    for name, residual in identities.items():
        require(not residual, f"nonzero polynomial residual: {name}")
    return {"variables": ["P", "R", "Q", "S", "k", "l", "H", "L"],
            "zero_residual_identities": sorted(identities)}


def finite_arithmetic():
    require(3**5 < 2**8, "first integer-power comparison")
    require(40**8 < 2**13 * 13**8, "minimum-thirteen product comparison")
    chains = {}
    for seed in range(1, 13, 2):
        state = seed
        chain = [state]
        while state != 1:
            require(len(chain) < 20, "small-state descent bound")
            raw = 3 * state + 1
            state = raw // (raw & -raw)
            chain.append(state)
        chains[str(seed)] = chain
    scalar_count = 0
    for p in range(1, 65):
        for q in range(p + 1, 129):
            k, l = 2**p, 2**q
            require((k - 1) * (l - 1) < 2 * k * (l - k), "general ratio")
            if q >= 2 * p:
                require((k - 1) * (l - 1) < k * (l - k), "strong ratio")
            scalar_count += 1
    return {"three_fifth": 3**5, "two_eighth": 2**8,
            "forty_eighth": 40**8, "product_upper": 2**13 * 13**8,
            "small_odd_seed_chains": chains, "ratio_controls": scalar_count,
            "ratio_range": "1<=p<=64, p<q<=128; universal proof uses the polynomial slack identities"}


def family_case(A, B, p, q):
    a, b = len(A), len(B)
    P, R, Q, S = 3**a, 3**b, 2**sum(A), 2**sum(B)
    k, l = 2**p, 2**q
    word = A + B + raise_last(A, p) + raise_last(B, q)
    gap = 2**sum(word) - 3**len(word)
    if gap <= 0:
        return None
    gap, d, states = actual_cycle(word)
    x, z, y, t = states[0], states[a], states[a + b], states[2 * a + b]
    ca, cb = intercept(A), intercept(B)
    require(2**a * ca < P * Q, "first intercept bound")
    require(2**b * cb < R * S, "second intercept bound")
    require(Q * z == P * x + d * ca and k * Q * t == P * y + d * ca, "A endpoints")
    require(S * y == R * z + d * cb and l * S * x == R * t + d * cb, "B endpoints")
    require(x < y and (y - x) % Q == 0 and (z - t) % S == 0, "paired order and integrality")
    H, L = (y - x) // Q, (z - t) // S
    require(H > 0 and H % 2 == 1 and L % 2 == 1 and L != 0, "exact quotient parity")
    require((l - 1) * x == Q * H - R * L and (k - 1) * t == S * L + P * H, "solved states")
    factor = (k - 1) * (l - 1)
    require(d * factor * ca == (k * Q * S * (l - 1) + P * R * (k - 1)) * L
            + P * Q * (l - k) * H, "first retained identity")
    require(d * factor * cb == (l * Q * S * (k - 1) - P * R * (l - 1)) * H
            - R * S * (k * l - 1) * L, "second retained identity")
    sign = intercept(rotate(word, a)) - intercept(rotate(word, 2 * a + b))
    require((sign > 0) == (L > 0) and (sign < 0) == (L < 0), "pure-word sign equivalence")
    require(sum(v != word[(i + a + b) % len(word)] for i, v in enumerate(word)) == 4,
            "four half-period mismatches")
    X, Y = R * ca, Q * cb
    cu, cv = intercept(A + B), intercept(raise_last(A, p) + raise_last(B, q))
    require(cu == X + Y and cv == X + k * Y, "two half intercepts")
    norm = k * l * cu**2 - cv**2
    require(norm == (k * l - 1) * X**2 + 2 * k * (l - 1) * X * Y + k * (l - k) * Y**2,
            "factored norm")
    require(d**2 * norm % gap == 0, "norm consequence with actual addend")
    if p < q and L > 0:
        require(d * factor > 2**a * H * (l - k), "retained H bound")
        require(2**a * H * (l - k) * 2**(p + 1) > 2**a * factor,
                "strict dyadic bound")
        require(d * P * (k - 1) > 2**a * k * S * L, "retained L bound")
        require(d * P > 2**a * S and d * 2**(p + 1) > 2**a, "weaker displayed bounds")
        require(d > 1, "positive-order integer-cycle exclusion control")
        if q >= 2 * p:
            require(d * 2**p > 2**a, "strong defect ratio bound")
    if p >= q:
        require(L > 0, "automatic order for reverse or equal magnitudes")
    return {"word": list(word), "addend": d, "boundaries": [x, z, y, t],
            "H": H, "L": L, "arrows": len(word)}


def cycle_grid():
    words = [word for length in range(1, 4) for word in product(range(1, 4), repeat=length)]
    counts = Counter()
    digest = sha256()
    for A in words:
        for B in words:
            for p in range(1, 6):
                for q in range(1, 6):
                    record = family_case(A, B, p, q)
                    if record is None:
                        counts["nonpositive_gaps_skipped"] += 1
                        continue
                    counts["actual_cycles"] += 1
                    counts["actual_arrows"] += record["arrows"]
                    counts["positive_L" if record["L"] > 0 else "negative_L"] += 1
                    if p < q:
                        counts["increasing_magnitudes"] += 1
                        if record["L"] > 0:
                            counts["main_bound_controls"] += 1
                            counts["opposite_parity_main_controls" if (p + q) % 2
                                   else "same_parity_main_controls"] += 1
                    digest.update(json.dumps([list(A), list(B), p, q, record], separators=(",", ":")).encode())
    require(counts["main_bound_controls"] > 0 and counts["negative_L"] > 0, "both sign branches represented")
    return {"block_lengths": [1, 3], "block_letters": [1, 3], "defect_range": [1, 5],
            "block_words": len(words), "counts": dict(sorted(counts.items())),
            "case_digest_sha256": digest.hexdigest(),
            "scope": "bounded formula controls only; the README proves the unrestricted exclusion"}


def named_and_shared_controls():
    negative = family_case((1,), (1,), 1, 2)
    positive = family_case((1,), (1,), 2, 3)
    require(negative == {"word": [1, 1, 2, 3], "addend": 47,
                         "boundaries": [73, 133, 223, 179], "H": 75, "L": -23, "arrows": 4},
            "named negative-order control")
    require(positive == {"word": [1, 1, 3, 4], "addend": 431,
                         "boundaries": [89, 349, 739, 331], "H": 325, "L": 9, "arrows": 4},
            "named positive-order control")
    require(min(negative["boundaries"]) > negative["addend"], "normalized negative control is everywhere above one")
    scaled_arrows = 0
    for record in (negative, positive):
        scaled_arrows += replay(tuple(record["word"]), 3 * record["addend"],
                                [3 * state for state in record["boundaries"]])
    data = json.loads(FIXTURES.read_text())
    arrows = sum(replay(tuple(cycle["valuations"]), cycle["d"], cycle["states"])
                 for cycle in data["cycles"])
    require({cycle["d"] for cycle in data["cycles"]} == {5, 7, 13, 61}, "shared addends")
    return {"negative_order": negative, "positive_order": positive,
            "odd_scaled_control_arrows": scaled_arrows,
            "shared_fixture_count": len(data["cycles"]), "shared_arrows": arrows,
            "shared_addends": sorted({cycle["d"] for cycle in data["cycles"]}),
            "fixture_sha256": sha256(FIXTURES.read_bytes()).hexdigest()}


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: check_order_bound.py [--write-receipt]")
    receipt = {"schema": "half-defect-positive-order-v1",
               "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
               "polynomial_algebra": polynomial_identities(),
               "finite_arithmetic": finite_arithmetic(),
               "cycle_grid": cycle_grid(),
               "actual_controls": named_and_shared_controls()}
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if sys.argv[1:] == ["--write-receipt"]:
        RECEIPT.write_text(encoded)
    else:
        require(RECEIPT.read_text() == encoded, "receipt mismatch; inspect changes before regeneration")
    print(json.dumps({"status": "pass", "schema": receipt["schema"],
                      "cycle_counts": receipt["cycle_grid"]["counts"],
                      "polynomial_identities": len(receipt["polynomial_algebra"]["zero_residual_identities"]),
                      "shared_fixtures": receipt["actual_controls"]["shared_fixture_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
