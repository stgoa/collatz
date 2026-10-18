# Lane 3 — independent Lean build audit of the C.1a external claim

**Status: IN PROGRESS, started 2026-10-18 17:40 -03. No result yet. Nothing
here is a premise.** Lane: branch `claude/lean-audit` (a separate Claude
session, authorized by the user to execute D7 items 2–4). This lane is
read-only with respect to `main` and `claude/sidekick`; it never pushes to
either. Results land in this directory and in the pull-request thread.

## What is being audited

`AxiomMath/CollatzPositiveDensity` at commit
`3a38bfbb70379e051b51155def1423846fab3a90`, the Lean artifact behind L3a
(Lau, `hexagon:2610.00249v1`, refining Mazur). Claimed in
`Challenge/Basic.lean`: for `X >= 2^2^2^2^87640`, at least
`X / 2^2^2^87640` integers `n < X` reach 1 within `floor(10.46 log n)`
ordinary steps; variants for odd starts, for targets coprime to 6, and for
targets `t` with `3` not dividing `t`.

## Facts established before building

- **Provenance.** The Hexagon page states that AxiomProver "autonomously
  produced the mathematics in this paper and formalized it in Lean"; Hexagon
  is an archive for LLM-assisted mathematics launched in August 2026;
  ProofAtlas describes itself as "AI agents working together on new
  mathematics". This is not a reason to reject the claim. It is the reason
  to build it rather than read it.
- **Toolchain.** `lean-toolchain` pins `leanprover/lean4:v4.35.0-rc2`, a
  release candidate. `lake-manifest.json` pins Mathlib
  `065356127b1dc0016f66b7283ce0ce2c4055aa55` (input rev `v4.35.0-rc2`) plus
  the standard Mathlib dependency set (batteries, aesop, Qq, ProofWidgets,
  import-graph, LeanSearchClient, plausible, Cli).
- **CI.** `.github/workflows/lean.yml` runs `leanprover/lean-action@v1` on
  push to `main`; six green runs through 2026-10-15. The workflow file has
  no `sorry`/axiom check and no comparator step. A library with `sorry`
  still builds green, so CI status is not evidence of a complete proof.
- **Layout.** No `lakefile.lean` at the root (HTTP 404), so the lakefile is
  presumably TOML (declarative). Roughly 500 `.lean` files under
  `CollatzPosDens/`. `Solution/Basic.lean` imports
  `CollatzPosDens.Main.{Main, MainJoint, EndpointJoint, EndpointNotThreeDvd}`.
  `Challenge/Basic.lean` has `sorry` bodies by design.
- **Kernel soundness bug #14576** (fixed 2026-07-28 by lean4 PR #14577,
  merge commit `a39eab69e1eee9ad38f4efe507907b1026a77808`, after an
  AI-assisted Collatz "disproof" exploited it). Checked mechanically with the
  GitHub compare API: tag `v4.35.0-rc2` (2026-09-16) is 363 commits ahead of
  that merge commit and 0 behind, so the pinned toolchain **contains the fix**.
- **CI duration.** In the green run on the pinned commit (run 38659218428),
  the `leanprover/lean-action@v1` step lasted 88 seconds (00:18:47 to
  00:20:15 UTC). That is far too short to compile a ~500-file
  Mathlib-dependent library from source. The job log
  (`receipts/ci_run_38659218428.log`) shows why: lean-action ran with
  `use-github-cache: true` and restored a ~2.1 GB Actions cache
  (`Cache hit for restore-key: lake-Linux-X64-…`) before `lake build`, so the
  run reused previously built artifacts rather than compiling the pinned
  commit from source; it also ran with `nanoda-allow-sorry: true`. CI status
  therefore certifies little here. The from-source build below is the test.
- **Comparator.** The repo ships `Comparator/comparator.json`: challenge
  module `Challenge.Basic`, solution module `Solution.Basic`, exactly the
  four theorem names, permitted axioms `propext`, `Quot.sound`,
  `Classical.choice`, `enable_nanoda: true`. The README claims the repo "has
  been locally verified with the comparator"; this lane replays that claim.
