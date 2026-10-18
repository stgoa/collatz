# L2 — Explicit large deviations for Syracuse valuations, and L3 — one-round descent

**Status: written proof with a finite certificate (`../check_L2.py`,
receipt `../receipts/L2_receipt.json`). Calibrates Terras (1976), Everett
(1977) and the Chernoff step of Lagarias (1985), Theorem B. No novelty
claim; no convergence claim.** Clock: odd-only Syracuse arrows. Domain:
positive odd integers. Everything below is for the map `S_d(N) =
(3N+d)/2^(v_2(3N+d))` with `d = 1` unless stated; the proofs use only that
`3` is invertible modulo powers of 2 and that `3N+d` is even for odd `N`,
so each statement holds verbatim for every odd `d` (checked for `d = 5`).

## Setting and L1 (recalled)

For odd `N` put `a_1(N) = v_2(3N+1)`, `N_1 = S(N)`, and inductively
`a_j = v_2(3N_(j−1)+1)`, `N_j = S(N_(j−1))`. Write `A_j = a_1+…+a_j`,
`A = A_n`. The affine formula is

```
S^n(N) = (3^n N + C_w) / 2^A,   C_w = Σ_(j=0)^(n−1) 3^(n−1−j) 2^(A_j),   A_0 = 0.   (1)
```

**L1 (exact cylinders).** The word `w = (a_1,…,a_n)` is determined by
`N mod 2^(A+1)`, and the odd `N` with word `w` form exactly one odd residue
class modulo `2^(A+1)`. (Induction on `n`: `a_1 = k` means `3N+1 ≡ 2^k
(mod 2^(k+1))`, one odd class mod `2^(k+1)`; then `S(N) mod 2^(A'+1)` is
determined by `N mod 2^(a_1+A'+1)` because `3` is invertible.) This is the
repository's frozen cylinder fact and Terras's Theorem 1.2.

Consequently, for an odd `N` drawn uniformly from any complete set of odd
residues modulo `2^(A+1)`, `P(word = w) = 2^(−A)`, so the `a_j` are
independent with `P(a_j = k) = 2^(−k)`, `k >= 1` (geometric, mean 2).

## L2 — the tail bound

**Lemma L2.** Let `a_1, a_2, …` be independent with `P(a = k) = 2^(−k)`
for integers `k >= 1`, and `A_n = a_1+…+a_n`. For every real `t` with
`n < t < 2n`,

```
P(A_n <= t) <= min_(u>1) u^t / (2u−1)^n = exp(−n I(t/n)),            (2)
I(θ) = θ log(2(θ−1)/θ) − log(θ−1),      1 < θ < 2,                   (3)
```

with the minimum attained at `u* = θ/(2(θ−1))`. `I` is positive on
`(1,2)`, `I(θ) → 0` as `θ → 2`, and the bound is monotone in `t`.
Moreover the number of words of length `n` with `A_n <= t` is exactly
`C(⌊t⌋, n)`.

**Proof.** For `u > 1`, `P(A_n <= t) = P(u^(−A_n) >= u^(−t)) <= u^t
E[u^(−A_n)] = u^t (E u^(−a))^n` by Markov's inequality, and
`E u^(−a) = Σ_(k>=1) (2u)^(−k) = 1/(2u−1)`. Minimising `u^θ/(2u−1)` over
`u > 1` for `t = θn`: the derivative of `θ log u − log(2u−1)` vanishes at
`θ(2u−1) = 2u`, i.e. `u* = θ/(2(θ−1))`, which exceeds 1 exactly when
`θ < 2`; there `2u*−1 = 1/(θ−1)`, so the bound is `[u*^θ (θ−1)]^n`, which
is (3). Positivity of `I` on `(1,2)`: `I(2) = 0` and `I'(θ) = log(2(θ−1)/θ)
+ θ(1/(θ−1) − 1/θ) − 1/(θ−1) = log(2(θ−1)/θ) < 0` for `θ < 2`, so `I`
decreases to 0. The word count: words with `A_n = A` are compositions of
`A` into `n` positive parts, `C(A−1, n−1)` of them; summing `A = n..⌊t⌋`
gives `C(⌊t⌋, n)` (hockey stick). ∎

**Explicit values** (receipt): `I(1.5) = 0.08530…`, `I(1.6) = 0.05054…`,
`I(1.7) = 0.02663…`, `I(1.8) = 0.01112…`, `I(1.9) = 0.00263…`.

## Integer counts

**Lemma L2'.** For every integer `X >= 1`, every `n >= 1` and every real
`t` with `n < t < 2n`,

```
#{odd N <= X : A_n(N) <= t} <= (X/2) exp(−n I(t/n)) + C(⌊t⌋, n).        (4)
```

