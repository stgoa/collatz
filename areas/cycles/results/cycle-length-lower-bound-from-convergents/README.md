---
id: cycle-length-lower-bound-from-convergents
kind: result
title: "A nontrivial 3x+1 cycle has at least 65,470,613,321 odd states: the continued-fraction period bound, replayed"
status: written
claim: >
  Raw odd-only 3x+1 map on the positive odd integers. Let θ = log₂3 with convergents p_k/q_k (q_0 = 1). A nontrivial
  cycle with m odd states, A halvings in total and minimum state L satisfies 2^A = Π(3 + 1/n_i), hence
  0 < A − mθ < m/(3L·ln 2) < 0.481·m/L, and therefore, for the index k with q_k ≤ m < q_{k+1},
  m > L/(0.481·(q_k + q_{k+1})). Consequently m ≥ B(L) := max(q_{k₁}, ⌊L/(0.481·(q_{k₁} + q_{k₁+1}))⌋ + 1), where k₁ is the
  least k with q_{k+1}·(q_k + q_{k+1}) > L/0.481, and the total length of the cycle under the full Collatz map is
  m + A ≥ B(L) + ⌊B(L)·θ⌋ + 1. With the external input that every integer below 2^71 converges (so L > 2^71):
  k₁ = 22, q_22 = 65,470,613,321, q_23 = 137,528,045,312, and every nontrivial cycle has m ≥ 65,470,613,321 odd states
  and total length ≥ 169,239,080,335. Calibration: L = 2^40 gives m ≥ 212,024, L = 2^60 gives m ≥ 397,573,379,
  L = 2^68 gives m ≥ 8,515,611,666. The continued fraction of θ is certified to 80 terms from a two-sided
  enclosure. This replays the method of Eliahou (1993) in its simplest form; his finer classification of the
  admissible lengths is not reproduced, and the bound is about half of the cited Hercher (2023) bound m > 1.375·10^11,
  which is not replayed. Nothing is claimed for 3x+d with d > 1, whose actual cycles have small minima.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-31
depends_on: []
assumes: [barina-2025-convergence-2-71]
certificates: [check_cycle_length_convergents.py]
evidence:
  - "cycle_length_convergents.json: the receipt; the 80 certified partial quotients and convergent denominators of log₂3, the check 0.481 > 1/(3 ln 2), the bounds B(L) and the total-length bounds for L = 2^40, 2^60, 2^68, 2^71, and the control count on the 3x+d corpus"
tags: [cycles, period-bound, continued-fractions, replay, calibration]
---

# A nontrivial `3x+1` cycle has at least 65,470,613,321 odd states: the continued-fraction period bound, replayed

## Statement

