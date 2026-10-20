---
id: constant-cancellation-two-growing-blocks
kind: attempt
title: A constant cancellation bound for two growing repeated blocks
status: reviewed
claim: >
  Tried: extend C001's constant bound gcd(C, D) | K from u^k v to u^k v^ℓ with both exponents
  growing. Verdict: false. For u = (1,1,3), v = (1,2,2), k = ℓ = t, K = 20 but
  gcd(C_w, D_w) = (32^t − 27^t)/5 (59 at t = 2) and den(w) = 5·(32^t + 27^t); cancellation grows
  exponentially. Thirteen actual decompositions in the C001 corpus also break a constant bound,
  e.g. the 3x+59 cycle from 221 with u = (1), k = 2, v = (2), ℓ = 4: C = 1105, D = 295, g = 5 > |K| = 2.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [repeated-block-cancellation-bound]
evidence:
  - "../results/equal-total-two-block-exclusion/two_blocks_audit.json: preserves all thirteen constant-bound failures found in actual stored decompositions (six distinct words across twelve parameters, including scaled repeats)"
  - "../results/equal-total-two-block-exclusion/c002_two_block_check.py, parts (2)-(3): side-lane check of the examples"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    scope: "Feed 2026-10-19 00:26, REFEREE C002: den((1,1,3)^t (1,2,2)^t) = 5(32^t + 27^t) with cancellation (32^t − 27^t)/5 growing past K = 20, and den((1,3)^t (3,1)^t) = 7(16^t + 9^t), both for t <= 40; the 3x+59 cycle 221 → 361 → 571 → 443 → 347 → 275 with C = 1105, D = 295, g = 5 > |K| = 2"
tags: [cycles, denominators, two-blocks, counterexample]
---

# A constant cancellation bound for two growing repeated blocks

## Idea

[`repeated-block-cancellation-bound`](../results/repeated-block-cancellation-bound/README.md) shows that for `u^k v` with `K ≠ 0` the cancellation `gcd(C, D)` divides the fixed integer `K`. The natural strengthening is a constant bound when **both** blocks repeat, `w = u^k v^ℓ` with `k, ℓ → ∞`.

## What happened

The exact elimination identities for two blocks give only `gcd(C_w, D_w) | |K|·gcd(G_u(k), G_v(ℓ))`, with a common geometric factor that can grow. Exact counterexample: for `u = (1,1,3)`, `v = (1,2,2)` and `k = ℓ = t`,

```
K = 20,
gcd(C_w, D_w) = (32^t − 27^t)/5,
den(w) = 5·(32^t + 27^t).
```

At `t = 2` the cancellation is 59, larger than 20, and it grows exponentially, while the reduced denominator still grows. The different sharpness family `u = (1,3)`, `v = (3,1)` has `den(u^t v^t) = 7·(16^t + 9^t)`.

In the actual-cycle corpus ([`actual-cycles-3x-d-corpus`](../results/actual-cycles-3x-d-corpus/README.md)), thirteen stored decompositions break a constant bound (six distinct words across twelve parameters, including scaled repeats). One is the `d = 59` cycle starting at 221, with `u = (1)`, `k = 2`, `v = (2)`, `ℓ = 4`: `C = 1105`, `D = 295`, `g = 5 > |K| = 2`. Even unequal slopes do not justify a constant bound.

## Why it fails

Both blocks have the same valuation-to-length ratio (`(32, 27)` for each block in the first example), so their geometric sums share the factor `(32^t − 27^t)/5`, which divides both `C_w` and `D_w`. Bounded cancellation in full generality is false; the common geometric factor is indispensable.

## What survives

- Exponential cancellation still leaves the denominator growing: the right statements keep the common factor. Equal slopes: [`proportional-slope-two-block-bound`](../results/proportional-slope-two-block-bound.md) (half the common exponent survives, and the `(1,3)/(3,1)` family shows the half is sharp). Distinct equal-total blocks: [`equal-total-two-block-exclusion`](../results/equal-total-two-block-exclusion/README.md). Unequal slopes: subexponential cancellation, [`unequal-slope-two-block-growth`](../results/unequal-slope-two-block-growth/README.md).

## History

- Split from `experiments/cycle_spectrum/C002/` (legacy ID `C002`, `REPORT.md` §3 "The failed stronger bound and its exact obstruction") at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. The obstruction was anticipated in C001's literature note §5.
