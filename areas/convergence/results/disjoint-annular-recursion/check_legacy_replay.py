"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/current_construction/recursive/check_annular_recursion.py: derives the residue table from inverse source arithmetic and compares the whole annular measure with the packet constructor at every multiple of 8 through 512 and at 1000 and 4096 (66 cases, expanded cutoffs up to 262144), with bands, both source components ...
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/current_construction/recursive/check_annular_recursion.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
