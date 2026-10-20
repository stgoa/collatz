"""Replay this node's unmodified side-lane control computation in a temporary copy of the legacy layout.

Written at the B16-invariants-viewpoints migration. The side-lane probe below computes control data (it
reports DONE, with no failure exit except when a cycle search fails), so it is replayed through
tools/legacy_replay.py, which rebuilds the pre-migration tree in a temporary directory, runs it there and
requires exit 0 and every file byte-identical afterwards: its committed receipt must be reproduced byte for
byte. This certifies the reported finite counts, not any growth statement. Nothing in the repository is
written. Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/automatic_rigidity_control.py: distinct 2-kernel elements (60-term prefixes, levels
    e <= 9) of the "which cycle" colourings of 3x+5, 3x+7, 3x+13 and of the indicators 1_(d|n), against
    automatic_rigidity_control.json.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/automatic_rigidity_control.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
