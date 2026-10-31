---
id: eliahou-1993-cycle-length
kind: source
title: "Eliahou (1993): lower bound on nontrivial cycle length"
status: cited
citation: >
  S. Eliahou, "The 3x+1 problem: new lower bounds on nontrivial cycle lengths", Discrete Mathematics
  118 (1993), 45–56. The legacy record gives only "Eliahou (1993)"; title, venue and pages are
  completed from general knowledge, not verified against the source.
created: 2026-10-18
tags: [cycles, period-bound]
---

# Eliahou (1993): lower bound on nontrivial cycle length

## Citation

Eliahou (1993). Citation incomplete in the legacy record (author and year only); the frontmatter's title, venue and pages are completed from general knowledge, not verified against the source.

## What we use

A nontrivial cycle of `3x+1` has **total length** (shortcut clock) `A ≥ 17,087,915`; in odd steps this gives `m ≥ 10,781,274` (the pair `(m, A) = (q_15, p_15)` of convergents of `log₂3`; earlier records wrote `m ≳ 1.08·10^7`). Correction recorded 2026-10-19 in S06/S07: an earlier version wrote `m ≥ 17,087,915`, confusing the total length `A` with the odd period `m`.

Legacy use: S06 and S07 name it as an alternative period import (S07 needs any period bound above `452,695`); the inputs actually used in C011 are [hercher-2023-cycle-length](hercher-2023-cycle-length.md) with [barina-2025-convergence-2-71](barina-2025-convergence-2-71.md).

## How it is checked

`cited`. The number is as quoted in the legacy record; the paper was not re-read there. 2026-10-31: the method and the constants were re-derived in [`cycle-length-lower-bound-from-convergents`](../areas/cycles/results/cycle-length-lower-bound-from-convergents/README.md): from the verified range `2^40` the exact enumeration of admissible `(m, A)` returns `17,087,915 = p_15`, `301,994 = p_13` and `85,137,581 = p_16`, matching this record; with the range `2^71` it gives `m ≥ 72,057,431,991`, `A ≥ 114,208,327,604`.
