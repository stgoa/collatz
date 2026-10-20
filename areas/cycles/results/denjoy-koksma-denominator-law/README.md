---
id: denjoy-koksma-denominator-law
kind: result
title: A denominator law for any number of mismatches, from the Denjoy–Koksma height bound
status: formal
claim: >
  For every primitive positive valuation word w (period m, total A, D = 2^A − 3^m > 0, letters ≥ 1) and every
  rotation 0 < h < m with gcd(h, m) = 1 having exactly s ≥ 1 mismatches, log₂ den(w) >
  1 + ⌈(m − s)/s⌉·log₂3 − (K(h/m) − 1)·(V_h + 2δ(w)) − λ(w), with K(h/m) the sum of the partial quotients
  of h/m, V_h = Σ_t |a_t − a_(t+h)|, δ(w) = A − m·log₂3 and λ(w) = log₂(m·2^A/(3D)); equivalently the same
  bound for log₂ q for a primitive odd cycle of 3x+q with such a rotation. No gap, period or L/q hypothesis.
  Informative only when (K − 1)·V_h is small; vacuous for h = 1 and for S7-type sawtooth words.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [denjoy-koksma-height-bound, paired-state-run-law]
lean:
  - LeanLane.Cyc.OddCycle.mis_empty_of_mod_zero
  - LeanLane.Cyc.OddCycle.dk_denominator_law
  - LeanLane.Cyc.OddCycle.ofWord_Vh
  - LeanLane.Cyc.OddCycle.word_dk_denominator_law
  - LeanLane.Cyc.OddCycle.Vh_sum_rotate
  - LeanLane.Cyc.OddCycle.word_dk_denominator_law'
  - LeanLane.Cyc.OddCycle.dk_denominator_law_coprime
  - LeanLane.Cyc.OddCycle.word_dk_denominator_law_coprime
evidence:
  - "s12_dk_denominator_law.py, s12_dk_denominator_law.json: side-lane probe (about 6 s): no violation on every primitive word over {1,2,3} up to length 12 with every coprime rotation (360,284 pairs), on 52,484 actual-cycle pairs (odd q < 2,000), and on 40 random near-critical low-variation chain words with 4-10 mismatches up to m = 3,200 (18 non-vacuous, slack ≥ 547 bits). Fails at its new path: it imports s1a_integer_cycle_check from its own folder (now in ../ordered-gap-closed-form/); with that folder on PYTHONPATH it exits 0 and leaves its receipt byte-identical (checked at migration). Passed at be73a66 as reviews/side_lane/s12_dk_denominator_law.py (archive/legacy-checker-run-be73a66.md)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Review of S12 §3a (labels (a) real versus integer height, (b) complementary to S9) and the scope remark on h = 1 (feed 17:32); formalised as S12-e, S9-e and S12-f part 3"
    link: ../../../../archive/side-lane/FEED.md
tags: [cycles, denominator, denjoy-koksma, 3x+d, formal]
---

# A denominator law for any number of mismatches, from the Denjoy–Koksma height bound

## Statement

Primitive positive word `w` (period `m`, total `A`, `D = 2^A − 3^m > 0`, letters `≥ 1`), reduced denominator `den(w) = D/gcd(C_w, D)`, drift `δ(w) = A − m·log₂3`, `λ(w) = log₂(m·2^A/(3D))`. For every rotation `0 < h < m` with `gcd(h, m) = 1` and exactly `s ≥ 1` mismatches,

```
log₂ den(w) > 1 + ⌈(m−s)/s⌉·log₂3 − (K(h/m) − 1)·(V_h + 2δ(w)) − λ(w),
```

with `K(h/m)` the sum of the partial quotients of `h/m` and `V_h = Σ_t |a_t − a_(t+h)|`. The same holds for a primitive odd cycle of `3x+q` with `log₂ q` on the left. The legacy note states it with `K` in place of `K − 1`; the formal version is the sharper one.

## Proof

