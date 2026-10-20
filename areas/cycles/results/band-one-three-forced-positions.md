---
id: band-one-three-forced-positions
kind: result
title: In the Collatz range, an ordered cycle in band 1 has at least three forced positions
status: formal
claim: >
  Raw odd-only 3x+q map, any q. Let a circularly ordered cycle with rank shift s have positive letters
  (a_i ≥ 1) and m < A < 2m (equivalently floor(A/m) = 1). If all its heights lie in {0, 1} and at least one
  height is 1, then its sorted gap system has J ≥ 3 forced positions. (J = 2 occurs only for A ≥ 2m.)
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [ordered-gap-closed-form, dyadic-order-lemma]
lean:
  - LeanLane.Cyc.OrdCycle.q'_eq_one_of_range
  - LeanLane.Cyc.OrdCycle.J_ge_three
evidence:
  - "Side-lane feed entry 2026-10-19 06:30 ('In the Collatz range, band 1 forces J ≥ 3 (proved)') and update 08:20 (Lean S1-e)"
  - "jterm_gap_check.py (legacy reviews/side_lane/, migrated by a later batch): asserts J ≥ 3 on every band-1 ordered cycle among its 900 Collatz-range cycles (m ≤ 12, letters 1-3), and reports 27 cases with J = 2 outside the Collatz range (A ≥ 2m)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Lean unit S1-e verified (iteration 47), statement checked against the feed's argument (legacy lean/STATE.md row S1-e and its note); the lane pointed out that the argument uses letter positivity, now an explicit hypothesis"
tags: [cycles, ordered-cycles, gap-system, band-one, formal]
---

# In the Collatz range, an ordered cycle in band 1 has at least three forced positions

## Statement

Notation of [`ordered-gap-closed-form`](ordered-gap-closed-form/README.md) and [`dyadic-order-lemma`](dyadic-order-lemma.md): normalised letters `c_i = a_i + h_(i+1) − h_i`, rank exponents `e_r = floor(A/m) + [r ≥ m − s]`. Let an ordered cycle have every letter `a_i ≥ 1` and `m < A < 2m`. If all heights lie in `{0, 1}` and some height is `1` (band 1), then `J ≥ 3`.

## Proof

Side-lane feed, 2026-10-19 06:30 (lightly edited). Take `m < A < 2m`. Then a non-wrapping step has `c = 1`, and since `a = c + h_i − h_(i+1) ≥ 1`, it cannot raise the height. `J = 2` means sorted heights `0^k 1^(m−k)` (the seam and one change). Every rank in `[max(0, k−s), min(k, m−s))` would then rise on a non-wrapping step, giving a zero letter. That interval is never empty. So `J = 2` occurs only for `A ≥ 2m`; `J = 1` would make the cycle narrow (no height 1).

## Lean

`lean/CycleSpectrum.lean`, Lean unit S1-e (iteration 47); axioms `propext`, `Classical.choice`, `Quot.sound`. `J_ge_three` takes letter positivity (`∀ i, 1 ≤ a i`), `q' = 1` (the range; `q'_eq_one_of_range` derives `q' = floor(A/m) = 1` from `m < A < 2m`), band 1 as `∀ i, h i ≤ 1`, and some height `1`; it concludes `3 ≤ J`. The proof is the feed's with one rank chosen from the interval, `r* = max(0, k − s)`: `r* < k`, `k ≤ r* + s`, `r* + s < m` are the three facts behind "never empty"; at the index of `r*` one gets `c = e(r*) = 1` against `c = a + 1`, so `a = 0`. No reducedness or oddness of `q` is needed. `B` in the structure is an upper bound, so "band 1" is the hypothesis on the heights, not on `B`.

## Remarks

- **Scope.** An ordered-class statement for every `q`: every closed form of [`ordered-gap-closed-form`](ordered-gap-closed-form/README.md) in this band has at least three nonzero terms. Nothing about whether `H < 4L` Collatz cycles exist follows.
- **Outside the Collatz range** (`A ≥ 2m`), `J = 2` occurs; there, in 27 tested cases, `gcd(C, D) = gcd(2^(u1) − 3^(v1), 2^(u2) − 3^(v2))` with `(u1 + u2, v1 + v2) = (A, m)` (observed by `jterm_gap_check.py`, not proved).
- Novelty: none claimed.

## History

- Created from the side-lane feed entry of 2026-10-19 06:30 (marked "proved" in prose; flagged 08:06 as the one informal lead statement bearing on the `H < 4L` rung) and update 08:20 (Lean S1-e verified), by the B05 migration (Claude, Opus 5.5). Legacy ID S1 (part e); no legacy folder. Side lane (Claude, Opus); formalised by the Lean lane (Claude, Fable).
