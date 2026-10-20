# C013 — Polynomial cancellation with an arbitrary common background

**Status: written proof, with one explicitly imported logarithm estimate.**
The polynomial identities, Fourier estimate and resultant bounds below are
elementary. Effective denominator finiteness and the denominator-one
restriction use the explicit Matveev estimate already sourced in
[C011/EXCLUSION.md](../two-defect-rotation-exclusion/EXCLUSION.md). No novelty, human review or formal
verification is claimed. The clock is raw positive odd-only, without an
absorber. The results do not exclude every nontrivial integer cycle.

## 1. Objects and exact common-background elimination

Let U be a positive valuation word or the empty word, of length n>=0,
total A_U and intercept C_U. For the empty word set A_U=C_U=0.
Let a=(a_0,...,a_(r-1)) be a positive marker word of
length r>=2 and total T. Consider

```text
w=(U,a_0,U,a_1,...,U,a_(r-1)),
m=r(n+1),       A=r A_U+T,
u=2^A_U,        alpha=3^(n+1),        E=3 C_U+u.
```

No contraction or ordering hypothesis is imposed on U. Each block
`(U,a_j)` has the same affine numerator `alpha*x+E`, divided by
`u*2^a_j`. Set `P_j=sum_(i<j) a_i` and define monic integer polynomials

```text
P(X)=sum_(j=0)^(r-1) 2^P_j X^(r-1-j),
Q(X)=X^r-2^T.
```

Direct composition, at the displayed cut before the first U, gives

```text
S=u^(r-1) P(alpha/u),
C_w=E S,
D=2^T u^r-alpha^r=-u^r Q(alpha/u).                 (1)
```

Assume D>0. The normalized positive rational cycle has reduced
denominator `q=D/gcd(D,C_w)`. This formula remains valid for repeated
words; primitivity is not needed for the algebra below.

Let G be the monic polynomial gcd of P,Q over the rationals. By the
monic version of Gauss's lemma, G and both quotients have integer
coefficients. Write

```text
d=deg G,        e=r-d,
Pbar=P/G,       Qbar=Q/G,
G_h=u^d G(alpha/u),
Pbar_h=u^(e-1) Pbar(alpha/u),
Qbar_h=u^e Qbar(alpha/u).
```

All three homogeneous evaluations are integers, and

```text
D=-G_h Qbar_h,           C_w=E G_h Pbar_h,
gcd(D,C_w)=|G_h| gcd(Qbar_h,E Pbar_h),
q=|Qbar_h|/gcd(Qbar_h,E Pbar_h).                  (2)
```

Here and below gcd is positive and insensitive to signs. D>0 ensures
G_h and Qbar_h are nonzero. Equation (2) extracts the entire polynomial
common factor before any numerical gcd estimate.

### The remaining numerical cancellation

Let `R=Res(Pbar,Qbar)`. It is a nonzero integer because the quotients
are coprime over the rationals. Put `h=gcd(Qbar_h,Pbar_h)`. Then

```text
h divides R,
gcd(Qbar_h,E Pbar_h)=h gcd(Qbar_h/h,E),
q=|Qbar_h/h|/gcd(Qbar_h/h,E),
q >= |Qbar_h|/(E |R|).                           (3)
```

For the empty U, `u=E=1`, `alpha=3`, and these identities apply
directly to any positive marker word, including the actual fixtures.
The nonempty case is the substantive arbitrary-background setting.

To prove the first assertion, the integral resultant Bezout identity
expresses R as an integer polynomial combination of Pbar,Qbar.
Evaluate at alpha/u and clear sufficiently many powers of u. The
result is an integer combination of Pbar_h,Qbar_h equal to `R*u^N`.
Since Qbar_h divides D and D is coprime to 6, h is coprime to u;
therefore h divides R. In fact h divides the part of R coprime to 6.
For the second assertion divide Qbar_h and Pbar_h by h; the two
quotients are coprime. This retains the residual gcd with E instead
of silently declaring different cancellation mechanisms independent.

