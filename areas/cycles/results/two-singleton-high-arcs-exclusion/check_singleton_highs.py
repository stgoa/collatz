"""Exact period closure and addend-aware controls for two high singletons.

The existing common checker is replayed without mutation and with source and
receipt hashes pinned. Its local descent and universal positive logarithm gap
are independent of the former geometric class and of the separately imported
Barina computation. Finite word controls are not an absence proof.
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
                arithmetic_scope="Only local descent and the universal positive logarithm gap are reused; neither uses Barina or any geometric word restriction.",
                external_convergence_replayed=False)


def exact_transfer():
    require(3**32 < 2**51 and 3**80 < 2**127 and 2**3 < 3**2,
            "exact comparisons for alpha")
    require(F(257, 258)-F(255, 256) > 0, "strict profile coefficient below 3/8")
    threshold, drift = F(5, 2384), F(1, 393216)
    coefficient = F(3, 2)*(threshold-drift)
    require(coefficient == F(122731, 39059456), "exact error absorption")
    scale = 1/coefficient
    x0, x1 = 515, 342
    z0, z1 = 27*3+64*x0, 27*2+64*x1
    polynomial = [scale*(x0+F(6, 5)*x0*z0+2),
                  scale*(x1+F(6, 5)*(x0*z1+x1*z0)), scale*F(6, 5)*x1*z1]
    base = sum(value*48**i for i, value in enumerate(polynomial))
    require(base == F(4310155828077002752, 613655) < 2**48,
            "preliminary dyadic cutoff")
    require(all(x > 0 for x in polynomial) and F(49, 48)**2 < 2,
            "positive quadratic and all subsequent dyadic bands")
    Y, n = 112, 97
    numerator = Y+F(6, 5)*Y*(27*n+64*Y)+2
    bound = scale*numerator
    require(numerator == F(6577434, 5) and bound == F(256910993915904, 613655),
            "post-gap exact bound")
    upper = bound.numerator//bound.denominator
    require(upper == 418657053 and bound < 2**29 < 72057431991,
            "integer core bound and separate imported-period contradiction")
    return dict(geometric_error_lower=str(threshold), drift_error_upper=str(drift),
                scale=str(scale), dyadic_polynomial=list(map(str, polynomial)),
                polynomial_at_48=str(base), induction_ratio="2401/2304",
                preliminary_period_upper_exclusive=2**48,
                gap_eta_power=64, post_gap_Y_upper=112, post_gap_cf_digit_upper=97,
                post_gap_numerator=str(numerator), exact_period_upper=str(bound),
                integer_period_upper=upper, EXT1_only_cutoff=2**29,
                separately_sourced_period_lower=72057431991,
                source_scope="EXT1 gives the finite bound; Barina is used only for the all-length contradiction.")


def actual_word_controls():
    counts = dict(opposite=0, adjacent=0)
    placements = dict(opposite=0, adjacent_plus=0, adjacent_minus=0)
    geometries = cycles = arrows = factors = runs = agreement_runs = 0
    digest = sha256()
    label_sets = [(1, 2, 3, 5), (1, 3, 7, 16), (1, 7, 16, 31), (2, 3, 4, 7)]
    for m in range(4, 13):
        for b in range(1, m-2):
            d = m-b-2
            for h in range(1, m):
                if gcd(h, m) != 1:
                    continue
                normalized_h = min(h, m-h)
                u = F(normalized_h, m)
                K = continued_fraction_sum(pow(normalized_h, -1, m), m)
                for labels in label_sets:
                    for low_swap, high_swap, kind in product((False, True), (False, True), ("opposite", "adjacent")):
                        A, B = labels[:2][::(-1 if low_swap else 1)]
                        U, V = labels[2:][::(-1 if high_swap else 1)]
                        track = ([U]+[A]*b+[V]+[B]*d if kind == "opposite"
                                 else [U, V]+[A]*b+[B]*d)
                        word = [0]*m
                        for j, letter in enumerate(track):
                            word[j*h % m] = letter
                        counts[kind] += 1
                        geometries += 1
                        require(all(any(word[i] != word[(i+s) % m] for i in range(m))
                                    for s in range(1, m)), "unique high labels force primitivity")
                        low, high_low = min(A, B), max(A, B)
                        template = [min(letter, high_low) for letter in word]
                        template_total = sum(template)
                        deviations, prefix = [], 0
                        for i, letter in enumerate(template):
                            deviations.append(m*prefix-template_total*i)
                            prefix += letter
                        Delta = 2*(high_low-low)*(K-1)
                        require(max(deviations)-min(deviations) <= m*Delta,
                                "all cyclic-factor discrepancies from the exact prefix span")
                        factors += m*(m-1)
                        weights = [word[i]-template[i] for i in range(m)]
                        high_indices = [i for i, weight in enumerate(weights) if weight]
                        require(len(high_indices) == 2, "two positive unequal excess weights")
                        S = sum(weights)
                        origin, other = high_indices
                        lam = F(weights[origin], S)
                        v = F((other-origin) % m, m)
                        if v < 1-lam:
                            origin, other = other, origin
                            lam = F(weights[origin], S)
                            v = F((other-origin) % m, m)
                        require(v >= 1-lam and 0 < lam < 1, "global post-drop minimum alignment")
                        # Original e_i=(i+1)/m; rotating by the chosen high e_origin
                        # gives these residues, including its exact pre-drop zero.
                        coordinates = [F(((i+1)-(origin+1)) % m, m) for i in range(m)]
                        profile = [lam if e == 0 else e-(1-lam if e > v else 0) for e in coordinates]
                        require(all(0 <= g <= (e if e else 1) for g, e in zip(profile, coordinates)),
                                "unequal profile dominated by the pre-drop single sawtooth")
                        for i in range(m):
                            require(S*(profile[(i+1) % m]-profile[i]) == F(S, m)-weights[i],
                                    "exact weighted profile increment with the (i+1)/m clock")
                        cuts = {i for i in range(m) if word[i] != word[(i+normalized_h) % m]}
                        cut_coords = {coordinates[i] for i in cuts}
                        if kind == "opposite":
                            expected = {F(0), (-u) % 1, v, (v-u) % 1}
                            placement = "opposite"
                        else:
                            if v == u:
                                fixed, placement = {F(0), (-u) % 1, u}, "adjacent_plus"
                            else:
                                require(v == 1-u, "two adjacent orientations after alignment")
                                fixed, placement = {F(0), (-u) % 1, (-2*u) % 1}, "adjacent_minus"
                            require(fixed <= cut_coords and len(cut_coords-fixed) == 1,
                                    "one additional lower-label boundary")
                            expected = fixed | (cut_coords-fixed)
                        require(len(cuts) == 4 and cut_coords == expected, "faithful genuine h-cut placement")
                        placements[placement] += 1
                        refined = cuts | {(i-normalized_h) % m for i in cuts}
                        actual_second = {i for i in range(m) if word[i] != word[(i+2*normalized_h) % m]}
                        require(actual_second <= refined, "artificial cuts refine the 2h mismatch set")
                        cycle = reduced_cycle(word)
                        if cycle is None:
                            continue
                        q, states = cycle
                        cycles += 1
                        arrows += m
                        runs += addend_runs(word, states, q)
                        for j, endpoints in ((1, cuts), (2, refined)):
                            ordered = sorted(endpoints)
                            for position, e in enumerate(ordered):
                                previous = ordered[position-1]
                                gap = (e-previous) % m
                                length = gap-1
                                require(length >= 0, "nonempty cut gaps")
                                for step in range(1, gap):
                                    index = (previous+step) % m
                                    require(word[index] == word[(index+j*normalized_h) % m],
                                            "every artificial-gap interior agrees")
                                partner = (e+j*normalized_h) % m
                                require(abs(states[e]-states[partner]) % (2*3**length) == 0,
                                        "integer paired-state difference on every agreement subinterval")
                                require(max(states[e], states[partner]) > 2*3**length,
                                        "addend-aware end witness uses actual integer states")
                                agreement_runs += 1
                        digest.update((repr((word, q, states))+"\n").encode())
    require(all(counts.values()) and all(placements.values()), "every placement tested")
    return dict(word_geometries=geometries, geometries_by_arrangement=counts,
                aligned_placements=placements, proper_factors_covered_by_prefix_span=factors,
                actual_reduced_cycles=cycles, exact_arrows=arrows, integral_ones_runs=runs,
                agreement_subintervals=agreement_runs, digest_sha256=digest.hexdigest(),
                scope="All m=4..12, positive b+d=m-2, all coprime h, both placements and both label orders for four listed label sets; D<=0 words retain geometry checks only.",
                label_sets=label_sets,
                normalization="Every positive-D word is replayed as a genuine 3x+q integer cycle. No normalized rational state is silently treated as integral.")


def build():
    return dict(constants=exact_transfer(), common_arithmetic=replay_common_arithmetic(),
                family_controls=actual_word_controls(), standard_controls=standard_controls())

if __name__ == "__main__":
    data = build()
    path = HERE/"check_singleton_highs.json"
    text = json.dumps(data, indent=2, sort_keys=True)+"\n"
    if "--write" in sys.argv:
        path.write_text(text)
    else:
        require(path.read_text() == text, "generated arithmetic/cycle receipt differs")
    print("PASS: exact two-singleton period upper 418657053; actual controls and pinned arithmetic replay")
