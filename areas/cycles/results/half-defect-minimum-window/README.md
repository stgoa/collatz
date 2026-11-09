---
id: half-defect-minimum-window
kind: result
title: Half-defect minima obey a weighted short-window bound
status: written
claim: >
  Raw odd-only positive integer 3x+1 cycles. In the canonical half-defect
  word W=A B A[p] B[q], with nonempty positive words A,B, distinct
  p,q>=1 and half length N=len(A)+len(B), assume EXT-1. Every global
  minimum occurs in the common arc immediately after the larger
  increased half-defect: first A if p<q, second B[q] if p>q. Its
  zero-based input offset i satisfies i<173N/1000. More precisely, with
  M the minimum, ell=log2(M), K=317/200, D0=3024133/2000000 and
  B0=1024967/2000000, the ordinary common-block excesses before and
  after that input and in the other block satisfy
  D0*i+(K+2)e_other+(K+1)e_prefix+2(K+1)e_suffix+omega*min(p,q)
  <B0*N+(K+1)ell, where omega=1 for p<q and omega=K+1 for p>q.
  Suffix excess in B[q] is measured in ordinary B, with q kept
  separate. N is the half length, not the length of the common arc.
  Both parities and every minimizing location are covered. This is a
  necessary restriction, not an exclusion of all half-defect cycles.
