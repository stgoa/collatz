---
id: three-mismatch-exclusion
kind: result
title: No rotation of a nontrivial 3x+1 cycle differs from it in exactly three positions, so ρ ≥ 4
status: formal
claim: >
  Raw odd-only 3x+1 map (q = 1). Let a primitive integer cycle of period m ≥ 2^19, minimum L ≥ 2^20 satisfy
  the linear-form gap 2^A ≤ 2^172·m^341·(2^A − 3^m). Then no rotation h with 1 ≤ h < m of its valuation word
  differs from it in exactly three positions; if moreover its band is attained, every such rotation differs in
  at least four positions (ρ(w) ≥ 4), combining the exclusion of zero and one mismatch (primitivity, equal
  totals) and of exactly two (two-mismatch-exclusion-via-gap). The written threshold is m ≥ 452,695, from a
  numerical scan. With the replayed gap_all (EXT-1), Barina's L > 2^71 and a period bound above 2^19
  (Hercher 2023, or Eliahou 1993 in odd steps), every hypothetical nontrivial integer cycle has ρ(w) ≥ 4.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [two-mismatch-exclusion-via-gap, mismatch-height-tradeoff, cycle-height-ceiling, paired-state-run-law]
assumes: [musson-collatz-gap-all, hercher-2023-cycle-length, barina-2025-convergence-2-71]
lean:
  - LeanLane.Cyc.OddCycle.z_pos_step
  - LeanLane.Cyc.OddCycle.z_neg_step
  - LeanLane.Cyc.OddCycle.z_pos_run
  - LeanLane.Cyc.OddCycle.z_neg_run
  - LeanLane.Cyc.OddCycle.z_min_pos
  - LeanLane.Cyc.OddCycle.z_pred_min_neg
  - LeanLane.Cyc.OddCycle.z_max_neg
  - LeanLane.Cyc.OddCycle.z_pred_max_pos
  - LeanLane.Cyc.OddCycle.sum_a_shift
  - LeanLane.Cyc.OddCycle.mis_card_ne_one
  - LeanLane.Cyc.OddCycle.witness_gt
  - LeanLane.Cyc.OddCycle.n_mul_pow_excess_le
  - LeanLane.Cyc.OddCycle.h_add_excess_le
  - LeanLane.Cyc.OddCycle.card_down_eq_card_up
  - LeanLane.Cyc.OddCycle.down_mem_mis
  - LeanLane.Cyc.OddCycle.up_mem_mis
  - LeanLane.Cyc.OddCycle.exists_down_window
  - LeanLane.Cyc.OddCycle.exists_up_window
  - LeanLane.Cyc.OddCycle.three_mismatch_changes
  - LeanLane.Cyc.OddCycle.excess_add_dexcess
  - LeanLane.Cyc.OddCycle.dexcess_le_two_excess
  - LeanLane.Cyc.OddCycle.alignment
  - LeanLane.Cyc.OddCycle.window_conditions
  - LeanLane.Cyc.OddCycle.unique_in_window
  - LeanLane.Cyc.OddCycle.agree_of_window
  - LeanLane.Cyc.OddCycle.three_mismatch_structure
  - LeanLane.Cyc.OddCycle.run_bound_max
  - LeanLane.Cyc.OddCycle.arc_le
  - LeanLane.Cyc.OddCycle.hsep_of_runs
  - LeanLane.Cyc.OddCycle.three_mismatch_witness
  - LeanLane.Cyc.OddCycle.log_three_bounds
  - LeanLane.Cyc.OddCycle.numeric_WA
  - LeanLane.Cyc.OddCycle.numeric_F
  - LeanLane.Cyc.OddCycle.no_three_mismatch_of_gap
  - LeanLane.Cyc.OddCycle.four_le_mis_card_of_gap