Legacy S12 note §3a (side lane), lightly edited. Chain the longest run `t ≥ ⌈(m−s)/s⌉` (pigeonhole), the witness `2·3^t < H = L·2^B` ([`paired-state-run-law`](../paired-state-run-law.md)), the height bound `B ≤ (K − 1)·(V_h + 2δ)` ([`denjoy-koksma-height-bound`](../denjoy-koksma-height-bound/README.md)), and `L ≤ m·q·2^A/(3D)` (S7's (F4), Lean `three_L_D_le`).

Two labels from the Lean lane's review:
- **(a)** `B` here is the real log-height `log₂(n_max/L)`, which is what the `1 +` presupposes. With the integer band of the `OddCycle` structure (`n < 2^(B+1)·L`), the 1 cancels.
- **(b)** The law is **complementary to S9, not a replacement**. For S7-type sawtooth words, `V_h` is about the height and this law says nothing; [`two-three-mismatch-denominator-laws`](../two-three-mismatch-denominator-laws/README.md) covers `s ≤ 3` there. Conversely, S9 says nothing for `s ≥ 4`, where this law covers low-variation words.

## Certificates

None run by CI; `s12_dk_denominator_law.py` is a probe (see `evidence`): no violation in 360,284 exhaustive pairs (words over `{1,2,3}`, `m ≤ 12`), in 52,484 actual-cycle pairs, or in 40 low-variation chain words (18 non-vacuous, slack ≥ 547 bits).

## Lean

`lean/CycleSpectrum.lean` (axioms `propext`, `Classical.choice`, `Quot.sound`; receipts `lean/receipts/CycleSpectrum.*`), namespace `LeanLane.Cyc.OddCycle`:

- **S12-e** (iteration 85): `mis_empty_of_mod_zero`; **`dk_denominator_law`** (primitive cycle, rotation `h ≤ m` coprime to `m`, a ladder of `h/m` with `q_n = m` and admissible denominators, exactly `s ≥ 1` mismatches: `log 2 + ((m − 1)/s)·log 3 < log q + λ_nat + (K − 1)(V_h·log 2 + 2δ_nat)`); `ofWord_Vh`; **`word_dk_denominator_law`** (the same for a positive word with `den(w)`).
- **S9-e** (iteration 86): `Vh_sum_rotate`; **`word_dk_denominator_law'`** (no minimal-rotation normalisation).
- **S12-f part 3** (iteration 90): **`dk_denominator_law_coprime`**, **`word_dk_denominator_law_coprime`** (the ladder supplied by `ladder_of_coprime`: only `0 < h < m` and `gcd(h, m) = 1` remain, for words with `D_w > 0` and distinct rotated intercepts).

**Statement match.** `word_dk_denominator_law_coprime`, divided by `log 2`, is the Statement, with `(m − 1)/s` in natural division equal to `⌈(m−s)/s⌉` (checked for `m < 500`, `s < 60`), `λ_nat = log m + A·log 2 − log 3 − log D`, `δ_nat = A·log 2 − m·log 3`, `K = DK.cfK m h`. Primitivity is distinct rotated intercepts. No gap and no `L/q` hypothesis.

## Remarks

- **When it bites.** For low-variation words (small letter jumps at the mismatches) with tame `h/m`, the denominator is exponentially large for every fixed `s`, not only `s ≤ 3` as in S9. Each mismatch contributes at least 1 to `V_h`, so the law can exclude a word only if `(K − 1)·s² ≲ (m − 1)·log₂3`.
- **`h = 1` is vacuous** (the Lean lane's scope remark, ACK at 17:32): `K(1/m) = m` and `V_1 ≥ s ≥ 2`, so the right side carries at least `(m − 1)·s·log 2`, which exceeds the left side `log 2 + ((m − 1)/s)·log 3` for every `s ≥ 2` and `m ≥ 2`.
- **A complementary law** exponential in `s`, with no coprimality: [`rise-lemma-denominator-law`](../rise-lemma-denominator-law.md).

## History

- Split from `experiments/cycle_spectrum/S12/DENJOY_KOKSMA.md` §3a (legacy ID `S12`; side-lane producer batch S12, 2026-10-19) at commit `be73a66`, by the B06 migration (Claude, Opus 5.5). The probe `reviews/side_lane/s12_dk_denominator_law.{py,json}` moved here.
- Side lane (Claude, Opus), feed 2026-10-19 15:20 (S12 entry, "a denominator law for any number of mismatches"). Formalised by the Lean lane (Claude, Fable): S12-e at 16:15 (`2ab54ea`), S9-e at 16:23 (`c1cf07c`), S12-f part 3 at 16:54 (`03b2807`). Scope remark on `h = 1` acknowledged at 17:32.
