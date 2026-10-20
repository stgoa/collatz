---
id: one-cycle-exclusion-via-gap
kind: result
title: Given the linear-form gap, no 3x+1 cycle has word 1^(m−1)V for m ≥ 2^13 (a route to Steiner's theorem)
status: formal
claim: >
  Raw odd-only 3x+1 map (q = 1). For a cycle read from its minimum n_0 whose letters are a_k = 1 for k < m − 1
  (word 1^(m−1)V), D = 2^A − 3^m divides 2^(A−m) − 1, so D ≤ 2^(A−m) − 1. If moreover the linear-form gap
  2^A ≤ 2^172·m^341·D holds, then 2^m < 2^172·m^341, so no such cycle exists for m ≥ 2^13 (the exact
  threshold of the last inequality is m ≥ 4,287). Conditional on the gap; far weaker than Steiner's
  unconditional theorem on 1-cycles.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
assumes: [musson-collatz-gap-all]
lean:
  - LeanLane.Cyc.OddCycle.m_le_Apre
  - LeanLane.Cyc.OddCycle.Apre_ones
  - LeanLane.Cyc.OddCycle.Cpre_ones
  - LeanLane.Cyc.OddCycle.one_cycle_D_dvd
  - LeanLane.Cyc.OddCycle.one_cycle_D_le
  - LeanLane.Cyc.OddCycle.one_cycle_pow_lt
  - LeanLane.Cyc.OddCycle.no_one_cycle_of_gap
evidence:
  - "../attempts/four-mismatch-size-method-limit/README.md, section 4 'By-product' (legacy S08 note), and feed update 2026-10-19 15:06 (exact threshold 4,287 rechecked by the side lane in exact integers; not backed by a committed script)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed update 13:17 (the 1-cycle by-product checks out) and Lean unit S8-a verified (iteration 78; convention checked: V is the last letter a_(m−1) read from the minimum n_0)"
    link: ../../../archive/side-lane/FEED.md
tags: [cycles, one-cycles, linear-forms, known-result, formal]
---

# Given the linear-form gap, no 3x+1 cycle has word 1^(m−1)V for m ≥ 2^13 (a route to Steiner's theorem)

## Statement

Let a cycle of the raw odd-only `3x+1` map, read from its minimum `n_0`, have letters `a_k = 1` for `k < m − 1` and last letter `V = a_(m−1)` (a 1-cycle in Steiner's sense). Then

```
D = 2^A − 3^m  divides  2^(A−m) − 1,   so   D ≤ 2^(A−m) − 1.
```

If moreover `2^A ≤ 2^172·m^341·D` (`gap_all`, [`musson-collatz-gap-all`](../../../sources/musson-collatz-gap-all.md)), then `2^m < 2^172·m^341`, which fails for `m ≥ 2^13`; so no such cycle exists for `m ≥ 2^13`.

## Proof

Legacy S08 §4, by-product. For the word `1^(m−1)V`, `C_w = 3^m − 2^m` (the prefix sums are `A_j = j` for `j ≤ m − 1`). Since `n_0·D = C_w` and `3^m ≡ 2^A (mod D)`, `D | 3^m − 2^m ≡ 2^m·(2^(A−m) − 1)`, and `D` is odd, so `D | 2^(A−m) − 1` and `D ≤ 2^(A−m) − 1`. With the gap, `2^A/(2^172·m^341) ≤ D < 2^(A−m)`, i.e. `2^m < 2^172·m^341`.

## Lean

`lean/CycleSpectrum.lean`, Lean unit S8-a (iteration 78); axioms `propext`, `Classical.choice`, `Quot.sound`. In `OddCycle`: `m_le_Apre`, `Apre_ones`, `Cpre_ones` (`C_j = 3^j − 2^j` under `1^(m−1)V`), **`one_cycle_D_dvd`** (`q = 1`, `a_k = 1` for `k < m − 1` ⇒ `D ∣ 2^(A−m) − 1`), `one_cycle_D_le`, `one_cycle_pow_lt` (with the gap, `2^m < 2^172·m^341`), **`no_one_cycle_of_gap`** (with the gap and `m ≥ 2^13`, `False`). The statement matches the claim. Convention checked by the Lean lane: `V` is the last letter `a_(m−1)` read from the minimum `n_0`, and `A_j = j` for `j ≤ m − 1` matches `Cpre`'s indexing. The exact threshold `4,287` (`2^4287 ≥ 2^172·4287^341` and `2^4286 < 2^172·4286^341`) was checked by exact integer arithmetic outside Lean; the formal statement uses `2^13`.

## Remarks

- **Known result.** Nontrivial 1-cycles do not exist unconditionally (Steiner 1977, [`steiner-1977-one-cycles`](../../../sources/steiner-1977-one-cycles.md)). This is Steiner's theorem by a different route, conditional on the gap and only for `m ≥ 2^13`; it is recorded as a by-product, labelled as known.
- **The device.** "Reduce mod `D` to a small nonzero number" was proposed as the natural tool to try next on four-mismatch words ([`four-mismatch-size-method-limit`](../attempts/four-mismatch-size-method-limit/README.md)).
- Nothing about the actual Collatz map is asserted beyond these cycle hypotheses.

## History

- Created by the B05 migration (Claude, Opus 5.5) from the legacy S08 note §4 (`experiments/cycle_spectrum/S08/FOUR_MISMATCH_MAP.md` at `be73a66`; the note's headline is withdrawn, this by-product remains valid) and the feed updates of 2026-10-19 13:17 and 15:06. Side lane (Claude, Opus); formalised by the Lean lane (Claude, Fable) as part of S8-a. The note's "once `2^m > 2^172·m^341`" was first estimated as "`m ≥ ~4,200`"; the exact threshold is 4,287.
