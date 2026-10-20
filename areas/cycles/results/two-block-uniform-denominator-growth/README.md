---
id: two-block-uniform-denominator-growth
kind: result
title: Two-block words u^k v^ℓ with k, ℓ ≥ 2 have denominators growing uniformly in the total, ineffectively
status: written
claim: >
  Raw odd-only clock. Let u, v be nonempty positive valuation words, w = u^k v^ℓ with k, ℓ ≥ 2,
  A = Σw, M = |w|, 2^A > 3^M, and K = D_u·C_v − D_v·C_u ≠ 0. For every ε > 0 there is a threshold,
  independent of u, v, k, ℓ, above which den(w) ≥ 2^((η − ε)·A), η = (5·log₃2 − 3)/14 =
  0.0110463406…; unequal slopes alone give the rate log₃(2)/2 = 0.3154648768…. Hence every bounded
  denominator layer contains only finitely many such representations even as both words vary.
  Conditional on two Corvaja–Zannier inputs; the threshold is ineffective, so the finitely many
  possible exceptions (denominator 1 included) are not identified.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [unequal-slope-two-block-growth, proportional-slope-two-block-bound]
assumes: [corvaja-2005-s-unit-height]
certificates: [check_legacy_replay.py]
evidence:
  - "UNEQUAL_PROBE.md: the written proof (Theorems 1-2, the integer lemma (8), the proportional square bound, the determinant route and its limits)"
  - "check_variable_blocks.py, variable_blocks_audit.json: main-lane finite checker and receipt. Fails at its new path: it loads the corpus as HERE.parent/'C001/actual_cycles.json'. Passed at be73a66 as experiments/cycle_spectrum/C003/check_variable_blocks.py (archive/legacy-checker-run-be73a66.md). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "INDEPENDENT_REVIEW.md, ROOT_REVIEW.md: main-lane reviews; SIDE_REVIEW.md: the main lane's read of the side-lane feed"
  - "delivery_checks.json, full_gate.json: historical delivery receipt and historical finite gate"
  - "../contracting-two-block-effective-exclusion/c003_variable_blocks_check.py, part (4): side-lane check of the coprime integer lemma (8) and of η"
tags: [cycles, denominators, two-blocks, s-units, ineffective, conditional]
---

# Two-block words u^k v^ℓ with k, ℓ ≥ 2 have denominators growing uniformly in the total, ineffectively

## Statement

Let `u, v` be nonempty words of positive odd-step valuations and `w = u^k v^ℓ` with `k, ℓ ≥ 2`. Write

```
A = sum(w), M = len(w), D_z = 2^sum(z) − 3^len(z),
C_z = sum_j 3^(len(z)−1−j)·2^(sum of entries before j),
K = D_u·C_v − D_v·C_u,
den(w) = (2^A − 3^M)/gcd(C_w, 2^A − 3^M).
```

Assume `2^A > 3^M` and `K ≠ 0`. For every `ε > 0` there is a threshold, **independent of `u, v, k, ℓ`**, above which

```
den(w) ≥ 2^((η − ε)·A),   η = (5·log₃(2) − 3)/14 = 0.0110463406… > 0.
```

Consequently every bounded denominator layer contains only finitely many such representations, even when both words vary. The threshold is ineffective: the argument does not identify or eliminate the possible denominator-1 exceptions below it.

The proof has two branches ([`UNEQUAL_PROBE.md`](UNEQUAL_PROBE.md), Theorems 1–2):

- **Unequal slopes** (`Δ = Σu·|v| − Σv·|u| ≠ 0`, `k, ℓ ≥ q ≥ 2`): `liminf log(den(w))/(A·log 2) ≥ ν_q = 1 − (2 − log₃2)/q`; at `q = 2` the lower rate is `log₃(2)/2 = 0.3154648768…`.
- **Proportional slopes** (`Δ = 0`, `K ≠ 0`, `k, ℓ ≥ 2`): rate `η` above. For `k, ℓ ≥ 3` a separate elementary bound holds at every size, `den(w) > (1/2)·2^(ρ_3·A)` with `ρ_3 = (2·log₃(2) − 1)/6 > 1/24`, so `den(w) > 2^(A/24 − 1)`; this branch is effective.

## Proof

Written proof: [`UNEQUAL_PROBE.md`](UNEQUAL_PROBE.md). Summary (legacy report, lightly edited):

> One fixed group of rational 2/3-units permits the Corvaja–Zannier gcd estimate uniformly over all blocks. A global power-gap estimate controls `2^A − 3^M`, even near the positivity boundary. For proportional slopes, the exact shared factor is retained, and the elementary inequality
>
> ```
> 5·(R·k + S·ℓ − gcd(R·k, S·ℓ) + 1) ≥ 7·(R + S)
> ```
>
> for coprime `R, S` and `k, ℓ ≥ 2` gives the positive rate above. All imported estimates, local terms and exceptional sets are explicit in the proof.

The imported inputs are exactly Input A (Corollary 1, Eq. (1.3)) and Input B (Proposition 1, Eq. (2.2)) of [`corvaja-2005-s-unit-height`](../../../../sources/corvaja-2005-s-unit-height.md), as already audited for a fixed pair in [`unequal-slope-two-block-growth`](../unequal-slope-two-block-growth/README.md). The group choice and word-size estimates are this argument's own; the integer lemma and the proportional comparison are elementary (the latter is the proportional bound of [`proportional-slope-two-block-bound`](../proportional-slope-two-block-bound.md) with the factor `E` retained).

