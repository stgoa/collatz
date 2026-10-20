"""Sidekick probe: R62's sigma/rho compatibility theorem on actual sigma-valid plans.

R62 (main, staged after d265d94): on the returning class E, rho(u) = (9 sigma(u) + 5)/8, and
rho = sigma elsewhere. For a sigma-valid plan of P(w): if w is in E the plan is rho-valid; if
not, the requests with rho(u) >= rho(w) are exactly the E-requests with
ceil((8 rho(w) - 5)/9) <= sigma(u) < rho(w).

Checks: identity (1) on 20,000 E inputs; the theorem on the quotient-prefix sigma plans of
the 23:43 entry (built from main's code, checked with main's sigma validator), for random w
at 24/40/64 bits. Also measured: how often such a plan is already strictly rho-decreasing.
Standard library. Run without -O.
"""
from collections import Counter
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import backward_word_rule as B  # noqa: E402

SIG, NORMAL, RANK, combine = B.SIG, B.NORMAL, B.RANK, B.combine


def in_E(u):
    return SIG.RETURN.returning(u)


def prefix_plan(w):
    q, target = NORMAL.normal_form(3*w), SIG.sigma(w)
    parts, x, n = [(1, NORMAL.bridge(3*w)["current"])], q, 0
    while x >= target and x != 1:
        b = NORMAL.quotient_bridge(x)
        parts.append((1, b["current"]))
        x, n = b["minimum"], n + 1
    z = NORMAL.normal_form(w)
    hx, hz = SIG.absorption_plan(x), SIG.absorption_plan(z)
    parts += [(1, hx["current"]), (-1, NORMAL.bridge(w)["current"]), (-1, hz["current"])]
    coeff = Counter(hx["coefficients"])
    for u, c in hz["coefficients"].items():
        coeff[u] -= c
    data = dict(seed=w, current=combine(*parts), coefficients={u: c for u, c in sorted(coeff.items()) if c})
    SIG.validate(w, data)
    return n, data


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(62)
    e_checked = 0
    while e_checked < 20000:
        u = rng.randrange(2**20, 2**48)//8*8 + 5
        if in_E(u):
            assert 8*RANK.rho(u) == 9*SIG.sigma(u) + 5
            e_checked += 1
    tally = Counter()
    for bits in (24, 40, 64):
        for _ in range(1000):
            w = rng.randrange(2**(bits - 1), 2**bits)//8*8 + 5
            n, data = prefix_plan(w)
            R = RANK.rho(w)
            frontier = {u for u in data["coefficients"] if RANK.rho(u) >= R}
            if in_E(w):
                assert not frontier
                tally["E parent: rho-valid"] += 1
                continue
            lo = -(-(8*R - 5)//9)
            predicted = {u for u in data["coefficients"] if in_E(u) and lo <= SIG.sigma(u) < R}
            assert frontier == predicted, w
            tally["non-E parent"] += 1
            tally["non-E parent: already rho-valid"] += not frontier
    report = dict(scope="R62 compatibility identity and theorem on quotient-prefix sigma plans.",
                  e_identity_checked=e_checked, plans=dict(tally),
                  share_non_E_already_rho_valid=round(tally["non-E parent: already rho-valid"]/tally["non-E parent"], 3),
                  status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
