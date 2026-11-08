#!/usr/bin/env python3
"""Exact elementary checks for the expanding-negative-prefix exclusion."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
from itertools import product
import json
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CUTOFF = 1 << 20
LOCAL_LIMIT = 1 << 21
DESCENT_GUARD = 10000


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation(value: int) -> int:
    require(value != 0, "valuation of zero")
    value = abs(value)
    return (value & -value).bit_length() - 1


def intercept(word: list[int] | tuple[int, ...]) -> int:
    value, power = 0, 1
    for letter in word:
        require(letter >= 1, "nonpositive valuation")
        value = 3 * value + power
        power <<= letter
    return value


def trace(start: int, addend: int, word: list[int]) -> list[int]:
    states = [start]
    for letter in word:
        require(states[-1] != 0 and states[-1] % 2 == 1, "nonodd input")
        raw = 3 * states[-1] + addend
        require(raw != 0 and valuation(raw) == letter, "inexact arrow")
        states.append(raw // (1 << letter))
    require(states[-1] != 0 and states[-1] % 2 == 1, "nonodd output")
    return states


def log_enclosure(value: int, terms: int = 32) -> tuple[Fraction, Fraction]:
    # ln(value)=2*sum z^(2j+1)/(2j+1), z=(value-1)/(value+1).
    # Bound the positive remainder by replacing later denominators
    # with 2*terms+1 and summing a geometric series.
    require(value > 1 and terms > 0, "log series domain")
    z = Fraction(value - 1, value + 1)
    low = 2 * sum((z**(2*j + 1) / (2*j + 1) for j in range(terms)), Fraction())
    tail = 2 * z**(2*terms + 1) / ((2*terms + 1) * (1 - z*z))
    return low, low + tail


def constants() -> dict:
    ln2low, ln2high = log_enclosure(2)
    ln3low, ln3high = log_enclosure(3)
    require(Fraction(1, 2) < ln2low < ln2high < 1, "ln2 bounds")
    require(0 < ln3low < ln3high < 2, "ln3 height bound")
    require(3**2 > 2**3 and 3**5 < 2**8, "alpha bounds")
    require(10**4 < 2**7 * 3**4, "state-floor total bound")
    lmn = Fraction(2434, 100) * 1 * 2
    require(lmn == Fraction(1217, 25), "LMN specialized coefficient")
    require(lmn / ln2low < 98 and 2*lmn == Fraction(2434, 25) < 98,
            "binary-gap coefficient")
    require(Fraction(7, 4)/2 + 1 == Fraction(15, 8) < 2,
            "positive-form parameter")
    require(Fraction(8, 5)/2 + 1 < 2, "negative-form parameter")
    require(Fraction(16, 3) * 2 == Fraction(32, 3), "combined gap coefficient")
    H = 1 + 98 * 22**2
    margin = 3*CUTOFF - 32*(H + 1)
    derivative_margin = 3*CUTOFF - 12544*22
    require(H == 47433 and margin == 1627840 > 0, "uniform cutoff")
    require(derivative_margin > 0 and Fraction(1, 1)/ln2low < 22,
            "cutoff derivative and decreasing ratio")
    return dict(log_series_terms=32,
                logarithm_enclosures={"ln2": [str(ln2low), str(ln2high)],
                                      "ln3": [str(ln3low), str(ln3high)]},
                alpha_bounds=["3/2", "8/5"],
                lmn_logarithmic_heights=[1, 2], lmn_field_degree=1,
                lmn_coefficient=str(lmn), binary_gap_coefficient=98,
                half_length_cutoff=CUTOFF, H_at_cutoff=H,
                cutoff_margin=margin, derivative_margin_times_cutoff=derivative_margin,
                full_word_length_upper_bound=2*CUTOFF)


def polynomial_identity() -> dict:
    # Variables N,R,U,V,W,h,g stand for N,3^a,2^P,3^b,2^T,h,g.
    zero = (0,) * 7

    def constant(n):
        return {zero: n} if n else {}

    def variable(i):
        exponents = [0] * 7
        exponents[i] = 1
        return {tuple(exponents): 1}

    def add(*values):
        out = {}
        for value in values:
            for term, coefficient in value.items():
                out[term] = out.get(term, 0) + coefficient
        return {term: coefficient for term, coefficient in out.items() if coefficient}

    def scale(n, value):
        return {term: n*coefficient for term, coefficient in value.items() if n*coefficient}

    def mul(*values):
        out = constant(1)
        for value in values:
            nxt = {}
            for x, cx in out.items():
                for y, cy in value.items():
                    term = tuple(a+b for a, b in zip(x, y))
                    nxt[term] = nxt.get(term, 0) + cx*cy
            out = {term: coefficient for term, coefficient in nxt.items() if coefficient}
        return out

    N, R, U, V, W, h, g = [variable(i) for i in range(7)]
    D = add(mul(U, W), scale(-1, mul(R, V)))
    CA = add(mul(h, R), scale(-1, mul(g, U)))
    F = add(mul(add(scale(2, N), constant(-1)), h, R),
            scale(-1, mul(add(N, constant(-2)), g, U)))
    positiveF = add(mul(add(N, constant(1)), h, R),
                    mul(add(N, constant(-2)), CA))
    numerator = add(mul(h, add(scale(2, mul(add(N, constant(-1)), R, V)), mul(U, W))),
                    scale(-1, mul(add(N, constant(-2)), g, U, V)))
    require(not add(F, scale(-1, positiveF)), "positive residual-factor identity")
    require(not add(numerator, scale(-1, mul(h, D)), scale(-1, mul(V, F))),
            "canonical residual-denominator identity")
    return dict(variables=["N", "3^a", "2^P", "3^b", "2^T", "h", "g"],
                exact_polynomial_identities=2)


def intercept_grid() -> dict:
    count, equality = 0, 0
    for length in range(1, 8):
        for word in product(range(1, 5), repeat=length):
            total, C = sum(word), intercept(word)
            prefix = 0
            for i, letter in enumerate(word):
                require(prefix <= total-length+i, "prefix exponent bound")
                prefix += letter
            bound = (1 << (total-length)) * (3**length - (1 << length))
            require(C <= bound < (1 << (total-length))*3**length, "intercept estimate")
            equality += C == bound
            count += 1
    return dict(lengths=[1, 7], letters=[1, 4], words=count, sharp_bound_equalities=equality)


def negative_prefix_controls() -> dict:
    cycles = [(1, [1]), (5, [1, 2]), (17, [1, 1, 1, 2, 1, 1, 4])]
    cases = []
    for origin, word in cycles:
        states = trace(-origin, 1, word)
        require(states[-1] == -origin and max(states) < 0, "negative cycle")
        for cut, state in enumerate(states[:-1]):
            rotated, h = word[cut:] + word[:cut], -state
            for repetitions in (1, 2, 4):
                cases.append((h, h, rotated * repetitions))
            for length in range(1, len(word)):
                tail = rotated[:length]
                g = -trace(-h, 1, tail)[-1]
                if g >= h:
                    continue
                A, repetitions = list(tail), 0
                while 3**len(A) <= 1 << sum(A):
                    require(repetitions < 200, "negative-prefix construction guard")
                    repetitions += 1
                    A = rotated * repetitions + tail
                cases.append((h, g, A))
    # A nonclosed expanding prefix whose starting magnitude is divisible
    # by 3: this guards against importing the closed-case odd-J argument.
    cases.append((3, 1, [3, 1, 1, 1]))
    boundary_checks, nonclosed, divisible_three = 0, 0, 0
    rows = []
    for h, g, A in cases:
        a, P, C = len(A), sum(A), intercept(A)
        require(0 < g <= h and h % 2 == g % 2 == 1, "negative-interface scope")
        require(trace(-h, 1, A)[-1] == -g, "exact negative prefix")
        require(3**a > 1 << P, "expanding negative prefix")
        require(C == h*3**a-g*(1 << P), "prefix endpoint identity")
        require(h*(3**a-(1 << P)) <= C < (1 << (P-a))*3**a,
                "endpoint elimination from intercept")
        nonclosed += g < h
        divisible_three += h % 3 == 0
        for J in (2, 3, 7):
            N = 1 << J
            F = (2*N-1)*h*3**a-(N-2)*g*(1 << P)
            require(F == (N+1)*h*3**a+(N-2)*C and 0 < F < 2*N*h*3**a,
                    "residual factor bounds at every parity of J")
            for q in (1, 5, 61):
                modulus = 3**a
                Y = (-q*g*pow(1 << (J-1), -1, modulus)) % modulus
                if Y % 2 == 0:
                    Y += modulus
                while True:
                    raw = (1 << P)*((1 << (J-1))*Y+q*g)
                    require(raw % modulus == 0, "modified-boundary congruence")
                    start = raw // modulus - q*h
                    if start > 0:
                        break
                    Y += 2*modulus
                modified = A[:-1] + [A[-1]+J-1]
                require(trace(start, q, modified)[-1] == Y, "genuine modified prefix")
                require(valuation(start+q*h) == P, "exact shifted valuation")
                boundary_checks += 1
        rows.append(dict(h=h, g=g, length=a, total=P))
    require(nonclosed > 0 and divisible_three > 0, "nonclosed scope controls present")
    return dict(prefixes=len(cases), nonclosed_prefixes=nonclosed,
                starts_divisible_by_three=divisible_three,
                J_values=[2, 3, 7], additive_parameters=[1, 5, 61],
                modified_positive_trajectories=boundary_checks, rows=rows,
                scope="Genuine prefixes only; no complete admissible second segment is asserted")


def fractional_gap_bootstrap() -> dict:
    ln2low, ln2high = log_enclosure(2, 80)
    ln3low, ln3high = log_enclosure(3, 80)
    alpha_low, alpha_high = ln3low/ln2high, ln3high/ln2low
    scale = 1 << 96
    low_num = (alpha_low*scale).numerator // (alpha_low*scale).denominator
    high_scaled = alpha_high*scale
    high_num = -(-high_scaled.numerator // high_scaled.denominator)
    require(Fraction(low_num, scale) <= alpha_low < alpha_high <= Fraction(high_num, scale),
            "outward dyadic rounding")
    require(high_num == low_num+1, "adjacent dyadic enclosure")
    low, high = 0, 0
    minimum_low = minimum_complement = scale
    minimum_low_at = minimum_complement_at = 0
    threshold = 1 << 71
    for exponent in range(1, CUTOFF):
        low += low_num
        high += high_num
        floor = low >> 96
        require(high >> 96 == floor, "fractional interval crosses an integer")
        residue = low - (floor << 96)
        complement = scale - (high - (floor << 96))
        require(residue > threshold and complement > threshold, "finite two-sided fractional gap")
        if residue < minimum_low:
            minimum_low, minimum_low_at = residue, exponent
        if complement < minimum_complement:
            minimum_complement, minimum_complement_at = complement, exponent
    return dict(series_terms=80, dyadic_denominator_bits=96,
                alpha_lower_numerator=low_num, alpha_upper_numerator=high_num,
                exponent_minimum=1, exponent_maximum=CUTOFF-1,
                checked_exponents=CUTOFF-1, fractional_distance_bits=25,
                threshold_numerator=threshold,
                minimum_certified_fraction_numerator=minimum_low,
                minimum_certified_fraction_at=minimum_low_at,
                minimum_certified_complement_numerator=minimum_complement,
                minimum_certified_complement_at=minimum_complement_at,
                natural_log_gap_bits=26, eta_epsilon_bits=27)


def finite_power_bootstrap() -> dict:
    a_bound, m_bound = 55, 298
    initial_m_strict = Fraction(16, 3)*(27+27+2)
    require(initial_m_strict == Fraction(896, 3) and
            (initial_m_strict.numerator-1)//initial_m_strict.denominator == m_bound,
            "initial integer bootstrap endpoints")
    stages = []
    for bits in (9, 7):
        epsilon_minimum, eta_minimum = Fraction(1), Fraction(1)
        epsilon_at = eta_at = 0
        for a in range(1, a_bound+1):
            three = 3**a
            P = three.bit_length()-1
            epsilon = Fraction(three-(1 << P), three)
            require(epsilon > Fraction(1, 1 << bits), "negative finite power gap")
            if epsilon < epsilon_minimum:
                epsilon_minimum, epsilon_at = epsilon, a
        for m in range(1, m_bound+1):
            three = 3**m
            S = three.bit_length()
            eta = Fraction((1 << S)-three, 1 << S)
            require(eta > Fraction(1, 1 << bits), "positive finite power gap")
            if eta < eta_minimum:
                eta_minimum, eta_at = eta, m
        next_a = 2*bits+1
        next_m_strict = Fraction(16, 3)*(2*bits+2)
        next_m = (next_m_strict.numerator-1)//next_m_strict.denominator
        stages.append(dict(input_a_max=a_bound, input_m_max=m_bound,
                           strict_gap_bits=bits, epsilon_minimum=str(epsilon_minimum),
                           epsilon_minimum_at=epsilon_at, eta_minimum=str(eta_minimum),
                           eta_minimum_at=eta_at, output_a_max=next_a, output_m_max=next_m))
        a_bound, m_bound = next_a, next_m
    require((a_bound, m_bound) == (15, 85), "final small lengths")
    maximum, maximum_at, pairs = Fraction(), (0, 0), 0
    for a in range(1, a_bound+1):
        three = 3**a
        for P in range(a, three.bit_length()):
            two = 1 << P
            require(two < three, "expanding prefix parameter grid")
            bound = Fraction((1 << (P-a))*three, three-two)
            require(bound < 9510, "uniform endpoint ceiling")
            if bound > maximum:
                maximum, maximum_at = bound, (a, P)
            pairs += 1
    require(pairs == 78 and maximum == Fraction(68024448, 7153) and maximum_at == (12, 19),
            "endpoint maximum")
    state_ceiling = 3*9510*(1 << 7)//2
    require(state_ceiling == 1825920 < LOCAL_LIMIT, "local state ceiling")
    return dict(initial_a_max=55, initial_m_max=298, stages=stages,
                endpoint_parameter_pairs=pairs, endpoint_maximum=str(maximum),
                endpoint_maximum_at=list(maximum_at), strict_endpoint_ceiling=9510,
                strict_state_ceiling=state_ceiling, local_limit_exclusive=LOCAL_LIMIT)


def local_descent() -> dict:
    count, steps, maximum_steps, longest_seed, peak = 0, 0, 0, 0, 1
    for seed in range(3, LOCAL_LIMIT, 2):
        current, used = seed, 0
        while current >= seed:
            require(used < DESCENT_GUARD, f"local descent guard at seed {seed}")
            raw = 3*current+1
            current = raw >> ((raw & -raw).bit_length()-1)
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


def actual_controls() -> dict:
    path = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    rows, arrows = [], 0
    for entry in json.loads(path.read_text())["cycles"]:
        d, states, word = entry["d"], entry["states"], entry["valuations"]
        require(trace(states[0], d, word) == states + [states[0]], "actual fixture arrows")
        C, D = intercept(word), (1 << sum(word))-3**len(word)
        require(D > 0 and Fraction(C, D) == Fraction(states[0], d), "normalized fixture")
        q = D // gcd(C, D)
        require(d % q == 0 and q > 1, "control fails denominator-one hypothesis")
        rows.append(dict(addend=d, length=len(word), reduced_denominator=q,
                         failed_hypothesis="q=1"))
        arrows += len(word)
    require(len(rows) == 11 and {r["addend"] for r in rows} == {5, 7, 13, 61},
            "complete shared control set")
    return dict(fixture_sha256=digest(path), cycles=rows, count=len(rows), arrows=arrows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    receipt = dict(schema="expanding-negative-prefix-v1", constants=constants(),
                   polynomial=polynomial_identity(), intercepts=intercept_grid(),
                   negative_prefixes=negative_prefix_controls(),
                   fractional_gaps=fractional_gap_bootstrap(), finite_powers=finite_power_bootstrap(),
                   local_descent=local_descent(),
                   positive_controls=actual_controls())
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    target = HERE / "check_all_endpoints.json"
    if args.write_receipt:
        target.write_text(encoded)
    else:
        require(target.read_text() == encoded, "receipt differs; inspect before regenerating")
    print(f"PASS all endpoints: {receipt['intercepts']['words']} intercepts; "
          f"{receipt['negative_prefixes']['modified_positive_trajectories']} exact prefixes; "
          f"{receipt['fractional_gaps']['checked_exponents']} gap intervals; "
          f"{receipt['local_descent']['odd_seeds']} local seeds; eleven actual cycles")


if __name__ == "__main__":
    main()
