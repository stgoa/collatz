"""Sidekick probe: acceptance meter and gap map for main's expanded seven-rule union
(commit bcde58e, experiments/residual_progress/double_inverse/expanded_union.py).

For random w = 5 (mod 8) of each bit size, this calls main's one_step(w), which builds and
validates the plan, and records the accepting rule (None means uncovered). At 48 bits it
also splits coverage by class: w mod 3, and whether 3w is selected.
Measurement of main's dispatcher, not a check. Standard library. Run without -O.
"""
from collections import Counter
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "experiments" / "residual_progress" / "double_inverse")]
import expanded_union as E  # noqa: E402
from fibre_count_check import selected  # noqa: E402


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(5)
    rows, gap_map = [], {}
    for bits in (10, 14, 18, 24, 32, 48, 64):
        n = 2000 if bits <= 24 else 1000
        rules, tot, gap = Counter(), Counter(), Counter()
        for _ in range(n):
            w = rng.randrange(2**(bits - 1), 2**bits)//8*8 + 5
            d = E.one_step(w)
            rules[d["rule"] if d else "uncovered"] += 1
            key = "w mod 3 = %d, 3w %s" % (w % 3, "selected" if selected(3*w) else "non-selected")
            tot[key] += 1
            gap[key] += d is None
        rows.append(dict(bits=bits, samples=n, accepted=round(1 - rules["uncovered"]/n, 4),
                         by_rule={k: round(v/n, 4) for k, v in sorted(rules.items()) if k != "uncovered"}))
        if bits == 48:
            gap_map = {k: round(gap[k]/tot[k], 3) for k in sorted(tot)}
    report = dict(scope="Measurement of main's expanded union by size and class; not a check.",
                  rows=rows, uncovered_by_class_at_48_bits=gap_map, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
