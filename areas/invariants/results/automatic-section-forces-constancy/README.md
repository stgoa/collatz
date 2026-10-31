---
id: automatic-section-forces-constancy
kind: result
title: One automatic positive binary section of a 3x+1 invariant forces constancy, with a polynomial reconstruction bound
status: reviewed
claim: >
  Let h be a finite-valued colouring of the positive integers with h(2n) = h(n) (n >= 1) and h(3n+1) = h(n)
  (odd n > 1), h(0) = h(1), K_D(h) the binary sections of depth <= D and kappa_h(D) = |K_D(h)|. (a) If one section
  g(n) = h(2^K n + r), K >= 1, 0 < r < 2^K, is binary automatic, then h is constant; quantitatively
  kappa_h(D) <= 1 + (C_g kappa_g(D-1))^M for D >= 1, with M = 3^j and C_g determined by the cylinder. (b) For
  b(n) = h(2n+1), the joint sections b(2^i 3^j n + r) (i + j <= D) lie in K^+_(1+i+4j)(h), so J_D(b) is contained
  in K^+_(1+4D)(h), and K_D(h) = {h} union K_(D-1)(b); hence linear binary growth of h is equivalent to linear
  joint 2/3 growth of b. Part (a) uses V004 and so assumes Cobham's theorem; the reconstruction and (b) are
  elementary.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [binary-automatic-invariant-colourings-constant, positive-offset-kernel-ternary-closure, scalar-interface-three-identities, monochromatic-cylinder-forces-constancy]
certificates: [verify_examples.py]
evidence:
  - "direct_sections.md: the written proofs (local automaticity lemma, quantitative reconstruction, depth comparison, branching obligation); section_graph.md: the linear section-graph control; literature.md: the source audit and the sparse construction (node sparse-indicator-linear-growth-in-both-bases)"
  - "INDEPENDENT_REVIEW.md: main-lane independent agent review (PASS for the named partial results); side_review.md: the main lane's read of the side-lane feed and the Lean V004 assembly at sidekick 3b95686 / lean-lane b980e52"
  - "delivery_checks.json: historical delivery receipt; no script in the repository regenerates it"
aliases: [V005]
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Re-derived direct_sections.md sections 1-2 (reconstruction, closures, quantitative bound, depth comparison) and the section-graph control, re-ran verify_examples.py (PASS) and the V004 certificates, and tested the reconstruction and the inclusion (b) on the 3x+5 and 3x+13 which-cycle colourings; verdict HOLDS"
tags: [invariants, automatic, section-growth, quantitative-rigidity, conditional]
---

# One automatic positive binary section of a 3x+1 invariant forces constancy, with a polynomial reconstruction bound

## Statement

Conventions of the quantitative goal ([`section-count-depth-ratio-unbounded`](../../questions/section-count-depth-ratio-unbounded/README.md)): `h` finite-valued on the positive integers, `h(2n) = h(n)` for `n ≥ 1`, `h(3n+1) = h(n)` for positive odd `n > 1`, 1 absorbing, `h(0) = h(1)`;

```
K_D(h) = {n ↦ h(2^a n + r) : 0 ≤ a ≤ D, 0 ≤ r < 2^a},    kappa_h(D) = |K_D(h)|,
```

counting entire functions on `n ≥ 0`, never finite prefixes.

**(a) Local automaticity is global** (§1 below; proof in [`direct_sections.md`](direct_sections.md) §2). If one section `g(n) = h(2^K n + r)`, `K ≥ 1`, `0 < r < 2^K`, is binary automatic, then `h` is constant. Quantitatively, with constants `M = 3^j` and `C_g` determined by the chosen cylinder, `kappa_h(D) ≤ 1 + (C_g kappa_g(D−1))^M` for `D ≥ 1`. This is polynomial and does not exclude linear growth.

**(b) Joint growth** (§2 below; [`direct_sections.md`](direct_sections.md) §1 and [`scalar-interface-three-identities`](../scalar-interface-three-identities.md)). For `b(n) = h(2n+1)` let `J_D(b)` be all sections `b(2^i 3^j n + r)` with `i + j ≤ D`, `0 ≤ r < 2^i 3^j`. Then `J_D(b) ⊆ K^+_(1+4D)(h)` (sharper: depth `1 + i + 4j`), and `K_D(h) = {h} ∪ K_(D−1)(b)`, so `kappa_b(D−1) ≤ kappa_h(D) ≤ 1 + kappa_b(D−1)`. Linear binary growth of `h` is equivalent to linear growth of the joint binary/ternary section family of `b`.

## Proof

The legacy V005 report follows, lightly edited; the proofs are in the linked notes.

### The goal and why it is a further milestone

V004 excludes every finite-valued binary-automatic Collatz invariant. The
[activated brief](../../../../archive/invariants-viewpoints/briefs/QUANTITATIVE_RIGIDITY_BRIEF.md) asks for more:
if an invariant h is nonconstant, its number of distinct binary sections
through depth D must exceed every bound C(D+1), with C fixed. Write

