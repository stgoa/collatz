---
id: matveev-2000-linear-forms
kind: source
title: "Matveev (2000): explicit lower bound for linear forms in logarithms"
status: cited
citation: >
  E. M. Matveev, "An explicit lower bound for a homogeneous rational linear form in the logarithms
  of algebraic numbers. II", Izvestiya: Mathematics 64(6) (2000), 1217–1269.
  DOI 10.1070/IM2000v064n06ABEH000314.
url: https://doi.org/10.1070/IM2000v064n06ABEH000314
created: 2026-10-18
tags: [linear-forms, baker, cycles]
---

# Matveev (2000): explicit lower bound for linear forms in logarithms

## Citation

E. M. Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II*, Izvestiya: Mathematics 64(6), 2000, 1217–1269, [official record](https://www.mathnet.ru/eng/im314), DOI 10.1070/IM2000v064n06ABEH000314. Direct retrieval of the original record timed out during the C006 audit; **no direct inspection of Matveev's original proof is claimed**.

## What we use

The repository never applies Matveev's original statement directly. It uses two published restatements, each its own source node:
- [languasco-2025-two-primes](languasco-2025-two-primes.md), Theorem 2.1, the positive rational "product minus one" form, giving for `0 < A < 2m`, `2^A > 3^m`:
  `log(1 − 3^m/2^A) > −600,000,000·(1 + log(2m))` (natural logs). Used by C011 and C013.
- [bugeaud-2022-two-logarithms](bugeaud-2022-two-logarithms.md), Theorem 1.1 (1.2), an effective two-logarithm bound attributed there to Waldschmidt and Matveev. Used by C006.

Legacy CONVENTIONS §5 lists this input as "Matveev: explicit lower bound for linear forms in logarithms; used by C011 and C013. S06 and S11 replace it with EXT-1" ([musson-collatz-gap-all](musson-collatz-gap-all.md)).

## How it is checked

`cited`. Imported, not re-proved or formally verified. The cited restatements were inspected at the stated theorem numbers; the original was not.
