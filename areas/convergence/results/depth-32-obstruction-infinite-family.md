---
id: depth-32-obstruction-infinite-family
kind: result
title: The complete depth-32 obstruction lifts to every cutoff N = 96 2^24 q with q = 1 mod 3^22
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1; A_N the six-band annulus; G_32(N) the first 32 arrows exposed from every
  nonzero source. For every integer q >= 1 with q = 1 mod 3^22 and N = 96 2^24 q, the component of 144N - 1 in
  the entire G_32(N) is exactly C_N = (3^j 64N/2^j - 1 : 0 <= j <= 34), joined by consecutive arrows, with only
  the sources A_N(64N-1) = -2, A_N(96N-1) = 2, A_N(144N-1) = 2; so no current on G_32(N) represents A_N with
  nonpositive residual. This includes N = 12 2^(27 + 20920706406 k), k >= 0, on a required ray. The proof
  lifts every one of the 9171 inverse decisions as affine functions of q (42487 exact inequalities, maximal
  denominator 3^20). The exposure depth stays fixed at 32: depth 33 or larger is not excluded here.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [depth-32-aggregate-exposure-obstruction]
evidence:
  - "unbounded-exposure-depth-necessary/check_symbolic_lift.py, unbounded-exposure-depth-necessary/symbolic_component_lift.py, unbounded-exposure-depth-necessary/symbolic_lift_audit.json: the symbolic lift prove_chain_lift(96*2**24, 32) and its checker, which regenerates every affine inequality, compares the receipt (with SHA-256 digests of the query and comparison tables), reruns the integer oracle at q = 1, 1 + 3^22 and 1 + 2*3^22, checks 2^(2*3^21) = 1 mod 3^22 by modular exponentiation, and runs a depth-2 instance at N_0 = 384 with a numerical dyadic sample. It passes at its new path and is listed as a certificate of unbounded-exposure-depth-necessary, whose folder holds all the template scripts"
aliases: [R13-c]
tags: [convergence, packet-currents, annular, exposure-depth, symbolic-lift, obstruction]
---

# The complete depth-32 obstruction lifts to every cutoff N = 96 2^24 q with q = 1 mod 3^22

## Statement

Put `N_0 = 96·2^24 = 12·2^27` and `M = 3^22 = 31 381 059 609`. For every integer `q ≥ 1` with `q ≡ 1 (mod M)` and `N = N_0·q`, the component of `144N − 1` in the entire historical exposure graph `G_32(N)` (odd-only clock, absorbing at 1; the definitions of [`depth-32-aggregate-exposure-obstruction`](depth-32-aggregate-exposure-obstruction.md)) is exactly

```
C_N = { 3^j·64N/2^j − 1 : 0 ≤ j ≤ 34 },
```

with arrows between consecutive states and the only source coefficients `A_N(64N − 1) = −2`, `A_N(96N − 1) = 2`, `A_N(144N − 1) = 2`. So `A_N(C_N) = 2`, `1 ∉ C_N`, and no current on any arrows of `G_32(N)` gives `A_N = (I − P)J + ζ` with `ζ ≤ 0`. The family contains the progression `N = N_0(1 + 3^22·k)` and the required-ray subfamily `N = 12·2^(27 + 20 920 706 406·k)`, `k ≥ 0`, because `2^(2·3^21) ≡ 1 (mod 3^22)`.

The depth is still fixed at 32; this does not exclude a universal catalogue of depth 33 or more, and it constructs no residual family closed under recursive template packing. It is not a Collatz counterexample or a universal current construction.

## Proof

The legacy note "An infinite family of complete aggregate obstructions at depth 32" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

Date: 2026-10-17. Status: written finite-to-infinite argument, exact symbolic
arithmetic certificate, and independent numeric comparisons. This strengthens
the earlier single-cutoff obstruction to an infinite family. It does not
establish obstructions at arbitrarily large depths, a Collatz counterexample,
or a universal current construction. No novelty claim is made.

**Subsequent result:** the separate [unbounded-depth theorem](unbounded-exposure-depth-necessary/README.md)
now proves an aggregate obstruction at every fixed depth, using a different
ternary phase and an inverse-history invariant. The fixed-depth proof below
is retained as independently checked evidence and as the route to that result.

The source is the actual annular measure `A_N`, with `8|N`. The graph
`G_D(N)` includes the first `D` arrows from **every** nonzero annular source,
with absorption at 1. Definitions, the inverse oracle's completeness proof,
and the original finite witness are in [AGGREGATE_EXPOSURE.md](depth-32-aggregate-exposure-obstruction.md).
All original witnesses and their checker remain unchanged.

