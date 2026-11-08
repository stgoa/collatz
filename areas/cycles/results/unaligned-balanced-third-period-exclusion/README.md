---
id: unaligned-balanced-third-period-exclusion
kind: result
title: Unaligned balanced third-period words exclude denominator one
status: written
claim: >
  In the raw odd-only clock, let u,v be finite lists of positive
  integers, possibly empty, and let a,b,delta>=1. Put A=(u,a),
  B=(v,b+delta), and W=A[+delta] B A B[-delta] A B, where bracketed
  changes affect only the final letter. No positive odd integer
  3x+1 cycle follows W with period |W|. Equivalently, for this word
  family, D_W>0 implies D_W does not divide C_W, hence den(W)>1.
  There is no primitivity, block-length, defect-size, or state-bound
  assumption. The theorem concerns this explicit six-block family;
  it does not formalize the reduction of all four-mismatch
  third-period words to aligned and unaligned placements.
authors:
  - Codex signed-endpoint formalisation lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex cycle-frontier lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex residue lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [doubled-word-cancellation-formula]
assumes: [mathlib-065356127b1d]
lean:
  - LeanLane.ThirdPeriod.no_positive_odd_cycle
  - LeanLane.ThirdPeriod.discriminant_not_dvd_intercept
evidence:
  - "../../../../lean/receipts/ThirdPeriod.build.txt: pinned library build"
  - "../../../../lean/receipts/ThirdPeriod.axioms.txt: every new theorem's axiom report"
  - "../../../../lean/receipts/ThirdPeriod.sha256.txt: compiled source hash"
tags: [cycles, denominators, third-period, balanced-defects, lean]
---

# Unaligned balanced third-period words exclude denominator one

## Statement

Use the shared valuation-word conventions

```
C_[] = 0,   C_(a::w) = 3^|w| + 2^a C_w,
D_w = 2^sum(w) - 3^|w|,
den(w) = D_w / gcd(C_w,D_w)       when D_w>0.
```

Let `u,v` be positive-integer lists, possibly empty, and let
`a,b,delta>=1`. Define

```
A = (u,a),        B = (v,b+delta),
W = (u,a+delta) B A (v,b) A B.                         (1)
```

Thus every modified letter remains positive. There is no positive
odd integer sequence `x_i`, periodic with period `|W|`, satisfying

```
2^(W_(i mod |W|)) x_(i+1) = 3x_i+1.
```

Also, `D_W>0` implies `D_W` does not divide `C_W`, or equivalently
`den(W)>1`. No minimal-period hypothesis is needed.

This is the complete unaligned six-block branch of
[the balanced third-period result](../balanced-third-period-denominator-law/README.md).
The placement classification and aligned branch of that broader
result remain outside this formal statement.

## Proof

Write

```
l=|A|, n=|B|, g=l+n, T=sum(A)+sum(B),
alpha=3^l, beta=3^n, Q=2^sum(A), S=2^sum(B),
P=alpha beta=3^g, Z=QS=2^T, k=2^delta,
C=C_A, E=C_B, X=beta C, Y=QE,
Phi=P^2+PZ+Z^2, R=PX-ZY.
```

The word in (1) has length `3g` and valuation sum `3T`.
Changing a final letter leaves its intercept unchanged. Direct
concatenation gives

```
C_W=(X+kY)Phi+(k-1)ZR,
D_W=(Z-P)Phi.                                        (2)
```

Suppose first that `D_W` divides `C_W`. Since `P` is a power of
three and `Z` a power of two, `gcd(Z,Phi)=1`. Therefore
`Phi | (k-1)R`. Set `d=gcd(k-1,Phi)`. Then `0<d<k`, and Bezout's
identity gives `dR=h Phi` for an integer `h`.

Reducing this equation modulo `Z` and `P`, and cancelling the
coprime powers of two and three, gives integers `t,s` with

```
dC=h alpha+Zt,   dE=-hS+Ps,   beta t-Qs=h.             (3)
```

Both `t,s` are positive. If `h>=0`, the second equation first
gives `s>0`, then the third gives `t>0`; if `h<0`, the first and
third equations give the reverse implication. Substitution yields
the retained-term identity

```
d C_AB = beta P t + QZ s >= beta P + QZ.              (4)
```

Induction on positive words proves the strict intercept bound

```
2^|w| C_w < 2^sum(w) 3^|w|.
```

Apply it to `A B[-delta]`, whose intercept equals `C_AB` and
whose sum is `T-delta`. Multiplying by `k` gives

