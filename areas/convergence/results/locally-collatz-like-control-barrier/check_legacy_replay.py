"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B18-replay-revival migration (on tools/legacy_replay.py). The legacy scripts load
sibling modules and data by their pre-migration paths, so they no longer run in this folder;
tools/legacy_replay.py rebuilds the pre-migration tree in a temporary directory and runs them there,
requiring exit 0 and every file byte-identical afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/packet_currents/negative_controls/affine_controls.py: the controls of this node and the certificate checker (python3 <this folder>/affine_controls.py --check CERT.json);
  - experiments/packet_currents/negative_controls/reduction_audit.py: the independent audit of R2–R4 and the minimality checks (right-aligned-reduction-independent-checks, exact-current-minimality);
  - experiments/packet_currents/negative_controls/check_review_scope.py: the main lane's checker for the PR1 review's counterexamples (exact-current-minimality).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/packet_currents/negative_controls/affine_controls.py', 'experiments/packet_currents/negative_controls/reduction_audit.py', 'experiments/packet_currents/negative_controls/check_review_scope.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
