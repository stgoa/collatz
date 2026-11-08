---
id: two-half-defect-mersenne-normal-form
kind: result
title: Unequal same-parity half defects have an exact two-segment Mersenne normal form
status: written
claim: >
  Raw odd-only positive valuation words, with C and D the additive-one
  intercept and denominator. For equal-length halves
  differing at exactly two positions with unequal same-parity absolute
  changes p<q, put J=(p+q)/2, r=(q-p)/2, 2S=sum(u)+sum(v), and
  P=2^S+3^n. Up to cyclic rotation, P divides C_(uv) exactly when the word
  is reconstructed from two nonempty signed odd-only segments with addends
  2^J-1 and 2^r-1, in either order, joining -h to h for a positive odd h.
  In high-to-low order, the last segment valuations must exceed p and r;
  in low-to-high order, the final valuation must exceed J. The explicit
  reconstruction preserves S as the sum of the segment valuations.
  At the canonical cut, C_v=2^s*C_u-hP with s=J or r respectively.
  If D>0, the normalized rational 3x+1 cycle state is
  (C_u-h*2^sum(u))/(2^s*2^sum(u)-3^n), and it is below 1 exactly when
  F_u(1)<2^s+h. This is an exact parametrization and conditional
  denominator-1 obstruction, not a proof of that inequality for every pair.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [antiperiodic-intercept-nondivisibility, baseline-obligation-transfer-controls]
certificates: [check_mersenne_normal_form.py]
evidence:
  - "check_mersenne_normal_form.json: coefficient identities, all sign/order patterns, forward and reverse reconstruction, known-family and actual-cycle controls"
tags: [cycles, denominators, half-defects, signed-orbits, normal-form, research-tool]
---

# Unequal same-parity half defects have an exact two-segment Mersenne normal form

## Statement

Throughout, `C_w` is the intercept of the affine `3x+1`
word composition and `D_w=2^sum(w)-3^len(w)`. The normalized
rational cycle state is `C_w/D_w`; for the same word under
`3x+d`, the actual state is `d*C_w/D_w`. The symbols `p,q`
below denote defect magnitudes, not the additive parameter.

For a positive word `A`, let `A[d]` mean that only its last
letter is increased by the integer `d`; use this notation
only when the resulting last letter is positive. Concatenation
is written by juxtaposition.

For an odd integer `x` and positive odd `d`, define the signed
odd-only map

```
T_d(x)=(3x+d)/2^v_2(3x+d),
```

where `v_2` uses the absolute value when the numerator is
negative. The map is undefined when `3x+d=0`. A segment
below consists entirely of nonzero odd integer states and
records the exact positive valuations of its arrows.

Fix integers `J>r>=1`, and set `p=J-r`, `q=J+r`.
These are precisely the unequal positive magnitudes `p<q`
of the same parity. Write

```
d_H=2^J-1,   d_L=2^r-1.
```

The following two constructions give **all** full plus-factor
cancellations for these magnitudes, up to cyclic rotation.
Both use two nonempty segments with valuation words `A,B`,
joining `-h -> z -> h`, where `h` is a positive odd integer.

| Segment order | Last-valuation conditions | Reconstructed halves | Normalized changes |
|---|---|---|---|
| `T_(d_H)` then `T_(d_L)` | `last(A)>p`, `last(B)>r` | `u=A[-p]B[-r]`, `v=AB[J]` | `(+p,+q)` |
| `T_(d_L)` then `T_(d_H)` | `last(B)>J` | `u=A[p]B[-J]`, `v=AB[r]` | `(-p,+q)` |

The two changed positions are the end of `A` and the end of
`B`, which are distinct because both blocks are nonempty.
In either row,

```
n=len(A)+len(B),   S=sum(A)+sum(B),   P=2^S+3^n,
sum(u)+sum(v)=2S,   P | C_(uv).                       (1)
```

Conversely, every pair of positive equal-length halves with
the stated defect magnitudes and `P | C_(uv)` can be put
into one of these forms by a cyclic cut. No bound on the
lengths, letters, parameters or intermediate states is used.

**Cycle-state criterion.** At the displayed canonical cut,
put `s=J` in the first row or `s=r` in the second row,
`alpha=3^n`, and `beta=2^sum(u)`. Then

```
C_v=2^s C_u-hP,
C_(uv)/D_(uv)=(C_u-h*beta)/(2^s*beta-alpha).           (2)
```

If `D_(uv)>0`, this state is positive and it is below 1
exactly when

```
F_u(1)=(alpha+C_u)/beta < 2^s+h.                     (3)
```

Under (3), the word and all its rotations have reduced
denominator greater than 1. The theorem does not assert
that (3) holds for every reconstructed segment pair.
Opposite-parity and equal-magnitude defects are outside
this statement.

## Proof

### 1. Canonical cuts and the positive weighted intercept

The rotation identity

```
2^w_0 C_(R_1w)=3C_w+(2^(2S)-3^(2n))
```

