"""Exact profile, integer-control and cutoff checks for a maximum arc.

The positive-logarithm enclosure and one-sided gap method are reproduced
from general-three-label-four-arc-exclusion/check_bootstrap.py (Codex
residue research lane, GPT-6 Astra), rather than imported as a new source.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys

F = Fraction
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PERIOD_RECEIPT = "areas/cycles/results/cycle-length-lower-bound-from-convergents/cycle_length_convergents.json"
PERIOD_SHA256 = "e48b19926ca0c155032a9d85d3c28f3f6fbe69ae404163638414a7c848c65f64"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def valuation(value):
    require(value != 0, "valuation at zero")
    value = abs(value)
    return (value & -value).bit_length()-1


def logarithm_bounds(value, terms=80):
    """Positive atanh sum with an exact geometric upper bound on its tail."""
    require(value > 1 and terms >= 1, "logarithm domain")
    z = Fraction(value - 1, value + 1)
    lower = 2 * sum(
        (z ** (2 * j + 1) / (2 * j + 1) for j in range(terms)),
        Fraction(0),
    )
    tail = 2 * z ** (2 * terms + 1) / (
        (2 * terms + 1) * (1 - z * z)
    )
    require(tail > 0, "positive logarithm tail")
    return lower, lower + tail



def exact_gap():
    low2, high2 = logarithm_bounds(2)
    low3, high3 = logarithm_bounds(3)
    require(Fraction(1, 2) < low2 < high2 < 1, "ln2 enclosure")
    require(1 < low3 < high3 < Fraction(11, 10), "ln3 enclosure")
    alpha_low, alpha_high = low3 / high2, high3 / low2
    left, right = alpha_low, alpha_high
    p_previous_previous, p_previous = 0, 1
    q_previous_previous, q_previous = 1, 0
    terms = []
    convergents = []
    for _ in range(100):
        lower_digit, upper_digit = left.__floor__(), right.__floor__()
        require(lower_digit == upper_digit, "unambiguous continued-fraction digit")
        digit = lower_digit
        p = digit * p_previous + p_previous_previous
        q = digit * q_previous + q_previous_previous
        terms.append(digit)
        convergents.append((p, q))
        if q > 2**48:
            break
        left, right = 1 / (right - digit), 1 / (left - digit)
        p_previous_previous, p_previous = p_previous, p
        q_previous_previous, q_previous = q_previous, q
    else:
        raise RuntimeError("continued-fraction iteration guard")
    p, q = convergents[-2]
    p_next, q_next = convergents[-1]
    require((p, q) == (83130157078217, 52449289519716), "lower convergent")
    require((p_next, q_next) == (683381996816440, 431166034846567),
            "upper convergent")
    require(Fraction(p, q) < alpha_low < alpha_high < Fraction(p_next, q_next),
            "opposite bracket signs")
    require(p_next * q - p * q_next == 1, "unimodular bracket")
    require(q_next > 2**48, "coverage of every possible full period")
    gap = q * alpha_low - p
    require(gap > Fraction(1, 2**62), "one-sided logarithm gap")
    # The manuscript's integer-coordinate argument, not an enumeration,
    # now gives E-m*alpha>gap for EVERY 0<m<q_next with E-m*alpha>0.
    # ln2>1/2 gives Lambda>2^-63; eta>min(Lambda/2,1/2)>2^-64.
    return {
        "atanh_terms": 80,
        "ln2_interval": [str(low2), str(high2)],
        "ln3_interval": [str(low3), str(high3)],
        "continued_fraction_digits": terms,
        "lower_convergent": {"p": p, "q": q},
        "upper_convergent": {"p": p_next, "q": q_next},
        "positive_gap_lower": str(gap),
        "positive_gap_power": 62,
        "eta_power": 64,
        "scope": "Every integer full period 0<m<2^48; no m>=q restriction.",
    }


def constants():
    require(388**5 < 2**8*129**5, "mean below 8/5")
    require(3**32 < 2**51 and F(2, 387) < F(1, 160), "kappa below 8/5")
    require(F(51, 32)+F(1, 160) == F(8, 5), "kappa constants")
    require(3*2**17*F(2, 3) == 2**18, "locally verified drift constant")
    require(F(8, 5)**5 < 11, "four-mismatch rise constant")
    coefficient = F(3, 8)-F(20, 64)-F(10, 258)
    require(coefficient == F(49, 2064), "maximum-letter forcing coefficient")
    first_margin = coefficient*2**22-(11*(172+342*23)+11)
    require(first_margin == F(1437715, 129) > 0, "forcing dyadic base")
    require(coefficient*2**22 > 11*342, "forcing dyadic induction")
    count_margin = (F(39, 64)-F(3, 5))*2**22-39
    require(count_margin == F(196413, 5) > 0, "at most38 maximum letters")
    require(F(257, 258)-F(255, 256) == F(1, 33024) > 0,
            "cluster profile coefficient")
    require(3**80 < 2**127, "sharper alpha comparison")
    spread_coefficient = 1-F(257, 258)*F(80, 127)
    require(spread_coefficient == F(6103, 16383), "spread profile coefficient")
    spread_margin = F(1, 4)-F(2, 3)*spread_coefficient
    require(spread_margin == F(325, 196596) > F(1, 1216), "spread obstruction margin")
    require(32*38 == 1216, "uniform clustered margin")
    threshold = F(3, 2)*(F(1, 1216)-F(1, 393216))
    require(threshold == F(6125, 4980736) > 0, "error absorption threshold")
    require(393216 == 3*2**17, "normalized drift error")
    scale = 1/threshold
    x0, x1 = 515, 342
    z0, z1 = 27*3+64*x0, 27*2+64*x1
    polynomial = [scale*(x0+F(6, 5)*x0*z0+2),
                  scale*(x1+F(6, 5)*(x0*z1+x1*z0)),
                  scale*F(6, 5)*x1*z1]
    require(all(c > 0 for c in polynomial), "positive cutoff polynomial")
    initial = sum(c*48**i for i, c in enumerate(polynomial))
    require(initial == F(549617186130624512, 30625) < 2**48, "cutoff base")
    require(F(49, 48)**2 < 2, "cutoff dyadic induction")
    final = scale*(112+F(6, 5)*112*(27*97+64*112)+2)
    require(final == F(32760462311424, 30625) < 2**30, "post-gap period upper bound")
    require(F(2**112, 3)+1 < 2**112 and 2*48+1 == 97, "post-gap height and digit bounds")
    raw = (ROOT/PERIOD_RECEIPT).read_bytes()
    require(sha256(raw).hexdigest() == PERIOD_SHA256, "pinned existing period receipt")
    period = int(json.loads(raw)["V3"]["2^71"]["least_m"])
    require(period == 72057431991 > 2**30 and period > 2**22,
            "separately sourced full odd-period contradiction")
    return dict(local_minimum_used=2**17, maximum_count_cutoff_bits=22,
                maximum_letter_denominator=64, maximum_multiplicity=38,
                forcing_coefficient=str(coefficient), forcing_base_margin=str(first_margin),
                multiplicity_margin=str(count_margin), spread_coefficient=str(spread_coefficient),
                spread_margin=str(spread_margin), uniform_error_threshold="1/1216",
                drift_error_upper="1/393216", absorbed_threshold=str(threshold),
                cutoff_polynomial=[str(c) for c in polynomial], cutoff_bits=48,
                cutoff_base_upper=str(initial), cutoff_base_margin=str(2**48-initial),
                dyadic_ratio_upper="2401/2304", post_gap_height_upper=112,
                post_gap_digit_count_upper=97, post_gap_full_period_upper=str(final),
                integer_full_period_upper=final.numerator//final.denominator,
                imported_odd_period_lower=period, period_receipt_sha256=PERIOD_SHA256,
                external_convergence_replayed=False)


def rank_cases():
    records = []
    for d in range(2, 39):
        error = F(1, 32*d)
        final_lower = 1-F(3, 8*d)-error
        require(final_lower >= F(25, 32), "last-point lower bound")
        first_u = (5-8*error)/(5*d+3)
        first_R = 1-d*first_u
        require(first_R <= F(1, 4) and d*first_u >= F(3, 4) > F(13, 32),
                "rank1 location")
        first_e2 = F(8, 5)*(first_R+error)
        first_e3 = F(8, 5)*(first_e2-F(3, 8)*F(d-1, d)+error)
        require(first_e2 <= F(7, 12) and first_e3 <= F(41, 60) < final_lower,
                "rank1 contradiction")
        second_u = (25-104*error)/(25*d+39)
        require(d*second_u > F(1, 2) > F(13, 32), "rank2 last branch")
        second_e3 = 1+F(3, 5*d)-F(8*d, 5)*second_u+F(8, 5)*error
        require(second_e3 < F(1, 5)+F(13, 20*d) <= F(21, 40) < final_lower,
                "rank2 contradiction")
        third_u = F(13, 32*d*d)
        third_upper = F(39, 25)*third_u+F(104, 25)*error
        third_lower = F(5, 8)-F(5*d+3, 8)*third_u-error
        require(third_upper <= F(715, 3200) < F(455, 1024) <= third_lower,
                "rank3 contradiction")
        records.append(dict(d=d, error=str(error), rank1_margin=str(final_lower-first_e3),
                            rank2_margin=str(final_lower-second_e3),
                            rank3_margin=str(third_lower-third_upper)))
    return dict(maximum_multiplicities=[2, 38], records=records,
                scope="Exact monotone endpoint inequalities for all admissible multiplicities; the manuscript proves the rank argument.")


def residue_one(value):
    return value % 1 or F(1)


def profile(d, step):
    points = Counter(residue_one(1-j*step) for j in range(d))
    count = 0
    low = high = F(0)
    for point, multiplicity in sorted(points.items()):
        before = d*point-count
        after = before-multiplicity
        low, high = min(low, after), max(high, before)
        count += multiplicity
    require(count == d, "all profile jumps counted")
    return points, low, high


def spread_profiles():
    endpoints = interiors = 0
    largest = F(0)
    checksum = sha256()
    for d in range(2, 39):
        cuts = {F(1, d), F(1, 2)}
        for denominator in range(2, d):
            for numerator in range(1, denominator//2+1):
                point = F(numerator, denominator)
                if F(1, d) <= point <= F(1, 2):
                    cuts.add(point)
        ordered = sorted(cuts)
        values = []
        for step in ordered:
            points, low, high = profile(d, step)
            q = step.denominator
            N, r = divmod(d, q)
            require(2 <= q <= d and N >= 1, "all collision denominators covered")
            uniform = Counter({F(i, q): N for i in range(1, q+1)})
            tail = Counter(residue_one(1-j*step) for j in range(r))
            require(points == uniform+tail, "full uniform periods plus residual points")
            require(r <= q-1 <= N*(2*q-3), "rational endpoint bound")
            require(high-low <= N+r <= F(2*d, 3), "spread endpoint oscillation")
            values.append(high-low)
            largest = max(largest, (high-low)/d)
            checksum.update(f"{d}:{step}:{low}:{high}\n".encode())
            endpoints += 1
        for i in range(len(ordered)-1):
            for fraction in (F(1, 3), F(1, 2), F(2, 3)):
                step = (1-fraction)*ordered[i]+fraction*ordered[i+1]
                _, low, high = profile(d, step)
                require(high-low <= (1-fraction)*values[i]+fraction*values[i+1],
                        "interior convexity control")
                interiors += 1
    require(largest == F(2, 3), "sharp rational spread control")
    return dict(multiplicities=[2, 38], complete_collision_endpoints=endpoints,
                interior_convexity_controls=interiors, maximum_normalized_oscillation=str(largest),
                profile_sha256=checksum.hexdigest(),
                scope="Every ordering-cell endpoint in the bounded multiplicity range; unbounded-cell convexity is proved in the manuscript.")


def local_descent():
    checksum = sha256()
    total = maximum = peak = 0
    for seed in range(3, 2**17, 2):
        state, steps = seed, 0
        while state >= seed:
            require(steps < 10000, "unfinished local first descent")
            raw = 3*state+1
            state = raw >> valuation(raw)
            require(state > 0 and state % 2 == 1, "positive odd local state")
            checksum.update(f"{seed}:{state}\n".encode())
            steps += 1
            peak = max(peak, state)
        total += steps
        maximum = max(maximum, steps)
    return dict(odd_seed_range=[3, 2**17-1], seeds=2**16-1, exact_odd_steps=total,
                maximum_steps=maximum, maximum_output=peak,
                first_descent_sha256=checksum.hexdigest(),
                scope="Every seed reaches a smaller positive odd integer; strong induction gives convergence to1 throughout the range.")


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


def family_controls():
    words = cycles = arrows = factors = clustered = spread = runs = 0
    checksum = sha256()
    for m in range(5, 12):
        for d in range(2, m-2):
            for a in range(1, m-d-1):
                for b in range(1, m-d-a):
                    c = m-d-a-b
                    for h in range(1, (m+1)//2):
                        if gcd(h, m) != 1:
                            continue
                        k, step = pow(h, -1, m), F(h, m)
                        K = continued_fraction_sum(k, m)
                        for t in (2, 3, 7):
                            for V in (t+1, t+9):
                                for A, B in ((1, t), (t, 1)):
                                    track = [V]*d+[A]*a+[B]*b+[A]*c
                                    word = [0]*m
                                    offset = (m-1-(d-1)*h) % m
                                    for j, letter in enumerate(track):
                                        word[(offset+j*h) % m] = letter
                                    template = [A if letter == V else letter for letter in word]
                                    high = [i+1 for i, letter in enumerate(word) if letter == V]
                                    scaled = [d*(i+1)-m*sum(z < i+1 for z in high) for i in range(m)]
                                    boundaries = {(m-1) % m, (m-1-d*h) % m,
                                                  (m-1+a*h) % m, (m-1+(a+b)*h) % m}
                                    mismatches = {i for i in range(m) if word[i] != word[(i+h) % m]}
                                    require(mismatches == boundaries and len(boundaries) == 4,
                                            "four exact track boundaries")
                                    variation = sum(abs(word[i]-word[(i+h) % m]) for i in range(m))
                                    require(variation == 2*(V-A)+2*abs(A-B) < 4*V,
                                            "maximum variation bound")
                                    require(sum(word)-sum(template) == d*(V-A), "template edit total")
                                    for start in range(m):
                                        number = total = 0
                                        for length in range(1, m):
                                            index = (start+length-1) % m
                                            number += word[index] == V
                                            total += template[index]
                                            end = (start+length) % m
                                            require(scaled[end]-scaled[start] == d*length-m*number,
                                                    "exact cyclic profile difference")
                                            deviation = m*total-sum(template)*length
                                            require(abs(deviation) <= 2*(t-1)*(K-1)*m,
                                                    "weighted proper-factor discrepancy")
                                            factors += 1
                                    _, low, high_value = profile(d, step)
                                    if d*h < m:
                                        require(low == 0, "cluster profile minimum")
                                        R = 1-d*step
                                        for i in range(m):
                                            e = F(i+1, m)
                                            J = max(F(scaled[i], m*d), F(scaled[(i+h) % m], m*d))
                                            if e <= R:
                                                require(J == e+step, "cluster first branch")
                                            else:
                                                require(J <= e, "cluster middle bound")
                                            if e > 1-step:
                                                require(J == e-F(d-1, d), "cluster last branch")
                                            if e == 1:
                                                require(J == F(1, d), "cluster final value")
                                        clustered += 1
                                    else:
                                        require(high_value-low <= F(2*d, 3), "spread finite-word profile")
                                        spread += 1
                                    words += 1
                                    cycle = reduced_cycle(word)
                                    if cycle is not None:
                                        q, states = cycle
                                        require(q > 1, "finite actual controls retain higher addends")
                                        runs += addend_runs(word, states, q)
                                        cycles += 1
                                        arrows += m
                                        checksum.update(f"{m}:{d}:{a}:{b}:{c}:{h}:{t}:{V}:{A}:{q}:{states}\n".encode())
    require(clustered and spread and cycles and runs, "both profile regimes and genuine cycle controls")
    return dict(periods=[5, 11], multiplicities="every2..m-3", lower_labels=[2, 3, 7],
                maximum_values="t+1 and t+9", track_steps="all coprime0<h<m/2",
                lower_label_arrangements="both", all_positive_arc_lengths=True,
                geometry_words=words, proper_profile_and_discrepancy_factors=factors,
                clustered_words=clustered, spread_words=spread, actual_reduced_cycles=cycles,
                exact_cycle_arrows=arrows, addend_ones_runs=runs, control_sha256=checksum.hexdigest(),
                scope="Exact identities and actual 3x+q controls; finite absence is not used to prove the theorem.")


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


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: checker [--write-receipt]")
    result = dict(schema="contiguous-maximum-four-arc-v1", constants=constants(),
                  rank_cases=rank_cases(), spread_profiles=spread_profiles(), exact_gap=exact_gap(),
                  local_descent=local_descent(), family_controls=family_controls(),
                  standard_controls=standard_controls())
    encoded = json.dumps(result, sort_keys=True, indent=2)+"\n"
    destination = HERE/"check_maximum_arc.json"
    if sys.argv[1:]:
        destination.write_text(encoded)
    else:
        require(destination.read_text() == encoded, "receipt differs; inspect before regenerating")
    print(json.dumps(dict(status="passed", maximum_multiplicities=37,
                          profile_endpoints=result["spread_profiles"]["complete_collision_endpoints"],
                          local_seeds=result["local_descent"]["seeds"],
                          geometry_words=result["family_controls"]["geometry_words"],
                          actual_reduced_cycles=result["family_controls"]["actual_reduced_cycles"],
                          standard_cycles=result["standard_controls"]["cycles"]), sort_keys=True))


if __name__ == "__main__":
    main()


