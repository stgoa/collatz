# V001 — Guarded affine composition versus semigroup lifting

**Status: bounded discrimination probe.** This compares two descriptions on
small exact examples and one published induction step. No new infinite-family
certificate, proof method or convergence theorem is supplied. Only this note
was added for the probe; no computational searches, scripts or formal replay were run.

Use positive odd `S_d`, absorbed at 1. `C_d` denotes the shortcut clock
`n/2` for even n, `(3n+d)/2` for odd n. All inverse descriptions below identify
the forward clock explicitly. The nonabsorbing d=5 control stays away from 1.

## 1. Minimum data needed to compose legal blocks

### V2: guarded affine blocks

A previously verified block can be represented by:

- the map parameter d and absorber convention;
- its exact source domain D, including positivity and valuation guards;
- its affine map `F(x)=(3^k x+d b)/2^A`;
- its odd-arrow count k, total valuation A and a witness for block legality.

The full valuation word is a convenient witness. Once legality on D has been
proved, its affine map, domain and clock suffice for composition. A slope or
triple of local norms alone does not.

For consecutive blocks `(F1,D1)` and `(F2,D2)`, the actual domain is

```
D = D1 intersect F1^(-1)(D2),
F2(F1(x)) = [3^(k1+k2)x + d(3^k2 b1 + 2^A1 b2)] / 2^(A1+A2).
```

Their clocks add. If the first block reaches the absorber, the second cannot
be continued as a nontrivial unabsorbed block. For an exact ordinary valuation
word with total A, its source cylinder uses modulus `2^(A+1)`.

This is the affine framework, with offsets retained, used in
[Tao, corrected v7, §1.2](https://arxiv.org/html/1909.03562v7#S1.SS2).
Reading the coefficients at several places adds bookkeeping; it does not
remove the domain-pullback obligation.

### V3: multiplicative factors

A rational product alone has forgotten state dependence. To lift a product,
retain an ordered factor list, its current integer state at each step, the
specific allowed inverse branch, and its clock. For d=1:

```
2:                     y -> 2y, for every positive integer y;
(2k+1)/(3k+2):    3k+2 -> 2k+1, at that specific source state.
```

Even **factor order plus positive integer intermediate values** is insufficient:
`10*(3/5)=6` is integral, but `C_1(6)=3`, not 10. Thus it is not the inverse
arrow represented by `3/5`. Two lifted blocks compose only when the terminal
state of the first equals the admissible initial state of the second.
Restoring these conditions returns a state-dependent path structure.

## 2. Exact example: 3 reaches 5 and then 1

For d=1, take the two one-arrow blocks

```
F1(x)=(3x+1)/2,    D1: x=3 mod4,
F2(y)=(3y+1)/16,   D2: y=5 mod32.
```

The pullback gives `x=3 mod64`, and their composite is
`(9x+5)/32`. At x=3 it is exactly `3 -> 5 -> 1`, two odd arrows.

Three losses of information produce explicit errors:

1. **Discarding order:** the reversed affine composition is `(9x+19)/32`.
   Its slope is the same `9/32`, but its offset and legal domain differ.
2. **Discarding the intercept:** `9*3/32=27/32` is not the actual endpoint 1.
3. **Discarding the extra modulus bit:** x=35 satisfies `x=3 mod32`, and
   `(9x+5)/32=10` is an integer. Nevertheless its actual odd path is
   `35 -> 53 -> 5`, with word `(1,5)`. The putative word `(1,4)` stops
   at an even intermediate and is not its Syracuse word.

V3 records the correct inverse factorization
`3=2^3*(5/8)*(3/5)`, realized as
`1 -> 2 -> 4 -> 8 -> 5 -> 3`: five inverse shortcut arrows.
Moving `3/5` to the front preserves the product but starts with the
noninteger state 3/5. Commutativity has erased exactly the needed legality.

## 3. Exact cycle control: d=5

Split the odd word `(1,1,3)` into `(1,1)` followed by `(3)`:

```
G1(x)=(9x+25)/4,   D1: x=3 mod8,
G2(y)=(3y+5)/8,    D2: y>1 and y=1 mod16.
```

The composed domain is `x=19 mod64`, and
`G2(G1(x))=(27x+95)/32`. At x=19 this gives
`19 -> 31 -> 49 -> 19`, three odd arrows. The real slope 27/32 is below 1,
but the offset produces a positive fixed point. For the same word at general
d, the affine fixed point is `19d/5`; its integrality changes between d=1 and 5.

V3 sees
`2^2*(49/76)*(31/49)*(19/31)=1`. In the displayed order, starting at 19,
this is the legal inverse shortcut cycle
`19 -> 38 -> 76 -> 49 -> 31 -> 19`.
A unit product records a closed path; it does not identify that path with
the basin of 1. Neither description removes this control by itself.

## 4. One published induction step: the missing multiplication bridge

[Applegate–Lagarias, §2, Lemma 2.1 and Table 1, row `7 mod64`](https://arxiv.org/html/math/0411140v2#S2)
uses an initial multiplication by 5, permitted by membership in their wild
semigroup, followed by genuine shortcut steps. Its representative is

```
7 --multiply by5--> 35 -> 53 -> 80 -> 40 -> 20 -> 10 -> 5.
```

For `x=7 mod64`, the six shortcut steps starting from **5x** have endpoint
`C_1^6(5x)=(45x+5)/64 < x` for x>=7. This is a valid semigroup induction
step. The initial multiplication is an additional operation: `S_1(7)=11`
and `C_1(7)=11`, not 35. The published argument does not assert otherwise.

It gives a clear *missing interface*: relate x to 5x on this whole domain
by an independently valid absorption implication or a supplied current.
Semigroup membership of the multiplier supplies neither. For the single
representative, actual paths do merge:

```
7 -> 11 -> 17 -> 13 -> 5       (four odd arrows),
35 -> 53 -> 5                 (two odd arrows).
```

Consequently the finite current with rows
`[7]+[11]+[17]+[13]-[35]-[53]` has divergence `[7]-[35]`.
This verifies only that individual bridge. It is not a whole-class lift of
the published multiplier step. The clock of the artificial multiplication
must never be counted as a Collatz arrow.

## 5. Selection after this probe

**Prefer V2 as the exact representation for any further comparison.** It
retains an auditable composition law and places the missing condition in an
explicit domain intersection. This is useful discipline, not a newly found
progress estimate; multi-place norms themselves added no new constraint here.

**Defer V3 as a research direction.** The inspected published step produces
an explicit candidate bridge obligation, but its advantage comes from allowing
multiplication without supplying that bridge. Restoring legality recovers the
same kind of missing current input already tracked in this repository. The
probe found no independent lifting mechanism and no reason to begin a larger
semigroup search.

This selects a representation for subsequent viewpoint comparison, not a
proof route. A genuine gain would still require a new arithmetic restriction
or a new certified comparison, and neither was obtained in this bounded probe.
