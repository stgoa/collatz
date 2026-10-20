# Exact cancellation after an arbitrarily long initial isolation

Date: 2026-10-17. Status: written elementary partial-current construction,
with exact checks and two complete finite component witnesses. This does
not construct a current for the whole annulus. No Collatz or novelty claim
is supplied; the argument is not human peer-reviewed or formally verified.

The clock is odd-only Syracuse, absorbed at 1. We use the actual six-band
annular measure `A_N`, with `8|N`, and write `G_D(N)` for the first `D`
arrows exposed from **every** nonzero source. Historical intersections
are retained. All coefficients below are actual annular coefficients.

## 1. What changes at release

The previous [unbounded-depth theorem](../templates/UNBOUNDED_EXPOSURE_DEPTH.md)
isolates three sources, of coefficients `-2,+2,+2`, on a rising chain.
Its positive component mass is 2. A newly attached negative source need
not reduce that mass: other sources can join through the same exposed
edges. The two exact examples in Section 6 distinguish these outcomes.

Here we construct infinitely many arithmetic families in which **two
specified negative annular sources cancel that entire three-source
block**. The resulting finite current is everywhere nonpositive, hence
has zero positive cost. The families have unbounded initial isolation
depth, and each has infinitely many realizations on the required ladder
`N=96*64^k`.

This is a universal identity for a five-source **submeasure**. Extra
sources of the full exposed component are not omitted from a claimed
component certificate: a complete component claim is made only for the
finite examples in Section 6. The construction does not account for the
rest of `A_N` or prove that every positive plateau ends.

## 2. Parameters and congruences

Choose an integer `h>=2`. Let `r` be the least nonnegative integer such
that

\[
\lambda=4\left(\frac43\right)^h\left(\frac23\right)^r
\le\frac{27}{8}.
\]

Then `r>=1` and `9/4<lambda<=27/8`. Retain the values of `h` for which

\[
\boxed{\quad\frac{81}{32}<\lambda\le\frac{27}{8}.\quad}
\tag{1}
\]

There are arbitrarily large such `h`. Indeed, if a value fails (1), then
`9/4<lambda<=81/32`; at `h+1`, the same `r` gives
`3<(4/3)lambda<=27/8`, and is still the least admissible `r`.
Thus two consecutive values of `h` cannot both fail (1). This conclusion
is an exact inequality argument, not an inference from the finite list.

Choose either `V=47` or `V=155`. All modular inverses in the following
formula are taken modulo `3^(r+4)`. Set

\[
U_0\equiv
4^{-h-1}\left(3^r2^{-r}(V+1)-2\right)
\pmod{3^{r+4}},
\tag{2}
\]

and require

\[
X\equiv1+3^hU_0\pmod{3^{h+r+4}},\qquad
2^{\max(h+5,10)}\mid X.
\tag{3}
\]

The two moduli are coprime, so (3) has an unbounded positive arithmetic
progression of solutions. Since `r>=1`, (2) gives `U_0=1 modulo3`.
Consequently **every** solution has `v_3(X-1)=h` exactly.

Write

\[
c=\lambda+1-2\left(\frac23\right)^r,
\]

and impose the explicit size condition

\[
X\ge1024,\qquad
X>\frac{c+1/2}{\lambda-81/32}.
\tag{4}
\]

This excludes only finitely many members of the progression. Define

\[
N=\frac{3X}{128},\qquad U=\frac{X-1}{3^h},\qquad
v=\frac{2^r\bigl(4^{h+1}U+2\bigr)}{3^r}-1,
\tag{5}
\]

\[
t=\frac{2v-1}{3},\qquad
u=\frac{4t-1}{3}=\frac{8v-7}{9}.
\tag{6}
\]

The congruence (2) says exactly that (5) is integral and
`v=V modulo81`. Its numerator shows that `v` is odd: `U` is odd and
`4^(h+1)U+2` has 2-adic valuation 1. Thus `v=V modulo162`.
In particular, (6) consists of odd integers. More explicitly,

| `v modulo162` | `v modulo18` | `t modulo18` | `u modulo18` |
|---|---:|---:|---:|
| 47 | 11 | 13 | 5 |
| 155 | 11 | 13 | 11 |

