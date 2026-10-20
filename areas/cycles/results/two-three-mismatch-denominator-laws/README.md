---
id: two-three-mismatch-denominator-laws
kind: result
title: "Two- and three-mismatch words have exponentially large denominators unless their drift is linear (every 3x+q)"
status: formal
claim: >
  For every primitive positive valuation word w (period m, total A, D = 2^A − 3^m > 0, letters ≥ 1), with
  drift δ(w) = A − m·log₂3 and λ(w) = log₂(m·2^A/(3D)), and its reduced denominator den(w) = D/gcd(C_w, D):
  (i) if some rotation of w differs from w in exactly two positions, then
  log₂ den(w) > 1 + ⌈(m−2)/2⌉·log₂3 − (m−1)·log₂(3/2) − δ(w) − λ(w), the main term being about 0.2075·m;
  (ii) if m ≥ 2^19 and some rotation differs from w in exactly three positions, then
  log₂ den(w) > m/70 − δ(w) − λ(w). Equivalently, for a primitive odd cycle of 3x+q (odd q) with such a
  rotation, the same bounds hold for log₂ q. No linear-form gap and no hypothesis on L/q are used. The laws
  are informative only for words with small drift (cycles with L ≫ q); they are vacuous when δ(w) is linear.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [global-drift-ceiling, paired-state-run-law]
lean:
  - LeanLane.Cyc.OddCycle.exists_longest_run
  - LeanLane.Cyc.OddCycle.D_div_le_delta
  - LeanLane.Cyc.OddCycle.three_L_D_le
  - LeanLane.Cyc.OddCycle.two_mismatch_denominator_law
  - LeanLane.Cyc.OddCycle.two_mismatch_denominator_law'
  - LeanLane.Cyc.OddCycle.two_mismatch_denominator_law_odd
  - LeanLane.Cyc.OddCycle.n_le_drift
  - LeanLane.Cyc.OddCycle.three_mismatch_witness_drift
  - LeanLane.Cyc.OddCycle.numeric_WA_drift
  - LeanLane.Cyc.OddCycle.numeric_F_drift
  - LeanLane.Cyc.OddCycle.no_three_mismatch_of_small_drift
  - LeanLane.Cyc.OddCycle.three_mismatch_denominator_law
  - LeanLane.Cyc.OddCycle.ofWord_den
  - LeanLane.Cyc.OddCycle.word_two_mismatch_law
  - LeanLane.Cyc.OddCycle.word_three_mismatch_law
  - LeanLane.Cyc.OddCycle.den_rotate
  - LeanLane.Cyc.OddCycle.mismatch_card_rotate
  - LeanLane.Cyc.OddCycle.word_two_mismatch_law'
  - LeanLane.Cyc.OddCycle.word_three_mismatch_law'
evidence:
  - "s9_denominator_law.py, s9_denominator_law.json: side-lane probe (about 30 s): computes Λ₃(m) and checks laws (i) and (ii) on every primitive word over {1,2,3} up to length 12, random two- and three-arc chain words up to m = 1,600, near-critical chain words up to m = 3,200, main's C013 §3 distance-three family, and the words of actual 3x+q cycles (odd q < 2,000); no violation. Fails at its new path: it imports s7_three_mismatch from its own folder (now in ../three-mismatch-exclusion/), which imports s1a_integer_cycle_check (now in ../ordered-gap-closed-form/); with both folders on PYTHONPATH it exits 0 and leaves its receipt byte-identical (checked at migration). Passed at be73a66 as reviews/side_lane/s9_denominator_law.py (archive/legacy-checker-run-be73a66.md)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed S9 entry, update 13:29: inventory of where q enters (only through the factor q in (I1), the ceiling's drift and L ≤ mq·2^A/(3D)); no hidden q = 1; the drift caveat is intrinsic; correction (c) on C013's 0.447m. Lean units S9-a to S9-e verified (iterations 76-86)"
    link: ../../../../archive/side-lane/FEED.md
aliases: [S09]
tags: [cycles, rotation-distance, denominator, 3x+d, formal]
---

# Two- and three-mismatch words have exponentially large denominators unless their drift is linear (every 3x+q)

## Statement

Take any primitive positive word `w` (period `m`, total `A`, `D = 2^A − 3^m > 0`, letters `≥ 1`) and its reduced integer cycle: the parameter is `q = den(w) = D/gcd(C_w, D)`, the states `n_i = C(w_i)/gcd(C_w, D)` are odd, and the arrows are `2^(a_i) n_(i+1) = 3n_i + q`. Write `δ(w) = A − m·log₂3` (the drift, in bits) and `λ(w) = log₂(m·2^A/(3D))`.

