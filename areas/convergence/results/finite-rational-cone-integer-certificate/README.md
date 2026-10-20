---
id: finite-rational-cone-integer-certificate
kind: result
title: A finite rational cone compiles supplied five-ray packet certificates into an exact integer absorption current
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1; U_t counts the odd states 1 < x <= t. (Integer-component lemma) If a
  finite signed integer measure mu satisfies mu = (I - P)J + Z with a finite rational current J and
  ||Z+||_1 < 1, the finite graph of the current arrows, the sources and 1 supports an integer current for mu
  with everywhere nonpositive residual; if mu >= 0, every source lies in the component of 1 and the graph
  supplies its actual paths to 1. (Conditional compiler) Enumerate the five rays as N_k = a_i 2^b, k = 5b + i,
  a in (12, 14, 16, 18, 21); with r = 35/27, lambda(r) = r^-10 + (r^3 + r^-2)/3 < 1, and the finite nonnegative
  inverse of I - A on a block I = (15, ..., K) gives exact rational weights. Conditional on supplied, checked
  finite currents Pi_(N_k) = (I - P)J_k + zeta_k with zeta_k <= 0 for every k in I, and on the known finite
  absorption of the lower boundary counting measures and of the fixed-core remainders eta_(N_k), if the exact
  upper boundary mass T is below 1 these finitely many inputs give a finite exact integer current for U_g
  (g the first grid cutoff >= m) and actual halting paths for every odd seed <= g. An explicit sufficient
  block has O(log m) cutoffs, the largest O(m^2.14682); for m = 97 the exact solve with B = 9 uses the 30
  starting cutoffs through 5376 and gives T = 31562113241597/46422343855805 < 1. The input certificates are
  not constructed; they may lie above the target scale, so using them in a decreasing induction would be
  circular.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [five-ray-current-criterion, right-aligned-fixed-core-remainder]
certificates: [check_cone_recompute.py, check_legacy_replay.py]
evidence:
  - "check_finite_cone.py, finite_cone_audit.json: the legacy checker (rational comparison constants, seven integer tail bounds, every transpose equation, rounded and unrounded measure coefficients, four full single-cutoff boundary identities (6) at N = 96, 112, 192, 5376, the strict-gap implication on 216000 finite integer cases, and the four cone plans). Fails at its new path: it loads experiments/packet_currents/right_aligned_packets.py relative to the repository root (now ../right-aligned-fixed-core-remainder/right_aligned_packets.py). Passed at be73a66 as experiments/residual_progress/duality/check_finite_cone.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "finite_cone.py: the legacy library finite_forcing_plan(m, B) returning the exact cone weights (runs without error but checks nothing on its own). check_cone_recompute.py imports it from this folder; the legacy compiler of actual-graph-current-compiler loads it by its old path ../duality/finite_cone.py"
aliases: [R11]
tags: [convergence, packet-currents, five-rays, finite-cone, integer-gap, conditional, constructive]
---

# A finite rational cone compiles supplied five-ray packet certificates into an exact integer absorption current

## Statement

Use the odd-only map `S`, absorbing at 1, its killed pushforward `P`, and the counting measures `U_t` of the odd states `1 < x ≤ t`. `Π_N` is the right-aligned packet and `η_N` its fixed-core remainder (support in `{5, 7, 11, 13}`) from [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md); `K_N = ν_N + 3(U_N − U_(N/4))`.

**Integer-component lemma (§1 below).** For a finite signed **integer** measure `μ` and a finite rational current with `μ = (I − P)J + Z`, `‖Z⁺‖₁ < 1`, the finite graph containing all current arrows, source states and 1 supports an integer current for `μ` with nonpositive residual. If `μ ≥ 0`, every nonzero source belongs to the component of 1 and the graph supplies its actual finite path to 1. The strict threshold and the integrality of `μ` are both essential.

