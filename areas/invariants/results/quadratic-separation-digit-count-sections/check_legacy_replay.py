"""Replay this node's unmodified side-lane check in a temporary copy of the legacy layout.

Written at the B16-invariants-viewpoints migration. The side-lane probe below rewrites its receipt and
reports PASS without a failure exit of its own, so it is replayed through tools/legacy_replay.py, which
rebuilds the pre-migration tree in a temporary directory, runs it there and requires exit 0 and every
file byte-identical afterwards: its committed receipt must be reproduced byte for byte. Nothing in the
repository is written. Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/v006_quadratic_check.py: the quadratic example (64 sequences, a, t <= 7, distinct on a
    400-term prefix), the search for digit-count sections in the actual 3x+5, 3x+13 and 3x+61 cycle
    labellings (none found), and the adjacent-11 control's invariance failure at 3, against
    v006_quadratic_check.json.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/v006_quadratic_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