- **(i) Two mismatches.** If some rotation differs from `w` in exactly two positions, then

  ```
  log₂ den(w) > Φ₂(m) − δ(w) − λ(w),     Φ₂(m) = 1 + ⌈(m−2)/2⌉·log₂3 − (m−1)·log₂(3/2) ≈ 0.2075·m.
  ```

- **(ii) Three mismatches.** If `m ≥ 2^19` and some rotation differs from `w` in exactly three positions, then

  ```
  log₂ den(w) > m/70 − δ(w) − λ(w).
  ```

  The legacy note states the sharper written form `log₂ den(w) > Λ₃(m) − δ(w) − λ(w)` with `Λ₃(m) = sup{Λ : S7's conditions W, A, P, F hold at ℓ = Λ, ε = 0}`; the probe gives `Λ₃ = 1.8, 4.7, 15.7, 44, 147, 1,458` at `m = 10², 3·10², 10³, 3·10³, 10⁴, 10⁵`, so asymptotically `Λ₃ ≈ 0.0146·m`, condition W binding. The formal constant `1/70` is below the admissible ratio `Λ₃(m)/m ≈ 0.01457` for every `m ≥ 2^19` (computed by both lanes).

Both laws hold verbatim for a primitive odd cycle of `3x+q` (odd `q`) whose word has such a rotation, with `log₂ q` on the left. No linear-form gap and no hypothesis on `L/q` are used.

## Proof

Legacy note `DENOMINATOR_LAW.md` (S9, side lane), §§1–2, lightly edited. Its status line read: "A written extension of S6/S7 with a probe. It changes one ingredient, the ceiling, and reuses every other step unchanged. Novelty undetermined."

### 1. The global-drift ceiling

The one new ingredient is [`global-drift-ceiling`](../global-drift-ceiling.md): for every index `k` counted forward from the minimum `L`,

```
log₂(n_k / L) ≤ k·log₂(3/2) − X_k + δ(w),          X_k = Σ_(i<k)(a_i − 1),
```

with no hypothesis on `L/q`. S6-a/S7 used the per-step form `k·log₂(1 + q/(3L))`, which is small only when `L ≫ mq`. Unchanged from S7 (F4): `L ≤ m·q·2^A/(3D)`.

The run law ([`paired-state-run-law`](../paired-state-run-law.md)), the witnesses, the sign lemma, the window and alignment steps, and the witness index all hold verbatim at any odd `q`, since `q` cancels in `δ_i = n_(i+h) − n_i`. In S7's conditions ([`three-mismatch-exclusion`](../three-mismatch-exclusion/README.md)), `κ` becomes `log₂(3/2)`, and `ℓ` becomes `Λ = log₂ L + δ(w)`.

### 2. The laws

