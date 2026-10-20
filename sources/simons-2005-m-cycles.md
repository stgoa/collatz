---
id: simons-2005-m-cycles
kind: source
title: "Simons–de Weger (2005): no m-cycles for small m"
status: cited
citation: >
  J. Simons and B. de Weger, Acta Arithmetica (2005): exclusion of nontrivial m-cycles of the 3x+1
  problem for 1 ≤ m ≤ 68; author-hosted update v1.43 (2007) extends this to m ≤ 75.
  Citation incomplete in the legacy record (title, volume and pages not stated).
url: https://math.deweger.net/papers/%5B35%5DSidW-3n%2B1-ActaArith%5B2005%5D.pdf
created: 2026-10-18
tags: [cycles, local-minima, linear-forms, comparison]
---

# Simons–de Weger (2005): no m-cycles for small m

## Citation

Simons and de Weger, [Acta Arithmetica 2005 version](https://math.deweger.net/papers/%5B35%5DSidW-3n%2B1-ActaArith%5B2005%5D.pdf): no nontrivial `m`-cycles for `1 ≤ m ≤ 68`. Their [author-hosted update v1.43 (2007)](https://www.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.43%5B2007%5D.pdf), abstract and Theorem 3, extends this to `m ≤ 75`; the two versions must be distinguished. Here `m` counts **local minima under the shortcut map** (circuits), not odd-only steps. Citation incomplete in the legacy record (title, volume and pages not stated; first names not given, initials completed from general knowledge, not verified).

## What we use

Comparison of scope only: legacy C001, C005, C008–C011 show that their word families have unbounded shortcut local-minimum counts and so lie outside these fixed-count hypotheses; they do not claim the paper's methods fail on them. S06/S07 recover the 1- and 2-cycle exclusions (Steiner, Simons) for `m ≥ m0` as a consistency check. The circuit count is formalised unconditionally in `mmusson/collatz` as `few_runs_cycle_trivial_uncond` ([musson-collatz-gap-all](musson-collatz-gap-all.md)).

## How it is checked

`cited`. No replay of its computation.