**Proof.** By L1 the odd `N <= X` with a given word `w` lie in one odd
class modulo `2^(A_w+1)`, which contains at most `X/2^(A_w+1) + 1` of
them. Summing over the `C(⌊t⌋,n)` words with `A_w <= t`:
`(X/2) Σ_w 2^(−A_w) + C(⌊t⌋,n) = (X/2) P(A_n <= t) + C(⌊t⌋,n)`, and (2)
bounds the probability. ∎

The boundary term is exact bookkeeping, not an `O(1)`: it forces
`C(⌊t⌋, n) << X`, i.e. roughly `n <= log_2 X / (θ H(1/θ))` with `H` the
binary entropy, before (4) says anything. This is the explicit form of the
usual "`n` at most a constant times `log X`" restriction.

## L3 — one-round descent

**Lemma L3.** For odd `N`, `n >= 1` and the word `w` of `N`,

```
S^n(N) = 3^n N / 2^A + C_w / 2^A,     0 < C_w / 2^A <= (3/2)^n − 1.      (5)
```

Hence, for `1 < θ < 2`, every odd `N <= X` outside the exceptional set
counted in (4) with `t = θn` satisfies

```
S^n(N) < N (3/2^θ)^n + (3/2)^n,                                       (6)
```

a decrease by the factor `(3/2^θ)^n` up to an additive term that is of
lower order whenever `(3/2)^n << N (3/2^θ)^n`, i.e. `2^((θ−1)n) << N`;
with `n = κ log_2 N` this holds as soon as `(θ−1)κ < 1 + κ log_2(3/2^θ)`,
which is the case throughout the trade-off table below. The factor is a
genuine contraction once `2^θ > 3`, i.e. `θ > log_2 3 = 1.58496…`.

**Proof.** In (1), every later valuation is at least 1, so
`A − A_j >= n − j` for `j <= n−1`, hence `2^(A_j − A) <= 2^(−(n−j))` and
`C_w/2^A <= Σ_(j=0)^(n−1) 3^(n−1−j) 2^(−(n−j)) = (1/2) Σ_(i=0)^(n−1) (3/2)^i
= (3/2)^n − 1`. For (6), `A > θn` gives `3^n/2^A < (3/2^θ)^n`. ∎

*Correction record.* The first draft of this note claimed the multiplicative
form `S^n(N) <= 3^n (N+1)/2^A`, i.e. `C_w <= 3^n`. That is false: the word
`(10, 1)` has `C_w = 3 + 2^10 = 1027 > 9`. The checker's exact test
rejected it before anything was committed; the additive form (5) is the
correct Terras-type statement.

## What this does and does not give

- With `θ` between `log_2 3` and 2 there is a trade-off between the
  descent factor `3/2^θ` per step and the rate `I(θ)`; the receipt
  tabulates it. One round from scale `X` with `n = ⌊κ log_2 X⌋` leaves an
  exceptional fraction `<= X^(−κ I(θ)/ln 2) + 2C(⌊θn⌋,n)/X` and lands
  below `X (3/2^θ)^n + (3/2)^n`. These are Terras/Everett/Korec-type
  statements with every constant explicit.
- It does **not** iterate: the landing points of one round are not
  uniformly distributed in residue classes, and the repository's own
  barriers (P6-002/P6-003) show that arbitrary-target iteration fails.
  Tao's mixing of the Syracuse random variables (L4) is what licenses
  iteration; its constants are the open problem of this programme.
- d-control: (2)–(4) hold for every odd `d` with the same constants, since
  only the valuation law is used. For `S_d` the affine formula (1) reads
  `S_d^n(N) = (3^n N + d C_w)/2^A`, so (5)–(6) hold with the additive term
  multiplied by `d`: `S_d^n(N) < N (3/2^θ)^n + d (3/2)^n`. The checker
  repeats the integer counts and the descent test for `d = 5` with that
  factor. The d-specific input of the programme is L7 alone.

## Checker

`python3 check_L2.py` (exact rationals for probabilities and counts,
floating point only for `I(θ)` with an explicit tolerance) verifies, and
writes `receipts/L2_receipt.json`:

1. (2) against the exact distribution `P(A_n = A) = C(A−1,n−1)/2^A` for
   `n <= 60` and `θ ∈ {1.3,…,1.95}`;
2. L1 on actual integers for `X = 2^16`, `d ∈ {1,5}`: each word is one odd
   class mod `2^(A+1)`, counts within `±1` of `X/2^(A+1)`;
3. (5) exactly (the affine formula, `C_w/2^A <= (3/2)^n − 1`, and the
   falsity of the discarded multiplicative form) for 20,000 random odd
   `N < 2^64` and `n <= 40`;
4. (4) and (6) as integer counts for `X = 2^20`, `n ∈ {6,8,10}`,
   `θ ∈ {1.6,1.7,1.8}`, `d ∈ {1,5}`;
5. the explicit trade-off table.
