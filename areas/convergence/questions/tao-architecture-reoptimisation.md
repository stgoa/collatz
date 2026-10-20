---
id: tao-architecture-reoptimisation
kind: question
title: Can re-optimised parameters bring Tao's architecture down to the verified range?
status: open
claim: >
  In Tao's argument (arXiv 1909.03562v7, Sections 5-7), the exponents 0.6, 0.7, 0.8 and 0.1 of log x, the divisor
  100 in m_0 = floor((alpha-1) log x/100), alpha (printed 1.001), and the constants C_A and epsilon are free
  choices. Is there a choice for which the argument, with every constant explicit, is non-vacuous at log x of the
  order of the verified range (x = 2^71, log x < 50; the lane used 2^68, log x = 47.1), and so certifies some
  C(delta) <= 2^71 with delta < 1? Candidate answer (heuristic, the explicit-Tao lane): no; the vacuity threshold
  is not expected below log x ~ 10^3, probably not below 10^5.
created: 2026-10-18
tags: [convergence, explicit-tao, tao, mixing, barrier, heuristic]
---

# Can re-optimised parameters bring Tao's architecture down to the verified range?

## Question

With its printed parameters, Tao's first-passage window is empty unless `log x > 6.27·10^13` and the 3-adic level `m_0` is 0 unless `log x >= 10^5` ([`tao-printed-window-vacuity`](../results/tao-printed-window-vacuity/README.md)). The exponents `0.6, 0.7, 0.8, 0.1`, the divisor `100` in `m_0`, and `α` are all free choices made for asymptotics. Is there any choice inside the same architecture (first passage between scales `x, x^α, x^(α²), …`, 3-adic mixing at level `m_0`, Chernoff windows, `log^(−c) x` errors) that is non-vacuous at the verified scale? Proving "no" would need to formalise "the architecture" as a parametrised family; that was not attempted.

## Why it matters

A "no" would close every explicit-Tao route that keeps Tao's architecture, and leave only structurally different, fixed-scale arguments for [`explicit-almost-all-descent-threshold`](explicit-almost-all-descent-threshold.md). A "yes" would reopen the explicit-constant programme ([`explicit-tao-almost-all-constants`](../attempts/explicit-tao-almost-all-constants.md)) at its legacy L4–L6.

## Known progress

**The lane's assessment (heuristic, candidate, not proved).** Shrinking the free parameters runs into the reason they were chosen:
- the Chernoff window must dominate the fluctuation of `a_[1,n]` over the `(α²−1) log x / log(4/3)` steps between the scales;
- the 3-adic level `m_0` must be large enough that the `m^(−A)` mixing bound is small with a `C_A`-sized deviation allowance;
- the `log^(−c) x` errors must be summable over the chain of scales `x, x^α, x^(α²), …` down to the target.

At `log x = 47` there are fewer than 200 Syracuse steps between any two scales of interest, and a deviation allowance of order `C_A(√(n log n) + log n)` already exceeds `2n` for moderate `C_A`. The lane's assessment was that no choice of these parameters brings the vacuity threshold below `log x ~ 10^3`, i.e. `x ~ 2^1500`, and probably not below `10^5`; the side lane's independent estimate is `log x` of order `10^12` for the union bound (5.12) as written. Either way the target is out of reach by orders of magnitude in the exponent. These numbers are estimates, not computed results.

Two data points are computed: opening the window alone at `x = 2^68` needs `α ≈ 1.22` (receipt of [`tao-printed-window-vacuity`](../results/tao-printed-window-vacuity/README.md)), and whether the Section 5 estimates survive such an `α` was not examined; the `m_0 = 0` obstruction is independent of `α` at that scale unless `α` is far larger (the side lane's first-pass trace: `α > 3.1`).

## Suggested attacks

- Parametrise Section 5 (the windows (5.9)–(5.12), (5.16), (5.20)) with symbolic exponents and `α`, and compute the smallest `log x` at which all constraints can hold simultaneously, before any implied constant is traced. That would turn the candidate into a finite certificate for that parametrised family.
- Look for a different first-passage bookkeeping (a direct dyadic-block version) whose windows are not powers of `log x`. Speculative.
