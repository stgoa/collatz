#!/usr/bin/env python3
"""Replay V002's bounded examples with exact standard-library arithmetic.

Default: compare a deterministic receipt without writing anything.
--write-receipt: replace this directory's receipt (or --receipt's destination).
These checks do not prove all-modulus rigidity or any convergence theorem.
"""

import argparse
from collections import Counter, deque
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
DS = (1, 5, 7, 13, 61)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def valuation(n):
    require(isinstance(n, int) and n > 0, "valuation requires a positive integer")
    return (n & -n).bit_length() - 1


def odd_step(n, d=1):
    require(isinstance(d, int) and d > 0 and d % 2 and d % 3,
            "d must be positive odd and coprime to3")
    require(isinstance(n, int) and n > 0 and n % 2, "source must be positive odd")
    if n == 1:
        return 1, None  # Absorbing marker, never a raw valuation.
    numerator = 3 * n + d
    a = valuation(numerator)
    return numerator >> a, a


def trace(n, steps, d=1):
    states, word = [n], []
    for _ in range(steps):
        n, a = odd_step(n, d)
        states.append(n)
        word.append(a)
    return states, word


def partition(size, edges):
    """Connected components of explicitly supplied finite equalities."""
    parent = list(range(size))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for x, y in edges:
        parent[find(x)] = find(y)
    groups = {}
    for x in range(size):
        groups.setdefault(find(x), []).append(x)
    return sorted(groups.values())