authors:
  - Codex formal research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex residue research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex root research lane (GPT-6; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [half-defect-imbalance-growth]
assumes: [musson-collatz-gap-all]
certificates: [check_minimum_window.py]
evidence:
  - "check_minimum_window.json: exact coefficient identities, actual-addend prefix and suffix bounds, minimum offsets and shared cycle controls"
tags: [cycles, half-defects, minimum-bounds, valuation-excess, exact-certificates]
---

# Half-defect minima obey a weighted short-window bound

## Statement

Use the raw odd-only clock. For a nonempty positive valuation
word A, let A[p] increase only its last letter by p. Suppose a
positive odd integer `3x+1` cycle has word

```
W=A B A[p] B[q],       a=len(A)>=1, b=len(B)>=1,
N=a+b,                p,q>=1, p!=q.
```

The full odd period displayed by W is `2N`. This word has exactly
four mismatches with its half-period rotation. Conversely, the
cyclic normalization in
[half-defect imbalance growth](../half-defect-imbalance-growth/README.md)
puts any such four-mismatch word in this form, while retaining
both possible orders of the positive amplitudes p,q.

Assume [EXT-1](../../../../sources/musson-collatz-gap-all.md).
Write `M=min(state)` and `ell=log_2(M)`. The dependency proves
that every minimizing state is an input in first A if p<q,
and in second B[q] if p>q. It also excludes equal amplitudes.
For each minimum define the following data:

| Magnitude order | Actual copy containing the minimum | Ordinary block U | Other block V | omega |
|---|---|---|---|---|
| p<q | first A | A | B | 1 |
| p>q | second B[q] | B | A | K+1 |

Here `K=317/200`. The indicated copy begins immediately after
the letter carrying the larger increased half-defect. Let i be
the zero-based offset of the minimizing input within that copy,
so `0<=i<len(U)`. Split the ordinary word `U=C D` at that input:

```
len(C)=i,             len(D)=len(U)-i,
e_prefix=sum(C)-len(C),
e_suffix=sum(D)-len(D),
e_other=sum(V)-len(V),
s=min(p,q).
```

These are nonnegative integer excesses over the all-ones word.
For the second B[q] copy, they are calculated in ordinary B:
the extra terminal q is not included in `e_suffix`. It is retained
separately through the term `omega*s` below.

Set

```
D0=3024133/2000000,       B0=1024967/2000000.
```

Then every minimum satisfies the weighted inequality

```
D0*i+(K+2)e_other+(K+1)e_prefix+2(K+1)e_suffix+omega*s
   < B0*N+(K+1)ell.                                    (1)
```

Since the prefix C reaches a minimum from a state at least M,
(1) further implies

```
(3024033/1000000)*i+(K+2)e_other+2(K+1)e_suffix+omega*s
   < B0*N+(K+1)ell.                                    (2)
```

In particular,

```
i < (90212151/522149698)*N < 173N/1000.                  (3)
```

The denominator in (3) is the whole half length N, not the
length of U. Offset zero is allowed, and the argument applies
to every minimizing location without assuming uniqueness.
No restriction on the parity of p+q or an upper bound on either
amplitude is imposed.

The weaker consequence

```
sum(A)+sum(B)-N < 203N/1000                             (4)
```

is recorded for comparison. It is already recoverable from the
previous node's uneliminated minimum bounds and the full valuation
budget. The added information in (1) is the minimum's offset and
the extra weight on the suffix after it; (4) is not claimed as
an independent advance.

This node imports the existing finite-closure lemma under EXT-1.
It performs no new convergence or period-lower-bound computation.
The remaining half-defect candidates are not excluded.

## Proof

### 1. Retain the actual addend in the local estimates

First let the cycle have any actual positive odd addend d. Write

```
x --A--> z --B--> y --A[p]--> t --B[q]--> x,
P=3^a, R=3^b, Q=2^sum(A), S=2^sum(B),
rho=PR/(QS),          r0=y/x,
M=min(state),         gamma=(3+d/M)/2.
```

The exact boundary identities established in the dependency give

```
x<y,       H=(y-x)/Q positive odd,
J=(z-t)/S nonzero odd.                                 (5)
```

For general d, the p<q estimates below assume J<0 explicitly;
that sign is proved for d=1. When p>q, J>0 follows directly from
the positive first-intercept identity for every d. Thus put

```
r=t/z>1  if p<q and J<0,
r=z/t>1  if p>q.
```

All prefixes of a pair of copies whose last letters differ use
the same ordinary letters. Every actual arrow of valuation v
satisfies

```
next <= gamma*current/2^(v-1).                          (6)
```

We use this with the exact remaining suffix, including the
additional q in a B[q] suffix when present.

### 2. A minimum in first A when p<q

Suppose the minimum is at offset i in first A. Write `A=C D`,
`len(D)=c=a-i`, `u=sum(C)`, `v=sum(D)` and `s_B=sum(B)`.
Then `e_suffix=v-c`. The positive integer quotients in (5) give

```
y=x+QH>Q,             t=z+S(-J)>S.
```

Therefore `x>Q/r0` and `z>S/r`. The exact C prefix from x to M
and the D suffix from M to z, using (6), yield

```
M*r0 > 3^i*2^v,                                      (7A)
M*r*gamma^c > 2^(s_B+e_suffix).                       (7B)
```

For the first inequality, `M>=3^i*x/2^u` and `Q=2^(u+v)`.
For the second, `z<=gamma^c*M/2^e_suffix` while `z>S/r`.
The paired state at the minimum has the exact difference

```
state_(N+i)-M=3^i*2^v*H.                              (8)
```

Compared with the previous bounds `M>2^a/r0` and
`M>2^b/(r*gamma^a)`, the lower bounds in (7) retain the factors

```
(3/2)^i*2^e_suffix,
gamma^i*2^(e_other+e_suffix),
```

respectively. Both factors were previously replaced by one.

### 3. A minimum in second B[q] when p>q

Now split ordinary `B=C D` at the minimum, where `len(C)=i`,
`len(D)=c=b-i`, and again write `u=sum(C)`, `v=sum(D)`.
Here `t>S/r` because `z=t+SJ>S`. The unchanged C prefix gives

```
M*r > 3^i*2^v.                                       (9A)
```

The remaining actual suffix is D[q]. Its valuation excess is
`e_suffix+q`, so (6) gives

```
x<=gamma^c*M/2^(e_suffix+q).
```

Since `r0*x=y>Q`, this implies the second exact bound

```
M*r0*gamma^c > 2^(sum(A)+q+e_suffix).                 (9B)
```

The terminal q has not been absorbed into an ordinary-block
excess or discarded. No assumption that B[q] is a contracting
affine map is needed.

In either case, the ordinary prefix C ends at a minimum M
and starts at a state at least M. Its exact equation is

```
2^sum(C)*M=3^i*start+d*C_C.
```

For `i>0`, its intercept `C_C` is positive. Hence
`2^sum(C)>3^i` when i>0; for i=0 both powers are one.
Writing `alpha=log_2(3)`, we have

```
e_prefix >= (alpha-1)*i,                              (10)
```

strictly when i>0. The zero-offset equality is retained.

### 4. Specialize only the integer 3x+1 cycle

Return to d=1. The dependency supplies the correct minimum
location used in sections 2--3 and the local threshold `M>=2^17`.
The exact integer comparisons

```
3^10000>2^15849,       393217^200<2^3717
```

give

```
A0=15849/10000 < alpha,
kappa=log_2(3+1/M) < K=317/200.
```

Let `T=sum(A)+sum(B)` and `E=2T+p+q`, the full valuation total.
The full 2N-step product gives `E<2KN`. Put

```
Delta=|p-q|,          e=e_prefix+e_suffix+e_other,
c0=2K-A0-1=5851/10000,     e0=K-A0=1/10000.
```

The ordinary block ratio estimates in the dependency give

```
log_2(r0) < E-T-alpha*N < c0*N-e,
log_2(r0) < (p+q)/2+e0*N,
log_2(r)  < Delta/2+e0*N,
gamma < 2^(K-1).                                    (11)
```

For the first line, retain `T=N+e`. For the second, use
`E-T=(E+p+q)/2`. The bounds use the full valuation total E;
there is no substitution of a half-period power gap.

**The p<q order.** Let `e_A=e_prefix+e_suffix` and
`e_B=e_other`. Taking logs in (7), then applying (11), gives

```
ell > a+(A0-1)i+e_suffix+e_A+e_B-c0*N,
ell > N-K*a+(K-1)i+e_B+e_suffix-Delta/2-e0*N.
```

Multiply the first line by K and add the second, cancelling a.
With

```
cA=1-e0-K*c0=145033/2000000,
D0=K*A0-1=3024133/2000000,
```

we obtain

```
cA*N+D0*i+K*e_A+(K+1)(e_B+e_suffix)
   < (K+1)ell+Delta/2.                               (12A)
```

The full valuation budget also gives

```
Delta/2 < (K-1)N-e-p.
```

Substituting this in (12A), and expanding e_A, yields (1) with
`omega=1`, since `K-1-cA=B0`.

**The p>q order.** Here `e_A=e_other` and ordinary B has
excess `e_prefix+e_suffix`. Equations (9),(11) give

```
ell > b+(A0-1)i+e_suffix-Delta/2-e0*N,
ell > N-K*b+(K-1)i+e_A+e_suffix-Delta/2-e0*N.
```

The second line uses `q-(p+q)/2=-Delta/2`; this is the
point where the separately retained terminal q matters.
Multiplying the first line by K and adding the second gives

```
cD*N+D0*i+e_A+(K+1)e_suffix
   < (K+1)(ell+Delta/2),                             (12D)
cD=1-(K+1)e0=1999483/2000000.
```

Now `Delta/2<(K-1)N-e-q`. Since

```
(K^2-1)-cD = K-1-cA = B0=1024967/2000000,
```

(12D) becomes (1) with `omega=K+1`. This proves the same
weighted position/excess law in both chronological orders.

### 5. The short window and the inherited closure

Equation (10) and `alpha>A0` imply
`e_prefix>=(A0-1)i`, including offset zero. The combined
coefficient in (1) is exactly

```
D0+(K+1)(A0-1)=3024033/1000000=:I0.
```

This proves (2). The dependency's general finite-closure lemma
states that under EXT-1 a nontrivial positive odd integer cycle
with displayed length 2N cannot satisfy `N<259log_2(M)`.
Our word is nontrivial, so

```
ell<=N/259.                                         (13)
```

Dropping the nonnegative excess and amplitude terms in (2)
and using (13) gives

```
i < [(B0+(K+1)/259)/I0]*N
  = (90212151/522149698)*N.
```

The exact comparison to 173/1000 is certified by

```
(173/1000)*I0-B0-(K+1)/259
  =179620131/259000000000>0.
```

This proves (3). It uses the previously established closure
rather than a new local convergence computation.

### 6. Relation to the earlier excess bound

The previous uneliminated minimum bounds, together with the
full valuation budget and the retained `-e` in the first
r0 estimate of (11) when p<q, already imply

```
(K+1)e+omega*s < B0*N+(K+1)ell.                      (14)
```

For p<q, combine the old two case-A bounds to obtain
`cA*N+K*e<(K+1)ell+Delta/2`, then use
`Delta/2<(K-1)N-e-p`. For p>q, the old case-D consequence
is `cD*N<(K+1)(ell+Delta/2)`; use the same budget with q
instead of p. These are exactly (14) in the two orders.

The new inequality (1) retains, in addition to (14),

```
D0*i+e_other+(K+1)e_suffix.
```

The position and suffix terms are therefore the refinement.
For completeness, (13),(14) give

```
e < (270636453/1339030000)*N < 203N/1000,
```

where the last comparison has exact slack

```
(203/1000)(K+1)-B0-(K+1)/259
  =1186637/518000000>0.
```

This proves the subordinate consequence (4) and identifies
precisely what it inherits from the earlier raw bounds.

## Certificates

Run the standard-library certificate from the repository root:

```
python3 areas/cycles/results/half-defect-minimum-window/check_minimum_window.py
python3 -O areas/cycles/results/half-defect-minimum-window/check_minimum_window.py
```

The generated [receipt](check_minimum_window.json) records exact
rational identities for all coefficients, the two elimination
steps and the strict comparisons in (3),(4). Finite word controls
reconstruct actual positive `3x+d` cycles and check every arrow,
all minimizing inputs, the exact paired-prefix factors, the
ordinary suffix excesses and the extra q in B[q]. Both magnitude
orders and both parities are represented: the main grid contains
13394 unequal-amplitude actual cycles and 139634 arrows, with
2024 case-A and 11370 case-D minimum configurations, 530 interior
minima and 7138 opposite-parity examples. These are checks of the
formulas, not an absence search or an extrapolation over words.

The controls retain their actual addend d and use the rational
quantity `gamma=(3+d/M)/2` in (7),(9). The fixed q1 constants
are not imposed on controls with an insufficient normalized
minimum; the receipt explicitly records zero eligible controls
for that fixed-constant specialization. Its rational coefficient
identities are checked separately. The inherited EXT-1 finite
closure is a cited theorem; this certificate does not rerun or
replace its convergence proof.
The eleven shared actual `3x+5,7,13,61` cycle fixtures are also
replayed.

An actual-d control illustrates the distinction. For

```
A=(1,1), B=(2,1,1), p=3, q=1, d=499,
```

the complete cycle is

```
9925 -> 15137 -> 22955 -> 17341 -> 26261
 -> 39641 -> 59711 -> 11227 -> 8545 -> 13067 -> 9925.
```

Its minimum is at offset one in second B[q], whereas
`173N/1000=173*5/1000<1`. The raw bounds remain valid;
the claimed 3x+1 window is not applied to this d=499 cycle.
Its normalized minimum `8545/499` is below `2^17`.

The default command verifies the receipt; `--write-receipt`
regenerates it. The program is deterministic and keeps its
checks active under Python optimization.

## Remarks

The shorter window constrains the geometry after the larger
increased defect; it is not a claim that a minimum must occur
at that boundary. A large common valuation may still occur
inside the short prefix. The weighted law retains the costs
of that prefix, the suffix after the minimum and the other
common arc separately.

This is a written conditional refinement. Same-session audits
and exact finite formula controls do not make it independently
reviewed or formally verified. Novelty outside the repository
is undetermined. The remaining half-period problem stays open.

## History

- 2026-11-08: retained the exact minimizing offset and ordinary
  suffix excess in both surviving cases of the half-defect
  minimum-placement theorem. The two full-budget eliminations
  give the same weighted law and the common window
  `i<173N/1000`; the density-only consequence is credited to
  the earlier uneliminated bounds.
