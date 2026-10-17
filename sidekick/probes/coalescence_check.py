"""Sidekick probe: main's halving coalescence (commit 8e2b5eb,
residual_return/SHRINKING_COALESCENCE.md). Two parts: an independent check, and
its effect on the hard core.

Identity: for odd x = 2^a t - 1 (a = v2(x+1) >= 2, t odd) with t = 3^a (mod 4),
S^a(x) = S^a(q), where q = (x-1)/2.

Checked here:
  1. the identity for every selected x < 2^21 and 2000 random selected x < 2^200;
  2. the coverage claim |R'_N| = 25N/576 + O(log N), within main's stated 6A, by explicit
     enumeration of R_N and of its selected part at several cutoffs;
  3. asymptotic effect: an exact 2-adic dynamic program for roots in (N, 3N/2).
     Selection equals "the valuation after a run of 1s is >= 3".
     Three certificate types are allowed at any orbit state:
       D, descent below N;
       M, merger with S([1,N]);
       H, a selected climber below 2N, whose partner (y-1)/2 is below N.
     It records the uncertified fraction per bit depth and the decay rate.
Exact arithmetic; no termination claim. Standard library. Run without -O.
"""
from fractions import Fraction
from pathlib import Path
import json
import math
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step  # noqa: E402
from residual_vs_induction import R  # noqa: E402


def iterate(x, k):
    for _ in range(k):
        x = step(1, x)
    return x


def selected(x):
    if x % 4 != 3:
        return None
    a = ((x + 1) & -(x + 1)).bit_length() - 1
    t = (x + 1) >> a
    return a if t % 4 == pow(3, a, 4) else None


def check_identity():
    count = 0
    for x in range(3, 2**21, 4):
        a = selected(x)
        if a:
            assert iterate(x, a) == iterate((x - 1)//2, a), x
            count += 1
    rng = random.Random(1017)
    for _ in range(2000):
        while True:
            x = rng.randrange(2**199, 2**200) | 3
            a = selected(x)
            if a:
                break
        assert iterate(x, a) == iterate((x - 1)//2, a)
    return count


def check_coverage(N):
    r = R(N)
    g = sum(c for x, c in r.items() if selected(x))
    rest = sum(r.values()) - g
    A = math.floor(math.log2(3*N/2))
    assert abs(rest - Fraction(25*N, 576)) <= 6*A
    return dict(N=N, R_mass=sum(r.values()), selected_mass=g, remaining_mass=rest,
                remaining_over_25N_576=round(rest/(25*N/576), 4))


def undecided(m, use_M=True, use_H=True):
    states, und = {(1, 1, True): Fraction(1)}, Fraction(0)
    while states:
        nxt = {}
        for (j, A, run_ok), p in states.items():
            for a in range(1, m - A):
                q, j2, A2 = p/2**a, j + 1, A + a
                if 3**j2*3 < 2**(A2 + 1):
                    continue                                              # D
                if use_M and a % 2 and a >= 3 and 3**j2 <= 2**A2:
                    continue                                              # M
                if a == 1:
                    ok = run_ok if run_ok is not None else (3**j*3 <= 2**(A + 2))
                    nxt[(j2, A2, ok)] = nxt.get((j2, A2, ok), 0) + q
                elif use_H and run_ok and a >= 3:
                    continue                                              # H
                else:
                    nxt[(j2, A2, None)] = nxt.get((j2, A2, None), 0) + q
            und += p/2**(m - A - 1)
        states = nxt
    return und


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    identities = check_identity()
    coverage = [check_coverage(N) for N in (96, 768, 6144, 49152, 98304)]
    table = {}
    for m in (16, 32, 64, 96):
        table[m] = [float(undecided(m, False, False)), float(undecided(m, True, False)),
                    float(undecided(m))]
    rates = [(table[96][k]/table[64][k])**(1/32) for k in range(3)]
    report = dict(scope="Independent check of main's halving coalescence and its effect on the "
                  "2-adic undecided core; no termination claim.",
                  identity_checked_small=identities, identity_checked_random_200bit=2000,
                  coverage=coverage, undecided_D_DM_DMH=table,
                  rate_per_bit_64_to_96=dict(D=rates[0], DM=rates[1], DMH=rates[2]), status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
