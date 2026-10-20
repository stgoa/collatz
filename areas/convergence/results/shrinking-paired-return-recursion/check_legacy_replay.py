"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/second_return/check_paired_return.py: the legacy constructor and checker (4096 w values, 72 terminal cylinders, 56 recursive integer cases through depth 64, 65 exponent lifts, eight actual Mersenne bridges, the a = 39 supplied-current conversion with a 5000-step cap on the lower path);
  - reviews/side_lane/batch_64fff1d_check.py: side-lane probe (Claude side lane, 2026-10-17) of concrete identities in R30, R31 (bounded-runs-exclude-finite-label-potentials) and R32 (merger-catalogue-scope).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/second_return/check_paired_return.py', 'reviews/side_lane/batch_64fff1d_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
