"""Exact algebra and control replay; no finite census proves the theorem."""

from collections import Counter
from fractions import Fraction as Q
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
    for key, value in b.items():
        out[key] = out.get(key, 0) + value
    return {k: v for k, v in out.items() if v}


def scale(a, c):
    return {k: c * v for k, v in a.items() if c * v}


def mul(a, b):
    out = {}
    for key, value in a.items():
        for other, coefficient in b.items():
            term = tuple(x + y for x, y in zip(key, other))
            out[term] = out.get(term, 0) + value * coefficient
    return {k: v for k, v in out.items() if v}


def variables(n):
    one = {(0,) * n: 1}
    return [one] + [{tuple(int(i == j) for j in range(n)): 1} for i in range(n)]


def symbolic_checks():
    one, M, N, lam, h = variables(4)
    d, e = add(M, scale(one, -1)), add(N, scale(one, -1))
    common = add(mul(h, d), mul(mul(mul(M, lam), h), e))
    coefficient = add(N, scale(M, -1))
    at_low = add(common, scale(mul(mul(coefficient, lam), h), -1))
    at_high = add(common, mul(coefficient, h))
    require(at_low == mul(mul(h, d), add(one, mul(N, lam))), "lower T endpoint identity")
    require(at_high == mul(mul(h, e), add(one, mul(M, lam))), "upper T endpoint identity")
    one, K, R, lam = variables(3)
    difference = add(mul(add(one, mul(K, lam)), add(R, scale(one, -1))),
                     scale(mul(add(one, mul(R, lam)), add(K, scale(one, -1))), -1))
    require(difference == mul(add(R, scale(K, -1)), add(one, lam)), "ordering identity")
    one, M, K, lam, h, X = variables(5)
    base = mul(mul(M, add(K, scale(one, -1))), X)
    left = add(mul(h, add(one, mul(K, lam))), scale(mul(base, add(one, scale(lam, -1))), -1))
    right = add(mul(lam, add(base, mul(K, h))), scale(add(base, scale(h, -1)), -1))
    require(left == right, "slope threshold identity")
    return dict(identities=4, method="exact sparse polynomial coefficients")


def enclosure(M, N, h, lam):
    require(M > 1 and N > 1 and M != N and h > 0 and 0 < lam < 1, "enclosure hypotheses")
    K, R = min(M, N), max(M, N)
    lower = h * (1 + R * lam) / (M * (R - 1) * (1 - lam))
    upper = h * (1 + K * lam) / (M * (K - 1) * (1 - lam))
    threshold = Q(M * (K - 1) - h, M * (K - 1) + K * h)
    return lower, upper, threshold


def abstract_affine_controls():
    signs = Counter()
    cases = lower_bound_checks = 0
    for M in (2, 4, 8, 16):
        for N in (2, 4, 8, 16):
            if M == N:
                continue
            for h in (1, 3, 9):
                for lam in (Q(1, 9), Q(1, 2), Q(8, 9)):
                    for theta in (Q(1, 7), Q(1, 3), Q(1, 2), Q(6, 7)):
                        T = -lam * h + theta * h * (1 + lam)
                        c, a = Q(1, 2), 2 * lam
                        z = T / c
                        b, e = (z + a * h) / (M - 1), (h - T) / (N - 1)
                        require(b > 0 and e > 0, "positive abstract intercepts")
                        x = (M * c * b + N * e - h) / (M * (1 - lam))
                        left = M * (M - 1) * (N - 1) * (1 - lam) * x
                        right = h * (M - 1) + M * lam * h * (N - 1) + (N - M) * T
                        require(left == right, "exact state identity")
                        endpoint_N = h * (1 + N * lam) / (M * (N - 1) * (1 - lam))
                        endpoint_M = h * (1 + M * lam) / (M * (M - 1) * (1 - lam))
                        require(x == (1 - theta) * endpoint_N + theta * endpoint_M, "convex representation")
                        lower, upper, threshold = enclosure(M, N, h, lam)
                        require(lower < x < upper, "all-sign enclosure")
                        if lam <= threshold:
                            require(x < 1, "threshold exclusion")
                        for X in (Q(1, 3), Q(1), Q(7)):
                            if x >= X:
                                K = min(M, N)
                                bound = (M * (K - 1) * X - h) / (M * (K - 1) * X + K * h)
                                require(lam > bound, "state lower-bound consequence")
                                lower_bound_checks += 1
                        signs["negative" if z < 0 else "positive" if z > 0 else "zero"] += 1
                        cases += 1
    require(set(signs) == {"negative", "zero", "positive"}, "interface sign coverage")
    return dict(cases=cases, interface_signs=dict(signs), lower_bound_checks=lower_bound_checks,
                scope="positive rational affine data, not claimed to be signed valuation words",
                M_N_values=[2, 4, 8, 16], h_values=[1, 3, 9],
                slopes=["1/9", "1/2", "8/9"], weights=["1/7", "1/3", "1/2", "6/7"])


def step(x, d):
    require(x % 2 == 1 and x != 0 and d % 2 == 1 and d > 0, "signed odd domain")
    numerator = 3 * x + d
    require(numerator != 0, "undefined signed step")
    exponent = (abs(numerator) & -abs(numerator)).bit_length() - 1
    return exponent, numerator // (1 << exponent)


