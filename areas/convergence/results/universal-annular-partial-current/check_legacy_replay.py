"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/annular_construction/arithmetic/check_arithmetic_reductions.py: the legacy checker of the catalogue (66 cases: every multiple of 8 through 512, and 768, 1536), of the root-collapse norm of annular-root-collapse-contraction and of the outer profile of outer-profile-closure-obstruction (cutoffs 8, 24, 96, 128, depths 0–4 ...;
  - experiments/annular_construction/arithmetic/combined_partial_current.py: the legacy reusable constructor build_combined_partial_current(N), returning the full current and residual, audited at N = 8, 72, 96, 160, 168, 384, 768, 6144.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/annular_construction/arithmetic/check_arithmetic_reductions.py', 'experiments/annular_construction/arithmetic/combined_partial_current.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
