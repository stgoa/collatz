---
id: expanding-third-block-minimum-bound
kind: result
title: An expanding third block forces an exponential cycle minimum
status: written
claim: >
  Raw odd-only 3x+1 clock. Let U,V be positive valuation words
  of the same length g>=1, put P=3^g, Q=2^sum(U), S=2^sum(V),
  and suppose Q>P>S and D_(UUV)=Q^2*S-P^3>0. If den(UUV)=1,
  its actual integer-cycle minimum L satisfies
  L>2^g*S/(P-S) and L>2^(2g/5). Under EXT-1 this forces
  g<2^14 and the displayed word length 3g<=49149. With the
  additional declared Barina convergence input, den(UUV)>1
  at every length in this mixed-direction family. The displayed
  word need not be primitive, the two blocks may vary freely,
  and no restriction on individual letters or their differences
  is imposed. The configuration with the repeated block
  expanding and the third block contracting is not covered.
authors:
  - Codex root research lane (GPT-6; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [cycle-length-lower-bound-from-convergents]
assumes: [musson-collatz-gap-all, barina-2025-convergence-2-71]
certificates: [check_mixed_blocks.py]
evidence:
  - "check_mixed_blocks.json: exact repeated-block lattice, interior-state bounds, actual addend-aware controls, local descent and dyadic constants"
tags: [cycles, two-blocks, third-period, expanding-blocks, minimum, effective-exclusion]
---

# An expanding third block forces an exponential cycle minimum

## Statement

Use the raw odd-only clock. Let `U,V` be positive-integer
valuation words of equal length `g>=1`. Write

```
a=sum(U), b=sum(V), e=a-b,
P=3^g, Q=2^a, S=2^b, W=U U V.
```

Assume

```
Q>P>S,       D_W=Q^2*S-P^3>0.                       (1)
```

Thus each complete U-block contracts and the V-block expands.
If `den(W)=1`, its positive odd integer cycle has minimum `L`
satisfying the unconditional necessary bounds

```
L>2^g*S/(P-S),       L>2^(2g/5).                    (2)
```

Under [EXT-1](../../../../sources/musson-collatz-gap-all.md),
these imply

```
g<2^14,       |W|=3g<=49149.                        (3)
```

With the additional declared
[Barina convergence input](../../../../sources/barina-2025-convergence-2-71.md),
no such word has denominator one, at any length.
The external computation is used only through the
[replayed full odd-period bound](../cycle-length-lower-bound-from-convergents/README.md)
`72057431991`. The displayed word need not have least period
`3g`: the least odd period is at most `3g`, which suffices for
the comparison. Neither conclusion uses LMN or Chim.

The opposite mixed direction, where U expands and V contracts,
is outside this statement. The result also does not cover
unequal block lengths or arbitrary repetition counts.

## Proof

### 1. Exact integer states and their boundary differences

Suppose `den(W)=1`. Its reduced rational cycle is an actual
positive odd integer `3x+1` cycle: the rotation identity

```
2^(w_i) C_next=3C_rot+D_W
```

propagates divisibility by the odd integer `D_W` to every
rotated intercept. The resulting states are positive integers,
and positive letters make the intercepts and states odd.
Let `x0,x1,x2` be the states at the starts of U, U, and V.
The three complete block equations are

```
Q*x1=P*x0+C_U,
Q*x2=P*x1+C_U,
S*x0=P*x2+C_V.                                     (4)
```

Since `P>S` and `C_V>0`, the last equation gives `x0>x2`.
Subtracting the first two equations gives

```
Q*(x2-x1)=P*(x1-x0).
```

Both differences have the same sign, hence are negative.
Both are even, and `gcd(P,Q)=1`. Therefore an integer `t>=1`
satisfies

```
x1-x0=-2Q*t,       x2-x1=-2P*t,
x0=x2+2(Q+P)*t.                                   (5)
```

The factor two uses actual odd integer states. Substituting
(5) into the V equation yields the exact positive identity

```
(P-S)*x2=2S(Q+P)*t-C_V.                            (6)
```

### 2. Positive letters bound every interior state

For any positive word of length `g` and total `b`, every
prefix sum `B_i` is at most `b-(g-i)`. Consequently

```
C_V=sum_(i=0)^(g-1) 3^(g-1-i)*2^B_i
   <=2^(b-g) sum_(i=0)^(g-1) 3^(g-1-i)*2^i
   =2^(b-g)(3^g-2^g)
   <S*P/2^g.                                      (7)
```

Equations (6)--(7), `t>=1`, and `P-S>0` imply

```
(P-S)*x2 > 2S(Q+P)-S*P/2^g > S*Q,
x2>S*Q/(P-S).                                     (8)
```

This is a bound on the smallest *block-start* state. To pass
to the actual cycle minimum, consider any prefix of length
`j`, `0<=j<g`, inside either block. Its valuation sum `A_j`
is at most `a-(g-j)`, since both block totals are at most `a`
and every remaining letter is positive. A state `y` at that
prefix, from its block-start state `x`, satisfies

```
y>=3^j*x/2^A_j
 >=(2^g/Q)(3/2)^j*x
 >=(2^g/Q)*x2.                                    (9)
```

The first inequality follows from the positive affine
intercept; it also includes the empty prefix. The block-start
states obey `x0>x1>x2`, by (5). Thus (9) covers every state,
including all interiors, and proves

```
L>=2^g*x2/Q>2^g*S/(P-S)>2^g*S/P.                   (10)
```

No interval between block fixed points is used.

### 3. The full-cycle mean turns this into an exponential bound

The word cannot consist entirely of twos, because `S<P<4^g`.
The cycle is therefore nontrivial. The certificate checks
that every odd seed `3<=s<2^17` descends below its starting
value. A nontrivial cycle cannot have such a minimum, so
`L>=2^17`, in particular `L>=129`.

The product of the actual q=1 step ratios, together with
`388^5<2^8*129^5`, gives

```
2^(2a+b)=product_i(3+1/n_i)<2^(8*(3g)/5),
E=2a+b=3b+2e<24g/5.                               (11)
```

Since `b>=g`, equation (11) implies

```
e<9g/10.                                          (12)
```

The full discriminant in (1) gives a second exact constraint:

```
Q^2*S=2^(2e)*S^3>P^3,
S/P>2^(-2e/3).                                    (13)
```

Combining (10), (12) and (13),

```
L>2^(g-2e/3)>2^(2g/5),                            (14)
```

as claimed. This part uses only exact local descent and the
integer cycle equations, not any external gap or trajectory bound.

### 4. EXT-1 gives the finite cutoff

Put `m=3g`, `D=2^E-3^m` and `eta=D/2^E`. The product identity
also gives

```
eta=1-product_i(1-1/(3n_i+1))
   <=sum_i 1/(3n_i+1)<m/(3L).
```

EXT-1 says `eta>=2^-172*m^-341`, hence

```
log_2(L)<172+342log_2(3g).                          (15)
```

If `2^j<=g<2^(j+1)`, then `log_2(3g)<j+3`.
Equations (14)--(15) would force

```
(2/5)*2^j<172+342(j+3).                            (16)
```

At `j=14` the left minus right is `2838/5>0`.
Thereafter the left doubles while the right increases by
342, less than the initial left side. Thus (16) is impossible
for every `j>=14`, proving `g<2^14` and `3g<=49149`.

Only now use the external Barina-dependent bound: every
nontrivial cycle has least odd period at least `72057431991`.
Its least period is at most the displayed length `3g`, in
contradiction to (3). No primitivity of U, V, or W was needed.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/expanding-third-block-minimum-bound/check_mixed_blocks.py
python3 -O areas/cycles/results/expanding-third-block-minimum-bound/check_mixed_blocks.py
```

The deterministic standard-library certificate checks the
intercept bound, exact boundary differences and (6) with the
true additive constant q, and every interior-prefix inequality.
It covers all eligible block pairs of lengths 1 through 4 with
letters 1 through 4, plus 1200 seeded larger pairs. These give
4973 actual reduced `3x+q` cycles and 96612 exact odd arrows.
It also checks 65535 local descent seeds, all eleven shared
`3x+5`, `3x+7`, `3x+13`, `3x+61` fixtures, and the rational
cutoff constants. Use `--write-receipt` to regenerate its receipt.

The minimum mechanism is tested nonvacuously on an actual
mixed-direction control:

```
U=(2), V=(1), W=(2,2,1), q=5,
37 -> 29 -> 23 -> 37.
```

For general q, (6) contains `-q*C_V`. The checker retains this
term; it tests the minimum conclusion only under the sufficient
exact condition `q*C_V<S*P`. The q=1 proof obtains that condition
from (7). The q=1 product-mean estimate (11) is not transferred
to the q=5 control, whose mean valuation is `5/3`.
These computations check finite algebra and controls; they do
not infer the unbounded theorem from a search without examples.

## Remarks

The earlier
[interval-trapping attempt](../../attempts/interval-trapping-expanding-blocks.md)
fails for mixed directions: block-start states need not lie
between the two block fixed points. The surviving integer
spacing idea works here through (6) and the interior lower
bound (9). It forces a large *minimum*, rather than a bound on
that invalid fixed-point interval.

For an aligned third-period word, rotate to `U U V`, where U
is the majority block. If the total change in V is negative,
then a positive full discriminant forces U to contract. When
V also contracts, the
[two-copy contracting theorem](../contracting-two-block-double-repeat-exclusion/README.md)
already applies. When V expands, the present result applies.
Thus these two results cover the aligned negative-total-change
branch under their declared inputs. The aligned positive-change
case with expanding U, and unaligned unbalanced third-period
words, remain open.

This is a written result, not a formalization. Same-session
proof audits do not confer independent-review status. Novelty
outside the repository is undetermined.

## History

- 2026-11-08: derived the expanding-third-block boundary identity
  and an all-interior-state lower bound, giving the exponential
  minimum and explicit mixed-direction exclusion.
