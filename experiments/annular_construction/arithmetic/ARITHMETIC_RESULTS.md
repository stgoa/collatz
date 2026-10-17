# Constructive arithmetic reductions for the annular increments

Date: 2026-10-17. Status: written proofs and finite arithmetic checks.
No universal complete current, termination proof for a complete constructor,
or novelty claim is supplied. All measures use the repository's odd-only
Syracuse map, absorption at 1, and exact revised annulus `A_N`, with `8|N`
and `Q=9N/4`. The six annular coefficient rows are the ones proved in
`experiments/current_construction/recursive/annular_recursion.md`.

This note supplies two explicit finite **partial** currents for every such
`N`. Their remaining positive mass is retained and identified below.

## 1. A five-family cancellation current with zero positive cost

In this section all inequalities are strict. For each row of the following
table, take every integer `x` in the stated interval and residue classes.
Put `x_1=(3x+1)/2` and `x_2=(9x+5)/4`. Each listed residue is 7 modulo 8,
so both first valuations are exactly 1. The one-step row only uses `x_1`.

| Family | Interval for x | x modulo 72 | Actual coefficients at x,x1,x2 | Current coefficients at x,x1 |
|---|---|---|---|---|
| E | 12N < x < 16N | 7 | (-3,3), with no x2 term | (-3), with no x1 row |
| D | 16N < x < 18N | 23,71 | (-1,0,1) | (-1,-1) |
| B | 24N < x < 32N | 7 | (-2,1,1) | (-2,-1) |
| C | 32N < x < 36N | 23 | (-3,1,2) | (-3,-2) |
| A | 48N < x < 64N | 7,55 | (-1,-1,2) | (-1,-2) |

The A-family residue 7 rule was found independently in the component
investigation. The present catalogue adds its residue 55 counterpart and
the other four families.

Let `mu_cat,N` be the sum of all listed signed chains, and `J_cat,N` the
sum of their current rows. Then

\[
\mu_{\rm cat,N}=(I-P)J_{\rm cat,N},\qquad J_{\rm cat,N}\le0,
\qquad A_N=(I-P)J_{\rm cat,N}+Z_N.
\]

The nonzero supports of the chains are pairwise disjoint, and each chain
removes the **whole** actual coefficient of `A_N` at each of its nonzero
positions. Thus `Z_N` is exactly `A_N` with these positions set to zero.
All other coefficients, including all remaining positive coefficients,
are retained unchanged. This is not a nonpositive-residual certificate.

### Verification of the families and disjointness

The coefficient table and the affine formulas put the chains in these
locations, listing state intervals in units of `N` and residues modulo 18:

| Family | x | x1 | x2 |
|---|---|---|---|
| E | (12,16), residue 7, band 2 | (18,24), residue 11, band 3 | not used |
| D | (16,18), residues 5 or 17, band 2 | (24,27), residue 17, band 3, coefficient 0 | (36,81/2), residue 17, band 4 |
| B | (24,32), residue 7, band 3 | (36,48), residue 11, band 4 | (54,72), residue 17, band 4 |
| C | (32,36), residue 5, band 3 | (48,54), residue 17, band 4 | (72,81), residue 17, band 5 |
| A | (48,64), residues 7 or 1, band 4 | (72,96), residue 11, band 5 | (108,144), residue 17, band 5 |

The half-step affine offsets cannot cross a displayed band boundary:
the original interval endpoints are even integers and the permitted states
are odd. In the D-family the upper endpoint `81N/2` is also even because
`8|N`. The residue restrictions similarly exclude the borderline cases.
The nonzero columns in this table are disjoint by interval or residue;
each affine map is injective. Within family A the two input residues also
have disjoint images under the same injective maps. This proves that no
coefficient is spent twice. Zero intermediate points do not contribute
source measure.

For a chain with weights `(c0,c1,c2)` summing to zero, the displayed current
is `c0 delta_x+(c0+c1) delta_x1`, whose divergence is the chain. Every
listed current coefficient is negative. This proves the current identity
and the sign claim using only the first two exact branches.

### Exact amount removed

Write

\[
C(a,b;r)=\left\lfloor\frac{bN-1-r}{72}\right\rfloor
          -\left\lfloor\frac{aN-r}{72}\right\rfloor.
\]

This counts `aN<x<bN`, `x=r modulo 72`. The removed positive mass is

\[
\begin{split}
D(N)={}&3C(12,16;7)+C(16,18;23)+C(16,18;71)\\
 &+2C(24,32;7)+3C(32,36;23)\\
 &+2C(48,64;7)+2C(48,64;55).
\end{split}
\]

Consequently `||Z_N^+||_1=99N/4-D(N)` and
`||Z_N||_1=99N/2-2D(N)` exactly. In particular, for `72|N`,

\[
D(N)=3N/2,\qquad \|Z_N^+\|_1=93N/4.
\]

