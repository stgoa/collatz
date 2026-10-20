#!/usr/bin/env python3
"""Exact bounded V005 witnesses; no whole-kernel equality from finite prefixes.

Default replay compares the receipt without changing it. The universal claims
are written arguments; these finite checks neither prove them nor the goal.
"""

import argparse
from hashlib import sha256
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(value):
    return sha256(json.dumps(value, sort_keys=True,
                             separators=(",", ":")).encode()).hexdigest()


def shortcut(n, d=1):
    require(n > 0 and d > 0 and d % 2, "positive odd parameter required")
    if n == 1:
        return 1
    return (3 * n + d) // 2 if n % 2 else n // 2


def cylinder(K, r):
    require(K >= 1 and 0 < r < 2**K, "positive cylinder required")
    # Raw parity templates are algebraic data. Their evaluation at r may
    # pass through1; the actual witness below starts above2^K instead.
    x, j, B = r, 0, 0
    for i in range(K):
        if x % 2:
            j += 1
            B = 3 * B + 2**i
            x = (3 * x + 1) // 2
        else:
            x //= 2
    M = 3**j
    require(j > 0 and B % 3 and (M * r + B) % 2**K == 0,
            "cylinder affine data invalid")
    c = (M * r + B) // 2**K
    require(c == x and c > 0 and c % 3, "cylinder endpoint invalid")
    return M, B, c


def reconstruction():
    rows, paths, tuples = [], [], []
    arrows = max_clock = 0
    for K in range(1, 5):
        for r in range(1, 2**K):
            M, B, c = cylinder(K, r)
            choices = {}
            for a in range(1, M):
                if a % 3 == 0:
                    continue
                s = 0
                while (2**s * a - c) % M or 2**s * a <= c:
                    s += 1
                    require(s <= 2 * M + K + 10,
                            "unresolved: reconstruction exponent cap")
                u = (2**s * a - c) // M
                require(0 < u < 2**s, "reconstruction section offset invalid")
                choices[a] = (s, u)
                rows.append([K, r, M, B, c, a, s, u])
                for q in range(4):
                    target = M * q + a
                    start = 2**K * (2**s * q + u) + r
                    n = start
                    require(start > 2**K, "actual witness too small")
                    route = [n]
                    for _ in range(K):
                        require(n > 1, "actual cylinder used absorber exit")
                        n = shortcut(n)
                        route.append(n)
                    require(n == 2**s * target and n > 1,
                            "actual cylinder missed prescribed endpoint")
                    for _ in range(s):
                        require(n > 1 and n % 2 == 0,
                                "halving suffix has invalid endpoint")
                        n = shortcut(n)
                        route.append(n)
                    require(n == target, "reconstruction target missed")
                    arrows += K + s
                    max_clock = max(max_clock, K + s)
                    paths.append([K, r, a, q, route])
            parameters = []
            for t in range(M):
                q_t, a_t = divmod(6 * t + 4, M)
                s, u = choices[a_t]
                A_t, B_t = 6 * 2**s, 2**s * q_t + u
                require(0 < B_t < A_t, "quantitative affine offset invalid")
                parameters.append((A_t, B_t))
            for depth in range(4):
                for offset in range(2**depth):
                    for t in range(M):
                        w, v = divmod(2**depth * t + offset, M)
                        A, Bv = parameters[v]
                        quotient, remainder = divmod(A * w + Bv, 2**depth)
                        require(0 <= w < 2**depth and 0 <= quotient < A,
                                "kernel tuple quotient bound failed")
                        for ell in (0, 1, 3):
                            require(A * 2**depth * ell + A * w + Bv
                                    == 2**depth * (A * ell + quotient) + remainder,
                                    "kernel tuple affine identity failed")
                        tuples.append([K, r, depth, offset, t, quotient, remainder])
    return {"K_range": [1, 4], "q_range": [0, 3],
            "cylinder_residue_choices": len(rows), "actual_paths": len(paths),
            "shortcut_arrows": arrows, "max_shortcut_clock": max_clock,
            "tuple_decompositions": len(tuples), "rows_sha256": digest(rows),
            "paths_sha256": digest(paths), "tuples_sha256": digest(tuples)}


def power2(t):
    return t > 0 and t & (t - 1) == 0


def transition(state, bit):
    require(bit in (0, 1), "binary digit required")
    if isinstance(state, int):
        return state + bit
    return {"H": ("H", "B"), "B": ("C", 2), "C": (1, "B")}[state][bit]


def output(state):
    return int(power2(state)) if isinstance(state, int) else 1


def value(state, n):
    require(n >= 0, "nonnegative index required")
    while n:
        state = transition(state, n & 1)
        n >>= 1
    return output(state)


