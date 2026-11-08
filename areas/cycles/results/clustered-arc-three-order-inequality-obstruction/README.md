---
id: clustered-arc-three-order-inequality-obstruction
kind: result
title: Three clustered-arc gap systems force a positive error margin
status: written
claim: >
  Pure real algebra, with no orbit, map or clock assumption. Let
  a,c,u,v,epsilon be real numbers, a>=1, c>=1, r=a+c, and r*u<1.
  If any one of the three displayed gap-witness inequality systems
  holds, then epsilon>1/(104*r). The first system implies the same
  conclusion without r*u<1. The statement starts from the raw gap
  inequalities and derives their positive polynomial combinations.
  It does not establish that a geometric profile satisfies one of
  these systems and does not assert any cycle exclusion.
authors:
  - Codex signed-endpoint formalisation lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
assumes: [mathlib-065356127b1d]
lean:
  - LeanLane.ClusterInequalities.first_order
  - LeanLane.ClusterInequalities.second_order
  - LeanLane.ClusterInequalities.third_order
  - LeanLane.ClusterInequalities.three_order_obstruction
evidence:
  - "../../../../lean/receipts/ClusterInequalities.build.txt: pinned library build"
  - "../../../../lean/receipts/ClusterInequalities.axioms.txt: every new theorem's axiom report"
  - "../../../../lean/receipts/ClusterInequalities.sha256.txt: compiled source hash"
tags: [cycles, real-inequalities, clustered-arcs, polynomial-positivity, lean]
---

# Three clustered-arc gap systems force a positive error margin

## Statement

Let `a,c,u,v,epsilon` be real numbers satisfying

```
a>=1, c>=1, r=a+c, r*u<1.
```

Consider the following three alternative systems. Fractions are
ordinary real division; in particular `r>=2`.

**First order:**

```
v-c*u       <= (3/8)*(v-(c-1)*u)+epsilon,
1-a*u-v     <= (3/8)*(a/r-(a-1)*u)+epsilon,
a*u         <= 3/(8*r)+epsilon.                         (I)
```

**Second order:**

```
v-c*u       <= (3/8)*(v-(c-1)*u)+epsilon,
1-v         <= 3/(8*r)+epsilon.                         (II)
```

**Third order:**

```
1-a*u       <= (3/8)*(1-(a-1)*u)+epsilon.                (III)
```

If at least one of `(I)`, `(II)`, `(III)` holds, then

```
epsilon > 1/(104*r).                                   (1)
```

The conclusion from `(I)` does not require `r*u<1`.
No sign or integrality condition on `u,v,epsilon` is needed.
The names of the systems record their geometric origin, not
additional order hypotheses in this algebraic statement.

## Proof

Suppose instead `epsilon<=1/(104*r)`. Since `r>0`,

```
r*epsilon <= 1/104.                                    (2)
```

For `(I)`, move each inequality to the left and clear the
positive denominator `r` in the second and third. The three
resulting expressions are nonpositive:

```
H1 = (5/8)*v-((5/8)*c+3/8)*u-epsilon,
H2 = r-r*v-r*((5/8)*a+3/8)*u-(3/8)*a-r*epsilon,
H3 = a*r*u-3/8-r*epsilon.
```

Put

```
T = (5/8)*a+c+39/40,
C = (129/40)*a+c+39/40,
L0 = (5/8)*a^2+a*c-(15/64)*a-(3/8)*c-117/320.
```

All three weights in the following identity are positive:

```
(8/5)*a*r*H1+a*H2+T*H3 = L0-r*C*epsilon.
```

Thus `L0<=r*C*epsilon<=C/104`, using `(2)` and `C>0`.
But the exact polynomial identity

```
L0-C/104 = 3/5+(129/65)*(a-1)+(8/13)*(c-1)
            +(5/8)*(a-1)^2+(a-1)*(c-1)
```

has a strictly positive right side. This is a contradiction.

For `(II)`, keep `H1` and let
`H2'=r-r*v-3/8-r*epsilon`. Their positive combination is

```
(8/5)*r*H1+H2'
 = a-39/40-(13/5)*r*epsilon+(c+3/5)*(1-r*u) <= 0.
```

The first three terms are at least `a-1>=0`, because
`39/40+(13/5)/104=1`. The last product is strictly positive
by `c>=1` and `r*u<1`, again a contradiction.

For `(III)`, multiply its rearranged left side by `r>0`:

```
(5/8)*c-3/8-r*epsilon
  +((5/8)*a+3/8)*(1-r*u) <= 0.
```

Its first line is at least `1/4-1/104=25/104>0` by `(2)`
and `c>=1`. Its final product is positive by `a>=1` and
`r*u<1`. This proves `(1)` in the remaining case.

## Lean

The module
[`LeanLane/ClusterInequalities.lean`](../../../../lean/LeanLane/ClusterInequalities.lean)
defines `FirstSystem`, `SecondSystem` and `ThirdSystem`
exactly as `(I)`, `(II)`, `(III)`, substituting `a+c` for
`r`. All five variables have type `Real`. The theorems
`first_order`, `second_order` and `third_order` prove the
three implications, with precisely the hypotheses stated
above. `three_order_obstruction` takes their disjunction
and proves `(1)`.

The auxiliary lemmas `scaled_error_le` and `residual_pos`
prove `(2)` and positivity of `L0-C/104`. The case proofs
start from the displayed raw systems; no eliminated
inequality or positive residual is an assumed hypothesis.

Build from `lean/` with `lake build LeanLane`; directly
replay the module and its six axiom reports with
`lake env lean LeanLane/ClusterInequalities.lean`.
The [build receipt](../../../../lean/receipts/ClusterInequalities.build.txt),
[axiom receipt](../../../../lean/receipts/ClusterInequalities.axioms.txt)
and [source hash](../../../../lean/receipts/ClusterInequalities.sha256.txt)
bind these checks to the source. The library-root
[build receipt](../../../../lean/receipts/LeanLane.build.txt)
and [source hash](../../../../lean/receipts/LeanLane.sha256.txt)
bind its import to the same library build. Run
`python3 tools/check_lean_receipts.py` from the repository
root to audit the recorded hashes and permitted axioms.

The sole external input is the pinned
[Mathlib library](../../../../sources/mathlib-065356127b1d.md).
This node remains `written` until the Lean build passes CI.

## Remarks

These systems are the algebraic step in section 3 of
[`clustered-two-maximum-arcs-exclusion`](../clustered-two-maximum-arcs-exclusion/README.md).
That node derives them from the three strict boundary
orders of a clustered two-arc profile. The present proof
is self-contained from the systems themselves, so it does
not inherit the external cycle estimates used there.

The geometry establishing the witness systems, alignment
at a global profile minimum, transfer to actual odd-only
cycles, and all numerical cycle exclusions are outside
this formal statement. The earlier result retains its
own status and assumptions. This pure algebra theorem
does not exclude any `3x+d` cycle or impose `d=1`; the
actual `3x+5,7,13,61` controls are therefore unaffected.
Novelty undetermined; this is a formalisation of the
existing written algebraic argument.

## History

- 2026-11-08: isolated the complete three-order real
  inequality obstruction from the clustered-profile proof.
