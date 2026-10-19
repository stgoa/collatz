"""Sidekick probe: how much of main's R17/R20 outer residual can 2-adic cylinders certify?

Main's residual roots R_N (RETAINED_GRAPH_EXTENSION.md, Section 4; commit 46198fb) are
the roots x = 3 or 7 (mod 12) in the outer shell (N, 3N/2). R20 asks for a
noncircular rule taking every root below N, into the already absorbed seeds.

Terras-style certificate: the first j Syracuse valuations of x are fixed by
x mod 2^(A_j + 1), where A_j is their sum. If such a determined prefix has
3^j * (3/2) < 2^(A_j), the whole residue class drops below N. This holds for
every root in (N, 3N/2) once N exceeds a class constant, and uses only 2-adic
arithmetic. The 3-adic class mod 12 or 36 is independent of these bits (CRT).

d(m) is the exact 2-adic measure, within x = 3 (mod 4), of classes NOT certified
using m bits. A dynamic program computes it; brute-force cylinder enumeration
cross-checks it for m <= 14. Actual roots at two cutoffs are compared against
the class prediction.
Finite exact arithmetic; no universal termination claim. Standard library.
"""
from fractions import Fraction
from pathlib import Path
import json
import math
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step  # noqa: E402


def certified(j, A):
    return 3**j*3 < 2**(A + 1)            # 3^j * (3/2) < 2^A


def undecided_measure(m):
    states, und = {(1, 1): Fraction(1)}, Fraction(0)     # first valuation is 1 (x = 3 mod 4)
    while states:
        nxt = {}
        for (j, A), p in states.items():
            for a in range(1, m - A):
                if not certified(j + 1, A + a):
                    nxt[(j + 1, A + a)] = nxt.get((j + 1, A + a), 0) + p/2**a
            und += p/2**(m - A - 1)
        states = nxt
    return und


def brute_measure(m):
    und = total = 0
    for c in range(3, 2**m, 4):
        total += 1
        x, bits, j, A, ok = c, m, 0, 0, False
        while bits > 0:
            z = (3*x + 1) % 2**bits
            if z == 0:
                break
            a = (z & -z).bit_length() - 1
            if a >= bits:
                break
            j, A, x, bits = j + 1, A + a, z >> a, bits - a
            if certified(j, A):
                ok = True
                break
        und += not ok
    return Fraction(und, total)


def roots(N):
    out = [x for x in range(N + 1, 3*N//2) if x % 12 == 3]
    out += [x for x in range(9*N//8 + 1, 3*N//2) if x % 12 == 7]
    out += [x for x in range(N + 1, 9*N//8) if x % 36 in (7, 19)]
    return sorted(set(out))


def descent_steps(x, N):
    t = 0
    while x > N:
        x, t = step(1, x), t + 1
    return t


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    for m in (8, 10, 12, 14):
        assert undecided_measure(m) == brute_measure(m)
    table = {m: float(undecided_measure(m)) for m in (16, 24, 32, 48, 64, 96, 128)}
    rate = (table[128]/table[64])**(1/64)
    actual = []
    for N in (6144, 98304):
        rs = roots(N)
        steps = sorted(descent_steps(x, N) for x in rs)
        actual.append(dict(N=N, roots=len(rs), median_descent_steps=steps[len(steps)//2],
                           max_descent_steps=steps[-1],
                           slowest_roots=sorted(rs, key=lambda x: -descent_steps(x, N))[:5]))
    report = dict(scope="Exact 2-adic cylinder measure for main's outer residual roots; no "
                  "termination claim.", brute_force_agreement_m=[8, 10, 12, 14],
                  undecided_fraction=table, asymptotic_rate_per_bit=rate,
                  core_exponent=1 + math.log2(rate), actual_roots=actual, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__" and "--merge" not in sys.argv:
    main()


def undecided_with_merge(m):
    """As undecided_measure, but a prefix also certifies merger with S([1,N]):
    y_j <= 3N/2 reached by an odd valuation >= 3 (its valuation-1 predecessor
    (2y_j-1)/3 <= N is an absorbed seed off the orbit)."""
    states, und = {(1, 1): Fraction(1)}, Fraction(0)
    while states:
        nxt = {}
        for (j, A), p in states.items():
            for a in range(1, m - A):
                j2, A2 = j + 1, A + a
                if certified(j2, A2) or (a % 2 and a >= 3 and 3**j2 <= 2**A2):
                    continue
                nxt[(j2, A2)] = nxt.get((j2, A2), 0) + p/2**a
            und += p/2**(m - A - 1)
        states = nxt
    return und


if __name__ == "__main__" and "--merge" in sys.argv:
    for m in (16, 32, 64, 96, 128):
        print(m, float(undecided_measure(m)), float(undecided_with_merge(m)))
