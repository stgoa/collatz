---
id: unequal-one-five-half-defect-classification
kind: result
title: Half defects of amplitudes one and five have one full-cancellation family
status: written
claim: >
  Raw odd-only valuation words, any 3x+q. Let u,v be positive words of equal
  length n, differing at exactly two positions with absolute changes 1 and 5,
  in any order and with any signs. Put 2S=sum(u)+sum(v) and P=2^S+3^n.
  Then P divides C_(uv) if and only if uv is a cyclic rotation of U_t V_t
  for some integer t>=0, where U_t=(1,2,1,1,(3,1)^t,2,1,1,2) and
  V_t=(1,2,1,1,(3,1)^t,3,1,1,7). Here n=8+2t, S=14+4t,
  gcd(2S,2n)=4, the word is primitive, and 2^(2S)>2*3^(2n).
  Thus no near-critical word of this half-defect class cancels the full
  plus factor, and no index-2 word of this class does so even far from
  critical. Every displayed family member fully cancels its index-4
  primitive factor P, but has a rational 3x+1 state strictly between 0 and 1.
  Thus every positive word of this half-defect class with D>0 has reduced
  denominator greater than 1, excluding all positive integer 3x+1 cycles
  in the class, at every length. The base member is an already stored
  3x+893 cycle.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [unequal-one-three-half-defect-exclusion, actual-cycles-3x-d-corpus]
certificates: [check_one_five.py]
evidence:
  - "check_one_five.json: complete positive transition closure, sign/order normalization, weighted identities, endpoint controls and family checks"
tags: [cycles, denominators, unequal-amplitudes, near-doubled, signed-orbits, classification]
---

# Half defects of amplitudes one and five have one full-cancellation family

## Statement

Let `u,v` be positive valuation words of the same length `n>=2`,
differing at exactly two positions with absolute changes 1 and 5.
Their total is even; write `sum(u)+sum(v)=2S`, and let
`P=2^S+3^n`. Then `P | C_(uv)` exactly when `uv`, up to cyclic
rotation, is a member of the family

```
U_t = (1,2,1,1,(3,1)^t,2,1,1,2),
V_t = (1,2,1,1,(3,1)^t,3,1,1,7),       t=0,1,2,... .       (1)
```

Here `(3,1)^t` means `t` concatenated copies, including an empty
word when `t=0`. Every member has

```
n=8+2t,  S=14+4t,  gcd(2S,2n)=4,
2^(2S)>2*3^(2n).
```

Consequently, full plus-factor cancellation is impossible in
this class under either the near-critical condition
`3^(2n)<2^(2S)<2*3^(2n)` or the index-2 condition `gcd(S,n)=1`.
Under either of those restrictions, if `2^S>3^n`, the proper-divisor bound gives
`gcd(C_(uv),P)<2^S`; at index 2 this is the primitive half bound.
These conclusions concern the stated half-period defects,
not arbitrary four-mismatch rotations.

**Integer-cycle consequence.** Every such word with
`D=2^(2S)-3^(2n)>0` has reduced denominator greater than 1.
Therefore no positive integer cycle of raw odd-only `3x+1`
has half-word defects of absolute sizes 1 and 5. This
consequence holds at every length, without a near-critical
assumption.

## Proof

### 1. Reduction to two coefficient blocks

The normalization and weighted-intercept calculation in
[`unequal-one-three-half-defect-exclusion`](../unequal-one-three-half-defect-exclusion/README.md)
apply with the larger change 5 as follows. The identity

```
2^w_0 C_(R_1 w)=3C_w+(2^(2S)-3^(2n))
```

preserves `gcd(C_w,P)` under cyclic rotation. For ordered half
changes `(delta_1,delta_2)`, cutting after the first changed
position sends the ordered pair to `(delta_2,-delta_1)`.
Iterating therefore allows the normalization

```
v_i=u_i+epsilon,  v_h=u_h+5,  i<h,  epsilon in {-1,1}.
```

Write `B=sum(u)` and `j=(epsilon+5)/2`, so `S=B+j`.
Split `C_u=X+Y+Z` at term indices `t<=i`, `i<t<=h`, and `t>h`.
The changed prefix exponents give

```
epsilon=-1, j=2:  2*(4C_u-C_v)=6X+7Y-24Z;
epsilon=+1, j=3:      8C_u-C_v=7X+6Y-56Z.              (2)
```

Set `(a,b)=(6,7)` or `(7,6)` respectively; both right sides
are `aX+bY-2^j aZ`. Rotate `u` to start after `h`, obtaining
`r`, and assign coefficient `a` to its first `n-h+i` terms
and coefficient `b` to its remaining `h-i` terms. Both blocks
are nonempty. Its weighted intercept is

```
M=sum_(t<n) b_t*3^(n-1-t)*2^(sum_(k<t)r_k).
```

For `p=sum_(t<=h)u_t`, direct rotation of the sums yields

```
3^(n-1-h)*2^p*M = 3^n*aZ+2^B*(aX+bY)
                = 2^B*(aX+bY-2^j*aZ)  (mod P).
```

