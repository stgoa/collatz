---
id: quantitative-rigidity-programme
kind: attempt
title: Five batches toward superlinear section growth of 3x+1 invariants, which reached only an additive gain
status: reviewed
claim: >
  Tried (main lane, V005-V009, 2026-10-18): prove that every nonconstant finite-valued 3x+1 invariant colouring has
  sup_D kappa_h(D)/(D+1) infinite, by comparing mechanisms batch by batch (reconstruction from one section, packing
  descendant families, separate and joint two-base growth, digit-count sections, finite separators in the joint
  section graph, the full root identities, near-minimal binary growth, linear-algebraic detection). Verdict: stalled.
  The batches proved scoped structural results and one all-invariant additive gain, kappa_h(D) - (D+1) -> infinity,
  but no fixed fractional improvement and not the unbounded ratio; several tempting shortcuts were refuted by exact
  controls. The goal was replaced, unresolved, on 2026-10-19.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [automatic-section-forces-constancy, quadratic-separation-digit-count-sections, singleton-exit-separator-exclusion, two-exit-interior-counterexample, additive-section-excess-unbounded]
evidence:
  - "../../results/automatic-section-forces-constancy/section_graph.md: the linear section-graph control; ../../results/quadratic-separation-digit-count-sections/overlap.md section 4 and joint_literature.md: the adjacent-11 control and the T/U action control"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Batch table and refuted shortcuts checked against the thirteen cited nodes; the five controls (section graph, sparse indicator, adjacent-11, T/U action, two-exit rotation) recomputed independently; the 242/259 and digit-count-search receipts re-run; node moved to a folder with 24 links repaired; verdict HOLDS WITH CORRECTIONS (Cobham scope noted in History)"
tags: [invariants, section-growth, quantitative-rigidity, stalled]
---

# Five batches toward superlinear section growth of 3x+1 invariants, which reached only an additive gain

## Idea

After [`binary-automatic-invariant-colourings-constant`](../../results/binary-automatic-invariant-colourings-constant/README.md) excluded finite-state invariants, the owner activated a quantitative target ([`section-count-depth-ratio-unbounded`](../../questions/section-count-depth-ratio-unbounded/README.md)): exclude invariants whose binary-section count grows only linearly. The generic infinite-kernel bound `kappa_h(D) ≥ D + 1` does not meet it, so success needed invariance-specific input. The brief asked to compare a few bounded mechanisms before deepening and to preserve exact hypotheses, controls and failed approaches.

## What happened

| Batch | Mechanism | Result | Decision |
|---|---|---|---|
| V005 | Reconstruct `h` from one positive section; separate vs joint two-base growth | One automatic section forces constancy, with a polynomial bound only; linear binary growth of `h` ⇔ linear joint growth of `b` ([`automatic-section-forces-constancy`](../../results/automatic-section-forces-constancy/README.md)); the three scalar identities ([`scalar-interface-three-identities`](../../results/scalar-interface-three-identities.md), formal); separate two-base linear growth does not force periodicity ([`sparse-indicator-linear-growth-in-both-bases`](../../results/sparse-indicator-linear-growth-in-both-bases/README.md)) | Keep the joint family |
| V006 | Distinguish mixed descendants of a digit-count ray | Quadratic separation ([`quadratic-separation-digit-count-sections`](../../results/quadratic-separation-digit-count-sections/README.md), formal), hence quadratic growth if one digit-count section exists ([`digit-count-section-forces-quadratic-growth`](../../results/digit-count-section-forces-quadratic-growth.md)) | Extraction of such a section unproved |
| V007 | Finite separators in the joint section graph | Two-base automaticity is one condition ([`reverse-closure-two-base-automaticity`](../../results/reverse-closure-two-base-automaticity.md), formal); no finite single-exit interior ([`singleton-exit-separator-exclusion`](../../results/singleton-exit-separator-exclusion/README.md)), but only `|J_D(b)| ≥ 2D + 1` | Linear, weaker than generic after depth conversion |
| V008 | Two-exit interiors; the full root identities; the growth hypothesis at full strength | Generic two-exit exclusion refuted ([`two-exit-interior-counterexample`](../../results/two-exit-interior-counterexample/README.md)); `|J_1(b)| ≥ 4` ([`first-shell-three-state-rigidity`](../../results/first-shell-three-state-rigidity/README.md)); uniform future cuts, but no bounded-width stretches ([`linear-growth-uniform-future-cuts`](../../results/linear-growth-uniform-future-cuts.md)) | Stop excluding fixed boundary sizes one at a time |
| V009 | Near-minimal binary growth; linear algebra of section spans | `kappa_h(D) − (D+1) → ∞` ([`additive-section-excess-unbounded`](../../results/additive-section-excess-unbounded/README.md)); short detection under linear growth ([`linear-growth-short-detection`](../../results/linear-growth-short-detection.md)) | Two candidate routes named, neither supplied |

