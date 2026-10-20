"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B13-residual-R78-R94 migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/batch_r81_r83_check.py: the side-lane probe of R81 and R83: 3,301 lifts of the R80 cell, 400 random merger cells with binary minimality, receipt reproduced byte for byte. The legacy checker check_history_lifting.py was not replayed when this file was written (it pins the hash of this node's note, now an edited README, and the replay did not yet restore rewritten notes from git); it is replayed now (below).
  - experiments/residual_progress/history_lifting/check_history_lifting.py: the legacy compiler, checker and receipt: 18 specifications, 189 lifts, 592 memberships, 191 native plans, 62 old-phase records with 38 genuine high requests, 19 rejections, three supplied outputs (b = 3849, 2838201 ... (added at the B18-replay-revival migration).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/batch_r81_r83_check.py', 'experiments/residual_progress/history_lifting/check_history_lifting.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
