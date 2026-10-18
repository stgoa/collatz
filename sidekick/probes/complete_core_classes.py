"""Sidekick probe: is the complete closure core of main's fifteen-family dispatcher a union of
low-modulus classes? For each W5 class r mod 576, 16 random 32-bit w = r (mod 576) are closed
with refined_rules.close (commit d265d94); the share with no remaining leaf is reported.
Measurement, not a check. Standard library. Run without -O.
"""
from collections import Counter
from pathlib import Path
import json
import random
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "experiments/residual_progress/refined_rules"))
import refined_rules as R  # noqa: E402


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    rng, M, rates = random.Random(7), 576, {}
    for r in range(5, M, 8):
        done = sum(not R.close(r + M*rng.randrange(2**22, 2**23), max_nodes=20000)["unresolved"]
                   for _ in range(16))
        rates[r] = done/16
    top = sorted(rates.items(), key=lambda kv: -kv[1])[:5]
    report = dict(scope="Complete-closure share by W5 class mod 576 at 32 bits; measurement, not a check.",
                  classes=len(rates), max_share=max(rates.values()), top_classes=top,
                  histogram={str(k): v for k, v in sorted(Counter(round(p, 1) for p in rates.values()).items())},
                  status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
