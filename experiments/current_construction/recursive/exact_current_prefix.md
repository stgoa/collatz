# Exact prefix certificates and a sparse equivalent criterion

Date: 2026-10-17. Status: written elementary proof, scoped to **exact** finite
signed currents. No novelty or universal certificate-construction claim.
The packet definitions, source measure, fixed core, and absorption convention
are those of the current main proof note.

## A finite prefix means convergence of a finite seed interval

For each integer `M>=8`, the following are equivalent:

1. Every positive odd seed `r<=floor((3M+1)/2)` reaches 1.
2. For every integer `8<=N<=M`, `PiR_N` has a finite exact current.
3. For every integer `8<=N<=M` with `N modulo 8` in `{2,5}`, `PiR_N`
   has a finite exact current.

The interval is an exact finite statement, not a claim that existence can
be decided without convergence information. In particular, the implication
from 3 can be vacuous at tiny `M`; the required finite seed interval there
is part of the directly terminating base core below.

### Proof

Let `e(r)` indicate nontermination. It is invariant under `S`, with `e(1)=0`.
Every finite signed divergence has zero pairing with `e`. The fixed core
`{5,7,11,13}` has zero pairing with `e`, so

\[
\langle e,\Pi^{\rm R}_N\rangle=\langle e,\nu_N\rangle.
\]

Statement 1 implies 2: all sources in `nu_N` lie below
`floor((3M+1)/2)`, hence they and their packet endpoints terminate. Summing
the finitely many packet pushes through their last absorption time gives
an exact finite current. Statement 2 immediately implies 3.

For 3 implies 1, suppose a nonterminating odd seed exists in the named
interval and let `r` be the least nonterminating positive odd seed. The
odd seeds through 15 terminate by direct finite computation, so `r>=17`.
Minimality gives two elementary restrictions:

- If `r=1 modulo 4`, its first valuation is at least 2 and `S(r)<r`, a
  contradiction. Thus `r=3 modulo 4`.
- If `r=2 modulo 3`, the odd integer `x=(2r-1)/3` is positive and smaller
  than `r`, and `S(x)=r`, another contradiction.

It follows that `r=12m+3` or `r=12m+7`. Set

\[
N=\left\lceil\frac{2r-1}{3}\right\rceil.
\]

For the two residue cases this is respectively `N=8m+2` or `N=8m+5`.
Therefore `N modulo 8` is in `{2,5}`, `8<=N<=M`, and its upper cutoff
`n_1(N)` is `r` or `r+1`. The latter extra point is even. The second
component cutoff `n_2(N)` is strictly smaller than `r`. All other odd
source states therefore terminate. As `r` is not 2 modulo 3, its one
remaining source coefficient is -1, yielding

\[
\langle e,\nu_N\rangle=-1.
\]

An exact current for `PiR_N` would instead make this pairing zero.
This contradiction proves 1 and completes the equivalence.

## Consequences and scope

Taking all `M`, Collatz is equivalent to the existence of exact finite
currents only at integer cutoffs `N>=8` with `N modulo 8` in `{2,5}`.
This thins the exact-certificate target to one quarter of the cutoffs.
It does not provide any of those currents.

The proof also locates the remaining arithmetic obligation sharply:
at the cutoff that first isolates a least exceptional seed, the packet's
unknown component has coefficient -1. A finite exact current excludes
that seed because the pairing must vanish. An everywhere nonpositive
residual permits a negative pairing; consequently the same proof does
**not** establish the sparse criterion for incomplete currents.

No trajectory scan or search is needed for these implications beyond the
fixed base seeds through 15 already checked by the repository's existing
verification suite. The argument does not claim that finite exact currents
at a single large cutoff imply all smaller seeds terminate.
