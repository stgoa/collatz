"""Exact controls and cutoff arithmetic for the high-order s=4 exclusion.

The geometric all-configuration proof is in its declared result node.
This checker retains actual additive constants in every finite cycle control.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations, product
import json
from math import gcd
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def actual_cycle(word):
    c, total = 0, 0
    for a in word:
        require(a >= 1, "positive letter")
        c = 3*c+2**total
        total += a
    D = 2**total-3**len(word)
    require(D > 0, "positive full discriminant")
    divisor = gcd(c, D)
    q, state = D//divisor, c//divisor
    states = []
    for a in word:
        require(state > 0 and state % 2, "positive odd actual state")
        states.append(state)
        numerator = 3*state+q
        require((numerator & -numerator).bit_length()-1 == a, "exact odd valuation")
        state = numerator >> a
    require(state == states[0], "cycle closure")
    require(len(set(states)) == len(word), "primitive actual states")
    cut = states.index(min(states))
    return q, states[cut:]+states[:cut], word[cut:]+word[:cut]


def check_ramp(word, states, q):
    m, E, L = len(word), sum(word), min(states)
    require(states[0] == L, "state clock starts at actual minimum")
    for i, a in enumerate(word):
        require(3*states[i]+q == 2**a*states[(i+1) % m], "actual addend retained")
        require(states[i]*2**i*3**m <= L*3**i*2**E,
                "minimum-state ramp in exact integer powers")
    return m


def check_shift(word, states, h, horizon=18):
    m = len(word)
    base = {i for i in range(m) if word[i] != word[(i+h) % m]}
    require(len(base) == 4, "exactly four base mismatches")
    order = m//gcd(h, m)
    require(order > horizon, "all tested shifts are nonidentity")
    doubled = word+word
    prefix = [0]
    for a in doubled:
        prefix.append(prefix[-1]+a)
    runs = artificial = coincidences = 0
    digest = sha256()
    for j in range(1, horizon+1):
        shift = (j*h) % m
        require(shift != 0, "nonidentity witness shift")
        actual = {i for i in range(m) if word[i] != word[(i+shift) % m]}
        raw = [(c-i*h) % m for c in base for i in range(j)]
        cuts = sorted(set(raw))
        require(actual <= set(cuts), "telescoping mismatch inclusion")
        artificial += len(set(cuts)-actual)
        coincidences += len(raw)-len(cuts)
        for k, end in enumerate(cuts):
            previous = cuts[k-1]
            length = (end-previous) % m-1
            start = (previous+1) % m
            require(length >= 0, "nonnegative agreeing length")
            require(all(word[(start+i) % m] == word[(start+i+shift) % m]
                        for i in range(length)), "all refined agreement arrows")
            A = prefix[start+length]-prefix[start]
            first = states[(start+shift) % m]-states[start]
            last = states[(end+shift) % m]-states[end]
            require(first != 0 and first % 2**(A+1) == 0, "integer odd-pair lattice")
            require(last == 2*3**length*(first//2**(A+1)), "exact paired endpoint identity")
            require(max(states[end], states[(end+shift) % m]) > 2*3**length,
                    "end witness uses state index end")
            digest.update(f"{j}:{previous}:{end}:{length}:{A}:{first}:{last}\n".encode())
            runs += 1
    return runs, artificial, coincidences, digest.hexdigest()


def track_word(M, tracks, step, lengths, labels):
    m, h = M*tracks, step*tracks
    require(gcd(step, M) == 1 and sum(lengths) == M, "track parameters")
    word = [2]*m
    track = [letter for count, letter in zip(lengths, labels) for _ in range(count)]
    for i, letter in enumerate(track):
        word[(i*h) % m] = letter
    return word, h


def family_controls():
    counts = Counter()
    by_order = Counter()
    by_gcd = Counter()
    digest = sha256()
    examples = {}
    for M, tracks in product((19, 23, 29), (1, 2, 3)):
        lengths_set = ((1, 1, 1, M-3), (2, 3, 4, M-9),
                       (M//4, M//4, M//4, M-3*(M//4)))
        for step, lengths, tail in product((1, 2, (M-1)//2), lengths_set, permutations((2, 3, 5))):
            word, h = track_word(M, tracks, step, lengths, (1,)+tail)
            if 2**sum(word) <= 3**len(word):
                counts["nonpositive_gap_geometries"] += 1
                continue
            q, states, rotated = actual_cycle(word)
            counts["arrows"] += check_ramp(rotated, states, q)
            runs, artificial, coincidences, casehash = check_shift(rotated, states, h)
            counts["actual_cycles"] += 1
            counts["refined_runs"] += runs
            counts["artificial_cuts"] += artificial
            counts["coincident_raw_cuts"] += coincidences
            by_order[M] += 1
            by_gcd[tracks] += 1
            key = "coprime" if tracks == 1 else "noncoprime"
            examples.setdefault(key, {"word": rotated, "q": q, "states": states,
                                      "h": h, "order": M, "gcd": tracks})
            digest.update(f"{M}:{tracks}:{step}:{lengths}:{tail}:{q}:{casehash}\n".encode())
    require(set(examples) == {"coprime", "noncoprime"}, "both shift types covered")
    require(counts["artificial_cuts"] and counts["coincident_raw_cuts"], "refinement and dedup exercised")
    return {"counts": dict(sorted(counts.items())), "orders": dict(sorted(by_order.items())),
            "shift_gcds": dict(sorted(by_gcd.items())), "examples": examples,
            "cases_sha256": digest.hexdigest(),
            "scope": "Actual primitive 3x+q controls, retaining q. No q=1 absence inference."}


def standard_controls():
    path = ROOT/"areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    raw = path.read_bytes()
    fixtures = json.loads(raw)["cycles"]
    arrows = 0
    for fixture in fixtures:
        states, word, q = fixture["states"], fixture["valuations"], fixture["d"]
        require(q in (5, 7, 13, 61), "fixture addend")
        i = states.index(min(states))
        arrows += check_ramp(word[i:]+word[:i], states[i:]+states[:i], q)
    require(len(fixtures) == 11 and arrows == 106, "all shared controls")
    word, h = track_word(18, 1, 7, (1, 1, 1, 15), (1, 2, 3, 5))
    q, states, word = actual_cycle(word)
    require(all(states[i] == states[(i+18*h) % 18] for i in range(18)), "identity has no separation")
    require(len({i for i in range(18) if word[i] != word[(i+h) % 18]}) == 4,
            "order18 four-mismatch control")
    return {"fixtures": len(fixtures), "arrows": arrows, "fixture_sha256": sha256(raw).hexdigest(),
            "identity_gate_control": {"word": word, "q": q, "h": h, "order": 18,
                                      "eighteenth_shift_difference": 0}}


def local_descent():
    digest = sha256()
    count = maximum = 0
    for seed in range(3, 2**17, 2):
        n, steps = seed, 0
        while n >= seed:
            value = 3*n+1
            n = value >> ((value & -value).bit_length()-1)
            steps += 1
            require(steps < 10000, "local seed failed to descend")
        maximum = max(maximum, steps)
        count += 1
        digest.update(f"{seed}:{steps}:{n}\n".encode())
    require(count == 65535, "complete local range")
    return {"odd_seeds": count, "range": [3, 2**17-1], "maximum_steps": maximum,
            "cases_sha256": digest.hexdigest()}


def constants():
    require(3**2 > 2**3 and 3**5 < 2**8, "3/2<alpha<8/5")
    require(1/(F(3, 2)) == F(2, 3) and 1-1/F(8, 5) == F(3, 8), "ramp coefficients")
    require(3*2**17 == 393216, "drift divisor from ln3>1")
    base = F(2*(175+342*27), 3*2**26)+F(1, 393216)
    margin = F(1, 10000)-base
    require(base == F(9665, 100663296), "dyadic base")
    require(margin == F(250831, 62914560000) > 0, "strict geometric margin")
    require(2*517-(517+342) == 175 and 2*342-342 == 342, "dyadic monotonicity")
    require(72057431991 > 2**26, "declared external period comparison")
    return {"horizon": 18, "order_strict_lower": 18, "period_strict_upper": 2**26,
            "geometric_error_lower": "1/10000", "dyadic_error_upper": str(base),
            "strict_margin": str(margin), "drift_divisor": 393216,
            "imported_full_odd_period_lower": 72057431991,
            "external_scope": "Only the all-length comparison uses the declared convergence input."}


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: checker [--write-receipt]")
    result = {"schema": "high-order-four-mismatch-v1", "constants": constants(),
              "local_descent": local_descent(), "family_controls": family_controls(),
              "standard_controls": standard_controls()}
    encoded = json.dumps(result, sort_keys=True, indent=2)+"\n"
    receipt = HERE/"check_high_order.json"
    if sys.argv[1:]:
        receipt.write_text(encoded)
    else:
        require(receipt.read_text() == encoded, "receipt mismatch; inspect before regenerating")
    print(json.dumps({"status": "passed", **result["family_controls"]["counts"],
                      "local_seeds": result["local_descent"]["odd_seeds"],
                      "fixtures": result["standard_controls"]["fixtures"]}, sort_keys=True))


if __name__ == "__main__":
    main()