evidence:
  - "s7_three_mismatch.py, s7_three_mismatch.json: side-lane probe (about 15-25 s): Part 1 scans the conditions W, A, P, F for every m ≤ 10^7 at the worst case ℓ = ℓ*(m) and finds m0 = 452,695; Part 2 checks the q-independent steps on 616 actual 3x+q cycles. Fails at its new path: it imports the side-lane helper s1a_integer_cycle_check from its own folder (now in ../ordered-gap-closed-form/); with that folder on PYTHONPATH it exits 0 and rewrites its receipt byte for byte (checked at migration). Passed at be73a66 as reviews/side_lane/s7_three_mismatch.py (archive/legacy-checker-run-be73a66.md)"
  - "s7_stress_rational.py: the independent review agent's stress test, as a side-lane probe (no receipt). Needs arguments: run as python3 <this folder>/s7_stress_rational.py 3 14 (about 30 s), it tests Steps 2-5 on every primitive word over {1, 2, 3} up to length 14 and reports 5,116 three-mismatch rotations with no failure (re-run at migration: same counts, fails: []). Fails bare (exit 1 at be73a66 as reviews/side_lane/s7_stress_rational.py, archive/legacy-checker-run-be73a66.md)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed update 12:48: adversarial review of Steps 3-5, line by line, found no gap ('given the four numeric conditions W, A, P, F at ℓ = ℓ*(m), the written proof excludes s = 3'); four explicitness points applied. Lean units S7-a, S7-b (parts 1, 2, 3a, 3b), S7-c (parts 1, 2) and S7-d (parts 1, 2) verified (iterations 66-74)"
    link: ../../../../archive/side-lane/FEED.md
aliases: [S07]
tags: [cycles, rotation-distance, exclusion, linear-forms, formal]
---

# No rotation of a nontrivial 3x+1 cycle differs from it in exactly three positions, so ρ ≥ 4

## Statement

Raw odd-only `3x+1` map (`q = 1`), primitive integer cycle of period `m`, minimum `L`, total `A`, `D = 2^A − 3^m`. Assume the linear-form gap `2^A ≤ 2^172·m^341·D` (`gap_all`, [`musson-collatz-gap-all`](../../../../sources/musson-collatz-gap-all.md)).

1. **Formal form.** If `m ≥ 2^19 = 524,288` and `L ≥ 2^20`, then no rotation `1 ≤ h < m` of the valuation word differs from it in exactly three positions. If moreover the band is attained, every such rotation differs in at least four positions: `ρ(w) ≥ 4`.
2. **Written form.** The exclusion of exactly three holds for `m ≥ 452,695` and `L > 2^71`.
3. **Applied.** With Barina's `L > 2^71` ([`barina-2025-convergence-2-71`](../../../../sources/barina-2025-convergence-2-71.md)) and a period bound above `2^19` ([`hercher-2023-cycle-length`](../../../../sources/hercher-2023-cycle-length.md); Eliahou's bound, [`eliahou-1993-cycle-length`](../../../../sources/eliahou-1993-cycle-length.md), gives `m ≳ 1.08·10^7` odd steps), every hypothetical nontrivial Collatz cycle has `ρ(w) ≥ 4`, improving `ρ ≥ 3` of [`two-defect-rotation-exclusion`](../two-defect-rotation-exclusion/README.md) and [`two-mismatch-exclusion-via-gap`](../two-mismatch-exclusion-via-gap/README.md).

**Notation in this node.** As in the legacy note, `δ_i = n_(i+h) − n_i` is the state difference of the rotation (the `z_i` of [`paired-state-run-law`](../paired-state-run-law.md)), not the drift `δ` of `conventions/NOTATION.md`; `ℓ = log₂ L`; `ε = log₂(1 + 1/(3L))`; `κ = log₂(3/2) + ε`.

## Proof

Legacy note `THREE_MISMATCHES.md` (S7, side lane), §§1–3, lightly edited. Its status line read: "A written proof from elementary steps, plus the replayed `gap_all` and two imports (Barina's minimum, a period bound). There is a probe for the threshold and controls on actual `3x+q` cycles. The Lean lane reviewed it adversarially and found no gap (§5a). The sign lemma is formal (S7-a). Novelty undetermined."

### 1. The surrounding counts

