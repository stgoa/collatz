---
id: close-pair-lattice-criterion
kind: attempt
title: "Excluding denominator 1 by a universal close pair: some two states less than 2 apart"
status: reviewed
claim: >
  Tried: prove that every nontrivial primitive positive rational cycle of the odd-only 3x+1 map has
  two distinct states less than 2 apart (σ < 2), which with the odd-lattice bound d ≥ 2/σ would
  exclude reduced denominator 1. Verdict: false. The actual 3x+5 cycle 19 → 31 → 49 normalises to
  states 19/5, 31/5, 49/5 with σ = 12/5; the corpus has 28 distinct normalised failures (183 scaled
  source instances); and for every G > 0 there is a primitive rational cycle with every pair of
  states more than G apart and minimum above m·G, even with H < 2L. Lattice packing cannot supply
  its own missing upper bound.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [narrow-cycles-are-mechanical, mechanical-word-exact-denominator]
evidence:
  - "SIZE_PROBE.md: the written obstruction (sections 1-5) and its primary-source scope (section 6)"
  - "../../results/narrow-cycles-are-mechanical/rotation_audit.json: the 28 distinct normalised counterexamples and 156 coprime upper approximants with 20,085 adjacent gaps (historical receipt)"
  - "../../results/narrow-cycles-are-mechanical/c004_narrow_check.py, part (4): side-lane check of the d = 5 and d = 13 controls"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    scope: "Feed 2026-10-19 01:06, REFEREE C004: the d5 cycle 19 → 31 → 49 has normalised minimum gap 12/5 > 2 and the d13 mechanical cycle has ratio below 2; the close-pair counterexamples judged useful and correct. The all-G construction of SIZE_PROBE.md sections 3-4 was not separately re-derived there"
    link: ../../../../archive/side-lane/FEED.md
tags: [cycles, lattice, spacing, counterexample]
---

# Excluding denominator 1 by a universal close pair: some two states less than 2 apart

## Idea

For rational cycle states with common reduced denominator `d`, every numerator is odd, so adjacent sorted states differ by at least `2/d`. With `σ` the smallest distinct-pair distance and `W` the width,

```
d ≥ 2/σ,    d ≥ 2(m−1)/W.                               (1)
```

So a universal bound `σ < 2` (or `W < 2(m−1)`) on nontrivial cycles would exclude `d = 1`.

## What happened

The actual `3x+5` cycle

```
19 → 31 → 49 → 19       (valuations 1, 1, 3)
```

normalises to the primitive rational cycle `19/5 → 31/5 → 49/5`, with `σ = 12/5 > 2` and `W = 6 > 4`. It refutes both proposed uniform upper bounds. The actual-cycle sample has 28 distinct normalised failures, appearing in 183 scaled source instances.

A stronger all-size obstruction ([`SIZE_PROBE.md`](SIZE_PROBE.md)):

> For every real `G > 0`, a primitive positive rational cycle exists with at least two odd states, every distinct pair of odd states more than `G` apart, and minimum greater than `m·G`, where `m` is its number of odd states. The construction imposes no fixed reduced denominator.

These examples can still have `H < 2L`. Mechanical phase increments are single positive 2/3 monomials, `B_(ℓ+1) − B_ℓ = 3^(m−1−j)·2^floor((jA+ℓ)/m) > 3^(m−1)/2`, so with `δ = A − m·log₂3 > 0`, `σ > 1/(6(2^δ − 1))`; coprime upper approximations `δ → 0+` (obtained by an elementary pigeonhole argument that keeps the sign) make the normalised gaps arbitrarily large. Denominators vary with the examples; no fixed-`d` assertion or rescaling of the `d = 1` map is used. For example the `d = 13` mechanical cycle has ordered numerators `319, 367, 421, 485, 557`, minimum gap `48/13` and ratio `557/319 < 2`; the exact `(A, m) = (485, 306)` example has every gap greater than 100.

## Why it fails

The lattice inequalities (1) give only **lower** bounds on separation and width. Excluding `d = 1` through them needs an additional **upper** bound, and no constant upper bound on `σ` or on `W/(m−1)` holds over all primitive positive rational cycles. A large minimum is consistent with nonintegrality.

## What survives

- Phase order equals size order for mechanical cycles, with one explicit monomial per adjacent increment; positive approximation errors tending to zero make every pair gap unbounded together with the minimum.
- An integer-cycle obstruction must retain denominator-specific arithmetic or further structure. The ratio condition does: [`narrow-cycles-are-mechanical`](../../results/narrow-cycles-are-mechanical/README.md) (`H < 2L` forces a mechanical word, hence its exact denominator). The close-pair criterion cannot be reinstated as a consequence of narrowness, since mechanical cycles can have ratio below 2 and every pair gap arbitrarily large.
- The related ordered-cycle variant "some normalised pair has primitive odd gap at most `q`" also fails: [`ordered-cycle-shortcuts`](../ordered-cycle-shortcuts.md).

## History

- Split from `experiments/cycle_spectrum/C004/` (legacy ID `C004`; `REPORT.md` §3, `SIZE_PROBE.md`, `ROTATION_LATTICE.md` §4) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. The construction develops R71's mechanical upper-approximant family ([`mechanical-word-exact-denominator`](../../results/mechanical-word-exact-denominator/README.md), legacy `BALANCED_DENOMINATORS.md`; linked at the B12 migration).
