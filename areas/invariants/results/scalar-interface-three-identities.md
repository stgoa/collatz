---
id: scalar-interface-three-identities
kind: result
title: Three identities on the odd values are equivalent to 3x+1 invariance of a colouring
status: formal
claim: >
  For any sequence b on n >= 0 (any value set) put h(0) = b(0) and h(n) = b((oddpart(n) - 1)/2) for n > 0, so that
  h(0) = h(1), h(2n) = h(n) and h(2n+1) = b(n). Then h(3n+1) = h(n) for every positive odd n > 1 if and only if
  b(3n) = b(4n), b(3n+2) = b(2n+1) and b(4n+2) = b(n) for all n >= 0. Consequently these three identities on b
  correspond bijectively to invariant colourings of the positive integers (h -> n -> h(2n+1) and b -> h being
  mutually inverse there), and they imply b(3n+1) = b(16n+8). No finiteness or convergence is used.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
lean:
  - LeanLane.Scalar.ext_tri_iff
  - LeanLane.Scalar.scalar_interface_iff
  - LeanLane.Scalar.ext_tri
  - LeanLane.Scalar.ext_three_mul_add_two
  - LeanLane.Scalar.ext_odd_values
  - LeanLane.Scalar.v004_relation
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    scope: "Feed 22:10: the converse checked by hand (strong induction on E(m), cases m odd, 4l, 4l+2); feed 22:26: Lean V005-a read from source and receipts, statement match, orientation b(3n) = b(4n) and ext b 0 = b 0 confirmed"
aliases: [V005-a]
tags: [invariants, scalar-interface, colourings, formal]
---

# Three identities on the odd values are equivalent to 3x+1 invariance of a colouring

## Statement

Let b be any finite-valued sequence on n>=0. Set h(0)=b(0) and, for n>0,

```
h(n)=b((oddpart(n)-1)/2).
```

Then h(0)=h(1), h(2n)=h(n), and h(2n+1)=b(n). The remaining invariant
equation `h(3n+1)=h(n)` at positive odd n>1 is equivalent to the following
three identities, all for n>=0:

```
b(3n)=b(4n),
b(3n+2)=b(2n+1),
b(4n+2)=b(n).                                      (1)
```

The forward implication is the V004 algebra. The omitted odd source1
equation is already the valid color equality h(4)=h(1).

## Proof

For the converse prove E(n): `h(3n+2)=b(n)` by strong induction. E(0)
is h(2)=h(1)=b(0). If n=2m+1, then

```
h(3n+2)=h(6m+5)=b(3m+2)=b(2m+1).
```

If n=4m, use doubling and the first identity:

```
h(3n+2)=h(12m+2)=h(6m+1)=b(3m)=b(4m).
```

If n=4m+2, use E(m) and the third identity:

```
h(3n+2)=h(12m+8)=h(3m+2)=b(m)=b(4m+2).
```

Here m<n, so the induction is valid. Thus E holds everywhere, and

```
h(3(2n+1)+1)=h(6n+4)=h(3n+2)=b(n)=h(2n+1).
```

This gives the full invariant coloring. No orbit convergence or finite
kernel was used. The additional V004 relation
`b(3n+1)=b(16n+8)` now follows; it need not be an extra assumption.

## Lean

Lean unit V005-a, [`lean/ScalarInterface.lean`](../../../lean/ScalarInterface.lean) (receipts `lean/receipts/ScalarInterface.*`; axioms `propext`, `Classical.choice`, `Quot.sound`, `v004_relation` only `propext`, `Quot.sound`), namespace `LeanLane.Scalar`. `ext b x := b ((oddPart x − 1)/2)` with `oddPart n := n / 2^(v₂ n)` is the prose `h` (at `x = 0` truncated subtraction gives `b 0`, as in the prose: `ext_zero`, `ext_one`). `ext_tri_iff` is exactly the stated equivalence, proved by the same `E(m)` induction (`ext_three_mul_add_two`, cases `m` odd / `4l` / `4l+2`) and, forward, by the V004 algebra (`id1/id2/id3_of_colouring`, the `B4/B2/B1` of V004-i re-proved so the file is self-contained; the prose orientation `b(3n) = b(4n)` is used). Beyond the prose: `ext_tri` shows the rule then holds at every odd `n`, including `n = 1` (the prose's "omitted odd source 1 equation"); `scalar_interface_iff` packages the interface as "`b` satisfies the identities iff `b` is the odd-value sequence of some invariant colouring"; `ext_odd_values` (`ext (n ↦ h(2n+1)) x = h x` for `x > 0`, using only `h(2n) = h(n)`) with `ext_two_mul_add_one` makes the two passages mutually inverse on `n ≥ 1`; `v004_relation` is `b(3n+1) = b(16n+8)`. **Statement match:** exact for the claim; "finite-valued" is not needed (`α` is arbitrary). The complexity comparison (2) in the Remarks and everything about growth is **not** formalised.

## Remarks

### Exact complexity comparison (written, not formalised)

For D>=1 the positive-offset h-sections through depth D are exactly the
binary b-sections through depth D-1. In one direction strip the power of2
from the positive offset; in the other direction use

```
b(2^a*n+r)=h(2^(a+1)*n+2r+1).
```

The zero-offset sections of h all equal h. Therefore

```
K_D(h)={h} union K_(D-1)(b),
kappa_b(D-1) <= kappa_h(D) <= 1+kappa_b(D-1).           (2)
```

Combined with the depth comparison in [direct_sections.md](automatic-section-forces-constancy/direct_sections.md) (node [`automatic-section-forces-constancy`](automatic-section-forces-constancy/README.md)),
this makes linear binary growth of h equivalent to linear joint2/3 section
growth of b under (1). The unresolved target is to prove that a nonconstant
finite-valued b satisfying (1) cannot have that growth. Stating this
equivalence does not prove the required exclusion.

The [graph control](automatic-section-forces-constancy/section_graph.md) retains only the third relation of
(1), and fails the first at n=1. Its linear count is therefore a useful
test against discarding part of the interface, not a counterexample to it.

## History

- Migrated from `experiments/viewpoints/V005/scalar_interface.md` (legacy ID V005; Lean unit V005-a) at commit `be73a66`, by the B16 migration (Claude, Opus 5.5). Text kept; split into Statement, Proof and Remarks. The legacy status line read "written equivalence, independently agent-reviewed … a precise interface for the next growth argument, not a new convergence criterion or completion of the quantitative goal."
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `85a07c2`. Lean V005-a verified 2026-10-18 (Lean lane iteration 7, `claude/lean-lane` `3dd6cb7`; side-lane check, feed 22:26).
