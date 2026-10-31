---
id: ordered-cycle-denominator-one
kind: question
title: Do ordered cycles always have reduced denominator above 1?
status: open
claim: >
  Prove or refute: every nontrivial primitive positive rational cycle of the raw odd-only 3x+1 map
  whose dyadically normalised successor preserves circular order has reduced denominator q > 1, with
  no bound on period, height or number of height changes. Equivalently, no nontrivial integer 3x+1
  cycle is ordered. The ordered q = 5 and q = 233 cycles of 3x+5 and 3x+233 must remain allowed.
created: 2026-10-19
tags: [cycles, dyadic-order, frontier]
---

# Do ordered cycles always have reduced denominator above 1?

## Question

Use the dyadic normalisation of [`dyadic-order-lemma`](../results/dyadic-order-lemma.md): heights `h_i = floor(log₂(n_i/L))`, normalised states `z_i = n_i/2^(h_i) ∈ [L, 2L)`, images `F_i = 3z_i + q/2^(h_i)`. Call a cycle **ordered** when its normalised successor preserves circular order (equivalently, when `q ≤ L`, sorted `F` increases with sorted `z`).

**Target.** Exclude denominator one for every nontrivial cycle whose normalised successor preserves circular order, with no bound on period, height or height-change count.

For an ordered cycle the normalised word is the canonical lower mechanical word, `gcd(A, m) = 1`, and `D·L = q·C_h` with the weighted intercept `C_h = C_c − E_h`. The exact denominator-1 step is the congruence

```
D | C_h = C_c − E_h                                  (5)
```

for a legal odd ordered profile at `q = 1`. Any argument must retain the weighted intercept, the actual height coboundary, all adjacent-rank inequalities and exact odd outputs, and must allow the ordered `q = 5` and `q = 233` controls.

## Why it matters

It is an intermediate milestone under the all-cycle goal, not a replacement for it: it would eliminate an entire structural class at every size, leaving unordered cycles and divergent orbits. At `q = 1`, every nontrivial cycle with `H < 8L` is ordered ([`three-band-collatz-cycles-are-ordered`](../results/three-band-collatz-cycles-are-ordered.md)), so a positive answer would give `H > 8L` for every nontrivial Collatz cycle. No theorem places every hypothetical integer cycle in the ordered class, and no fixed ratio bound on all cycles is supplied.

## Known progress

- Structure: [`dyadic-order-lemma`](../results/dyadic-order-lemma.md), [`three-band-collatz-cycles-are-ordered`](../results/three-band-collatz-cycles-are-ordered.md).
- Complexity restrictions on ordered cycles: [`ordered-cycle-sparse-forcing`](../results/ordered-cycle-sparse-forcing/README.md) (`L > 2^(ceil(m/J) − 1 − B)`, `J ≥ B + 1`) and [`ordered-cycle-height-change-growth`](../results/ordered-cycle-height-change-growth.md) (fixed `q, J` leave finitely many ordered cycles; `J ≥ √m − O_q(log m)`). These restrict, they do not exclude.
- Exact arithmetic: [`ordered-cycle-residue-law`](../results/ordered-cycle-residue-law.md).
- Finite evidence: in the 1,185 normalised cycles of [`ordered-cycle-height-census`](../results/ordered-cycle-height-census.md), 51 lie in the ordered domain (`q ≤ L`, circular order), and the receipt records no failure of the candidate `B ≤ q − 1` among them. Finite evidence does not bear on untested periods.
- Failed routes: [`mechanical-normalized-word-transfer`](../attempts/mechanical-normalized-word-transfer.md), [`ordered-cycle-shortcuts`](../attempts/ordered-cycle-shortcuts/README.md), [`height-bound-via-residues-or-relaxation`](../attempts/height-bound-via-residues-or-relaxation.md).
- One candidate mechanism: the height–denominator bound `B ≤ q − 1` ([`height-denominator-candidate`](height-denominator-candidate/README.md)), whose `q = 1` case is exactly this question.

## Suggested attacks

From the legacy reports (C005–C007):

- Find a condition involving the height labels and the weighted sum (4) of [`mechanical-normalized-word-transfer`](../attempts/mechanical-normalized-word-transfer.md) that excludes `q = 1` while surviving the `q = 5, 11, 233` controls; test it at each dyadic boundary.
- Use the actual height jumps and their locations to obstruct total numerator cancellation, or convert the required growth in height complexity into a contradiction specific to `q = 1`. Extending bounded scans alone does not meet the target.
- Bounded first rungs: one-defect profiles ([`one-height-defect-ordered-cycles`](one-height-defect-ordered-cycles.md)), and the single band `B = 1` at `q = 1` (every nontrivial Collatz cycle has `H ≥ 4L`), which is strictly weaker than the full question.

## History

- Stated as the recommended next target in `experiments/cycle_spectrum/C005/REPORT.md` §4, `C006/REPORT.md` and `C007/REPORT.md` (legacy IDs `C005`, `C006`, `C007`), and listed as FRONTIER §5 of the legacy `docs/FRONTIER.md`; recorded as a node by the B03 migration (Claude, Opus 5.5) at commit `be73a66`.
