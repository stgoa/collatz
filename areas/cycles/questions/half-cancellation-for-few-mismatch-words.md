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
- **Exact cases.** Mechanical words (letters `1, 2` with coprime shift) have `G = 1` ([`mechanical-word-exact-denominator`](../results/mechanical-word-exact-denominator/README.md)); adjacent defects give `G | 2^k − 1` (two-defect node, part 5); the two-marker family gives `G = 2^(A/2) − 3^(m/2)` exactly; `1^t 2^(2t)` gives `G = gcd(4^t − 1, 3^t − 2^t) ≤ 3^t < 2^(A/2) = 2^(2.5t)` ([`fixed-defect-unbounded-cancellation`](../results/fixed-defect-unbounded-cancellation.md)).
- **Finite evidence** ([`few-arc-codings-denominator-census`](../results/few-arc-codings-denominator-census/README.md)): 493,483 census entries of primitive few-arc words (`s ≤ 4`, `m` up to 40, letters up to 8; a word is counted once per census), every one with `m ≥ 9` satisfies `G² < 2^A`; `log₂G − A/2 ≤ −2.81` for `s = 2`, `≤ −0.93` for `s = 3`, `≤ −0.06` for `s = 4`. The unique exception at `m ≤ 8` is the `3x+11` cycle `(1,1,2,2,1,1,3,3)`, `m = 8`, `G = 893`, `A = 14`. Finite evidence does not bear on large `m`.
- **Obstructions to the known routes for `s ≥ 3`:** [`coupled-defect-matrix-smith-form`](../results/coupled-defect-matrix-smith-form/README.md) (adjugate elimination is vacuous), [`three-defect-arbitrary-background`](../results/three-defect-arbitrary-background.md) (no fixed S-unit description), [`termwise-plateau-divisibility`](../attempts/termwise-plateau-divisibility.md).

## Suggested attacks

Proposals, not results.

- **Bound the gcd of two arc intercepts.** For `s = 2` everything reduces to `gcd(C_u, C_v)` for the complementary Sturmian arcs `u, v`. The one-letter-cut method that gives `G = 1` for mechanical words ([`mechanical-word-exact-denominator`](../results/mechanical-word-exact-denominator/README.md)) is a Euclidean descent on the word; try to run it on a two-letter Sturmian word with letters `a, a + k` and see what divisor of `2^k − 1` and which algebraic factors of `D` can survive.
- **Three and four arcs.** With mismatches `e_1 < e_2 < e_3`, the rotation difference is `C_(w′) − C_w = (2^(d_1) − 1)·3^(x)·2^(y)·C_α + (2^(d_1+d_2) − 1)·3^(x′)·2^(y′)·C_β`, a sum of two arc terms (`α, β` the arcs between consecutive mismatches, `d_r` the signed letter differences), so `G` divides a two-term S-unit combination of arc intercepts, cyclically in three ways. Look for a size argument on one such relation when one arc is short, and for an algebraic argument when `gcd(A, m) = 1`.
- **Separate the algebraic part.** Write `G = G_alg·G_rest` with `G_alg` supported on the algebraic factors `Φ_d(2^(A/e), 3^(m/e))` of `D`. Prove `G_rest` small first; then show that when `gcd(A, m)` is small the algebraic part is small, which is the near-critical case needed at `q = 1`.
- **Test adversarially** before proving: search for words with `s = 3, 4` and `gcd(A, m)` large (e.g. `A = 2m`, `A = 3m/2`) with symmetries exchanging arcs, the only mechanism that produced large `G` in the census.
