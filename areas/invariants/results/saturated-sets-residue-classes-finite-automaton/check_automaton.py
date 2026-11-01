#!/usr/bin/env python3
"""Certificate for saturated-sets-residue-classes-finite-automaton.

Setting: T the Collatz map on the positive integers, B a nonempty saturated set (x in B iff T(x) in B), M' coprime to 6,
o4 = ord_M'(4), v = v_3(o4), v* = max(1, v), m3 = 3^(v*+1). For an odd z write W = 3z + 1 and let its state be
(W mod M', W mod m3). Two moves on odd elements of B: the scaling sigma_s(z) = (4^s(3z+1) - 1)/3 (W -> 4^s W) and the
inverse iota_j(z) = (2^j z - 1)/3, legal iff 2^j z = 1 (mod 3) (W -> 2^j z). Free steering (the node's Lemma F) sets
W modulo any 3^(B+1) to any value with the same residue modulo m3 without changing W modulo M', so the digits of W
beyond m3 are free; in particular, before an inverse move the class of z modulo 3^(v*+1) can be any of the three
lifts of its class modulo 3^v*. The automaton on the M' * 3^v* states has the transitions
    (x, y) -> (4^s x, 4^s y)                                          for s >= 1,
    (x, y) -> (2^j (x-1)/3 mod M',  2^j z' mod m3)                    for legal j and each lift z' of (y-1)/3 mod 3^v*.
If it is strongly connected, every nonempty saturated set meets every class modulo 2^k 3^b M' for all k, b (the node's
theorem). Checks:
V1  for every M' <= N_MAX coprime to 6, the automaton is strongly connected (one strongly connected component); the
    receipt records v*, the number of states and the orders of 2 and 4;
V2  controls: for the map 3x+5 (W = 3z + 5, inverse legal iff 2^j z = 5 mod 3, scaling (4^s(3z+5) - 5)/3) the
    automaton modulo 5 is NOT strongly connected (the multiples of 5 are saturated for 3x+5), while modulo 7 it is;
V3  receipt comparison. Exit 1 on failure; --write-receipt regenerates automaton.json. Standard library only."""
import json
import sys
import time
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "automaton.json"
N_MAX = int(sys.argv[sys.argv.index("--nmax") + 1]) if "--nmax" in sys.argv else 1000
failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL:", msg)


def order(a, n):
    if n == 1:
        return 1
    k, x = 1, a % n
    while x != 1:
        x = x * a % n
        k += 1
    return k


def v3(n):
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


def lcm(a, b):
    return a * b // gcd(a, b)


