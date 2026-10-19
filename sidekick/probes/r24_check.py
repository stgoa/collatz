"""Sidekick probe: arithmetic of main's R24 induction (commit 8e2b5eb).

Ordered cutoffs a*2^b, a in {12,14,16,18,21}, b >= 9. Checks: consecutive
ratios are <= 7/6 < 3/2, so absorption through 3N/2 reaches the next cutoff;
every cutoff is divisible by 512; every odd seed <= 6144 reaches 1 (the base).
Standard library. Run without -O.
"""
from fractions import Fraction
from pathlib import Path
import json
import sys

sys.path[:0] = [str(Path(__file__).resolve().parents[2] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step  # noqa: E402


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    cuts = sorted(a << b for a in (12, 14, 16, 18, 21) for b in range(9, 80))
    ratios = {Fraction(n2, n1) for n1, n2 in zip(cuts, cuts[1:])}
    assert ratios == {Fraction(7, 6), Fraction(8, 7), Fraction(9, 8)}
    assert all(2*n2 <= 3*n1 for n1, n2 in zip(cuts, cuts[1:])) and all(n % 512 == 0 for n in cuts)
    assert cuts[0] == 6144
    for s in range(1, 6145, 2):
        x, t = s, 0
        while x != 1:
            x, t = step(1, x), t + 1
            assert t < 1000
    report = dict(scope="Finite arithmetic of main's R24 step and base; the completion rule is open.",
                  cutoffs_checked=len(cuts), ratios=sorted(str(r) for r in ratios),
                  base="all odd seeds <= 6144 reach 1", status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(report)


if __name__ == "__main__":
    main()
