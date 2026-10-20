# Preparatory upper attempt: matching two density estimates

**Status: candidate / none.** This is a bounded follow-up prepared during
P6-004 verification, separate from the completed two-level attempt in
[c2a_attempt.md](c2a_attempt.md). No new batch, accepted barrier, non-transfer
step, or Collatz proof is claimed. The exact checker and its receipt have
not been changed for this note.

The question is whether the fixed-target positive lower-density ingredient,
Tao's almost-bounded theorem, exact nonabsorbing-set invariance, and a
supplied finite absorption interval jointly give an upper estimate strong
enough to exclude a bad component. They give the density comparison below.
They do not currently give the strict comparison it would require.

## 1. Definitions and the two imported inputs

Use ordinary odd-only Syracuse S, absorbed at 1. All iteration counts below
are odd arrows; no finite or uniform bound on a hitting time is assumed.
For a positive odd integer n put

```
h(n) = min_{j>=0} S^j(n),
B = {odd n : S^j(n) != 1 for every j>=0},
P(a) = {odd n : S^j(n)=a for some j>=0},
O(X) = #{positive odd n<=X},
H_o(X) = sum_{positive odd n<=X} 1/n,
ell_X(A) = (sum_{n in A, n<=X} 1/n) / H_o(X).
```

The minimum exists by well ordering, even for an unbounded trajectory.
Define the upper logarithmic tail

```
tau(H) = limsup_{X->infinity} ell_X({n:h(n)>H}).      (1)
```

