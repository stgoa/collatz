---
id: two-defect-bounded-denominator-finiteness
kind: result
title: Each bounded-denominator layer of the two-defect class is finite, effectively in principle
status: reviewed
claim: >
  Raw odd-only clock. There are effective absolute constants c, K > 0 such that every positive
  valuation word with a nonidentity rotation differing in exactly two positions has reduced
  denominator q > c·(2/√3)^m·m^(−K), with no restriction on amplitude. Consequently, for every fixed
  Q > 0 only finitely many such words (of any period, alphabet, amplitude and rotation) have q ≤ Q,
  effectively in principle. Conditional on an effective two-logarithm lower bound for
  A·log 2 − m·log 3 (Bugeaud). No numerical cutoff or enumeration is supplied, and finitely many
  q = 1 exceptions are not excluded by this argument alone.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [two-defect-cancellation-bound]
assumes: [bugeaud-2022-two-logarithms]
evidence:
  - "two-defect-rotation-exclusion/ROTATION_DEFECTS.md, section 3 ('Every bounded denominator layer of the two-defect class is finite'): the written proof"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 2026-10-19 04:14: ROTATION_DEFECTS.md read in full, inequalities (5)-(9) and the finiteness argument re-derived by hand, no error"
tags: [cycles, rotation-distance, two-defect, finiteness, conditional]
---

# Each bounded-denominator layer of the two-defect class is finite, effectively in principle

## Statement

There are effective absolute constants `c, K > 0` such that every positive word with a two-defect rotation ([`two-defect-cancellation-bound`](two-defect-cancellation-bound.md)) satisfies

```
q > c·(2/√3)^m·m^(−K),                                        (8)
```

allowing unbounded amplitude. Hence:

> For every fixed positive `Q`, only finitely many positive valuation words with a two-defect cyclic rotation have reduced denominator at most `Q`. This finiteness is effective in principle and uniform in the period, alphabet, defect amplitude and rotation.

**Input.** [`bugeaud-2022-two-logarithms`](../../../sources/bugeaud-2022-two-logarithms.md), Theorem 1.1 (1.2): for the fixed bases 2, 3, degree one and coefficients `(A, −m)`, effective `c_0 > 0`, `K_0 > 0` with `δ = A·log 2 − m·log 3 ≥ c_0·m^(−K_0)` when `A < 2m`. No numerical value is computed.

## Proof

[`ROTATION_DEFECTS.md`](two-defect-rotation-exclusion/ROTATION_DEFECTS.md) §3. Take `c_0 ≤ 1`; then `1 − e^(−δ) ≥ c_0·m^(−K_0)/2` for `A < 2m`, while for `A ≥ 2m`, `1 − e^(−δ) ≥ 1 − (3/4)^m ≥ 7/16` (`m ≥ 2`). With (7) of [`two-defect-cancellation-bound`](two-defect-cancellation-bound.md) this gives (8), so `q ≤ Q` bounds `m`.

Bounded length alone does not give finitely many words, so the valuations must also be bounded. Put `S = A − k`. If `A < m·log₂3 + 1`, bounded `m` bounds `A`. Otherwise `1 − 3^m/2^A ≥ 1/2`, and (5), before using `k ≤ A − m`, gives `q > (1/2)·2^(S/2)·(2/3)^(m/2)` (9), so bounded `q, m` bound `S`. Rotate the upper defect letter `a + k` to the end: the intercept ignores it, and the last-letter bound gives `g ≤ C_rot < 2^(S−a−m+1)·3^m ≤ 2^(S−m)·3^m`. So `D = q·g ≤ Q·2^(S−m)·3^m` and `2^A = D + 3^m` are bounded, which bounds `A`, `k` and every valuation. QED.

## Remarks

- **Refinements.** (6) of [`two-defect-cancellation-bound`](two-defect-cancellation-bound.md) gives `q > c'·2^((m−k)/2)·m^(−K')` directly, a stronger rate under any amplitude ceiling or `k ≤ (1 − ε)m`. These are not needed for the finiteness theorem.
- **What it does not give.** It leaves finitely many exceptions at `q = 1`; the all-size exclusion needs explicit constants and the period bound, [`two-defect-rotation-exclusion`](two-defect-rotation-exclusion/README.md). The side lane's S09 (legacy `experiments/cycle_spectrum/S09/`, not yet migrated) later made the bounded-denominator finiteness explicit and exponential (feed 2026-10-19 13:22).
- **Controls.** The actual `3x+d` cycles with two-defect words are finitely many at each `d`, consistent with the statement.

## History

- Split from `experiments/cycle_spectrum/C011/` (legacy ID `C011`; `ROTATION_DEFECTS.md` §3) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. The side-lane referee (feed 04:08) tested the elementary bounds but not this asymptotic argument; the review on record is the Lean lane's hand re-derivation.