**Finite compiler theorem (§4).** On the five-ray grid `N_k = a_i·2^b`, `k = 5b + i`, the rounded comparison has shifts `−10, +3, −2` with weights `1, 1/3, 1/3`, and `r = 35/27` gives `λ(r) = 162742333796706147551/162889462677744140625 < 1`. Fix the interior block `I = {15, …, K}`, `K = 5B − 1`, and solve `w = (I − A)^(−T) e_(k*)` exactly. Suppose supplied, checked finite rational or integer currents satisfy `Π_(N_k) = (I − P)J_k + ζ_k`, `ζ_k ≤ 0`, for `k ∈ I`, together with the known finite absorption currents of the lower boundary counting measures and of `η_(N_k)`. If the exact upper boundary mass `T` of (5) is below 1, these finitely many inputs construct a finite exact **integer** current for `U_g` and actual halting paths for every odd seed at most `g`.

**Size of the input block.** For a target `m`, an explicit sufficient block has `5(B − 3)` cutoffs, all `a_i·2^b` with `3 ≤ b < B`, the largest `21·2^(B−1) = O(m^(p/(p−1)))`, `p = 5 log₂(35/27) ≈ 1.87198`, `p/(p−1) ≈ 2.14682`. This bounds **which** input certificates suffice, not their size, cost, search time or existence. For `m = 97` (`g = 112`): the bound (2) selects `B = 10` (35 packets, mass `94871593415091/257308134588959`); the exact solve at `B = 9` uses the 30 starting cutoffs through 5376 with `T ≈ 0.6798906`; `B = 8` gives `T ≈ 1.2856977`, so that cone does not certify the target (not an impossibility result).

Scope: a written conditional construction. It does not construct its required packet inputs, prove Collatz, or claim novelty.

## Proof

The legacy note "A finite rational cone turns packet certificates into absorption paths" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

2026-10-17. **Written conditional construction and exact finite checks.**
This note does not construct its required input packet currents universally,
prove Collatz, or assert novelty. It makes the five-ray implication finite
and constructive, retaining every source-scale boundary term.

All states are positive odd integers. The Syracuse map is
`S(x)=(3x+1)/2^v2(3x+1)`; mass at 1 is absorbed. Let `U_t` count the states
`1<x<=t`. Currents may initially have rational coefficients. Their source
measure will be integral when the rounding lemma is invoked.

### 1. Less than one unit of positive residual can be rounded away

**Integer-component lemma.** Let `mu` be a finite signed **integer** measure.
Suppose a finite rational current satisfies

\[
\mu=(I-P)J+Z,\qquad \|Z^+\|_1<1.
\]

Then the finite graph containing all current arrows, source states, and 1
supports an **integer** current for `mu` with nonpositive residual. If
`mu>=0`, every nonzero source belongs to the component containing 1, and
the graph supplies its actual finite path to 1 and an exact integer current.

**Proof.** In each nonabsorbing weak component C, cancellation of the
current divergence gives

\[
\sum_C\mu=\sum_C Z\le\|Z^+\|_1<1.
\]

The left side is an integer, hence at most zero. Route integer source
coefficients along an undirected spanning tree to one anchor per component;
use signed coefficients when traversing an arrow backwards. All unabsorbed
anchor masses are nonpositive. When `mu>=0`, no source can belong to a
nonabsorbing component. A finite functional graph component containing the
sink 1 has no other sink or directed cycle: every vertex follows its unique
outgoing arrows to 1. These actual paths give an exact nonnegative current
for `mu`. QED.

The strict threshold is essential: in a general functional graph, a positive
unit source at a nonabsorbing fixed point has residual mass 1 and no
certificate. No positive Syracuse fixed point is supplied by this example.
Integrality of `mu` is
also essential. This lemma does **not** authorize discarding a small positive
integer residual in the all-horizon work argument. Instead it uses a
rational identity and an integer obstruction on its entire finite graph.

### 2. An exact rational comparison for the five rays

Let `(a_0,...,a_4)=(12,14,16,18,21)` and enumerate the grid by

\[
N_k=a_i2^b,\qquad k=5b+i,\qquad k\ge15.
\]

