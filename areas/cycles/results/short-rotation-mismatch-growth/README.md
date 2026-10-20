---
id: short-rotation-mismatch-growth
kind: result
title: "Short rotations of a 3x+1 cycle have mismatch counts growing like log m, and the low mismatch spectrum is sparse"
status: reviewed
claim: >
  Raw odd-only 3x+1 map (q = 1), conditional on the replayed gap gap_all (EXT-1), for a primitive integer cycle
  of period m with minimum L ≥ 2^20. Combining the rise lemma with S5's end witness, with no height
  hypothesis: (Cor. 2) every rotation with |h|_m ≤ H₀ has at least F(m, H₀) mismatches, an explicit count
  computed by a committed script (e.g. F = 28 for |h|_m ≤ 1 and 23 for |h|_m ≤ √m at m = 1.375·10^11), and
  every rotation with |h|_m ≤ m^(1−θ) has s(h) ≥ θ·log_κ m − log_κ log_κ m − O(1), about 1.5·θ·log₂ m;
  (Cor. 3) a rotation with s(h) ≤ S has |h|_m ≥ c_S·m, with c_4 = 0.0752 at m = 1.375·10^11; (Cor. 5) since
  s(h₁ − h₂) ≤ s(h₁) + s(h₂), the rotations with at most S mismatches number at most
  ⌊(m − 2H*(S))/H*(2S)⌋ + 1 (156 for S = 4 at m = 1.375·10^11), and all but m^θ rotations have at least
  (θ/2)·log_κ m − O(log log m) mismatches. Long rotations (|h|_m ≥ m/10) get at most 4, no better than ρ ≥ 4.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [rise-lemma, mismatch-height-tradeoff]
assumes: [musson-collatz-gap-all]
lean:
  - LeanLane.Cyc.OddCycle.rise_from_min_uniform
  - LeanLane.Cyc.OddCycle.log_rise_from_min
  - LeanLane.Cyc.OddCycle.mis_card_neg
  - LeanLane.Cyc.OddCycle.mis_card_le_of_add_mod
  - LeanLane.Cyc.OddCycle.mis_card_add
  - LeanLane.Cyc.OddCycle.mis_card_sub
certificates: [s13_short_rotations.py]
evidence:
  - "s13_short_rotations.py, s13_short_rotations.json: computes F(m, H₀) (exact integer search over s, bisection over B), the localization thresholds c_S and the asymptotic table from ℓ'_max = 172 + 342·log₂m − log₂3 and η at L = 2^20 (about 1 s). Exits 0 at its new path and leaves its receipt byte-identical. Passed at be73a66 as reviews/side_lane/s13_short_rotations.py (archive/legacy-checker-run-be73a66.md)"
  - "s13_corollaries.py, s13_corollaries.json: side-lane probe for Corollaries 5-7 (about 7 s): subadditivity on 3,963,083 rotation pairs of actual 3x+q cycles (m ≤ 120), the forced-letter law on 99,169 rotations of 4,218 actual cycles, and the q = 1 tables (sparsity, forced letter, ρ from the largest letter); no violation. Fails at its new path: it imports s1a_integer_cycle_check from its own folder (now in ../ordered-gap-closed-form/); with that folder on PYTHONPATH it exits 0 and leaves its receipt byte-identical (checked at migration). It also imports s13_short_rotations from this folder. Passed at be73a66 as reviews/side_lane/s13_corollaries.py (archive/legacy-checker-run-be73a66.md)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed S13 entry, update 17:40: review of S13 with independent spot checks (ℓ'_max(1.375·10^11) ≈ 12,824, F(1) = 28, F(√m) = 23, c_4 ≈ 0.0752); later review of Corollaries 5-7 ('all correct'), with the rounding-sensitive count |E_4| ≤ 156 restated exactly. Subadditivity and the orientation lemma verified as S13-c (iteration 94)"
tags: [cycles, rotation-distance, rise-lemma, linear-forms]
---

# Short rotations of a 3x+1 cycle have mismatch counts growing like log m, and the low mismatch spectrum is sparse

## Statement

Raw odd-only `3x+1` map (`q = 1`), primitive integer cycle of period `m`, minimum `L ≥ 2^20` (so `η < 5·10^(−7)`), notation of [`rise-lemma`](../rise-lemma/README.md). Assume the replayed gap `gap_all` (EXT-1, [`musson-collatz-gap-all`](../../../../sources/musson-collatz-gap-all.md)).

