---
id: mechanical-cycles-high-rational-controls
kind: result
title: "Mechanical cycles give rational 3x+1 cycles and integer 3x+d cycles arbitrarily far above the absorber, with d varying"
status: formal
claim: >
  Raw odd-only clock, no absorption. For every k >= 1 let A be the bit length of 3^k, so 3^k < 2^A < 2 3^k. For
  every phase l < k, every state of the positive rational odd-only 3x+1 cycle of the mechanical word mech(A,k,l)
  exceeds k/6 (6C > kD), and the reduced integer cycle of 3x+q, q = 2^(A/g) - 3^(k/g) its reduced denominator, has
  every state n_i > kq/6. For every k >= 3 the reduced denominator exceeds 1 (it equals 1 exactly at k = 1, 2). So
  for any C > 0 and k > 6C there is a rational 3x+1 cycle with all states above C and an integer 3x+d cycle with all
  states above C d, d > 1, but d varies with k: this gives no high cycles for a fixed d, no uniform constant over
  all d, and does not show that these maps pass or fail any finite base test.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [mechanical-word-exact-denominator]
lean:
  - LeanLane.Cyc.mech_state_bound
  - LeanLane.Cyc.mech_term_lower
  - LeanLane.Cyc.mech_summand_lower
  - LeanLane.Cyc.exists_total
  - LeanLane.Cyc.mech_cycle_state_bound
  - LeanLane.Cyc.den_mech_gt_one
  - LeanLane.Cyc.two_mul_three_pow_le_four_pow
certificates: [r71c_state_bound_check.py]
evidence:
  - "../mechanical-word-exact-denominator/check_balanced_cycles.py: its 130 high controls (k = 1..128 and 256/512) check bound (5) exactly"
  - "The side lane's independent check of Lean R71-d is c006b_erun_check.py in ../ordered-cycle-sparse-forcing/ (den > 1 for every phase for k = 3..80, den = 1 only at k = 1, 2); it imports r71c_state_bound_check from its own folder, so at its new path it fails (r71c_state_bound_check.py now lives here)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: r71c_state_bound_check.py
    scope: "Feed 2026-10-19 08:39 and 08:47, VERIFIED Lean R71-c and R71-d (statement match and receipts checked), with independent exact checks for k = 1..80 and A the bit length of 3^k: 6C > kD for every phase and 6 n_i > kq for every state of the reduced cycle (the bound is loose: the smallest state is 2.07 to 127 times k/6); den = 1 exactly at k = 1, 2 (words (2) and (2,2)) and den > 1 for every phase for k = 3..80 (c006b_erun_check.py)"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Lean units R71-c (iteration 49) and R71-d (iteration 50) verified in lean/CycleSpectrum.lean with the standard axioms; statement match recorded in the legacy lean/STATE.md, which also found the exact threshold k >= 3 for den > 1 (see Lean)"
aliases: [R71-c, R71-d]
tags: [cycles, mechanical-words, controls, three-x-plus-d, formal]
---

# Mechanical cycles give rational 3x+1 cycles and integer 3x+d cycles arbitrarily far above the absorber, with d varying

## Statement

Raw odd-only clock, no absorption. For `k ≥ 1` let `A` be the bit length of `3^k`, equivalently `A = ⌈k·log₂3⌉`, so that `3^k < 2^A < 2·3^k` and `0 < D < 3^k`. Let `mech(A, k, l)` and its reduced denominator `d = 2^(A/g) − 3^(k/g)` be as in [`mechanical-word-exact-denominator`](../mechanical-word-exact-denominator/README.md).

1. **State bound.** For every phase `l < k`, every state of the positive rational cycle of `mech(A, k, l)` exceeds `k/6`:

       every cycle state x > k/6.                                         (5)

   The reduced integer cycle of `3x + d` has every state `n_i > k·d/6`.
2. **Avoiding the absorber.** For every `k ≥ 3`, `d > 1`; `d = 1` exactly at `k = 1, 2` (words `(2)` and `(2,2)`).
3. **Controls.** Given `C > 0`, any integer `k > 6C` gives a rational `3x+1` cycle with all states above `C` and an integer `3x+d` cycle with all states above `C·d`, `d > 1`.

The denominator `d` varies with `k`: this is not a construction of arbitrarily high cycles for one fixed `d`, there is no constant `C` uniform over all `d` bounding every cycle minimum by `C·d`, and it does not show that these maps pass any proposed finite base test (smaller seeds may already fail to reach `d`). It therefore does not, by itself, refute a method that separately checks all required base cases and proves a genuinely applicable integer induction.

## Proof

The argument is §3 of the legacy note, reproduced in [`mechanical-word-exact-denominator`](../mechanical-word-exact-denominator/README.md) (lightly edited):

> For each `k ≥ 1`, choose `A` as the bit length of `3^k`, equivalently `A = ceil(k log_2 3)`. Exact integer arithmetic gives `3^k < 2^A < 2·3^k`, `0 < D < 3^k`. The word entries are 1 or 2. For every intercept `l` and every `j`, `floor((jA+l)/k) > jA/k − 1`, so `3^(k−1−j)·2^floor((jA+l)/k) > (3^(k−1)/2)·(2^(A/k)/3)^j ≥ 3^(k−1)/2`. Summing `k` terms and dividing by `D < 3^k` proves every cycle state `x > k/6` (5). Given any `C > 0`, choose an integer `k > 6C`. This yields a rational `S_1` cycle with all states `> C`. With `d` from (3), the corresponding integer `S_d` cycle has every state `> C·d`. For `k > 6`, `d > 1` and the cycle avoids the fixed absorber `d`.