The three rounded targets in the existing five-ray proof are precisely
`N_(k-10)`, `N_(k+3)`, and `N_(k-2)`. The first is `N_k/4`; the second is
at least `3N_k/2`, and the third is half the second, hence at least `3N_k/4`.
Use the same definition for the finitely many lower indices 5 through 14;
their cutoffs are at most 84. Their counting measures have known finite
absorption, verified in the repository's finite base check.

For **any** rational `r>1` satisfying

\[
\lambda(r)=r^{-10}+\tfrac13(r^3+r^{-2})<1,
\]

the weight `f_k=r^k` is strictly contracted by this comparison. A convenient
choice, stronger in growth than the previous `2^(k/3)`, is

\[
r=\frac{35}{27},\qquad
\lambda(r)=\frac{162742333796706147551}{162889462677744140625}<1.
\]

All comparisons are rational. Also `r^5>2` and `a_i/r^i<=12` for every i.
Thus, for an arbitrary indicator q with `q(1)=0`, without any assumption
of global invariance,

\[
\frac{\langle q,U_{N_k}\rangle}{r^k}
\le \frac{N_k}{2r^k}
\le 6\left(\frac2{r^5}\right)^b.                 \tag{1}
\]

For a target positive integer m, let `k_*` be the first `k>=15` with
`g=N_k>=m`. Choose an integer `B>=4`, with `k_*<5B`, such that

\[
6r^{k_*}\left(\frac2{r^5}\right)^B<1.             \tag{2}
\]

The script chooses the first such B by exact rational comparisons. The
required packet cutoffs are all `N_k`, `15<=k<=5B-1`, or equivalently all
five rays with `3<=b<B`. Their number is `5(B-3)` and their maximum is
`21*2^(B-1)`. With `p=5 log_2(35/27)`, this ceiling is
`O(m^(p/(p-1)))`, where `p≈1.87198` and `p/(p-1)≈2.14682`. This is an
upper bound on **which input certificates suffice**, not on their size,
cost, search time, or existence.

### 3. A finite positive inverse gives explicit rational weights

Fix the interior index set `I={15,...,K}`, where `K=5B-1`. Define the finite
nonnegative matrix A by putting weights `1,1/3,1/3` from row k to columns
`k-10,k+3,k-2`, respectively, when the column lies in I. All omitted terms
are boundary terms. Since `Af<=lambda(r) f` on I, the weighted sup norm
of A is less than one. Therefore

\[
(I-A)^{-1}=\sum_{j\ge0}A^j
\]

exists and is nonnegative. This argument proves positivity; the algorithm
computes the finite rational inverse action by exact Gaussian elimination,
not by summing infinitely many terms. Define

\[
w=(I-A)^{-T}e_{k_*}.                              \tag{3}
\]

Then every `w_k>=0` is rational. For each omitted target ordinal ell,
let `c_ell` be the sum of the incoming `w_k` times its transition coefficient.
Lower boundary targets have `ell<15`; upper ones are among `K+1,K+2,K+3`.

Define the rounded scale measure

\[
\widetilde D_k=3U_{N_k}-3U_{N_{k-10}}
                  -U_{N_{k+3}}-U_{N_{k-2}}.
\]

Equation (3) is exactly the finite measure identity

\[
U_g=\sum_{k\in I}\frac{w_k}{3}\widetilde D_k
       +\sum_{\ell\notin I}c_\ell U_{N_\ell}.      \tag{4}
\]

The cardinality of `U_N` is `N/2-1` at all these even cutoffs. Put

\[
T=\sum_{\ell>K}c_\ell(N_\ell/2-1).                \tag{5}
\]

The exact number T may be sharper than the sufficient bound in (2).
Indeed T is the target coordinate of the unique solution `h=Ah+b`, with
zero lower boundary and upper boundary values `N_ell/2-1`. The elementary
finite maximum principle for `h_k/r^k` gives