## 2. Residual degree is exactly Fourier support

Set `theta=2^(T/r)` and let zeta be a primitive r-th root of unity.
Define the positive periodic sequence

```text
x_j=2^P_j theta^(-j),       x_(j+r)=x_j.
```

The extension is consistent because `P_r=T`. At the distinct roots of Q,

```text
P(theta*zeta^k)
 =theta^(r-1)*zeta^(k(r-1))*sum_j x_j*zeta^(-kj).
```

Consequently

```text
e = number of nonzero Fourier coefficients of x.  (4)
```

This statement concerns the marker word alone; it requires neither
D>0 nor primitivity. Since x is positive, its zero-frequency
coefficient is nonzero. Thus e=1 exactly when x is constant, which by
`x_(j+1)/x_j=2^a_j/theta` is exactly when the marker word is constant.
Every nonconstant marker word has e>=2.

### All rotation distances, with no fixed defect-count restriction

Fix any marker shift k for which
`s=#{j:a_(j+k)!=a_j}>0`. Define the cyclic sequence

```text
y_j=x_(j+k+1)*x_j-x_(j+k)*x_(j+1)
   =theta^(-1)*x_j*x_(j+k)*(2^a_(j+k)-2^a_j).
```

Its ordinary support has exactly s elements. Write
`x_j=sum_(p in K) c_p zeta^(pj)`, with `|K|=e`. Terms with p=q
cancel in y. The combined contribution of an unordered distinct pair
p,q to frequency p+q has coefficient

```text
c_p c_q (zeta^p-zeta^q)(zeta^(pk)-zeta^(qk)).
```

Hence the Fourier support of y has size at most `binom(e,2)`.
Coincident pair sums or further zero coefficients only decrease it.

For completeness, if a nonzero cyclic function f has ordinary support
a and Fourier support b, Cauchy--Schwarz and Parseval give

```text
||fhat||_infinity <= sqrt(a) ||f||_2,
r ||f||_2^2 = ||fhat||_2^2 <= b ||fhat||_infinity^2.
```

Thus ab>=r. Applying this to y proves

```text
s binom(e,2) >= r.                               (5)
```

This is an elementary polynomial-complexity restriction for every
positive marker word and every rotation with nonzero mismatch count.
It is not the stronger unproved bound `s*e>=r`. Constant words and
rotations preserving the word have s=0 and are outside (5).

## 3. Uniform resultant and denominator estimates

All roots of Q have modulus theta. Under D>0, `alpha<theta*u`, so

```text
|G_h| <= (2 theta u)^d,
eta=1-alpha^r/(2^T u^r)=D/(2^T u^r)>0,
|Qbar_h| >= theta^e u^e eta/2^d.                 (6)
```

Distinct roots of Q have separation at least
`2 theta sin(pi/r)>=4 theta/r`. At any root beta of Qbar, each
summand in P(beta) has absolute value at most `2^(2T)`, and hence

```text
|P(beta)| <= r 2^(2T),
|G(beta)| >= (4 theta/r)^d,
|Pbar(beta)| <= r^(d+1) 2^(2T).
```

The last bound discards the beneficial divisor `(4 theta)^d`.
The monic product formula for the resultant therefore gives

```text
1 <= |R| <= r^[e(d+1)] 2^(2Te).                  (7)
```

This estimate is uniform over all positive marker words with the
specified r,T. It does not treat R as an absolute constant when the
marker pattern grows.

Positivity of every valuation in U gives

```text
C_U <= (u/2^n)(3^n-2^n),
E <= u(alpha/2^n-2) < u alpha/2^n.               (8)
```

For example, the intercept bound follows term by term from
`prefix_U(j)<=A_U-n+j`. Combining (3), (6), and (8) yields the strict
bound

```text
q > theta^e eta 2^n u^(e-1)/(2^d alpha |R|)
  > theta^(e-1) eta 2^n u^(e-2)/(2^d |R|).       (9)
```

For a nonconstant marker word e>=2, and `u>=2^n`, so in particular

