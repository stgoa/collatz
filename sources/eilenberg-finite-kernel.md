---
id: eilenberg-finite-kernel
kind: source
title: "Eilenberg's finite-kernel characterisation of automatic sequences"
status: cited
citation: >
  Eilenberg's characterisation of k-automatic sequences by finiteness of the k-kernel, as stated in
  Adamczewski–Bell, "A problem about Mahler functions", Theorem 7.1, and in Allouche–Shallit
  (Automatic Sequences), Theorem 6.6.2. The original source is not cited in the legacy record.
created: 2026-10-18
tags: [automatic-sequences, invariants, classical]
---

# Eilenberg's finite-kernel characterisation of automatic sequences

## Citation

Cited in the legacy record through [adamczewski-2013-mahler-functions](adamczewski-2013-mahler-functions.md), Theorem 7.1 (with Definition 7.1), and Allouche–Shallit, *Automatic Sequences*, Theorem 6.6.2 (edition and year not in the record). The original source (Eilenberg's monograph) is not cited in the legacy record (citation incomplete).

## What we use

A sequence `f : ℕ → α` is `k`-automatic iff its `k`-kernel `{n ↦ f(k^e·n + j) : e ≥ 0, 0 ≤ j < k^e}` is finite. V004 notes that Adamczewski–Bell's Definition 7.1 displays the offset range with an apparent typo; the standard range `0 ≤ r < k^a` is used throughout.

Legacy use: V004 and its `d`-uniform extension (and V005–V007 through V004). In Lean the characterisation is taken as the **definition** `KAutomatic k f := (Kernel k f).Finite` in [`lean/V004_Assembly.lean`](../lean/V004_Assembly.lean), so the Lean statements are about finite kernels; the equivalence with automata is this external input.

## How it is checked

`cited`. Classical theorem, taken as published.