- Every nonidentity rotation differs in at least one position, by primitivity. It never differs in exactly one, because the totals agree: `Σ a_i = Σ a_(i+h)` (Lean `mis_card_ne_one`).
- C011 (main, [`two-defect-rotation-exclusion`](../two-defect-rotation-exclusion/README.md)), or S6 ([`two-mismatch-exclusion-via-gap`](../two-mismatch-exclusion-via-gap/README.md), formal as S6-b/c for `m ≥ 2^15`), excludes exactly two.
- So with any period import above 452,695, for example Eliahou's bound (total cycle length `A ≥ 17,087,915`, so `m ≳ 1.08·10^7` odd steps) or the Hercher/Barina bound used in C011, **every nonidentity rotation of a hypothetical nontrivial Collatz cycle differs in at least four positions**. In main's notation that is `ρ(w) ≥ 4`; C011 gave `ρ(w) ≥ 3`.

### 2. Setting and four standing facts

- **The cycle.** Odd states `n_i` (indices mod `m`), all distinct. The arrows are `2^(a_i) n_(i+1) = 3n_i + 1` with every `a_i ≥ 1`, and `A = Σ a_i`, `D = 2^A − 3^m > 0`. Index 0 is the minimum `L`, `j` is the position of the maximum `H`, and `ℓ = log₂ L`. (This `ℓ` is the logarithm of the minimum. It is not the additive constant in S5's trade-off.)
- **The rotation.** For a rotation `h ≢ 0`, put `δ_i = n_(i+h) − n_i`. It is nonzero (distinct states) and even.
  - The mismatch set is `M = {i : a_i ≠ a_(i+h)}`, with `|M| = s`.
  - The mismatches cut the circle into `s` agreeing runs, of lengths `t_k ≥ 0` with `Σ t_k = m − s`.

**(F1) The run law with witnesses** (main's `OVERLAP_THEORY` §1; Lean `q_bound_rational` family).
- At an agreeing position `i`, `2^(a_i) δ_(i+1) = 3δ_i`.
- So along a run of length `t` that ends at the mismatch `e`, `2^E δ_e = 3^t δ_(start)`. Hence `3^t | δ_e`, and since `δ_e` is even, `|δ_e| ≥ 2·3^t`.
- The **witness** of that run is the larger of the two states compared: `z = e + h` if `δ_e > 0`, and `z = e` if `δ_e < 0`. It satisfies `n_z > 2·3^t`.

**(F2) Sign persistence.** By (F1), `δ` keeps its sign at every agreeing position. It can change sign only at mismatches. Going once round the cycle, there are as many `+ → −` changes as `− → +` changes.

**(F3) The ceiling from the minimum** (Lean S6-a, `n_le_climb`). Put `κ = log₂(3/2) + ε` with `ε = log₂(1 + 1/(3L))`.
- For every index `0 ≤ k ≤ m − 1`, counting letters forward from the minimum: `log₂ n_k ≤ ℓ + k·κ`. This holds at every index, in the climb or not, because every letter is at least 1.
- Tracking the letters, `log₂(n_k / L) ≤ kκ − Σ_(i<k)(a_i − 1)`.

**(F4) The size of the minimum.**
- `Σ log(1 + 1/(3n_i)) = log(2^A/3^m) ≥ D/2^A`, and the left side is at most `m/(3L)`. So `L ≤ m 2^A/(3D)`.
- With `gap_all` (`2^A ≤ 2^172 m^341 D`; replayed as EXT-1), `ℓ ≤ ℓ*(m) = 172 + 342 log₂ m − log₂ 3`. The formal pieces are the Lean lane's `L_mul_delta_le` and `delta_ge_gap`, plus the gap.

### 3. Proof (`s = 3`)

**Step 1 (sizes).**
- Each witness has `n_z ≤ H ≤ L·2^((m−1)κ)`. So every run satisfies `t ≤ t_max`, the largest integer below `T = (ℓ + (m−1)κ − 1)/log₂ 3 ≈ 0.369m + 0.631ℓ`. This `t_max` is a uniform bound on every run, not the length of the longest one.
- The three runs sum to `m − 3`, so every run has length at least `m − 3 − 2t_max ≈ 0.262m − 1.26ℓ`. Write `σ_min = m − 2(t_max + 1)` for the resulting lower bound on the **spacing** (run length plus one) between consecutive mismatches. "Spacing" is used to avoid the programme's `gap`, which means `Δ_r`.
- The longest run has length at least `t* = ⌈(m−3)/3⌉`, so `log₂ H > 1 + t* log₂ 3`. `X*` and `d*` below use this worst case, the smallest possible longest run, which makes them as large as possible. Combined with (F3) up to `j`:
  - the **climb excess** `X_c = Σ_(i<j)(a_i − 1)` satisfies `X_c < X* = (m−1)κ − 1 − t* log₂ 3 + ℓ ≈ 0.057m + ℓ`. The climb bound used is `log₂(H/L) ≤ jκ − X_c`, the exact form of S6-a's `h_le_climb`.
  - the **descent window** `W = [j, m)` has length `d = m − j < d* = m − (1 + t* log₂ 3 − ℓ)/κ ≈ 0.097m + 1.71ℓ`. Keeping `X_c` gives the sharper `d < d* − X_c/κ`, which is not needed.

**Step 2 (two sign changes, located).**
- `δ_(j−h) = H − n_(j−h) > 0` and `δ_(m−h) = L − n_(m−h) < 0`. So some mismatch `e_a ∈ W − h = [j−h, m−h)` is a `+ → −` change.
- `δ_j = n_(j+h) − H < 0` and `δ_m = n_h − L > 0`. So some mismatch `e_b ∈ W` is a `− → +` change.
- By (F2) the number of changes is even and at most three, so it is exactly two. The third mismatch `e_c` is not a change.
- So `δ < 0` on the forward stretch `(e_a, e_b]` and `δ > 0` on `(e_b, e_a]`.

**Step 3 (the windows are disjoint).** Take the representative `1 ≤ h ≤ m − 1`. Both window conditions are needed: `d ≤ h ≤ m − d`.
- Suppose `h < d` or `h > m − d`. Then `W` and `W − h` overlap.
  - If `h < d`, the union is `[j − h, m)`, of length `d + h ≤ 2d − 1`.
  - If `h > m − d`, the union wraps: it is `[j, m) ∪ [0, m − h)`, of length `d + (m − h) ≤ 2d − 1`.
  - The union contains `e_a` and `e_b`. They are distinct because their change types differ (`+ → −` against `− → +`). So two mismatches would lie in an arc of at most `2d − 1` positions, while every two mismatches are at least `σ_min` apart. Condition **W**, `σ_min ≥ 2d_max − 1`, rules this out.
- With `h ≥ d`, the copies `W + h = [j + h − m, h)` start at or after index 0. With `h ≤ m − d = j`, they end at or before `j`. So `W + h ⊂ [0, j)`, the climb, and symmetrically `W − h ⊂ [0, j)`.
- Each of `W` and `W − h` contains exactly one mismatch, `e_b` and `e_a` respectively. This uses `σ_min > d_max`, which condition W also covers. It is the second place where `m ≥ m0` enters.

**Step 4 (alignment: `e_a + h = e_b`).**
- Every `i ∈ W` other than `e_b` is agreeing, so `a_i = a_(i+h)` with `i + h` in the climb. Hence `Σ_(W ∖ {e_b}) (a_i − 1) ≤ X_c`.
- Likewise every `i ∈ W` other than `e_a + h` has `a_i = a_(i−h)` with `i − h` in the climb.
- If `e_a + h ≠ e_b`, then `e_b − h ∈ W − h` is not a mismatch, so `a_(e_b) = a_(e_b − h)` is a climb letter and `a_(e_b) − 1 ≤ X_c`. With the first estimate this gives `X_d ≤ 2X_c`, where `X_d = Σ_W (a_i − 1)`. (This is the Lean lane's shorter form. Adding the two estimates gives the same conclusion.)
- Then `A − m = X_c + X_d ≤ 3X_c < 3X*`. Condition **A**, `⌈m log₂ 3⌉ − m ≥ 3X*`, contradicts this. So `x := e_b = e_a + h`.
- A by-product: the excess in `W` sits at `x`, with `a_x − 1 ≥ X_d − X_c > A − m − 2X* ≈ 0.47m`. The whole descent is one huge letter.

**Step 5 (the third witness lies inside the climb).** The mismatches are `x − h`, `x` and `e_c`. There are two cyclic orders.

- **Order 1: `x − h → x → e_c` (forward).**
  - The run `(x, e_c)`, of length `t′`, ends at `e_c`. That position lies in the stretch `(x, x − h]`, where `δ > 0`, so the larger of the two compared states is `n_(e_c + h)`. Its witness is `z = e_c + h`, with `n_z > 2·3^(t′)`.
  - The forward spacings are `t + 1` (from `x − h` to `x`), `t′ + 1` and `t″ + 1`, and they sum to `m`. So `z ≡ x − (t″ + 1)`.
  - As an index, `x ∈ [j, m − 1]`. Condition **P** (`m − d_max ≥ t_max + 1`) gives `x ≥ t″ + 1`. P is in fact implied by Step 3, since `(x, m)` lies inside `W` and holds no mismatch, so `e_c < x − h`. An independent review found that it never binds; it is kept as a check. So `z` is the integer `x − (t″ + 1) ∈ [0, m)`, `n_z = n_(e_c + h)` by the congruence, and `z ≤ m − 2 − t″ = t + t′ + 1`.
  - Since `t″ + 1 > d`, also `z < m − d = j`. So `z` is a climb index, reached forward from the minimum. (F3) would apply at any index anyway.
- **Order 2: `x − h → e_c → x`.**
  - The run `(x − h, e_c)`, of length `t₁`, ends at `e_c`. That position lies in `(x − h, x]`, where `δ < 0`, so the larger state is `n_(e_c)` itself. Its witness is `z = e_c`.
  - As an index, `z = x − (t₂ + 1) ≤ t₁ + t₃ + 1`, where `t₂` is the run `(e_c, x)` and `t₃` the run `(x, x − h)`. Again `z < j`, so there is no wrap.
- **In both orders** one run `τ` has its witness at an index at most `τ + τ° + 1`, where `τ°` is one of the other two runs. By (F1) and (F3), `τ log₂ 3 + 1 < ℓ + (τ + τ° + 1)κ`.
- Since `log₂ 3 − κ = 1 − ε`, this gives `τ (1 − ε) < ℓ + (τ° + 1)κ − 1 ≤ ℓ + (t_max + 1)κ − 1`. So `τ ≲ ℓ + 0.585·t_max`.

**Step 6 (the count).** The special run `τ` is at most `τ_max`, the largest integer below `(ℓ + (t_max + 1)κ − 1)/(1 − ε)`. The other two runs are each at most `t_max`, because `t_max` bounds every run. So `m − 3 = Σ t_k ≤ 2t_max + τ_max ≈ 0.954m + 2.63ℓ`. Condition **F** contradicts this. ∎

**Thresholds.** All four conditions get harder as `ℓ` or `ε` grows. So they are evaluated at `ℓ = ℓ*(m)` (from F4) and `ε` at `L = 2^71`.
- The probe scans every `m` up to `10^7`. The last failure is at `m = 452,694`, where condition W binds.
- Beyond the scan the margins grow linearly. Condition W's margin is about `0.069m − 4.68ℓ*(m)`, which increases for `m > 3.4·10^4`, and the others behave alike.
- Hence `m0 = 452,695`.

## Lean

`lean/CycleSpectrum.lean`, Lean units S7-a to S7-d (iterations 66–74); axioms `propext`, `Classical.choice`, `Quot.sound` (`pred_add_mod`: `propext`, `Quot.sound`; seven periodicity helpers on `propext` only); receipts `lean/receipts/CycleSpectrum.*`. In `OddCycle`, with `z h i = n_(i+h) − n_i` (the note's `δ_i`):

- **S7-a (F2, signs).** `z_pos_step`, `z_neg_step`, `z_pos_run`, `z_neg_run` (the sign is constant across an agreeing step and run); `z_min_pos`, `z_pred_min_neg`, `z_max_neg`, `z_pred_max_pos` (the four strict signs of Step 2 at `0`, `−h`, `j`, `j − h`; `−h` is written `m − h % m`).
- **S7-b part 1.** `sum_a_shift`, `mis_card_ne_one` (`s ≠ 1` from the equal totals, no primitivity); `witness_gt` ((F1) at a run's end: `2·3^t < max(n_(i+t), n_(i+t+h))`); `n_mul_pow_excess_le`, `h_add_excess_le` ((F3) tracked, for any `q` with letters `≥ 1`).
- **S7-b part 2 (Step 2).** `card_down_eq_card_up` (as many `+→−` as `−→+` changes, by the telescoping sum `sum_sgn_tele`), `down_mem_mis`, `up_mem_mis`, `exists_down_window`, `exists_up_window`, `three_mismatch_changes` (with three mismatches exactly one change of each kind and a third mismatch with no change).
- **S7-b parts 3a/3b (Steps 3–4).** `excess_add_dexcess` (`X_c + X_d + m = A`), `dexcess_le_two_excess`, `alignment`; `window_conditions` (`2d ≤ σ + 1` ⇒ `d ≤ h ≤ j`), `unique_in_window`, `agree_of_window`, `three_mismatch_structure` (Steps 2–4 assembled; it needs no card-3 hypothesis, only the spacing bound and condition A).
- **S7-c (Steps 1, 5, 6).** `run_bound_max` (uniform run bound), `arc_le`, `hsep_of_runs` (the spacing `σ = m − 2(T + 1)`, the only place `s = 3` enters), `three_mismatch_witness` (Step 5 in product form, with the three runs and their sum `m − 3`; the orders are the cases `e_c < e_a` and `e_a < e_c < e_b`, and condition P is not needed).
- **S7-d (numbers and assembly).** `log_three_bounds` (`1054·log 2 < 665·log 3`, `306·log 3 < 485·log 2`), `numeric_WA` (conditions W and A at `m ≥ 2^19`), `numeric_F` (the final contradiction); **`no_three_mismatch_of_gap`**: primitive, `q = 1`, `2^A ≤ 2^172·m^341·(2^A − 3^m)`, `m ≥ 2^19`, `L ≥ 2^20`, `1 ≤ h < m` ⇒ the rotation does not have exactly three mismatches; **`four_le_mis_card_of_gap`**: with the attained band `hB`, `4 ≤ |mis h|`, from `exists_mis`, `mis_card_ne_one`, `no_two_mismatch_of_gap` and `no_three_mismatch_of_gap`.

**Statement match.** Part 1 of the Statement is exactly `no_three_mismatch_of_gap` and `four_le_mis_card_of_gap`. The gap is an input mirroring an effective Baker-type bound (`gap_all`, replayed in `mmusson/collatz` as EXT-1, not imported into this file). The formal threshold `2^19` is above the written `m0 = 452,695` and serves the tangent bound on `log m`; `L ≥ 2^20` is weaker than the note's `L > 2^71` (only `ε ≤ 1/(3·2^20)` is used). A rotation `h ≥ m` would first be reduced modulo `m` (not formalised, not needed). Condition P of the note is unused. The longest run doubles as the uniform run bound `T` and as `t*`. Nothing is asserted about cycles with `m < 2^19` or without the gap. The side lane refereed each unit from receipts (feed S7 entry, updates 12:44–13:53, and the 14:20 milestone entry); at `m = 2^19` it rechecked F independently: `T ≤ 197,705.6`, so `τ ≥ 128,873.9`, while the witness allows only `τ < 122,318.5`, a gap of 6,555.4 (the probe gives +6,556). *[That entry first quoted hand-rounded values, corrected within the minute.]*

## Remarks

The rest of the legacy note (§§4–6), lightly edited.

### 4. Numbers (`s7_three_mismatch.py`, Part 1)

The conditions are evaluated at the worst case `ℓ = ℓ*(m)`. Each entry is a margin, and positive means the condition holds.

| `m` | W | A | P | F | `t_max` | `d_max` | `σ_min` |
|---|---|---|---|---|---|---|---|
| 452,695 | 4 | 168,101 | 226,349 | 3,457 | 171,236 | 55,109 | 110,221 |
| 10^6 | 35,499 | 394,080 | 517,749 | 27,586 | 373,477 | 108,773 | 253,044 |
| 17,087,915 | 1.13·10^6 | 7.07·10^6 | 9.11·10^6 | 7.6·10^5 | 6.31·10^6 | 1.67·10^6 | 4.46·10^6 |
| 1.14·10^11 (Hercher) | 7.8·10^9 | 4.7·10^10 | 6.1·10^10 | 5.2·10^9 | 4.2·10^10 | 1.1·10^10 | 3.0·10^10 |

### 5. Controls on actual `3x+q` cycles (Part 2)

The sample is the 616 cycles with `m ≥ 3` for odd `q < 400`, `3 ∤ q`, from starts up to 3,001. It includes the controls `q = 5, 7, 13, 61`.

- **The exact, `q`-independent claims hold on every rotation checked:** 287 rotations with exactly two mismatches and 196 with exactly three.
  - The two located sign changes (Step 2) are always present.
  - With three mismatches, there are always exactly two changes.
  - Every run end satisfies `|δ_e| ≥ 2·3^t` and its witness bound.
  - The `q`-version of the ceiling, `n_z ≤ L·Π_(i<pos z)(3/2)(1 + q/(3n_i))`, holds.
- **Alignment holds in 78 of the 196 three-mismatch rotations.** In every aligned case the witness identity of Step 5 (`z = x − (t° + 1)`, with no wrap) holds exactly.
- **What fails at `q > 1` is the size input.**
  - These cycles have `log₂ L / m ≈ 1.5–1.6`, so all four conditions fail by wide margins, and three-mismatch rotations duly exist. One example is `q = 13`, `m = 5`, `L = 287`, `h = 2`, which is aligned (order 1).
  - The same holds for main's C013 §3 distance-three family of rational cycles. *[Corrected 13:29: an earlier version wrote `log₂ q ≈ 0.447m`. That is C013 §5's lower bound; the actual denominators are `den ≈ D`, `log₂ den ≈ 1.55m` (S9, [`two-three-mismatch-denominator-laws`](../two-three-mismatch-denominator-laws/README.md)).]*
  - The proof uses `q = 1` only through `ℓ = O(log m)` (F4) and `ε ≈ 0`.

### 5a. Review and a consistency check

- **The Lean lane's review** (2026-10-19, of `d978b57`) attacked Steps 3–5 line by line and found no gap.
  - It asked for four points to be made explicit, now done: the wrap case of Step 3; that `X*` and `d*` use the worst case `t*`; that the witness index `z` is an integer in `[0, m)` with `n_z = n_(e_c+h)`; and that `s ≠ 1` comes from the equal totals, not from primitivity.
  - S7-a, the sign lemma, is formal. The other steps are planned as S7-b, S7-c and S7-d.
- **Consistency with known results.** Two short arguments recover the Steiner/Simons exclusions of 1-cycles and 2-cycles for `m ≥ m0`, through rotations alone.
  - **One letter `≥ 2`.** Every rotation of a word with exactly one letter `≥ 2` has two mismatches, so S6 excludes it.
  - **Two letters `V, W ≥ 2`, at `x` and `y`.** The rotation by `r = y − x` can only mismatch at `x`, `y` and `2x − y`. So it has 3 mismatches (`V ≠ W`), 2 (`V = W`), or, when `2r ≡ 0`, 2 or 0.
  - S6, S7 and primitivity exclude every case.
  - This is a check that the theorem has content, not a new result. Words with three or more letters `≥ 2` are not reached this way.
- **An independent review agent also found no gap** (2026-10-19).
  - It recomputed the four conditions in 80-digit decimal arithmetic. W is −1 at 452,694 and 4 at 452,695, so `m0` is exact.
  - It tested every q-independent step (2–5) under its actual hypotheses on all primitive words up to length 14 (rational cycles). `s7_stress_rational.py 3 14` reproduces this here: 5,116 three-mismatch rotations, with no failure. The Step 4 transfer is exercised on 260 unaligned rotations, and Step 5 on 444 aligned ones.
  - Its minor points are applied: `ε` is computed with `log1p`, "longer than" is now "at least", P is noted as redundant, and the Eliahou citation is corrected.
- **The Lean lane's observation (from S7-b part 3b).** Steps 2–4 hold for any mismatch count `s`, given the spacing bound `σ ≥ 2d − 1` and condition A.
  - The count `s = 3` enters only in Step 1, which produces `σ_min` and `X*`.
  - "`σ_min > d_max`" can be weakened to `σ_min ≥ d_max`.
  - This is exactly where S8's four-mismatch words escape.
- **Relation to the literature.**
  - `ρ ≥ 4` improves this programme's `ρ ≥ 3` (C011).
  - The k-cycle literature bounds a different statistic, the number of local minima, as settled in the S6 dispute. No comparison with it is implied beyond the check above.

### 6. Limits and what it does not give

- **The output is `ρ ≥ 4`, not a growing `F(m)`.** At `s = 4`, the pigeonhole gives only `log₂ H > 0.396m`. Then the descent window can be about `0.32m` and the runs need not be bounded below. Steps 3–4 fail, so a new idea is needed.
  - Step 5's device does extend: each run's witness sits at a computable position, and witnesses far inside the climb are cheap. A bound for general `s` would need the witnesses to be spread out.
- **Imports.**
  - `gap_all` (formal in `mmusson/collatz`, replayed) is used only through `ℓ ≤ ℓ*(m)`. An irrationality measure for `log₂ 3` with a smaller exponent (Rhin-type) would lower `m0` a lot, but none is formal.
  - Barina's `L > 2^71` is used only to make `ε` negligible; `L ≥ 2^20` changes nothing visible.
  - The period import is any `m ≥ 452,695`.
- **Formalisation.** The proof splits into four lemmas, each elementary:
  - the sign lemma (F2 plus Step 2);
  - window disjointness;
  - alignment by excess transfer;
  - the refined ceiling at the witness (S6-a's `n_le_climb` at a position).
  - The numeric step has the same shape as S6-b's `numeric_step`.

## History

- Migrated from `experiments/cycle_spectrum/S07/THREE_MISMATCHES.md` (legacy ID `S07`; side-lane producer batch S7, 2026-10-19) at commit `be73a66`, by the B05 migration (Claude, Opus 5.5). The side-lane probes `reviews/side_lane/s7_three_mismatch.{py,json}` and `s7_stress_rational.py` moved here. The note's "Reproduce" block pointed to the old paths; the scripts now sit in this folder (see `evidence`).
- Side lane (Claude, Opus), feed 2026-10-19 12:40 ("a written proof with a numeric threshold, not yet adversarially reviewed"; the Lean lane had pre-reviewed the sketch, accepted the sign and size steps, sharpened the alignment, and asked for the witness step in detail).
- **Review (12:48).** The Lean lane's adversarial review found no gap; four explicitness points were applied (the wrap case of Step 3; `X*` and `d*` at the worst case `t*`; the witness index `z` an integer in `[0, m)` with `n_z = n_(e_c+h)`; `s ≠ 1` from the equal totals, not from primitivity — **correction:** §1 had credited primitivity).
- **Review (13:03).** An independent review agent (unnamed in the record) found no gap, recomputed `m0` exactly, and stress-tested Steps 2–5; its minor points were applied (`ε` via `log1p`, "at least" wording, P noted as redundant). **Correction (citation):** Eliahou's 17,087,915 bounds the total cycle length `A`, not `m`; in odd steps `m ≳ 1.08·10^7`. Conclusions unchanged.
- **Correction (13:29).** §5 first wrote `log₂ q ≈ 0.447m` for the distance-three family; corrected as quoted in §5 (see also [`distance-three-height-family`](../distance-three-height-family.md)).
- Formalised by the Lean lane (Claude, Fable) as S7-a to S7-d against the note at legacy commits `d978b57` (revised `e4d97ad`); the milestone "`ρ ≥ 4` formal end to end, given the linear-form gap" was recorded in the feed at 14:20 (Lean-lane commit `bd627c9`).