```text
q > eta 2^[n(e-1)-d]/|R|,
log_2 q > log_2 eta+n(e-1)-d
          -e(d+1)log_2 r-2Te.                  (10)
```

This is a denominator estimate across the 3x+q family, rather than
just a polynomial-rank statement. The eta factor and the dependence
on marker totals remain explicit.

### Effective bounded-denominator finiteness

For fixed r,T and any fixed denominator ceiling Q_*, there are only
finitely many representations `(U,a)` as above with nonconstant a,
D>0 and `q<=Q_*`. The bound is effective, and the entire U is allowed
to vary.

Here is a proof with uniform constants. From (7), use

```text
R_0=r^(r^2) 2^(2Tr),      C_0=2^(3-r)/R_0.
```

Because theta>=2 and e>=2, equation (9) implies
`q>C_0*eta*2^n`. Let `A=r A_U+T`, `m=r(n+1)`.

* If A>=2m, then `eta>=1-(3/4)^m>=1/4`; thus
  `2^n<4 Q_*/C_0`, an effective bound on n.
* If A<2m, the explicit positive-rational Matveev estimate in
  [C011, equation (1)](../two-defect-rotation-exclusion/EXCLUSION.md) gives

  ```text
  log eta > -K(1+log(2m)),       K=600,000,000,
  q > C_0 exp[n log 2-K(1+log(2r(n+1)))].       (11)
  ```

  The exponent tends effectively to infinity. Its derivative is
  `log 2-K/(n+1)`, which is positive and bounded below by
  `(log 2)/2` once `n+1>=2K/log 2`. Thus (11) gives an effective
  bound on n at the fixed Q_*.

Once n is bounded, the branch A<2m bounds A_U directly. In the branch
A>=2m, the first line of (9), eta>=1/4, and e>=2 give

```text
u^(e-1) < 4 Q_* 2^d alpha |R|/(theta^e 2^n),
```

which bounds A_U. There are then finitely many positive U, and there
were already finitely many positive markers at fixed r,T. This proves
the assertion. No numerical cutoff is computed here.

Constant marker words are deliberately excluded: the full word is
then a repetition of one block, and its primitive denominator need
not grow with the repetition count. The theorem leaves finite q=1
exceptions and supplies no all-size exclusion for each marker word.

## 4. A uniform restriction on hypothetical integer cycles

Suppose the marker word is nonconstant, the represented rational cycle
has q=1, and its primitive cycle is nontrivial. Every odd state is at
least 3. The product of
the arrows gives `2^A=product(3+1/n_i)<4^m`, even when the displayed
word repeats the primitive cycle. Thus A<2m and (11)'s logarithm
estimate applies.

From (10), with `d=r-e`,

```text
n(e-1) < d+2Te+e(d+1)log_2 r
          +(K/log 2)(1+log(2m)).                (12)
```

Dividing by e-1 and using e>=2, d<=r-2 gives the simpler uniform
restriction

```text
n < r+4T+2(r-1)log_2 r
      +(K/log 2)(1+log(2m)).                    (13)
```

In particular, fix any marker-average bound H>=1. For representations
with `T<=Hr`, equation (13) implies

```text
r = Omega_H(sqrt(m/log m)).                     (14)
```

Indeed r<=m, `m=r(n+1)`, and every term in the right side of (13),
plus one, is at most `C_H r log m` for a fixed effective constant
C_H and m>=4. Thus `m<C_H r^2 log m`. The constant includes K;
no small useful numerical threshold is asserted.

**Here r counts copies of one identical shared background. It does
not count mismatches with a rotation.** A general sparse-rotation
word need not admit this representation, and even within this class
its mismatch count may be smaller than r. Equations (12)--(14) do
not establish the proposed unrestricted mismatch-growth milestone.
Their scope is an arbitrary marker pattern and arbitrary common U,
not a ladder of fixed three- or four-marker cases.

## 5. Two controls that prevent overinterpretation

### Primitive marker words can have polynomial common factors

Take

