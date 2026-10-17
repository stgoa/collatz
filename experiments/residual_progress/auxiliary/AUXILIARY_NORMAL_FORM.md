# A terminating auxiliary normalization, with its exact positive obstruction

Date: 2026-10-17. Status: written elementary proofs and finite checks.
This note constructs a universal **partial** normalization. It does not
construct complete annular certificates or prove Collatz. The height bound
below does not improve the repository's existing absorption cutoff `64N`.
Its additional features are a nonpositive current, a decreasing integer
potential, an order-independent residual, and an exact obstruction to
continuing with the same kind of local rewrites. No novelty is claimed.

All measures are finite integer signed measures on odd states greater than
1, with the repository's Syracuse map `S` and killed pushforward `P`.
The source `A_N` is the existing six-band annulus, with `8|N`, not an
inherited deeper packet family. Auxiliary intermediate vertices are actual
integer states; they need not be nonzero source atoms.

## 1. Short backward chains with a smaller endpoint

Use the following rules. A chain `q,r,y` means `S(q)=r`, `S(r)=y`;
a one-row chain means `S(q)=y`.

| y modulo 18 | q | Intermediate r | Exact forward valuations |
|---:|---:|---:|---|
|5 or 11|`(2y-1)/3`|none|1|
|13|`(8y-5)/9`|`(4y-1)/3`|1,2|
|17|`(4y-5)/9`|`(2y-1)/3`|1,1|

The congruences make every displayed state an odd integer. In the second
row `q=11 modulo 16` and `r=1 modulo 8`, so both valuations are exact. In
the third row `q=7 modulo 8` and `r=3 modulo 4`. The one-step predecessor
is `3 modulo 4`. In every row,

\[
3\le q<\frac89 y<y.
\]

For coefficient `c>0`, replace `c delta_y` by `c delta_q`. The associated
current is `-c delta_q` in the one-step case and
`-c delta_q-c delta_r` in the two-step case. In each case it is nonpositive
and its divergence is `c delta_y-c delta_q`. Intermediate source
coefficients are not spent; their divergence terms cancel exactly.

### Exhaustiveness at depth two

**Lemma.** An odd `y>1` has an odd ancestor `1<x<y` at Syracuse distance
one or two if and only if `y modulo 18` belongs to `{5,11,13,17}`.

**Proof.** The displayed rules prove sufficiency. Conversely, write a
two-step ancestry as `x -> r -> y`. Since `x<y`,
`r<=T(x)<(3y+1)/2`, where `T(x)=(3x+1)/2`. A last valuation at least3
would give `r>=(8y-1)/3>(3y+1)/2`, impossible for `y>=3`. The earlier
valuation also cannot be at least3: since `r>=(2y-1)/3`, it would give
`x>=(16y-11)/9>y`. A one-step smaller ancestor similarly has valuation
1 or2. Thus only the two valuations 1 and 2 need inspection.

If `3|y`, there is no incoming arrow. If `y=7 modulo 18`, its valuation-2
predecessor is divisible by 3 and exceeds `y`, so no second predecessor
exists on that branch. Valuation1 is not integral. If `y=1 modulo 18`,
its valuation-2 predecessor is `1 modulo 3`; the only compatible next
valuation from `{1,2}` is 2, giving `(16y-7)/9>y`. This leaves exactly
the four listed residue classes. \(\square\)

Consequently the terminal classes below describe precisely the obstruction
to **all** strictly height-decreasing predecessor substitutions of length
at most two, rather than an arbitrary subset of short rules.

## 2. Universal termination and a unique normal form

Let the active set be the four residue classes above, and write `f(y)=q`
for the selected rule. Whenever an active state has positive current
source coefficient `c`, make the replacement in Section 1 using that full
coefficient. The source coefficient at `y` becomes zero; the coefficient
at `f(y)` increases by `c`. Combine all coincident states exactly.

**Theorem.** Every sequence of such replacements terminates after finitely
many operations. The final residual `Z(mu)` and accumulated current `J(mu)`
are independent of the processing order. They obey

\[
\mu=(I-P)J(\mu)+Z(\mu),\qquad J(\mu)\le0,
\]

and every positive residual coefficient belongs to the classes

\[
x\equiv1,3,7,9,15\pmod{18}.
\]

**Termination.** The nonnegative integer

\[
\Phi(\mu)=\sum_x x\max(\mu(x),0)
\]

decreases by at least `c(y-f(y))>0` at each replacement. Any pre-existing
negative coefficient at `f(y)` only makes the decrease larger. Thus no
infinite sequence is possible. Each lineage contracts by a factor strictly
less than `8/9`; a lineage starting at height at most `M` has at most
`floor(log_(9/8)(M/3))` replacements. This is a bound for these particular
rewrites, not for the original Collatz orbit.