### 1. The resulting theorem

Put

\[
N_0=96\cdot2^{24}=12\cdot2^{27},\qquad M=3^{22}=31\,381\,059\,609.
\]

**Theorem.** For every integer `q>=1` satisfying `q=1 modulo M`, let
`N=N_0 q`. The component of `144N-1` in the entire historical exposure
graph `G_32(N)` is exactly

\[
C_N=\left\{\frac{3^j64N}{2^j}-1:0\le j\le34\right\}.
\]

Its arrows join consecutive displayed states. Its only annular source
coefficients are

\[
A_N(64N-1)=-2,\qquad A_N(96N-1)=2,\qquad A_N(144N-1)=2.
\]

Thus `A_N(C_N)=2`, and the component does not contain 1. For every such
`N`, no current supported on **any arrows of the whole graph G_32(N)** can
give `A_N=(I-P)J+zeta` with `zeta<=0`.

The theorem includes the arithmetic progression `N=N_0(1+3^22 k)`, `k>=0`.
It also includes an infinite subfamily of the required dyadic ray:

\[
\boxed{\quad N=12\cdot2^{27+20\,920\,706\,406\,k},\qquad k\ge0.\quad}
\]

Indeed `2^(2*3^21)=1 modulo 3^22`. One elementary proof starts from
`4=1 modulo 3` and cubes repeatedly: if `z=1 modulo 3^r`, then
`z^3=1 modulo 3^(r+1)`. Taking powers `k` preserves the congruence.
No enormous integer in the boxed family needs to be materialized for the
proof.

The same dual-component argument as before excludes complete packed
source covers by common-tail trees whose source-to-anchor depth is at
most 32. It permits larger depths, new residual sources, and unbounded
recursive constructions.

### 2. Lifting the complete inverse computation

We verify the whole component closure, including the absence of all extra
incoming exposed arrows. Lifting the increasing chain alone would not
suffice.

Use a real symbolic parameter `q>=1` for inequalities, and later restrict
to integers in the stated congruence class. Every state in the finite
inverse computation is represented by

\[
x(q)=a q+b,\qquad a,b\in\mathbb Z[1/3].
\]

The initial chain slopes are the positive even integers
`a_j=3^j64N_0/2^j`, `0<=j<=34`, and all their intercepts are `-1`.
The denominator cancellation follows from `64N_0=3*2^35`.

An inverse branch transforms these affine states by

\[
(a,b)\longmapsto\left(\frac{2^v a}{3},\frac{2^v b-1}{3}\right),
\qquad v\ge1.
\]

Every resulting slope remains positive and has an even numerator in
lowest terms. Every denominator remains a power of 3. Positivity at
`q=1`, checked for every queried state, therefore implies positivity for
all `q>=1`.

#### Congruences preserve all exact branch and source decisions

For a queried state with denominator dividing `3^h`, suppose
`x(1)` is an odd integer and `q=1 modulo 3^(h+2)`. Then

\[
x(q)-x(1)=a(q-1)\in18\mathbb Z.
\]

The power of 3 supplies divisibility by 9 after clearing the denominator;
the even numerator supplies the extra factor 2. Thus the state stays an
odd integer with the same full residue modulo 18. This preserves:

- the allowed parity of every inverse valuation `v`, determined modulo 3;
- the coefficient within each annular band, determined modulo 18;
- the exclusion of all inverse predecessors when the target is divisible
  by 3.

The verifier finds maximal denominator `3^20`. Consequently the single
condition `q=1 modulo 3^22` preserves every such decision. It requires no
additional power-of-two congruence on `q`: even values of `q` are allowed.

#### All support and height decisions persist on the entire half-line

Because `144N_0` is divisible by `2^33`, all relevant height bounds are
exactly affine:

\[
B_r(q)=\frac{3^r144N_0}{2^r}q-1,\qquad0\le r\le32.
\]

Annular band boundaries are also linear functions of `q`. Every comparison
in the oracle can therefore be written as `f(q)>=0` or `f(q)>0`, with
`f(q)=u q+v` rational affine. The checker verifies `u>=0` and the required
weak or strict inequality at `q=1`. Since

\[
f(q)=f(1)+u(q-1),
\]

this proves the same comparison for every real `q>=1`.

The checks include source-band lower and upper boundaries, exclusion
below or above the support, the reachability height cap, every admitted
inverse predecessor, the **first excluded** inverse predecessor, and
strict positivity above the absorber. Subsequent inverse valuations in
the same parity class increase `2^v` by a factor of 4. Positivity of the
target state therefore proves that they too exceed the bound. No incoming
branch is dropped because it was inconvenient to evaluate.

