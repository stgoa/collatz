---
id: doubled-words-periodic-and-antiperiodic-points
kind: result
title: "Doubled words: the two factors of D test the half-words' periodic and antiperiodic points"
status: written
claim: >
  Raw odd-only clock, any 3x+q. Let w = (u, v) with |u| = |v| = n and even total A = 2S, so that
  D = 2^A − 3^(2n) = Φ₁·Φ₂ with Φ₁ = 2^S − 3^n and Φ₂ = 2^S + 3^n coprime. Put j = (S_v − S_u)/2 ∈ Z and, for a
  word z of length n, x_z = C_z/Φ₁ and y_z = C_z/Φ₂: the fixed point and the antiperiodic point (T(−y) = y) of the
  affine map T(x) = (3^n x + C_z)/2^S. Then gcd(C_w, Φ₁) = gcd(2^j C_u + C_v, Φ₁) and
  gcd(C_w, Φ₂) = gcd(2^j C_u − C_v, Φ₂), with 2^j read modulo the odd factor; so Φ₁ | C_w iff 2^j x_u + x_v ∈ Z,
  Φ₂ | C_w iff 2^j y_u − y_v ∈ Z, and G = gcd(C_w, D) is the product of the two gcds. Corollaries: (i) for
  v = u + 2j·e_i (j ≥ 1) and u' = u + j·e_i, gcd(C_w, Φ₁) = gcd((2^j + 1)·C_(u'), D_(u')), so Φ₁ | C_w iff u' is the
  valuation word of an integer cycle of 3x+q' for some q' | 2^j + 1, and gcd(C_w, Φ₂) = gcd((2^j − 1)·C_(u°), Φ₂)
  with u° the rotation of u starting after position i; (ii) the two-marker family is the case u' = (2)^n, j = 1,
  which gives G = 4^n − 3^n in two lines; (iii) for two rotations R_r u, R_s u of the valuation word of an actual
  3x+d cycle with states n_r, n_s, Φ₁ | C_(R_r u, R_s u) iff d | n_r + n_s. Data: among the 1,176 distinct cycle
  words of actual-cycles-3x-d-corpus, 1,809 of the 739,757 rotation pairs satisfy d | n_r + n_s; every one has
  Φ₁ | C_w and G = Φ₁·gcd(C_w, Φ₂); with exact rotation distances, 131 of them violate G² < 2^A, the smallest with
  ρ = 8 (m = 18), none of the 66 with ρ ≤ 7 (their gcd(C_w, Φ₂) ∈ {1, 5}); the 8 one-letter words built from the
  cycles of 3x+5, 3x+17 and 3x+257 all have gcd(C_w, Φ₂) = 1 and G = Φ₁, one of them (m = 32) within
  7·10^(−6) bits of G² = 2^A.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-31
depends_on: [actual-cycles-3x-d-corpus]
certificates: [check_doubled_words.py]
evidence:
  - "doubled_words.json: the receipt; H1 the identity and gcd checks on 2,000 pseudo-random pairs and 1,000 one-letter pairs (seed 20261030), H2 the two-marker family n ≤ 40, H3 the corpus scan (counts, the table by rotation distance, the violations with m ≤ 36 and the closest word with ρ ≤ 7, as explicit words), H4 the one-letter words from fresh scans of 3x+5, 3x+11, 3x+13, 3x+17, 3x+41, 3x+65, 3x+257 (odd seeds ≤ 200,000) with their cycle minima"
tags: [cycles, denominators, cancellation, cyclotomic-factors, doubled-words, controls]
---

# Doubled words: the two factors of D test the half-words' periodic and antiperiodic points

## Statement

Notation of [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §2: a positive word `z` has total `S_z`, intercept `C_z = Σ_(t<|z|) 3^(|z|−1−t)·2^(s_t)` (prefix sums `s_t`; the intercept does not depend on the last letter), `D_z = 2^(S_z) − 3^|z|`, and when `D_z > 0` its rational cycle point `C_z/D_z`, with reduced denominator `den(z)`. For the valuation word of an actual `3x+d` cycle with states `n_0, …, n_(|z|−1)` coprime to `d`, `den(z) = d` and the rational cycle point of the rotation `R_r z` (starting at `n_r`) is `n_r/d`.

**Setting.** `w = (u, v)` with `|u| = |v| = n ≥ 1` and `A = S_u + S_v = 2S` even. Then `m = 2n` and

```
D = 2^A − 3^m = Φ₁·Φ₂,     Φ₁ = 2^S − 3^n,     Φ₂ = 2^S + 3^n,     gcd(Φ₁, Φ₂) = 1,
```

since a common divisor divides `2·3^n` while both factors are odd and prime to 3. Put `j = (S_v − S_u)/2 ∈ Z`. For a word `z` of length `n` write `T_z(x) = (3^n x + C_z)/2^S` (the affine map of `z` with its total read as `S`; this is the map of a legal word exactly when the last letter can be adjusted to make the total `S`, but the statements below need only the map) and

```
x_z = C_z / Φ₁   (the fixed point:  T_z(x_z) = x_z),        y_z = C_z / Φ₂   (the antiperiodic point:  T_z(−y_z) = y_z).
```

**Theorem.** With `2^j` read as the inverse of `2^(−j)` modulo the odd factor when `j < 0` (equivalently, multiply the other term by `2^(−j)`):

```
gcd(C_w, Φ₁) = gcd(2^j·C_u + C_v, Φ₁),          gcd(C_w, Φ₂) = gcd(2^j·C_u − C_v, Φ₂),          G = gcd(C_w, D) = gcd(C_w, Φ₁)·gcd(C_w, Φ₂).
```

Hence `Φ₁ | C_w` iff `2^j·x_u + x_v ∈ Z`, and `Φ₂ | C_w` iff `2^j·y_u − y_v ∈ Z`: the algebraic factor tests the periodic points of the two half-maps, the other factor their antiperiodic points. (When `S_u = S_v` this reads `x_u + x_v ∈ Z` and `y_u − y_v ∈ Z`.)

**Corollary (i): one-letter changes.** Let `v = u + 2j·e_i` for some position `i` and `j ≥ 1`, and `u' = u + j·e_i`, so `S_(u') = S` and `D_(u') = Φ₁`. Then

```
gcd(C_w, Φ₁) = gcd((2^j + 1)·C_(u'), D_(u')),        gcd(C_w, Φ₂) = gcd((2^j − 1)·C_(u°), Φ₂),
```

where `u° = (a_(i+1), …, a_(n−1), a_0, …, a_i)` is the rotation of `u` starting after position `i`. In particular `Φ₁ | C_w` iff `den(u') | 2^j + 1`, i.e. iff `u'` is the valuation word of an integer cycle of `3x+q'` for some `q' | 2^j + 1` (`q'` is automatically coprime to 6).

**Corollary (ii): the two-marker family.** `u = (1, 2^(n−1))`, `v = (3, 2^(n−1))` is the case `i = 0`, `j = 1`, `u' = (2)^n`, the trivial cycle: `gcd(C_w, Φ₁) = gcd(3·(4^n − 3^n), 4^n − 3^n) = 4^n − 3^n`, and `u° = (2^(n−1), 1)` has `C_(u°) = 4^n − 3^n`, so `gcd(C_w, Φ₂) = gcd(4^n − 3^n, 4^n + 3^n) = gcd(4^n − 3^n, 2·3^n) = 1`. Hence `G = 4^n − 3^n`, the exact denominator of [`two-marker-constant-background-exact-denominator`](../two-marker-constant-background-exact-denominator/README.md).

**Corollary (iii): rotation pairs of actual cycles.** Let `u` be the valuation word of an actual `3x+d` cycle with reduced denominator `d` and states `n_0, …, n_(n−1)`, and `w = (R_r u, R_s u)`. Then `S_u = S_v`, `Φ₁ = D_u`, `x_(R_r u) = n_r/d`, and

```
Φ₁ | C_w     iff     d | n_r + n_s.
```

**Data (certificate H3, H4).** Over the 1,176 distinct cycle words with `n ≥ 2` of [`actual-cycles-3x-d-corpus`](../actual-cycles-3x-d-corpus/README.md) (`d ≤ 999`, seeds `≤ 5000`), 1,809 of the 739,757 rotation pairs `r < s` have `d | n_r + n_s`; the criterion of (iii) agrees with direct divisibility on every pair, and `G = Φ₁·g₂` with `g₂ = gcd(C_w, Φ₂)` on every hit. Rotation distances `ρ(w)` were computed exactly:

| `ρ(w)` | words | `G² ≥ 2^A` | max `log₂G − A/2` | `g₂ > 1` |
|---|---|---|---|---|
| 2 | 8 | 0 | −0.549 | 0 |
| 4 | 33 | 0 | −0.046 | 3 |
| 6 | 16 | 0 | −0.182 | 4 |
| 7 | 9 | 0 | −0.322 | 4 |
| 8 | 35 | 2 | +3.055 | 2 |
| 9 | 18 | 0 | −0.235 | 0 |
| 10 | 42 | 3 | +4.832 | 3 |
| 11 | 10 | 0 | −0.011 | 0 |
| 12 | 45 | 1 | +5.139 | 1 |
| all | 1,809 | 131 | +7.811 | — |

The smallest violation of the half bound `G² < 2^A` is `w = (1,1,2,1,1,3,1,2,9,3,1,2,9,1,1,2,1,1)`, `m = 18`, `ρ = 8`, from rotations 0 and 5 of the `3x+307` cycle through 5, with `g₂ = 7` and `log₂G − A/2 = +2.79`; the largest excess is `+7.81` bits (`m = 96`, `3x+307`, `g₂ = 305`). Of the 66 words with `ρ ≤ 7` none violates the bound; eleven have `g₂ = 5` (all from `3x+499` cycles of length 10, where `5 | Φ₂` and `3^n/2^S = 0.90`), the rest `g₂ = 1`; the closest to the bound is `(2,1,1,1,1,6,2,1,5,1,1,2,2,1,5,1,1,2,2,1,1,1,1,6)`, `m = 24`, `ρ = 4`, from the `3x+965` cycle through 163, at `−0.046` bits with `g₂ = 1`.

The one-letter words of (i) built from every cycle of `3x+q'` found from odd seeds `≤ 200,000` for `q' ∈ {5, 11, 13, 17, 41, 65, 257}` (the `q' ≤ 257` for which `2^j ≡ −1 (mod q')` has a solution `j ≤ 12`, other than those needing a letter above every letter present) number 8: six from the `3x+5` cycles through 1, 19, 187 and 347 (`j = 2`), one from the `3x+17` cycle through 1 (`j = 4`, word `(2, 5)`), one from the `3x+257` cycle through 1 (`j = 8`, `n = 16`, letter 9). All eight have `g₂ = 1`, so `G = Φ₁` exactly; the `3x+257` word has `m = 32`, `S = 43` and `log₂G − A/2 = log₂(1 − 3^16/2^43) = −7·10^(−6)`.

## Proof

**Concatenation.** The prefix sums of `w` on the second half are `S_u + s_t(v)` and the powers of 3 on the first half are `3^(2n−1−t) = 3^n·3^(n−1−t)`, so `C_w = 3^n·C_u + 2^(S_u)·C_v` (checked as an identity in H1).

**The two congruences.** Modulo `Φ₁`, `3^n ≡ 2^S`, hence `C_w ≡ 2^S·C_u + 2^(S_u)·C_v = 2^(S_u)·(2^(S−S_u)·C_u + C_v)` and `S − S_u = (S_v − S_u)/2 = j`. Modulo `Φ₂`, `3^n ≡ −2^S`, hence `C_w ≡ −2^(S_u)·(2^j·C_u − C_v)`. If `j < 0`, multiply through by `2^(−j)`. Since 2 is a unit modulo each odd factor, the gcds follow, and `gcd(C_w, D) = gcd(C_w, Φ₁)·gcd(C_w, Φ₂)` because `Φ₁`, `Φ₂` are coprime. The point statements: `T_z(x) = x` iff `(2^S − 3^n)x = C_z`, and `T_z(−y) = y` iff `C_z − 3^n y = 2^S y`; for `j ≥ 0`, `2^j x_u + x_v = (2^j C_u + C_v)/Φ₁` is an integer iff `Φ₁ | 2^j C_u + C_v`, and likewise for `y` (for `j < 0` use the multiplied form).

**(i).** Write `P_≤ = Σ_(t≤i) 3^(n−1−t)2^(s_t)` and `P_> = Σ_(t>i) 3^(n−1−t)2^(s_t)`, so `C_u = P_≤ + P_>`. The prefix sums of `v` are `s_t + 2j·[t > i]`, so `C_v = P_≤ + 2^(2j)·P_>`, `S_v − S_u = 2j` and the theorem's `j` is this `j`. Then `2^j C_u + C_v = (2^j + 1)·(P_≤ + 2^j·P_>) = (2^j + 1)·C_(u')`, because `u'` has prefix sums `s_t + j·[t > i]`; and `S_(u') = S_u + j = S`, so `D_(u') = Φ₁`. Also `2^j C_u − C_v = (2^j − 1)·(P_≤ − 2^j·P_>)`. For the rotation `u°`, the letters `a_(i+1), …, a_(n−1)` come first with prefix sums `s_t − s_(i+1)` and powers `3^(n−1−(t−i−1))`, and `a_0, …, a_i` follow with prefix sums `S_u − s_(i+1) + s_t` and powers `3^(i−t)`; multiplying by `3^(n−1−i)·2^(s_(i+1))`,

```
3^(n−1−i)·2^(s_(i+1))·C_(u°) = 3^n·P_> + 2^(S_u)·P_≤ ≡ −2^(S_u+j)·P_> + 2^(S_u)·P_≤ = 2^(S_u)·(P_≤ − 2^j·P_>)   (mod Φ₂),
```

so `gcd(C_w, Φ₂) = gcd((2^j − 1)·C_(u°), Φ₂)`. Finally `gcd((2^j + 1)C_(u'), D_(u')) = D_(u')` iff `D_(u') | (2^j + 1)·C_(u')` iff `den(u') | 2^j + 1`, and `den(u') | q'` is exactly the condition for `u'` to be the valuation word of an integer `3x+q'` cycle (NOTATION §2).

**(ii).** `C_((2)^n) = Σ_(t<n) 3^(n−1−t)·4^t = 4^n − 3^n = D_((2)^n)`, so `den((2)^n) = 1`; `C_((2^(n−1), 1))` has the same terms (the last letter does not enter), and `gcd(4^n − 3^n, 4^n + 3^n) = gcd(4^n − 3^n, 2·3^n) = 1`.

**(iii).** `S_(R_r u) = S_(R_s u) = S_u`, so `j = 0` and `Φ₁ = D_u`; `x_(R_r u) = C_(R_r u)/D_u = n_r/d` by NOTATION §2, so `x_(R_r u) + x_(R_s u) = (n_r + n_s)/d`.

The data are exact integer computations, described under Certificates.

## Certificates

[`check_doubled_words.py`](check_doubled_words.py) (standard library, about 5 s) checks: **H1** on 2,000 pseudo-random pairs (`n ≤ 14`, letters `≤ 6`, seed 20261030) the concatenation identity, both gcd formulas, the periodic and antiperiodic criteria with exact rationals, and `T_z(x_z) = x_z`, `T_z(−y_z) = y_z`; on 1,000 random one-letter pairs the two formulas of (i). **H2** the two-marker family for `2 ≤ n ≤ 40`, directly and through (ii). **H3** every rotation pair of every distinct cycle word of the corpus: the criterion (iii) against direct divisibility, `G = Φ₁·g₂`, the exact `ρ(w)`, the table above, no violation with `ρ ≤ 7`, smallest violating `ρ = 8`; it also records (as a labelled heuristic, not a check) the sum over the 66 words with `ρ ≤ 7` of `Σ_(p | Φ₂, p < 10^5) 1/p`, which is 7.98, against the 11 words observed with `g₂ > 1`. **H4** the one-letter words from fresh cycle scans: `Φ₁ | C_w`, `ρ(w) = 2`, `G = Φ₁·g₂`, `g₂ = 1` for all 8. **H5** the receipt [`doubled_words.json`](doubled_words.json); `--write-receipt` regenerates it. Finite statements only.

## Remarks

- **What the theorem says.** At `gcd(A, m) = 2` the factor `Φ₂` is the primitive factor of `D` and `Φ₁` the algebraic one ([`algebraic-and-primitive-cancellation-census`](../algebraic-and-primitive-cancellation-census/README.md)); the theorem turns both divisibilities into statements about the two half-words alone. The `Φ₂` condition is the plus-sign condition of [`near-doubled-words-primitive-factor-test`](../near-doubled-words-primitive-factor-test/README.md), now read as an antiperiodic point: `T_u(−y) = y` is a "cycle" that returns to the negative of its start, which no genuine odd-only orbit does (the odd-only map preserves the sign of integers), so the integrality `2^j y_u − y_v ∈ Z` has no orbit model, while the `Φ₁` condition is about genuine cycle points.
- **Where large cancellation comes from.** Corollary (iii) manufactures words with `G ≥ Φ₁ ≈ 2^(A/2)·(1 − 3^n/2^S)` from any actual `3x+d` cycle and any two of its states summing to `0 (mod d)`; corollary (i) does the same from any `3x+q'` cycle with `q' | 2^j + 1` and a letter `≥ j + 1`. The half bound `G² < 2^A` then holds iff `g₂ < 1/(1 − 3^n/2^S)`: automatic when `g₂ = 1`, and false as soon as a small prime of `Φ₂` divides `C_w` on a word far from critical. The eleven `g₂ = 5` words with `ρ ≤ 7` survive only because their `3^n/2^S = 0.90`; the explicit refutation of the half-cancellation conjecture at `ρ = 4` is [`half-cancellation-counterexample-rotation-pair`](../half-cancellation-counterexample-rotation-pair/README.md). The counts of `g₂ > 1` match the heuristic that `g₂` behaves like a random divisor of `Φ₂` (11 observed against 7.98 expected among the `ρ ≤ 7` words), which is also what [`algebraic-and-primitive-cancellation-census`](../algebraic-and-primitive-cancellation-census/README.md) found for the primitive part.
- **Sharpness of the exponent and of the constant.** The two-marker family has `G = 2^(A/2)·(1 − (3/4)^n)`; the one-letter word from the `3x+257` cycle has `G = 2^(A/2)·(1 − 3^16/2^43)`, within `7·10^(−6)` bits of `2^(A/2)` at `m = 32` with `ρ = 2`. So in `G² < 2^A` neither the exponent nor the constant 1 can be improved, even for `ρ = 2`, without a hypothesis on how far the word is from critical.
- **Controls.** The constructions take actual `3x+d` cycles as input, so every word here is itself an actual `3x+q` cycle word with `q = D/G` (for the corpus pairs, `q = Φ₂/g₂`); nothing is claimed about `q = 1`. The `3x+11` cycle `(1,1,2,2,1,1,3,3)` of the half-cancellation question is a doubled word with `v = u + e_2 + e_3`, outside corollary (i) (two letters change), but the theorem applies: `Φ₁ = 47 | 2C_u + C_v = 235` and `19 | Φ₂ = 209` with `19 | 2C_u − C_v = 57`.
- **Scope and novelty.** Finite data only beyond the stated identities. The factorisation of `D` for even `(A, m)` and the concatenation identity are elementary; the reading through periodic and antiperiodic points and the use of actual cycles as a source of cancellation are, as far as this repository knows, new here; novelty undetermined.

## History

- Written 2026-10-31 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, while trying to prove the `e = 2` case of the half-cancellation conjecture; the theorem explained the two-marker family and then produced the counterexample recorded in [`half-cancellation-counterexample-rotation-pair`](../half-cancellation-counterexample-rotation-pair/README.md).