## 3. The actual source coefficients and the exact paths

Define the three original chain sources

\[
y_1=\frac32X-1=64N-1,\quad
y_2=\frac94X-1=96N-1,\quad
y_3=\frac{27}{8}X-1=144N-1.
\]

Their coefficients are `-2,+2,+2`, because `X=1 modulo9` and their
residues are `5,17,17` modulo18. Also `S(y_1)=y_2` and `S(y_2)=y_3`,
both with exact valuation 1.

Formula (5) is equivalently `v=lambda X-c`. Conditions (1) and (4) give

\[
\frac{81}{32}X+\frac12<v<\frac{27}{8}X-1=y_3.
\tag{7}
\]

For the upper inequality, use `c=lambda+1-2(2/3)^r>1`: indeed
`lambda/[2(2/3)^r]=2(4/3)^h>1`.
From (6) and (7),

\[
y_1<72N<t<y_2<u<v<y_3.
\tag{8}
\]

Thus `u,v,t` all lie in the **top band** `(72N,144N)`. Its coefficient
row, at residues `(1,5,7,11,13,17)`, is `(0,-1,0,-1,0,2)`.
Consequently

\[
A_N(u)=A_N(v)=-1,\qquad A_N(t)=0.
\]

The two identities in (6) give exact Syracuse arrows

\[
u\mathrel{\mathop{\longrightarrow}^{2}}t
\mathrel{\mathop{\longrightarrow}^{1}}v,
\tag{9}
\]

where the labels are valuations. Exactness follows because their
successors are odd.

The path from `v` to `y_1` has the explicit forward valuation word

\[
\boxed{\quad(\underbrace{1,\ldots,1}_{r},
\underbrace{2,\ldots,2}_{h},3).\quad}
\tag{10}
\]

To check the whole word without an orbit assumption, reverse it from
`y_1`. The first inverse valuation 3 gives `4X-3=4(X-1)+1`. After `j`
inverse valuations 2, for `0<=j<=h`, the state is

\[
w_j=4\left(\frac43\right)^j(X-1)+1.
\]

It is an odd integer, since `3^h` divides `X-1`. At `j=h` this equals
`w_h=4^(h+1)U+1`. After `l` subsequent inverse valuations 1 the state is

\[
z_l=\frac{2^l(w_h+1)}{3^l}-1,\qquad0\le l\le r.
\]

Equation (2) makes all these states integral; they are odd, and `z_r=v`.
Each inverse identity therefore has the claimed exact forward valuation.
The `w_j` increase and exceed `y_3`. Each `z_l` before `v` is at least
`z_(r-1)=(3v+1)/2>y_3`, by (7). Hence the path in (10) meets the annulus
only at its two endpoints `v,y_1`, and has no collision with `u,t,y_2,y_3`.
Repeated states in this path would give a cycle followed by `y_1`, which
is impossible for a deterministic map with these endpoint heights.

## 4. A finite current of zero positive cost

Let `L=h+r+1`, and let `p_0=v,...,p_L=y_1` be the path (10). Define

\[
\mu=-\delta_u-\delta_v-2\delta_{y_1}
             +2\delta_{y_2}+2\delta_{y_3},
\]

\[
\boxed{\quad
J=-\delta_u-\delta_t-2\sum_{j=0}^{L-1}\delta_{p_j}
                 -4\delta_{y_1}-2\delta_{y_2}.
\quad}
\tag{11}
\]

Telescoping along (9), (10), and the last two chain arrows gives

\[
(I-P)J
=(-\delta_u+\delta_v)+(-2\delta_v+2\delta_{y_1})
  +(-4\delta_{y_1}+4\delta_{y_2})
  +(-2\delta_{y_2}+2\delta_{y_3})
=\mu.
\]

All five coefficients of `mu` equal the corresponding actual coefficients
of `A_N`; the five points are distinct by (8). Thus subtracting `mu`
uses valid annular source capacity and removes exactly **4 units of
positive mass**. All current coefficients are nonpositive, so
`||J^+||_1=0`. The current has `L+4` rows and `||J||_1=2L+8`.
In addition, `r<=h`: taking `r=h` gives
`4(8/9)^h<=256/81<27/8` for `h>=2`. Hence