The general correction `D(N)-3N/2` is periodic under `N -> N+72` on
multiples of 8. The exact count formula avoids treating this boundary
correction as an asymptotic estimate. Since `J_cat,N<=0`, for every horizon
`L`, `H_L(mu_cat,N)<=0`, and therefore `H_L(A_N)<=H_L(Z_N)` with no positive
current cost.

## 2. Exact one-step norm contraction and an explicit coalescence current

Define `F(x)=4x+1`. Then `S(F(x))=S(x)` on positive odd states. Every odd
state belongs to a unique `F`-chain rooted at a state `rho(x)` with first
valuation 1 or 2: repeatedly replace `x` by `(x-1)/4` while `x=5 modulo 8`.
Each replacement decreases the positive integer, so this procedure always
terminates. Root 1 is discarded in measures.

Let `R mu` sum coefficients at these roots. Because `P R mu=P mu`,

\[
J_F=\mu-R\mu,\qquad
\mu=(I-P)J_F+R\mu,
\]

is an exact finite partial current for every finite measure `mu`.
Different roots have different successors: a successor `y=2 modulo 3`
has root `(2y-1)/3`, and one `y=1 modulo 3` has root `(4y-1)/3`.
Hence

\[
\|R A_N\|_1=\|P A_N\|_1.
\]

For the annular family this norm has the exact formula

\[
\boxed{\ \|P A_N\|_1=\frac{171N}{4}-|c_N|\ },\qquad |c_N|\le3.
\]

Here `c_N` is the signed mass of the unique `F`-chain rooted at 1 before
absorption. Thus

\[
\|R A_N\|_1\le\frac{19}{22}\|A_N\|_1.
\]

This is an unconditional one-pass contraction, with an explicit current
realizing the change of representative. It does not assert that the
residual is another annulus or that repeated application continues to
contract: `R` is idempotent, so a second `R` pass does nothing.

### Proof by finite residue profiles

Write `f_j(r)` for annular row `j`, with zero coefficients on odd multiples
of 3. The first annular point in each `F`-chain is called its entry. Entries
in bands 0 and 1 are all odd states in those bands. Entries in bands 2
through 5 are exactly the states not equal to 5 modulo 8; otherwise the
previous `F`-point would still be in the annulus. If an entry is in band
`j`, its successive annular points are in bands `j,j+2,...,5`.

The sum along this chain is

\[
g_j(x)=\sum_{0\le k\le(5-j)/2}f_{j+2k}\bigl(F^k(x)\bmod18\bigr).
\]

Here is the resulting period-18 table, including the odd multiples of 3:

| j / r | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 |
|---|--:|--:|--:|--:|--:|---:|---:|---:|---:|
| 0 | 0 | 1 | 2 | 3 | 1 | -1 | -3 | -2 | -1 |
| 1 | -1 | 3 | 1 | 2 | 0 | 1 | -1 | -3 | -2 |
| 2 | 1 | 2 | -1 | -2 | -1 | 2 | 1 | -1 | -1 |
| 3 | 0 | 0 | -3 | -3 | 0 | 3 | 3 | 0 | 0 |
| 4 | -1 | 0 | -2 | -1 | 0 | 1 | 2 | 0 | 1 |
| 5 | 0 | 0 | -1 | 0 | 0 | -1 | 0 | 0 | 2 |

The absolute sums in one period are 14 and 14 for bands 0 and 1. In
bands 2 through 5 the entry condition introduces modulus 8; in each
complete period of length 72 the absolute sums are 36,36,24,12.
Those four band lengths and boundaries are multiples of 72. Since
band `j` has length `2^j Q`, the six exact norm contributions are

\[
N\,(7/4,\ 7/2,\ 9/2,\ 9,\ 12,\ 12),
\]

which sum to `171N/4`. Killing the class rooted at 1 subtracts `|c_N|`.
This class has an entry in band 0 or 1 and three annular points, so the
first two rows of the table prove `|c_N|<=3`. To compute it, start at 1,
iterate `F` until first exceeding `Q`, and add its three annular
coefficients. Zero is possible; the arithmetic formula gives `c_80000=0`.

### Exactly where a positive obstruction remains

For every

\[
32Q<p<64Q,\qquad p\equiv-1\pmod{36},
\]

the root is `rho(p)=p`, the annular coefficient is 2, and `F(p)>64Q`.
Thus `(R A_N)(p)=2` exactly. There are `2N` such states, so the residual
has at least `4N` positive mass. This rules out completing the construction
using `F`-coalescence diamonds alone. Equivalently, such diamonds preserve
`P mu`, whereas a nonpositive residual would have nonpositive pushforward;
`P A_N` has the corresponding positive atoms.

This obstruction allows combinations with further forward transport,
larger affine identities, or cross-time intersections.

## 3. Why bounded residue profiles do not close under forward transport

There is an exact surviving outer profile after any fixed number `t>=0`
of forward Syracuse steps. Put `lambda=3/2`. On odd states in the strip

\[
\lambda^t(32Q+1/3)<y+1\le64\lambda^t Q,
\]