def digest(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return sha256(payload).hexdigest()


def check_colors():
    cases, histogram = [], {}
    for d in DS:
        counts = Counter()
        require(odd_step(1, d) == (1, None), "absorber was replaced by a raw arrow")
        for modulus in range(1, 97):
            doubling = [(n % modulus, 2 * n % modulus)
                        for n in range(1, modulus + 1)]
            sources = range(3, 2 * modulus + 2, 2)
            ordinary = doubling + [(n % modulus, (3 * n + d) % modulus)
                                   for n in sources]
            actual = doubling + [(n % modulus, odd_step(n, d)[0] % modulus)
                                 for n in sources]
            got = partition(modulus, actual)
            require(got == partition(modulus, ordinary),
                    f"odd/ordinary quotient mismatch: d={d}, M={modulus}")
            g = gcd(modulus, d)
            orbits = partition(g, [(r, factor * r % g)
                                   for r in range(g) for factor in (2, 3)])
            predicted = sorted([[n for n in range(modulus) if n % g in orbit]
                                for orbit in orbits])
            require(got == predicted, f"color classification mismatch: d={d}, M={modulus}")
            counts[len(got)] += 1
            cases.append({"d": d, "M": modulus, "partition": got})
        histogram[str(d)] = {str(k): value for k, value in sorted(counts.items())}
    raw_at_one_d7 = (3 + 7) >> valuation(3 + 7)
    require(raw_at_one_d7 == 5 and odd_step(1, 7)[0] == 1,
            "d7 must distinguish raw and absorbed maps at1")
    require(odd_step(5, 5)[0] == 5 and odd_step(61, 61)[0] == 61,
            "nonabsorbing fixed-point control failed")
    return {"cases": len(cases), "moduli": [1, 96], "d": list(DS),
            "residue_vertices": 23280, "actual_odd_arrows": 23280,
            "odd_source_range": "3,5,...,2M+1; source1 excluded",
            "partition_sha256": digest(cases), "component_histogram": histogram,
            "absorbed_d7_at1": 1, "raw_d7_at1": raw_at_one_d7}


def check_histories():
    q, p = 11547, 11391
    qs, qw = trace(q, 2)
    ps, pw = trace(p, 14)
    require(qw == [1, 2] and pw == [1] * 6 + [2, 2] + [1] * 4 + [2, 6],
            "R81 exact words failed")
    require(qs[-1] == ps[-1] == 12991 and max(ps) == 369521, "R81 endpoint/peak failed")
    require(2**19 * q - 3**12 * p == 309105, "R81 relation failed")
    cq, cp = 1074429, 1059967
    require(2**19 * cq - 3**12 * cp == 309105 and odd_step(cq)[1] == 3,
            "R81 missing-guard counterexample failed")

    ell, D = 922454, 7153
    z = 471104208005 + 2**14 * 3**16 * ell
    numerator = 2**31 * z - 665034679
    require(numerator % 3**15 == 0, "R93 Q is not integral")
    Q = numerator // 3**15
    require(Q % 3 == 0, "R93 lower origin is not integral")
    n = valuation(D * z - 53)
    require(n == 33, "R93 selected order is wrong")
    upper, upper_word = trace(Q, 30)
    lower, lower_word = trace(Q // 3, 28)
    z1_numerator = 3**12 * z - 53
    require(z1_numerator % 2**19 == 0, "R93 return coordinate is not integral")
    z1 = z1_numerator // 2**19
    require(upper[18] == 864 * z - 257 and lower[16] == z,
            "R93 initial two-source paths failed")
    require(upper_word[:18] == [1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 3, 1, 2],
            "R93 upper source word failed")
    require(lower_word[:16] == [2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 3, 2, 1, 5, 2, 3],
            "R93 lower source word failed")
    require(upper_word[18:] == [1, 1, 1, 1, 3, 1, 4, 1, 2, 1, 1, 2]
            and upper[30] == 864 * z1 - 257, "R93 upper return failed")
    N, E = 53, 0
    for i in range(12):
        a = valuation(3 * N + D)
        require(lower_word[16 + i] == a, "R93 actual lower history left shadow early")
        N = (3 * N + D) >> a
        E += a
    require((N, E, valuation(3 * N + D)) == (7931, 32, 1),
            "R93 last matching shadow state failed")
    require(E < n <= E + valuation(3 * N + D), "R93 departure boundary failed")
    joint_left = 2**E * 3**12 * (D * lower[28] - N)
    joint_right = 3**12 * 2**19 * (D * z1 - 53)
    require(joint_left == joint_right, "R93 joint relation failed")
    require(lower[28] < z + 115 < Q < upper[30], "R93 endpoints cannot be cancelled")
    require(z1 - z == 8876123885813760, "R93 missing coordinate defect changed")
    return {"R81": {"ordinary_clocks": [2, 14], "q": q, "p": p,
                    "endpoint": qs[-1], "peak": max(ps),
                    "unguarded_pair": [cq, cp], "wrong_first_valuation": 3},
            "R93": {"ell": ell, "z": z, "Q": Q, "order": n,
                    "upper_clock": 30, "upper_endpoint": upper[30],
                    "lower_clock": 28, "lower_endpoint": lower[28],
                    "shadow_numerator": N, "shadow_cost": E,
                    "coordinate_defect": z1 - z, "joint_relation": "exact equality",
                    "comparison_status": "unfinished; distinct endpoint atoms retained"}}


def check_ensembles():
    cycle, word = trace(19, 3, 5)
    require(cycle == [19, 31, 49, 19] and word == [1, 1, 3], "d5 cycle failed")
    require(Fraction(27 * 19 + 95, 32) == 19, "d5 affine return failed")
    mergers = []
    for d, sources, endpoint, valuations in [(1, [13, 53], 5, [3, 5]),
                                           (5, [19, 81], 31, [1, 3])]:
        arrows = [odd_step(n, d) for n in sources]
        require(arrows == list(zip([endpoint] * 2, valuations)), "entropy merger failed")
        recovered = [(2**a * y - d) // 3 for y, a in arrows]
        require(recovered == sources, "endpoint plus word did not recover source")
        law = Counter(y for y, _ in arrows)
        require(law == {endpoint: 2}, "uniform law did not merge")
        mergers.append({"d": d, "sources": sources, "endpoint": endpoint,
                        "valuations": valuations, "source_entropy_bits": 1,
                        "endpoint_entropy_bits": 0, "conditional_entropy_bits": 1})
    require(Counter(odd_step(x, 5)[0] for x in cycle[:-1]) == Counter(cycle[:-1]),
            "uniform cycle law was not permuted")
    return {"d5_cycle": cycle, "valuations": word, "mergers": mergers,
            "uniform_cycle_law": "invariant, entropy log2(3); not absorbed"}


def rational_string(q):
    return f"{q.numerator}/{q.denominator}"


def check_geometry():
    path, word = trace(7, 5)
    require(path == [7, 11, 17, 13, 5, 1], "geometry supplied path failed")
    domain = set(path)
    tails = [(7, [], 9, Fraction(4, 27)), (11, [], 29, Fraction(4, 87)),
             (17, [], 45, Fraction(4, 135)), (13, [], 69, Fraction(4, 207)),
             (5, [3], 53, Fraction(19, 53))]
    entries = []
    for y, isolated, first, stated_upper in tails:
        inverse = []
        for a in range(1, 27):
            numerator = 2**a * y - 1
            if numerator % 3 == 0:
                x = numerator // 3
                if x > 1 and x != y and x not in domain:
                    require(odd_step(x) == (y, a), "inverse conductance arrow failed")
                    inverse.append(x)
        ray = [first]
        for _ in range(10):
            ray.append(4 * ray[-1] + 1)
        expected = isolated + ray
        require(inverse[:len(expected)] == expected, "escape-series decomposition failed")
        upper = sum((Fraction(1, x) for x in isolated), Fraction()) + Fraction(4, 3 * first)
        require(upper == stated_upper, "rational tail bound was transcribed incorrectly")
        partial = sum((Fraction(1, x) for x in expected), Fraction())
        require(partial <= upper, "finite inverse-tail sum exceeds stated upper bound")
        entries.append({"vertex": y, "isolated": isolated, "tail_start": first,
                        "upper": rational_string(upper), "checked_tail_terms": len(ray)})
    small = set(range(1, 14, 2))
    adjacency = {x: set() for x in small}
    for x in small - {1}:
        y = odd_step(x)[0]
        if y in small and y != x:
            adjacency[x].add(y)
            adjacency[y].add(x)
    seen, queue = {7}, deque([7])
    while queue:
        for y in adjacency[queue.popleft()]:
            if y not in seen:
                seen.add(y)
                queue.append(y)
    require(seen == {7, 9, 11} and odd_step(11)[0] == 17,
            "height13 escape component failed")
    probability = Fraction(1, 1) / (1 + Fraction(12, 5))
    require(probability == Fraction(5, 17), "forward-edge lower comparison failed")
    require([odd_step(x, 5)[0] for x in [11, 81, 129]] == [19, 31, 49],
            "cycle-control incoming edges failed")
    return {"path": path, "ordinary_word": word, "tail_entries": entries,
            "height13_component_of7": sorted(seen), "height13_voltage_at7": 0,
            "forward_probability_lower": rational_string(probability),
            "path_probability_lower": rational_string(probability**5),
            "infinite_tail_status": "written geometric comparison; finite prefixes checked here"}


def check_transducer():
    state, emitted, rows = (0, 1), [], []
    for bit in [1, 1, 0, 0]:
        total = sum(state) + bit
        output, carry = total % 2, int(total >= 2)
        new_state = (bit, carry)
        rows.append([bit, list(state), total, output, list(new_state)])
        emitted.append(output)
        state = new_state
    require(rows == [[1, [0, 1], 2, 0, [1, 1]], [1, [1, 1], 3, 1, [1, 1]],
                     [0, [1, 1], 2, 0, [0, 1]], [0, [0, 1], 1, 1, [0, 0]]],
            "V14 local trace mismatch")
    value = sum(bit * 2**i for i, bit in enumerate(emitted))
    require(value == 10 == 3 * 3 + 1 and state == (0, 0), "transducer integer output failed")
    shortcut = [3]
    for _ in range(5):
        x = shortcut[-1]
        shortcut.append(x // 2 if x % 2 == 0 else (3 * x + 1) // 2)
    require(shortcut == [3, 5, 8, 4, 2, 1] and trace(3, 2)[0] == [3, 5, 1],
            "V14 clock distinction failed")
    return {"local_trace": rows, "emitted_least_first": emitted, "integer_output": value,
            "local_transitions": 4, "shortcut_arrows": 5, "odd_arrows": 2,
            "parallel_automaton_update_count": "not asserted"}


def report():
    return {"schema": 1, "status": "PASS", "verifier_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
            "scope": "Finite V002 examples only; written all-input arguments remain separate. No convergence claim.",
            "colorings": check_colors(), "histories": check_histories(),
            "ensembles": check_ensembles(), "geometry": check_geometry(),
            "base_conversion": check_transducer()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    parser.add_argument("--receipt", type=Path, default=HERE / "verification.json")
    args = parser.parse_args()
    try:
        actual = report()
        if args.write_receipt:
            args.receipt.write_text(json.dumps(actual, indent=2, sort_keys=True) + "\n")
        else:
            expected = json.loads(args.receipt.read_text())
            require(expected == actual, "receipt mismatch; no receipt was modified")
    except (ValueError, OSError, TypeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: 480 finite coloring partitions and exact V002 history, ensemble, geometry and transducer examples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
