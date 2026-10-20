"""Sidekick probe: where the full signed closure of main's fifteen-family dispatcher stops.

For random w = 5 (mod 8) of each size, run main's refined_rules.close(w) (commit d265d94),
which expands every accepted plan recursively under strict rho and keeps unrecognized
inputs as signed leaves. Recorded per size: root accepted; closure complete (no leaves);
all leaves below 2^20 (complete up to a finite table); leaf count; and the gap in bits
between rho(w) and the largest leaf rank. Measurement, not a check. Run without -O.
"""
from pathlib import Path
from statistics import median
import json
import math
import random
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "experiments/residual_progress/refined_rules"))
import refined_rules as R  # noqa: E402

RANK = R.RANK


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng = random.Random(61)
    rows = []
    for bits in (16, 24, 32, 48, 64):
        n, acc, complete, small, capped, gaps, leaves = 200, 0, 0, 0, 0, [], []
        for _ in range(n):
            w = rng.randrange(2**(bits - 1), 2**bits)//8*8 + 5
            try:
                c = R.close(w, max_nodes=20000)
            except RuntimeError:
                capped += 1
                continue
            acc += bool(c["expanded"]) and w in c["expanded"]
            ranks = [RANK.rho(u) for u in c["unresolved"]]
            leaves.append(len(ranks))
            complete += not ranks
            small += all(r < 2**20 for r in ranks)
            if ranks:
                gaps.append(math.log2(RANK.rho(w)/max(ranks)))
        rows.append(dict(bits=bits, samples=n, capped=capped, root_accepted=round(acc/n, 3),
                         closure_complete=round(complete/n, 3), all_leaves_below_2_20=round(small/n, 3),
                         median_leaves=median(leaves), median_gap_bits=round(median(gaps), 2),
                         gap_at_least_8_bits=round(sum(g >= 8 for g in gaps)/len(gaps), 3)))
        print(json.dumps(rows[-1]))
    report = dict(scope="Closure frontier of main's fifteen-family dispatcher by size; measurement, not a check.",
                  rows=rows, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
