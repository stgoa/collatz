---
id: invariant-sets-meet-every-residue-class
kind: question
title: Does every nonempty union of 3x+1 orbit components meet every residue class modulo every M?
status: open
claim: >
  For the 3x+1 map on the positive integers, let B be a nonempty union of orbit components (closed under the forward
  map and under all inverse branches; 1 absorbing). Prove or refute that B meets every residue class modulo every
  M >= 1. Implied by convergence (which makes the set of all positive integers the only such B); the side lane rated
  it strictly weaker than convergence, and it is stronger than the periodic classification, which says only that a
  nonempty proper B cannot be a union of residue classes; a positive answer rules out every congruence-based
  isolation of a counterexample. The
  3x+d analogue fails for d > 1 (the multiples of d form an invariant union of components avoiding the nonzero
  classes mod d).
created: 2026-10-18
aliases: [VP-S2]
tags: [invariants, viewpoints, residues, profinite, rigidity, open]
---

# Does every nonempty union of 3x+1 orbit components meet every residue class modulo every M?

## Question

As in the claim: the "intermediate milestone" of the side lane's viewpoint card S2 (×2×3 rigidity as a theoretical home for V13; side-lane referee sheet [`archive/side-lane/VIEWPOINTS.md`](../../../archive/side-lane/VIEWPOINTS.md), and feed 19:13 of 2026-10-18 in [`archive/side-lane/FEED.md`](../../../archive/side-lane/FEED.md)). The side lane proposed it as a bounded computation plus a V13-style argument; residue-level closure needs the parity and mod-3 data of members, so work modulo `6M`.

## Why it matters

The S2 card places the invariants area inside a classical rigidity theme for the multiplicatively independent pair 2, 3: Furstenberg (1967) on closed subsets of the circle invariant under ×2 and ×3, Rudolph (1990) on measures, and Cobham (1969) as the automata analogue, already used by [`binary-automatic-invariant-colourings-constant`](../results/binary-automatic-invariant-colourings-constant/README.md). The periodic classification [`periodic-invariant-colourings-classification`](../results/periodic-invariant-colourings-classification/README.md) is the clopen case on the profinite integers: for `d = 1` no nonconstant clopen invariant set exists, while for `3x+d` with `d > 1` the clopen set `dẐ` is invariant under `x ↦ 2x`, `x ↦ 3x` and `x ↦ 3x + d`; the `+1` is the affine twist, measured by the commutator shift by `d`. This question asks for density in `Ẑ` of every nonempty invariant set, which is more than "not equal to a periodic set".

The card's own translation of the obstacle: rigidity theorems control closed sets and measures, while a hypothetical bad set is a discrete subset whose closure in `Ẑ` can be all of `Ẑ` while the set stays thin; so even a positive answer does not reach convergence, and the difficulty lands again at integer realisation and uniform control of the non-absorbed set.

## Known progress
- **Proved for every `M ≤ 100`** ([`saturated-sets-meet-residue-classes-small-moduli`](../results/saturated-sets-meet-residue-classes-small-moduli/README.md)) by a finite closure search over residues (budgets: at most one halving and six inverse steps; `2^k` needs `k` inverse steps, `3^k` one halving and one inverse step); the same search fails for `3x+5` at `M = 5`, as it must.
- **Proved for every modulus `2^k·3^b`** ([`saturated-sets-meet-residue-classes-six-smooth-moduli`](../results/saturated-sets-meet-residue-classes-six-smooth-moduli/README.md)): every nonempty saturated set is dense in `Z_2 × Z_3`. The proof is an induction on `k` whose lift step (`j = v_2(3u+1)` doublings and one inverse step) works for any extra modulus `M′` prime to 6, so the question reduces to its base case: odd elements in every joint class modulo `3^b·M′`. For moduli with a prime factor `≥ 5` only the finite verification `M ≤ 100` is known, and no uniform bound on the inverse depth is proved.
- Before that, only probes: the side lane checked the `d = 1` clopen statement for `M ≤ 400` (its V13 check, now [`v13_coloring_check.py`](../results/periodic-invariant-colourings-classification/v13_coloring_check.py)). The `3x+d` sublattice copy (`S_d(dy) = d·S_1(y)`) was checked for `d ∈ {5, 7, 13, 61}` and `y < 10^4` in the side lane's V001 probe ([`viewpoint_v001_check.py`](../attempts/viewpoint-language-survey/viewpoint_v001_check.py)). Novelty and difficulty are undetermined; the card proposed a literature check first.

## Suggested attacks

From the card: (i) a literature check on affine-semigroup versions of Furstenberg's theorem on `Ẑ` or on solenoids, and whether the Collatz affine pair appears there; (ii) the finite question modulo `6M`, combining residue-graph computation with the commutator argument of the periodic classification. Mark any extension beyond these as speculation.

## History

- New node by the B16 migration (Claude, Opus 5.5) from the side lane's card S2 (Claude side lane, Opus, 2026-10-18 19:13; [`archive/side-lane/VIEWPOINTS.md`](../../../archive/side-lane/VIEWPOINTS.md), legacy path `archive/side_lane/VIEWPOINTS.md`) at commit `be73a66`. The side lane's other card, S1 (formerly labelled V11 on its sheet), is the same statement as [`nonabsorbing-set-linear-lower-density`](../../convergence/results/nonabsorbing-set-linear-lower-density/README.md) and is not a separate node.
- 2026-10-31: Known progress gains the finite verification for `M ≤ 100` (Claude cycles lane, Fable 5.1).
- 2026-10-31, later: Known progress gains the proof for all moduli `2^k·3^b` and the reduction of the general case to its base case (Claude cycles lane, Fable 5.1).
