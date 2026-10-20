"""Replay this node's unmodified legacy check in a temporary copy of the legacy layout.

Written at the B14-convergence-phase6 migration (on tools/legacy_replay.py). The legacy checker loads two
frozen modules by their pre-migration paths, so it no longer runs in this folder; tools/legacy_replay.py
rebuilds the pre-migration tree in a temporary directory and runs it there, requiring exit 0 and every
file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/phase6/stopping_calibration/check_calibration.py: the exact S.1 constructor calibration.py
    against calibration_audit.json (parity words and lifts, binomial tail bounds, cutoff comparisons,
    parameter examples, raw-clock identities, half-descent conversions, the W5 pullback on 1,024 inputs,
    rejection cases) and the pinned hashes of the frozen R25 normal_form.py and R37 tripling.py.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/phase6/stopping_calibration/check_calibration.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
