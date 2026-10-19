# V006 — Independent review of the digit-count quadratic mechanism

**Status: mathematical argument PASS, 2026-10-18.**
This review checks the exact theorem below from its supplied argument and
the subsequently saved [overlap note](overlap.md), Sections 1–5.
It is an independent agent review, not formal verification, human peer
review, or a novelty assessment. The result has a digit-count hypothesis
and does not complete the unrestricted active goal.

## 1. Reviewed statement

Let F:N_0->C be any finite-valued sequence which is not eventually
periodic. Define, for a,t>=0,

```
A_(a,t)(n)=F(t+s_2(3^a n)),       n>=0.
```

**Claim:** these whole sequences are pairwise distinct. Consequently,
for g(n)=F(s_2(n)), its joint binary/ternary section family satisfies

```
|J_g(D)| >= (D+1)(D+2)/2,       D>=0.
```

The proof below verifies all parameters, including a=0 and t=0.

## 2. Equality forces equal digit-count offsets

For any fixed positive odd m and every sufficiently large k,

```
m(2^k-1)=(m-1)2^k+(2^k-m),
s_2(2^k-m)=k-s_2(m-1),
s_2(m(2^k-1))=k.
```

Here take 2^k>m, so the two displayed blocks do not overlap. Thus equality
of A_(a,t) and A_(b,u), evaluated at n=2^k-1, gives
`F(t+k)=F(u+k)` for all sufficiently large k. If t differs from u,
this is eventual periodicity with positive period |t-u|. The hypothesis
therefore forces t=u.

## 3. The balanced repetend identity

Fix ell>=1 and let L=2*3^(ell-1). The standard order calculation gives

```
2^(L/2) = -1 (mod 3^ell).
```

Put m=L/2 and A=(2^m+1)/3^ell. Then A is a positive odd integer less
than 2^m, and

```
Q_L=(2^L-1)/3^ell=A(2^m-1)
   =(A-1)2^m+(2^m-A).
```

The complement identity gives `s_2(Q_L)=m=L/2`. If K is any positive
multiple of L, then

```
(2^K-1)/3^ell = Q_L*(1+2^L+...+2^(K-L)).
```

This consists of nonoverlapping copies of the length-L block Q_L,
including its leading zeroes. Hence its binary digit weight is K/2.
The integer is odd, so subtracting 1 reduces its weight by exactly 1:

```
s_2((2^K-1)/3^ell-1)=K/2-1.              (R1)
```

**Boundary caution:** `2^(K/2)=-1 mod 3^ell` does not hold for every
multiple K of L. The repeated-block argument above, rather than that
stronger assertion, justifies (R1) for arbitrary multiples.

## 4. Equality forces equal ternary exponents

After t=u has been proved, suppose b>a. Choose K to be a sufficiently
large positive multiple of `2*3^(b-1)` and put

```
c=(2^K-1)/3^b.
```

This is a positive integer. For k sufficiently large that
`2^k>3^b c`, both inputs below are positive and the block identity gives

```
s_2(3^v(2^k-c))
 = k+s_2(3^v-1)-s_2(3^v c-1),       v=a,b.
```

For v=b the last weight is K-1. For v=a, apply (R1) with ell=b-a;
the chosen K is a multiple of its fundamental length. Its last weight
is K/2-1. Therefore the resulting two argument shifts differ by

```
Delta = K/2+s_2(3^a-1)-s_2(3^b-1).
```

Only one K could make this zero. Choosing any sufficiently large
admissible K makes Delta positive. Equality of the two A sequences would
now imply equality of F at two fixed shifts of every sufficiently large
integer k, with positive difference Delta. That again makes F eventually
periodic, a contradiction. Thus a=b, proving pairwise distinctness.

## 5. Operator-depth accounting

Taking t binary digit-1 sections of g gives
`n -> F(t+s_2(n))`. Applying a ternary digit-0 sections then gives
A_(a,t). The total number of section operations is a+t. Therefore all
pairs a+t<=D are present by joint depth D, and the triangular count follows.
No finite-prefix equality or empirical count is used.

Now suppose a positive binary section of a Collatz invariant h at depth
K has this digit-count form. V004's positive-section formulas cost at most
one additional binary level per binary digit and four per ternary digit.
The states above therefore lie among binary sections of h by depth
`K+t+4a<=K+4D`. Consequently

```
kappa_h(K+4D) >= (D+1)(D+2)/2.
```

If F is eventually periodic instead, g is binary automatic: a finite
automaton can store the digit count exactly below its eventual threshold,
and thereafter store its residue modulo the eventual period. V005's
local automaticity lemma then forces h constant.

Thus a nonconstant invariant with such a section has the displayed
quadratic lower bound and meets the requested unbounded linear ratio.
An arbitrary section need not have the specified form. Establishing this
for the full class of invariants still requires another argument.

## 6. Saved source and the adjacent-11 control — PASS

The saved overlap note includes an arbitrary initial offset t_0. Replacing
F by its tail shift preserves non-eventual-periodicity, so all arguments
above cover that version. Its balanced-block proof uses the fundamental
length before repeating blocks; it avoids the half-period pitfall noted
in Section 3 of this review. The all-depth coefficient 1/32 follows by
taking D=floor((N-K)/4) in the triangular bound.

The added adjacent-11 control is also valid. Appending a suffix word for
r of exactly a bits gives

```
N_11(2^a n+r)=N_11(n)+N_11(r)+epsilon*(n mod2),
```

where epsilon is the suffix's most significant bit and N_11(r) counts
its internal adjacent pairs. Leading zeroes in that suffix create no
internal pair. Thus the displayed section formulas and `kappa_z(D)<=2D`
bound hold, including r=0 and the original state.

The two even test inputs in the note have the same digit count k, but
adjacent-pair counts k-1 and 0. Their comparison would force F constant
on a tail if any section depended only on digit count. The chosen
power-of-two indicator is not eventually constant. Appending m ones
gives the stated shifts of F, and testing at `n=2^k-1` proves their
whole-function distinctness from non-eventual-periodicity.

Finally, appending 101 and appending 1 create the same boundary pair and
no internal pair, proving the reduced return identity. The exact values
z(3)=1 and z(10)=0 verify failure of the full guarded map. This control
does not contradict the theorem; it shows why the digit-count extraction
hypothesis is substantive.
