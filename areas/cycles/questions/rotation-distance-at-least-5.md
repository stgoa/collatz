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

- **2026-11-08: arbitrary mechanical edits have a uniform denominator law.**
  [`mechanical-edit-denominator-law`](../results/mechanical-edit-denominator-law/README.md)
  handles all mechanical totals and phases, with arbitrary signed
  replacements. It excludes at most two edits using only EXT-1,
  and at most ten with the separately declared convergence input.
  Under EXT-1, a hypothetical cycle of length `m>=2^32` also differs
  in more than `sqrt(m)` positions from every contracting mechanical
  word. Mechanical edit distance is not rotation distance; the
  general four-mismatch question remains open.
- **2026-11-08: common additive factors constrain signed endpoints.**
  [`odd-order-residue-signed-endpoint-divisibility`](../results/odd-order-residue-signed-endpoint-divisibility/README.md)
  proves that every prime-power component of a common addend whose
  residue orders of 2 and 3 are odd must divide the endpoint `h`
  of a signed `-h -> h` join. This applies to both Mersenne orders
  at arbitrary levels and lengths. In the endpoint-one,
  low-to-high `r=1` subclass, it excludes every level divisible
  by 11 or 25. Other endpoints and levels remain open here.
- **2026-11-08: one arbitrary change to a mechanical word is excluded.**
  [`one-edit-mechanical-denominator-growth`](../results/one-edit-mechanical-denominator-growth/README.md)
  proves an explicit denominator law for every primitive word differing
  in at most one position from a positive mechanical word, with arbitrary
  base total, phase and replacement. Under EXT-1, exact local finite
  checks exclude denominator 1 at every length. This includes the
  [prime four-mismatch family](../results/sparse-rotation-bounded-period-reduction-obstruction/README.md)
  whose bounded-period decomposition obstruction remains valid.
  General four-mismatch words need not have this form; the question
  remains open.
- **2026-11-08: a uniform endpoint-and-slope enclosure.**
  [`mersenne-join-state-enclosure`](../results/mersenne-join-state-enclosure/README.md)
  bounds the canonical normalized state for either interface sign
  in every unequal same-parity Mersenne normal form. A state lower
  bound gives an explicit necessary lower bound on the total
  segment slope; failure excludes denominator 1. Positive cycle
  insertions decrease the upper state bound. The result has no
  level or length restriction, but does not assert that every
  join lies in the excluded slope region.
- **2026-11-08: small signed endpoints are excluded at every amplitude.**
  [`small-mersenne-endpoint-exclusion`](../results/small-mersenne-endpoint-exclusion/README.md)
  proves the linked-segment affine test whenever `M>=7h+1`, where
  `M-1` is the first Mersenne addend and the signed endpoints are
  `-h,h`; a sharper quadratic condition is also proved. Both
  segment orders and arbitrary lengths and levels are covered,
  without external inputs. A denominator-one candidate must have
  `h>(M-1)/7`. This leaves the larger-endpoint region unresolved.
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
- **2026-11-08: changes to any fixed expanding background must grow.**
  [`expanding-background-defect-growth`](../results/expanding-background-defect-growth/README.md)
  proves an explicit bound, under EXT-1, for arbitrary positive
  substitutions in repetitions of a fixed expanding word. It allows
  every phase and both increases and decreases, and gives effective
  finiteness at fixed substitution count. Its independently replayed
  four-increase `(2,1)` corollary subsumes the earlier lifted family;
  the node credits the stronger prior `(1,2)`-perturbation result.
  Sparse rotations need not admit a fixed background of this kind,
  so the general rotation-distance question remains open.
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

**2026-11-08: move to the other order or higher low levels.** The
[unit-low-level theorem](../results/unit-low-level-mersenne-exclusion/README.md)
settles all low-to-high `r=1` denominator-one candidates under
LMN, including `g>h` and contracting first prefixes. This
supersedes the remaining-case targets for that subclass below;
their earlier text is retained as history. The signed auxiliary
joins are not themselves ruled out. The next normal-form targets
are high-to-low order and low-to-high `r>=2`; arbitrary
four-mismatch rotations still need additional structure.

**2026-11-08: isolate the remaining negative interfaces.** Under LMN
alone, the
[expanding-prefix exclusion](../results/expanding-negative-prefix-mersenne-exclusion/README.md)
removes low-to-high `r=1` joins `-h -> -g -> h` with `g<=h`
and expanding first slope, including every closed negative prefix
at every endpoint. Remaining low-to-high `r=1` candidates must
have `g>h` or a contracting first slope; slope 1 is impossible.
The other segment order, other `r` and the full four-mismatch
question remain outside this result.

