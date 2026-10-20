---
id: local-packet-calibration-extension
kind: result
title: Inner absorption gives an automatic one-sided packet input whose residual is exactly the unresolved complement
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1; 8 | N; U_t counts odd 1 < x <= t; Pi_N the right-aligned packet, eta_N
  its fixed-core remainder, K_N = nu_N + 3(U_N - U_(N/4)). (Split) D_N = 3U_N - 3U_(N/4) - U_(3N/2) - U_(3N/4)
  = Pi_N + eta_N + (I - P)K_N = I_N - L_N with I_N = 2U_N - U_(N/4) - U_(3N/4) >= 0 and
  L_N = 2U_(N/4) + (U_(3N/2) - U_N) >= 0. (Automatic input) Conditional on a supplied finite exact current H
  for I_N (inner absorption is an input), Pi_N = (I - P)(H - K_N - E_N) - L_N. (Conversion) For any supplied
  Pi_N = (I - P)J + zeta, zeta <= 0, L_N = (I - P)C - zeta with C = H - K_N - E_N - J; an exact input absorbs
  every odd seed <= 3N/2, and on the nonzero-row graph of C the unabsorbed counts satisfy
  2 M_low + M_out <= ||zeta^-||_1; feeding the automatic input back returns C = 0 and the whole complement.
  (Coverage barrier) D_N(x) > 0 exactly when x <= N < 4x, so any positive scalar cone with residual budget
  below 1 that covers a seed x uses a cutoff with x <= N < 4x, whose automatic input already needs x: this
  particular induction is circular. Signed combinations of exact inputs, independent residual cancellation
  and other graph connections are outside this scoped obstruction.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [finite-rational-cone-integer-certificate, right-aligned-fixed-core-remainder]
certificates: [check_legacy_replay.py]
evidence:
  - "check_local_extension.py, local_extension.py, local_extension_audit.json, outer_96_current.csv: the legacy implementation (source split, automatic input, local conversion, finite component count) and its checker (64 complete source identities at N = 8, 16, ..., 512; 16640 pointwise scale coefficients; the finite examples at N = 24, 96, 384; the stored 102-row outer current at N = 96; the no-progress feedback at N = 8, 24, 96). Fails at its new path: local_extension.py loads ../forcing/actual_graph_compiler.py by its pre-migration path (now ../actual-graph-current-compiler/, which itself no longer runs). Passed at be73a66 as experiments/residual_progress/closure/check_local_extension.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). The legacy constructor of retained-graph-complement-constructor loads local_extension.py by its old path ../closure/. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
aliases: [R14]
tags: [convergence, packet-currents, local-extension, conditional, circularity, obstruction]
---

# Inner absorption gives an automatic one-sided packet input whose residual is exactly the unresolved complement

## Statement

Fix `N ≥ 8` divisible by 8; odd-only clock, absorbing at 1. With `Π_N`, `η_N` (support in `{5, 7, 11, 13}`) from [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md), `E_N` the known finite core current with `(I − P)E_N = η_N`, and `K_N`, `D_N` as in [`finite-rational-cone-integer-certificate`](../finite-rational-cone-integer-certificate/README.md):

1. **Split.** `D_N = Π_N + η_N + (I − P)K_N = I_N − L_N` with the nonnegative measures `I_N = 2U_N − U_(N/4) − U_(3N/4)` (inner interval `(N/4, N]`) and `L_N = 2U_(N/4) + W_N`, `W_N = U_(3N/2) − U_N`; `‖I_N‖₁ = N/2`, `‖L_N‖₁ = N/2 − 2`, `‖W_N‖₁ = N/4`.
2. **Automatic input (conditional: inner absorption is an input).** If a finite current `H` with `(I − P)H = I_N` is supplied, then `Π_N = (I − P)(H − K_N − E_N) − L_N`.
3. **Conversion.** For any supplied `Π_N = (I − P)J + ζ`, `ζ ≤ 0`, put `C = H − K_N − E_N − J`: then `L_N = (I − P)C − ζ` and `W_N = (I − P)C − 2U_(N/4) − ζ`. If `ζ = 0`, every odd seed `≤ 3N/2` is absorbed using existing rows. In general, on the graph of the nonzero rows of `C`, the numbers `M_low`, `M_out` of unabsorbed seeds in `(1, N/4]` and `(N, 3N/2]` satisfy `2M_low + M_out ≤ ‖ζ⁻‖₁` and `M_out ≤ ‖(−2U_(N/4) − ζ)⁺‖₁`.
4. **No progress by feedback.** Substituting the automatic input gives `C = 0` and `−ζ = L_N`: the composition returns the unresolved complement unchanged (an algebraic statement about these two constructions only).
5. **Coverage barrier.** `D_N(x)` is `0, −1, 2, 1, −2` on `N < 2x/3`, `2x/3 ≤ N < x`, `x ≤ N < 4x/3`, `4x/3 ≤ N < 4x`, `N ≥ 4x`. In any identity `μ = Σ α_N D_N + b − V + Z` with `α_N ≥ 0`, `V ≥ 0`, `b(x) = 0`, `‖Z⁺‖₁ ≤ ε < 1` and `μ(x) ≥ 1`, the weights on `x ≤ N < 4x` sum to at least `(1 − ε)/2`; for these cutoffs the automatic input already requires the absorption of `x`.

