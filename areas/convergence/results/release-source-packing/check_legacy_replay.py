"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/release_packing/release_packing.py: the legacy extended constructor build_extended_partial_current(N) and its audit (every multiple of 8 through 1024 and 6144: every source, disjoint capacity against the old constructor, full divergence, and all 27 boundary phases of the floor counts);
  - reviews/side_lane/release_families_check.py: side-lane probe (Claude side lane, 2026-10-17): rebuilds both families from their statements with its own A_N.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/release_packing/release_packing.py', 'reviews/side_lane/release_families_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
