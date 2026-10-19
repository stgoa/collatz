"""Sidekick probe: compare main's R17 outer residual R_N with classical strong induction.

Assume every odd seed <= N reaches 1 (main's supplied inner absorption).
In the shell (N, 3N/2), classical strong induction looks for odd x that are
neither reached from [1, N] within two steps (x not in S([1,N]) or S^2([1,N]))
nor non-climbers. The probe checks that the support of R_N (RETAINED_GRAPH_EXTENSION.md,
Section 4; commit 46198fb) equals that set exactly:
  supp R_N = { odd x in (N, 3N/2) : x = 3 mod 4, x != 2 mod 3, x not in S^2([1,N]) },
and that R_N's mass differs only by its coefficient-2 compression.
Finite exact check over several cutoffs. Standard library. Run without -O.
"""
from pathlib import Path
import json
import sys

sys.path[:0] = [str(Path(__file__).resolve().parents[2] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import step  # noqa: E402


def R(N):
    out = {}
    for x in range(N + 1, 3*N//2):
        if x % 12 == 3:
            out[x] = 1
        elif x % 12 == 7 and x > 9*N//8:
            out[x] = 1
        elif x % 36 in (7, 19) and x < 9*N//8:
            out[x] = 2
    return out


def induction_residual(N):
    one = {step(1, s) for s in range(1, N + 1, 2)}
    two = {step(1, y) for y in one} | one
    return {x for x in range(N + 1, 3*N//2, 2) if x % 4 == 3 and x not in two}


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rows = []
    for N in (96, 768, 6144, 9216, 49152, 98304):
        r, residual = R(N), induction_residual(N)
        assert set(r) == residual, N
        assert all(x % 3 != 2 for x in residual)
        rows.append(dict(N=N, support=len(residual), R_mass=sum(r.values()),
                         multiples_of_3=sum(1 for x in residual if x % 3 == 0)))
    report = dict(scope="Finite exact identification of main's R_N support; no termination claim.",
                  identity="supp R_N = shell climbers not in S([1,N]) or S^2([1,N])",
                  rows=rows, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