- **(i)** *Proof (S6's chain, [`two-mismatch-exclusion-via-gap`](../two-mismatch-exclusion-via-gap/README.md)).* The longest run has `t ≥ ⌈(m−2)/2⌉`. Then `1 + t·log₂3 < log₂ H ≤ log₂ L + (m−1)·log₂(3/2) + δ(w)`, and `log₂ L ≤ log₂ q + λ(w)`.
- **(ii)** *Proof.* This is S7, contrapositively. If `Λ = log₂ L + δ(w) ≤ Λ₃(m)`, then Steps 1–6 of S7 run and exclude the rotation. None of those steps uses the gap; S7 uses it only to bound `ℓ`. The formal version runs the same steps with `Λ ≤ (m/70)·log 2` (natural logs) for `m ≥ 2^19`.

## Certificates

None run by CI. `s9_denominator_law.py` (§4 of the legacy note, about 30 s) is a probe; see `evidence`.

| test set | rotations with `s = 2` | rotations with `s = 3` | non-vacuous cases | violations |
|---|---|---|---|---|
| every primitive word over `{1,2,3}`, `m ≤ 12` | 1,498 | 1,274 | 0 | 0 |
| random 2- and 3-arc chain words, `m ≤ 1,600` | 163 | 192 | 16 | 0 |
| near-critical chain words (`A = ⌈m log₂ 3⌉`), `m ≤ 3,200` | 50 | 50 | 50 + 20 | 0 |
| C013 §3 family, `(a,b)` up to `(1539, 971)`, `m ≤ 2,913` | — | 5 | 1 (`m = 2,913`) | 0 |
| words of actual `3x+q` cycles, odd `q < 2,000` | 451 | 392 | 0 | 0 |

- **Slack.** Generic words have `den(w) ≈ D`, so the slack is large; it is 281 bits or more in every non-vacuous case.
- **Tightness cannot be tested.** The laws could only be tight for hypothetical small-denominator words, which the data cannot produce. So the table is a consistency check, not evidence of strength.
- **A note on main's family.** Reconciled with the Lean lane: there is no conflict. C013 §5's `≈ 0.447m` is a lower bound (`liminf (log q)/b`), derived from the same inequality as (I1). This probe measures the actual denominators: `den ≈ D`, `log₂ den/m ≈ 1.53–1.58`. So the lower bounds agree with each other, and the actual value lies far above both. Earlier S5/S7 wording called the bound sharp on the family; that is corrected (see History).

## Lean

`lean/CycleSpectrum.lean`, Lean units S9-b to S9-e (iterations 77, 79, 84, 86; axioms `propext`, `Classical.choice`, `Quot.sound`, some helpers on subsets; receipts `lean/receipts/CycleSpectrum.*`), namespace `LeanLane.Cyc.OddCycle`. The ceiling itself is S9-a, in [`global-drift-ceiling`](../global-drift-ceiling.md).

- **S9-b, law (i) for cycles.** `exists_longest_run`, `D_div_le_delta`, `three_L_D_le` (S7's (F4): `3LD ≤ mq·2^A`); **`two_mismatch_denominator_law`** (primitive, letters `≥ 1`, `h % m ≠ 0`, `|mis h| = 2`: some run `T` with `m ≤ 2(T + 1)` has `log 2 + T·log 3 < log q + (m − 1)·log(3/2) + δ_nat + λ_nat`), **`two_mismatch_denominator_law'`** (with `T ≥ ⌈(m−2)/2⌉`), `two_mismatch_denominator_law_odd` (odd `q` gives letters `≥ 1`).
- **S9-c, law (ii) for cycles.** `n_le_drift`, **`three_mismatch_witness_drift`** (S7 Step 5 with the drift ceiling), **`numeric_WA_drift`**, **`numeric_F_drift`** (conditions W, A, F for `m ≥ 2^19` under `Λ ≤ (m/70)·log 2`), **`no_three_mismatch_of_small_drift`** (`log L + δ_nat ≤ (m/70)·log 2` ⇒ `|mis h| ≠ 3`; no gap, no `L/q` hypothesis), **`three_mismatch_denominator_law`** (`(m/70)·log 2 < log q + δ_nat + λ_nat`).
- **S9-d, the `q = den(w)` glue.** `ofWord_den` (the reduced cycle `ofWord w` has parameter `den(w)`), and the word laws **`word_two_mismatch_law`**, **`word_three_mismatch_law`** under a minimal-rotation normalisation.
- **S9-e, rotation invariance.** `den_rotate`, `mismatch_card_rotate` and helpers; **`word_two_mismatch_law'`**, **`word_three_mismatch_law'`**: the word laws for every positive primitive word with `D_w > 0`, no normalisation hypothesis.

**Statement match.** With `δ_nat = A·log 2 − m·log 3` and `λ_nat = log m + A·log 2 − log 3 − log D`, dividing by `log 2` gives (i) and (ii) of the Statement, in natural-division form `⌊(m−1)/2⌋ = ⌈(m−2)/2⌉` (checked for `m = 3…39`). Primitivity is expressed as distinct rotated intercepts; letters `≥ 1` and `D_w > 0` are hypotheses. Not formal: the sharper `Λ₃(m)` form of (ii) and its numerical values, and the gap-conditional form (iii) in Remarks. A first S9-d draft omitted the `(m − 1)·log(3/2)` term of `Φ₂`; the build caught it, and the committed statement has it.

## Remarks

- **(iii) With `gap_all` (conditional on EXT-1, [`musson-collatz-gap-all`](../../../../sources/musson-collatz-gap-all.md); not part of the claim).** `λ(w) ≤ log₂(m/3) + 172 + 341·log₂ m`. So for near-critical words (`δ(w) < 1`, which includes every word of a cycle with `L ≫ mq`), `den(w) ≥ 2^(Φ_s(m) − 174 − 342·log₂ m)` for `s = 2, 3`. At `q = 1` this returns S6 and S7 ([`two-mismatch-exclusion-via-gap`](../two-mismatch-exclusion-via-gap/README.md), [`three-mismatch-exclusion`](../three-mismatch-exclusion/README.md)); at `q = 1` the laws themselves are weaker than those exclusions, and their content is the general-`q` family. At fixed `q` it bounds the period of every near-critical two- or three-mismatch word explicitly.
- **Dependencies, stated precisely.** The argument reuses the `q`-independent Steps 1–6 of [`three-mismatch-exclusion`](../three-mismatch-exclusion/README.md) and S6's chain. Those steps do not use the gap or the period imports, so this node does not list those two gap-conditional results under `depends_on` (MAP.md would otherwise show it resting on their imports); the Lean proofs above are self-contained.
- **Height is eliminated for `s ≤ 3`.** Main's C013 inequality (6) ([`shared-background-denominator-law`](../shared-background-denominator-law/README.md)) holds at every `q` but keeps the height `B`; its §5 says the height shortcut "does not eliminate B". The global-drift ceiling eliminates `B` at a cost of `0.585m`. That is affordable for `s = 2` (`0.792 > 0.585`) and, with S7's refinement, for `s = 3`. S8 ([`four-mismatch-size-method-limit`](../../attempts/four-mismatch-size-method-limit/README.md)) shows it is not affordable at `s = 4`, so this is the exact reach of the method.
- **Relation to C011.** C011 proves bounded-denominator finiteness for the two-defect class ([`two-defect-bounded-denominator-finiteness`](../two-defect-bounded-denominator-finiteness.md)). (i) is an explicit exponential version, under the drift caveat.
- **The three-mismatch class.** (ii) is, as far as the side lane knew, the programme's first denominator law for it. It is consistent with main's C013 §3 distance-three family ([`distance-three-height-family`](../distance-three-height-family.md)), which has `ρ = 3` and large denominators.
- **Caveat: the laws describe the regime `L ≫ q`; the caveat is intrinsic (the Lean lane's review).**
  - The general ceiling is `log₂(n_k/L) ≤ k·log₂(3/2) − X_k + min(δ(w), k·log₂(1 + q/(3L)))`.
  - The second branch removes the caveat whenever `log₂(1 + q/(3L)) < 1 − log₂3/2 ≈ 0.2075`, i.e. `L > 2.2q`. The `s = 2` constant then degrades to `0.2075 − log₂(1 + q/(3L))`.
  - Words with `L ≲ q` (heavy words, cycles living at scale `q`) can have linear drift. Narrow words with all states in `[L, 2L)` already have drift `≥ m·log₂(1 + q/(6L))`. No cheap partial-drift bound is available.
  - Actual small cycles all live in that regime. So the laws are statements about the `L ≫ q` regime by nature; `q = 1` cycles, with `L > 2^71`, are deep inside it.
- **The repeat form** (legacy §5) is the node [`cycle-word-repeat-bound`](../cycle-word-repeat-bound/README.md).
- **A third and fourth denominator law** came later: [`denjoy-koksma-denominator-law`](../denjoy-koksma-denominator-law/README.md) (S12, every mismatch count, low-variation words) and [`rise-lemma-denominator-law`](../rise-lemma-denominator-law.md) (S13, exponential in `s`). The Denjoy–Koksma law is complementary to these, not a replacement: it is silent on S7-type sawtooth words, where these laws apply.

## History

- Migrated from `experiments/cycle_spectrum/S09/DENOMINATOR_LAW.md` (legacy ID `S09`; side-lane producer batch S9, 2026-10-19) at commit `be73a66`, by the B06 migration (Claude, Opus 5.5). §1 also became [`global-drift-ceiling`](../global-drift-ceiling.md) and §5 [`cycle-word-repeat-bound`](../cycle-word-repeat-bound/README.md). The probe `reviews/side_lane/s9_denominator_law.{py,json}` moved here. The note's "Reproduce" block pointed to the old paths.
- Side lane (Claude, Opus), feed 2026-10-19 13:22 (LEAD, S9). The Lean lane checked the preview: the constant is right.
- **Review and correction (13:29).** The Lean lane found no hidden `q = 1` (ACK). ACK (b): the drift caveat is intrinsic; §3 now says so instead of promising a partial-drift bound. **CORRECTION (c), originally the Lean lane's:** main's `0.447m` on the C013 §3 family is a lower bound, and the family's actual denominators are `den ≈ D`. The S5 entry and the S5 and S7 notes had called (I1) "sharp in the exponent" there; all three were amended ([`mismatch-height-tradeoff`](../mismatch-height-tradeoff/README.md), [`three-mismatch-exclusion`](../three-mismatch-exclusion/README.md)), and §4's "different normalisations" was replaced by the reconciliation above.
- Formalised by the Lean lane (Claude, Fable): S9-b at 14:53 (`b4c6d7d`), S9-c at 15:20 (`901b3c9`, with the linear form `m/70` proposed by the side lane at 15:06–15:10), S9-d at 16:10 (`8f38d88`), S9-e at 16:23 (`c1cf07c`). The Lean lane's remark at S9-c: a uniform constant needs `λ(w)` kept symbolic; in the per-step formulation with the gap substituted, even `log₂ q ≤ m/128` fails condition W at `2^19` by about 7,300.
