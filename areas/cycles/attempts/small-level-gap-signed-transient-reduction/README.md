---
id: small-level-gap-signed-transient-reduction
kind: attempt
title: A small level gap gives a negative-addend transient but no uniform exclusion
status: written
claim: >
  For low-to-high positive-interface Mersenne joins with J>r>=1 and
  positive reconstructed denominator, the paired reduced integer
  3x+q states give an exact odd-only 3w-q*(2^(J-r)-1) transient along
  B[-r]. Its initial state is 3^len(A) times a positive odd integer,
  and its last valuation exceeds J-r. This reduction does not by itself
  give a uniform cycle exclusion: a genuine q=4069 join defeats the
  rational-state sign shortcut, and positive 3w-1 paths of unbounded
  length satisfy the isolated initial-divisibility and last-valuation
  conditions. The latter paths are not asserted to retain the coupled
  Mersenne endpoints or positive reconstructed denominator.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [two-half-defect-mersenne-normal-form, mersenne-join-state-enclosure, bounded-unequal-half-defect-exclusion, baseline-obligation-transfer-controls]
certificates: [check_small_gap.py]
evidence:
  - "check_small_gap.json: exact reconstructed joins, negative-addend transients, repeatable positive-path controls, and eleven actual-cycle fixtures"
tags: [cycles, half-defects, signed-orbits, stalled-approach, controls]
---

# A small level gap gives a negative-addend transient but no uniform exclusion

## Idea

The remaining low-to-high positive-interface problem allows a small
level gap `p=J-r` even when both levels are large. Compare the paired
actual states with ratio `2^p` after the first segment. Their difference
then follows a map whose negative addend depends on the small gap.
One might hope that its initial power of 3, positivity, and large final
valuation force a short transient, or transform it into an already
excluded signed Mersenne return.

The [state enclosure](../../results/mersenne-join-state-enclosure/README.md)
already warns that changing the defect cut produces mixed-sign addends.
This attempt makes the different, small-gap difference path explicit,
including its exact valuations and endpoints. The path identity survives;
the proposed sign and transient-length shortcuts do not supply an
exclusion.

## What happened

### The exact surviving reduction

Use the raw odd-only clock, with exact positive valuations and no zero
states or numerators. Let `J>r>=1`, and put

```
p=J-r,   M=2^r,   N=2^J,   delta=2^p-1.
```

Take nonempty signed segments `A,B` in the low-to-high
[normal form](../../results/two-half-defect-mersenne-normal-form/README.md):

```
A: -h -> z  under 3y+(M-1),
B:  z -> h  under 3y+(N-1),
h,z positive odd,   last(B)>J.
```

Writing `A[t]` for changing only the last valuation by `t`, reconstruct
the positive words

```
u=A[p]B[-J],    v=AB[r].
```

Suppose `D_(uv)>0`. Let `q=D_(uv)/gcd(C_(uv),D_(uv))` be the odd
reduced denominator and `X=q*C_(uv)/D_(uv)` the actual positive odd
integer state at the canonical cut of the associated `3x+q` cycle.
The opposite half starts at `X'=M*X+q*h`. If `Y` is the state after
`A[p]` in `u` and `Z` the state after `A` in `v`, the normal-form
identities give

```
F_A^(q)(X)=2^p*Y,    F_A^(q)(X')=Z,
Z=N*Y-q*z.                                           (1)
```

Here `F_A^(q)` is the affine composition with additive constant `q`.
Put `a=len(A)` and `P=sum(A)`. Since `X'>X` and the slope of this
composition is `3^a/2^P`,

```
W_0 = Z-2^p*Y
    = 3^a*((M-1)*X+q*h)/2^P > 0.                    (2)
```

It is odd because `Z,Y` are odd and `p>=1`. Consequently
`v_2((M-1)*X+q*h)=P`, and

```
t=((M-1)*X+q*h)/2^P
```

is a positive odd integer, with `W_0=3^a*t`.

Let `U_i,V_i` denote the paired actual states along the common prefix
of `B`, beginning at `Y,Z`. Their differences `W_i=V_i-2^p*U_i`
are odd and obey

```
W_(i+1)=(3*W_i-q*delta)/2^(B_i).                    (3)
```

Every such division is exact in the odd-only sense: its output is odd,
so `B_i` is the full valuation of the nonzero numerator. The difference
may be negative, but it cannot be zero.

For the final letter `s=last(B)`, the actual `u` arrow has valuation
`s-J` and ends at `X'`; the actual `v` arrow has valuation `s+r` and
ends at `X`. Therefore

```
3*W_(b-1)-q*delta
 = 2^(s+r)*X-2^p*2^(s-J)*X'
 = 2^(s-r)*(M*(M-1)*X-q*h),       b=len(B).           (4)
```

The bracket is odd and hence nonzero. Also `s-r>J-r=p>=1`.
Equations (2)--(4) prove that `B[-r]` is an exact signed odd-only
transient under `3w-q*(2^p-1)`, with

```
3^a*t  ->  M*(M-1)*X-q*h,    last(B[-r])>p.          (5)
```

