# V007 — The first finite-separator obstruction

**Progress; the full quantitative goal remains active and unresolved.**
V006 was delivered at `ceebb935137fc9e153b558ec6a2a4a66ce010395`.
This bounded pass addresses its proposed singleton separator test. It
does not assume a digit-count section, regularity of the nonabsorbing set,
or a classification of every graph with linear growth.

## Result and why it matters

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

## Comparison and next decision

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

## Verification and controls

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

## External input

The [side review](side_review.md) records fetched pin
`bc76c7d3f3d31c109d63984c595866ba9054aef3`. The latest feed reproduces V006's
scoped result and reports a Lean scalar-interface check. Main did not
independently replay that Lean artifact in this batch. It supplies no
quantitative estimate and does not change the completion condition.
