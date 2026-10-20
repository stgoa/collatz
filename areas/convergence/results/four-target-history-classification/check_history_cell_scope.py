"""Independent all-ray certificate replay for HISTORY_CELL_SCOPE.md."""

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("history_cell_scope", HERE / "history_cell_scope.py")
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)
RECEIPT = HERE / "history_cell_scope_audit.json"


def order2(x):
    assert x > 0
    a = 0
    while x % 2 == 0:
        x //= 2
        a += 1
    return a


def syracuse(x):
    assert x > 0 and x % 2
    if x == 1:
        return 1
    y = 3 * x + 1
    while y % 2 == 0:
        y //= 2
    return y


def canonical_minimum(x):
    """Independent closed F-strip formula, then one selected halving."""
    assert x > 0 and x % 2
    k = (order2(3 * x + 1) - 1) // 2
    r = ((3 * x + 1) // 4**k - 1) // 3
    assert r % 8 != 5
    if r % 4 == 3:
        a = order2(r + 1)
        t = (r + 1) // 2**a
        if (t - 3**a) % 4 == 0:
            r = (r - 1) // 2
    return r


def step(x):
    assert canonical_minimum(x) == x
    return canonical_minimum(syracuse(x))


def bases_from_fibres(y):
    """Derive the two bases from F^k(y), F^k(2y+1), independently."""
    rays = []
    for scale, shift in ((1, 0), (2, 1)):
        b = scale * y + shift
        k = (1 - b) % 3
        f = 4**k * b + (4**k - 1) // 3
        A = 4**(k + 1) * scale
        B = 4**(k + 1) * shift + 4 * (4**k - 1) // 3 - 1
        assert (4 * f - 1) % 3 == 0
        rays.append(((4 * f - 1) // 3, A, B))
    rays.sort()
    out = []
    if y % 3 == 2:
        out.append(("point", 2, -1))
    out += [("ray" + str(j), A, B) for j, (_, A, B) in enumerate(rays)]
    return out


def independent_tree(a):
    D = 19 + a
    anchor = 3**a * (385940463 + 1) // 2**a - 1
    period = 64 * 3**19 * 3**a // 2**a
    stack, nodes, hits = [(anchor, period, [])], [], []
    while stack:
        assert len(nodes) < 100000, "independent enumeration capped"
        x, xp, word = stack.pop()
        depth = len(word)
        assert x > 1 and canonical_minimum(x) == x
        row = {"x": x, "period": xp, "depth": depth,
               "word": word, "first_excluded": []}
        if x <= 133704987:
            hits.append({"origin": x, "period": xp, "depth": depth, "word": word})
        if depth < D:
            remaining = D - depth - 1
            bound = (133704987 + 1) * 3**remaining // 2**remaining - 1
            for kind, A, B in bases_from_fibres(x):
                assert Fraction(A - B, 3) >= 1
                assert (A * x + B) % 3 == 0 and A * xp % 3 == 0
                child, increment = (A * x + B) // 3, A * xp // 3
                index = 0
                while child <= bound:
                    assert child > 1 and canonical_minimum(child) == child
                    assert step(child) == x
                    stack.append((child, increment, word + [[kind, index]]))
                    if kind == "point":
                        break
                    child, increment = 64 * child + 49, 64 * increment
                    index += 1
                if child > bound:
                    row["first_excluded"].append([kind, index, child, bound])
        nodes.append(row)
    nodes.sort(key=lambda row: (row["depth"], row["x"], row["word"]))
    hits.sort(key=lambda row: (row["depth"], row["origin"], row["word"]))
    return {"a": a, "horizon": D, "anchor": anchor, "period": period,
            "states": len(nodes), "nodes": nodes, "hits": hits}


def independent_prefix(x, length):
    states = [x]
    for _ in range(length):
        states.append(syracuse(states[-1]))
    return states


def rows(counter):
    return [[x, c] for x, c in sorted(counter.items()) if c and x != 1]


def independent_current(upper, lower):
    c = Counter(upper[:-1])
    c.subtract(lower[:-1])
    return rows(c)


def check_current(data):
    Q, n = data["parameters"]["Q"], data["parameters"]["n"]
    up, low = independent_prefix(Q, 23), independent_prefix(n, 5)
    assert up[-1] == low[-1]
    assert data["upper_states"] == up and data["lower_states"] == low
    current = independent_current(up, low)
    assert current == rows(data["current"])
    boundary = Counter()
    for x, c in current:
        boundary[x] += c
        boundary[syracuse(x)] -= c
    assert rows(boundary) == [[Q, 1], [n, -1]]
    quotient = [Q]
    for _ in range(18):
        quotient.append(step(quotient[-1]))
    assert quotient == data["quotient_states"] and quotient[-1] == n
    return {"m": data["parameters"]["m"], "upper_states": up,
            "lower_states": low, "quotient_states": quotient,
            "normalizer": rows(data["normalizer"]), "current": current}


def rejection_controls():
    cases = [
        ("negative parameter", lambda: C.parameters(-1)),
        ("fractional parameter", lambda: C.parameters(Fraction(1, 2))),
        ("boolean parameter", lambda: C.parameters(True)),
        ("negative target", lambda: C.parameters(0, -1)),
        ("target outside theorem", lambda: C.parameters(0, 4)),
        ("fractional target", lambda: C.parameters(0, 1.0)),
        ("zero valuation", lambda: C.v2(0)),
        ("even state", lambda: C.S(2)),
        ("zero state", lambda: C.nu(0)),
        ("noncanonical source", lambda: C.T(5)),
        ("absorbed inverse target", lambda: C.inverse_step(1, "ray0")),
        ("illegal point", lambda: C.inverse_step(C.N0, "point")),
        ("negative ray", lambda: C.inverse_step(C.N0, "ray0", -1)),
        ("nonzero point index", lambda: C.inverse_step(17, "point", 1)),
        ("zero node cap", lambda: C.anchor_tree(0, 0)),
        ("incomplete capped tree", lambda: C.anchor_tree(0, 1)),
        ("incomplete capped query", lambda: C.query(0, 0, 1)),
        ("unfixed valuation bit", lambda: C.affine_successor(C.Q0, 2)),
        ("unfixed F bit", lambda: C.affine_normal(9, 2)),
        ("unfixed selection bit", lambda: C.affine_normal(15, 8)),
    ]
    passed = []
    for label, operation in cases:
        try:
            operation()
        except (ValueError, RuntimeError):
            passed.append(label)
        else:
            raise AssertionError("bad input not rejected: " + label)
    return passed


def audit():
    assert not sys.flags.optimize, "run without optimization flags"
    limit = Fraction(C.QP * (C.N0 + 1), C.NP)
    assert limit == C.Q0 + 2 + Fraction(1226171, 387420489)
    assert C.Q0 + 1 < limit < C.Q0 + 3
    assert C.QP * (C.N0 + 1) - C.NP * (C.Q0 + 1) > 0
    symbolic = C.affine_paths()
    assert symbolic["valuation_sum"] == 26
    assert C.QP % 2**27 == 0
    # Independent exact linear replay of the full ordinary cylinder.
    base, period = C.Q0, C.QP
    for row, a in zip(symbolic["ordinary_states"][1:], C.WORD):
        assert order2(3 * base + 1) == a
        assert (3 * period) % 2**(a + 1) == 0
        base, period = (3 * base + 1) // 2**a, 3 * period // 2**a
        assert row == [base, period]
    trees = []
    for a, count in enumerate((64, 78, 89, 101)):
        actual, independent = C.anchor_tree(a), independent_tree(a)
        assert actual == independent and actual["states"] == count
        assert len(actual["hits"]) == 1
        hit = actual["hits"][0]
        assert (hit["origin"], hit["period"], hit["depth"]) == (C.Q0, C.QP, 18 + a)
        assert len(hit["word"]) == 18 + a
        assert C.replay_word(actual["anchor"], hit["word"]) == C.Q0
        trees.append(actual)
    # Direct finite cross-checks of the independent canonical implementation.
    canonical_checks = 0
    for x in range(1, 2048, 2):
        assert C.nu(x) == canonical_minimum(x) and C.S(x) == syracuse(x)
        canonical_checks += 1
    lifts, comparisons = [], []
    for m in (0, 1, 2, 7, 26, 3**19, 2**64):
        p = C.parameters(m)
        Q, n, v, raw = (p[key] for key in ("Q", "n", "v", "raw"))
        assert Q == 11547 + 3 * 2**19 * (85 + 16384 * m)
        assert p["b"] % 16 == 9 and v % 64 == 37
        assert v < Q < n and Q - v == 5058166 + 974892480 * m
        assert canonical_minimum(Q) == Q and canonical_minimum(n) == n
        assert canonical_minimum(raw) == n and order2(raw + 1) == 5
        assert C.Q0 + 1 <= C.cutoff(m) < limit
        data = C.comparison(m)
        checked = check_current(data)
        for j, (x0, xp) in enumerate(symbolic["quotient_states"]):
            assert data["quotient_states"][j] == x0 + xp * m
        for j, (x0, xp) in enumerate(symbolic["ordinary_states"]):
            assert data["upper_states"][j] == x0 + xp * m
        if m in (0, 1, 2**64):
            comparisons.append(checked)
        target = n
        for a in range(4):
            info = C.parameters(m, a)
            assert target == info["target"] == info["anchor"] + info["period"] * m
            assert canonical_minimum(target) == target
            assert info["period"] % 3**(19 + a) == 0
            assert info["period"] % 3**(20 + a) != 0
            answer = C.query(m, a)
            assert answer["complete"] and len(answer["origins"]) == 1
            hit = answer["origins"][0]
            assert (hit["origin"], hit["depth"]) == (Q, 18 + a)
            lifts.append([m, a, Q, target])
            if a < 3:
                assert order2(3 * target + 1) == 1 and step(target) == syracuse(target)
                target = syracuse(target)
    rejected = rejection_controls()
    files = [HERE / "HISTORY_CELL_SCOPE.md", HERE / "history_cell_scope.py",
             Path(__file__).resolve(),
             HERE.parent / "bridge_normal_form/BRIDGE_NORMAL_FORM.md",
             HERE.parent / "history_frontier/HISTORY_FRONTIER.md",
             HERE.parent / "w9_history_repair/W9_HISTORY_REPAIR.md"]
    hashes = {str(path.relative_to(HERE.parent)): hashlib.sha256(path.read_bytes()).hexdigest()
              for path in files}
    return {"status": "PASS", "scope": "Whole m>=0 cell; four targets through 19+a, and one fixed word at any depth. No terminal supply.",
            "source_parameters": {"Q0": C.Q0, "QP": C.QP, "N0": C.N0, "NP": C.NP},
            "cutoff_limit": [limit.numerator, limit.denominator],
            "symbolic_paths": symbolic, "trees": trees, "lifts": lifts,
            "full_comparisons": comparisons, "canonical_checks": canonical_checks,
            "rejection_controls": rejected, "node_cap": 100000,
            "source_hashes": hashes}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    data = audit()
    if args.write_receipt:
        RECEIPT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    else:
        assert data == json.loads(RECEIPT.read_text()), "history-cell receipt mismatch"
    print("PASS: complete history-cell scope; trees=" + str([t["states"] for t in data["trees"]])
          + ", lifts=" + str(len(data["lifts"])) + ", full currents="
          + str(len(data["full_comparisons"])) + ", rejections="
          + str(len(data["rejection_controls"])))


if __name__ == "__main__":
    main()
