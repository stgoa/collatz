---
id: excursion-cut-lemma
kind: result
title: An exact endpoint relation forces every intermediate odd state, and closing two blocks gives back D·x = q·C
status: formal
claim: >
  Raw odd-only 3x+q map. (i) Cut lemma: let w be a word of positive valuations with length ℓ, total a
  and intercept C_w, and let q, x > 0 and y odd be integers, q odd, with 2^a·y = 3^ℓ·x + q·C_w. Then
  every cut state u_j = (3^j·x + q·C(w_<j))/2^(P_j) is a positive odd integer and 2^(w_j)·u_(j+1) =
  3·u_j + q exactly, so every prescribed valuation is exact. (ii) Elimination: from 2^a·y = 3^ℓ·x + q·C_E
  and 2^b·x = 3^r·y + q·C_P one gets D·x = q·C with D = 2^(a+b) − 3^(ℓ+r) and C = 3^r·C_E + 2^a·C_P,
  the intercept of the concatenated word EP. (iii) At q = 1, for a nonempty positive word with D > 0,
  an integer cycle through x exists exactly when D | C; then every phase intercept is divisible by
  D, every quotient is odd, and every cut state is a positive odd integer with exact arrows.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: []
lean:
  - LeanLane.Cyc.cut_lemma
  - LeanLane.Cyc.elimination
  - LeanLane.Cyc.D_dvd_C_of_cycle
  - LeanLane.Cyc.integer_cycle_of_dvd
  - LeanLane.Cyc.cylinders_of_dvd
  - LeanLane.Cyc.dvd_C_rotate
  - LeanLane.Cyc.odd_quot_rotate
evidence:
  - "../attempts/excursion-compression/EXCURSION_ARITHMETIC.md, sections 1-2: the written proofs"
  - "../attempts/excursion-compression/excursions_audit.json: 28,831 prefix cylinders with complementary closure on the stored cycles (historical receipt; its checker no longer runs at the new path)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 2026-10-19 03:19: cut lemma and elimination re-derived by hand; Lean unit C009-a verified (iteration 30)"
    link: ../../../archive/side-lane/FEED.md
  - by: Claude side lane (Opus)
    date: 2026-10-19
    scope: "Feed 04:09: Lean C009-a VERIFIED, statement match and receipts (sha256 18cbad0b…) checked"
    link: ../../../archive/side-lane/FEED.md
tags: [cycles, cylinders, excursions, formal]
---

# An exact endpoint relation forces every intermediate odd state, and closing two blocks gives back D·x = q·C

## Statement

For a positive valuation word `w = (w_0, …, w_(ℓ−1))` put `P_j = Σ_(i<j) w_i`, `a = P_ℓ` and `C_w = Σ_(j<ℓ) 3^(ℓ−1−j)·2^(P_j)` (NOTATION.md).

1. **Cut lemma.** If `q > 0` is odd, `x > 0`, `y` is odd and `2^a·y = 3^ℓ·x + q·C_w`, then each `u_j = (3^j·x + q·C(w_0…w_(j−1)))/2^(P_j)` is a positive odd integer, `u_0 = x`, `u_ℓ = y`, and `2^(w_j)·u_(j+1) = 3u_j + q`: every intermediate state is legal and every valuation exact. Oddness of `x` follows.
2. **Elimination.** For segments `E` (length `ℓ`, total `a`) and `P` (length `r`, total `b`), the endpoint equations `2^a·y = 3^ℓ·x + q·C_E` and `2^b·x = 3^r·y + q·C_P` imply `D·x = q·C`, with `D = 2^(a+b) − 3^(ℓ+r)` and `C = 3^r·C_E + 2^a·C_P = C_(EP)`, without approximation.
3. **Equivalence at `q = 1`.** For a nonempty positive word with `D > 0`, an odd integer cycle through `x` exists iff `D | C`; in that case `D` divides every phase intercept `C_(i)`, each `C_(i)/D` is odd, and by (1) every cut state is a positive odd integer with exact arrows.

