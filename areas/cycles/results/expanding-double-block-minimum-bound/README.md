---
id: expanding-double-block-minimum-bound
kind: result
title: An expanding doubled block forces a minimum and denominator lower bound
status: written
claim: >
  Raw odd-only valuation words. Let U,V be nonempty positive words of
  equal length g, put a=sum(U), b=sum(V), P=3^g, Q=2^a, S=2^b,
  and suppose Q<P<S and D_(UUV)=Q^2*S-P^3>0. Every actual positive
  odd 3x+q cycle with positive odd q and word UUV has minimum
  L>2^(g+1)*(P+Q)/(S-P). In particular, with q=den(UUV) and
  eta=1-P^3/(Q^2*S), q>eta*2^(g+1)*(P+Q)/(g*(S-P)), without
  external inputs. If q=1 and a>=11g/10, an internal finite descent
  check gives L>2^(g/41); under EXT-1 this forces g<2^19 and
  displayed odd period 3g<=1572861. The additional declared Barina
  convergence input therefore excludes denominator one for this
  subfamily at every length. Primitivity is not required. The
  remaining mixed case a<11g/10 is not excluded.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex root research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [cycle-length-lower-bound-from-convergents]
assumes: [musson-collatz-gap-all, barina-2025-convergence-2-71]
certificates: [check_expanding_double.py]
evidence:
  - "check_expanding_double.json: actual reduced cycle controls, all-interior inequalities, local descent, exact constants and the declared period comparison"
tags: [cycles, third-period, expanding-blocks, minimum, denominators]
---

# An expanding doubled block forces a minimum and denominator lower bound

## Statement

For a positive valuation word `W`, use

```
C_W=sum_(j=0)^(len(W)-1) 3^(len(W)-1-j) 2^(W_0+...+W_(j-1)),
D_W=2^sum(W)-3^len(W),
den(W)=D_W/gcd(C_W,D_W) when D_W>0.
```

The affine action under `3x+q` is
`(3^len(W)*x+q*C_W)/2^sum(W)`. All states and valuations below use
the raw odd-only clock.

Let `U,V` have the same positive length `g`, with every letter at
least one. Define

```
a=sum(U),  b=sum(V),  P=3^g,  Q=2^a,  S=2^b,
w=UUV,    E=2a+b,    eta=1-3^(3g)/2^E.
```

Assume

```
Q<P<S,             Q^2*S>P^3.                         (1)
```

Thus `U` expands, `V` contracts, and the complete word has positive
discriminant. For every positive odd additive parameter `q`, every
actual positive odd `3x+q` cycle with this word has minimum

```
L > 2^(g+1)*(P+Q)/(S-P).                              (2)
```

In particular, the reduced cycle with additive parameter `q=den(w)`
satisfies the denominator law

```
q > eta*2^(g+1)*(P+Q)/(g*(S-P)).                       (3)
```

These two assertions have no external assumptions and hold at all
lengths. They retain the actual additive parameter of each control.

There is a stronger consequence for denominator one when

```
a >= 11g/10.                                         (4)
```

An internal finite descent certificate gives `L>2^(g/41)` for any
such integer `3x+1` cycle. Under the gap input
[EXT-1](../../../../sources/musson-collatz-gap-all.md),

```
g<2^19,             3g<=1572861.                      (5)
```

Adding the declared
[Barina convergence input](../../../../sources/barina-2025-convergence-2-71.md)
and its [replayed odd-period consequence](../cycle-length-lower-bound-from-convergents/README.md)
excludes `den(w)=1` at every length subject to (1) and (4).
The length `3g` is the displayed word length; it need not be the least
period. The assertions do not require `U,V` to differ in only two
positions.

## Proof

### 1. The expanding repeated-block lattice

Let `x0,x1,x2` be the actual odd integer states before the first `U`,
the second `U`, and `V`. Since `P>Q` and `C_U>0`,

```
x0<x1<x2.
```

Subtracting the two `U` equations gives

```
Q*(x2-x1)=P*(x1-x0).
```

Both differences are positive even integers and `P` is odd while
`Q` is a power of two. Therefore, for an integer `t>=1`,

```
x1-x0=2Q*t,         x2-x1=2P*t,
x2=x0+2(P+Q)*t.                                      (6)
```

The third block gives `S*x0=P*x2+q*C_V`. Substitution in both
directions yields the exact identities

```
(S-P)*x0=2P(P+Q)*t+q*C_V,
(S-P)*x2=2S(P+Q)*t+q*C_V.                             (7)
```

Consequently

```
x0>2P(P+Q)/(S-P),
x2>2S(P+Q)/(S-P).                                    (8)
```

The sign of the intercept term is essential: it is positive in both
identities, so no estimate replacing `q` by one is made here.

### 2. Every state inside all three blocks

Consider a block of length `g`, total `A`, and starting state `z`.
At its `j`th state, `0<=j<g`, let `A_j` be the preceding prefix total.
The remaining `g-j` letters are positive, hence
`A_j<=A-(g-j)`. Positivity of the affine prefix gives

```
z_j >= 3^j*z/2^A_j
    >= (2^g/2^A)*(3/2)^j*z
    >= (2^g/2^A)*z.                                 (9)
```

For either copy of `U`, the starting state is at least `x0`; (8)
and (9) imply

```
z_j > 2^(g+1)*P(P+Q)/(Q*(S-P))
    > 2^(g+1)*(P+Q)/(S-P).
```

For `V`, use its own total `b` and its larger starting state `x2`:

```
z_j > (2^g/S)*2S(P+Q)/(S-P)
    = 2^(g+1)*(P+Q)/(S-P).
```

