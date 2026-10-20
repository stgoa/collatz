---
id: viewpoint-language-survey
kind: attempt
title: A breadth-first survey of fourteen candidate languages for Collatz, ending in the choice of invariant colourings
status: reviewed
claim: >
  Tried (2026-10-18, owner's "change of viewpoint" goal): compare fourteen candidate mathematical languages (cards
  V1-V14: parity coding, mixed-place affine cocycles, multiplicative semigroups, absorbing operators, orbit groupoids
  and currents, Dirichlet energy, proof rewriting, induced maps, relational abstraction, rational denominator
  layers, occupation measures, information of integer ensembles, arithmetic regularity of invariant colourings,
  binary/ternary carry diagrams), each with objects, gain, translated gap, worked example, 3x+d controls, cheapest
  test and a partial milestone, and test a shortlist with bounded exact probes. Verdict: no language supplied a new
  estimate on convergence; every card relocates the difficulty to integer realisation of symbolic objects or to
  uniform control of the non-absorbed set. The relational-history and graph-geometry shortlists were demoted after
  their tests; arithmetic regularity of invariant colourings (V13) was selected as a working language because it
  gave a checkable theorem (periodic invariant colourings of 3x+1 are constant), explicitly without any claim of
  better convergence prospects.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
certificates: [check_legacy_replay.py]
evidence:
  - "symbolic_arithmetic.md (V1-V3), operators_geometry.md (V4-V6), rewriting_renormalization.md (V7-V9), rational_layers.md (V10): first-round cards; statistical_languages.md (V11-V12): second-round cards; the V13 card is periodic-invariant-colourings-classification, the V14 card is in binary-ternary-carry-frontier"
  - "lifting_probe.md, summary_probe.md, potential_probe.md: the three V001 discrimination probes; relational_test.md, geometry_test.md: the V002 shortlist tests; SELECTION_REVIEW.md: the main lane's requirement-by-requirement selection review"
  - "viewpoint_v001_check.py, viewpoint_v001_check.json: side-lane check of the three probes and the 3x+d sublattice copy; it has no failure exit, so check_legacy_replay.py replays it and requires its receipt byte for byte"
  - "../../results/periodic-invariant-colourings-classification/verify_examples.py: the main-lane verifier replays the survey's finite examples (R81/R93 histories and the missing-guard example, cycle and entropy examples, inverse-tail entries, the carry trace)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: viewpoint_v001_check.py
    scope: "Side-lane referee sheet (VIEWPOINTS.md) and feed 18:24: a verdict per card (promising, relocates, equivalent, known dead end) with the closest literature; the lifting, Applegate-Lagarias and potential probes recomputed independently; V13 rated promising, V11, V12 and V14 relocate. Main corrected two side wordings (S1 is a dichotomy, not a zero-one law; the V3 verdict is not an impossibility claim), which the side lane accepted"
aliases: [V001, V002-b]
tags: [invariants, viewpoints, survey, languages, rejected-mechanism]
---

# A breadth-first survey of fourteen candidate languages for Collatz, ending in the choice of invariant colourings

## Idea

On 2026-10-18 the owner replaced the prove-or-narrow objective of the convergence programme (frozen at R94) with a breadth-first search for a better *language*: "Grothendieck-style" changes of viewpoint ([`VIEWPOINT_BRIEF.md`](../../../../archive/invariants-viewpoints/briefs/VIEWPOINT_BRIEF.md)). A successful language had to improve a checkable proof obligation or expose useful structure, not just carry the same missing premise under another name; finite calculations test a translation but establish no uniform bound; every claim had to behave correctly on the `3x+5` and `3x+61` cycle controls, failing there at a named hypothesis. Each card records seven fields: objects, structural gain, translated gap, worked example, cycle controls, cheapest test, and a genuinely partial milestone.

## What happened

**Round 1 (V001): ten cards and three probes.**

