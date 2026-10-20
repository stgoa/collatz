---
id: two-mismatch-exclusion-via-gap
kind: result
title: "C011's two-mismatch exclusion without Matveev: from the trade-off, the replayed gap and the height ceiling"
status: formal
claim: >
  Raw odd-only 3x+1 map (q = 1). Let a primitive integer cycle of period m ≥ 2^15, minimum L ≥ 2^20 and
  attained band B satisfy the linear-form gap 2^A ≤ 2^172·m^341·(2^A − 3^m). Then no nonidentity rotation of
  its valuation word differs from it in exactly two positions. (The written threshold is m ≥ 24,891, from a
  numerical scan.) With the replayed gap_all (EXT-1), Barina's verification (any nontrivial cycle has
  L > 2^71) and a period bound m ≥ 2^15 (Hercher 2023, or Eliahou 1993 in odd steps), this is C011's
  conclusion ρ(w) ≥ 3 for every hypothetical nontrivial cycle, by a route that needs no Matveev bound.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [mismatch-height-tradeoff, cycle-height-ceiling, paired-state-run-law]
assumes: [musson-collatz-gap-all, hercher-2023-cycle-length, barina-2025-convergence-2-71]
lean:
  - LeanLane.Cyc.OddCycle.two_mismatch_bound
  - LeanLane.Cyc.OddCycle.no_two_mismatch
  - LeanLane.Cyc.OddCycle.numeric_step
  - LeanLane.Cyc.OddCycle.no_two_mismatch_of_gap
evidence:
  - "s6_c011_via_s5.py, s6_c011_via_s5.json: side-lane probe (about 1 s): evaluates the s = 2 inequality at the ceiling for every m ≤ 10^6 and the slope beyond, giving m0 = 24,891. It exits 0 at the new path and leaves its receipt unchanged, but it never fails (it reports 'CHECK' instead of exiting non-zero) and does not compare with its receipt, so it is kept as evidence. Its receipt's comparison field still says 'Eliahou_1993_cycle_length: m >= 17,087,915', the uncorrected reading (see History). Passed at be73a66 as reviews/side_lane/s6_c011_via_s5.py (archive/legacy-checker-run-be73a66.md)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed update 11:47: the derivation confirmed, with two corrections (the ceiling has no +1 and carries m − 1, threshold 24,891; the minimum enters only through the threshold) and one disputed point (k-cycle framing), withdrawn by the lane at 11:59. Lean units S6-a, S6-b and S6-c verified (iterations 64-65)"
aliases: [S06]
tags: [cycles, rotation-distance, two-defect, exclusion, linear-forms, formal]
---

# C011's two-mismatch exclusion without Matveev: from the trade-off, the replayed gap and the height ceiling

## Statement

Let a nontrivial Collatz cycle (`q = 1`) be primitive, with period `m` and minimum `L`. Assume the linear-form gap `2^A ≤ 2^172·m^341·D` (`gap_all`, [`musson-collatz-gap-all`](../../../../sources/musson-collatz-gap-all.md)).

