---
id: cobham-recognizability-theorem
kind: source
title: "Cobham's theorem: sets recognizable in two independent bases"
status: cited
citation: >
  Cobham's theorem on base-dependence of sets recognizable by finite automata, as stated in
  Adamczewski–Bell, "A problem about Mahler functions", Theorem 2.1, and in Allouche–Shallit
  (Automatic Sequences), Theorem 11.2.2. The original paper is not cited in the legacy record.
created: 2026-10-18
tags: [automatic-sequences, invariants, classical]
---

# Cobham's theorem: sets recognizable in two independent bases

## Citation

The legacy record cites Cobham's theorem only through secondary statements: [adamczewski-2013-mahler-functions](adamczewski-2013-mahler-functions.md), Theorem 2.1 (directly inspected), and Allouche–Shallit, *Automatic Sequences*, Theorem 11.2.2 (as cited by the side lane; edition and year not in the record). The original article is not cited in the legacy record (citation incomplete; it is commonly given as A. Cobham, "On the base-dependence of sets of numbers recognizable by finite automata", Mathematical Systems Theory 3 (1969), completed from general knowledge, not verified against the source).

## What we use

A set of nonnegative integers recognizable by finite automata in two multiplicatively independent bases is eventually periodic. In the kernel form used here (with [eilenberg-finite-kernel](eilenberg-finite-kernel.md)): for a finite alphabet `α`, every `f : ℕ → α` with finite 2-kernel and finite 3-kernel is eventually periodic.

Legacy use: V004 (binary-automatic invariant colorings of `3x+1` are constant), its `d`-uniform extension, and through V004 also V005, V006 and V007, whose constancy steps go through V004 (a dependence the side lane flagged as unrecorded in the legacy RESULTS lines). In Lean it is the named hypothesis `CobhamStatement α` of `LeanLane.V004.automatic_rigidity` and `constant_of_ternary_automatic` ([`lean/V004_Assembly.lean`](../lean/V004_Assembly.lean)); it is not proved in this repository and is not in Mathlib.

## How it is checked

`cited`. Classical theorem, taken as published; no formal replay.
