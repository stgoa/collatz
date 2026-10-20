"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B13-residual-R78-R94 migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/batch_r78_r80_check.py: the side-lane probe of R78-R80 (from ../high-smaller-origin-history/): the R79 identity Y(U(b)) = (729/512) Y(b) and the return count on 3,000 seeds, receipt reproduced byte for byte. The legacy checker check_nine_growth.py was not replayed when this file was written (it pins the hash of this node's note, now an edited README, and the replay did not yet restore rewritten notes from git); it is replayed now (below).
  - experiments/residual_progress/native_nine_growth/check_nine_growth.py: the legacy implementation, checker and receipt: 123 cylinders, 216 exit-phase cases, 27 full H17 comparisons, 24 full returns, 54 inverse undos, 383 local bounds, 16 rejections, complete failed-current tables at r = 1, 2 (78/134 rows) (added at the B18-replay-revival migration).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/batch_r78_r80_check.py', 'experiments/residual_progress/native_nine_growth/check_nine_growth.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
