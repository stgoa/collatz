---
id: high-order-four-mismatch-exclusion
kind: result
title: Four-mismatch rotations have order at most eighteen
status: written
claim: >
  Raw odd-only 3x+1 clock. Let a nontrivial primitive positive integer
  cycle have m odd states and valuation word w. If w differs from its
  shift by H at exactly four positions and M=m/gcd(H,m)>18, then
  EXT-1 forces m<2^26. With the separately declared Barina convergence
  input, no such rotation exists at any length. Consequently every
  four-mismatch rotation in a hypothetical nontrivial primitive cycle
  has order 2<=M<=18 under these inputs; in particular no coprime shift
  has four mismatches. There is no restriction on label counts,
  multiplicities, arc placements, or the gcd of H and m. Orders 2
  through 18, larger mismatch counts, and divergent orbits are not
  settled by this result.
authors:
  - Codex root research lane (GPT-6; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [free-four-cut-eighteen-rotation-obstruction, paired-state-run-law, cycle-length-lower-bound-from-convergents]
assumes: [musson-collatz-gap-all, barina-2025-convergence-2-71]
certificates: [check_high_order.py]
evidence:
  - "check_high_order.json: exact state-index ramp, refined-run witnesses, actual addend-aware controls, local descent and dyadic cutoff"
tags: [cycles, four-mismatch, multirotation, bounded-order, effective-exclusion]
---

# Four-mismatch rotations have order at most eighteen

## Statement

Let `n_i`, with indices modulo `m`, be the distinct positive odd states
of a nontrivial primitive cycle of the raw odd-only `3x+1` map. Write

```
2^w_i n_(i+1)=3n_i+1,       w_i>=1,
s(H)=#{i modulo m: w_i!=w_(i+H)},
M=m/gcd(H,m).
```

Suppose `s(H)=4` and `M>18`. Under
[EXT-1](../../../../sources/musson-collatz-gap-all.md),

```
m<2^26=67108864.                                      (1)
```

With the additional declared
[Barina convergence input](../../../../sources/barina-2025-convergence-2-71.md),
the [replayed full odd-period bound](../cycle-length-lower-bound-from-convergents/README.md)
is `m>=72057431991`, contradicting (1). Thus under both inputs every
four-mismatch rotation has order between 2 and 18. In particular a
coprime shift, whose order is `m`, cannot have four mismatches.

There is no assumption on the number, size, multiplicity or arrangement
of letters, and no assumption that `H` is coprime to `m`.
Primitivity concerns the actual cycle: every nonidentity shift then
pairs distinct states. The conclusion does not exclude all cycles.

## Proof

### 1. A height envelope in the actual state clock

Replace `H` by its least positive representative or by `m-H`, as
needed, so `0<H<m/2`. Mismatch count and order are unchanged; equality
with `m/2` is impossible when `M>18`. Put `h=H/m` and rotate the
cycle so that `n_0=L=min_i n_i`. Define

```
alpha=log_2(3),       ell=log_2(L),       Y=log_2(L+1),
E=sum_i w_i,         delta=E-m*alpha>0.
```

The product of all step equations gives

```
delta=sum_i log_2(1+1/(3n_i)).                         (2)
```

For the state at index `i`, `0<=i<m`, the prefix equations imply

```
log_2(n_i)
 =ell+i*alpha-sum_(k<i) w_k
       +sum_(k<i) log_2(1+1/(3n_k))
 <=ell+(alpha-1)*i+delta.                             (3)
```

Define `f(0)=1` and `f(x)=x` for `0<x<1`, reducing arguments modulo
one. Equation (3) gives the uniform, deliberately relaxed envelope

```
log_2(n_i)<=ell+(alpha-1)*m*f(i/m)+delta.              (4)
```

The coordinate is the actual state index `i/m`. At zero, the value
`f(0)=1` only enlarges the upper bound on the minimum state. No
assumption about a unique large letter or a single actual height
drop is needed.

### 2. Every refined gap supplies an integer-pair witness

Let the four base cuts be

```
C={i/m: w_i!=w_(i+H)},
C_j=union(C-r*h: 0<=r<j),       1<=j<=18,              (5)
```

with points reduced modulo one and coincident cuts removed.
Telescoping the `j` comparisons shows

```
{i/m: w_i!=w_(i+jH)} is a subset of C_j.              (6)
```

Indeed, if all comparisons between `w_(i+rH)` and
`w_(i+(r+1)H)` agree, their first and last entries agree.
The sets in (5) may include artificial cuts, where the
`jH` comparison agrees. They still subdivide into valid agreement
intervals.

Take any positive circular gap `G` between consecutive distinct
cuts of `C_j`, ending at `e=b/m`. If the preceding cut is `a/m`,
the arrows starting just after `a` and ending just before `b`
agree under the shift `jH`. Their number is exactly

```
r=m*G-1>=0.                                          (7)
```

All tested shifts are nonidentity, since `1<=j<=18<M`. The paired
states are distinct by primitivity. Let their initial signed
difference be `d_start`, and let `F` be the sum of the common
valuations on these `r` arrows. The
[paired-state run law](../paired-state-run-law.md) gives

```
2^F*d_end=3^r*d_start.
```

Both states at either end are odd. Coprimality of `2^F` and `3^r`
then gives, for a nonzero integer `t`,

```
d_start=2^(F+1)*t,       d_end=2*3^r*t.
```

This remains valid when `r=0`. Positivity of both endpoint states
implies

```
max(n_b,n_(b+jH))>abs(d_end)>=2*3^(m*G-1).            (8)
```

Thus every raw refined gap in (5), including those adjacent to
artificial or coincident cuts, has an endpoint witness. Its endpoint
need not be an actual mismatch.

### 3. Transfer to the eighteen-rotation obstruction

Take logarithms in (8) and bound both endpoint states by (4):

```
1+(m*G-1)*alpha
 <ell+(alpha-1)*m*max(f(e),f(e+j*h))+delta.
```

Consequently

```
G<((alpha-1)/alpha)*max(f(e),f(e+j*h))
       +(ell+delta+alpha-1)/(alpha*m).                (9)
```

The exact comparisons `3^2>2^3` and `3^5<2^8` give
`3/2<alpha<8/5`, hence `(alpha-1)/alpha<3/8`.
Enlarge the positive error to

```
epsilon=(ell+delta+alpha)/(alpha*m).                  (10)
```

Equations (9)--(10) imply all eighteen gap inequalities with
coefficient `3/8` in the
[free four-cut obstruction](../free-four-cut-eighteen-rotation-obstruction/README.md).
Its order hypothesis holds because the reduced denominator of
`h=H/m` is `M>18`. It therefore forces

```
epsilon>=1/10000.                                    (11)
```

The geometric result includes all wraps and collisions at fixed
`h`; no generic-position hypothesis is imposed on the cycle.

### 4. The error is too small once m reaches 2^26

The local certificate checks that every odd seed `3<=s<2^17`
descends below itself. A nontrivial cycle cannot have such a
minimum, nor can it contain 1. Therefore `L>=2^17`.
Using (2), `ln(1+x)<x` and `ln(3)>1`,

```
delta/(alpha*m)
 =sum_i ln(1+1/(3n_i))/(m*ln(3))
 <1/(3L*ln(3))<1/393216.                             (12)
```

For example, `ln(3)>1` follows from `exp(1)<3`: in the exponential
series, `k!>=2^(k-1)` for `k>=2`, strictly for `k>=3`, bounds
the tail strictly below 1.

Set `eta=1-3^m/2^E`. The product identity also yields

```
eta=1-product_i(1-1/(3n_i+1))
   <=sum_i 1/(3n_i+1)<m/(3L).
```

EXT-1 is `eta>=2^-172*m^-341`. Thus

```
ell<172+342log_2(m),       Y<173+342log_2(m).           (13)
```

The latter bound uses `L+1<2L`. Since `alpha>3/2`, `alpha<2`
and `ell<Y`, (10), (12) and (13) imply

```
epsilon<(2/(3m))*(Y+2)+1/393216
       <(2/(3m))*(175+342log_2(m))+1/393216.          (14)
```

If `2^d<=m<2^(d+1)`, the right side of (14) is less than

```
A_d=2*(175+342(d+1))/(3*2^d)+1/393216.
```

These bounds decrease with `d>=0`: writing the numerator's
linear factor as `N_d=517+342d`,
`2N_d-N_(d+1)=175+342d>0`. At `d=26`, exact arithmetic gives

```
A_26=9665/100663296,
1/10000-A_26=250831/62914560000>0.                    (15)
```

Thus `m>=2^26` contradicts (11), proving (1) with EXT-1 alone.
Only now invoke the separately declared period lower bound
`72057431991>2^26` to exclude this class at every length.

## Certificates

Run from the repository root with Python 3.10 or later:

```
python3 areas/cycles/results/high-order-four-mismatch-exclusion/check_high_order.py
python3 -O areas/cycles/results/high-order-four-mismatch-exclusion/check_high_order.py
```

The deterministic standard-library certificate checks the finite
constants, all 65535 local descent seeds, and the transfer identities
on 486 actual primitive `3x+q` cycles of rotation orders 19, 23 and
29, with shift gcds 1, 2 and 3. These controls exercise 23004 arrows
and 144990 refined agreement runs, including 29700 artificial cuts
and 187434 coincidences in the raw cut lists. The checker tests the
state-index ramp by an exact inequality between integer powers,
the telescoping mismatch inclusion, every agreement arrow, the
odd-pair lattice, and the endpoint witness (8). It also checks all
eleven shared `3x+5,7,13,61` fixtures, covering 106 arrows.

Every control retains its actual addend `q`. The run-difference
identity cancels a common addend, and (3) holds with
`delta=sum log_2(1+q/(3n_i))`; the small drift (12) is specific to
`q=1`. The controls are not normalized into nonexistent integer
`3x+1` cycles. An order-18 four-mismatch control explicitly checks
that the eighteenth shift is the identity and has zero paired
difference, demonstrating why the order gate cannot be omitted.

The default command verifies the generated
[`check_high_order.json`](check_high_order.json); `--write-receipt`
regenerates it. The universal geometric step is the separate exact
certificate in its declared dependency. The unbounded transfer is
the proof above, not an inference from the finite control family.

## Remarks

This changes the general four-mismatch target from arbitrary
rotation order to the finite list `2,...,18`, while the number of
tracks, block lengths and letters can remain unbounded. All
coprime four-mismatch cases are covered simultaneously. The
earlier label-specific results retain their original, sometimes
weaker-input, claims.

For the remaining small orders, sufficiently large multiples of
the shift are the identity. Equation (8) then fails because the
paired difference is zero. Further progress needs information
beyond blindly extending this list of distinct rotations; the
half-period and third-period arithmetic nodes address parts of
that remaining problem.

This is a written, conditional result, not a Lean formalization.
Audits within this authoring session do not confer independent
review status. Novelty outside the repository is undetermined.
The full four-mismatch question and the Collatz conjecture remain
open.

## History

- 2026-11-08: transferred the exact eighteen-rotation free-cut
  obstruction to arbitrary primitive cycle words using the actual
  state clock, all refined agreement intervals and an explicit
  drift budget. Derived the EXT-1 cutoff and the conditional
  reduction to rotation orders at most eighteen.
