---
id: primitive-cancellation-below-half
kind: question
title: Is the primitive cancellation of a few-mismatch word below 2^(A/2)?
status: open
claim: >
  Remaining target (C), raw odd-only clock, any 3x+q: determine which exponents
  c(s) and length thresholds m_0(s) make every primitive positive valuation word
  with m>=m_0(s), total A, D=2^A-3^m>0 and a rotation of exactly s mismatches
  satisfy g_prim<=2^(c(s)*A), or make every near-critical such word satisfy
  G<=2^(c(s)*A), where G=gcd(C_w,D), e=gcd(A,m) and
  g_prim=gcd(G,Phi_e(2^(A/e),3^(m/e))). The original form (A) is false,
  and the near-critical forms (A-prime) and (B) are also false: the existing
  3x+295 cycle of length 12 has A=20, rotation distance 4, and
  g_prim=G=1753>1024, as proved in near-critical-four-mismatch-corpus-counterexample.
created: 2026-10-31
tags: [cycles, denominators, cancellation, cyclotomic-factors, rotation-distance, frontier]
---

# Is the primitive cancellation of a few-mismatch word below `2^(A/2)`?

## Question

**Correction 2026-11-08: the near-critical forms (A′) and (B) are false.**
[`near-critical-four-mismatch-corpus-counterexample`](../results/near-critical-four-mismatch-corpus-counterexample/README.md)
rechecks the already recorded `3x+295` cycle with word
`(1,1,3,1,2,1,1,1,1,2,1,5)`: `m=12`, `A=20`, `rho=4`,
`3^12<2^20<2*3^12`, and `g_prim=G=1753>1024=2^(A/2)`.
Thus neither proposed half bound holds throughout the near-critical
class. **This node stays open only for part (C)**, which allows a
different exponent and a length threshold. The earlier formulations
and progress notes below are retained as history; statements there
that the near-critical forms remain open are superseded by this note.

**Correction 2026-10-31 (same day): part (A) as posed is false.** The complete census [`rho-four-census-letters-three`](../results/rho-four-census-letters-three/README.md) finds the word `(1,1,2,2,1,3,1,2,2,2,3,3)` (`m = 12`, `A = 23`, `gcd(A, m) = 1`, `ρ = 4`, the word of a `3x+1327` cycle) with `g_prim = G = 5921 > 2^(11.5)`, and another at `m = 20`. Both are far from critical (`2^A/3^m = 15.8` and `2.46`); no near-critical word (`2^A < 2·3^m`) violates either bound in that census. The open forms are therefore the **near-critical** ones: (A′) `g_prim < 2^(A/2)` and (B) `G² < 2^A` for near-critical primitive words with `ρ ≤ 4` and `m ≥ 9` (B implies A′), and (C). The text below is kept as posed.

Notation of [`conventions/NOTATION.md`](../../../conventions/NOTATION.md) §2 and of [`algebraic-and-primitive-cancellation-census`](../results/algebraic-and-primitive-cancellation-census/README.md): `w` primitive positive, `m`, `A`, `D = 2^A − 3^m > 0`, `G = gcd(C_w, D)`, `ρ(w)` its rotation distance, `e = gcd(A, m)`,

```
D = Π_(d | e) Φ_d(2^(A/e), 3^(m/e)),        g_prim = gcd(G, Φ_e(2^(A/e), 3^(m/e)))        (g_prim = G when e = 1).
```

**(A) Prove or refute:** if `m ≥ 9` and `ρ(w) ≤ 4`, then `g_prim < 2^(A/2)`.

**(B) Also:** does the plain bound `G² < 2^A` hold for the near-critical words, `2^A < 2·3^m`, with `m ≥ 9` and `ρ(w) ≤ 4`?

**(C) Also:** for which `c(s)` does every primitive word with a rotation of exactly `s` mismatches (and `m ≥ m₀(s)`) satisfy `g_prim ≤ 2^(c(s)·A)`, or the near-critical ones `G ≤ 2^(c(s)·A)`?

This replaces [`half-cancellation-for-few-mismatch-words`](half-cancellation-for-few-mismatch-words.md), whose plain bound `G² < 2^A` for all `ρ ≤ 4` words was refuted on 2026-10-31 by [`half-cancellation-counterexample-rotation-pair`](../results/half-cancellation-counterexample-rotation-pair/README.md): a word of length 20 with `ρ = 4`, `G = 5·(2^20 − 3^10)` and `G² ≈ 22·2^A`. There the whole algebraic factor `2^(A/2) − 3^(m/2)` divides `C_w` and the primitive part is 5; the word is far from critical (`3^10/2^20 = 0.056`).