## Proof

[`EXCURSION_ARITHMETIC.md`](../attempts/excursion-compression/EXCURSION_ARITHMETIC.md) §§1–2. Composition gives `C_w = 3^(ℓ−j)·C_j + 2^(P_j)·C_tail`; reducing the endpoint relation modulo `2^(P_j)` and cancelling the unit `3^(ℓ−j)` shows `2^(P_j) | 3^j·x + q·C_j`, so `u_j` is an integer, positive, with `2^(w_j)·u_(j+1) = 3u_j + q`. If some `u_j` with `j < ℓ` were even, the right side would be odd while the left is even (`w_j ≥ 1`); so all are odd and each valuation is exact. Elimination is a ring identity. At `q = 1`, necessity is (2); conversely `x = C/D` is a positive odd integer, the recurrence `2^(a_i)·C_(i+1) = 3C_(i) + D` with `gcd(D, 2) = 1` propagates `D | C_(i)` to every phase, and (1) recovers the cylinders.

## Lean

`lean/CycleSpectrum.lean`, Lean unit C009-a (legacy `lean/STATE.md`, now [`archive/lean-lane/STATE.md`](../../../archive/lean-lane/STATE.md), iteration 30), axioms `propext`, `Classical.choice`, `Quot.sound` (two helpers `propext` only); receipts `lean/receipts/CycleSpectrum.*`. No external input.

- `LeanLane.Cyc.cut_lemma` is (1): hypotheses positive word, `q > 0` odd, `x > 0`, `y` odd and `2^(Σw)·y = 3^|w|·x + q·C_w`; conclusions for `cutState w q x j = (3^j·x + q·C(take j w))/2^(Σ take j w)`: `u_0 = x`, `u_ℓ = y`, the cleared identity, positivity, oddness and the exact arrow. The prose's "x odd" is not assumed; it is a consequence.
- `LeanLane.Cyc.elimination` is (2) with `C_(E++P) = 3^r·C_E + 2^a·C_P` (`C_append`).
- (3) is `D_dvd_C_of_cycle` (necessity), `integer_cycle_of_dvd` and `cylinders_of_dvd` (sufficiency: `D > 0`, `D·x = C` give the positive odd integer cycle through `x` with all cut states positive odd and exact arrows), `dvd_C_rotate` and `odd_quot_rotate` (propagation to every phase, odd quotients).

Not formalised (and not part of this claim): the `k`-block Smith form `diag(1, …, 1, D)` and the scaling remark of `EXCURSION_ARITHMETIC.md` §2, recorded with the mechanism in [`excursion-compression`](../attempts/excursion-compression/README.md).

## Remarks

- **What it says.** Exact endpoint compression loses no valuation cylinder; and composing compressed blocks gives exactly the original word test. The cut lemma retains the complete intercept; an approximate or mechanical intercept would invalidate it.
- **Controls.** The ordered `q = 5` cycle `(19, 31, 49)`: excursion `31 → 49 → 19` (word `(1,3)`) and complement `19 → 31` (word `(1)`) give `16·19 = 9·31 + 5·5`, `2·31 = 3·19 + 5`, `D = 2^5 − 3^3 = 5`, `C = 3·5 + 16·1 = 31`, so `D·31 = q·C`; at `q = 1` the same shape has state `31/5`. The `q = 13` cycle `(283, 431, 653, 493, 373)`: `8·493 = 9·431 + 13·5`, `32·431 = 27·493 + 13·37`, `D = 13`, `C = 431`.
- **Novelty.** Elementary; none claimed.

## History

- Split from `experiments/cycle_spectrum/C009/` (legacy ID `C009`; `EXCURSION_ARITHMETIC.md` §§1–2) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. Formalised by the Lean lane (Claude Lean lane, Fable) as C009-a, iteration 30.
