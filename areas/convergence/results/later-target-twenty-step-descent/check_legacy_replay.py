"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B13-residual-R78-R94 migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/batch_r84_r85_check.py: the side-lane probe of R84 and R85: 3,000 thirteen-arrow prefixes and 300 sharp twentieth-step descents, receipt reproduced byte for byte. The legacy checker check_history_transition.py was not replayed when this file was written (it pins the hash of this node's note, now an edited README, and the replay did not yet restore rewritten notes from git); it is replayed now (below).
  - experiments/residual_progress/history_transition/check_history_transition.py: the legacy constructor, checker and receipt: 1024 full plans, 70 template instances covering all fourteen words, 144 progression cases, 20 sharp cases, 66 actual old failures, 26 rejections, three supplied outputs outside R81 with 148/153/172 rows (added at the B18-replay-revival migration).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/batch_r84_r85_check.py', 'experiments/residual_progress/history_transition/check_history_transition.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
