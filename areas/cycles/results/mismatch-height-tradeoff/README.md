---
id: mismatch-height-tradeoff
kind: result
title: "Mismatch–height trade-off at q = 1: every rotation differs in more than log₂3·m/(B + 342 log₂ m + 172) positions"
status: formal
claim: >
  Raw odd-only 3x+1 map (q = 1), no order assumed. Let a primitive integer cycle have period m, total A,
  D = 2^A − 3^m and band B (every state below 2^(B+1)·L), and assume the linear-form gap
  2^A ≤ 2^c·m^μ·D. Then for every nonidentity rotation h, with s the number of mismatch positions
  {i < m : a_i ≠ a_(i+h)}, there is t with m ≤ s(t+1) and 6·3^t < 2^(B+1+c)·m^(μ+1). With the replayed
  gap_all, (c, μ) = (172, 341), this gives s > log₂3·m/(B + 342·log₂ m + 172). Hence any height bound
  B = o(m) for such cycles would give a mismatch count growing with m.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [paired-state-run-law]
assumes: [musson-collatz-gap-all]
lean:
  - LeanLane.Cyc.OddCycle.a_per
  - LeanLane.Cyc.OddCycle.z_eq_zero_of_agree_period
  - LeanLane.Cyc.OddCycle.exists_mis
  - LeanLane.Cyc.OddCycle.pigeonhole
  - LeanLane.Cyc.OddCycle.run_bound_of_gap
  - LeanLane.Cyc.OddCycle.mismatch_height
evidence:
  - "s5_mismatch_height.py, s5_mismatch_height.json: side-lane probe (about 1 s): (a) on 283 actual 3x+q cycles (odd q < 200, 3 ∤ q) and all 3,100 nonidentity rotations, the longest agreeing run meets the pigeonhole and C013 (7) in exact integers; (b) the q = 1 bound at m = 1.375·10^11 by band, and the largest band keeping it above 3. Fails at its new path: it imports the side-lane helper s1a_integer_cycle_check from its own folder (now in ../ordered-gap-closed-form/). Passed at be73a66 as reviews/side_lane/s5_mismatch_height.py (archive/legacy-checker-run-be73a66.md)"
  - "s5_cycle_heights.py: side-lane data probe for the appendix (about 4 s, no receipt; prints only). Fails at its new path for the same import. Passed at be73a66 as reviews/side_lane/s5_cycle_heights.py (archive/legacy-checker-run-be73a66.md)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed update 11:35: S5 reviewed; one off-by-one corrected (173 − log₂ 6, not 172 − log₂ 6); confirmed the pigeonhole direction and count, z ≠ 0 for every h ≢ 0, the height ceiling (sharpened), the section 0 rank-two observation and the section 4 reading. Lean unit S5-a verified (iteration 63)"
aliases: [S05]
tags: [cycles, rotation-distance, height, linear-forms, formal]
---

# Mismatch–height trade-off at q = 1: every rotation differs in more than log₂3·m/(B + 342 log₂ m + 172) positions

## Statement

Throughout, the cycle is a primitive integer cycle of the raw odd-only `3x+1` map (`q = 1`), of period `m`, total `A`, `D = 2^A − 3^m`, minimum `L` and band `B` (`H < 2^(B+1)·L`). No circular order is assumed. For a nonidentity rotation `h` let `s` be its number of mismatch positions in one period.

**Integer form (formal).** If `2^A ≤ 2^c·m^μ·D`, then there is `t` with

```
m ≤ s(t + 1)   and   6·3^t < 2^(B+1+c)·m^(μ+1).
```

**Logarithmic form.** With `gap_all`'s `(c, μ) = (172, 341)` ([`musson-collatz-gap-all`](../../../../sources/musson-collatz-gap-all.md), EXT-1), every agreeing run satisfies `t < (B + 342·log₂ m + 173 − log₂ 6)/log₂ 3`, and every nonidentity rotation has

