---
id: one-point-deletion-rank-shift
kind: result
title: Deleting one rank from a circular shift by s leaves a circular shift only when s = 1 or s = m − 1
status: formal
claim: >
  Finite rank permutations. Let m ≥ 2, 1 ≤ s < m and R(j) = j + s mod m. Delete one rank and take
  the first-return permutation of R on the remaining m − 1 ranks, kept in circular order. The induced
  permutation is a circular rank shift if and only if s = 1 or s = m − 1. (No coprimality of s and m
  is needed.) Consequence for cycles: a primitive ordered 3x+q cycle with q ≤ L, exactly one
  positive-height state and interior normalised shift 2 ≤ s ≤ m − 2 has a height-zero first-return
  map that is not a circular shift.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [dyadic-order-lemma]
lean:
  - LeanLane.Cyc.one_point_deletion
  - LeanLane.Cyc.retMap
  - LeanLane.Cyc.compMap
  - LeanLane.Cyc.IsRankShift
evidence:
  - "../attempts/excursion-compression/FIRST_RETURN_ORDER.md: the written proof and the q = 13 and q = 83 controls"
  - "../attempts/excursion-compression/check_return_order.py: a certificate of that node; checks the deletion formula on 105,388 permutations through m = 80"
  - "../attempts/excursion-compression/c009_excursion_check.py: side-lane check of the theorem for 3 ≤ m ≤ 40"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: ../attempts/excursion-compression/c009_excursion_check.py
    scope: "Feed 2026-10-19 03:17: exhaustive check of 13,108 cases (3 ≤ m ≤ 40, coprime s); update 05:07: 1,770 cases with m ≤ 60 and no coprimality filter; Lean C009-b VERIFIED, receipts (sha256 1f618576…) checked"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 03:19: deletion table re-derived by hand; Lean unit C009-b verified (iteration 33)"
tags: [cycles, dyadic-order, permutations, formal]
---

# Deleting one rank from a circular shift by s leaves a circular shift only when s = 1 or s = m − 1

## Statement

Let `R(j) = j + s mod m` with `m ≥ 2` and `1 ≤ s < m`. Delete one rank and take the first-return permutation on the remaining `m − 1` ranks, keeping their circular order. This induced permutation is a circular rank shift **if and only if** `s = 1` or `s = m − 1`.

The legacy statement assumed `gcd(s, m) = 1`; the Lean proof and the side-lane check show it is not needed.

**Cycle consequence.** If a primitive ordered `3x+q` cycle with `q ≤ L` has exactly one positive-height state and normalised successor shift `s` ([`dyadic-order-lemma`](dyadic-order-lemma.md)), its height-zero first-return map is the one-point-deleted permutation above; for an interior shift `2 ≤ s ≤ m − 2` it is not a circular shift. This is conditional: it does not assert that such cycles exist at every `m`, and excludes no `q = 1` cycle.

## Proof

[`FIRST_RETURN_ORDER.md`](../attempts/excursion-compression/FIRST_RETURN_ORDER.md). The choice of circular origin does not affect whether a permutation is a rank shift, so rotate the deleted rank to 0. Retained ranks `j = 1, …, m − 1` get compressed ranks `j − 1`. All returns take one old step except the predecessor `j = m − s`, which takes two steps through 0. Compressed shifts, modulo `m − 1`:

| Old source ranks | Number | Compressed shift |
| --- | ---: | ---: |
| `1 ≤ j < m − s` | `m − s − 1` | `s` |
| `m − s < j < m` | `s − 1` | `s − 1` |
| `j = m − s`, via 0 to `s` | 1 | `2s − 1` |

For `2 ≤ s ≤ m − 2` both regular groups are nonempty and their shifts differ modulo `m − 1`, so the map is not a rotation. For `s = 1` all shifts reduce to 1; for `s = m − 1`, to −1. For `m = 2` the retained singleton has the identity permutation and `s = 1`.

## Lean

`lean/CycleSpectrum.lean`, Lean unit C009-b (legacy `lean/STATE.md`, iteration 33), axioms `propext`, `Quot.sound` only; receipts `lean/receipts/CycleSpectrum.*`.

- `LeanLane.Cyc.retMap m s j`: the first-return map on old ranks after deleting rank 0 (`(j+s) mod m`, or `(j+2s) mod m` when the first step lands on 0); `compMap m s j = retMap m s (j+1) − 1`, compressed to `{0, …, m−2}`; `IsRankShift m s` is `∃ c, ∀ j < m − 1, compMap m s j = (j + c) mod (m − 1)`.
- `LeanLane.Cyc.one_point_deletion`: for `2 ≤ m`, `1 ≤ s < m`, `IsRankShift m s ↔ s = 1 ∨ s = m − 1`. This is the claim with the deleted rank fixed at 0 (the prose's own normalisation); no coprimality hypothesis.
- The `q = 13` control is checked by `decide`: with the positive-height state relabelled to 0, `compMap 5 3 = (3, 2, 0, 1)` (the prose's `(2, 0, 3, 1)` conjugated by the cyclic relabelling) and `¬ IsRankShift 5 3`.

The cycle consequence (identifying the height-zero first-return map of an ordered cycle with one positive-height state with this permutation) is not formalised; it is a direct reading of the ordered successor as a rank shift.

## Remarks

- **Control.** The reduced `q = 13` cycle `n = (283, 431, 653, 493, 373)`, `a = (1,1,2,2,2)`, `h = (0,0,1,0,0)`, `A = 8`, `m = 5`, shift `s = 3`: removing 653 leaves the sorted core `(283, 373, 431, 493)` with first-return ranks `(2, 0, 3, 1)`.
- **Use.** It refutes the inheritance of circular order needed by [`excursion-compression`](../attempts/excursion-compression/README.md). Keeping a more general return permutation and each block's affine coefficients preserves the data but not the single-step circle-order theorem as an induction hypothesis.
- **Novelty.** Elementary; none claimed.

## History

- Split from `experiments/cycle_spectrum/C009/` (legacy ID `C009`; `FIRST_RETURN_ORDER.md`) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. Formalised by the Lean lane (Claude Lean lane, Fable) as C009-b, iteration 33, without the coprimality hypothesis.
