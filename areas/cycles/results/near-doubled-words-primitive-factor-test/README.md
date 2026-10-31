---
id: near-doubled-words-primitive-factor-test
kind: result
title: "The primitive factor at gcd(A, m) = 2 never divides the intercept of a near-doubled word: an adversarial test"
status: written
claim: >
  Raw odd-only clock, any 3x+q. For A, m even write x = 2^(A/2), y = 3^(m/2), D = Φ_1·Φ_2 with
  Φ_1 = x − y, Φ_2 = x + y. (i) Reduction: for w = (u, v) with |u| = |v| = m/2 and Δ = S_u − S_v,
  Φ_1 | C_w iff C_u ≡ −2^(Δ/2)·C_v (mod Φ_1) and Φ_2 | C_w iff C_u ≡ 2^(Δ/2)·C_v (mod Φ_2); since Φ_2 is odd
  and below 2^(A/2+1), the primitive-cancellation conjecture g_prim < 2^(A/2) at e = 2 is equivalent to
  Φ_2 ∤ C_w. (ii) For the near-doubled words, v = u with two letters swapped (rotation by m/2 has four
  mismatches) and v = u with one letter raised by 2 or 4 (two mismatches), the condition becomes
  Φ_2 | (2^(b−a) − 1)·F(z) for the sub-word z strictly between the swapped letters, respectively
  2^j·C_u ≡ C_v (mod Φ_2). Exhaustive search finds no primitive word with Φ_2 | C_w: transpositions for
  n = m/2 ≤ 11, ⌈n·log₂3⌉ ≤ B ≤ 2.3n, letter gaps ≤ 5 (2,547,805 sub-words; a uniform-residue heuristic
  expects 3.0 hits), and one-letter changes for n ≤ 9 (3,897,348 conditions; the heuristic expects 14.2,
  or 3.9 after the size and parity constraints), both certified; exploration extends the transposition
  search to n ≤ 14 (236 million further sub-words, 1.2 further expected hits) and the one-letter search to
  n ≤ 11 (539 million further conditions, 6.7 expected), with no hit. (iii) Among the
  65,548 words with gcd(A, m) = 2 of the five few-arc censuses the primitive part never exceeds Φ_2/6.7
  (log₂g_prim − A/2 ≤ −2.75). Finite ranges only; the deficits against the heuristic are at the level
  p ≈ 0.02 and prove no obstruction.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-28
depends_on: [algebraic-and-primitive-cancellation-census]
certificates: [check_near_doubled.py]
evidence:
  - "near_doubled.json: the receipt; the reduction-identity sample size, the sub-word counts and uniform expectations per (n, B) for the transposition search, the condition counts per (n, B, j) for the one-letter search, and the e = 2 census statistics"
tags: [cycles, cancellation, cyclotomic-factors, adversarial-test, census]
---

# The primitive factor at `gcd(A, m) = 2` never divides the intercept of a near-doubled word: an adversarial test

## Statement

Notation of [`algebraic-and-primitive-cancellation-census`](../algebraic-and-primitive-cancellation-census/README.md): `D = Π_(d|e) Φ_d(2^(A/e), 3^(m/e))`, `e = gcd(A, m)`, primitive cancellation `g_prim = gcd(G, Φ_e)`. This node tests the conjecture `g_prim < 2^(A/2)` of [`half-cancellation-for-few-mismatch-words`](../../questions/half-cancellation-for-few-mismatch-words.md) where a `q = 1` cycle would make it tight: `e = 2`, where `Φ_2 = 2^(A/2) + 3^(m/2)` is itself only `≈ 2^(A/2)`.

**1. The reduction at `e = 2`.** Let `A` and `m` be even, `x = 2^(A/2)`, `y = 3^(m/2)`, so `D = (x − y)(x + y) = Φ_1·Φ_2`. For any word `w = (u, v)` with `|u| = |v| = m/2`, `C_w = 3^(m/2)·C_u + 2^(S_u)·C_v`; with `Δ = S_u − S_v` (even) and `2^(S_u) = x·2^(Δ/2)`,

```
C_w ≡ 3^(m/2)·(C_u + 2^(Δ/2)·C_v)   (mod Φ_1),          C_w ≡ 3^(m/2)·(C_u − 2^(Δ/2)·C_v)   (mod Φ_2).
```

So `Φ_1 | C_w ⟺ C_u ≡ −2^(Δ/2)C_v (mod Φ_1)` and `Φ_2 | C_w ⟺ C_u ≡ 2^(Δ/2)C_v (mod Φ_2)`. The two algebraic factors differ by one sign. **Consequence.** `Φ_2` is odd and `2^(A/2) < Φ_2 < 2^(A/2+1)`, so every proper divisor of `Φ_2` is at most `Φ_2/3 < 2^(A/2)`; hence at `e = 2`,

```
g_prim < 2^(A/2)     ⟺     Φ_2 ∤ C_w.
```

For a `q = 1` cycle with `e = 2`, `Φ_2 | D | C_w`, which is exactly what the conjecture forbids.

