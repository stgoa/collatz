---
id: rotation-distance-at-least-5
kind: question
title: Can a rotation of a nontrivial 3x+1 cycle differ from it in exactly four positions?
status: open
claim: >
  Prove or refute: no nonidentity rotation of the valuation word of a hypothetical nontrivial primitive
  integer cycle of the raw odd-only 3x+1 map differs from it in exactly four positions, so that ρ(w) ≥ 5
  (given the same imports as ρ ≥ 4: the replayed gap EXT-1 and the period and minimum bounds).
created: 2026-10-19
tags: [cycles, rotation-distance, frontier]
---

# Can a rotation of a nontrivial 3x+1 cycle differ from it in exactly four positions?

## Question

Exclude rotations with exactly four mismatches for hypothetical nontrivial `q = 1` cycles of the raw odd-only `3x+1` map, giving `ρ(w) ≥ 5`, or exhibit a reason that the available methods cannot. This is a one-step improvement; the growing target is [`rotation-distance-growth`](rotation-distance-growth.md).

## Why it matters

It is the next constant after `ρ ≥ 4` ([`three-mismatch-exclusion`](../results/three-mismatch-exclusion/README.md), formal given EXT-1 for `m ≥ 2^19`, `L ≥ 2^20`). It was the legacy frontier's second target. The side lane paused it because the size method it was using cannot go beyond it.

## Known progress

- `ρ ≥ 4`: [`three-mismatch-exclusion`](../results/three-mismatch-exclusion/README.md).
- S8's claim that size arguments stop at three mismatches was withdrawn ([`four-mismatch-size-method-limit`](../attempts/four-mismatch-size-method-limit/README.md)): its words fail the rotation by `2h`.
- S10 ([`multi-rotation-four-mismatch-exclusion`](../attempts/multi-rotation-four-mismatch-exclusion/README.md)): in a continuous model of the aligned single-drop structure, both four-mismatch patterns are excluded by several rotations (`v₂ = v₄` by `h`, `2h`; `v₂ ≠ v₄` by `h, …, 12h`), but five and six mismatches survive; no exclusion is claimed, and exact certificates, finite `m`, the 2–2 case, the small-rotation branch and short arcs are missing.
- The sign structure of a four-mismatch rotation is formal: [`four-mismatch-sign-dichotomy`](../results/four-mismatch-sign-dichotomy.md).
- Conditional on EXT-1: a four-mismatch rotation needs `|h|_m ≥ 0.075m`, at most 156 such rotations exist at `m = 1.375·10^11` ([`short-rotation-mismatch-growth`](../results/short-rotation-mismatch-growth/README.md)), and it forces a letter `≥ 0.0220m`, so `ρ ≥ 5` holds for cycles with `m ≥ 1.375·10^11` whose letters are all below `0.022m` ([`largest-letter-rho-reduction`](../results/largest-letter-rho-reduction.md)).

## Suggested attacks

From the legacy S10 §6 and frontier, marked as proposals: exact Farkas certificates per linear cell (one rotation with a uniform margin per region), the finite-`m` threshold against `ℓ* ≈ 342·log₂ m + 172`, the `(1, 1, 2)` window theorem (queued in the Lean lane), the `(2, 2, 0)` case and the small-rotation branch, and the `v₂ ≠ v₄` pattern with the slope cost of its letters `≥ 3`. Alternatively, a letter bound below `0.022m` ([`largest-letter-sublinear`](largest-letter-sublinear.md)).
