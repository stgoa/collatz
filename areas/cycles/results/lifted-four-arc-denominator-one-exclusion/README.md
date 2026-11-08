---
id: lifted-four-arc-denominator-one-exclusion
kind: result
title: A lifted four-arc family has no denominator-one word
status: written
claim: >
  Raw odd-only clock. For integers r>=2, a,b>=1 and c>=2, let
  z=(1^(2r-4),a,1,c,1^(2r-2),c,1,b), and replace each letter d of z
  by the two-letter block (2,d), obtaining W. For every such W with
  D_W=2^sum(W)-3^len(W)>0, its reduced denominator is greater than 1,
  using the replayed effective gap and a self-contained finite descent
  and product certificate.
  No near-critical or parity hypothesis is imposed. An explicit
  resultant is always nonzero, and positivity bounds its dyadically
  reduced value by 1703025*K^2/2, where K=2^(a+b+2c-4).
  A hypothetical denominator-one member would have r<=511 and hence
  at most 4088 odd steps, which the attached exact certificate excludes.
  The shift 4r-2 has at most four mismatches. The class includes
  primitive near-critical words with unbounded shortcut local-minimum
  count, so it is not restricted to finitely many circuits.
authors:
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [baseline-obligation-transfer-controls]
assumes: [musson-collatz-gap-all]
certificates: [check_resultant.py]
evidence:
  - "check_resultant.json: symbolic identities, exact cutoff, descent through 2^21, product exclusion through 4088 steps, parameter checks, structural examples and 3x+d controls"
tags: [cycles, four-arcs, denominators, resultants, effective-exclusion, lifted-words]
---

# A lifted four-arc family has no denominator-one word

## Statement

For integers `r>=2`, `a,b>=1`, `c>=2`, set

```
z = (1^(2r-4), a, 1, c, 1^(2r-2), c, 1, b).
```

Here `1^j` means `j` copies of the letter 1, allowing `j=0`.
Let `W` be obtained by replacing every letter `d` of `z` by
the two-letter word `(2,d)`. Its length and total are

```
m=8r,     A=12r+s,     s=a+b+2c-4>=2.
```

**If `D=2^A-3^m>0`, then `den(W)=D/gcd(C_W,D)>1`.**
Thus no positive integer cycle of the raw odd-only `3x+1`
map has this word, or a cyclic rotation of it. There is no
bound on `r,a,b,c`, and no restriction on the parity of `A`
or on the drift. Primitivity is not required.

The only external input is the replayed
[effective gap](../../../../sources/musson-collatz-gap-all.md),
`2^A <= 2^172*m^341*(2^A-3^m)` whenever `m>0` and `D>0`.

The new arithmetic reduction is elementary: a denominator-one
member would have `r<=511`, hence at most 4,088 odd steps.
The attached certificate excludes every nontrivial integer
cycle of at most that length using descent through `2^21`
and exact product inequalities. No published convergence
verification or cycle-period bound is imported.

### Structural scope

Under the shift `2r-1`, the letters of `z`, starting at `b`,
are read in the cyclic order `(b,c,c,a,1^(4r-4))`. After the
lift, the shift `h=4r-2` preserves the fixed 2 positions and
has exactly

```
[a!=1]+[a!=c]+[b!=1]+[b!=c] <= 4
```

mismatches; `gcd(h,8r)=2`. It has four mismatches when
`a,b` both avoid `{1,c}`. This is one specified track shape,
not a classification of arbitrary four-mismatch words.

In the shortcut clock, every odd valuation at least 2 gives
one descending even run and hence one local minimum. The
lift inserts `4r` such letters, in addition to the two `c`
positions and any high `a,b`. This count is unbounded even
among primitive near-critical members: for every `r>=16`,
choose `a=3`, `c=2`, and

```
b = bit_length(3^(8r))-12r-3.
```

The inequality `3^16>2^25` gives `b>r/2-3>=5`, so the
unique letter `b` proves primitivity. The total is precisely
`bit_length(3^(8r))`, giving `3^m<2^A<2*3^m`. These words
have four mismatches at `h` and `4r+4` shortcut local minima.
Thus the theorem is not just an application of a fixed
small-local-minimum exclusion.

## Proof

### 1. The block map and a polynomial intercept

The block `(2,d)` acts on a rational input by

```
x -> (9x+7)/2^(d+2).
```

Put

```
Q=2^a,   T=2^b,   R=2^c,   K=2^s=Q*T*R^2/16,
X=8^r,   Y=9^r.
```

Then `D=KX^4-Y^4`. The block intercept has a common factor
7, so write `C_W=7C_*`, where `C_*` is the integer intercept
of the same `4r` block maps with additive constant 1.
Direct concatenation gives

```
2048C_* = 2048Y^4+N X^2Y^2+Z X^4,                         (1)
N = 18[Q(17+32R)-162],
Z = 4QR(17R-162).
```

