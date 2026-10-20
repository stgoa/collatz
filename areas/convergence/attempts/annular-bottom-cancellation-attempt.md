---
id: annular-bottom-cancellation-attempt
kind: attempt
title: Proving the annular obligation by cancelling positive and negative mass above the bottom
status: reviewed
claim: >
  Tried (time-boxed), toward the five-ray / annular current obligation for 3x+1 (odd-only clock, absorbing
  at 1): show that the positive and negative mass of the annular increments A_N cancel above some height
  Q/C, so that the bottom of the dynamics is irrelevant. Verdict: no proof. At the six sampled cutoffs
  N = 96, 168, 384, 768, 1536, 3072 the canonical exact currents J_N = Σ_j P^j A_N reach state 5 and carry
  nonzero signed traffic into 1 through several entry states (at N = 3072: −136 through 5, +146 through
  341), with positive cost about 3 times the source positive mass (finite data). After the main lane's
  review, only "these six exact currents do not cancel entirely above the bottom" stands; the broader
  readings (every certificate must keep those rows, "no cancellation above the bottom to exploit", the
  approach has no leverage) are assessments, not consequences.
authors:
  - Claude PR1 lane (Opus)
created: 2026-10-17
depends_on: [class-wise-obligation-equivalence, exact-current-minimality, locally-collatz-like-control-barrier, progress-measures-control-3x-61]
evidence:
  - "../results/locally-collatz-like-control-barrier/attempt_probes.py, attempt_probes.json (high_level_annihilation): a certificate of that node (exits 0 at its new path and rewrites its receipt byte for byte)"
  - "../results/locally-collatz-like-control-barrier/NOTE.md §§12.1 and 12.3; PR1_REVIEW.md §4 (the review of these conclusions)"
reviewed_by:
  - by: ChatGPT main lane (Codex)
    date: 2026-10-17
    link: ../results/locally-collatz-like-control-barrier/PR1_REVIEW.md
    scope: "§4: the six-sample facts stand as finite observations; a forced positive bottom row is compulsory within a sampled absorbing basin, but a negative row need not be present (A_768 drops row 5); 'no separate leverage', 'three facts together leave no room' and 'no cancellation above the bottom to exploit' are assessments of a research approach, not proved consequences"
aliases: [PR1-C5-b]
tags: [convergence, packet-currents, annular, attempt]
---

# Proving the annular obligation by cancelling positive and negative mass above the bottom

## Idea

The legacy programme reduced Collatz convergence to supplying finite currents with nonpositive residual for the right-aligned packets on five dyadic rays, and then for the 64-fold annular increments `A_N` (legacy R5, R6; [`qualitative-current-criterion`](../results/qualitative-current-criterion.md), [`packet-current-supply`](../questions/packet-current-supply.md)). If the positive and negative mass of `A_N` cancelled above some height `Q/C`, the bottom of the dynamics would not matter and an almost scale-free problem would remain. The PR1 lane tried this directly, using the main lane's results R5–R13 together with its own controls.

## What happened

From legacy `NOTE.md` §12, kept as written except for the scope corrections of the review.

**High-level annihilation fails for the sampled exact currents (finite certificates).** For the canonical exact current `J_N = Σ_j P^j A_N` at `N = 96, 168, 384, 768, 1536, 3072`:

| N | rows of J_N | ‖J_N⁺‖₁ | source positive mass | signed traffic into 1 (entry state: amount) |
|---:|---:|---:|---:|---|
| 96 | 5,018 | 7,224 | 2,376 | 5: 6, 85: −3, 341: −2, 5461: −1 |
| 168 | 8,702 | 13,263 | 4,158 | 5: 5, 85: 7, 341: −9, 5461: −2, 21845: −1 |
| 384 | 20,221 | 27,238 | 9,504 | 5: 10, 85: 11, 341: −17, 5461: −3, 21845: −1 |
| 768 | 40,106 | 53,758 | 19,008 | 5: −55, 85: 5, 341: 49, 5461: −3, 21845: 4 |
| 1536 | 80,236 | 110,734 | 38,016 | 5: −103, 85: 6, 341: 98, 5461: −4, 21845: 3 |
| 3072 | 161,092 | 233,437 | 76,032 | 5: −136, 85: −14, 341: 146, 5461: −1, 21845: 5 |