## Why it matters

- **Payoff at `q = 1` (form A).** A nontrivial `q = 1` cycle has `G = D`, hence `g_prim = Φ_e(2^(A/e), 3^(m/e))`. With `x/y = (2^A/3^m)^(1/e)` just above 1, `Φ_e(x, y) = y^φ(e)·Φ_e(x/y) ≈ 3^(mφ(e)/e)·Φ_e(1)`, which exceeds `2^(A/2)` whenever `φ(e)/e > 1/2` (for `e = 2, 4, 8`: `Φ_e = x^(e/2) + y^(e/2) > 2^(A/2)` exactly), and for `e = 1` it is `D` itself, which the replayed gap EXT-1 ([`musson-collatz-gap-all`](../../../sources/musson-collatz-gap-all.md)) puts above `2^(A/2)` for `m > 5,580` and the irrationality measure of [`rhin-1987-irrationality-measure`](../../../sources/rhin-1987-irrationality-measure.md), as recorded, for `m ≥ 131`. So (A) excludes every rotation with at most four mismatches for every `q = 1` cycle whose `gcd(A, m)` is 1, a prime power, or any `e` with `φ(e)/e > 1/2`; with the period bound of [`hercher-2023-cycle-length`](../../../sources/hercher-2023-cycle-length.md) that is `ρ ≥ 5` ([`rotation-distance-at-least-5`](rotation-distance-at-least-5.md)) for those cycles. It is silent when `φ(e)/e < 1/2`, i.e. when `e` is even with a second prime factor (`6, 10, 12, 14, …`) or odd with many prime factors (`105, …`); form (B) would cover those too, since a `q = 1` cycle is near-critical.
- **It is what the data support.** Across the censuses ([`few-arc-codings-denominator-census`](../results/few-arc-codings-denominator-census/README.md), [`algebraic-and-primitive-cancellation-census`](../results/algebraic-and-primitive-cancellation-census/README.md)) `g_prim ≤ 2^16.2` with `A` up to 141 and `log₂(g_prim)/A ≤ 0.446`; in the doubled-word families the primitive part is at most 305 while the algebraic part is all of `2^(A/2) − 3^(m/2)` ([`doubled-words-periodic-and-antiperiodic-points`](../results/doubled-words-periodic-and-antiperiodic-points/README.md)). Every large cancellation ever observed is algebraic.
- **It is sharp.** For `ρ = 2` words the algebraic part alone reaches `2^(A/2)·(1 − 3^(m/2)/2^(A/2))`, within `7·10^(−6)` bits of `2^(A/2)` ([`doubled-words-periodic-and-antiperiodic-points`](../results/doubled-words-periodic-and-antiperiodic-points/README.md), the `3x+257` word); the exponent `A/2` in (A) cannot be lowered for `e = 2` either, where the conjecture says exactly `Φ₂ ∤ C_w` ([`near-doubled-words-primitive-factor-test`](../results/near-doubled-words-primitive-factor-test/README.md)).

## Known progress

- **2026-11-08: the near-critical example is unique in one sparse four-arc family.**
  [`sparse-four-arc-near-critical-classification`](../results/sparse-four-arc-near-critical-classification/README.md)
  considers `(1^(2r-4),a,1,c,1^(2r-2),c,1,b)`, with `r>=2`,
  `a,b>=1`, `c>=2`, even total, and near-critical drift. Under
  the coprime shift `2r-1`, its prescribed arc lengths are
  `(4r-4,1,2,1)`. A positive-letter residue bound reduces all
  lengths to 11,697 finite cases and proves that full plus-factor
  cancellation occurs only for the `3x+295` counterexample.
  Its other denominator factor survives, so this near-critical
  family contains no denominator-1 word. The result does not
  bound partial cancellation or classify arbitrary four-arc words;
  part (C) remains open and forms (A′), (B) remain refuted.