\[
L\le2h+1,\qquad |\operatorname{supp}J|\le2h+5,
\qquad \|J\|_1\le4h+10.
\]

Every current arrow belongs to `G_L(N)`: the long path starts at the
actual source `v`, the two-arrow path starts at the actual source `u`,
and the final two origins `y_1,y_2` are sources themselves. This statement
does not require that `G_L` has only these five sources in its component.
It is a finite exact certificate for `mu`, leaving `A_N-mu` unclaimed.

No simultaneous packing with the earlier catalogues is claimed here.
Those catalogues may reuse `u` or `v`; combined source capacity would need
a separate proof. This family removes a constant amount per chosen `X`,
not a positive fraction of the whole annulus by itself.

## 5. Unbounded initial delay and required-ray realizations

### A sharper form of the existing isolation argument

If `h>=2`, `v_3(X-1)>=h`, and
`2^max(D+4,10)` divides `X`, the existing complete-chain proof remains
valid for **every `1<=D<=h+1`**. Its sources and whole component are the
same three-source chain, of mass 2.

Here is the precision check required for this refinement. In that proof,
an extra inverse history ending at `y_k` has, after `l` steps,

\[
x-z=u(X-1),\qquad u=3^{k-l}2^{A-k}.
\]

Before the first integral auxiliary value, the old argument is unchanged.
After that arrival, the only possible denominator of `u` is a power of3.
To make the **next** auxiliary value integral at step `l`, it is enough
that the difference at step `l-1` is divisible by3. Its ternary valuation
is at least

\[
h+k-(l-1)\ge h+1-(D-1)\ge1
\]

for `k>=1` and `l<=D<=h+1`. Thus every admitted inverse remains governed
by the same positive integral auxiliary values. The proved invariant
`u>=4`, `z>0`, with its special condition at `z=5`, still excludes every
extra source. No extra divisibility of the **final** difference is needed.
The bottom and terminal closure arguments are unchanged. This checks all
incoming histories, rather than just the visible chain.

Our conditions (3) supply the binary requirement with `D=h+1`. Therefore
each family in Sections 2–4 has a complete mass-2 top component through
depth `h+1`, followed by an explicit cancellation of its three designated
sources inside exposure `L=h+r+1`. Since qualifying `h` are unbounded,
these are actual partial cancellations after arbitrarily long isolation.
The theorem does not say that the **whole** component at depth `L` has
nonpositive mass, because other annular sources may have joined by then.

This refinement also improves the previously recorded lower bound on
the whole-annulus sufficient exposure depth. With infinity allowed,

\[
\boxed{\quad d_*(96\cdot64^k)\ge v_3(k+2)+4,\qquad k\ge0.\quad}
\tag{12}
\]

Indeed, `X=2^e`, where `e=6(k+2)`, has
`h=v_3(X-1)=2+v_3(k+2)`. The exact valuation follows from the cubing
calculation below and the factorization
`(a^q-1)/(a-1)=1+a+...+a^(q-1)=q modulo3` when `a=1 modulo3`
and `3` does not divide `q`. Also `e>=max(h+5,10)` for all `k>=0`.
Thus `G_(h+1)` has the complete mass-2 component, forcing
`d_*>=h+2`. This is a lower bound on exposure required for the **whole
annulus**, and does not assert that this depth is sufficient.

### Each congruence family occurs on the required ladder

Put `M=h+r+4`. The residue for `X` in (3) is a unit modulo `3^M`.
The integer 2 generates all units modulo `3^M`; an elementary proof is
included to avoid relying on an unstated number-theoretic input.

Write `4^(3^n)=1+3^(n+1)b_n`. At `n=0`, `b_0=1`. Cubing gives

\[
b_{n+1}=b_n+3^{n+1}b_n^2+3^{2n+1}b_n^3\equiv b_n\pmod3.
\]

