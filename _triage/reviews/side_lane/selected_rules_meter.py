"""Sidekick probe: acceptance meter for main's twelve-family dispatcher (R41-R57,
experiments/residual_progress/selected_rules/selected_rules.py).

Random w = 5 (mod 8) per bit size; one_step(w) builds and validates the plan (None means
unresolved). Reports overall acceptance, the accepting rule, and acceptance by class
(3w selected or not, w mod 3). Uses this checkout's copy of main's code when present,
otherwise main's working copy two levels above the worktree (read-only).
Measurement, not a check. Standard library. Run without -O.
"""
from collections import Counter
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SRC = ROOT / "experiments/residual_progress/selected_rules"
if not SRC.exists():
    SRC = ROOT.parents[2] / "experiments/residual_progress/selected_rules"
sys.path[:0] = [str(HERE), str(SRC)]
import selected_rules as R  # noqa: E402
from fibre_count_check import selected  # noqa: E402


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(5)
    rows = []
    for bits in (10, 14, 18, 24, 32, 48, 64):
        n = 1000
        rules, tot, acc = Counter(), Counter(), Counter()
        for _ in range(n):
            w = rng.randrange(2**(bits - 1), 2**bits)//8*8 + 5
            d = R.one_step(w)
            rules[d["rule"].split("_")[0] if d else "unresolved"] += 1
            key = "%s, w mod 3 = %d" % ("3w selected" if selected(3*w) else "3w non-selected", w % 3)
            tot[key] += 1
            acc[key] += d is not None
        rows.append(dict(bits=bits, samples=n, accepted=round(1 - rules["unresolved"]/n, 3),
                         by_rule={k: v for k, v in sorted(rules.items()) if k != "unresolved"},
                         accepted_by_class={k: round(acc[k]/tot[k], 2) for k in sorted(tot)}))
    report = dict(scope="Measurement of main's twelve-family dispatcher by size and class; not a check.",
                  source=str(SRC), rows=rows, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps([dict(bits=r["bits"], accepted=r["accepted"]) for r in rows]))


if __name__ == "__main__":
    main()
