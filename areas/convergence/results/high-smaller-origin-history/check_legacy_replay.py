"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B13-residual-R78-R94 migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/batch_r78_r80_check.py: the side-lane probe of R78-R80: the R80 family on 30 cases and the complete forward closure of the anchor 11547, receipt reproduced byte for byte. The legacy checker check_native_history.py was not replayed when this file was written (it pins the hash of this node's note, now an edited README, and the replay did not yet restore rewritten notes from git); it is replayed now (below).
  - experiments/residual_progress/native_history/check_native_history.py: the legacy constructor, checker, receipt and the 4892-state anchor table: all anchor edges, 54 family/native plans, 54 W5-frontier variants, 54 actual R44/R52 failures, 88 base inverse words, 18 varied words, 11 rejections ... (added at the B18-replay-revival migration).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/batch_r78_r80_check.py', 'experiments/residual_progress/native_history/check_native_history.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
