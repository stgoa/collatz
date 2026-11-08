---
id: unequal-two-four-half-defect-classification
kind: result
title: Half defects of amplitudes two and four have two full-cancellation families
status: written
claim: >
  Raw odd-only valuation words, any 3x+q. Let u,v be positive words of equal
  length n, differing at exactly two positions with absolute changes 2 and 4,
  in any order and with any signs. Put 2S=sum(u)+sum(v) and P=2^S+3^n.
  Then P divides C_(uv) exactly for cyclic rotations of the two families
  U_t=(2,1,1,(3,1)^t,1,3), V_t=(2,1,1,(3,1)^t,3,7), and
  U_(t,k)=(2,1,1,(3,1)^t,1,4,2^k,1),
  V_(t,k)=(2,1,1,(3,1)^t,3,4,2^k,5), where t,k>=0 and 2^k denotes
  k copies of the letter 2. Every exceptional word is primitive, has
  S=2n+1 and cyclotomic index 2, fully cancels its primitive factor P,
  and is far from critical. Nevertheless each has a rational 3x+1 state
  strictly between 0 and 1. Hence every word in the stated half-defect
  class with D>0 has reduced denominator greater than 1: no positive
  integer 3x+1 cycle belongs to this class, at any length.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [unequal-one-five-half-defect-classification, actual-cycles-3x-d-corpus, baseline-obligation-transfer-controls]
certificates: [check_two_four.py]
evidence:
  - "check_two_four.json: complete transition closure, all sign/order patterns, weighted identities, affine interval bounds and family samples"
tags: [cycles, denominators, unequal-amplitudes, near-doubled, signed-orbits, classification]
---

# Half defects of amplitudes two and four have two full-cancellation families

## Statement

Let `u,v` be positive valuation words of equal length `n>=2`,
differing at exactly two positions with absolute changes 2 and 4.
Put `sum(u)+sum(v)=2S` and `P=2^S+3^n`.

Then `P | C_(uv)` if and only if `uv` is a cyclic rotation of
one of the following words, with integer parameters `t,k>=0`:

```
U_t = (2,1,1,(3,1)^t,1,3),
V_t = (2,1,1,(3,1)^t,3,7);                           (I)

U_(t,k) = (2,1,1,(3,1)^t,1,4,2^k,1),
V_(t,k) = (2,1,1,(3,1)^t,3,4,2^k,5).                 (II)
```

Here word powers mean concatenation: `2^k` is `k` copies
of the letter 2, not a single letter of value `2^k`.
Family (I) has `n=5+2t`; family (II) has `n=6+2t+k`.
Both have `S=2n+1` and cyclotomic index `gcd(2S,2n)=2`.
Their primitive factor is exactly `P`, and fully cancels.
All are far from critical: `2^(2S)>2*3^(2n)`.

Despite this cancellation, every exceptional word has a
rational `3x+1` state strictly between 0 and 1. Every other
word in the class fails to cancel `P`, a divisor of `D`.
Therefore **every word of this half-defect class with
`D=2^(2S)-3^(2n)>0` has reduced denominator greater than 1**.
This excludes the class from positive integer cycles of the
raw odd-only `3x+1` map, at all lengths and without any
near-critical hypothesis or external bound. It does not
exclude arbitrary four-mismatch rotations.

## Proof

### 1. Normalization and weighted endpoints

The cyclic normalization and integer-cut argument in
[`unequal-one-five-half-defect-classification`](../unequal-one-five-half-defect-classification/README.md)
give the following specialization. The rotation identity
`2^w_0 C_(R_1w)=3C_w+D` preserves `gcd(C_w,P)`.
Cutting after the first changed position transforms the
ordered half changes `(delta_1,delta_2)` into
`(delta_2,-delta_1)`. Iteration therefore normalizes them to

```
v_i=u_i+epsilon,   v_h=u_h+4,   i<h,   epsilon in {-2,2}.
```

Write `B=sum(u)`, `j=(epsilon+4)/2`, and `S=B+j`.
Split `C_u=X+Y+Z` at term indices `r<=i`, `i<r<=h`,
and `r>h`. Direct changes of prefix exponents give

```
epsilon=-2, j=1:  4*(2C_u-C_v)=4X+7Y-8Z;
epsilon=+2, j=3:      8C_u-C_v=7X+4Y-56Z.             (1)
```

Rotate `u` to begin after `h`, assign coefficients `(a,b)`
equal to `(4,7)` or `(7,4)` respectively, and give coefficient
`a` to the first `n-h+i` terms and `b` to the last `h-i` terms.
Both blocks are nonempty. Their weighted intercept is

```
M=sum_(r<n) b_r*3^(n-1-r)*2^(sum_(s<r)u'_s).
```

With `p=sum_(r<=h)u_r`, rotation of the three sums gives

