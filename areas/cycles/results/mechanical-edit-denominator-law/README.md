---
id: mechanical-edit-denominator-law
kind: result
title: Few changes to a mechanical word force denominator growth
status: written
claim: >
  Raw odd-only clock. Let W be a primitive positive word of length
  m>=2, total A and D=2^A-3^m>0. Compare it with any positive
  mechanical word U of length m, total F and arbitrary phase.
  Let s count changed positions, B=sum max(U_i-W_i,0), and
  t=floor((m-2)/(s+1)). Unconditionally,
  den(W)>3^(t+1)*min(1,2^F/3^m)*D/(2^(B+1)*m*2^A).
  For s>=1 there is also an unconditional all-slope law
  den(W)>2^(3m/[5(4^s-1)])*D/(32m*2^A), independent of edit
  amplitudes. Under only the replayed gap EXT-1, a denominator-one word of
  length m>=2^32 differs in more than sqrt(m) positions from
  every contracting mechanical word (2^F>3^m). No ordering of
  cycle states is assumed. Also under only EXT-1, denominator
  one is excluded at every length when s<=2,
  with arbitrary increases, decreases, phases and edit positions.
  The finite closure uses a local descent below 2^18 and exact
  comparisons through m=2^18-1. With the additional declared
  Barina convergence input, the replayed period bound excludes
  denominator one for every s<=10 at every mechanical base slope.
  Arbitrary four-mismatch and nonprimitive words are not excluded.
authors:
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [paired-state-run-law, mechanical-word-exact-denominator, cycle-length-lower-bound-from-convergents]
assumes: [musson-collatz-gap-all, barina-2025-convergence-2-71]
certificates: [check_edit_law.py]
evidence:
  - "check_edit_law.json: mechanical factors and signed edits, reduced-cycle inequalities, exact cutoffs, finite length closure, local descent and actual-cycle controls"
tags: [cycles, mechanical-words, denominators, factor-complexity, edit-distance]
---

# Few changes to a mechanical word force denominator growth

## Statement

For integers `m>=2`, `F>=m`, and `0<=ell<m`, put

```
U_i=floor(((i+1)F+ell)/m)-floor((iF+ell)/m),  0<=i<m.
```

These include all phases and both lower and upper mechanical
conventions. Let `W` be any primitive positive word of the same
length, with total `A` and `D=2^A-3^m>0`. Define

```
q=den(W)=D/gcd(C_W,D),       beta=F/m,
s=#{i:W_i!=U_i},            B=sum_i max(U_i-W_i,0),
t=floor((m-2)/(s+1)),       R=max(1,3^m/2^F).
```

Here `s` is Hamming distance, while `B` retains the total size of
the decreases. Increases have arbitrary size, and the total `F`
of the comparison word need not equal `A`.

**General denominator law, with no external input:**

```
q > 3^(t+1)*D / [2^(B+1)*m*R*2^A].                    (1)
```

With the sole external input
[EXT-1](../../../../sources/musson-collatz-gap-all.md),
`2^A<=2^172*m^341*D`, this becomes

```
q > 3^(t+1) / [2^(B+173)*m^342*R].                     (2)
```

There is also an **all-slope law**, retaining no edit-amplitude cost.
For `s>=1`, put `K_s=5(4^s-1)/3`. Then

```
q > 2^(m/K_s)*D/(32m*2^A),                              (U1)
q > 2^(m/K_s-177)/m^342  under EXT-1.                    (U2)
```

The following consequences distinguish their inputs explicitly:

1. **Distance from every contracting mechanical word.** For a
   hypothetical primitive `3x+1` cycle, if `2^F>3^m` and `m>=8s`,
   then, with `alpha=log_2(3)`,

   ```
   alpha*(m-2) < (s+1)*(s+173+342*log_2(m)).             (3)
   ```

   Consequently, for every `m>=2^32`, its valuation word differs
   in **more than `sqrt(m)` positions from every contracting
   mechanical word** of length `m`, with every total and phase
   allowed. This includes the mechanical words with total `F=A`.
   No circular-order or normalized-height-order hypothesis is used.