```
s > m / (1 + (B + 342·log₂ m + 173 − log₂ 6)/log₂ 3)  =  log₂3·m / (B + 342·log₂ m + 172).
```

The equality uses `log₂ 3 − log₂ 6 = −1`. This is main's C013 (6) at `q = 1` ([`paired-state-run-law`](../paired-state-run-law.md)), with Matveev's `K_0 ≈ 6·10^8` replaced by the replayed exponent 341.

## Proof

Legacy note `MISMATCH_HEIGHT.md` (S5, side lane), lightly edited. It is a composition of results that are already formal, with one elementary step (a pigeonhole) and the literature import of the gap.

### 0. Why S5 does not use C012's coupled matrix (an observation, not new mathematics)

S5 was announced as a coupled two-plateau estimate at three mismatches. Reading C012 §§4–5 ([`coupled-defect-matrix-smith-form`](../coupled-defect-matrix-smith-form/README.md)) shows why that cannot give a size bound by congruences alone.

- **The rank-two structure.** C012 §4 shows `W ≡ u·vᵀ (mod D)`, where `v` is the first row of `W`. So `Wc ≡ u·X_0` and `W′c ≡ u′·Y_0 (mod D)`, with `X_0` and `Y_0` the two rotated intercepts at block start 0.
- **What the system says modulo `g`.** Hence `Mc ≡ u′Y_0 − u·X_0`. Modulo any `g` dividing `D`, the coupled system says only that `g | X_0` and `g | Y_0`. That holds automatically, since `g` divides every rotated intercept.
- **Why `s = 2` is different.** C011's gain at `s = 2` ([`two-defect-rotation-exclusion`](../two-defect-rotation-exclusion/README.md)) comes from inverting `M` over the integers with the small determinant `Π|β′ − β|`, not from congruences. At `s ≥ 3`, `det M` carries `D^(s−2)` (C012 (5)).
- **Consequence.** Any bound at `s ≥ 3` must come from integer sizes. S5 therefore uses the size route already in C013.

### 1. The inputs

- **(I1) C013-b** (Lean `q_bound_rational`; [`paired-state-run-law`](../paired-state-run-law.md)). Take a nonidentity rotation `h` and an agreeing run of length `t` (the letters agree with their `h`-shifts) with exponent total `E`. Primitivity makes `z ≠ 0`. Then `6D·max(2^E, 3^t) < m·q·2^A·(2^(B+1) − 1)`. This is main's C013 (7). It uses no ordering and no comparison of `q` with `L`.
- **(I2) The pigeonhole** (elementary; formal as `pigeonhole`). If `w` and `w.rotate(h)` differ in exactly `s` positions, the `m − s` agreeing positions form at most `s` cyclic runs. So some agreeing run has length at least `ceil((m−s)/s)`. A mismatch exists because a full period of agreement would give `D·z = 0`.
- **(I3) `gap_all`** (`mmusson/collatz`, replayed by the Lean lane as EXT-1, standard axioms): `2^A ≤ 2^172·m^341·D`.

### 2. The trade-off (exact, given I1–I3)

At `q = 1`, combining I1 and I3 gives `3^t < 2^(B+173)·m^342/6`. Hence every agreeing run satisfies `t < (B + 342·log₂ m + 173 − log₂ 6)/log₂ 3`. Combining this with I2, for **every** nonidentity rotation, the mismatch count satisfies the bound of the Statement. Main's warning applies: `B` must be kept. Its distance-three family ([`distance-three-height-family`](../distance-three-height-family.md)) shows that a bounded rotation distance does not bound the height, at least for rational cycles.

## Lean

