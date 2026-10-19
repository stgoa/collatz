# A disjoint annular recursion for the revised packets

Date: 2026-10-17. Status: written elementary identities with finite arithmetic
checks. This note supplies no universal current construction, Collatz proof,
or novelty claim. All clocks and measures are those of
`papers/right_aligned_reduction/right_aligned_reduction.tex`: odd-only Syracuse,
absorption at 1, exact integer source cutoffs, and the revised right-aligned
depth-one packets.

## Statement

Let `N` be any positive integer divisible by 8 and put `Q=9N/4`. Then `Q` is
a positive even multiple of 18. There is the exact identity

\[
\Pi^{\rm R}_{64N}=\Pi^{\rm R}_N+A_N,\qquad
\eta_{64N}=\eta_N,
\]

with disjoint supports

\[
\operatorname{supp}\Pi^{\rm R}_N\subset(1,Q),\qquad
\operatorname{supp}A_N\subset(Q,64Q).
\]

For `j=0,...,5`, on the integer band `2^j Q < y < 2^(j+1) Q`, `A_N(y)`
depends only on `y modulo 18`. It vanishes on multiples of 3 and has this
table on the remaining odd residues:

| j | 1 | 5 | 7 | 11 | 13 | 17 |
|---|--:|--:|--:|---:|---:|---:|
| 0 | 1 | 0 | 1 | 0 | -2 | 0 |
| 1 | 2 | 1 | -1 | 1 | -1 | -2 |
| 2 | 3 | -1 | -3 | 2 | 0 | -1 |
| 3 | 1 | -3 | -2 | 3 | 1 | 0 |
| 4 | -1 | -2 | -1 | 1 | 2 | 1 |
| 5 | 0 | -1 | 0 | -1 | 0 | 2 |

Every individual band has signed total zero. As useful exact checks,

\[
\sum_y A_N(y)=0,\qquad \sum_y yA_N(y)=63Q.
\]

The same table gives the exact source-size formulas

\[
\|A_N\|_1=99N/2,\qquad \|A_N^+\|_1=99N/4,\qquad
|\operatorname{supp}A_N|=267N/8.
\]

## Proof of the recursion

For `8|N`, both source cutoffs are even integers,

\[
n_1(N)=3N/2,\qquad n_2(N)=3N/4,
\]

and `n_i(64N)=64 n_i(N)`. Recall the exact valuation representatives
`q_a`, periods `M_a=2^(a+1)`, endpoint progressions `e_a+6t`, and first
lift indices from the main proof note. Their exact shift identities are

\[
q_{a+6}=64q_a+21,\quad M_{a+6}=64M_a,\quad e_{a+6}=e_a.
\]

The source cutoff difference `n_i(N)-q_a` is odd. Its fractional quotient
by the even integer `M_a` is at least `1/M_a`; consequently subtracting
`21/(64M_a)` cannot change its floor. This includes negative quotients.
Therefore

\[
\left\lfloor\frac{64n_i(N)-q_{a+6}}{M_{a+6}}\right\rfloor
=\left\lfloor\frac{n_i(N)-q_a}{M_a}\right\rfloor.
\]

The first lift index is unchanged, so the entire lift interval, its length
modulo 3, and its right-aligned triple partition are unchanged. Corresponding
sources satisfy `x'=64x+21`, hence `x'=x modulo 3`; their coefficients agree
in each of the two components. Thus valuations `a+6` at cutoff `64N`
reproduce exactly valuation `a` at cutoff `N`. The valuation budget also
shifts by exactly 6.

Only valuations `a=1,...,6` remain. At cutoff `64N` both source cutoffs are
divisible by `3M_a` for these six valuations. If `a` is odd, its lift count
is therefore divisible by 3 and there is no leftover. If `a` is even,
its lift count is 2 modulo 3, and its two leftovers have endpoints 7 and
13. Summing both components, the leftover coefficient pairs for `a=2,4,6`
are respectively `(-2,1)`, `(1,-2)`, and `(1,1)`. They sum to zero.
This proves `eta_(64N)=eta_N`, and `A_N` is exactly the total one-step
pushforward supplied by valuations 1 through 6 at cutoff `64N`.

## Derivation of the bands

For an odd endpoint `y` not divisible by 3, valuation `a` contributes only
when

\[
x_a=(2^a y-1)/3
\]

is an integer. Equivalently `a` is odd for `y=5 modulo 6` and even for
`y=1 modulo 6`. Its two cutoff conditions, on odd integer endpoints, are

\[
y<2^{7-a}Q\quad\hbox{(outer component)},\qquad
y<2^{6-a}Q\quad\hbox{(inner component)}.
\]

The possible fractional `1/2^a` in solving the source inequality makes
no difference: every displayed threshold is even and every endpoint is
odd. Endpoints equal to 1 are discarded throughout.

