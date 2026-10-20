---
id: linear-growth-short-detection
kind: result
title: Linear joint section growth forces every nonzero combination of depth-A sections to be detected within O(sqrt(A)) digits
status: reviewed
claim: >
  For a real-valued sequence s on n >= 0 let J_D(s) be its sections s(2^a 3^b n + r) with a + b <= D,
  0 <= r < 2^a 3^b, and W_D(s) their real span. (a) If 0 != g in W_A(s) first becomes nonzero at an input
  N >= 9^L, then dim W_(A+L)(s) >= (L+1)(L+2)/2. (b) Hence if |J_D(s)| <= C(D+1) for every D (fixed C >= 1), every
  nonzero g in W_A(s) is nonzero at some input below 9^L with L = ceil(2C + sqrt(2C(A+1)) + 1), i.e. within
  O_C(sqrt(A+1)) binary or ternary digits; evaluation on that prefix is injective on W_A(s). Generic theorem about
  sequences: no Collatz identity, no Cobham.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
evidence:
  - "additive-section-excess-unbounded/global_growth.md: the written theorem (sections 1-3), the route to the full goal (section 4), why dimension counting does not supply the delay (section 5), the calibration against the digit-count result (section 6.2); additive-section-excess-unbounded/GLOBAL_REVIEW.md: main-lane independent review"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    scope: "Feed 23:36: the global detection bound checked (first nonzero indices floor(N/m) distinct since N >= mm', the (L+1)(L+2)/2 triangular independent sections inside W_(A+L), the contradiction once L > C + sqrt(C^2 + 2C(A+1)), satisfied by the stated L); elementary and generic, no Cobham"
    link: ../../../archive/side-lane/FEED.md
  - by: Claude Lean lane (Fable)
    date: 2026-10-18
    scope: "Iteration 10: global_growth.md read in full (the floors floor(N/m), mm' < 9^L, the triangular independence, the explicit L-hat, the rank-plateau argument and the section 6.2 recurrence); no gap"
aliases: [V009-b]
tags: [invariants, section-growth, quantitative-rigidity, linear-algebra]
---

# Linear joint section growth forces every nonzero combination of depth-A sections to be detected within O(sqrt(A)) digits

## Statement

For a real-valued sequence `s` on `n ≥ 0` (a finite colour set may be encoded injectively by reals; this preserves which entire sections are equal) put

```
J_D(s) = {n ↦ s(2^a 3^b n + r) : a, b ≥ 0, a + b ≤ D, 0 ≤ r < 2^a 3^b},
W_D(s) = span_R J_D(s),     d_D(s) = dim W_D(s),     nu(g) = min{n ≥ 0 : g(n) ≠ 0}.
```

**(a) Lemma.** If `0 ≠ g ∈ W_A(s)` and `nu(g) ≥ 9^L`, then `d_(A+L)(s) ≥ (L+1)(L+2)/2`.

**(b) Detection bound.** If `|J_D(s)| ≤ C(D+1)` for every `D ≥ 0`, then every nonzero `g ∈ W_A(s)` has `nu(g) < 9^L` with `L = L_C(A) = min{L ≥ 0 : (L+1)(L+2)/2 > C(A+L+1)}`, and `L_C(A) ≤ ⌈2C + √(2C(A+1)) + 1⌉`. So evaluation on the first `9^L` inputs is injective on `W_A(s)`, and any two distinct states of `J_A(s)` are distinguished by an input with at most `2L` ternary or `⌈L log₂ 9⌉` binary digits.

## Proof

From [`global_growth.md`](additive-section-excess-unbounded/global_growth.md) §§2–3. (a): with `N = nu(g)`, for each `m = 2^a 3^b`, `a + b ≤ L`, put `r_m = N mod m` and `g_m(n) = g(mn + r_m)`; then `nu(g_m) = ⌊N/m⌋`. Distinct multipliers `m, m' ≤ 3^L` have `mm' < 9^L ≤ N`, so `|N/m − N/m'| > 1` and the first nonzero indices are distinct. Each `g_m` lies in `W_(A+L)(s)` (a state `s(Mn + t)` of `J_A` has `m`-section `s(Mm n + M r_m + t)` with `0 ≤ M r_m + t < Mm`). Sequences with distinct first nonzero indices are linearly independent (triangular order), and there are `(L+1)(L+2)/2` pairs. (b): otherwise (a) would give `(L+1)(L+2)/2 ≤ d_(A+L) ≤ |J_(A+L)| ≤ C(A+L+1)`, contrary to the choice of `L`; for the explicit cutoff put `x = √(2C(A+1))`, so `L̂ ≥ 2C + x + 1` and `L̂²/2 − C L̂ ≥ (2C + x + 1)(x + 1)/2 > x²/2 = C(A+1)`, while `(L+1)(L+2)/2 ≥ L²/2`. ∎

## Remarks

- **The route it opens** (`global_growth.md` §4): construct nonzero `g_j ∈ W_(A_j)(b)`, `b(n) = h(2n+1)`, with `log(nu(g_j))/√(A_j + 1)` unbounded. Their independent mixed sections would force an unbounded joint ratio, and then an unbounded binary ratio through the depth conversion of [`automatic-section-forces-constancy`](automatic-section-forces-constancy/README.md), i.e. the quantitative goal [`section-count-depth-ratio-unbounded`](../questions/section-count-depth-ratio-unbounded/README.md). The missing step is to produce such delays from arbitrary nonconstancy and the full Collatz identities; no construction is supplied. A formally cancelled expression that is identically zero is not a witness.
- **Why it is not already a contradiction** (§5): an infinite finite-alphabet joint kernel has strictly increasing span dimension (a rank plateau would close a finite-dimensional span under all section maps), so `dim W_A ≥ A + 1`; that rank count alone gives a nonzero combination vanishing on only `A` initial inputs, while the detection bound permits zero prefixes exponential in `√A`. An additional arithmetic mechanism is essential. The calibration of §6.2 recovers the digit-count quadratic phenomenon ([`digit-count-section-forces-quadratic-growth`](digit-count-section-forces-quadratic-growth.md)) by constructing exponentially delayed combinations; it does not assume every invariant has such a section.
- Novelty: none claimed.

## History

- New node by the B16 migration (Claude, Opus 5.5) from `experiments/viewpoints/V009/global_growth.md` and the V009 report §§1–2 (legacy ID V009) at commit `be73a66`; the note stays in [`additive-section-excess-unbounded`](additive-section-excess-unbounded/README.md)'s folder.
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `4be9bae`.
