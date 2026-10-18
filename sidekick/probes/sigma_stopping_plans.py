"""Sidekick probe: under R51's sigma, plain quotient-orbit prefixes give valid plans for all of W5.

For w in W5 let q = nu(3w) and follow T = nu o S from q to the first state x < sigma(w)
(n quotient steps). The plan
    N_3w + sum_{i<n} quotient_bridge(T^i q) + H_x - N_w - H_z,   z = nu(w),
has boundary P(w) - requests(H_x) + requests(H_z); by R51 every request has
sigma <= max(x, z) < sigma(w). Each plan is built from main's code (commit 8764158) and
checked with main's sigma_rank.validate. Reported: validation count, and the lookahead n
needed, by class, next to main's continued dispatcher (seven rules + R52 + R53).
Standard library. Run without -O.
"""
from collections import Counter, defaultdict
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import backward_word_rule as B  # noqa: E402  (imports main's sigma_rank and continued_rules)

SIG, NORMAL, CONT, combine = B.SIG, B.NORMAL, B.CONT, B.combine


def stopping_plan(w, cap=10**4):
    q, target = NORMAL.normal_form(3*w), SIG.sigma(w)
    parts, x, n = [(1, NORMAL.bridge(3*w)["current"])], q, 0
    while x >= target and x != 1:
        b = NORMAL.quotient_bridge(x)
        parts.append((1, b["current"]))
        x, n = b["minimum"], n + 1
        assert n < cap, "no quotient descent within the cap"
    z = NORMAL.normal_form(w)
    hx, hz = SIG.absorption_plan(x), SIG.absorption_plan(z)
    parts += [(1, hx["current"]), (-1, NORMAL.bridge(w)["current"]), (-1, hz["current"])]
    coeff = Counter(hx["coefficients"])
    for u, c in hz["coefficients"].items():
        coeff[u] -= c
    data = dict(seed=w, current=combine(*parts), coefficients={u: c for u, c in sorted(coeff.items()) if c})
    SIG.validate(w, data)
    return n


def label(w):
    s = "3w selected" if NORMAL.selected(3*w) else "3w non-selected"
    return "%s, w=%d mod 3%s" % (s, w % 3, " (returning)" if SIG.RETURN.returning(w) else "")


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(9)
    validated, by_class = Counter(), defaultdict(list)
    for bits in (24, 40, 64):
        for _ in range(1200):
            w = rng.randrange(2**(bits - 1), 2**bits)//8*8 + 5
            n = stopping_plan(w)
            validated[bits] += 1
            by_class[label(w)].append((n, CONT.one_step(w) is not None))
    table = {}
    for cls, rows in sorted(by_class.items()):
        m = len(rows)
        table[cls] = dict(samples=m, continued_dispatcher=round(sum(a for _, a in rows)/m, 3),
                          **{"lookahead<=%d" % L: round(sum(n <= L for n, _ in rows)/m, 3) for L in (1, 2, 4, 8, 16, 32)},
                          max_lookahead=max(n for n, _ in rows))
    allrows = [r for rows in by_class.values() for r in rows]
    total = {"lookahead<=%d" % L: round(sum(n <= L for n, _ in allrows)/len(allrows), 3) for L in (1, 2, 4, 8, 16, 32)}
    report = dict(scope="Quotient-prefix plans checked with main's sigma validator; lookahead needed by class "
                        "versus main's continued dispatcher (measurement for the latter).",
                  validated_by_bits=dict(validated), all_inputs=total, by_class=table, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