1. **Formal form.** If `m ≥ 2^15 = 32,768` and `L ≥ 2^20`, then no nonidentity rotation of its valuation word differs from it in exactly two positions.
2. **Written form.** The same holds for `m ≥ 24,891` and `L > 2^71` (the threshold from the probe's scan to `10^6` and the positive slope beyond).
3. **Applied.** Every nontrivial cycle has `L > 2^71` ([`barina-2025-convergence-2-71`](../../../../sources/barina-2025-convergence-2-71.md)) and `m` far above `2^15` ([`hercher-2023-cycle-length`](../../../../sources/hercher-2023-cycle-length.md); Eliahou's 1993 bound, [`eliahou-1993-cycle-length`](../../../../sources/eliahou-1993-cycle-length.md), already gives `m ≳ 1.08·10^7` odd steps). So every hypothetical nontrivial integer cycle has `ρ(w) ≥ 3`: C011's conclusion ([`two-defect-rotation-exclusion`](../two-defect-rotation-exclusion/README.md)).

More generally, a rotation with exactly three mismatches requires `B > 0.528m − 342·log₂ m − 172`, near the top of the possible height range (written, not formalised).

## Proof

Legacy note `C011_VIA_S5.md` (S6, side lane), lightly edited.

1. **S5-a** (Lean `mismatch_height`, formal; [`mismatch-height-tradeoff`](../mismatch-height-tradeoff/README.md)). Take `q = 1`, a gap hypothesis `2^A ≤ 2^c·m^μ·D`, and `h ≢ 0`. Then there is a `t` with `m ≤ s(t+1)` and `6·3^t < 2^(B+1+c)·m^(μ+1)`.
2. **`gap_all`** (`mmusson/collatz`, replayed as EXT-1, standard axioms) supplies the gap hypothesis with `(c, μ) = (172, 341)`.
3. **The height ceiling** ([`cycle-height-ceiling`](../cycle-height-ceiling.md), the Lean lane's argument in its S5 review; formal as S6-a). Along the arc from the minimum to the maximum, each step multiplies by `(3 + 1/n_i)/2^(a_i) ≤ (3/2)(1 + 1/(3L))`. So `B ≤ (log₂ 3 − 1)(m − 1) + (m − 1)·log₂(1 + 1/(3L))`. With `L > 2^71` the last term is below `10^(−20)·m`.
4. **Combining.** If `s = 2`, then `t ≥ ceil(m/2) − 1`. Taking logarithms gives `log₂ 6 + (ceil(m/2) − 1)·log₂ 3 < (log₂ 3 − 1)(m − 1) + 173 + ε + 342·log₂ m`. The left side grows like `0.792m` and the right like `0.585m + 342·log₂ m`. The probe finds the inequality false for every `m ≥ 24,891`, and the slope is positive from `m ≥ 2^12` on.
5. **`s = 3`.** Here `t ≥ ceil(m/3) − 1`, which gives `B > (log₂ 3/3)·m − 342·log₂ m − O(1) ≈ 0.528m − 342·log₂ m − 172`.

## Lean

`lean/CycleSpectrum.lean`, Lean units S6-a (the ceiling, see [`cycle-height-ceiling`](../cycle-height-ceiling.md)) and S6-b/c (iteration 65); axioms `propext`, `Classical.choice`, `Quot.sound`. In `OddCycle`:

- `two_mismatch_bound`: primitive, `q = 1`, gap `(c, μ)`, attained `B`, `h % m ≠ 0`, `(mis h).card = 2` ⇒ `∃ t, m ≤ 2(t+1) ∧ log 6 + t·log 3 < (m−1)(log 3 − log 2) + (m−1)·log(1 + 1/(3L)) + (1+c)·log 2 + (μ+1)·log m` (S5-a at `s = 2` with the ceiling: steps 1–4 up to the numeric evaluation).
- `no_two_mismatch`: the exclusion with the numeric step as an explicit hypothesis; `numeric_step`: the numeric step for `m ≥ 2^15`, `L ≥ 2^20`, `(c, μ) = (172, 341)` (Mathlib's `log 2` decimals, `3^41 < 2^65` and `2^19 < 3^12` giving `19/12 < log₂3 < 65/41`, the tangent bound on `log m`, `log(1+x) ≤ x`).
- **`no_two_mismatch_of_gap`**: primitive, `q = 1`, `2^A ≤ 2^172·m^341·D`, attained `B`, `m ≥ 2^15`, `L ≥ 2^20`, `h % m ≠ 0` ⇒ `(mis h).card ≠ 2`. This is part 1 of the Statement exactly.

The gap is a hypothesis standing for `gap_all`, proved in `mmusson/collatz` and replayed there as EXT-1, not imported into this file. The threshold `2^15` replaces the side lane's exact 24,891 for a clean formal proof; `L ≥ 2^20` replaces `L > 2^71` (§3 already notes `L ≥ 2^20` suffices). The period input remains an explicit hypothesis. The `s = 3` clause is not formalised (it is `mismatch_height` at `s = 3` read as a lower bound on `B`). Parts 2–3 of the Statement are part 1 with the imported inputs.

## Remarks

**What changes compared with C011.**

| | C011 (main) | S6 |
|---|---|---|
| Linear-forms input | Matveev (Languasco–Luca–Moree–Togbe), `K_0 < 6·10^8`, imported, not formal | `gap_all`, formal in `mmusson/collatz` and replayed here (EXT-1) |
| Period input | `m > 1.375·10^11` (Hercher/Barina) | `m ≥ 24,891` (formal: `m ≥ 2^15`) |
| Minimum input | (through the period input) | `L > 2^71` (Barina), used only to make the `ε` term negligible; any `L ≥ 2^20` suffices |
| Formal status | written proof with two imports | S5-a formal; `gap_all` formal elsewhere; the ceiling elementary (formal later as S6-a, and the whole route as S6-b/c, given the gap); the period input imported |

For the period input, Hercher's bound or even Eliahou's 1993 bound is far more than needed. *[Corrected 2026-10-19: Eliahou's 17,087,915 bounds the total cycle length `A`, so in odd steps it gives `m ≳ 1.08·10^7`. An earlier version wrote `m ≥ 17,087,915`.]*

**Remarks from the Lean lane's review.**

- **The minimum enters only through the threshold.** The slope comparison needs `log₂(1 + 1/(3L)) < log₂3/2 − (log₂ 3 − 1) ≈ 0.2075`, which holds for `L ≥ 3`. So the exclusion holds eventually for every positive cycle; `L ≥ 2^20` only fixes the threshold, and `L > 2^71` makes the term negligible. The result is really about the period.
- **The relation to the k-cycle literature.** Simons–de Weger ([`simons-2005-m-cycles`](../../../../sources/simons-2005-m-cycles.md)) and its successors exclude cycles with few local minima (k-cycles). The two-defect class is a different kind of low complexity: words that are near-periodic with one defect pair, which can have about `m/3` local minima. Example: the positive-range words `x(122)^k`, with one inserted letter, have a rotation by 3 with exactly two mismatches; at `m = 118` they have 78 run boundaries. So the k-cycle results do not cover C011's class. (The Lean lane first suggested the class was covered by the k-cycle literature; it withdrew that point at 11:59.)

**Limits.**

- **Not a new exclusion.** C011's statement is unchanged; what changes is the route, which no longer needs Matveev. No cycle is excluded outright: cycles with `m < 2^15` are outside the formal statement.
- **The period input is still computational.** Some computation must rule out cycles of period below 24,891 (formally, `2^15`).
- **The `s = 3` clause** is the trade-off at its top end: three mismatches are possible only for nearly maximal height. It is superseded by [`three-mismatch-exclusion`](../three-mismatch-exclusion/README.md).
- **Controls.** Actual `3x+q` cycles with two-mismatch rotations (e.g. at `q = 5, 7, 13`) are allowed: the gap bounds `L` only at `q = 1`, and the claim is about `q = 1`.
- Novelty undetermined. The side lane's two web searches (feed 11:49, calibration only) found no prior exclusion of near-periodic two-defect cycle words.

## History

- Migrated from `experiments/cycle_spectrum/S06/C011_VIA_S5.md` (legacy ID `S06`; side-lane producer batch S6, 2026-10-19, "a written derivation from formal and replayed components plus one elementary inequality; it proves no new exclusion") at commit `be73a66`, by the B05 migration (Claude, Opus 5.5). The side-lane probe `reviews/side_lane/s6_c011_via_s5.{py,json}` moved here.
- Side lane (Claude, Opus), feed 2026-10-19 11:40 (headline threshold `m ≥ 24,895`).
- **Correction (2026-10-19 11:47, the Lean lane's review).** The ceiling has no `+ 1`, and the `ε` term carries `(m − 1)`: the threshold became `m0 = 24,891`. The minimum enters only through the threshold.
- **Dispute (11:47, resolved 11:59).** The Lean lane suggested the two-defect class was already excluded by the k-cycle literature; the side lane disagreed (§ Remarks); the Lean lane withdrew the point.
- **Correction (2026-10-19 13:03, citation).** Eliahou's 17,087,915 bounds the total cycle length `A`, not `m`; in odd steps it gives `m ≳ 1.08·10^7`. The note was corrected; the probe's receipt (pinned, not edited) still carries the old wording.
- Formalised by the Lean lane (Claude, Fable) as S6-a (iteration 64, feed 11:59) and S6-b/c (iteration 65, feed 12:35), against the corrected note (legacy commits `a3c4d91`, corrected `6cff0f3`).
