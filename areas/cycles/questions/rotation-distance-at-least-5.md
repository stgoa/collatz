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

- **2026-11-08: bounded unequal half defects are excluded without external inputs.**
  [`bounded-unequal-half-defect-exclusion`](../results/bounded-unequal-half-defect-exclusion/README.md)
  excludes denominator 1 whenever the two half-defect magnitudes are
  unequal, have the same parity, and sum to at most 24, with arbitrary
  length, common letters, signs and positions. Complete signed state
  graphs reduce full plus-factor cancellation to 74 base joins;
  an affine convexity argument handles every cycle repetition.
  This gives an unconditional proof for this bounded-variation class,
  already excluded with the stronger imported mismatch bounds below.
  Larger amplitudes and the general four-mismatch question remain open.
- **2026-11-08: a lifted four-arc class is excluded at every length.**
  [`lifted-four-arc-denominator-one-exclusion`](../results/lifted-four-arc-denominator-one-exclusion/README.md)
  excludes denominator 1 for the words obtained by replacing every
  letter `d` in `(1^(2r-4),a,1,c,1^(2r-2),c,1,b)` by `(2,d)`,
  for all `r>=2`, `a,b>=1`, `c>=2`. A nonzero resultant and the
  declared gap EXT-1 force at most 4,088 odd steps; a local exact
  descent and product certificate excludes those lengths. No
  near-critical or parity hypothesis is used. This specified track
  shape includes primitive near-critical four-mismatch words with
  unbounded shortcut local-minimum counts; arbitrary four-mismatch
  words remain outside the result.
- **2026-11-08: a general half-defect normal form.**
  [`two-half-defect-mersenne-normal-form`](../results/two-half-defect-mersenne-normal-form/README.md)
  parametrizes full plus-factor cancellation for every unequal same-parity
  pair of half-defect magnitudes by two linked signed odd-only segments
  with addends `2^J-1` and `2^r-1`. It includes both sign orders and gives
  an exact affine-state test sufficient to exclude denominator 1.
  That test is not proved uniformly; the general question remains open.
- **2026-11-08: amplitudes 2 and 4 are excluded at every length.**
  [`unequal-two-four-half-defect-classification`](../results/unequal-two-four-half-defect-classification/README.md)
  excludes positive integer `3x+1` cycles whose halves differ at
  exactly two positions with absolute changes 2 and 4, in any signs
  or order. Full plus-factor cancellation occurs in two explicit
  infinite families, but a uniform affine bound gives a rational
  state strictly between 0 and 1 in each. The exclusion uses no
  near-critical hypothesis or external bound. It covers only this
  half-period four-mismatch class; the general question remains open.
- **2026-11-08: an unconditional half-period subcase is excluded.**
  [`unequal-one-five-half-defect-classification`](../results/unequal-one-five-half-defect-classification/README.md)
  excludes positive integer `3x+1` cycles whose two halves differ at
  exactly two positions with absolute changes 1 and 5, in any signs
  or order, at every length. The proof classifies full plus-factor
  cancellation and shows that every exceptional word still has
  denominator greater than 1. It uses no near-critical assumption
  or external bound. This settles only that half-period four-mismatch
  class; the general question remains open.
- `ρ ≥ 4`: [`three-mismatch-exclusion`](../results/three-mismatch-exclusion/README.md).
- S8's claim that size arguments stop at three mismatches was withdrawn ([`four-mismatch-size-method-limit`](../attempts/four-mismatch-size-method-limit/README.md)): its words fail the rotation by `2h`.
- S10 ([`multi-rotation-four-mismatch-exclusion`](../attempts/multi-rotation-four-mismatch-exclusion/README.md)): in a continuous model of the aligned single-drop structure, both four-mismatch patterns are excluded by several rotations (`v₂ = v₄` by `h`, `2h`; `v₂ ≠ v₄` by `h, …, 12h`), but five and six mismatches survive; no exclusion is claimed, and exact certificates, finite `m`, the 2–2 case, the small-rotation branch and short arcs are missing.
- The sign structure of a four-mismatch rotation is formal: [`four-mismatch-sign-dichotomy`](../results/four-mismatch-sign-dichotomy.md).
- Conditional on EXT-1: a four-mismatch rotation needs `|h|_m ≥ 0.075m`, at most 156 such rotations exist at `m = 1.375·10^11` ([`short-rotation-mismatch-growth`](../results/short-rotation-mismatch-growth/README.md)), and it forces a letter `≥ 0.0220m`, so `ρ ≥ 5` holds for cycles with `m ≥ 1.375·10^11` whose letters are all below `0.022m` ([`largest-letter-rho-reduction`](../results/largest-letter-rho-reduction.md)).

## Suggested attacks

**2026-11-08: separate transients from repeatable cycles.** The
[bounded-amplitude theorem](../results/bounded-unequal-half-defect-exclusion/README.md)
settles the linked-segment affine test for `2<=J<=12`, all `1<=r<J`,
at every word length. Its loop convexity argument reduces arbitrary
positive cycle insertions to base values and fixed-point limits.
The remaining unbounded-amplitude target is to control crossing
graphs and transient paths uniformly, or find another integrality
obstruction. Equal magnitudes, opposite parities and other shifts
require their corresponding scoped arguments.

**2026-11-08: linked signed segments.** For unequal same-parity half
defects, use the [Mersenne normal form](../results/two-half-defect-mersenne-normal-form/README.md)
to seek a uniform bound `F_u(1)<2^s+h`, or an integrality obstruction
that does not require this bound. Both the high boundary valuations
and the common signed endpoints must be retained. This is a target,
not a consequence already supplied by the parametrization.

From the legacy S10 §6 and frontier, marked as proposals: exact Farkas certificates per linear cell (one rotation with a uniform margin per region), the finite-`m` threshold against `ℓ* ≈ 342·log₂ m + 172`, the `(1, 1, 2)` window theorem (queued in the Lean lane), the `(2, 2, 0)` case and the small-rotation branch, and the `v₂ ≠ v₄` pattern with the slope cost of its letters `≥ 3`. Alternatively, a letter bound below `0.022m` ([`largest-letter-sublinear`](largest-letter-sublinear.md)).

## History

- 2026-11-08: added the unconditional bounded unequal half-defect
  exclusion and the transient-versus-loop research target. The
  general question remains `open` (Codex cycle research lane,
  GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: added the lifted four-arc denominator-one exclusion,
  conditional only on the declared gap EXT-1, with a locally replayed
  finite length exclusion. The general question remains `open`
  (Codex four-arc research lane, GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: added the general signed-Mersenne half-defect normal form
  and its unresolved affine-state target; the question remains `open`
  (Codex cycle research lane, GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: added the unconditional amplitudes-2-and-4 half-period
  exclusion from [`unequal-two-four-half-defect-classification`](../results/unequal-two-four-half-defect-classification/README.md).
  The arbitrary four-mismatch question remains `open`
  (Codex cycle research lane, GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: added the unconditional amplitudes-1-and-5 half-period
  exclusion from [`unequal-one-five-half-defect-classification`](../results/unequal-one-five-half-defect-classification/README.md).
  The arbitrary four-mismatch question remains `open`
  (Codex cycle research lane, GPT-6 Astra; directed by Santiago Armstrong).
