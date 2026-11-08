#!/usr/bin/env python3
"""Finite closure certificate for all gap-fourteen transposition cancellations."""
from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "check_classification.json"
K = 14
D = (1 << K)-1


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def step(x, d=D):
    require(x % 2 == 1, ("even state", x))
    numerator = 3*x+d
    require(numerator != 0, ("zero numerator", x))
    magnitude = abs(numerator)
    valuation = (magnitude & -magnitude).bit_length()-1
    require(valuation >= 1, ("nonpositive valuation", x))
    y = numerator // (1 << valuation)
    require(y % 2 == 1 and (1 << valuation)*y == numerator,
            ("inexact arrow", x))
    return y, valuation


def intercept(word):
    c = total = 0
    for a in word:
        c = 3*c+(1 << total)
        total += a
    return c


def finite_basin(seeds):
    states = set()
    for seed in sorted(seeds):
        x = seed
        while x not in states:
            require(len(states) < 100000, "basin resource guard")
            require(x > 0, ("positive basin lost sign", x))
            states.add(x)
            x, _ = step(x)
    require(set(seeds) <= states, "crossing seed omitted")
    rows = []
    for x in sorted(states):
        y, valuation = step(x)
        require(y in states, ("basin not forward closed", x, y))
        rows.append([x, valuation, y])
    return rows


def finite_signed_orbit(start):
    indices = {}
    path = []
    x = start
    while x not in indices:
        require(len(path) < 100000, "signed orbit resource guard")
        indices[x] = len(path)
        y, valuation = step(x)
        path.append([x, valuation, y])
        x = y
    repeat_index = indices[x]
    require(all(row[2] == path[i+1][0] for i, row in enumerate(path[:-1])),
            "disconnected signed path")
    require(path[-1][2] == path[repeat_index][0], "cycle does not close")
    require(len({row[0] for row in path}) == len(path), "premature repetition")
    return path, repeat_index


def compute():
    crossings = []
    for magnitude in range(1, D, 2):
        if 3*magnitude < D:
            y, valuation = step(-magnitude)
            require(y > 0 and valuation < K, "incorrect crossing")
            crossings.append([-magnitude, valuation, y])
    seeds = sorted({row[2] for row in crossings})
    basin = finite_basin(seeds)
    high = [row for row in basin if row[1] >= K+2]
    require(high == [[453291, 16, 21]], "unexpected candidate last arrows")
    candidates = []
    for source, c, endpoint in high:
        for r in range(1, c-K):
            # With r=1 there are only the two transposed outside letters.
            if r == 1 and (c-K) % 2:
                continue
            start = -(3**r)*endpoint
            path, repeat_index = finite_signed_orbit(start)
            hits = [i for i, row in enumerate(path) if row[0] == source]
            require(all(i < repeat_index for i in hits),
                    "a terminal source recurs periodically; classification must expand")
            candidates.append({"source": source, "last_valuation": c,
                               "endpoint": endpoint, "r": r, "start": start,
                               "signed_path": path, "repeat_index": repeat_index,
                               "hits": hits})
    require(len(candidates) == 1, "unexpected feasible parameter triples")
    candidate = candidates[0]
    require((candidate["r"], candidate["start"], candidate["hits"])
            == (1, -63, [187]), "unexpected signed hit")
    path = candidate["signed_path"]
    word = tuple(row[1] for row in path[:187])
    u = (1,)+word+(15,)
    v = (15,)+word+(1,)
    n, total = len(u), sum(u)
    plus = (1 << total)+3**n
    minus = (1 << total)-3**n
    cuv = intercept(u+v)
    f = intercept(word+(16,))
    require(D*f == 21*plus, "signed endpoint intercept identity")
    require(cuv % plus == 0, "constructed word does not cancel plus factor")
    require(minus > 0 and gcd(cuv, plus*minus) == plus, "wrong total cancellation")
    require((n, total, len(word), sum(word), gcd(n, total)) == (189, 336, 187, 320, 21),
            "wrong word parameters")
    require((1 << (2*total)) > 2*3**(2*n), "classified word is near-critical")
    require((len(seeds), len(basin), len(path), candidate["repeat_index"],
             path[candidate["repeat_index"]][0]) == (1365, 5472, 659, 407, 4155),
            "wrong finite closure sizes")
    controls = []
    for d in (5, 7, 13, 61):
        y, valuation = step(-1, d)
        require(y > 0, ("missing crossing control", d))
        controls.append({"d": d, "arrow": [-1, valuation, y]})
    return {"k": K, "d": D, "row_format": ["source", "valuation", "target"],
            "crossings": crossings, "seeds": seeds, "basin": basin,
            "high_arrows": high, "candidates": candidates,
            "unique_word": {"z": word, "u": u, "v": v, "n": n, "B": total,
                            "gcd_B_n": gcd(n, total), "plus_factor": plus,
                            "minus_factor": minus, "intercept": cuv,
                            "middle_total": sum(word), "near_critical": False},
            "controls": controls}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    result = compute()
    encoded = json.dumps(result, indent=2, sort_keys=True)+"\n"
    if args.write_receipt:
        RECEIPT.write_text(encoded)
    else:
        require(RECEIPT.exists(), "missing receipt")
        require(RECEIPT.read_text() == encoded, "receipt mismatch")
    print(json.dumps({"status": "PASS", "positive_basin_states": len(result["basin"]),
                      "crossing_seeds": len(result["seeds"]),
                      "candidate_last_arrows": len(result["high_arrows"]),
                      "signed_orbit_states": len(result["candidates"][0]["signed_path"]),
                      "unique_word_half_length": result["unique_word"]["n"],
                      "unique_word_half_total": result["unique_word"]["B"],
                      "receipt_bytes": len(encoded.encode())}))


if __name__ == "__main__":
    main()