Raw odd-only clock ([`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §1): a cycle of the map `n ↦ (3n + 1)/2^(v₂(3n+1))` on positive odd integers has states `n_1, …, n_m`, valuations `a_i = v₂(3n_i + 1)`, `A = Σ a_i`, minimum `L = min n_i`. The trivial cycle is `{1}` (`m = 1`, `A = 2`); every other cycle is *nontrivial*, and no nontrivial cycle is known.

Write `θ = log₂3 = [1; 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3, 1, 1, 15, 1, 9, 2, 5, 7, …]` with convergents `p_k/q_k` (`p_0/q_0 = 1/1`, `p_1/q_1 = 2/1`, `p_2/q_2 = 3/2`, `8/5`, `19/12`, `65/41`, `84/53`, `485/306`, `1054/665`, `24727/15601`, …). The denominators used below are

| `k` | 13 | 14 | 15 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|
| `q_k` | 190,537 | 10,590,737 | 10,781,274 | 397,573,379 | 6,189,245,291 | 6,586,818,670 | 65,470,613,321 | 137,528,045,312 |

**Theorem.** Let a nontrivial cycle have `m` odd states, `A` halvings and minimum `L`. Then

```
(1)   0 < A − mθ < m / (3L·ln 2) < 0.481·m/L,
(2)   m > L / (0.481·(q_k + q_(k+1)))      for the k with q_k ≤ m < q_(k+1),
(3)   m ≥ B(L) := max( q_(k₁),  ⌊ L / (0.481·(q_(k₁) + q_(k₁+1))) ⌋ + 1 ),     k₁ := min{ k : q_(k+1)·(q_k + q_(k+1)) > L/0.481 },
(4)   m + A ≥ B(L) + ⌊B(L)·θ⌋ + 1       (the length of the cycle under the full Collatz map).
```

**Corollary (with the external input).** Every positive integer below `2^71` reaches 1 ([`barina-2025-convergence-2-71`](../../../../sources/barina-2025-convergence-2-71.md)), so a nontrivial cycle has `L > 2^71`, `k₁ = 22`, and

```
m ≥ 65,470,613,321 = q_22,        m + A ≥ 169,239,080,335.
```

**Calibration values** (from the certificate): `B(2^40) = 212,024` (`k₁ = 13`), `B(2^60) = 397,573,379 = q_19`, `B(2^68) = 8,515,611,666` (`k₁ = 21`, the second branch of the maximum), `B(2^71) = 65,470,613,321 = q_22`.

## Proof

**(1).** For each state, `2^(a_i) = (3n_i + 1)/n_(i+1)` (indices modulo `m`), so multiplying around the cycle, `2^A = Π_i (3n_i + 1)/n_(i+1) = Π_i (3 + 1/n_i)` because `Π n_i = Π n_(i+1)`. Every factor exceeds 3 and is at most `3 + 1/L`, with equality in all factors only when all states equal `L`, i.e. for `m = 1`, where `3L + 1 = 2^A·L` forces `L = 1`: the trivial cycle. So for a nontrivial cycle `3^m < 2^A < (3 + 1/L)^m`, i.e. `0 < A·ln 2 − m·ln 3 < m·ln(1 + 1/(3L)) < m/(3L)`; dividing by `ln 2` gives `0 < A − mθ < m/(3L·ln 2)`, and `1/(3·ln 2) = 0.4809… < 0.481` (the certificate checks `3·0.481·ln 2 > 1` against an enclosure of `ln 2`).

**Two facts about convergents** (standard; proofs included for completeness). Let `e_k = |q_kθ − p_k|`; the signs of `q_kθ − p_k` alternate (`p_k/q_k < θ` for even `k`, `> θ` for odd `k`), `p_(k+1)q_k − p_kq_(k+1) = (−1)^k`, and `q_(k+1) = a_(k+1)q_k + q_(k−1)`.

*Fact A (best approximation of the second kind).* If `0 < m < q_(k+1)` and `A` is any integer, then `|mθ − A| ≥ e_k`. *Proof.* Solve `x·q_k + y·q_(k+1) = m`, `x·p_k + y·p_(k+1) = A` in integers (the determinant is `±1`). If `y = 0` then `m = x·q_k` with `x ≥ 1` and `|mθ − A| = x·e_k ≥ e_k`. If `x = 0` then `m = y·q_(k+1) ≥ q_(k+1)`, excluded. Otherwise `0 < m < q_(k+1)` forces `x` and `y` to have opposite signs; since `q_kθ − p_k` and `q_(k+1)θ − p_(k+1)` also have opposite signs, the two terms of `mθ − A = x(q_kθ − p_k) + y(q_(k+1)θ − p_(k+1))` have the same sign, so `|mθ − A| ≥ |x|·e_k ≥ e_k`. ∎

*Fact B.* `e_k > 1/(q_k + q_(k+1))`. *Proof.* With the complete quotient `α_(k+1) = [a_(k+1); a_(k+2), …] < a_(k+1) + 1`, the standard formula `e_k = 1/(α_(k+1)q_k + q_(k−1))` gives `e_k > 1/((a_(k+1) + 1)q_k + q_(k−1)) = 1/(q_(k+1) + q_k)`. ∎

**(2).** Let `q_k ≤ m < q_(k+1)` (such `k` exists since `q_0 = 1 ≤ m` and `q_k → ∞`). By (1), Fact A and Fact B, `0.481·m/L > A − mθ = |mθ − A| ≥ e_k > 1/(q_k + q_(k+1))`, which is (2).

**(3).** From `m < q_(k+1)` and (2), `q_(k+1)·(q_k + q_(k+1)) > L/0.481`, so `k ≥ k₁`. For `k = k₁`, (2) and `m ≥ q_(k₁)` give `m ≥ B(L)`. For `k > k₁`, `m ≥ q_k ≥ q_(k₁+1)`, and `q_(k₁+1) ≥ B(L)` because `q_(k₁+1) ≥ q_(k₁)` and `q_(k₁+1) ≥ L/(0.481·(q_(k₁) + q_(k₁+1)))` is the defining inequality of `k₁`. ∎

**(4).** `A > mθ` by (1), so `A ≥ ⌊mθ⌋ + 1`, and `m + ⌊mθ⌋ + 1` is increasing in `m`. ∎

**The corollary** substitutes `L > 2^71` (so `B(L) ≥ B(2^71)`, since `B` is nondecreasing in `L`) and the certified convergents: `q_23·(q_22 + q_23) = 2.79·10^22 > 2^71/0.481 = 4.91·10^21 > q_22·(q_21 + q_22) = 4.72·10^21`, so `k₁ = 22`; the second branch of the maximum is `⌊2^71/(0.481·(q_22 + q_23))⌋ + 1 = 24,180,773,870 < q_22`. ∎

## Certificates

[`check_cycle_length_convergents.py`](check_cycle_length_convergents.py) (standard library, under a second): **V1** the continued fraction of `θ` to 80 terms from a two-sided rational enclosure `lo < θ < hi` built from the correctly rounded `decimal` logarithms of 2 and 3 at precisions 160 and 220 (the four expansions agree on all 80 terms; since the reals with a given initial expansion form an interval containing `lo` and `hi`, the terms are those of `θ`), the convergents by the recurrence, and the exact integer cross-check `2^(p_k) > 3^(q_k)` for odd `k` and `<` for even `k` on the nine convergents with `q_k ≤ 3000`; **V2** `3·0.481·ln 2 > 1` against the enclosure of `ln 2`; **V3** `k₁`, `B(L)` and the total-length bound for `L = 2^40, 2^60, 2^68, 2^71`, with `⌊B·θ⌋` determined by the enclosure; **V4** controls: on all 2,459 cycles of the `3x+d` corpus ([`actual-cycles-3x-d-corpus`](../actual-cycles-3x-d-corpus/README.md), 333 values of `d ≤ 999`), the exact identity `2^A·Π n_i = Π(3n_i + d)` and the exact inequalities `3^m < 2^A ≤ (3 + d/L)^m` (cleared of denominators), with equality exactly for the one-state cycles; **V5** the receipt [`cycle_length_convergents.json`](cycle_length_convergents.json) (`--write-receipt` regenerates it). Finite statements only; the theorem's proof is the text above.

## Remarks

- **What is replayed and what is not.** Eliahou (1993, [`eliahou-1993-cycle-length`](../../../../sources/eliahou-1993-cycle-length.md)) uses exactly the inequality (1) and the continued fraction of `θ`, but then classifies all fractions `A/m` in the admissible interval (convergents and intermediate fractions), which for the verification range of his time gives his statement that the shortcut length `A` is `301,994a + 17,087,915b + 85,137,581c` (these are `p_13`, `p_15` and `p_16`; the `m` behind `17,087,915` is `q_15 = 10,781,274`). The bound here keeps only the coarse step `|mθ − A| ≥ e_k` and gives `m ≥ 212,024` at `L = 2^40`, far below his `m = q_15`; the finer classification is the natural next step and is not done here. The cited Hercher bound `m > 1.375·10^11` ([`hercher-2023-cycle-length`](../../../../sources/hercher-2023-cycle-length.md), Corollary 29, a different method) is about twice the bound proved here and remains unreplayed. The present bound already exceeds every period import the lane's cycle results needed (`m > 452,695` in [`three-mismatch-exclusion`](../three-mismatch-exclusion/README.md) and [`two-mismatch-exclusion-via-gap`](../two-mismatch-exclusion-via-gap/README.md)), so those imports can be met by a bound checked in this repository.
- **Sharpness of the coarse step.** At `L = 2^71` the bound is the convergent denominator `q_22` itself, because the other branch of the maximum, `L/(0.481(q_22 + q_23))`, is smaller. Whether `m = q_22` is admissible depends on `e_22·L < 0.481·q_22`, which (1) does not decide without the finer analysis; so (3) is the best this step gives, and a refinement would start from the intermediate fractions between `p_22/q_22` and `p_23/q_23`.
- **Clocks.** `m` counts odd states (the repository's odd-only period), `A` the halvings; the full Collatz map takes `m + A` steps around the cycle and the shortcut map `A` steps. Eliahou's numbers are shortcut lengths `A`; Hercher's `K` counts odd members and equals our `m`. The source node of Eliahou records the earlier confusion of `A` with `m`.
- **Controls.** The identity and inequalities (1) hold for `3x+d` with `1/L` replaced by `d/L` (certificate V4), but the bound (3) needs `L` large relative to `d`: the actual cycles of `3x+5`, `3x+7`, `3x+13`, `3x+61` have minima below `d^2` and are not excluded, as they must not be. Novelty: none; this is a replay with exact certified constants, which the repository's calibration programme ([`local-minima-cycle-exclusion-replay`](../../questions/local-minima-cycle-exclusion-replay.md)) asked for in a stronger form.
- **On the enclosure of `θ`.** The certificate relies on Python's `decimal` module computing `ln` correctly rounded (documented behaviour of the standard library); the nine smallest convergents are additionally confirmed by exact integer comparisons of powers of 2 and 3, and the partial quotients agree with the published expansion of `log₂3`.

## History

- Written 2026-10-31 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, as the first replayed period bound in the repository.