def automaton(Mp, d=1):
    """Returns (strongly_connected, number_of_states, v*, number_of_components, ord2, ord4)."""
    o2, o4 = order(2, Mp), order(4, Mp)
    v = max(1, v3(o4))
    m3, m3v = 3 ** (v + 1), 3 ** v
    inv3M = pow(3, -1, Mp) if Mp > 1 else 0
    ys = [y for y in range(m3) if y % 3 == d % 3]           # W = d (mod 3)
    yi = {y: i for i, y in enumerate(ys)}
    n = Mp * len(ys)

    def idx(x, y):
        return x * len(ys) + yi[y]

    scal = {(pow(4, s, Mp), pow(4, s, m3)) for s in range(1, lcm(o4, m3v) + 1)}
    invm = {0: set(), 1: set()}
    for j in range(1, lcm(o2, 2 * m3v) + 1):
        invm[j % 2].add((pow(2, j, Mp), pow(2, j, m3)))
    succ = [set() for _ in range(n)]
    for x in range(Mp):
        for y in ys:
            out = succ[idx(x, y)]
            for a, b in scal:
                out.add(idx(a * x % Mp, b * y % m3))
            z3 = ((y - d) // 3) % 3
            if z3 == 0:
                continue                                      # no legal inverse from a multiple of 3
            par = 0 if z3 == d % 3 else 1                     # 2^j z = d (mod 3): j even iff z = d (mod 3)
            zm = ((y - d) // 3) % m3v
            xp_base = ((x - d) * inv3M) % Mp if Mp > 1 else 0
            for a, b in invm[par]:
                xp = a * xp_base % Mp
                for t in range(3):
                    out.add(idx(xp, b * (zm + t * m3v) % m3))
    # Kosaraju's algorithm
    order_, seen = [], bytearray(n)
    for s0 in range(n):
        if seen[s0]:
            continue
        stack = [(s0, iter(succ[s0]))]
        seen[s0] = 1
        while stack:
            u, it = stack[-1]
            nxt = next(it, None)
            if nxt is None:
                order_.append(u)
                stack.pop()
            elif not seen[nxt]:
                seen[nxt] = 1
                stack.append((nxt, iter(succ[nxt])))
    pred = [[] for _ in range(n)]
    for u in range(n):
        for w in succ[u]:
            pred[w].append(u)
    comp, c = [-1] * n, 0
    for u in reversed(order_):
        if comp[u] != -1:
            continue
        stack, comp[u] = [u], c
        while stack:
            a = stack.pop()
            for w in pred[a]:
                if comp[w] == -1:
                    comp[w] = c
                    stack.append(w)
        c += 1
    return c == 1, n, v, c, o2, o4


def main():
    write = "--write-receipt" in sys.argv
    t0 = time.time()
    summary = {"V1": {"N_MAX": N_MAX, "moduli": {}}, "V2": {}}
    moduli = [m for m in range(1, N_MAX + 1) if gcd(m, 6) == 1]
    max_states, max_vstar = 0, 0
    for Mp in moduli:
        ok, n, v, c, o2, o4 = automaton(Mp)
        summary["V1"]["moduli"][str(Mp)] = {"connected": ok, "states": n, "v_star": v, "ord2": o2, "ord4": o4}
        max_states, max_vstar = max(max_states, n), max(max_vstar, v)
        if not ok:
            fail(f"V1: automaton not strongly connected for M' = {Mp} ({c} components)")
    bad = [m for m in moduli if m > 1 and v3(order(2, m)) > 0]
    summary["V1"]["count"] = len(moduli)
    summary["V1"]["max_states"] = max_states
    summary["V1"]["max_v_star"] = max_vstar
    summary["V1"]["moduli_with_3_dividing_ord2"] = len(bad)
    print(f"V1: {len(moduli)} moduli M' <= {N_MAX} coprime to 6, all strongly connected; largest automaton {max_states} states, "
          f"largest v* {max_vstar}; {len(bad)} of them have 3 | ord(2) ({time.time() - t0:.0f} s)")
    ok5, n5, _, c5, _, _ = automaton(5, d=5)
    ok7, n7, _, c7, _, _ = automaton(7, d=5)
    if ok5:
        fail("V2: the 3x+5 automaton modulo 5 is strongly connected")
    if not ok7:
        fail("V2: the 3x+5 automaton modulo 7 is not strongly connected")
    summary["V2"] = {"3x+5 modulo 5": {"connected": ok5, "states": n5, "components": c5},
                     "3x+5 modulo 7": {"connected": ok7, "states": n7, "components": c7}}
    print(f"V2: 3x+5 modulo 5: {c5} components (not connected, as it must be); modulo 7: connected = {ok7}")
    if write:
        RECEIPT.write_text(json.dumps(summary, indent=1) + "\n")
        print("receipt written")
    elif not RECEIPT.exists():
        fail("V3 receipt missing")
    elif json.loads(RECEIPT.read_text()) != summary:
        fail("V3 summary differs from the receipt")
    if failures:
        print(f"{len(failures)} failure(s)")
        sys.exit(1)
    print(f"all checks passed ({time.time() - t0:.0f} s)")


if __name__ == "__main__":
    main()
