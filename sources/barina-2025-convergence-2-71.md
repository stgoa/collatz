---
id: barina-2025-convergence-2-71
kind: source
title: "Barina (2025): convergence verified below 2^71"
status: cited
citation: >
  Barina, 2025, Section 6: verification of the Collatz conjecture for every positive integer below 2^71.
  Citation incomplete in the legacy record (title, venue and volume not stated).
url: https://link.springer.com/article/10.1007/s11227-025-07337-0
created: 2026-10-18
tags: [computation, verification, cycles, minimum-bound]
---

# Barina (2025): convergence verified below 2^71

## Citation

Barina, [2025 paper, Section 6](https://link.springer.com/article/10.1007/s11227-025-07337-0), reporting that every positive integer below `2^71` reaches 1. Citation incomplete in the legacy record: the title, venue and volume are not stated there, only the author, the year, the section and the publisher link. The initial of the first name is likewise not in the record.

## What we use

- **Minimum bound** (legacy CONVENTIONS §5): every element of a nontrivial cycle of `3x+1` exceeds `2^71`, i.e. `L > 2^71`.
- **Period bound**, with [hercher-2023-cycle-length](hercher-2023-cycle-length.md): the verified range contains Hercher's required endpoint `3·2^69`, giving `m > 1.375·10^11`.

Legacy results using it: C011 (period bound, EXCLUSION.md §2); S06; S07 (Barina's `L > 2^71`, used only to make an error term `ε` negligible; `L ≥ 2^20` changes nothing visible). Barina's separate total-length number is not substituted for an odd-only count. Some legacy notes quote the older verified range `2^68`; the input used by results is `2^71`.

## How it is checked

`cited`. Published computation; not rerun here, not formal.
