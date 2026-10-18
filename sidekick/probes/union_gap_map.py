"""Sidekick probe: where does the uncovered part of W5 sit, under main's rule union?
(commit a06ef3c; uses union_acceptance_meter.which, i.e. main's own predicates).

Random w = 5 (mod 8) at 48 bits are classified by w mod 3 and by whether 3w is a
selected climber. Since w = 5 (mod 8), 3w = 7 (mod 8) is always a climber. Records each
class's share of W5, the fraction left uncovered, and its share of the total gap.
Measurement of main's dispatcher, not a check. Standard library. Run without -O.
"""
from collections import Counter
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from union_acceptance_meter import which  # noqa: E402
from fibre_count_check import selected  # noqa: E402


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(9)
    n, total, gap = 20000, Counter(), Counter()
    for _ in range(n):
        w = rng.randrange(2**47, 2**48)//8*8 + 5
        assert (3*w) % 8 == 7
        key = "w mod 3 = %d, 3w %s" % (w % 3, "selected" if selected(3*w) else "non-selected")
        total[key] += 1
        if which(w) is None:
            gap[key] += 1
    g = sum(gap.values())
    rows = [dict(cls=k, share=round(total[k]/n, 4), uncovered=round(gap[k]/total[k], 4),
                 share_of_gap=round(gap[k]/g, 4)) for k in sorted(total, key=lambda k: -gap[k])]
    report = dict(scope="Measurement of main's rule-union gap by class at 48 bits; not a check.",
                  samples=n, uncovered_overall=round(g/n, 4), rows=rows, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
