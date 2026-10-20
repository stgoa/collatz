"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/s13_corollaries.py: side-lane probe for Corollaries 5-7 (about 7 s): subadditivity on 3,963,083 rotation pairs of actual 3x+q cycles (m ≤ 120), the forced-letter law on 99,169 rotations of 4,218 actual cycles, and the q = 1 tables (sparsity, forced letter ...
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/s13_corollaries.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
