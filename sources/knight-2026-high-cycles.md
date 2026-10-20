---
id: knight-2026-high-cycles
kind: source
title: "Knight: Collatz high cycles do not exist"
status: cited
citation: >
  K. Knight, "Collatz high cycles do not exist", Discrete Mathematics 349(3) (2026), 114812.
  DOI 10.1016/j.disc.2025.114812.
url: https://doi.org/10.1016/j.disc.2025.114812
created: 2026-10-18
tags: [cycles, christoffel, mechanical-words]
---

# Knight: Collatz high cycles do not exist

## Citation

Kevin Knight, *Collatz high cycles do not exist*, Discrete Mathematics 349(3), 2026, 114812, DOI 10.1016/j.disc.2025.114812 ([publisher page](https://www.sciencedirect.com/science/article/pii/S0012365X25004200)). Only the publisher abstract and section previews were inspected; the full journal text and HAL PDF were inaccessible. (One legacy citation gives the year as 2025, matching the DOI; the record settles on volume 349, 2026.)

## What we use

A **high cycle** is the rational cycle that maximises the cycle minimum at fixed shortcut length and odd count; its parity word is the (upper) Christoffel word. Knight shows that no high cycle consists of positive integers. A large absolute minimum alone is not this hypothesis.

Legacy use: R71-a and C004-c (no nontrivial integer cycle has a mechanical / Christoffel valuation word) are this known theorem, re-derived here by a different route and formalised in the Lean lane; no priority is claimed. C001, C005, C010 use it as a scope comparison. The Christoffel case is also kernel-checked in `mmusson/collatz` (`NormBridge.cycle_one_move_christoffel`, crediting Knight, Lebel, Mghirbi and Solomon); see [musson-collatz-gap-all](musson-collatz-gap-all.md).

## How it is checked

`cited`. The conclusion is independently re-proved in the repository (R71, C004); the paper itself was read only at preview level.
