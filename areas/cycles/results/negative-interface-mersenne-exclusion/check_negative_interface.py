#!/usr/bin/env python3
"""Exact general-level identities and pinned unit-level finite closure."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import gcd
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PREDECESSOR = HERE.parent / "unit-low-level-mersenne-exclusion"
PINNED = {
    "check_unit_low_level.py": "6f80acf34870842a0c13febd70bf1f6e572b5eb451c4517436f2154d65c436d3",
    "check_unit_low_level.json": "919d6d41b83350c9fe968f10f3ccee0f7d2ba5417a8f6bc44f756ddb37073356",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def valuation(value: int) -> int:
    require(value != 0, "valuation of zero")
    value = abs(value)
    return (value & -value).bit_length() - 1


def intercept(word: list[int]) -> int:
    value, power = 0, 1
    for letter in word:
        require(letter >= 1, "nonpositive valuation")
        value = 3 * value + power
        power <<= letter
    return value


def trace(start: int, addend: int, word: list[int]) -> list[int]:
    states = [start]
    for letter in word:
        require(states[-1] != 0 and states[-1] % 2 == 1, "nonodd signed cut")
        raw = 3 * states[-1] + addend
        require(raw != 0 and valuation(raw) == letter, "incorrect exact valuation")
        states.append(raw // (1 << letter))
    require(states[-1] != 0 and states[-1] % 2 == 1, "nonodd endpoint")
    return states


def symbolic_identities() -> dict:
    # Integer polynomial ring in M,N,h,g,R,U,V,W,C; the endpoint relation
    # is (M-1)C-hR+gU=0, with R=3^a,U=2^P,V=3^b,W=2^T,C=C_A.
    zero = (0,) * 9

    def const(n: int) -> dict:
        return {zero: n} if n else {}

    def var(i: int) -> dict:
        exponents = [0] * 9
        exponents[i] = 1
        return {tuple(exponents): 1}

    def add(*values: dict) -> dict:
        result = {}
        for value in values:
            for term, coefficient in value.items():
                result[term] = result.get(term, 0) + coefficient
        return {term: coefficient for term, coefficient in result.items() if coefficient}

    def scale(n: int, value: dict) -> dict:
        return {term: n * coefficient for term, coefficient in value.items() if n * coefficient}

    def mul(*values: dict) -> dict:
        result = const(1)
        for value in values:
            product = {}
            for x, cx in result.items():
                for y, cy in value.items():
                    term = tuple(a + b for a, b in zip(x, y))
                    product[term] = product.get(term, 0) + cx * cy
            result = {term: coefficient for term, coefficient in product.items() if coefficient}
        return result

    M, N, h, g, R, U, V, W, C = [var(i) for i in range(9)]
    M1, N1 = add(M, const(-1)), add(N, const(-1))
    difference = add(N, scale(-1, M))
    relation = add(mul(M1, C), scale(-1, mul(h, R)), mul(g, U))
    D = add(mul(U, W), scale(-1, mul(R, V)))
    F = add(mul(add(mul(M, N), const(-1)), h, R), scale(-1, mul(difference, g, U)))
    F0 = add(mul(add(N, const(1)), h, R), mul(difference, C))
    factor = add(F, scale(-1, mul(M1, F0)), mul(difference, relation))
    require(not factor, "full factorization modulo endpoint identity")
    numerator = add(mul(M, N1, V, C), mul(h, U, W), mul(N, g, U, V))
    reduced = add(numerator, scale(-1, mul(h, D)), scale(-1, mul(V, F0)),
                  scale(-1, mul(N, V, relation)))
    require(not reduced, "divided canonical identity modulo endpoint relation")
    return dict(variables=["M", "N", "h", "g", "3^a", "2^P", "3^b", "2^T", "C_A"],
                endpoint_relation="(M-1)C_A-h*3^a+g*2^P=0",
                factorization_residual_terms=len(factor), canonical_residual_terms=len(reduced))


def prefix_and_affine_controls() -> dict:
    levels = [1, 2, 3, 4, 5, 8, 13]
    regimes = {key: 0 for key in ["closed_expanding", "expanding_increase",
                                 "expanding_decrease", "contracting_decrease"]}
    examples, by_level = {}, {}
    by_order = {"LH": 0, "HL": 0}
    prefixes = modified = affine = zero_stops = positive_stops = boundary_rejections = 0
    for j1 in levels:
        M, per_level = 1 << j1, 0
        starts = {1, 3, 5, M - 1, M + 1, 2 * M - 1, 3 * M - 1}
        starts.update(M - 1 + 2 * offset for offset in range(-8, 9))
        for h in sorted(value for value in starts if value > 0 and value % 2 == 1):
            state, A = -h, []
            for a in range(1, 9):
                raw = 3 * state + M - 1
                if raw == 0:
                    zero_stops += 1
                    break
                exponent = valuation(raw)
                successor = raw // (1 << exponent)
                if successor > 0:
                    positive_stops += 1
                    break
                A.append(exponent)
                state = successor
                g, P, C = -state, sum(A), intercept(A)
                R, U = 3**a, 1 << P
                require(trace(-h, M - 1, A)[-1] == -g, "genuine negative prefix")
                require((M - 1) * C == h * R - g * U > 0, "general-level endpoint identity")
                if R < U:
                    require(g < h, "contracting negative prefix increases magnitude")
                    kind = "contracting_decrease"
                else:
                    require(R > U, "nonempty unit slope")
                    kind = "closed_expanding" if g == h else (
                        "expanding_increase" if g > h else "expanding_decrease")
                regimes[kind] += 1
                examples.setdefault(f"first_level={j1}:{kind}", dict(first_level=j1, h=h, g=g, word=list(A)))
                prefixes += 1
                per_level += 1
                second_levels = {j1 + 1, j1 + 3, 2 * j1 + 1}
                if j1 > 1:
                    second_levels.update([1, j1 - 1, max(1, j1 // 2)])
                for j2 in sorted(second_levels):
                    N, shift = 1 << j2, j2 - j1
                    order = "LH" if shift > 0 else "HL"
                    if A[-1] + shift <= 0:
                        boundary_rejections += 1
                        continue
                    F = (M * N - 1) * h * R - (N - M) * g * U
                    F0 = (N + 1) * h * R + (N - M) * C
                    require(F == (M - 1) * F0, "general-level full factorization")
                    middle = Fraction(M * N - 1, M - 1) * h * R
                    if M < N:
                        require(0 < F0 < middle < 2 * N * h * R, "LH residual bound")
                    else:
                        require(0 < middle < F0 < (N + 1) * h * R < 2 * N * h * R,
                                "HL residual bound")
                    by_order[order] += 1
                    for q in [1, 5, 7, 13, 61]:
                        changed = A[:-1] + [A[-1] + shift]
                        total = P + shift
                        modulus = 1 << (total + 1)
                        start = (((1 << total) - q * C) * pow(R, -1, modulus)) % modulus
                        require(start > 0 and start % 2 == 1, "positive exact cylinder start")
                        Y = trace(start, q, changed)[-1]
                        binary_exponent = P + min(shift, 0)
                        bracket = ((M - 1) * (1 << max(shift, 0)) * Y
                                   + q * g * (1 << max(-shift, 0)))
                        require(R * ((M - 1) * start + q * h) == (1 << binary_exponent) * bracket,
                                "scaled general-level boundary equation")
                        require(binary_exponent >= a and bracket % 2 == 1,
                                "boundary positivity and odd bracket")
                        require(valuation((M - 1) * start + q * h) == binary_exponent,
                                "exact general-level shifted valuation")
                        modified += 1
                    # Second blocks here are affine data, not claimed valuation words.
                    for b in [1, 3]:
                        T = max(b + j2, (R * 3**b).bit_length() - P)
                        require((1 << (P + T)) > R * 3**b, "positive abstract half gap")
                        c = Fraction(3**b, 1 << T)
                        lam = Fraction(R, U) * c
                        eta = 1 - lam
                        e = Fraction(h, N - 1) + Fraction(c * g, N - 1)
                        x = (M * c * Fraction(C, U) + N * e - h) / (M * eta)
                        D = (1 << (P + T)) - R * 3**b
                        require(M * (N - 1) * D * x == h * D + 3**b * F0,
                                "divided affine identity")
                        low = min(M, N)
                        require(0 < x < h * (1 + low * lam) / (M * (low - 1) * eta),
                                "general-level state enclosure")
                        coefficient = (Fraction(M + 1, M) if M < N else
                                       Fraction((N + 1) * (M - 1), M * (N - 1)))
                        require((M - 1) * x + h < h * coefficient / eta < 4 * h / eta,
                                "uniform shifted state bound")
                        require(x.denominator * F0 % D == 0, "residual divisibility without cancellation")
                        affine += 1
        by_level[str(j1)] = per_level
    require(all(regimes.values()) and all(by_level.values()) and all(by_order.values()),
            "all requested prefix regimes, levels and orders")
    return dict(first_levels=levels, first_lengths=[1, 8], prefixes=prefixes,
                prefixes_by_level=by_level, admissible_first_prefix_cases_by_order=by_order,
                regimes=regimes, examples=examples, exact_modified_positive_prefixes=modified,
                abstract_second_affine_checks=affine, zero_stops=zero_stops,
                positive_crossings_excluded=positive_stops,
                nonpositive_modified_boundary_rejections=boundary_rejections,
                scope="First prefixes and modified positive paths are genuine; abstract second blocks are not asserted signed valuation segments")


def signed_second_and_positive_interface() -> dict:
    B = [1, 6]
    second = trace(-3, 31, B)
    require(second == [-3, 11, 1] and B[-1] > 5, "high-terminal signed second segment")
    c = Fraction(3**len(B), 1 << sum(B))
    budget = Fraction(31, 32) * (Fraction(3, 2)**len(B) - 1)
    require(1 + 3 * c <= budget and 2 < Fraction(3, 2)**len(B), "negative-interface budget")

    A, other_B = [2, 1, 1], [6]
    first = trace(-1, 7, A)
    last = trace(first[-1], 31, other_B)
    require(first == [-1, 1, 5, 11] and last == [11, 1], "positive-interface genuine join")
    require(not 2 < Fraction(3, 2)**len(other_B), "positive-interface endpoint budget must fail")
    u, v = [2, 1, 3, 1], [2, 1, 1, 9]
    word = u + v
    C, D = intercept(word), (1 << sum(word)) - 3**len(word)
    common = gcd(C, D)
    q, start = D // common, C // common
    require(q == 41 and Fraction(C, D) == Fraction(1, 41), "positive-interface normalized state")
    states = trace(start, q, word)
    require(states[-1] == start, "positive-interface actual cycle")
    return dict(negative_second=dict(J=5, compatible_low_levels=[1, 2, 3, 4],
                                     states=second, word=B,
                                     scope="Second segment only, not a full admissible join"),
                positive_interface=dict(r=3, J=5, h=1, interface=11, A=A, B=other_B,
                                        A_states=first, B_states=last, u=u, v=v,
                                        reduced_denominator=q, normalized_state=str(Fraction(C, D)),
                                        actual_cycle=states[:-1],
                                        failed_hypothesis="negative interface"))


def predecessor_replay() -> dict:
    def check_hashes() -> None:
        for name, expected in PINNED.items():
            require(hashlib.sha256((PREDECESSOR / name).read_bytes()).hexdigest() == expected,
                    f"predecessor changed: {name}")

    check_hashes()
    script = PREDECESSOR / "check_unit_low_level.py"
    result = subprocess.run([sys.executable, "-O", str(script)], cwd=ROOT,
                            text=True, capture_output=True, timeout=60, check=False)
    require(result.returncode == 0, f"predecessor replay failed: {result.stdout}\n{result.stderr}")
    check_hashes()
    summary = json.loads(result.stdout)
    require(summary["result"] == "passed" and summary["gap_intervals"] == (1 << 22) - 1
            and summary["finite_minimum_checks"] == 1844
            and summary["local_odd_seeds"] == (1 << 19) - 1
            and summary["standard_cycles"] == 11, "predecessor finite scope")
    receipt = json.loads((PREDECESSOR / "check_unit_low_level.json").read_text())
    require(receipt["local_descent"]["limit_exclusive"] == 1 << 20,
            "predecessor local convergence range")
    return dict(source_and_receipt_sha256=PINNED, optimized_python=True, summary=summary,
                finite_scope=dict(half_length_cutoff=1 << 22, final_half_length_maximum=1844,
                                  local_limit_exclusive=1 << 20,
                                  local_odd_steps=receipt["local_descent"]["odd_steps"]))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    receipt = dict(schema="negative-interface-mersenne-v1", polynomial=symbolic_identities(),
                   general_prefixes=prefix_and_affine_controls(),
                   signed_controls=signed_second_and_positive_interface(),
                   predecessor=predecessor_replay())
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    target = HERE / "check_negative_interface.json"
    if args.write_receipt:
        target.write_text(encoded)
    else:
        require(target.read_text() == encoded, "receipt differs; inspect before regenerating")
    print(json.dumps(dict(result="passed", first_levels=receipt["general_prefixes"]["first_levels"],
                          negative_prefixes=receipt["general_prefixes"]["prefixes"],
                          modified_positive_prefixes=receipt["general_prefixes"]["exact_modified_positive_prefixes"],
                          predecessor_gap_intervals=receipt["predecessor"]["summary"]["gap_intervals"],
                          standard_cycles=11), sort_keys=True))


if __name__ == "__main__":
    main()
