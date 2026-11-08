"""Exact formula/control checks; the README proves the unbounded theorem."""

from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def add(a, b):
    out = dict(a)
    for exponent, value in b.items():
        out[exponent] = out.get(exponent, 0) + value
    return {k: v for k, v in out.items() if v}


def scale(a, k):
    return {e: k * c for e, c in a.items() if k * c}


def mul(a, b):
    out = {}
    for e, c in a.items():
        for f, d in b.items():
            g = tuple(x + y for x, y in zip(e, f))
            out[g] = out.get(g, 0) + c * d
    return {k: v for k, v in out.items() if v}


def polynomial_checks():
    # Independent sparse expansion in two formal variables.
    one, M, h = {(0, 0): 1}, {(1, 0): 1}, {(0, 1): 1}
    delta = add(add(add(mul(M, M), scale(M, -1)), scale(mul(M, h), -6)),
                add(scale(h, -1), scale(mul(h, h), -3)))
    expanded = add(mul(add(M, h), add(add(M, scale(one, -1)), scale(h, -3))),
                   scale(mul(M, h), -4))
    require(delta == expanded, "threshold polynomial")
    rewritten = add(mul(M, add(add(M, scale(h, -6)), scale(one, -1))),
                    scale(mul(h, add(scale(h, 3), one)), -1))
    require(delta == rewritten, "immediate-crossing implication")
    # Now the variables are h,t and M=7h+1+t.
    h, t = {(1, 0): 1}, {(0, 1): 1}
    M = add(add(scale(h, 7), one), t)
    substituted = add(add(add(mul(M, M), scale(M, -1)), scale(mul(M, h), -6)),
                      add(scale(h, -1), scale(mul(h, h), -3)))
    expected = add(add(scale(mul(h, h), 4), mul(add(scale(h, 8), one), t)), mul(t, t))
    require(substituted == expected, "linear threshold polynomial")
    one, M, h, x = {(0, 0, 0): 1}, {(1, 0, 0): 1}, {(0, 1, 0): 1}, {(0, 0, 1): 1}
    left = add(mul(add(mul(M, x), h), add(add(M, scale(one, -1)), scale(h, -3))),
               scale(mul(mul(M, h), add(scale(x, 3), one)), -1))
    right = add(mul(mul(x, M), add(add(M, scale(one, -1)), scale(h, -6))),
                scale(mul(h, add(one, scale(h, 3))), -1))
    require(left == right, "state-dependent necessary inequality")
    return dict(identities=4, method="exact sparse polynomial coefficient equality")


def step(x, d):
    require(x % 2 == 1 and x != 0 and d > 0 and d % 2 == 1, "signed odd domain")
    numerator = 3 * x + d
    require(numerator != 0, "undefined signed step")
    exponent = (abs(numerator) & -abs(numerator)).bit_length() - 1
    return exponent, numerator // (1 << exponent)


def affine(word, x=Fraction(1)):
    for exponent in word:
        x = (3 * x + 1) / (1 << exponent)
    return x


def intercept(word):
    c, total = 0, 0
    for exponent in word:
        c = 3 * c + (1 << total)
        total += exponent
    return c


