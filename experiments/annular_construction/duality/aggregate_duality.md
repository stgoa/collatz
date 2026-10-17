# Aggregate annular currents: exact duals and information lost by compression

17 October 2026. Written proofs and exact finite certificates. This note does
not prove a universal positive-integer current construction or an unbounded
aggregate exposure depth. No novelty claim is made.

The positive annulus `A_N`, for `8 | N`, is the six-band signed measure from
`experiments/current_construction/recursive/annular_recursion.md`. Put
`Q=9N/4`; its support lies in `(Q,64Q)`, its total mass is zero, and its
coefficients in band `j` depend on the six residues `1,5,7,11,13,17 mod18`.
All ordinary Collatz statements below use the odd-only clock and absorption
at positive 1. Section 5 explicitly changes to negative integers for a
counterexample to an overgeneralized method.

## 1. The finite graph supplies an exact dual certificate

Let `mu` be a finite signed integer source measure, and expose a finite set
`E` of actual forward arrows. Include their endpoints, every source, and
the absorber in the vertex set. A current restricted to `E` can use arbitrary
signed coefficients on its arrows. The question is whether

\[
\mu=(I-P)J+\zeta,\qquad \operatorname{supp}J\subseteq E,
\quad\zeta\le0.
\]

**Finite duality.** Such a current exists exactly when every connected
component of the exposed undirected graph not containing 1 has nonpositive
total source mass. If component `C` has positive mass, its indicator `q=1_C`
is a finite dual obstruction:

\[
q\ge0,\qquad q(1)=0,\qquad q(x)=q(Sx)\text{ on every exposed arrow},
\qquad\langle q,\mu\rangle>0.
\]

Pairing a proposed identity with `q` yields a contradiction. Conversely,
when all component masses have the required sign, route source coefficients
along undirected spanning trees to an anchor of each component, using signed
flow when traversing an arrow backwards. Choose 1 as the absorbing component's
anchor. The resulting residual is the component mass at each other anchor.
This is an integral construction. It is the elementary graph version of the
finite linear-programming duality; no numerical optimizer is required.

The dual is **restricted to the exposed graph**. It does not prove that a
current using unexposed arrows is impossible. To prove global impossibility,
the function must be invariant on the entire relevant deterministic graph.

This gives an exact target for an adaptive constructor: eliminate every
positive component witness by exposing a connection to sufficient negative
source mass or to the absorber. Merely shrinking the number of unresolved
components is insufficient if a surviving component has positive mass.

## 2. The missing term in a constructive scale argument is an exact boundary flux

For an integer `t`, let `U_t` count the positive odd states `1<x<=t`, and
let `F_t=U_(64t)-U_t`. Fix `8|N`, so all the arguments below are integers.
Define

\[
\begin{split}
V_N&=\nu_{64N}-\nu_N,\\
K_N&=V_N+3(F_N-F_{N/4}),\\
D_N&=3F_N-3F_{N/4}-F_{3N/2}-F_{3N/4}.
\end{split}
\]

**Exact identity.** With the original source multiplicities and all integer
cutoffs retained,

\[
\boxed{D_N=A_N+(I-P)K_N.}                              \tag{1}
\]

**Proof.** Partition odd sources by first valuation. Valuation 1 maps
bijectively to residue 5 modulo 6 up to `3N/2`; valuation 2 maps to residue
1 modulo 6, excluding the absorber, up to `3N/4`. Sources with valuation
at least 3 are `4z+1`, with odd `z<=N/4`, and have the same successor as
`z`. The exceptional `z=1`, source 5, contributes nothing after absorption.
The floor in `(N-1)/4` causes no difference because `N/4` is even.
Consequently, if `T_r(t)` counts the odd nonabsorbing states in the stated
residue class,

\[
P(U_N-U_{N/4})=T_5(3N/2)+T_1(3N/4).
\]

The definition of the two-component source therefore gives

\[
\nu_N=3P(U_N-U_{N/4})-U_{3N/2}-U_{3N/4}.
\]

Subtract this identity at `N` from the one at `64N`:

\[
V_N=3P(F_N-F_{N/4})-F_{3N/2}-F_{3N/4}.
\]

Hence `D_N=V_N+3(I-P)(F_N-F_(N/4))`. The fixed core cancels under the
64-fold scale change, so `A_N=PV_N`. Substitution proves equation (1),
including its sign and the factor 3. No asymptotic cutoff replacement occurs.

For a finite exposed-component indicator `q`, with `q(1)=0`, pairing
equation (1) gives

\[
\langle q,D_N\rangle
=\langle q,A_N\rangle+\mathcal F_N(q),\qquad
\mathcal F_N(q)=\sum_x K_N(x)\bigl(q(x)-q(Sx)\bigr).     \tag{2}
\]

