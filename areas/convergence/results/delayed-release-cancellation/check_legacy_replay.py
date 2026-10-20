"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/release/check_release.py: the legacy checker (both complete first-release components; divergence and actual source capacity for 22 parameter families with three representatives each and two required-ray representatives; the canonical-parameter dichotomy for 2 <= h <= 64 ...;
  - reviews/side_lane/delayed_release_check.py: side-lane probe (Claude side lane, 2026-10-17): rebuilds the construction from its statement with its own A_N.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/release/check_release.py', 'reviews/side_lane/delayed_release_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
