"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/odd_pair_closure/check_odd_interface.py: the legacy interface, compiler and checker (8192 Q interfaces and static labels, 2731 odd-h reductions below 32768, 528 Zplus parameter cases through k = 32, 171 parent clocks, 14 expanding examples ...
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/odd_pair_closure/check_odd_interface.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
