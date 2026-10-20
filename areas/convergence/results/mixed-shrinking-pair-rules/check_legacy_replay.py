"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/paired_completion/check_mixed_pairs.py: the legacy constructor and checker (4096 domain inputs, 510 complete mixed cylinders, 28 long words through depth 64, four actual Mersenne bridges, exact merger clocks, full source multiplicity ...;
  - reviews/side_lane/batch_r33_r36_check.py: side-lane probe (Claude side lane, 2026-10-17) of R33, R34 (decreasing-inverse-ancestry) and R36 (missing-one-mod-8-pair-domain).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/paired_completion/check_mixed_pairs.py', 'reviews/side_lane/batch_r33_r36_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