| View | What becomes clearer | What remains difficult | Decision |
|---|---|---|---|
| V1 [Parity coding](symbolic_arithmetic.md) | Dynamics becomes a shift; prefixes and tails are explicit | Which infinite codes come from positive integers | Supporting language; overlaps frozen prefix results |
| V2 [Mixed-place affine cocycles](symbolic_arithmetic.md) | Real size, binary legality, ternary endpoints and offsets kept together | A coupling bound beyond separate estimates | Keep as common arithmetic representation; no new inequality |
| V3 [Multiplicative semigroups](symbolic_arithmetic.md) | A relaxed factorisation problem is already solved | Legal ordering and state-dependent realisation | Defer: the inspected induction uses an unsupplied multiplication bridge |
| V4 [Absorbing operators](operators_geometry.md) | Survival of an input ensemble is one observable | A uniform estimate without arbitrary-target contraction | Keep as measurement language; no spectral-gap claim |
| V5 [Orbit groupoids and currents](operators_geometry.md) | Meeting lags, cycles and labels stay visible | An invariant beyond component and current algebra | Defer bare homology or categorical reformulations |
| V6 [Dirichlet energy](operators_geometry.md) | Finite access-to-1 probabilities with explicit boundary flux | Quantitative control as domains grow | Demoted after V002 |
| V7 [Proof rewriting](rewriting_renormalization.md) | Compatibility of certificate transformations | Universal discharge of remaining leaves | Tool only; confluence does not imply termination |
| V8 [Induced maps](rewriting_renormalization.md) | A long excursion becomes one parameterised branch | Leaving a guard need not reduce height | Defer; much is already done (R31, R77) |
| V9 [Relational abstraction](rewriting_renormalization.md) | Soundness, precision and counters explicit | A relation between unequal-time histories that survives composition | Demoted after V002: already in R81/R93 |
| V10 [Rational denominator layers](rational_layers.md) | Related maps become layers of one rational system | A property of the denominator-one layer forcing progress | Control bookkeeping |

The probes: **lifting** ([`lifting_probe.md`](lifting_probe.md)): for valuations `(1,4)` the exact map is `(9x+5)/32` on `x ≡ 3 (mod 64)`; keeping only the slope loses the offset, reversing the word changes it, modulus 32 wrongly admits 35 (actual word `(1,5)`), and an integral rational-factor step can be illegal (`10·(3/5) = 6`, but the shortcut image of 6 is 3); the Applegate–Lagarias step from `7 (mod 64)` multiplies by 5 and needs an unsupplied comparison between `x` and `5x`. **Loop summary** ([`summary_probe.md`](summary_probe.md)): on R31's guard an unbounded valuation counter decreases by 11 per block while height grows, proving exit from one guard, not descent. **Potential** ([`potential_probe.md`](potential_probe.md)): on `{1, 3, 5}` with conductance `1/n` the voltage at 3 and 5 is `1/(1 + 5T)` with `9/14 ≤ u ≤ 13/18`, below 1 because omitted inverse edges lead to escape; on the `d = 5` cycle the voltage is 0; positive voltage only certifies a path already known.

**Round 2 (V002): shortlist tests and four more cards.** Shortlist A, relational histories (V2 + V9, [`relational_test.md`](relational_test.md)): R81 already supplies the proposed guarded merger relation and R93 the compact asynchronous invariant; dropping guards admits illegal histories; no new closure. Shortlist B, graph geometry (V6 via V4, [`geometry_test.md`](geometry_test.md)): an inverse-conductance tail at most `4/(3n_0)` from the first omitted source, which holds on the cycle controls too; no growing-domain average. Both were demoted as scoped decisions, not impossibility theorems, and the survey expanded to V11 occupation measures and V12 information of integer ensembles ([`statistical_languages.md`](statistical_languages.md)), V13 arithmetic regularity of invariant colourings ([`periodic-invariant-colourings-classification`](../../results/periodic-invariant-colourings-classification/README.md)) and V14 carry diagrams ([`binary-ternary-carry-frontier`](../binary-ternary-carry-frontier/README.md)).

