---
id: explicit-valuation-large-deviations
kind: result
title: Explicit large deviations for Syracuse valuation sums, with exact integer counts
status: written
claim: >
  Odd-only clock, odd positive N, any odd d (map S_d(N) = (3N+d)/2^v2(3N+d)); a_j the j-th valuation, A_n = a_1 +
  ... + a_n. (L1) The word (a_1, ..., a_n) is determined by N mod 2^(A_n+1), and each word is exactly one odd class
  mod 2^(A_n+1). (L2) For a_j iid with P(a = k) = 2^(-k), k >= 1, and every real t with n < t < 2n:
  P(A_n <= t) <= min_(u>1) u^t/(2u-1)^n = exp(-n I(t/n)), I(theta) = theta log(2(theta-1)/theta) - log(theta-1),
  positive on (1,2) and decreasing to 0 at theta = 2; exactly C(floor t, n) words of length n have A_n <= t.
  (L2') For every integer X >= 1, n >= 1 and n < t < 2n: #{odd N <= X : A_n(N) <= t} <= (X/2) exp(-n I(t/n)) +
  C(floor t, n), with the same constants for every odd d. A calibration of Terras (1976), Everett (1977) and the
  Chernoff step of Lagarias (1985), Theorem B, with every constant explicit; no novelty claim, no convergence claim.
authors:
  - Claude explicit-Tao lane (Opus)
created: 2026-10-18
depends_on: []
certificates: [check_L2.py, fable_L2_check.py]
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-18
    link: fable_L2_check.py
    scope: "Side-lane feed 2026-10-18 19:36, CONFIRMED at claude/explicit-tao 88d2424: an independent probe (nothing imported) re-checks the rate formula against numerical minimisation, the Chernoff bound against the exact law for n <= 60 and theta in [1.3, 1.95] (worst ratio 0.61), the hockey-stick word count, and (L2') on actual integers at X = 2^20, n in {6, 8, 10}, theta in {1.6, 1.7, 1.8}, d in {1, 5}. It found four hand-quoted I(theta) values misprinted (three overstated), corrected in e01d62f. A finite re-check, not a recorded line-by-line reading of the proof, so the node stays written"
aliases: [TAO-L2, TAO-L1]
tags: [convergence, explicit-tao, large-deviations, valuations, cylinders, calibration, explicit-constants]
---

# Explicit large deviations for Syracuse valuation sums, with exact integer counts

## Statement

Clock: odd-only Syracuse arrows. Domain: positive odd integers. Everything below is for the map `S_d(N) = (3N+d)/2^(v_2(3N+d))` with `d = 1` unless stated; the proofs use only that `3` is invertible modulo powers of 2 and that `3N+d` is even for odd `N`, so each statement holds verbatim for every odd `d` (checked for `d = 5`).

For odd `N` put `a_1(N) = v_2(3N+1)`, `N_1 = S(N)`, and inductively `a_j = v_2(3N_(j−1)+1)`, `N_j = S(N_(j−1))`. Write `A_j = a_1+…+a_j`, `A = A_n`. The affine formula is

```
S^n(N) = (3^n N + C_w) / 2^A,   C_w = Σ_(j=0)^(n−1) 3^(n−1−j) 2^(A_j),   A_0 = 0.   (1)
```

**L1 (exact cylinders).** The word `w = (a_1,…,a_n)` is determined by `N mod 2^(A+1)`, and the odd `N` with word `w` form exactly one odd residue class modulo `2^(A+1)`.

**Lemma L2.** Let `a_1, a_2, …` be independent with `P(a = k) = 2^(−k)` for integers `k >= 1`, and `A_n = a_1+…+a_n`. For every real `t` with `n < t < 2n`,

```
P(A_n <= t) <= min_(u>1) u^t / (2u−1)^n = exp(−n I(t/n)),            (2)
I(θ) = θ log(2(θ−1)/θ) − log(θ−1),      1 < θ < 2,                   (3)
```

with the minimum attained at `u* = θ/(2(θ−1))`. `I` is positive on `(1,2)`, `I(θ) → 0` as `θ → 2`, and the bound is monotone in `t`. Moreover the number of words of length `n` with `A_n <= t` is exactly `C(⌊t⌋, n)`.

**Lemma L2'.** For every integer `X >= 1`, every `n >= 1` and every real `t` with `n < t < 2n`,

```
#{odd N <= X : A_n(N) <= t} <= (X/2) exp(−n I(t/n)) + C(⌊t⌋, n).        (4)
```

The one-round descent that follows from L1 and L2' (legacy L3) is the separate node [`explicit-one-round-descent`](../explicit-one-round-descent.md).

## Proof

**L1.** Induction on `n`: `a_1 = k` means `3N+1 ≡ 2^k (mod 2^(k+1))`, one odd class mod `2^(k+1)`; then `S(N) mod 2^(A'+1)` is determined by `N mod 2^(a_1+A'+1)` because `3` is invertible. This is the repository's frozen cylinder fact and Terras's Theorem 1.2 ([`terras-1976-stopping-time`](../../../../sources/terras-1976-stopping-time.md)).

Consequently, for an odd `N` drawn uniformly from any complete set of odd residues modulo `2^(A+1)`, `P(word = w) = 2^(−A)`, so the `a_j` are independent with `P(a_j = k) = 2^(−k)`, `k >= 1` (geometric, mean 2).

**L2.** For `u > 1`, `P(A_n <= t) = P(u^(−A_n) >= u^(−t)) <= u^t E[u^(−A_n)] = u^t (E u^(−a))^n` by Markov's inequality, and `E u^(−a) = Σ_(k>=1) (2u)^(−k) = 1/(2u−1)`. Minimising `u^θ/(2u−1)` over `u > 1` for `t = θn`: the derivative of `θ log u − log(2u−1)` vanishes at `θ(2u−1) = 2u`, i.e. `u* = θ/(2(θ−1))`, which exceeds 1 exactly when `θ < 2`; there `2u*−1 = 1/(θ−1)`, so the bound is `[u*^θ (θ−1)]^n`, which is (3). Positivity of `I` on `(1,2)`: `I(2) = 0` and `I'(θ) = log(2(θ−1)/θ) + θ(1/(θ−1) − 1/θ) − 1/(θ−1) = log(2(θ−1)/θ) < 0` for `θ < 2`, so `I` decreases to 0. The word count: words with `A_n = A` are compositions of `A` into `n` positive parts, `C(A−1, n−1)` of them; summing `A = n..⌊t⌋` gives `C(⌊t⌋, n)` (hockey stick). ∎

**Explicit values** (from [`receipts/L2_receipt.json`](receipts/L2_receipt.json), six decimals, truncated): `I(1.5) = 0.084950`, `I(1.6) = 0.050534`, `I(1.7) = 0.026610`, `I(1.8) = 0.011134`, `I(1.9) = 0.002633`. (An earlier hand-computed version of this line overstated three of these in the third decimal; the side lane's independent probe `fable_L2_check.py` caught it. The checker and receipt were never affected.)

**L2'.** By L1 the odd `N <= X` with a given word `w` lie in one odd class modulo `2^(A_w+1)`, which contains at most `X/2^(A_w+1) + 1` of them. Summing over the `C(⌊t⌋,n)` words with `A_w <= t`: `(X/2) Σ_w 2^(−A_w) + C(⌊t⌋,n) = (X/2) P(A_n <= t) + C(⌊t⌋,n)`, and (2) bounds the probability. ∎

The boundary term is exact bookkeeping, not an `O(1)`: it forces `C(⌊t⌋, n) << X`, i.e. roughly `n <= log_2 X / (θ H(1/θ))` with `H` the binary entropy, before (4) says anything. This is the explicit form of the usual "`n` at most a constant times `log X`" restriction.

## Certificates

- [`check_L2.py`](check_L2.py) (about 6 s; exact rationals for probabilities and counts, floating point only for `I(θ)` with an explicit tolerance) rewrites [`receipts/L2_receipt.json`](receipts/L2_receipt.json) byte-identically and exits 0 iff every check passes. It verifies:
  1. (2) against the exact distribution `P(A_n = A) = C(A−1,n−1)/2^A` for `n <= 60` and `θ ∈ {1.3,…,1.95}` (480 cases, worst exact/bound ratio 0.61), and the hockey-stick word count;
  2. L1 on actual integers for `X = 2^16`, `d ∈ {1,5}`: each word is one odd class mod `2^(A+1)`, counts within `±1` of `X/2^(A+1)`;
  3. the affine formula (1) and the descent bound of [`explicit-one-round-descent`](../explicit-one-round-descent.md), with the falsity of its discarded multiplicative form, for 20,000 random odd `N < 2^64` and `n <= 40`;
  4. (4) and the descent inequality as integer counts for `X = 2^20`, `n ∈ {6,8,10}`, `θ ∈ {1.6,1.7,1.8}`, `d ∈ {1,5}`;
  5. the explicit trade-off table (rate, descent factor per step, admissible `κ`) used by the descent node.
- [`fable_L2_check.py`](fable_L2_check.py) (about 3 s) is the side lane's independent probe (receipt [`fable_L2_check.json`](fable_L2_check.json)); see `reviewed_by`. Its checks are `assert`s: run it without `-O`, as its docstring says.

Both pass at their current paths, leaving their receipts unchanged.

## Remarks

- **Calibration, not novelty.** These are Terras/Everett/Korec-type statements ([`terras-1976-stopping-time`](../../../../sources/terras-1976-stopping-time.md), [`everett-1977-stopping-time`](../../../../sources/everett-1977-stopping-time.md), the Chernoff step of [`lagarias-1985-survey`](../../../../sources/lagarias-1985-survey.md), Theorem B) with every constant explicit. No novelty claim; no convergence claim.
- **d-control.** (2)–(4) hold for every odd `d` with the same constants, since only the valuation law is used; the checker repeats the integer counts for `d = 5`.
- **Place in the explicit-Tao line.** Legacy lemmas L2 and L2' of the lemma table in [`explicit-tao-almost-all-constants`](../../attempts/explicit-tao-almost-all-constants.md); L1 was recalled there from the frozen record (S.1, Terras). The next step, explicit mixing (legacy L4), is where that programme stopped.

## History

- Migrated from `experiments/explicit_tao/lemmas/L2_valuation_tail.md` (legacy IDs `L2`, `L2'`; aliases `TAO-L2`, with `TAO-L1` for the recalled cylinder lemma) at commit `be73a66`, with `experiments/explicit_tao/check_L2.py`, `experiments/explicit_tao/receipts/L2_receipt.json` and the side-lane probe `reviews/side_lane/fable_L2_check.py` with its receipt. The L3 part of the legacy note moved to [`explicit-one-round-descent`](../explicit-one-round-descent.md).
- Written by the Claude explicit-Tao lane (branch `claude/explicit-tao`), iteration 1, 2026-10-18.
- 2026-10-18: the hand-quoted `I(θ)` values were corrected from the receipt after the side-lane probe found them misprinted (feed 19:36: four of the quoted values were off beyond truncation, three of them overstated, which is the unsafe direction for an exceptional-set bound; the comparison is in `fable_L2_check.json`). No computed result changed.