```
k 2^g C_AB < ZP.
```

Together with `d<k` and (4), this implies

```
Q 2^g < P,       beta 2^g < Z.
```

Every letter of `A` is positive, so `Q>=2^l`. Thus

```
2^(l+g)<3^g,     3^n 2^g<2^T.                        (5)
```

Now suppose an actual positive odd `3x+1` cycle follows `W`.
The exact cycle equation gives `D_W | C_W`, so (5) holds. The
word cannot consist entirely of twos: it contains both `a` and
`a+delta`. A positive odd cycle containing `1` has every state
equal to `1` and every valuation equal to `2`, by forward
propagation and periodicity. The exact odd steps

```
3 -> 5 -> 1,      7 -> 11 -> 17 -> 13 -> 5 -> 1
```

therefore show that every state is at least `9`. Multiplying
the cycle equations and using this minimum gives

```
2^(3T) 9^(3g) <= 28^(3g).                            (6)
```

The final comparison uses integer powers only. The exact
constants `3^17<2^27`, `2^19<3^12`, and
`28^25<2^41 9^25` turn (5)--(6) into

```
17l<10g,     19n+12g<12T,     25T<41g.
```

Since `g=l+n>0`, the first two give `337g<204T`.
This contradicts the third, because `25*337=8425>8364=204*41`.

Finally, if `D_W>0` and `D_W | C_W`, every rotated intercept
is divisible by `D_W`. The states
`x_i=C_(rotate W i)/D_W` are positive integers. The rotation
identity gives their exact cycle equations and periodicity.
Positive valuation letters make every rotated intercept odd,
and the discriminant is odd, so every `x_i` is odd. This
constructs the forbidden cycle and proves the word-level claim.

## Certificates

The Lean proof checks the numerical power comparisons and the
small-state transitions exactly. There is no finite-search
assumption or separate Python certificate.

The module also checks a genuine positive-addend control:
`A=(2)`, `B=(3)`, `delta=1` gives

```
W=(3,3,2,2,2,3), C_W=12091, D_W=32039,
3x+32039 states: 12091,8539,7207,13415,18071,21563.
```

The `q=1` hypothesis is essential. No step transfers the
minimum-nine assertion or final `3x+1` product bound to
the known `3x+5`, `3x+7`, `3x+13` or `3x+61` cycles.

## Lean

The proof is in
[`LeanLane/ThirdPeriod.lean`](../../../../lean/LeanLane/ThirdPeriod.lean).
The external library is the pinned
[Mathlib source](../../../../sources/mathlib-065356127b1d.md).

- `ThirdPeriod.word` is exactly (1). `Positive u` means every
  prefix letter is strictly positive; `u` and `v` may be empty.
- `no_positive_odd_cycle` takes the actual `IsCycle 1 W x`
  equations, positive odd states, and the five word hypotheses.
  It derives (2)--(6), including nontriviality and the minimum.
- `discriminant_not_dvd_intercept` takes only those word
  hypotheses and `D_W>0`. It constructs the integral odd cycle
  from divisibility and invokes the first theorem.
- `retained_word_constraints` derives both inequalities (5)
  from word divisibility. The abstract `retained_lattice`
  proves (3)--(4) from the cyclotomic divisibility statement;
  that statement is derived from the actual six-block
  intercept, rather than assumed by either main theorem.
- `CycleEquation.minimum_nine` and
  `RationalCycle.integral_cycle_of_dvd` supply the two cycle
  interfaces. `ThirdPeriodPowers.integer_power_contradiction`
  is the log-free last step.

The existing shared cycle-equation, rotation and product
lemmas are unconditional. No logarithmic-form estimate,
external trajectory verification or imported period bound
enters this proof. The full balanced-placement classification
is not claimed formal by this node.

The source is compiled on the repository's pinned Lean
toolchain; cached Mathlib dependencies are reused, rather
than claimed rebuilt from source. The node remains `written`
until the Lean CI build passes. Build, source-hash and complete
axiom receipts are listed in the frontmatter.

## Remarks

This formalizes the unaligned all-defect exclusion already
proved in the balanced third-period node. It adds machine
verification of that scoped branch, not a novelty claim for
the mathematical argument. Same-session audits are not an
independent-session review.

## History

- 2026-11-08: Added the explicit six-block formalization,
  including the integral-cycle converse and minimum-nine
  argument. The broader written node is unchanged.