def graph_control():
    reach, frontier, counts = {"H"}, {"H"}, [1]
    for depth in range(1, 17):
        frontier = {transition(s, b) for s in frontier for b in (0, 1)}
        reach |= frontier
        expected = (2, 4)[depth - 1] if depth < 3 else depth + 3
        require(len(reach) == expected, "reachable label count changed")
        counts.append(len(reach))
    for state in reach:
        require(output(state) == output(transition(state, 0)),
                "leading zero convention failed")
        for n in range(129):
            for bit in (0, 1):
                require(value(state, 2 * n + bit)
                        == value(transition(state, bit), n), "actual section identity failed")
    witnesses = []
    for t in range(1, 17):
        for u in range(t + 1, 17):
            P = 1
            while P <= 2 * max(t, u):
                P *= 2
            n = 2**(P - t) - 1
            require(value(t, n) == 1 and value(u, n) == 0,
                    "G-state distinction witness failed")
            witnesses.append([t, u, n])
    for n in range(1025):
        require(value("H", 2 * n) == value("H", n), "doubling control failed")
        require(value("H", 8 * n + 5) == value("H", 2 * n + 1),
                "positive return control failed")
    require(value("H", 9) == 1 and value("H", 28) == 0,
            "full Collatz guard failure disappeared")
    return {"reachable_label_counts_through_depth16": counts,
            "G_state_distinguishing_witnesses": len(witnesses),
            "witnesses_sha256": digest(witnesses), "identity_indices": 1025,
            "Collatz_failure": {"source": 9, "image": 28, "colors": [1, 0]},
            "scope": "Exact reachable labels and bounded actual sequence evaluations. Entire-state distinctness is proved in section_graph.md."}


def sparse_value(n):
    if n < 1:
        return 0
    exponent = 0
    while n % 6 == 0:
        n //= 6
        exponent += 1
    return int(n == 1 and power2(exponent))


def sparse_control():
    counts, comparisons = [], 0
    for p, coefficient in ((2, 5), (3, 3)):
        for D in range(1, 65):
            deltas = set()
            e = 1
            while e < D:
                for a in range(e + 1, D + 1):
                    deltas.add(6**e // p**a)
                e *= 2
            count = D + 2 + len(deltas)
            require(count <= coefficient * D + 3, "sparse linear upper bound failed")
            counts.append([p, D, count])
        for a in range(1, 8):
            support, e = {}, 1
            while e < a:
                q, r = divmod(6**e, p**a)
                require(r and r not in support, "nonzero sparse cells collided")
                support[r] = q
                e *= 2
            for r in range(1, p**a):
                for n in range(17):
                    expected = int(r in support and n == support[r])
                    require(sparse_value(p**a * n + r) == expected,
                            "sparse cell classification failed")
                    comparisons += 1
    mixed = []
    D, e = 8, 32
    pairs = [(a, b) for a in range(D + 1) for b in range(D - a + 1)]
    for index, (a, b) in enumerate(pairs):
        n = 2**(e - a) * 3**(e - b)
        require(sparse_value(2**a * 3**b * n) == 1, "mixed source witness failed")
        for aa, bb in pairs[index + 1:]:
            require(sparse_value(2**aa * 3**bb * n) == 0,
                    "mixed functions not separated by witness")
            mixed.append([a, b, aa, bb, n])
    require(sparse_value(3) == 0 and sparse_value(6) == 1,
            "sparse example accidentally has doubling invariance")
    return {"pure_base_counts": counts, "cell_evaluations": comparisons,
            "mixed_depth": D, "distinct_mixed_zero_sections": len(pairs),
            "mixed_distinguishing_pairs": len(mixed),
            "mixed_sha256": digest(mixed), "doubling_failure": [3, 6]}


def actual_controls():
    checks = []
    for d in (5, 61):
        color = lambda n: int(n % d == 0)
        for n in range(1, 4 * d + 1):
            require(color(n) == color(shortcut(n, d)), "actual d-color invariant failed")
        n = 3 * d + d
        while n % 2 == 0:
            n //= 2
        require(n == d and d != 1, "nonabsorbing fixed-point control failed")
        require(color(3 * d) == 1 and color(16 * d + 1) == 0,
                "d1 rigidity identity incorrectly transferred")
        checks.append({"d": d, "fixed_odd_cycle": [d], "source_count": 4 * d})
    return checks


def report():
    return {"status": "PASS", "schema": 1,
            "scope": "Bounded arithmetic, actual paths and explicit sequence witnesses; no proof of the full quantitative goal or equality of unknown infinite sections.",
            "verifier_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
            "reconstruction": reconstruction(), "graph_control": graph_control(),
            "sparse_control": sparse_control(), "actual_d_controls": actual_controls()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    receipt = HERE / "verification.json"
    try:
        result = report()
        if args.write_receipt:
            receipt.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        else:
            require(json.loads(receipt.read_text()) == result, "receipt mismatch; unchanged")
    except (ValueError, OSError, TypeError) as error:
        print("FAIL:", error, file=sys.stderr)
        return 1
    print("PASS: V005 reconstruction paths, section controls and sparse witnesses")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