**Refuted shortcuts**, each by an exact control that satisfies the reduced hypotheses and fails full Collatz invariance at a named input:
- *Local nonautomaticity plus the first return identity* ([`section_graph.md`](../../results/automatic-section-forces-constancy/section_graph.md)): a section graph with `kappa(D) = D + 3` for `D ≥ 3`, every section nonautomatic, obeying doubling and `h(8n+5) = h(2n+1)`, all infinite descendant families overlapping; it fails invariance at 9 (`h(9) = 1`, `h(28) = 0`).
- *Separate linear growth in two bases* (the sparse indicator, which fails doubling at 3).
- *Linear growth contains a digit-count section*: the adjacent-11 sequence `z(n) = F(N_11(n))` has `kappa_z(D) ≤ 2D`, `z(2n) = z(n)`, `z(8n+5) = z(2n+1)` and no digit-count section; it fails at 3 (`z(3) = 1`, `z(10) = 0`).
- *Importing semigroup growth theorems*: they count transformations, not one orbit; the maps `T(n) = n + 1`, `U(n) = n + 1 + 1_(n a positive power of 2)` have at most `2D + 1` states reachable from 0 through depth `D` but `2^D` distinct words of length `D` ([`joint_literature.md`](../../results/quadratic-separation-digit-count-sections/joint_literature.md)).
- *Excluding boundary widths one at a time* (the two-exit counterexample) and *inferring bounded-width stretches from cumulative growth* (the bounded-degree control).

## Why it fails

Every proved mechanism either needs an extra hypothesis that no genuine invariant is known to satisfy (a digit-count section; the side lane found none in the actual `3x+5`, `3x+13`, `3x+61` labellings it tested), or yields a linear or additive bound that the depth conversion `J_D(b) ⊆ K^+_(1+4D)(h)` cannot turn into a ratio gain. The two remaining routes (delayed nonzero combinations; extending the return contraction to several states per layer) each lack their key step. The side lane's calibration: the target appears `d`-uniform (the `3x+5` and `3x+13` labellings already have at least 242 and 259 binary sections by depth 9), and the best published quantitative Cobham bounds are far too weak; so even a success would exclude one description class, not bear on convergence without an upper bound for the actual bad set.

Process notes: after V005–V007 the side lane proposed D8 (a `(1+ε)` first milestone and a two-batch stopping rule). The main lane kept part 1 as a diagnostic and rejected automatic abandonment because the goal was the owner's active objective. V008 added dated notes recording that the Collatz applications of V005–V007 inherit Cobham through V004. On 2026-10-19 the owner replaced the goal with the cycle-spectrum programme (the cycles area), leaving the target open.

## What survives

- The formal interface: [`scalar-interface-three-identities`](../../results/scalar-interface-three-identities.md), [`reverse-closure-two-base-automaticity`](../../results/reverse-closure-two-base-automaticity.md), [`quadratic-separation-digit-count-sections`](../../results/quadratic-separation-digit-count-sections/README.md), the `K_+` closure with its depth-4 bound ([`positive-offset-kernel-ternary-closure`](../../results/positive-offset-kernel-ternary-closure.md)).
- The complete joint section-graph interface (five digit transitions, six radix identities, three root identities; [`graph_interface.md`](../../results/quadratic-separation-digit-count-sections/graph_interface.md)), which reconstructs actual sequences in both bases.
- The additive theorem and the detection bound, and the exact controls above, as tests for any future proposal.

## History

- New node by the B16 migration (Claude, Opus 5.5) summarising the V005–V009 reports, the legacy brief `experiments/viewpoints/briefs/QUANTITATIVE_RIGIDITY_BRIEF.md` and the viewpoint log (both now in [`archive/invariants-viewpoints/`](../../../../archive/invariants-viewpoints/README.md)), and the side lane's direction D8 and feed entries 21:26–23:55 of 2026-10-18, at commit `be73a66`.
- Main lane (ChatGPT/Codex), 2026-10-18, main commits `85a07c2` (V005) to `4be9bae` (V009).
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. Corrections: the node was moved from `quantitative-rigidity-programme.md` to `quantitative-rigidity-programme/README.md` to hold the review, and its 24 relative paths (22 links and the two `evidence` paths) were repaired by one more `../`; no text changed. Scope note: the additive gain `kappa_h(D) - (D+1) -> infinity` and the Collatz applications of V005-V007 that the claim summarises are conditional on Cobham's theorem through V004, as their nodes state; the claim text was left as written. The review is [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