Here is a derivation independent of a parameter sample.
The constant block has numerator multiplier 9, denominator
8, and intercept 1. Its run of length `j` has intercept
`9^j-8^j`. Relative to these constant blocks, the three
nonfinal markers multiply subsequent denominator prefixes
by `Q/2`, then `R/2`, then `R/2`. Splitting the intercept
sum at those three positions therefore gives

```
C_* = Y^4
    + [(Q/2-1)*(9/8)^3 + Q(R-2)*(9/8)/4]*X^2Y^2
    + [QR(R-2)*(9/8)^2/8 - QR^2/8]*X^4.
```

Multiplication by 2048 gives (1). The last marker `b`
affects the total, not the intercept. The certificate also
checks (1) as a polynomial identity using the concatenation
law, with formal variables for the two long-run weights.

### 2. Elimination retains the factor 7

Assume for contradiction `den(W)=1`, so `D | C_W`.
Reducing (1) modulo `D`, where `Y^4=KX^4`, and cancelling
only powers of 2 gives

```
D | 7(LX^2+NY^2),
L = 2048K+Z = 4QR[(32T+17)R-162].                          (2)
```

Both `L` and `N` are positive for `Q,T>=2`, `R>=4`.
Multiplying the expression in (2) by
`7(LX^2-NY^2)` and using `Y^4=KX^4` gives

```
D | 49E,       E=L^2-KN^2.
```

The factor 7 need not be a unit modulo `D` and is not
cancelled. An exact factorization is

```
E = (QR^2/4)*F,                                           (3)
F = 64Q[(32T+17)R-162]^2
             -81T[Q(17+32R)-162]^2.
```

The factor `QR^2/4` is a power of 2. Since `D` is odd,
we obtain the useful divisibility **`D | 49F`**.

### 3. The resultant cannot vanish

If `s` is odd, `K=2^s` is not a rational square.
The equality `L^2=KN^2` contradicts the parity of the
2-adic valuations, since `L,N>0`.

If `s` is even, write `K=U^2`, `U=2^t>=2`.
Since `L,N>0`, vanishing means `L=UN`, hence

```
Q = (2048U^2+2916U)
      /[18(17+32R)U-4R(17R-162)].                         (4)
```

The denominator is positive. The numerator has 2-adic
valuation `t+2`; the denominator's two displayed terms
have valuations `t+1` and `c+3`, respectively. The latter
uses `c>=2`, which gives `v_2(17R-162)=1`.

If `c+2<t`, unequal valuations in the denominator force
`Q=U/(2R)`. Substituting into (4) yields

```
(153-1760R)U = R(2592+34R),
```

impossible because the left side is negative for `R>=4`
and the right side is positive.

If `c+2>t`, (4) forces `Q=2`. The inequality between
the integer exponents gives `R>=U/2`, while
`T=8U^2/R^2>=2` gives `R<=2U`. Since `R,U` are powers
of 2, their ratio is one of `1/2,1,2`. Substitution into
the remaining equation

```
256U^2+(288-144R)U+17R^2-162R=0
```

gives, respectively,

```
(753/4)U^2+207U,     129U^2+126U,     36U(U-1),
```

all strictly positive for `U>=2`.

Finally, if `c+2=t`, then `R=U/4`, and (4) becomes

```
Q = 16(512U+729)/(559U+1872).
```

This lies strictly between 8 and 16 for `U>=2`, so it is
not a power of 2. Thus **`E!=0` and `F!=0` in every case**.
No exceptional algebraic family has been discarded.

### 4. Positivity bounds the reduced resultant

The two bracketed expressions in (3) are positive and obey

```
(32T+17)R-162 <= (81/2)TR,
Q(17+32R)-162 <= (145/4)QR.
```

Since `QTR^2=16K`, these bounds give

```
|F| <= max(1679616KT,1703025KQ).
```

Also `Q,T>=2` imply `max(Q,T)<=8K/R^2<=K/2`.
Consequently

```
0 < |F| <= (1703025/2)K^2 < 2^20 K^2,
D <= 49|F| < 2^26 K^2.                                  (5)
```

The bound uses positivity of both outer markers. Bounding
an unreduced resultant would lose the dyadic factor in (3)
and would give a weaker estimate.

### 5. The gap and the integer-cycle product force a small period

The [effective gap](../../../../sources/musson-collatz-gap-all.md),
applied with the actual odd-step length `m=8r`, says

```
K*4096^r = 2^A <= 2^172*(8r)^341*D.
```

Combining this with (5) gives

```
4096^r < 2^1221*r^341*K.                                 (6)
```

Because `den(W)=1`, its rational cycle is a positive integer
cycle. The word contains a letter 1 and therefore is not
a repetition of the trivial valuation word `(2)`. An
integer cycle containing state 1 is trivial, so all its
states are at least 3. Multiplying its exact arrows gives

```
2^A = product_(i<m)(3+1/n_i) <= (10/3)^(8r),
K <= [(10/3)^8/4096]^r.                                  (7)
```

This is an unconditional product bound for the assumed
integer cycle, not a near-critical assumption. Substituting
(7) into (6) yields