**Corollary 2 (short rotations, combined with S5).**
- **Inputs.** `ℓ' ≤ ℓ'_max = 172 + 342·log₂ m − log₂3`, from the drift bound `L ≤ m·2^A/(3D)` (formal: `three_L_D_le`) and `gap_all` (`2^A ≤ 2^172·m^341·D`). Corollary 2's numbers inherit the status of `gap_all`.
- **The two bounds.** S5's end witness ([`mismatch-height-tradeoff`](../mismatch-height-tradeoff/README.md)) forces `1 + t·log₂3 < ℓ' + B` on the longest run `t ≥ ⌈(m − s)/s⌉`; this weakens as `B` grows. Corollary 1 of the rise lemma strengthens as `B` grows.
- **Combination.** Taking the worse of the two over all `B` gives a guaranteed count `F(m, H₀)` for every rotation with `|h|_m ≤ H₀`. It uses no height hypothesis at all (`s13_short_rotations.py`, exact integer search over `s`, bisection over `B`).

| `m` | `|h|_m ≤ 1` | `≤ ℓ'_max` | `≤ 10ℓ'_max` | `≤ √m` | `≤ m^(3/4)` | `≤ m/1000` | `≤ m/100` | `≤ m/10` | `≤ m/3` |
|---|---|---|---|---|---|---|---|---|---|
| `2^19` | 6 | 6 | 4 | 6 | 5 | 6 | 6 | 4 | 3 |
| `10^7` | 11 | 10 | 8 | 11 | 6 | 10 | 7 | 4 | 3 |
| `1.375·10^11` | **28** | **27** | 25 | 23 | 11 | 11 | 7 | 4 | 3 |
| `10^15` | 46 | 45 | 42 | 32 | 15 | 11 | 7 | 4 | 3 |
| `10^20` | 70 | 69 | 65 | 43 | 20 | 11 | 7 | 4 | 3 |
| `10^30` | 117 | 116 | 113 | 68 | 32 | 11 | 7 | 4 | 3 |

The columns are not in increasing order of `H₀` at small `m`; for example, at `m = 2^19`, `√m = 724` while `ℓ'_max = 6,668`. `F` is nonincreasing in `H₀` at fixed `m`.

**Asymptotics.** For any `X > 0`: `s(h) ≥ min(m·log₂3/(ℓ' + X + σ), log_κ(1 + X/c) − 1)`. Take `X = m/log_κ m`. With `ℓ' = O(log m)`, every rotation with `|h|_m ≤ m^(1−θ)` then has

```
s(h) ≥ θ·log_κ m − log_κ log_κ m − O(1)
```

mismatches. Here `κ → log₂3`, so the rate is about `1.505·θ·log₂ m`. Computed values of `F(m, m^(1−θ))`:

| `m` | `θ = 1/4` | `θ = 1/2` | `θ = 3/4` | `θ = 1` |
|---|---|---|---|---|
| `10^12` | 11 | 25 | 32 | 32 |
| `10^24` | 25 | 53 | 82 | 89 |
| `10^48` | 53 | 111 | 170 | 205 |

**Corollary 3 (localization of small mismatch counts).** At fixed `S`, `F(m, H₀) ≤ S` forces `H₀` above a threshold. So a rotation with `s(h) ≤ S` must have `|h|_m ≥ c_S·m`. The thresholds are essentially independent of `m` once `m ≥ 10^11`:

| `S` | 4 | 5 | 6 | 7 | 8 | 10 | 12 | 15 |
|---|---|---|---|---|---|---|---|---|
| `c_S` at `m = 1.375·10^11` | 0.0752 | 0.0365 | 0.0187 | 0.0100 | 0.0055 | 0.0017 | 0.00057 | 0.00011 |

- S7 ([`three-mismatch-exclusion`](../three-mismatch-exclusion/README.md)) already excludes `s ≤ 3`.
- Any rotation with four mismatches, the paused `ρ ≥ 5` case ([`rotation-distance-at-least-5`](../../questions/rotation-distance-at-least-5.md)), must therefore have `|h|_m ≥ 0.075m`.
- At `m = 2^19` and `10^7`, only `S ≤ 5` and `S ≤ 10` respectively have a positive threshold (`s13_short_rotations.json`).

**Corollary 5 (the low spectrum is sparse; added 2026-10-19 after review).**
- **Subadditivity.** `s(h₁ − h₂) ≤ s(h₁) + s(h₂)`: if `a_i ≠ a_(i+h₁−h₂)`, then `i ∈ mis(h₁)` or `i + h₁ − h₂ ∈ mis(h₂)`.
- **Consequence.** Write `E_S = {h ≢ 0 : s(h) ≤ S}`. Any two of its members differ by a rotation with at most `2S` mismatches. By Corollary 3, `E_S` therefore lies in the arc `[H*(S), m − H*(S)]` with pairwise cyclic distances `≥ H*(2S)`, where `H*(S) = c_S·m` is Corollary 3's threshold. So

  ```
  |E_S| ≤ ⌊(m − 2H*(S))/H*(2S)⌋ + 1.
  ```

| `S` | 4 | 5 | 6 | 7 | 8 | 10 | 12 |
|---|---|---|---|---|---|---|---|
| `|E_S|` at most (`m = 1.375·10^11`) | 156 | 540 | 1,695 | 5,067 | 14,712 | 118,906 | 1,031,595 |

