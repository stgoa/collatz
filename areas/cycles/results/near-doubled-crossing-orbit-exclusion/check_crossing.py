#!/usr/bin/env python3
"""Certify finite crossing basins and exceptional signed orbits for 3x+d.

The finite sets are constructed deterministically, then checked explicitly for
closure. Termination is certified by those finite sets, not inferred from a
trajectory cutoff. A resource guard fails instead of producing partial evidence.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "check_crossing.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def step(x, d):
    require(x % 2 == 1, ("even state", x, d))
    numerator = 3*x+d
    require(numerator != 0, ("zero reached", x, d))
    magnitude = abs(numerator)
    valuation = (magnitude & -magnitude).bit_length()-1
    require(valuation >= 1, ("zero valuation", x, d))
    return numerator // (1 << valuation), valuation


def closed_orbits(seeds, d):
    seen = set()
    for seed in sorted(set(seeds)):
        x = seed
        while x not in seen:
            require(len(seen) < 100000, "orbit construction resource guard")
            seen.add(x)
            x, _ = step(x, d)
    rows = []
    for x in sorted(seen):
        y, valuation = step(x, d)
        require(y in seen, ("set not forward closed", x, d, y))
        require(3*x+d == (1 << valuation)*y and y % 2 == 1,
                ("wrong exact transition", x, d))
        rows.append({"x": x, "valuation": valuation, "next": y})
    require(set(seeds) <= seen, ("missing seeds", d))
    return rows


def compute():
    results = []
    for k in range(3, 13):
        d = (1 << k)-1
        crossings = []
        for magnitude in range(1, d, 2):
            if 3*magnitude >= d:
                continue
            y, valuation = step(-magnitude, d)
            require(y > 0, "crossing output is not positive")
            require(valuation < k, "crossing has unexpectedly large valuation")
            crossings.append({"negative": -magnitude,
                              "valuation": valuation, "positive": y})
        seeds = sorted({row["positive"] for row in crossings})
        basin = closed_orbits(seeds, d)
        require(all(row["x"] > 0 for row in basin), "positive basin lost sign")
        one_letter = []
        transpositions = []
        for row in basin:
            c, endpoint = row["valuation"], row["next"]
            if c >= k+1:
                start = -endpoint
                orbit = closed_orbits([start], d)
                require(row["x"] not in {r["x"] for r in orbit},
                        ("one-letter exceptional endpoint survives", k, row))
                one_letter.append({"last_source": row["x"], "last_valuation": c,
                                   "endpoint": endpoint, "start": start,
                                   "signed_orbit": orbit})
            if c >= k+2:
                for r in range(1, c-k):
                    start = -(3**r)*endpoint
                    orbit = closed_orbits([start], d)
                    require(row["x"] not in {item["x"] for item in orbit},
                            ("transposition exceptional endpoint survives", k, r, row))
                    transpositions.append({"last_source": row["x"],
                                           "last_valuation": c, "endpoint": endpoint,
                                           "r": r, "start": start, "signed_orbit": orbit})
        results.append({"k": k, "d": d, "crossings": crossings,
                        "seeds": seeds, "basin": basin,
                        "basin_size": len(basin),
                        "max_valuation": max(row["valuation"] for row in basin),
                        "one_letter_exceptions": one_letter,
                        "transposition_exceptions": transpositions})
    controls = []
    for d in (5, 7, 13, 61):
        y, valuation = step(-1, d)
        require(y > 0, ("missing sign-crossing control", d))
        controls.append({"d": d, "start": -1, "valuation": valuation, "end": y})
    return {"scope": {"minimum_gap": 3, "maximum_gap": 12},
            "results": results, "controls": controls}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    result = compute()
    if args.write_receipt:
        RECEIPT.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    else:
        require(RECEIPT.exists(), "missing receipt")
        require(json.loads(RECEIPT.read_text()) == result, "receipt mismatch")
    print(json.dumps({"status": "PASS", "families": len(result["results"]),
                      "basin_states": sum(r["basin_size"] for r in result["results"]),
                      "one_letter_exceptions": sum(len(r["one_letter_exceptions"])
                                                    for r in result["results"]),
                      "transposition_exceptions": sum(len(r["transposition_exceptions"])
                                                       for r in result["results"])}))


if __name__ == "__main__":
    main()
