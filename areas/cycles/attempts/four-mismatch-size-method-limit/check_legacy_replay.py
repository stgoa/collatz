"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/s8_multirotation_check.py: side-lane probe (about 20 s, no receipt), feed update 13:36: the survivor words against every rotation by a convergent denominator of h^(−1)/m (times 1, 2, 3) with at most 60,000 mismatches; all margins positive. It did not include the rotation 2h;
  - reviews/side_lane/s8_multiple_rotations.py: the counterexample check of feed 13:44 (about 30-40 s, no receipt): the survivor words against the rotations by k·h, k = ±1..±12; the rotation 2h fails by 193,000 bits (ℓ = ℓ*), 209,000 (ℓ = 71) and 287,000 (ℓ = 100) at m = 10^6, and 3h, 4h, 5h, 7h ...
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/s8_multirotation_check.py', 'reviews/side_lane/s8_multiple_rotations.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
