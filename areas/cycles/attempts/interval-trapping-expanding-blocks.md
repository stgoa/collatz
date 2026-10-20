---
id: interval-trapping-expanding-blocks
kind: attempt
title: Interval trapping of block starts when one block expands
status: reviewed
claim: >
  Tried: extend the interval-trapping and lattice-spacing proof of the contracting two-block
  theorem to pairs with an expanding block (D_u < 0). Verdict: the mechanism fails. The actual
  3x+499 cycle through 6605 has word (1)^4 (1,3)^3 with D_u = −1, C_u = 1, D_v = 7, C_v = 5,
  K = −12, C_w = 85865, D_w = 6487, gcd 13, den 499; its rational start 6605/499 lies outside the
  interval between the block fixed points −1 and 5/7. This refutes the proof mechanism, not a
  possible denominator inequality proved otherwise.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [contracting-two-block-effective-exclusion]
evidence:
  - "../results/contracting-two-block-effective-exclusion/c003_variable_blocks_check.py, part (3): side-lane replay of the cycle"
  - "../results/two-block-uniform-denominator-growth/variable_blocks_audit.json: the actual mixed-direction cases with both counts at least three are four representations of this same d = 499 cycle"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    scope: "Feed 2026-10-19 00:48, REFEREE C003: the actual 3x+499 cycle through 6605 replayed with exactly these valuations; its start lies outside the interval between the block fixed points, so interval trapping genuinely fails for expanding blocks"
tags: [cycles, two-blocks, expanding-blocks, counterexample]
---

# Interval trapping of block starts when one block expands

## Idea

[`contracting-two-block-effective-exclusion`](../results/contracting-two-block-effective-exclusion/README.md) traps every block-boundary state between the two block fixed points, then uses integer lattice spacing. If that trapping held with one expanding block, the effective all-size bound would extend to mixed-direction pairs.

## What happened

The stored `d = 499` cycle admits the representation `u = (1)`, `k = 4`, `v = (1,3)`, `ℓ = 3`:

```
D_u = −1, C_u = 1, D_v = 7, C_v = 5, K = −12,
C_w = 85865, D_w = 6487, gcd(C_w, D_w) = 13,
den(w) = 499, starting integer state = 6605.
```

The pure block fixed points are −1 and 5/7. The mixed rational cycle starts at `6605/499`, outside their interval.

## Why it fails

With `D_u < 0` the first block expands, so the block maps no longer contract toward a common interval, and the positive interval trapping used for contracting blocks fails for this actual cycle.

## What survives

- The refutation is of the proof mechanism only; it does not refute a possible denominator inequality with a different proof.
- The asymptotic theorem [`two-block-uniform-denominator-growth`](../results/two-block-uniform-denominator-growth/README.md) still applies to this structural class (ineffectively), as does [`unequal-slope-two-block-growth`](../results/unequal-slope-two-block-growth/README.md) for a fixed pair.
- An effective treatment of the mixed-block finite exceptions was named as a useful secondary target; it would still be a subclass result.

## History

- Split from `experiments/cycle_spectrum/C003/` (legacy ID `C003`, `REPORT.md` §3 "The expanding-block obstruction is real") at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19.
- A separate draft example `(1)^3 (2)^5` was corrected before delivery: `C = 10865`, `D = 1631`, `gcd 1`, reduced denominator 1631 (an expanding-block example with no cancellation).
