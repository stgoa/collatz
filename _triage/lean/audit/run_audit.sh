#!/bin/bash
# Lane-3 audit driver. Run on the host after the Mathlib cache is present in
# ~/lean-audit/src/CollatzPositiveDensity/.lake (host setup.log: SETUP_DONE)
# and the container has its toolchain (container_prep.log: CONTAINER_PREP_DONE).
# Lake 5 has no -j flag: parallelism follows the CPUs visible in the container,
# so limit it with `docker update --cpuset-cpus`.
set -u
AUDIT="$HOME/lean-audit"; LOGS="$AUDIT/logs"; REC="$AUDIT/receipts"
# The tree was copied from the bind mount (/work, I/O-starved) to the container
# filesystem at /build/CollatzPositiveDensity; all lake commands run there.
W=/build/CollatzPositiveDensity
# The elan home was also copied off the bind mount, to /opt/.elan (the mount
# produced spurious EMFILE/ENOENT errors while 8 lean processes imported the
# toolchain's oleans in parallel).
# The toolchain's own bin/ is on PATH because `lake comparator` looks up the
# bundled external checkers (nanoda_bin, lean4lean, leanchecker-paranoid,
# con-leche, con-ron, leanexport) by name.
TB=/opt/.elan/toolchains/leanprover--lean4---v4.35.0-rc2/bin
run() { docker exec -w "$W" -e ELAN_HOME=/opt/.elan -e PATH="$TB:/opt/.elan/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" -e HOME=/root -e LANG=C.UTF-8 leanaudit "$@"; }

docker exec leanaudit mkdir -p /audit
docker cp "$AUDIT/bin/AuditSolution.lean" leanaudit:/audit/AuditSolution.lean
docker cp "$AUDIT/bin/AuditChallenge.lean" leanaudit:/audit/AuditChallenge.lean

echo "=== versions $(date '+%F %T %z') ==="
run lean --version; run lake --version; run git rev-parse HEAD; run nproc; run free -m | head -2

echo "=== lake build Challenge Solution  $(date '+%T') ==="
( time run lake build Challenge Solution ) > "$LOGS/lake_build_solution.log" 2>&1
BUILD_EXIT=$?
tail -6 "$LOGS/lake_build_solution.log"; echo "build exit=$BUILD_EXIT  $(date '+%T')"
echo "error lines: $(grep -c -i 'error' "$LOGS/lake_build_solution.log")"
echo "sorry warnings: $(grep -c "declaration uses 'sorry'" "$LOGS/lake_build_solution.log")"
if [ "$BUILD_EXIT" -ne 0 ]; then echo "BUILD FAILED; stopping before the checks"; echo "AUDIT_STOPPED $(date '+%T')"; exit 1; fi

echo "=== axioms + statements, solution side  $(date '+%T') ==="
run lake env lean /audit/AuditSolution.lean > "$REC/audit_solution.out" 2>&1; echo "exit=$?"
grep -n "depends on axioms" "$REC/audit_solution.out"

echo "=== axioms + statements, challenge side ==="
run lake env lean /audit/AuditChallenge.lean > "$REC/audit_challenge.out" 2>&1; echo "exit=$?"
grep -n "depends on axioms" "$REC/audit_challenge.out"

echo "=== diff of statements and definitions (axiom lines removed) ==="
diff <(grep -v "depends on axioms" "$REC/audit_challenge.out") <(grep -v "depends on axioms" "$REC/audit_solution.out") > "$REC/statement_diff.txt"
echo "diff exit=$? ($(wc -l < "$REC/statement_diff.txt" | tr -d ' ') lines)"

echo "=== lake comparator, sandboxed (bwrap), --paranoid  $(date '+%T') ==="
( time run lake comparator --config Comparator/comparator.json --paranoid ) > "$LOGS/comparator_sandboxed.log" 2>&1
CMP1=$?
tail -15 "$LOGS/comparator_sandboxed.log"; echo "comparator (sandboxed) exit=$CMP1  $(date '+%T')"
if [ "$CMP1" -ne 0 ]; then
  echo "=== lake comparator, --inadvisably-no-sandbox --paranoid (container is the sandbox)  $(date '+%T') ==="
  ( time run lake comparator --config Comparator/comparator.json --paranoid --inadvisably-no-sandbox ) > "$LOGS/comparator_nosandbox.log" 2>&1
  CMP2=$?
  tail -25 "$LOGS/comparator_nosandbox.log"; echo "comparator (no sandbox) exit=$CMP2  $(date '+%T')"
fi

echo "AUDIT_DONE $(date '+%T')"