This proves (2) for the global minimum, including the interior of
the contracting block. Bounding that interior by the smaller
boundary state `x0` would lose an unnecessary factor `P/S`.

### 3. The unconditional denominator law

Normalize a positive `3x+q` cycle by dividing all its states by `q`;
its minimum is `X=L/q`. The product identity over the full `3g`
arrows gives

```
eta = 1-product_i (1+1/(3X_i))^(-1).
```

For positive `y_i`,
`1-product_i(1+y_i)^(-1)<sum_i y_i`: for example use
`1-exp(-z)<z` and `log(1+y)<y`. Therefore

```
eta < sum_i 1/(3X_i) <= g/X,
L/q=X<g/eta.                                         (10)
```

Combining (2) and (10) proves (3). In particular this applies to
the actual reduced `3x+den(w)` cycle associated with every word in
(1). Rational normalization is used only for (10); the even lattice
(6) was proved for the actual integer states.

### 4. The valuation threshold makes the minimum exponential

Now assume `q=1`. The word cannot be a repetition of `(2)`, since
`U` expands. The certificate follows every odd seed `3<=n<2^17`
until a smaller odd value is reached. A minimum in that range
could not lie in a nontrivial cycle; a cycle containing `1` is
trivial. Thus

```
L>=2^17.                                             (11)
```

This is a local exact replay, independent of the external convergence
input. Put `alpha=log2(3)`, `ell=log2(L)`, and
`delta=E-3g*alpha`. The `3x+1` product identity and
`log(1+x)<x` give

```
0<delta<g/(L*ln(2))<2g/L<=g/65536,                   (12)
```

where `ln(2)>1/2` follows by integrating `1/t>1/2` on `(1,2)`.
By (2), `P+Q>P` and `S-P<S`,

```
ell > g+1+alpha*g-b
    = 2a-(2alpha-1)*g+1-delta.                        (13)
```

The exact integer comparison `3^80<2^127` proves `alpha<127/80`.
Under (4), (12) and (13) now yield

```
ell > (1/40-1/65536)*g+1 > g/41,                    (14)
```

because
`1/40-1/65536-1/41=7987/13434880>0`.

### 5. The source-dependent length conclusions

EXT-1, applied to the full length `m=3g`, gives
`eta>=2^(-172)*(3g)^(-341)`. At `q=1`, (10) consequently implies

```
ell < 172+342*log2(3g).                              (15)
```

Suppose `g>=2^19`, and choose an integer `j>=19` with
`2^j<=g<2^(j+1)`. Equations (14) and (15) would require

```
2^j/41 < 172+342*(j+3).
```

At `j=19`, the left side minus the right side is `208752/41>0`.
Its next increment is `2^j/41-342`, already positive at `j=19` and
increasing. This proves (5) using EXT-1, without Barina.

With Barina, the declared period result says that the least odd
period of a nontrivial integer cycle is at least `72057431991`.
That least period is at most its displayed length `3g<=1572861`.
This contradiction proves the all-length exclusion under both
external inputs. No claim of primitivity of `UUV` is needed.

## Certificates

[`check_expanding_double.py`](check_expanding_double.py) checks the
boundary identities with the actual additive parameter, the even
lattice, every interior-state bound, and the denominator inequality
on a declared finite set of genuine reduced cycles. It includes
all eligible pairs with lengths `1..4` and letters `1..4`, together
with `1200` fixed-seed longer controls: `4262` actual cycles and
`86784` arrows in total, including `1631` cycles whose minimum lies
inside `V`. The finite controls check formulas; the proof above
supplies the all-length assertion.

The script also independently replays all `65535` odd nontrivial
seeds below `2^17`, checks the exact powers and rational constants,
and replays all eleven shared `3x+5`, `3x+7`, `3x+13` and `3x+61`
fixtures. The explicit mixed control `U=(1)`, `V=(3)` is the actual
`3x+5` cycle `19 -> 31 -> 49 -> 19`; it satisfies the universal
minimum and denominator laws. Other controls satisfy (4) at true
`q>1`; they are not excluded by the `q=1` conclusion.

[`check_expanding_double.json`](check_expanding_double.json) is generated
by the script. From the repository root:

```
python3 areas/cycles/results/expanding-double-block-minimum-bound/check_expanding_double.py
python3 -O areas/cycles/results/expanding-double-block-minimum-bound/check_expanding_double.py
```

The default verifies the receipt; `--write-receipt` regenerates it.
The external gap theorem and Barina's convergence computation are
declared inputs, not computations performed by this script.

## Remarks

- This is the mixed direction complementary to
  [the expanding-third-block bound](../expanding-third-block-minimum-bound/README.md),
  which assumes `Q>P>S`. Both proofs use exact boundary differences
  and positive prefix bounds. The invalid
  [fixed-point interval argument](../../attempts/interval-trapping-expanding-blocks.md)
  is not used.
- In an aligned third-period four-mismatch word, two changed letters
  can lie in the same length-`g` block, producing `UUV` after a cut.
  This result applies when (1) and (4) hold, regardless of the signs
  or sizes of those changes. It also applies to arbitrary `U,V`
  without a two-change restriction. The remaining expanding-`U`
  branch with `a<11g/10` and unaligned three-block placements remain
  outside the exclusion.
- Equation (13) retains a sharper state-dependent restriction than
  the convenient threshold (4). No uniform exclusion of all expanding
  repeated blocks is asserted. Novelty is undetermined; the mechanism
  uses the established even lattice for repeated blocks.

## History

- 2026-11-08: derived the expanding repeated-block boundary identities
  and their all-interior minimum and denominator laws, then combined
  the valuation threshold with a local descent replay and the separately
  declared gap and period inputs. Same-session mathematical scrutiny
  does not change the written status.
