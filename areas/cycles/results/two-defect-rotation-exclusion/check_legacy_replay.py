"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/cycle_spectrum/C011/check_rotation_defects.py: main-lane checker and receipt (27,646 rotations, 1,481,154 word positions, 192 two-defect rotations with 384 oriented arc identities, 108 eligible actual cycles of which 22 have unit-amplitude two-defect rotations; 51 cancellation-family examples ...;
  - experiments/cycle_spectrum/C011/check_coupled_defects.py: main-lane check of the q = 97, 233, 359 coupled controls.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/cycle_spectrum/C011/check_rotation_defects.py', 'experiments/cycle_spectrum/C011/check_coupled_defects.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