- **`Attr.lean`** declares a tag attribute `collatz_pos_dens` whose `add`
  handler is `pure ()`; it stores nothing and executes nothing else.

## Pre-build source audit (done 17:51 -03, host clone at the pinned commit)

- Tree: 743 `.lean` files (738 under `CollatzPosDens/`), 75,690 lines.
  `lakefile.toml` is declarative; there is no `lakefile.lean`. The library
  `CollatzPosDens` is the default target; `Challenge` and `Solution` are
  separate `lean_lib`s, and the lakefile comment says the comparator builds
  both itself.
- SHA-256 of pinned sources (`receipts/pinned_source_hashes.txt`):
  `lean-toolchain` 8dc8d6f5…, `lake-manifest.json` 7a7828b6…,
  `lakefile.toml` 70a5a20b…, `Challenge/Basic.lean` e3e828be…,
  `Solution/Basic.lean` 2b0fdaab….
- Whole-tree grep, `.lake` excluded (`receipts/grep_constructs.txt`):
  `sorry` 5 hits, all accounted for: 4 are the four challenge statements in
  `Challenge/Basic.lean`, 1 is a comment in `lakefile.toml`. `admit` 0,
  `native_decide` 0, `implemented_by` 0, `@[extern` 0, `unsafe` 0, `axiom` 0,
  `IO.Process` 0, `run_cmd` 0, `#eval` 0, `ofReduceBool` 0, `opaque … :=` 0.
  One `initialize`: `CollatzPosDens/Attr.lean:20`, a
  `Lean.registerBuiltinAttribute` call (an attribute registration; read in
  full before building).
- A textually sorry-free library is necessary, not sufficient: the build must
  succeed and `#print axioms` must report only the standard axioms.

## Method (D7 items 2–4)

1. Clone at the pinned commit into an isolated directory outside every
   checkout (`~/lean-audit/src/`), with an isolated `HOME`/`ELAN_HOME`
   (`~/lean-audit/home/`) and an environment scrubbed of credentials
   (`env -i`). The Docker daemon is not running on this machine, so
   isolation is directory- and environment-level, not a container. This is
   recorded as a limitation of item 3.
2. Before invoking `lake`: inspect the lakefile; grep the whole tree for
   `sorry`, `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`,
   `axiom`, `initialize`, `IO.Process`, `run_cmd`, `#eval`, `ofReduceBool`.
   Stop if a `lakefile.lean` or a code-executing construct appears outside
   ordinary proof text.
3. Install elan, the pinned toolchain, `lake exe cache get`, then
   `lake build`, in the background, with timings and logs kept.
4. A scratch file importing the solution runs `#print axioms` on each of the
   four theorems. Statement match is tested as
   `example : <type of the Challenge theorem> := Solution.<theorem>` for each,
   so that the solution is accepted against the challenge's own statement.
5. Receipts (logs, hashes of the pinned sources, axiom output, grep output)
   are stored here.

## What this will and will not establish

- A clean build, with only `propext`, `Classical.choice` and `Quot.sound`
  reported for all four theorems, on a toolchain containing the #14577 fix,
  makes the four **Lean statements** theorems, subject to Lean's trusted
  base. It does not verify the paper's prose, and it says nothing about
  C.2a: route C would still need density zero of the non-absorbing starts.
- `sorryAx`, a custom axiom, `native_decide`, a failed build or a statement
  mismatch means L3a stays unverified and must not become a premise.

## Request to the other lanes

None. Per D7, accepted at main `44a2745`, C.1a should not be promoted to a
premise until this lands. No action is required from `main` or from
`claude/sidekick`.

## Housekeeping note for main

At about 17:12 -03 this lane accidentally terminated main's running
`verify_all.py --cpp --transfer-controls` process (PID 18053, log
`/private/tmp/collatz_phase6_linear_density_gate.log`) while cleaning up
its own replay. Nothing in main's checkout was modified. That gate run needs
to be repeated. Apologies.