**Order independence.** All residual transport goes from a larger integer
to a smaller one and all arrivals are nonnegative. Let `F(x)` be the total
mass eventually sent from `x`. It is uniquely determined, in descending
order, by

\[
F(x)=
\begin{cases}
\max\bigl(\mu(x)+\sum_{f(y)=x}F(y),0\bigr),&x\text{ active},\\
0,&x\text{ inactive}.
\end{cases}
\]

The final coefficient is
`Z(mu)(x)=mu(x)+sum_(f(y)=x)F(y)-F(x)`. Every legal processing order has
exactly these total departures: at an active vertex a negative initial
coefficient first absorbs arrivals; all remaining positive mass departs.
The fixed chain for each departure also determines the same current rows.
The divergence identity follows by summing the finite local identities.
\(\square\)

The implementation processes vertices in descending order and visits each
odd residual vertex at most once. All residual states remain between 3 and
the initial maximum `M`, giving the explicit finite visit cap `(M-1)//2`.
Auxiliary current vertices can exceed the state being replaced; they are
not residual arrivals and do not invalidate the decreasing potential.

## 3. An exact replacement profile for the whole annulus

Apply the rule once to every originally positive active atom of `A_N`.
Let `B_N` be the resulting residual. Its base part is `A_N` with positive
coefficients in residues `{5,11,13,17}` deleted, retaining all negative
coefficients and the originally positive residues1 and 7. Add the following
nine profiles; all interval inequalities are strict.

| Interval for q | q residue | Modulus | Added coefficient |
|---|---:|---:|---:|
|`3N<q<6N`|3|12|1|
|`3N<q<6N`|7|12|1|
|`6N<q<12N`|7|12|2|
|`12N<q<24N`|7|12|3|
|`16N<q<32N`|11|16|1|
|`24N<q<48N`|7|12|1|
|`32N<q<64N`|11|16|2|
|`16N<q<32N`|7|8|1|
|`32N<q<64N`|7|8|2|

This is a complete description, including every remaining negative and
positive coefficient. The common residue modulus is 144 on the intervals
cut out by the listed boundaries and the six original band boundaries.
It follows directly by substituting each original positive residue and
its band into the affine predecessor formula. Since `8|N`, all boundaries
needed here are even integers; the odd residue conditions resolve each
strict endpoint without rounding ambiguity.

Write `A_N=(I-P)J_1+B_N`. Then `J_1<=0` and all its rows are below `96N`.
Every positive coefficient of `B_N` is below `64N`. Further normalization
only moves positive coefficients downward, so for `Z_N=Z(A_N)` and
`J_N=J(A_N)`:

\[
\operatorname{supp}Z_N^+\subset(1,64N),\qquad
\operatorname{supp}J_N\subset(1,96N),\qquad J_N\le0.
\]

The **whole** residual is still supported below `144N`, because the upper
negative annular sources are retained. Reducing the maximum positive
height is not a reduction of the entire source support. For all horizons,
the nonpositive current gives `H_L(A_N)<=H_L(Z_N)`. The unknown positive
residual remains in that inequality.

## 4. Exactly 21N/4 of unavoidable positive mass is already visible

Every multiple of 3 is inactive and has no incoming Syracuse arrow. The
original annulus vanishes there. Thus a positive arrival at such a vertex
cannot be canceled by later arrivals or moved by any predecessor rule.

The first pass creates the following mass at multiples of 3:

| Predecessor interval | Residue and modulus | Coefficient |
|---|---|---:|
|`(3N,6N)`|3 modulo 12|1|
|`(16N,32N)`|27 modulo 48|1|
|`(32N,64N)`|27 modulo 48|2|
|`(16N,32N)`|15 modulo 24|1|
|`(32N,64N)`|15 modulo 24|2|

The first line comes from original residue 5. The next two come from
residue 13 and the last two from residue 17. The residue 11 rule ends at
`7 modulo 12`, so contributes no multiple of 3 directly. Counts in this
table are additive, including any coincident arrivals.

For a strict interval define

\[
C_N(a,b;r,m)=
\left\lfloor\frac{bN-1-r}{m}\right\rfloor
-\left\lfloor\frac{aN-r}{m}\right\rfloor.
\]

The five counts in table order, with weights `(1,1,2,1,2)`, are:

| N | Five unweighted counts | Weighted sum |
|---:|---|---:|
|8|`2,2,6,6,10`|42|
|16|`4,6,10,10,22`|84|
|24|`6,8,16,16,32`|126|

