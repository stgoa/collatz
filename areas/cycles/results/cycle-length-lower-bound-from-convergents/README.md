---
id: cycle-length-lower-bound-from-convergents
kind: result
title: "A nontrivial 3x+1 cycle has at least 72,057,431,991 odd states and 114,208,327,604 halvings: Eliahou's continued-fraction bound, replayed"
status: written
claim: >
  Raw odd-only 3x+1 map on the positive odd integers. Let θ = log₂3 with convergents p_k/q_k and e_k = |q_kθ − p_k|.
  (1) A nontrivial cycle with m odd states, A halvings in total and minimum state L satisfies 2^A = Π(3 + 1/n_i),
  hence 0 < A − mθ < m/(3L·ln 2) < 0.481·m/L; call a pair (m, A) admissible for L if it satisfies this.
  (2) For q_k ≤ m < q_{k+1} let x, y be the integers with m = x·q_k + y·q_{k+1}, A = x·p_k + y·p_{k+1}; then
  A − mθ = (−1)^(k+1)·(x·e_k − y·e_{k+1}), and admissibility forces y ≥ 1, x ≤ −1 for even k and x ≥ 1, y ≤ 0 for
  odd k, with |x|·e_k < 0.481·q_{k+1}/L and |y|·e_{k+1} < 0.481·q_{k+1}/L; so the admissible pairs below any q_K form
  a finite set computed exactly by the certificate, whose least m bounds the period from below and is nonincreasing
  in L. (3) With the external input that every integer below 2^71 converges (L > 2^71): the least admissible pair is
  (m, A) = (q_23 − q_22, p_23 − p_22) = (72,057,431,991, 114,208,327,604), so every nontrivial cycle has at least
  72,057,431,991 odd states, at least 114,208,327,604 halvings and length at least 186,265,759,595 under the full
  Collatz map; the same least pair holds already for L ≥ 2^68. Calibration: for L = 2^40 the least admissible pair is
  (q_15, p_15) = (10,781,274, 17,087,915) and the admissible A below q_16 are 17,087,915 + 301,994·j, j = 0..3, which
  is Eliahou's 1993 bound and the first terms of his 301,994a + 17,087,915b + 85,137,581c; for L = 2^60 it is
  (q_19, p_19) = (397,573,379, 630,138,897). The continued fraction of θ is certified to 80 terms from a two-sided
  enclosure. The cited Hercher (2023) bound m > 1.375·10^11 (a different method) is not replayed. Nothing is claimed
  for 3x+d with d > 1, whose actual cycles have small minima.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-31
depends_on: []
assumes: [barina-2025-convergence-2-71]
certificates: [check_cycle_length_convergents.py]
evidence:
  - "cycle_length_convergents.json: the receipt; the 80 certified partial quotients and convergent denominators of log₂3, the check 0.481 > 1/(3 ln 2), the admissible pairs for L = 2^40, 2^60, 2^68, 2^71 with their lattice coordinates, and the control count on the 3x+d corpus"
tags: [cycles, period-bound, continued-fractions, replay, calibration, eliahou]
---

# A nontrivial `3x+1` cycle has at least 72,057,431,991 odd states and 114,208,327,604 halvings: Eliahou's continued-fraction bound, replayed

## Statement

