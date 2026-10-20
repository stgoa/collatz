"""Replay this node's unmodified side-lane check in a temporary copy of the legacy layout.

Written at the B16-invariants-viewpoints migration. The side-lane probe below rewrites its receipt and
reports PASS without a failure exit of its own, so it is replayed through tools/legacy_replay.py, which
rebuilds the pre-migration tree in a temporary directory, runs it there and requires exit 0 and every
file byte-identical afterwards: its committed receipt must be reproduced byte for byte. Nothing in the
repository is written. Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/v13_coloring_check.py: the periodic classification on residue graphs (2,400 cases,
    M <= 400, d in {1, 5, 7, 11, 13, 61}: components equal the <x2, x3>-orbits on Z/gcd(M, d)Z) and the
    d | n controls, against v13_coloring_check.json.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/v13_coloring_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
