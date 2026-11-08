"""Exact finite controls for the written, unbounded signed-endpoint lemma."""

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import gcd, isqrt, lcm
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def prime(p):
    return p >= 2 and all(p % k for k in range(2, isqrt(p) + 1))


def order(b, modulus):
    require(gcd(b, modulus) == 1, "order requires a unit")
    value = 1
    for exponent in range(1, modulus + 1):
        value = value * b % modulus
        if value == 1:
            return exponent
    raise RuntimeError("unit order not found within modulus")


def valuation(x, p):
    require(x != 0, "finite valuation")
    out = 0
    while x % p == 0:
        x //= p
        out += 1
    return out


def residue_checks():
    prime_rows = []
    for p, expected in ((23, (11, 11)), (601, (25, 75))):
        require(prime(p), "claimed prime")
        o2, o3 = order(2, p), order(3, p)
        require((o2, o3) == expected, "exact prime orders")
        exponent = lcm(o2, o3)
        require(exponent % 2 == 1, "common exponent is odd")
        prime_rows.append(dict(prime=p, order_2=o2, order_3=o3,
                               odd_common_exponent=exponent))
    tables = []
    for modulus in (23, 601, 23 * 601, 23**2):
        o2, o3 = order(2, modulus), order(3, modulus)
        require(o2 % 2 == o3 % 2 == 1, "odd orders for complete table")
        powers2 = [pow(2, s, modulus) for s in range(o2)]
        powers3 = [pow(3, m, modulus) for m in range(o3)]
        require(all(gcd(modulus, x + y) == 1 for x in powers2 for y in powers3),
                "complete residue table contains forbidden sum")
        tables.append(dict(modulus=modulus, order_2=o2, order_3=o3,
                           power_sum_pairs=o2 * o3))
    lifts = []
    for row in prime_rows:
        p, exponent = row["prime"], row["odd_common_exponent"]
        for e in range(1, 5):
            modulus, lifted = p**e, exponent * p**(e - 1)
            require(lifted % 2 == 1 and pow(2, lifted, modulus) == pow(3, lifted, modulus) == 1,
                    "prime-power common exponent")
            for s, m in product(range(33), repeat=2):
                require(gcd(modulus, pow(2, s, modulus) + pow(3, m, modulus)) == 1,
                        "prime-power sum sample")
            lifts.append(dict(prime=p, power=e, modulus=modulus, odd_exponent=lifted,
                              sum_samples=33**2))
    return dict(primes=prime_rows, complete_residue_tables=tables,
                total_complete_pairs=sum(row["power_sum_pairs"] for row in tables),
                prime_power_lifts=lifts, lift_sample_exponents="0<=S,m<=32")


def step(x, d):
    require(x % 2 == 1 and x != 0 and d > 0 and d % 2 == 1, "signed domain")
    numerator = 3 * x + d
    require(numerator != 0, "undefined signed arrow")
    exponent = valuation(numerator, 2)
    require(exponent >= 1, "odd input/addend")
    return numerator // 2**exponent, exponent


def path(start, addends, expected_word):
    require(len(addends) == len(expected_word) > 0, "path lengths")
    states = [start]
    for d, expected in zip(addends, expected_word):
        nxt, exponent = step(states[-1], d)
        require(exponent == expected, "exact path valuation")
        states.append(nxt)
    return states


def signed_controls():
    rows = []
    for modulus in (23, 23**2, 23**3, 601, 601**2, 23 * 601):
        for multipliers, word in (((5,), (1,)), ((5, 13), (1, 4))):
            addends = [modulus * d for d in multipliers]
            states = path(-modulus, addends, word)
            require(states[-1] == modulus, "allowed opposite endpoint control")
            require(all(d % modulus == 0 for d in addends), "common additive modulus")
            rows.append(dict(modulus=modulus, h=modulus, addends=addends,
                             valuations=list(word), states=states))
    failing_hypothesis = []
    for d, exponent in ((5, 1), (7, 2)):
        states = path(-1, [d], [exponent])
        require(states[-1] == 1 and d > 1, "signed crossing control")
        o2, o3 = order(2, d), order(3, d)
        require(o2 % 2 == 0 or o3 % 2 == 0, "odd-order hypothesis must fail")
        failing_hypothesis.append(dict(addend=d, states=states, valuation=exponent,
                                       order_2=o2, order_3=o3))
    return dict(allowed_returns=rows, odd_order_hypothesis_failures=failing_hypothesis)


