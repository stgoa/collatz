---
id: half-cancellation-for-few-mismatch-words
kind: question
title: Is the cancellation of a few-mismatch word at most half of 2^A?
status: open
claim: >
  Prove or refute: every primitive positive valuation word w of length m ≥ 9 with total A,
  D = 2^A − 3^m > 0, that has a nonidentity rotation differing from it in at most four positions, satisfies
  gcd(C_w, D)² < 2^A; equivalently its reduced denominator is q > 2^(A/2)·(1 − 3^m/2^A). Raw odd-only
  clock, any 3x+q. The exponent A/2 is sharp (the two-marker family has gcd = 2^(A/2) − 3^(m/2)), the
  bound m ≥ 9 is needed (the 3x+11 cycle (1,1,2,2,1,1,3,3) has gcd² > 2^A), and the statement cannot hold
  for all mismatch counts (actual small-d cycles with large m have gcd ≈ D/d). Also asked: the right
  dependence on the mismatch count s for which a bound gcd ≤ 2^(c(s)·A) holds.
created: 2026-10-28
tags: [cycles, denominators, cancellation, rotation-distance, frontier]
---

# Is the cancellation of a few-mismatch word at most half of `2^A`?

## Question

Notation of [`conventions/NOTATION.md`](../../../conventions/NOTATION.md) §2. For a primitive positive word `w` of length `m` and total `A` with `D = 2^A − 3^m > 0`, let `G = gcd(C_w, D)` and `q = D/G` be its cancellation and reduced denominator, and `ρ(w)` its rotation distance.

**Prove or refute:** if `m ≥ 9` and `ρ(w) ≤ 4`, then

```
G² < 2^A,        equivalently        q > 2^(A/2)·(1 − 3^m/2^A).
```

Also: find the correct dependence on `s`. For which function `c(s)` does every primitive word with a rotation of exactly `s` mismatches (and `m ≥ m_0(s)`) satisfy `G ≤ 2^(c(s)·A)`? The data below is consistent with `c(s) = 1/2` for `s ≤ 4`; since actual `3x+d` cycles with small `d` and large `m` have `G ≈ D/d ≈ 2^A` and `ρ ≥ m/5` (the stored cycles, see [`rotation-defect-denominator-candidate`](rotation-defect-denominator-candidate.md)), `c(s) → 1` as `s/m` grows.

## Why it matters

- **It is the sharp form of the denominator candidate.** [`rotation-defect-denominator-candidate`](rotation-defect-denominator-candidate.md) asks for `G^s·4^m < 2^(As)·3^m`, i.e. `G < 2^(A − (2 − log₂3)·m/s)`. The half bound `G ≤ 2^(A/2)` implies it for every `s ≥ 1`, because `A ≥ m > 2(2 − log₂3)·m/s`. In the exhaustive census of [`few-arc-codings-denominator-census`](../results/few-arc-codings-denominator-census/README.md) the candidate holds with a slack that grows linearly in `m` (at least `2^(17.5)` for `s = 3`), while the half bound is attained up to a factor `1 − (3/4)^n` by [`two-marker-constant-background-exact-denominator`](../results/two-marker-constant-background-exact-denominator/README.md). So this, and not the candidate, is the statement the data points at.
- **Payoff at `q = 1`.** A nontrivial `q = 1` cycle has `G = D`, so the bound says `D² < 2^A`, i.e. `D/2^A < 2^(−A/2)`. The replayed gap EXT-1 ([`musson-collatz-gap-all`](../../../sources/musson-collatz-gap-all.md)) gives `D/2^A ≥ 2^(−172)·m^(−341)`, which contradicts `D/2^A < 2^(−A/2)` as soon as `A/2 > 172 + 341·log₂m`; with `A > m·log₂3` this holds for every `m > 5,600`. So a positive answer, with EXT-1, excludes every rotation with at most four mismatches for all `q = 1` cycles of period above `5,600`, and with the period bound of [`hercher-2023-cycle-length`](../../../sources/hercher-2023-cycle-length.md) it gives `ρ ≥ 5`: the target of [`rotation-distance-at-least-5`](rotation-distance-at-least-5.md). A version with `c(s) < 1` for `s` growing with `m` would give `ρ → ∞` ([`rotation-distance-growth`](rotation-distance-growth.md)).
- **It separates the two regimes cleanly.** Large cancellation needs an algebraic factor `2^(A/e) − 3^(m/e)` of `D` (`e = gcd(A, m) > 1`) together with a symmetry of the word; near-critical words have small `gcd(A, m)` and tiny `G`. The question asks for the theorem behind that observation.

