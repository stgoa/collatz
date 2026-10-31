---
id: section-count-depth-ratio-unbounded
kind: question
title: Must every nonconstant 3x+1 invariant colouring have binary section count growing faster than any linear function of depth?
status: open
claim: >
  Let h be a finite-valued colouring of the positive integers with h(2n) = h(n) for n >= 1 and h(3n+1) = h(n) for
  positive odd n > 1 (1 absorbing), extended by h(0) = h(1), and let kappa_h(D) be the number of distinct entire
  sequences n -> h(2^a n + r), 0 <= a <= D, 0 <= r < 2^a. Prove that if h is nonconstant then
  sup_D kappa_h(D)/(D+1) is infinite (for every C some D has kappa_h(D) > C(D+1)). The generic infinite-kernel bound
  kappa_h(D) >= D+1 and the proved additive gain kappa_h(D) - (D+1) -> infinity do not suffice. A positive answer
  excludes one more description class for a hypothetical nonabsorbing set; it does not bear on convergence without
  an upper bound on the section count of the actual bad set, and its 3x+d analogue appears consistent with the
  genuine 3x+5 and 3x+13 separations.
created: 2026-10-18
certificates: [check_legacy_replay.py]
evidence:
  - "automatic_rigidity_control.py, automatic_rigidity_control.json: side-lane control data (distinct 60-term prefixes of the 2-kernels, levels e <= 9) for the 'which cycle' colourings of 3x+5, 3x+7, 3x+13, the indicators 1_(d|n) and Thue-Morse; replayed by check_legacy_replay.py"
aliases: [VP-V13]
tags: [invariants, section-growth, quantitative-rigidity, automatic, open]
---

# Must every nonconstant 3x+1 invariant colouring have binary section count growing faster than any linear function of depth?

## Question

As in the claim: the "quantitative rigidity" target of the legacy brief ([`QUANTITATIVE_RIGIDITY_BRIEF.md`](../../../../archive/invariants-viewpoints/briefs/QUANTITATIVE_RIGIDITY_BRIEF.md)): "Prove that any nonconstant finite-valued Collatz invariant requires binary-section complexity exceeding every linear bound." Sections are entire functions on `n ≥ 0`, never finite prefixes. The target is `sup_D kappa_h(D)/(D+1) = ∞`, not the stronger `kappa_h(D)/(D+1) → ∞`. Do not assume any regularity of the actual nonabsorbing set.

Equivalent forms: by [`automatic-section-forces-constancy`](../../results/automatic-section-forces-constancy/README.md) (b), linear binary growth of `h` is equivalent to linear growth of the joint binary/ternary section family `J_D(b)` of `b(n) = h(2n+1)`, which satisfies the three scalar identities of [`scalar-interface-three-identities`](../../results/scalar-interface-three-identities.md). So the question is whether a nonconstant `b` with `b(3n) = b(4n)`, `b(3n+2) = b(2n+1)`, `b(4n+2) = b(n)` can have `|J_D(b)| ≤ C(D+1)`.

## Why it matters

[`binary-automatic-invariant-colourings-constant`](../../results/binary-automatic-invariant-colourings-constant/README.md) (V004) excludes finite-state descriptions of a hypothetical nonabsorbing set: its indicator has an infinite binary kernel, hence `kappa_h(D) ≥ D + 1`. This question asks to exclude descriptions whose complexity grows only linearly. It would exclude one more description class while leaving unrestricted components open; "the actual bad set is automatic" (or linearly complex) is equivalent to convergence and is not a milestone.

**Calibration (side lane, labelled assessments, feeds 20:02, 20:40, 21:26).** The question appears `d`-uniform: the actual `3x+5` and `3x+13` cycle labellings already have at least 242 and 259 distinct binary sections by depth 9 (rigorous lower bounds from distinct 60-term prefixes, [`automatic_rigidity_control.json`](automatic_rigidity_control.json)), growing by a ratio of about 1.8 per level, so a proof using `d = 1` only in the commutator step would also hold for these genuine separations. The best published quantitative Cobham theorem (Mol–Rampersad–Shallit–Stipulanti, arXiv:1809.00679, Cor. 6–7) gives only about `(log log n)^(1/4)` automaticity in the second base; the indicator of `{2^(2^k)}` is not 2-automatic and has `kappa(D) = D + 3`, so the target needs invariance-specific input, not just non-automaticity. Turning any complexity lower bound into convergence would need an upper bound on the actual bad set's section count, and none is known or suggested.

