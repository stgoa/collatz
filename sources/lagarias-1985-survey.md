---
id: lagarias-1985-survey
kind: source
title: "Lagarias (1985): survey of the 3x+1 problem"
status: cited
citation: >
  J. C. Lagarias, "The 3x+1 problem and its generalizations", American Mathematical Monthly 92 (1985),
  3–23. Title, venue and pages completed from general knowledge, not verified against the source.
url: https://www.cecm.sfu.ca/organics/papers/lagarias/paper/html/theorem-D.html
created: 2026-10-18
tags: [survey, stopping-time, density]
---

# Lagarias (1985): survey of the 3x+1 problem

## Citation

Lagarias's 1985 survey of the `3x+1` problem. The legacy record gives only author, year, "survey", and HTML pages of the online edition ([Theorem D](https://www.cecm.sfu.ca/organics/papers/lagarias/paper/html/theorem-D.html), [Theorem F](https://www.cecm.sfu.ca/organics/papers/lagarias/paper/html/theorem-F.html)). The title, venue and pages in the frontmatter are completed from general knowledge, not verified against the source.

## What we use

- **Theorem B** (the Chernoff step): calibrated by explicit-Tao L2 ([`explicit-valuation-large-deviations`](../areas/convergence/results/explicit-valuation-large-deviations/README.md), legacy `experiments/explicit_tao/lemmas/L2_valuation_tail.md`), which proves its own explicit version with a finite certificate.
- **Theorems D and F**, as benchmarks for Phase 6 audit L1a: with `θ = 1/log₂3` and `h = −θ·log₂θ − (1−θ)·log₂(1−θ) ≈ 0.949955527188`, the density of seeds with shortcut stopping time `σ > k` is at most `2^(−(1−h)k)`, and the count with infinite `σ` up to `X` is at most `c_1·X^h` for an unspecified `c_1`. The primary TeX formulas were checked because the HTML shows equations as images. These are not reproduced, and they bound strict stopping exceptions, not the nonabsorbing basin.
- General orientation (2-adic conjugacy, periodicity conjecture), "throughout".

## How it is checked

`cited`. Taken as published; not reproduced.
