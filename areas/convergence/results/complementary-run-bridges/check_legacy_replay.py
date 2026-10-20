"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/complementary_bridge/check_run_bridge.py: the legacy constructor (both run branches, exact cylinders, weighted floor counts, rational series bounds, supplied-current conversion) and checker (4096 complementary seeds below 32768, 2883 parameter branches, 68 exact normalized counts ...;
  - reviews/side_lane/run_bridge_check.py: side-lane probe (Claude side lane, 2026-10-17): rebuilds the return formulas and checks bridges for all 25,002 complementary roots below 200000 and the coverage at three cutoffs with its own nu.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/complementary_bridge/check_run_bridge.py', 'reviews/side_lane/run_bridge_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
