---
id: three-arc-intercept-elimination
kind: attempt
title: "Three arcs: the rotation difference is a two-term relation between arc intercepts, and eliminating across the three relations is vacuous"
status: written
claim: >
  Tried, toward a cancellation bound for words with a three-mismatch rotation (the s = 3 case of the
  half-cancellation question): express the rotation difference C_(w′) − C_w through the arcs between
  consecutive mismatches and eliminate. Result: with mismatches e_1 < e_2 < e_3, signed differences
  d_r = a_(e_r+h) − a_(e_r) (Σ d_r = 0) and arcs α = (e_1, e_2], β = (e_2, e_3], γ = (e_3, e_1 + m],
  C_(w′) − C_w = 3^(m−1−e_3)·2^(s_(e_1+1))·Ξ_1 with
  Ξ_1 = (2^(d_1) − 1)·3^(ℓ_β)·C_α + (2^(−d_3) − 1)·2^(S_α)·C_β, so G = gcd(C_w, D) divides Ξ_1 (and its two
  cyclic analogues); Ξ_1 ≠ 0 unless d_1, d_3 > 0 and S_α = d_3, and it never vanished on 20,832 words.
  But the cyclic 3×3 system of the three relations has determinant −(2^(d_1) − 1)(2^(d_2) − 1)(2^(d_3) − 1)·D,
  so eliminating the arc intercepts gives only G | D·(…), the s = 3 instance of the Smith-form obstruction
  of coupled-defect-matrix-smith-form; and the size bound from a single relation, G ≤ |Ξ_1|, is the run
  witness of mismatch-height-tradeoff in disguise. No new cancellation bound was obtained.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-28
depends_on: [coupled-defect-matrix-smith-form]
certificates: [check_three_arc_relations.py]
tags: [cycles, cancellation, three-mismatch, obstruction]
---

# Three arcs: the rotation difference is a two-term relation between arc intercepts, and eliminating across the three relations is vacuous

## Idea

For two mismatches, [`two-defect-cancellation-bound`](../../results/two-defect-cancellation-bound.md) gets `G | (2^k − 1)·C_u` because the rotation difference `C_(w′) − C_w` is a *single* arc term. The hope was that for three mismatches the difference is a short combination of arc terms, that cutting at each of the three mismatches gives three such relations, and that eliminating the arc intercepts, or bounding one relation, gives a cancellation bound of the kind the half-cancellation question ([`half-cancellation-for-few-mismatch-words`](../../questions/half-cancellation-for-few-mismatch-words.md)) asks for at `s = 3`.

## What happened

Notation: `w` positive of length `m`, prefix sums `s_j = a_0 + … + a_(j−1)`, rotation `w′_j = a_(j+h)`, mismatches `e_1 < e_2 < e_3` with `d_r = a_(e_r+h) − a_(e_r)`, `Σ d_r = 0`. Cut the cycle after each mismatch: arcs `α = (a_(e_1+1), …, a_(e_2))`, `β = (a_(e_2+1), …, a_(e_3))`, `γ = (a_(e_3+1), …, a_(e_1+m))`, with lengths `ℓ_α + ℓ_β + ℓ_γ = m`, totals `S_α + S_β + S_γ = A`, and intercepts `C_α`, `C_β`, `C_γ`.

**The two-term relation.** `s′_j − s_j = Σ_(e_r < j) d_r` is `0` for `j ≤ e_1`, `d_1` on `(e_1, e_2]`, `d_1 + d_2 = −d_3` on `(e_2, e_3]`, and `0` after `e_3`. Hence

```
C_(w′) − C_w = (2^(d_1) − 1)·Σ_(e_1<j≤e_2) 3^(m−1−j)2^(s_j) + (2^(−d_3) − 1)·Σ_(e_2<j≤e_3) 3^(m−1−j)2^(s_j)
             = 3^(m−1−e_3)·2^(s_(e_1+1))·Ξ_1,
Ξ_1 = (2^(d_1) − 1)·3^(ℓ_β)·C_α + (2^(−d_3) − 1)·2^(S_α)·C_β,                                     (R1)
```