**2. The adversaries.** The known large cancellations ([`two-marker-constant-background-exact-denominator`](../two-marker-constant-background-exact-denominator/README.md), the half-swap words of [`few-arc-codings-denominator-census`](../few-arc-codings-denominator-census/README.md)) realise the minus sign: `C_u ≡ −C_v (mod Φ_1)` through a symmetry exchanging the halves. The natural attempt at the plus sign with few mismatches is a **near-doubled** word, `v` a small modification of `u`:

- **(T) a transposition.** `v = u` with `a = u_i` and `b = u_k` swapped (`i < k`, `a ≠ b`). Then `S_u = S_v`, the rotation by `m/2` has exactly four mismatches, and `C_v − C_u = (2^(b−a) − 1)·3^(n−1−k)·2^(s_(i+1))·F(z)` with `z = u[i+1..k−1]` and `F(z) = Σ_(t≤|z|) 3^(|z|−t)·2^(σ_t)` (`σ_t` the prefix sums of `z`). So `Φ_2 | C_w ⟺ Φ_2 | (2^(b−a) − 1)·F(z)`: a condition on the sub-word strictly between the swapped letters, independent of the rest of `u`.
- **(O) one letter raised by `2j`.** `v_i = u_i + 2j`, so `Δ = −2j`, `Φ_2 = 2^(B+j) + 3^n` with `B = S_u`, the rotation by `m/2` has exactly two mismatches, and `Φ_2 | C_w ⟺ 2^j·C_u ≡ C_v (mod Φ_2)`, with `C_v = C_u + (2^(2j) − 1)·Σ_(l>i) 3^(n−1−l)2^(s_l)`. Splitting `C_u` at position `i` into its prefix and suffix parts turns this into `2^(S_tail)·C_pre + 3^(|pre|)·C_tail ≡ 0`, which is the intercept of the concatenation `(tail, pre)`: **`Φ_2 | C_w ⟺ (2^(B+j) + 3^n) | C_(u′)` for the rotation `u′ = (u_(i+1), …, u_(n−1), u_0, …, u_i)` of the half-word.** So the one-letter family asks whether some word of length `n` and total `B` has an intercept divisible by `2^(B+j) + 3^n`, `j ≥ 1`.

(If `u = v`, `w = u²` is not primitive and `Φ_2 | C_w` trivially: `C_(u²) = C_u·Φ_2`. Primitivity is what makes the question nontrivial.)

**3. The search.** Writing `n = m/2`:

| family | range | conditions | uniform-heuristic expectation | with size and parity | hits |
|---|---|---|---|---|---|
| (T), certified | `5 ≤ n ≤ 11`, `⌈n·log₂3⌉ ≤ B ≤ 2.3n`, gaps `k ≤ 5` | 2,547,805 sub-words | 3.01 | 2.55 | **0** |
| (T), exploration | `n = 12, 13, 14`, same `B` range | 65 + 236 million sub-words | 0.64 + 1.17 | ≈ 1.5 | **0** |
| (O), certified | `5 ≤ n ≤ 9`, `⌈n·log₂3⌉ − 2 ≤ B ≤ 2.3n`, `j ∈ {1, 2}` | 3,897,348 | 14.18 | 3.88 | **0** |
| (O), exploration | `n = 10, 11`, `B` up to `2.5n` | 539 million | 6.73 | ≈ 1.8 | **0** |

"Uniform-heuristic expectation" is `Σ (number of distinct conditions)/Φ_2`, treating each residue as uniform. "With size and parity" removes the conditions that cannot hold at all: for (T), `(2^k − 1)·F(z) ≥ Φ_2` is needed since `F(z) ≠ 0`; for (O), `H_i − 2^j·T_i` (prefix part minus `2^j` times the suffix part of `C_u`) is odd while `Φ_2` is odd, so the multiple is nonzero and `|H_i − 2^j T_i| ≥ Φ_2` is needed. The deficits (0 against about 4 for (T) up to `n = 14`, 0 against about 6 for (O) up to `n = 11`) correspond to `p ≈ 0.02` and `p ≈ 0.003` under a Poisson reading of the corrected expectations, about `p ≈ 10^(−4)` together. They are suggestive, and they prove nothing: the corrected expectations themselves carry factor-of-two uncertainties (the residues are not uniform, see the Remarks).

**4. The census at `e = 2`.** Among the 65,548 census words with `gcd(A, m) = 2` (one representative per rotation class and census), 6,929 have `g_prim > 1`, and `log₂g_prim − A/2 ≤ −2.752`: the largest primitive share of `Φ_2` is `19` of `Φ_2 = 209` at `m = 8` (`w = (4,4,1^6)`, and the `3x+11` cycle). No census word has `Φ_2 | C_w`.

## Proof

