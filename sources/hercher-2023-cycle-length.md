---
id: hercher-2023-cycle-length
kind: source
title: "Hercher (2023): no Collatz m-cycles with m ≤ 91, and the period bound"
status: cited
citation: >
  Hercher, "There are no Collatz m-cycles with m <= 91", Journal of Integer Sequences 26 (2023);
  arXiv:2201.00406. Corrigendum (14 June 2026) repairing Theorem 21.
url: https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html
created: 2026-10-18
tags: [cycles, period-bound, computation]
---

# Hercher (2023): no Collatz m-cycles with m ≤ 91, and the period bound

## Citation

Hercher, *There are no Collatz m-cycles with m <= 91*, Journal of Integer Sequences, volume 26 (2023), [journal PDF](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf); [arXiv:2201.00406](https://arxiv.org/abs/2201.00406). The author's first name and the article number are not in the legacy record. The journal's [corrigendum of 14 June 2026](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf) repairs an inequality step in Theorem 21 and retains the bound used afterward.

Parts used:
- **Corollary 29 and Remark 30, printed pp. 20–21:** once convergence is verified through `3·2^69`, every nontrivial cycle has more than `137,500,000,000` odd members.
- **Theorem 23:** no nontrivial `m`-cycles for `m ≤ 91`, where Hercher's `m` counts local minima under the shortcut map. The journal PDF uses `X0 = 695·2^60` in that proof; versions must not be silently mixed.

## What we use

**Period bound** (legacy CONVENTIONS §5 "Period bound"), combined with [barina-2025-convergence-2-71](barina-2025-convergence-2-71.md), whose verification below `2^71` strictly contains the endpoint `3·2^69 < 2^71`:

```
every nontrivial cycle of the odd-only 3x+1 map has period m > M = 137,500,000,000 = 1.375·10^11.
```

Clock translation: Hercher's `K` counts odd members and equals our `m`; his variable `m` counts shortcut local minima and is a different quantity. Corollary 29 uses the separate Lemma 26 method, so the corrigendum to Theorem 21 does not change it (checked by the main lane and a separate reviewing agent in C011).

Legacy results using it: C011 (all-size two-defect exclusion, EXCLUSION.md (2)); S06, S07, S11 (as "the period import", where much weaker bounds suffice); the EXT-1 composition in C006 (`J > ≈ 1.07·10^7`). Theorem 23 (`m ≤ 91` local minima) is a comparison point for C001, C005, C008–C011 and phase 6 audit L4, not a premise.

Scope: the bound is for `d = 1` only. It does not hold for `3x+d` in general (the `3x+5`, `3x+7`, `3x+13`, `3x+61` controls have small positive cycles).

## How it is checked

`cited`. Taken as published; the computational proof was not rerun here, and nothing is formal. Reading the published proof and correction is not independent execution of its code. `mmusson/collatz` contains a Hercher merge lemma parametric in a verified-range hypothesis, with only `2^24` kernel-checked there; it was not used to replay this bound.
