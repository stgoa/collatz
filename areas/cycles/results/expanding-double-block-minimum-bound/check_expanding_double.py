"""Exact minimum and denominator controls for expanding doubled blocks.

All word examples are genuine positive odd 3x+q cycles, retaining q.
The all-length claims are proved in README.md; finite controls verify the
identities and the declared local convergence/arithmetic inputs.
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
        c = 3*c+2**total
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



def check_pair(u, v):
    g = len(u)
    require(g == len(v) and g >= 1 and min(u+v) >= 1, "positive equal-length blocks")
    a,b = sum(u),sum(v)
    P,Q,S = 3**g,2**a,2**b
    D = Q*Q*S-P**3
    require(Q < P < S and D > 0, "expanding U, contracting V and positive full gap")
    q,states = actual_cycle(u+u+v)
    x0,x1,x2 = states[0],states[g],states[2*g]
    require(x0 < x1 < x2, "expanding boundary order")
    require((x1-x0) % (2*Q) == 0, "even repeated-block lattice")
    t = (x1-x0)//(2*Q)
    require(t >= 1 and x2-x1 == 2*P*t, "both exact boundary differences")
    cv = intercept(v)
    require((S-P)*x0 == 2*P*(P+Q)*t+q*cv, "first boundary identity with q")
    require((S-P)*x2 == 2*S*(P+Q)*t+q*cv, "third boundary identity with q")
    require((S-P)*x0 > 2*P*(P+Q), "first boundary lower bound")
    require((S-P)*x2 > 2*S*(P+Q), "third boundary lower bound")
    prefixes = 0
    for start,block in ((0,u),(g,u),(2*g,v)):
        block_total = sum(block)
        block_power = 2**block_total
        running = 0
        for j in range(g):
            value = states[start+j]
            require(running <= block_total-(g-j), "positive suffix bounds every prefix")
            require(value*2**running >= states[start]*3**j, "positive affine prefix")
            require(value*block_power*2**j >= 2**g*3**j*states[start], "prefix factor bound")
            require(value*(S-P) > 2**(g+1)*(P+Q), "all-interior minimum bound")
            if start < 2*g:
                require(value*Q*(S-P) > 2**(g+1)*P*(P+Q), "stronger U interior bound")
            running += block[j]
            prefixes += 1
    L = min(states)
    require(L*(S-P) > 2**(g+1)*(P+Q), "global minimum bound")
    require(L*S > 2**(g+1)*P, "relaxed logarithmic minimum inequality")
    require(L*D < q*g*Q*Q*S, "normalized minimum upper bound from the product")
    require(q*g*(S-P)*Q*Q*S > D*2**(g+1)*(P+Q), "unconditional denominator law")
    return {"u":list(u),"v":list(v),"q":q,"states":states,"t":t,
            "minimum":L,"minimum_lower_bound":str(F(2**(g+1)*(P+Q),S-P)),
            "denominator_lower_bound":str(F(D*2**(g+1)*(P+Q),g*(S-P)*Q*Q*S)),
            "valuation_threshold":10*a >= 11*g,"prefixes":prefixes,
            "minimum_location":"U" if states.index(L) < 2*g else "V"}


def composition(total, length, rng):
    word = [1]*length
    for _ in range(total-length):
        word[rng.randrange(length)] += 1
    return tuple(word)


def family_controls():
    counts = Counter()
    digest = sha256()
    examples = {}
    def record(u,v,category):
        row = check_pair(u,v)
        counts[category] += 1
        counts["actual_cycles"] += 1
        counts["arrows"] += len(row["states"])
        counts["prefix_checks"] += row["prefixes"]
        counts["threshold_controls"] += row["valuation_threshold"]
        counts["minimum_in_"+row["minimum_location"]] += 1
        key = "threshold" if row["valuation_threshold"] else "below_threshold"
        examples.setdefault(key,row)
        digest.update((json.dumps(row,sort_keys=True)+"\n").encode())
    for g in range(1,5):
        P = 3**g
        words = list(product(range(1,5),repeat=g))
        expanding = [u for u in words if 2**sum(u) < P]
        contracting = [v for v in words if 2**sum(v) > P]
        for u in expanding:
            for v in contracting:
                if 2**(2*sum(u)+sum(v)) > P**3:
                    record(u,v,"exhaustive_pairs")
    rng = random.Random(20261108)
    for _ in range(1200):
        g = rng.randrange(5,25)
        P = 3**g
        a = rng.randrange(g,P.bit_length())
        b = (P**3).bit_length()-2*a
        require(b >= g and 2**(2*a+b) > P**3, "least admissible third total")
        b += rng.randrange(4)
        record(composition(a,g,rng),composition(b,g,rng),"seeded_pairs")
    require(set(examples) == {"threshold","below_threshold"}, "both threshold regimes exercised")
    require(counts["minimum_in_V"] > 0, "contracting-block minima are checked")
    return {"counts":dict(sorted(counts.items())),"examples":examples,"cases_sha256":digest.hexdigest(),
            "ranges":{"exhaustive_lengths":[1,4],"exhaustive_letters":[1,4],
                      "seeded_lengths":[5,24],"seeded_pairs":1200,"seed":20261108},
            "scope":"Actual 3x+q arithmetic with q retained; no bounded absence inference."}


def arithmetic():
    require(3**80 < 2**127, "alpha upper bound by integer powers")
    require(F(2,2**17) == F(1,65536), "internal drift bound")
    coefficient = 2*F(11,10)-(2*F(127,80)-1)-F(1,65536)
    require(coefficient == F(8187,327680), "minimum coefficient")
    slack = coefficient-F(1,41)
    require(slack == F(7987,13434880) > 0, "strict coefficient greater than 1/41")
    base = F(2**19,41)-(172+342*(19+3))
    increment = F(2**19,41)-342
    require(base == F(208752,41) > 0, "dyadic cutoff base")
    require(increment == F(510266,41) > 0, "positive and increasing dyadic increments")
    upper = 3*(2**19-1)
    require(upper == 1572861, "displayed full odd length")
    # The period receipt belongs to the declared result. Its publication
    # computation is an external input, not replayed by this comparison.
    period = ROOT/"areas/cycles/results/cycle-length-lower-bound-from-convergents/cycle_length_convergents.json"
    raw = period.read_bytes()
    data = json.loads(raw)
    imported = int(data["V3"]["2^71"]["least_m"])
    require(imported == 72057431991, "declared least odd period in dependency receipt")
    require(upper < imported, "separate external period comparison")
    return {"alpha_power_comparison":{"ternary_power":80,"binary_power":127},
            "threshold":"11/10","drift_per_g_upper":"1/65536",
            "log_minimum_coefficient":str(coefficient),"coefficient_slack":str(slack),
            "minimum_log2_simplification":"1/41","dyadic_start":19,
            "dyadic_base_margin":str(base),"dyadic_increment_at_base":str(increment),
            "block_length_strict_upper":2**19,"displayed_word_length_upper":upper,
            "imported_least_odd_period_lower":72057431991,"period_receipt_sha256":sha256(raw).hexdigest(),
            "external_scope":"The minimum coefficient is local; the block cutoff uses EXT1; only the final period comparison uses Barina."}


def standard_controls():
    fixture = ROOT/"areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    raw = fixture.read_bytes()
    rows = json.loads(raw)["cycles"]
    arrows = 0
    for row in rows:
        q,states,word = row["d"],row["states"],row["valuations"]
        require(q in (5,7,13,61), "standard additive parameter")
        for i,a in enumerate(word):
            numerator = 3*states[i]+q
            require(numerator == 2**a*states[(i+1) % len(states)], "fixture arrow")
            require((numerator & -numerator).bit_length()-1 == a, "fixture exact valuation")
            arrows += 1
    require(len(rows) == 11 and arrows == 106, "all standard fixtures")
    explicit = check_pair((1,),(3,))
    require(explicit["q"] == 5 and explicit["states"] == [19,31,49], "explicit mixed control")
    return {"cycles":len(rows),"arrows":arrows,"fixture_sha256":sha256(raw).hexdigest(),
            "explicit_expanding_U_control":explicit}


def main():
    require(sys.argv[1:] in ([],["--write-receipt"]), "usage: checker [--write-receipt]")
    result = {"schema":"expanding-double-block-minimum-v1","arithmetic":arithmetic(),
              "local_descent":local_descent(),"family_controls":family_controls(),
              "standard_controls":standard_controls(),
              "checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest()}
    encoded = json.dumps(result,sort_keys=True,indent=2)+"\n"
    path = HERE/"check_expanding_double.json"
    if sys.argv[1:]:
        path.write_text(encoded)
    else:
        require(path.read_text() == encoded,"receipt mismatch; inspect before regenerating")
    print(json.dumps({"status":"passed",**result["family_controls"]["counts"],
                      "local_seeds":result["local_descent"]["seeds"],
                      "standard_cycles":result["standard_controls"]["cycles"]},sort_keys=True))


if __name__ == "__main__":
    main()