Part 1 is the two-line computation displayed, with `2^(S_u) = 2^(A/2)·2^((S_u − S_v)/2)` and `x ≡ ±y`; the consequence uses that the smallest prime factor of the odd number `Φ_2` is at least 3 (it is coprime to 6). Part 2 is the prefix-sum bookkeeping of [`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md) (a transposition changes the prefix sums on `(i, k]` by `b − a`; a raised letter changes them after `i` by `2j`). Part 3 is the computation: the sub-word search uses `F(zc) = 3·F(z) + 2^(σ_|z|+c)` along a depth-first enumeration of all `z` with `|z| ≤ n − 2` and `Σz ≤ B − n + |z| − 1` (what remains of `u` must be fillable by letters `≥ 1`), tests `F(z) ≡ 0` modulo `Φ_2/gcd(Φ_2, 2^k − 1)` for `k ≤ 5`, and on a residue hit rebuilds a witness `u` and verifies `Φ_2 | C_w` on the primitive `w`; the one-letter search enumerates all `u` directly. Part 4 reuses the enumeration of the censuses with the primitive factor `Φ_2`.

## Certificates

[`check_near_doubled.py`](check_near_doubled.py) (standard library, about 60 s): N1 checks the reduction identities of part 1 on 1,981 pseudo-random pairs `(u, v)` with a fixed seed; N2 and N3 run the certified ranges of the table and fail on any hit; N4 recomputes the `e = 2` census statistics; all counts are compared with [`near_doubled.json`](near_doubled.json). The exploration rows (`n = 12, 13, 14` for (T); `n = 10, 11` for (O)) were run outside the repository with the same code and are not certified.

## Remarks

- **Why this test is weak by nature, and what that means.** Few-arc words are polynomially many in `m`, while `Φ_2 ≈ 2^(A/2)` is exponential. Even the near-doubled families, which trade few mismatches for exponentially many words, give only `≈ Φ_2/25` distinct conditions per `(n, B)`. So an *accidental* violation of `g_prim < 2^(A/2)` at `e = 2` is unlikely in any range a computer can reach, and the conjecture can fail only through a *structure* forcing `C_u ≡ 2^(Δ/2)C_v (mod Φ_2)`, the way the half-swap and two-marker symmetries force the minus sign modulo `Φ_1`. None is known; the sign is the whole difference.
- **Non-uniformity.** Intercept residues modulo `Φ_2` are not uniform: among all words of a given `(n, B)`, collisions `C_u ≡ C_v (mod Φ_2)` occur 3–4 times less often than `N²/(2Φ_2)` would give (anti-concentration), and for a prime `p | Φ_2` the rate of `p | (2^d − 1)F(z)` deviates from `1/p` by factors up to 20 in either direction, reflecting the subgroup generated by 2 and 3 modulo `p`. The heuristic expectations above should be read with that in mind.
- **The census gap this closes.** The censuses enumerated coprime shifts (and `gcd(h, m) ∈ {2, 3}` for two arcs); the near-doubled words have `gcd(h, m) = m/2` and were not covered, although they have `ρ ≤ 4`. For `n ≤ 11` (transpositions) and `n ≤ 9` (one letter) they now are.
- **Controls.** The `3x+11` cycle `w = (1,1,2,2,1,1,3,3)` is an `e = 2` word (`A = 14`, `m = 8`, `Φ_1 = 47`, `Φ_2 = 209 = 11·19`) that is neither a transposition nor a one-letter change of its first half; the reduction of part 1 still applies, with `u = (1,1,2,2)`, `v = (1,1,3,3)`, `Δ = −2`, `C_u = 73`, `C_v = 89`: `2C_u − C_v = 57 = 3·19`, so `19 | C_w` and `11 ∤ C_w`, which is exactly its primitive part `g_prim = 19` (and its `G = 47·19` as `47 = Φ_1` also divides). Consistent with the conjecture, and an example of the reduction producing a partial primitive cancellation.
- **A cleaner target.** Through the rotation reformulation of (O), the one-letter family is the question whether an intercept `C_z` (length `ℓ`, total `S`) can be divisible by `2^(S+j) + 3^ℓ` for some `j ≥ 1`; the transposition family is the same question for the sub-word between the swapped letters, with the modulus `2^(S+j) + 3^(ℓ+i)`, `j > i ≥ 2`, and a factor `2^k − 1` allowed. Both are statements about one word and one two-term number, with no rotation or cycle in sight; a proof or a counterexample would settle the `e = 2` case of the conjecture for these families.
- Novelty undetermined; the reduction is elementary.

## History

- Written 2026-10-28 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, as the adversarial test of the primitive-cancellation conjecture at `e = 2` requested after the descent batch.
- 2026-10-31: the algebraic factor on these words is explained by corollary (i) of [`doubled-words-periodic-and-antiperiodic-points`](../doubled-words-periodic-and-antiperiodic-points/README.md): `Φ₁ | C_w` iff `u + j·e_i` is a `3x+q'` cycle word with `q' | 2^j + 1`, and the plus-sign condition is the antiperiodic-point criterion. The plain half bound was refuted the same day ([`half-cancellation-counterexample-rotation-pair`](../half-cancellation-counterexample-rotation-pair/README.md)); the primitive form tested here continues as [`primitive-cancellation-below-half`](../../questions/primitive-cancellation-below-half.md) (Claude cycles lane, Fable 5.1).
