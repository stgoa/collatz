"""Exact finite steps for positive-interface Mersenne exclusions."""

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CUTOFF = 1 << 23
LOCAL_LIMIT = 1 << 23
LOW_LEVEL_LIMIT = 256
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


def constants_and_small_seeds():
    low2, high2 = log_enclosure(2, 32)
    low3, high3 = log_enclosure(3, 32)
    require(Fraction(1, 2) < low2 < high2 < 1 and 0 < low3 < high3 < 2,
            "elementary logarithm and LMN height bounds")
    require(3**5 < 2**8, "alpha below eight fifths")
    require(2**8 * 35**5 - 106**5 == 63344224 > 0, "minimum-35 product bound")
    require(Fraction(1217, 25) / low2 < 98, "LMN coefficient")
    require(Fraction(8, 5)/2 + 1 < 2, "LMN coefficient parameter")
    require(Fraction(2, 5)-Fraction(3, 5)**2 == Fraction(1, 25),
            "positive elimination coefficient")
    require(25*(Fraction(3, 5)+1) == 40 and 25*Fraction(3, 5) == 15,
            "HL first length coefficients")
    require(Fraction(3, 5)*40+1 == 25 and Fraction(3, 5)*15+1 == 10,
            "HL second length coefficients")
    require(Fraction(13, 5)*Fraction(3, 8) == Fraction(39, 40), "LH cone coefficient")
    require(40*Fraction(13, 5) == 104, "LH cone length")
    require(65/Fraction(17, 32) == Fraction(2080, 17), "HL cone length")
    H = 1+98*25**2
    bounds = {
        "low_level_band": (Fraction(65), Fraction(25*LOW_LEVEL_LIMIT+65)),
        "low_high_cone": (Fraction(104), Fraction(40)),
        "high_low_cone": (Fraction(2080, 17), Fraction(2080, 17)),
    }
    records = {}
    for name, (slope, constant) in bounds.items():
        upper = slope*H+constant
        derivative_bound = slope*392*25
        require(upper < CUTOFF, "LMN cutoff: "+name)
        require(derivative_bound < CUTOFF, "cutoff derivative: "+name)
        records[name] = dict(coefficient=str(slope), constant=str(constant),
                             upper_at_cutoff=str(upper), margin=str(CUTOFF-upper),
                             derivative_margin_times_cutoff=str(CUTOFF-derivative_bound))
    require(1/low2 < 25, "decreasing logarithmic ratio")
    require(H == 61251, "H at cutoff")
    rows = []
    for seed in range(3, 34, 2):
        states = [seed]
        while states[-1] != 1:
            require(len(states) < DESCENT_GUARD, "unfinished small-seed convergence")
            raw = 3*states[-1]+1
            states.append(raw >> valuation(raw))
        rows.append(dict(seed=seed, states=states))
    require(len(rows) == 16, "complete minimum-35 check")
    return dict(log_series_terms=32, ln2_bounds=[str(low2), str(high2)],
                ln3_bounds=[str(low3), str(high3)], local_minimum=35,
                small_seed_trajectories=rows, low_level_limit=LOW_LEVEL_LIMIT,
                half_length_cutoff=CUTOFF, H_at_cutoff=H,
                length_regions=records, lmn_coefficient="1217/25",
                logarithmic_heights=[1, 2], binary_gap_coefficient=98)


def polynomial_identities():
    # Coefficient dictionaries give identities, not evaluations at selected points.
    variables = ["N", "L", "h", "z", "c", "lambda"]
    zero = (0,)*len(variables)

    def constant(value):
        return {zero: value} if value else {}

    def var(index):
        term = [0]*len(variables)
        term[index] = 1
        return {tuple(term): 1}

    def add(*polys):
        answer = {}
        for poly in polys:
            for term, coefficient in poly.items():
                answer[term] = answer.get(term, 0)+coefficient
        return {term: c for term, c in answer.items() if c}

    def scale(value, poly):
        return {term: value*c for term, c in poly.items() if value*c}

    def mul(*polys):
        answer = constant(1)
        for poly in polys:
            result = {}
            for first, a in answer.items():
                for second, b in poly.items():
                    term = tuple(x+y for x, y in zip(first, second))
                    result[term] = result.get(term, 0)+a*b
            answer = {term: c for term, c in result.items() if c}
        return answer

    N, L, h, z, c, lam = [var(i) for i in range(len(variables))]
    one = constant(1)
    Nm, Lm = add(N, constant(-1)), add(L, constant(-1))
    eta = add(one, scale(-1, lam))
    state_num = add(mul(h, Nm), mul(N, lam, h, Lm),
                    mul(add(L, scale(-1, N)), c, z))
    K_num = add(state_num, mul(h, N, Lm, eta))
    claimed = add(mul(add(mul(N, L), constant(-1)), h),
                  scale(-1, mul(add(N, scale(-1, L)), c, z)))
    require(not add(K_num, scale(-1, claimed)), "HL canonical K identity")
    # The numerator after subtracting (addend)*B[-cut] and B is odd.
    require(not add(mul(Nm, h), scale(-1, mul(N, h)), h),
            "LH second-block endpoint subtraction")
    require(not add(mul(Lm, h), scale(-1, mul(L, h)), h),
            "HL second-block endpoint subtraction")
    # The sharper LH affine estimate uses sigma*h=(L-1)b_A-z.
    require(not add(add(one, mul(L, lam)), mul(L, eta),
                    scale(-1, add(L, one))), "LH sharper affine coefficient")
    return dict(variables=variables, coefficient_identities=4)


