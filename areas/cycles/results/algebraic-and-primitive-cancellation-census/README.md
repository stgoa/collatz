---
id: algebraic-and-primitive-cancellation-census
kind: result
title: "Cancellation splits into an algebraic part and a small primitive part: census of few-arc words"
status: written
claim: >
  Raw odd-only clock, any 3x+q. For a positive word w with total A, length m, D = 2^A − 3^m > 0 and
  e = gcd(A, m), the factor D = Π_(d | e) Φ_d(2^(A/e), 3^(m/e)) of homogenised cyclotomic polynomials has the
  primitive factor Φ_e; the primitive cancellation is g_prim = gcd(G, Φ_e) with G = gcd(C_w, D), and
  g_prim = G when gcd(A, m) = 1. Over the five exhaustive censuses of few-arc-codings-denominator-census
  (493,483 entries of primitive words with a rotation of s ≤ 4 mismatches, m ≤ 40, letters ≤ 8):
  (i) g_prim = 1 for 88.9% (s = 2), 93.8% (s = 3) and 93.1% (s = 4) of the words, and g_prim < 2^17
  everywhere; the maxima are 18,631 (s = 2, m = 30, A = 135), 19,909 (s = 3, m = 30, A = 96) and 71,791
  (s = 4, m = 22, A = 45), with log₂(g_prim)/A ≤ 0.446 (attained at m = 13); (ii) the tail counts
  #{g_prim ≥ 2^k} lie between 0.08 and 0.54 times N/2^k for every k ≤ 14 in every census; (iii) among the
  291,469 words with gcd(A, m) = 1 the largest cancellation is G = 71,791 (that same m = 22 word) while A
  reaches 141; (iv) of the 907 words with log₂G ≥ A/4, 800 have gcd(A, m) > 1, and their primitive part is
  at most 2^16.2. Every large cancellation observed is algebraic, and the primitive cancellation behaves
  like a random-like divisor; nothing is claimed beyond the enumerated ranges.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-28
depends_on: [few-arc-codings-denominator-census]
certificates: [check_primitive_cancellation.py]
evidence:
  - "primitive_cancellation.json: the receipt; per census it stores the word count, the number of words with g_prim = 1, the tail counts #{g_prim ≥ 2^k} and their ratios to N/2^k, the maximal g_prim and the word attaining it, the maximal log₂(g_prim)/A, the number of gcd(A, m) = 1 words and their maximal G, the words with log₂G ≥ A/4 and how many have gcd(A, m) > 1, and the maximal g_prim per m"
tags: [cycles, denominators, cancellation, cyclotomic-factors, census]
---

# Cancellation splits into an algebraic part and a small primitive part: census of few-arc words

## Statement

