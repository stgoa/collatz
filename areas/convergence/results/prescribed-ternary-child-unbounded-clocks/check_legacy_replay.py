"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B13-residual-R78-R94 migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/r93_r94_check.py: the side-lane probe of R93, R94 and the later-target probe (from ../two-source-normalisation-first-departure/): the centres, shadows, 112-word certificate, 39 cylinders and 156 replayed pairs, receipt reproduced byte for byte. The legacy checker check_child_catalogue_scope.py is not replayed: it pins the hash of this node's note, now an edited README.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/r93_r94_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
