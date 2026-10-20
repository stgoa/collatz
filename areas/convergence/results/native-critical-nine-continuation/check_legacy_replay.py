"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B13-residual-R78-R94 migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/native_nine/check_native_nine.py: the legacy checker of this node: 383 local bounds, 226 native cases, 150 full two-ray substitutions, 134 next-A2 cells, 30 exact inequalities, 13 rejections and three supplied outputs, against native_nine_audit.json;
  - reviews/side_lane/batch_r78_r80_check.py: the side-lane probe of R78-R80 (from ../high-smaller-origin-history/), whose committed receipt must be reproduced byte for byte.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/native_nine/check_native_nine.py', 'reviews/side_lane/batch_r78_r80_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