```text
a=(3,1,3,3,1,1),       r=6, T=12,
P=X^5+8X^4+16X^3+128X^2+1024X+2048
 =(X+4)^2(X^3+128),
Q=X^6-4096,           G=X+4,            e=5.
```

The marker word is primitive, yet G is nonconstant. Polynomial
cancellation therefore cannot be dismissed as merely a repetition
factor. This marker has a rotation by three with two mismatches;
its interleavings already belong to C011's two-defect class. It is
an algebra calibration, not a new cycle exclusion.

### Polynomial coprimality does not imply numerical coprimality

The existing actual d5 fixture with minimum 347 has valuation word

```text
(1,1,1,1,3,1,1,1,1,2,2,4,1,2,1,2,2),
m=17, A=27,
C=352383011, D=5077565, gcd(C,D)=1015513, q=5.
```

Its exact raw states are

```text
347,523,787,1183,1777,667,1003,1507,2263,
3397,2549,1913,359,541,407,613,461.
```

These data are retained in the fixture with minimum 347 in
[C005/mechanical_blocks_audit.json](../rotation-block-exclusion/mechanical_blocks_audit.json).
Apply the marker polynomial construction directly to this valuation
word. Since gcd(17,27)=1, `Q=X^17-2^27` is irreducible over the
rationals, so G=1 and e=17. Nevertheless evaluation at X=3 has the
large numerical gcd displayed above.

The needed irreducibility fact has a short proof: if a monic integer
factor of `X^m-2^A` has degree b, its nonzero constant term has absolute
value `2^(Ab/m)`, because all roots have that modulus. Integrality
forces `Ab/m` to be an integer. When gcd(A,m)=1 this forces m to
divide b. Gauss's lemma then rules out any proper rational factor.

Thus maximal residual degree can coexist with substantial numerical
cancellation. The resultant and E factors in (3) and (9) remain
necessary. This control does not refute the proposed arbitrary-s
denominator bound. Actual cycles at d5, d7 and d13 retain their true
reduced denominators throughout; no scaling to additive 1 is treated
as an integer q=1 cycle.

## 6. Candidate ledger and remaining obligation

1. **Objects:** a positive arbitrary background U, any nonconstant
   positive marker word a, the exact polynomials P,Q and their monic
   gcd, and the full rational-cycle denominator.
2. **Structural gain:** exact removal of systematic polynomial
   cancellation; residual degree equals Fourier support and obeys
   (5); equations (9)--(14) give quantitative denominator restrictions
   uniform in U and marker order.
3. **Translated unresolved gap:** arbitrary sparse-rotation cuts do
   not necessarily share one identical U. Numerical cancellation is
   not controlled by residual degree alone. Growing marker totals
   are charged explicitly, rather than discarded.
4. **Worked examples:** the primitive six-marker polynomial factor
   and the actual q5 period-17 numerical-cancellation control above.
5. **Known-cycle controls:** retain actual q5/7/13 cycles and repeated
   `(2)`. A constant marker is excluded from the finiteness assertion;
   the q1 argument requires both nonconstant markers and a nontrivial
   primitive cycle.
6. **Cheapest meaningful next test:** audit (5) on actual words and
   nontrivial polynomial-gcd controls; test (1)--(3) with several
   arbitrary positive U, including expanding U. The batch checker
   supplies finite evidence separately from these written proofs.
7. **Intermediate milestone:** transfer the exact factor extraction
   and quantitative estimate to distinct but compatible shared arcs,
   with a bound on all retained resultant/height terms. The present
   theorem supplies a common-background case, not that transfer.

The comparison with published cycle work is limited: these are
structural denominator restrictions and effective bounded-denominator
finiteness in a specified class. They do not improve a universal
numerical cycle record or provide a new unrestricted exclusion.
Relative to this repository, C011 gives an all-size two-defect
exclusion; C012 retains general coupled sums. The present theorem
allows every number and pattern of markers with an arbitrary repeated
background, but leaves finite exceptions and does not subsume all
arbitrary sparse rotations. No novelty claim is made against published
cycle literature.