def terminal_intercepts():
    count = equalities = 0
    for length in range(1, 7):
        for prefix in product(range(1, 4), repeat=length-1):
            for last in range(1, 10):
                word = prefix+(last,)
                total, C = sum(word), intercept(word)
                running = 0
                for i, letter in enumerate(word):
                    require(running <= total-last-length+1+i, "terminal prefix exponent")
                    running += letter
                actual = Fraction(C, 1 << total)
                bound = Fraction(3**length-(1 << length), 1 << (last+length-1))
                require(actual <= bound, "terminal intercept upper bound")
                equalities += actual == bound
                count += 1
    return dict(lengths=[1, 6], prefix_letters=[1, 3], last_letters=[1, 9],
                words=count, sharp_equalities=equalities)


def signed_join(name, J, r, order, h, A, B):
    N, L = 1 << J, 1 << r
    d_A, d_B = (N-1, L-1) if order == "HL" else (L-1, N-1)
    states_A = trace(-h, d_A, A)
    z = states_A[-1]
    require(z > 0 and trace(z, d_B, B)[-1] == h, "positive-interface signed join")
    require(J > r >= 1 and (A[-1] > J-r and B[-1] > r if order == "HL"
                            else B[-1] > J), "signed boundary conditions")
    u, v = list(A)+list(B), list(A)+list(B)
    if order == "HL":
        u[len(A)-1] -= J-r
        u[-1] -= r
        v[-1] += J
    else:
        u[len(A)-1] += J-r
        u[-1] -= J
        v[-1] += r
    word = u+v
    a, b, P, T = len(A), len(B), sum(A), sum(B)
    m, S = a+b, P+T
    require(sum(word) == 2*S and len(word) == 2*m, "half length and total")
    D, C = (1 << (2*S))-3**(2*m), intercept(word)
    require(D > 0, "positive reconstructed denominator")
    q = D//gcd(C, D)
    x = Fraction(C, D)
    X = q*x
    require(X.denominator == 1 and X.numerator % 2 == 1 and q % 2 == 1,
            "odd reduced integer cycle")
    actual = trace(X.numerator, q, word)
    require(actual[-1] == X.numerator and min(actual) > 0, "reduced cycle closure")
    Y, y = actual[a], Fraction(actual[a], q)
    sigma, c = Fraction(3**a, 1 << P), Fraction(3**b, 1 << T)
    eta = 1-sigma*c
    R_a = Fraction(3, 2)**a
    first_power = N if order == "HL" else L
    require(Fraction(actual[m], q) == first_power*x+h, "canonical half closure")
    if order == "HL":
        K = (N-1)*X.numerator+q*h
        prefix_bracket = (N-1)*Y-(1 << (J-r))*q*z
        difference = (L-1)*Y-q*z
        tail_bracket = N*(L-1)*X.numerator-q*h
        prefix_exponent, tail_exponent = P-J+r, T-r
        require(3**a*K == (1 << prefix_exponent)*prefix_bracket,
                "HL exact modified first boundary")
        require((N-1)*x+h == ((N*L-1)*h-(N-L)*c*z)/(N*(L-1)*eta),
                "HL canonical K formula")
        require((N-1)*x+h < L*h/((L-1)*eta) <= 2*h/eta,
                "HL tight K upper bound")
        require(sigma*h+z < L*(R_a-1) and h < Fraction(1 << (P+r), 1 << a),
                "HL signed first budget")
        require((L-1)*y < 2*L*R_a/eta and z < 2*L*R_a/eta,
                "HL positive difference size bounds")
    else:
        K = (L-1)*X.numerator+q*h
        prefix_bracket = (L-1)*(1 << (J-r))*Y-q*z
        difference = (N-1)*Y-q*z
        tail_bracket = L*(N-1)*X.numerator-q*h
        prefix_exponent, tail_exponent = P, T-J
        require(3**a*K == (1 << P)*prefix_bracket, "LH exact modified first boundary")
        require((L-1)*x+h < (1+Fraction(1, L))*h/eta,
                "LH sharp K upper bound")
        require(h < Fraction((L-1)*(1 << P), 1 << a), "LH signed first budget")
        require((N-1)*y < (L+1)*R_a/eta and z < (L+1)*R_a/eta,
                "LH sharp positive difference size bounds")
        # Exponentiate the denominator law to avoid floating-point logarithms.
        # From a<r+log2(q/eta), and b<(alpha-1)a+r+log2(q/eta)+c_r:
        require(Fraction(1 << a) < L*q/eta, "LH rational first-length bound")
        require(Fraction(1 << b) < R_a*(L+1)*q/eta, "LH rational second-length bound")
    require(prefix_bracket % 2 and tail_bracket % 2, "both boundary brackets odd")
    require(valuation(K) == prefix_exponent, "exact first binary valuation")
    require(3**b*difference == (1 << tail_exponent)*tail_bracket,
            "exact second start-difference identity")
    require(difference != 0 and valuation(difference) == tail_exponent,
            "exact second binary valuation")
    require(abs(difference) < max((L-1 if order == "HL" else N-1)*Y, q*z),
            "positive start difference bounded by maximum")
    require(q > 1, "actual reconstructed control retains denominator")
    return dict(name=name, J=J, r=r, order=order, h=h, interface=z,
                A=list(A), B=list(B), half_length=m, half_total=S,
                normalized_state=str(x), denominator=q, actual_start=X.numerator,
                actual_modified_endpoint=Y, scaled_difference=difference,
                prefix_v2=prefix_exponent, difference_v2=tail_exponent,
                actual_minimum=min(actual), arrows=len(word))