- **2026-11-08: both near-critical half bounds refuted.**
  The [exact corpus counterexample](../results/near-critical-four-mismatch-corpus-counterexample/README.md)
  has primitive cyclotomic index 4, full primitive cancellation 1753,
  and four-mismatch rotations at coprime shifts 5 and 7. It contains
  a letter 5, outside the letters-at-most-3 census; its half-period
  shift has 8 mismatches, outside the small half-defect exclusions.
  The example does not refute an asymptotic bound with a larger
  threshold, and satisfies the weaker
  [`rotation-defect-denominator-candidate`](rotation-defect-denominator-candidate.md).

- **2026-11-08: gap fourteen is completely classified.**
  [`transposition-gap-fourteen-complete-classification`](../results/transposition-gap-fourteen-complete-classification/README.md)
  proves that every gap-fourteen transposition which cancels the entire
  plus factor is the pair `(1,z,15),(15,z,1)` of the
  [counterexample node](../results/transposition-gap-fourteen-full-plus-cancellation/README.md),
  up to exchanging halves. Its half-length and total are forced to
  `n=189`, `B=336`, with `gcd(B,n)=21`, and it is far from critical.
  Thus no near-critical gap-fourteen transposition cancels the full
  plus factor, and none at index `e=2` does so even far from critical.
  This classifies arbitrary word lengths through a finite crossing
  closure and the complete forced signed orbit, rather than a bounded
  word census. The general near-critical plain bound was subsequently
  refuted by the corpus counterexample above.

- **2026-11-08: equal-amplitude half defects reduce to balanced transfers.**
  [`equal-amplitude-half-defect-normal-form`](../results/equal-amplitude-half-defect-normal-form/README.md)
  shows that two changes of the same absolute amplitude can be made
  opposite in sign by changing the cyclic cut. The middle-intercept
  identity and signed-crossing constraints require only a balanced
  transfer, not a literal transposition. Consequently the full plus
  factor is excluded for every amplitude through 12 in this enlarged
  family, uniformly in word length and the other letters. At index 2
  this gives the primitive half bound, including genuine near-critical
  pairs with unequal half totals.

- **2026-11-08: modification parameters through twelve, at every length.**
  [`near-doubled-crossing-orbit-exclusion`](../results/near-doubled-crossing-orbit-exclusion/README.md)
  removes the coprimality restriction below for every one-letter raise
  `2j`, `1<=j<=12`, and every transposition gap `1<=k<=12`. Finite
  forward-closed sets for the auxiliary maps `3x+(2^k-1)` and their
  exceptional signed endpoints prove the plus factor cannot cancel
  completely, with no bound on the word length or the remaining letters.
  At `e=2` this gives the primitive half bound without a near-critical
  assumption. These two families do not cover all four-mismatch words.

- **2026-11-08: clean-intercept target and coprime near-doubled cases proved.**
  [`antiperiodic-intercept-nondivisibility`](../results/antiperiodic-intercept-nondivisibility/README.md)
  proves `2^B t+3^n s` never divides the intercept of a positive word of length
  `n` and total `B`, for all positive integers `s,t`: otherwise its affine
  word would take a negative integer to a positive integer through integral
  cuts. This settles the one-letter family when
  `gcd(2^j-1,2^(B+j)+3^n)=1` (always for `j=1,2`) and the transposition
  family when `gcd(2^k-1,2^B+3^n)=1` (always for letter gaps `k=1,2`).
  At `e=2` these give the primitive half bound without any near-critical
  restriction. The nonunit cases and general four-mismatch problem remain.

