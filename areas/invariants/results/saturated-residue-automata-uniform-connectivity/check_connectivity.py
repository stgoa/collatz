#!/usr/bin/env python3
"""Finite checks of the sparse residue graph and its W-coordinate embedding.

The all-modulus result is proved in README.md; this certificate checks bounded
instances and the 3x+d controls without assuming the theorem's conclusion.
"""
from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "check_connectivity.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def reachable(adj):
    seen = {0}
    stack = [0]
    while stack:
        for other in adj[stack.pop()]:
            if other not in seen:
                seen.add(other)
                stack.append(other)
    return len(seen)


def check(m, v, d):
    n = m * 3**v
    inv4 = pow(4, -1, n)
    succ = [[] for _ in range(n)]
    pred = [[] for _ in range(n)]
    q3 = 3 ** (v + 1)
    embedded_edges = 0
    for z in range(n):
        scale = (4*z + d) % n
        source = ((3*z + d)*inv4) % n
        for a, b in ((z, scale), (source, z)):
            succ[a].append(b)
            pred[b].append(a)
        # Independently check the defining congruence of the inverse arrow.
        require((4*source-d-3*z) % n == 0, "inverse congruence")
        # W=(3z+d mod m, 3z+d mod 3^(v+1)). Check the old automaton's
        # s=1 scaling arrow and one of its three j=2 lift arrows.
        w = (3*z+d) % q3
        wscale = (3*scale+d) % q3
        require(wscale == 4*w % q3, "scaling W coordinate")
        require((3*scale+d-4*(3*z+d)) % m == 0, "scaling m coordinate")
        wsource = (3*source+d) % q3
        require(source % 3 == d % 3, "j=2 legality")
        lifts = [source + t*3**v for t in range(3)]
        require(any(4*t % q3 == w for t in lifts), "inverse W lift")
        require((3*z+d-4*source) % m == 0, "inverse m coordinate")
        require((wsource-d) % 3 == 0, "source state legality")
        embedded_edges += 2
    forward, backward = reachable(succ), reachable(pred)
    connected = forward == n and backward == n
    require(connected == (gcd(m, d) == 1), "connectivity criterion")
    if gcd(m, d) > 1:
        divisor = gcd(m, d)
        require(all(b % divisor == 0 for a in range(0, n, divisor)
                    for b in succ[a]), "control closed subset")
    return {"M": m, "v": v, "d": d, "vertices": n,
            "edge_instances": embedded_edges, "strongly_connected": connected,
            "reachable_from_zero": forward, "can_reach_zero": backward}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    cases = [(m, v, 1) for m in range(1, 102) if gcd(m, 6) == 1
             for v in (1, 2, 3)]
    cases.append((487, 5, 1))
    cases.extend((m, v, d) for d in (5, 7, 13, 61)
                 for m in (1, 5, 7, 13, 25, 35, 61, 91)
                 for v in (1, 2))
    rows = [check(*case) for case in cases]
    result = {"cases": len(rows), "vertices_checked": sum(r["vertices"] for r in rows),
              "embedded_edge_instances": sum(r["edge_instances"] for r in rows),
              "rows": rows}
    if args.write_receipt:
        RECEIPT.write_text(json.dumps(result, indent=2) + "\n")
    else:
        require(RECEIPT.exists(), "missing receipt")
        require(json.loads(RECEIPT.read_text()) == result, "receipt mismatch")
    print(f"PASS: {result['cases']} graphs; {result['vertices_checked']} vertices; "
          f"{result['embedded_edge_instances']} coordinate embeddings; d controls passed")


if __name__ == "__main__":
    main()
