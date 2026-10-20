---
id: canonical-quotient-cycle-exclusion
kind: question
title: Is {1} the only cycle of the canonical quotient map T?
status: open
claim: >
  Odd-only 3x+1 map S, absorbing at 1; T = nu S the canonical quotient of elementary-bridge-quotient-normal-form on
  its positive canonical roots. Show that T has no finite positive cycle other than {1} (Phase 6 route node Y.2).
  Any word-based proof must specify all admissible words, reconstruct the exact ordinary arrows and establish the
  required integer-lattice condition. This is the cycle half of Collatz in quotient form, insufficient by itself:
  unbounded positive orbits would remain. The unrestricted no-cycle assertion fails for the raw 3x+d controls.
created: 2026-10-18
aliases: [P6-Y.2]
tags: [cycles, phase6, quotient, no-cycles]
---

# Is {1} the only cycle of the canonical quotient map T?

## Question

As in the claim. The quotient `T` and its relation to ordinary orbits are those of [`elementary-bridge-quotient-normal-form`](../../convergence/results/elementary-bridge-quotient-normal-form/README.md) (legacy R25). By that node, `T^n(ν(x)) = 1` implies `S^(n+2)(x) = 1` and `S^n(x) = 1` implies `T^n(ν(x)) = 1`, so a cycle of `T` other than `{1}` would give a positive odd orbit of `S` that is never absorbed; the quotient form changes the bookkeeping, not the difficulty.

## Why it matters

It is the cycle route Y of Phase 6. Even a proof would leave possible unbounded positive orbits; it must be combined with a separate no-divergence argument (for example [`universal-w5-quotient-stopping`](../../convergence/questions/universal-w5-quotient-stopping.md), [`unabsorbed-count-power-saving`](../../convergence/questions/unabsorbed-count-power-saving.md) or [`canonical-rigidity-bounded-invariants`](../../convergence/questions/canonical-rigidity-bounded-invariants.md)). A cycle-only result must never be called convergence.

**Transfer.** An unrestricted no-cycle assertion fails for the raw `S_d` controls; the Phase 6 harness recognises their full cycles and minima, with the three cycles through 1 as terminal baselines under absorption ([`baseline-obligation-transfer-controls`](../../convergence/results/baseline-obligation-transfer-controls/README.md)). No generalised canonical normal form is assumed.

## Known progress

The cycles area works on the same question in the ordinary odd-only setting: see [`areas/cycles/OVERVIEW.md`](../OVERVIEW.md). The frozen R71 mechanical-word theorem ([`mechanical-word-exact-denominator`](../results/mechanical-word-exact-denominator/README.md)) addresses only its stated subclass. Published exclusions with few local minima are the benchmark [`local-minima-cycle-exclusion-replay`](local-minima-cycle-exclusion-replay.md).

## Suggested attacks

None specific to the quotient were attempted in Phase 6.
