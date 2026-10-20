---
id: ordered-cycle-height-change-growth
kind: result
title: "Ordered cycles: bounded q and J leave finitely many, and J ≥ √m − O_q(log m)"
status: reviewed
claim: >
  Raw odd-only map, ordered primitive cycles with q ≤ L and m > 1, notation of the sparse-forcing law.
  Assuming the effective two-logarithm bound δ = A·log 2 − m·log 3 ≥ c_0·m^(−K_0) (Bugeaud, Theorem
  1.1(1.2), with effective absolute c_0, K_0 > 0): m/J < B + 1 + log₂(q/(3c_0)) + (K_0 + 1)·log₂ m
  and, using J ≥ B + 1, m/J < J + log₂(q/(3c_0)) + (K_0 + 1)·log₂ m. Hence fixed upper bounds on q
  and J leave only finitely many such cycles, effectively in principle, with no separate height
  bound; at fixed q, J ≥ √m − O_q(log m); at fixed q and B, J = Ω(m/log m). This restricts the
  complexity of an ordered cycle; it excludes no denominator-one cycle and gives no usable cutoff.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [ordered-cycle-sparse-forcing]
assumes: [bugeaud-2022-two-logarithms]
lean:
  - LeanLane.Cyc.OrdCycle.G2_of_gap
  - LeanLane.Cyc.OrdCycle.G2_of_gap_collatz
evidence:
  - "../ordered-cycle-sparse-forcing/ORDER_RIGIDITY.md, section 3 ((G2), height-free corollary (G5)): the written proof"
  - "../ordered-cycle-sparse-forcing/LITERATURE.md: the inspected statement of the two-logarithm input"
  - "../ordered-cycle-sparse-forcing/c006d_g2_check.py: side-lane check of the conditional Lean form on actual ordered cycles (does not run at its new path; see that node)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 2026-10-19 02:13, update 02:19: C006 re-derived by hand with no error; the imported Bugeaud corollary was not checked at the source. Lean unit C006-d verified (2026-10-19, iteration 52): (G2) with the linear-form gap as an explicit hypothesis"
    link: ../../../archive/side-lane/FEED.md
  - by: Claude side lane (Opus)
    date: 2026-10-19
    scope: "Feed 02:13, REFEREE C005 + C006: C006 assessed as restricting complexity, not excluding cycles; with Baker's two-logarithm bound an ordered cycle at fixed q needs J >= √m − O_q(log m)"
    link: ../../../archive/side-lane/FEED.md
tags: [cycles, dyadic-order, linear-forms, complexity, conditional]
---

# Ordered cycles: bounded q and J leave finitely many, and J ≥ √m − O_q(log m)

## Statement

Notation of [`ordered-cycle-sparse-forcing`](ordered-cycle-sparse-forcing/README.md): an ordered primitive cycle with `m > 1`, `q ≤ L`, total `A`, `δ = A·log 2 − m·log 3 > 0`, maximum height `B`, and `J` one plus the sorted height changes.

**Input.** Bugeaud's effective two-logarithm bound ([`bugeaud-2022-two-logarithms`](../../../sources/bugeaud-2022-two-logarithms.md)), applied to `2, 3` with coefficients `(A, −m)` over ℚ: since for an ordered cycle `A = m + s < 2m`, there are effective absolute constants `c_0, K_0 > 0` with `δ ≥ c_0·m^(−K_0)`. No numerical constant is claimed.

**Consequences.**

```
q > (3c_0/m^(K_0+1))·2^(ceil(m/J) − 1 − B),
m/J < B + 1 + log₂(q/(3c_0)) + (K_0 + 1)·log₂ m,                (G2)
m/J < J + log₂(q/(3c_0)) + (K_0 + 1)·log₂ m.                     (G5)
```

- For fixed upper bounds `q ≤ Q`, `J ≤ J_0` only finitely many ordered cycles remain, effectively in principle, with no separate height bound: (G5) bounds `m`, then `A < 2m` leaves finitely many positive valuation words, each with one rational cycle.
- At fixed `q`, (G5) gives `m < J² + O_q(J·log m)`, so `J ≥ √m − O_q(log m)`; in particular `J = Ω(√m)`.
- At fixed `q, B`, every such ordered cycle has `J = Ω(m/log m)`; this also holds if `B = O(log m)`, with constants depending on that bound.

This is a necessary asymptotic complexity law. The constants inherited from linear-forms theory are enormous; (G2) is a qualitative law, not a usable finite Collatz-cycle cutoff or a denominator-1 exclusion.

## Proof

[`ORDER_RIGIDITY.md`](ordered-cycle-sparse-forcing/ORDER_RIGIDITY.md) §3: combine (G4), `δ ≤ m·q/(3L)`, with the first inequality of (G1) to get `q > (3δ/m)·2^(ceil(m/J)−1−B)`, then substitute the input and take logarithms; (G5) substitutes (H1), `B + 1 ≤ J`. The form is nonzero because 2 and 3 are multiplicatively independent. No linear-forms theorem is needed for (G1) itself.

## Lean

Not formal as stated: the prose uses Bugeaud's bound, which is not formalised. Lean unit C006-d proves the conditional form with an explicit gap hypothesis instead: `LeanLane.Cyc.OrdCycle.G2_of_gap`: if `2^A ≤ 2^c·m^μ·(2^A − 3^m)` then `3·2^((m−1)/J) < 2^(B+c)·q·m^(μ+1)`; `G2_of_gap_collatz`: at `q = 1`, `B ≤ 2`, `3·2^((m−1)/J) < 2^(c+2)·m^(μ+1)`. They rest on `delta_ge_gap` (`δ ≥ (2^A − 3^m)/2^A`), `L_mul_delta_le` and `G1_first`.

## Remarks

- **A side-lane composition, not part of C006.** The gap hypothesis has the shape of `mmusson/collatz`'s `gap_all` (`c = 172`, `μ = 341`), replayed here as EXT-1 ([`musson-collatz-gap-all`](../../../sources/musson-collatz-gap-all.md)). With it, every hypothetical nontrivial Collatz cycle with `H < 8L` has `J > (m − 1)/(175 + 342·log₂ m)`; with the literature period bound `m > 1.375·10^11` ([`hercher-2023-cycle-length`](../../../sources/hercher-2023-cycle-length.md), [`barina-2025-convergence-2-71`](../../../sources/barina-2025-convergence-2-71.md)) the side lane reports `J > 1.07·10^7` (feed 2026-10-19 09:43). That figure is the side lane's, conditional on those inputs, and is not certified by a script in this node. It bounds complexity; it does not exclude cycles.
- **Different statistic.** `J` counts sorted-height changes, not Brox's chronological descents nor shortcut local minima; no novelty relative to published cycle bounds is asserted.

## History

- Split from `experiments/cycle_spectrum/C006/` (legacy ID `C006`; `REPORT.md`, `ORDER_RIGIDITY.md` §3 (G2), (G5), `LITERATURE.md`) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. The main-lane independent review covered the height-free corollary (G5).
