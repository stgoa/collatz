"""Replay this node's unmodified side-lane check in a temporary copy of the legacy layout.

Written at the B16-invariants-viewpoints migration. The side-lane probe below rewrites its receipt and
reports PASS without a failure exit of its own, so it is replayed through tools/legacy_replay.py, which
rebuilds the pre-migration tree in a temporary directory, runs it there and requires exit 0 and every
file byte-identical afterwards: its committed receipt must be reproduced byte for byte. Nothing in the
repository is written. Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/viewpoint_v001_check.py: the V001 probes (the (1,4) composite (9x+5)/32 on
    x = 3 mod 64 over 1,563 starts, the Applegate-Lagarias row 7 mod 64 on 2,000 members, the potential
    u(3) = u(5) = 1/(1+5T)) and the 3x+d sublattice copy S_d(dy) = d S_1(y), against viewpoint_v001_check.json.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/viewpoint_v001_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
