---
id: singleton-exit-separator-exclusion
kind: result
title: The joint section graph of a nonconstant 3x+1 invariant has no finite forward interior with a single exit
status: reviewed
claim: >
  Generic theorem: on entire sequences with binary sections E_i (i = 0, 1) and ternary sections T_j (j = 0, 1, 2),
  which always satisfy the six radix identities T_j E_i = E_l T_k for 2j + i = 3l + k, assume (I): every reachable
  vertex has infinitely many distinct binary and infinitely many distinct ternary descendants. Then there is no finite
  nonempty set U of reachable vertices and vertex q outside U such that every transition from U lands in U union {q}
  and some transition lands at q. Application: for a nonconstant finite-valued 3x+1 invariant h, (I) holds for the
  joint graph of b(n) = h(2n+1), so no such single-exit interior exists at any depth; numerically this gives only
  |J_D(b)| >= 2D + 1, weaker than the generic binary bound after depth conversion. The generic theorem is elementary;
  the application derives (I) through V005 and V004 and so assumes Cobham's theorem.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [reverse-closure-two-base-automaticity, automatic-section-forces-constancy, binary-automatic-invariant-colourings-constant, positive-offset-kernel-ternary-closure]
evidence:
  - "separator.md: the written theorem (sections 1-4), reverse closure (section 1.1, node reverse-closure-two-base-automaticity), the exact gain (section 5); affine_growth.md: the parallel source audit (no applicable theorem turning a linear count of whole sections into automaticity)"
  - "INDEPENDENT_REVIEW.md: main-lane second-agent review; side_review.md: the main lane's read of the side-lane feed at sidekick bc76c7d"
  - "delivery_checks.json: historical delivery receipt; no script in the repository regenerates it"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-18
    scope: "Iteration 8, second read (main b24020f): separator.md sections 2-4 checked step by step (boundary polynomial identity, unique escaping binary digit, propagation, residue-set equation, the lock to (0,0) or (1,2), the T_1-closed finite set and the two evaluation formulas) and the reverse-closure table; no error. Scope point: the Collatz application is conditional on Cobham, the theorem under (I) is unconditional"
  - by: Claude side lane (Opus)
    date: 2026-10-18
    scope: "Feed 22:40 (REFEREE V007): reverse closure checked by hand (all four cases and offset bounds); the singleton theorem is generic and applied to Collatz through (I); same Cobham scope note"
    link: ../../../../archive/side-lane/FEED.md
aliases: [V007]
tags: [invariants, section-graph, quantitative-rigidity, separators, conditional]
---

# The joint section graph of a nonconstant 3x+1 invariant has no finite forward interior with a single exit

## Statement

From [`separator.md`](separator.md) §1. Use the five transitions and six identities of the joint section graph ([`graph_interface.md`](../quadratic-separation-digit-count-sections/graph_interface.md)):

```
E_i(s)(n) = s(2n+i),     i = 0, 1,
T_j(s)(n) = s(3n+j),     j = 0, 1, 2,
T_j(E_i(s)) = E_l(T_k(s))   whenever 2j + i = 3l + k.
```

Vertices are entire sequences: unequal vertices differ at some integer. **Infinitude hypothesis (I):** every reachable vertex has infinitely many distinct binary descendants and infinitely many distinct ternary descendants (descendants include the vertex itself and use only the indicated radix).

**Theorem.** Under (I), there is no finite nonempty set `U` of reachable vertices and vertex `q ∉ U` such that every transition from `U` lands in `U ∪ {q}` and some transition from `U` lands at `q`. This includes a singleton distance layer: if `B_(d+1) \ B_d = {q}`, take `U = B_d`.

**Application.** For a nonconstant finite-valued Collatz invariant `h`, [`automatic-section-forces-constancy`](../automatic-section-forces-constancy/README.md) excludes binary automaticity of every positive binary section, [`reverse-closure-two-base-automaticity`](../reverse-closure-two-base-automaticity.md) (§1.1) excludes ternary automaticity, and V004 represents every joint section as a positive binary section, so (I) holds for the whole joint graph of `b(n) = h(2n+1)`. Its numerical consequence is only `|J_D(b)| ≥ 2D + 1`.

## Proof

The written proof is [`separator.md`](separator.md) §§2–4: a single exit propagates unless one radix already closes (§2); an infinite one-vertex extension has only two possible tails, locking to `(0,0)` or `(1,2)` (§3); in both tails a finite orbit under the middle ternary digit makes entire section sequences repeat, contradicting the required new vertices (§4). The legacy V007 report follows, lightly edited.

### Result and why it matters

The [written theorem](separator.md) excludes a finite forward interior
with exactly one exit in the joint binary/ternary section graph of a
nonconstant invariant. The interior may occur at any depth and may have
arbitrary finite size. Every arrow returning to the interior is retained.