```
3^(n-1-h)*2^p*M = 3^n*aZ+2^B*(aX+bY)
                = 2^B*(aX+bY-2^j*aZ)  (mod P).
```

Together with (1) and `C_(uv)=3^n C_u+2^B C_v`, this proves
`gcd(C_(uv),P)=gcd(M,P)`: all cancelled factors are powers
of 2 or 3, units modulo `P`.

Increase the last rotated letter by `j`. This gives total
`S` without changing `M`. If `P | M`, then `H=M/P>0` is
an integer and the weighted composition sends `-H` to `H`.
Every intermediate cut is integral, by reducing the endpoint
equation modulo each prefix power of 2 and cancelling the odd
suffix multiplier. Thus

```
2^r_i*x_(i+1)=3*x_i+b_i
```

holds with integer states, all `r_i>=1`, and final `r_i>=j+1`.
Inputs to `+4` are even, inputs to `+7` are odd, and `H`
has the parity of the first coefficient. The last endpoint
can have different parity from the last coefficient.

### 2. The coefficient order 4 then 7 is impossible

Here `H` is even, the final exponent is at least 2,
and the last `+4` exponent is the original decreased letter
`u_i>=3`. A negative even input remains negative under `+4`,
so the `+7` block starts at a negative odd integer.

Its first positive output comes from `-1`, giving 1 at
exponent 2 or 2 at exponent 1. If the block continues,
parity forces the odd output 1. The complete positive odd
orbit and its even exits are

```
1 --1--> 5 --1--> 11 --3--> 5;
-1 --1--> 2,   11 --2--> 10,   11 --1--> 20.
```

Arrow labels are division exponents. The only even endpoint
compatible with final exponent at least 2 is `H=10`.
But the `+4` segment would then start at `-10`; its only
integral first arrow is `-10 --1--> -13`. The odd output
cannot feed another `+4` step, so this must be the boundary
arrow. Its exponent 1 contradicts the required bound 3.

### 3. The coefficient order 7 then 4 has two tail shapes

Now `H` is odd and the final exponent is at least 4.
The even interface cannot be zero, since `3x+7=0` has no
integer solution. If it were negative, every subsequent
`+4` state would remain negative. Thus the interface is
positive. The preceding crossing and positive odd orbit
show that it belongs to `{2,10,20}`.

For each even `x`, enumerate all exponents
`1<=r<=v_2(3x+4)`. All except the largest yield even states
which may continue inside the block; the largest gives its
odd endpoint. The complete even closure is:

| Input | All even successors, with exponent | Odd endpoint, with exponent |
|---|---|---|
| 2 | none | 5 (1) |
| 4 | 8 (1), 4 (2), 2 (3) | 1 (4) |
| 8 | 14 (1) | 7 (2) |
| 10 | none | 17 (1) |
| 14 | none | 23 (1) |
| 16 | 26 (1) | 13 (2) |
| 20 | 32 (1), 16 (2), 8 (3), 4 (4), 2 (5) | 1 (6) |
| 26 | none | 41 (1) |
| 32 | 50 (1) | 25 (2) |
| 50 | none | 77 (1) |

Every even successor is listed, so induction proves closure
for paths of arbitrary length. The only odd endpoints with
exponent at least 4 are `20 --6--> 1` and `4 --4--> 1`.
Hence `H=1`. From the possible interfaces, all paths reaching
either terminal arrow are exactly

```
20 --6--> 1;                                         (I)
20 --4--> 4,  k copies of 4 --2--> 4,  4 --4--> 1.    (II)
```

In particular the interface is 20. Starting at `-H=-1`,
the preceding `+7` block must be

```
-1 --2--> 1 --1--> 5 --1--> 11,
t copies of 11 --3--> 5 --1--> 11,
then 11 --1--> 20.                                  (2)
```

All nonterminal `+7` outputs must be odd, fixing those
exponents, and the last arrow to 20 fixes exponent 1.

### 4. Reconstruction and the converse

Combining (2) with the two tails gives the exponent words

```
(2,1,1,(3,1)^t,1,6),
(2,1,1,(3,1)^t,1,4,2^k,4).
```

Undo the final increase by `j=3`. The resulting words are
exactly the two displayed `U` families. Raising the letter
at the end of the `+7` block by 2 and the final letter by
4 gives the respective `V`. The unchanged suffix after the
original second changed position shows that the simultaneous
half rotations reconstruct the original full word up to
cyclic rotation and exchange of the halves.

Conversely, every `t,k>=0` gives the displayed integral
segment from `-1` to 1. Each inserted loop preserves its
endpoints, so its weighted intercept is `M=P`. The weighted
gcd identity proves full plus-factor cancellation. This
also persists under every cyclic rotation.

