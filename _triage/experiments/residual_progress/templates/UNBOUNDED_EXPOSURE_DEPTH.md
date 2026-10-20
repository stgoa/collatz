# Actual annular current certificates require unbounded exposure depth

Date: 2026-10-17. Status: written elementary proof with exact finite checks
and independent model-assisted audits. Not human peer-reviewed or formally
verified. No Collatz proof, counterexample, or novelty claim is supplied.

This theorem concerns the **whole actual annulus**, including every source
atom and every incoming historical connection. It strengthens the earlier
finite depth-32 example and its infinite fixed-depth lift. The source
family is the repository's revised six-band annulus `A_N`, `8|N`, with
`Q=9N/4` and support in `Q<x<64Q=144N`.

For `D>=1`, let `G_D(N)` include the first `D` odd-only Syracuse arrows
from every nonzero source of `A_N`, with absorption at 1. A component's
signed source mass must be nonpositive for a current supported on this
graph to have an everywhere nonpositive residual, unless that component
contains 1.

## 1. The theorem and all quantifiers

Fix an arbitrary integer `D>=1`. Let `X` be any positive integer satisfying

\[
2^{\max(D+4,10)}\mid X,\qquad X\equiv1\pmod{3^{D+2}},
\]

and put `N=3X/128`. Then `N` is an integer divisible by 8. Define

\[
y_k=\frac{3^kX}{2^k}-1,\qquad 1\le k\le D+3.
\]

**Theorem.** The entire component of the top source `y_3=144N-1` in
`G_D(N)` is precisely

\[
y_1\longrightarrow y_2\longrightarrow\cdots\longrightarrow y_{D+3}.
\]

Its only annular source atoms are

\[
(y_1,-2)=(64N-1,-2),\quad
(y_2,2)=(96N-1,2),\quad
(y_3,2)=(144N-1,2).
\]

Its signed mass is therefore **2**, and it does not contain 1. No finite
current supported on the whole graph `G_D(N)` can represent `A_N` with a
nonpositive residual.

These cutoffs exist on a required dyadic ray. For every `D>=1` and `t>=1`,
set

\[
e_D=2\cdot3^{D+1},\qquad
X=2^{e_Dt},\qquad
\boxed{\ N=12\cdot2^{e_Dt-9}.\ }
\]

The elementary congruence `2^(2*3^(D+1))=1 modulo 3^(D+2)` follows by
repeatedly cubing `4=1 modulo 3`. Also `e_Dt>=max(D+4,10)` and the ray
exponent `e_Dt-9>=3`. Thus for **every fixed exposure depth D**, infinitely
many cutoffs on the required ray with mantissa 12 fail at that depth.

Equivalently, every one of these examples lies on the single base-64
ladder starting at 96:

\[
N=96\cdot64^{3^Dt-2}.
\]

If `d_*(N)` is the least exposure depth that supports a one-sided current,
with infinity allowed, this gives the explicit lower bound

\[
d_*(96\cdot64^k)\ge v_3(k+2)+1,\qquad k\ge0.
\]

For `v_3(k+2)>=1`, use `D=v_3(k+2)` in the theorem. For valuation zero,
the bound follows because the depth-zero graph has positive source atoms
and no arrows.

### Consequence for finite template catalogues

A finite catalogue of common-tail current trees whose sources are packed
from actual annular coefficients has a finite maximal source-to-anchor
depth `D`. Every arrow of every such copy lies in `G_D(N)`, after pruning
branches with no source. The theorem therefore rules out any such
catalogue completing every actual annulus, even allowing arbitrary signed
current coefficients, fractional combinations, and cancellation across
all packets and bands.

This allows recursive use of a finite catalogue with **unbounded total
depth**, currents using larger exposed graphs, and arbitrary finite depth
depending on `N`. It does not assert that a full current is absent at any
one of these cutoffs. Unbounded complexity is permitted by the programme's
sufficient criterion, so the theorem is a structural constraint on a
constructor, not a refutation of that criterion.

## 2. The three sources and the displayed arrows