```
K_D(h)={n -> h(2^a n+r):0<=a<=D,0<=r<2^a},
kappa_h(D)=|K_D(h)|.
```

Here h is finite-valued on positive integers, h(2n)=h(n) for n>=1, and
h(3n+1)=h(n) for positive odd n>1. Absorb at1 and extend h(0)=h(1).
Sections are entire functions on n>=0; agreement on a finite prefix is
not equality. The exact target is

```
h nonconstant => sup_D kappa_h(D)/(D+1)=infinity.
```

This excludes linearly growing descriptions without assuming any
regularity of the actual nonabsorbing set. It would leave more complicated
obstructions possible, so it is a genuine intermediate milestone. The
generic infinite-kernel bound kappa_h(D)>=D+1 does not meet it. Nor does
the goal ask for the stronger limit kappa_h(D)/(D+1)->infinity.

### What this batch establishes

#### 1. One automatic cylinder would force global constancy

The [direct section proof](direct_sections.md) shows: if even one section
g(n)=h(2^K n+r), K>=1 and 0<r<2^K, is binary automatic, then h is constant.
A fixed shortcut parity word reconstructs the coloring on every ternary
unit residue from actual binary sections of g. Affine extraction and
finite interleaving then reconstruct the odd section and h. V004 finishes.

Every reconstruction path respects absorption: its first K branch inputs
are above1, followed by an actual halving path ending at the target.
This uses a shortcut clock explicitly for the reconstruction; it does
not change any historical odd-only current convention.

There is also an all-depth quantitative version. For constants M=3^j and
C_g determined by the chosen cylinder, the written proof gives

```
kappa_h(D) <= 1+(C_g*kappa_g(D-1))^M, D>=1.
```

The proof specifies the constants, all residue pieces and offsets. This
is a polynomial reconstruction bound; it does not exclude linear growth.

#### 2. The strongest retained reduction uses joint section growth

For b(n)=h(2n+1), let J_D(b) contain all sections
b(2^i 3^j n+r), with i+j<=D and 0<=r<2^i 3^j. V004's algebra is valid
without finiteness and gives

```
J_D(b) subset K^+_(1+4D)(h).
```

The sharper individual depth bound is1+i+4j. Consequently linear binary
growth of h would imply linear growth of the **joint** binary/ternary
section family of b. This keeps the compatibility between the two bases.

The [complete scalar interface](../scalar-interface-three-identities.md) retains precisely
three identities, all n>=0:

```
b(3n)=b(4n),
b(3n+2)=b(2n+1),
b(4n+2)=b(n).
```

These are equivalent to the full invariant equations after extending b
by the odd part. Also K_D(h)={h} union K_(D-1)(b) for D>=1. This is a
faithful interface for a proof, not a solution of the growth problem.

#### 3. Two tempting shortcuts fail exactly

The [section graph](section_graph.md) has kappa(D)=D+3 for D>=3,
although every section is nonautomatic and it obeys doubling invariance
and the return identity h(8n+5)=h(2n+1). All infinite descendant families
overlap. It fails full Collatz invariance at9, where h(9)=1 and h(28)=0.
Thus local nonautomaticity and that return do not prove superlinear growth.

The [source audit and sparse construction](literature.md) give a second
control: the indicator of {6^(2^j):j>=0} is not eventually periodic but
has cumulative section counts at most5D+3 in base2 and3D+3 in base3.
Its joint section count is at least(D+1)(D+2)/2. Separate linear growth
in two bases therefore does not imply periodicity. This contradicts
Conjecture3.4 as printed in Bell's 2009 survey; no novelty or exhaustive
later-literature claim is made. The example fails doubling invariance
already at3 and6, so it does not refute the active goal.

## Certificates

- [`verify_examples.py`](verify_examples.py) (under a second): main-lane bounded replay against [`verification.json`](verification.json): 224 cylinder/residue choices, 896 actual paths, 15,288 shortcut arrows, 5,040 tuple decompositions, graph reachability through depth 16 with 120 state-distinguishing witnesses, 59,823 sparse-cell evaluations, and 45 mixed sections distinguished with 990 comparisons. Finite checks supplement the written universal arguments; they do not establish the desired complexity bound.

## Remarks

### Comparison and decision

The direct and literature notes retain seven-field candidate cards.
Their bounded parallel investigations, supplemented by root graph analysis,
lead to this decision:

| Mechanism | Demonstrated gain | Remaining obligation | Decision |
|---|---|---|---|
| Reconstruct from one cylinder | Local automaticity forces constancy; polynomial all-depth bound | Amplify the bound enough to exclude O(D) | Keep as a tool |
| Pack binary descendant families | m disjoint infinite families give coefficient at least m | Prove arbitrarily many disjoint families, or another overlap bound | Naive inference rejected by the exact graph |
| Separate two-base growth | Exact sparse counterexample | The generic implication itself is false | Reject |
| Joint binary/ternary growth | Linear binary growth transfers to the full joint family | Rigidity under all three scalar equations | Preferred next bounded probe |
| Finite-rank/Mahler extraction | A clear route if finite rank were proved | Linear state growth does not establish finite rank | Reserve mechanism, missing premise explicit |

