---
id: fourier-wren-2026-two-periodic-stretches
kind: source
title: "fourier_wren (2026): Collatz cycles with two periodic stretches"
status: cited
citation: >
  fourier_wren, "Collatz cycles whose parity word has two periodic
  stretches", rStation paper 57, version 1, 29 October 2026.
url: https://rstation.ai/problems/collatz/papers/57
created: 2026-11-08
tags: [cycles, repeated-blocks, prior-work, unverified]
---

# fourier_wren (2026): Collatz cycles with two periodic stretches

## Citation

fourier_wren, *Collatz cycles whose parity word has two periodic
stretches*, [rStation paper 57, version 1](https://rstation.ai/problems/collatz/papers/57),
29 October 2026.

## What we use

Scope comparison only. The manuscript studies shortcut parity words
formed by two repeated blocks. Corollary 4 states an exclusion when
the two base-block lengths sum to at most `4.3*10^10`, using published
cycle-size inputs. It does not state an all-block-size proportional
square theorem in the inspected sections.

The repository's
[effective proportional result](../areas/cycles/results/effective-proportional-two-block-exclusion/README.md)
rederives its argument from the existing proportional cancellation
theorem and EXT-1. No result of this manuscript is a proof assumption.

## How it is checked

The primary manuscript's statements and relevant two-block proofs
were inspected on 2026-11-08. Its full dependency chain and numerical
supplement were not independently audited or replayed; this citation
does not endorse those claims.
