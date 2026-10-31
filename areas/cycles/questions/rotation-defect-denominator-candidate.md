---
id: rotation-defect-denominator-candidate
kind: question
title: "Is g^s·4^m < 2^(As)·3^m for every word and every rotation with s mismatches?"
status: open
claim: >
  Prove or refute: for every positive valuation word w of length m with total A, D = 2^A − 3^m > 0 and
  g = gcd(C_w, D), and every nonidentity rotation differing from w in s ≥ 2 positions,
  g^s·4^m < 2^(As)·3^m, equivalently q = D/g > (1 − 3^m/2^A)·(4/3)^(m/s). Raw odd-only clock, any 3x+q.
  At s = 2 it is proved. If true, with the explicit linear-form bound it would force every nontrivial
  integer 3x+1 cycle to have s > log(4/3)·m/(600,000,000·(1 + log(2m))) for every rotation.
created: 2026-10-19
tags: [cycles, rotation-distance, conjecture]
---

# Is g^s·4^m < 2^(As)·3^m for every word and every rotation with s mismatches?

## Question

For a positive word `w` (length `m`, total `A`, `D = 2^A − 3^m > 0`, `g = gcd(C_w, D)`, `q = D/g`) and a nonidentity rotation differing from it in `s` positions, the **candidate** (legacy C012) is

```
g^s·4^m < 2^(As)·3^m,     equivalently     q > (1 − 3^m/2^A)·(4/3)^(m/s).
```

The two forms are equivalent. It is stated for every member of the `3x+q` family; actual cycles have `q = d` and must satisfy it.

## Why it matters

**Conditional payoff (heuristic until the candidate is proved).** A nontrivial integer cycle has `A < 2m`; with the explicit bound of [`languasco-2025-two-primes`](../../../sources/languasco-2025-two-primes.md) at `q = 1` the candidate would force

```
s > log(4/3)·m / (600,000,000·(1 + log(2m)))
```

for every rotation, i.e. `ρ(w) = Ω(m/log m)`: a strong form of [`rotation-distance-growth`](rotation-distance-growth.md). This is an implication, not an achieved bound.

## Known progress

- `s = 2` is proved: (7) of [`two-defect-cancellation-bound`](../results/two-defect-cancellation-bound.md), `g² < 2^(2A−2m)·3^m`, which is the candidate at `s = 2`; in Lean, `LeanLane.Cyc.two_defect_q_bound` is exactly its cleared integer form (normal form).
- Obstructions to proofs: adjugate elimination of the coupled system is vacuous for `s ≥ 3` ([`coupled-defect-matrix-smith-form`](../results/coupled-defect-matrix-smith-form/README.md)); three mismatches can hide an arbitrary background, beyond any fixed S-unit description ([`three-defect-arbitrary-background`](../results/three-defect-arbitrary-background.md)); termwise divisibility fails ([`termwise-plateau-divisibility`](../attempts/termwise-plateau-divisibility.md)). None refutes the candidate.
- A shared-background analogue is proved: [`shared-background-denominator-law`](../results/shared-background-denominator-law/README.md), but its count `r` is not `s`.
- **Finite evidence, and when it discriminates.** Every `q > 1` is coprime to 6, so `q ≥ 5`, and the candidate can fail only when `(1 − 3^m/2^A)·(4/3)^(m/s) ≥ 5`, needing `m/s ≥ log 5/log(4/3) ≈ 5.6`. All stored cycles pass, but nondiscriminatingly (`m/s ≤ 5`). The side lane's exhaustive grid (all primitive words of length ≤ 9, letters 1–5: 18,892,900 rotations) has no counterexample and **0** discriminating cases; its structured random search (`(x_1, U, x_2, U, …, x_s, U)`, `s = 3, 4, 5`, `m/s` up to about 21) found **56,150 discriminating cases of 59,759, no failure**, worst exponent ratio 0.525 at `m = 18`, `s = 3`, `g = 1837` (certificate `c012_candidate_check.py` in [`coupled-defect-matrix-smith-form`](../results/coupled-defect-matrix-smith-form/README.md); feed 2026-10-19 04:35). Random, not adversarial; finite evidence does not bear on large `m`.
- **Exhaustive census (2026-10-28).** [`few-arc-codings-denominator-census`](../results/few-arc-codings-denominator-census/README.md) enumerates every primitive word with a rotation of exactly `s` mismatches (`gcd(h, m) = 1`, plus the `gcd ∈ {2, 3}` two-arc words) for `s = 2` (`m ≤ 40`, letters `≤ 8`), `s = 3` (`m ≤ 30`, letters `≤ 4`) and `s = 4` (`m ≤ 22`, letters `≤ 3`): 493,483 census entries (a word is counted once per census it belongs to), 334,731 of them discriminating (`m ≥ 6s`), **no failure**, and the slack grows linearly in `m` (`log₂` of the ratio at most `−8.75`, `−17.5`, `−13.5` for `s = 2, 3, 4`, falling to `−99` at `s = 3`, `m = 30`). The sharp statement the data points at is the stronger `G² < 2^A` for `m ≥ 9`, posed as [`half-cancellation-for-few-mismatch-words`](half-cancellation-for-few-mismatch-words.md); it implies this candidate for every `s`.
- The C013 batch's own generated tests were labelled nondiscriminating by the main lane. The unreviewed C014 draft (`SIDE_REVIEW.md` in [`compatible-arcs-common-partition-limits`](../results/compatible-arcs-common-partition-limits/README.md)) argues that label was too strong (the observed `q` already contains the cancellation under study) and counts 178 of C013's 243 cases above the floor, 96 of 141 with at least three mismatches. That correction is unverified.

## Suggested attacks

- Adversarial tests: the sharpness families (arbitrary even `s`, prescribed divisors of `g`) of [`coupled-defect-matrix-smith-form`](../results/coupled-defect-matrix-smith-form/README.md); restrict any test to the discriminating region.
- A size estimate on the two surviving coupled congruences, using the actual rotation compatibility of the arcs (legacy C012/C013 recommendation).

## History

- 2026-10-28: Known progress gains the exhaustive few-arc census and the sharper half-cancellation question (Claude cycles lane, Fable 5.1).
- 2026-10-31: the half form [`half-cancellation-for-few-mismatch-words`](half-cancellation-for-few-mismatch-words.md) was refuted ([`half-cancellation-counterexample-rotation-pair`](../results/half-cancellation-counterexample-rotation-pair/README.md)); the counterexample satisfies this candidate at `s = 4` (`G^4·4^20 = 2^(128.95) < 2^160·3^20 = 2^(191.70)`), which therefore stands, with [`primitive-cancellation-below-half`](primitive-cancellation-below-half.md) as its surviving sharp form (Claude cycles lane, Fable 5.1).