On every exposed arrow, `q(x)=q(Sx)`. Thus the flux in equation (2) comes
entirely from **unexposed rows of the explicit finite measure `K_N`**.
For a globally invariant indicator, such as the nonhalting indicator, the
flux vanishes. Finite graph duals need not have that property. Equation (2)
is the precise missing term when a scalar cutoff comparison is applied to
an unresolved finite component.

**A positive component with nonzero flux.** Expose 27 steps from every
source of the actual positive annulus `A_96`. Let `q` indicate the component
containing 1819. It has 83 vertices and 31 source atoms; both complete lists
are saved in `duality_audit.json`. Its source pairing is 17. The exact scale
identity gives

\[
\langle q,D_{96}\rangle=10=17-7,
\qquad\mathcal F_{96}(q)=-7.
\]

There are exactly 11 nonzero flux rows. In each, `q(x)-q(Sx)=-1`:

| `K_96(x)` | Row states `x` |
|---:|---|
| 1 | 2553, 3639, 3831, 4095, 4311, 4539 |
| 2 | 4851, 6057 |
| -1 | 6375, 9079, 9087 |

This is an exact counterexample to omitting the flux for a finite-component
indicator. It is on positive integers and uses the actual annular measure.

**Zeroing this flux is still insufficient.** Add every arrow whose tail
has nonzero coefficient in `K_96` to this depth-27 graph. Every component
indicator of the enlarged graph now has zero `K_96` flux. Nevertheless,
the graph still has one positive component, of mass 17. Its scale pairing
has changed to 17 along with its enlarged vertex set. Thus this finite
source-scale closure does not establish a current with nonpositive residual.
One more ordinary exposure level does resolve the example, as recorded below.

A possible constructor can use `K_N` to expose arithmetic boundary rows
instead of expanding every orbit uniformly. The obligation is then to prove
that the resulting component extensions eventually reduce positive mass.
Simply dropping the flux, or making it zero at one cutoff while ignoring
the change of the component indicator, does not prove that progress.

## 3. A valid integer progress potential has uncontrolled plateaus

For a nested sequence of exposed graphs define

\[
\Phi(E)=\sum_{C:\,1\notin C}\max\left(\sum_{x\in C}\mu(x),0\right).
\]

**Proposition.** `Phi(E)` is a nonnegative integer. It never increases when
arrows are added, and it is zero exactly when the exposed graph supports a
current with nonpositive residual.

**Proof.** A new arrow either stays in one component or merges two components.
For real `u,v`, `max(u+v,0)<=max(u,0)+max(v,0)`. If a component merges into
the absorbing component, its formerly counted positive mass disappears.
These observations prove monotonicity, and Section 1 proves the zero criterion.

For the actual positive annulus `A_96`, the exact finite experiment gives
`Phi(E_0)=2376`. Here `E_d` exposes the first `d` steps from every original
nonzero source atom, retaining all historical intersections. The potential
is 17 at every depth from 20 through 27. At depth 27 there is one positive
component, containing 31 source atoms, and its indicator pairs to 17.
It follows that **no** current restricted to that entire exposed graph has
an everywhere nonpositive residual. At depth 28 the potential becomes zero,
so the finite graph does support such a current.

This is a useful monotone measure of progress, but not a termination proof.
It can decrease strictly only finitely many times and still stay positive
forever on a plateau. A constructor needs an arithmetic argument that every
positive plateau ends after finitely many new exposures. A capped scan cannot
establish that statement for all five-ray cutoffs.

The five-ray maximum principle does not supply this missing strict decrease.
Its comparison is in the cutoff index, and its hypothesis already controls
the pairing with the nonhalting indicator. At a finite graph stage there
are many separate component-indicator duals, with unknown future mergers.
Contracting a scalar count across cutoffs gives no bound on the duration of
their plateaus. A proposed constructive lifting must explicitly control those
duals or exhibit the connections which invalidate them.

## 4. Every fixed binary-residue view eventually sees the annulus as zero

This is an aggregate identity for the actual six-band measures, not an
argument about isolated triples.

**Theorem.** Fix `K>=1`. If `2^(K+2) | N`, then in each of the six bands
separately,

\[
\sum_{\substack{y\text{ in band }j\\y=r\pmod{2^K}}} A_N(y)=0,
\qquad
\sum_{\substack{y\text{ in band }j\\y=r\pmod{3\cdot2^K}}} A_N(y)=0
\]

for every residue `r`. In particular, the source projects to the zero measure
on either finite quotient.

**Proof.** Each band has length `2^j Q`, and its endpoints are multiples of
`9*2^K`, because `Q=9N/4`. In the annular table, every row sums to zero
separately on the three residues `1,7,13 mod18` and the three residues
`5,11,17 mod18`; the coefficients at multiples of 3 are zero.