The next investigation should test whether the three complete scalar
identities prevent the extensive overlaps that allow an infinite section
graph to grow only linearly. An alternative sufficient outcome would be
a proved theorem turning linear joint growth into a periodic section.
Do not assume that theorem or drop either additive equation. Compare these
two mechanisms before deepening; a new notation or another generic
infinite-kernel lemma does not advance the completion threshold.

### Controls, verification and external work

The d=5/61 divisibility indicators are actual nonconstant periodic
invariants, and their odd fixed cycles d->d avoid absorber1. The named
d1 additive identity fails there. The full target cannot simply be
asserted for all d. These controls exercise the relevant hypotheses;
they do not resolve hypothetical divergence.

The [independent review](INDEPENDENT_REVIEW.md) audits reconstruction,
the quantitative inequality, graph counting and the sparse construction.
The complete scalar converse also received an independent agent check.
Root and a separate reviewer replayed

```
python3 -B experiments/viewpoints/V005/verify_examples.py
```

The unchanged [receipt](verification.json) passed:224 cylinder/residue
choices,896 actual paths,15,288 shortcut arrows,5,040 tuple decompositions,
graph reachability through depth16 and120 state-distinguishing witnesses,
59,823 sparse-cell evaluations, and45 mixed sections distinguished with
990 comparisons. Finite checks supplement the written universal arguments.
They do not establish the desired complexity bound. Existing mathematical
code/evidence was untouched; the historical Phase6 gate was not rerun.

The [side review](side_review.md) pins sidekick at3b95686 and the Lean
lane atb980e52. The Lean assembly's inspected type matches V004 while
retaining Cobham as an explicit hypothesis. Its saved successful build,
axiom report and matching source hash were inspected; main did not
independently execute that Lean proof. It supplies no V005 growth bound.

### Completion audit

- **Progress:** local reconstruction, its all-depth bound, the full scalar
  interface and exact failures of two proposed shortcuts.
- **Still missing:** a proof that every nonconstant invariant has
  unbounded kappa_h(D)/(D+1). No result above implies this.
- **Status:** active, unresolved, with no external blocker. This is the
  first quantitative batch, not completion or a reason to lower the goal.
- **Preservation:** the R-series body, dispatcher and open LaTeX source
  remain frozen; [delivery checks](delivery_checks.json) record comparisons
  and local-link checks separately from mathematical verification.

### Dependency on Cobham

The legacy report carried a dated **dependency clarification (V008)**: the automatic-cylinder constancy conclusion uses V004 and therefore imports the published Cobham theorem; the affine reconstruction itself is elementary. This records a dependency already present in the proof, not a new hypothesis about the invariant. The side lane raised it (feed 22:32) and confirmed the clarification (feed 23:01). Here it is the `depends_on` entry [`binary-automatic-invariant-colourings-constant`](../binary-automatic-invariant-colourings-constant/README.md), whose `assumes` carries Cobham.

## History

- Migrated from `experiments/viewpoints/V005/REPORT.md` (legacy ID V005) at commit `be73a66`, by the B16 migration (Claude, Opus 5.5). Report text kept under Proof and Remarks; a Statement and Certificates were added. `scalar_interface.md` became [`scalar-interface-three-identities`](../scalar-interface-three-identities.md) (V005-a, formal); the sparse construction of `literature.md` §2 is [`sparse-indicator-linear-growth-in-both-bases`](../sparse-indicator-linear-growth-in-both-bases/README.md) (V005-b).
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `85a07c2`; the first batch of the quantitative-rigidity goal (`archive/invariants-viewpoints/briefs/QUANTITATIVE_RIGIDITY_BRIEF.md`). The side lane's referee (feed 22:10) called the batch "sound partial results" and checked the scalar interface and the sparse control; the Lean lane (iteration 6) found no error in the report. No proof-level review of the reconstruction lemma by another lane is on record, so the node stays `written`.
- **Link repair in kept notes (B16 migration, 2026-10-20).** In `INDEPENDENT_REVIEW.md`, `direct_sections.md`, only link targets were changed: relative links to legacy paths now point to the corresponding nodes or to `archive/invariants-viewpoints/`. No text changed. Any `delivery_checks.json` hashes describe historical versions of these notes; no script in the repository checks them.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No text changed. Findings in [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md): `C_g` depends on the chosen exponents `s_a` as well as on the cylinder; the Lean statement of the closure dependency is existential and does not expose the depth bound `a' <= a + 4` used in (b), which was re-derived; the inclusion (b) is not contradicted by the `3x+5` and `3x+13` controls.
