"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B13-residual-R78-R94 migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/r93_r94_check.py: the side-lane probe of R93, R94 and this probe (from ../../results/two-source-normalisation-first-departure/): the r = 4 and r = 8 paths S^78(Q) = y and S^126(Q) = y, the ray cutoffs and all 23 and 37 maximal endpoints above Q, receipt reproduced byte for byte. The legacy checker check_later_target_probe.py is not replayed: it pins the hashes of this note and of ../../results/history-beyond-prescribed-growth/README.md (legacy NATIVE_GROWTH_ESCAPE.md), now edited READMEs.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/r93_r94_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
