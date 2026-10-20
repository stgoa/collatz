"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/shadow_precision/check_shadow_precision.py: the legacy Python classifier, checker, receipt and the independent C++ classifier (compiled and compared only with --cpp): the full 1,732,883-origin basin with its 19 hit records, the c0 cycle, the branch inequalities ...
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/shadow_precision/check_shadow_precision.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
