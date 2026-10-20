"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B12-residual-R61-R77 migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/mixed_exit/check_mixed_exit.py: the exit parameters, next-block plans, re-entries, repeated currents, families, maxima and rejections, against mixed_exit_audit.json.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/residual_progress/mixed_exit/check_mixed_exit.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
