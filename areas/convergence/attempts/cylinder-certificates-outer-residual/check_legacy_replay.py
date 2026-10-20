"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/residual_cylinder_core.py: side-lane probe (2026-10-17): exact dynamic program over valuation cylinders for the descent rule, and with --merge the one-step merger rule; brute-force cross-check for m <= 14; actual-root descent counts at N = 6144 and 98304 (slowest 48 and 81 steps).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/residual_cylinder_core.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