**Selection** ([`SELECTION_REVIEW.md`](SELECTION_REVIEW.md), 2026-10-18): recommend V13 as the working language, with one V14 probe and V12 as an independent statistical alternative. Three qualifications from the main lane's skeptical review were kept: working-language priority is supported, superior convergence prospects are not; a finite-state carry mechanism does not imply a finite ternary kernel; fixed-budget regular predecessor languages are prior work, and their union over unbounded budgets need not be regular.

## Why it fails

As a route to convergence, every card relocates the difficulty. The side lane's referee sheet summarised where it lands: **(I) integer realisation** (which 2-adic, rational or symbolic objects are actual positive-integer paths: V1, V2, V3, V8, V9, V10), or **(II) uniform control of the non-absorbed set** (V4, V6, V11, V12, and the earlier routes S and C); V5 and V7 are bookkeeping. The first round's information-loss lesson: simplifying a representation can discard exactly what is needed to recover an actual positive-integer path. These are scoped demotions of the tested proposals, not impossibility theorems for the fields named.

## What survives

- **V13**, which became the invariants area: [`periodic-invariant-colourings-classification`](../../results/periodic-invariant-colourings-classification/README.md), then [`binary-automatic-invariant-colourings-constant`](../../results/binary-automatic-invariant-colourings-constant/README.md) and the quantitative programme ([`quantitative-rigidity-programme`](../quantitative-rigidity-programme.md)).
- The two retained statistical targets, as questions: [`occupation-measure-tightness`](../../questions/occupation-measure-tightness.md) (V11) and [`capped-first-passage-power-bounds`](../../questions/capped-first-passage-power-bounds.md) (V12).
- The side lane's own cards (VIEWPOINTS.md): S1, the empty-or-positive-density dichotomy, which is the existing [`nonabsorbing-set-linear-lower-density`](../../../convergence/results/nonabsorbing-set-linear-lower-density/README.md) (retained by the main lane under historical C.2a, not as a fifteenth language); S2, ×2×3 rigidity as the theoretical home of V13, whose milestone is [`invariant-sets-meet-every-residue-class`](../../questions/invariant-sets-meet-every-residue-class.md).
- Exact fixtures: the R81 anchor (16 arrows), the R93 example (30 upper and 28 lower arrows), the `d = 5` cycle `19 → 31 → 49` with exact return `(27x + 95)/32`, the inverse-tail series, the entropy mergers (`{13, 53} → 5`, `{19, 81} → 31` at `d = 5`).
- V2 stays the arithmetic bookkeeping layer, V4 the survival observable, V10 the control index, V11 the check against losing mass at infinity. The remaining cards' milestones are templates, not ready programmes; they stay in the archived map ([`archive/invariants-viewpoints/MAP.md`](../../../../archive/invariants-viewpoints/MAP.md)).

## History

- New node by the B16 migration (Claude, Opus 5.5) from the V001 and V002 notes (legacy IDs V001; V002's survey part, here `V002-b`) and the viewpoint map's comparison table, at commit `be73a66`. All V001 notes and V002's `SELECTION_REVIEW.md`, `relational_test.md`, `geometry_test.md` and `statistical_languages.md` moved here; their links to legacy result paths were repointed to the corresponding nodes (link targets only). The side-lane check `reviews/side_lane/viewpoint_v001_check.*` moved here.
- Main lane (ChatGPT/Codex), 2026-10-18: V001 delivered at main `77ce821` (record `bff8938`), V002 at `cdfb143` (record `c47d91b`). Side-lane referee 18:24 and the referee sheet `archive/side_lane/VIEWPOINTS.md` (legacy path; placed in `archive/` by a later batch).
- **Link repair in kept notes (B16 migration, 2026-10-20).** In `SELECTION_REVIEW.md`, `geometry_test.md`, `operators_geometry.md`, `relational_test.md`, `rewriting_renormalization.md`, `statistical_languages.md`, `summary_probe.md`, `symbolic_arithmetic.md`, only link targets were changed: relative links to legacy paths now point to the corresponding nodes or to `archive/invariants-viewpoints/`. No text changed. Any `delivery_checks.json` hashes describe historical versions of these notes; no script in the repository checks them.
