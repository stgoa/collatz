# V008 — Independent audit of the two-exit control and first shell

**Result: PASS for both written arguments at their stated scopes.**
Reviewed the actual sources [two_exit.md](two_exit.md) and
[ROOT_REVIEW.md](ROOT_REVIEW.md). This is an independent mathematical
source audit, not formal verification, human review, or a novelty claim.
The active unbounded-linear-ratio theorem remains open.

## 1. Exact two-exit construction

For irrational 0<alpha<1, the strict interval definition gives p(0)=1
and p(1)=0 exactly. The floor identities yield both E-children of s
equal to u and all three T-children equal to v. The displayed evaluations
at n=2 and n=3 distinguish s,u,v as entire sequences. Thus U={s} has
exactly two exits. The evaluations at n=1 separately distinguish p from
all three, so the boundary basis vector e_p is legitimate.

These are actual sequences, and therefore satisfy all six radix
identities and the leading-zero output conditions at every descendant.
The destination-valued boundary equation is coefficient-exact: residues
0,...,5 have one mixed-digit representation in each ordering. The
calculation does not merge distinct exit states or suppress multiplicity.
The example's identity (6) correctly couples B_u to A_v; it supplies
no corresponding identification of E_i(u) with T_j(v).

## 2. Density and automaticity obstruction

For every integer m>=1,r>=0 and t in {0,...,5}, the decomposition

```
s(m(6l+t)+r) = p(ml+floor((mt+r)/6))
```

is exact. The rotation increment m*alpha is irrational. The geometric-sum
argument for every nonzero Fourier mode, followed by interval
approximation, gives natural frequency alpha on each of the six
subsequences. Their equal asymptotic weights give the same frequency
for the entire affine section. No endpoint convention or finite
exception changes that calculation.

The finite-kernel frequency argument is sound. Its rational stochastic
matrix P counts all padded digit words uniformly, so (P^j w)_f is
exactly the average on [0,k^j). Bounded powers exclude nontrivial Jordan
blocks at unit-modulus eigenvalues. Cesaro averaging projects onto
ker(I-P) along im(I-P), killing every other generalized eigenspace.
These two complementary spaces have rational bases, so the projection
has rational entries. If the original state's natural frequency exists,
its Cesaro-averaged coordinate must equal that frequency and is rational.
Frequencies of other states are not assumed to exist.

It follows that every affine section in the example has infinite binary
kernel and infinite ternary kernel. This proves the claimed hypothesis
(I) throughout the reachable graph, rather than only at the root.

## 3. Named guard failure and whole-section growth

The full Collatz root relation b(4n+2)=b(n) fails for b=s at n=1:
s(6)=p(1)=0 while s(1)=p(0)=1. The construction is therefore no
counterexample to an assertion requiring all three scalar identities.

The quadratic lower bound is also exact. For positive integers m<M,

```
alpha/M < x < min(1/M,alpha/m)
```

is a nonempty interval. On it both mx and Mx are below 1, while
mx<alpha<Mx. Density of {n*alpha} supplies an integer witness separating
p(mn) from p(Mn). Thus every distinct multiplier in
2^(a-1)3^(b-1), a,b>=1, gives a different entire zero-offset section
of s. Counting a+b<=D gives D(D-1)/2 distinct states for D>=2.
The argument counts entire functions, not finite prefixes.

**Scope:** the example refutes exclusion of one finite two-exit interior
under the generic radix-plus-(I) hypotheses. It neither has linear
joint growth nor establishes repeated bounded layers.

## 4. First-shell theorem

The six transitions R0–R5 in ROOT_REVIEW.md use the correct composition
order. The setup p=E1b=T2b, q=E0u=T0b, t=T1b, E1u=b is valid for
u=E0b. If p,q lie in {b,u}, binary closure is immediate. Otherwise
the five ordered pairs (v,b),(v,u),(v,v),(b,v),(u,v) are exhaustive.

Independently checked each case and all seven surviving rows. In the
p=q=v case, R1 at u gives E0A=v, while R0 at u gives E0t=E0A.
Thus t=b would force u=v and is correctly excluded. The reported draft
correction is mathematically necessary. In the p=b,q=v,t=u case, the
additional R1 swap at v indeed forces A=v. In both rows with a fourth
state w, w=E0v and both binary children of w are explicitly accounted
for. No unresolved child is hidden in the finite closure.

Finally the scalar relations at zero give b(0)=b(1)=b(2). Hence every
first-shell state has the same output at zero, and any added w=E0v
has that output too. Binary reading stays inside the exhibited finite
closed family and proves b(n)=b(0) for every n>=0. This finish works
for an arbitrary output set; it requires neither Cobham nor a separate
finite-valued hypothesis.

**Scope:** |J_1(b)|<=3 forces constancy under all three full root
identities. Equivalently a nonconstant invariant has |J_1(b)|>=4.
This is a first-shell result, not an arbitrary-depth two-exit exclusion
or an asymptotic rate improvement. The actual two-exit example has
three first-shell states and fails the required root relation, so the
two results are consistent.

## 5. Verification boundary

No discrepancy remains in the reviewed versions. No computational
frequency estimate, finite-prefix equality test, historical code change,
or full Phase 6 rerun was needed. The generalized-map controls fail the
stated d=1 hypotheses or finite-kernel infinitude condition and are not
improperly excluded. Correctness of these written arguments does not
settle the full quantitative goal or Collatz convergence.