`lean/CycleSpectrum.lean`, Lean unit S5-a (iteration 63); axioms `propext`, `Classical.choice`, `Quot.sound`. In `OddCycle`: `a_per` (the valuation word is `m`-periodic), `agree`, `mis h` (the mismatch positions in one period; `s = card`), `z_eq_zero_of_agree_period` (a full period of agreement forces `z = 0`), `exists_mis` (`s ≥ 1` for a primitive cycle), `pigeonhole` ((I2): a mismatch exists and every agreeing run has length `≤ T` ⇒ `m ≤ (T+1)s`), `run_bound_of_gap` ((I1)+(I3): at `q = 1` with `2^A ≤ 2^c·m^μ·D`, every agreeing run with `z ≠ 0` at its end has `6·3^t < 2^(B+1+c)·m^(μ+1)`), and **`mismatch_height`**: primitive, `q = 1`, the gap, `h % m ≠ 0` ⇒ `∃ t, m ≤ s(t+1) ∧ 6·3^t < 2^(B+1+c)·m^(μ+1)` (the `t` produced is the longest run, via `Nat.findGreatest`). That is the integer form of the Statement with `(c, μ)` free. `B` is the structure's upper bound on the heights; attainment is not needed. The logarithmic form at `(c, μ) = (172, 341)` (taking `log₂` and using `t + 1 ≥ m/s`) is elementary and not restated in Lean. The gap itself is not proved in this file: it is the hypothesis `hgap`, discharged by `gap_all` in `mmusson/collatz` (EXT-1).

## Remarks

**Numbers (with a period input; `s5_mismatch_height.py`).** These use, in addition, the period bound `m > 1.375·10^11` ([`hercher-2023-cycle-length`](../../../../sources/hercher-2023-cycle-length.md) with [`barina-2025-convergence-2-71`](../../../../sources/barina-2025-convergence-2-71.md)), which the claim above does not. At `m = 1.375·10^11`, every nonidentity rotation of a hypothetical nontrivial Collatz cycle has mismatch count `s` greater than:

| band `B` | 0–10 | 100 | 10^3 | 10^4 | 10^5 | 10^6 | 10^7 |
|---|---|---|---|---|---|---|---|
| lower bound on `s` | 1.70·10^7 | 1.69·10^7 | 1.58·10^7 | 9.5·10^6 | 1.9·10^6 | 2.2·10^5 | 2.2·10^4 |