The argument first supplies the missing symmetry between the two bases:
any positive binary section which is ternary-automatic would also force
global constancy. Consequently every joint vertex has infinitely many
descendants in each base separately. The six exact radix identities then
force a hypothetical single exit to propagate along one of two possible
tails. In both tails a finite orbit under the middle ternary digit makes
entire section sequences repeat, contradicting the required new vertices.

This is a structural exclusion for every invariant under investigation.
It does not require the extra digit-count hypothesis in V006. However its
numerical consequence is only

```
|J_D(b)| >= 2D+1,                  b(n)=h(2n+1).
```

The conversion `J_D(b) subset K_(1+4D)^+(h)` therefore gives a binary
lower bound weaker than the generic `kappa_h(D)>=D+1`. No improved binary
growth rate is claimed. Linear joint growth with a larger coefficient
could still have layers with two or more vertices.

## Remarks

### Comparison and next decision

The parallel [source audit](affine_growth.md) found no applicable theorem
turning a linear count of whole sections into automaticity. Global
extension conditions on decorated trees and automaticity modulo
density-zero errors require premises not supplied by the count or cut.
This is a bounded literature assessment, not an exhaustive absence claim.

Retain the full high-level goal: prove that every nonconstant finite-valued
invariant has unbounded `kappa_h(D)/(D+1)`. The next bounded test should
retain the identity of each state in a two-exit boundary, and ask whether
the radix equations force a finite orbit. A two-exit result alone would
also be partial. Completion needs all possible linear coefficients, via
an arbitrary finite-width argument or another growth mechanism.

The singleton proof uses a scalar indicator polynomial because every
exit from the interior reaches the same state. Several exits require
equations retaining their distinct destinations. Collapsing them to a
Boolean union would lose the information that made the proof work.

### Verification and controls

Root independently checked the full singleton argument and reverse-closure
formulas. The second lane independently checked reverse closure; its
final theorem review is recorded in [INDEPENDENT_REVIEW.md](INDEPENDENT_REVIEW.md).
These are written mathematical reviews, not formal Lean verification.
No finite prefix agreement is used to identify entire sequences.

For the generalized odd map with d=5 or61, the invariant
`h_d(n)=1_(d divides n)` for positive n (and `h_d(0)=h_d(1)=0`) has finite
kernels. Its positive component contains the fixed odd cycle d, since
`(3d+d)/4=d`. Thus it fails the infinitude hypothesis of the theorem.
The d=1 scalar equation also actually fails on these controls: at n=3,
`b_5(3n)=0` and `b_5(4n)=1`; at n=10, `b_61(3n)=1` and `b_61(4n)=0`.
Absorber1 is retained, and no cycle containing1 is used as a witness.

No existing mathematical code or evidence was changed. Verification for
this prose-only batch consists of the symbolic reviews, explicit control
calculations, link checks and frozen-file comparisons; the historical
Phase6 finite gate was not rerun. Correctness, novelty and usefulness for
convergence remain separate questions. Novelty and human review are
unclaimed.

### External input

The [side review](side_review.md) records fetched pin
`bc76c7d3f3d31c109d63984c595866ba9054aef3`. The latest feed reproduces V006's
scoped result and reports a Lean scalar-interface check. Main did not
independently replay that Lean artifact in this batch. It supplies no
quantitative estimate and does not change the completion condition.

### Dependency on Cobham

The legacy report and `separator.md` carried a dated **dependency clarification (V008)**: the generic separator theorem under infinitude in both bases is elementary; obtaining that infinitude from Collatz invariance invokes V005/V004, including the published Cobham theorem, so the Collatz application inherits that classical input. The Lean lane (iteration 8) and the side lane (feed 22:40) raised this independently; the original V007 text did not mention Cobham.

The side lane's calibration (feed 22:40): three batches (V005–V007) were each sound, and none improved the generic all-invariant bound; it proposed direction D8 (the `(1+ε)` diagnostic), see [`quantitative-rigidity-programme`](../../attempts/quantitative-rigidity-programme/README.md).

## History

- Migrated from `experiments/viewpoints/V007/REPORT.md` (legacy ID V007) at commit `be73a66`, by the B16 migration (Claude, Opus 5.5). Report text kept under Proof and Remarks; Statement added from `separator.md` §1. The reverse-closure lemma (`separator.md` §1.1, Lean V007-a) is the node [`reverse-closure-two-base-automaticity`](../reverse-closure-two-base-automaticity.md). The Lean lane queued the singleton theorem itself as the larger unit V007-b; it was not formalised.
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `b24020f`; the third batch of the quantitative goal.
- **Link repair in kept notes (B16 migration, 2026-10-20).** In `affine_growth.md`, `separator.md`, `side_review.md`, only link targets were changed: relative links to legacy paths now point to the corresponding nodes or to `archive/invariants-viewpoints/`. No text changed. Any `delivery_checks.json` hashes describe historical versions of these notes; no script in the repository checks them.