Raw odd-only clock ([`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §1): a cycle of the map `n ↦ (3n + 1)/2^(v₂(3n+1))` on positive odd integers has states `n_1, …, n_m`, valuations `a_i = v₂(3n_i + 1)`, `A = Σ a_i` (the halvings), minimum `L = min n_i`. The trivial cycle is `{1}` (`m = 1`, `A = 2`); every other cycle is *nontrivial*, and none is known. Under the full Collatz map the cycle has length `m + A`; under the shortcut map `(3n+1)/2`, length `A`.

`θ = log₂3 = [1; 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3, 1, 1, 15, 1, 9, 2, 5, 7, …]`, convergents `p_k/q_k` (`p_0/q_0 = 1/1`, `2/1`, `3/2`, `8/5`, `19/12`, `65/41`, `84/53`, `485/306`, `1054/665`, `24727/15601`, …), `e_k = |q_kθ − p_k|`. The convergents used below:

| `k` | 13 | 14 | 15 | 16 | 19 | 22 | 23 |
|---|---|---|---|---|---|---|---|
| `q_k` | 190,537 | 10,590,737 | 10,781,274 | 53,715,833 | 397,573,379 | 65,470,613,321 | 137,528,045,312 |
| `p_k` | 301,994 | 16,785,921 | 17,087,915 | 85,137,581 | 630,138,897 | 103,768,467,013 | 217,976,794,617 |

**Theorem 1 (the cycle inequality).** A nontrivial cycle with `m` odd states, `A` halvings and minimum `L` satisfies

```
(1)   0 < A − mθ < m / (3L·ln 2) < 0.481·m/L.
```

A pair of positive integers `(m, A)` is called **admissible for `L`** if it satisfies (1). Admissibility is monotone: a pair admissible for `L′ ≥ L` is admissible for `L`.

**Theorem 2 (the admissible pairs).** Let `(m, A)` be admissible for `L` and `k` the index with `q_k ≤ m < q_(k+1)`. Let `x, y` be the integers with `m = x·q_k + y·q_(k+1)` and `A = x·p_k + y·p_(k+1)` (they exist and are unique because `p_(k+1)q_k − p_kq_(k+1) = (−1)^k`). Then

```
(2)   A − mθ = (−1)^(k+1)·(x·e_k − y·e_(k+1)) = |x|·e_k + |y|·e_(k+1),
```

where for even `k`: `y ≥ 1` and `x ≤ −1`; for odd `k`: `x ≥ 1` and `y ≤ 0`; and in both cases `|x|·e_k < 0.481·q_(k+1)/L` and `|y|·e_(k+1) < 0.481·q_(k+1)/L`. Hence the admissible pairs with `m < q_K` form a finite set, computed exactly by the certificate, and its least `m` is a lower bound for the period of every nontrivial cycle with minimum at least `L`.

**Corollary (with the external input).** Every positive integer below `2^71` reaches 1 ([`barina-2025-convergence-2-71`](../../../../sources/barina-2025-convergence-2-71.md)), so a nontrivial cycle has `L > 2^71`. The least admissible pair for `L = 2^71` is

```
(m, A) = (q_23 − q_22, p_23 − p_22) = (72,057,431,991, 114,208,327,604),      m + A = 186,265,759,595,
```

so every nontrivial cycle has at least `72,057,431,991` odd states, at least `114,208,327,604` halvings, and length at least `186,265,759,595` under the full map. The next admissible pairs are `(q_23, p_23) = (137,528,045,312, 217,976,794,617)` and `(q_23 + j(q_23 − q_22) … )`; the receipt lists all 59 admissible pairs below `q_24 = 753,110,839,881`. The same least pair is already forced by `L ≥ 2^68`.

**Calibration.** For `L = 2^40` the least admissible pair is `(q_15, p_15) = (10,781,274, 17,087,915)`, and the admissible pairs below `q_16` have `A = 17,087,915 + 301,994·j`, `j = 0, 1, 2, 3` (lattice coordinates `(x, y) = (1 + 5j, −j)` at `k = 15`, since `5p_15 − p_16 = p_13 = 301,994`): this is Eliahou's bound `A ≥ 17,087,915` on the shortcut length and the beginning of his form `301,994a + 17,087,915b + 85,137,581c`. For `L = 2^60`: `(q_19, p_19) = (397,573,379, 630,138,897)`.

## Proof

**Theorem 1.** For each state, `2^(a_i) = (3n_i + 1)/n_(i+1)` (indices modulo `m`); multiplying around the cycle, `2^A = Π_i (3n_i + 1)/n_(i+1) = Π_i (3 + 1/n_i)` because `Π n_i = Π n_(i+1)`. Every factor exceeds 3 and is at most `3 + 1/L`, with equality in every factor only when all states equal `L`, i.e. `m = 1`, where `3L + 1 = 2^A·L` forces `L = 1`: the trivial cycle. So for a nontrivial cycle `3^m < 2^A < (3 + 1/L)^m`, i.e. `0 < A·ln 2 − m·ln 3 < m·ln(1 + 1/(3L)) < m/(3L)`; dividing by `ln 2` gives (1), with `1/(3·ln 2) = 0.4809… < 0.481` (certificate V2). Monotonicity in `L` is clear from the form of (1). ∎

**Theorem 2.** Standard facts about convergents: `p_(k+1)q_k − p_kq_(k+1) = (−1)^k`; the signs of `q_kθ − p_k` alternate, `q_kθ − p_k = (−1)^k e_k` (`p_k/q_k < θ` for even `k`); `e_k > 0`; `q_(k+1) > q_k` for `k ≥ 1`. The linear system `x·q_k + y·q_(k+1) = m`, `x·p_k + y·p_(k+1) = A` has determinant `±1`, so it has a unique integer solution for every integer pair `(m, A)`. Then

```
A − mθ = x(p_k − q_kθ) + y(p_(k+1) − q_(k+1)θ) = x·(−1)^(k+1)e_k + y·(−1)^(k+2)e_(k+1) = (−1)^(k+1)(x·e_k − y·e_(k+1)),
```

which is the first equality in (2). Now let `(m, A)` be admissible, so `A − mθ > 0` and `0 < m < q_(k+1)`.

*Even `k`:* `A − mθ = y·e_(k+1) − x·e_k > 0`. If `y ≤ 0` then `x·e_k < y·e_(k+1) ≤ 0`, so `x < 0` and `m = x·q_k + y·q_(k+1) < 0`, impossible; hence `y ≥ 1`, and `m < q_(k+1)` gives `x·q_k < (1 − y)·q_(k+1) ≤ 0`, so `x ≤ −1`. Then `A − mθ = |y|·e_(k+1) + |x|·e_k`.

*Odd `k`:* `A − mθ = x·e_k − y·e_(k+1) > 0`. If `x ≤ 0` then `y·e_(k+1) < x·e_k ≤ 0`, so `y < 0` and `m < 0`, impossible; hence `x ≥ 1`, and `m < q_(k+1)` gives `y·q_(k+1) < q_(k+1) − x·q_k < q_(k+1)`, so `y ≤ 0`. Then `A − mθ = |x|·e_k + |y|·e_(k+1)`.

In both cases (1) gives `|x|·e_k + |y|·e_(k+1) = A − mθ < 0.481·m/L < 0.481·q_(k+1)/L`, which bounds `|x|` and `|y|`; for each `k` there are finitely many candidates, each decided by (1) itself. The least admissible `m` is a lower bound for the period because every nontrivial cycle with minimum `L′ ≥ L` yields a pair admissible for `L′`, hence for `L`. ∎

**The corollary and the calibration** are the certificate's enumeration (V3), which decides each candidate pair by interval arithmetic on the enclosure of `θ` and fails if any candidate is undecided. ∎

## Certificates

[`check_cycle_length_convergents.py`](check_cycle_length_convergents.py) (standard library, about one second): **V1** the continued fraction of `θ` to 80 terms from a two-sided rational enclosure `lo < θ < hi` built from the correctly rounded `decimal` logarithms of 2 and 3 at precisions 160 and 220 (the four expansions agree on all 80 terms; the reals with a given initial expansion form an interval containing `lo` and `hi`, hence `θ`), the convergents by the recurrence, and the exact integer cross-check `2^(p_k) > 3^(q_k)` for odd `k` and `<` for even `k` on the nine convergents with `q_k ≤ 3000`; **V2** `3·0.481·ln 2 > 1` against the enclosure of `ln 2`; **V3** for `L = 2^40, 2^60, 2^68, 2^71`, the admissible pairs below `q_K` (with `K` the first index giving at least three admissible `m`), each candidate `(k, x, y)` of Theorem 2 decided by the enclosure of `e_k, e_(k+1)` (an undecided candidate fails the certificate), the least `m`, the least `m + A`, and the first pairs with their lattice coordinates; **V4** controls: on all 2,459 cycles of the `3x+d` corpus ([`actual-cycles-3x-d-corpus`](../actual-cycles-3x-d-corpus/README.md), 333 values of `d ≤ 999`), the exact identity `2^A·Π n_i = Π(3n_i + d)` and the exact inequalities `3^m < 2^A ≤ (3 + d/L)^m` (cleared of denominators), with equality exactly for the one-state cycles; **V5** the receipt [`cycle_length_convergents.json`](cycle_length_convergents.json) (`--write-receipt` regenerates it). Finite statements only; the theorems' proofs are the text above.

## Remarks

- **What is replayed.** Theorems 1 and 2 are the argument of Eliahou (1993, [`eliahou-1993-cycle-length`](../../../../sources/eliahou-1993-cycle-length.md)): the cycle inequality plus the lattice description of the fractions `A/m` near `θ`. At `L = 2^40` the enumeration returns his constants exactly (`17,087,915 = p_15` as the least shortcut length, `301,994 = p_13` as the step, `85,137,581 = p_16`), which fixes the earlier confusion in the source node between the shortcut length `A` and the odd period `m` (`m = q_15 = 10,781,274` for his least case). At `L = 2^68` the least pair gives `A ≥ 114,208,327,604`, the number quoted in the literature for the `2^68` verification range (not checked against a source here); with `L = 2^71` the least pair is the same, because `(q_23 − q_22, p_23 − p_22)` remains admissible up to `L ≈ 0.481·m/(e_22 + e_23) ≈ 4.4·2^71`.
- **What is not replayed.** The cited bound `m > 1.375·10^11` ([`hercher-2023-cycle-length`](../../../../sources/hercher-2023-cycle-length.md), Corollary 29, from his Lemma 26 rather than from (1) alone) is about twice the bound here and excludes the pair `(72,057,431,991, 114,208,327,604)` by other means; it stays unreplayed, as do the `m`-cycle exclusions of [`local-minima-cycle-exclusion-replay`](../../questions/local-minima-cycle-exclusion-replay.md). The present bound already exceeds every period import the lane's cycle results needed (`m > 452,695` in [`three-mismatch-exclusion`](../three-mismatch-exclusion/README.md) and [`two-mismatch-exclusion-via-gap`](../two-mismatch-exclusion-via-gap/README.md)), so those imports can be met by a bound checked in this repository.
- **Sharpness.** Theorem 2 describes *all* pairs compatible with (1), so the least `m` cannot be improved by any argument that uses only the size of the cycle equation; the first excluded candidate below it, `(q_22, p_22)`, fails because `p_22/q_22 < θ` (even `k`), and `(q_22, p_22 + 1)` fails because then `A − mθ ≈ 1`. A better lower bound must use more than (1), as Hercher's does.
- **Clocks.** `m` counts odd states (the repository's odd-only period), `A` the halvings; the full Collatz map takes `m + A` steps around the cycle and the shortcut map `A` steps. Eliahou's numbers are shortcut lengths `A`; Hercher's `K` counts odd members and equals our `m`.
- **Controls.** The identity and inequalities (1) hold for `3x+d` with `1/L` replaced by `d/L` (certificate V4), but the admissibility analysis needs `L` large relative to `d`: the actual cycles of `3x+5`, `3x+7`, `3x+13`, `3x+61` have minima below `d²` and are not excluded, as they must not be. Novelty: none; this is a replay with exact certified constants.
- **On the enclosure of `θ`.** The certificate relies on Python's `decimal` module computing `ln` correctly rounded (documented behaviour of the standard library); the nine smallest convergents are additionally confirmed by exact integer comparisons of powers of 2 and 3, and the partial quotients agree with the published expansion of `log₂3`.

## History

- Written 2026-10-31 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, as the first replayed period bound in the repository. A first draft of the same day used only the coarse step `|mθ − A| ≥ e_k` and stated `m ≥ q_22 = 65,470,613,321`; the certificate's sharpness check showed that `(q_22, p_22)` lies on the wrong side of `θ`, and the full lattice classification (Theorem 2) replaced it before the node was merged.