**Threshold.** The legacy text says "for `k > 6`, `d > 1`". The exact threshold is `k ≥ 3` (Lean unit R71-d, confirmed by the side lane): by (3), `d = 1` forces `k/g = 1` and `2^(A/g) = 4`, i.e. `A = 2k`, and `2^(2k) = 4^k ≥ 2·3^k > 2^A` for `k ≥ 3`, a contradiction; for `k/g ≥ 2`, `2^(A/g) − 3^(k/g) ≠ 1` modulo 8. At `k = 1, 2` the words are `(2)` and `(2,2)`, with `d = 1`.

## Certificates

[`r71c_state_bound_check.py`](r71c_state_bound_check.py) (under 1 s; side lane, independent code): for `k = 1..80` and `A` the bit length of `3^k`, `6C > kD` for every phase and `6n_i > kq` for every state of the reduced cycle, with the tightness ratio reported; and `den = 1` exactly at `k = 1, 2`, `den > 1` for every `k ≥ 3` in range. It prints its report and writes a receipt only when given an output path.

## Lean

`lean/CycleSpectrum.lean`, Lean units R71-c and R71-d (legacy `lean/STATE.md`; namespace `LeanLane.Cyc`). Axioms `propext`, `Classical.choice`, `Quot.sound` (some helpers fewer); receipts `lean/receipts/CycleSpectrum.*`. No external input.

- **(5).** `mech_state_bound`: `0 < k`, `l < k`, `3^k < 2^A < 2·3^k` ⇒ `k·D(mech A k l) < 6·C(mech A k l)`, i.e. every phase state `C/D` exceeds `k/6`; since the rotations of a mechanical word are its phases (`mech_rotate`), this is every state. The termwise bound is `mech_term_lower` (`3^j ≤ 2^(⌊(jA+l)/k⌋+1)` when `3^k ≤ 2^A`, by comparing `k`-th powers instead of the real quantity `2^(A/k)/3 ≥ 1`) and `mech_summand_lower` (each summand of `C` is at least `3^(k−1)/2`); the prose's strict per-term `>` becomes `≥`, and strictness comes from `D < 3^k`.
- **Bit length.** `exists_total`: for every `k ≥ 1`, `A = log₂(3^k) + 1` satisfies `3^k < 2^A < 2·3^k` (equality `2^A = 2·3^k` is excluded by parity).
- **Integer cycles.** `mech_cycle_state_bound`: the reduced integer `3x+q` cycle `OddCycle.ofWord (mech A k 0)` has `k·q < 6·n_i` for every `i`; this is the prose's "every state `> C·d`". Letter positivity is passed as a hypothesis, implied by `3^k < 2^A`.
- **Threshold.** `den_mech_gt_one`: `k ≥ 3`, `l < k`, `3^k < 2^A < 2·3^k` ⇒ `1 < den (mech A k l)`, through `den_mech`, `mech_D_ne_one` and `two_mul_three_pow_le_four_pow` (`2·3^k ≤ 4^k` for `k ≥ 3`). Item 2 of the statement is this, plus the direct computation at `k = 1, 2`.
- Item 3 is the arithmetic choice `k > 6C` applied to these bounds. Not formalised: the `3x+d` transport remarks of the legacy §0 (see [`scaling-transfer-to-3x-plus-d`](../../attempts/scaling-transfer-to-3x-plus-d/README.md)).

## Remarks

- **Role.** A control for arguments that use only identities on rationals and size inequalities: any proposed universal argument must cope with these genuine positive cycles, which sit above any prescribed constant (times `d`).
- **Uses.** The `k/6` size bound and the term estimate are used by [`perturbed-mechanical-block-family`](../perturbed-mechanical-block-family.md) and [`rotating-mechanical-two-block-family`](../rotating-mechanical-two-block-family.md); the legacy notes of [`rotation-block-exclusion`](../rotation-block-exclusion/README.md) (`LITERATURE.md`, `INDEPENDENT_REVIEW.md`) and [`repeated-block-cancellation-bound`](../repeated-block-cancellation-bound/README.md) (`REPETITION_SPECTRUM.md`, `LITERATURE.md`) quote the same bound for the base mechanical cycle.
- **Literature.** Close to Fernández and Ibáñez's extremal Christoffel parity patterns (arXiv 2607.24844, 2026; shortcut clock), cited in the legacy note but not used; Christoffel cycles maximise the minimum (Halbeisen–Hungerbühler, [`halbeisen-1997-rational-cycles`](../../../../sources/halbeisen-1997-rational-cycles.md)). The Lean lane labels R71-b..d "first in this programme with novelty undetermined".

## History

- Split from `experiments/residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md` §3 (legacy ID R71; Lean units R71-c, R71-d) at commit `be73a66`, by the B12 migration (Claude, Opus 5.5). The side-lane check `reviews/side_lane/r71c_state_bound_check.*` moved here.
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `ea3278e`. Formalised by the Lean lane (Claude Lean lane, Fable), 2026-10-19: R71-c (iteration 49), R71-d (iteration 50, with the exact threshold `k ≥ 3` in place of the prose's `k > 6`; the claim states the formal threshold).