Family (I) has a unique letter 7, and family (II) a unique
letter 5, proving primitivity. Their totals give `S=2n+1`,
so `gcd(2S,2n)=2` and the primitive cyclotomic factor is `P`.
Also

```
2^(2S)/3^(2n)=4*(16/9)^n>2.
```

Thus full primitive cancellation here lies outside the
explicit near-critical range.

### 5. A uniform affine bound excludes denominator 1

For either canonical family, set `alpha=3^n`,
`beta=2^sum(U)`, so `P=alpha+8beta`. Split `C_U=X+Y`
at its first changed letter. Since the last change affects
no intercept term, `C_V=X+4Y`, whereas `M=7X+4Y=P`.
Consequently

```
C_V=8C_U-P,
C_(UV)=P*(C_U-beta),
C_(UV)/D_(UV)=(C_U-beta)/(8beta-alpha).               (3)
```

The denominator on the right is positive since `S=2n+1`,
and the numerator is positive since `C_(UV)>0`.
To bound the ratio below 1, it suffices to prove
`alpha+C_U<9beta`.

Use the rational affine letter maps `F_a(x)=(3x+1)/2^a`.
Their composition for `U` satisfies
`F_U(1)=(alpha+C_U)/beta`; these auxiliary rational inputs
are not claimed to be integer odd-only orbit states.
The shared prefix `(2,1,1)` sends 1 to `7/2`.
Each `(3,1)` loop is `x -> (9x+11)/16`, preserving
`[11/7,7/2]`. The following letter 1 therefore gives at
most `23/4`.

For family (I), the last letter 3 gives
`F_U(1)<=73/32<9`. For family (II), the next letter 4
gives at most `73/64`. The map for letter 2,
`x -> (3x+1)/4`, preserves `[0,73/64]`; after any number
of its repetitions, the final letter 1 gives
`F_U(1)<=283/128<9`. These exact bounds hold for all
parameters. Equation (3) is therefore strictly between
0 and 1, and the reduced denominator exceeds 1.

Rotation preserves the reduced denominator by the same
intercept rotation identity. All other words in the class
fail `P | C`, hence fail `D | C` since `P | D`. This proves
the unconditional integer-cycle exclusion in the statement.

## Certificates

[`check_two_four.py`](check_two_four.py) checks every integral
arrow in the finite closure, all eight sign/order patterns
of the original defects, the weighted identities and
boundary condition, and the exact affine interval bounds.
It also checks finite samples of both parameter families
and reconstructs the base positive cycle. It replays all
eleven standard actual-cycle
[fixtures](../../../convergence/results/baseline-obligation-transfer-controls/README.md),
including every exact valuation, and verifies that none
belongs to this half-defect class. The closed
transition table and invariant intervals prove the
unbounded statements; the family samples are additional checks.

```
python3 areas/cycles/results/unequal-two-four-half-defect-classification/check_two_four.py
```

The deterministic receipt [`check_two_four.json`](check_two_four.json)
is regenerated with `--write-receipt`. Only the standard
library and exact arithmetic are used, with explicit
failure checks active under `python3 -O`.

## Remarks

- **Existing base cycle.** Family (I) at `t=0` has
  `C=194735`, `D=4135255`, `P=2291`, `G=11455`, and
  reduced denominator 361. Its positive `3x+361` cycle has
  minimum 17 and was already stored in
  [`actual-cycles-3x-d-corpus`](../actual-cycles-3x-d-corpus/README.md),
  at JSON pointer `/cycles/792`, discovery seed 17.
  No new-cycle claim is made.
- **Cancellation versus integer cycles.** Both families
  fully cancel the index-2 primitive factor, exceeding
  the primitive half bound outside the near-critical range.
  The remaining factor still prevents denominator 1.
  The exclusion uses the exact word structure and affine
  bound, not a universal assertion that `q=1` implies
  near-criticality.
- **Scope and controls.** Only the half-period class with
  absolute changes 2 and 4 is classified. The general
  [`rotation-distance-at-least-5`](../../questions/rotation-distance-at-least-5.md)
  question remains open. The base `3x+361` cycle and the
  standard `3x+5,7,13,61` sign-crossing controls remain
  valid; no general sign-preservation assertion is used.
  All eleven actual-cycle fixtures lie outside this class:
  their periods are odd except for the period-2 control,
  whose halves cannot differ at two distinct positions.
- **Novelty and status.** Novelty undetermined. Written
  proof and deterministic certificate; no independent-session
  review or Lean formalisation is claimed.

## History

- 2026-11-08: derived by the Codex cycle research lane
  (GPT-6 Astra; directed by Santiago Armstrong). A complete
  signed transition closure gives two infinite exceptional
  families. Uniform affine interval bounds then exclude
  denominator 1 throughout the half-defect class, at all lengths.
