"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/cycle_spectrum/C006/check_order_rigidity.py: main-lane finite checker, receipt and root replay record;
  - reviews/side_lane/c006b_erun_check.py: side-lane independent checks of Lean units R71-d and C006-b to C006-f;
  - reviews/side_lane/c006c_g4_check.py: side-lane independent checks of Lean units R71-d and C006-b to C006-f;
  - reviews/side_lane/c006d_g2_check.py: side-lane independent checks of Lean units R71-d and C006-b to C006-f;
  - reviews/side_lane/c006e_cc_check.py: side-lane independent checks of Lean units R71-d and C006-b to C006-f;
  - reviews/side_lane/c006f_order_word_check.py: side-lane independent checks of Lean units R71-d and C006-b to C006-f.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/cycle_spectrum/C006/check_order_rigidity.py', 'reviews/side_lane/c006b_erun_check.py', 'reviews/side_lane/c006c_g4_check.py', 'reviews/side_lane/c006d_g2_check.py', 'reviews/side_lane/c006e_cc_check.py', 'reviews/side_lane/c006f_order_word_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
