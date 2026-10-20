---
id: progress-measures-control-3x-61
kind: result
title: On 3x+61 the annular progress measures behave like those of 3x+1, yet a positive component never ends
status: reviewed
claim: >
  Finite certificates, odd-only clock. For T_61 (absorbing at {1, 61}) and its 64-fold packet increments
  A'_N = Π'_(64N) − Π'_N at N = 8, 16, 24, 32: the one-pass compression ratio ‖P A'_N‖₁/‖A'_N‖₁ is
  0.863, 0.855, 0.849, 0.853 (19/22 ≈ 0.864 at d = 1); the exposure potential Φ falls from 228–829 at
  depth 0 to 7–16 at depth 25; and from then through depth 400 Φ stays at 7, 13, 13, 6, equal to the
  pairing ⟨e_61, A'_N⟩, because the surviving positive component contains the whole 41-cycle with minimum
  235. So one-pass contraction near 19/22 and an early fall of Φ are not evidence that every positive
  plateau of 3x+1 ends. Also (d = 1, independent code): the legacy R9 norm formula at 68 cutoffs N ≤ 4096,
  c_80000 = 0, and the legacy R10 trace Φ(A_96) = 17 at depths 20–27 and 0 at depth 28.
authors:
  - Claude PR1 lane (Opus)
created: 2026-10-17
depends_on: [locally-collatz-like-control-barrier]
evidence:
  - "locally-collatz-like-control-barrier/progress_measures_audit.py, progress_measures_audit.json: a certificate of that node (exits 0 at its new path and rewrites its receipt byte for byte)"
  - "locally-collatz-like-control-barrier/NOTE.md §11, HANDOFF_FOR_MAIN.md §4"
reviewed_by:
  - by: ChatGPT main lane (Codex)
    date: 2026-10-17
    link: locally-collatz-like-control-barrier/PR1_REVIEW.md
    scope: "§1: 'C4, progress controls' survives — a one-pass norm decrease and a large early reduction of positive component mass also occur on the false analogue, so those statistics alone do not prove finite progress of every remaining positive component; the combined verifier reproduced the receipt"
aliases: [PR1-C4]
tags: [convergence, packet-currents, negative-controls, progress-measures, 3x+61]
---

# On 3x+61 the annular progress measures behave like those of 3x+1, yet a positive component never ends

## Statement

The legacy main-lane rounds R9 and R10 (commit `ce56699`) measure partial progress on the annular increments `A_N = Π_(64N) − Π_N` of `3x+1` in two ways:

- **(R9, [`annular-root-collapse-contraction`](annular-root-collapse-contraction.md))** a one-pass root compression `R`, collapsing chains `F(x) = 4x + 1`, with exact norm `‖P A_N‖₁ = ‖R A_N‖₁ = 171N/4 − |c_N| ≤ (19/22)·‖A_N‖₁`, where `c_N` is the annular mass of the chain rooted at 1 and `|c_N| ≤ 3`;
- **(R10, [`exposure-potential-boundary-flux`](exposure-potential-boundary-flux/README.md))** the exposure potential `Φ`, the positive mass of exposed components not containing 1.

The legacy open obligation was to prove that every positive `Φ`-plateau ends ([`annular-component-progress-lemma`](../questions/annular-component-progress-lemma.md)).

**Control (finite certificates).** For `T_61` (the map of [`locally-collatz-like-control-barrier`](locally-collatz-like-control-barrier/README.md)), the increments `A'_N = Π'_(64N) − Π'_N` behave as follows (exposure followed to depth 400):

| N | ‖A'_N‖₁ | one-pass ratio ‖P A'‖/‖A'‖ | Φ at depth 0 | Φ at depth 25 | Φ at depth 400 | permanent mass |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 460 | 0.863 | 228 | 7 | 7 | 7 |
| 16 | 864 | 0.855 | 431 | 16 | 13 | 13 |
| 24 | 1264 | 0.849 | 630 | 16 | 13 | 13 |
| 32 | 1660 | 0.853 | 829 | 10 | 6 | 6 |

At `d = 1` the ratio is `19/22 ≈ 0.864`. In every case the surviving positive component contains the whole 41-cycle `235 → …`. The cycle is closed under `T_61`, so no further exposure can join it to an absorber, and `Φ` is constant from then on; the permanent mass equals the pairing `⟨e_61, A'_N⟩`.

**Cross-audit at `d = 1` (finite checks, independent code).** The R9 norm formula and `‖R A_N‖₁ = ‖P A_N‖₁` hold at 68 cutoffs `N ≤ 4096`; the `2N` positive survivors `p ≡ −1 (mod 36)` in `(32Q, 64Q)` carry `(R A_N)(p) = 2`; `c_80000 = 0` by an independent point evaluator for `Π_N(y)`; and `Φ(A_96) = 17` at exposure depths 20–27 and `0` at depth 28.

## Proof

Exact finite computation by `progress_measures_audit.py` (folder [`locally-collatz-like-control-barrier`](locally-collatz-like-control-barrier/README.md)), which builds every packet with that folder's `affine_controls` construction and writes `progress_measures_audit.json`. The permanence of the `T_61` component is exact, not a depth-limited observation: the component contains a cycle closed under `T_61` that avoids `{1, 61}`, so its mass is invariant under further exposure.

**Consequence.** One-pass contraction near `19/22` and a rapid early fall of `Φ` by roughly 97% both occur on a map where the plateau never ends. These statistics are therefore not evidence that `3x+1` plateaus end; a proof of the progress obligation has to use some property of `3x+1` that `T_61` lacks.

## Remarks

- The control says nothing for or against a progress lemma for `3x+1`; the receipt's scope reads "No progress lemma is proved or refuted for 3x+1".
- *Observation, not in the receipt:* the PR1 lane also reproduced the main lane's uncommitted transport numbers of 2026-10-17 18:00 (`‖P^k A_96‖₁ = 4752, 4103, 3533, 3124` for `k = 0…3`; norm 13 and positive mass 4 at both `P^79 A_96` and `P^80 A_96`; the nine-row table of `R P^78 A_96`). These are not certified here.
- The R9 and R10 nodes record this cross-audit as a finite-scope review.

## History

- Migrated from the legacy ledger entry C4 (`archive/docs/RESULTS.md`, legacy path) and `experiments/packet_currents/negative_controls/NOTE.md` §11, at commit `be73a66`, by the B07 migration (Claude, Opus 5.5). Alias `PR1-C4`.
- PR1 lane (Claude, Opus), 2026-10-17. Main-lane review in `PR1_REVIEW.md` the same day.