## Known progress

- **`s = 2`, the proved form.** [`two-defect-cancellation-bound`](../results/two-defect-cancellation-bound.md) (7): `G² < 2^(2A−2m)·3^m`, i.e. `G < 2^(A − 0.2075m)`. The half bound would be `G < 2^(A − A/2) ≈ 2^(A − 0.79m)` at the critical total. The proof bounds `gcd(C_u, C_v)` of the two arcs between the mismatches by `√(C_u·C_v)`; that step is exact for the two-marker family but loses about `m/2` bits on near-critical words, where the census finds the gcd to be `O(1)` (71 at `m = 17`).
- **The Sturmian two-arc case is settled, and it is exactly the adjacent-defect case.** [`two-arc-word-rotation-structure`](../results/two-arc-word-rotation-structure/README.md) shows that a two-arc word has adjacent mismatches iff its arc length equals the track step iff its mask is mechanical; there R71's one-step descent gives `G | 2^|b−a| − 1` (two-defect node, part 5), far below `2^(A/2)`. The open two-arc case is the non-Sturmian one, where the two mismatches sit at natural distance `2 ≤ ℓ ≤ m − 2`.
- **The cancellation is almost entirely algebraic.** [`algebraic-and-primitive-cancellation-census`](../results/algebraic-and-primitive-cancellation-census/README.md): with `e = gcd(A, m)`, `D = Π_(d|e) Φ_d(2^(A/e), 3^(m/e))`, and the primitive cancellation `g_prim = gcd(G, Φ_e)` (all of `G` when `gcd(A, m) = 1`) is `1` for about nine words in ten, never exceeds `2^16.2` over the 493,483 census entries (`A` up to 141), and has a random-divisor-like tail. Every large `G` in the census lives in the algebraic factors, which need `gcd(A, m) > 1` and a symmetry of the word. **Sharper conjecture:** `g_prim < 2^(A/2)` for words with `ρ ≤ 4` and `m ≥ 9` (the data gives `log₂(g_prim)/A ≤ 0.446`). At `q = 1` with `gcd(A, m) = 1` it says `D < 2^(A/2)`, i.e. `A·log 2 − m·log 3 < 2^(1−A/2)`; the irrationality measure of [`rhin-1987-irrationality-measure`](../../../sources/rhin-1987-irrationality-measure.md), as recorded, forbids that for `A ≥ 207` (`m ≥ 131`), and EXT-1 for `m ≥ 5,580`. For `e = 2, 3, 4` the primitive factor is `≈ 2^(A/2)`, `2^(2A/3)`, `2^(A/2)` and the conjecture still bites; for `e` with `φ(e)/e < 1/2` (`6 | e`, `10 | e`, …) it does not, and the algebraic factors, which also divide `C_w` at `q = 1`, would have to carry the argument.
- **Three mismatches by elimination: vacuous.** [`three-arc-intercept-elimination`](../attempts/three-arc-intercept-elimination/README.md) writes the rotation difference as two arc terms and shows the three cyclic relations have determinant `−Π(2^(d_r) − 1)·D`, the `s = 3` face of the Smith-form obstruction; a single relation gives only the run witness.
- **Exact cases.** Mechanical words (letters `1, 2` with coprime shift) have `G = 1` ([`mechanical-word-exact-denominator`](../results/mechanical-word-exact-denominator/README.md)); adjacent defects give `G | 2^k − 1` (two-defect node, part 5); the two-marker family gives `G = 2^(A/2) − 3^(m/2)` exactly; `1^t 2^(2t)` gives `G = gcd(4^t − 1, 3^t − 2^t) ≤ 3^t < 2^(A/2) = 2^(2.5t)` ([`fixed-defect-unbounded-cancellation`](../results/fixed-defect-unbounded-cancellation.md)).
- **Finite evidence** ([`few-arc-codings-denominator-census`](../results/few-arc-codings-denominator-census/README.md)): 493,483 census entries of primitive few-arc words (`s ≤ 4`, `m` up to 40, letters up to 8; a word is counted once per census), every one with `m ≥ 9` satisfies `G² < 2^A`; `log₂G − A/2 ≤ −2.81` for `s = 2`, `≤ −0.93` for `s = 3`, `≤ −0.06` for `s = 4`. The unique exception at `m ≤ 8` is the `3x+11` cycle `(1,1,2,2,1,1,3,3)`, `m = 8`, `G = 893`, `A = 14`. Finite evidence does not bear on large `m`.
- **Obstructions to the known routes for `s ≥ 3`:** [`coupled-defect-matrix-smith-form`](../results/coupled-defect-matrix-smith-form/README.md) (adjugate elimination is vacuous), [`three-defect-arbitrary-background`](../results/three-defect-arbitrary-background.md) (no fixed S-unit description), [`termwise-plateau-divisibility`](../attempts/termwise-plateau-divisibility.md).

