---
id: rotation-distance-finite-exceptions
kind: question
title: For each bound s, do only finitely many 3x+1 cycles have a rotation with at most s mismatches?
status: open
claim: >
  Raw odd-only 3x+1 clock. Prove or refute, for every integer s >= 1: only finitely many nontrivial primitive
  positive integer cycles have a nonidentity rotation of their valuation word with at most s mismatches. An
  ineffective proof is acceptable here; an explicit rate is the separate question rotation-distance-growth.
  Known under the stated inputs: no such cycle for s <= 3 (EXT-1 with the period and minimum imports), and
  finitely many cycles with a rotation of exactly four mismatches (EXT-1 and Ridout's theorem); together these
  give the case s = 4. Open from s = 5 on.
created: 2026-11-23
tags: [cycles, rotation-distance, s-units, ridout, finiteness, frontier]
---

# For each bound s, do only finitely many 3x+1 cycles have a rotation with at most s mismatches?

## Question

Let `rho(w)` be the rotation distance of the primitive valuation word of a cycle
([`conventions/NOTATION.md`](../../../conventions/NOTATION.md)). For each integer `s`, is the set of
hypothetical nontrivial integer cycles of the raw odd-only `3x+1` map with `rho(w) <= s` finite?

A positive answer for every `s` says that `rho(w)` tends to infinity along every infinite family of cycles. It
gives no rate. Proofs through Ridout's theorem or the subspace theorem are ineffective, and that is accepted
for this question.

## Why it matters

It is the qualitative form of [`rotation-distance-growth`](rotation-distance-growth.md), which asks for an
explicit `F(m)` with `rho(w) >= F(m)`. The size method that produced `rho >= 4` stalls when a mismatch has a
very large amplitude. The half-period case shows that exactly this regime can be handled, without a bound, by
Diophantine approximation with restricted prime factors. If the mechanism extends, bounded rotation distance
would be ruled out for all but finitely many cycles, for every bound. Across the family `3x+d` infinitely many
actual cycles have small `rho`, so no proof can be uniform in `d`; the half-period case uses `d = 1` through the
size of the minimum.

## Known progress

- `s <= 3`: no cycle, by [`three-mismatch-exclusion`](../results/three-mismatch-exclusion/README.md) and the
  results it combines, under EXT-1 with the period and minimum imports.
- Exactly four mismatches: finitely many cycles, under EXT-1 and Ridout's theorem.
  [`non-half-period-four-mismatch-exclusion`](../results/non-half-period-four-mismatch-exclusion/README.md)
  leaves only the rotation by half the period, and
  [`half-period-four-mismatch-finiteness`](../results/half-period-four-mismatch-finiteness/README.md) shows that
  only finitely many cycles have such a rotation. With the line above this gives `s = 4`, under the union of
  the inputs. Whether the exceptional set is empty is
  [`rotation-distance-at-least-5`](rotation-distance-at-least-5.md).
- 2026-11-23, six mismatches, half-period rotations only: finitely many cycles, under EXT-1 and Evertse's
  theorem on vanishing sums with small parts outside 2 and 3
  ([`half-period-six-mismatch-finiteness`](../results/half-period-six-mismatch-finiteness.md), resting on
  [`half-period-six-mismatch-local-law`](../results/half-period-six-mismatch-local-law/README.md)). The law uses
  the relations between consecutive paired quotients, in three- and four-term form, and an exact
  linear-programming certificate. It does not treat rotations with five mismatches, nor rotations with six
  mismatches other than the rotation by half the period, so `s = 5` and `s = 6` stay open.
- A general tool: [`mismatch-chain-ridout-criterion`](../results/mismatch-chain-ridout-criterion/README.md).
  For any rotation, any mismatched start position after a common run of `a - 1` positions and any later end
  position, an exact identity relates `3^(a+n) g` to `2^c U`. Under Ridout's theorem, for each fixed
  `epsilon > 0`, the error `Theta` satisfies `U Theta >= 3^(a+n) / (2^c U)^epsilon` with finitely many
  exceptions.
- A rotation with at most `S` mismatches forces a mismatch of linear amplitude, under EXT-1
  ([`largest-letter-rho-reduction`](../results/largest-letter-rho-reduction.md)). So the regime where the size
  method stalls is always present.

## Suggested attacks

These are proposals, not results.

- **Chains and a size statement.** A rotation with `s` mismatches has at most `s^2` chains, in the sense of
  the criterion, that start at a mismatch, take its whole common run and end at a mismatch. Normalise the arc lengths, arc totals, amplitudes and the heights of the states after the
  mismatches by the period. The cycle imposes linear constraints on these quantities: the valuation budget, the
  bounds from paired differences at the start and the end of every common run, positivity, and a minimum of
  height `O(log m)` under EXT-1. Finiteness for that `s` would follow from showing that these constraints force
  one of the sufficient forms of the criterion with a fixed `epsilon`. In the half-period four-mismatch case
  this is the computation that produces the constant `1 - log_2 3 + 1/log_2 3`.
- **First targets.** Half-period words whose halves differ in three positions (six mismatches), where the sign
  pattern of the three changes can no longer be normalised; and rotations with exactly five mismatches, which
  cannot be half-period rotations. *Update 2026-11-23:* the first of these is done (see "Known progress"). The
  second needs, before any S-unit argument, the list of rotation structures with five mismatches that survive
  the size constraints, as was done for four mismatches by
  [`non-half-period-four-mismatch-exclusion`](../results/non-half-period-four-mismatch-exclusion/README.md).
- **Eight half-period mismatches.** In a normalised model, the relations used for six mismatches and longer
  ones of the same kind do not force a small product for four changed positions (exploration in
  [`half-period-six-mismatch-local-law`](../results/half-period-six-mismatch-local-law/README.md)). Relations
  with more than four terms were not tried.
- **Several error terms.** When no single chain is good, a sum of more than two terms of the form
  `(power of 2)(power of 3)(small cofactor)` vanishes. The subspace theorem handles such sums when the
  cofactors are small compared with the powers. The accounting of exponents would have to be done with the same
  care as in the two-term case.