def comparison_samples():
    starts = arrows = sharper_only = 0
    for level in range(3, 13):
        M = 1 << level
        for h in range(1, min((M - 1) // 3, 31) + 1, 2):
            if M * M - M - 6 * M * h - h - 3 * h * h < 0:
                continue
            sharper_only += M < 7 * h + 1
            a, x = step(-h, M - 1)
            y = Fraction(4, 1 << a)
            kappa = Fraction(4, M - 1 - 3 * h)
            require(x > 0 and y == kappa * x, "first crossing equality")
            require(kappa * (M - 1) > 1, "comparison coefficient")
            for _ in range(16):
                a, x = step(x, M - 1)
                y = (3 * y + 1) / (1 << a)
                require(y <= kappa * x, "positive comparison propagation")
                arrows += 1
            starts += 1
    require(sharper_only > 0, "sharper criterion control missing")
    return dict(levels=[3, 12], odd_h_max=31, quadratic_condition_required=True,
                positive_steps_per_start=16, starts=starts, arrows=arrows,
                cases_outside_simple_threshold=sharper_only,
                scope="formula samples only; no exhaustive segment-join claim")


def join_control(name, J, r, order, h, A, B, condition_expected):
    p = J - r
    M, N = ((1 << J), (1 << r)) if order == "HL" else ((1 << r), (1 << J))
    require(A and B and min(A + B) >= 1, "nonempty positive words")
    require((A[-1] > p and B[-1] > r) if order == "HL" else B[-1] > J, "boundary conditions")
    x = -h
    for exponent in A:
        actual, x = step(x, M - 1)
        require(actual == exponent, "first segment valuation")
    z = x
    for exponent in B:
        actual, x = step(x, N - 1)
        require(actual == exponent, "second segment valuation")
    require(x == h, "signed endpoint")
    if order == "HL":
        u = A[:-1] + (A[-1] - p,) + B[:-1] + (B[-1] - r,)
        v = A + B[:-1] + (B[-1] + J,)
    else:
        u = A[:-1] + (A[-1] + p,) + B[:-1] + (B[-1] - J,)
        v = A + B[:-1] + (B[-1] + r,)
    require(min(u + v) >= 1, "positive reconstruction")
    n, S = len(u), sum(A) + sum(B)
    P = (1 << S) + 3 ** n
    require(intercept(v) == M * intercept(u) - h * P, "weighted intercept identity")
    c, b = Fraction(3 ** len(B), 1 << sum(B)), Fraction(intercept(B), 1 << sum(B))
    require(h == c * z + (N - 1) * b, "auxiliary second segment")
    require(affine(u) == M * c * affine(A) + N * b, "both-order reconstruction identity")
    delta = M * M - M - 6 * M * h - h - 3 * h * h
    require((delta >= 0) == condition_expected, "control hypothesis")
    if delta >= 0:
        kappa = Fraction(4, M - 1 - 3 * h)
        require(affine(A) <= kappa * z, "first-segment comparison")
        require(affine(u) < M * kappa * h <= M + h, "strict endpoint bound")
    state_comparison_inputs = []
    if M > 6 * h + 1:
        for test_x in (1, 3, 17):
            kappa_x = Fraction(3 * test_x + 1, M - 1 - 3 * h)
            require(affine(A, Fraction(test_x)) <= kappa_x * z, "state-dependent propagation")
            require(affine(u, Fraction(test_x)) < M * kappa_x * h, "state-dependent strict bound")
            state_comparison_inputs.append(test_x)
    word = u + v
    C, D = intercept(word), (1 << sum(word)) - 3 ** len(word)
    require(D > 0, "positive control denominator")
    require(affine(u, Fraction(C, D)) == M * Fraction(C, D) + h, "canonical closing identity")
    G = gcd(C, D)
    states = [intercept(word[i:] + word[:i]) // G for i in range(len(word))]
    for i, state in enumerate(states):
        require(step(state, D // G) == (word[i], states[(i + 1) % len(word)]), "actual reduced cycle")
    if delta >= 0:
        require(0 < Fraction(C, D) < 1 and D // G > 1, "denominator exclusion")
    return dict(name=name, J=J, r=r, order=order, h=h, M=M, N=N, delta=delta,
                condition_holds=delta >= 0, A=A, B=B, u=u, v=v, interface=z,
                state_comparison_inputs=state_comparison_inputs,
                F_u_one=str(affine(u)), normalized_state=str(Fraction(C, D)),
                reduced_denominator=D // G, actual_minimum=min(states))


def actual_fixtures():
    path = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    records = []
    for f in json.loads(path.read_text())["cycles"]:
        xs, word, d = f["states"], f["valuations"], f["d"]
        require(len(xs) == len(word) and min(xs) == f["minimum"], "fixture shape")
        for i, x in enumerate(xs):
            require(step(x, d) == (word[i], xs[(i + 1) % len(xs)]), "fixture replay")
        require(len(word) % 2 == 1 or len(word) == 2, "fixture class separation")
        records.append(dict(d=d, minimum=min(xs), period=len(word)))
    return dict(sha256=sha256(path.read_bytes()).hexdigest(), replayed=records,
                scope="outside two changed half positions: odd period or half-length one")


def main():
    controls = []
    for t in (0, 1, 3):
        controls.append(join_control("high_low_repeated_cycle", 3, 1, "HL", 1,
                                     (2, 1) + (1, 3) * (t + 1), (4,), True))
        controls.append(join_control("low_high_repeated_cycle", 5, 3, "LH", 1,
                                     (2, 1) + (1, 3) * t + (1,), (6,), True))
    controls.append(join_control("endpoint_three", 5, 4, "HL", 3,
                                 (1, 6, 1, 1, 1, 1, 3, 1, 2, 2), (3, 5), True))
    controls.append(join_control("outside_small_endpoint_region", 3, 2, "HL", 3,
                                 (1, 2, 1, 1, 3), (1, 1, 4), False))
    require(controls[0]["reduced_denominator"] == 361, "3x+361 control")
    require(controls[-1]["reduced_denominator"] == 893, "3x+893 control")
    receipt = dict(polynomials=polynomial_checks(), comparison=comparison_samples(),
                   joins=controls, actual_fixtures=actual_fixtures(),
                   theorem_scope="unbounded Mersenne levels and lengths; mathematical proof in README")
    (HERE / "check_small_endpoint.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(dict(polynomial_identities=4, comparison_starts=receipt["comparison"]["starts"],
                          comparison_arrows=receipt["comparison"]["arrows"],
                          reconstructed_joins=len(controls),
                          actual_fixtures=len(receipt["actual_fixtures"]["replayed"])), sort_keys=True))


if __name__ == "__main__":
    main()