For `1<y<Q`, all three compatible valuations in `1,...,6` occur in both
components. Passing from `a` to `a+2` replaces `x_a` by `4x_a+1`, so the
three source residues modulo 3 run through all three classes. Each
component's coefficient sum is zero. For `y>64Q` no valuation occurs.
The new contribution is therefore confined to `(Q,64Q)`.

In band `j`, put `k=6-j`. The outer component includes exactly the
compatible valuations `a<=k`, and the inner component those `a<=k-1`.
Consequently its coefficient is the explicit finite formula

\[
 A_N(y)=\sum_{\substack{1\le a\le k\\2^ay\equiv1\ (3)}}
       (3\mathbf1_{x_a\equiv2\ (3)}-1)
 +\sum_{\substack{1\le a<k\\2^ay\equiv1\ (3)}}
       (3\mathbf1_{x_a\equiv1\ (3)}-1).
\]

This depends only on `y modulo 18` and evaluates to the table above.
Every row has coefficient sum zero. Every band boundary is a multiple of
18, so each row's residues occur equally often; this proves zero mass
for each band. The weighted residue sums are respectively
`(-18,-36,-18,18,36,18)`. Multiplying by the number `2^j Q/18` of full
18-blocks proves the first-moment identity `63Q`.
The row absolute sums are `(4,8,10,10,8,4)` and the row support sizes
are `(3,6,5,5,6,3)`. Since band `j` contains `2^j N/8` complete blocks,
their weighted sums give `99N/2` and `267N/8`, respectively. Zero signed
mass makes the positive mass exactly half the absolute mass.

Finally a packet endpoint at cutoff `N` is at most `(3n_1(N)+1)/2=Q+1/2`.
It is odd, while `Q` is even, so it is at most `Q-1`. This proves disjointness.

## What the identity does and does not construct

It gives the exact measure recursion

\[
\Pi^{\rm R}_{64^hN}=\Pi^{\rm R}_N+
\sum_{r=0}^{h-1} A_{64^rN},\qquad h\ge1,
\]

whose annular supports are pairwise disjoint. A certificate `J_N` and an
exact annular certificate `K_N` with `A_N=(I-P)K_N` would indeed give
`J_(64N)=J_N+K_N`. The table does **not** supply `K_N`. Zero signed mass in
each band does not control its unknown future.

Disjointness also gives exact norm and atom-count recursions:

\[
\begin{aligned}
\|\Pi^{\rm R}_{64^hN}\|_1
 &=\|\Pi^{\rm R}_N\|_1+\frac{11N}{14}(64^h-1),\\
|\operatorname{supp}\Pi^{\rm R}_{64^hN}|
 &=|\operatorname{supp}\Pi^{\rm R}_N|
   +\frac{267N}{8\cdot63}(64^h-1).
\end{aligned}
\]

Thus their normalized limits along any such scaling ray are `11/14`
and `89/168`. These count the source measure; they are not bounds on
the size or positive cost of a current.

There is a particularly simple lower-source representative. Let
`V_N=nu_(64N)-nu_N`. The equality of the core remainders gives

\[
A_N=PV_N=V_N-(I-P)V_N.
\]

Writing `w_r(x)=3 1_(x=r mod3)-1`, this `V_N` is exactly:

- `w_1(x)` on `3N/4 < x <= 3N/2`;
- `w_1(x)+w_2(x)=1-3 1_(3|x)` on `3N/2 < x <= 48N`;
- `w_2(x)` on `48N < x <= 96N`;
- zero elsewhere.

Thus an annular current exists precisely when one exists for this
three-interval signed source measure. This is a reversible change of
representative, not a terminating induction: the new measure is not a
smaller member of the same six-band family.

One can make that obstruction explicit in the finite-current quotient.
Let `U_t` be counting measure on odd states `1<x<=t`, and let
`F_t=U_(64t)-U_t` whenever the arguments below are integers. The exact
source transport identity implies

\[
[A_N]=3[F_N]-3[F_{N/4}]-[F_{3N/2}]-[F_{3N/4}].
\]

Here brackets mean equality modulo a finite signed divergence. This is
the same expanding source-scale operator as the original problem: the
term `F_(3N/2)` exceeds the source scale `N`. No contraction or finite
termination follows from the annular recursion alone.

## Reproduce the checks

Run from the repository root, without Python optimization:

```sh
python3 experiments/current_construction/recursive/check_annular_recursion.py
```

The checker derives the residue table independently from exact inverse
source arithmetic, compares the entire annular measure against the
existing packet constructor at all multiples of 8 through 512 and the
additional cutoffs 1000 and 4096, and checks each band, both source
components, the core identity, and the first moment. It uses no trajectory
search to prove or test this recursion. `--write-receipt` refreshes the
adjacent finite audit JSON. These are finite implementation checks; the
general identity is proved above.
