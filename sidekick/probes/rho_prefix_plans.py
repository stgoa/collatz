"""Sidekick probe: quotient-prefix plans with target (8 rho(w) - 5)/9 are strictly rho-decreasing.

Claim (written proof, from main's R43/R51/R62): for w in W5, let q = nu(3w) = rho(w) and follow
T = nu o S from q to the first state x with 9x + 5 < 8 rho(w). Then
    J = N_3w + sum_{i<n} quotient_bridge(T^i q) + H_x - N_w - H_z,   z = nu(w),
has divergence P(w) - requests(H_x) + requests(H_z), and every request has rho < rho(w):
  * H_x requests have sigma(u) <= nu(x) = x (R51). By R62 (1), rho(u) = (9 sigma(u) + 5)/8 on
    E and rho(u) = sigma(u) off E; either way rho(u) <= (9x + 5)/8 < rho(w).
  * H_z requests have rho(u) <= (9z + 5)/8 (R43), z <= (w - 1)/4, and rho(w) > w.
So universal P(w) follows if every such quotient orbit drops below (8 rho(w) - 5)/9.

Check: main's own rho validator (critical_rank.rank_closure.validate_step) accepts every plan,
for random w at 24/40/64 bits in every class; lookahead n reported by class. Main code at
793e835 (read-only imports). Standard library. Run without -O.
"""
from collections import Counter, defaultdict
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import backward_word_rule as B  # noqa: E402

SIG, NORMAL, RANK, combine = B.SIG, B.NORMAL, B.RANK, B.combine


def rho_prefix_plan(w):
    R = RANK.rho(w)
    q, x, n = NORMAL.normal_form(3*w), None, 0
    parts, x = [(1, NORMAL.bridge(3*w)["current"])], q
    while 9*x + 5 >= 8*R and x != 1:
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
    RANK.validate_step(w, data)
    return n


def label(w):
    s = "3w selected" if NORMAL.selected(3*w) else "3w non-selected"
    return "%s, w=%d mod 3%s" % (s, w % 3, " (returning)" if SIG.RETURN.returning(w) else "")


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(89)
    validated, by_class = Counter(), defaultdict(list)
    for bits in (24, 40, 64):
        for _ in range(1200):
            w = rng.randrange(2**(bits - 1), 2**bits)//8*8 + 5
            by_class[label(w)].append(rho_prefix_plan(w))
            validated[bits] += 1
    allrows = [n for rows in by_class.values() for n in rows]
    cum = lambda rows: {"n<=%d" % L: round(sum(n <= L for n in rows)/len(rows), 3) for L in (2, 4, 8, 16, 32)}
    report = dict(scope="Quotient-prefix plans with target (8 rho - 5)/9, checked with main's rho validator.",
                  validated_by_bits=dict(validated), all_inputs=dict(cum(allrows), max=max(allrows)),
                  by_class={k: dict(cum(v), samples=len(v), max=max(v)) for k, v in sorted(by_class.items())},
                  status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["all_inputs"]), json.dumps(report["validated_by_bits"]))


if __name__ == "__main__":
    main()