preserves divisibility by `P`, since `P | D` and 2 and 3
are units modulo `P`. If the changes at positions `i<h`
are `(delta_1,delta_2)`, cutting the full word after `i`
sends the ordered changes to `(delta_2,-delta_1)`.
By these cuts and a half exchange, one can arrange
`(+p,+q)` or `(-p,+q)`, preserving positivity.

Rotate both halves to start after the second change.
Their suffix after that change was common, so this is
a cyclic rotation of the full word followed by a half-turn.
The second changed position is now the final letter.
Let `X` be the terms of `C_u` up to and including the first
changed position, and `Y` the remaining terms. Both blocks
are nonempty, and `C_u=X+Y`.

In the positive case, set `s=J`. The prefix changes give

```
M_0=2^J C_u-C_v=(2^J-1)X+2^p(2^r-1)Y.              (4)
```

In the negative case, set `s=r`. Then

```
2^p M_0=2^p(2^r C_u-C_v)
       =2^p(2^r-1)X+(2^J-1)Y.                       (5)
```

Both are weighted intercepts with positive coefficients.
Concatenation and `3^n=-2^s*2^sum(u) (mod P)` show

```
P | C_(uv)  iff  P | M_0.
```

If divisibility holds, `h=M_0/P` is positive. It is odd:
each positive-word intercept is odd, so `2^s C_u-C_v` is
odd, and `P` is odd. The weighted intercept in (4) is `hP`;
the one in (5) is `2^p hP`.

Increase the last letter of `u` by `s`. Its total is `S`,
and its intercept is unchanged. The resulting weighted
composition sends `-H` to `H`, where `H=h` in (4) and
`H=2^p h` in (5). Every intermediate cut is integral:
the endpoint equation modulo a prefix power of 2 cancels
the odd suffix multiplier. This is the integer-cut argument
of [`antiperiodic-intercept-nondivisibility`](../antiperiodic-intercept-nondivisibility/README.md),
which works unchanged for arbitrary integer additive
coefficients.

### 2. Exact parity propagation through the even block

Write `K=2^p` and let the even coefficient be `K*d_L`.
In either weighted word, the last arrow of the even block
has exponent strictly greater than `p` and an odd output.
In (4), it is the final arrow, with exponent
`u_(n-1)+J>p`. In (5), it is the boundary arrow, whose
exponent is the original decreased letter `u_i>p`; its
output is odd because it feeds the odd-coefficient block.

For this last arrow, write its input and output as `x,y`
and its exponent as `a>p`. Then

```
3x=2^p*(2^(a-p)*y-d_L).
```

The bracket is odd, so the integer `x` has valuation
exactly `p`. Propagate backward: if the next state is
`2^p z` with `z` odd, any preceding exponent `a>=1` gives

```
3x=2^p*(2^a*z-d_L),                                 (6)
```

whose bracket is again odd. Thus every input in the
even block is `2^p` times a nonzero odd integer. This
argument excludes zero without a sign assumption.

Consequently all these inputs are `K` times nonzero odd
integers. Inputs to the odd-coefficient block are odd as
well. Its outputs are odd except for a terminal even
output where explicitly required below. This also rules
out an intermediate zero at that block: it cannot feed
another odd-coefficient step, or serve as the nonzero
interface or endpoint. No oddness or exactness is merely
assumed for the original weighted cuts.

### 3. Recovering the two ordinary signed segments

In (4), divide the even-block states by `K`. At the boundary,
increasing the preceding odd-block exponent by `p` changes
its output from `Kz` to `z`. The even block now has coefficient
`d_L`; reduce its final weighted exponent by `p` so that
its endpoint is `h`, rather than `h/K`.
The two ordinary segment words are therefore

```
A: first block, last exponent u_i+p > p;
B: second block, last exponent u_(n-1)+J-p
                              =u_(n-1)+r > r.
```

All cuts are odd, so every exponent is the exact valuation
of its nonzero numerator. This is the high-to-low row.

In (5), divide the first block's states by `K`, including
its start `-K h`. Decreasing its boundary exponent by `p`
preserves the unscaled odd interface `z`. The second block
has coefficient `d_H`; increasing its final weighted exponent
by `p` changes its endpoint from `K h` to `h`. Thus

```
A: first block, last exponent u_i-p >= 1;
B: second block, last exponent u_(n-1)+r+p
                              =u_(n-1)+J > J.
```

This is the low-to-high row. The total of the ordinary
segment words is `S` in both cases.

### 4. Reconstruction is the inverse operation

Start with either pair of ordinary segments in the table.
In high-to-low order, multiply the input states of the
second block by `K`, leaving its terminal endpoint `h`
unchanged. Decrease the first block's last exponent by `p`,
and increase the second block's last exponent by `p`.
This gives a weighted segment from `-h` to `h` with
coefficients `(d_H,K*d_L)`. Its exponent word is `u`
with its last letter increased by `J`.