\[
T\le r^{k_*}\max_{\ell>K}\frac{N_\ell/2-1}{r^\ell}
 <6r^{k_*}(2/r^5)^B.
\]

Thus (2) guarantees `T<1`; independently, any exact solve with `T<1`
is sufficient even when (2) is not met.

### 4. Restore actual cutoffs, packet currents, and every boundary flux

For each selected N, set

\[
\begin{split}
D_N&=3U_N-3U_{N/4}-U_{3N/2}-U_{3N/4},\\
K_N&=\nu_N+3(U_N-U_{N/4}).
\end{split}
\]

Here N is divisible by 8. The odd-source floor `floor((N-1)/4)` and N/4
give the same counting measure, since N/4 is even. The exact source
transport and right-aligned decomposition give

\[
\boxed{D_N=\Pi_N+\eta_N+(I-P)K_N.}                 \tag{6}
\]

For completeness, `nu_N=3P(U_N-U_(N/4))-U_(3N/2)-U_(3N/4)` and
`P nu_N=Pi_N+eta_N`; substitution gives (6) with this sign. For a finite
component indicator q the additional term is
`sum_x K_N(x)(q(x)-q(Sx))`. It is retained as a current in (6), never set
to zero by assuming q globally invariant.

The rounding difference is an explicit nonnegative measure:

\[
W_k=(U_{N_{k+3}}-U_{3N_k/2})
        +(U_{N_{k-2}}-U_{3N_k/4})\ge0,
\quad \widetilde D_k=D_{N_k}-W_k.                 \tag{7}
\]

**Finite compiler theorem.** Suppose supplied, checked finite rational or
integer currents satisfy

\[
\Pi_{N_k}=(I-P)J_k+\zeta_k,\qquad\zeta_k\le0,
\quad k\in I.
\]

Supply also the already known finite absorption currents for the lower
boundary counting measures and for `eta_(N_k)`, whose support is contained
in `{5,7,11,13}`. If the rational solve (3) gives `T<1`, these finitely
many inputs construct a finite exact **integer** current for `U_g`, and
actual halting paths for every odd seed at most g.

**Proof.** Substitute (6) and (7) into (4), and substitute every input
current. The result has the exact form

\[
U_g=(I-P)J_*+Z,
\]

where

\[
Z=\sum_k\frac{w_k}{3}\zeta_k
     -\sum_k\frac{w_k}{3}W_k
     +\sum_{\ell>K}c_\ell U_{N_\ell}.
\]

All coefficients multiplying the supplied nonpositive residuals and the
nonnegative rounding shells are nonnegative. Hence `||Z^+||_1<=T<1`.
The source `U_g` is an integer nonnegative measure. Section 1 now constructs
its exact integer current and actual paths using the finite union of input,
boundary, core, and base arrows. QED.

This is a finite nonnegative-cone elimination with a strict integer gap.
It requires no compactness theorem, no invariant indicator on the infinite
graph, and no unbounded trajectory search after its inputs are supplied.
It cannot manufacture those inputs. In particular, applying it to a
residual supported below m can demand packet certificates at cutoffs much
larger than m. Treating those as available during a decreasing induction
would be circular unless a separate construction supplies them.

For any finite signed source whose positive atoms lie below m, the resulting
absorption paths remove all its positive mass, leaving a nonpositive residual.
This is a conditional way to end every positive component plateau on that
source. The universal availability of the requisite input packets remains
the open obligation.

### 5. A concrete finite cone and reproducible evidence

For `m=97`, the first covering grid cutoff is `g=112`, `k_*=16`.

- The exact rational comparison (2) selects `B=10`: 35 packets, maximum
  cutoff 10752. Their exact cone mass is
  `94871593415091/257308134588959 < 1` (about 0.3687081).
- Solving the finite cone directly improves this to `B=9`: **30 packets**,
  precisely the already identified starting cutoffs `a_i*2^b`, `3<=b<=8`,
  with maximum 5376. The exact mass is about 0.6798906; its fraction and
  every rational weight are persisted in `finite_cone_audit.json`.
