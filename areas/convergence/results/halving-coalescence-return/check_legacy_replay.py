"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/residual_return/check_halving_return.py: the legacy constructor (selected-class test, finite bridge, logarithmic count, capacity-preserving conversion) and checker (8192 selected and 8192 complementary seeds below 65536, 1016 parameterized prefix cases, the profile at 512 cutoffs N = 8..4096 ...;
  - reviews/side_lane/coalescence_check.py: side-lane probe (Claude side lane, 2026-10-17): checks the identity and the coverage claim, then runs an exact cylinder dynamic program with descent, merger and halving certificates (see cylinder-certificates-outer-residual).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/residual_return/check_halving_return.py', 'reviews/side_lane/coalescence_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