Notation of [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §2 and of [`few-arc-codings-denominator-census`](../few-arc-codings-denominator-census/README.md): `w` a positive word, `A`, `m`, `D = 2^A − 3^m > 0`, `C_w` its intercept, `G = gcd(C_w, D)`, `q = D/G`.

**The decomposition.** Let `e = gcd(A, m)`, `x = 2^(A/e)`, `y = 3^(m/e)`. Then `D = x^e − y^e = Π_(d | e) Φ_d(x, y)`, where `Φ_d(x, y) = y^φ(d)·Φ_d(x/y)` is the homogenised `d`-th cyclotomic polynomial. The factor `Φ_e(x, y)` is the **primitive factor** of `D` (for `e = 1` it is `D` itself); the others, `Φ_d` for `d | e`, `d < e`, are the **algebraic factors**: they exist only when `gcd(A, m) > 1`, and they are the `D`'s of the "fractional words" `(A/e·d, m/e·d)`. Define the primitive cancellation

```
g_prim = gcd(G, Φ_e(x, y)),            g_prim = G  when gcd(A, m) = 1.
```

(`Φ_e(x, y)` is computed as `Π_(d | e) (x^d − y^d)^μ(e/d)`.) The part of `G` outside `g_prim` is supported on the algebraic factors, up to the small primes that two cyclotomic values can share.

**The census.** The same five enumerations as [`few-arc-codings-denominator-census`](../few-arc-codings-denominator-census/README.md): every primitive word with a rotation `h`, `gcd(h, m) = 1`, of exactly `s` mismatches (an `s`-arc rotation coding), for `s = 2` (`m ≤ 40`, letters `≤ 4`; `m ≤ 36`, letters `≤ 8`; and `gcd(h, m) ∈ {2, 3}` with constant tracks, `m ≤ 30`), `s = 3` (`m ≤ 30`, letters `≤ 4`) and `s = 4` (`m ≤ 22`, letters `≤ 3`), one representative per rotation class.

| census | words `N` | `g_prim = 1` | max `g_prim` | at | max `log₂g_prim / A` | `gcd(A,m) = 1` words | their max `G` |
|---|---|---|---|---|---|---|---|
| `s2_v4` | 29,340 | 26,953 (91.9%) | 6,553 = `2^12.68` | `m = 35`, `A = 57` | 0.386 (`m = 5`) | 17,793 | 6,553 |
| `s2_v8` | 113,165 | 100,615 (88.9%) | 18,631 = `2^14.19` | `m = 30`, `A = 135`, `e = 15` | 0.386 (`m = 5`) | 64,428 | 6,553 |
| `s2_gcd` | 13,207 | 11,434 (86.6%) | 931 = `2^9.86` | `m = 30`, `A = 48`, `e = 6` | 0.327 (`m = 14`) | 5,265 | 517 |
| `s3_v4` | 205,640 | 192,812 (93.8%) | 19,909 = `2^14.28` | `m = 30`, `A = 96`, `e = 6` | 0.425 (`m = 7`) | 143,902 | 13,127 |
| `s4_v3` | 132,131 | 123,066 (93.1%) | 71,791 = `2^16.13` | `m = 22`, `A = 45`, `e = 1` | 0.446 (`m = 13`) | 83,139 | 71,791 |

**Tails.** `#{g_prim ≥ 2^k}` against `N/2^k`:

| census | `k = 4` | `6` | `8` | `10` | `12` | `14` | `16` |
|---|---|---|---|---|---|---|---|
| `s2_v8` (`N/2^k`: 7,073 / 1,768 / 442 / 111 / 28 / 7 / 2) | 2,932 | 666 | 148 | 41 | 8 | 1 | 0 |
| `s3_v4` (`N/2^k`: 12,852 / 3,213 / 803 / 201 / 50 / 13 / 3) | 2,804 | 572 | 171 | 36 | 7 | 1 | 0 |
| `s4_v3` (`N/2^k`: 8,258 / 2,065 / 516 / 129 / 32 / 8 / 2) | 1,914 | 429 | 137 | 20 | 5 | 3 | 1 |

The ratio to `N/2^k` stays between 0.08 and 0.54 for every `k ≤ 14` in every census (the one entry at `k = 16` is a single word).

**Large cancellations are algebraic.** Of the words with `log₂G ≥ A/4` (77 + 347 + 146 + 52 + 285 = 907 across the censuses), 800 have `gcd(A, m) > 1`, and the primitive part of every one of them is at most `2^16.13`. Examples: the half-swap `(1,3)` words of the census node have `G = (2^m − 3^(m/2))/7 = Π_(d | m/2) Φ_d(4, 3)/7`, entirely algebraic (`e = m`); the two-marker words `(1, 2^(n−1), 3, 2^(n−1))` have `G = 4^n − 3^n = Π_(d | n) Φ_d(4, 3)`, entirely algebraic (`e = 2n`); the `3x+11` cycle `(1,1,2,2,1,1,3,3)` has `D = Φ_1·Φ_2 = 47·209`, `G = 47·19` and `g_prim = 19`. The largest primitive cancellation of all, `71,791` at `m = 22`, `A = 45`, `gcd(A, m) = 1`, is the whole `G` of the word `(1,1,3^9,1^6,2^5)`: a plain divisor of `D = 2^45 − 3^22`.

## Proof

The claim is a finite computation. Completeness of the enumeration is proved in [`few-arc-codings-denominator-census`](../few-arc-codings-denominator-census/README.md) (an `s`-mismatch rotation with coprime shift is an `s`-arc rotation coding; the `gcd(h, m) > 1` two-arc case follows [`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md), part 1). The factorisation `x^e − y^e = Π_(d|e) Φ_d(x, y)` and the Möbius formula `Φ_e(x, y) = Π_(d|e) (x^d − y^d)^μ(e/d)` are standard; the certificate computes `Φ_e(2^(A/e), 3^(m/e))` exactly as that quotient and checks that it is an integer. All statistics are exact integer computations; `log₂` values are rounded to two decimals in the receipt.

## Certificates

[`check_primitive_cancellation.py`](check_primitive_cancellation.py) (standard library, about 50 s) recomputes the five censuses with the decomposition, fails if any word has `g_prim ≥ 2^17` (P1), if any word with `gcd(A, m) = 1` has `G ≥ 2^17` (P2), or if the summary differs from [`primitive_cancellation.json`](primitive_cancellation.json) (P3); `--write-receipt` regenerates the receipt. Finite statements only.

## Remarks

- **Reading.** The cancellation of a few-arc word is, in this range, the product of an algebraic part that exists only when `gcd(A, m) > 1` and is explained by the cyclotomic factors of `D` together with a symmetry of the word, and a primitive part that is 1 for nine words in ten and otherwise distributed like a random divisor: the tail `#{g_prim ≥ x}` tracks `c·N/x` with `c` between 0.1 and 0.5, and the observed maxima (`2^12.7`–`2^16.1`) are what such a tail over `10^5` words produces. No structured large primitive cancellation appears. The per-`m` maxima of `g_prim` grow with `m`, but so do the number of words and the number of divisors of `Φ_e`; the data cannot separate these, and no growth rate is claimed.
- **Why this is the right split for `q = 1`.** A `q = 1` cycle has `G = D`, so its primitive cancellation is `Φ_e(x, y) ≈ y^φ(e)·Φ_e(x/y)` with `x/y = (2^A/3^m)^(1/e)` barely above 1: for `gcd(A, m) = 1` it is all of `D`; for `e = 2, 3, 4` it is about `2^(A/2)`, `2^(2A/3)`, `2^(A/2)`; it falls below `2^(A/2)` only when `φ(e)/e < 1/2` (`e` divisible by 6, 10, 14, …). The sharp conjecture suggested by the data, `g_prim < 2^(A/2)`, is recorded in [`half-cancellation-for-few-mismatch-words`](../../questions/half-cancellation-for-few-mismatch-words.md) with its payoff: for a `q = 1` cycle with `gcd(A, m) = 1` it says `D < 2^(A/2)`, which already an irrationality measure for `log₂3` forbids beyond a small period, with no use of EXT-1.
- **Relation to the half-cancellation finding.** [`few-arc-codings-denominator-census`](../few-arc-codings-denominator-census/README.md) found `G² < 2^A` for `m ≥ 9`. This node explains the shape of that bound: the algebraic part can reach `2^(A/2)` (the two-marker family), the primitive part never came close.
- **Controls and scope.** Actual small-`d` cycles with large `m` have `G ≈ D/d`, hence large primitive cancellation; they have `ρ ≥ m/5` and are outside the few-arc censuses, so nothing here contradicts them. Finite ranges only. Novelty undetermined; the decomposition is elementary.

## History

- Written 2026-10-28 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, while following the "separate the algebraic part" attack of the half-cancellation question.
- 2026-10-28, later: the `e = 2` case is tested adversarially in [`near-doubled-words-primitive-factor-test`](../near-doubled-words-primitive-factor-test/README.md).
- 2026-10-31: the plain half bound `G² < 2^A` was refuted at `ρ = 4` by a word whose cancellation is the full algebraic factor times a primitive part 5 ([`half-cancellation-counterexample-rotation-pair`](../half-cancellation-counterexample-rotation-pair/README.md)), as the split recorded here suggests; the conjecture on `g_prim` continues as [`primitive-cancellation-below-half`](../../questions/primitive-cancellation-below-half.md) (Claude cycles lane, Fable 5.1).
