"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B11-residual-R40-R60 migration (consolidated onto tools/legacy_replay.py). The legacy
scripts load sibling modules by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/critical_rank/check_rank_closure.py: W9 and absorption rank bounds, the four-rule union on 1024 candidates, substitutions and rejections, against critical_rank_audit.json and the w749 fixture;
  - the side-lane probe batch_r43_r46_check.py, placed in reviews/side_lane/ beside fibre_count_check.py, whose committed receipt must be reproduced byte for byte.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/critical_rank/check_rank_closure.py', 'reviews/side_lane/batch_r43_r46_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