Together with `C_(uv)=3^n C_u+2^B C_v` and (2), this gives
`gcd(C_(uv),P)=gcd(M,P)`, since 2 and 3 are units modulo `P`.

Increase the last letter of `r` by `j`, giving total `S`
without changing `M`. If `P | M`, write `H=M/P>0`. The
weighted affine equation then sends `-H` to `H`.
Every cut is integral: the endpoint equation modulo each
prefix power of 2 cancels an odd suffix multiplier, just as
in the cited result. Thus its integer states satisfy

```
2^r_k*x_(k+1)=3*x_k+b_k,
```

where the notation `r_k` now includes that final increase.
The last division exponent is at least `j+1`.

At each step, integrality forces the input parity to match
the additive coefficient. Thus inputs to `+6` are even,
and inputs to `+7` are odd; the last endpoint need not have
the parity of the last coefficient. Also `H` has the parity
of the first coefficient, because `M` does. These parity
conditions are retained throughout the argument.

### 2. Coefficients 6 then 7 cannot realize the endpoints

Here `H` is even and the last division exponent is at least 3.
The last `+6` exponent is the original letter `u_i`, which
is at least 2 because this letter was decreased by 1 in `v`.
This boundary condition is essential.

A negative even state under `+6` stays nonpositive. To
become positive it must pass through `-2 -> 0 -> 3`;
the arrow out of zero has exponent 1. The odd state 3
cannot be an input to another integral `+6` step. Therefore
this crossing would have to occur at the last `+6` arrow,
contrary to its exponent being at least 2. The interface
cannot be zero either, because `+7` has no integral output
from zero. Hence the `+7` block starts at a negative odd state.

The first positive `+7` output can only come from `-1`:
it is 1 at exponent 2, or 2 at exponent 1. If this is not
the last step, parity forces the odd output 1. Its complete
positive odd orbit is

```
1 --1--> 5 --1--> 11 --3--> 5.
```

Arrow labels are division exponents. The only positive even
endpoints reachable from this crossing and orbit are

```
-1 --1--> 2,   11 --2--> 10,   11 --1--> 20.
```

All have exponent below 3, contradicting the final condition.

### 3. Coefficients 7 then 6 have a finite complete closure

Now `H` is odd and the last division exponent is at least 4.
If the even interface entering the `+6` block were nonpositive,
the only possible positive exit would again be `0 -> 3` at
exponent 1, necessarily the last arrow. Therefore the interface
is positive. The preceding `+7` block starts at `-H<0` and
has odd inputs, so the preceding crossing argument proves
that its possible positive even interfaces are exactly among
`{2,10,20}`.

For an even input `x`, put `v=v_2(3x+6)`. Every allowable
division exponent is in `1,...,v`. Exponents below `v` give
even outputs, which can continue inside the `+6` block;
exponent `v` gives its sole odd output, which must terminate
the block at `H`. The complete closure from `{2,10,20}` is:

| Input | All even successors, with exponent | Odd endpoint, with exponent |
|---|---|---|
| 2 | 6 (1) | 3 (2) |
| 6 | 12 (1), 6 (2) | 3 (3) |
| 10 | 18 (1) | 9 (2) |
| 12 | none | 21 (1) |
| 18 | 30 (1) | 15 (2) |
| 20 | none | 33 (1) |
| 24 | none | 39 (1) |
| 30 | 48 (1), 24 (2), 12 (3), 6 (4) | 3 (5) |
| 48 | none | 75 (1) |

Every even successor is in this table, proving closure by
induction for paths of every length, including arbitrarily
many repetitions of `6 -> 6`. No upper bound on path length
is imposed. The only terminal exponent at least 4 is
`30 -> 3` at exponent 5. Therefore `H=3`, and the path from
the interface is forced to be

```
10 --1--> 18 --1--> 30 --5--> 3.
```

Starting at `-H=-3`, the preceding `+7` block is then forced:

```
-3 --1--> -1 --2--> 1 --1--> 5 --1--> 11,
then t copies of 11 --3--> 5 --1--> 11,
then 11 --2--> 10,                         t>=0.       (3)
```

These are all possibilities because each nonterminal `+7`
output must be odd, fixing its division exponent, while
the required interface 10 fixes the last exponent at 2.

### 4. Reconstructing the family, and the converse

The exponents of the signed segment in (3) and the forced
`+6` tail are

```
(1,2,1,1,(3,1)^t,2,1,1,5).
```

Undoing the final increase by `j=3` gives `r=U_t`.
The first changed letter is at the end of the `+7` block;
raising it by 1 and raising the last letter by 5 gives `V_t`.
The suffix after the original position `h` was common to
both halves, so rotating the full word after that position
produces the rotated halves in exchanged order. A half-turn
therefore identifies the original word, up to cyclic
rotation, with `U_t V_t`.

Conversely, every `t>=0` gives the displayed integral path
from `-3` to 3: inserting the loop in (3) preserves its
endpoints. Hence its weighted intercept is `M=3P`, so the
weighted gcd identity proves `P | C_(U_t V_t)`. Rotation
preserves this divisibility. This proves both directions.