def composition_checks():
    cases = integral_odd_paths = opposite_returns = 0
    options = tuple(product((1, 2, 3), (5, 13)))
    for modulus in (23, 601):
        for length in range(1, 5):
            for entries in product(options, repeat=length):
                total, intercept = 0, 0
                for exponent, multiplier in entries:
                    intercept = 3 * intercept + modulus * multiplier * 2**total
                    total += exponent
                require(intercept % modulus == 0, "composition common addend")
                for factor in (-5, -3, -1, 1, 3, 5):
                    start = factor * modulus
                    state = Fraction(start)
                    odd_path = True
                    for exponent, multiplier in entries:
                        state = (3 * state + modulus * multiplier) / 2**exponent
                        odd_path = odd_path and state.denominator == 1 and state.numerator % 2 == 1
                    require(state * 2**total == 3**length * start + intercept,
                            "exact weighted composition identity")
                    cases += 1
                    if odd_path:
                        integral_odd_paths += 1
                        if start < 0 and state == -start:
                            require((-start) % modulus == 0, "signed endpoint divisibility")
                            opposite_returns += 1
    require(integral_odd_paths > 0 and opposite_returns > 0, "nonvacuous exact path controls")
    return dict(compositions=cases, integral_odd_paths=integral_odd_paths,
                opposite_returns=opposite_returns, moduli=[23, 601],
                lengths="1..4", letters=[1, 2, 3], addend_multipliers=[5, 13],
                start_multipliers=[-5, -3, -1, 1, 3, 5])


def intercept(word):
    total = out = 0
    for exponent in word:
        out = 3 * out + 2**total
        total += exponent
    return out


def mersenne_checks():
    gcd_cases = prime_tests = 0
    for J in range(2, 81):
        for r in range(1, J):
            common = gcd(2**J - 1, 2**r - 1)
            require(common == 2**gcd(J, r) - 1, "Mersenne gcd identity")
            for p, o2 in ((23, 11), (601, 25)):
                require(valuation(common, p) == min(valuation(2**J - 1, p), valuation(2**r - 1, p)),
                        "common prime-power valuation")
                require((common % p == 0) == (gcd(J, r) % o2 == 0), "order versus common level")
                prime_tests += 1
            gcd_cases += 1
    rows = []
    examples = [
        ("HL", 3, 2, 3, (1, 2, 1, 1, 3), (1, 1, 4)),
        ("HL", 3, 1, 1, (2, 1, 1, 3), (4,)),
        ("LH", 5, 3, 1, (2, 1, 1), (6,)),
    ]
    for order_name, J, r, h, A, B in examples:
        p = J - r
        first, second = (J, r) if order_name == "HL" else (r, J)
        states_A = path(-h, [2**first - 1] * len(A), A)
        states_B = path(states_A[-1], [2**second - 1] * len(B), B)
        require(states_B[-1] == h, "normal-form endpoints")
        if order_name == "HL":
            require(A[-1] > p and B[-1] > r, "HL boundary conditions")
            u = A[:-1] + (A[-1] - p,) + B[:-1] + (B[-1] - r,)
            v = A + B[:-1] + (B[-1] + J,)
        else:
            require(B[-1] > J, "LH boundary condition")
            u = A[:-1] + (A[-1] + p,) + B[:-1] + (B[-1] - J,)
            v = A + B[:-1] + (B[-1] + r,)
        require(min(u + v) >= 1, "positive reconstructed letters")
        plus = 2**sum(A + B) + 3**len(A + B)
        require(intercept(v) == 2**first * intercept(u) - h * plus, "reconstruction intercept")
        require(intercept(u + v) % plus == 0, "full plus cancellation control")
        rows.append(dict(order=order_name, J=J, r=r, h=h, A=list(A), B=list(B),
                         states_A=states_A, states_B=states_B, u=list(u), v=list(v)))
    return dict(gcd_grid="2<=J<=80, 1<=r<J", gcd_cases=gcd_cases,
                prime_valuation_tests=prime_tests, exact_reconstructions=rows)


def actual_controls():
    source = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    data = json.loads(source.read_text())
    rows = []
    for cycle in data["cycles"]:
        d, states, word = cycle["d"], cycle["states"], cycle["valuations"]
        require(len(states) == len(word) > 0 and min(states) > 0, "positive fixture domain")
        for i, (x, exponent) in enumerate(zip(states, word)):
            nxt, exact = step(x, d)
            require((nxt, exact) == (states[(i + 1) % len(states)], exponent), "actual cycle replay")
        require(states[0] != -states[0], "positive closed cycle is not an opposite return")
        rows.append(dict(d=d, minimum=min(states), period=len(states)))
    require(len(rows) == 11, "eleven standard fixtures")
    return dict(fixture_sha256=sha256(source.read_bytes()).hexdigest(), cycles=rows,
                scope="positive closed cycles have equal, not opposite, endpoints")


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script [--write-receipt]")
    receipt = dict(residues=residue_checks(), signed_controls=signed_controls(),
                   compositions=composition_checks(), mersenne=mersenne_checks(),
                   actual_cycles=actual_controls())
    target = HERE / "check_odd_order_endpoints.json"
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if sys.argv[1:]:
        target.write_text(encoded)
    else:
        require(target.read_text() == encoded, "receipt differs; inspect and regenerate")
    print(json.dumps(dict(result="passed", complete_residue_pairs=receipt["residues"]["total_complete_pairs"],
                          exact_compositions=receipt["compositions"]["compositions"],
                          mersenne_gcd_cases=receipt["mersenne"]["gcd_cases"],
                          actual_cycles=len(receipt["actual_cycles"]["cycles"])), sort_keys=True))


if __name__ == "__main__":
    main()
