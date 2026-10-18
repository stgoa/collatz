# Permanent limits of inverse-only descent, with forward escape

**Status: written structural proofs, two finite all-depth exclusion
certificates, and exact partial currents.** Collatz remains open. These
results distinguish a complete inverse obstruction from failure of a capped
search. No novelty, human review, or formal verification claim is made.

Use positive odd Syracuse `S`, absorbed at 1; the elementary canonical
minimum `nu`; and `T=nu S`, with `T nu=nu S`. A canonical state is fixed by
`nu`. The complete inverse branches below are those proved in
[R25](../bridge_normal_form/BRIDGE_NORMAL_FORM.md) and written in affine
form in [R41](../critical_inverse/CRITICAL_INVERSE.md). Currents use the
ordinary odd-only clock and killed atom `[1]=0`. A count of T steps is
explicitly called a **quotient** count.

## 1. A complete known history cannot be enlarged by inverse-only search

Let Q be any T-forward-closed set of canonical states, finite or infinite,
and let `E=nu^(-1)(Q)`. Semiconjugacy makes E S-forward-closed. If a
canonical target q is outside Q, then

```
T^d(p)=q, d>=0  => p not in Q;
S^d(x)=q, d>=0  => x not in E.                         (1)
```

This follows by forward closure, without any absorption assumption.
Consequently no number of inverse steps from an unknown target can reach
a fully forward-closed supplied history. A supplied complete history can
still be enlarged by **forward motion from the target** into that history.

In particular define, for canonical q>1,

```
Q_<q = union { T^j(p): p canonical, 1<=p<q, j>=0 }.
```

Then q has a strictly smaller canonical ancestor at some positive depth
if and only if `q in Q_<q`. This is an exact membership equivalence, not
an algorithm for computing an infinite union. Uniform inverse formulas
remain useful: they prove membership and give finite currents without
enumerating the whole union, and can support a decreasing induction.
The implication does not say that those formulas are redundant as proofs.

### A finite all-depth exclusion certificate

Suppose a finite exact T-edge table Q contains every canonical p<b,
is forward-closed, and excludes canonical b>1. Then **no** p<b canonical
has `T^d(p)=b`, for **any** d>=1. This is a finite invariant-set proof of
an unbounded-depth statement. It also excludes an ordinary odd p<b with
`S^d(p)=b`: its canonical origin is at most p and obeys the same quotient
relation. Absorption of Q is unnecessary for the exclusion theorem.

## 2. Two absorbed critical roots with no smaller ancestor at any depth

[anchor_certificates.json](anchor_certificates.json) stores complete edge
tables and all current rows. The table for each anchor is exactly Q_<b,
as verified by tracing every canonical origin below b inside the supplied
finite table. Both tables are absorbing; no unknown orbit is followed by
the default certificate verifier.

| canonical b | critical W5 input w=b/3 | states in Q_<b | maximum | supplied lower current | actual P(w) current |
|---|---:|---:|---:|---:|---:|
|39|13|43|1025|54 rows for U38|9 rows|
|135|45|68|1457|114 rows for U134|11 rows|

Both w are 5 modulo 8 and 3w is nonselected, so their critical image is
`rho(w)=3w=b`. The second input is also divisible by 3. Neither b is in
its complete smaller-origin closure. Thus both critical roots permanently
defeat strict smaller-origin inverse search, including every quotient ray.
They nevertheless have exact first entries into their smaller history:

```
39  -> 59  -> 89  -> 33,
135 -> 203 -> 305 -> 57.                               (2)
```

These are three T arrows. In each row the first three vertices are outside
Q_<b and the last is inside. Their T bridges are materialized as signed
ordinary currents. Combining each bridge with the supplied finite-core
absorption of its last vertex, and subtracting supplied absorption of w,
gives the stored exact P(w) current. This does not assume a missing pair.

## 3. There are infinitely many absorbed inverse-minimal canonical states

Call m inverse-minimal if no strictly smaller canonical origin reaches m
under T. Infinitely many such m are absorbed.

Indeed, R25's complete inverse ray of 1 contains

```
r_k=(16*64^k-7)/9, k>=0,       T(r_k)=1.               (3)
```

These are infinitely many distinct absorbed canonical states. For any
absorbed canonical q, let m(q) be the least canonical origin reaching q,
allowing depth zero. This minimum exists among positive integers. Any
smaller ancestor of m(q) would also reach q, so m(q) is inverse-minimal.
It is absorbed because it reaches q. If only finitely many such minima
existed, their finite absorbing forward orbits would contain every
absorbed canonical q, contradicting (3).

This is a general existence theorem. It does **not** assert infinitely
many inverse-minimal critical W5 roots, or give an enumeration of all
minima. Section 2 supplies two exact critical examples.

## 4. Lifting a permanent anchor to a complete depth-D obstruction

Let b>1 have a finite exclusion certificate as in Section 1. For every
D>=1 and every canonical q>b satisfying

```
q=b mod 3^D,                                           (4)
```

every canonical p with `T^d(p)=q`, `1<=d<=D`, satisfies **p>q**.
All inverse rays and all ray indices are included.

**Proof.** The complete inverse branches are `y -> alpha*y+beta` with
`alpha>0`, denominator 3, numerator of alpha a power of 2. A ray's
arbitrary index j>=0 replaces its base p by
`64^j*p+49*(64^j-1)/63`. For every branch