The raw top packet atom `9N/4 − 1` is not an intrinsic dependency: `K_N` cancels it. No packet currents or inner absorption are supplied at arbitrary cutoffs; no Collatz or novelty claim.

## Proof

The legacy note "Local packet inputs: constructive conversion and the remaining sign barrier" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

2026-10-17. **Written conditional constructions, a scoped obstruction, and
exact finite certificates.** These results do not supply packet currents or
inner absorption at arbitrary cutoffs. They do not prove Collatz or assert
novelty. All maps use positive odd Syracuse with absorption at 1.

The question here is whether the finite-cone compiler can supply its own
inputs by an induction on smaller seeds. The answer for the direct scalar
route is precise: an inner interval freely supplies a one-sided packet
certificate, but its negative residual retains the unknown complement.
A better packet certificate can reduce that obligation; the conversion below
quantifies exactly what must improve.

### 1. Split the exact scale source into two nonnegative measures

Fix an integer `N>=8` divisible by 8. Let `U_t` count odd states `1<x<=t`,
and retain the actual right-aligned packet source and core remainder:

\[
P\nu_N=\Pi_N+\eta_N,\qquad
\operatorname{supp}\eta_N\subseteq\{5,7,11,13\}.
\]

Define

\[
\begin{split}
K_N&=\nu_N+3(U_N-U_{N/4}),\\
D_N&=3U_N-3U_{N/4}-U_{3N/2}-U_{3N/4},\\
I_N&=2U_N-U_{N/4}-U_{3N/4},\\
W_N&=U_{3N/2}-U_N,\\
L_N&=2U_{N/4}+W_N.
\end{split}                                                   \tag{1}
\]

All cutoffs are exact integers. The odd counting measures at `N/4` and
`floor((N-1)/4)` agree because `N/4` is even. The source identity gives

\[
D_N=\Pi_N+\eta_N+(I-P)K_N=I_N-L_N.               \tag{2}
\]

Both `I_N` and `L_N` are nonnegative integer measures. The inner source
has coefficient 1 on `(N/4,3N/4]` and 2 on `(3N/4,N]`, restricted to odd
states. The complement has coefficient 2 below `N/4` and 1 in the outer
shell `(N,3N/2]`. Their masses are

\[
\|I_N\|_1=N/2,\qquad \|L_N\|_1=N/2-2,
\qquad\|W_N\|_1=N/4.                              \tag{3}
\]

The two negative regions in `L_N` are retained separately; no sign or
multiplicity is suppressed. Let `E_N` be the known finite signed path
current for the fixed core, so `(I-P)E_N=eta_N`.

### 2. Inner absorption supplies a one-sided input immediately

**Automatic input construction.** Suppose a finite current H is supplied
with `(I-P)H=I_N`. Equivalently, the odd seeds in `(N/4,N]` have finite
absorption certificates. Then

\[
\boxed{\Pi_N=(I-P)(H-K_N-E_N)-L_N.}               \tag{4}
\]

Thus `J_auto=H-K_N-E_N` is an explicit packet current with the everywhere
nonpositive residual `-L_N`. It uses the supplied inner paths, the explicit
rows of `K_N`, and the known core paths. No absorption of the low quarter
or outer shell is an input to this construction. Equation (4) follows by
rearranging (2), and its full coefficient identity is checked by the code.

This does not assume that all states below N converge. Only the indicated
inner interval is required. Its paths can visit larger states; they must
be actual supplied finite paths, not an unproved stopping-time assumption.

### 3. A packet certificate returns a quantified complement certificate

Keep the supplied H. Suppose another checked finite packet identity is
available:

\[
\Pi_N=(I-P)J+\zeta,\qquad\zeta\le0.             \tag{5}
\]

The coefficients may be rational; integer inputs give integer outputs.
Set

\[
C=H-K_N-E_N-J.
\]

Then the exact constructive conversions are

\[
\boxed{L_N=(I-P)C-\zeta},\qquad
\boxed{W_N=(I-P)C-2U_{N/4}-\zeta}.               \tag{6}
\]