Each member has a unique letter 7, and hence is primitive.
The totals are `n=2(t+4)` and `S=2(2t+7)`. Since
`(2t+7)-2(t+4)=-1`, their full cyclotomic index is

```
gcd(2S,2n)=4*gcd(2t+7,t+4)=4.
```

Its primitive factor is therefore
`Phi_4(2^(7+2t),3^(4+t))=P`, and fully cancels. Finally,
`2^28=268435456>86093442=2*3^16` and `2^8=256>81=3^4`.
The ratio `2^(2S)/3^(2n)` starts above 2 and is multiplied
by `256/81` per increment of `t`, proving the stated
far-from-critical inequality for every member.

### 5. Even the exceptional family cannot have denominator 1

Put `L=16^t` and `K=9^t`, so `L>=K>0`. For the prefix
`p=(1,2,1,1)`, loop `l=(3,1)` and tail `z=(2,1,1,2)`,
their intercepts are `C_p=85`, `C_l=11` and `C_z=103`.
Concatenation and the geometric sum give

```
C_(l^t)=11*(L-K)/7,
C_(U_t)=81*K*85+32*81*11*(L-K)/7+32*L*103
       =(19683*K+51584*L)/7.                         (4)
```

Write `C_(U_t)=X+Y`, with `Y` the terms after its first
changed position. The weighted intercept is `7X+6Y=3P`,
while `C_(V_t)=X+2Y`. Hence
`C_(V_t)=8C_(U_t)-3P`. Since
`2^sum(U_t)=2048L` and `3^n=6561K`, concatenation yields

```
C_(U_t V_t)/P=C_(U_t)-3*2048L
             =(19683K+8576L)/7.
```

The rational `3x+1` starting state of this word is therefore

```
C_(U_t V_t)/D_(U_t V_t)
  = (19683K+8576L)/(7*(16384L-6561K)).                (5)
```

Its numerator and denominator are positive, and denominator
minus numerator is `106112L-65610K>0`, since `L>=K>0`.
Thus (5) is strictly between 0 and 1 and is not an integer.
The reduced denominator is invariant under cyclic rotation,
so every exceptional rotation has denominator greater than 1.
Every other word in the class fails `P | C`, and since
`P | D`, it also fails `D | C`. These two cases prove the
integer-cycle consequence.

## Certificates

[`check_one_five.py`](check_one_five.py) enumerates every
integral division at every state in the finite `+6` closure,
checks the complete `+7` positive odd orbit and its even
exits, and verifies the exceptional signed path. It also
checks normalization over both amplitude orders and all
signs, the weighted identities, and explicit family members.
The exact coefficients in (4) and (5), and the positive
coefficient difference proving the rational state is below 1,
are also checked.
The all-length classification follows from the closed
transition table and the loop argument above, not from
the bounded sample of words.

```
python3 areas/cycles/results/unequal-one-five-half-defect-classification/check_one_five.py
```

The deterministic receipt is [`check_one_five.json`](check_one_five.json),
regenerated with `--write-receipt`. The script uses only
exact integers and the standard library; its checks also
run under `python3 -O`.

## Remarks

- **Existing base cycle.** At `t=0`, `C=92628965`,
  `D=225388735`, `P=22945`, `G=252395`, and `D/G=893`.
  The positive `3x+893` cycle has minimum 367 and is already
  recorded in [`actual-cycles-3x-d-corpus`](../actual-cycles-3x-d-corpus/README.md),
  at JSON pointer `/cycles/2158`, discovery seed 5.
  The certificate independently reconstructs its exact
  positive odd states. No new-cycle claim is made.
- **Why the boundary condition matters.** The signed path
  `-2 -> 0 -> 3 -> 2` with coefficients `(6,6,7)` and
  exponents `(1,1,3)` is valid. It fails the required
  exponent at the end of the `+6` block. Omitting positivity
  of the decreased letter would invalidate the exclusion.
- **Scope.** The near-critical and index-2 exclusions concern
  full cancellation of `P` in this half-defect class. The
  general near-critical half bounds are false, as shown by
  [`near-critical-four-mismatch-corpus-counterexample`](../near-critical-four-mismatch-corpus-counterexample/README.md).
  The integer-cycle exclusion applies to the stated
  half-defect class; no exclusion of arbitrary cycles is made.
  The auxiliary `+6` and `+7` maps permit sign crossings;
  the proof retains them rather than excluding actual
  `3x+d` control cycles.
- **Novelty and status.** Novelty undetermined. Written proof
  and deterministic certificate, without an independent-session
  review or Lean formalisation.

## History

- 2026-11-08: derived by the Codex cycle research lane
  (GPT-6 Astra; directed by Santiago Armstrong). The two
  coefficient blocks give an exact infinite exceptional
  family and exclude all near-critical members of the
  stated half-defect class.
- 2026-11-08: the explicit exceptional-family intercept
  places one rational state strictly between 0 and 1.
  Combined with the classification, this strengthens the
  consequence to denominator-1 exclusion throughout the
  stated half-defect class, at every length and without
  a near-critical assumption.
