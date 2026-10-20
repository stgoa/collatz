---
id: largest-letter-sublinear
kind: question
title: Is the largest valuation of a nontrivial 3x+1 cycle o(m)?
status: open
claim: >
  Prove or refute: every hypothetical nontrivial primitive integer cycle of the raw odd-only 3x+1 map, of
  period m, has all valuations a_i = v₂(3n_i + 1) ≤ f(m) for some explicit f(m) = o(m). Known only:
  a_max ≤ B + log₂L + 2 ≤ 0.585·m + O(log m). Given the replayed gap (EXT-1), a positive answer gives ρ → ∞,
  and f(m) ≤ m^(1−ε) gives ρ ≥ (ε − o(1))·log_κ m.
created: 2026-10-19
tags: [cycles, largest-letter, rotation-distance, frontier]
---

# Is the largest valuation of a nontrivial 3x+1 cycle o(m)?

## Question

For a hypothetical nontrivial primitive integer cycle of the raw odd-only `3x+1` map (`q = 1`) with period `m`, prove that its largest letter `a_max = max_i v₂(3n_i + 1)` is at most an explicit `f(m) = o(m)`; or show that no argument of a stated kind can give it.

## Why it matters

By [`largest-letter-rho-reduction`](../results/largest-letter-rho-reduction.md) (S13, Corollaries 6–7; conditional on EXT-1, [`musson-collatz-gap-all`](../../../sources/musson-collatz-gap-all.md)), a rotation with at most `S` mismatches forces a letter of size `≥ f(S) ≈ 2·log₂3·m/(S²(κ^(S+1) − 1))`, e.g. `0.0220m` for `S = 4`. So a sublinear letter bound alone answers [`rotation-distance-growth`](rotation-distance-growth.md): `ρ → ∞`, and `a_max ≤ m^(1−ε)` gives `ρ ≥ (ε − o(1))·log_κ m`. It is strictly weaker than the height bound [`cycle-height-bound`](cycle-height-bound.md), since `a_max ≤ B + log₂ L + 2`. A bound `a_max < 0.022m` at `m ≥ 1.375·10^11` would already give `ρ ≥ 5` ([`rotation-distance-at-least-5`](rotation-distance-at-least-5.md)).

## Known progress

- Only `a_max ≤ B + log₂ L + 2 ≤ 0.585m + O(log m)`, from the height ceiling ([`cycle-height-ceiling`](../results/cycle-height-ceiling.md)) and `log₂ L = O(log m)` under the gap.
- **The obstruction.** A tall profile with one single-step drop of `εm` bits is consistent with every size constraint known here: S7–S10 ([`three-mismatch-exclusion`](../results/three-mismatch-exclusion/README.md), [`four-mismatch-size-method-limit`](../attempts/four-mismatch-size-method-limit/README.md), [`multi-rotation-four-mismatch-exclusion`](../attempts/multi-rotation-four-mismatch-exclusion/README.md)), and S12's height bound is silent when the drop sits at a mismatch ([`denjoy-koksma-height-bound`](../results/denjoy-koksma-height-bound/README.md)).
- *Heuristic (labelled):* in random-like cycles the largest valuation is about `log₂ m`.

## Suggested attacks

From the side-lane notes (S13 §1 and the legacy frontier), marked as proposals: excluding the tall tooth needs arithmetic, not sizes. The drop requires the orbit of the post-drop element `L'` to land exactly on `(2^V L' − 1)/3` after `m − 1` steps; *heuristically* the odds are about `2^(−V)` per candidate `L'`. Start from S13 §§1–4 ([`rise-lemma`](../results/rise-lemma/README.md) and the nodes split from it), S10 for the shape of the surviving configurations, and the comparison with negative integer cycles in [`ones-run-divisibility`](../results/ones-run-divisibility.md).
