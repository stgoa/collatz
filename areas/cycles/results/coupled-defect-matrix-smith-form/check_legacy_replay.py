"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/cycle_spectrum/C012/check_coupled_system.py: main-lane checker and receipt (all 27,646 nonidentity rotations of the 1,185 normalised cycles and 11 fixtures; selected determinants and minors);
  - experiments/cycle_spectrum/C012/check_shared_arcs.py: main-lane shared-arc checker and receipt (350 fixed-total backgrounds, 3,582 backgrounds with A < 2m, seven prime sets; 177,288 raw arrows, 173,349 rotations).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/cycle_spectrum/C012/check_coupled_system.py', 'experiments/cycle_spectrum/C012/check_shared_arcs.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
