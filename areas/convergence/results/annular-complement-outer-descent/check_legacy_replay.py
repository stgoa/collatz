"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/complement_recursion/check_transfer.py: the legacy constructor and checker (positive-source ancestor formulas and exact catalogue coverage at M = 8, 16, ..., 512, 768, 6144: 353280 positive atoms, 164 matched roots; five actual transfers at M = 8, 96, 168, 384 ...
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/complement_recursion/check_transfer.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
