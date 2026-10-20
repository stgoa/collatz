---
id: one-height-defect-ordered-cycles
kind: question
title: Can an ordered 3x+1 cycle have exactly one state of height one?
status: open
claim: >
  Ordered odd-only cycles at q = 1 with one chronological height h_t = 1 and all other heights 0:
  legality forces c_(t−1) = 2, and reduced denominator 1 would require D | C_c − M_t/2, where C_c is
  the lower mechanical intercept of (A, m), M_t = 3^(m−1−t)·2^(P_t) and D = 2^A − 3^m. Decide, for all
  periods, whether a legal and actual profile can satisfy this congruence.
created: 2026-10-19
tags: [cycles, dyadic-order, one-defect]
---

# Can an ordered 3x+1 cycle have exactly one state of height one?

## Question

In the notation of [`ordered-cycle-sparse-forcing`](../results/ordered-cycle-sparse-forcing/README.md), take the general one-defect pattern: `h_t = 1` and all other heights zero. Then `a_(t−1) ≥ 1` requires `c_(t−1) = 2`, the weighted intercept is `C_h = C_c − M_t/2`, and the exact open denominator-1 subproblem is whether a **legal and actual** ordered profile can satisfy

```
D | C_c − M_t/2.
```

Excluding one-height defects for all periods would be a further intermediate result toward [`ordered-cycle-denominator-one`](ordered-cycle-denominator-one.md). The single-defect congruence is only a candidate route; a finite scan is not a proof of its failure.

## Why it matters

It is the simplest wide ordered profile, and the bounded first probe of whether the arithmetic of the weighted intercept can exclude `q = 1` across all periods. A legal defect can create genuine cancellation, though in the known control not all of `D`.

## Known progress

- The actual ordered `q = 233` one-defect cycle has `C_c = 14501`, `M_t/2 = 1152`, `C_h = 13349`, `D = 1631 = 7·233` and `gcd(C_h, D) = 7` ([`mechanical-normalized-word-transfer`](../attempts/mechanical-normalized-word-transfer.md)): cancellation occurs, so `gcd(C_c, D) = 1` alone gives no all-period exclusion.

## Suggested attacks

- Strengthen the gap law with exact height-jump locations, or find a legal-height congruence in the one-defect case, retaining all adjacent inequalities and excluding the `q = 1` zero-valuation relaxation (`4 → 13 → 5 → 4`, see [`ordered-cycle-shortcuts`](../attempts/ordered-cycle-shortcuts.md)). (Legacy C006 suggestion.)

## History

- Stated in `experiments/cycle_spectrum/C006/ORDER_RIGIDITY.md` §§4, 6 and `C006/REPORT.md` (legacy ID `C006`), and in `C007/INDEPENDENT_ARITHMETIC.md`; recorded as a node by the B03 migration (Claude, Opus 5.5) at commit `be73a66`.
