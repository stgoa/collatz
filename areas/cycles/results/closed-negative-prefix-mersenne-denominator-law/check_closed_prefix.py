#!/usr/bin/env python3
"""Exact finite closure for the closed-negative-prefix denominator law."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CUTOFF = 1 << 15
LOCAL_LIMIT = 1 << 23
STATE_FACTOR = 82443
ENDPOINT_LIMIT = 91
DESCENT_GUARD = 10000


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def v2(value: int) -> int:
    require(value != 0, "valuation of zero")
    value = abs(value)
    return (value & -value).bit_length() - 1


def intercept(word: list[int]) -> int:
    total, power = 0, 1
    for letter in word:
        require(letter >= 1, "nonpositive valuation")
        total = 3 * total + power
        power <<= letter
    return total


def trace(start: int, addend: int, word: list[int]) -> list[int]:
    states = [start]
    for letter in word:
        require(states[-1] != 0 and states[-1] % 2 == 1, "nonodd signed cut")
        raw = 3 * states[-1] + addend
        require(raw != 0 and v2(raw) == letter, "incorrect exact arrow")
        states.append(raw // (1 << letter))
    require(states[-1] != 0 and states[-1] % 2 == 1, "nonodd endpoint")
    return states


def polynomial_identity() -> dict:
    # Integer polynomial ring in N,R,U,V,W; R=3^a,U=2^P,V=3^b,W=2^T.
    zero = (0,) * 5

    def const(n: int) -> dict:
        return {zero: n} if n else {}

    def var(i: int) -> dict:
        exponents = [0] * 5
        exponents[i] = 1
        return {tuple(exponents): 1}

    def add(*values: dict) -> dict:
        out = {}
        for value in values:
            for term, coefficient in value.items():
                out[term] = out.get(term, 0) + coefficient
        return {term: coefficient for term, coefficient in out.items() if coefficient}

    def scale(n: int, value: dict) -> dict:
        return {term: n * coefficient for term, coefficient in value.items() if n * coefficient}

    def mul(left: dict, right: dict) -> dict:
        out = {}
        for x, cx in left.items():
            for y, cy in right.items():
                term = tuple(a + b for a, b in zip(x, y))
                out[term] = out.get(term, 0) + cx * cy
        return {term: coefficient for term, coefficient in out.items() if coefficient}

    N, R, U, V, W = [var(i) for i in range(5)]
    D = add(mul(U, W), scale(-1, mul(R, V)))
    F = add(mul(add(scale(2, N), const(-1)), R),
            scale(-1, mul(add(N, const(-2)), U)))
    numerator = add(scale(2, mul(mul(add(N, const(-1)), R), V)),
                    mul(U, W), scale(-1, mul(mul(add(N, const(-2)), U), V)))
    difference = add(numerator, scale(-1, D), scale(-1, mul(V, F)))
    require(not difference, "symbolic residual-denominator identity")
    require(9 > 8 and 10000 < 128 * 81, "logarithmic rational comparisons")
    value = Fraction(3 * CUTOFF, 10) - 174 - 341 * 15
    require(value == Fraction(22707, 5) > 7, "large-length cutoff")
    require(Fraction(3, 10) > Fraction(682, CUTOFF), "positive cutoff derivative")
    require((ENDPOINT_LIMIT * (1 << 174) * CUTOFF**341)**10 < 1 << (3 * CUTOFF),
            "cleared cutoff including endpoint factor")
    return dict(variables=["N", "3^a", "2^P", "3^b", "2^T"],
                residual_polynomial_terms=len(difference),
                logarithmic_comparisons={"9>8": True, "10000<128*81": True},
                cutoff=CUTOFF, cutoff_value=str(value),
                derivative_lower_bound=str(Fraction(3, 10) - Fraction(682, CUTOFF)),
                endpoint_cutoff_comparison=True)


def negative_prefix_checks() -> tuple[dict, list[tuple[int, list[int]]]]:
    cycles = [(1, [1]), (5, [1, 2]), (17, [1, 1, 1, 2, 1, 1, 4])]
    records, cases, boundary_checks = [], [], 0
    for origin, word in cycles:
        states = trace(-origin, 1, word)
        require(states[-1] == -origin and max(states) < 0, "negative cycle closure")
        require(len(set(states[:-1])) == len(word), "negative cycle primitivity")
        records.append(dict(states=states[:-1], valuations=word))
        for cut, state in enumerate(states[:-1]):
            rotated = word[cut:] + word[:cut]
            h = -state
            require(h % 3 != 0, "closed negative endpoint divisible by3")
            for repetitions in [1, 2, 4]:
                A = rotated * repetitions
                a, P = len(A), sum(A)
                require(trace(-h, 1, A)[-1] == -h, "repeated negative prefix")
                require(intercept(A) == h * (3**a - (1 << P)) > 0,
                        "closed negative intercept identity")
                cases.append((h, A))
                for J in [3, 5, 15]:
                    for q in [1, 5, 7, 13, 61]:
                        modulus = 3**a
                        Y = (-q * h * pow(1 << (J - 1), -1, modulus)) % modulus
                        if Y % 2 == 0:
                            Y += modulus
                        while True:
                            numerator = (1 << P) * ((1 << (J - 1)) * Y + q * h)
                            require(numerator % modulus == 0, "boundary congruence")
                            start = numerator // modulus - q * h
                            if start > 0:
                                break
                            Y += 2 * modulus
                        modified = A[:-1] + [A[-1] + J - 1]
                        require(trace(start, q, modified)[-1] == Y, "genuine modified prefix")
                        require(v2(start + q * h) == P, "exact shifted-prefix valuation")
                        boundary_checks += 1
    origins = sorted({h for h, _ in cases})
    require(origins == [1, 5, 7, 17, 25, 37, 41, 55, 61, 91], "negative origins")
    return dict(cycles=records, origins=origins, repeated_rotated_prefixes=len(cases),
                genuine_modified_prefix_checks=boundary_checks), cases


def affine_checks(cases: list[tuple[int, list[int]]]) -> dict:
    count = 0
    for h, A in cases:
        a, P = len(A), sum(A)
        sigma = Fraction(3**a, 1 << P)
        for J in [3, 5, 15]:
            N = 1 << J
            for b in [1, 3, 7]:
                T = b + J
                while (1 << (P + T)) <= 3**(a + b):
                    T += 1
                for extra in [0, 1, 3]:
                    total = T + extra
                    c = Fraction(3**b, 1 << total)
                    lam = sigma * c
                    eta = 1 - lam
                    e = h * (1 + c) / (N - 1)
                    x = (2 * c * h * (sigma - 1) + N * e - h) / (2 * eta)
                    m, S = a + b, P + total
                    D = (1 << S) - 3**m
                    F = (2 * N - 1) * 3**a - (N - 2) * (1 << P)
                    require(0 < F < 2 * N * 3**a, "residual factor sign and size")
                    require(2 * (N - 1) * x / h == 1 + Fraction(3**b * F, D),
                            "canonical affine identity")
                    require(0 < x < h * (1 + 2 * lam) / (2 * eta) < 3 * h / (2 * eta),
                            "strict state enclosure")
                    require(2 * c * (sigma * x + h * (sigma - 1)) + N * e == 2 * x + h,
                            "normal-form affine fixed point")
                    require((x.denominator * h * F) % D == 0, "uncancelled endpoint factor")
                    count += 1
    return dict(cases=count, scope="Abstract second-block affine data, not asserted exact signed valuation words")


def finite_gap_closure() -> dict:
    three, worst_num, worst_den, worst_m, worst_total = 1, 0, 1, 0, 0
    digest = hashlib.sha256()
    for m in range(1, CUTOFF):
        three *= 3
        total = three.bit_length()
        two = 1 << total
        gap = two - three
        require(3 * two < 2 * STATE_FACTOR * gap, f"finite enclosure at half-length{m}")
        require(3 * ENDPOINT_LIMIT * two < 2 * LOCAL_LIMIT * gap,
                f"bounded-endpoint enclosure at half-length{m}")
        numerator, denominator = 3 * two, 2 * gap
        if numerator * worst_den > worst_num * denominator:
            worst_num, worst_den, worst_m, worst_total = numerator, denominator, m, total
        digest.update(f"{m}:{total}\n".encode())
    require(worst_m == 15601, "finite maximum location")
    require((worst_num + worst_den - 1) // worst_den == STATE_FACTOR,
            "finite strict upper integer")
    require(ENDPOINT_LIMIT * STATE_FACTOR == 7502313 < LOCAL_LIMIT, "state ceiling")
    return dict(half_lengths=CUTOFF - 1, minimum_half_length=1,
                maximum_half_length=CUTOFF - 1, state_factor=STATE_FACTOR,
                endpoint_limit=ENDPOINT_LIMIT, state_ceiling=ENDPOINT_LIMIT * STATE_FACTOR,
                worst_half_length=worst_m, worst_minimum_total=worst_total,
                worst_unit_endpoint_bound_floor=worst_num // worst_den,
                worst_endpoint_bound_floor=ENDPOINT_LIMIT * worst_num // worst_den,
                parameter_sha256=digest.hexdigest())


def local_descent() -> dict:
    count, steps, maximum_steps, longest_seed, peak = 0, 0, 0, 0, 1
    for seed in range(3, LOCAL_LIMIT, 2):
        current, used = seed, 0
        while current >= seed:
            require(used < DESCENT_GUARD, f"local descent guard at seed{seed}")
            raw = 3 * current + 1
            current = raw >> ((raw & -raw).bit_length() - 1)
            require(current > 0 and current % 2 == 1, "positive odd local cut")
            peak = max(peak, current)
            used += 1
        count += 1
        steps += used
        if used > maximum_steps:
            maximum_steps, longest_seed = used, seed
    require(count == LOCAL_LIMIT // 2 - 1, "complete local seed coverage")
    return dict(limit_exclusive=LOCAL_LIMIT, odd_seeds=count, odd_steps=steps,
                maximum_local_steps=maximum_steps, first_longest_seed=longest_seed,
                peak_odd_output=peak, per_seed_guard=DESCENT_GUARD,
                conclusion="Every odd seed3<=s<limit reaches a smaller positive odd seed")


def signed_scope_controls() -> dict:
    immediate = trace(-1, 7, [2])
    require(immediate == [-1, 1] and not 2 > 3, "terminal boundary control")
    A, B = [2, 1, 1], [6]
    low = trace(-1, 7, A)
    high = trace(low[-1], 31, B)
    require(low[-1] == 11 and high[-1] == 1, "r3 genuine join")
    u, v = [2, 1, 3, 1], [2, 1, 1, 9]
    word = u + v
    C, D = intercept(word), (1 << sum(word)) - 3**len(word)
    require(D > 0, "positive outside-scope join")
    q = D // gcd(C, D)
    state = C // gcd(C, D)
    require(trace(state, q, word)[-1] == state, "outside-scope reduced cycle")

    states, valuations, seen = [], [], {}
    current, d = -1, (1 << 15) - 1
    while current not in seen:
        require(len(states) < 1000, "level15 closure guard")
        seen[current] = len(states)
        states.append(current)
        raw = 3 * current + d
        exponent = v2(raw)
        valuations.append(exponent)
        current = raw // (1 << exponent)
    entry = seen[current]
    require(entry == 75 and len(states) - entry == 150 and current == 98303,
            "level15 exact first-repeat closure")
    require(1 not in states, "level15 endpoint unexpectedly reached")
    require((pow(2, 120, d) + pow(3, 75, d)) % d == 0,
            "level15 arithmetic feasibility")
    return dict(immediate_plus7=dict(states=immediate, valuations=[2],
                                    failed_hypothesis="last(B)>J"),
                nonclosed_r3_join=dict(A_states=low, B_states=high, u=u, v=v,
                                      denominator=q, canonical_state=str(Fraction(C, D)),
                                      failed_hypotheses=["r=1", "A closes at-h"]),
                level15=dict(congruence_witness=[120, 75], transient=entry,
                             cycle_length=len(states) - entry, cycle_entry=current,
                             cycle_valuation_total=sum(valuations[entry:]),
                             cycle_minimum=min(states[entry:]), cycle_maximum=max(states[entry:]),
                             endpoint_one_reached=False))


def recognized_closed_prefix(word: list[int]) -> list[dict]:
    if len(word) % 2:
        return []
    m, matches = len(word) // 2, []
    for cut in range(len(word)):
        rotated = word[cut:] + word[:cut]
        u, v = rotated[:m], rotated[m:]
        for a in range(1, m):
            J = u[a - 1] - v[a - 1] + 1
            if J <= 1 or v[-1] - u[-1] != J + 1:
                continue
            if any(u[i] != v[i] for i in range(m) if i not in [a - 1, m - 1]):
                continue
            A, B = v[:a], v[a:-1] + [v[-1] - 1]
            if not B or min(B) < 1 or B[-1] <= J:
                continue
            residual = 3**a - (1 << sum(A))
            if residual <= 0:
                continue
            h = Fraction(intercept(A), residual)
            if h.denominator != 1 or h.numerator % 2 == 0:
                continue
            endpoint = h.numerator
            if ((1 << J) - 1) * intercept(B) != endpoint * ((1 << sum(B)) + 3**len(B)):
                continue
            require(trace(-endpoint, 1, A)[-1] == -endpoint, "recognized prefix closure")
            require(trace(-endpoint, (1 << J) - 1, B)[-1] == endpoint,
                    "recognized opposite endpoint")
            matches.append(dict(cut=cut, J=J, h=endpoint, A=A, B=B))
    return matches


def positive_controls() -> dict:
    fixture = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    raw = fixture.read_bytes()
    controls, arrows, recognized = [], 0, 0
    for item in json.loads(raw)["cycles"]:
        d, states, word = item["d"], item["states"], item["valuations"]
        require(trace(states[0], d, word) == states + [states[0]], "actual fixture arrows")
        require(min(states) == item["minimum"] and len(set(states)) == len(word), "fixture scope")
        C, D = intercept(word), (1 << sum(word)) - 3**len(word)
        require(D > 0 and Fraction(C, D) == Fraction(states[0], d), "normalized fixture state")
        q = D // gcd(C, D)
        require(d % q == 0, "actual denominator divides addend")
        matches = recognized_closed_prefix(word)
        for match in matches:
            rotated = word[match["cut"]:] + word[:match["cut"]]
            m, S, h = len(word) // 2, sum(word) // 2, match["h"]
            halfD = (1 << S) - 3**m
            if min(Fraction(value, d) for value in states) >= 3:
                require((q * h * (1 << S))**10 * (1 << 20) > halfD**10 * (1 << (3 * m)),
                        "denominator law on actual in-scope control")
            require(q > 1, "nontrivial denominator-one fixture")
            require(intercept(rotated) > 0, "positive canonical control")
        recognized += len(matches)
        arrows += len(word)
        controls.append(dict(addend=d, minimum=min(states), length=len(word), denominator=q,
                             normalized_minimum=str(Fraction(min(states), d)),
                             closed_prefix_matches=matches))
    require(len(controls) == 11, "complete standard fixture list")
    return dict(fixture_sha256=hashlib.sha256(raw).hexdigest(), cycles=controls,
                count=len(controls), arrows=arrows, in_scope_rotations=recognized)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    negative, cases = negative_prefix_checks()
    receipt = dict(schema="closed-negative-prefix-v1", symbolic=polynomial_identity(),
                   negative_prefixes=negative, abstract_affine=affine_checks(cases),
                   finite_gap=finite_gap_closure(), local_descent=local_descent(),
                   signed_controls=signed_scope_controls(), positive_controls=positive_controls())
    serialized = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    target = HERE / "check_closed_prefix.json"
    if args.write_receipt:
        target.write_text(serialized)
    else:
        require(target.read_text() == serialized, "receipt differs; inspect before regenerating")
    print(f"PASS closed negative prefixes: {receipt['finite_gap']['half_lengths']} exact gaps; "
          f"{receipt['local_descent']['odd_seeds']} local odd seeds; "
          f"{negative['genuine_modified_prefix_checks']} exact prefix checks; "
          f"{receipt['positive_controls']['count']} actual-cycle controls")


if __name__ == "__main__":
    main()