No state-floor, near-critical, or external computation hypothesis is
used in this identity.

### A real join where the rational sign argument fails

An existing control in the
[bounded half-defect certificate](../../results/bounded-unequal-half-defect-exclusion/check_bounded_halves.json)
has `J=7,r=6,p=1,h=1`, with

```
A=(2):       -1 -> 15             under 3y+63,
B=(2,8):     15 -> 43 -> 1        under 3y+127,
u=(3,2,1),   v=(2,2,14).
```

The reduced denominator is `q=4069`. The actual `3x+4069` cycle is

```
1 -> 509 -> 1399 -> 4133 -> 4117 -> 4105 -> 1.
```

Thus `X=1`, `Y=509`, `Z=4117`, `t=1033`, and the difference word
`B[-6]=(2,2)` gives

```
3099 -> 1307 -> -37               under 3w-4069.
```

Its endpoint is `64*63-4069=-37`. Dividing this path by `4069`
produces a rational `3w-1` path crossing from positive to negative.
The normalized canonical state `1/4069` is indeed less than
`h/(M*(M-1))=1/4032`. This is an existing `3x+d` control, not a new
integer `3x+1` cycle.

## Why it fails

**The sign argument requires integer states.** When `q=1,p=1`,
every positive odd integer `w` has `3w-1>=2`. Starting from (2),
the transient stays positive, and (5) yields the valid necessary
condition

```
X > h/(M*(M-1)).                                    (6)
```

This is not a contradiction. The `q=4069` control shows why (6)
cannot be transferred to normalized rational states by dividing by
`q`: the scaled states no longer have the integer lower bound `w>=1`.
This is a concrete instance of the
[scaling-transfer obstruction](../scaling-transfer-to-3x-plus-d/README.md).
For `p>1`, even the numerator `3w-(2^p-1)` at a positive integer
need not be positive.

**The isolated transient conditions do not bound its length.** Under
the exact odd-only `3w-1` map,

```
9 -> 13 -> 19 -> 7 -> 5
```

has valuations `(1,1,3,2)`, and `5 -> 7 -> 5` has valuations
`(1,2)`. The latter composition is `(9w-5)/8`, which fixes 5.
Hence, for every integer `k>=0`, the word

```
(1,1,3,2)(1,2)^k
```

sends `9=3^2*1` to 5 through positive odd integers. It has length
`4+2k`, total valuation `7+3k`, and last valuation `2>p=1`.
The displayed fixed cycle proves the all-`k` statement; finite
representatives in the certificate only check the implementation.

This family does **not** preserve the coupled Mersenne endpoint
equations or the condition `D_(uv)>0`. It only refutes a length bound
derived from initial `3^a` divisibility, positivity, and the last
valuation condition alone. A useful exclusion must retain more of
the original coupling.

**A small gap does not bound the interface by the high level.** A
second existing control has `J=9,r=8,p=1,h=1`, `len(A)=30`,
`len(B)=28`, and `z=7527>2^J=512`. Its normalized canonical state is

```
1444813510101983474118931607 /
162254566700516117146743088684439.
```

The [receipt](check_small_gap.json) prints both full valuation words
and replays `-1 -> 7527 -> 1`, with `last(B)=12>J`. Thus replacing
the first segment by its first crossing, or assuming `z<2^J` from
`p=1`, would discard legitimate joins. No arbitrary-level conclusion
is inferred from this one control.

Finally, (5) has a **negative** addend and nonsymmetric endpoints.
It is not a positive-Mersenne `-h -> h` return. Reflection or a
change of cut does not supply the missing endpoint equations, so the
existing positive-Mersenne exclusions cannot be applied to this
transient without an additional argument.

## What survives

The exact reduction (5), its initial factor `3^a`, and the terminal
coupling `M*(M-1)*X-q*h` remain available. At `q=1,p=1`, the
necessary inequality (6) also survives. The unresolved step is to
use the full coupled endpoint and denominator conditions, rather
than the isolated negative-addend path, to force an exclusion.

The [certificate](check_small_gap.py) verifies both reconstructed
joins, their actual positive integer cycles, every signed transient
and the identities above. It checks representative repeat counts
for the explicit `3w-1` family and the loop's exact affine fixed
point, and replays all eleven shared actual `3x+d` fixtures.
There is no absence census or probabilistic claim. Run from the
repository root:

```
python3 areas/cycles/attempts/small-level-gap-signed-transient-reduction/check_small_gap.py
python3 -O areas/cycles/attempts/small-level-gap-signed-transient-reduction/check_small_gap.py
```

The argument gives no new cycle exclusion. Novelty is undetermined;
the two genuine joins are reused controls, and the elementary
negative-addend cycle is only an obstruction to the weakened route.

## History

- 2026-11-08: recorded the small-gap difference identity and the
  precise failures of sign transfer and transient-only length
  bounds. Same-session scrutiny does not change `written` status
  (Codex cycle research lane, GPT-6 Astra; directed by Santiago Armstrong).