```
alpha-beta>=1, with strict inequality on every ray.    (5)
```

The only other branch is the point predecessor `(2y-1)/3`, present
exactly at y=2 modulo 3; it has equality in (5). These statements include
all j, as shown by R41's exact affine formula.

Shadow an arbitrary inverse word from q at b, denoting successive actual
and shadow states by p_i,c_i. The same branch is legal on both: before
step i<=D their difference is divisible by `3^(D-i+1)`. More explicitly,

```
p_i=lambda_i*(q-b)+c_i,   lambda_i=2^(A_i)/3^i.        (6)
```

All shadows are positive canonical ancestors of b, so c_i>=b by its
complete exclusion certificate. The initial b cannot be 2 modulo 3:
its point predecessor would be positive, canonical, and smaller than b.
Thus the first inverse step is a ray. Define

```
G_i=lambda_i-(c_i+1)/(b+1).
G_0=0,
G_i=alpha_i*G_(i-1)+(alpha_i-beta_i-1)/(b+1).          (7)
```

The first gap is strictly positive; subsequent gaps stay positive.
Hence `lambda_i>(c_i+1)/(b+1)>=1`, and (6) gives p_i>q. This proves the
claim for every word of every length at most D. Semiconjugacy also
excludes an ordinary odd origin p<=q reaching q in 1 through D ordinary
steps, since nu(p)<=p. No finite ray-index truncation enters the proof.

### Fixed ternary valuation on the nonselected critical-five domain

Apply the theorem to the two anchors using, for every integer t>=1,

```
q=b+256*3^D*t,    w=q/3.
b=39,  D>=2: v3(q)=1, w=13 mod256;
b=135, D>=4: v3(q)=3, w=45 mod128, v3(w)=2.           (8)
```

All q are canonical, all w are 5 modulo 8, and 3w is nonselected.
If `3 does not divide t`, the shadow precision `v3(q-b)=D` is exact.
Thus there are arbitrarily deep **complete** inverse obstructions even
at these fixed ternary valuations, including a fixed valuation on the
remaining multiples-of-three input domain. The family varies with D;
only the two anchors themselves have been proved permanently
inverse-minimal by these certificates.

## 5. The same lifted families escape forward in three quotient steps

The two complete binary cylinders in (8) have the following exact
forward reductions. Write q=3w. In both cases the first two ordinary
successors are canonical, and the third raw successor is

```
y=(27q+19)/16,   r=T^3(q)=nu(y).
w=13 mod256: r=(27q+3)/32;
w=45 mod128: r<=(27q+3)/64.                           (9)
```

For the first row y is selected with `v2(y+1)=2`, so
`nu(y)=(y-1)/2`. For the second row y=5 modulo 8, so its first inverse
F step is `(y-1)/4`, followed if necessary by more decreasing
normalization. The smallest q in the rows are 39 and 135, respectively.
Both therefore satisfy

```
r<q,     9r+5<8q.                                    (10)
```

For example the first rank inequality reduces to `13q>187`.
Let D_w be the sum of the three canonical quotient bridges, so
`div D_w=[q]-[r]`. If `N_w` bridges w to z=nu(w), then the R43 formal
absorption plans give

```
J_w=D_w-N_w+H_r-H_z,
div J_w=P(w)-sum_v (A_r(v)-A_z(v))P(v).               (11)
```

Every upper request has rank at most `(9r+5)/8<q`; lower requests also
have smaller rank since `z<=(w-1)/4`. This is a strict-rho **conditional**
plan. Only supplied missing pair currents may be substituted. Section 2
separately provides actual currents for w13 and w45 using finite input
history.

These forward cylinders are already contained in
[R48's complete a=3 classification](../nonselected_forward/NONSELECTED_FORWARD.md).
The run parameter there is `d=v2(9t-1)` for `q=8t-1`: it is 2 in the
first cylinder and 3 in the second. No independent coverage gain is
claimed here. Their role is sharper: the very same families have an
arbitrarily long complete inverse obstruction and a fixed three-step
forward reduction. For D>=3 there is no contradiction: the forward
arrows go **from q to r**, whereas the excluded paths would go from a
smaller origin **to q**.

## 6. Reproduction and limits

```
python3 experiments/residual_progress/inverse_scope/check_inverse_scope.py
```

The default check reads the two full stored certificates, verifies every
edge, smaller-origin inclusion, forward closure, exact lower current,
and exact pair current; it does not rediscover absorption. It also checks
bounded complete origin sets, affine-word samples including large ray
indices, the two complete binary formulas, and rejection of malformed
certificates. The written affine proof supplies the unbounded ray and
depth quantifiers; samples do not substitute for it.

`--write-receipt` refreshes the deterministic receipt. The explicit
`--rebuild-certificates` option rediscovers only anchors 39 and 135 with
at most 1000 quotient steps per origin and 1024-bit states; a cap is an
unresolved discovery, never an exclusion proof. The resulting full
tables are then verified independently of those caps.

No result here supplies every W5 pair, closes the annular residual, or
establishes universal termination. The structural conclusion is that a
complete constructor must allow forward motion or another operation
beyond strict smaller-origin inverse search alone.