Every sign in (6) matters: the nonpositive packet residual becomes a
**positive** complement residual. Merely having a one-sided packet input
therefore does not erase the remaining absorption obligation.

**Exact-input extension.** If `zeta=0`, then C is already an exact finite
current for `L_N`. As its source is nonnegative, every state in its support
is in the absorbing component of its finite current graph. Together with
the supplied inner paths, this proves absorption of every odd seed at most
`3N/2`. The conversion requires no new trajectory search outside the inner
interval; it uses only the already supplied current rows and arithmetic.

**Quantitative unresolved count.** Let E be the finite graph of the
**nonzero rows of the converted current C**, with all source states,
endpoints, residual states, and 1 included. Let `M_low` and `M_out` count
the states in `(1,N/4]` and `(N,3N/2]`, respectively, whose E-components
do not contain 1. Summing the first identity in (6) over these components
gives the exact identity and bound

\[
\boxed{2M_{\rm low}+M_{\rm out}
 =-\sum_{x\text{ outside the absorbing component}}\zeta(x)
 \le\|\zeta^-\|_1.}                              \tag{7}
\]

In particular `M_out<=floor(||zeta^-||_1)`. The second identity in (6)
can give a sharper direct outer bound:

\[
M_{\rm out}\le
\left\|\bigl(-2U_{N/4}-\zeta\bigr)^+\right\|_1. \tag{8}
\]

Both statements also hold after adding more exposed arrows, including all
the individual input-current graphs. The actual counts can then decrease.
The numerical examples below use exactly the nonzero-row graph of C;
they do not silently retain rows canceled in the sum.

If either right-side bound relevant to a nonnegative target is below 1,
its integer unresolved count is zero. The graph then supplies an exact
integer current and actual absorption paths for that target. In particular,
the outer shell closes whenever
`||(-2U_(N/4)-zeta)^+||_1<1`, which can be stronger than asking for
`||zeta^-||_1<1`. This is the existing integer-component gap applied to an
explicit local conversion.

**Proof of the count.** On every nonabsorbing component the divergence
of C sums to zero. The source mass of `L_N` in that component is its low
quarter count with weight 2 plus its outer count. It equals the component's
mass in `-zeta`. Sum over those components. For (8), apply the same argument
to the outer identity and bound each component's residual mass by its
positive part. These are statements on the finite graph E, not assertions
that a finite component is globally invariant. QED.

### 4. Feeding the automatic certificate back gives an exact no-progress identity

Substitute the automatic input from (4) into (6). One obtains

\[
C=H-K_N-E_N-(H-K_N-E_N)=0,\qquad -\zeta=L_N.
\]

The complement identity becomes `L_N=(I-P)0+L_N`, and the outer identity
becomes `W_N=(I-P)0+W_N`. Therefore the direct composition retains exactly
the unresolved measure it was supposed to discharge.

This is an algebraic no-progress result for these two constructions. It
does not assert that the union of the supplied paths and explicit arrows
can never contain useful additional absorption paths. Such graph information
would be an extra input or argument, not a consequence of canceling the
two formulas. It also does not rule out a different packet current with a
better residual, cross-packet cancellation, or an independent arithmetic
extension of the exposed graph.

### 5. A precise coverage barrier for adaptive positive scale cones

For an odd `x>1` and `8|N`, the exact coefficient of the unrounded scale
measure is

\[
D_N(x)=
\begin{cases}
0,&N<2x/3,\\
-1,&2x/3\le N<x,\\
2,&x\le N<4x/3,\\
1,&4x/3\le N<4x,\\
-2,&N\ge4x.
\end{cases}                                                   \tag{9}
\]

In particular it is positive precisely when `x<=N<4x`.

**Positive-cone coverage obstruction.** Let an integer target measure mu
have `mu(x)>=1`. Suppose an adaptive finite scale argument has an exact
measure identity

\[
\mu=\sum_{N\in S}\alpha_N D_N+b-V+Z,
\quad\alpha_N\ge0,\quad V\ge0,\quad
b(x)=0,\quad\|Z^+\|_1\le\varepsilon<1.           \tag{10}
\]

Then some positive-weight cutoff satisfies `x<=N<4x`. More quantitatively,

\[
\sum_{\substack{N\in S\\x\le N<4x}}\alpha_N
\ge\frac{1-\varepsilon}{2}.                       \tag{11}
\]

**Proof.** Taking the coefficient at x in (10) gives
`sum alpha_N D_N(x)=mu(x)+V(x)-Z(x)>=1-epsilon>0`.
By (9), only the stated cutoff interval contributes positively, and those
positive coefficients are at most 2. Dropping the negative contributions
proves (11). QED.

