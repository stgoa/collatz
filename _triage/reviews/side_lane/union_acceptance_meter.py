"""Sidekick probe: size dependence of main's fixed-priority rule union (commit a06ef3c,
experiments/residual_progress/critical_rank/rules_union.py).

For random w = 5 (mod 8) of a given bit size, records which top-level strict-rank rule
accepts w: R41, R45, R44 (descending status) or R46, in the union's own priority order.
None means w stays in the complement on which supplied currents are still required.
This uses main's own predicates. It measures the dispatcher; it does not check it.
Standard library. Run without -O.
"""
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "experiments" / "residual_progress" / "critical_rank"))
import rules_union as U  # noqa: E402


def which(w):
    if U.RANK.INVERSE.eligible(w) and w % 9 != 3:
        return "R41"
    if U.BASE.decreasing_domain(w):
        return "R45"
    if U.RETURN.returning(w):
        return "R44" if U.RETURN.forward_plan(w)["status"] == "descending" else None
    if U.ESCAPE.recognized(w):
        return "R46"
    return None


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(5)
    rows = []
    for bits in (10, 14, 18, 24, 32, 48, 64, 80):
        n = 4000 if bits <= 18 else 2000
        counts = {}
        for _ in range(n):
            w = rng.randrange(2**(bits - 1), 2**bits)//8*8 + 5
            r = which(w)
            counts[str(r)] = counts.get(str(r), 0) + 1
        rows.append(dict(bits=bits, samples=n, accepted=round(1 - counts.get("None", 0)/n, 4),
                         by_rule={k: round(v/n, 4) for k, v in sorted(counts.items()) if k != "None"}))
    report = dict(scope="Measurement of main's rule-union acceptance by input size; not a check.",
                  rows=rows, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