**2026-11-08: move beyond closed negative prefixes.** Under EXT-1,
the [closed-prefix denominator law](../results/closed-negative-prefix-mersenne-denominator-law/README.md)
excludes denominator one for low-to-high `r=1` joins whose first
segment closes at `-h` with `h<=91`, including the endpoint-one
case. Within this normal-form subclass, remaining denominator-one
work must use a nonclosed first segment or `h>91`. The theorem
does not settle existence of the auxiliary signed returns.

**2026-11-08: retain residue restrictions on the endpoint.** Apply
the [common-addend divisibility condition](../results/odd-order-residue-signed-endpoint-divisibility/README.md)
before estimating a Mersenne join. For endpoint-one low-to-high
`r=1`, the first segment fixes `-1`; the remaining return under
`3x+(2^J-1)` is still unresolved at odd levels not removed by
the odd-order residue obstruction. A finite return search does
not settle those unbounded levels.

**2026-11-08: retain both the endpoint and total slope.** The
[state enclosure](../results/mersenne-join-state-enclosure/README.md)
covers negative as well as positive interfaces. Combine its
necessary slope threshold with the small-endpoint exclusion;
the remaining normal-form candidates must satisfy both. Moving
the cut to the other defect produces a mixed-sign auxiliary
description, so a second positive-addend bound needs justification.

**2026-11-08: the remaining endpoint region.** The
[uniform endpoint bound](../results/small-mersenne-endpoint-exclusion/README.md)
settles every normal-form join with `M>=7h+1`, independently of
the Mersenne levels. Focus on larger signed endpoints, including
paths whose first negative-to-positive crossing is delayed; the
bound does not assert that these cases fail.

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

- 2026-11-08: added the all-length
  [`unit-low-level-mersenne-exclusion`](../results/unit-low-level-mersenne-exclusion/README.md)
  and clarified that the remaining low-to-high `r=1` targets
  are now covered under LMN. Other orders and levels remain
  open, as does the general question (Codex cycle research lane,
  GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: separated the remaining `r=1` interfaces after the
  all-endpoint expanding-prefix exclusion under LMN alone;
  retained the earlier `h<=91` result with its sole-EXT-1 input
  (Codex signed-endpoint research lane, GPT-6 Astra;
  directed by Santiago Armstrong).

- 2026-11-08: refined the low-to-high `r=1` target after the
  closed-negative-prefix exclusion for `h<=91` under EXT-1.
  Auxiliary signed-return existence and the general question
  remain open (Codex closed-prefix research lane, GPT-6 Astra;
  directed by Santiago Armstrong).

- 2026-11-08: added the uniform mechanical-edit denominator bounds,
  with distinct inputs for the two-edit and ten-edit exclusions and
  the contracting-background square-root restriction. The general
  question remains `open` (Codex four-arc research lane, GPT-6 Astra;
  directed by Santiago Armstrong).
- 2026-11-08: added the all-length residue constraint on signed
  endpoints and its infinite level exclusions for the endpoint-one
  subclass. The general question remains `open` (Codex cycle
  research lane, GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: added the one-edit mechanical denominator law and its
  arithmetic exclusion of the prime four-mismatch coverage family,
  conditional only on EXT-1. The general question remains `open`
  (Codex four-arc research lane, GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: added the uniform Mersenne state enclosure and the
  combined endpoint-and-slope target. The general question remains
  `open` (Codex cycle research lane, GPT-6 Astra; directed by
  Santiago Armstrong).
- 2026-11-08: added the uniform small-endpoint criterion and its
  remaining larger-endpoint target. The general question remains
  `open` (Codex cycle research lane, GPT-6 Astra; directed by
  Santiago Armstrong).
- 2026-11-08: added the unconditional bounded unequal half-defect
  exclusion and the transient-versus-loop research target. The
  general question remains `open` (Codex cycle research lane,
  GPT-6 Astra; directed by Santiago Armstrong).
- 2026-11-08: added the fixed expanding-background substitution
  bound and the independently checked weaker instance of the
  known `(1,2)` perturbation exclusion. The general question stays
  `open` (Codex four-arc research lane, GPT-6 Astra;
  directed by Santiago Armstrong).
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