The divisibility hypothesis makes every `y_k` an odd integer. In fact
`y_k+1` remains divisible by 2 through `k=D+3`, and through `k=D+2` it is
divisible by 4. Therefore

\[
3y_k+1=2y_{k+1},\qquad v_2(3y_k+1)=1\quad(k\le D+2).
\]

The points `y_1=64N-1`, `y_2=96N-1`, and `y_3=144N-1` are in the last
two annular bands. Since `X=1 modulo 9`, their residues modulo 18 are
respectively `5,17,17`; the six-band table gives coefficients `-2,2,2`.
All later chain states are above the source support.

Every displayed arrow is in `G_D(N)`: the first three origins are sources,
and `y_k`, `3<=k<=D+2`, is at distance `k-3<=D-1` from the top source.
The terminal state `y_(D+3)` has no outgoing arrow in this graph. Any
source's state after at most `D-1` steps is bounded above by

\[
\left(\frac32\right)^{D-1}144N-1=y_{D+2}<y_{D+3}.
\]

It remains to exclude **every extra incoming exposed arrow**. This is the
main point of the proof.

## 3. Inverse histories and their value at X=1

Consider an admissible inverse history of length `l<=D` ending at a chain
point `y_k`. If its inverse valuations are `a_1,...,a_l>=1`, write
`A=a_1+...+a_l`. Every backward state has the exact form

\[
x=uX-c,\qquad u=3^{k-l}2^{A-k},\qquad c>0.
\]

An inverse step of valuation `a` acts by

\[
u' = \frac{2^a u}{3},\qquad
c' = \frac{2^a c+1}{3}.
\]

Define the auxiliary rational number

\[
z=u-c,
\]

which is what the affine state would equal at `X=1`. Its inverse update is

\[
z'=\frac{2^a z-1}{3}.
\]

These auxiliary numbers are used only to prove an arithmetic inequality.
They are not substituted for the actual positive odd Collatz states.

Each chain point is `-1 modulo 3`, so its direct inverse valuations are
odd. Valuation 1 leads to the preceding chain point. Every other inverse
branch begins with an odd valuation at least **3**. In the rest of this
section consider any history whose first inverse step is such an extra
branch. Its cumulative excess

\[
E=A-l=\sum_{i=1}^l(a_i-1)
\]

is at least 2 and cannot decrease.

### Before the first integer auxiliary value

Initially `c=1`. While `A<k`, the auxiliary state is not an integer and
`l<k`. The coefficient `u=3^(k-l)/2^(k-A)` is divisible by 3 in rational
arithmetic with powers of 2 as denominators. The actual state is integral
because `X` supplies all these powers of 2. Consequently the admissibility
condition for the next inverse branch is exactly

\[
3\mid 2^a c+1.
\]

Thus `c` remains a positive odd integer up to and including the first
step for which `A>=k`. That step occurs by `l<=k`, if the inverse history
is long enough to reach it. At that first step the auxiliary value is
indeed integral.

All auxiliary values through this point are positive. To see this,
compare inverse maps with `f_1(z)=(2z-1)/3`. Starting from
`z=(3/2)^k-1`, applying `l` copies of `f_1` would give
`(3/2)^(k-l)-1>=0` for `l<=k`. The first extra valuation gives a strict
increase over this comparison, and subsequent inverse maps preserve the
strict inequality while the comparison values remain nonnegative.

Before integer arrival, put `s=k-A>0` and `r=k-l`. Then
`r-s=E>=2`, so

\[
u=\frac{3^r}{2^s}=3^E\left(\frac32\right)^s\ge9.
\]

Hence every such predecessor is already above the annulus; Section 5
makes this height comparison explicit.

### At the first integer auxiliary value

Now put `r=k-l>=0` and `s=A-k>=0`. Since `r+s=E>=2`,

\[
u=3^r2^s\ge4.
\]

At this stage `u` is an integer, `c` is a positive odd integer, and
`z=u-c` is a positive integer. If `z` is odd and equals 5, the strict
inequality `u>z` gives `u>=6`. If `z` is even, then `u` is odd, so `s=0`
and `r>=2`; in this case `u>=9`.