- **`s = 2`, proved forms.** [`two-defect-cancellation-bound`](../results/two-defect-cancellation-bound.md) (7): `G² < 2^(2A−2m)·3^m`, far above `2^A`; its proof loses the gcd of the two arc intercepts. The Sturmian two-arc case is exact: `G | 2^k − 1` ([`two-arc-word-rotation-structure`](../results/two-arc-word-rotation-structure/README.md)).
- **Censuses.** 493,483 few-arc census entries (`s ≤ 4`, `m ≤ 40`): `g_prim < 2^17`, random-divisor-like tail ([`algebraic-and-primitive-cancellation-census`](../results/algebraic-and-primitive-cancellation-census/README.md)); the plain bound held throughout those censuses for `m ≥ 9` ([`few-arc-codings-denominator-census`](../results/few-arc-codings-denominator-census/README.md)), because none of their words has a full algebraic factor together with a nontrivial primitive one.
- **`e = 2`.** The conjecture is `Φ₂ = 2^(A/2) + 3^(m/2) ∤ C_w`; adversarial search over near-doubled words finds no violation ([`near-doubled-words-primitive-factor-test`](../results/near-doubled-words-primitive-factor-test/README.md)). The condition is the antiperiodic-point criterion `2^j·y_u − y_v ∈ Z` of [`doubled-words-periodic-and-antiperiodic-points`](../results/doubled-words-periodic-and-antiperiodic-points/README.md); in the one-letter family it is the twisted cycle condition `2^S + 3^n | (2^j − 1)·C_(u°)`.
- **The refutation of the plain form** and what it shows: the algebraic factor is realised in full by every rotation pair `(R_r u, R_s u)` of an actual `3x+d` cycle with `d | n_r + n_s`, so the plain bound rests on the primitive part being below `1/(1 − 3^(m/2)/2^(A/2))`; three cycle classes with `d ≤ 20,000` break it at `ρ = 4`, none of them near-critical ([`half-cancellation-counterexample-rotation-pair`](../results/half-cancellation-counterexample-rotation-pair/README.md)). Among 1,809 corpus pairs the plain bound also fails at `ρ = 8, 10, 12, …` with primitive parts up to 305.
- **Three mismatches by elimination: vacuous** ([`three-arc-intercept-elimination`](../attempts/three-arc-intercept-elimination/README.md)). **Obstructions** to the known routes for `s ≥ 3`: [`coupled-defect-matrix-smith-form`](../results/coupled-defect-matrix-smith-form/README.md), [`three-defect-arbitrary-background`](../results/three-defect-arbitrary-background.md), [`termwise-plateau-divisibility`](../attempts/termwise-plateau-divisibility.md).
- **Rotation pairs, exactly.** For `w = (R_r u, R_s u)` built from two rotations of an actual `3x+d` cycle word, `gcd(C_w, D_w) = G_u·gcd(n_r + n_s, d)·gcd(n_r − n_s, 2^S + 3^n)` ([`rotation-pair-words-exact-cancellation`](../results/rotation-pair-words-exact-cancellation/README.md), from the formal [`doubled-word-cancellation-formula`](../results/doubled-word-cancellation-formula/README.md)): the primitive-side factor is the gcd of a state difference with `2^S + 3^n`, at most 67,721 over 8.2 million pairs, so (A) holds throughout this family and says there that two states of a `3x+d` cycle never differ by a multiple of a divisor `≥ 2^S` of `2^S + 3^n`.
- **(A) refuted; the near-critical forms remain.** [`rho-four-census-letters-three`](../results/rho-four-census-letters-three/README.md) enumerates every primitive word with letters `≤ 3`, `9 ≤ m ≤ 20`, `D > 0` and `ρ ≤ 4` over all shifts (979,497 words, 29,052 near-critical): eight violate the plain bound, two of them with `gcd(A, m) = 1` (so `g_prim = G > 2^(A/2)`), all eight far from critical, none near-critical; the closest near-critical word for `m ≤ 16` is 1.0 bits below the bound. A labelled random-divisor heuristic predicts exactly this pattern: a handful of far-from-critical violations and about `0.3·c` near-critical ones, with the expected number per `m` decreasing in `m`.

## Suggested attacks

**Current target after the 2026-11-08 refutation.** Part (C) must allow
for the twelve-letter `3x+295` example. Investigate an asymptotic
threshold, a weaker mismatch-dependent exponent, or hypotheses that
use denominator 1 rather than the entire near-critical `3x+q` family.
The weaker rotation-defect denominator candidate remains unrefuted.
The family-specific signed-crossing results below still hold, but
cannot imply the refuted universal near-critical half bound.

**Updated target, 2026-11-08.** Equal-amplitude changes through 12 in
half-period four-mismatch pairs are covered by the balanced normal form.
The remaining half-pair targets have unequal absolute changes, or equal
amplitudes beyond the established range. For these, combine the exact
endpoint equations with the near-critical condition; general rotations
remain a separate target. Merely assuming that the two changed letters
must be a transposition would miss the cases now covered.

Proposals, not results.