2. **Two arbitrary changes, with only EXT-1.** Every primitive
   positive word with `s<=2` and `D>0` has `q>1`, with all mechanical
   base slopes, phases, edit positions and positive replacements
   allowed. A local finite closure proves this at every length.

3. **Ten arbitrary changes, with an additional convergence input.**
   With [Barina's declared verification input](../../../../sources/barina-2025-convergence-2-71.md),
   every such word with `s<=10` has `q>1`. This uses the
   [replayed odd-period lower bound](../cycle-length-lower-bound-from-convergents/README.md)
   `m>=72,057,431,991`. That external convergence input is used only
   for this third consequence; (1), (U1), the square-root result
   and the two-edit closure do not use it.

These are restrictions on specified comparison classes. They do
not identify Hamming distance to a mechanical word with rotation
distance, and do not exclude arbitrary four-mismatch candidates.

## Proof

### 1. Count all unchanged windows

A mechanical word has at most `t+1` distinct length-`t` cyclic
factors. Indeed, at phase `a` in `0,...,m-1`, its first `j` letters
sum to `floor((jF+a)/m)`. Each of these `t` prefix sums changes at
at most one threshold as `a` varies. This partitions the phases
into at most `t+1` factor classes. No coprimality is required.

An edit lies in at most `t` of the `m` cyclic length-`t` windows.
Thus at least `m-st` windows remain unchanged. By the choice of `t`,

```
(s+1)t<=m-2,       m-st>=t+2.
```

Two unchanged windows are therefore equal. This counts windows
across all unchanged arcs; it does not discard every arc except
the longest one. At `t=0` all windows are empty and the same
counting statement holds.

Realize `W` as its reduced positive odd integer `3x+q` cycle via
the [word-cycle correspondence](../mechanical-word-exact-denominator/README.md).
Primitivity makes its odd states distinct. If the common factor
has total `E`, the
[paired-state run law](../paired-state-run-law.md) gives

```
z_start=2^(E+1)*b,       z_end=2*3^t*b,       b!=0.
```

Hence, writing `H` for the maximum odd state,

```
H > 2*3^t.                                              (4)
```

Cyclic or overlapping windows cause no difficulty. For `t=0`,
two distinct odd states still differ by a nonzero even integer.

### 2. Mechanical balance controls growth despite signed edits

Every cyclic factor of `U` of length `j<m` has total greater than
`beta*j-1`. Its counterpart in `W` loses at most `B` in total, so

```
sum(factor of W) > beta*j-1-B.                          (5)
```

Set `rho=3/2^beta` and `K=2^(B+1)`. Each such factor's affine
slope is at most `K*rho^j`. Starting at a state `x_0`, the exact
affine expansion for a segment of length `l<m` is

```
x_l = (3^l/2^E_l)*x_0
      +(q/3)*sum_(j=1)^l [3^j/2^(total of the length-j suffix)].
```

Apply (5) to the full segment and every suffix. Since
`rho^j<=max(1,rho^m)=R` for `0<=j<m`,

```
x_l <= K*R*(x_0+mq/3).
```

The minimum `L` reaches `H` within `m-1` odd steps. Thus

```
H <= K*R*(L+mq/3).                                     (6)
```

The cycle product identity and logarithm inequalities give

```
ln(2^A/3^m)=sum_i ln(1+q/(3n_i)) < mq/(3L),
ln(2^A/3^m)>D/2^A,
L < mq*2^A/(3D).
```

Since `D<2^A`, equation (6) implies

```
H < K*R*(2mq*2^A)/(3D).
```

Combine this with (4) to obtain (1). Substitution of EXT-1 gives
(2). None of this argument assumes `q<=L` or that the base expands
or contracts.

### 3. At denominator one, decreases are small

Suppose `q=1`. A primitive cycle of length `m>=2` cannot contain
the fixed point 1, so all its odd states are at least 3. Therefore

```
2^A=product_i(3+1/n_i) <= (10/3)^m < 2^(7m/4),
A < 7m/4.                                               (7)
```

The last strict comparison is the integer inequality
`10^4<2^7*3^4`.

Every decrease is at most `ceil(beta)-1<beta`. In particular,
the universally valid weak inequalities are

```
B<=s*beta,       A>=F-B>=beta*(m-s).
```

These also cover `s=0`. If `m>=8s`, then `m-s>0` and (7) gives

```
beta <= A/(m-s) < 7m/[4(m-s)] <= 2.
```

The base letters are therefore 1 or 2, and each decrease is at
most one:

```
B<=s.                                                   (8)
```

For a same-total comparison `F=A`, (7) gives `beta<2` and (8)
directly, without the condition `m>=8s`.

### 4. Contracting backgrounds require square-root distance

If `2^F>3^m`, then `R=1`. Equations (2) and (8), with `q=1`, give
`alpha*(t+1)<s+173+342*log_2(m)`. Since
`t+1>(m-2)/(s+1)`, this proves (3).

Suppose `m>=2^32` and `s<=sqrt(m)`. Then `m>=8s`. Set
`C=173+342*log_2(m)`. For every such `m`,

```
C+1 < sqrt(m)/4.                                       (9)
```

At `m=2^32`, this says `11118<16384`. The difference between
the right and left sides increases thereafter: its derivative
is `1/(8sqrt(m))-342/(m*ln2)>1/(8sqrt(m))-684/m>0`, using
`ln2>1/2` and `sqrt(m)>=65536>5472`.

Consequently,

```
(s+1)(s+C)
 <= m+(C+1)sqrt(m)+C
 < 5m/4+sqrt(m)/4-1
 < 3(m-2)/2
 < alpha*(m-2).
```

The penultimate inequality is equivalent to `m-sqrt(m)>8`,
valid here; the last uses `3^2>2^3`. This contradicts (3).
Thus `s>sqrt(m)` for every contracting mechanical comparison.

### 5. A clean mechanical run has bounded length at its starting state

Let a clean run have length `l` and start at the odd state `x`.
For `l>=1`, put `v=floor((l-1)/2)`. The `v+2` windows of length
`v` starting at `0,...,v+1` fit inside the run. Two repeat; if their
common valuation total is `E`, then `E>beta*v-1`. The run law gives
a nonzero starting-state difference divisible by `2^(E+1)`.
Thus one of those starting states is greater than `2^(beta*v)`.

The affine balance bound, now with no edits, bounds all these
early states by

```
2*max(1,rho^(v+1))*(x+q(v+1)/3),       rho=3/2^beta.
```

If `rho>1`, divide by `rho^(v+1)` and use `2rho<=3`, since
`beta>=1`. Also `2beta-alpha>=2-alpha>2/5`. If `rho<=1`, use
`beta>=alpha>2/5` directly. In either case,

```
2^(2v/5) < 3x+q(v+1) <= 3(x+qm).
```

Since `l<=2v+2` and `alpha<8/5`, this implies

```
l < 5*log_2(x+qm)+10.                                  (10)
```

For `l=0` the same inequality is automatic; no negative `v` is
used. The strict slope comparisons here are `3^2>2^3` and
`3^5<2^8`.

### 6. Choose a cut adjacent to an edit and use exactly s chunks

Assume `s>=1`. The edited arrows delimit `s` clean runs, allowing
empty runs. Choose a clean run containing the minimum state `L`,
including either endpoint. Set `eta=D/2^A`.

If `rho>1`, cut at the start `x` of that run, just after an edited
arrow. Along the prefix from `x` to `L`, mechanical balance gives
its multiplier greater than `rho^j/2>=1/2`, so `x<2L` (also true
when `j=0`). The cycle splits into exactly `s` chunks, each a clean
run followed by one edited arrow.

If `rho<=1`, cut at the end `x` of the chosen run, just before an
edited arrow. The clean suffix from `L` to `x` gives
`x<2(L+mq/3)`; the zero-length case also satisfies this bound.
The cycle now splits into exactly `s` chunks, each one edited arrow
followed by a clean run. Every edit and every odd step is counted
once in either construction.

For any starting state put `N=x+qm` and `Z=log_2(N)+3`. Every odd
step, including an edited one, satisfies

```
N_next <= (3/2)N < 2^(3/5)N.
```

For a clean-first chunk, (10) gives length
`l+1<5log_2(N)+11=5Z-4`. For an edit-first chunk, its first step
changes `log_2(N)` by less than `3/5`, and (10) gives length
`l+1<5log_2(N)+14=5Z-1`. Therefore every chunk satisfies

```
chunk length < 5Z,       Z_next < 4Z.                   (11)
```

The minimum bound from section 2 gives `L<mq/(3eta)`. Both choices
of initial cut consequently satisfy

```
N_0 < (7/3)*mq/eta,
Z_0 < log_2(q)+log_2(m)+log_2(1/eta)+5.
```

Summing the `s` chunk bounds from (11),

```
m < 5*(1+4+...+4^(s-1))*Z_0 = K_s*Z_0.
```

Rearrangement proves (U1); EXT-1 proves (U2). The base slope and
all edit amplitudes have disappeared. The case `s=0` is precisely
mechanical and its denominator-one exclusion is already supplied
by the [exact mechanical theorem](../mechanical-word-exact-denominator/README.md).

### 7. All two-edit lengths close using only EXT-1

For `1<=s<=2`, `K_s<=25`. If `q=1`, (U2) gives

```
log_2(q) > m/25-177-342*log_2(m).                       (12)
```

At `m=2^18`, the right side is `103819/25>0`. It increases
thereafter: its derivative exceeds `1/25-684/m>0`, since
`ln2>1/2` and `2^18>17100`. Hence `m<2^18`.

For the remaining lengths put `A_min=bit_length(3^m)` and
`D_min=2^A_min-3^m`. Since `D/2^A` increases with `A`, the
certificate's exact comparisons, for every `560<=m<2^18`,

```
2^floor(m/25)*D_min > 32m*2^A_min                       (13)
```

make the lower bound in (U1) exceed one for all admissible totals.

The certificate also replays that every odd seed `3<=x<2^18`
reaches a smaller positive odd integer under `3x+1`. Induction
proves that they all reach 1. A nontrivial cycle therefore has
minimum greater than `L_*=2^18`, whose endpoint is even. For every
`2<=m<=559`, the certificate checks

```
(3L_*+1)^m < 2^A_min*L_*^m.                            (14)
```

The cycle product would give `2^A<=(3+1/L_*)^m<2^A_min`,
impossible. This completes the two-edit exclusion without an
external period or convergence-range bound.

### 8. Ten edits with the separately declared period input

For `1<=s<=10`, `K_s<=K_10=5(4^10-1)/3`. If `q=1`, (U2)
requires

```
m < K_10*(177+342*log_2(m)).                            (15)
```

The certificate verifies

```
K_10*(177+342*35)<2^35,       684*K_10<2^35.
```

Thus (15) fails at `m=2^35` and thereafter: the derivative of
`m-K_10*(177+342*log_2(m))` is greater than
`1-684*K_10/m>0`. So `m<2^35`.

The [replayed continued-fraction bound](../cycle-length-lower-bound-from-convergents/README.md),
conditional on [Barina's external convergence verification](../../../../sources/barina-2025-convergence-2-71.md),
requires `m>=72,057,431,991>2^35` for a nontrivial `3x+1` cycle.
This contradiction closes the ten-edit class. The computation
below `2^71` is not replayed here; it is an additional assumption
only of this consequence.

## Certificates

The deterministic [certificate](check_edit_law.py) checks the
mechanical phase and factor identities, arbitrary cyclic edit
positions, increases and decreases, reduced actual cycle arrows,
the growth and denominator inequalities, and the exact cutoff
constants. It checks the minimum-adjacent cut, exactly `s` chunks,
their growth inequalities, and the unconditional all-slope law.
It replays all comparisons (13)-(14), every required
odd descent below `2^18`, and the eleven standard actual-cycle
fixtures for `d=5,7,13,61`. A fixed per-seed guard makes descent
failure terminate. The [receipt](check_edit_law.json) gives all
finite ranges and counts. Checks remain active under `python3 -O`.

The finite word samples test the formulas; they do not replace
the arbitrary-length proof. Only (13)-(14) and local descent are
exhaustive finite steps in the EXT-1-only two-edit exclusion.

## Remarks

**Relation to the earlier one-edit law.** The
[one-edit result](../one-edit-mechanical-denominator-growth/README.md)
uses generic maximum growth and treats every base slope. Here all
unchanged windows are counted together, and mechanical balance
improves the maximum-growth estimate while retaining the loss `B`
from negative edits. This gives the contracting-background square-root
distance. Controlling clean runs separately, with a cut adjacent to
an edit, also gives the all-slope law and two-edit exclusion.
The coefficients may be weaker than the one-edit law in some
one-edit cases; no claim of uniform numerical dominance is made.

**Antecedents and distinct parameters.**
[Lyapunov Weaver (2026), sections 6-7](../../../../sources/lyapunov-weaver-2026-finite-mechanical-approximation.md)
already combines bounded substitutions and mechanical growth to
obtain square-root separation for parity prefixes from critical
irrational Sturmian factors. Here substitutions change odd-only
valuations by arbitrary amounts, the comparison is rational and
contracting, and the cycle gap eliminates the initial state.
The square-root mechanism itself is not claimed as new.

Repeated-factor separation
is the established [cycle-word repeat method](../cycle-word-repeat-bound/README.md),
with the complexity antecedent credited in
[Dubickas (2009)](../../../../sources/dubickas-2009-linear-map-complexity.md).
The existing [ordered-cycle square-root law](../ordered-cycle-height-change-growth.md)
and [its derivation](../ordered-cycle-sparse-forcing/ORDER_RIGIDITY.md)
concern changes of dyadic height in sorted normalized rank, with
an ordering hypothesis. The present square-root statement needs
no ordering, but its parameter is Hamming distance from a separate
contracting mechanical word. The two counts are not identified,
and this is not a theorem about all chronological minima or all
rotation mismatches. Novelty of the scoped result is undetermined.

The [fixed expanding-background theorem](../expanding-background-defect-growth/README.md)
instead fixes a repeated base word and allows all substitutions.
Here the mechanical total, phase and primitive period all vary.
The published `(1,2)`-perturbation result cited there is a fixed
periodic-background exclusion, not this varying-template statement.

**Controls and limits.** The genuine `3x+5` cycle with word
`(1,1,3)` differs from the contracting mechanical word `(1,2,2)`
by a decrease and an increase. It is retained by the general law;
the denominator-one conclusions use `q=1` explicitly. Repeated
all-2 words show why primitivity cannot be omitted. General
four-mismatch words need not be close to a mechanical comparison,
and are not excluded here.

## History

- 2026-11-08: combined the existing repeated-factor separation
  with mechanical balance and signed edit loss; derived the
  contracting-background square-root distance and the uniform
  clean-run law. Closed all two-edit words by exact local checks,
  and the ten-edit class with the separately declared convergence input.
  Same-session audits do not upgrade the node to `reviewed`.