Hence `v_3(4^(3^n)-1)=n+1`, so the order of4 modulo `3^M` is exactly
`3^(M-1)`. The order of2 is even, because its residue modulo3 is -1;
therefore it is `2*3^(M-1)`. This equals the number of units modulo `3^M`,
so every unit is a power of2.

Consequently there is an exponent `e_0`, unique modulo `2*3^(M-1)`,
with `2^e_0` equal to the required residue. Taking
`X=2^(e_0+j*2*3^(M-1))` for sufficiently large integers `j` satisfies
both the binary and size conditions. Since `X=1 modulo9`, its exponent
`e` is divisible by6. For `e>=12`,

\[
N=\frac{3\cdot2^e}{128}=96\cdot64^{e/6-2}.
\]

Thus every qualifying `h` has infinitely many examples on the single
required ladder. Finding a small representative exponent is not needed
for the existence proof or current identity.

For the smallest case `h=r=2`, the two residues for `X` modulo6561 are
631 and 2818. Exact exponent representatives are respectively 3462 and
546 modulo4374. The ladder indices are therefore

\[
k=575\pmod{729}\quad\hbox{or}\quad k=89\pmod{729}.
\]

In this case `v=(256X-265)/81` and `u=(2048X-2687)/729`.

## 6. Two complete first-release witnesses

The bounded inverse oracle checks **every incoming historical source**.
The receipt stores all vertices, arrows, source coefficients, caps, and
query counts. Neither example reaches 1 in its exposed component.

| Parameter | Before release | First release | Effect |
|---|---|---|---|
| `X=2583691264`, `N=60555264`, `h=4` | `G_8`: 11 vertices, 3 sources, mass2 | `G_9`: 23 vertices, 6 sources, mass2 | Three new sources have total0. |
| `X=14512291840`, `N=340131840`, `h=2` | `G_4`: 7 vertices, 3 sources, mass2 | `G_5`: 15 vertices, 5 sources, mass0 | Two new sources have total-2. |

For the neutral release, the extra sources are

\[
(4301295295,+2),\quad(5735060393,-1),\quad(6451942943,-1).
\]

The last source has forward word `(1,1,1,1,2,2,2,2,3)` to `y_1`.
The first source is its valuation-one predecessor, and the middle source
is the valuation-two predecessor of the first. A selected negative
attachment would therefore misreport the complete mass change.

For the resolving release, the complete five-source table is

| Source | Coefficient |
|---:|---:|
| 21768437759 | -2 |
| 32652656639 | +2 |
| 40769785577 | -1 |
| 45866008775 | -1 |
| 48978984959 | +2 |

Here (11) certifies **the entire exposed top component at depth5**,
because the complete oracle source list equals `mu`. The current has
nine rows, norm18, and positive cost0. This is not a certificate for the
other components of the annulus.

The new source `u` reaches `y_1` in seven arrows, even though the entire
current is already in `G_5`: `v` is itself a source, so its outgoing
history is exposed independently. This is why an ordinary single-path
length must not be substituted for the historical graph's exposure clock.

## 7. Reproduction and remaining question

```sh
python3 experiments/residual_progress/release/check_release.py
```

The checker regenerates both complete component witnesses, verifies the
exact divergence and actual source capacities for 22 parameter families
and three representatives per family, and checks two actual required-ray
representatives. Its receipt stores compact hashes for the regenerable
family currents and full rows for the resolving component certificate.
It also checks the canonical-parameter dichotomy for `2<=h<=64`; the
unbounded conclusion follows from the inequality proof, not that scan.
The precision refinement is checked against the complete inverse oracle
at `D=h+1`, for every `2<=h<=16` and both possible next nonzero ternary
digits, as well as six explicit required-ladder cutoffs.

The first-release examples use caps of 2,000 vertices and 100,000 inverse
reachability queries. A cap is unresolved and cannot produce a completed
component claim. The default verification asserts both searches finish.

**Open:** extend this mechanism to control every remaining positive
component, or prove that its recursive use closes a specified residual
family with a decreasing parameter. The isolated block can be canceled
after arbitrarily long delay in these explicit families; a universal
annular completion or termination theorem does not follow.
