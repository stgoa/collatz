"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/cycle_spectrum/C005/check_mechanical_blocks.py: main-lane rotation-block checker and receipt; check_order.py, order_audit.json: main-lane order checker and receipt (check_mechanical_blocks.py pins the hashes of both);
  - experiments/cycle_spectrum/C005/check_order.py: legacy check;
  - reviews/side_lane/c005_c006_order_check.py: side-lane REFEREE check of C005 and C006 (run with arguments ../../experiments/cycle_spectrum/C001/actual_cycles.json from its legacy folder).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/cycle_spectrum/C005/check_mechanical_blocks.py', 'experiments/cycle_spectrum/C005/check_order.py', 'reviews/side_lane/c005_c006_order_check.py']
ARGS = {'reviews/side_lane/c005_c006_order_check.py': ['../../experiments/cycle_spectrum/C001/actual_cycles.json']}

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS, args=ARGS))
