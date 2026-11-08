"""Exact controls for the expanding-third-block minimum bound.

All word controls are genuine integer 3x+q cycles with q retained.
They check algebra and prefix inequalities, not a search-based q=1 exclusion.
The manuscript proves the unbounded implication. Only the final period
comparison uses the declared external convergence input.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from math import gcd
from pathlib import Path
import random
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def intercept(word):
    c, total = 0, 0
    for letter in word:
        c = 3*c + 2**total
        total += letter
    return c


def actual_cycle(word):
    c = intercept(word)
    d = 2**sum(word) - 3**len(word)
    require(d > 0, "positive full discriminant")
    divisor = gcd(c, d)
    q, current = d // divisor, c // divisor
    states = []
    for letter in word:
        require(current > 0 and current % 2, "positive odd state")
        states.append(current)
        numerator = 3*current + q
        require((numerator & -numerator).bit_length()-1 == letter, "exact valuation")
        current = numerator >> letter
    require(current == states[0], "actual cycle closure")
    return q, states


def check_pair(u, v):
    g = len(u)
    require(g == len(v) and g >= 1 and min(u+v) >= 1, "positive equal lengths")
    a, b = sum(u), sum(v)
    Q, S, P = 2**a, 2**b, 3**g
    require(Q > P > S and Q*Q*S > P**3, "mixed directions and positive full gap")
    cv = intercept(v)
    require(2**g * cv <= S*(P-2**g) < S*P, "positive-word intercept bound")
    q, states = actual_cycle(u+u+v)
    x0, x1, x2 = states[0], states[g], states[2*g]
    require(x0 > x1 > x2, "boundary direction from expanding V")
    require((x0-x1) % (2*Q) == 0, "odd repeated-block lattice")
    t = (x0-x1) // (2*Q)
    require(t >= 1 and x1-x2 == 2*P*t, "both exact block differences")
    require((P-S)*x2 == 2*S*(Q+P)*t-q*cv, "addend-aware third-block identity")
    prefixes = 0
    for start, block in ((0, u), (g, u), (2*g, v)):
        running = 0
        for j in range(g):
            state = states[start+j]
            require(running <= a-(g-j), "suffix positivity bounds prefix")
            require(state*2**running >= states[start]*3**j, "positive affine prefix")
            require(state*Q*2**j >= 2**g*3**j*x2, "all-state prefix lower bound")
            running += block[j]
            prefixes += 1
    L = min(states)
    require(L*Q >= 2**g*x2, "global minimum includes interior states")
    # This sufficient condition can hold at true q>1. It exercises the
    # minimum mechanism without replacing q by1 in any actual equation.
    dominated = q*cv < S*P
    if dominated:
        require((P-S)*x2 > S*Q, "conditional minimum boundary estimate")
        require((P-S)*L > 2**g*S, "conditional global minimum estimate")
    e = a-b
    require(2**(2*e)*S**3 > P**3, "full gap in excess coordinates")
    return {"u": list(u), "v": list(v), "q": q, "states": states,
            "t": t, "dominated_control": dominated, "prefixes": prefixes}


def positive_composition(total, length, rng):
    word = [1]*length
    for _ in range(total-length):
        word[rng.randrange(length)] += 1
    return tuple(word)


def family_controls():
    counts = Counter()
    digest = sha256()
    examples = {}
    def record(u, v, category):
        row = check_pair(u, v)
        counts[category] += 1
        counts["actual_cycles"] += 1
        counts["arrows"] += len(row["states"])
        counts["prefix_checks"] += row["prefixes"]
        counts["dominated_actual_controls"] += row["dominated_control"]
        key = "dominated" if row["dominated_control"] else "retained_addend"
        examples.setdefault(key, row)
        digest.update((json.dumps(row, sort_keys=True)+"\n").encode())
    for g in range(1, 5):
        P = 3**g
        words = list(product(range(1, 5), repeat=g))
        contracting = [u for u in words if 2**sum(u) > P]
        expanding = [v for v in words if 2**sum(v) < P]
        for u in contracting:
            for v in expanding:
                if 2**(2*sum(u)+sum(v)) > P**3:
                    record(u, v, "exhaustive_pairs")
    rng = random.Random(20261108)
    for _ in range(1200):
        g = rng.randrange(5, 25)
        P = 3**g
        largest_expanding_sum = P.bit_length()-1
        b = rng.randrange(g, largest_expanding_sum+1)
        a = largest_expanding_sum+1
        while 2**(2*a+b) <= P**3:
            a += 1
        a += rng.randrange(4)
        record(positive_composition(a, g, rng), positive_composition(b, g, rng), "seeded_pairs")
    require(counts["dominated_actual_controls"] > 0 and len(examples) == 2,
            "nonvacuous true-addend controls")
    return {"counts": dict(sorted(counts.items())), "examples": examples,
            "case_sha256": digest.hexdigest(),
            "ranges": {"exhaustive_lengths": [1, 4], "exhaustive_letters": [1, 4],
                       "seeded_lengths": [5, 24], "seed": 20261108},
            "scope": "Exact actual 3x+q arrows; no finite absence inference."}


def local_descent():
    maximum_steps = 0
    digest = sha256()
    count = 0
    for seed in range(3, 2**17, 2):
        value, steps = seed, 0
        while value >= seed:
            numerator = 3*value+1
            value = numerator >> ((numerator & -numerator).bit_length()-1)
            steps += 1
            require(steps < 10000, "local seed did not descend")
        maximum_steps = max(maximum_steps, steps)
        digest.update(f"{seed}:{steps}:{value}\n".encode())
        count += 1
    require(count == 65535, "all odd nontrivial seeds below2^17")
    return {"seeds": count, "maximum_odd_steps_to_descent": maximum_steps,
            "cases_sha256": digest.hexdigest(), "minimum_excluded_below": 2**17}


def arithmetic():
    require(388**5 < 2**8*129**5, "q=1 mean bound at L>=129")
    coefficient = F(1)-F(2, 3)*F(9, 10)
    require(coefficient == F(2, 5), "exponential minimum coefficient")
    base = F(2, 5)*2**14-(172+342*(14+3))
    require(base == F(2838, 5) > 0, "dyadic cutoff base")
    require(F(2, 5)*2**14 > 342, "all later dyadic increments")
    require(3*(2**14-1) == 49149 < 49152, "displayed word-length bound")
    imported = 72057431991
    require(49149 < imported, "declared external period comparison")
    # The strict mean inequality is E=3b+2e<24g/5.
    # 9g-10e = (24g-5E)+15(b-g), with b>=g.
    for g, b, e in product(range(1, 17), range(1, 25), range(1, 25)):
        E = 3*b+2*e
        require(9*g-10*e == (24*g-5*E)+15*(b-g), "mean-to-excess identity")
    return {"minimum_log2_coefficient": str(coefficient),
            "dyadic_start": 14, "dyadic_base_margin": str(base),
            "block_length_strict_upper": 2**14,
            "displayed_word_length_upper": 49149,
            "imported_full_odd_period_lower": imported,
            "external_scope": "Only the last comparison uses Barina through the declared period node."}


def fixtures():
    path = ROOT/"areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    raw = path.read_bytes()
    rows = json.loads(raw)["cycles"]
    arrows = 0
    for fixture in rows:
        q, states, word = fixture["d"], fixture["states"], fixture["valuations"]
        require(q in (5, 7, 13, 61), "known addend")
        for i, a in enumerate(word):
            numerator = 3*states[i]+q
            require(numerator >> a == states[(i+1) % len(states)], "fixture arrow")
            require((numerator & -numerator).bit_length()-1 == a, "fixture exact odd valuation")
            arrows += 1
    require(len(rows) == 11 and arrows == 106, "all fixture controls")
    control = check_pair((2,), (1,))
    require(control["q"] == 5 and control["states"] == [37, 29, 23], "explicit mixed control")
    return {"cycles": len(rows), "arrows": arrows, "fixture_sha256": sha256(raw).hexdigest(),
            "mixed_control": control}


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: checker [--write-receipt]")
    result = {"schema": "expanding-third-block-minimum-v1", "arithmetic": arithmetic(),
              "local_descent": local_descent(), "family_controls": family_controls(),
              "standard_controls": fixtures()}
    encoded = json.dumps(result, sort_keys=True, indent=2)+"\n"
    destination = HERE/"check_mixed_blocks.json"
    if sys.argv[1:]:
        destination.write_text(encoded)
    else:
        require(destination.read_text() == encoded, "receipt mismatch; inspect before regenerating")
    print(json.dumps({"status": "passed", **result["family_controls"]["counts"],
                      "local_seeds": result["local_descent"]["seeds"],
                      "fixtures": result["standard_controls"]["cycles"]}, sort_keys=True))


if __name__ == "__main__":
    main()