The common period of the coefficient pattern and a residue condition modulo
`2^K` is `9*2^K`. Within that period a fixed odd binary residue visits every
odd residue modulo 18 equally once, so the coefficients sum to zero. For
the modulus `3*2^K`, a fixed odd residue instead visits the three classes
in its fixed residue class modulo 6, whose coefficient sum is again zero.
Every band contains an integral number of these common periods. Its endpoints
are even and are outside the odd source support. This proves both statements.

**Exact scope.** Any test function that depends only on the band index and
the residue modulo `2^K` or `3*2^K` pairs to zero with the annulus. For every
fixed `K`, all sufficiently large cutoffs on each of the five rays satisfy
the divisibility hypothesis. A finite-state compression retaining only these
data therefore sees the same source vector as it sees for the empty measure.
It cannot by itself certify matching of the actual integer states.

This is an information-loss theorem for these specific quotients. It does
not rule out finite-state methods carrying additional information, such as
residues modulo 9, exact offsets, carry data, symbolic parameters, or checked
integer lifting identities. In particular, the existing coefficient table
already retains information modulo 18 that these coarser projections lose.

It also limits a proposed negative-cycle shadowing proof. A bounded-precision
periodic shadow indicator, even with a separate value in each band, has zero
annular pairing and cannot be a positive dual witness. To prove that aggregate
exposure depths are unbounded, a shadowing argument must additionally control
all extra source atoms in the actual exposed component and produce a positive
total after their cancellations. The known isolated-triple obstruction does
not perform that step. **No unbounded aggregate-depth result is proved here.**

## 5. A fully certified counterexample to replacing component bounds by scalar bounds

This counterexample is deliberately outside the positive-integer Collatz
domain. It tests the logic of methods based only on band balance, scalar work,
or the coarser finite projections.

Reflect the positive source annulus `A_96` onto negative states:

\[
\widetilde A_{96}(-y)=A_{96}(y),\qquad y>0.
\]

Use the same exact odd Syracuse formula on negative odd integers; positive
1 remains the only absorber. Negative odd states stay negative, so every
source has infinite hitting time of 1. Since the source has total mass zero,

\[
H_L(\widetilde A_{96})=0\qquad\text{for every }L\ge0.
\]

The projections modulo `2,4,8,6,12,24` also vanish, since reflection permutes
residue classes and Section 4 applies at `N=96`.

Nevertheless, all 3204 sources can be followed by finite, explicitly checked
paths into three distinct negative cycles. Their signed component masses are:

| Cycle | Number of source atoms | Signed source mass |
|---|---:|---:|
| `-1 -> -1` | 1054 | -20 |
| `-5 -> -7 -> -5` | 1027 | -73 |
| `-17 -> -25 -> -37 -> -55 -> -41 -> -61 -> -91 -> -17` | 1123 | **93** |

Every path reaches its chosen cycle anchor within 86 steps. The persisted
5868-row signed current and three-atom residual verify the exact identity

\[
\widetilde A_{96}=(I-P)J-20\delta_{-1}-73\delta_{-5}+93\delta_{-17}.
\]

The indicator of the basin of the seven-state cycle is globally invariant,
zero at the absorber, and pairs to 93 with the source. Thus **no finite exact
current and no finite current with an everywhere nonpositive residual exists**
for this reflected measure, including currents with arbitrary auxiliary states.

This is a rigorous failure of the inference “balanced bands and bounded
scalar work imply a current.” It is not a counterexample to the original
positive annulus or to the five-ray theorem. Its purpose is to identify what
a successful positive-integer argument must use beyond those scalar facts:
the distribution of source signs among actual orbit components.

## 6. Reproduction and the next constructive obligation

Run without Python optimization:

```sh
python3 experiments/annular_construction/duality/check_duality.py
```

The command checks the saved `duality_audit.json`, the current and residual
CSV files, seven exact annular source-scale identities, all eight materialized
modular-projection cases `K=1,...,8`, the positive `A_96` exposure potential
through depth 28, every recorded finite-component flux, the depth-27 closure
example, and the reflected source classification. It also independently
checks the arithmetic agent's `19/22` collapse formula at nine cutoffs by
grouping actual `F(x)=4x+1` chains and separately pushing the source. These
checks agree with the proof, including absorption of the root-1 class and
the `2N` surviving positive outer atoms. Use `--write-receipt` to regenerate
these exact artifacts.
The finite graph search has a depth cap of 128; negative-source classification
has a 1000-step cap and cycle detection. An unresolved cap is never interpreted
as nonexistence.

The constructor's next concrete obligation is now a component progress lemma:
given a positive exposed component of an annular source on one of the 30
sequences, prove that a finite arithmetic extension of the graph either
reduces its positive mass through a negative merger or connects it to the
absorber. The integer potential then bounds the number of strict decreases.
The required proof is the finite end of every positive plateau; none of the
scalar contraction, source-table balance, or fixed-residue identities above
supplies it.