- The values are stable for larger `m`; at `10^15` they are 156, 540, 1,694, ….
- **Asymptotics.** `c_S = log₂3/(σ·S·(κ^(S+1) − 1))` up to `O(ℓ'/m)`, and `|E_S| ≤ 1/c_(2S) + 1 ≈ 0.74·S·κ^(2S+1)`. Equivalently, **all but `m^θ` rotations have at least `(θ/2)·log_κ m − O(log log m)` mismatches**.
- Without the subadditivity step, Corollary 3 alone would allow every long rotation to have few mismatches.
- **The exact count at `S = 4`** (ACK of the Lean lane's review): `H*(4)/m = 0.0752456` and `H*(8)/m = 0.0054519`, so `(m − 2H*(4))/H*(8) = 155.82` and `|E_4| ≤ 156`; rounded inputs `0.0752` and `0.0055` would give 155. Likewise `S = 5`: ratio `539.15`, `|E_5| ≤ 540`; `S = 6`: ratio `1694.34`, `|E_6| ≤ 1,695`.

## Proof

Legacy S13 note §1, Corollaries 2, 3 and 5 (side lane). The combination is Corollary 1 of [`rise-lemma`](../rise-lemma/README.md) (with `Δ = (σ + η)·|h|_m` in the better orientation) against S5's end witness on the longest run ([`mismatch-height-tradeoff`](../mismatch-height-tradeoff/README.md)), with `ℓ' ≤ ℓ'_max` from the gap. For each `m` and `H₀` the script finds the least `s` that both bounds allow for some `B`; Corollary 3 inverts it; Corollary 5 adds subadditivity (proved above, formal as `mis_card_sub`). The asymptotic statement follows by taking `X = m/log_κ m` as above.

## Certificates

`s13_short_rotations.py` recomputes every table above except Corollary 5's (thresholds `c_S`, `F(m, H₀)` and the asymptotic values) and rewrites its receipt; at migration it exited 0 and left the receipt byte-identical. Corollary 5's counts and the subadditivity check are in `s13_corollaries.py` (see `evidence`).

## Lean

Formal pieces (`lean/CycleSpectrum.lean`, namespace `LeanLane.Cyc.OddCycle`; receipts `lean/receipts/CycleSpectrum.*`): Corollary 1 (`rise_from_min_uniform`, `log_rise_from_min`, `mis_card_neg`; see [`rise-lemma`](../rise-lemma/README.md)) and Corollary 5's subadditivity (S13-c, iteration 94: `mis_card_le_of_add_mod`, `mis_card_add`, `mis_card_sub`). **Not formal:** the numerical thresholds of Corollaries 2, 3 and 5 (they use `gap_all`, EXT-1, and `ℓ'_max`), and the asymptotic statements. The status is therefore `reviewed`, not `formal`.

## Remarks

- **A growing bound for a class of rotations defined by `|h|_m` alone.** No height hypothesis and no property of the word are needed. As far as the side lane knew, it was the first such bound in the programme. S5 and S12 give growth only under a height or variation hypothesis; C011, S6 and S7 give the constants 3 and 4.
- **It moves the main objective.** Every rotation with `|h|_m = o(m)` has `s(h) → ∞`. Any hypothetical cycle with a bounded-mismatch rotation has it at a rotation by a fixed fraction of the period (Corollary 3). The open targets are [`rotation-distance-growth`](../../questions/rotation-distance-growth.md) and [`largest-letter-sublinear`](../../questions/largest-letter-sublinear.md).
- **Long rotations are unchanged.** For `|h|_m ≥ m/10` the combined count is at most 4, and S7's formal `ρ ≥ 4` is at least as strong there.
- **`L ≥ 2^20`** holds for every nontrivial cycle by the convergence verification below `2^71` ([`barina-2025-convergence-2-71`](../../../../sources/barina-2025-convergence-2-71.md)); the claim states it as a hypothesis.
- **Reviews wanted.** The legacy frontier listed the corollaries of S13 among results with no independent human review.

## History

- Split from `experiments/cycle_spectrum/S13/RISE_LEMMA.md` §1, Corollaries 2, 3 and 5 (legacy ID `S13`; side-lane producer batch S13, 2026-10-19) at commit `be73a66`, by the B06 migration (Claude, Opus 5.5). The probes `reviews/side_lane/s13_short_rotations.{py,json}` and `s13_corollaries.{py,json}` moved here (the second also serves [`largest-letter-rho-reduction`](../largest-letter-rho-reduction.md) and imports the first).
- Side lane (Claude, Opus), feed 2026-10-19 17:32 (LEAD, S13, Corollaries 2–4). Update 17:40: the Lean lane's review and spot checks; **ACK** that Corollary 2's numbers inherit EXT-1. Update 17:46: Corollaries 5 and 6. The Lean lane's review of Corollaries 5–7 ("all correct") was acknowledged with the exact `|E_S|` counts above.
