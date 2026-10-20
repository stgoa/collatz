"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B12-residual-R61-R77 migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/batch_r75_r77_check.py: the side-lane probe of R75 and R77 (growth bound, 37-return threshold, spacing lemma, fixed-word copy counts), placed in reviews/side_lane/ beside fibre_count_check.py, whose committed receipt must be reproduced byte for byte. The legacy checker experiments/residual_progress/itinerary_complexity/check_itinerary_complexity.py was not replayed when this file was written (it pins the hashes of two notes that are now edited READMEs, and the replay did not yet restore rewritten notes from git); it is replayed now (below).
  - experiments/residual_progress/itinerary_complexity/check_itinerary_complexity.py: the legacy implementation, checker and receipt: 62 affine words, 186 lifts, 630 copy cases including 90 zero-copy cases, 12 R67/R74 boundary cases, 32 finite positive traces, 11242 factor repeats including 524 overlapping ones, 45 exact threshold cases ... (added at the B18-replay-revival migration).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/batch_r75_r77_check.py', 'experiments/residual_progress/itinerary_complexity/check_itinerary_complexity.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
