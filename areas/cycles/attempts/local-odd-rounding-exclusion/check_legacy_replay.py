"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/cycle_spectrum/C010/check_integer_gaps.py: main-lane checker and receipt (2,459 source cycles, 1,185 normalised, 52 ordered cases, 474 adjacent gap equations, 7,022 circular pair bounds);
  - reviews/side_lane/c010b_gap_lattice_check.py: side-lane checks of Lean units C010-b and C010-c;
  - reviews/side_lane/c010c_any_arrangement_check.py: side-lane checks of Lean units C010-b and C010-c.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/cycle_spectrum/C010/check_integer_gaps.py', 'reviews/side_lane/c010b_gap_lattice_check.py', 'reviews/side_lane/c010c_any_arrangement_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
