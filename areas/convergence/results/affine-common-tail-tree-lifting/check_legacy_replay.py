"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/annular_construction/components/affine_template_compiler.py: the legacy compiler; checks both compiled identities at arbitrary-size integer parameters, the linear band bounds on selected scales through 64^20, all 45 progression-capacity checks, and every allowed cutoff from 8 through 4096 for the summed two-class family;
  - experiments/annular_construction/components/check_annular_components.py: the capped incremental constructor and its audit driver (the six component diagnostics, the finite work witnesses and the stored A_96 and A_168 currents)..
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/annular_construction/components/affine_template_compiler.py', 'experiments/annular_construction/components/check_annular_components.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
