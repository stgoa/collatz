---
id: largest-letter-rho-reduction
kind: result
title: "A low-mismatch rotation forces a letter of linear size, so ρ → ∞ follows from a largest letter of size o(m)"
status: reviewed
claim: >
  Raw odd-only 3x+1 map (q = 1), conditional on the replayed gap gap_all (EXT-1), for a primitive integer cycle
  of period m with minimum L ≥ 2^20 and largest letter a_max. (Cor. 6) A rotation h with s(h) mismatches has
  V_h ≥ 2·(B/(κ^(s+1) − 1) − ℓ' − 1 − δ), so some letter is at least 1 + V_h/s; with S5's height this is a
  letter of linear size, at least 0.0220·m for s ≤ 4, 0.0085·m for s ≤ 5 and 0.0037·m for s ≤ 6 (values
  stable in m, computed by a committed script). (Cor. 7) Hence a rotation with s(h) ≤ S forces a letter
  ≥ f(S) ≈ 2·log₂3·m/(S²(κ^(S+1) − 1)), and ρ = min_h s(h) ≥ 1 + max{S : f(S) > a_max}: ρ → ∞ whenever
  a_max = o(m), and a_max ≤ m^(1−ε) gives ρ ≥ (ε − o(1))·log_κ m. With ρ ≥ 4 (S7, which also rests on the
  period and minimum imports), every such cycle with m ≥ 1.375·10^11 and all letters below 0.022·m has
  ρ ≥ 5. No sublinear bound on a_max is known; only a_max ≤ B + ℓ' + 2 ≤ 0.585·m + O(log m).
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [rise-lemma, mismatch-height-tradeoff, denjoy-koksma-height-bound, three-mismatch-exclusion]
assumes: [musson-collatz-gap-all]
lean:
  - LeanLane.Cyc.OddCycle.sum_mu_eq_zero
  - LeanLane.Cyc.OddCycle.exists_mu_nonpos
  - LeanLane.Cyc.OddCycle.two_abs_sub_le_varMu
  - LeanLane.Cyc.OddCycle.mu_le_half_varMu
  - LeanLane.Cyc.OddCycle.forced_variation
  - LeanLane.Cyc.OddCycle.forced_letter_variation
  - LeanLane.Cyc.OddCycle.Vh_le_card_mul
  - LeanLane.Cyc.OddCycle.exists_card_mul_ge_Vh
  - LeanLane.Cyc.OddCycle.natAbs_sub_le_max
  - LeanLane.Cyc.OddCycle.exists_letter_card_mul_ge_Vh
  - LeanLane.Cyc.OddCycle.Vh_le_card_mul_of_le
  - LeanLane.Cyc.OddCycle.forced_letter_bound
  - LeanLane.Cyc.OddCycle.rise_endwitness_combination
evidence:
  - "../short-rotation-mismatch-growth/s13_corollaries.py and its receipt: the forced-letter law checked on 99,169 rotations of 4,218 actual 3x+q cycles with each cycle's own B, ℓ' and δ (minimum margin 2.68), and the q = 1 tables of Corollaries 6-7 (see that node's evidence for how it runs)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Review of Corollaries 5-7 of S13 ('all correct'), acknowledged by the side lane in the feed S13 entry; the numerical thresholds inherit EXT-1. The mechanism (averaging step, letter-bound form, the end-witness combination) verified as S13-c and S13-d (iterations 94-95)"
tags: [cycles, rotation-distance, largest-letter, rise-lemma, linear-forms]
---

# A low-mismatch rotation forces a letter of linear size, so ρ → ∞ follows from a largest letter of size o(m)

## Statement

Raw odd-only `3x+1` map, primitive integer cycle of period `m`, minimum `L ≥ 2^20`, notation of [`rise-lemma`](rise-lemma/README.md) (`ℓ' = log₂ L`, `B` the log-height, `κ = log₂3 + η`, `δ = A − m·log₂3` in bits). Assume `gap_all` (EXT-1, [`musson-collatz-gap-all`](../../../sources/musson-collatz-gap-all.md)) for the numerical parts.

**Corollary 6 (a low-mismatch rotation forces a letter of linear size).**
- `Δ⁺ ≤ max_p μ(p) ≤ Var(μ)/2 ≤ V_h/2 + δ`, because `μ(p) = y_(p+d) − y_p` has mean exactly 0 ([`denjoy-koksma-height-bound`](denjoy-koksma-height-bound/README.md), (3)). The rise lemma then gives

  ```
  V_h ≥ 2·(B/(κ^(s+1) − 1) − ℓ' − 1 − δ).
  ```

- Some mismatch has `|a_e − a_(e+h)| ≥ V_h/s`, so the cycle has a letter `≥ 1 + V_h/s`.
- At `q = 1` with S5's height ([`mismatch-height-tradeoff`](mismatch-height-tradeoff/README.md): `B > ⌈(m − s)/s⌉·log₂3 − ℓ' + 1`), the forced letter is:

| `s(h) ≤` | 4 | 5 | 6 | 7 | 8 | 10 |
|---|---|---|---|---|---|---|
| some letter at least | `0.0220m` | `0.0085m` | `0.0037m` | `0.0017m` | `0.0008m` | `0.0002m` |

  These values are stable in `m`.

**Corollary 7 (the frontier is the largest single letter).** Corollary 6 with S5's height shows that a rotation with `s(h) ≤ S` forces a letter `≥ f(S) ≈ 2·log₂3·m/(S²(κ^(S+1) − 1))`. Hence

```
ρ = min_h s(h) ≥ 1 + max{S : f(S) > a_max},     a_max = the largest letter of the cycle.
```

- **In particular, `ρ → ∞` whenever `a_max = o(m)`.** This is a strictly weaker requirement than S5's `B = o(m)`, because `a_max ≤ B + ℓ' + 2`.
- Quantitatively, `a_max ≤ m^(1−ε)` gives `ρ ≥ (ε − o(1))·log_κ m`.
- Computed values (`s13_corollaries.py`):

| `m` | `a_max ≤ m/100` | `≤ m/1000` | `≤ m^(3/4)` | `≤ √m` | `≤ 10^6` | `≤ 10^3` |
|---|---|---|---|---|---|---|
| `1.375·10^11` | `ρ ≥ 5` | 8 | 8 | 18 | 16 | 27 |
| `10^20` | 5 | 8 | 15 | 36 | 55 | 68 |
| `10^30` | 5 | 8 | 26 | 59 | 102 | 115 |

- **With S7** ([`three-mismatch-exclusion`](three-mismatch-exclusion/README.md), `ρ ≥ 4`): `ρ ≥ 5` (the paused S10 case) holds for every `q = 1` cycle with `m ≥ 1.375·10^11` and all letters below `0.022m`. At that `m`, `f(4)/m = 0.0220`, and the ratio is nondecreasing in `m`; at smaller `m` the threshold is lower. *(Scope clarified a few minutes after the feed post.)* The period `1.375·10^11` is the imported bound of [`hercher-2023-cycle-length`](../../../sources/hercher-2023-cycle-length.md); it is a hypothesis here.
- No sublinear bound on `a_max` is known here; only `a_max ≤ B + ℓ' + 2 ≤ σm + O(log m)` is proved.

## Proof

Legacy S13 note §1, Corollaries 6–7 (side lane). Corollary 6: `μ` has mean zero, so `max μ ≤ Var(μ)/2`; with `Var(μ) ≤ V_h + 2δ` this bounds the partner offset `Δ⁺`, and Corollary 1 of the rise lemma, `B + c ≤ κ^(s+1)·c` with `c = ℓ' + 1 + Δ⁺`, rearranges to the bound on `V_h`. Only mismatch positions contribute to `V_h`, so some mismatch carries at least `V_h/s`. Corollary 7: S5's end witness gives the lower bound on `B` used above; inserting it gives `f(S)`, and a cycle whose largest letter is below `f(S)` has no rotation with at most `S` mismatches.

## Lean

`lean/CycleSpectrum.lean` (axioms `propext`, `Classical.choice`, `Quot.sound`; `natAbs_sub_le_max` on `[propext, Quot.sound]`; receipts `lean/receipts/CycleSpectrum.*`), namespace `LeanLane.Cyc.OddCycle`:

- **S13-c** (iteration 94): `sum_mu_eq_zero`, `exists_mu_nonpos`, `two_abs_sub_le_varMu`, **`mu_le_half_varMu`** (`μ_h(t₀) ≤ Var(μ_h)/2`); **`forced_variation`** (`log n_j − log n₀ ≤ (κ^(s+1) − 1)(log n₀ + log 2 + Var(μ_d)/2)`) and **`forced_letter_variation`** (the same with `(V_d·log 2 + 2δ_nat)/2`): Corollary 6's inequality in natural logs, before division by `κ^(s+1) − 1`.
- **S13-d** (iteration 95): `Vh_le_card_mul`, `exists_card_mul_ge_Vh`, `natAbs_sub_le_max`, **`exists_letter_card_mul_ge_Vh`** (some letter `a_q` has `|mis d|·a_q ≥ V_d`), `Vh_le_card_mul_of_le`, **`forced_letter_bound`** (Corollary 6 when every letter is at most `A`), **`rise_endwitness_combination`** (Corollary 7's mechanism: primitive cycle, letters `≥ 1`, a rotation with `s ≥ 1` mismatches and all letters `≤ A` give `log 2 + ((m − 1)/s)·log 3 < log n₀ + (κ^(s+1) − 1)(log n₀ + log 2 + (s·A·log 2 + 2δ_nat)/2)`).

**Not formal:** the numerical thresholds (the tables, `0.0220m`, `f(S)`), which depend on `gap_all` (EXT-1) through `ℓ'_max`; Corollary 7's `ρ ≥ 5` at `m ≥ 1.375·10^11` is the numerical instance of `rise_endwitness_combination` with S7's `ρ ≥ 4`. The status is therefore `reviewed`.

## Remarks

- **This makes the obstruction rigorous.** Any configuration left over at a long rotation is a tall profile with a spike of linear size at a mismatch. That is exactly where S12 loses (the drop sits at a mismatch), where C011's product bound loses (amplitude; [`two-defect-cancellation-bound`](two-defect-cancellation-bound.md)), and where the size method stops (S7–S10: [`three-mismatch-exclusion`](three-mismatch-exclusion/README.md), [`four-mismatch-size-method-limit`](../attempts/four-mismatch-size-method-limit/README.md), [`multi-rotation-four-mismatch-exclusion`](../attempts/multi-rotation-four-mismatch-exclusion/README.md)).
- **The open configurations** are exactly the tall teeth with one large single-step drop, `v₂(3n + 1) ≥ εm`. The target is [`largest-letter-sublinear`](../questions/largest-letter-sublinear.md).
- *Heuristic (labelled; not part of the claim):* in random-like cycles the largest valuation is about `log₂ m`. A single drop of `εm` bits requires the orbit of the post-drop element `L'` to land exactly on `(2^V L' − 1)/3` after `m − 1` steps. The heuristic odds of that are about `2^(−V)` for each candidate `L'`.

## History

- Split from `experiments/cycle_spectrum/S13/RISE_LEMMA.md` §1, Corollaries 6–7 (legacy ID `S13`; side-lane producer batch S13, 2026-10-19) at commit `be73a66`, by the B06 migration (Claude, Opus 5.5). The supporting probe is in [`short-rotation-mismatch-growth`](short-rotation-mismatch-growth/README.md).
- Side lane (Claude, Opus), feed 2026-10-19 17:46 (Corollary 6) and 17:50 (Corollary 7: "the cycle-spectrum objective now reduces to the largest single letter"). **Scope clarification (17:50 + a few minutes):** the `ρ ≥ 5` statement holds at `m ≥ 1.375·10^11`; at smaller `m` the threshold is lower.
- The Lean lane reviewed Corollaries 5–7 ("all correct") and formalised the mechanism as S13-c (18:12, `1c33452`) and S13-d (18:21, `8b56b8e`).
