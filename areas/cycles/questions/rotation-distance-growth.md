---
id: rotation-distance-growth
kind: question
title: Must the rotation distance of a nontrivial 3x+1 cycle grow with its period?
status: open
claim: >
  Find an explicit F(m) → ∞ such that the primitive valuation word w of every hypothetical
  nontrivial integer cycle of the odd-only 3x+1 map (period m) satisfies ρ(w) ≥ F(m), where
  ρ(w) = min over nonidentity rotations r of #{i : a_i ≠ a_(i+r mod m)}. A bound of order m/log m would
  be a stronger outcome. Intermediate target under the all-cycle goal: high-complexity cycles would
  remain possible.
created: 2026-10-19
tags: [cycles, rotation-distance, frontier]
---

# Must the rotation distance of a nontrivial 3x+1 cycle grow with its period?

## Question

For a word `w` of primitive period `m`, `ρ(w) = min_(1 ≤ r < m) #{i : a_i ≠ a_(i+r mod m)}` ([`conventions/NOTATION.md`](../../../conventions/NOTATION.md)). Find an explicit `F(m) → ∞` with `ρ(w) ≥ F(m)` for every hypothetical nontrivial integer cycle of the odd-only `3x+1` map. Constant bounds proved one count at a time do not answer it.

## Why it matters

It is a uniform structural restriction on every hypothetical cycle, specific to `d = 1` through `q = 1`, and strictly weaker than excluding all cycles (high-complexity cycles would remain). It was the recommended intermediate target of the legacy C012 and C013 batches and was endorsed by the side-lane referee (feed 2026-10-19 04:35). Actual `3x+d` cycles (e.g. `d = 5, 7, 13`) have small `ρ`, so any proof must use `q = 1`.

## Known progress

- `ρ ≥ 3`, conditional on published inputs: [`two-defect-rotation-exclusion`](../results/two-defect-rotation-exclusion/README.md).
- Later side-lane results: S05 ([`mismatch-height-tradeoff`](../results/mismatch-height-tradeoff/README.md)) reduces the question to a height bound, see [`cycle-height-bound`](cycle-height-bound.md); S06 ([`two-mismatch-exclusion-via-gap`](../results/two-mismatch-exclusion-via-gap/README.md)) re-derives `ρ ≥ 3` from the replayed gap EXT-1 ([`musson-collatz-gap-all`](../../../sources/musson-collatz-gap-all.md)); S07 ([`three-mismatch-exclusion`](../results/three-mismatch-exclusion/README.md)) excludes exactly three mismatches for `m ≥ 452,695`, so `ρ ≥ 4` with the period input, formal given the gap (feed 2026-10-19 14:20); S08's claim that size arguments stop at three mismatches was withdrawn the same day ([`four-mismatch-size-method-limit`](../attempts/four-mismatch-size-method-limit/README.md)); whether they reach `ρ ≥ 5` is open. Not yet migrated (legacy `experiments/cycle_spectrum/S12/`, `S13/`): S13 shows short rotations of a `q = 1` cycle have mismatch counts growing like `log m` (rise lemma).
- A growth law for one structured class: [`shared-background-denominator-law`](../results/shared-background-denominator-law/README.md) forces the number `r` of copies of one shared background to grow like `√(m/log m)` at bounded marker average; `r` is not the mismatch count.
- A sufficient candidate: [`rotation-defect-denominator-candidate`](rotation-defect-denominator-candidate.md) would give `ρ = Ω(m/log m)`.
- Obstructions to shortcuts: [`termwise-plateau-divisibility`](../attempts/termwise-plateau-divisibility.md), [`fixed-defect-unbounded-cancellation`](../results/fixed-defect-unbounded-cancellation.md), [`coupled-defect-matrix-smith-form`](../results/coupled-defect-matrix-smith-form/README.md), [`three-defect-arbitrary-background`](../results/three-defect-arbitrary-background.md), [`distance-three-height-family`](../results/distance-three-height-family.md) (bounded `ρ` does not bound height), and the unreviewed C014 coverage obstructions [`compatible-arcs-common-partition-limits`](../results/compatible-arcs-common-partition-limits/README.md) and [`rotated-residual-resultant-invariance`](../results/rotated-residual-resultant-invariance.md).

## Suggested attacks

From the legacy reports (C012–C014), marked as their authors' proposals:

- Exploit how the shared arcs overlap inside the same word: transfer the polynomial factor extraction of the shared-background law to distinct but compatible overlapping arcs, charging every numerical gcd and resultant term; seek a consequence uniform in mismatch count and height.
- Keep the distinguished evaluation point `X = 3` and the actual overlapping pieces; scalar resultants from more rotations do not restore the information they discard (C014 draft, unreviewed).
- If a bounded discrimination probe cannot retain the overlap information, compare another mechanism rather than extending a fixed-count catalogue.
