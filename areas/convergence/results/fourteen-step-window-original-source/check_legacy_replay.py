"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B13-residual-R78-R94 migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - reviews/side_lane/r92_inverse_tree_check.py: the side-lane probe of R92: complete inverse trees at two concrete sources (r = 0 and r = 1) and the R25 inverse table, receipt reproduced byte for byte. The legacy checker check_deeper_window.py is not replayed: it pins a superseded hash of ../binary-return-exit-control/phi_exit_control_audit.json and the hashes of three notes, now edited READMEs.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['reviews/side_lane/r92_inverse_tree_check.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
