---
id: explicit-almost-all-descent-threshold
kind: question
title: An explicit almost-all descent threshold C(δ) at or below the verified range
status: open
claim: >
  Ordinary Collatz map (or, equivalently for this purpose, the odd-only clock on odd N). For delta in (0,1), find an
  explicit C(delta) such that all but logarithmic density delta of positive integers N have an orbit whose minimum
  is below C(delta), as Tao's theorem gives with C(delta) << exp(delta^(-O(1))) and unspecified constants. Target:
  some delta < 1 with C(delta) <= V, the verified range (2^71, barina-2025-convergence-2-71; the explicit-Tao lane
  used 2^68); that would prove that an explicit proportion 1 - delta of integers, in logarithmic density, reach 1.
  Tabulated targets delta in {0.9, 0.5, 0.1, 0.01}, all open.
created: 2026-10-18
aliases: [TAO-L5, TAO-L6]
tags: [convergence, explicit-tao, tao, density, explicit-constants, frontier]
---

# An explicit almost-all descent threshold C(δ) at or below the verified range

## Question

Find an explicit function `C(δ)` with: all but logarithmic density `δ` of positive integers have an orbit dipping below `C(δ)`. [`tao-2019-almost-all`](../../../sources/tao-2019-almost-all.md) (Theorems 1.3 and 1.6, Remark 1.4) gives such a statement for every `f → ∞` and a constant `C_δ << exp(δ^(−O(1)))`, with no numerical constants. The target is a `δ < 1` with `C(δ) <= V`, where `V` is the verified range ([`barina-2025-convergence-2-71`](../../../sources/barina-2025-convergence-2-71.md)): every `N <= V` reaches 1, so every orbit that dips below `V` reaches 1.

The explicit-Tao lane split the work into lemmas L1–L7; this question carries the aliases of the two it never started: **L5** (renewal / first-passage transfer from the random model to actual integers with explicit error, Tao §§5–6) and **L6** (iteration across scales in logarithmic density with summable explicit errors, and the assembly of `C(δ)`).

## Why it matters

- **A new theorem at any `δ < 1`.** `C(δ) <= V` would give an explicit proportion of integers that reach 1, which no current method gives.
- **The sharpest form of the remaining problem.** By [`nonabsorbing-set-linear-lower-density`](../results/nonabsorbing-set-linear-lower-density/README.md) (assuming [`lau-2026-positive-density`](../../../sources/lau-2026-positive-density.md)), a nonempty bad set has positive lower density, hence positive lower logarithmic density. So `C(δ) <= V` for **every** `δ > 0` would be equivalent to Collatz; the lane read this as "Collatz ⇔ the bad set has logarithmic density 0 ⇔ log-almost all orbits dip below the verified range". The statistical counterpart without explicit thresholds is [`nonabsorbed-fraction-arbitrarily-small`](nonabsorbed-fraction-arbitrarily-small.md).
- **`d`-control.** Every averaging step is `d`-blind; the only `d`-specific input is the verified range (false for `3x+5`, where 19 → 31 → 49 does not reach 1), as it must be.

## Known progress

- **Explicit one-round statements**, every constant explicit: [`explicit-valuation-large-deviations`](../results/explicit-valuation-large-deviations/README.md) (legacy L1, L2, L2′) and [`explicit-one-round-descent`](../results/explicit-one-round-descent/README.md) (L3). They do not iterate.
- **Method lower bounds, not upper-bound theorems.**
  - Tao's argument with its printed parameters is vacuous below `log x ≈ 6.27·10^13`, so it certifies no `C(δ)` below `exp(6.27·10^13)` for any `δ`: [`tao-printed-window-vacuity`](../results/tao-printed-window-vacuity/README.md).
  - The machine-checked explicit mixing constants need 3-adic levels `>= 2^80000`, so any `C(δ)` from them is at least of the order of `3^(2^80000)`; that route contributes only `C = 1` at natural density `1 − 2^(−2^(2^87640))`: [`explicit-tao-via-formal-mixing-constants`](../attempts/explicit-tao-via-formal-mixing-constants.md).
- **The programme as a whole** stopped at that scoped barrier: [`explicit-tao-almost-all-constants`](../attempts/explicit-tao-almost-all-constants.md).
- Before the barrier, the lane's numeric target for Tao's exponent was below about 5.6 at `δ = 1/2` and below about 36 at `δ = 0.9` (for `exp(δ^(−O(1))) <= e^47`); the barrier makes that exponent irrelevant at the verified scale.

## Suggested attacks

- **Fixed-scale mixing (the research gap).** A proof at the verified scale would need mixing statements for the Syracuse random variables with no `log x`-sized auxiliary windows. None is known; this is not a constants problem. Speculative.
- **Re-optimising Tao's free parameters** is the narrower open question [`tao-architecture-reoptimisation`](tao-architecture-reoptimisation.md); the lane's heuristic answer is no.
- **Bookkeeping** (the lane's open choice): which first-passage / log-density formulation, Tao's or a direct dyadic-block version, gives the cleanest explicit error accumulation in L6. Before deriving anything, search the literature for an existing explicit version of Tao's constants (none was known to the lane).