Tao's Theorem 1.6 gives, for every function f on the positive odds with
f(n) tending to infinity, relative logarithmic density one to h(n)<f(n).
The fixed-threshold tightness formulation is tau(H) tending to zero as
H tends to infinity. Theorem 1.3 and Remark 1.4 state the corresponding
all-integer formulation and explain the fixed-threshold distinction.
See the [corrected primary paper, v7](https://arxiv.org/html/1909.03562v7).

The second input remains the literature-qualified ingredient audited in
[terminal_audit.md](terminal_audit.md): for each fixed positive odd a with
3 not dividing a, there is a constant lambda_a>0 such that

```
liminf_{X->infinity} #P(a) intersect [1,X] / O(X)
    >= lambda_a.                                  (2)
```

The constant and threshold depend on a; no uniform positive lower bound
in a is supplied. This note does not re-prove that ingredient or upgrade
its independent formal-verification status.

## 2. The exact upper constraint that follows

Suppose a finite certificate establishes absorption of every positive odd
seed through V. Exact invariance gives B contained in {h>V}. Hence

```
limsup_X ell_X(B) <= tau(V).                       (3)
```

If a is a bad ternary-unit target, P(a) is contained in B. Lower natural
density implies at least the same lower logarithmic density, with the
relative-odd normalizations used here. Indeed partial summation gives

```
sum_{n in A, n<=X} 1/n = A(X)/X + integral_1^X A(t)/t^2 dt,
H_o(X) = (1/2) log X + O(1).
```

Applying A(t)>=(lambda_a-epsilon)O(t) at every sufficiently large t and
then letting epsilon decrease to zero proves the implication. Thus

```
0 < lambda_a
  <= liminf_X ell_X(B)
  <= limsup_X ell_X(B)
  <= tau(V).                                     (4)
```

This is a necessary quantitative comparison, not a contradiction.
The two positive numbers in (4) may be arbitrarily small.

There is also an exact finite-target approximation. For an integer H let

```
U_H = union_{odd a<=H, a in B} P(a).
```

Then U_H is contained in B, and

```
B \ U_H = B intersect {h>H},
limsup_X ell_X(B \ U_H) <= tau(H) -> 0.           (5)
```

Every bad trajectory which enters [1,H] hits a bad seed in that interval.
Conversely, a predecessor of a bad seed is bad. Formula (5) is the exact
place where invariance is useful. It does not decide which of the finitely
many seed basins in U_H are bad. At a supplied verified cutoff V, U_V is
empty, but H cannot then be sent to infinity without additional input.

For finitely many targets in distinct bad components, their predecessor
sets are disjoint. The same argument bounds the sum of their lower
constants by tau(V). A uniform positive lower constant would restrict
the number of such components; the current input provides no such
uniformity and the sum need not vanish.

## 3. A precise candidate, and why it is missing

If B is nonempty, let m=min B and a=S(m). Then a is a positive odd
ternary unit in B, a>=m, and all smaller seeds absorb. Applying (4) with
V=m-1 gives

```
lambda_{S(m)} <= tau(m-1).                        (6)
```

A concrete sufficient next target would be certified functions L and U
with the following all-cutoff meanings:

* L(a)>0 is a lower bound in (2), for every fixed eligible a.
* U(H) is an upper bound for the limsup in (1), for every fixed H.
* For every possible least bad seed m beyond the supplied finite base,
  `L(S(m)) > U(m-1)`.

The third line is the **matched density gap** candidate. It is unproved.
It is not obtained by substituting two asymptotic statements into one
another. Neither the audited lower construction nor Tao's tightness
assertion provides this comparison between their target-dependent
constants. No numerical constant comparison has been certified here.

In particular, choosing epsilon<lambda_a first supplies some threshold
C_epsilon with tau(C_epsilon)<=epsilon. It does not show that
C_epsilon<m, or that all seeds through C_epsilon are already absorbed.
This is the quantifier gap in the proposed combination. Choosing a
diverging f cannot keep f(n) below a fixed unknown minimum m indefinitely.

The candidate is recorded as a testable missing quantitative step, not as
an easier theorem or an accepted reformulation of convergence.

## 4. A countermodel to using only these aggregate inputs

The following elementary model isolates the scope of the gap. It is
**not** an affine Syracuse map. It does not model exact valuation
cylinders, ternary transfer laws, Tao's stronger first-passage mechanism,
or his finite-distribution mixing theorem. It models only:

1. a deterministic map on the positive odds with absorber 1;
2. full invariance of its actual nonabsorbing set;
3. any prescribed finite interval of verified absorption;
4. positive lower natural density of every fixed-target predecessor set;
5. the almost-bounded conclusion for every diverging f.

Fix an integer r>=2, as large as desired. On positive integer indices set

```
p_r(1)=1,  p_r(r)=r,
p_r(i)=floor(i/2) otherwise.
```

Transfer this map to the odd integers by

```
T_r(2i-1)=2 p_r(i)-1.
```

Every orbit reaches either 1 or m=2r-1, because the index decreases except
at those two fixed points. All odd seeds below m reach 1. The actual bad
set consists exactly of the binary descendants of index r, is fully
invariant, and contains the second fixed point m. Choosing m>V supplies
any prescribed finite verified interval without eliminating this set.

Every fixed target has a positive-density predecessor set. For target
index a, choose b=a unless a is a proper binary ancestor of r. In that
case choose the child b in {2a,2a+1} whose subtree does not contain r.
In either case every index in each interval

```
[b*2^k, (b+1)*2^k-1],  k>=0,
```

reaches a before encountering a changed arrow. The intervals are disjoint.
For every large index cutoff Y, the largest completed such interval has
length greater than (Y+1)/(2(b+1)). Thus the target's relative-odd lower
natural density is at least 1/(2(b+1))>0. This statement includes both
fixed points and every other target.

Nevertheless h_T(n)<=m for every n. For every diverging f, the inequality
h_T(n)<f(n) holds for all sufficiently large n, stronger than the
almost-bounded conclusion. The bad set still has positive logarithmic
density. Direct summation over its dyadic intervals gives

```
delta_log(B_T) = log(1+1/r)/log 2 > 0.
```

For 1<=H<m the model's tail tau_T(H) equals this positive number; for
H>=m the tail is zero. Thus the model also satisfies tightness and all
the comparisons (3)–(6). Its positive bad mass can be made arbitrarily
small by increasing r.

**Conclusion and scope:** there is no implication from just the five
listed aggregate/functional-graph properties to absorption. An argument
for ordinary Collatz must use additional affine or distributional
information, or establish a strict quantitative comparison absent from
these properties. This is preparatory evidence about a specified method;
it is not automatically a Phase 6 barrier award and does not rule out a
proof using the full Tao machinery or exact Syracuse arithmetic.

## 5. The d=5 and d=61 controls

These controls use S_d(n)=(3n+d)/2^v2(3n+d), absorbed **only at 1**.
For every fixed positive odd d and positive odd u,

```
S_d(d*u)=d*S_1(u),
S_d(d)=d.
```

Thus every odd multiple of d>1 is nonabsorbing and this sector has
relative-odd natural and logarithmic density 1/d. The identity holds at
every iterate; the sector never encounters the absorber 1.

On this same sector Tao's ordinary theorem imports an almost-bounded
statement exactly. Given any diverging f on the positive odds, put
g(u)=f(d*u)/d. Then g diverges and

```
min_{j>=0} S_d^j(d*u) = d*min_{j>=0} S_1^j(u).
```

The exceptions to this minimum being below f(d*u) have relative
logarithmic density zero **within the odd multiples of d**. The factor
1/d in each logarithmic weight cancels from that relative normalization.
There is no assertion here of a global almost-bounded theorem for all
seeds of S_d. This is an exact positive-density nonabsorbing sector on
which the asserted stopping conclusion already holds.

Likewise any ordinary fixed-target predecessor lower bound scales to
targets d*a within this sector, with the corresponding factor in its
absolute density. This observation is conditional only on the ordinary
lower bound being used; it needs no theorem about all other d-sectors.

The stored nonprincipal cycles add exact bounded-orbit controls:

| d | Minimum | Odd-arrow length | Total valuation |
|---|---:|---:|---:|
|5|19|3|5|
|61|235|41|66|

The first is 19 -> 31 -> 49 -> 19. All arrows of both stored cycles were
rechecked by integer arithmetic. A trajectory entering one of these
cycles has orbit minimum at most its cycle minimum, so a statement about
eventually beating every diverging threshold cannot distinguish it from
absorption. Neither cycle contains 1. The scaled-sector fixed points 5
and 61 give separate, simpler controls.

## 6. Verification and decision

Only bounded focused checks were made:

* Replayed the two specified stored cycles, including all exact valuations:
  3 and 41 odd arrows, respectively.
* Checked the scaling identity at u=1,3,5,17,27 for d=5 and61, and both
  fixed points.
* For the explicit model r=17, verified absorption through odd cutoff31
  and the fixed seed33. For target indices1,2,8,17,34, checked the two
  subtree interval boundaries at depths0,1,2,3. The all-index assertions
  follow from the written halving proof, not extrapolation of these tests.

No full gate, large orbit scan, modified receipt, frozen-source edit, or
claim of a new actual-B estimate was made. Outcome remains **none**.
The practical next obligation is an affine/arithmetic upper constraint
or a proved matched density gap. Merely combining the two qualitative
density statements does not supply it.