## Results (2026-10-18, 18:39 -03; comparator replay still running)

**Environment actually used.** Docker container `leanaudit` (Rancher
Desktop VM, linux/aarch64, 4 CPUs via cpuset, 7 GB memory limit),
`ubuntu:24.04`, elan 4.2.4, `Lean (version 4.35.0-rc2,
aarch64-unknown-linux-gnu, commit 11acb17ec6b07a8f9e9173e6845197929540936b,
Release)`, Lake 5.0.0. Project at the pinned commit, Mathlib cache fetched
with `lake exe cache get` (8,536 Mathlib `.olean`s). Toolchain and project
were copied onto the container's own filesystem after the macOS bind mount
proved I/O-starved and produced spurious `EMFILE`/`ENOENT` errors; the
final run used no bind-mounted files.

**1. From-source build: PASS.** `lake build Challenge Solution` compiled the
four-theorem closure, which is 737 of the 738 library modules (74,803
lines), from source: `Build completed successfully (4107 jobs)`, wall time
6 min 02 s, zero errors, zero `declaration uses 'sorry'` warnings
(`receipts/lake_build_solution.log`).

**2. Axioms: PASS.** `#print axioms` in a fresh `lean` process importing
`Solution.Basic` (`receipts/audit_solution.out`), for each of the four
theorems:

```
positive_density_collatz_reaches_one                               [propext, Classical.choice, Quot.sound]
positive_density_collatz_and_collatzAccel_reaches_one              [propext, Classical.choice, Quot.sound]
positive_density_collatz_and_collatzAccel_reaches_of_coprime_six   [propext, Classical.choice, Quot.sound]
positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd [propext, Classical.choice, Quot.sound]
```

No `sorryAx`, no custom axiom, no `native_decide` (`Lean.ofReduceBool`).

**3. Statement match: PASS.** With `set_option pp.all true`, the four
theorem types and the seven definitions they use (`collatz`, `ReachWithin`,
`collatzDensity`, `collatzDensityThreshold`, `collatzAccel`,
`collatzDensityDep`, `collatzDensityThresholdDep`) were printed from the
human-written `Challenge.Basic` and from `Solution.Basic` and diffed
(`receipts/audit_challenge.out`, `receipts/audit_solution.out`): 445
lines, identical. The only differing lines in the raw outputs are the
challenge's own `sorryAx` entries, as expected.

**4. Kernel-fix containment: PASS** (see facts above): the toolchain
contains lean4 #14577.

**5. Independent kernel replay (`lake comparator` with the authors'
`Comparator/comparator.json`, which enables nanoda; then `--paranoid`, which
also runs `leanchecker-paranoid`, `lean4lean`, `con-leche`, `con-ron`; then
`lake check --paranoid`): running at the time of this commit.** Note on
scope: the comparator's own `bwrap` sandbox cannot create user namespaces
inside an unprivileged Docker container, so it runs with
`--inadvisably-no-sandbox`; the Docker container is the sandbox, and the
source audit above found no code-executing construct in the project (its
lakefile is TOML; the only metaprogram is a no-op attribute). Record this
when citing the comparator result.

### Verdict so far

The four Lean statements in `Challenge/Basic.lean` are theorems of
Lean + Mathlib, under the standard axioms, as checked by Lean's own kernel
in a from-source build on this machine. In particular, the statement the
route map calls C.1a — for every fixed target `t` with `3 ∤ t`, a positive
proportion of integers reach `t` (with tower-sized constants and a
logarithmic clock) — has a machine-checked proof at the pinned commit,
subject to Lean's trusted base and the trusted-base remark below.

What this does **not** establish: anything about the paper's prose, the
transfer of the statement to `3x+d`, or C.2a. Route C would still need
density zero of the non-absorbing starts, which remains open. The theorem
is d-sensitive in the right way (its `d=5` analogue is false), so it is the
first input in this programme that is not a transferable local identity.
