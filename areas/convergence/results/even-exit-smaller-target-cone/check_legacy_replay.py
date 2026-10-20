"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B13-residual-R78-R94 migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/r86_even_exit_check.py: the side-lane probe of R86: 1,152 CRT cases of the raw-target cone, receipt reproduced byte for byte. The legacy checker check_even_exit_history.py was not replayed when this file was written (it pins the hash of this node's note, now an edited README, and the replay did not yet restore rewritten notes from git); it is replayed now (below).
  - experiments/residual_progress/even_exit_history/check_even_exit_history.py: the legacy constructor, checker and receipt: 640 arithmetic cells, 50 full plans, 256 minimal-H cells through H = 256, D = 32, 72 valid CRT memberships in 7680 attempts, 34 old-seventeen progression cases, 28 rejection controls ... (added at the B18-replay-revival migration).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/r86_even_exit_check.py', 'experiments/residual_progress/even_exit_history/check_even_exit_history.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
