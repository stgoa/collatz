"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/pair_scope/check_pair_scope.py: the legacy local-current interface (compare_half, the augmented formal label, the counterfamily) and checker (the boundary (4) and decomposition (5) on every complementary root through 32767, 741 parameter cases, 4096 hypothetical edges ...;
  - reviews/side_lane/pair_merge_controls.py: side-lane negative controls (Claude side lane, 2026-10-17 21:09, COUNTEREXAMPLE (generic form)): odd w = 3 mod 8 below 4000 whose w and 3w lie in different basins for 3x-1 (357), 3x+13 (100) and 3x+61 (30).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/pair_scope/check_pair_scope.py', 'reviews/side_lane/pair_merge_controls.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