one has

\[
(P^t A_N)(y)=
\begin{cases}
3\mathbf1_{3^{t+2}\mid y+1}-1,&3^{t+1}\mid y+1,\\
0,&\text{otherwise}.
\end{cases}
\]

In particular the coefficient is +2 at every positive state in this strip
equal to -1 modulo `2*3^(t+2)`. These contributions have not disappeared
in a signed norm estimate.

### Proof of the outer profile

Let `T(x)=(3x+1)/2`. Its iterates are `T^t(x)=lambda^t(x+1)-1`.
All Syracuse trajectories are bounded above by these iterates. If one
of the first `t` valuations is at least 2, bound the other steps by `T`
and the exceptional step by `T/2`. The largest resulting value occurs
when the exceptional step comes first. Since every annular source is
at most `64Q-1`, its endpoint then obeys

\[
y+1\le\lambda^t(32Q+1/3).
\]

Thus every contribution in the displayed strip has the all-one valuation
word. Its unique possible source is

\[
x=\frac{2^t(y+1)}{3^t}-1,
\]

which lies in the original top band. The original top-band coefficient
is -1 on `x=5,11 modulo18`, +2 on `x=17 modulo18`, and zero elsewhere.
Substitution gives exactly the formula above. The divisibility conditions
also guarantee integrality and the exact all-one branch. For `t=0` this
is just the original top-band row.

### A scoped closure obstruction

On odd integers the nonzero periodic function above has least even period
`2*3^(t+2)`. Indeed its value at -1 is 2, while translating -1 by an even
integer `M` with `3^(t+2)` not dividing `M` gives value 0 or -1.

Consequently there is no representation of all the forward iterates
`P^t A_N` using a finite fixed list of periodic residue profiles on intervals,
with a number of interval pieces bounded independently of `N` for each
fixed `t`. To see this, let `M` be a common even modulus of the alleged
finite list. Choose `t` with `v_3(M)<t+2`. As `N` grows along any allowed
dyadic ray, the outer strip grows without bound. One interval piece must
then contain enough complete periods to witness two points separated by
`M` with different coefficients, a contradiction.

This excludes a finite fixed-modulus profile ansatz under literal forward
pushforward. It does not exclude growing moduli, a number of pieces growing
with the scale, or algebraic current rewrites before further transport.

## 4. Reproduction and remaining obligation

Run from the repository root without Python optimization:

```sh
python3 experiments/annular_construction/arithmetic/check_arithmetic_reductions.py
```

The checker reconstructs both universal partial-current formulas, verifies
their exact divergences and residuals, checks the norm formula and catalogue
counts on the specified finite range, and checks the outer profile at fixed
finite depths. The adjacent audit JSON records exactly what was run.
`--write-receipt` updates that file. These tests support the implementations;
the general claims above rest on the written arithmetic proofs.

The remaining constructive problem is to remove or control the residual
positive components. The catalogue gives an all-horizon upper-bound
reduction at zero positive cost. The `F` collapse gives an exact norm
contraction of 19/22 on the original annular family. Its residual does not
remain in that family, and its next literal forward profiles require new
ternary digits. No iterated contraction or termination theorem has been
established.

## 5. Reusable combined partial constructor

`combined_partial_current.py` combines the five-chain current above with
all admissible copies of the compiled five-source family from
`../components/AFFINE_COMPONENTS.md`. That note supplies the cross-family
capacity proof; the constructor also checks the entire union of source
supports directly, rejecting any reuse of a source coefficient.

Its reusable entry point is

```python
current, residual, summary = build_combined_partial_current(N)
```

The first two values are full integer dictionaries on actual odd states.
For every positive `N` divisible by 8 they satisfy

\[
A_N=(I-P)\,\text{current}+\text{residual}.
\]

Writing `C(N)` for the number of admissible five-source copies and `D(N)`
for the exact catalogue count above, the constructor verifies

\[
\|\text{residual}^+\|_1=99N/4-D(N)-3C(N),\qquad
\|\text{current}^+\|_1\le3C(N).
\]

The residual is exactly `A_N` with the union of both families' nonzero
source supports deleted. Remaining positive coefficients are returned,
not discarded. The finite template is loaded from its stored receipt and
checked directly; no trajectory search is used during construction.

Run the representative audit, including the empty five-source case at
`N=160` and the larger cutoff `N=6144`:

```sh
python3 experiments/annular_construction/arithmetic/combined_partial_current.py
```

Run a single construction, optionally saving its full current and residual
tables alongside the script:

```sh
python3 experiments/annular_construction/arithmetic/combined_partial_current.py --cutoff 168
python3 experiments/annular_construction/arithmetic/combined_partial_current.py --cutoff 168 --write-tables
```

The default audit compares against `combined_audit.json`; use
`--write-receipt` explicitly to refresh that receipt. This combined
constructor is a universal partial construction. It supplies no complete
certificate or termination theorem for eliminating the remaining positive
mass.