These three boundary phases prove the formula for every multiple of 8.
Indeed under `N -> N+24`, the five counts increase exactly by
`(6,8,16,16,32)`, because every endpoint shift is a whole multiple of the
relevant modulus. Their weighted increase is 126, equal to `21*24/4`.
Consequently

\[
\boxed{\quad
\sum_{3\mid x} B_N(x)=\frac{21N}{4},\qquad
\sum_{3\mid x} Z_N(x)\ge\frac{21N}{4}.
\quad}
\]

All coefficients at multiples of 3 in either measure are nonnegative.
The normalization therefore cannot finish a certificate at any annular
cutoff. It necessarily leaves linear positive mass at an identified set
of actual integers.

### A necessary cost for the continuation, not the final summed current

Suppose a further current `L` satisfies
`Z_N=(I-P)L+W` with `W<=0`. At `3|x`, there is no incoming arrow, hence

\[
L(x)=Z_N(x)-W(x)\ge Z_N(x).
\]

Thus `||L^+||_1>=21N/4`: completion requires positive additional current.
This is **not** a lower bound on the positive cost of the final current
`J_N+L`. Since `A_N(x)=0` at multiples of 3, the normalization identity
gives `J_N(x)=-Z_N(x)`. The required positive continuation can cancel
these negative prefix rows. Confusing continuation cost with summed cost
would give an incorrect obstruction.

### Failure of a literal half-scale closure

For every `q=15 modulo 24` in `(32N,64N)`, the top source
`y=(9q+5)/4` is an actual positive annular atom with coefficient 2. Therefore
`Z_N(q)>=2`. Such a q exists for every `8|N`. Meanwhile every `Z_M` with
`M<=N/2` has no positive coefficient above `32N`. Hence an identity

`Z_N=sum_i c_i Z_(M_i)+W`, with all `c_i>=0`, `M_i<=N/2`, and `W<=0`,

is impossible. This rules out that literal residual recursion. It does not
rule out a recursion using additional signed currents, affine lifts,
different auxiliary families, or larger transport depths.

## 5. Why increasing the inverse depth is a new obligation

There is no fixed inverse depth guaranteeing a smaller ancestor for every
inactive positive state. More precisely, if `y>1` is odd and
`y=1 modulo 3^D`, then every positive odd ancestor reaching `y` in between
one and `D` steps exceeds `y`.

To prove this, take any valid inverse valuation word of length `d<=D`.
Its affine map has the form `h(z)=gamma*z-beta`, where
`gamma=2^A/3^d` and `beta>0`. Applying the same word to 1 gives an integer
at every intermediate stage: before each division by 3, the difference
between the two paths is divisible by the necessary remaining power of 3.
Starting at 1, each integral inverse step is positive and odd, so
`h(1)>=1`. Therefore `gamma=h(1)+beta>1` and

`h(y)=h(1)+gamma*(y-1)>y`.

This is a statement about strict ancestor descent, not about all possible
current cancellations. For any fixed D, actual annular positive residue 1
atoms of this form occur in the third or earlier positive bands at
sufficiently large cutoffs, including on each required dyadic ray.
Auxiliary composition may use growing depth, but its termination requires
a further argument beyond the normalization proved here.

## 6. Executable construction and verification

`check_auxiliary_normal_form.py` provides:

- `first_pass(measure)`: the full nonpositive current and exact first residual;
- `normalize(measure)`: the full nonpositive current, unique terminal residual,
  and finite processing statistics;
- `annular_first_profile(N, original)`: the independent nine-profile formula.

The checker compares direct normalization with first-pass-then-normalize,
including equality of the full current tables; verifies exact divergence,
the flow recurrence, residue support, all height bounds and all leaf counts;
and checks the exhaustive short-ancestor classification through 4097. It
uses explicit finite visit bounds, with no absorption search.

```sh
python3 experiments/residual_progress/auxiliary/check_auxiliary_normal_form.py
```

The adjacent receipt covers every multiple of 8 through 512, plus 768 and 6144.
Use `--write-receipt` only to intentionally refresh it. Selected results are:

| N | Initial positive mass | Terminal positive mass | Terminal mass at multiples of 3 |
|---:|---:|---:|---:|
|8|198|157|65|
|96|2376|1859|805|
|168|4158|3257|1398|
|384|9504|7453|3198|
|6144|152064|119310|51434|

These experiments validate the implementation. The universal claims rest
on the explicit chain, potential, flow, and floor-count arguments above.
The positive remainder and its required continuation are still open.
