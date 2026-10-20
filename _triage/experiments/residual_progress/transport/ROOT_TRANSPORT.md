# Root collapse and transport: exact normal form and surviving positive atoms

Date: 2026-10-17. Status: written elementary proofs with bounded arithmetic
checks. These are scoped obstructions to one proposed residual mechanism.
They do not rule out affine current rewrites, cancellation at different
times, or a universal constructor using other operations. No proof of
Collatz, universal termination, or novelty claim is supplied.

We use finite integer signed measures on positive odd states greater than 1.
The Syracuse pushforward `P` discards a contribution when its successor is 1.
Write `rho(x)` for the root obtained by repeatedly replacing `x` by
`(x-1)/4` while `x=5 modulo 8`. The operator `R` collects coefficients at
these roots and discards the class rooted at 1. The annular measure `A_N`,
for positive `8|N`, is exactly the six-band measure in
`../../current_construction/recursive/annular_recursion.md`.

## 1. Interleaving does not produce a new residual dynamics

**Theorem.** On finite signed measures,

\[
R^2=R,\qquad PR=P.
\]

Every finite word in `P,R` therefore has one of the forms
`I`, `R`, `P^k`, or `RP^k`, where `k>=1` is the number of `P` operations.
In particular, starting with `mu_0=R mu` and iterating `mu_(t+1)=RP mu_t`,

\[
\mu_t=RP^t\mu,\qquad
\|\mu_t\|_1=\|P^{t+1}\mu\|_1,\qquad
\|\mu_t^+\|_1=\|(P^{t+1}\mu)^+\|_1.
\]

Thus interleaving root collapse does not create a stronger synchronous
residual evolution. It changes the representatives of successor classes.
The resulting current tables or their positive costs can depend on how the
operations are implemented; the claim here concerns the exact residual.

**Proof.** The `F(x)=4x+1` identity gives `S(F(x))=S(x)`, including the
class killed at 1. Consequently `PR=P`. Root representatives are unchanged
by another root collapse, proving `R^2=R`. Repeated use of these relations
eliminates every `R` except a possible leftmost one. It also gives
`(RP)^t R=RP^t` for every `t>=0`.

The roots greater than1 are precisely the odd integers greater than1 in
the residue classes `3 modulo 4` or `1 modulo 8`. Their exact valuations
are respectively 1 and 2. The map

\[
\phi(x)=S(x)
\]

is a bijection from these roots to the odd integers greater than 1 not
divisible by 3. Indeed its inverse is

\[
\phi^{-1}(y)=
\begin{cases}
(2y-1)/3,&y=2\pmod3,\\
(4y-1)/3,&y=1\pmod3.
\end{cases}
\]

The displayed inverse roots have the claimed exact valuations. No root
greater than 1 maps to 1. Therefore `P` preserves both total variation and
positive mass on root-supported measures. Applying this to `R mu` and
using `PR=P` proves both norm identities. It proves more: on roots the
killed map `Q(x)=rho(S(x))` is conjugate through `phi` to ordinary killed
Syracuse on odd states not divisible by 3, because

\[
\phi(Q(x))=S(S(x))=S(\phi(x)).
\]

When `rho(S(x))=1`, both sides are killed; this includes states whose first
successor is greater than 1 but belongs to the `F`-class of 1. This handles
the absorption convention exactly. The conjugacy is an identity of
dynamics and supplies no independent termination theorem. \(\square\)

## 2. An explicit family survives every bounded number of operations

Let `lambda=3/2`. Fix `N>0` divisible by 8 and an integer `t>=0`. Define

\[
X_{N,t}=\{x:72N<x<144N,\quad
                 x\equiv-1\pmod{9\,2^{t+2}}\}.
\]

**Theorem.** The set has exactly

\[
C_{N,t}=\left\lfloor\frac{4N}{2^t}\right\rfloor
       -\left\lfloor\frac{2N}{2^t}\right\rfloor
\]

elements. For each `x` in this set and every `0<=j<=t`, put

\[
y_j=\frac{3^j(x+1)}{2^j}-1.
\]

Then every first `j` Syracuse valuation is 1, `y_j=3 modulo 4`, and

\[
(P^j A_N)(y_j)=(RP^j A_N)(y_j)=2.
\]

For each fixed `j`, the displayed states for distinct `x` are distinct.
In particular both residuals have positive mass at least `2C_(N,t)`.

**Proof of the count and branches.** Write `M=9*2^(t+2)` and `x=Mm-1`.
The interval condition gives

\[
\left\lfloor\frac{72N+1}{M}\right\rfloor<m
\le\left\lfloor\frac{144N}{M}\right\rfloor.
\]

Because `72N` is a multiple of 9 and `M` is a multiple of 9,
`floor((72N+1)/M)=floor(72N/M)`. The difference of the two floors is
exactly `C_(N,t)`. Furthermore, `y_j+1` is divisible by
`2^(t+2-j)`, which is at least 4 for every `j<=t`. Thus `y_j=3 modulo 4`.
The valuation at each preceding step is exactly 1, so the formula for
`y_j` is its actual Syracuse orbit segment. The initial state is in the
top annular band and is `17 modulo 18`, with coefficient 2.

