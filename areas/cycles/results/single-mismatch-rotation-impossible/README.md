---
id: single-mismatch-rotation-impossible
kind: result
title: "No rotation of a word differs from it in exactly one position; a primitive word has rotation distance at least 2"
status: formal
claim: >
  Raw odd-only clock, any 3x+q, or any word at all: for every word w of length m and every shift h, the number of
  positions j < m with a_j ≠ a_(j+h) (indices mod m) is never 1; if the rotation R_h w differs from w at all,
  it differs in at least two positions. Hence every primitive word (no rotation by 0 < h < m fixes it) has
  rotation distance ρ(w) ≥ 2, and a cycle of the shift permutation that carries a mismatch carries at least
  two. Proved in Lean (lean/LeanLane/RotationDistance.lean) with the standard axioms only, for words with
  letters in ℕ.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-31
depends_on: []
lean:
  - LeanLane.RotationDistance.sum_diff
  - LeanLane.RotationDistance.mismatches_ne_one
  - LeanLane.RotationDistance.two_le_mismatches_of_ne
evidence:
  - "../../../../lean/receipts/RotationDistance.build.txt, RotationDistance.axioms.txt, RotationDistance.sha256.txt: build status, the #print axioms lines (standard axioms only) and the source hash, produced on the pinned toolchain"
tags: [cycles, rotation-distance, words, lean]
---

# No rotation of a word differs from it in exactly one position

## Statement

Notation of [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md): for a word `w = (a_0, …, a_(m−1))` and a shift `h`, `mism(w, h) = #{j < m : a_j ≠ a_(j+h)}` (indices mod `m`) and `ρ(w) = min_(0<h<m) mism(w, h)`.

**Theorem.** `mism(w, h) ≠ 1` for every word `w` and every `h`. Consequently, if `R_h w ≠ w` (`0 < h < m`) then `mism(w, h) ≥ 2`, and a primitive word has `ρ(w) ≥ 2`.

The statement is used silently throughout the cycles area: the few-arc censuses start at `s = 2` ([`few-arc-codings-denominator-census`](../few-arc-codings-denominator-census/README.md)), the track-structure enumeration of [`rho-four-census-letters-three`](../rho-four-census-letters-three/README.md) excludes cycles with a single change point, and the two-defect node observes that the differences `a_(i+h) − a_i` sum to zero on each cycle of the shift ([`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md), part 1). The two-marker family therefore has `ρ(w_n) = 2` exactly ([`two-marker-constant-background-exact-denominator`](../two-marker-constant-background-exact-denominator/README.md): its rotation by `n` has exactly two mismatches).

## Proof

The rotated word `R_h w` is a permutation of `w`, so `Σ_(j<m) a_(j+h) = Σ_(j<m) a_j` and the signed differences `d_j = a_(j+h) − a_j` sum to zero. If exactly one `d_j` were nonzero, the sum would equal that term, which is nonzero. So the number of nonzero `d_j`, which is `mism(w, h)`, is never 1. If `R_h w ≠ w`, some `d_j ≠ 0`, so `mism(w, h) ≥ 2`; a primitive word has `R_h w ≠ w` for every `0 < h < m`, hence `ρ(w) ≥ 2`. (Per cycle of the shift permutation the same telescoping holds, which is the per-cycle form used by the censuses.)

## Lean

[`lean/LeanLane/RotationDistance.lean`](../../../../lean/LeanLane/RotationDistance.lean), namespace `LeanLane.RotationDistance`, a module of the `LeanLane` library (imports `LeanLane.CycleEquation` for `getD_rotate`); standard axioms only (receipts `RotationDistance.*` in [`lean/receipts/`](../../../../lean/receipts/)). `mismatches w h` is `LeanLane.Words.mismatches`: the number of `j < w.length` with `w.getD j 0 ≠ w.getD ((j + h) % w.length) 0`.

| Claim | Declaration | Statement |
|---|---|---|
| the differences sum to zero | `sum_diff` | `((List.range w.length).map (diff w h)).sum = 0`, with `diff w h j = ((w.rotate h).getD j 0 : ℤ) − (w.getD j 0 : ℤ)` |
| never exactly one mismatch | `mismatches_ne_one` | `mismatches w h ≠ 1` for every `w : List ℕ` and `h : ℕ` |
| a differing rotation differs twice | `two_le_mismatches_of_ne` | `w.rotate h ≠ w → h < w.length → 2 ≤ mismatches w h` |

Helpers: `map_range_getD`, `mismatches_eq_countP_diff`. `ρ(w) ≥ 2` for primitive words is the last statement read over all `0 < h < m` (primitivity is exactly `w.rotate h ≠ w` for those `h`); the per-cycle form is not stated separately in Lean.

## Certificates

None: the content is the Lean module.

## Remarks

- **Scope.** Any finite word over any alphabet with a subtraction; nothing specific to valuation words. Novelty: none claimed, the argument is the standard telescoping; it is recorded because the area uses it in several places without a reference.

## History

- Written and formalised 2026-10-31 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong.