def genuine_controls():
    rows = []
    for loops in (0, 1, 3):
        rows.append(signed_join("two_four", 3, 1, "HL", 1,
                                (2, 1)+(1, 3)*(loops+1), (4,)))
        rows.append(signed_join("one_five", 3, 2, "HL", 3,
                                (1, 2, 1)+(1, 3)*(loops+1), (1, 1, 4)))
        rows.append(signed_join("low_high_cone", 5, 3, "LH", 1,
                                (2, 1)+(1, 3)*loops+(1,), (6,)))
    rows.append(signed_join("large_endpoint", 8, 6, "HL", 261,
                            (4, 2, 2, 1, 5, 1, 1, 1, 1, 3, 3, 1, 2, 2, 6, 1, 2, 2, 1, 1, 3),
                            (1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 7)))
    require(rows[0]["denominator"] == 361 and rows[0]["scaled_difference"] == -600,
            "negative difference countercontrol")
    require(rows[2]["denominator"] == 41 and 8*rows[2]["r"] <= 5*rows[2]["J"],
            "genuine inside-cone control")
    return dict(count=len(rows), records=rows, arrows=sum(row["arrows"] for row in rows),
                scope="Specified genuine signed joins and exact reduced 3x+q cycles; no absence census")


def finite_minimum_bound():
    band = 65*27+25*LOW_LEVEL_LIMIT+65-1
    lh_cone = 104*27+40-1
    hl_cone = (Fraction(2080, 17)*28).__ceil__()-1
    require((band, lh_cone, hl_cone) == (8219, 2847, 3425), "strict region cutoffs")
    maximum, maximum_at, maximum_total = Fraction(), 0, 0
    checksum = sha256()
    three = 1
    for m in range(1, band+1):
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
    require(ceiling == 4687853 < LOCAL_LIMIT and maximum_at == 7621,
            "maximum minimum bound")
    return dict(exponents=[1, band], checks=band, exact_gap_sha256=checksum.hexdigest(),
                region_half_length_maxima=dict(band=band, low_high=lh_cone, high_low=hl_cone),
                maximum_minimum_bound=str(maximum), maximum_at=maximum_at,
                maximum_total=maximum_total, strict_integer_ceiling=ceiling,
                local_limit_exclusive=LOCAL_LIMIT)


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script [--write-receipt]")
    receipt = dict(schema="positive-interface-mersenne-v1", constants=constants_and_small_seeds(),
                   polynomial=polynomial_identities(), terminal_intercepts=terminal_intercepts(),
                   signed_joins=genuine_controls(), fractional_gaps=fractional_gaps(),
                   finite_minimum=finite_minimum_bound(), local_descent=local_descent(),
                   actual_controls=actual_controls())
    target = HERE / "check_positive_interface.json"
    encoded = json.dumps(receipt, indent=2, sort_keys=True)+"\n"
    if sys.argv[1:]:
        target.write_text(encoded)
    else:
        require(target.read_text() == encoded, "receipt differs; inspect and regenerate")
    print(json.dumps(dict(result="passed", terminal_words=receipt["terminal_intercepts"]["words"],
                          genuine_signed_joins=receipt["signed_joins"]["count"],
                          gap_intervals=receipt["fractional_gaps"]["checked_exponents"],
                          finite_minimum_checks=receipt["finite_minimum"]["checks"],
                          local_odd_seeds=receipt["local_descent"]["odd_seeds"],
                          standard_cycles=11), sort_keys=True))


if __name__ == "__main__":
    main()
