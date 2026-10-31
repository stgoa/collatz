---
id: local-minima-cycle-exclusion-replay
kind: question
title: Reproduce a published exclusion of 3x+1 cycles with few local minima, with its constants and computational inputs
status: open
claim: >
  Calibration target (Phase 6 route node Y.1): reproduce, in this repository, one published exclusion of
  nontrivial cycles of the 3x+1 shortcut map with a bounded number m of local minima (Simons-de Weger 2005: m <= 68;
  Hercher 2023, Theorem 23: m <= 91, read together with its 14 June 2026 corrigendum to Theorem 21), with its
  explicit Diophantine constants, its computational assumptions (e.g. the verified initial range, X0 = 695*2^60
  in Hercher's journal PDF) and its original clock, without mixing versions. The numerical assertions do not hold
  verbatim for 3x+d: the controls contain small positive cycles.
created: 2026-10-18
aliases: [P6-Y.1]
tags: [cycles, phase6, calibration, local-minima, literature]
---

# Reproduce a published exclusion of 3x+1 cycles with few local minima, with its constants and computational inputs

## Question

As in the claim. The sources are [`simons-2005-m-cycles`](../../../sources/simons-2005-m-cycles.md) and [`hercher-2023-cycle-length`](../../../sources/hercher-2023-cycle-length.md); the scope notes are in [`route-literature-transfer-audit`](../../convergence/results/route-literature-transfer-audit.md) L4. The authors' later updated Simons–de Weger version must be distinguished from the 2005 bound. A proof-level calibration must read the corrigendum as well as the paper and reproduce the required computational inputs.

## Why it matters

Phase 6's cycle route Y treated these exclusions as published benchmarks, not reproduced certificates. A replay would make them usable as checked inputs for the cycle-area nodes that cite them.

**Transfer.** The `3x+1` numerical exclusions fail verbatim for the actual `3x+d` cycles ([`baseline-obligation-transfer-controls`](../../convergence/results/baseline-obligation-transfer-controls/README.md), [`actual-cycles-3x-d-corpus`](../results/actual-cycles-3x-d-corpus/README.md)). The underlying inequalities may transfer after changing constants; a named distinguishing step is still required.

## Known progress

- None on the `m`-cycle exclusions themselves (Simons–de Weger, Hercher Theorem 23) in Phase 6; the side lane did not check the reference to Hercher's corrigendum (feed 2026-10-18 15:38).
- **A neighbouring published bound is replayed** (2026-10-31): [`cycle-length-lower-bound-from-convergents`](../results/cycle-length-lower-bound-from-convergents/README.md) proves, with certified continued-fraction constants and the verified range `2^71` as its only external input, that a nontrivial cycle has at least `65,470,613,321` odd states (Eliahou's method in its coarse form, about half of Hercher's cited Corollary 29 bound). Hercher's and Simons–de Weger's exclusions of cycles with few local minima remain unreplayed.

## Suggested attacks

Start from the corrigendum's repaired Theorem 21 and the explicit linear-forms constants it uses; keep the shortcut clock and the local-minimum count of the original.

## History

- 2026-10-31: Known progress records the replayed continued-fraction period bound (Claude cycles lane, Fable 5.1).
