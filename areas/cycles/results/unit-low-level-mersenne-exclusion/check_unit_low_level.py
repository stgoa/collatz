"""Exact finite steps for the all-r=1 low-to-high Mersenne exclusion."""

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CUTOFF = 1 << 22
LOCAL_LIMIT = 1 << 20
DESCENT_GUARD = 100000


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def valuation(value):
    require(value != 0, "valuation of zero")
    value = abs(value)
    return (value & -value).bit_length() - 1


def intercept(word):
    C = total = 0
    for letter in word:
        require(letter >= 1, "positive valuation")
        C = 3 * C + (1 << total)
        total += letter
    return C


def trace(start, addend, word):
    states = [start]
    for letter in word:
        require(states[-1] != 0 and states[-1] % 2 == 1, "nonzero odd input")
        raw = 3 * states[-1] + addend
        require(raw != 0 and valuation(raw) == letter, "exact signed valuation")
        states.append(raw // (1 << letter))
    require(states[-1] != 0 and states[-1] % 2 == 1, "nonzero odd endpoint")
    return states


def log_enclosure(value, terms):
    z = Fraction(value - 1, value + 1)
    low = 2 * sum((z**(2*j + 1) / (2*j + 1) for j in range(terms)), Fraction())
    tail = 2 * z**(2*terms + 1) / ((2*terms + 1) * (1-z*z))
    return low, low + tail


def constants_and_small_seeds():
    low2, high2 = log_enclosure(2, 32)
    low3, high3 = log_enclosure(3, 32)
    require(Fraction(1, 2) < low2 < high2 < 1 and 0 < low3 < high3 < 2,
            "elementary logarithm and LMN height bounds")
    require(3**5 < 2**8, "alpha below eight fifths")
    require(2**8 * 35**5 - 106**5 == 63344224 > 0, "state-floor product bound")
    lmn = Fraction(2434, 100) * 1 * 2
    require(lmn == Fraction(1217, 25) and lmn / low2 < 98, "LMN coefficient")
    require(Fraction(8, 5)/2 + 1 == Fraction(9, 5) < 2, "LMN parameter")
    require(Fraction(2, 5) - Fraction(3, 5)**2 == Fraction(1, 25),
            "positive elimination coefficient")
    require(25 * (Fraction(3, 5) + 1) == 40 and
            25 * (2*Fraction(3, 5) + 1) == 55, "second length constants")
    require(Fraction(3, 5)*40+1 == 25 and Fraction(3, 5)*55+2 == 35,
            "first length constants")
    H = 1 + 98 * 24**2
    margin = CUTOFF - (65*H+90)
    derivative_margin = CUTOFF - 25480*24
    require(H == 56449 and margin == 525029 > 0, "LMN length cutoff")
    require(65*196*2 == 25480 and derivative_margin == 3582784 > 0,
            "cutoff derivative")
    require(1/low2 < 24, "decreasing logarithmic ratio")
    rows = []
    for seed in range(3, 34, 2):
        states = [seed]
        while states[-1] != 1:
            require(len(states) < DESCENT_GUARD, "unfinished small-seed convergence")
            raw = 3*states[-1]+1
            states.append(raw >> valuation(raw))
        rows.append(dict(seed=seed, states=states))
    require(len(rows) == 16, "complete minimum-35 control")
    return dict(log_series_terms=32,
                logarithm_enclosures={"ln2": [str(low2), str(high2)],
                                      "ln3": [str(low3), str(high3)]},
                local_minimum=35, product_margin=63344224, small_seed_trajectories=rows,
                lmn_coefficient=str(lmn), lmn_logarithmic_heights=[1, 2],
                binary_gap_coefficient=98, half_length_cutoff=CUTOFF,
                H_at_cutoff=H, cutoff_margin=margin,
                derivative_margin_times_cutoff=derivative_margin,
                length_bound_coefficients=[65, 90])


def polynomial_identity():
    zero = (0,) * 7

    def constant(n):
        return {zero: n} if n else {}

    def variable(i):
        powers = [0] * 7
        powers[i] = 1
        return {tuple(powers): 1}

    def add(*values):
        out = {}
        for value in values:
            for term, coefficient in value.items():
                out[term] = out.get(term, 0) + coefficient
        return {term: c for term, c in out.items() if c}

    def scale(n, value):
        return {term: n*c for term, c in value.items() if n*c}

    def mul(*values):
        out = constant(1)
        for value in values:
            nxt = {}
            for x, cx in out.items():
                for y, cy in value.items():
                    term = tuple(a+b for a, b in zip(x, y))
                    nxt[term] = nxt.get(term, 0) + cx*cy
            out = {term: c for term, c in nxt.items() if c}
        return out

    N, R, U, V, W, h, g = [variable(i) for i in range(7)]
    D = add(mul(U, W), scale(-1, mul(R, V)))
    CA = add(mul(h, R), scale(-1, mul(g, U)))
    F = add(mul(add(scale(2, N), constant(-1)), h, R),
            scale(-1, mul(add(N, constant(-2)), g, U)))
    positive = add(mul(add(N, constant(1)), h, R), mul(add(N, constant(-2)), CA))
    numerator = add(mul(h, add(scale(2, mul(add(N, constant(-1)), R, V)), mul(U, W))),
                    scale(-1, mul(add(N, constant(-2)), g, U, V)))
    require(not add(F, scale(-1, positive)), "positive residual rewrite")
    require(not add(numerator, scale(-1, mul(h, D)), scale(-1, mul(V, F))),
            "canonical residual identity")
    return dict(variables=["N", "3^a", "2^P", "3^b", "2^T", "h", "g"], identities=2)


def terminal_intercepts():
    checked = equalities = 0
    for b in range(1, 7):
        for prefix in product(range(1, 4), repeat=b-1):
            for J in range(2, 8):
                for extra in (1, 2, 3):
                    v = J + extra
                    B = prefix + (v,)
                    T, C = sum(B), intercept(B)
                    current = 0
                    for i, letter in enumerate(B):
                        require(current <= T-v-b+1+i, "terminal prefix exponent bound")
                        current += letter
                    bound = Fraction(3**b-(1 << b), 1 << (v+b-1))
                    actual = Fraction(C, 1 << T)
                    require(actual <= bound, "terminal-intercept bound")
                    require(((1 << J)-1)*actual <=
                            Fraction((1 << J)-1, 1 << J)*(Fraction(3, 2)**b-1),
                            "uniform high-boundary budget")
                    equalities += actual == bound
                    checked += 1
    return dict(lengths=[1, 6], preceding_letters=[1, 3], levels=[2, 7],
                terminal_excess=[1, 2, 3], words=checked, sharp_bound_equalities=equalities)


def signed_prefixes():
    counts = {name: 0 for name in ("closed_expanding", "expanding_increase",
                                  "expanding_decrease", "contracting_decrease")}
    examples = {}
    cases = modified = divisible_three = 0
    for h in range(1, 64, 2):
        A, state = [], -h
        for a in range(1, 13):
            raw = 3*state+1
            exponent = valuation(raw)
            A.append(exponent)
            state = raw >> exponent
            g, P, C = -state, sum(A), intercept(A)
            require(0 < g and C == h*3**a-g*(1 << P) > 0, "negative endpoint identity")
            require(3**a != 1 << P, "nonempty slope is not one")
            if 3**a < 1 << P:
                require(g < h, "contraction decreases magnitude")
                kind = "contracting_decrease"
            else:
                kind = "closed_expanding" if g == h else (
                    "expanding_increase" if g > h else "expanding_decrease")
            counts[kind] += 1
            examples.setdefault(kind, dict(h=h, g=g, word=list(A), length=a, total=P))
            cases += 1
            divisible_three += h % 3 == 0
            for J in (2, 3, 7):
                N = 1 << J
                F = (2*N-1)*h*3**a-(N-2)*g*(1 << P)
                require(F == (N+1)*h*3**a+(N-2)*C and 0 < F < 2*N*h*3**a,
                        "residual bounds without slope restriction")
                for q in (1, 5, 61):
                    modulus = 3**a
                    Y = (-q*g*pow(1 << (J-1), -1, modulus)) % modulus
                    if Y % 2 == 0:
                        Y += modulus
                    start = Fraction((1 << P)*((1 << (J-1))*Y+q*g), modulus)-q*h
                    while start <= 0:
                        Y += 2*modulus
                        start = Fraction((1 << P)*((1 << (J-1))*Y+q*g), modulus)-q*h
                    require(start.denominator == 1, "integral modified start")
                    changed = A[:-1]+[A[-1]+J-1]
                    require(trace(start.numerator, q, changed)[-1] == Y, "exact modified positive prefix")
                    require(valuation(start.numerator+q*h) == P, "shifted binary valuation")
                    modified += 1
    require(all(counts.values()) and divisible_three > 0, "all first-prefix regimes represented")

    second = []
    for J, g, h, guard in ((5, 3, 1, 10), (17, 53399, 1, 10)):
        d = (1 << J)-1
        states, B = [-g], []
        while True:
            require(len(B) < guard, "specified second segment did not reach its endpoint")
            raw = 3*states[-1]+d
            require(raw != 0, "specified second segment hit zero")
            v = valuation(raw)
            B.append(v)
            states.append(raw >> v)
            if states[-1] == h and v > J:
                break
        b, T = len(B), sum(B)
        c = Fraction(3**b, 1 << T)
        require(trace(-g, d, B) == states, "exact second segment replay")
        require(h+c*g == d*Fraction(intercept(B), 1 << T), "second endpoint identity")
        require(h+c*g <= Fraction(d, 1 << J)*(Fraction(3, 2)**b-1), "signed second budget")
        require(h+1 < Fraction(3, 2)**b, "strict endpoint budget")
        second.append(dict(J=J, g=g, h=h, length=b, total=T, last_valuation=B[-1],
                           last_predecessor=states[-2],
                           word_sha256=sha256(json.dumps(B).encode()).hexdigest()))
    return dict(first_starts_odd=[1, 63], first_lengths=[1, 12],
                first_prefixes=cases, regimes=counts, examples=examples,
                starts_divisible_by_three=divisible_three,
                modified_levels=[2, 3, 7], modified_addends=[1, 5, 61],
                modified_positive_trajectories=modified, second_segments=second,
                scope="Genuine partial segments; no complete first/second join is asserted")


def fractional_gaps():
    low2, high2 = log_enclosure(2, 80)
    low3, high3 = log_enclosure(3, 80)
    low_alpha, high_alpha = low3/high2, high3/low2
    scale = 1 << 96
    low_num = (low_alpha*scale).__floor__()
    high_num = (high_alpha*scale).__ceil__()
    require(Fraction(low_num, scale) <= low_alpha < high_alpha <= Fraction(high_num, scale),
            "outward dyadic enclosure")
    require(high_num == low_num+1, "adjacent dyadic endpoints")
    low = high = 0
    minimum, minimum_at = scale, 0
    threshold = 1 << 71
    for r in range(1, CUTOFF):
        low += low_num
        high += high_num
        floor = low >> 96
        require(high >> 96 == floor, "fractional interval crosses an integer")
        complement = scale-(high-(floor << 96))
        require(complement > threshold, "positive fractional gap too small")
        if complement < minimum:
            minimum, minimum_at = complement, r
    return dict(series_terms=80, dyadic_denominator_bits=96,
                alpha_lower_numerator=low_num, alpha_upper_numerator=high_num,
                exponents=[1, CUTOFF-1], checked_exponents=CUTOFF-1,
                fractional_distance_bits=25, natural_log_gap_bits=26, eta_bits=27,
                threshold_numerator=threshold, minimum_complement_numerator=minimum,
                minimum_complement_at=minimum_at)


def finite_minimum_bound():
    max_m = 65*27+90-1
    require(max_m == 1844, "strict integer length cutoff")
    maximum, maximum_at, maximum_total = Fraction(), 0, 0
    checksum = sha256()
    three = 1
    for m in range(1, max_m+1):
        three *= 3
        S = three.bit_length()
        two = 1 << S
        gap = two-three
        require(3*LOCAL_LIMIT*gap > m*two, "finite minimum-state contradiction")
        upper = Fraction(m*two, 3*gap)
        if upper > maximum:
            maximum, maximum_at, maximum_total = upper, m, S
        checksum.update(f"{m}:{S}:{gap:x}\n".encode())
    ceiling = maximum.__ceil__()
    require(ceiling < LOCAL_LIMIT, "minimum ceiling below local descent range")
    return dict(exponents=[1, max_m], checks=max_m, exact_gap_sha256=checksum.hexdigest(),
                maximum_minimum_bound=str(maximum), maximum_at=maximum_at,
                maximum_total=maximum_total, strict_integer_ceiling=ceiling,
                local_limit_exclusive=LOCAL_LIMIT)


def local_descent():
    count = steps = maximum_steps = longest_seed = 0
    peak = 1
    for seed in range(3, LOCAL_LIMIT, 2):
        current, used = seed, 0
        while current >= seed:
            require(used < DESCENT_GUARD, "unfinished local descent")
            raw = 3*current+1
            current = raw >> valuation(raw)
            require(current > 0 and current % 2 == 1, "positive odd local cut")
            peak = max(peak, current)
            used += 1
        count += 1
        steps += used
        if used > maximum_steps:
            maximum_steps, longest_seed = used, seed
    require(count == LOCAL_LIMIT//2-1, "complete local seed coverage")
    return dict(limit_exclusive=LOCAL_LIMIT, odd_seeds=count, odd_steps=steps,
                maximum_local_steps=maximum_steps, first_longest_seed=longest_seed,
                peak_odd_output=peak, per_seed_guard=DESCENT_GUARD,
                conclusion="Every odd seed 3<=s<limit reaches a smaller positive odd seed")


def actual_controls():
    path = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    rows, arrows = [], 0
    for entry in json.loads(path.read_text())["cycles"]:
        d, states, word = entry["d"], entry["states"], entry["valuations"]
        require(trace(states[0], d, word) == states+[states[0]], "actual fixture arrows")
        C, D = intercept(word), (1 << sum(word))-3**len(word)
        require(D > 0 and Fraction(C, D) == Fraction(states[0], d), "normalized fixture")
        q = D//gcd(C, D)
        require(d % q == 0 and q > 1, "control fails denominator-one hypothesis")
        rows.append(dict(addend=d, odd_period=len(word), reduced_denominator=q,
                         failed_hypothesis="q=1"))
        arrows += len(word)
    require(len(rows) == 11 and {row["addend"] for row in rows} == {5, 7, 13, 61},
            "complete actual-cycle controls")
    return dict(fixture_sha256=sha256(path.read_bytes()).hexdigest(), cycles=rows,
                count=len(rows), arrows=arrows)


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script [--write-receipt]")
    receipt = dict(schema="unit-low-level-mersenne-v1", constants=constants_and_small_seeds(),
                   polynomial=polynomial_identity(), terminal_intercepts=terminal_intercepts(),
                   signed_prefixes=signed_prefixes(), fractional_gaps=fractional_gaps(),
                   finite_minimum=finite_minimum_bound(), local_descent=local_descent(),
                   actual_controls=actual_controls())
    target = HERE / "check_unit_low_level.json"
    encoded = json.dumps(receipt, indent=2, sort_keys=True)+"\n"
    if sys.argv[1:]:
        target.write_text(encoded)
    else:
        require(target.read_text() == encoded, "receipt differs; inspect and regenerate")
    print(json.dumps(dict(result="passed", terminal_words=receipt["terminal_intercepts"]["words"],
                          modified_prefixes=receipt["signed_prefixes"]["modified_positive_trajectories"],
                          gap_intervals=receipt["fractional_gaps"]["checked_exponents"],
                          finite_minimum_checks=receipt["finite_minimum"]["checks"],
                          local_odd_seeds=receipt["local_descent"]["odd_seeds"],
                          standard_cycles=11), sort_keys=True))


if __name__ == "__main__":
    main()
