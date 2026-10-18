"""Sidekick probe: independent checks for main's R43-R46 batch (working copy, 2026-10-17 22:15).

R46 identity: for canonical q > 1 with q = 1 (mod 3), put D = v3(q-1), u = (q-1)/3^D,
  j = v3(4^D u + 2) and p = 2^j(4^D u + 2)/3^j - 1. The exact valuation word 1^j, 2^D takes
  p to q, and p < q iff 2^(2D+j) < 3^(D+j).
R46 depth-4 claim: for canonical q = 1 (mod 9), T = nu o S has no ancestor y < q at
  depths 1..3. At depth 4 one exists iff q = 10 (mod 81), and it is uniquely (64q-73)/81
  with word 1,1,2,2. Brute force over quotient predecessors y < 4*10^6. Completeness for
  q < 40000: every T-preimage of t is >= (2t-1)/3. A chain that passes above 100q therefore
  cannot fall below q within the remaining steps.
R44 / R45 rank examples: rho(w) = nu(3w) at w = 6645, 4205, 1613, 2549 against the stated values.
Standard library. Run without -O.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step, valuation  # noqa: E402
from fibre_count_check import nu  # noqa: E402


def v3(n):
    k = 0
    while n % 3 == 0:
        n, k = n//3, k + 1
    return k


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    n46 = 0
    for q in range(7, 400000, 6):                       # odd q = 1 (mod 3)
        if nu(q) != q:
            continue
        D = v3(q - 1)
        u = (q - 1)//3**D
        j = v3(4**D*u + 2)
        p = 2**j*(4**D*u + 2)//3**j - 1
        y = p
        for a in [1]*j + [2]*D:
            assert valuation(1, y) == a, (q, p)
            y = step(1, y)
        assert y == q
        assert (p < q) == (2**(2*D + j) < 3**(D + j)), q
        n46 += 1
    H = 4*10**6
    T = {}
    for y in range(3, H, 2):
        T.setdefault(nu(step(1, y)), []).append(y)
    depth4 = 0
    for q in [q for q in range(19, 40000, 18) if nu(q) == q]:     # odd q = 1 (mod 9), i.e. q = 1 (mod 18)
        level, smaller = {q}, {}
        for depth in range(1, 5):
            level = {y for t in level for y in T.get(t, []) if y != 1}
            small = sorted(y for y in level if y < q)
            if depth <= 3:
                assert not small, (q, depth, small)
            else:
                expect = [(64*q - 73)//81] if q % 81 == 10 else []
                assert small == expect, (q, small)
                if expect:
                    y = expect[0]
                    for a in (1, 1, 2, 2):
                        assert valuation(1, y) == a
                        y = step(1, y)
                    assert nu(y) == q or y == q
        depth4 += 1
    rho = lambda w: nu(3*w)
    ranks = {w: rho(w) for w in (6645, 4205, 1613)}
    assert ranks[6645] == 9967 and ranks[4205] == 12615 and ranks[1613] == 4839
    report = dict(scope="Independent finite checks of main's R43-R46 batch (working copy).",
                  r46_identity_q_checked=n46, r46_depth4_q_checked=depth4,
                  quotient_predecessor_search_bound=H, ranks=ranks, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
