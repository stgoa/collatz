"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B13-residual-R78-R94 migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/batch_r84_r85_check.py: the side-lane probe of R84 and R85 (from ../later-target-twenty-step-descent/): 24 brute-force instances of the clock barrier, receipt reproduced byte for byte. The legacy checker check_history_barrier.py was not replayed when this file was written (it pins the hash of this node's note, now an edited README, and the replay did not yet restore rewritten notes from git); it is replayed now (below).
  - experiments/residual_progress/history_cover_scope/check_history_barrier.py: the legacy constructor, checker and receipt: 62 quotient and 126 ordinary domains with 3911/16008 origin instances, 196 critical and 60 H17 CRT cells, 200 inverse words with ray indices through 64, 15 equality spines, 1560 ordinary-word attempts ... (added at the B18-replay-revival migration).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/batch_r84_r85_check.py', 'experiments/residual_progress/history_cover_scope/check_history_barrier.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
