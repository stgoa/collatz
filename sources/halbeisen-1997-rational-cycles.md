---
id: halbeisen-1997-rational-cycles
kind: source
title: "Halbeisen–Hungerbühler (1997): optimal bounds for rational Collatz cycles"
status: cited
citation: >
  L. Halbeisen and N. Hungerbühler, "Optimal bounds for the length of rational Collatz cycles",
  Acta Arithmetica 78 (1997), 227–239.
url: https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf
created: 2026-10-17
tags: [cycles, rational-cycles, christoffel, affine-composition]
---

# Halbeisen–Hungerbühler (1997): optimal bounds for rational Collatz cycles

## Citation

Halbeisen and Hungerbühler, *Optimal bounds for the length of rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239 ([author copy](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf)). The authors' initials are completed from general knowledge, not verified against the source. Parts read: Lemmas 1–2 and equation (4) (parity legality of rational pseudo-cycles, the affine formula, concatenation) and Theorem 3. It uses the shortcut clock.

## What we use

- **Background:** the affine word formula `x → (3^m·x + C_w)/2^A`, rational cycle points `C_w/D_w` and concatenation (attributed as background in C001, C009, C010; the repository re-derives them in R71).
- **Theorem 3** (upper half): for every shortcut-map cycle with minimum `x_min`, length `L` and `k` odd steps, `x_min·(2^L − 3^k) ≤ chr(L, k)`, the Böhm–Sontacchi sum of the lower Christoffel word. Kernel-checked in `mmusson/collatz` as `Collatz.cycle_min_le_chr` and replayed here ([musson-collatz-gap-all](musson-collatz-gap-all.md)). Comparison for C004 (narrow cycles), C005 and C006 (generic minimum bound).

## How it is checked

`cited`; Theorem 3's upper half is additionally kernel-checked in an outside library replayed here (statement read, proof not reviewed line by line).
