#!/usr/bin/env python3
"""Replay the exact two-source normalization and first-departure certificate."""

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import two_source_history as H

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "two_source_history_audit.json"


def odd_step(x):
    assert x > 0 and x % 2 == 1
    y = 3 * x + 1
    exponent = 0
    while y % 2 == 0:
        y //= 2
        exponent += 1
    return y, exponent


def actual_word(x, count):
    states, word = [x], []
    for _ in range(count):
        x, exponent = odd_step(x)
        word.append(exponent)
        states.append(x)
    return states, word


def independent_divergence(current):
    out = Counter()
    for x, coefficient in current.items():
        out[x] += coefficient
        out[odd_step(x)[0]] -= coefficient
    return {x: c for x, c in out.items() if c}


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def reject(call):
    try:
        call()
    except ValueError:
        return
    raise AssertionError("invalid or capped request was accepted")


def run():
    # Independent Fraction implementation, including the complete repeated edge.
    value = Fraction(53, H.D)
    seen, states, word, costs = {}, [], [], [0]
    while value not in seen:
        seen[value] = len(states)
        states.append(value)
        raw = 3 * value + 1
        exponent = 0
        numerator = raw.numerator
        while numerator % 2 == 0:
            numerator //= 2
            exponent += 1
        value = Fraction(numerator, raw.denominator)
        word.append(exponent)
        costs.append(costs[-1] + exponent)
    cycle_start = seen[value]
    cert = H.shadow_certificate()
    assert all(x.denominator == H.D and x > 0 for x in states)
    assert cert["numerators"] == [x.numerator for x in states]
    assert cert["word"] == word and cert["costs"] == costs
    assert cycle_start == cert["cycle_start"] == 71
    assert len(states) == 448 and len(states) - cycle_start == 377
    assert costs[cycle_start] == 146 and costs[-1] - costs[cycle_start] == 739
    assert states[cycle_start].numerator == 7817
    assert max(states) == Fraction(819533, H.D) < 115
    assert all(3**i <= 2**costs[i] for i in range(len(costs)))
    assert 3**377 < 2**739

    initial = []
    for ell in range(64):
        data = H.initial_identity(ell)
        up, uw = actual_word(data["Q"], 18)
        low, lw = actual_word(data["b"], 16)
        assert tuple(uw) == H.UPPER_WORD and tuple(lw) == H.LOWER_WORD
        assert sum(uw) == 26 and sum(lw) == 31
        assert up[-1] == 864 * data["z"] - 257 and low[-1] == data["z"]
        assert independent_divergence(data["current"]) == H.combine(
            (1, {data["Q"]: 1, data["b"]: -1}), (-1, data["residual"]))
        initial.append([ell, data["Q"], data["z"], data["order"]])

    # All cost locations in the preperiod and the first complete cycle.
    departure_rows, short_count, long_count = [], 0, 0
    for n in range(14, 146 + 739 + 1):
        spec = H.shadow_prefix(n)
        extras = [None] if spec["mode"] == "short" else [1, 2, 7]
        for extra in extras:
            for offset in (0, 1):
                data = H.family(n, extra=extra, offset=offset)
                dep = data["departure"]
                actual, aw = actual_word(data["z"], dep["steps"] + 1)
                assert aw[:-1] == dep["word"]
                assert actual[-2] == dep["state"] and actual[-1] == dep["endpoint"]
                assert aw[-1] == dep["actual_exponent"] != dep["next_exponent"]
                assert all(x < data["z"] + 115 < data["Q"] for x in actual[:-1])
                assert dep["endpoint"] < data["Q"]
                assert data["precision"] == n + 1 + (extra or 0)
                assert data["ell_modulus"] == 2**(data["precision"] - 14)
                # The opposite lift at the exact valuation bit invalidates the cell.
                opposite = H.parameters(data["ell"] + data["ell_modulus"] // 2)
                opposite_dep = H.first_departure(opposite["z"])
                if extra is None:
                    assert opposite_dep["order"] != n
                    short_count += 1
                else:
                    assert opposite_dep["order"] == n
                    assert opposite_dep["extra"] != extra
                    long_count += 1
                departure_rows.append([n, dep["mode"], extra, offset, dep["steps"],
                                       dep["cost"], dep["actual_exponent"], data["ell"]])

    # Explicit joint upper/lower cases, including long prefixes and every h.
    joint_rows, stored = [], []
    cases = [(r, h) for r in range(9) for h in range(18, 37)]
    cases += [(r, h) for r in (32, 64, 128) for h in (18, 24, 36)]
    for r, h in cases:
        n = 19 * r + h - 4
        spec = H.shadow_prefix(n)
        data = H.family(n, extra=3 if spec["mode"] == "long" else None)
        assert data["returns"] == r and data["upper_exit_order"] == h
        z = data["z"]
        for step in range(r):
            next_z = H.psi(z)
            path, actual = actual_word(H.upper(z), 12)
            assert tuple(actual) == H.RETURN_WORD
            assert path[-1] == H.upper(next_z)
            assert H.D * next_z - 53 == (H.D * z - 53) * 3**12 // 2**19
            z = next_z
        reject(lambda z=z: H.psi(z))
        dep = data["departure"]
        after, _ = actual_word(dep["state"], 12)
        assert all(x < data["Q"] for x in after)
        # Slope and affine intercept, checked exactly rather than numerically.
        upper_bound = Fraction(3**12, 2**12) * (data["z"] + 116) - 1
        assert upper_bound < data["Q"]
        comparison = H.paired_history(data["ell"], lower_after=12)
        assert comparison["ordinary_clocks"] == [18 + 12 * r, 28 + dep["steps"]]
        assert independent_divergence(comparison["current"]) == H.combine(
            (1, {data["Q"]: 1, data["b"]: -1}), (-1, comparison["residual"]))
        joint_rows.append([r, h, n, dep["steps"], dep["mode"],
                           comparison["ordinary_clocks"], len(comparison["current"])])
        if (r, h) in ((0, 18), (1, 24), (3, 36)):
            stored.append({"ell": data["ell"], "Q": data["Q"], "b": data["b"],
                           "ordinary_clocks": comparison["ordinary_clocks"],
                           "current": sorted(comparison["current"].items()),
                           "residual": sorted(comparison["residual"].items()),
                           "status": "unfinished two-source comparison"})

    # Eventual periodic phase statement, independent of selected integer samples.
    phase_cases = []
    for n in range(147, 147 + 739):
        first = H.shadow_prefix(n)
        second = H.shadow_prefix(n + 739)
        assert second["steps"] == first["steps"] + 377
        assert second["cost"] == first["cost"] + 739
        for key in ("numerator", "next_exponent", "next_numerator", "gap", "mode"):
            assert second[key] == first[key]
        phase_cases.append([n, first["steps"], first["gap"], first["mode"]])
    assert (19 * 739) % 19 == 0
    assert 2**43 - 3**27 == 1170495537221
    base_slack = ((2**31 * H.Z0 - 665034679) * 2**12
                  - 3**15 * (3**12 * (H.Z0 + 116) - 2**12))
    assert base_slack == 551425372148651686473501 > 0

    long_n = next(n for n in range(14, 30) if H.shadow_prefix(n)["mode"] == "long")
    short_n = next(n for n in range(14, 30) if H.shadow_prefix(n)["mode"] == "short")
    bad = [lambda: H.parameters(-1), lambda: H.parameters(True),
           lambda: H.parameters(Fraction(1, 2)), lambda: H.syracuse(0),
           lambda: H.syracuse(4), lambda: H.v2(0), lambda: H.psi(2),
           lambda: H.psi(H.Z0), lambda: H.family(13),
           lambda: H.family(long_n), lambda: H.family(long_n, extra=0),
           lambda: H.family(short_n, extra=1), lambda: H.family(short_n, offset=-1),
           lambda: H.shadow_prefix(1000, max_steps=1),
           lambda: H.path(H.Q0, 18, max_steps=17),
           lambda: H.paired_history(0, returns=1),
           lambda: H.paired_history(0, lower_after=13),
           lambda: H.paired_history(0, max_steps=1),
           lambda: H.first_departure(2)]
    for call in bad:
        reject(call)

    hashes = {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
              for name in ("two_source_history.py", "check_two_source_history.py", "TWO_SOURCE_HISTORY.md")}
    return {"status": "PASS; unfinished comparisons, no terminal supply",
            "source_hashes": hashes, "rational_certificate": cert,
            "initial_cases": len(initial), "initial_digest": digest(initial),
            "departure_cases": len(departure_rows), "short_cases": short_count,
            "long_cases": long_count, "departure_digest": digest(departure_rows),
            "joint_cases": len(joint_rows), "joint_digest": digest(joint_rows),
            "phase_cases": len(phase_cases), "phase_digest": digest(phase_cases),
            "base_slack": base_slack, "stored_comparisons": stored,
            "rejections": len(bad)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    result = run()
    # Normalize tuple rows exactly as JSON will read them back.
    result = json.loads(json.dumps(result))
    if args.write_receipt:
        RECEIPT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    else:
        assert result == json.loads(RECEIPT.read_text()), "stored receipt differs"
    print("PASS: retained two-source history; "
          f"{result['initial_cases']} initial, {result['departure_cases']} departures, "
          f"{result['joint_cases']} joint, {result['phase_cases']} phases, "
          f"{len(result['stored_comparisons'])} unfinished tables, {result['rejections']} rejections")


if __name__ == "__main__":
    main()