def intercept(word):
    c, total = 0, 0
    for exponent in word:
        c = 3 * c + (1 << total)
        total += exponent
    return c


def affine(word, x):
    return (3 ** len(word) * x + intercept(word)) / (1 << sum(word))


def word_control(name, J, r, order, h, A, B):
    M, N = ((1 << J), (1 << r)) if order == "HL" else ((1 << r), (1 << J))
    p = J - r
    require(A and B and min(A + B) >= 1, "nonempty words")
    require((A[-1] > p and B[-1] > r) if order == "HL" else B[-1] > J, "boundary conditions")
    state = -h
    for exponent in A:
        actual, state = step(state, M - 1)
        require(actual == exponent, "first segment")
    z = state
    for exponent in B:
        actual, state = step(state, N - 1)
        require(actual == exponent, "second segment")
    require(state == h, "signed endpoint")
    if order == "HL":
        u = A[:-1] + (A[-1] - p,) + B[:-1] + (B[-1] - r,)
        v = A + B[:-1] + (B[-1] + J,)
    else:
        u = A[:-1] + (A[-1] + p,) + B[:-1] + (B[-1] - J,)
        v = A + B[:-1] + (B[-1] + r,)
    require(min(u + v) >= 1, "positive reconstruction")
    n, S = len(u), sum(A) + sum(B)
    lam = Q(3 ** n, 1 << S)
    P = (1 << S) + 3 ** n
    require(intercept(v) == M * intercept(u) - h * P, "weighted intercept identity")
    word = u + v
    C, D = intercept(word), (1 << sum(word)) - 3 ** len(word)
    require(D > 0 and 0 < lam < 1, "positive denominator")
    x = Q(C, D)
    require(affine(u, x) == M * x + h, "canonical closing identity")
    lower, upper, threshold = enclosure(M, N, h, lam)
    require(lower < x < upper <= 1 and lam <= threshold, "word enclosure and exclusion")
    c = Q(3 ** len(B), 1 << sum(B))
    T = c * z
    require(-lam * h < T < h, "interface interval")
    require(M * (M - 1) * (N - 1) * (1 - lam) * x ==
            h * (M - 1) + M * lam * h * (N - 1) + (N - M) * T, "word state identity")
    G = gcd(C, D)
    states = [intercept(word[i:] + word[:i]) // G for i in range(len(word))]
    for i, state in enumerate(states):
        require(step(state, D // G) == (word[i], states[(i + 1) % len(word)]), "reduced actual cycle")
    return dict(name=name, J=J, r=r, order=order, h=h, A=A, B=B, interface=z,
                slope=str(lam), lower=str(lower), state=str(x), upper=str(upper),
                threshold=str(threshold), reduced_denominator=D // G, actual_minimum=min(states))


def actual_fixtures():
    path = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    records = []
    for f in json.loads(path.read_text())["cycles"]:
        xs, word, d = f["states"], f["valuations"], f["d"]
        require(len(xs) == len(word) and min(xs) == f["minimum"], "fixture shape")
        for i, x in enumerate(xs):
            require(step(x, d) == (word[i], xs[(i + 1) % len(xs)]), "actual fixture replay")
        require(len(word) % 2 == 1 or len(word) == 2, "fixture class separation")
        records.append(dict(d=d, minimum=min(xs), period=len(word)))
    return dict(sha256=sha256(path.read_bytes()).hexdigest(), records=records,
                scope="outside two changed half positions: odd period or half-length one")


def main():
    words = []
    previous = {}
    for t in (0, 1, 3):
        controls = [
            word_control("two_four", 3, 1, "HL", 1, (2, 1) + (1, 3) * (t + 1), (4,)),
            word_control("one_five", 3, 2, "HL", 3, (1, 2, 1) + (1, 3) * (t + 1), (1, 1, 4)),
            word_control("low_high", 5, 3, "LH", 1, (2, 1) + (1, 3) * t + (1,), (6,)),
        ]
        for record in controls:
            name = record["name"]
            if name in previous:
                require(Q(record["slope"]) < Q(previous[name]["slope"]), "cycle contraction")
                require(Q(record["upper"]) < Q(previous[name]["upper"]), "upper-bound persistence")
            previous[name] = record
            record["inserted_cycle_count"] = t
            words.append(record)
    words.append(word_control("large_endpoint", 8, 6, "HL", 261,
                              (4, 2, 2, 1, 5, 1, 1, 1, 1, 3, 3, 1, 2, 2, 6, 1, 2, 2, 1, 1, 3),
                              (1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 7)))
    require(words[0]["reduced_denominator"] == 361 and words[1]["reduced_denominator"] == 893,
            "existing inside-class controls")
    receipt = dict(symbolic=symbolic_checks(), affine_controls=abstract_affine_controls(),
                   signed_word_controls=words, actual_fixtures=actual_fixtures(),
                   theorem_scope="Unbounded levels and lengths; no finite census used in the proof")
    (HERE / "check_state_enclosure.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(dict(symbolic_identities=receipt["symbolic"]["identities"],
                          abstract_affine_cases=receipt["affine_controls"]["cases"],
                          interface_signs=receipt["affine_controls"]["interface_signs"],
                          signed_word_controls=len(words), actual_fixtures=len(receipt["actual_fixtures"]["records"])),
                     sort_keys=True))


if __name__ == "__main__":
    main()