`K = 0` is essential: powers of a common primitive cycle retain their denominator indefinitely. This includes the actual denominator-1, 5, 7 and 13 controls. The theorem cannot exclude that branch by assumption.

## Certificates

None runs at the new path (they are replayed in the legacy layout, below). The main-lane checker [`check_variable_blocks.py`](check_variable_blocks.py) recomputes [`variable_blocks_audit.json`](variable_blocks_audit.json) by default (see `evidence` for why it now fails). The receipt records:

| Check | Scope |
| --- | --- |
| Actual cycle source | 2,459 stored cycles over 333 parameters from C001; every raw arrow replayed. |
| Rotations and decompositions | All 36,912 rotations; 1,694,160 exact power decompositions. Rotations are not additional primitive cycles. |
| Contracting inequalities on actual data | 1,256,140 exact commutator checks and 2,512,280 lattice-height checks. |
| Strong all-size theorem on actual data | **Zero eligible decompositions.** This part of the actual sample is vacuous. |
| Generated grid | 84 words of lengths 1–3 and entries 1–4; all ordered pairs and counts 1–6: 254,016 cases. |
| Positive generated realizations | 243,878 at 2,741 reduced denominators; 4,650,456 exact odd arrows. These are not all distinct primitive cycles. |
| Strong contracting bound | 153,696 eligible checks; 90,912 checks of the both-counts-at-least-three maximum-length bound. |
| Proportional refinement | 23,696 actual and 25,056 generated exact checks. |
| Coprime integer lemma | 78,287 cases with `R, S ≤ 32` and `k, ℓ ≤ 12`; the sharp equality is retained. |
| Common-cycle controls | 3,384 positive generated `K = 0` cases retained. |

No finite test verifies the imported asymptotic estimates. A deliberately stronger all-size exponent diagnostic, testing for `den^16 < 2^(5A)`, found no failures in 154 actual and 150,622 generated unequal-slope decompositions; its absence of counterexamples does not remove the ineffective cutoff. The actual mixed-direction cases with both counts at least three are four representations of the same `d = 499` cycle ([`interval-trapping-expanding-blocks`](../../attempts/interval-trapping-expanding-blocks.md)).

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_variable_blocks.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 48 s). It checks finite steps only; the status is unchanged.

## Remarks

- **Status.** `written`, conditional on the Corvaja–Zannier inputs. The side lane reproduced the effective contracting theorem, the worked examples and the integer lemma, but recorded that this asymptotic theorem "rests on Corvaja–Zannier and is ineffective" and did not review it; the main lane's [`INDEPENDENT_REVIEW.md`](INDEPENDENT_REVIEW.md) and [`ROOT_REVIEW.md`](ROOT_REVIEW.md) are same-lane reviews.
- **The determinant route** (`UNEQUAL_PROBE.md` §6) gives an exact computable divisibility for each instance but not the uniform rate: for `u = (7)`, `v = (9)`, `k = 11`, `ℓ = 13`, `A = 194` while both exponents in (13) are 286.
- **Effective companion.** For contracting blocks with a block repeated three times there is an all-size effective exclusion: [`contracting-two-block-effective-exclusion`](../contracting-two-block-effective-exclusion/README.md). An all-size nonintegrality claim for an expanding/contracting pair remains unproved here.
- **What this changes.** C003 removes the fixed-catalogue limitation for the two-block class. These classes can have unbounded internal word complexity and unbounded numbers of local minima; that is distinct from improving a published bound for every cycle with a given minima count. No general record or novelty claim (the bounded search found a repeated-word 2-adic budget in author-hosted 2026 notes that disclaim formal verification; they do not supply this bound). Novelty undetermined.
- **Next mechanism (legacy).** Target a restriction intrinsic to arbitrary cycle words, connecting their denominator to the sizes of their rotated cycle points; merely increasing the number of repeated motifs leaves the structural gap. Seven-field record of the legacy report: translated unresolved gap, arbitrary words need not have these repetitions, general thresholds are ineffective, `K = 0` remains essential; cheapest next test, a rotation-invariant size/residue constraint on every actual cycle (taken up by [`narrow-cycles-are-mechanical`](../narrow-cycles-are-mechanical/README.md)).

## History

- Migrated from `experiments/cycle_spectrum/C003/` (legacy ID `C003`; `REPORT.md`, proof `UNEQUAL_PROBE.md`) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). The legacy report's §2 became [`contracting-two-block-effective-exclusion`](../contracting-two-block-effective-exclusion/README.md) (with `PROPORTIONAL_UNIFORM.md`) and its §3 became [`interval-trapping-expanding-blocks`](../../attempts/interval-trapping-expanding-blocks.md).
- Main lane (ChatGPT/Codex), 2026-10-19; `UNEQUAL_PROBE.md` was written by an independent main-lane agent, the integer lemma (8) by the root. Corrected before delivery: the draft example `(1)^3 (2)^5` had an incorrect coefficient and denominator (correct: `C = 10865`, `D = 1631`, `gcd 1`); the report was made to state the exact finite diagnostic `den^16 < 2^(5A)` rather than imply that the logarithmic rate was verified numerically at every size.