In low-to-high order, multiply the input states of the
first block by `K`, leaving its odd interface unchanged.
Increase its last exponent by `p`, and decrease the
second block's last exponent by `p`. This gives a
weighted segment from `-K h` to `K h` with coefficients
`(K*d_L,d_H)`. Its exponent word is `u` with its last
letter increased by `r`.

The stated strict boundary bounds make every reconstructed
letter positive. The weighted endpoint equations give
`M_0=hP` using (4) or (5), hence `P | C_(uv)`. The displayed
changes of the last letters give precisely the two defects
and `sum(u)+sum(v)=2S`. These operations undo the forward
construction, proving both directions for all parameters
and all cyclic cuts.

### 5. The affine-state test

From `M_0=hP`, obtain `C_v=2^s C_u-hP` and
`P=alpha+2^s beta`. Therefore

```
C_(uv)=alpha*C_u+beta*C_v=P*(C_u-h*beta),
D_(uv)=P*(2^s*beta-alpha).
```

These are (2). If `D>0`, both the denominator in (2) and
its numerator are positive. Comparing (2) to 1 is exactly
`alpha+C_u<(2^s+h)beta`, or (3). A positive rational
cycle state below 1 is not an integer, so the reduced
denominator exceeds 1. The rotation identity preserves
that denominator. This is a conditional criterion; the
normal form alone supplies no general upper bound for
`F_u(1)`.

## Certificates

[`check_mersenne_normal_form.py`](check_mersenne_normal_form.py)
checks the coefficient formulas, cyclic normalization,
boundary conditions, and forward reconstruction on a
bounded grid stated in its receipt. Explicit ordinary
segments check the reverse construction in both orders,
including the known amplitudes `(1,5)` and `(2,4)` families
and an opposite-sign `(2,8)` example. It verifies (2) and
(3) by exact rational arithmetic and replays the eleven
standard actual-cycle fixtures.

```
python3 areas/cycles/results/two-half-defect-mersenne-normal-form/check_mersenne_normal_form.py
```

The deterministic receipt is
[`check_mersenne_normal_form.json`](check_mersenne_normal_form.json),
regenerated with `--write-receipt`. All checks use the
standard library, exact arithmetic and explicit failures
active under `python3 -O`. The written parity argument
and inverse construction establish the unbounded theorem.

## Remarks

- **Known cases recovered.** Magnitudes `(1,3)` give
  addends 3 and 1. Every defined signed odd step from a
  negative state under either map remains negative; the
  `+3` numerator can be zero at `-1`, but then no signed
  odd step exists. Thus the normal form recovers the
  [all-length exclusion](../unequal-one-three-half-defect-exclusion/README.md).
  The `(1,5)` and `(2,4)` families use addend pairs `(7,3)`
  and `(7,1)`; their finite closures and affine bounds are
  given in the respective
  [one/five](../unequal-one-five-half-defect-classification/README.md)
  and [two/four](../unequal-two-four-half-defect-classification/README.md)
  classifications.
- **Both orders occur.** For `J=5,r=3`, the low-to-high
  segments `-1 -> 1 -> 5 -> 11` under `+7`, with valuations
  `(2,1,1)`, and `11 -> 1` under `+31`, with valuation `(6)`,
  reconstruct `u=(2,1,3,1)`, `v=(2,1,1,9)`. Their changes
  are `(-2,+8)`, and their canonical rational state is `1/41`.
  The certificate verifies this control directly.
- **What remains.** The exact state test is a reformulation
  of the size of the canonical rational state, not a new
  universal bound. The research target is to prove a bound
  such as (3), or a weaker integrality obstruction, using
  the two linked ordinary signed segments and their high
  boundary valuations. No claim that every `q=1` cycle is
  near-critical is needed or made.
- **Relation to earlier failed elimination.** The
  [termwise-divisibility attempt](../../attempts/termwise-plateau-divisibility.md)
  and [three-arc elimination](../../attempts/three-arc-intercept-elimination/README.md)
  warn against dropping coupled coefficients. Here the
  whole weighted intercept is retained. Integer cuts and
  exact 2-adic propagation convert it into two ordinary
  signed orbits; no divisibility of separate summands is
  inferred. The conversion does not itself resolve the
  remaining denominator factor.
- **Scope, controls and novelty.** The result parametrizes
  full plus-factor cancellation in the stated two-half
  class. It excludes neither arbitrary four-mismatch words
  nor general `3x+d` cycles. Actual-cycle and signed-crossing
  controls are retained. Novelty undetermined; written
  proof only, without an independent-session review or
  Lean formalisation.

## History

- 2026-11-08: derived by the Codex cycle research lane
  (GPT-6 Astra; directed by Santiago Armstrong). Exact
  valuation propagation unifies the previous weighted
  two-block arguments into a bidirectional signed-Mersenne
  parametrization and separates the remaining affine-state
  bound from the normal-form theorem.
