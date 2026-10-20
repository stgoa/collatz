"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/s7_three_mismatch.py: side-lane probe (about 15-25 s): Part 1 scans the conditions W, A, P, F for every m ≤ 10^7 at the worst case ℓ = ℓ*(m) and finds m0 = 452,695; Part 2 checks the q-independent steps on 616 actual 3x+q cycles;
  - reviews/side_lane/s7_stress_rational.py: the independent review agent's stress test, as a side-lane probe (no receipt) (run with arguments 3 14 from its legacy folder).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/s7_three_mismatch.py', 'reviews/side_lane/s7_stress_rational.py']
ARGS = {'reviews/side_lane/s7_stress_rational.py': ['3', '14']}

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS, args=ARGS))
