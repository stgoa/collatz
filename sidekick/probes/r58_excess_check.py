"""Sidekick probe: test R58's classification of above-seed requests in formal absorption.

R58 (main working copy, 2026-10-18): with n = nu(s), the unchanged formal plan H_s requests
only rho(u) <= n, unless n = 27 mod 48, v2(3n-1) = 4 and 3z is noncanonical for
z = (3n-1)/16; then exactly one request exceeds n, namely u* = 4z+1 with coefficient +1 and
rho(u*) = (9n+5)/8, and all other requests have rho < n.

H_s is taken from main's committed R43 code (critical_rank.rank_closure.absorption_plan at
7206f9c), not from R58's new module. Checked: every odd s in [3, 200001], plus 3000 random
odd s at each of 40 and 64 bits, plus 3000 random canonical s satisfying the exceptional
condition at each size. Standard library. Run without -O.
"""
from collections import Counter
from pathlib import Path
import json
import random
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "experiments/residual_progress/critical_rank"))
import rank_closure as RANK  # noqa: E402

NORMAL = RANK.NORMAL


def v2(n):
    return (n & -n).bit_length() - 1


def exceptional(n):
    if n % 48 != 27 or v2(3*n - 1) != 4:
        return None
    z = (3*n - 1)//16
    return None if NORMAL.canonical(3*z) else 4*z + 1


def check(s, tally):
    n = NORMAL.normal_form(s)
    req = RANK.absorption_plan(s)["coefficients"]
    high = {u: c for u, c in req.items() if RANK.rho(u) > n}
    u_star = exceptional(n)
    if u_star is None:
        assert not high, (s, n, high)
        tally["ordinary"] += 1
    else:
        assert high == {u_star: 1} and 8*RANK.rho(u_star) == 9*n + 5, (s, n, high)
        assert all(RANK.rho(u) < n for u in req if u != u_star), s
        tally["exceptional"] += 1
    if s != n:
        assert all(RANK.rho(u) < s for u in req), s
        tally["noncanonical"] += 1


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    tally = Counter()
    for s in range(3, 200002, 2):
        check(s, tally)
    rng = random.Random(58)
    for bits in (40, 64):
        for _ in range(3000):
            check(rng.randrange(2**(bits - 1), 2**bits) | 1, tally)
        found = 0
        while found < 3000:
            n = rng.randrange(2**(bits - 1), 2**bits)//48*48 + 27
            if NORMAL.canonical(n) and exceptional(n) is not None:
                check(n, tally)
                found += 1
    report = dict(scope="R58 classification tested against main's committed formal absorption plans.",
                  tally=dict(tally), status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