## 4. A preserved inequality after integer arrival

The ternary congruence makes the auxiliary integers track all subsequent
inverse admissibility decisions. At a history length `l<=D`,

\[
x-z=u(X-1),\qquad u=3^{k-l}2^{A-k}.
\]

After integer arrival the only possible denominator of `u` is a power of
3, of exponent at most `max(l-k,0)`. Since `X-1` is divisible by
`3^(D+2)`, the difference `x-z` is an integer divisible by 3 throughout
the histories under consideration. An admissible inverse branch at the
actual state therefore also has `3|(2^a z-1)`. Its new auxiliary value is
a positive integer. After one such inverse step it is odd.

For positive odd auxiliary values preserve the three conditions

\[
c>0,\qquad u\ge4,\qquad z=5\ \Longrightarrow\ u\ge6.
\tag{*}
\]

They hold at an odd first integer arrival by the preceding section. If
the first integer auxiliary value is even, `u>=9`, so its next valid
inverse has odd auxiliary value and `u'=2^a u/3>=6`. This also establishes
all three conditions.

To prove preservation, first note that `c'=(2^a c+1)/3>0`, hence `u'>z'`.

- If `a>=2`, then `u'>=4u/3>=16/3>4`.
- If `a=1`, an admissible odd `z` must be `2 modulo 3`, hence `z=5` or
  `z>=11`. At `z=5`, condition (*) gives `u'=2u/3>=4`. At `z>=11`,
  `u>z` gives `u'>22/3>4`.
- If the **new** auxiliary value is 5, then `2^a z=16`. With `z` positive
  and odd, the only possibility is `z=1`, `a=4`. Thus
  `u'=16u/3>=64/3>6`, proving the extra condition at 5.

This proves (*) by induction. Every extra-branch ancestor, before or after
integer arrival, therefore has

\[
u\ge4,\qquad z>0.
\]

The special condition at auxiliary value 5 is necessary for this
inequality proof; simply assuming `u>=4` and `u>z` would not suffice.

## 5. Excluding every extra incoming exposed edge

For any of these extra-branch predecessors,

\[
x=uX-c=u(X-1)+z>4(X-1).
\]

For `X>=8`,

\[
4(X-1)>\frac{27}{8}X-1=144N-1.
\]

Our divisibility assumptions imply `X>=1024`. Thus **no predecessor on
an extra inverse branch of length at most D is an annular source**, since
all annular sources are at most `144N-1`.

An extra incoming arrow `p -> y_k` could belong to `G_D(N)` only if some
annular source reached `p` in at most `D-1` steps. Reversing that history
would give an excluded extra-branch inverse history of length at most D.
Therefore no such incoming arrow is present.

The valuation-one predecessor at the bottom is `X-1`. It is divisible by
3, so it has annular coefficient zero and has no positive odd Syracuse
predecessor. It is not an exposed origin. All other valuation-one
predecessors are precisely the preceding displayed chain points.

Together with the terminal height bound, these facts exhaust every
incident arrow of every chain point. The chain is the **complete**
historical component. Its mass 2 proves the theorem.

## 6. Verification and exact scope

The proof above covers arbitrary integer depths and all inverse
valuations; a finite scan is not used to establish those quantifiers.
The companion checker verifies its arithmetic constants and source
formulas, then compares the complete predicted component against the
independent bounded inverse oracle at selected CRT and required-ray
cutoffs. The CRT representatives keep the numerical checks manageable;
the required-ray existence proof remains symbolic at large depths.

```sh
python3 experiments/residual_progress/templates/check_unbounded_exposure.py
```

Its receipt states every finite input and cap. A cap is always unresolved,
never an obstruction. The original finite examples and fixed-depth
symbolic lift remain available as independent evidence and provenance.

The theorem closes the earlier question of whether a uniform exposure
depth can suffice for all actual annuli: **it cannot**. It leaves the
main construction problem open. A successful universal method must allow
unbounded historical exposure, or recursive identities whose total
source-to-anchor depth grows with the cutoff.