## Suggested attacks

Proposals, not results.

- **Bound the gcd of two arc intercepts in the non-Sturmian case.** For `s = 2` everything reduces to `gcd(C_u, C_v)` for the two arcs between the mismatches. The Sturmian case is done (R71's descent, `G | 2^k − 1`; [`two-arc-word-rotation-structure`](../results/two-arc-word-rotation-structure/README.md)); the open case is a two-interval coding whose interval length differs from the step, where the arcs are long and their intercepts are nearly coprime in the data. A descent would have to use the induced rotation on an arc (Rauzy induction for two-interval codings), not the phase shift.
- **Three and four arcs.** The two-term relations are written out in [`three-arc-intercept-elimination`](../attempts/three-arc-intercept-elimination/README.md); elimination across them is vacuous and a single relation is the run witness. What is left is to use the relations together with the arcs' structure as stretches of a three-interval rotation coding, or to work modulo the cyclotomic factors of `D` directly.
- **Separate the algebraic part.** Done as data ([`algebraic-and-primitive-cancellation-census`](../results/algebraic-and-primitive-cancellation-census/README.md)): the primitive part is tiny, the algebraic part carries every large cancellation. The theorem to aim for is a bound on `g_prim = gcd(G, Φ_e(2^(A/e), 3^(m/e)))` for few-arc words, first for `gcd(A, m) = 1` where `g_prim = G`. Its heuristic truth is that `C_w mod p` is equidistributed for the primes `p | Φ_e`; a proof would need the arithmetic of `C_w` modulo primes `p` with `2^(A/e) ≡ ζ·3^(m/e) (mod p)` for a primitive `e`-th root of unity `ζ`.
- **Test adversarially** before proving: search for words with `s = 3, 4` and `gcd(A, m)` large (e.g. `A = 2m`, `A = 3m/2`) with symmetries exchanging arcs, the only mechanism that produced large `G` in the census.

## History

- Posed 2026-10-28 by the Claude cycles lane (Fable 5.1).
- 2026-10-28, later: the Sturmian two-arc case recorded as settled (it was already part 5 of the two-defect node), the algebraic/primitive decomposition and the sharper conjecture on `g_prim` added, the attack list corrected accordingly (Claude cycles lane, Fable 5.1).