- **Work modulo the primes of `Φ_e`.** `g_prim > 1` needs a prime `p | Φ_e(2^(A/e), 3^(m/e))`, i.e. `2^(A/e) ≡ ζ·3^(m/e) (mod p)` for a primitive `e`-th root of unity `ζ`, with `p | C_w`. The heuristic truth of (A) is that `C_w mod p` is equidistributed for such `p`; a proof needs the arithmetic of the few-arc intercepts modulo these primes, starting with `e = 1` (then `ζ = 1`, `2^A ≡ 3^m`, and `p | D`) and `e = 2` (`ζ = −1`).
- **The remaining antiperiodic problem at `e = 2`.** The clean-intercept
  subtarget is now proved by
  [`antiperiodic-intercept-nondivisibility`](../results/antiperiodic-intercept-nondivisibility/README.md),
  and the noncoprime factors are handled through parameter 12 by
  [`near-doubled-crossing-orbit-exclusion`](../results/near-doubled-crossing-orbit-exclusion/README.md).
  For larger parameters, classify the feasible signed segments of
  `3x+(2^k-1)` subject to the near-critical inequality
  `2^(2S)<2*3^(2n)` and the endpoint and word-fillability conditions.
  Also study half-pairs with two unequal changes that are not a
  transposition; those are not covered by the current argument.
- **Classify the signed endpoints, including repeated hits.** The
  [gap-fourteen classification](../results/transposition-gap-fourteen-complete-classification/README.md)
  demonstrates a finite reduction: a closed crossing basin gives
  finitely many last arrows and forced signed starts. A complete orbit
  then distinguishes transient hits from periodic families. Positive
  cycle repetitions increase `2^S/3^n`, so each periodic family has
  a finite exact test for the near-critical interval. Seek structural
  restrictions on these candidate orbits and their repeat ratios;
  the method requires supplied finite closures and does not assume
  them for every auxiliary parameter.
- **Test (B) adversarially** with the doubled-word constructions restricted to near-critical cycles: rotation pairs `(R_r u, R_(r+n/2) u)` of actual `3x+d` cycles with `d | n_r + n_(r+n/2)` and `2^(2S) < 2·3^(2n)`, and one-letter doublings of near-critical `3x+q'` cycles with `q' | 2^j + 1`; a violation would need a prime of `Φ₂` above `1/(1 − 3^n/2^S) ≥ 3.4` dividing `C_w`.
- **Two arcs, non-Sturmian case.** Bound `gcd(C_u, C_v)` for the two arcs of a two-interval rotation coding whose interval length differs from the step, by a Rauzy-type induction on the arc, as suggested in [`half-cancellation-for-few-mismatch-words`](half-cancellation-for-few-mismatch-words.md).

## History

- 2026-11-08: added the scoped sparse four-arc classification and
  its near-critical denominator-1 exclusion (Codex four-arc research
  lane, GPT-6 Astra; directed by Santiago Armstrong). The counterexample
  and the remaining asymptotic question are unchanged.

- 2026-11-08: forms (A′) and (B) refuted by
  [`near-critical-four-mismatch-corpus-counterexample`](../results/near-critical-four-mismatch-corpus-counterexample/README.md).
  Updated the claim to the remaining part (C), kept status `open`,
  and retained the original formulations under the dated correction.
  Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong).

- 2026-11-08: added the complete gap-fourteen transposition
  classification, its near-critical and index-2 exclusions, and the
  finite signed-endpoint research direction (Codex crossing research
  lane, GPT-6 Astra; directed by Santiago Armstrong). No general
  near-critical half bound is claimed.

- 2026-11-08: added the equal-amplitude balanced normal form and refined
  the suggested attacks to the remaining half-pair and rotation cases
  (Codex cycle research lane, GPT-6 Astra; directed by Santiago Armstrong).

- 2026-11-08: added the finite-crossing proof for all lengths with
  modification parameters through 12 and replaced the now-solved
  clean-intercept suggested attack with the remaining signed-segment
  and nontransposition targets (Codex crossing research lane, GPT-6
  Astra; directed by Santiago Armstrong). The near-critical question
  and the general four-mismatch exclusion remain open.

- 2026-11-08: added the signed-intercept theorem and its one-letter and
  transposition consequences (Codex cycle research lane, GPT-6 Astra;
  directed by Santiago Armstrong). The question remains open.

- Posed 2026-10-31 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, as the surviving form of [`half-cancellation-for-few-mismatch-words`](half-cancellation-for-few-mismatch-words.md) after its refutation the same day.
- 2026-10-31, later: Known progress gains the exact rotation-pair formula (Claude cycles lane, Fable 5.1).
- 2026-10-31, later: part (A) refuted by [`rho-four-census-letters-three`](../results/rho-four-census-letters-three/README.md); the question continues in its near-critical forms (A′), (B) and (C) (Claude cycles lane, Fable 5.1).