- **Cycles with `H < 8L`.** Since `B ≤ 2`, every rotation differs in more than `1.7·10^7` positions. This sits alongside the `J > 10^7` bound for the same band ([`ordered-cycle-height-change-growth`](../ordered-cycle-height-change-growth.md)).
- **Comparison with C011.** The bound stays above 3, the case C011 already excludes, for every `B ≤ 7.26·10^10 ≈ 0.53m` (receipt: largest such `B` is 72,644,101,790).
- **The height ceiling** (sharpened by the Lean lane; [`cycle-height-ceiling`](../cycle-height-ceiling.md), formal). Along the arc from the minimum to the maximum, each step multiplies the state by `(3 + q/n_i)/2^(a_i) ≤ (3/2)(1 + q/(3L))`. The note states `B ≤ (log₂ 3 − 1)(m − 1) + m·log₂(1 + q/(3L)) + 1`; at `q = 1` with `L > 2^71`, the middle term is below `10^(−20)·m`, so `B ≤ 0.585(m−1) + 1`. The bound is therefore vacuous only in the top tenth of the possible height range. *(The slightly sharper form proved later, without the `+ 1` and with `m − 1` in the last term, is [`cycle-height-ceiling`](../cycle-height-ceiling.md); the note's form is weaker and still valid.)*
- **Data.** On 283 actual `3x+q` cycles (odd `q < 200`) and all 3,100 of their nonidentity rotations, the longest agreeing run satisfies both the pigeonhole and (7) exactly. The `q = 1` statement has no nontrivial instance to test.

**Consistency check (the Lean lane's observation, corrected).** Run the same chain at general `q` on main's distance-three family ([`distance-three-height-family`](../distance-three-height-family.md)). There the runs have length about `m/3`, `B/m → (2 − log₂ 3)·log₂(3/2)/3 ≈ 0.081`, and `2^A/D = Θ(m)`. The chain gives `log₂ q ≳ (m/3)·log₂ 3 − 0.081m − O(log m) ≈ 0.447m`. *[Corrected 2026-10-19 13:29, after the Lean lane's own correction: `0.447m` is that node's part-5 lower bound (`liminf`), derived from the same inequality. The family's actual denominators are `den ≈ D`, with `log₂ den ≈ 1.53–1.58m` (S9's probe). So the (I1) chain at general `q` reproduces the part-5 lower bound on the family, and the actual `den ≈ D` is far above both. Neither bound is sharp there.]*

**What remains (§4 of the note).** Main's recommended intermediate milestone is a growing lower bound `F(m)` on the mismatch count of every rotation of any hypothetical nontrivial cycle ([`rotation-distance-growth`](../../questions/rotation-distance-growth.md)). By the trade-off it follows from any height bound `B ≤ o(m)` for `q = 1` cycles, and `B = O(log m)` would give main's "order `m/log m`" payoff. So the open obstacle is exactly a **height bound for integer cycles**: [`cycle-height-bound`](../../questions/cycle-height-bound.md). No such bound is known to the side lane; the distance-three family shows it cannot come from rotation distance alone, so it would have to use `q = 1` arithmetic. A literature search (feed update 15:08, extended search, calibration only) found no bound on `H/L` for nontrivial `3x+1` cycles.

**Appendix: heights of actual cycles (data only, `s5_cycle_heights.py`).** The sample is the actual reduced `3x+q` cycles for odd `q < 1000` with `3 ∤ q`, found from starts `≤ 3001`: 1,147 cycles with `m ≥ 2`. `B` never exceeds 17; `B/log₂ m ≤ 3.0` for `m ≥ 30`, and `≤ 2.4` for `100 ≤ m < 200`. This is consistent with a height bound `B = O(log m)`, but the sample has small minima, `q/L = O(1)`, while a `q = 1` cycle would have `L > 2^71`, the opposite regime. **These numbers are not evidence about `q = 1` heights, and no mechanism is proposed.** (The probe prints only; it has no committed receipt.)

**Controls and scope.** The proof uses `q = 1` only through the gap (which bounds `L`) and through I1 at `q = 1`; actual `3x+q` cycles with few mismatches are allowed because their `q` is large. No cycle is excluded. Novelty undetermined.

## History

- Migrated from `experiments/cycle_spectrum/S05/MISMATCH_HEIGHT.md` (legacy ID `S05`; side-lane producer batch S5, 2026-10-19) at commit `be73a66`, by the B05 migration (Claude, Opus 5.5). The side-lane probes `reviews/side_lane/s5_mismatch_height.{py,json}` and `s5_cycle_heights.py` moved here. The note's §3 numbers and appendix are under Remarks; its §4 became the question [`cycle-height-bound`](../../questions/cycle-height-bound.md); the height ceiling it quotes is [`cycle-height-ceiling`](../cycle-height-ceiling.md).
- Side lane (Claude, Opus), feed 2026-10-19 11:24 (status line: "no cycle is excluded, and novelty is undetermined"; the shape is main's C013 inequality (6), and what is new is only that the replayed `gap_all` makes it quantitatively strong).
- **Correction (2026-10-19 11:35, after the Lean lane's review).** The first version had `172 − log₂ 6` in place of `173 − log₂ 6` in both formulas of §2, which made the bound slightly too strong. The difference is about one part in 12,000 at `m = 1.375·10^11` (`B = 0`: 16,992,485 → 16,991,160), and the rounded numbers are unchanged. The corrected bound simplifies exactly to `log₂3·m/(B + 342·log₂ m + 172)`.
- **Correction (2026-10-19 13:29).** The consistency check first called the general-`q` chain "sharp in the exponent" on the distance-three family; corrected as quoted above (also recorded in [`distance-three-height-family`](../distance-three-height-family.md)).
- Formalised by the Lean lane (Claude, Fable) as S5-a, legacy commit of the note `2858b07`, corrected `47c2fa8`.