This includes the finite-cone method's coefficient identity with its lower
boundary b supported below the new seed, its nonnegative rounding slack V,
and its designated upper boundary budget Z. Changing the rational comparison,
allowing irregular cutoffs, or selecting scales adaptively cannot make that
positive-budget argument use only cutoffs `N<x`.

The scope is essential. The obstruction concerns the displayed positive
cone and its specified residual budget. A favorable **supplied packet
residual** can cancel additional boundary mass after substitution; that is
extra certificate information, precisely the resource measured by (6)--(8).
Negative combinations of exact input certificates, or additional graph
connections, are also outside (10). No general impossibility of an arithmetic
Collatz constructor is claimed.

For direct induction from inner absorption, the forced cutoff `N>=x`
has x in its required inner interval when `N<4x`. Thus its automatic input
would already require the new seed's absorption. This pinpoints the
circularity of supplying those particular positive-cone inputs by the
automatic inner-interval construction.

#### The raw top atom is not an intrinsic dependency

Every right-aligned packet at `8|N` has coefficient 2 at its largest
state `9N/4-1`. Its unique source is `3N/2-1`, with first valuation 1 and
coefficient 2; this endpoint exceeds the fixed core. However, the explicit
current `K_N` in (2) cancels that atom. The positive support of `D_N` lies
entirely below N. Consequently, a claim that every packet input necessarily
requires absorption through `9N/4` would be wrong. That height is an
obstacle only to naive separate absorption of its raw sources. The genuine
barrier for the scalar induction is (9)--(11) and the residual sign in (6).

### 6. Actual positive-integer examples and reproduction

`local_extension.py` implements the exact source split, automatic input,
local conversion, and finite component count. All input identities are
checked. Capped searches supply only the finite examples; no universal
absorption or search termination is assumed.

- At `N=24`, the packet search stops at depth 1 with
  `zeta=-delta_31-delta_47`. Inner absorption, the explicit arithmetic
  currents, and that input leave exactly outer seeds **27 and 31** outside
  the absorbing component of the converted-current graph. Bound (7) is
  sharp: both sides are 2. This is a finite graph obstruction, not a claim
  that either positive seed fails to terminate.
- At `N=96`, the input is exact. Conversion closes the entire complement.
  The extracted exact nonnegative current for the outer shell has **102 rows**,
  stored in `outer_96_current.csv`. Its divergence is 1 at each odd state
  from 97 through 143 and zero elsewhere. Extraction exposes no new arrows.
- At `N=384`, the input has negative residual mass 5. The converted graph
  leaves outer seeds **447, 495, 511, 559**, giving exact unresolved mass 4;
  one unit of the negative residual is already in the absorbing component.

The receipt contains the full residuals, all unresolved source lists, and
hashes of the regenerated current tables. It also verifies that feeding the
automatic input back at `N=8,24,96` returns zero current and the full original
complement residual.

```sh
python3 experiments/residual_progress/closure/check_local_extension.py
```

The default checker is read-only and compares the stored receipt and full
outer-current table. `--write-receipt` regenerates those two files. It checks
64 complete source identities at `N=8,16,...,512`, 16640 pointwise scale
coefficients, the actual finite examples, and every claimed output identity.
All discovery is capped. These finite checks supplement the general proofs;
they do not establish universal packet supply or a strictly decreasing
induction.

## Certificates

No certificate ran at this path before the B18 replay revival; the legacy checker was evidence only until the B18 replay revival (below). The finite examples recorded in its receipt: at `N = 24` the input `ζ = −δ_31 − δ_47` leaves exactly the outer seeds 27 and 31 unabsorbed (bound (7) is sharp, both sides 2); at `N = 96` the exact input closes the whole complement and the 102-row outer current [`outer_96_current.csv`](outer_96_current.csv) has divergence 1 at each odd state 97..143; at `N = 384` the residual budget 5 leaves the four outer seeds 447, 495, 511, 559. The commands in the legacy text name `experiments/residual_progress/closure/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_local_extension.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 9 s). It checks finite steps only; the status is unchanged.

## Remarks

- The conversion quantifies exactly what a better packet certificate must improve. The retained cutoff graph improves the automatic input in [`retained-graph-complement-constructor`](../retained-graph-complement-constructor/README.md).
- The coverage barrier concerns the displayed positive cone and its residual budget; a favourable supplied residual can cancel more boundary mass after substitution (the resource measured by item 3). No general impossibility of an arithmetic constructor is claimed.
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/closure/LOCAL_EXTENSION.md` (legacy ID R14) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). Note, scripts, receipt and stored current moved byte-identical. Legacy status: "written constructive identities and a scoped positive-cone obstruction; finite certificates".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `a7b7b47`. The round report's "independent reviews" of the local conversion were run by the main lane's own agents and are not counted as independent.