- `B=8` gives about 1.2856977, so this particular cone does not certify
  the target with that smaller block. This is not an impossibility result
  for other weights, stronger inequalities, or other certificates.

`finite_cone.py` exposes `finite_forcing_plan(m, B=None)`. It returns exact
`Fraction` coefficients: `packet_weights[N]=w_N/3`, the lower/upper
boundary counting-measure coefficients, and `upper_boundary_mass=T`.
The optional B permits a smaller exact solve; callers must check
`forces_target` or the exact inequality `T<1`.

Run the scoped checker with:

```sh
python3 experiments/residual_progress/duality/check_finite_cone.py
```

Use `--write-receipt` only to regenerate its deterministic receipt. The checker
verifies rational comparison constants, integer tail bounds, all transpose
equations, the exact rounded and unrounded measure coefficients, four full
single-cutoff boundary identities, the strict-mass integer-component implication
on an exhaustive finite family, and the stated finite cone examples. The separate
`../forcing/` demonstration supplies and joins actual positive-integer packet
certificates. Neither finite demonstration proves the universal inputs exist.

## Certificates

- [`check_cone_recompute.py`](check_cone_recompute.py) (written at the B09 migration, under 1 s, standard library). It imports the unchanged legacy library `finite_cone.py` from this folder and recomputes the comparison constant `λ(35/27) < 1`, the seven tail-bound exponents, the four cone plans (`m = 97` with `B = 8, 9, 10`, and `m = 1001`): block, packet count, largest cutoff, exact `T`, the forcing flag, every boundary coefficient and the 30 packet weights at `m = 97, B = 9`; it checks the measure identity (4) coefficient by coefficient for each plan and compares everything with the legacy receipt `finite_cone_audit.json`. It does not recheck the single-cutoff identities (6) or the 216000-case integer-gap audit; those were evidence only until the B18 replay revival (below) (the legacy checker no longer runs at this path).
- The commands in the legacy text name the pre-migration path `experiments/residual_progress/duality/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_finite_cone.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 10 s). It checks finite steps only; the status is unchanged.

## Remarks

- **What remains.** The compiler does not supply its own universal input certificates; the inputs may lie above the target scale. Its finite demonstration is [`actual-graph-current-compiler`](../actual-graph-current-compiler/README.md). Whether the inputs can be supplied by smaller absorbed seeds is examined in [`local-packet-calibration-extension`](../local-packet-calibration-extension/README.md): the automatic route is circular. The open targets are [`packet-current-supply`](../../questions/packet-current-supply.md) and [`five-ray-annular-current-supply`](../../questions/five-ray-annular-current-supply.md).
- The subunit-defect part (b) of [`mesh-maximum-principle-alternative-grids`](../mesh-maximum-principle-alternative-grids.md) is the same strict integer gap in scalar form; this node turns it into an explicit finite current.
- **Controls.** The lemma is stated for a general finite functional graph with a sink; the strict threshold is essential, since a positive unit source at a nonabsorbing fixed point has residual mass exactly 1 and no certificate. The compiler needs supplied inputs at every block cutoff, which the `3x+61` controls of [`locally-collatz-like-control-barrier`](../locally-collatz-like-control-barrier/README.md) cannot provide at their failing cutoffs.
- Novelty undetermined (the legacy note asserts none).

## History

- Migrated from `experiments/residual_progress/duality/FINITE_CONE.md` (legacy ID R11; the ledger groups it with the `forcing/` demonstration, here [`actual-graph-current-compiler`](../actual-graph-current-compiler/README.md), alias R11-b) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical; `check_cone_recompute.py` was added at the migration. Legacy status: "written conditional constructive theorem; exact finite demonstration. Required packet inputs remain unproved universally".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `ce56699`. The round report says independent model reviews checked the root-1 convention, the integer gap and every boundary sign; those reviews were run by the main lane's own agents and are not counted as independent. No review from another lane is on record.
