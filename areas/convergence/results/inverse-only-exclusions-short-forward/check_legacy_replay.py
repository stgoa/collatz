"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B11-residual-R40-R60 migration (consolidated onto tools/legacy_replay.py). The legacy
scripts load sibling modules by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/inverse_scope/check_inverse_scope.py: the two all-depth closed tables, inverse words, forward plans, against inverse_scope_audit.json and anchor_certificates.json;
  - the side-lane probe r49_ancestor_free.py, placed in reviews/side_lane/ beside fibre_count_check.py, whose committed receipt must be reproduced byte for byte.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/inverse_scope/check_inverse_scope.py', 'reviews/side_lane/r49_ancestor_free.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
