"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/s5_mismatch_height.py: side-lane probe (about 1 s): (a) on 283 actual 3x+q cycles (odd q < 200, 3 ∤ q) and all 3,100 nonidentity rotations, the longest agreeing run meets the pigeonhole and C013 (7) in exact integers; (b) the q = 1 bound at m = 1.375·10^11 by band ...
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/s5_mismatch_height.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
