---
id: occupation-measure-tightness
kind: question
title: Does at least half the logarithmic seed mass spend its time in a bounded set?
status: open
claim: >
  Odd-only 3x+1 map S on positive odd integers with S(1) = 1, time counted in odd arrows. For a seed n let
  m_(n,T) = T^(-1) sum_(j<T) delta_(S^j(n)) be its empirical occupation measure, and mu_X the logarithmic law on odd
  seeds up to X (mu_X(n) proportional to 1/n). Prove
  lim_(K -> infinity) liminf_(X -> infinity) liminf_(T -> infinity) E_(n ~ mu_X)[ m_(n,T)([1, K]) ] >= 1/2,
  i.e. at least half the asymptotic logarithmic seed mass ends in finite cycles. Weaker than absorption: it allows
  other cycles and a remaining divergent basin, and it is not supplied by almost-bounded-minimum theorems.
created: 2026-10-18
aliases: [VP-V11]
tags: [invariants, viewpoints, occupation-measures, tightness, density, open]
---

# Does at least half the logarithmic seed mass spend its time in a bounded set?

## Question

As in the claim: the "partial milestone" of viewpoint card V11 (occupation measures; [`statistical_languages.md`](../attempts/viewpoint-language-survey/statistical_languages.md) §V11). The order of limits matters: an argument that obtains a finite `K` only after fixing `X`, or exchanges the limits without a uniform estimate, does not prove it, and a limiting probability must not simply discard the escape mass.

## Why it matters

The card's structural gain: every orbit either enters a finite cycle (its empirical law tends to the uniform law on the cycle) or has no repeated state (its empirical mass on every finite set tends to 0), so the countably additive invariant probability measures are mixtures of cycle laws (compare Assani, arXiv:2208.11675v2, Theorem 3.1, for the shortcut clock). Occupation measures thus separate **cycle mass** from **escape of mass**: the stationarity defect `(δ_(S^T(n)) − δ_n)/T` tends to 0 without ensuring tightness, and all mass may escape. A positive answer would put at least half of the logarithmic mass into finite cycles. Tightness addresses divergence only; identifying the cycle stays separate (the `3x+5` cycle `19 → 31 → 49` gives a perfectly tight invariant law that never reaches 1).

## Known progress

None. The survey kept V11 as a diagnostic only, "until a quantitative mechanism is proposed" ([`viewpoint-language-survey`](../attempts/viewpoint-language-survey/README.md)). The side lane's verdict: it relocates the obstacle to tightness uniform in the range of seeds, i.e. to uniform control of the non-absorbed set (referee sheet, feed 18:24). Density results for the nonabsorbing set itself are all-or-nothing ([`nonabsorbing-set-linear-lower-density`](../../convergence/results/nonabsorbing-set-linear-lower-density/README.md)); this question concerns where time is spent, not membership.

## Suggested attacks

The card's cheapest test: write an attempted tightness bound with the exact orders of `X`, `T` and `K`, and check that it neither exchanges limits nor discards escape mass. No uniform tightness estimate is currently identified. (Speculation-free: nothing beyond the card is proposed here.)

## History

- New node by the B16 migration (Claude, Opus 5.5) from the V11 card in `experiments/viewpoints/V002/statistical_languages.md` (legacy ID V002; card V11 of the viewpoint map) at commit `be73a66`. Main lane (ChatGPT/Codex), 2026-10-18.