**Why other sources do not cancel this coefficient.** The largest initial
annular state is at most `144N-1`. The all-valuation-one map
`T(x)=(3x+1)/2` has `T^j(x)=lambda^j(x+1)-1`. If at least one of the first
`j` valuations is at least 2, replace all other steps by `T` and that one
by `U=T/2`. This gives an upper bound for the actual endpoint. Moving `U`
to the beginning increases that endpoint: `TU>UT`, with difference 1/4,
and all subsequent maps are increasing. Therefore every such endpoint
`z` satisfies

\[
z+1\le\lambda^j(72N+1/3).
\]

Our selected point has

\[
y_j+1=\lambda^j(x+1)>\lambda^j(72N+1),
\]

so any contribution arriving there has only valuations 1. This branch is
injective and its unique source is `x`, proving `(P^j A_N)(y_j)=2`.

Finally `y_j=3 modulo 4` is already a root. The entire transported support
is at most `144N*lambda^j-1`. Its next `F`-point satisfies

\[
F(y_j)=4\lambda^j(x+1)-3
       >288N\lambda^j-3
       >144N\lambda^j-1.
\]

Thus no other member of its `F`-chain is in the transported support.
Root collapse leaves its coefficient exactly 2. \(\square\)

### Consequences and exact scope

1. `C_(N,t)>0` for every `0<=t<=floor(log2(4N))`. Consequently a word in
   `P,R` with at most that many transports cannot make `A_N` nonpositive.
   There is no fixed finite number of `P/R` operations that completes
   every annulus, including along any of the five required rays.
2. There is no uniform linear height bound on this residual evolution.
   For `N=a*2^b`, choose the actual top source `x=144N-1`. It belongs to
   `X_(N,b+2)`, and after `b+2` transports it is still a positive atom of
   coefficient 2 at

   \[
   y_{b+2}=324a\,3^b-1.
   \]
   Its ratio to `N` is `324*(3/2)^b-1/N`, which is unbounded. This applies
   to each fixed mantissa `a` in the five-ray reduction. It refutes closure
   in `state<=K*N` for a constant `K` under literal `P/R` evolution.
3. These statements give a lower bound on the time and height needed by
   this particular process. They do not prove that positive plateaus
   persist forever, nor do they exclude a bound that grows with `N`.
   They also do not rule out cross-time current cancellations: those can
   remove a source using a future intersection while another transported
   coefficient remains positive at a particular synchronous time.

## 3. Two exact failed contraction claims on a required ray

The stronger annular claim

\[
\|P^{t+1}A_N\|_1\le(19/22)\|P^tA_N\|_1
\quad\hbox{for all }t,N
\]

already fails at `N=96`, `t=2`:

\[
\|A_{96}\|_1=4752,\quad
\|PA_{96}\|_1=4103,\quad
\|P^2A_{96}\|_1=3533,\quad
\|P^3A_{96}\|_1=3124.
\]

Here `22*3124=68728>67127=19*3533`. This is compatible with the proved
one-pass annular estimate; the third input is no longer an annulus.

Even replacing `19/22` by an arbitrary constant strictly less than 1 does
not yield a one-step norm decrease on every unresolved reachable
residual. Let `mu=RP^78 A_96`. Its full nonzero row list is

| State | Coefficient |
|---:|---:|
|17|-1|
|81|2|
|433|2|
|479|-1|
|577|-3|
|607|-1|
|1079|-1|
|1367|-1|
|2051|-1|

Both `mu` and `RP mu=RP^79 A_96` have norm 13 and positive mass 4. Thus
this is a genuine positive plateau, not a tail that is already everywhere
nonpositive. Equivalently `P^79 A_96` and `P^80 A_96` have the same norm 13
and positive mass 4. The receipt stores all four exact measures. This
finite plateau does not rule out eventual progress or a longer-block
estimate with an explicitly proved bound.

## 4. Reproduction and reusable bounded current

Run from the repository root:

```sh
python3 experiments/residual_progress/transport/check_root_transport.py
```

The script checks the conjugacy arithmetic on odd states through 4097;
the operator identities and surviving atom formulas at `N=8,96,168,384`
through depth 12; and the exact `N=96` counterexamples through depth 80.
It compares with `root_transport_audit.json`. Use `--write-receipt` only
to intentionally regenerate that receipt. Every transport loop is capped.

The reusable function `collapsed_transport_current(measure, steps)`
returns the full pair `(J,Z)` with

\[
J=\sum_{j=0}^{\text{steps}-1}P^j\mu
       +P^{\text{steps}}\mu-RP^{\text{steps}}\mu,
\qquad Z=RP^{\text{steps}}\mu,
\qquad \mu=(I-P)J+Z.
\]

The last difference has zero pushforward, so the identity telescopes
exactly. The function retains every positive residual coefficient and
verifies the divergence. Supplying a finite cap is not a termination proof.

The remaining research obligation is unchanged: supply an additional
arithmetic mechanism that forces finite progress of every positive
component, with the exact residual and boundary contributions retained.
