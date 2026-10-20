---
id: explicit-tao-almost-all-constants
kind: attempt
title: Making Tao's almost-all theorem explicit enough to meet the verified range
status: written
claim: >
  Tried (Claude explicit-Tao lane, 2026-10-18, Leg 1): make Tao (2019) explicit, i.e. compute C(delta) such that
  all but logarithmic density delta of positive integers have a Collatz orbit dipping below C(delta), and compare
  it with the verified range (2^68 in the lane's figure). Verdict: closed at a scoped barrier. Explicit one-round
  descent is proved (explicit-valuation-large-deviations, explicit-one-round-descent), but Tao's argument with its
  printed parameters is vacuous below log x ≈ 6.27·10^13 (tao-printed-window-vacuity), and the machine-checked
  explicit mixing constants need 3-adic levels >= 2^80000 (explicit-tao-via-formal-mixing-constants); no C(delta)
  at or below the verified range came out for any delta < 1. Whether re-optimised parameters could help is open,
  with a heuristic "no" (tao-architecture-reoptimisation). The renewal transfer, the iteration across scales
  (legacy L5, L6) and the lane's Legs 2 and 3 were not started.
authors:
  - Claude explicit-Tao lane (Opus)
created: 2026-10-18
depends_on: [explicit-valuation-large-deviations, explicit-one-round-descent, tao-printed-window-vacuity, nonabsorbing-set-linear-lower-density]
assumes: [tao-2019-almost-all, lau-2026-positive-density]
tags: [convergence, explicit-tao, tao, mixing, barrier, explicit-constants, programme]
---

# Making Tao's almost-all theorem explicit enough to meet the verified range

## Idea

**Goal.** Make Tao (2019) ([`tao-2019-almost-all`](../../../sources/tao-2019-almost-all.md), arXiv 1909.03562, corrected v7) explicit: compute `C(δ)` such that all but logarithmic density `δ` of positive integers have an orbit dipping below `C(δ)`, tabulate it for `δ ∈ {0.9, 0.5, 0.1, 0.01}`, and compare it with the verified range `V`. Tao proves: for every `f → ∞`, `Col_min(N) < f(N)` for log-almost all `N`. The gap between "`f → ∞`" and "`f = V`" is the whole conjecture. Any `δ < 1` with `C(δ) <= V` would be a new theorem: an explicit proportion `1 − δ` of integers (in logarithmic density) reach 1. The target is the open question [`explicit-almost-all-descent-threshold`](../questions/explicit-almost-all-descent-threshold.md).

**Why it looked worth doing.** The machine-checked positive-density theorem ([`lau-2026-positive-density`](../../../sources/lau-2026-positive-density.md)) gives, through [`nonabsorbing-set-linear-lower-density`](../results/nonabsorbing-set-linear-lower-density/README.md), that a nonempty bad set `B` has positive lower density, hence (Abel summation) positive lower logarithmic density. So Collatz ⇔ `B` has logarithmic density 0 ⇔ log-almost all orbits dip below the verified range. The lane took this as the sharpest honest form of the remaining problem, and an explicit Tao as the natural attack on it.

**Lemma decomposition** (legacy IDs, aliased `TAO-L1` … `TAO-L6` in this repository; Phase 6's literature audits L1–L5 are unrelated):

| Lemma | Content | Outcome | Transfer to `3x+d` |
|---|---|---|---|
| L1 | Exact valuation cylinders: the first `n` Syracuse valuations are determined by `N mod 2^(A+1)`, each word one odd class | recalled with proof in [`explicit-valuation-large-deviations`](../results/explicit-valuation-large-deviations/README.md) (frozen S.1; Terras 1976) | transfers |
| L2 | Explicit large deviations for `A`: Chernoff with exact rate `I(θ)`; integer counts with boundary error `C(⌊θn⌋, n)` | [`explicit-valuation-large-deviations`](../results/explicit-valuation-large-deviations/README.md), written, with a finite certificate | transfers (checked for `d = 5`) |
| L3 | One-round explicit descent: outside an explicit exceptional count, `S^n(N) < N(3/2^θ)^n + (3/2)^n` | [`explicit-one-round-descent`](../results/explicit-one-round-descent.md), written | transfers (additive term times `d`) |
| L4 | Mixing of the Syracuse random variables `Syrac(Z/3^n)` (Tao Prop. 1.17, §§3–4) with explicit constants: the crux | part 0: [`explicit-tao-via-formal-mixing-constants`](explicit-tao-via-formal-mixing-constants.md); part 1: [`tao-printed-window-vacuity`](../results/tao-printed-window-vacuity/README.md) | model statement, `d`-blind |
| L5 | Renewal / first-passage transfer from the random model to actual integers with explicit error (Tao §§5–6) | not started | transfers |
| L6 | Iteration across scales in logarithmic density, summable explicit errors; assembly of `C(δ)` | not started | transfers |
| L7 | Verified range: every `N <= V` reaches 1 (published computation, not re-run here; now [`barina-2025-convergence-2-71`](../../../sources/barina-2025-convergence-2-71.md)) | input | **`d`-specific** (false for `d = 5`: 19 → 31 → 49) |

## What happened

The lane ran two iterations on 2026-10-18, on branch `claude/explicit-tao`, with the side lane reviewing.

- **Iteration 1: L2 + L3.** Written proofs of the explicit valuation large-deviation bound with exact rate `I(θ) = θ log(2(θ−1)/θ) − log(θ−1)`, exact integer counting with boundary error `C(⌊θn⌋, n)`, and the one-round descent off the exceptional set, with the checker `check_L2.py`. The first draft of L3 stated the multiplicative form `S^n(N) <= 3^n(N+1)/2^A`; the checker's exact test rejected it (word `(10,1)`: `C_w = 1027 > 9`) and the additive Terras form replaced it before any commit. The side lane confirmed L2, L2′ and L3 by independent code and found four hand-quoted `I(θ)` values misprinted; they were corrected from the receipt.
- **Iteration 1, lead from the side lane.** The audited AxiomMath library already contains a machine-checked explicit mixing estimate. Reading it showed mixing only for 3-adic levels `m >= 2^80000`, so any `C(δ)` from it is `>~ 3^(2^80000)`: [`explicit-tao-via-formal-mixing-constants`](explicit-tao-via-formal-mixing-constants.md). This sharpened L4 into a numeric question about Tao's own exponent in `exp(δ^(−O(1)))`.
- **Iteration 2: Tao's architecture at the verified scale.** The lane verified the side lane's trace of v7 against the arXiv HTML (Theorem 3.1 with `c` never numerical, `α = 1.001`, `n_0`, `m_0`, the windows (5.9)–(5.12), (5.16), (5.20), the Section 6 and 7 constants) and computed that the first-passage window is empty unless `log x > 6.27·10^13`, and `m_0 = 0` unless `log x >= 10^5`: [`tao-printed-window-vacuity`](../results/tao-printed-window-vacuity/README.md). The side lane reproduced every number in 50-digit arithmetic and agreed with the labels.
- **Post-mortem.** Written at iteration 2 because the evidence was decisive, not because the lane's stop rule (three iterations without a new explicit constant or proved lemma) had fired.

The `C(δ)` table at closure:

| δ | `C(δ)` | Status |
|---|---|---|
| 0.9, 0.5, 0.1, 0.01 | none | open |
| `1 − 2^(−2^(2^87640))` | `1` (reaches 1), natural density, `N >= 2^2^2^2^87640` | machine-checked (`Main.positive_density_collatz_reaches_one` of the external library); calibration only, useless for the target |

Lower bounds on what the available methods can give (not upper-bound theorems): the AxiomMath mixing lemma, no `C(δ)` below about `3^(2^80000)` for any `δ`; Tao's architecture with its printed parameters, no `C(δ)` below `exp(6.27·10^13)` for any `δ`. The verified range `2^68 = e^47` is unreachable by both.

## Why it fails

Two independent readings of v7 (this lane and the side lane) agree on the printed parameter choices: the auxiliary scales of the proof are powers of `log x`. The first-passage window has half-width `log^0.8 x` around a centre that moves by only `(α−1) log x / log(4/3)` with `α = 1.001`, the 3-adic level is `m_0 = ⌊(α−1) log x / 100⌋`, and the union bound needs `exp(−c log^0.2 x) <= log^(−10) x`. At the verified range `log x = 47`. So, as written, the method certifies no `C(δ) < exp(6 × 10^13)` for any `δ < 1`; the constants `c`, `C_A`, `ε` (none of which the paper gives numerically) never enter. The machine-checked variant is worse still (`m >= 2^80000`). Re-optimising the free parameters inside the same architecture is judged unable to bring the vacuity threshold within many orders of magnitude of `log x = 47`; that judgement is a heuristic candidate, recorded as [`tao-architecture-reoptimisation`](../questions/tao-architecture-reoptimisation.md).

Explicit one-round descent is cheap and exact; iteration is what fails, and it fails for architectural reasons at fixed scale. A fixed-scale version would need mixing statements with no `log x`-sized auxiliary windows. None is known; this is the precise research gap, and it is not a constants problem.

## What survives

1. [`explicit-valuation-large-deviations`](../results/explicit-valuation-large-deviations/README.md) and [`explicit-one-round-descent`](../results/explicit-one-round-descent.md): explicit one-round statements at scale `X` with exceptional fraction `e^(−n I(θ)) + 2 C(⌊θn⌋,n)/X` and descent factor `(3/2^θ)^n`, every constant explicit, for every odd `d`.
2. The reformulation: with the positive-density theorem machine-checked, Collatz ⇔ `B` has logarithmic density 0 ⇔ log-almost all orbits dip below the verified range ([`nonabsorbing-set-linear-lower-density`](../results/nonabsorbing-set-linear-lower-density/README.md); the target is [`explicit-almost-all-descent-threshold`](../questions/explicit-almost-all-descent-threshold.md)).
3. The `d`-specific step of any such proof is the verified range itself (L7); everything else in the averaging toolbox is `d`-blind.
4. [`tao-printed-window-vacuity`](../results/tao-printed-window-vacuity/README.md): the quantitative reason why an explicit version of the existing almost-all theorem does not meet the verified range.

**Not started.** L5–L6. Leg 2 (a density dichotomy for the invariant bad set `B` inside Tao's framework; planned as one bounded unit stating what the dichotomy already gives and what its converse, density 0 ⇒ empty, would require; the side lane noted that this converse is the whole problem). Leg 3 (extending `m`-cycle exclusion beyond Hercher's bound, [`hercher-2023-cycle-length`](../../../sources/hercher-2023-cycle-length.md), by Baker-type bounds and computation; the side lane advised reading Hercher's corrigendum of 14 June 2026 first). The legacy index of 2026-10-19 marks the whole line closed.

## History

- Migrated from `experiments/explicit_tao/README.md` (the line's index, "closed; Leg 1 ended at a scoped barrier", 2026-10-18) at commit `be73a66`. The lane journals `experiments/explicit_tao/STATE.md` (goal logic, lemma table, post-mortem, `C(δ)` table, blockers, legs, rules) and `experiments/explicit_tao/LOG.md` (iteration log, newest first) are absorbed here and archived unchanged in [`archive/convergence-explicit-tao/`](../../../archive/convergence-explicit-tao/STATE.md).
- Written by the Claude explicit-Tao lane (branch `claude/explicit-tao`), 2026-10-18, with reviews by the side lane (feed 2026-10-18 19:36, 19:39, 19:44, 19:50).
- The lane wrote `V = 2^68` "per the published Barina verification, to be cited exactly before use". The repository's input is now `2^71` ([`barina-2025-convergence-2-71`](../../../sources/barina-2025-convergence-2-71.md)); no conclusion here changes.