## Known progress

All in this area; the generic bounds are elementary, the Collatz applications inherit Cobham's theorem through V004.

- **Scoped gains.** Quadratic growth if `h` has one digit-count section ([`digit-count-section-forces-quadratic-growth`](../../results/digit-count-section-forces-quadratic-growth.md), from the generic [`quadratic-separation-digit-count-sections`](../../results/quadratic-separation-digit-count-sections/README.md), formal); no finite single-exit interior in the joint graph ([`singleton-exit-separator-exclusion`](../../results/singleton-exit-separator-exclusion/README.md), numerically only `|J_D(b)| ≥ 2D + 1`); `|J_1(b)| ≥ 4` ([`first-shell-three-state-rigidity`](../../results/first-shell-three-state-rigidity/README.md)).
- **The best all-invariant result.** `kappa_h(D) − (D+1) → ∞` ([`additive-section-excess-unbounded`](../../results/additive-section-excess-unbounded/README.md)): an additive gain that still permits `D + √D`.
- **Restrictions on a hypothetical linear-growth invariant.** Short detection of every nonzero combination of depth-`A` sections within `O_C(√(A+1))` digits ([`linear-growth-short-detection`](../../results/linear-growth-short-detection.md)); arbitrarily late cuts with a uniform future cumulative bound ([`linear-growth-uniform-future-cuts`](../../results/linear-growth-uniform-future-cuts.md)); two-base automaticity is a single condition ([`reverse-closure-two-base-automaticity`](../../results/reverse-closure-two-base-automaticity.md)).
- **Refuted shortcuts.** Separate linear growth in two bases does not force periodicity ([`sparse-indicator-linear-growth-in-both-bases`](../../results/sparse-indicator-linear-growth-in-both-bases/README.md)); finite two-exit interiors cannot be excluded generically ([`two-exit-interior-counterexample`](../../results/two-exit-interior-counterexample/README.md)); local nonautomaticity with the first return identity allows `kappa = D + 3`, and linear growth need not produce a digit-count section (the section-graph and adjacent-11 controls, [`quantitative-rigidity-programme`](../../attempts/quantitative-rigidity-programme/README.md)).

## Suggested attacks

From the last batch (V009); none is supplied.
- **Delayed combinations.** Construct nonzero `g_j ∈ W_(A_j)(b)` from arbitrary nonconstancy and the full identities with `log(nu(g_j))/√(A_j + 1)` unbounded; their independent mixed sections would force an unbounded ratio ([`linear-growth-short-detection`](../../results/linear-growth-short-detection.md)).
- **Extend the return contraction** of [`additive-section-excess-unbounded`](../../results/additive-section-excess-unbounded/README.md) to several states per layer, without assuming bounded layer widths from cumulative growth (which [`linear-growth-uniform-future-cuts`](../../results/linear-growth-uniform-future-cuts.md) shows is not available).
- **Diagnostic** (side lane's D8, kept by the main lane as a progress diagnostic, not a success condition): `kappa_h(D) ≥ (1+ε)(D+1)` infinitely often for every nonconstant `h`, with a fixed `ε > 0`. Not reached.
- Do not proceed by excluding successive fixed boundary sizes, and keep whole-sequence distinctions (finite-prefix convergence cannot produce an automatic actual section). A finite-rank or Mahler extraction would need finite rank, which linear growth does not supply.

## History

- New node by the B16 migration (Claude, Opus 5.5) from the legacy brief `experiments/viewpoints/briefs/QUANTITATIVE_RIGIDITY_BRIEF.md` (now archived), the V005–V009 reports and the viewpoint map's "active V13 milestone", at commit `be73a66`. The side-lane control `reviews/side_lane/automatic_rigidity_control.*` (computed for the earlier "full automatic rigidity" proposal) moved here.
- Activated by the owner on 2026-10-18 after V004; worked by the main lane in five batches (V005–V009); replaced unresolved by the cycle-spectrum programme on 2026-10-19.
