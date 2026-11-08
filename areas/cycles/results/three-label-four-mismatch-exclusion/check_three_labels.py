"""Exact transfer and actual-cycle checks for the three-label theorem.

Elementary reduced-cycle and addend-aware run routines are reused from
clustered-two-maximum-arcs-exclusion/check_clustered_arcs.py. That checker
is replayed unchanged with pinned source/receipt hashes for the common
local descent and exact logarithm gap. No external convergence computation
is replayed; finite word controls are not an absence proof.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import gcd
from pathlib import Path
import subprocess
import sys

F = Fraction
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
DEPENDENCY = "areas/cycles/results/clustered-two-maximum-arcs-exclusion/check_clustered_arcs.py"
SOURCE_SHA256 = "710ceaea7ae8cfeadd63d3ff5dbd8561db25b109a8496a2619f5fcaaed7d1561"
RECEIPT_SHA256 = "969da7512889e8ba6cfddbaa8c30438672f61e960a40b9dd2c1bee5e279f1b07"

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def valuation(value):
    require(value != 0, "valuation at zero")
    value = abs(value)
    return (value & -value).bit_length()-1

def continued_fraction_sum(k, m):
    result = 0
    while k:
        quotient, remainder = divmod(m, k)
        result += quotient
        m, k = k, remainder
    return result

def reduced_cycle(word):
    total = intercept = 0
    for letter in word:
        intercept = 3*intercept+2**total
        total += letter
    D = 2**total-3**len(word)
    if D <= 0:
        return None
    divisor = gcd(intercept, D)
    q, state = D//divisor, intercept//divisor
    states = []
    for letter in word:
        require(state > 0 and state % 2 == 1, "positive odd reduced state")
        states.append(state)
        raw = 3*state+q
        require(valuation(raw) == letter, "exact reduced valuation")
        state = raw >> letter
    require(state == states[0] and len(set(states)) == len(word), "primitive reduced closure")
    return q, states

def addend_runs(word, states, q):
    count = 0
    for start in range(len(word)):
        if word[start] != 1 or word[start-1] == 1:
            continue
        length = 0
        while word[(start+length) % len(word)] == 1:
            length += 1
            require(length < len(word), "ones run ends")
        x = states[start]
        e = word[(start+length) % len(word)]
        target = states[(start+length+1) % len(word)]
        require(valuation(x+q) == length+1, "addend-aware start congruence")
        z = (x+q) >> (length+1)
        require(z > 0 and z % 2 == 1 and 2**(e-1)*target == 3**(length+1)*z-q,
                "addend-aware exact ones-run identity")
        count += 1
    return count

def standard_controls():
    path = ROOT/"areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    rows = json.loads(path.read_text())["cycles"]
    arrows = runs = 0
    for row in rows:
        word, states, q = row["valuations"], row["states"], row["d"]
        require(q in (5, 7, 13, 61), "standard actual addends")
        for i, letter in enumerate(word):
            raw = 3*states[i]+q
            require(valuation(raw) == letter and raw >> letter == states[(i+1) % len(states)],
                    "standard actual arrow")
            arrows += 1
        runs += addend_runs(word, states, q)
    require(len(rows) == 11 and arrows == 106, "all eleven shared controls")
    return dict(cycles=len(rows), exact_arrows=arrows, addend_ones_runs=runs,
                fixture_sha256=sha256(path.read_bytes()).hexdigest(),
                scope="The true addend is retained; normalized states are not treated as integers.")


def replay_common_arithmetic():
    path = ROOT/DEPENDENCY
    receipt_path = path.with_suffix(".json")
    source, raw = path.read_bytes(), receipt_path.read_bytes()
    require(sha256(source).hexdigest() == SOURCE_SHA256, "pinned transfer source")
    require(sha256(raw).hexdigest() == RECEIPT_SHA256, "pinned transfer receipt")
    command = [sys.executable]+(["-O"] if sys.flags.optimize else [])+[str(path)]
    process = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    require(process.returncode == 0, "common arithmetic replay failed: "+process.stdout+process.stderr)
    require(path.read_bytes() == source and receipt_path.read_bytes() == raw,
            "replay must leave dependency artifacts unchanged")
    data = json.loads(raw)
    case = data["constants"]["cases"][0]
    require(case["case"] == "clustered" and case["scale"] == "64749568/24329",
            "common error absorption constants")
    require(case["integer_period_upper"] == 3501056435 and case["EXT1_only_cutoff_bits"] == 32,
            "exact repeated-maximum closure")
    require(data["local_descent"]["odd_seeds"] == 65535 and data["bootstrap"]["eta_power"] == 64,
            "local minimum and universal gap replay")
    require(data["bootstrap"]["imported_odd_period_lower"] == 72057431991,
            "separately sourced full odd period")
    return dict(source=DEPENDENCY, source_sha256=SOURCE_SHA256, receipt_sha256=RECEIPT_SHA256,
                replay_status="passed", local_odd_seeds=65535, eta_power=64,
                upper_convergent=data["bootstrap"]["upper_convergent"],
                nested_bootstrap_source_sha256=data["bootstrap"]["source_sha256"],
                nested_bootstrap_receipt_sha256=data["bootstrap"]["receipt_sha256"],
                arithmetic_scope="The local descent and universal gap do not use Barina or a clustering condition; the new analytic geometry supplies the same error threshold.",
                external_convergence_replayed=False)


def exact_transfer():
    require(3**80 < 2**127 and 3**32 < 2**51 and 2**3 < 3**2,
            "exact alpha comparisons")
    coefficient = 1-F(257, 258)*F(80, 127)
    require(coefficient == F(6103, 16383), "height profile coefficient")
    height_margin = F(1, 4)-F(2, 3)*coefficient
    require(height_margin == F(325, 196596) > F(1, 3952), "height margin covers common threshold")
    require(F(1, 16) > F(1, 3952) and F(5, 96) > F(1, 3952),
            "both residual margins exceed common threshold")
    require(104*38 == 3952, "strong cluster common threshold")
    Y, n = 112, 97
    B = Y+F(6, 5)*Y*(27*n+64*Y)+2
    require(B == F(6577434, 5), "post-gap numerator")
    repeated = F(64749568, 24329)*B
    contiguous = F(4980736, 6125)*B
    singleton = F(1536, 5)*Y*(27*n+64*Y)
    require(repeated == F(425886010048512, 121645), "repeated-maximum bound")
    require(contiguous == F(32760462311424, 30625), "contiguous-maximum extraction")
    require(singleton == F(1683677184, 5), "singleton-maximum extraction")
    require(2**22 < singleton < 2**29 < contiguous < 2**30 < repeated < 2**32,
            "all branches fit the unified cutoff, including omitted small periods")
    upper = repeated.numerator//repeated.denominator
    require(upper == 3501056435 and 72057431991 > 2**32, "integer and sourced period comparison")
    rows = []
    for name, scale in [("repeated_maximum", F(64749568, 24329)),
                        ("contiguous_maximum_at_least_two", F(4980736, 6125))]:
        x0, x1 = 515, 342
        z0, z1 = 27*3+64*x0, 27*2+64*x1
        polynomial = [scale*(x0+F(6, 5)*x0*z0+2),
                      scale*(x1+F(6, 5)*(x0*z1+x1*z0)), scale*F(6, 5)*x1*z1]
        base = sum(value*48**i for i, value in enumerate(polynomial))
        require(all(value > 0 for value in polynomial) and base < 2**48,
                "branch preliminary cutoff")
        rows.append(dict(branch=name, polynomial=list(map(str, polynomial)), base_at_48=str(base)))
    singleton_poly = [F(1536, 5)*515*(27*3+64*515),
                      F(1536, 5)*(342*(27*3+64*515)+515*(27*2+64*342)),
                      F(1536, 5)*342*(27*2+64*342)]
    singleton_base = sum(value*48**i for i, value in enumerate(singleton_poly))
    require(singleton_base == F(28249216922112, 5) < 2**48,
            "singleton preliminary cutoff")
    require(all(value > 0 for value in singleton_poly) and F(49, 48)**2 < 2,
            "all larger dyadic bands for every branch")
    rows.append(dict(branch="singleton_maximum", polynomial=list(map(str, singleton_poly)),
                     base_at_48=str(singleton_base)))
    return dict(profile_coefficient=str(coefficient), oscillation_margin=str(height_margin),
                residual_margins=["1/16", "5/96"], common_error_threshold="1/3952",
                preliminary_dyadic_checks=rows, induction_ratio="2401/2304",
                gap_scope="Every positive integer full period below2^48; no family restriction.",
                repeated_maximum_upper=str(repeated), contiguous_maximum_upper=str(contiguous),
                singleton_maximum_upper=str(singleton), integer_period_upper=upper,
                EXT1_only_cutoff=2**32, source_period_lower=72057431991,
                source_scope="EXT1 alone gives all three finite bounds; Barina is used only to contradict the unified bound at every length.")


def classify_runs(pattern):
    require(len(pattern) == 4 and len(set(pattern)) == 3, "three labels in four runs")
    require(all(pattern[i] != pattern[(i+1) % 4] for i in range(4)), "cyclic runs are maximal")
    repeated = next(label for label in set(pattern) if pattern.count(label) == 2)
    positions = [i for i, label in enumerate(pattern) if label == repeated]
    require((positions[1]-positions[0]) % 4 == 2, "repeated label is opposite")
    singletons = [label for label in set(pattern) if pattern.count(label) == 1]
    require(len(singletons) == 2, "two single-run indicators force primitivity")
    return "repeated_maximum" if repeated == max(pattern) else "contiguous_maximum"


def actual_word_controls():
    patterns = [p for p in product(range(3), repeat=4)
                if len(set(p)) == 3 and all(p[i] != p[(i+1) % 4] for i in range(4))]
    require(len(patterns) == 12, "all cyclic four-run patterns on three named labels")
    pattern_counts = {"repeated_maximum": 0, "contiguous_maximum": 0}
    for pattern in patterns:
        pattern_counts[classify_runs(pattern)] += 1
    require(pattern_counts == {"repeated_maximum": 4, "contiguous_maximum": 8}, "complete structural split")
    geometries = cycles = arrows = runs = factors = 0
    case_counts = {"repeated_maximum": 0, "contiguous_maximum": 0}
    repeated_regimes = {"clustered": 0, "not_clustered": 0}
    digest = sha256()
    label_sets = [(1, 2, 3), (1, 3, 7), (1, 7, 16), (2, 3, 4)]
    for m in range(4, 10):
        for a in range(1, m-2):
            for b in range(1, m-a-1):
                for c in range(1, m-a-b):
                    lengths = (a, b, c, m-a-b-c)
                    for h in range(1, m):
                        if gcd(h, m) != 1:
                            continue
                        K = continued_fraction_sum(pow(h, -1, m), m)
                        for labels in label_sets:
                            for pattern in patterns:
                                case = classify_runs(pattern)
                                track = [labels[p] for p, length in zip(pattern, lengths) for _ in range(length)]
                                word = [0]*m
                                for j, letter in enumerate(track):
                                    word[j*h % m] = letter
                                require(sum(word[i] != word[(i+h) % m] for i in range(m)) == 4,
                                        "exact coprime four-mismatch word")
                                require(all(any(word[i] != word[(i+s) % m] for i in range(m))
                                            for s in range(1, m)), "full word primitive")
                                V = max(labels)
                                r = word.count(V)
                                # For a repeated maximum the other labels each occupy a single arc.
                                # Replacing V with either lower label therefore gives a binary interval template.
                                if case == "repeated_maximum":
                                    lower = min(labels)
                                    template = [lower if x == V else x for x in word]
                                    require(sum(template[i] != template[(i+h) % m] for i in range(m)) == 2,
                                            "one interval of each remaining label")
                                    high_positions = [i+1 for i in range(m) if word[i] == V]
                                    profile = [r*(i+1)-m*sum(z < i+1 for z in high_positions) for i in range(m)]
                                    variation = 2*(max(template)-min(template))
                                    require(sum(word)-sum(template) == r*(V-lower), "edit total")
                                    for start in range(m):
                                        total = number = 0
                                        for length in range(1, m):
                                            i = (start+length-1) % m
                                            total += template[i]
                                            number += word[i] == V
                                            end = (start+length) % m
                                            require(profile[end]-profile[start] == r*length-m*number,
                                                    "pre-drop profile identity with i+1 clock")
                                            require(abs(m*total-sum(template)*length) <= variation*(K-1)*m,
                                                    "inverse-step template discrepancy")
                                            factors += 1
                                    regime = "clustered" if r*min(h, m-h) < m else "not_clustered"
                                    repeated_regimes[regime] += 1
                                geometries += 1
                                case_counts[case] += 1
                                cycle = reduced_cycle(word)
                                if cycle is None:
                                    continue
                                q, states = cycle
                                require(q > 1, "finite controls retain their nonunit actual addend")
                                runs += addend_runs(word, states, q)
                                cycles += 1
                                arrows += m
                                digest.update(f"{m}:{lengths}:{h}:{labels}:{pattern}:{q}:{states}\n".encode())
    require(all(repeated_regimes.values()) and all(case_counts.values()) and cycles and runs,
            "both structural branches and both repeated-maximum regimes exercised")
    return dict(periods=[4, 9], patterns=len(patterns), pattern_counts=pattern_counts,
                all_positive_run_lengths=True, all_coprime_track_steps=True,
                label_sets=label_sets, geometry_words=geometries, branch_word_counts=case_counts,
                repeated_maximum_regime_counts=repeated_regimes, exact_proper_factors=factors,
                actual_reduced_cycles=cycles, exact_arrows=arrows, addend_ones_runs=runs,
                control_sha256=digest.hexdigest(),
                scope="Every listed word is reconstructed directly; actual states use their true3x+q addend. Finite absence at q1 is not the universal proof.")


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: checker [--write-receipt]")
    receipt = dict(schema="three-label-four-mismatch-transfer-v1", arithmetic=exact_transfer(),
                   dependency_replay=replay_common_arithmetic(), words=actual_word_controls(),
                   standard_controls=standard_controls())
    encoded = json.dumps(receipt, sort_keys=True, indent=2)+"\n"
    destination = HERE/"check_three_labels.json"
    if sys.argv[1:]:
        destination.write_text(encoded)
    else:
        require(destination.read_text() == encoded, "receipt mismatch; regenerate explicitly")
    print(json.dumps(dict(status="passed", geometry_words=receipt["words"]["geometry_words"],
                          actual_cycles=receipt["words"]["actual_reduced_cycles"],
                          standard_cycles=receipt["standard_controls"]["cycles"],
                          integer_period_upper=receipt["arithmetic"]["integer_period_upper"]), sort_keys=True))


if __name__ == "__main__":
    main()
