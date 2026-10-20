---
id: q-one-inversion-pair-reduction
kind: result
title: At q = 1 an image inversion needs height gap at least 3, and at gap 3 it is a sorted-adjacent pair (n, 8n+1)
status: formal
claim: >
  Raw odd-only 3x+q map, primitive integer cycle, scaled states Z_i = 2^(B−h_i)·n_i and images
  F_i = 3Z_i + 2^(B−h_i)·q. For Z_i < Z_j: F_j < F_i iff h_i < h_j and 3r < q(2^k − 1), where k = h_j − h_i
  and r = n_j − 2^k·n_i > 0; ties F_i = F_j are impossible. At q = 1 every inversion has k ≥ 3, and k = 3
  forces n_j = 8n_i + 1; with B = 3 and heights (0, 3) the two points are sorted-adjacent. Hence a q = 1
  cycle with B ≤ 3 (H < 16L) is ordered unless it contains such a pair (n, 8n+1) at heights (0, 3); this
  last combination is written, not formalised as one theorem.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [dyadic-order-lemma]
lean:
  - LeanLane.Cyc.OddCycle.r_pos
  - LeanLane.Cyc.OddCycle.inversion_iff
  - LeanLane.Cyc.OddCycle.inversion_gap_ge_three
  - LeanLane.Cyc.OddCycle.inversion_gap_three
  - LeanLane.Cyc.OddCycle.pair_adjacent
evidence:
  - "../../attempts/band-three-ordering-extension/README.md, 'What happened' section 1: the written reduction (legacy S03 note section 1)"
  - "s3a_inversion_iff_check.py, s3a_inversion_iff_check.json: side-lane check of Lean unit S3-a on 162 actual 3x+q cycles (odd q < 120, 3 ∤ q) and all 14,774 ordered pairs Z_i < Z_j (1,979 inversions): the equivalence holds on every pair. Fails at its new path: it imports the side-lane helper s1a_integer_cycle_check from its own folder (now in ../ordered-gap-closed-form/). Passed at be73a66 as reviews/side_lane/s3a_inversion_iff_check.py (archive/legacy-checker-run-be73a66.md)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed update 11:11: section 1 of the S03 note checked by hand, the reduction is correct (with two precisions: the extension to H < 16L would go through C006-f's any-q ordered form, not three_band; the 37 pairs at other q are not controls for the q = 1 target). Lean unit S3-a verified (iteration 61)"
tags: [cycles, dyadic-order, inversion, formal]
---

# At q = 1 an image inversion needs height gap at least 3, and at gap 3 it is a sorted-adjacent pair (n, 8n+1)

## Statement

Setting of [`dyadic-order-lemma`](../dyadic-order-lemma.md): a primitive integer cycle of the raw odd-only `3x+q` map, heights `h_i`, scaled states `Z_i = 2^(B−h_i)·n_i` and images `F_i = 3Z_i + 2^(B−h_i)·q`. For `Z_i < Z_j` put `k = h_j − h_i` and `r = n_j − 2^k·n_i`.

1. `F_j < F_i` iff `h_i < h_j` and `3r < q(2^k − 1)`; then `r > 0` and `r` is odd. Ties `F_i = F_j` are impossible.
2. At `q = 1`: `k = 1` would need `3r < 1` and `k = 2` would need `3r < 3`, which never happen, so every inversion has `k ≥ 3`; `k = 3` needs `3r < 7`, so `r = 1`: `n_j = 8n_i + 1`.
3. With `B = 3` and heights `(0, 3)`, the points `Z = 8n` and `8n + 1` are sorted-adjacent: no `2^(3−h)·odd` with `h ≤ 3` lies strictly between them.

So a `q = 1` cycle with `H < 16L` (`B ≤ 3`) is ordered unless it contains a pair `(n, 8n+1)` with `h(n) = 0` and `h(8n+1) = 3` (written combination; see Lean).

## Proof

Legacy S03 §1, now in [`band-three-ordering-extension`](../../attempts/band-three-ordering-extension/README.md). 1 is C005's inversion formula `F_j − F_i = [3r − q(2^k − 1)]/2^(h_j)` read as an equivalence (when `h_j ≤ h_i` both terms of `F_j − F_i` are positive, so there is no inversion); ties are excluded by primitivity. 2 is arithmetic on `3r < q(2^k − 1)` with `r` a positive odd integer. 3: between `8n` and `8n + 1` there is no integer, and every scaled state is an integer when `B = 3`.

## Lean

`lean/CycleSpectrum.lean`, Lean unit S3-a (iteration 61); axioms `propext`, `Classical.choice`, `Quot.sound` (`pair_adjacent`: `propext`, `Quot.sound`). In `OddCycle`, any `q`: `r_pos` (`Z_i < Z_j`, `h_i ≤ h_j` ⇒ `r > 0`); `inversion_iff` (1, as an iff for `Z_i < Z_j`; the case `h_j ≤ h_i` is shown to give no inversion, so `h_i < h_j` is part of the conclusion); `inversion_gap_ge_three` (`q = 1` ⇒ `k ≥ 3`); `inversion_gap_three` (`q = 1`, `k = 3` ⇒ `n_j = 8n_i + 1`, using `r` odd); `pair_adjacent` (3, stated for `B = 3` and heights `(0, 3)`; under `H < 16L`, `k = 3` forces `B = 3`). The tie case is C005-b's `Z_eq_of_F_eq`. Not restated as one theorem: the combination "a `q = 1` cycle with `B ≤ 3` is ordered unless it contains the pair" (it combines these with the order structure, `hord` being an iff over all pairs), and the extension of C006-f and the `J` bound to `H < 16L`.

## Remarks

- **What it would give.** If no such pair exists, the ordered machinery extends from `H < 8L` ([`three-band-collatz-cycles-are-ordered`](../three-band-collatz-cycles-are-ordered.md)) to `H < 16L`, through C006-f's any-`q` ordered form ([`dyadic-order-lemma`](../dyadic-order-lemma.md)) and the `J` bound ([`ordered-cycle-height-change-growth`](../ordered-cycle-height-change-growth.md)). Excluding the pair directly is blocked: [`band-three-ordering-extension`](../../attempts/band-three-ordering-extension/README.md).
- **Controls.** At `q > 1` inversions occur at every height gap `k = 1…11` (S03's probe), consistent with 1: the `q = 1` restrictions in 2 use `q = 1`.
- Novelty: none claimed.

## History

- Split from `experiments/cycle_spectrum/S03/INVERSION_PAIRS.md` §1 (legacy ID `S03`) at commit `be73a66`, by the B05 migration (Claude, Opus 5.5). The side-lane check `reviews/side_lane/s3a_inversion_iff_check.{py,json}` moved here. Side lane (Claude, Opus), feed 2026-10-19 10:58; formalised by the Lean lane as S3-a (feed update 11:19).