```
(12/5)^(8r) < 2^1221*r^341.
```

The exact inequality `12^8>2^10*5^8` therefore implies

```
10r < 1221+341*log_2(r).                                 (8)
```

If `r>=512`, take the integer `k>=9` with
`2^k<=r<2^(k+1)`. Then (8) would require
`10*2^k < 1221+341*(k+1)`. This fails at `k=9`:
`5120>4631`; and the gap increases with `k`, since
`10*2^k>341`. Thus `r<=511` and `m<=4088`.

### 6. A finite descent and product certificate excludes the remaining lengths

Put `L=2^21`. For every odd seed `3<=n<L`, the attached
certificate applies the raw odd-only `3x+1` map until the
value is strictly smaller than `n`. It verifies this for
all 1,048,575 seeds, using 3,651,430 odd steps in total;
the longest individual descent has 141 steps. The loop
has a fixed failure guard, so a failure cannot run forever.
Induction on the odd seeds, starting at 1, proves that
every positive odd integer at most `L` reaches 1.
Therefore every state of a nontrivial integer cycle is
strictly greater than `L`.

For each integer `1<=m<=4088`, the certificate verifies
the exact integer inequality

```
(3L+1)^m < 2^bit_length(3^m) * L^m.                       (9)
```

There is no rounding in (9): both powers on the left and
`3^m` are updated by integer multiplication, while the
right side is a power of 2. A positive integer cycle
with `m` odd steps would have

```
2^A = product_(i<m)(3+1/n_i)
     <= (3+1/L)^m
     < 2^bit_length(3^m).
```

But `2^A>3^m` requires the integer `A` to be at least
`bit_length(3^m)`, a contradiction. This argument also
allows repeated traversals. Hence the length bound from
section 5 is impossible, and `den(W)>1`.
The standard intercept rotation identity preserves the
reduced denominator, so the conclusion also covers all
cyclic cuts of the word.

## Certificates

[`check_resultant.py`](check_resultant.py) verifies the
intercept and resultant factorizations by symbolic polynomial
arithmetic, the algebra in the three zero-resultant branches,
and the exact constants in the size and dyadic-cutoff bounds.
It independently evaluates the full ordinary `3x+1` word
intercepts in a finite parameter box, including both total
parities. Those samples supplement the written universal
proof; they are not used to exclude all parameters.

The finite descent and all 4,088 inequalities (9) are
recomputed on every certificate run. It also checks the
track mismatch formula, positive
near-critical examples with growing local-minimum counts,
and all eleven standard `3x+5,7,13,61`
[fixtures](../../../convergence/results/baseline-obligation-transfer-controls/README.md)
by their actual arrows and product identities. The `q=1` product
specialization in (7) is not applied to these other maps.

```
python3 areas/cycles/results/lifted-four-arc-denominator-one-exclusion/check_resultant.py
```

The deterministic receipt is [`check_resultant.json`](check_resultant.json),
regenerated with `--write-receipt`. The script uses only the
standard library and exact arithmetic, with failure checks
active under `python3 -O`. It does not re-prove the one
external effective-gap input.

## Remarks

- **Relation to the earlier sparse family.** The unlifted
  [four-arc classification](../sparse-four-arc-near-critical-classification/README.md)
  has at most four shortcut local minima. The block lift
  studied here has unboundedly many, including in the
  primitive near-critical subfamily described above. The
  lift changes the affine numerator from `3x+1` per letter
  to `9x+7` per block; the factor 7 remains in the proof.
- **Other structural exclusions.** The
  [fixed-defect theorem](../repeated-block-cancellation-bound/README.md)
  fixes its defect while the repeated block grows; here both
  long runs and all three marker values vary. The natural
  representation in the [shared-background law](../shared-background-denominator-law/README.md)
  has background `(2)` of length 1 and `4r` markers, so its
  background-length restriction supplies no exclusion here.
  The [equal-total two-block theorem](../equal-total-two-block-exclusion/README.md)
  needs a different decomposition, which is not automatic:
  the lifted `(r,a,b,c)=(3,3,5,2)` example has no such
  representation under any cut. The certificate checks that
  finite comparison; no general disjointness claim is made.
- **Limits.** This excludes one specified structural class
  at denominator 1, using the declared effective-gap input.
  It neither excludes arbitrary positive cycles nor gives
  an asymptotic bound for all four-mismatch words. The
  general [rotation-distance target](../../questions/rotation-distance-at-least-5.md)
  remains open.
- **Novelty and status.** Novelty is undetermined. Written
  proof and reproducible algebra checks; no independent-session
  review or Lean formalisation is claimed.

## History

- 2026-11-08: Codex four-arc research lane (GPT-6 Astra;
  directed by Santiago Armstrong) derived the lifted block
  intercept, proved the resultant nonzero for both parities,
  and combined its positive-letter bound with the recorded
  effective gap. A local descent and exact product certificate
  closes the remaining finite length range.
