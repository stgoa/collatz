---
id: bugeaud-2022-two-logarithms
kind: source
title: "Bugeaud: effective lower bound for two logarithms"
status: cited
citation: >
  Y. Bugeaud, arXiv:2209.00275v1, Theorem 1.1, equation (1.2), p. 2. Cited in the legacy record
  as "B′". Citation incomplete in the legacy record (title and venue not stated; the year 2022 is
  read from the arXiv identifier).
url: https://arxiv.org/pdf/2209.00275
created: 2026-10-19
tags: [linear-forms, baker, cycles]
---

# Bugeaud: effective lower bound for two logarithms

## Citation

Yann Bugeaud, [arXiv:2209.00275v1](https://arxiv.org/pdf/2209.00275), Theorem 1.1, equation (1.2), PDF page 2, cited in the legacy record as "B′". It states an effective lower bound for a nonzero integer linear form in logarithms of algebraic numbers, with polynomial dependence on the maximum coefficient for fixed algebraic inputs, and attributes the underlying estimates to Waldschmidt and Matveev ([matveev-2000-linear-forms](matveev-2000-linear-forms.md)). Citation incomplete in the legacy record: no title or venue is given.

## What we use

Inputs `2` and `3`, coefficients `A, −m`, the rational field (degree one). For an ordered nontrivial cycle, `m < A < 2m`, so the coefficient bound is `max(3, A, m) = A < 2m`. Hence there is an effective absolute `K > 0` with

```
δ = A·log 2 − m·log 3 ≥ (2m)^(−K) = c_0·m^(−K),   c_0 = 2^(−K).
```

No numerical value of `K` is computed. Legacy results using it: C006 (G2: effective fixed-`q, J` finiteness for ordered cycles, `m/J < B + 1 + log₂(q/(3c_0)) + (K+1)·log₂ m`), and C011's bounded-denominator finiteness (the `A < 2m` branch). In the side lane's EXT-1 composition this input is replaced by [musson-collatz-gap-all](musson-collatz-gap-all.md).

## How it is checked

`cited`. Imported classical theorem, not a formal replay. The side lane and the Lean lane recorded that the Bugeaud import was not checked at the source by them; the main lane inspected the stated theorem.
