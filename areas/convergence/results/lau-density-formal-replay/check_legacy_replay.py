"""Replay this node's unmodified legacy check in a temporary copy of the legacy layout.

Written at the B14-convergence-phase6 migration (on tools/legacy_replay.py). The legacy test reads
StatementAudit.lean from its own folder, and that file moved to lean/audit/phase6/ (Lean files live only
under lean/), so it no longer runs in this folder; tools/legacy_replay.py rebuilds the pre-migration tree
in a temporary directory and runs it there, requiring exit 0 and every file byte-identical afterwards.
Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/phase6/linear_density_audit/test_formal_replay.py: eleven receipt-integrity tests of the
    stage runner run_formal_replay.py (stale-PASS invalidation, Popen failure, missing, failed or mutated
    predecessors, mandatory chain edges, exact axiom-report parsing, disallowed and lookalike axioms, legacy
    sealing, conflicting object rebinding). No Lean, network or live replay stage is executed; this checks
    the runner's fail-closed logic, not the external Lean development.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

SCRIPTS = ['experiments/phase6/linear_density_audit/test_formal_replay.py']

if __name__ == "__main__":
    sys.exit(legacy_replay.main(SCRIPTS))
