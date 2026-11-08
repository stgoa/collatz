#!/usr/bin/env python3
"""Exact finite certificate for signed-endpoint residue order depths."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import gcd, lcm
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def factors(n: int) -> dict[int, int]:
    require(n >= 1, "positive factorization input")
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def valuation(n: int, p: int) -> int:
    require(n != 0 and p > 1, "finite valuation input")
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def order(base: int, modulus: int) -> int:
    require(modulus > 1 and gcd(base, modulus) == 1, "unit order input")
    phi = modulus
    for p in factors(modulus):
        phi = phi // p * (p - 1)
    out = phi
    for p in factors(phi):
        while out % p == 0 and pow(base, out // p, modulus) == 1:
            out //= p
    require(pow(base, out, modulus) == 1, "order exponent")
    require(all(pow(base, out // p, modulus) != 1 for p in factors(out)), "order minimality")
    return out


def components(Q: int) -> dict[int, int]:
    require(Q > 1 and gcd(Q, 6) == 1, "modulus scope")
    out: dict[int, int] = {}
    for p, e in factors(Q).items():
        require(order(2, p) % 2 == 1, "order-of-two hypothesis")
        v = valuation(order(3, p), 2)
        out[v] = out.get(v, 1) * p**e
    require(product_values(out.values()) == Q, "full prime-power partition")
    return out


def product_values(values) -> int:
    out = 1
    for value in values:
        out *= value
    return out


def congruence_witness(Q: int, h: int) -> dict | None:
    residual = Q // gcd(Q, h)
    if residual == 1:
        return dict(residual_modulus=1, S=1, n=1)
    depths = {valuation(order(3, p), 2) for p in factors(residual)}
    if len(depths) != 1 or 0 in depths:
        return None
    O = lcm(*(order(3, p**e) for p, e in factors(residual).items()))
    require(O == order(3, residual) and O % 2 == 0, "common lifted order")
    n = O // 2
    L = order(2, residual)
    S = ((n + L - 1) // L) * L
    require(S >= n >= 1, "positive valuation budget")
    require(pow(3, n, residual) == residual - 1, "common half-order gives minus one")
    require(h * (pow(2, S, Q) + pow(3, n, Q)) % Q == 0, "constructed congruence")
    return dict(residual_modulus=residual, S=S, n=n)


def residue_checks() -> dict:
    expected = {7: (3, 6), 23: (11, 11), 31: (5, 30), 73: (9, 12),
                127: (7, 126), 151: (15, 50), 337: (21, 168)}
    prime_rows, lifts = [], []
    for p, pair in expected.items():
        require(factors(p) == {p: 1}, "claimed prime")
        o2, o3 = order(2, p), order(3, p)
        require((o2, o3) == pair, "claimed prime orders")
        v = valuation(o3, 2)
        prime_rows.append(dict(p=p, order_2=o2, order_3=o3, depth=v))
        for e in range(1, 5):
            Q = p**e
            O2, O3 = order(2, Q), order(3, Q)
            require(O2 % o2 == O3 % o3 == 0, "order reduction")
            require(p**(e - 1) % (O2 // o2) == p**(e - 1) % (O3 // o3) == 0,
                    "prime-power order quotient")
            require(O2 % 2 == 1 and valuation(O3, 2) == v, "depth preserved on lifting")
            lifts.append(dict(p=p, e=e, modulus=Q, order_2=O2, order_3=O3, depth=v))

    endpoints = {
        7: [1, 7], 7**2: [1, 7, 7**2], 7**3: [1, 7, 7**2, 7**3],
        23**2: [1, 23, 23**2], 73: [1, 73], 73**2: [1, 73, 73**2],
        337: [1, 337], 511: [1, 7, 73, 511],
        7**2 * 73: [1, 7, 7**2, 73, 7 * 73, 7**2 * 73],
        6223: [1, 7, 49, 127, 6223],
        2097151: [1, 7, 49, 127, 337, 7 * 337, 6223, 2097151],
        32767: [1, 7, 31, 151, 7 * 31, 7 * 151, 31 * 151, 32767],
    }
    tables = []
    for Q, hs in endpoints.items():
        parts = components(Q)
        O2, O3 = order(2, Q), order(3, Q)
        powers2 = [pow(2, S, Q) for S in range(O2)]
        counts = {h: 0 for h in hs}
        depth_counts = {h: {} for h in hs}
        lists = {h: [] for h in hs}
        digests = {h: sha256() for h in hs}
        for n in range(1, O3 + 1):
            target = valuation(n, 2) + 1
            divisor = Q // parts.get(target, 1)
            y = pow(3, n, Q)
            for S, x in enumerate(powers2):
                needed = Q // gcd(Q, x + y)
                for h in hs:
                    if h % needed:
                        continue
                    require(h % divisor == 0, "full-component fixed-length law")
                    counts[h] += 1
                    depth_counts[h][target] = depth_counts[h].get(target, 0) + 1
                    digests[h].update(f"{S},{n}\n".encode())
                    if len(lists[h]) < 128:
                        lists[h].append([S, n])
        rows = []
        for h in hs:
            witness = congruence_witness(Q, h)
            require((counts[h] > 0) == (witness is not None), "congruence-existence equivalence")
            row = dict(h=h, residual_modulus=Q // gcd(Q, h), solutions=counts[h],
                       length_depth_counts=depth_counts[h], sha256=digests[h].hexdigest(),
                       witness=witness)
            if counts[h] <= 128:
                row["all_residue_solutions"] = lists[h]
            rows.append(row)
        tables.append(dict(Q=Q, components=parts, order_2=O2, order_3=O3,
                           S_range=[0, O2 - 1], n_range=[1, O3],
                           residue_pairs=O2 * O3, endpoint_classes=rows))
    require(components(2097151) == {1: 6223, 3: 337}, "J21 full components")
    J15 = next(row for row in tables if row["Q"] == 32767)
    h1 = next(row for row in J15["endpoint_classes"] if row["h"] == 1)
    require((J15["order_2"], J15["order_3"]) == (15, 150), "J15 full periods")
    require(h1["all_residue_solutions"] == [[0, 75]], "J15 exact residue class")
    require((pow(2, 120, 32767) + pow(3, 75, 32767)) % 32767 == 0,
            "J15 positive-budget witness")
    require(3**75 < 2**120, "J15 witness power comparison")
    return dict(prime_orders=prime_rows, prime_power_lifts=lifts, complete_tables=tables,
                residue_pairs=sum(row["residue_pairs"] for row in tables),
                endpoint_pair_checks=sum(row["residue_pairs"] * len(row["endpoint_classes"])
                                         for row in tables),
                J15_example=dict(S=120, n=75))


def step(x: int, d: int) -> tuple[int, int]:
    require(x != 0 and x % 2 == 1 and d > 0 and d % 2 == 1, "signed arrow domain")
    raw = 3 * x + d
    require(raw != 0, "undefined zero numerator")
    a = valuation(raw, 2)
    require(a >= 1, "positive exact valuation")
    return raw // (1 << a), a


def check_path(Q: int, h: int, addends: list[int], word: list[int]) -> dict:
    require(len(addends) == len(word) > 0 and h > 0 and h % 2 == 1, "signed path shape")
    require(all(d % Q == 0 for d in addends), "common additive divisor")
    states = [-h]
    C = S = 0
    for d, expected in zip(addends, word):
        nxt, a = step(states[-1], d)
        require(a == expected, "signed path exact valuation")
        C = 3 * C + d * (1 << S)
        S += a
        states.append(nxt)
    n = len(word)
    require(states[-1] == h, "signed opposite endpoint")
    require(C == h * ((1 << S) + 3**n), "weighted composition identity")
    parts = components(Q)
    divisor = Q // parts.get(valuation(n, 2) + 1, 1)
    require(h % divisor == 0, "actual path depth law")
    return dict(Q=Q, h=h, n=n, S=S, required_divisor=divisor,
                addends=addends, valuations=word, states=states)


def signed_controls() -> list[dict]:
    recipes = [
        (7, 1, [7], [2]), (49, 7, [49], [2]), (343, 49, [343], [2]),
        (529, 529, [5 * 529], [1]), (511, 73, [511], [2]),
        (511, 7, [511, 113953], [1, 14]), (73, 1, [73, 16279], [1, 14]),
        (337, 1, [337, 337, 337, (1 << 26) - 3 * 797], [1, 1, 1, 26]),
    ]
    recipes.append((2097151, 6223,
                    [d * 6223 for d in recipes[-1][2]], recipes[-1][3]))
    # A varying-addend witness for the complementary depth-one component.
    # Only the last addend changes; this is not a constant Mersenne orbit.
    residual = 6223
    n = order(3, residual) // 2
    state, addends, word = -1, [], []
    for _ in range(n - 1):
        state, a = step(state, residual)
        addends.append(residual)
        word.append(a)
    lower = sum(word) + max(1, (3 * abs(state)).bit_length() + 1)
    period = order(2, residual)
    S = ((lower + period - 1) // period) * period
    last = S - sum(word)
    final_addend = (1 << last) - 3 * state
    require(final_addend > 0 and final_addend % residual == 0, "constructed final coefficient")
    recipes.append((2097151, 337, [d * 337 for d in addends + [final_addend]], word + [last]))
    return [check_path(*recipe) for recipe in recipes]


def composition_checks() -> dict:
    count = exact_paths = returns = 0
    options = [(1, 1), (2, 1), (1, 5), (4, 13)]
    for Q in (7, 23, 511, 3577):
        parts = components(Q)
        for length in range(1, 5):
            for entries in product(options, repeat=length):
                S = C = 0
                for a, multiplier in entries:
                    C = 3 * C + Q * multiplier * (1 << S)
                    S += a
                require(C % Q == 0, "common additive weighted intercept")
                for h in sorted({1, 7, 73, Q}):
                    state = Fraction(-h)
                    exact = True
                    for a, multiplier in entries:
                        state = (3 * state + Q * multiplier) / (1 << a)
                        exact = exact and state.denominator == 1 and state.numerator % 2 == 1
                    require(state * (1 << S) == -3**length * h + C, "weighted identity")
                    count += 1
                    if exact:
                        exact_paths += 1
                        if state == h:
                            require(h % (Q // parts.get(valuation(length, 2) + 1, 1)) == 0,
                                    "composed exact return depth")
                            returns += 1
    require(exact_paths > 0 and returns > 0, "nonvacuous composition controls")
    return dict(moduli=[7, 23, 511, 3577], lengths=[1, 4],
                valuation_and_addend_multiplier_options=options,
                compositions=count, exact_odd_paths=exact_paths, exact_opposite_returns=returns)


def intercept(word: list[int]) -> int:
    S = C = 0
    for a in word:
        C = 3 * C + (1 << S)
        S += a
    return C


def normal_forms() -> list[dict]:
    examples = [
        ("HL", 6, 3, 1, [2, 2, 4], [1, 1, 1, 2, 1, 3, 2, 6]),
        ("HL", 3, 1, 1, [2, 1, 1, 3], [4]),
        ("LH", 5, 3, 1, [2, 1, 1], [6]),
    ]
    rows = []
    for direction, J, r, h, A, B in examples:
        first, second = (J, r) if direction == "HL" else (r, J)
        d1, d2 = (1 << first) - 1, (1 << second) - 1
        states, current = [-h], -h
        for d, word in ((d1, A), (d2, B)):
            for expected in word:
                current, a = step(current, d)
                require(a == expected, "normal-form exact arrow")
                states.append(current)
        require(current == h, "normal-form endpoint")
        p = J - r
        if direction == "HL":
            require(A[-1] > p and B[-1] > r, "HL boundary valuations")
            u = A[:-1] + [A[-1] - p] + B[:-1] + [B[-1] - r]
            v = A + B[:-1] + [B[-1] + J]
        else:
            require(B[-1] > J, "LH boundary valuation")
            u = A[:-1] + [A[-1] + p] + B[:-1] + [B[-1] - J]
            v = A + B[:-1] + [B[-1] + r]
        require(min(u + v) > 0, "positive reconstructed word")
        plus = (1 << sum(A + B)) + 3**len(A + B)
        require(intercept(v) == (1 << first) * intercept(u) - h * plus, "normal-form intercept")
        require(intercept(u + v) % plus == 0, "full plus cancellation")
        Q = gcd(d1, d2)
        require(Q == (1 << gcd(J, r)) - 1, "Mersenne common modulus")
        if Q > 1:
            part = components(Q)
            require(h % (Q // part.get(valuation(len(A + B), 2) + 1, 1)) == 0,
                    "normal-form component divisibility")
        rows.append(dict(order=direction, J=J, r=r, h=h, Q=Q, A=A, B=B,
                         states=states, u=u, v=v))
    return rows


def residual_J15() -> dict:
    d = (1 << 15) - 1
    states, word, seen = [], [], {}
    x = -1
    for _ in range(1000):
        if x in seen:
            break
        seen[x] = len(states)
        states.append(x)
        x, a = step(x, d)
        word.append(a)
    else:
        raise RuntimeError("J15 orbit did not close within the declared guard")
    index = seen[x]
    require(1 not in states, "J15 orbit reached one")
    require(index == 75 and len(states) - index == 150 and x == 98303, "J15 closure shape")
    cycle = states[index:]
    require(min(cycle) == 1229 and max(cycle) == 2342315, "J15 cycle extrema")
    require(sum(word[index:]) == 315, "J15 cycle valuation total")
    require(all(z > 0 for z in cycle), "J15 positive cycle")
    return dict(J=15, addend=d, transient_length=index, cycle_length=len(cycle),
                repeated_state=x, cycle_valuation_total=sum(word[index:]),
                cycle_minimum=min(cycle), cycle_maximum=max(cycle), reaches_one=False,
                guard=1000, transient_states=states[:index], cycle_states=cycle,
                valuations=word)


def actual_controls() -> dict:
    source = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    data = json.loads(source.read_text())["cycles"]
    rows, arrows = [], 0
    for cycle in data:
        d, states, word = cycle["d"], cycle["states"], cycle["valuations"]
        require(len(states) == len(word) > 0 and min(states) == cycle["minimum"], "fixture shape")
        for i, (x, a) in enumerate(zip(states, word)):
            require(step(x, d) == (states[(i + 1) % len(states)], a), "actual cycle arrow")
            arrows += 1
        require(states[0] > 0 and states[0] != -states[0], "positive cycle is not an opposite return")
        rows.append(dict(d=d, minimum=min(states), odd_period=len(states)))
    require(len(rows) == 11 and {row["d"] for row in rows} == {5, 7, 13, 61}, "standard controls")
    return dict(fixture_sha256=sha256(source.read_bytes()).hexdigest(), cycles=rows,
                actual_arrows=arrows)


def main() -> None:
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script [--write-receipt]")
    receipt = dict(schema="signed-endpoint-order-depth-v1", residues=residue_checks(),
                   signed_controls=signed_controls(), compositions=composition_checks(),
                   normal_forms=normal_forms(), residual_J15=residual_J15(),
                   actual_controls=actual_controls())
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    target = HERE / "check_order_depth.json"
    if sys.argv[1:]:
        target.write_text(encoded)
    else:
        require(target.read_text() == encoded, "receipt differs; inspect and regenerate")
    print("PASS signed-endpoint order depths: "
          f"{receipt['residues']['residue_pairs']} complete residue pairs; "
          f"{receipt['residues']['endpoint_pair_checks']} endpoint checks; "
          f"{len(receipt['signed_controls'])} genuine signed traces; "
          "J15 orbit closed; 11 actual-cycle controls")


if __name__ == "__main__":
    main()
