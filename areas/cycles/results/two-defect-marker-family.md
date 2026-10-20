---
id: two-defect-marker-family
kind: result
title: The words (3, b_n, 4, b_n) are never integer 3x+1 cycles, with growing minimum and local-minimum count
status: reviewed
claim: >
  Raw odd-only clock. For r ≥ 1 let n = 2^r − 1, A_0 = ceil(n·log₂3), b_n the lower mechanical
  positive word of length n and total A_0, and w_n = (3, b_n, 4, b_n), so m = 2n + 2 = 2^(r+1) and
  A = 2A_0 + 7. Then w_n is primitive, gcd(A, m) = 1, rotation by n + 1 differs from w_n in exactly two
  positions with amplitude one, and its reduced denominator satisfies q > (8/3)·2^(m/2) > 1, with no
  imported analytic or computational input. Every rational state of its cycle exceeds n/128, and its
  shortcut-clock local-minimum count is 2(A_0 − n) + 2, which tends to infinity.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [two-defect-cancellation-bound]
evidence:
  - "two-defect-rotation-exclusion/ROTATION_DEFECTS.md, section 5: the written proof; LITERATURE.md there: the scope comparison"
  - "two-defect-rotation-exclusion/c011_two_defect_check.py: side-lane check of the family for r = 2..6 (period up to 128)"
  - "two-defect-rotation-exclusion/rotation_defect_audit.json: eight marker cases, 1,020 exact raw arrows and 1,012 rotations (historical receipt; its checker no longer runs at the new path)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: two-defect-rotation-exclusion/c011_two_defect_check.py
    scope: "Feed 2026-10-19 04:08, REFEREE C011: for r = 2..6 the word is primitive, its half-period rotation has exactly two unit mismatches, every rational state exceeds n/128, and den > 1"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 04:14: the marker family re-derived by hand, including β > n/12, every state above n/128 and the local-minimum count, no error"
tags: [cycles, rotation-distance, two-defect, mechanical-words]
---

# The words (3, b_n, 4, b_n) are never integer 3x+1 cycles, with growing minimum and local-minimum count

## Statement

For `r ≥ 1` put `n = 2^r − 1`, `A_0 = ceil(n·log₂3)`, let `b_n` be the lower mechanical positive word of length `n` and total `A_0`, and

```
w_n = (3, b_n, 4, b_n),      m = 2n + 2 = 2^(r+1),      A = 2A_0 + 7.
```

1. `w_n` is primitive (markers 3 and 4 occur once each), `A` is odd so `gcd(A, m) = 1`, and rotation by `n + 1` has exactly two mismatches, of amplitude one.
2. `q > (8/3)·2^(m/2) > 1`: no member is an integer cycle, with no linear-form estimate or published cycle record needed.
3. Every rational state of the cycle exceeds `n/128`.
4. The number of shortcut-clock local minima is exactly `2(A_0 − n) + 2` (a shortcut count, not an odd-only count); it tends to infinity.

## Proof

[`ROTATION_DEFECTS.md`](two-defect-rotation-exclusion/ROTATION_DEFECTS.md) §5. `2^A/3^m = (128/9)·(2^(A_0)/3^n)² > 128/9 > 9`, so `2 sinh(δ/2) > 8/3`, and (6) of [`two-defect-cancellation-bound`](two-defect-cancellation-bound.md) gives (2). For (3): the affine map of `b_n` has intercept `β = C_(b_n)/2^(A_0)`; every summand of `C_(b_n)` exceeds `3^(n−1)/2` and `2^(A_0) < 2·3^n`, so `β > n/12`; the state before each marker exceeds `n/12`, after a marker 3 or 4 it exceeds `n/64`, and every prefix of the lower mechanical word has slope `3^j/2^floor(jA_0/n) > 1/2` (since `0 < A_0 − n·log₂3 < 1`) and nonnegative intercept, so every state exceeds `n/128`. For (4), each valuation-2 letter of the two mechanical blocks and each marker contributes one last even-to-odd descent followed by an increasing odd shortcut step.

## Remarks

- **Scope beyond earlier classes.** Unique markers rule out any representation `u^k v^ℓ` with both exponents at least two ([`two-block-uniform-denominator-growth`](two-block-uniform-denominator-growth/README.md)); coprime total and length rule out equal-total block concatenations with more than one block ([`equal-total-two-block-exclusion`](equal-total-two-block-exclusion/README.md)) and multiple rotations of a common base ([`rotation-block-exclusion`](rotation-block-exclusion/README.md)); the word is not mechanical; and it is not an unbounded subfamily of one fixed `u^k v` family ([`repeated-block-cancellation-bound`](repeated-block-cancellation-bound/README.md)), since both marker distances grow. These comparisons concern the stated classes, not every consequence of their identities.
- **Comparison with published records.** The growing minimum and local-minimum count eventually exceed any fixed threshold used by fixed-count results ([`simons-2005-m-cycles`](../../../sources/simons-2005-m-cycles.md), [`hercher-2023-cycle-length`](../../../sources/hercher-2023-cycle-length.md)). This is a comparison of hypotheses, not a larger universal record, and not a claim that no published method could treat the family. Novelty undetermined.
- **Within the general theorem.** The family lies inside [`two-defect-rotation-exclusion`](two-defect-rotation-exclusion/README.md), which needs published inputs; this subfamily does not.

## History

- Split from `experiments/cycle_spectrum/C011/` (legacy ID `C011`; `ROTATION_DEFECTS.md` §5, `LITERATURE.md`) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19.
