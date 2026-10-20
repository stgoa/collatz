---
id: linear-form-gap-own-proof
kind: question
title: Can the replayed linear-form gap EXT-1 be proved in this repository?
status: open
claim: >
  Give a proof inside this repository (a complete written proof, and ideally a Lean proof under the pinned
  toolchain with the standard axioms only) of the effective gap used as EXT-1: for all natural numbers k, L
  with 0 < k and 3^k < 2^L, 2^L ≤ 2^172·k^341·(2^L − 3^k). Today it is the external theorem
  Collatz.gap_all of mmusson/collatz, replayed here under its own toolchain (kernel-checked, standard axioms)
  but not reviewed line by line and not part of this repository's Lean development; or a weaker explicit
  gap of the same shape that the dependent results can use.
created: 2026-10-19
tags: [cycles, linear-forms, lean, external-input, frontier]
---

# Can the replayed linear-form gap EXT-1 be proved in this repository?

## Question

EXT-1 is the inequality `2^L ≤ 2^172·k^341·(2^L − 3^k)` for `0 < k` and `3^k < 2^L`: an explicit lower bound for the gap between a power of 2 and a smaller power of 3. It enters this repository as the external Lean theorem `Collatz.gap_all` ([`musson-collatz-gap-all`](../../../sources/musson-collatz-gap-all.md)). The Lean lane replayed it on 2026-10-19: the external development built under its own toolchain (`leanprover/lean4:v4.34.0-rc2`, not this repository's `v4.35.0-rc2`) and `#print axioms` showed only the standard axioms, but the proofs were not reviewed line by line and nothing of them is copied here. Theorems in [`lean/CycleSpectrum.lean`](../../../lean/CycleSpectrum.lean) that use it take the inequality as an explicit hypothesis, so each application is a composition across two libraries on different toolchains, not a single Lean theorem.

The target is a proof that this repository owns: a complete written proof that can be reviewed, and a formal proof that the Lean files here can import, which would turn the hypothesis into a theorem. A different explicit gap `2^L ≤ 2^c·k^μ·(2^L − 3^k)` with other constants would also serve, if the dependent results are re-run with its constants.

## Why it matters

Every result that assumes EXT-1 is conditional on it, including three of the strongest results of the cycles area:
- [`three-mismatch-exclusion`](../results/three-mismatch-exclusion/README.md) (`ρ ≥ 4`), [`two-mismatch-exclusion-via-gap`](../results/two-mismatch-exclusion-via-gap/README.md) and [`mismatch-height-tradeoff`](../results/mismatch-height-tradeoff/README.md), formal given the gap;
- [`one-cycle-exclusion-via-gap`](../results/one-cycle-exclusion-via-gap.md), [`short-rotation-mismatch-growth`](../results/short-rotation-mismatch-growth/README.md), [`largest-letter-rho-reduction`](../results/largest-letter-rho-reduction.md), [`cycle-word-repeat-bound`](../results/cycle-word-repeat-bound/README.md) and [`shared-background-copies-via-gap`](../results/shared-background-copies-via-gap/README.md).

A proof here would remove EXT-1 from their "Rests on" column in [`MAP.md`](../../../MAP.md). The other external inputs of the applied forms (the period and minimum bounds) would remain.

## Known progress

- The external replay above, with its receipt [`lean/receipts/mmusson_gap_all.txt`](../../../lean/receipts/mmusson_gap_all.txt) and the Lean lane's unit-table row EXT-1 ([`archive/lean-lane/STATE.md`](../../../archive/lean-lane/STATE.md)).
- Some results were first proved from Matveev's bound ([`matveev-2000-linear-forms`](../../../sources/matveev-2000-linear-forms.md)) instead, e.g. [`two-defect-rotation-exclusion`](../results/two-defect-rotation-exclusion/README.md); that is a published input too, not a proof owned here.

## Suggested attacks

None recorded in the legacy material beyond the item itself, which was listed in the formalisation queue of the legacy frontier as "a self-contained proof of EXT-1 (currently replayed, not ours)". Re-deriving or porting the external proof to the pinned toolchain, with a line-by-line review, is the obvious route (speculation).

## History

New node at the B17 migration (Claude, Opus 5.5), from the formalisation-queue item of the legacy `docs/FRONTIER.md` §6 ([`archive/pre-migration-2026-10-20/docs/FRONTIER.md`](../../../archive/pre-migration-2026-10-20/docs/FRONTIER.md)), the EXT-1 row of the legacy `docs/CONVENTIONS.md` §5 and the EXT-1 row of the legacy `lean/STATE.md`, at commit `be73a66`. It was the only open target of the legacy frontier without a question node.
