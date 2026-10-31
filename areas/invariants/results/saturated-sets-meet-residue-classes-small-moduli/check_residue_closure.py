#!/usr/bin/env python3
"""Certificate for saturated-sets-meet-residue-classes-small-moduli.

Setting: T the Collatz map on the positive integers (n -> n/2 for even n, 3n+1 for odd n), and B a nonempty set that is
saturated, i.e. x in B iff T(x) in B. Then B is closed under the four moves
    double  x -> 2x,   halve  (x even) x -> x/2,   forward  (x odd) x -> 3x+1,   inverse  (x = 4 mod 6) x -> (x-1)/3,
and B contains an odd element (halve any element until it is odd).
Residue bookkeeping: with M = 2^aM 3^bM M' (gcd(M', 6) = 1), after i halvings and j inverse steps a class modulo
L(i, j) = 2^(aM+a-i) 3^(bM+b-j) M' is known, and each move's result is determined modulo the next level's modulus.
V1  for every M <= N_CERT: the least budget (a, b), by increasing a + b, such that from EVERY ODD residue class modulo
    L(0, 0) every class modulo M is reached (backward search from each target class); this proves that every saturated
    nonempty B meets every residue class modulo M;
V2  control: for the map 3x+5 (forward x -> 3x+5, inverse x = 2 mod 6 -> (x-5)/3) the same search FAILS for M = 5 with
    every budget a, b <= 4, as it must, since the odd multiples of 5 generate a saturated set avoiding the other classes;
V3  receipt comparison. Exit 1 on failure; --write-receipt regenerates residue_closure.json. Standard library only."""
import json
import sys
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "residue_closure.json"
N_CERT = 100
AMAX, BMAX = 6, 6
failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL:", msg)


def factor_M(M):
    aM = bM = 0
    while M % 2 == 0:
        M //= 2
        aM += 1
    while M % 3 == 0:
        M //= 3
        bM += 1
    return aM, bM, M


def check(M, a, b, d=1):
    """True iff from every odd start class modulo L(0, 0) every residue class modulo M is reachable within the budget."""
    aM, bM, Mp = factor_M(M)

    def L(i, j):
        return 2 ** (aM + a - i) * 3 ** (bM + b - j) * Mp

    offset, total = {}, 0
    for i in range(a + 1):
        for j in range(b + 1):
            offset[(i, j)] = total
            total += L(i, j)
    rev = [[] for _ in range(total)]

    def idx(i, j, c):
        return offset[(i, j)] + c

    inv_class = (d + 3) % 6                     # x = d + 3 (mod 6) iff (x - d)/3 is an odd integer
    for i in range(a + 1):
        for j in range(b + 1):
            Lij = L(i, j)
            has2 = (aM + a - i) >= 1
            has3 = (bM + b - j) >= 1
            for c in range(Lij):
                src = idx(i, j, c)
                rev[idx(i, j, (2 * c) % Lij)].append(src)
                if has2:
                    if c % 2 == 0:
                        if i < a:
                            rev[idx(i + 1, j, (c // 2) % L(i + 1, j))].append(src)
                    else:
                        rev[idx(i, j, (3 * c + d) % Lij)].append(src)
                    if has3 and c % 6 == inv_class and j < b:
                        rev[idx(i, j + 1, ((c - d) // 3) % L(i, j + 1))].append(src)
    L0 = L(0, 0)
    for r in range(M):
        seen = bytearray(total)
        dq = deque()
        for i in range(a + 1):
            for j in range(b + 1):
                for c in range(r % M, L(i, j), M):
                    s = idx(i, j, c)
                    seen[s] = 1
                    dq.append(s)
        while dq:
            s = dq.popleft()
            for p in rev[s]:
                if not seen[p]:
                    seen[p] = 1
                    dq.append(p)
        if any(not seen[idx(0, 0, c)] for c in range(1, L0, 2)):
            return False
    return True


def least_budget(M, d=1, amax=AMAX, bmax=BMAX):
    for s in range(0, amax + bmax + 1):
        for a in range(0, min(s, amax) + 1):
            b = s - a
            if b <= bmax and check(M, a, b, d):
                return [a, b]
    return None


def v1():
    table = {}
    for M in range(1, N_CERT + 1):
        bud = least_budget(M)
        if bud is None:
            fail(f"V1 no budget up to ({AMAX}, {BMAX}) works for M = {M}")
        table[str(M)] = bud
    return table


def v2():
    out = {}
    for a in range(0, 5):
        for b in range(0, 5):
            if check(5, a, b, d=5):
                fail(f"V2 the 3x+5 control passed for M = 5 with budget ({a}, {b})")
    out["3x+5, M=5, budgets <= (4,4)"] = "fails for every budget, as it must"
    # and the same search does prove M = 2 for 3x+5 (parity is not obstructed)
    out["3x+5, M=2"] = least_budget(2, d=5)
    return out


def main():
    write = "--write-receipt" in sys.argv
    summary = {"V1": v1(), "V2": v2()}
    if write:
        RECEIPT.write_text(json.dumps(summary, indent=1) + "\n")
        print("receipt written")
    elif not RECEIPT.exists():
        fail("V3 receipt missing")
    elif json.loads(RECEIPT.read_text()) != summary:
        fail("V3 summary differs from the receipt")
    t = summary["V1"]
    ok = {int(k): v for k, v in t.items() if v is not None}
    print(f"V1: {len(ok)} of {N_CERT} moduli proved; max halvings {max(v[0] for v in ok.values())}, max inverse steps {max(v[1] for v in ok.values())}")
    print("V2:", summary["V2"])
    if failures:
        print(f"{len(failures)} failure(s)")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
