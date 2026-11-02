#!/usr/bin/env python3
"""Certificate for collatz-conjecture-logical-form.

The node shows that "the odd-only 3x+d map has no cycle of period m other than the known ones" is decided by a finite
search: a cycle of period m has a valuation word w of length m with total A satisfying 3^m < 2^A < (3 + d)^m (from
2^A prod n_i = prod (3 n_i + d), n_i >= 1), so 3^m < 2^A <= (3 + d)^m, with equality only at the fixed point 1; its least-rotation state is x0 = d C_w / D_w with
D_w = 2^A - 3^m, and w is a cycle word iff x0 is a positive odd integer whose orbit follows w for m steps.
V1  for d = 1 and every m <= M_MAX, the procedure finds exactly the trivial cycle {1} (m = 1) and nothing else;
V2  controls: for d in {5, 7, 13} and m <= M_CTRL, the procedure finds exactly the primitive cycles of 3x+d with all
    states coprime to d that are found by direct iteration from odd seeds below SEED (cross-check both ways);
V3  receipt comparison. Exit 1 on failure; --write-receipt regenerates cycle_decision.json. Standard library only."""
import itertools
import json
import sys
from math import gcd, log2
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "cycle_decision.json"
M_MAX, M_CTRL, SEED = 12, 7, 20000
failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL:", msg)


def C(w):
    # C_w with C_[] = 0, C_(a::z) = 3^|z| + 2^a C_z
    c = 0
    for i in range(len(w) - 1, -1, -1):
        c = 3 ** (len(w) - 1 - i) + 2 ** w[i] * c
    return c


def follows(x, w, d):
    for a in w:
        y = 3 * x + d
        if y % (2 ** a) or (y // 2 ** a) % 2 == 0:
            return False
        x = y // 2 ** a
    return True


def compositions(total, parts):
    """Positive integer words of the given length and total."""
    for cuts in itertools.combinations(range(1, total), parts - 1):
        bounds = (0,) + cuts + (total,)
        yield [bounds[i + 1] - bounds[i] for i in range(parts)]


def cycles_by_decision(m, d):
    """Primitive cycles of period m of the odd-only 3x+d map with states coprime to d, as sorted state tuples."""
    found = set()
    a_max = int(m * log2(3 + d)) + 1
    for A in range(1, a_max + 1):
        D = 2 ** A - 3 ** m
        if D <= 0 or 2 ** A > (3 + d) ** m:
            continue
        for w in compositions(A, m):
            num = d * C(w)
            if num % D:
                continue
            x0 = num // D
            if x0 <= 0 or x0 % 2 == 0 or gcd(x0, d) != 1 or not follows(x0, w, d):
                continue
            states, x = [], x0
            for a in w:
                states.append(x)
                x = (3 * x + d) // 2 ** a
            if len(set(states)) == m:            # primitive (least period exactly m)
                found.add(tuple(sorted(states)))
    return found


def cycles_by_iteration(d, m_max):
    found = set()
    for s in range(1, SEED, 2):
        if gcd(s, d) != 1:
            continue
        seen, x, order = {}, s, []
        while x not in seen and x < 10 ** 30:
            seen[x] = len(order)
            order.append(x)
            y = 3 * x + d
            while y % 2 == 0:
                y //= 2
            x = y
        if x in seen:
            cyc = order[seen[x]:]
            if len(cyc) <= m_max:
                found.add(tuple(sorted(cyc)))
    return found


def main():
    write = "--write-receipt" in sys.argv
    s = {}
    by_m = {}
    for m in range(1, M_MAX + 1):
        cyc = cycles_by_decision(m, 1)
        by_m[str(m)] = [list(c) for c in sorted(cyc)]
        expected = {(1,)} if m == 1 else set()
        if cyc != expected:
            fail(f"V1: d = 1, m = {m}: found {sorted(cyc)}")
    s["V1"] = {"m_max": M_MAX, "cycles": by_m}
    print(f"V1: 3x+1, periods m <= {M_MAX}: only the trivial cycle (1)")
    s["V2"] = {}
    for d in (5, 7, 13):
        dec = set()
        for m in range(1, M_CTRL + 1):
            dec |= cycles_by_decision(m, d)
        it = cycles_by_iteration(d, M_CTRL)
        if dec != it:
            fail(f"V2: d = {d}: decision {sorted(dec)} vs iteration {sorted(it)}")
        s["V2"][str(d)] = sorted([list(c) for c in dec])
        print(f"V2: 3x+{d}, periods <= {M_CTRL}: {len(dec)} cycles, the same set as direct iteration "
              f"(minima {sorted(min(c) for c in dec)})")
    if write:
        RECEIPT.write_text(json.dumps(s, indent=1) + "\n")
        print("receipt written")
    elif not RECEIPT.exists():
        fail("V3 receipt missing")
    elif json.loads(RECEIPT.read_text()) != s:
        fail("V3 summary differs from the receipt")
    if failures:
        print(f"{len(failures)} failure(s)")
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()