#### Recursive decisions and the final closure

Use the exact recurrence `Reach(x,r)` from the earlier note. A true
decision may stop at a nonzero annular source or at one already proved
true predecessor. A false decision must exhaust all bounded predecessors,
unless a proved height exclusion or zero remaining depth already rules
out all routes. Induction on `r` proves that every stored decision is
correct simultaneously for the whole parameter family.

For each of the 35 proposed component states, the verifier then proves:

1. The outgoing arrow belongs to exposure precisely at indices `j<34`.
2. For these indices, `3x_j(q)+1=2x_(j+1)(q)` and the next state is odd;
   the valuation is therefore exactly 1.
3. The incoming exposed predecessors are precisely `x_(j-1)(q)` for
   `j>=1`, and none for `j=0`.
4. The annular source coefficients are exactly `(-2,2,2,0,...,0)`.

These statements give the **complete** graph component, not a subgraph.
The finite component criterion then proves the theorem.

### 3. Exact certificate and its audit

The symbolic certificate has:

| Quantity | Value |
|---|---:|
|Component vertices / arrows|35 / 34|
|Memoized affine reachability decisions|9,171|
|Verified affine inequalities|42,487|
|Comparisons with zero slope|96|
|Largest denominator power|`3^20`|
|Smallest positive comparison slope|10,737,418,240|
|Smallest positive comparison value at `q=1`|1|

All operations use Python integers and exact rational fractions. There
are no floating-point tolerances. The complete query and comparison
tables are reproducibly returned by
`symbolic_component_lift.prove_chain_lift(96*2**24,32)`. Their SHA-256
digests are stored alongside the exact receipt, so a changed proof trace
is detected by the default check.

Run from the repository root:

```sh
python3 experiments/residual_progress/templates/check_symbolic_lift.py
```

The checker regenerates every symbolic inequality and compares the saved
receipt. It also independently reruns the earlier integer inverse oracle
at `q=1`, `q=1+3^22` (even), and `q=1+2*3^22`, comparing the full nodes,
arrows, and source coefficients. The main dyadic congruence is checked
with modular exponentiation; its first nontrivial multiplier has over
twenty billion bits and is deliberately not allocated.

A separate depth-2 symbolic instance at `N_0=384` has `K=2`, with dyadic
period 6. Its nontrivial dyadic sample `q=64`, `N=24576`, is compared
numerically against the independent oracle. This smaller instance checks
the dyadic specialization without pretending to enumerate the enormous
main-family cutoff.

The symbolic generator has an explicit query cap. An unstable affine
decision or an exhausted cap rejects the proposed lift; it does not
establish nonexistence of another family. The successful main proof uses
a cap of 20,000 decisions.

### 4. Scope of this lift and subsequent progress

The exposure depth is still fixed at **32**. Increasing the parameter
produces arbitrarily large cutoffs and infinitely many required-ray
examples; it does not increase the proved depth. In particular, this
does not exclude a universal catalogue of depth 33 or another larger
fixed depth.

The later [unbounded-depth theorem](unbounded-exposure-depth-necessary/README.md) supplies a
new argument showing a suitable complete positive component for each `D`.
This does not follow merely from parameterizing the present symbolic
verifier by depth. No residual family closed under recursive template
packing is proved. The constructive target remains a finite current at
every required cutoff, with arbitrary finite complexity permitted.

## Certificates

This node has no folder of its own. Its finite certificate is [`check_symbolic_lift.py`](unbounded-exposure-depth-necessary/check_symbolic_lift.py) (about 1 s), listed under [`unbounded-exposure-depth-necessary`](unbounded-exposure-depth-necessary/README.md), whose folder holds every template script because they import the oracle from their own folder. It passes at its new path with its receipt unchanged. The command in the legacy text names `experiments/residual_progress/templates/`.

## Remarks

- Superseded in strength by [`unbounded-exposure-depth-necessary`](unbounded-exposure-depth-necessary/README.md), which proves an obstruction at every fixed depth with a different ternary phase; that theorem does not follow from parameterising this verifier by depth. This lift is kept as independently checked evidence and as the route to it.
- The same affine-decision verifier, with an added translation argument, proves the phase classes of [`short-delay-all-phase-obstruction`](short-delay-all-phase-obstruction/README.md).
- Novelty undetermined.

## History

- Migrated from `experiments/residual_progress/templates/INFINITE_COMPONENT_FAMILY.md` (legacy ID R13, its intermediate part; alias R13-c here) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). Legacy status: "written finite-to-infinite argument, exact symbolic arithmetic certificate, and independent numeric comparisons".
- Main lane (ChatGPT, Codex), 2026-10-17.