because `Σ_(e_1<j≤e_2) 3^(m−1−j)2^(s_j) = 3^(m−1−e_2)·2^(s_(e_1+1))·C_α` (the arc's own intercept, shifted) and likewise for `β`, with `3^(m−1−e_2)/3^(m−1−e_3) = 3^(ℓ_β)` and `s_(e_2+1) − s_(e_1+1) = S_α`. Since every rotated intercept is divisible by `G` and `G` is coprime to 6, **`G` divides the numerator of `Ξ_1`** (`Ξ_1` is a rational with a power-of-two denominator when a `d` is negative). Starting the cycle at `e_2` or `e_3` gives the two cyclic analogues:

```
G | (2^(d_2) − 1)·3^(ℓ_γ)·C_β + (2^(−d_1) − 1)·2^(S_β)·C_γ,        (R2)
G | (2^(d_3) − 1)·3^(ℓ_α)·C_γ + (2^(−d_2) − 1)·2^(S_γ)·C_α.        (R3)
```

For `s = 2`, `d_1 + d_2 = 0` kills the second term of (R1), which is why the two-defect case yields `G | (2^k − 1)·C_u` outright.

**When `Ξ_1` vanishes.** The coefficients `2^(d_1) − 1` and `2^(−d_3) − 1` have the signs of `d_1` and `−d_3`. If they agree, `Ξ_1 ≠ 0`. If `d_1 > 0 > −d_3`, then `Ξ_1 = (2^(d_1) − 1)3^(ℓ_β)C_α − (2^(d_3) − 1)2^(S_α − d_3)C_β`, and the two terms have 2-adic valuations `0` and `S_α − d_3` (arc intercepts are odd: their leading term is a power of 3 and the rest is even), so `Ξ_1 = 0` forces `S_α = d_3`, i.e. the whole arc `α` has letter sum equal to the jump at `e_3`. The case `d_1 < 0 < −d_3` gives valuations `0` and `S_α + |d_1| > 0`, so `Ξ_1 ≠ 0`. In the certificate's 20,832 words `Ξ_1` never vanished.

**Elimination is vacuous.** The three relations say `M·(C_α, C_β, C_γ)ᵀ ≡ 0 (mod G)` with

```
M = [ (2^(d_1)−1)3^(ℓ_β)    (2^(−d_3)−1)2^(S_α)    0                   ]
    [ 0                     (2^(d_2)−1)3^(ℓ_γ)     (2^(−d_1)−1)2^(S_β) ]
    [ (2^(−d_2)−1)2^(S_γ)   0                      (2^(d_3)−1)3^(ℓ_α)  ].
```

Its determinant is `Π_r(2^(d_r) − 1)·3^m + Π_r(2^(−d_r) − 1)·2^A`, and since `Σ d_r = 0`, `Π_r(2^(−d_r) − 1) = −Π_r(2^(d_r) − 1)`; so

```
det M = −(2^(d_1) − 1)(2^(d_2) − 1)(2^(d_3) − 1)·(2^A − 3^m) = −Π_r(2^(d_r) − 1)·D.
```

Multiplying by the adjugate gives `G | det M·C_α`, automatic because `G | D`. This is the `s = 3` instance of [`coupled-defect-matrix-smith-form`](../../results/coupled-defect-matrix-smith-form/README.md) (`|det M| = D^(s−2)·Π|β′_i − β_i|`), reached here through the arcs rather than the block matrix. Nothing is new in the obstruction; the arc form just makes the three surviving relations explicit.

**A single relation gives only the run witness.** From (R1), `G ≤ |Ξ_1| ≤ 2^(max(d_1, −d_3, 0))·(3^(ℓ_β)C_α + 2^(S_α)C_β) = 2^(max(d_1,−d_3,0))·C_(αβ)`, the intercept of the concatenated arc `αβ = (e_1, e_3]`. For the rational cycle `x_j = C_(w^(j))/D` the stretch identity gives `C_(αβ) = 2^(S_α+S_β)·x_(e_3+1) − 3^(ℓ_α+ℓ_β)·x_(e_1+1) < 2^(A−S_γ)·x_max`. At `q = 1` (`G = D`, integer states, maximum `H`) this reads `D < 2^|d|·2^(A−S_γ)·H`, i.e. `S_γ < B + ℓ′ + |d| + log₂(2^A/D)`: every arc between consecutive mismatches has letter sum at most the log-height plus `O(log m)` terms. That is the start/end witness of [`mismatch-height-tradeoff`](../../results/mismatch-height-tradeoff/README.md) (`F < ℓ′ + B` for every agreeing run), weakened by `|d|` and by the gap term. The arc relations contain no size information beyond the run witness.

## Why it fails

The information in `C_(w′) − C_w` for three mismatches is two arc terms with S-unit coefficients, and the three cyclic cuts are linearly dependent modulo `D`: their determinant is a unit times `D`. So neither elimination nor a single relation can see past `D`, which is exactly what one wants to bound. The two-mismatch success rests on the vanishing of the second coefficient, which is special to `s = 2`.

## What survives

- The explicit relations (R1)–(R3): any arithmetic attack on three-mismatch words has them as its starting congruences, and at `q = 1` they are congruences modulo `D` between the three arc intercepts, `(2^(d_1) − 1)3^(ℓ_β)C_α ≡ −(2^(−d_3) − 1)2^(S_α)C_β (mod D)`.
- The vanishing criterion for `Ξ_1`, and the observation that the three-arc words of the census, [`few-arc-codings-denominator-census`](../../results/few-arc-codings-denominator-census/README.md), have cancellation far below what (R1) allows, so a bound must use more than one relation together with the arcs' internal structure (they are stretches of a three-interval rotation coding, [`two-arc-word-rotation-structure`](../../results/two-arc-word-rotation-structure/README.md) gives the analogous structure for two arcs).
- The census finding that the cancellation of these words is almost entirely algebraic ([`algebraic-and-primitive-cancellation-census`](../../results/algebraic-and-primitive-cancellation-census/README.md)) points at the cyclotomic factors of `D`, not at the arc relations, as the place where a proof would have to work.

## Certificates

[`check_three_arc_relations.py`](check_three_arc_relations.py) (standard library, exact rationals, about 2 s) verifies, on every primitive three-arc word with `m ≤ 16`, letters 1–3 and `D > 0` (20,832 words), the relation (R1) as an exact identity, `G | Ξ_1` with `Ξ_1 ≠ 0`, and the determinant identity.

## History

- Written 2026-10-28 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, as the second step of the descent attack on the half-cancellation question; it rediscovered the C012 obstruction from the arc side and records what the arc form adds.