`J_N` reaches state 5 in every case, and its signed traffic into 1 through several entry states is nonzero and grows with `N`. The positive costs are about `75N`, about 3 times the source positive mass. Most mass cancels within a few steps and some signed traffic reaches 1. These are six finite samples; no universal linear cost bound follows.

**Class-wise equivalence (written proof).** The obligation splits exactly into "no nontrivial cycles" and "no divergent orbits", each at full strength: [`class-wise-obligation-equivalence`](../results/class-wise-obligation-equivalence.md).

**The other ingredients.** Exact-current minimality is conditional ([`exact-current-minimality`](../results/exact-current-minimality.md)); generic arguments are ruled out by the `3x+61` controls ([`locally-collatz-like-control-barrier`](../results/locally-collatz-like-control-barrier/README.md), [`progress-measures-control-3x-61`](../results/progress-measures-control-3x-61.md)).

## Why it fails

The tested exact currents do not annihilate above the bottom, each orbit class must be excluded separately at full strength, and generic arguments do not separate `3x+1` from `3x+61`. One possible direction the lane named is `d = 1`-specific self-similarity (the main lane's annular recursion, legacy R6) together with a proved rule for continuing unresolved components: `T_61` has no exact `×64` recursion, and the negative integers fail because of their small cycles. But the source recurrence contains the expanding `3N/2` term, and every exceptional status propagates upward along valuation-1 climbs, so an induction on scale never closes without controlling climbs, which is the classical problem. This is not an exhaustive classification of possible proofs.

**Correction (2026-10-17, the main lane's review, `PR1_REVIEW.md` §4).** The original note drew stronger conclusions, which are withdrawn:

- Only the following stand: (1) the tested exact currents do not annihilate entirely above the bottom; (2) within a sampled absorbing basin, a **positive** exact-current row is compulsory in every one-sided certificate (hitting-indicator argument); (3) the finite evidence does not rule out a different universal proof that handles the remaining contribution structurally.
- A **negative** exact-current row need not be present: the `A_768` certificate with row 5 removed has the same positive cost 53,758 ([`exact-current-minimality`](../results/exact-current-minimality.md)). So "the only candidate is the forced current" cannot support the bottom-traffic claim.
- A forced positive bottom row does not imply that all source trajectories must be exposed individually to 1, and residual bottom traffic does not imply that there is no cancellation above it; the stored constructions already show large partial cancellation with a nonzero bottom contribution.
- "No separate leverage", "three facts together leave no room" and "there is therefore no cancellation above the bottom to exploit" are assessments of an approach, not consequences of the equivalence or the six samples. The note's closing sentence, that proving the five-ray obligation is equivalent with no change in strength to Collatz, is the class-wise equivalence (true) read as a verdict on the approach (an assessment).

## What survives

- The six exact-current samples and their bottom traffic, as finite data (`attempt_probes.json`).
- [`class-wise-obligation-equivalence`](../results/class-wise-obligation-equivalence.md).
- The requirement that any proposed progress lemma name the `d = 1`-specific arithmetic it uses, and be run against the `3x+61` and `3x−1` controls.
- The main lane's subsequent decision (legacy `PR1_REVIEW.md` §7 onward): a tactical pivot toward recursive descent while keeping the current formulation; the control maps remain tests of universal claims.

## History

- Migrated from the legacy ledger entry C5 (second half; `archive/docs/RESULTS.md`, legacy path) and `experiments/packet_currents/negative_controls/NOTE.md` §§12.1 and 12.3, at commit `be73a66`, by the B07 migration (Claude, Opus 5.5). Alias `PR1-C5-b`, new.
- PR1 lane (Claude, Opus), 2026-10-17. Reviewed and scope-corrected by the main lane the same day (`PR1_REVIEW.md`); the side lane accepted the review (feed 2026-10-17 19:03).
