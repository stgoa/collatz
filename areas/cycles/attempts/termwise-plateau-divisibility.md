---
id: termwise-plateau-divisibility
kind: attempt
title: Extending the two-defect bound to more mismatches by dividing each prefix plateau separately
status: reviewed
claim: >
  Tried: for a word w and a rotation v with any number of mismatches, write C_v − C_w as a signed sum
  over the maximal plateaus of constant nonzero prefix discrepancy, each ±2^u·3^v·(2^|δ| − 1)·C_arc,
  and infer, as in the two-defect case, that the cycle cancellation g = gcd(C_w, D) divides each
  plateau term (hence each arc intercept up to 2^|δ| − 1). Verdict: false beyond two mismatches.
  Actual cycles with q = 97 (3 mismatches), q = 233 (4) and q = 359 (6) have g dividing the total
  but no individual plateau contribution; for q = 97, the difference 100 = 36 + 64 with g = 5.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [two-defect-cancellation-bound]
evidence:
  - "../results/two-defect-rotation-exclusion/GENERAL_DEFECTS.md: the exact identity and the three controls"
  - "../results/two-defect-rotation-exclusion/check_coupled_defects.py, coupled_defect_controls.json: main-lane check of every arrow, primitive period, plateau, residue and corpus membership (historical receipt; the checker no longer runs at the new path)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 2026-10-19 04:14: GENERAL_DEFECTS.md read in full, no error; the q = 97 coupling 100 = 36 + 64 and the other controls re-derived"
tags: [cycles, rotation-distance, cancellation, counterexample]
---

# Extending the two-defect bound to more mismatches by dividing each prefix plateau separately

## Idea

For two rotations `w, v` with prefix totals `P_j, P'_j`, every positive word satisfies

```
C_v − C_w = Σ_(j<m) 3^(m−1−j)·(2^(P'_j) − 2^(P_j)).                     (1)
```

The discrepancy `P'_j − P_j` is constant between mismatch positions. Grouping (1) by maximal nonzero plateaus, a plateau with discrepancy `δ` contributes `±2^u·3^v·(2^|δ| − 1)·C_arc` with a positive arc intercept (negative discrepancies factor out the smaller power of two). The common divisor `g` divides the full sum and the sum at every cyclic cut. With two mismatches a suitable cut leaves one nonzero plateau, which gives [`two-defect-cancellation-bound`](../results/two-defect-cancellation-bound.md). The hope was to bound `g` plateau by plateau for any mismatch count.

## What happened

Three actual controls (all in the stored corpus [`actual-cycles-3x-d-corpus`](../results/actual-cycles-3x-d-corpus/README.md)):

| Reduced `q` | Word | Rotation | `g` | Nonzero plateau contributions | Residues mod `g` |
| --- | --- | --- | --- | --- | --- |
| 97 | (2,4,3) | 1 | 5 | 36, 64 | 1, 4 |
| 233 | (1,1,2,1,2,1,3,2) | 3 | 7 | 972, 8352 | 6, 1 |
| 359 | (1,1,2,3,1,1,2,4) | 1 | 73 | 972, 3888, 1536, 14336 | 23, 19, 3, 28 |

Each total is divisible by `g`, no contribution is. Mismatch counts are 3, 4 and 6. For `q = 97` the cycle is `17 → 37 → 13 → 17`, `C = 85`, `D = 485`, rotated intercept 185, difference `100 = 36 + 64`: the smallest possible mismatch count outside the two-defect theorem (three mismatches need at least three letters).

## Why it fails

Divisibility of a sum does not pass to its terms. With two mismatches one cut isolates `(2^k − 1)·C_arc`; with more, the plateau terms are coupled and `g` can divide only their combination. The factor `2^|δ| − 1` cannot be dropped either: the arc alone is automatically divisible only when `k = 1`.

## What survives

- Identity (1) at arbitrary mismatch count, and the three controls as tests.
- The legacy next step: combine the sums at all cyclic cuts of one rotation pair, keeping the common divisor, signed coefficients and dependencies among cuts, and look for one estimate valid for every mismatch count. This became [`coupled-defect-matrix-smith-form`](../results/coupled-defect-matrix-smith-form/README.md) and the target [`rotation-distance-growth`](../questions/rotation-distance-growth.md).
- Side-lane note (feed 04:08): the `q = 97, 233, 359` controls (`g = 5` dividing the total but neither part) show why a proof cannot just add up per-mismatch contributions.

## History

- Split from `experiments/cycle_spectrum/C011/` (legacy ID `C011`; `GENERAL_DEFECTS.md`) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. Draft correction recorded in the legacy note: independent review caught an omitted `2^|δ| − 1` factor in the first draft's description of each plateau, and corrected the implied divisibility of the arc alone to divisibility of `(2^k − 1)·C_arc`; the checker and main theorem already kept these factors.
