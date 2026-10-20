---
id: digit-count-section-forces-quadratic-growth
kind: result
title: A nonconstant 3x+1 invariant with one digit-count section has quadratically many binary sections
status: reviewed
claim: >
  Let h be a nonconstant finite-valued colouring of the positive integers with h(2n) = h(n) (n >= 1) and
  h(3n+1) = h(n) (odd n > 1), and kappa_h(D) its number of distinct binary sections of depth <= D. If one positive
  binary section has the form h(2^K n + r) = F(s_2(n)) with K >= 1, 0 < r < 2^K, then
  kappa_h(K + 4D) >= (D+1)(D+2)/2 for every D >= 0 (leading coefficient 1/32 in the depth). The step excluding an
  eventually periodic F goes through V005 and V004 and so assumes Cobham's theorem. No argument shows that an
  arbitrary invariant has such a section.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [quadratic-separation-digit-count-sections, automatic-section-forces-constancy, positive-offset-kernel-ternary-closure]
evidence:
  - "quadratic-separation-digit-count-sections/overlap.md section 3: the written corollary; section 4: the adjacent-11 control"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    scope: "Feed 22:26: 'The conditional consequence follows', using V004's factor-4 depth bound and V005's cylinder theorem; feed 22:32: the corollary inherits Cobham through V005/V004 (scope note, not an error)"
    link: ../../../archive/side-lane/FEED.md
  - by: Claude Lean lane (Fable)
    date: 2026-10-18
    scope: "Iteration 8: the depth accounting K + t + 4a matches the witnesses of kernel_ternary_closure (Case A a+v, Case B a-l+4); not formalised"
aliases: [V006-b]
tags: [invariants, digit-count, section-growth, quantitative-rigidity, conditional]
---

# A nonconstant 3x+1 invariant with one digit-count section has quadratically many binary sections

## Statement

Let `h` be a nonconstant finite-valued invariant colouring (`h(2n) = h(n)`, `h(3n+1) = h(n)` for odd `n > 1`, 1 absorbing) and suppose it has a positive binary section of digit-count type,

```
h(2^K n + r) = F(s_2(n)),     K ≥ 1, 0 < r < 2^K.                (8)
```

Then for every `D ≥ 0`

```
kappa_h(K + 4D) ≥ (D+1)(D+2)/2.                                   (9)
```

For every `N ≥ K` one may take `D = ⌊(N − K)/4⌋`, so the bound holds at all sufficiently large depths with leading lower-bound coefficient `1/32`. The same holds for a section `F(t_0 + s_2(n))` (absorb `t_0` into `F`).

## Proof

From [`overlap.md`](quadratic-separation-digit-count-sections/overlap.md) §3. If `F` were eventually periodic, `F(s_2(n))` would be binary automatic (an automaton can keep the exact digit count below the eventual cutoff and the count modulo the period above it), and the local automaticity lemma of [`automatic-section-forces-constancy`](automatic-section-forces-constancy/README.md) would make `h` constant. So for nonconstant `h`, `F` is not eventually periodic and [`quadratic-separation-digit-count-sections`](quadratic-separation-digit-count-sections/README.md) makes the states `Q_(a,t)` pairwise distinct. Each `Q_(a,t)` is an `h`-section of depth at most `K + t + 4a` by the exact mixed-section formulas of [`positive-offset-kernel-ternary-closure`](positive-offset-kernel-ternary-closure.md) (a ternary digit raises the binary depth by at most 4); the common bound `K + 4D` gives (9). ∎

## Remarks

- **Conditional on Cobham** through [`automatic-section-forces-constancy`](automatic-section-forces-constancy/README.md) and V004. With "`F` not eventually periodic" as an explicit hypothesis instead, the bound needs no Cobham.
- **The extraction gap.** Nothing shows that an arbitrary linearly growing binary-section graph contains a digit-count section, so (9) is a scoped gain, not the quantitative goal [`section-count-depth-ratio-unbounded`](../questions/section-count-depth-ratio-unbounded/README.md). The adjacent-11 control ([`overlap.md`](quadratic-separation-digit-count-sections/overlap.md) §4) shows extraction cannot follow from linear growth, doubling and the binary return alone: `z(n) = F(N_11(n))`, `F` the indicator of positive powers of 2 and `N_11` the number of adjacent 11 pairs, has `kappa_z(D) ≤ 2D`, obeys `z(2n) = z(n)` and `z(8n+5) = z(2n+1)`, has no digit-count section, and fails full invariance at 3 (`z(3) = 1`, `z(10) = 0`).
- The side lane found no nonconstant digit-count section in the actual `3x+5`, `3x+13`, `3x+61` cycle labellings it tested (feed 22:26).

## History

- New node by the B16 migration (Claude, Opus 5.5) from `experiments/viewpoints/V006/overlap.md` §3 and the V006 report §1 (legacy ID V006) at commit `be73a66`; the note stays in [`quadratic-separation-digit-count-sections`](quadratic-separation-digit-count-sections/README.md)'s folder.
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `ceebb93`. The Cobham dependence was added to the legacy report as a dated V008 clarification after the side lane's scope note (feed 22:32).
