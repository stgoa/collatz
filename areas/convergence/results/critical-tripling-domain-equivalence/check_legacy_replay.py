"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/tripling_equivalence/check_tripling.py: the legacy plan constructor (local steps with exact boundaries, static and critical decreasing plans, compile_plan accepting only checked supplied pair currents) and checker (16,384 local steps, 6,144 inputs of W, 2,731 critical inverse inputs ...;
  - reviews/side_lane/batch_436f51f_check.py: side-lane probe (Claude side lane, 2026-10-17) of R37, R38 (odd-h-pair-interface-compiler), R39 (coupled-even-pair-recursion) and negative controls on W.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/tripling_equivalence/check_tripling.py', 'reviews/side_lane/batch_436f51f_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
