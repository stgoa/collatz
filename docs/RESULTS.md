# Result ledger

Last updated: 2026-10-18. This ledger summarizes scope; the linked proof notes and exact data contain the supporting arguments.

## Current programme and preserved Phase6 standing

R1–R94 below are frozen infrastructure. The active
[quantitative-rigidity brief](QUANTITATIVE_RIGIDITY_BRIEF.md) develops the
language selected through [VIEWPOINT_MAP.md](../VIEWPOINT_MAP.md), with
exploration decisions in [VIEWPOINT_LOG.md](VIEWPOINT_LOG.md).
The [route map](../ROUTE_MAP.md) and [Phase6 ledger](PHASE6_LEDGER.md)
retain earlier obligations, grades and completed evidence. Viewpoint
recommendations are distinct from the written mathematical results below.

V002 recommends arithmetic regularity of component colorings after comparing
fourteen viewpoints and testing the first shortlist. Its
[finite-period classification](../experiments/viewpoints/V002/invariant_colors.md)
is a separate elementary written diagnostic, not a new R-series convergence
result. Automaticity of an actual bad set is not supplied. V002 proposed carry
boundaries and integer-ensemble laws as bounded follow-ups; the initial
relational and geometric portfolios were demoted with recorded reasons.

V003 supplies a separate [partial classification and kernel reduction](../experiments/viewpoints/V003/REPORT.md):
all invariants depending only on binary digit count are constant; the first
ternary image of a finite binary kernel adds at most one function; and its
pure-zero ternary orbit is finite. An explicit automatic counterexample
refutes a scaling-only completion. Those lemmas did not establish full
mixed-section closure. The carry probe adds no new
relation and is closed. These written, independently agent-reviewed proofs
have no novelty or convergence claim and do not alter the frozen R-series.

V004 supplies the [full binary-automatic classification](../experiments/viewpoints/V004/GLOBAL_RIGIDITY.md):
every finite-valued binary-automatic Collatz invariant is constant, for
arbitrary finite automata. Positive-offset binary sections close under
ternary sections; Cobham gives periodicity of the odd section, and an
elementary residue argument forces constancy. This is a written proof
with independent agent review, imported classical inputs, and separate
bounded arithmetic checks. Novelty, formal verification and regularity
of the actual nonabsorbing set are not supplied. The R-series is unchanged.

V005 supplies [partial quantitative results](../experiments/viewpoints/V005/REPORT.md):
one automatic positive binary section forces constancy; its exact
reconstruction gives a polynomial all-depth complexity bound; and binary
growth controls joint binary/ternary section growth. Exact counterexamples
refute descendant-infinitude and separate-base-growth shortcuts. The full
Collatz identities have a three-equation scalar interface, with the growth
step still missing. The constancy conclusion imports Cobham through V004;
the reconstruction is elementary. The activated unbounded-ratio goal remains open.
The separate Lean lane reports a V004 derivation conditional on Cobham;
main inspected the statement and source receipt, without independent replay.

V006 proves a [scoped quadratic lower bound](../experiments/viewpoints/V006/overlap.md):
all mixed states `F(t+s_2(3^a*n))` are distinct when F is not eventually
periodic. This distinctness argument is elementary. One positive digit-count
section forces quadratic growth of a nonconstant invariant's binary kernel,
using Cobham through V005/V004 to exclude eventually periodic F. The missing extraction hypothesis
is not assumed. An adjacent11-pair control rejects extraction from weaker
binary premises. A separate action counterexample rejects importing linear
semigroup growth from a linear rooted orbit. The full radix graph is
faithfully represented, but its general growth problem remains open.

V007 proves an [arbitrary-depth singleton-exit exclusion](../experiments/viewpoints/V007/separator.md).
Every joint section of a nonconstant invariant has infinite kernels in
both bases, using a new reverse-closure argument. The exact radix identities
exclude a finite forward interior with one exit. This forces at least two
new joint states per depth, still a linear bound, and gives no improved
binary growth rate after depth conversion. Larger finite boundaries and
the full unbounded-ratio target remain open. The result has written
independent review; novelty and formal verification are unclaimed. The
generic separator theorem is elementary; its Collatz application imports
Cobham through the V005/V004 infinitude argument.

V008 supplies an [exact two-exit counterexample and full-root distinction](../experiments/viewpoints/V008/REPORT.md).
The generic two-exit extension of V007 is false even for an actual section
graph with infinite kernels in both bases everywhere. The example has
quadratic joint growth and fails the Collatz root identities. Those full
identities force constancy when the first joint ball has at most three
states, by an elementary corrected case proof. Linear cumulative growth
has a uniform future-mean consequence, but a bounded-degree graph control
rejects a stronger bounded-layer inference. No universal asymptotic rate
improvement is proved. The quantitative goal remains open.

V009 proves [unbounded additive binary-section excess](../experiments/viewpoints/V009/binary_tail.md):
every nonconstant finite-valued invariant satisfies `kappa_h(D)-(D+1)->infinity`.
The proof excludes an eventual single-state binary tail by classifying
its maximal transition phases and controlling every earlier-state return.
Exact radix commutation forces contraction of return blocks, bounded
return families and equality of whole sections. This imports Cobham
through the existing two-base infinitude premise. It gives no fixed
fractional improvement and does not complete the unbounded-ratio goal.
The separate elementary [global detection theorem](../experiments/viewpoints/V009/global_growth.md)
shows that under `|J_D|<=C(D+1)`, every nonzero vector in the real span
of J_A is detected before `9^L`, for
`L=ceil(2C+sqrt(2C(A+1))+1)`. Longer first-nonzero delays would force
quadratic mixed-section rank, but their full-class construction remains
missing. Both arguments have written agent review, without a novelty or
formal-verification claim. Frozen mathematical infrastructure is unchanged.

S.1 now has a [written stopping calibration](../experiments/phase6/stopping_calibration/STOPPING_CALIBRATION.md)
with explicit finite horizons, integer cutoffs and a separate W5 pullback.
Its ordinary estimate transfers to each fixed supported `3x+d` map and does
not remove every exception. S.2 and universal current supply remain open.
This is a re-derived published stopping limit, with no novelty claim.

S.2 has a [written transport barrier](../experiments/phase6/stopping_transport/STOPPING_TRANSPORT.md):
no fixed cardinality multiplier plus a uniform sublinear error controls
first-half preimages of every target subset. The obstruction already uses
one-arrow sources and transfers to each supported fixed d. It does not
exclude estimates specific to the actual bad set or bounds in a global
weighted growth norm. Verification status is in the Phase 6 ledger.

A separate [growth-norm proof](../experiments/phase6/growth_norm_transport/GROWTH_NORM_TRANSPORT.md)
now addresses that gap: for every fixed supported d and every0<alpha<1,
some fixed infinite target set of finite power-growth norm expands under
first-half preimages. The S.1 finite-cylinder calibration supplies the
prefix-free word family; averaging exact target residues produces the
witness. The four-word explicit subcase already expands by more than241/240
through alpha7/8, while the d1 one-arrow operator contracts by10/13 for
alpha>=4/5. The all-exponent result concerns arbitrary-target contraction,
not a bound tailored to the actual nonabsorbing set. Full verification for
P6-003 passed; Collatz remains open.

P6-004 supplies [an audited external linear lower theorem](../experiments/phase6/linear_density_audit/README.md)
through independent source compilation, exact statement correspondence and
actual axiom checks, followed by a successful fresh replay into the same
Lean kernel. Its explicit bound applies to every fixed target not
divisible by3, with no convergence premise. The separate written counting
reconstruction is conditional on Tao's mixing theorem and has a qualitative
general-d extension. Our actual-B residue attempt still permits a positive
leading-density profile; C.2a remains open. The full finite gate passed119
fields. Formal replay, handwritten proof status and programme grade none
are distinguished in the Phase6 ledger and evidence.

## R1 — Exact source transport and original packets

**Status: inherited written proofs and finite certificates.**

The master handoff develops exact cylinders, the stopping-work recurrence, the signed source measure `nu_N`, and the original packet decomposition. Finite currents cancel unknown common futures, including unequal arrival times. See [master handoff](../COLLATZ_PROGRAMME_MASTER_HANDOFF.md), Sections 2–10, and the [original research note](../collatz_research_20261017/collatz_packet_currents/research_note.md).

The original complete tables certify all-horizon packet work in `[-1406,2364]` at `N=4096`, depth 2, and `[-57661,63824]` at `N=262144`, depth 4. These are two finite source cutoffs, not a uniform theorem. Python and independently compiled C++ verification passed at both cutoffs.

Archive SHA-256: `025c8fafe25940951fe408b32b1ec806259725a6b4f8855d9f2b022911fe5447`. All 31 original manifest entries were checked.

## R2 — Right-aligned depth-one fixed-core remainder

**Status: written elementary proof; finite implementation checks.**

For every integer `N >= 8`, form complete triples from the right in each valuation cylinder and source component. Then

`P nu_N = Pi_right_N + eta_N`, with `supp(eta_N) ⊆ {5,7,11,13}` and `||eta_N||_1 <= 6 ceil(log2 N)`.

Over-budget one-step valuations map to 1 and are killed. The four residual states have odd-only hitting times `1,5,4,2`, respectively. Hence, for every `T >= 1`,

`|3 E_T(N) - H_(T-1)(Pi_right_N)| <= 8 + 30 ceil(log2 N)`.

This is a new grouping. The original current tables cannot be relabeled as certificates for it. Full argument: [current proof note](../collatz_research_20261017/right_aligned_reduction.tex), Theorem 1. Implementation and receipts: [script](../collatz_research_20261017/right_aligned_packets.py), [audit](../collatz_research_20261017/right_aligned_audit.json).

## R3 — Qualitative current criterion

**Status: written equivalence; its universal hypothesis remains open.**

The following are equivalent:

1. Collatz holds.
2. For every integer `N >= 8`, the right-aligned packet work has a finite upper bound over all horizons; this bound may depend arbitrarily on N.
3. Every such packet family has a finite exact current.
4. Every such packet family has a finite current with an everywhere nonpositive residual.

The proof uses the nonhalting indicator and its source-count recurrence. The count satisfies `B <= L B`; the comparison function obeys `L(N^(3/2)) < (505/512) N^(3/2)` for `N >= 16`. A positive global maximum of `B(N)/N^(3/2)` is impossible. A separate least-exception argument checks the exact-current implication.

See [current proof note](../collatz_research_20261017/right_aligned_reduction.tex), Lemma 2 and Theorem 3. No inverse-basin theorem or uniform current-cost estimate is needed for this route. No universal constructor or termination proof has been established. The equivalence does not reduce the logical strength of the unresolved conjecture.

## R4 — Dyadic remainder and a sign guard

**Status: written exact formula; finite checks.**

For `N=2^b`, `b >= 3`, the core residual is periodic in b modulo 6, and for every `T >= 1`:

`H_(T-1)(Pi_right_N) - 12 <= 3 E_T(N) <= H_(T-1)(Pi_right_N) + 1`.

The proof uses `q_(a+6)=64 q_a+21` and cancellation of the six new valuation classes. The full formula appears in the current proof note. The reproducible audit checks b from 3 through 1000, as well as direct packet decomposition for every `8 <= N <= 2048` and `N=4096,10001,262144`.

Do not infer that all packet work is nonpositive: the exact finite witness is `H_39(Pi_right_32)=57`. The criterion is boundedness above for each cutoff, not a universal zero upper bound.

## R5 — Five dyadic rays suffice

**Status: written equivalence, independently model-audited, with exact finite base checks.**

R3 remains valid, but its every-integer hypothesis can be replaced by
`N=a*2^b`, `a in {12,14,16,18,21}`, `b>=3`. Each of bounded packet work,
exact finite currents, and finite currents with nonpositive residual on this
grid is equivalent to Collatz.

At the five ordered mantissas, rounding `3N/2` upward advances three positions
with a dyadic carry. The comparison `F(a_i*2^b)=2^((5b+i)/3)` gives
`F(rounded 3N/2)=2F(N)`. The exceptional-count recurrence contracts by
`2^(-10/3)+(2/3)(1+2^(-5/3)) < 89/90`. Its positive maximum on the grid is
impossible. The small target points lie below 96, where all odd seeds terminate.

See [main proof note](../collatz_research_20261017/right_aligned_reduction.tex),
Theorem 4, and the [sparse-criteria note](../experiments/current_construction/frontier/sparse_current_criteria.md).
The [checker](../experiments/current_construction/frontier/check_sparse_criteria.py)
verifies the transition inequalities, contraction, and all odd seeds below
65536 (more than required); their largest odd-only hitting time is 125.
Earlier 21-ray and 30-ray arguments remain as scoped alternatives. No infinite
ray has been certified. No minimality or novelty claim is made.

## R6 — Disjoint annular recursion

**Status: written identity and finite arithmetic checks; no universal current constructor.**

For every `8|N`, put `Q=9N/4`. Then
`Pi_right_(64N)=Pi_right_N+A_N`, `eta_(64N)=eta_N`,
`supp(Pi_right_N) ⊂ (1,Q)`, and `supp(A_N) ⊂ (Q,64Q)`.
The increment has six bands with tabulated coefficients modulo 18.
Each band has total zero. Exact identities include
`||A_N||_1=99N/2`, `|supp(A_N)|=267N/8`, and
`sum_y y*A_N(y)=63Q`. These describe source size, not current cost.

R5's rays split into 30 sequences `N=a*2^(r+6k)`, `r=3..8`.
Their initial cutoffs are at most 5376 and packet endpoints below 12096.
Verified convergence of all these endpoint seeds within 98 odd steps proves
exact currents exist for the 30 starting measures; their full tables are not
stored. Currents with nonpositive residual for **all increments on these
sequences** therefore suffice for Collatz. This universal obligation is open.

The recurrence does not produce those currents: modulo finite divergences,
`[A_N]=3[F_N]-3[F_(N/4)]-[F_(3N/2)]-[F_(3N/4)]`, with
`F_t=U_(64t)-U_t`. The expanding `3N/2` scale remains.
See the [annular proof](../experiments/current_construction/recursive/annular_recursion.md).
The [checker](../experiments/current_construction/recursive/check_annular_recursion.py)
passed 66 full-measure cases, through expanded cutoff 262144, without trajectory search.

## R7 — What currents detect and a scoped obstruction

**Status: written graph theorem, complete semidecision algorithm, and finite checks.**

A finite exact current exists precisely when every nonabsorbing orbit component
has total mass zero. A current with nonpositive residual exists precisely when
each such mass is nonpositive. Bounded work for a single measure only tests
their sum. Negative-integer Syracuse cycles give a separation example;
no positive nonterminating orbit is claimed.

Exposing longer paths from every source while retaining historical intersections
is complete for finding an existing certificate. Finite depth caps return
unresolved. The implementation was checked on all 1728 three-vertex map/measure
cases in both modes; this does not establish universal termination.

For every `H>=0`, let `K=2H+7`, `y=9*2^K-1`, and `N=4*2^K+5`.
An actual individual packet is `2 delta_y-delta_(y+6)-delta_(y+12)`.
Every current for it, including one with nonpositive residual and arbitrary
auxiliary states, needs more than H nonzero rows. The proof separates orbit
segments modulo 32. This rules out uniformly bounded per-packet catalogues;
unbounded recursive constructions and cancellation between packets remain possible.

See [proof and search specification](../experiments/current_construction/obstructions/functional_graph_currents.md),
[checker](../experiments/current_construction/obstructions/verify_obstructions.py),
and [whole-packet findings](../experiments/current_construction/obstructions/whole_packet_findings.md).
Stored new tables include an exact current at 65536 and a one-sided current at
2053. At 2053, certificates cancel components not yet linked to 1 in the
exposed graph. At 65536, the exposed graph already proves source absorption.
These certify only named finite revised measures.

## R8 — Affine lifting and a universal partial current

**Status: written constructive proofs; exact capacity and divergence checks. Complete residual construction remains open.**

A finite directed common-tail tree lifts to exact Syracuse trees for every integer `t>=0`: at vertex x use `x(t)=x+2^(A_x+1)*3^(D-d_x)*t`, where `d_x,A_x` are the remaining path length and valuation sum, and `D=max d_x`. This preserves every exact valuation. A zero-mass source therefore gives a finite exact current for every parameter, without following the lifted common sink. Actual annular coverage requires a separate check.

The checked five-source component from `A_96` supplies such a family. Its sources have weights `(-1,-1,1,2,-1)` and slopes `(384,512,576,864,1152)`. For `t=9s` its actual annular coverage is `96+72s<=N<=120+96s`; for `t=9s+3` it is `120+72s<=N<=152+96s`, always with `8|N` and `s>=0`. All ten source progressions are pairwise disjoint, by 45 exact gcd tests. Thus every admissible copy can be used together. The count is `C(N)=N/144+O(1)` and positive current cost is at most `3C(N)`.

Five further short-chain families have an everywhere nonpositive current and delete positive mass `D(N)=3N/2+O(1)`, with an explicit floor formula and correction periodic modulo 72. Their sources are pairwise disjoint and also disjoint from the entire five-source packing. Combining them gives a finite explicit current and an exact residual obtained by deleting the certified atoms:

`A_N=(I-P)J_N+Z_N`, `||J_N^+||_1<=3C(N)`,
`||Z_N^+||_1=99N/4-D(N)-3C(N)`.

The removed positive mass is `73N/48+O(1)`; the remaining positive mass is still unhandled in general. The construction terminates for each N by bounded arithmetic loops, but it is a **partial** constructor. No complete universal current or coverage claim follows.

Proofs: [affine components](../experiments/annular_construction/components/AFFINE_COMPONENTS.md), [arithmetic reductions](../experiments/annular_construction/arithmetic/ARITHMETIC_RESULTS.md), and the main LaTeX note. The [combined constructor](../experiments/annular_construction/arithmetic/combined_partial_current.py) returns the full current and residual and audits eight cutoffs through 6144. The packing checker validates every allowed cutoff through 4096 and exact identities at large integer parameters; the catalogue checker validates 66 cases. Independent model reviews checked both capacity proofs.

Stored actual annular certificates include a nonpositive-residual current for `A_96` and an exact current for `A_168`. At N=168 the graph cancels a balanced cross-band component before its sources are linked to 1. Exact witnesses `H_53(A_96)=699` and `H_9(A_384)=42` rule out a complete universally nonpositive current; positive cost must be allowed.

## R9 — Exact one-pass annular compression and its limits

**Status: written identity and finite arithmetic checks. No iterated contraction theorem.**

For `F(x)=4x+1`, states in the same F-chain have the same Syracuse successor. Map each state down to its unique root by `(x-1)/4` while `x=5 mod8`, discarding root 1, and call this operation R. Then `PRmu=Pmu`, and `mu=(I-P)(mu-Rmu)+Rmu` is an explicit finite partial current. For every `8|N`,

`||R A_N||_1 = ||P A_N||_1 = 171N/4-|c_N| <= (19/22)||A_N||_1`,

where c_N is the signed source mass in the root-1 chain and `|c_N|<=3`. Its correction can vanish: `c_80000=0`. A six-row entry-profile proof gives the exact formula. All 66 arithmetic cases passed, with a separate implementation checking nine cutoffs.

R is idempotent and its residual is not another annulus, so the contraction cannot be applied repeatedly as stated. In fact the compressed residual retains coefficient +2 at exactly 2N specified outer roots, leaving positive mass at least 4N.

Literal forward transport also has a specific closure obstruction. In the outer strip after t steps, the profile is `3*1_(3^(t+2)|y+1)-1_(3^(t+1)|y+1)` on odd y. Its least even period is `2*3^(t+2)`. Thus a finite fixed-modulus list with a bounded number of interval pieces cannot represent all such profiles. This concerns literal synchronous pushforward; it permits rewrites, growing moduli, and unequal-time cancellation. It does not prove aggregate historical exposure depths are unbounded.

See [full proof and checker description](../experiments/annular_construction/arithmetic/ARITHMETIC_RESULTS.md).

## R10 — Component progress, boundary flux, and information loss

**Status: written graph/arithmetic identities and exact scoped counterexamples. The progress lemma remains open.**

For exposed arrows E, `Phi(E)` is the sum of positive source masses of components not containing 1. It is a nonincreasing integer, and zero is equivalent to a nonpositive-residual current supported on E. Each positive component indicator is an exact dual obstruction restricted to that graph. Universal termination needs a proof that every positive plateau ends after finitely many extensions. For actual `A_96`, Phi stays 17 through exposure depths 20–27 and becomes zero at depth 28.

The scale quotient has an exact finite representative. Put `F_t=U_(64t)-U_t`, `V_N=nu_(64N)-nu_N`, `K_N=V_N+3(F_N-F_(N/4))`, and `D_N=3F_N-3F_(N/4)-F_(3N/2)-F_(3N/4)`. Then

`D_N=A_N+(I-P)K_N`.

For a finite-component indicator q, the extra pairing is the boundary flux `sum_x K_N(x)(q(x)-q(Sx))`. At depth 27 for A_96, a stored 83-vertex component has source mass 17 and flux -7, giving scale pairing 10. Adding every K_96 arrow makes the flux zero but still leaves positive mass 17. Neither omitting the flux nor closing it at one cutoff proves progress.

For fixed `k>=1` and `2^(k+2)|N`, each annular band projects to zero modulo `2^k` and `3*2^k`. Those data alone lose the distinction from an empty source. This does not exclude methods with richer arithmetic information.

A separately labeled **negative-integer** reflected annulus has identically zero work but component masses `-20,-73,+93` at three known cycles. A stored 5868-row current and residual verify these masses. It refutes an overgeneralized scalar-to-current inference; it is not a positive Collatz counterexample.

See [aggregate duality proof](../experiments/annular_construction/duality/aggregate_duality.md), [checker](../experiments/annular_construction/duality/check_duality.py), and [receipt](../experiments/annular_construction/duality/duality_audit.json), including every state and boundary row of the positive flux example.

## R11 — Finite rational cone and integer certificate conversion

**Status: written conditional constructive theorem; exact finite demonstration. Required packet inputs remain unproved universally.**

If a finite integer source satisfies `mu=(I-P)J+Z` with a finite rational current and `||Z^+||_1<1`, each unabsorbed exposed component has integer source mass below 1, hence at most zero. The same graph therefore supports an integer current with nonpositive residual. For a nonnegative source every source already belongs to the absorbing component, so the existing arrows give actual finite absorption paths and an exact nonnegative integer current. The strict threshold and source integrality are essential.

Enumerate the five rays by `N_k=a_i*2^b`, `k=5b+i`. The rounded recurrence uses shifts `-10,+3,-2` with weights `1,1/3,1/3`. The rational comparison `r=35/27` has `r^(-10)+(r^3+r^(-2))/3<1`. On a finite index block, the inverse `(I-A)^(-1)` is nonnegative. Solving `(I-A)^T w=e_target` supplies exact nonnegative rational weights for an identity among finite counting measures.

Restore the actual source-scale current `K_N=nu_N+3(U_N-U_(N/4))`, the signed core current, lower boundary absorption, and both nonnegative rounding shells with their negative signs. Given checked nonpositive-residual packet certificates at every selected cutoff, the weighted identity leaves positive residual bounded by the exact upper boundary mass T. If T<1, the integer-gap lemma extracts an integer current for the counting measure U_g, where g is the first grid cutoff at least the target m. No global-invariance assumption or further orbit exposure is used during extraction.

An explicit sufficient block has `O(log m)` input cutoffs and largest cutoff `O(m^(p/(p-1)))`, where `p=5 log_2(35/27)` and `p/(p-1)≈2.14682`. This is a bound on which input certificates suffice, not their cost, size, search time, or availability. The block can require inputs above the target scale, so it does not supply a decreasing induction.

For m=97, a sharper exact solve at B=9 uses the 30 starting cutoffs through 5376. Actual one-sided input currents compile to a 6217-row rational current with denominator `46422343855805` and positive residual numerator `29145292346068`. The strict gap extracts a stored 95-row nonnegative integer current for U_112, using only already present arrows. Twenty input searches completed with some sources still unlinked to 1 in their separate graphs.

Proof: [finite cone](../experiments/residual_progress/duality/FINITE_CONE.md). Reusable plan: [finite_cone.py](../experiments/residual_progress/duality/finite_cone.py). Actual implementation and evidence: [compiler note](../experiments/residual_progress/forcing/ACTUAL_COMPILER.md), [compiler](../experiments/residual_progress/forcing/actual_graph_compiler.py), [stored U_112 current](../experiments/residual_progress/forcing/forced_U112_current.csv). Checks include four exact cone plans, four full source identities, seven rational tail bounds, 216000 finite integer-gap cases, and the complete actual conversion. Independent model review checked the proof and all signs in the compiler.

## R12 — Root transport normal form and explicit surviving atoms

**Status: written operator identities and scoped obstructions; finite checks.**

Since `R^2=R` and `PR=P`, every finite sequence of the root collapse and transport operators has residual `I`, `R`, `P^t`, or `RP^t`. On roots, `RP` is conjugate to ordinary killed Syracuse on odd states coprime to 3. This supplies no independent descent mechanism.

For each `8|N` and integer t>=0, the actual top-band sources
`72N<x<144N`, `x=-1 mod(9*2^(t+2))`, number exactly
`floor(4N/2^t)-floor(2N/2^t)`. Every one retains coefficient +2 through all j<=t at `3^j*(x+1)/2^j-1` in both `P^j A_N` and `RP^j A_N`. The proof excludes all competing larger-valuation histories by a strict outer-height bound and excludes further root representatives above the support.

Thus no fixed number of those operations makes every annulus nonpositive. For N=a*2^b the top source survives b+2 transports at `324*a*3^b-1`, ruling out a uniform O(N) state-height closure of that process. Neither result excludes growing-depth constructions, affine rewrites, or historical intersections.

Exact N=96 counterexamples refute repeating the 19/22 contraction (`3533 -> 3124`) and any strict one-step norm decrease on every unresolved reachable residual (norm13 and positive mass4 remain unchanged). These finite plateaus do not establish infinite plateaus.

See [proof](../experiments/residual_progress/transport/ROOT_TRANSPORT.md), [checker and bounded current constructor](../experiments/residual_progress/transport/check_root_transport.py), and [receipt](../experiments/residual_progress/transport/root_transport_audit.json). Independent review checked the root-1 absorption convention, surviving count, and height inequalities.

## R13 — Complete aggregate obstructions at every fixed depth

**Status: written arbitrary-depth theorem, independently model-audited, with exact finite and symbolic checks. Complete current construction remains open.**

An inverse reachability oracle decides whether a state is an origin among the first D exposed arrows from any actual annular source, under exact forward height bounds. Exhausting its incoming and outgoing neighbors recovers a complete exposed component without materializing the full O(N) annulus. State/query caps return unresolved.

At `N=1610612736=12*2^27`, the depth-32 component of the top source has 35 vertices, 34 arrows, and exactly three source atoms `(64N-1,-2)`, `(96N-1,+2)`, `(144N-1,+2)`. Its total is +2 and it is unlinked to 1. The exact finite component closure excludes every other incoming exposed edge. Therefore no current supported on the **entire** depth-32 exposure graph can have a nonpositive residual for that annulus. This rules out a packed source cover by common-tail trees of source-to-anchor depth at most 32; it does not rule out deeper or recursive constructions.

The tempting always-positive top-chain claim fails: at N=10368, depth2, the complete top component contains 27 sources whose coefficients total zero. Unequal-time intersections attach negative mass that the bare growing orbit omits.

The inverse graph matches independent full forward graphs on 48 small cases; inverse branches are separately compared with brute-force predecessors through state2047. Both complete finite witnesses and explicit cap outcomes are persisted. See [proof and scope](../experiments/residual_progress/templates/AGGREGATE_EXPOSURE.md), [checker](../experiments/residual_progress/templates/check_inverse_exposure.py), and [full component receipt](../experiments/residual_progress/templates/inverse_exposure_audit.json).

The first extension lifts that entire depth-32 component to every `N=(96*2^24)q`, `q>=1`, `q=1 mod3^22`. Exact affine arithmetic proves all 9171 inverse decisions and 42487 inequalities over the whole half-line. The [symbolic lift](../experiments/residual_progress/templates/INFINITE_COMPONENT_FAMILY.md) preserves every excluded incoming edge, with an independent numeric oracle checking samples.

The stronger [inverse-history theorem](../experiments/residual_progress/templates/UNBOUNDED_EXPOSURE_DEPTH.md) applies to **every D>=1**. Choose `2^max(D+4,10)|X`, `X=1 mod3^(D+2)`, and `N=3X/128`. The complete component is `y_k=(3/2)^k X-1`, `k=1..D+3`, with only the three source weights `(-2,2,2)`. Every extra inverse history of length at most D has affine form `uX-c=u(X-1)+z` with `u>=4,z>0`, placing it above all annular sources. The bottom predecessor is an unsourced multiple of3; the terminal outgoing arrow exceeds the exact exposure-height bound. Thus all incident edges are accounted for, and mass2 obstructs a one-sided current on the entire G_D.

The hypotheses hold at `N=12*2^((2*3^(D+1))*t-9)=96*64^(3^D*t-2)`, every t>=1. Hence unbounded depth is already necessary on the single ladder starting96. If d_*(N) is the least sufficient exposure depth, allowing infinity, then `d_*(96*64^k)>=v_3(k+2)+1` for every k>=0. This excludes every finite source-covered catalogue with bounded source-to-anchor depth, even with cross-packet cancellation and fractional combinations. It permits recursive use with growing total depth, and does not prove that any full finite current is absent.

The [checker](../experiments/residual_progress/templates/check_unbounded_exposure.py) verifies 5715 bounded inverse-word cases, eight complete CRT components through D32, four required-ray components, and exact modular ray conditions through D128. The universal quantifiers follow from the written invariant proof, not the finite checks. Two independent model audits found no gap; human and formal review remain outstanding.

## R14 — Local packet calibration and the sign of the remaining obligation

**Status: written constructive identities and a scoped positive-cone obstruction; finite certificates.**

For 8|N, split the single-cutoff scale source as `D_N=I_N-L_N`, where `I_N=2U_N-U_(N/4)-U_(3N/4)>=0` is supported on `(N/4,N]`, and `L_N=2U_(N/4)+U_(3N/2)-U_N>=0`. If H absorbs I_N, E absorbs the fixed core, and `K_N=nu_N+3(U_N-U_(N/4))`, then `Pi_N=div(H-K_N-E)-L_N` is an automatic one-sided input. Feeding this input back into the reverse conversion leaves exactly the original complement residual; useful extra paths in the retained union graph would require a separate argument.

For an independently supplied `Pi_N=div J+zeta`, zeta<=0, the exact reverse conversion is `L_N=div(H-K_N-E-J)-zeta`. An exact input therefore absorbs the low quarter and outer shell `(N,3N/2]` on existing arrows. For a one-sided input, its negative residual becomes a positive complement residual. On the converted-current graph, twice the unabsorbed low-quarter count plus the unabsorbed outer count equals the mass of -zeta outside the absorbing component, at most `||zeta^-||_1`. The outer residual `-2U_(N/4)-zeta` can give a sharper bound.

The coefficient `D_N(x)` is positive precisely for `x<=N<4x`. A positive scalar cone with known lower support and designated positive residual below1 must therefore use a positive-weight cutoff in that interval. Its automatic inner-absorption input already includes x, so this particular induction is circular. Favorable independent residual cancellations, other graph connections, and signed combinations of exact inputs are outside this scoped obstruction. The raw top packet atom is not an intrinsic dependency; K_N removes it.

At N24 the actual residual `-delta31-delta47` leaves exactly outer seeds27,31 unabsorbed in the converted graph, attaining the bound2. At N96 an exact input yields a stored 102-row current absorbing odd97..143. At N384 the residual budget5 leaves four outer seeds. The [proof](../experiments/residual_progress/closure/LOCAL_EXTENSION.md), [implementation](../experiments/residual_progress/closure/local_extension.py), and [checker](../experiments/residual_progress/closure/check_local_extension.py) include 64 full identities and 16640 pointwise checks. Conversion exposes no new arrows.

## R15 — A terminating auxiliary normalization and its unavoidable remainder

**Status: written partial construction, order-independence proof, exact lower bound, and finite checks.**

Move positive mass at y to `(2y-1)/3` for residues5/11 modulo18, `(8y-5)/9` for residue13, and `(4y-5)/9` for residue17. The exact one/two-arrow paths supply nonpositive currents and endpoints strictly below8y/9. These are exactly the residue classes admitting a strictly smaller ancestor within two Syracuse steps. The integer potential `sum x*mu^+(x)` strictly decreases, proving termination for every finite source. Descending nonnegative flow makes the resulting current and residual independent of order.

For A_N, the current rows lie below96N and positive residual states below64N; negative source atoms remain as high as144N. An exact modulus144 first-pass profile and five floor counts prove that at least `21N/4` positive residual mass remains at multiples of3. These states have no incoming Syracuse arrows, so any completion from this residual must use at least that much positive continuation current. It is not a lower bound on the final summed current's positive cost, because the continuation may cancel earlier negative rows. The height bound does not improve the existing64N source-scale absorption cutoff.

The [proof and profile](../experiments/residual_progress/auxiliary/AUXILIARY_NORMAL_FORM.md), [reusable constructor/checker](../experiments/residual_progress/auxiliary/check_auxiliary_normal_form.py), and [receipt](../experiments/residual_progress/auxiliary/auxiliary_normal_form_audit.json) check 66 cutoffs through6144, every claimed full divergence and profile, processing-order equality, and short-ancestor classification through4097. The terminal residual remains unresolved; termination of the partial normalization is not termination of the Collatz programme.

## R16 — Exact cancellation after an unbounded delay, and additional source packing

**Status: written universal partial-current families, with complete finite component examples. Full component resolution at every parameter and complete annular certificates remain open.**

The delayed-release construction starts with the same three actual sources as R13: `y1=64N-1`, `y2=96N-1`, `y3=144N-1`, of weights `(-2,2,2)`. For infinitely many ternary depths h it constructs two further actual negative sources u,v, each of weight-1, joined through the valuation word `1^r,2^h,3`. Their combined five-source measure has an exact everywhere nonpositive current. Its rows are contained in exposure depth `h+r+1<=2h+1`. The original chain is still a complete positive component through depth `h+1`: the refined proof needs ternary divisibility of the previous shadow difference, rather than extra divisibility at the final state. Thus some arbitrarily delayed obstructions admit an explicit arithmetic cancellation. The same refinement strengthens R13's ladder lower bound to `d_*(96*64^k)>=v_3(k+2)+4` for every k>=0.

The parameters are exact: `lambda=4(4/3)^h(2/3)^r` must lie in `(81/32,27/8]`; the least r satisfying the upper bound qualifies for at least one of every two consecutive h. Put `X-1=3^h U`, `N=3X/128`, and `v=2^r(4^(h+1)U+2)/3^r-1`. A specified congruence gives `v=47 or155 mod162`, and an explicit large-X condition puts `t=(2v-1)/3`, `u=(4t-1)/3` in the required bands. CRT and an elementary power-of2 lifting argument realize infinitely many cutoffs on `N=96*64^k` for each qualifying h. The current is-1 at u,t; -2 along v to y1; -4 at y1; and-2 at y2. All intermediate coefficients, exact valuations, and source capacities are retained.

At `N=340131840`, the complete exposed component changes from three sources of mass2 at depth4 to five sources of mass0 at depth5, without reaching1. At `N=60555264`, the first new attachment instead adds a balanced three-source block, leaving mass2 at depths8 and9. Thus first attachment alone does not ensure progress. The general construction certifies its five-source submeasure; it does not assert that every larger full component has no additional positive sources. See [delayed-release proof and constructor](../experiments/residual_progress/release/DELAYED_RELEASE.md) and [exact checker](../experiments/residual_progress/release/check_release.py).

A separate [disjoint packing theorem](../experiments/residual_progress/release_packing/RELEASE_PACKING.md) adds two families to R8 at every 8|N: pairs `q=31 mod54`, `36N<q<54N`, with source `2delta_q-2delta_((4q-1)/3)`; and triples `q=31 or103 mod108`, `64N<q<72N`, with coefficients(-1,2,-1) along `u→q→v`. A full capacity proof separates them from each other and all old packed sources. The [extended constructor](../experiments/residual_progress/release_packing/release_packing.py) removes total positive mass `1073N/432+O(1)`, improving R8's `73N/48+O(1)`, with positive cost at most `73N/432+O(1)`. Exact floor counts and the full remaining measure are returned. This packing is separate from the general delayed five-source family; no unproved combined capacity is assumed.

## R17 — A partial extension from retained input arrows

**Status: written conditional constructor, complete arithmetic graph classification, and finite current certificates. Inner absorption remains an input.**

The explicit K_N in R14 has nonzero rows at every odd state `1<x<3N/2`. Retain these arrows even if their coefficients cancel in the summed automatic input. Given a finite exact current for I_N, the retained graph already absorbs every seed through N: lift each low-quarter seed by `F(x)=4x+1` to the inner interval and reuse its common successor.

The components of the K_N-only graph missing every state at most N are classified exactly. They consist of an outer root x and its boundary successor, with either x=3 modulo12; or x=7 modulo12 above9N/8. Below9N/8, roots x=7 or19 modulo36 also have one outer predecessor `p=(4x-1)/3`. The remaining x=31 modulo36 roots have a predecessor below N. This exhausts all incoming and outgoing cutoff arrows.

Compress the two-outer-source components to weight2 at their root and retain the single-source components with weight1. The resulting nonnegative profile R_N has exact mass `25N/288+O(1)`, with error between-19/9 and5/4. The supplied graph gives `Pi_N=div J_improved-R_N` using no new arrows. It absorbs all lower seeds and asymptotically47/72 of the outer shell; the original automatic residual mass was N/2-2. At N8 the new profile vanishes; it is nonzero at every allowed N>=16. On the ladder N=96*64^k its exact mass is `25N/288-4/3`.

This is an improvement over the scalar zero-current feedback, whose algebra remains valid. It does not supply its own inner absorption, prove a repeatable contraction of R_N, or rule out additional useful connections in the supplied inner-current graph. See [proof](../experiments/residual_progress/complement/RETAINED_GRAPH_EXTENSION.md), [constructor](../experiments/residual_progress/complement/complement_constructor.py), [checker](../experiments/residual_progress/complement/check_complement.py), and [stored small current](../experiments/residual_progress/complement/improved_packet_24_current.csv). The audit covers131 full cutoff graphs, all36 mass phases, and eight exact supplied-input conversions.

## R18 — Signed path collapse, intermediate capacity, and retained frontiers

**Status: written finite constructors, a restricted optimality theorem, and scoped obstructions. Forward path termination remains unproved in general.**

Let E0 contain every valuation1 Syracuse arrow and every valuation2 arrow whose source is2 modulo3. Each vertex has at most one incoming and one outgoing arrow. Two consecutive valuation2 arrows are impossible, so every two backward steps contract by less than8/9. Every vertex therefore has a unique finite backward root, even if that component's forward path is infinite.

The linear signed collapse B moves all source coefficients, including negative ones, to these roots and returns an exact finite current. Its current may have positive coefficients. A second constructor processes positive arrivals along every individual backward edge, using intermediate negative capacity that the old two-edge shortcuts missed. Its current is nonpositive. On a component path with source coefficients a_0,...,a_m, its root residual is exactly `max_j sum_(i=0)^j a_i`. This is the smallest possible root residual among nonpositive E0 currents with nonpositive residual away from the root, and is no larger than R15's root residual. Both constructions terminate by finite backward ancestry, not by a forward Collatz claim.

Naively pushing positive normalized roots forward once and applying the old normalizer again stabilizes in finitely many rounds, but for every annulus its fixed point retains at least N positive mass. The five inactive root classes3,7,15,19,27 modulo36 return immediately to themselves except for cancellation at existing negative successors. The exact N persistent atoms follow from two floor-count families.

For every `N=96*64^k`, set `L=12+6k` and `x_j=3^j2^(L-j)-1`, j=0,...,L-1. This is a complete E0 component with only the three source weights(-2,2,2), hence root mass2. Its first forbidden exit is `w=(3^L-1)/2^(2+v2(L))`, and an explicit current gives `-2delta_x1+2delta_x2+2delta_x3=div(-2delta_x1+2sum_(j=3)^(L-1)delta_xj)+2delta_w`. This retains the unresolved mass and escapes the immediate reset. For odd k, w is already an inactive root and w/x_0 grows without bound, excluding a decreasing-height recursion for this particular exit rule.

See [proof](../experiments/residual_progress/alternating/ALTERNATING_PATHS.md), [constructors/checker](../experiments/residual_progress/alternating/check_alternating_paths.py), and [receipt](../experiments/residual_progress/alternating/alternating_paths_audit.json). The finite audit checks20 annuli, states through4097, and11 growing-depth examples. At N96 the old normalizer leaves positive mass1859, the intermediate-capacity version1414, and signed collapse1337. These numbers are not uniform contraction constants. A retained frontier or equivalent history is needed to advance beyond an E0 component; its eventual cancellation remains open.

## R19 — Phase coverage and a fixed-order obstruction to depth2h+1

**Status: written arithmetic proof with exact finite symbolic verification; the all-phase completion candidate is refuted.**

Write `X=128N/3` and `U=(X-1)/3^h`. For h=2, `2^10|X`, and `X>=497664`, every unit phase `U mod27` except16 has the same complete depth5 component: eight vertices, source coefficients(-2,+2,+2), and mass2. For h=3, `2^11|X`, and `X>=8957952`, every unit phase `U mod81` except31 has the analogous complete depth7 component. These give17 of18 and53 of54 coarse unit phases. Each exceptional phase supplies an explicit additional source; this does not imply that its full component is resolved.

The proof enumerates complete inverse decisions with affine inequalities valid on a half-line. Translation checks preserve every queried state's integrality, parity, inverse branch, and actual source coefficient. The full modulo18 residue may change while its coefficient remains fixed. These symbolic checks establish the infinite classes; separate representative scans do not establish them.

On the required ladder `N=96*64^k`, every `k=2 mod27` has exact h=2 yet an isolated mass2 component at depth5. A separate135-comparison symbolic lift proves this family starting at N393216. Thus the proposed completion bound `2h+1` fails even with arbitrary source-covered valuation words. This does not rule out a different growing bound or eventual completion.

The old two delayed families cover a fraction `1/3^(r+3)` of unit-U classes at their stated modulus. A separate finite scan of1944 representatives at h2/h3 yields21 exact zero-cost partial currents with source capacity and attachment placement checked. No universal class coverage is inferred from those21 successes.

See [proof](../experiments/residual_progress/release_coverage/PHASE_COVERAGE.md), [checker](../experiments/residual_progress/release_coverage/check_coverage.py), and [receipt](../experiments/residual_progress/release_coverage/coverage_audit.json). Latest side-lane depth16 counts were independently reproduced at commit `f12da944dc68cfaff0884d874e11bc6c2cb98d34`; a bounded absence of negative capacity does not exclude deeper zero-cost attachments.

## R20 — Transfer annular cancellation to exact outer-seed descent

**Status: written conditional transfer theorem, explicit infinite descent families, and finite current certificates. Full residual coverage remains open.**

Let `8|M`, `N=64M`, and suppose an exact absorption current for U_N is supplied. Every positive atom of A_M has an ancestor at most N within two Syracuse arrows. Consequently, for a supplied exact capacity-checked block `P-Q=div J` with `P<=A_M^+`, `Q<=A_M^-`, the known graph absorbs P, and `Q=div(H_P-J)` gives a finite exact absorption certificate for Q. The current may be signed; nonnegative Q forces its sources into the absorbing finite component. Unrelated zero-source cycle components do not affect this conclusion.

Every R17 residual root x has a valuation1 exit `t=(3x+1)/2` in `(3N/2,9N/4)`, residue5 or11 modulo18, with `A_M(t)=-1`. If Q includes t, its certified path absorbs the entire R_N coefficient at x, either1 or2. Reusing an established path with multiplicity2 is valid; the annular block's source capacity was spent once. If `R_N=div T+R_remaining`, the upgraded packet current is `J_packet-T`, with residual `-R_remaining`.

The old packed trees cover exactly the roots `9183+768j` for their valid indices `j=9s` or `9s+3`. There are `C_old(M)=N/9216+O(1)` such roots. The other existing catalogue families add no remaining root: their exits lie too low or correspond to seeds already removed by R17. This distinguishes actual residual coverage from total cancelled annular mass.

For every R16 delayed family, the root `t=(2v-1)/3` is a remaining R_N atom of weight1, and has exact first descent to N-1 with valuation word `1^(r+1),2^h,3`, length `h+r+2<=2h+2`. All intermediate states exceed N, and the peak exceeds `(4/3)^h N`. These are genuine shrinking branches with unbounded excursions, including branches on the required ladder. A companion example at h=r3, X24315904, N36473856 has root40480795 of residual weight2 and an exact ten-arrow descent to36473855.

The [proof](../experiments/residual_progress/complement_recursion/ANNULAR_COMPLEMENT_TRANSFER.md), [constructor](../experiments/residual_progress/complement_recursion/transfer.py), and [checker](../experiments/residual_progress/complement_recursion/check_transfer.py) retain every uncovered coefficient. The [receipt](../experiments/residual_progress/complement_recursion/transfer_audit.json) checks66 cutoffs,353280 positive atoms,164 catalogue roots,five supplied-current conversions,and170 explicit descent branches. A full61-row [current for seed9183](../experiments/residual_progress/complement_recursion/outer_9183_current.csv) is stored; it improves the N6144 packet residual by exactly one unit.

## R21 — Sharp bounded source clusters within the restricted path graph

**Status: written universal local bound and finite preprocessing constructor; no universal exit or plateau termination claim.**

In the R18 graph E0, define adjusted height `h(x)=x` for x1 modulo3 and `h(x)=x/2` for x2 modulo3. Every nonzero A_N source satisfies `Q<h(x)<32Q`, with Q9N/4. An allowed step from type1 multiplies h by more than3/4; from type2 by more than3/2. Shrinking steps cannot be consecutive. Thus two sources in the same complete E0 component have even separation at most58 or odd separation at most63.

The63 bound is sharp: `x=3*2^95*t-5`, `Q=18*floor(x/18)`, t>=1, realizes `(1,2)^31,1` with nonzero source endpoints. The exact cylinder uses the extra bit: total valuation94, modulus2^95. Its complete source cluster has mass38 when3 does not divide t and35 otherwise.

At most63 predecessor and63 successor queries from a source recover every source in that component. Prefix sums give an exact current placing the whole cluster mass at its last source. All current rows lie below192N, and positive cost is at most `63||A_N^+||=6237N/4`. These are bounds for this partial preprocessing. A finite arithmetic guard scheme has sufficient period `2^96*3^65`; no practically enumerated catalogue or closure under continuation is claimed.

For a forbidden E0 edge `x->y`, valuation2 sends directly to an inactive smaller root. Valuation at least3 sends to a component root below x/4. The comparison uses the originating exit vertex x, which may be far above the last annular source. Moreover, for the old Mersenne family with odd k, the first exit enters a component containing no original annular source. Positive transported mass then becomes an auxiliary source. A complete continuation must handle such components rather than assume each exit finds negative capacity.

See [proof](../experiments/residual_progress/window_components/WINDOW_COMPONENTS.md), [constructor/checker](../experiments/residual_progress/window_components/check_window_components.py), and [receipt](../experiments/residual_progress/window_components/window_components_audit.json). Eight complete annuli agree with independent full-ancestry grouping; sharpness phases, exact affine guards, forbidden exits through8193, and four source-empty targets are checked.

## R22 — Arbitrarily large exposure depth with the ternary order fixed at2

**Status: written complete-component proof with a finite arithmetic certificate.**

For every integer D>=1, if `2^max(D+4,10)|X` and `X=10 mod3^(D+2)`, then N=3X/128 is an allowed cutoff, `v_3(X-1)=2`, and the entire depth-D component of144N-1 is the chain `y_j=3^j X/2^j-1`, j=1,...,D+3. Its only sources have coefficients(-2,+2,+2); its mass2 excludes a one-sided certificate on that graph. Every depth has infinitely many examples on `N=96*64^k`. Thus no finite-valued bound depending only on h can control sufficient exposure depth.

The proof exhausts incoming histories. Before the affine inverse slope becomes integral, height excludes every source. At the first integral slope, an offset c reaches1 under the auxiliary3x-1 map. A complete22-case finite barrier excludes any positive3x+1 shadow ancestor at most33; ternary precision propagates the shadow through every remaining inverse branch. The nontrivial3x-1 cycles exclude hypothetical barrier counterexamples; the actual offsets are in the basin of1.

See [full proof](../experiments/residual_progress/phase_depth/FIXED_H_DEPTH.md), [checker](../experiments/residual_progress/phase_depth/check_fixed_h.py), and [receipt](../experiments/residual_progress/phase_depth/fixed_h_audit.json). Eight complete finite components and modular ladder cases are checked. X varies with D: no permanent positive component or Collatz counterexample is asserted.

## R23 — A halving identity removes half the leading outer residual

**Status: written conditional construction, exact count, and checked finite currents.**

Let `x=2^a*t-1`, a>=2, t odd. If `t=3^a mod4`, then `S^a(x)=S^a((x-1)/2)`. The difference of the two finite prefix currents has divergence `delta_x-delta_((x-1)/2)`. Applying this identity to every selected R17 root uses only supplied absorption through N, since `(x-1)/2<3N/4`. All source weights, including coefficient2, are preserved. The upgraded packet identity is `Pi_N=div(J_0-T)-R'_N`, where T certifies the selected roots exactly.

The remaining profile is R_N restricted to `t=-3^a mod4`, with mass `25N/576+O(log N)`. An exact CRT floor formula proves this for every8|N; the absolute leading-term error is at most `6 floor(log2(3N/2))`. Combined with R17, this certifies asymptotically119/144 of the original outer shell. It is a single partial extension, not an iterable contraction. On the complementary branch, putting `d=v_2(3^(a-1)t-1)>=2` and `w=(3^(a-1)t-1)/2^d` gives `S^a(x)=3*2^(d-1)*w+1`; the smaller partner being known does not certify this larger state. The attempted same-identity extension fails at x27.

Selected required-ray roots `x=2^a-1`, even a>=8, have unbounded prefix length and height relative to N. The bridge still ends after a arrows on each side without an assumed larger absorption interval. The full [proof](../experiments/residual_progress/residual_return/SHRINKING_COALESCENCE.md), [constructor](../experiments/residual_progress/residual_return/halving_return.py), [checker](../experiments/residual_progress/residual_return/check_halving_return.py), and [receipt](../experiments/residual_progress/residual_return/halving_return_audit.json) include8192 selected seeds,1016 parameterized cases,512 cutoffs, and eight supplied-input conversions. At N6144,263 of532 residual units are certified. A coefficient2 current at root79 is stored in full.

## R24 — Completing the complementary profile on the five rays suffices by induction

**Status: elementary written conditional sufficiency, with a checked finite base; universal completion remains open.**

Order all cutoffs `a*2^b`, a in{12,14,16,18,21}, b>=9. Consecutive ratios are7/6,8/7,9/8,7/6,8/7. Suppose a rule certifies every remaining R23 root from a supplied exact U_N current at each such cutoff. R17 and R23 then extend absorption to3N/2, which includes the next cutoff. The checked baseU6144 and induction supply every positive seed. All cutoffs are divisible by512, so R20's annular-block alternative is available throughout. No larger absorption assumption is needed, but the universal completion rule has not been constructed.

A single factor64 ladder is too sparse for this step; the union of all five dyadic rays is sufficiently dense. Independent per-root certificates may reuse already certified input paths. Combining their source blocks into one annular submeasure instead requires joint capacity accounting. The [quantifier and literature audit](../experiments/residual_progress/sufficient_sets/SUFFICIENT_SETS_AUDIT.md) proves these distinctions and records why the cited sufficient-set/inverse-count results do not supply the missing bounded-height witnesses.

## R25 — Complete elementary bridge classes and an exact quotient

**Status: written classification and finite current constructors; quotient termination remains open.**

Let F(x)=4x+1. The equivalence generated by all one-step sibling identities and the R23 halving identities has exactly the components `{F^k(q),F^k(2q+1):k>=0}`. The unique minimum q is either1 modulo8 or a complementary climber `q=2^a*t-1`, `t=-3^a mod4`. Stripping inverse F steps and then at most one selected halving gives its terminating normal form nu and an exact finite current of divergence `delta_x-delta_nu(x)`. Every remaining R23 root is already canonical, so arbitrary use of just these identities cannot lower it.

Syracuse respects the classes: `nu S=nu S nu`. Thus `T(q)=nu(S(q))` is an exact quotient, and `T^n nu=nu S^n`. The class of1 absorbs within two actual steps, making universal quotient termination equivalent to Collatz. Complementary canonical states increase by valuation1; canonical1-modulo8 states above1 decrease. This supplies a closed state space, not a globally decreasing quantity.

All inverse branches are explicit: two rays under `q→64q+49`, plus the valuation1 point when the target is2 modulo3. Greedy least-predecessor iteration fails parametrically: for y=57+72j its depth2 value is409+512j, while the true minimum is203+256j. Odd-a seeds2^a−1 on required rays have arbitrarily long increasing quotient runs. Exact CRT counts give canonical density1/4 among integers, with error uniform in an auxiliary odd modulus.

See [proof](../experiments/residual_progress/bridge_normal_form/BRIDGE_NORMAL_FORM.md), [implementation](../experiments/residual_progress/bridge_normal_form/normal_form.py), and [receipt](../experiments/residual_progress/bridge_normal_form/normal_form_audit.json). Finite checks cover16,384 seeds,2,048 currents,6,143 complete bounded inverse sets and14,476 counting cases. No novelty claim is made.

## R26 — Complete complementary run bridges and normalized residual coverage

**Status: written conditional constructor and uniform counting theorem; an explicit residual remains.**

For every complementary root x=2^a*t−1, set d=v2(3^(a−1)t−1)>=2 and w=(3^(a−1)t−1)/2^d. If d is odd, the initial climb and valuation2 run give a finite bridge to `f(x)=3^((d−1)/2)w`. If d is even, the actual run ends at `f(x)=2*3^(d/2)w+1`. These formulas cover the whole parameter domain and have prescribed finite lengths. Append R25's bridge to `f_star(x)=nu(f(x))`.

Given a finite exact U_N current, every full-weight R'_N root with f_star(x)<=N is certified using only these explicit prefixes and supplied paths. Signed intermediate rows are retained and the finite graph supplies a nonnegative absorption current. The new packet identity retains the exact remaining nonnegative profile. For example at N168, root187 has weight2 and raw return211>N, but canonical return105<N; the stored14-row current certifies2 delta187.

The normalized selected mass is `beta*N+O(log^4 N)`, where beta is an explicit positive convergent series with a rational enclosure and `beta≈0.02399251818395744`. The remaining mass is `(25/576−beta)N+O(log^4 N)≈0.01941025959382034N`. This certifies about55.2788% of R23's complementary leading mass, conditionally covering about92.24% of the whole outer shell when combined with R17/R23. The exact count takes O(log^4 N) arithmetic terms; its uniform error proof retains affine offsets and growing odd moduli. The raw, unnormalized rule removes only about34.7449% of the complementary mass.

The rule does not close the profile: a=7 modulo16,t=1 gives an already canonical return(3^a−3)/8 with unbounded ratio to x. Both transitions27→31→91 increase height and return the run label(a,d) from(2,2) to(5,4) to(2,2). Thus neither a strictly decreasing rank of these two labels alone nor a lexicographic label-rank/height potential works for every transition. This is not an integer cycle or a prohibition on richer state.

See [proof](../experiments/residual_progress/complementary_bridge/RUN_BLOCK_BRIDGES.md), [constructor](../experiments/residual_progress/complementary_bridge/run_bridge.py), [receipt](../experiments/residual_progress/complementary_bridge/run_bridge_audit.json), and [weight2 certificate](../experiments/residual_progress/complementary_bridge/outer_187_double_current.csv). Checks cover4096 complementary seeds,2883 parameter cases,68 exact normalized counts and seven supplied-input conversions. At N6144,146 of269 remaining units are certified, leaving123. The numerical fraction is not a repeatable contraction.

## R27 — Infinite known fibres with uniform counts at arbitrary heights

**Status: written counting theorem and conditional finite certificates.**

Given absorption through N, every member of `I_N={x>0 odd:nu(x)<=N}` is certifiable by its explicit normalization bridge and the supplied current. This set is infinite. For every pair of integers X>=N>=8,

`#(I_N intersect [X,2X))=N/4+O(log N)`,

with error at most `2 floor(log2 N)+3`, independent of X. The proof writes both rays as `x=2^s*q+beta_s`, with beta_s=(2^s−1)/3 for even s and(2^(s+1)−1)/3 for odd s. Exact clamped canonical counts telescope; neighboring cutoffs differ by at most1/2, and only O(log N) corrections survive. This improves the preliminary O(log^2 N) bound. At X=HN the density among odd integers is `1/(2H)+O(log N/(HN))`.

Every individual high member needs only a finite explicit bridge; a single finite current is not asserted for the infinite union. The number of extra bridge rows is O(log N), independently of height, although integer bit cost depends on height. I_N extends beyond the finite forward-orbit union used by the excursion probe. Its spatial density is not an orbit hitting probability and does not establish universal convergence.

See [proof](../experiments/residual_progress/absorbed_fibers/ABSORBED_FIBERS.md), [constructor](../experiments/residual_progress/absorbed_fibers/fibers.py), and [receipt](../experiments/residual_progress/absorbed_fibers/fiber_audit.json). Checks compare direct enumeration, independent fibre enumeration and exact formulas on912 small,42 odd-cutoff boundary and18 high bands, including height multiplier2^512, and verify56 supplied-current conversions.

## R28 — Exact symbolic prefix rates and a scoped external barrier

**Status: written elementary rate proof for specified rules, exact finite checks, and external audit.**

For the D/M/H slope recognizers defined in the [proof](../experiments/residual_progress/cylinder_barrier/CYLINDER_RATES.md), conditional on initial valuation1, undecided cylinder measure has nth-root limit `rho≈0.946504576832584` after n odd steps. At m binary bits its mth-root limit is `beta≈0.965906553233438=rho^(1/log2(3))`. Composition counts, cyclic rotation and exponential-moment bounds prove both clocks separately. The fixed escape prefix(1,1,1,2), x=47 modulo64, supplies the matching lower bound for every stated enlarged rule. Equality of exponential rates need not mean constant-factor ratios.

The external exact-closing H dynamic program omitted cases where the unfinished closing valuation is already known to be at least3. For four bits x=3 modulo16 is selected; correcting the tail changes undecided measure from1 to3/4. Direct residue enumeration checks all four variants for bits2..14; exact dynamic programs run through128 bits. The correction changes finite coverage but not the proved rate.

The optional feed at commit491d26d766971bdf7fdce9bba288540423fd58c8 was reproduced and scoped. Its two new receipts match, while its finite forward-union density and merger timing do not exhaust arbitrary certifiable targets or prove an orbit hitting bound. An actual R23 family has a smaller partner below N and common state(3^a−1)/8 at unbounded relative height before any descent. R27 supplies an infinite additional target set; it can be incomparable with the finite forward union (R29/R32). The rate theorem is about symbolic slope prefixes, with no uniform finite-integer count when bits grow with log N; affine constants and increasing-modulus discrepancies remain separate obligations.

See [checker](../experiments/residual_progress/cylinder_barrier/check_cylinder_barrier.py), [finite receipt](../experiments/residual_progress/cylinder_barrier/cylinder_audit.json), and [pinned external review](../experiments/residual_progress/cylinder_barrier/external_review.json). No arbitrary-bridge obstruction or Collatz termination claim follows.

## R29 — Exact supplied-path saturation and a finite ordinary certificate core

**Status: written closure theorem and finite compiler; universal entry remains open.**

Let Y_N be the actual forward paths supplied by an exact U_N current and Q_N=nu(Y_N). The exact closure of the seeds through N under the R25 elementary identities and forward S arrows is E_N=nu^(-1)(Q_N). The quotient Q_N is finite and T-forward-closed. Its least-origin labels give the minimum canonical input seed reaching each target and determine every smaller-cutoff table. This minimum is for the specified operations, not all possible independent proofs.

For every finite T-closed canonical set Q, define W_Q={S(q),3q+2:q in Q}. Then S(nu^(-1)Q)=W_Q, S(W_Q) is contained in W_Q, |W_Q|=2|Q| and max W_Q=3maxQ+2. If Q absorbs, the finite ordinary S table absorbs and certifies any member of its infinite preimage set in at most2|Q| arrows. All construction after the supplied input follows finite tables. The pointwise corollary S(x)<=3nu(x)+2 shows that high elementary targets immediately return to a bounded region.

The compiler accepts any checked signed bridge whose target normalizes into Q_N. This improves R26's cutoff-only test: at N384, the full weight2 root415 returns to1579>N, but1579=S^9(327) is known. A stored48-row current certifies both units. At that cutoff saturation increases the accepted complementary mass from9 to11 of17. In this example415 itself already equals S^4(327), so the example demonstrates complete reuse of supplied history, not a new merger mechanism. These are finite examples, with no universal coverage claim.

For an arbitrary finite canonical Q with M=maxQ and integer X>=M, its high-band count differs from |Q| by at most floor(log2 M)+1. Signed weights have the same bound multiplied by their maximum magnitude. This additive estimate need not become a relative asymptotic: Q={1} has persistent counts0 and2 along two height sequences. No uniform relation between |Q_N|, maxQ_N and N is supplied.

The cutoff-only set I_N and known-forward union Y_N can be incomparable:41 lies in Y_32 but not I_32; I_N has arbitrarily high members while Y_N is finite. E_N contains both. Allowing arbitrary incoming arrows enlarges this closure and is a separate operation. See [proof](../experiments/residual_progress/known_saturation/KNOWN_SATURATION.md), [compiler](../experiments/residual_progress/known_saturation/saturation.py), [receipt](../experiments/residual_progress/known_saturation/saturation_audit.json), and [weight2 certificate](../experiments/residual_progress/known_saturation/root415_current.json).

## R30 — A shrinking paired recursion resolves infinite growing-return families

**Status: written partial construction with decreasing parameter, complete infinite cylinders, and finite currents.**

For positive w=3 modulo8 put h=v2(3w-1). If h=2k+2 is even, k>=1, set z=3^k(3w-1)/2^h. Exact prefixes give S^k(3w)=4z+1 and S^(k+1)(w)=2z+1. Canonical z gives an elementary terminal bridge between3w and w. If z=101 modulo128, put w'=(3z+1)/16. Then w'=3 modulo8, 0<w'<w/4, and an explicit local current has divergence delta_(3w)-delta_w+delta_(3w')-delta_w'. Subtracting a child bridge gives the required parent bridge. The recognizer always terminates, but returns unresolved for odd h and other noncanonical z classes.

With k=1 the child is R(w)=(27w+7)/256. For every r>=0, the complete cylinder `27^r(229w-7)=256^r(229*59-7) mod2^(8r+7)` gives exactly r recursive transitions followed by the terminal class w=59 modulo128. It has the prescribed merger `S^(3r+3)(3w)=S^(3r+4)(w)`. Binary exponent lifting yields an explicit class a=a_r modulo2^(8r+8) with a=7 modulo16 and w=(3^(a-1)-1)/8 in that cylinder. The first classes are199 modulo256 and2887 modulo65536.

For every such a, x=2^a-1 is an actual weight1 complementary R_N root at N=12*2^(a-4), q=2^(a-1)-1<N, and `S^(a+3r+3)(x)=S^(a+3r+3)(q)`. The old normalized return3w is already canonical and grows without bound relative to x along each class. These exact smaller-seed mergers resolve infinite subfamilies of R26's obstruction at every recursive depth. A second class a=39 modulo2^20 uses k=3 recursively then k=1 terminally, with merger time a+8.

Given a supplied exact signed current for q, add the R26 bridge x→3w, the pair bridge3w→w, and the negative of q's prescribed prefix to w. This gives an exact absorption current for x; a nonnegative current is extracted from the existing finite graph. The stored a39 example has191 rows and source549755813887. Coefficients may be scaled with their full weight. This does not assume absorption at an unknown larger cutoff.

See [proof](../experiments/residual_progress/second_return/SHRINKING_PAIRS.md), [constructor](../experiments/residual_progress/second_return/paired_return.py), [receipt](../experiments/residual_progress/second_return/paired_return_audit.json), and [actual current](../experiments/residual_progress/second_return/mersenne_39_current.csv). Checks cover4096 pairs,72 terminal cylinders,56 recursive integer cases through depth64,65 exponent lifts,eight actual Mersenne bridges,and one supplied-current conversion. Independent proof/code review passed. Universal coverage and any revised global residual fraction remain unproved.

## R31 — Repeated bounded runs exclude finite-label height potentials

**Status: written finite-cylinder theorem and scoped obstruction; no divergent positive orbit is exhibited.**

R26's normalized return is exactly T^k(x), with k=a+floor(d/2)−1. The eight-step valuation word(1,2,1,1,1,1,2,2) pairs run labels(2,2),(5,4). Its affine map is Psi(x)=(6561x+9221)/2048. All intermediate states are canonical and exceed the pair's starting seed whenever x=27 modulo2^17.

For every r>=1 choose any positive x congruent to−9221/4513 modulo2^(11r+6). The exact identity4513Psi(x)+9221=(6561/2048)(4513x+9221), together with4513*27+9221=2^17, forces r complete repeated words. All2r normalized returns strictly increase. Thus arbitrarily long growth occurs with a<=5,d<=4 and all ordinary valuations at most2. CRT supplies actual coefficient1 roots on infinitely many required cutoffs N=12*2^b for each r; the initial seed varies with r.

No potential of the form G(label(x),x), with a fixed finite label set and G nondecreasing in height for each label, can strictly decrease at every normalized return. A sufficiently long growing sequence repeats a label at a larger height, contradicting strict decrease. This covers finite residue augmentations and finite-rank/height lexicographic candidates. It permits unbounded arithmetic state, nonmonotone potentials, arguments allowing intermediate increases, and extra known-path mergers.

See [proof](../experiments/residual_progress/bounded_run_cycles/BOUNDED_RUN_GROWTH.md), [constructor](../experiments/residual_progress/bounded_run_cycles/bounded_runs.py), and [receipt](../experiments/residual_progress/bounded_run_cycles/bounded_runs_audit.json). Checks cover57 parameter cylinders through128 repeated words,21 required-ray witnesses and six finite-modulus examples, retaining the complete finite divergence. No uniform obstruction at a fixed seed is asserted.

## R32 — Exact merger scope, normalized prefix rates, and early cancellation

**Status: written scope results and an infinite actual-source cancellation family, with finite external reproductions.**

The known forward union F_N and elementary fibre set I_N can be incomparable:11 belongs to F_8 but not I_8, while21 belongs to I_8 but not F_8. Their elementary-plus-forward saturation is R29. Allowing arbitrary common-tail comparisons with known seeds gives exactly the basin of1, so universal common-tail certification is equivalent to absorption. A finite-sample density model cannot show that a successful proof must avoid mergers.

For every odd x, `S(x) in {S(nu(x)),3nu(x)+2}`, hence S(x)<=3nu(x)+2. Therefore a test nu(S^j x)<=N at some j<=L forces an ordinary state at most3N+2 within L+1 successors. For forward-saturated targets the bound uses maxQ_N instead; no uniform constant-factor bound by N has been established. The precise symbolic slope recognizer accepting nu(S^j x) with slope<2/3 has the R28 rates rho and beta for every fixed lookahead, with all normalization bits charged. The escape prefix(1,1,1,1,1,2), x191 modulo256, and positive-barrier composition counts prove the matching lower rates. This is not a moving-modulus integer-count theorem or an arbitrary-catalogue barrier.

For every a=1 modulo18, a>=19, put N=12*2^(a-5), z=2^a-1, p=(4z-1)/3 and q=4p+1. The actual annular coefficients provide +1 at p and -1 at q; S(p)=S(q)=z<p<q, so the one-row-pair current cancels these units before their shared future run. That run reaches2*3^(a-1)-1, whose ratio to both sources is unbounded. High future peaks therefore do not force merger while high. No future absorption is assumed for this identity.

The original feed pin ceb94fc372533e6fdc196595a817e8c01bc62d51 was audited: its R24 script/receipt was reproduced and all ten published sign/climb cells were independently rebuilt with capped paths. A later read at d2d85e1e49f0018a648c6daadc4fc93290c0d107 records the external withdrawal of the universal merger claim; the newer probes were not rerun in this batch. See [proof and review](../experiments/residual_progress/merger_scope/MERGER_SCOPE.md), [finite receipt](../experiments/residual_progress/merger_scope/merger_scope_audit.json), and [pinned reproduction](../experiments/residual_progress/merger_scope/external_review.json). Independent proof audit passed. Collatz remains open.

## R33 — Mixed shrinking pair rules with complete word cylinders

**Status: written partial recursion, exact binary-cylinder measure and finite certificates.**

For P(w)=delta_(3w)-delta_w, w=3 modulo8, set h=v2(3w-1). When h=2k+3 is odd, k>=0, z=3^k(3w-1)/2^h gives prefixes8z+1 and4z+1. If z=3 modulo8, the new O branch reduces to P(z) with positive orientation and z<w/2. When h=2k+2 is even, k>=1, the old canonical-z terminal rule remains. The new E1 branch z=29 modulo64 reduces to child(3z+1)/8<w/2; R30's E2 branch z=101 modulo128 has child(3z+1)/16<w/4. Both even branches subtract the child current. Their clock increments are k+1 for O and k+2 for E1/E2.

Every finite word in these complete branches, with arbitrary allowed k values, followed by a complete terminal cylinder has a unique nonempty binary cylinder. Backward inversion of each odd affine numerator retains all branch bits and proves actual positive integer realizations. Every such word lifts to an exponent class a=7 modulo16, giving the exact same-clock merger S^(a+l)(2^a-1)=S^(a+l)(2^(a-1)-1). New examples are a631 modulo2048 with l4, and a3655 modulo32768 with l6. Old canonical return height remains unbounded along each class.

The recognizer's exact binary-cylinder measure, conditional on w=3 modulo8, is32/157: terminal mass1/6, recursive masses1/6,1/96,1/192, and exact uniform child maps give the geometric sum. This is not a weighted R_N mass fraction, finite-integer asymptotic with growing depth, or repeatable contraction. Recognition terminates on every positive input, including explicit unresolved outcomes.

See [proof](../experiments/residual_progress/paired_completion/MIXED_SHRINKING_RULES.md), [constructor](../experiments/residual_progress/paired_completion/mixed_pairs.py), and [receipt](../experiments/residual_progress/paired_completion/mixed_pairs_audit.json). Checks cover4096 inputs,510 complete cylinders,28 long words through depth64,four actual Mersenne bridges,and one supplied-current conversion. At a631, x and its old return are absent from the elementary saturation of the supplied single lower-seed path; no claim is made about the unconstructed full U_N history. Independent proof/code review passed. Universal coverage remains open.

## R34 — Complete decreasing inverse ancestry and unbounded-return lower partners

**Status: written arithmetic extension, exact full-profile counting formula and finite currents.**

For canonical q, h=v3(q+1) and eta(q)=2^h(q+1)/3^h-1 give the unique maximal strictly decreasing canonical inverse chain. Its h edges have valuation1 and S^h(eta(q))=q. All such canonical valuation1 components are finite paths with unique minimum p, 3 not dividing p+1, and v2(p+1) states. The bridge has nonpositive rows and divergence delta_q-delta_eta(q). This local minimum is not a global ancestor minimum: q91+419904j has smaller ancestor27+131072j after eight ordinary arrows despite eta(q)=q. Advancing one quotient step is not well defined on the collapsed path classes without retaining exit information.

Apply eta to R26's normalized return. If the resulting p<N for8|N, a supplied U_N current certifies the full source weight. The recognized target q is already on supplied history because S^h(p)=q; the originating root x uses its additional R26 bridge and need not already be in R29's closure. Even-d returns have h0 and cannot improve. For odd d=2b+1 and elementary F-stratum k, h=min(b,v3(2k+1)) unless the two valuations coincide; the resonant case retains an exact valuation formula.

The small complete cylinder x19199 modulo65536 has q=(6561x+3745)/8192 and p=(2187x-117)/4096, with S^9(x)=S^2(p). Every actual source in it has p<N. For example at N65536, root84735 has q67865>N and p45243<N; its current is stored. The full extended count certifies1563 weighted units there versus1562 under R26. At N6144 the count stays146, so no improvement at that cutoff is claimed.

More generally, for every h>=2 set k=(3^h-1)/2,b=h+1,d=2h+3, and choose a with4/9<=lambda=3^a/2^(a+h+2+3^h)<2/3. An explicit complete binary cylinder of modulus2^K, K=a+2h+3^h+5, gives p=lambda*x+beta with -5/9<beta<-7/192, while q/x has limiting slope(3/2)^h lambda, unbounded with h. Thus p<N and q>x>N for every actual source in the cylinder. Exact merger time is S^(a+b)(x)=S^(h+1)(p). For each fixed h its weighted source count is25N/(72*2^K)+O(1), with error at most6, and both weight1 and weight2 cases occur on infinitely many required cutoffs. Periods depend on h; no uniform density for their union is asserted.

The complete extended profile also has an exact finite count using valuation-h intersections and exclusions in existing powers-of-three progressions, with at most O(log^5 N) arithmetic operations. No new leading coefficient for the entire profile is claimed. See [proof](../experiments/residual_progress/inverse_ancestry/INVERSE_ANCESTRY.md), [constructor and count](../experiments/residual_progress/inverse_ancestry/inverse_ancestry.py), and [receipt](../experiments/residual_progress/inverse_ancestry/inverse_ancestry_audit.json). Independent proof/code/count audits passed; all remaining branches stay explicit.

## R35 — General pair decomposition and exact scope of a restricted catalogue

**Status: written identities, complete static component classification and scoped counterfamily.**

For every complementary x=2^a t-1, let q=(x-1)/2 and 3^(a-1)t-1=2^d w. The exact smaller prefix satisfies S^(a-1)(q)=w. The remaining comparison after R26 is delta_f-delta_w, with f=3^k w for d2k+1 and f=2*3^k w+1 for d2k. It telescopes into tripling pairs T(u)=delta_(3u)-delta_u and, in the even case, one doubling pair D(u)=delta_(2u+1)-delta_u. The parameters can be larger than x; only two formal types does not imply a decreasing construction. Universal D(u) certificates are themselves equivalent to Collatz by strong induction; canonical D cases alone are already elementary.

Grant every hypothetical T(w) for w=3 modulo8 and combine it with all elementary identities, permitting both directions but no arbitrary forward arrows. On canonical minima the complete added edges are q→(q-3)/6 for q9 modulo48 and q→q/3 for q33 modulo48. Iterating these unique decreasing parents gives the exact full component label, even for paths using larger intermediates. Complementary canonical vertices with initial run length at least3 are isolated in this quotient graph.

For every a3 modulo16,a>=19, the actual required-ray root x2^a-1 has post-run pair(3w,w), w=(3^(a-1)-1)/8=1 modulo24. Their augmented labels remain distinct. This excludes completion by that specified one-run-plus-static-catalogue mechanism. It is not logical insufficiency of the hypothetical pair relation in a theory allowing other arguments. R36 resolves some of this family using additional ordinary arrows, consistently with the scope. See [proof](../experiments/residual_progress/pair_scope/PAIR_SCOPE.md), [local-current interface](../experiments/residual_progress/pair_scope/pair_scope.py), and [receipt](../experiments/residual_progress/pair_scope/pair_scope_audit.json).

## R36 — Two shrinking entries from the missing 1-modulo8 pair domain

**Status: written partial bridges, complete mixed cylinders and actual smaller-seed mergers.**

For P(w)=delta_(3w)-delta_w with w=1 modulo8, branch A has w17 modulo128 and child v=3(w-1)/16. Writing w16u+1 gives S(3w)=F(18u+1), S(w)=F(3u), and18u+1 is the selected partner of9u. Branch B has w105 modulo256 and v=(9w-1)/16=11 modulo16; two ordinary steps give selected partners2(3v)+1 and2v+1. Both have0<v<w and v3 modulo8. Their local current divergence is P(w)-P(v), so both add the child current. Child clocks l>=2 become l+1 and l+2 respectively.

Every mixed child cylinder v=r modulo M gives the complete A parent3w=16r+3 modulo16M. If r11 modulo16 it also gives the complete B parent9w=16r+1 modulo16M. CRT supplies positive integer witnesses. Binary exponent lifting realizes the parents in the separate a3 modulo16 Mersenne family. Terminal examples yield a1699 modulo4096 with merger time a+4, and a659 modulo4096 with time a+5, between2^a-1 and its smaller half2^(a-1)-1. The old normalized returns remain unbounded relative to the source. Parent and child failures stay unresolved; a147 is one explicit child failure.

See [proof](../experiments/residual_progress/pair_one/MISSING_PAIR_DOMAIN.md), [constructor](../experiments/residual_progress/pair_one/pair_one.py), and [receipt](../experiments/residual_progress/pair_one/pair_one_audit.json). Checks cover4096 domain inputs,213 complete mixed-cylinder examples,71 exponent lifts,four actual Mersenne bridges,and supplied-current conversions. The a659 conversion reconstructs3200 rows from its smaller input under a10000-step discovery cap; an11-row current for315 is stored. Weight2 scaling and the exact existing-edge extraction are checked. Independent proof/code reviews passed. No universal completion or new global source fraction follows.

## R37 — An exact critical tripling domain and conditional decreasing plans

**Status: written equivalence and explicit conditional compiler; finite checks.**

Let `P(w)=delta_(3w)-delta_w` and `W={w=5 mod8} union {w=9 mod16}`. The map `w -> nu(3w)` is a bijection from W onto the complementary canonical roots q not2 modulo3, with inverse `q/3` for q0 modulo3 and `(2q+1)/3` for q1 modulo3. Each inverse is smaller than q. All other least-counterexample cases have an elementary normalization, a forward descent, or a smaller exact predecessor. Therefore universal finite exact currents for P on W are equivalent to Collatz. This identifies the full missing input domain; it supplies no universal pair currents.

Separately, the formal graph with every elementary identity and every hypothetical tripling edge is connected by a terminating normalizer. Each invocation decreases q−1 by at least a factor2/3. The logarithmic invocation count bounds missing input requests, not the cost or discovery of those currents. The compiler rejects absent or incorrect pair inputs and retains every signed boundary. The static theorem includes selected halving; it makes no claim for F and tripling alone.

Proof and implementation: [critical tripling domain](../experiments/residual_progress/tripling_equivalence/TRIPLING_EQUIVALENCE.md), [compiler](../experiments/residual_progress/tripling_equivalence/tripling.py), [checker](../experiments/residual_progress/tripling_equivalence/check_tripling.py). Bounded checks cover16384 local steps,2048 complete formal plans and40 compiled examples with explicitly supplied, capped input currents. Stored examples include27 and31. No annular source-capacity or universal construction claim follows.

## R38 — Complete odd-h interface, critical input compiler and exact ternary scope

**Status: written complete arithmetic interface, conditional compiler and scoped obstruction; finite checks.**

For `Q(z)=delta_(6z+1)-delta_z`, every positive odd z has an elementary current with divergence Q(z)−P(u), where u=z if3z is canonical and u=4z+1 otherwise. Hence every actual odd-h P(w) run reduces to one P(u), with the child current added. Every h>=7 branch has u<7w/8; direct low-h branches also shrink. The nondirect h3 and h5 branches expand as `(3w+1)/2` and `(9w+5)/8`, with complete infinite examples. A prescribed parent clock is `k+1+max(ell,A)`; the maximum cannot be dropped. Child domains may be unproved W domains, so a shrinking interface is not a universal constructor.

The whole static R35 catalogue connects Q(z)'s endpoints exactly for z3 modulo8. On the missing z domain, `g(z)=nu(6z+1)` bijects onto the critical roots of R37, with z<=g(z)/3. Exact or one-sided Q currents for `I_M={z not3 mod8:g(z)<=M}` compile to an exact nonnegative U_M current using only supplied graph rows; U_M also supplies exact inputs for I_M. The universal statement is therefore Collatz-equivalent, and the finite compiler supplies none of its missing inputs.

Actual odd-h parameters range over exactly `Zplus={z:unit3(z)=1}`. Their critical images have unit3(q)=1 when q0 modulo3 and unit3(q−1)=2 when q1 modulo3. The complementary phases cannot be silently supplied by that restriction. Adding x10 modulo27 to R31's repeated word gives arbitrarily long growing actual weight2 prefixes that avoid all descending covered-phase substitutions, even after elementary normalization and decreasing valuation-one inversion. This excludes a bounded test using those operations. It does not prove logical insufficiency of universal Zplus currents or exclude full supplied-history closure.

Proof and code: [complete odd-pair interface](../experiments/residual_progress/odd_pair_closure/ODD_PAIR_INTERFACE.md), [implementation](../experiments/residual_progress/odd_pair_closure/odd_interface.py), [checker](../experiments/residual_progress/odd_pair_closure/check_odd_interface.py). Checks cover8192 Q interfaces,2731 odd-h reductions,528 exact parameter cases,171 clocks,14 expanding examples,16 actual ray witnesses through128 word pairs and exact/one-sided compilations at M64,128,512. Full U128 input and output currents are stored. No universal coverage or new global mass fraction follows.

## R39 — Coupled even-pair recursion escapes a complete split-catalogue obstruction

**Status: written exact identities and partial constructor, complete cylinders and stored finite currents.**

For d4 the old split algorithm uses elementary D(9w), then separate R33/R36 calls for P(w) and P(3w). Its exact success set is `w=105 mod256` with R33 accepting `(9w−1)/16`. In particular R33 can never accept both P(v) and P(6v+1): simultaneous acceptance would repeat the same condition at a strictly smaller positive parameter. This is an algorithm-specific obstruction.

Retaining `C(v)=delta_(18v+3)-delta_v` instead supplies a new state. For every `v=19 mod32`, its child `t=(3v−1)/8<3v/8` has an explicit local current of divergence C(v)−C(t), including the previously rejected child class7 modulo8. The terminal cylinder `v=39 mod8192` has `S^5(18v+3)=S^7(v)`. Depth r gives a complete cylinder modulo `2^(13+3r)` and clocks r+5 versus r+7. The extra valuation bit is retained, and every child current is added.

This closes additional d4 comparisons from the A entry `w=17 mod128` at equal original half-seed clock a+r+7; the successful B entry gives a+ell+2, initially a+5. Complete original-source cylinders exist for every a>=2. Their old normalized return exceeds x for a>=5 and has unbounded ratio as a grows. For each fixed cylinder of period L and cutoff8|N, the exact full-weight count is `25N/(72L)+error`, |error|<=6; this is not a global family-union asymptotic. Both actual source weights and supplied lower-input conversions are retained.

Proof: [coupled even-pair closure](../experiments/residual_progress/even_pair_closure/EVEN_PAIR_CLOSURE.md). [Implementation](../experiments/residual_progress/even_pair_closure/even_pairs.py) and [checker](../experiments/residual_progress/even_pair_closure/check_even_pairs.py) cover57 joint cylinders through depth64,8192 split inputs,8192 paired nonacceptances,384 original cylinders,12 required-ray sources,24 exact counts and two full weight2 conversions with stored tables. The joint recognizer remains partial. This does not close all d4, all even d, or R37's critical domain.

## R40 — Complete critical-nine elimination leaves a single sufficient pair class

**Status: written equivalence and terminating finite conditional compiler.**

For every w9 modulo16 there is an explicit finite integer current J and finitely supported signed integers c(u), with u5 modulo8, such that `div J=P(w)-sum c(u)P(u)` and every requested u is at most `(9w+3)/4`. Therefore universal finite exact P currents on **5 modulo8 alone** are Collatz-equivalent. This removes a whole independent premise domain; it does not construct the remaining inputs or prove descent within W5.

Put d=v2(9w-1). Prescribed equal-length prefixes give a sibling pair P(z) when d=2k+5, and the joint source `[6z+1]-[2z+1]` when d=2k+4. Complete critical plans on these endpoints have every W9 request strictly below w. The only possible nondecreasing request is one positive W5 input on d4,6,8 when3z is noncanonical; its exact values are `(9w+3)/4`, `(27w+13)/16`, `(81w+55)/64`. All other requests are smaller. The even-branch parameter z has ternary unit2, outside R38's unit1 parameterization. Expanding W9 requests recursively therefore terminates, preserving signs and cancellations. Missing or malformed W5 currents are rejected at substitution.

The identity at w9 retains `P21-P5`; it cannot justify a circular rule for P21. Conversely, exact signed cancellation removes every premise at w1561 and gives an explicit nine-row current, a finite example only. See [proof](../experiments/residual_progress/w9_closure/CRITICAL_NINE_ELIMINATION.md), [compiler](../experiments/residual_progress/w9_closure/w9_closure.py), and [receipt](../experiments/residual_progress/w9_closure/w9_closure_audit.json). Checks cover4096 local identities,4096 sharper endpoint bounds,616 exact high-valuation cases,256 recursive reductions,10 actual substitutions and four rejection cases.

## R41 — A complete decreasing W5 phase, an exact returning branch, and an exhaustive inverse barrier

**Status: written exact identities, conditional construction, sufficient-set refinement and scoped obstruction.**

Every positive odd q4 modulo9 has a smaller ancestor `p=2^h(2q+1)/3^h-1`, h=v3(2q+1)>=2, with exact ordinary word `1^(h-1),2`. Apply this to the whole domain `E={w5 mod8:3|w and3w selected}`. The canonical q=(3w-1)/2 has predecessor p, whose critical pair index v satisfies `v<8w/9`. An exact current reduces P(w) to P(v) plus absorption of v and nu(w), both smaller than w. Absorption of any seed s has a formal plan using only W5 indices below s: every original W9 request is at most s/3, so R40's expansion stays below s.

After eliminating W9, **every input decreases precisely on E_good={w in E:w not3 mod9}**. Universal P currents on W5 minus E_good already suffice by strong induction. On the returning row w3 modulo9, the W9 d4 rule requests the original w with coefficient+1. The infinite cylinder w21 modulo2304 realizes this; the P21 plan is exactly the tautology with zero current and its own sole request. The compiler rejects self-dependency. These are loops in the recipe, not positive Collatz cycles.

Separately, if canonical q>1 satisfies q1 modulo3^D, then every predecessor under1 throughD complete quotient steps T=nu S is larger than q. The proof exhausts every unbounded inverse ray. Shadow each affine inverse branch at1; all slopes/intercepts satisfy a-b>=1, and the first step gives a strict gap `lambda-(c+1)/2>0` that persists. The exact smallest predecessor over these lengths is `(4q-1)/3`; all off-spine states exceed4q+3. CRT gives infinitely many such critical q7 modulo32 at every depth, with W5 index5 modulo64. This rules out bounded-depth ancestor descent even after complete elementary normalization. It does not rule out forward excursions, supplied history, unequal-time mergers, or input-dependent unbounded inverse depth.

See [proof](../experiments/residual_progress/critical_inverse/CRITICAL_INVERSE.md), [constructor](../experiments/residual_progress/critical_inverse/critical_inverse.py) and [receipt](../experiments/residual_progress/critical_inverse/critical_inverse_audit.json). Checks cover1820 phase currents,1024 W5 absorption plans,683 E plans (455 descending and228 self-dependent),24 actual substitutions,73 inverse-affine cases,2478 finite inverse words,27 CRT examples throughdepth128 and six independent all-origin checks throughdepth6. Exact P69 and P117 tables are retained in the receipt. Universal completion of the reduced sufficient set is open.

## R42 — Complete joint-source interfaces retain an unbounded positive frontier

**Status: written full arithmetic interfaces, explicit growing prefixes and actual required-ray examples; scoped failure of a proposed closure.**

For every C(v)=[18v+3]-[v], v3 modulo4, a two-case table gives both exact two-arrow endpoints. On v3 modulo8 the lower endpoint is z=(9v+5)/2^(a+1), a=v2((9v+5)/2), and the upper is9·2^(a-1)z−7. On v7 modulo8 they are z=(9v+5)/4 and oddpart(9z−7). This full interface is not a closed shrinking C family.

The whole previously unresolved v3 modulo32 class has parameters t=(3v-1)/8,h=v2(3t+1),u=S(t), with u<=(9v+5)/32<=v/3. An exact prescribed block yields `C(v)=div L+[q]-[u]`, where j=floor((h-2)/3), s=h-1-3j and `q=2^s*3^(2j+3)u-5`; clocks are3+2j and2. The binary exponent decreases while the ternary coefficient increases. Every q22 modulo27; when critical, it occupies an omitted R38 phase. The residual is retained.

For v_r=(2^(6r+5)-5)/9, the lower seed absorbs in two arrows while q_r=2·3^(4r+3)-5 is canonical and q_r/v_r tends to infinity. For every positive multiple r of27 this embeds in an actual weight1 residual root `x_r=(2^(6r+15)-3365)/81` at required cutoff `N_r=12·2^(6r+5)`, with N_r<x_r<9N_r/8. Its smaller half absorbs in four arrows; the prescribed4r+7-arrow prefix from x ends at q_r, whose ratio to x is unbounded. This exhibits no permanent nontermination and excludes only a linear height bound for that block. The negative-cycle shadow constants are not a positive cycle.

See [proof](../experiments/residual_progress/joint_frontier/JOINT_FRONTIER.md), [constructor](../experiments/residual_progress/joint_frontier/joint_frontier.py), and [receipt](../experiments/residual_progress/joint_frontier/joint_frontier_audit.json). Bounded checks cover8192 whole-interface cases,2048 full subdomain cases,45 exact parameter pairs,11 expansion examples,five d4 embeddings and four required-ray sources. The stored r27 current is explicitly unfinished and retains its positive frontier; its four-row lower absorption input is stored separately. Full C closure remains open.

## R43 — Critical-image rank and finite signed composition

**Status: written bounds, sufficient-set theorem and conditional compiler.**

Use `rho(w)=nu(3w)` on W5 union W9. In a fully expanded R40 plan for w in W9, every W5 request u satisfies `8rho(u)<=27w+5`. The exceptional d4/6/8 ranks are `(27w+5)/8`, `(81w+23)/32`, `(243w+101)/128`; only d4 can increase rank. Induction on the decreasing W9 indices preserves the bound. Hence every request in the W5-only absorption plan H_s satisfies `rho(u)<=(9s+5)/8`. A critical root p has lower index v<=(2p+1)/3, so every H_v input has rank at most(3p+4)/4<p.

Any finite signed rule with boundary `P(w)-sum c(u)P(u)` and all requested ranks strictly below rho(w) composes by strong induction. Universal currents on the complement of its accepted domain suffice for Collatz. Finite unions use the same rank; pair indices may increase. The fixed-priority R41/R45/R44/R46 compiler terminates its formal expansion and retains unhandled leaves. It never constructs those missing currents automatically.

See [proof](../experiments/residual_progress/critical_rank/CRITICAL_IMAGE_RANK.md), [compiler](../experiments/residual_progress/critical_rank/rank_closure.py), [union](../experiments/residual_progress/critical_rank/rules_union.py), and [receipt](../experiments/residual_progress/critical_rank/critical_rank_audit.json). Checks cover2048 W9 plans,4096 absorption plans,1024 union candidates (195 accepted),58 mixed closures and seven actual substitutions. P1029 closes with no input through signed cancellation; P749 has stored inputs and output. These examples and counts give no universal coverage statement.

## R44 — Complete returning forward interface with decreasing subdomains

**Status: written whole-domain conditional identity and strict-rank rules on specified subdomains.**

For every returning w5 modulo8,w3 modulo9,3w selected, write `3w=2^a t-1`, a>=3, t=3^a modulo4,2^a t=10 modulo27. Then q=rho(w)=2^(a-1)t-1 reaches r=(3^(a-1)t-1)/2 by word1^(a-2),2. With z=nu(w), the current `N_(3w)+prefix-N_w+H_r-H_z` has exact P(w) boundary minus the signed difference of the two input vectors. Every lower request already has smaller rank. The complete canonical endpoint table bounds the upper ranks and gives a decidable sufficient descent test.

The test holds on every a3 input with r noncanonical or1 modulo8, and every a4 input with r noncanonical. For arbitrary a>=3, taking k>=1 with `4^k(2^(a+3)-20)>3^(a+1)-3` and r=F^k(s) gives complete nonempty CRT families with arbitrarily long rising runs. The proof retains exact stratum thresholds and intercepts. For the original run, prescribed absorption undoes only prefixes through a-3; at a-2 the endpoint is1 modulo8 and takes its forward step. The full R41 inverse at r undoes the entire run. These are failures of specified compositions, not all forward comparisons.

See [proof](../experiments/residual_progress/returning_phase/RETURNING_FORWARD_INTERFACE.md), [constructor](../experiments/residual_progress/returning_phase/returning_phase.py), and [receipt](../experiments/residual_progress/returning_phase/returning_phase_audit.json). Checks cover2048 bounds,228 returning inputs (126 rank-descending),456 undo checks,96 CRT examples through a128 and12 actual substitutions. Index decrease alone is insufficient for the common rank: w6645 requests4205<w but rho4205=12615>9967=rho6645. This case remains unresolved.

## R45 — Complete base inverse phases allow increasing pair indices

**Status: written classification of both specified base rays and strict-rank sufficient-set reduction.**

For w in W5 with3w nonselected, let k=4 or8, h=v3(kw+1), C=(kw+1)/3^h and p=2^(h+1)C-1. The exact inverse bridge uses h valuation1 arrows followed by the quotient bridge from2kw+1 to3w. For h>0, p is complementary canonical. The rank decreases exactly when h>=3 for k4 or h>=5 for k8. Thus the entire accepted domain is `w20 mod27 or w91 mod243`, with the nonselected and W5 conditions retained. Its leading child v has rank p; R43 bounds H_v requests below p and H_nu(w) requests below the parent rank3w.

The narrower index-decreasing subset has17 classes modulo729, while the rank-decreasing phase has30. Example1613 requests2549 yet drops4839→3823 in rank. The remaining positive-h cases are completely classified for these two base rays: h1,p0 gives the literal zero-current request{w:1}; every other failure retains a unique largest-rank W5 child with coefficient+1. Other ray indices, words or forward comparisons are not excluded.

See [proof](../experiments/residual_progress/nonselected_inverse/NONSELECTED_INVERSE_PHASES.md), [constructor](../experiments/residual_progress/nonselected_inverse/inverse_phases.py), and [receipt](../experiments/residual_progress/nonselected_inverse/nonselected_inverse_audit.json). Checks cover4096 nonselected inputs,2731 positive-h plans,288 exact parameter examples through h24,911 self-returns and four actual substitutions. The1613 input and current tables are stored. Universal supply outside the removed phase remains open.

## R46 — Variable-depth inverse escape and a fixed-precision barrier

**Status: written exact two-block criterion, decreasing W5 rule and scoped complete-inverse obstructions.**

For canonical q>1,q1 modulo3, set D=v3(q-1),u=(q-1)/3^D,j=v3(4^D u+2),p=2^j(4^D u+2)/3^j-1. The exact word1^j,2^D takes p to q. It has p<q iff `2^(2D+j)<3^(D+j)`; parity excludes small-u exceptions. For selected W5 roots q=(3w-1)/2, require both j>=2 and the strict slope inequality above. Then p<q and p7 modulo8. One critical step and the R43 absorption bound give only W5 requests with both smaller indices and smaller ranks. The new D>=2 domain has w1 modulo3 and is disjoint from R41 E. Every admissible D,j has a complete CRT family.

For every canonical q>1,q1 modulo9, no smaller quotient ancestor exists throughdepth3. At depth4 one exists iff q10 modulo81; it is uniquely(64q-73)/81 with word1,1,2,2. More generally R41's D-step barrier extends throughD+1 for D>=2. A separate family q=7+32*3^D*t,D>=2,t>=1 has fixed v3(q-1)=1 but no smaller canonical ancestor throughD steps, including every inverse ray. After k=1 or2 forward arrows, no inverse origin below q exists throughD+k quotient steps; equality only retraces the original path. This excludes depth bounds based only on that valuation and the specified short-forward repair, not arbitrary excursions or currents.

See [proof](../experiments/residual_progress/inverse_escape/INVERSE_ESCAPE.md), [constructor](../experiments/residual_progress/inverse_escape/inverse_escape.py), and [receipt](../experiments/residual_progress/inverse_escape/inverse_escape_audit.json). Checks cover2731 word cases,444 parameter examples through D256/j182,317 strict plans,16 actual substitutions,227 depth4 targets,3229 finite inverse words,48 long-ray words and15 complete small-origin checks. Three full current tables are retained. The unbounded statements rest on the written proof.

## R47 — Complete inverse interface for nonselected multiples of three

**Status: written exact two-block classification, decreasing subdomains and retained failure vectors.**

For w in W5 with3|w and3w nonselected, put D=v3(w),u=w/3^D. For each k4 or8, its base predecessor b=2kw+1 has maximal inverse blocks of lengths D and j=v3(k4^D u+1), giving `p=2^(j+1)(k4^D u+1)/3^j-1` and ordinary word1^j,2^D from p to b. The final quotient bridge reaches3w. Exactly one k has j>0. The endpoint decreases iff `k*2^(2D+j+1)<3^(D+j+1)`; this forces j>=4 and a W5 critical child. R43 bounds every auxiliary input below the parent rank.

The classification includes every failed branch after full formal substitution. At j0 the current is zero and the sole request is w. At a failed positive-j W5 child, that child has the unique largest rank. The j1,p0 row has a W9 return with exact formal defect `P(w)+H_C-e_C-H_(S(C))`, C=(k4^D u+1)/3. The parent or the defect's leading child is uniquely largest, according to C<3w or C>3w; no descent is hidden by cancellation. Both terminal ternary phases have full CRT families at every D; j=2D+6 is an explicit sufficient choice. This entire accepted domain is outside the earlier four direct rule domains.

See [proof](../experiments/residual_progress/nonselected_multiples/NONSELECTED_MULTIPLES.md), [constructor](../experiments/residual_progress/nonselected_multiples/multiple_escape.py), and [receipt](../experiments/residual_progress/nonselected_multiples/nonselected_multiples_audit.json). Checks cover682 inputs,1364 plans,240 CRT cases,24 farther families and four actual substitutions. The stored16653 example requests31189 while rank falls49959→46783. Remaining inputs and other inverse words are not settled.

## R48 — Complete forward blocks and exact low-exponent tests

**Status: written whole-domain conditional interface and exact classification of its rank test for a3/a4.**

For every nonselected W5 input, write q=3w=2^a t-1, d=v2(3^(a-1)t-1),u=(3^(a-1)t-1)/2^d. The R26 endpoint is f=3^floor(d/2)u for odd d, or2*3^(d/2)u+1 for even d. Its exact quotient return time is a+floor(d/2)-1. Odd d instead has ordinary comparison clocks a+(d-1)/2 versus1; even d is an ordinary path of length a+d/2-1. The formal current `D_q-N_w+H_f-H_nu(w)` retains every signed W5 request. R44's full canonical endpoint bound B(nu(f))<q gives a strict-rho rule.

For a3, the test accepts exactly: odd d; even d>=6; or a selected even endpoint f. For a4 it accepts exactly: odd d; even d>=10; or selected even f with d>=6, or d4 and nu(f) not3 modulo8. All intercepts are included. Complete multiples-of-three classes45 modulo384 and741 modulo768 lie inside this domain. For each a>=3 an explicit sufficiently large odd d and exact CRT progression give further accepted multiples of3. These are classifications of this sufficient test, not of all possible currents.

For a canonical even endpoint, the R46 maximal inverse parameters are D=d/2,j=a-1 and its predecessor is exactly q: it reverses the same block and cancels the current literally. See [proof](../experiments/residual_progress/nonselected_forward/NONSELECTED_FORWARD.md), [constructor](../experiments/residual_progress/nonselected_forward/nonselected_forward.py), and [receipt](../experiments/residual_progress/nonselected_forward/nonselected_forward_audit.json). Checks cover2047 inputs,1536 a3/a4 decisions,687 undo identities,75 CRT examples through a128,32 multiple3 phase examples and12 actual substitutions. Three current tables are retained; universal endpoint coverage is open.

## R49 — Permanent inverse-only exclusions coexist with short forward progress

**Status: finite all-depth exclusion certificates, a general operation-scope theorem and written all-ray lifts.**

If a canonical set Q is T-forward-closed and q is outside Q, no inverse ancestor of q belongs to Q. Thus inverse-only search cannot enlarge full supplied-history saturation. This does not prevent a uniform inverse formula from proving membership or supporting induction without materializing that history. A finite closed Q containing every canonical origin below b but excluding b proves that b has no smaller canonical ancestor at any depth.

Stored exact tables give this certificate at b39 (w13) and b135 (w45,3|w), with43 and68 states. Both nevertheless enter verified smaller-origin history in exactly three quotient arrows:39→59→89→33 and135→203→305→57. Exact lower absorption inputs and tripling currents are stored. Hence even unlimited inverse-only descent is not a universal completion on the remaining critical domain.

For b39,D>=2 or b135,D>=4, the family q=b+256*3^D*t,t>=1 preserves the forward cylinder yet has no smaller canonical inverse origin throughD steps, including every ray. The shadow proof uses the all-depth minimality of b and the strict affine gap lambda-(c+1)/(b+1). These families have fixed v3(q), respectively1 and3. Whole cylinders w13 modulo256 andw45 modulo128 have strict-rho three-step forward plans; they are contained in R48 and add no independent coverage. There are also infinitely many inverse-minimal absorbed canonical roots: otherwise finitely many finite absorbed forward orbits would cover the infinite absorbed canonical set. This last infinitude statement does not claim the roots all lie in the critical W5 class.

See [proof](../experiments/residual_progress/inverse_scope/INVERSE_SCOPE.md), [certificate verifier](../experiments/residual_progress/inverse_scope/inverse_scope.py), and [stored closed tables](../experiments/residual_progress/inverse_scope/anchor_certificates.json). Complete finite checks verify the certificates and forward resolutions; arbitrary-depth lifting rests on the written invariant, not a truncated search.

## R50 — Two inverse phases cross an intermediate increase

**Status: written complete endpoint test within the second-depth L>=3 domain and a strict-rank constructor.**

For nonselected W5 with3 not dividing w, choose k4 when w2 modulo3 andk8 otherwise. Set h=v3(kw+1)>=1,C=(kw+1)/3^h,r=2^(h+1)C-1,L=v3(2r+1)>=3,p=2^L(2r+1)/3^L-1. R45 gives a current with boundary[3w]-[r]; R41 gives one with boundary[r]-[p]. The combined bridge precedes every missing-current request. Exactly p<3w iff h+L>=5(k4) or>=6(k8); four explicit below-threshold cases prove necessity without small-input exceptions.

Since p7 modulo8, its critical child is W5 and all final requests decrease rho by R43. The new domains are k4:h1,L>=4 orh2,L>=3; k8:h1,L>=5,h2,L>=4,orh3/4,L>=3. Every one has r>3w but p<3w and a complete nonempty CRT family. Examplew53 compares159 with283 and then111 through inverse phases; this order is not the forward orbit. Inputs with L<3 and failed tests remain unhandled by this result.

See [proof](../experiments/residual_progress/double_inverse/DOUBLE_INVERSE_PHASES.md), [constructor](../experiments/residual_progress/double_inverse/double_inverse.py), and [receipt](../experiments/residual_progress/double_inverse/double_inverse_audit.json). Checks cover153 two-phase inputs,65 strict plans,408 exact CRT cases throughh128/L128 and four actual substitutions. The53 input and output are stored. The [expanded union](../experiments/residual_progress/double_inverse/expanded_union.py) combines seven strict-rho rules, preserving the earlier priority and explicit unresolved leaves. Its [receipt](../experiments/residual_progress/double_inverse/expanded_union_audit.json) covers1024 candidates,442 accepted rules,258 mixed closures and eight actual substitutions, with three full stored outputs. Those counts give no asymptotic or universal coverage theorem.

## R51 — A separate rank removes the absorption-bound overhead

**Status: written uniform rank bound, complete forward domain and conditional compiler.**

Define sigma(w)=rho(w) except on E_return, where sigma(w)=4w/3−1=(8rho(w)−5)/9. Every W5 request in the unchanged formal H_s has sigma<=nu(s). In R40's only rank-expanding d4 row, the exceptional index u=(9b+3)/4 is returning and has sigma(u)=3b; all other local or recursive requests have sigma<3b. This proves the uniform bound by the original decreasing critical plan. A complete first-step endpoint table sharpens it further.

Every nonselected input with first a5 and odd d>=3 now has an accepted sigma forward plan. The exact a5,d3 domain is w437 modulo512: q=32t−1, f=(243t−3)/8<q. At w44981 the child96069 increases rho134943→144103 but decreases sigma134943→128091. Conversely, the valid old-rho R44 plan at4629 requests2197, increasing sigma6171→6591. Thus the two inductions cannot be mixed automatically. The separate sigma dispatcher preserves nonreturning old rules and retests returning inputs.

See [proof](../experiments/residual_progress/phase_rank/PHASE_RANK.md), [constructor](../experiments/residual_progress/phase_rank/sigma_rank.py), and [receipt](../experiments/residual_progress/phase_rank/sigma_rank_audit.json). Checks cover1024 W9 eliminations,4096 absorption plans,132 exact progression examples through index2^128 and five actual substitutions; the44981 certificate is stored. On1024 candidates the sigma/old-rho domains have sizes459/442 with441 shared, illustrating their incomparability rather than universal coverage.

## R52 — A complete second forward interface for returning inputs

**Status: written conditional interface, exact low-exponent classification and complete CRT families.**

Compose R44's full returning prefix q→r, complete normalization r→nu(r), and a prescribed next forward block before requesting any H. The final signed current is N_(3w)+G+N_r+D−N_w+H_f−H_nu(w), accepted when the old-rho endpoint bound B(nu(f))<rho(w). Quotient clocks add; the intervening signed normalizer is not zero ordinary elapsed time. Some previously good tests worsen under the alternate path, so preserve prior accepted rules.

The entire first a3 failure corresponds exactly to complementary canonical r157 modulo243, with q=(8r−5)/9 and w=(16r−1)/27. For next exponents A2/A3/A4 the complete endpoint test is classified, including all affine offsets and arbitrarily large next d. For every original a>=3 and second A>=2, exact CRT families with sufficiently large odd d fail R44 but pass the new comparison. The full original ternary modulus3^(a+2) and exact binary bit2^(d+1) are retained. These families are outside all seven earlier direct domains; no claim about all earlier supplied history follows.

See [proof](../experiments/residual_progress/returning_continuation/RETURNING_SECOND_BLOCK.md), [constructor](../experiments/residual_progress/returning_continuation/returning_continuation.py), and [receipt](../experiments/residual_progress/returning_continuation/returning_continuation_audit.json). Checks cover910 returning inputs,768 exact low-exponent cells,132 long families through a=A=64 and eight actual conversions. Three complete outputs are stored. The bounded scan has184 new acceptances and23 cases where this alternate path worsens the old test; those are finite counts.

## R53 — Complete low-block continuation through unbounded prescribed growth

**Status: written complete phase table, maximal repeated-block interface and infinite decreasing-exit families.**

After a failed R48 first block with a3/a4, the whole domain whose next canonical exponent is2 has exactly eight first-phase rows. A full second block has an exact endpoint-test classification in each row; all odd second depths pass. The proof retains every affine intercept, including the odd generic bound(81n+133)/256. Actual current acceptance uses the original rho throughout.

The entire raw(a,d)=(2,2) pattern is x27 modulo32, with G(x)=(9x+5)/8. Its maximal length is floor((v2(x+5)−2)/3), and its three exit phases are explicit. In the remainder4 stratum after a first(3,2) block, w=(2^(3r+8)s−11)/9 takes r growing blocks to16*9^(r+1)s−5 before a final block. For every r>=1, a complete CRT family with d=4r+3 has a strict-rho endpoint below the original parent bound. All intermediate currents are retained before H; ordinary clocks are(4r+6,1), quotient length4r+5. The extra w45mod81 condition excludes all seven earlier direct rules.

See [proof](../experiments/residual_progress/forward_continuation/FORWARD_CONTINUATION.md), [constructor](../experiments/residual_progress/forward_continuation/forward_continuation.py), and [receipt](../experiments/residual_progress/forward_continuation/forward_continuation_audit.json). Checks cover570 complete table cases,224 maximal runs,56 CRT witnesses through r64 and three actual substitutions. The4258701 fixture stores its six inputs and65-row completed current. The [continued rho compiler](../experiments/residual_progress/continued_rules/continued_rules.py) adds R52/R53 after the earlier seven rules; its [receipt](../experiments/residual_progress/continued_rules/continued_rules_audit.json) preserves all442 earlier acceptances among1024 inputs and adds51, with six actual substitutions. It does not import the separate sigma rules.

## R54 — Growing positive prefixes retain an unhandled leading input

**Status: written arithmetic families and scoped obstruction to a specified lookahead/closure procedure.**

The entire phase w3445 modulo3456 has selected3w, w1 modulo3 and q=rho(w)=−17 modulo5184. Its inverse parameters D2,j1 exclude R46; the other eight direct predicates then available also fail. R55–R57 now resolve parts of this phase by additional comparisons. For any r>=1,s>=1, choose q=81*2^(11r+6)*s−17. Its first7r quotient steps repeat a complete affine word with return Psi(q)=(2187q+2363)/2048 and Psi(q)+17=(2187/2048)(q+17). All actual states are positive and every noninitial prefix exceeds the initial q. The negative shadow only records congruences; the seed changes with r.

Each cycle's critical states comprise two W5 endpoints and an intermediate W9 input. Complete d6 W9 elimination retains the next W5 endpoint at coefficient+1. For every prefix length n<=7r, appending the deterministic H gives a unique largest-rank unaccepted request: the current cycle's input at positions0–2, or the next cycle's input at positions3–6. All other requests are smaller, so further strict-rho expansion using those nine rules cannot cancel this leading coefficient. R52/R53 remain inapplicable at the lead. A separate sigma argument holds because sigma=rho on the lead and every other sigma rank is smaller; arbitrary mixing of the ranks remains invalid.

See [proof](../experiments/residual_progress/rule_avoidance/RULE_AVOIDANCE.md), [constructor](../experiments/residual_progress/rule_avoidance/rule_avoidance.py), and [receipt](../experiments/residual_progress/rule_avoidance/rule_avoidance_audit.json). Checks cover256 phase inputs,48 positive families through128 cycles,148 lookahead positions,20 full W9 plans and two separately ranked auxiliary expansions. Three unfinished currents are stored. This rules out a fixed lookahead guarantee for the stated procedure; it does not rule out another current representation, a supplied-history argument, input-dependent unbounded depth, or another comparison, and gives no forever-growing positive orbit.

## R55 — Complete forward tables for selected critical-five inputs

**Status: written full conditional interfaces, complete low-exponent tests and infinite decreasing arithmetic domains.**

For selected3w and w5 modulo8, q=rho(w)=(3w−1)/2=2^A t−1 is complementary canonical, with A>=2. Apply the complete R26 block, including its raw endpoint f and elementary normalization, before requesting H. The exact plan is `N_(3w)+D_q+N_f−N_w+H_nu(f)−H_nu(w)`. It strictly decreases rho whenever the complete branchwise endpoint bound B(nu(f))<q. The first-block table is exact for A2,3,4. After the failed first A2d2 block, a complete second-block table is exact for second exponents2,3,4. All signed W5 requests and ordinary versus quotient clocks remain explicit.

Every selected w2 modulo3 is outside the old nine direct predicates. For each A>=2 an exact CRT progression with sufficiently large odd depth d passes the new test. Examples are221 modulo384 and2813 modulo3072. Inside the old R54 entry phase, the entire progression10357 modulo13824 has A4d3 and decreases. The proposed replacement3445 modulo13824 is false:58741 and86389 are persisted counterexamples;3445 itself passes a different A4d4 branch. The maximal inverse of the first failed A2d2 endpoint exactly undoes that block, motivating the second forward comparison.

See [proof](../experiments/residual_progress/selected_forward/SELECTED_FORWARD.md), [constructor](../experiments/residual_progress/selected_forward/selected_forward.py), and [receipt](../experiments/residual_progress/selected_forward/selected_forward_audit.json). Checks cover2049 selected inputs below32768,256 second-block inputs,683 old-rule exclusions,78 CRT examples through A128,128 progression points and four actual substitutions. The finite window has905 new acceptances; this is no asymptotic coverage claim. Two completed output currents and their supplied inputs are stored. Universal selected-phase supply remains open.

## R56 — Two selected inverse choices and fixed-length escape through arbitrary forward depth

**Status: written exhaustive classification of two specified inverse plans, exact decreasing domains and conditional constructors.**

For selected3w with w5 modulo8,w16 modulo27, put q=(3w−1)/2 and v=(16w−13)/27=−7 modulo128. The inverse word1,2,2 reaches q from3v>q. From that intermediate state choose k4 or8, h=v3(kv+1), C=(kv+1)/3^h, and r=2^(h+1)C−1. The full ordinary words r→q are `1^h,2,1,1,4` and `1^h,2,3,2,2`, each of length h+4. Exactly h>=3 for k4 or h>=5 for k8 gives a strictly decreasing complete rho plan. Thus the accepted domains are precisely w718 modulo729 orw4255 modulo6561, with W5 and selected conditions retained.

After full W9 elimination every failed named plan is accounted for: h0 and h1 with r0 modulo3 retain the original request with coefficient+1; the other failed positive-h cases retain a unique higher-rank W5 request. Every accepted threshold and terminal ternary phase has a complete progression inside the R54 entry phase. For each requested forward depth L, CRT gives inputs with7L growing quotient steps but a seven-arrow inverse comparison (k4h3), or a nine-arrow one (k8h5). These inverse words are outside the old R54 procedure. The whole selected w16 modulo81 subphase has both h0 and remains unresolved by these two choices.

See [proof](../experiments/residual_progress/selected_inverse/SELECTED_INVERSE.md), [constructor](../experiments/residual_progress/selected_inverse/selected_inverse.py), and [receipt](../experiments/residual_progress/selected_inverse/selected_inverse_audit.json). Checks cover300 eligible inputs,600 signed plans,102 affine comparisons,192 progression cases through h128,36 forward-depth intersections through128 and four actual supplied-current conversions. Two full output currents and their inputs are stored. This does not exhaust other inverse words or prove universal coverage.

## R57 — Exact guarded cycles, all exit phases and further decreasing progressions

**Status: written complete exit interface, infinite arithmetic families and conditional finite currents.**

For q=−17 modulo5184 in the R54 entry phase, write E=v2(q+17),u=(q+17)/2^E. Exactly `r=floor((E−6)/11)` guarded cycles return to the entry phase, ending at Q=3^(7r)2^e u−17, e=E−11r in6 through16. The guard requires E>=17; the ordinary affine word alone is already valid at E>=12 and need not return to that phase. The cycle's signed quotient current is exactly the current of seven ordinary arrows with valuations1,1,1,2,1,1,4, by cancellation across its halving bridge. This sharpens the earlier clock accounting without identifying the intermediate ordinary and quotient states.

An eleven-row table processes every exit e6 through16, retaining variable valuations and full endpoint normalization. It accepts only when the endpoint's rho bound is below the original q. For every r>=0 and odd d>=2r+5, an explicit nonempty CRT progression enters exactly r guarded cycles, exits at e12, and passes this strict bound. The ordinary comparison clocks are `(7r+(d−1)/2+6,1)`; the quotient clock is7r+(d−1)/2+5. An additional coprime ternary condition makes every member fail both R55 and R56, as well as the old nine rules. It supplies further coverage at every repetition count, while other exits remain unresolved.

See [proof](../experiments/residual_progress/selected_cycle_exit/SELECTED_CYCLE_EXIT.md), [constructor](../experiments/residual_progress/selected_cycle_exit/selected_exit.py), and [receipt](../experiments/residual_progress/selected_cycle_exit/selected_exit_audit.json). Checks cover352 complete exit cases,264 maximal-cycle cases,128 progression cases including64 exclusions from R55/R56, and three actual supplied-current conversions. All three completed outputs and their18 distinct supplied inputs are stored. The [twelve-family rho union](../experiments/residual_progress/selected_rules/SELECTED_RULES.md) composes R55–R57 after the old nine rules, preserving signed dependencies and priority. The separate sigma system is not included. A [finite mixing survey](../experiments/residual_progress/rank_mixing/RANK_MIXING.md) found acyclic completed graphs of2075 and16619 nodes; it proves neither a common global rank nor universal termination.

## R58 — Exact classification of rank excess in formal absorption

**Status: written classification and complete conditional forward domain.**

For the unchanged fully W9-expanded `H_s`, put `n=nu(s)`. Every requested W5 rank is at most n, except precisely when canonical `n=27 mod48`, `v2(3n-1)=4`, and `3z` is noncanonical for `z=(3n-1)/16`. In that case exactly one request lies above n: `u=4z+1`, with coefficient+1 and `rho(u)=(9n+5)/8`; all others lie below n. At n1 there are no requests. If s is noncanonical, even this exceptional rank is strictly below s. The proof includes every recursive W9 branch and the small v9 case.

For the full R51 fifth-exponent family `w=437+512m`, the unchanged forward current is strict in the original rho exactly unless `m=7 mod16` and `3(2147+4374j)` is noncanonical, where `j=(m-7)/16`. Ordinary clocks remain(6,1), quotient clock5. The full progression `w=4021 mod294912` passes and is outside all twelve earlier direct domains. The retained failure44981 still requests96069 with rank144103 above134943; rho and sigma remain distinct.

The [proof](../experiments/residual_progress/exact_absorption_bound/EXACT_ABSORPTION_BOUND.md) and [receipt](../experiments/residual_progress/exact_absorption_bound/exact_bound_audit.json) record16384 odd seeds,2048 W9 plans,2048 fifth-family inputs (1983 descending,65 unresolved),69 new-progression examples through index2^128, three complete supplied-current outputs with12 distinct supplied pairs, and seven rejection checks. These audit the construction; the infinite classification rests on the written argument.

## R59 — Deferred original-rank testing and exact larger-request cancellation

**Status: written finite-rewriting theorem and two complete conditional domains.**

Start with any finite exact signed plan for P(w). Expand remaining requests of rank at least rho(w), largest first, using only the fixed twelve-family strict-rho resolver. Protect the original source and retain unavailable requests. Without a resource cap the formal procedure terminates after at most `max(0,M-rho(w)+1)` examined high-rank vertices, where M is the maximum initial rank. Injectivity of rho and strict decrease of every resolver edge prevent a processed rank from reappearing. A cap retains an exact unfinished frontier. The final comparison is strict only if all remaining ranks are below the original; rewriting termination alone does not prove this.

For every `w=245+1024n`, the exact R55 A4d2 plan already has smaller requests despite its rejected endpoint bound. Its subprogression245mod3072 is outside all twelve old domains. For `w=1301+32768l`, assume `g=3127+78732l` is selected. The first plan requests one larger pair `u=1853+46656l`; its accepted R55 rule cancels the intermediate normalization and absorption terms exactly. The composed q-to-g current is the eight ordinary valuations(1,1,1,1,2,1,3,2), with `T^8(q)=nu(g)` and ordinary normalized clocks `(8+a_g,a_g)`. The full progression1301mod786432 satisfies the hypothesis and is old-twelve-excluded. No unselected-g conclusion is asserted.

The [proof](../experiments/residual_progress/deferred_rank/DEFERRED_RANK.md) and [receipt](../experiments/residual_progress/deferred_rank/deferred_rank_audit.json) check127 candidate plans from1024 W5 roots,23 new descending seeds and101 protected-source cases,68 examples per complete family,72 new-domain examples through2^128, negative multipliers, caps and seven rejections. Four actual substitutions use13 distinct supplied pairs; full245/1301 tables are stored. The internal resolver is fixed and never calls this new dispatcher recursively.

## R60 — Maximal inverse-cycle continuation with a complete descent table

**Status: written word-domain, maximality and complete conditional-plan classification.**

On selected `w=3445 mod3456`, put `v=(16w-13)/27`, assume `3|v`, and set `b=8v+1`, `q=rho(w)`. Let `k=floor(v3(b+17)/7)`, `p=(2048/2187)^k(b+17)-17`, `j=v3(p+1)`, and `eta=2^j(p+1)/3^j-1`. For k>=1 the exact ordinary inverse comparison eta→q has word `1^j,(1,1,1,2,1,1,4)^k,2,1,1,4` and length j+7k+4. These are maximal repetitions of that specified cycle word and maximal valuation1 continuation, not maximality among all inverse choices.

The full signed plan is descending exactly for k1–5 with j>=3, k6–11 with j>=2, k12–17 with j>=1, and every k>=18. Failed k>=1 rows retain a unique higher request of rank eta; k0 retains the R56 original self-request. Exact affine intercepts as well as slopes are included in the classification. Complete CRT families realize every permitted remainder. A fixed14-arrow comparison at k1,j3 has whole old-twelve-excluded families through every prescribed guarded forward depth L. Some overlap R59, so this is not an exclusion from the newly enlarged dispatcher;11432437 is an actual R60 priority winner there.

The [proof](../experiments/residual_progress/cycle_inverse/CYCLE_INVERSE.md) and [receipt](../experiments/residual_progress/cycle_inverse/cycle_inverse_audit.json) retain512 affine checks, seven exact threshold boundaries,99 complete plans (57 descending,30 higher-leading failures,12 original self-requests), nine full old-twelve-exclusion families through L64, four long words, three actual substitutions with full first-two tables, and eight rejections. Supplied currents remain necessary for the surviving smaller inputs.

## R61 — Entire exponent-eleven exit and a scoped exact continuation undo

**Status: written exit identity and infinite-family limitation of a specified continuation procedure.**

For every r>=0 and positive odd s, `q=81*2^(11r+11)s-17` has exactly r guarded cycles before exit exponent11, whose endpoint is `f=3^(7r+10)s-6`. Its ordinary clocks are(7r+7,1) and quotient clock7r+6; the raw endpoint satisfies f>q exactly for r>=16. This does not imply every such input fails after normalization.

For every r>=16,A>=5,K>=0, a complete coprime CRT class makes f canonical with first complete block(A,2), followed by at least K growing(2,2) blocks. Both the original w and the unique leading input v=f/3 are outside the fixed twelve direct domains at7206f9c. Appending any of the prescribed full-block prefixes and applying the corresponding leading R41 inverses restores the original unfinished current and its entire signed request vector exactly. The surviving coefficient+1 at v has rank f>q; expansions of smaller requests cannot cancel it. The result excludes a uniform bound for that named procedure with the old twelve rules. It allows other inverse words, later rules, arbitrary comparisons and input-dependent longer continuation; the seed changes with K.

The [proof](../experiments/residual_progress/exit_continuation/ELEVEN_EXIT_CONTINUATION.md) and [receipt](../experiments/residual_progress/exit_continuation/exit_continuation_audit.json) check200 full exit cases,19 CRT families,40 exact complete-current undos, eight rejections and one full unfinished fixture. No absorption discovery supplies its unresolved leading input.

The [fifteen-family dispatcher](../experiments/residual_progress/refined_rules/REFINED_RULES.md) preserves the old twelve choices and appends R58/R59/R60 under rho. R61 supplies a scoped obstruction, not a new accepted rule. The finite1024-root replay preserves all722 earlier plans exactly and accepts747 in total, with277 unresolved. Explicit witnesses exercise all three added branches, including R60 after earlier priorities. Seven actual conversions use eight distinct supplied pairs, with full1301/11432437 tables;245 closes without any supplied pair. These finite figures do not imply an asymptotic coverage rate or universal closure.

## R62 — Original-rank resolution of the unique absorption defect

**Status: written compatibility theorem, exact whole-domain interfaces, complete local tables and a scoped surviving family.**

For any sigma-valid signed plan, a returning parent automatically gives a rho-valid plan. For a nonreturning parent w, the nondecreasing-rho requests are precisely returning u with `ceil((8rho(w)-5)/9)<=sigma(u)<rho(w)`. This is a complete compatibility criterion; it does not permit arbitrary mixing of ranked rules.

Every failed fifth-exponent plan has `w=4021+8192j`, original rank `Q=12063+24576j`, and one high request `u=8589+17496j` with coefficient+1. Substituting the entire first or second returning comparison gives exactly the final endpoint's formal absorption requests at ranks at least Q; all other terms lie below Q. This holds for arbitrary exponents without claiming every plan passes. When the defect exponent is3, the first comparison succeeds iff its endpoint r is noncanonical or1mod8. On its failed complementary branch, the second-exponent2 and3 tables classify every depth, including the selected endpoint's possible R58 excess. The nonexceptional W9 bound `(243n+511)/256` resolves the remaining small-even case. All tests use Q, not the larger child's rank.

The whole progression `w=53173+65536k` passes the first comparison. Conversely `w=44981+2^24 k` retains an unrecognized high u under the fixed fifteen-rule expansion; for k divisible by81 the original parent also misses all fifteen. This limitation concerns that fixed resolver and initial plan. Later rules and the new second interface are not excluded automatically.

See [proof](../experiments/residual_progress/defect_resolution/DEFECT_RESOLUTION.md), [constructor](../experiments/residual_progress/defect_resolution/defect_resolution.py), and [receipt](../experiments/residual_progress/defect_resolution/defect_resolution_audit.json). The code retains exact signed currents and permits compilation only after the original-rank test and supplied-input validation.

Finite evidence covers13 affine inequalities,76 sigma-valid plans,192 nonexceptional W9 roots,64 first-stage cases,544 second-stage cells, four large exact cells through depth129 and index2^128,90 higher-exponent interfaces,63 family instances and16 fixed-resolver expansions. Four actual outputs use21 distinct supplied pairs; full tables and an unfinished44981 fixture are stored. These checks support the implementation; the infinite quantifiers rest on the written proof.

## R63 — Complete refinement of the exponent-eleven obstruction and exact inverse undo

**Status: written classification of the whole R61 CRT family under the fixed fifteen rules.**

For every R61 parameter triple r>=16,A>=5,K>=0, the higher exit's leading pair remains outside all fifteen direct domains. At the original parent, R59's candidates retain either that unrecognized leading request or the protected original request. Thus the original parent is accepted by the fifteen-rule dispatcher iff R60's maximal-cycle/point threshold passes. Every feasible phase has a full CRT realization inside each fixed(r,A,K) family; both accepted and rejected subrows are infinite.

The prescribed quotient inverse word of length7r+6 from the higher exit f returns exactly to the original q. Its leading-pair plan is locally strict because q<f, but substituting it into the original exit plan cancels every current row and leaves precisely `{w:1}`. Stopping at the alternate inverse phase recovers R56's existing first node. These are complete exact undo identities for named paths, not barriers to other comparisons.

See [proof](../experiments/residual_progress/refined_obstruction/REFINED_ELEVEN.md) and [constructor](../experiments/residual_progress/refined_obstruction/refined_obstruction.py). R64 supplies a distinct comparison inside this family, so the old exclusion cannot be extended to all later rules.

## R64 — A lifted inverse ray with complete maximal continuation thresholds

**Status: written conditional construction and full arithmetic classification for a specified inverse family.**

On the R60 entry domain, put `v=(16w-13)/27`, `3|v`, and q=rho(w). Lift the first inverse ray to `b=512v+113`. Its ordinary tail to q is `(2,7,1,4)`. The rotated cycle `(1,1,2,1,1,4,1)` has affine center−25 and inverse slope2048/2187. The construction takes its maximal number of inverse copies and the maximal subsequent valuation1 run, retaining every ternary remainder and every failed signed plan.

For positive cycle count k, the exact point-depth thresholds descend from13 to0 at k=1,7,13,20,26,32,38,44,50,57,63,69,75,81. The proof checks finite affine intercepts as well as slopes. Whole subrows inside every R61(r,A,K) family pass below the original q and miss all fifteen previous rules. These are conditional pair constructions requiring their remaining smaller inputs, not universal supply or completeness among inverse words.

The zero-cycle branch also takes maximal point ancestry: it passes exactly at depth j>=14. Its special failed j1 endpoint0mod3 reproduces the old original+1 plan; every other failed row has a unique higher+1 request. Whole new subrows at k0,j14 and k1,j13 give respectively18 and24 ordinary arrows, independently of the prescribed R61 parameters. The seed varies with those parameters. These clocks cover the inverse comparison to q; pair normalizers and supplied helper currents retain their own rows.

See [proof and full zero-cycle continuation](../experiments/residual_progress/refined_obstruction/LIFTED_CYCLE.md), [constructor](../experiments/residual_progress/refined_obstruction/refined_obstruction.py), and [joint R63–R64 receipt](../experiments/residual_progress/refined_obstruction/refined_obstruction_audit.json). The [seventeen-family dispatcher](../experiments/residual_progress/resolved_rules/RESOLVED_RULES.md) appends R62/R64 after the fixed fifteen choices. R63 is a classification, not an accepted rule; R65 is a conditional change of source basis.

The new dispatcher preserves all747 accepted plans in the1024-input window, still leaving277 unresolved there. Its two new winning witnesses53173 and36641534965 are outside that window. Six actual conversions use14 distinct supplied pairs; full59-row and102-row output tables are stored. The finite acceptance count is not a global rate.

The joint R63–R64 receipt covers3298 affine checks,43 full plans (13 descending,29 higher failures and one exact self-return), nine old-cycle rows,16 new CRT rows through r64,A32,K64, four complete dispatcher classifications and two exact leading-current undos. Three actual supplied-current conversions produce102,215,1746 rows from9,15,42 pair inputs respectively; the first two full outputs are stored. Fifteen rejection checks retain invalid and missing-premise cases.

## R65 — The entire returning defect as an adjacent-source comparison

**Status: written triangular equivalence and checked conversion in both directions; no new accepted domain.**

The entire R58 exceptional domain is in bijection with returning pairs u and positive canonical `q=31mod108`, via `q=(9n+5)/8`, `u=(2q+1)/3`, `n=(8q-5)/9`. The raw defect lift n→q is the ordinary word(1,2). Set `D(q)=[q+2]-[q]`. There is an exact identity `P(u)=div K-D(q)+sum c(v)P(v)` in which every helper has `rho(v)<=(3q+7)/4<n`. Thus a supplied D(q) current gives P(u), and a supplied P(u) current gives D(q), using the same strictly smaller helpers. Composing these conversions returns the original supplied current row for row. The adjacent current is still a premise with coefficient−1.

Eliminating all returning requests from any formal H_s terminates and leaves nonreturning pairs and adjacent sources of native height at most nu(s). At the exceptional leading source the height equals nu(s), so this change of basis gives no strict progress. The old accepted rule at4629 still raises that proposed height from6171 to6591 after conversion. The constant source gap of two does not bound merger time, exposure depth or current cost.

The [proof](../experiments/residual_progress/defect_normal_form/ADJACENT_DEFECT_INTERFACE.md) also records why maximal inverse(1,2) normalization adds no W5 domain and fails to define a quotient dynamics. Its static two-pair boundary obstruction does not exclude inspecting internal supplied-current rows. The [receipt](../experiments/residual_progress/defect_normal_form/adjacent_defect_audit.json) checks512 defect interfaces,1024 mixed absorption plans,4096 inverse-scope cases and three bidirectional supplied-current conversions with complete stored tables.

## R66 — Complete ray-index decision and a uniform integer-count obstruction

**Status: written theorem, conditional constructor and finite replay.**

On the complete entry `v=4089+6144n`, `w=6901+10368n`, `q=10351+15552n`, the inverse ray is `b_L=64^L(8v+1)+49(64^L-1)/63`. Its four-arrow tail is(2,6L+1,1,4). Apply the named center17 or center25 seven-arrow rotation maximally, then all point inverses. The full signed plan passes exactly when its canonical endpoint eta is below q, except for the classified baseline self-returns, which never pass. Every failure retains its nondecreasing request with coefficient+1.

Original-rank bounds on the binary divisibility of eta+1 and the cycle endpoint give an explicit finite upper bound for every successful L. Thus the procedure can exhaust all ray indices at any fixed entry; w6901 is a proved complete failure. Independently, `v3(b_L-b_M)=v3(L-M)` shows every ternary precision is attainable by changing L. That fact alone cannot overcome growth by64^L.

For L>=1, success requires k>=10L or j>=8L. Counting the necessary ternary cylinders with the proved O(log N) ray cutoff gives, for every N>=1, `accepted(N)<=S*N+5T²+6T+1`, where `T=floor(log2(15552N))` and `S=1/729+3/((3^8-1)(1-3^-7))+3/(3^70-1)<1/500`. Hence limsup acceptance is below1/500 and liminf failure exceeds499/500. No existence of a natural density is asserted. This bounds only the specified two-rotation maximal-cycle/point procedure, not all inverse words, premature cycle stops, the existing dispatcher or other current constructions.

See [proof](../experiments/residual_progress/all_ray_continuation/ALL_RAY_CONTINUATION.md), [constructor](../experiments/residual_progress/all_ray_continuation/all_rays.py), and [receipt](../experiments/residual_progress/all_ray_continuation/all_rays_audit.json). Accepted outputs retain every supplied smaller pair premise; no new rule is added to the frozen seventeen-family dispatcher.

## R67 — Arbitrarily long growing blocks from actual mixed-rank comparisons

**Status: written exact signed interface and scoped potential obstruction.**

On `w=40529845 mod2^26`, an accepted sigma fifth-exponent plan followed by an accepted rho returning plan has leading child `V(w)=(531441w+311195)/524288>w`. The full combined current is `D_(3w,3V)+J_V-J_w`, and its request vector is `{V:1}+A_V-A_w`; all other ranks are below3w. The convenient absorption transport used in this derivation is restricted to its proved binary phase; f1371 is a retained counterexample to extending it universally.

For every m, the full progression `w=-311195/7153 mod2^(26+19(m-1))` admits m growing copies. Their complete current and requests telescope, retaining the highest coefficient+1. Quotient length is12m and ordinary common-tail clocks are(12m+1,1). At any fixed positive input obeying the guard, the maximal guarded count is exactly `1+floor((v2(7153w+311195)-26)/19)`; the exit valuation is7..25 and the terminal current remains missing.

The actual dependency edges rule out a common strictly decreasing potential with finitely many labels and nondecreasing dependence on height inside each label. They do not rule out unbounded arithmetic state, a different rule choice, richer cancellation or a potential outside that class. No infinite positive path or nontermination of fixed-priority dispatchers is asserted. Strict-rho expansions of the lower requests cannot cancel the retained highest request.

See [proof](../experiments/residual_progress/mixed_rank_recursion/MIXED_GROWING_BLOCK.md), [constructor](../experiments/residual_progress/mixed_rank_recursion/mixed_growth.py), and [receipt](../experiments/residual_progress/mixed_rank_recursion/mixed_growth_audit.json), including complete unfinished one- and two-copy currents.

## R68 — Native-height inverse obstruction with a fixed forward comparison

**Status: written all-ray separation and conditional adjacent-current construction.**

For every D>=3,t>=1, set `q=31+2^57*3^D*t` and `n=(8q-5)/9`. Every canonical ancestor of q at quotient depth1..D is either the unique two-arrow predecessor n or strictly above q. A six-state forward-closed certificate at the anchor31 and the complete affine inverse-gap recurrence prove this for all ray indices. The varying q prevents interpreting it as a permanent obstruction at one fixed input. It strengthens the height test: descent below q alone can return exactly the still-missing native seed n.

The same family preserves the 35-arrow ordinary word from31 to23, with total valuation56. Its endpoint is `y=23+2*3^(D+35)*t`, and `8n-(9y+5)=4+2*3^(D-2)*t*(2^62-3^39)>0`. The positive source q+2 also has a one-arrow comparison with all helpers below n. Combining both full currents gives an exact conditional D(q) plan with every pair request strictly below n. At q31 the plan has no missing requests. The whole adjacent domain remains open; no new dispatcher coverage is claimed.

The [proof](../experiments/residual_progress/adjacent_recursion/NATIVE_HEIGHT_SEPARATION.md) also derives the initial paired run and proves that transporting R44 through R65 is row-for-row the original forward endpoint comparison. The [constructor](../experiments/residual_progress/adjacent_recursion/native_height.py) and [receipt](../experiments/residual_progress/adjacent_recursion/native_height_audit.json) retain exact supplied-current demonstrations and the native-height tests.

## R69 — Arithmetic debt transport and a complete reset obstruction

**Status: written local progress identity and scoped potential impossibility theorem; exact conditional currents.**

With `L_W(w)=7153w+311195`, `L_E(u)=7153u+656187`, the two actual R67 leading edges obey `L_E(u)=3^7 L_W(w)/2^10` and `L_W(v)=3^5 L_E(u)/2^9`. Thus the positive integer `L_phase*2^v2(L_phase)` strictly decreases on those leading edges. This is not a full-current rank.

For every H>=26, the complete CRT progression `L_W(u)=2^H mod2^(H+1)`, `u=13 mod81`, gives a returning parent `w=(64u+5)/9`. Its already valid R44 exponent-three plan retains the unique highest child P(u)+1, with all requests strictly below the original rho. Nevertheless `v2(L_E(w))=3` and `v2(L_W(u))=H`, so the candidate potential increases without bound. Varying height at fixed order and then order forces any phase-dependent monomial `C_phase L_phase^alpha_phase 2^(beta_phase H_phase)` with nonnegative size exponents alpha_phase to have common exponents. Strict mixed-block decrease then requires beta>0, which the reset family contradicts. Both old centres in both phases also fail. No arbitrary-potential impossibility is claimed.

The whole reset frontier is exactly `P(u)+P((u-13)/72)-P((32u-11)/81)`, with its two lower absorption terms cancelling row for row after the specified bridge. The [proof](../experiments/residual_progress/arithmetic_progress/VALUATION_DEBT.md) also gives a necessary pulled-back-centre condition, without a closure theorem. The [module](../experiments/residual_progress/arithmetic_progress/valuation_debt.py) and [receipt](../experiments/residual_progress/arithmetic_progress/valuation_debt_audit.json) verify14 leading transports,24 complete signed reset plans,35 rational power cases and two supplied-current conversions with180/235 rows. Existing accepted domains are unchanged.

## R70 — Complete mixed exits and a growing conditional re-entry

**Status: written full exit interface and scoped failure of a natural continuation; no new accepted rule.**

At the end of R67's maximal guarded block let `7153v+311195=2^e z`, z odd, e7..25. The next R26 first exponent is always5. Its second depth is2 at e7, `3+v2(243z-294023)>=4` at e8, and3 at every e9..25. The complete composed current retains every signed helper and tests them against the original parent rank.

On `w=8515171531530858421 mod2^63`, the maximal old block has exactly one copy and exit e18. A natural continuation returns to a guarded pair

`R(w)=(282429536481w+328537586155)/2^37>w`.

The full current is an exact comparison from3w to3R(w) plus `H_R(w)-H_w`, with requests `{R(w):1}+A_R(w)-A_w`; all other ranks are below3w. Crucially, the continuation's returning R44 comparison is **not rho-descending**. The larger request remains an unresolved premise. Its quotient length is24 and ordinary common-tail clocks are(30,6).

Writing `E=144990583009`, `C=328537586155`, one has `ER(w)+C=(282429536481/2^37)(Ew+C)`. For every r>=1 the complete cylinder `w=-C/E mod2^(63+37(r-1))` gives r growing re-entries. At a fixed positive guarded seed their exact maximal count is `1+floor((v2(Ew+C)-63)/37)`; the new exit remains open. Repeated clocks are(24r+6,6). This is not an infinite positive path, accepted mixed-dispatcher loop or impossibility of other exit comparisons.

The full exponent18-to-guard congruence is also proved for every maximal old count m, with clocks(12(m+1)+6,6). Its other helpers need not lie below the original rank. See [proof](../experiments/residual_progress/mixed_exit/MIXED_EXIT_REENTRY.md), [constructor](../experiments/residual_progress/mixed_exit/mixed_exit.py) and [receipt](../experiments/residual_progress/mixed_exit/mixed_exit_audit.json):114 exit cases,19 full exit plans, eight general re-entries, eight fully composed re-entries, eight repeated currents,24 long arithmetic families through128 copies and37 exact maxima. One- and two-copy unfinished currents are stored.

## R71 — Whole-word integrality and rational cycle controls

**Status: self-contained derivation and finite exact implementation of a restricted cycle result with published antecedents.**

For the mechanical valuation words `a_i=floor(((i+1)A+l)/k)-floor((iA+l)/k)`, A>=k>=1,0<=l<k,2^A>3^k, put g=gcd(A,k). Every rational cycle state has exact reduced denominator `2^(A/g)-3^(k/g)`. In the primitive case all intercept words are rotations, their gcds with `2^A-3^k` agree, and the change from intercept0 to1 is one pure2/3-power term. This forces gcd1. Repetitions reduce to primitive parameters. Modulo8 excludes denominator1 except the all-2 word and cycle1.

Taking `A=ceil(k log2 3)` also gives every rational cycle state greater than k/6. Thus integer3x+d controls can have minimum above any prescribed multiple of d, **with d varying**. This does not give high cycles for a fixed d or certify any finite base test. It excludes neither arbitrary integer cycles nor aperiodic divergence. Rational scaling preserves local identities but changes the integer lattice; whole-word integrality is a distinct requirement.

The [proof and literature audit](../experiments/residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md) acknowledges Knight's published nonintegrality result for high cycles and rational-cycle antecedents. No novelty or new current coverage is claimed. The [module](../experiments/residual_progress/lattice_cycles/balanced_cycles.py) and [receipt](../experiments/residual_progress/lattice_cycles/balanced_cycles_audit.json) check1320 arbitrary rational words,336 mechanical families,8232 intercepts,130 high controls and11 domain rejections. The [side-lane review](../experiments/residual_progress/side_lane_review_678e565.md) separately reproduces both pinned transfer/catalogue probes unchanged.

## R72 — No finite affine-valuation rank for the fixed mixed phases

**Status: written scoped impossibility theorem, with complete accepted comparisons and exact finite checks.**

In each of R69's two fixed phases, allow a positive increasing affine height raised to any nonnegative real power, multiplied by powers of2 whose exponent is an arbitrary real weighted sum of finitely many rational affine valuations. Forms must be nonzero on the phase. No such potential can be nonincreasing on both mixed leading edges and all the returning comparisons below, while strictly decreasing across every mixed block. Arbitrary additional phases, nonlinear forms, infinitely many centres, amortized signed-vector ranks and other rule selections are outside the claim.

For L1mod3, put p=4^L and choose minimal a>=3 with `lambda=6p(2/3)^a<=4`. Complete coprime CRT conditions produce guarded children u of every exact order H>=26 and returning parents `w=lambda*u+lambda/9-1/3+(2/3)^a/3`. They satisfy `2u<w<=4u`. The full R44 vector is `{u:1}+A_u-A_nu(w)`; P(u) is the unique highest request and all requests strictly decrease original rho. Quotient length is a-1 from rho(w); ordinary common-tail clocks are(a,1).

The parent image of `theta_W=-311195/7153` has reduced denominator of exact ternary order a-1 on L4mod9, giving infinitely many distinct centres. Mixed-block nonincrease forces common height powers and common net centre weight; strict block decrease forces that weight positive. A finite parent-centre list omits one of the constructed centres. Along its H→infinity family every parent valuation stabilizes while the child factor grows as2^(bH), contradicting nonincrease. This argument allows negative individual weights and does not infer a universal theorem from a finite sample.

See [full proof](../experiments/residual_progress/finite_centres/FINITE_CENTRES.md), [constructor](../experiments/residual_progress/finite_centres/finite_centres.py) and [receipt](../experiments/residual_progress/finite_centres/finite_centres_audit.json). The replay checks192 arithmetic CRT cases,48 full signed comparisons,24 distinct poles, three finite-list illustrations, four mixed-stabilization cases and12 rejections. Two actual supplied-current conversions give158/211-row outputs from3/13 pair inputs. No dispatcher domain or universal current supply is added.

## R73 — Exact normalization and cancellation of signed pair frontiers

**Status: written terminating algebraic compiler for two complete identities; terminal currents remain explicit premises.**

The first identity sends `w=93 mod512` to `u=(9w-5)/64` with an eight-row exact current for P(w)-P(u). Both endpoint comparisons have ordinary clocks(3,1). The second sends `b=1285 mod2048` to `a=9(b-5)/256` with ten rows and lower/upper clocks(3,1)/(4,2). Both strictly decrease rho. Their guards are disjoint and each child is at most9/64 of its parent. Arbitrarily long prescribed mixed inverse words have complete positive CRT families; an r-edge chain pads to clocks(2r+2,2) at both endpoints.

Every finite integer coefficient vector has a unique terminal normal form `N(c)_t=sum_(tau(w)=t)c_w`, with exact current `Gamma(c)=sum_w c_w C_w`. This map is integer linear and idempotent. Each aggregate rewrite strictly decreases `sum|c_w|w`, including after signed coefficient merging. Its kernel is exactly the integer relation module generated by these two identities. Zero terminal vector supplies a complete current; nonzero terminal coefficients, including negative ones, remain required pair inputs. This kernel statement is not about all possible Collatz comparisons.

On the whole R69 reset family, the full three-request vector `P(u)+P(a)-P(b)` reduces exactly to P(u). More strongly, `J_44-C_II(b)=C_I(w)` row for row. This eliminates both helper premises through their joint current, leaving only the smaller P(u). It adds no dispatcher coverage. In contrast, R67's input and larger leading child are terminals for these two rules; their full normalized vector retains that unique higher+1 request. The absolute-height potential therefore fails on that comparison even after this normalization.

See [proof](../experiments/residual_progress/frontier_progress/SIGNED_FRONTIER_NORMAL_FORM.md), [compiler](../experiments/residual_progress/frontier_progress/frontier_normal_form.py) and [receipt](../experiments/residual_progress/frontier_progress/frontier_normal_form_audit.json). Checks cover512 bridges,4096 singleton normalizations,28 mixed-word families through32 edges,128 signed vectors,12 full reset compressions, six retained mixed-growth leaders and seven rejection cases. One complete input-free current and one31-row supplied conversion with its inputs are stored. No universal leaf supply or termination of the full programme is proved.

## R74 — Complete integer cylinders for arbitrary mixed exit18 returns

**Status: written complete prefix and counting theorem for the specified return subsystem; aperiodic integer survival remains open.**

Let G be `w=40529845 mod2^26`. Returning to G by R67's V has complete domain `2218391138229 mod2^45`; returning by R70's R has domain `8515171531530858421 mod2^63`. In coordinate Y=7153w+311195 the first branch requires order at least45, the second exact order37, so the domains are disjoint. Every maximal-count-m exit18 re-entry is exactly the chronological word V^(m-1)R.

For every finite word omega over V/R, set `e=19#V+37#R`, `ell=12#V+24#R`, and compose `F_omega(w)=(3^ell*w+c)/2^e`. Its exact full domain is `w=(2^e*40529845-c)*(3^ell)^(-1) mod2^(26+e)`. Every positive member follows all guards and grows; any additional initial odd-modulus congruence can be imposed by CRT. Thus every prescribed finite sequence of maximal re-entry counts is realized on the integer lattice. The seed may depend on the prescribed finite word; no single positive seed realizing an infinite word is supplied.

Full currents telescope to `D_(3w0,3wk)+J_wk-J_w0`, with vector `{wk:1}+A_wk-A_w0`. The leading request stays larger than the original; helpers are below3w_(k-1) and can exceed the original rank. Quotient length is ell. Ordinary common-tail clocks are(ell+1,1) or(ell+6,6), according to the last symbol V or R. These remain conditional growing comparisons, not accepted dispatcher rules.

Every infinite word defines one2-adic point. An eventually periodic word has a negative rational point because every cycle affine slope exceeds1 and its offset is positive; it cannot be a positive integer. This leaves genuinely aperiodic possible survivors. For s=2^-19+2^-37, the exact fixed-depth density is2^-26*s^m and the uniform counting error is less than2^m. Possible infinite survivors have density zero and count at most `3*(X/2^26)^alpha` for X>=2^26, alpha=log(2)/log(2/s). Neither sparsity nor periodic exclusion proves emptiness.

See [proof and classical coding context](../experiments/residual_progress/integer_prefix/INTEGER_PREFIXES.md), [constructor](../experiments/residual_progress/integer_prefix/integer_prefix.py) and [receipt](../experiments/residual_progress/integer_prefix/integer_prefix_audit.json). Checks cover510 words/1530 positive lifts,20 long words through256 symbols,108 odd-CRT cases, nine maximal-count lists,310 eventually periodic points,32 density/count checks and30 full signed compositions. Two complete unfinished currents, missing-supply rejections, cap behavior and ten invalid-input rejections are retained. Finite-prefix integrality does not exclude this whole class; a constraint on the same integer across unbounded prefixes is still needed.

## R75 — A common critical rank after retaining both pair types

**Status: written source-basis and rule-translation theorem with an exact conditional compiler; terminal current supply remains open.**

Retain W=W5 union W9 and rho(w)=nu(3w). R37's unexpanded critical absorption plan `[s]=div Jhat_s+sum Ahat_s(v)P(v)` has every requested rank at most nu(s). For every E_return input u, put q=(3u-1)/2, n=(4u-3)/3=sigma(u), b=n/3 in W9. The ordinary path n→q has valuations(1,2). The current `C_u=N_(3u)-D_(n,q)+Jhat_b-Jhat_u` gives

`P(u)=div C_u+P(b)+sum(Ahat_b-Ahat_u)P`.

Its unique highest request is b with coefficient +1 and rho(b)=n<q; every other request has rank below n. Replacing every signed E_return child of any sigma-valid W5 plan by this identity produces a rho-valid plan in W. All other children already have rho=sigma. Every old rho-valid W5 plan stays valid without changing its rows or requests. Thus both collections can be used under one strict rank **after translation**, with finite conditional expansion. The original incompatible edges are not claimed to share a rank.

On the full R67 guard, q=3w has an ordinary common-tail comparison to f=(729w+147)/256<q at clocks(6,1). Using the critical plans gives `D_(q,f)+Jhat_f-Jhat_w` and requests Ahat_f-Ahat_w. Its unique highest input is the W9 pair b=f/3 of rank f<q. The larger R67 W5 request is avoided, but this smaller auxiliary current remains a premise. This is an enlarged induction universe, not new completed W5-only coverage.

The local W9 rule is rho-valid except exactly d=v2(9b-1)=4 with 3z noncanonical, z=(9b-1)/16. That branch has unique higher input u=4z+1. Composing it with the E conversion restores coefficient +1 at b, with only lower other requests. Universal zero current is false: u=453, b=201 leaves `{201:1,5:1,25:1}` and a nonzero 14-row current. The leading self-request prevents strict descent.

See [proof](../experiments/residual_progress/critical_basis/CRITICAL_BASIS.md), [compiler](../experiments/residual_progress/critical_basis/critical_basis.py), and [finite receipt with supplied examples](../experiments/residual_progress/critical_basis/critical_basis_audit.json). The seventeen-family W5 dispatcher and its frozen internal resolvers are unchanged. Neither successful translation nor termination of conditional rewriting supplies unknown terminal currents.

## R76 — Complete exclusion of one uniform fixed-word pair model

**Status: written exhaustive-search theorem with retained finite certificate and independent enumeration.**

On every w(n)=40529845+2^26*n, n>=0, no uniformly smaller affine positive W5 partner u(n) has common tails on both pair endpoints with all four ordinary valuation words fixed independently of n. Clocks may differ or be zero. The all-n integrality hypothesis forces integer affine coefficients. The parent lower and upper fixed paths have lengths 11 and 17. Equality of lower slopes forces ell+v3(alpha)=j, so ell<=j<=11. A proved slope bound gives all possible inverse valuations without a guessed cap.

Two independent searches agree on 43 candidate lower partners and no upper fixed-path intersection. The constructor visits 1110 nodes; the exact-length/total-valuation check visits 3401 nodes and 450 complete inverse words. See [proof](../experiments/residual_progress/uniform_pair_scope/UNIFORM_PAIR_SCOPE.md), [constructor](../experiments/residual_progress/uniform_pair_scope/uniform_pair.py), and [complete candidate receipt](../experiments/residual_progress/uniform_pair_scope/uniform_pair_audit.json). The default checker also verifies 215 direct instances, 256 small affine paths, 12 domain boundaries and 20 rejected inputs.

The theorem does not exclude fixed clocks with varying intermediate valuations, refined progressions, variable words or clocks, non-affine or non-W5 partners, multiple pairs, or general signed currents. R75 uses the enlarged critical source basis outside this excluded model.

## R77 — Same-seed factor complexity and a finite return bound

**Status: written conditional complexity theorem, exact fixed-word repetition formula, and finite all-seed bound for the specified R74 subsystem.**

Put K=311195/7153 and Lambda=3^24/2^37. Along a positive legal V/R trajectory, states strictly increase and w_j+K<=Lambda^j(w_0+K). If a length-L factor omega repeats at i<j, both starting states belong to its one complete cylinder. Hence `2^(26+e_omega) <= w_j-w_i < Lambda^j(w_0+K)`, including overlapping factors. Here e_omega>=19L. Thus any one fixed positive infinite survivor has `liminf p(L)/L>=19/log2(Lambda)=18.2850540694...`, where p(L) counts all distinct length-L factors in its itinerary. The exact inequality 3^432<2^685 gives the strict bound >18; p(L)<=18L+O(1) is impossible even along unbounded lengths. High-complexity aperiodic survivors are not excluded.

For every positive starting value at most `floor(2^1305/3^768-311195/7153)=260028359941009900571662033`, 37 consecutive returns are impossible. Otherwise the 33 length-five windows would all be different by the spacing bound, although only 32 binary words exist. This proves exit from this return subsystem, not absorption, ordinary stopping, or termination of other comparisons.

For a fixed nonempty word F(w)=(aw+c)/2^e, the exact number of consecutive complete copies from w in G is `floor((v2((a-2^e)w+c)-26)/e)`. The positive defect is finite; changing the next word can allow more returns. For V, the count is one less than R67's guarded block count. A powers-of-three-denominator sequence with real limit 0 and 2-adic limit 1 explicitly refutes identifying limits in the two completions.

See [proof](../experiments/residual_progress/itinerary_complexity/ITINERARY_COMPLEXITY.md), [exact implementation](../experiments/residual_progress/itinerary_complexity/itinerary_complexity.py), and [receipt](../experiments/residual_progress/itinerary_complexity/itinerary_complexity_audit.json). Checks cover 62 affine words, 186 lifts, 630 copy cases including 90 zero-copy cases, 12 R67/R74 boundary cases, 32 finite positive traces, 11242 factor repeats including 524 overlapping ones, 45 exact threshold cases, 62 negative rational periodic words, 80 distinct-completion controls and 12 rejections. Infinite survival is a hypothesis, never a computationally supplied object.

## R78 — Native critical-nine continuation at the original rank

**Status: written conditional composition theorem and complete decisions on the stated domains; universal supply remains open.**

For every positive b905mod8192, put t=(27b+13)/128=191mod1728, n=3b, c=(27t-1)/4, m=3c. The exact six-arrow upper prefix has valuations(1,2,1,1,1,2) and ends at selected r=(81t-1)/2 with nu(r)=m. Substituting the retained local R40 plan gives current `G+N_r+L_c+J_c-J_b`, requests `l_c+A_c-A_b`. Against the original n this fails exactly at D=v2(9c-1) in{4,6} with noncanonical3z. Each failure has a unique higher request+1. The successful first-stage rows were already implicit in R52; this is a complete native interface, not a new local orbit identity.

At D6, the higher W5 input is p=(19683b+12677)/8192, Q=rho(p)=(59049b+29839)/16384. The k4 inverse and subsequent E conversion leave the full current `J_c-L_(c,ell)-J_ell` and requests `{b:1}+A_c-A_ell`, with ell=(Q+2)/3 and ordinary c-to-ell word(2,1,2). The lower current need not vanish. The k8 inverse leaves higher W9c+1. Both are failures at the original rank.

Using the next forward block instead yields the entire signed vector `A_f+A_c-A_ell-A_b`. On the complete next-initial-exponent A2 domain it is strict exactly when the next depth d is odd, even d>=6, or the raw endpoint f is selected. Canonical d2/d4 retain a genuine higher critical request. Other A are explicitly unclassified. At b4187017 the locally accepted d4 child has endpoint12732427 above original n12561051, so local child acceptance would be an incorrect substitution.

See [proof](../experiments/residual_progress/native_nine/NATIVE_NINE_CONTINUATION.md), [constructor](../experiments/residual_progress/native_nine/native_nine.py), and [receipt](../experiments/residual_progress/native_nine/native_nine_audit.json). Checks cover383 local bounds,226 native cases,150 full two-ray undos,134 complete next-A2 cells,30 exact inequalities and13 invalid inputs. Three supplied conversions retain all3/8/6 premise tables and produce43/97/102 rows. The W5 dispatcher is unchanged.

Supplement to R75: the [complete immediate-loop classification](../experiments/residual_progress/lower_loop_scope/LOWER_LOOP_SCOPE.md) proves that its self-return current is zero except exactly u453mod576. The nonzero lower identity is oriented at v=(u-3)/18=25mod32, with unique highest critical rank3v; all such W9 pairs already pass the nonblocked rule. The [receipt](../experiments/residual_progress/lower_loop_scope/lower_loop_audit.json) checks894 inputs,218 nonzero and676 zero, plus64 full-progression cases and6 rejections. This supplies neither a new accepted domain nor the original self-request.

## R79 — Exact native return counts and a full original-rank exit obstruction

**Status: written scoped growth/exit theorem and exact-current audit; no new accepted pair domain.**

On G={b905mod8192}, U(b)=(729b+223)/512 and Y(b)=217b+223 satisfy Y(Ub)=729Y(b)/512. At least r complete returns occupy one cylinder modulo2^(13+9r). Each fixed positive b has exactly `floor((v2(Y(b))-13)/9)` complete re-entries, followed by one more native comparison from the last guarded source. The full s-step current has requests `{U^s(b):1}+A_(U^s(b))-A_b`; its unique largest request grows. Ordinary comparison clocks are(6s+3,3), quotient clock6s. Arbitrarily long finite chains use different seeds.

All nine final binary phases13..21 are classified. On the full H17 family v2(Y(b))=9r+17, write c=U^(r+1)(b), z=(9c-1)/16. Exact cancellation yields requests `{z:1}+A_z-A_b` and ordinary clocks(6r+12,4), quotient6r+8. The leading rank3z is below3b exactly at r0; every r>=1 leaves it higher. Other helpers need not remain below the original rank, but none cancels the unique leader. The two named base-ray inverses restore respectively the preceding growing comparison and the exit comparison, row for row.

The bound `(27M+23)/32` for nonblocked local W9 plans is a useful stopping interface only until a smaller rank, W5 leaf or blocked W9 leaf is reached. It gives no closure across those leaves. The higher-ray candidate is now completed on explicit all-return-count subfamilies in R83; the whole exit type remains open.

See [proof](../experiments/residual_progress/native_nine_growth/NATIVE_NINE_GROWTH.md), [implementation](../experiments/residual_progress/native_nine_growth/nine_growth.py), and [receipt](../experiments/residual_progress/native_nine_growth/nine_growth_audit.json). Checks cover123 cylinders,216 exit-phase cases,27 full H17 comparisons,24 full returns,54 inverse undos,383 local bounds and16 rejections. Complete failed-current tables at r1/r2 contain78/134 rows. No absorption search or accepted dispatcher rule is added.

## R80 — A high smaller-origin history defeats arbitrarily deep inverse barriers

**Status: written conditional whole-family theorem, finite all-depth anchor certificate and exact supplied-current demonstrations.**

For D>=12,t>=0 let `q=11547+2^17*3^D*t`, `b=q/3`, `p=11391+2^36*3^(D-12)*t`, and `y=(3q+1)/2`. Then b<p<q<y, p/q/y are canonical, and b lies in the blocked W9 d4/noncanonical-upper row. The entire D12 progression has the thirteen-arrow p word `(1^6,2,2,1^4,2)` ending at F²(y)=24q+13. Every intermediate after p is above q, with peak32q+17. The actual ordinary merger is `S²(q)=S¹⁴(p)=(9q+5)/8>q`; quotient clocks are(1,13).

With L_p that thirteen-arrow current and x=F²(y), `K=delta_q-L_p-delta_x+delta_y` has divergence[q]-[p]. The pair current `K+J_p-J_b` requests `A_p-A_b`, all signed ranks at most p<q. Missing currents remain required. The same particular comparison also passes with old W5-only H_p/H_b frontiers: p127mod512 makes the original absorption bound safe at p. R75 is convenient but not necessary for this family, whose parent is W9.

An independently checked forward-closed table of4892 canonical states includes all2887 canonical origins below11547 and excludes11547. It proves no smaller canonical ancestor at any depth for this anchor. R49's complete inverse shadow theorem lifts this: for t>0, every canonical ancestor of q at each depth1..D is strictly above q, over all inverse rays and indices. Ordinary ancestors at most q are excluded through D as well. Increasing D changes the seed; only the anchor has an all-depth conclusion. The smaller p reaches q's future, not q itself.

The prescribed R44/R52 endpoint comparisons retain the same genuine higher request throughout this family, even with the native absorption basis. Failure of the full seventeen-rule dispatcher is recorded only for four finite samples. No new W5-only coverage or universal history-hitting theorem is claimed.

See [proof](../experiments/residual_progress/native_history/HIGH_HISTORY.md), [constructor](../experiments/residual_progress/native_history/native_history.py), [anchor table](../experiments/residual_progress/native_history/anchor_certificate.json), and [receipt](../experiments/residual_progress/native_history/native_history_audit.json). Default verification checks the supplied anchor edges,54 family/native plans,54 W5-frontier variants,54 actual R44/R52 failures,88 base inverse words,18 varied words and11 rejections. Two supplied conversions produce46/229 rows with all5/9 required pair-current tables. Bounded inverse examples are evidence; the all-ray quantifiers follow from the written shadow proof.

## R81 — Complete fixed-word history cells and original-rank transport

**Status: written maximal-cell theorem, conditional signed compiler and exact supplied-current audit.**

For positive odd anchors q0,p0 whose ordinary words alpha,beta meet, let a,b be their lengths and A,B their total valuations. Every positive same-word merger is exactly `q=q0+M*k`, `p=p0+P*k`, k integer, where `M=2^(A+1)*3^max(b-a,0)` and `P=2^(B+1)*3^max(a-b,0)`. M is minimal. The exact positivity and p<q intervals are given; all k>=0 are smaller precisely when p0<q0 and P<=M. Equal slope and finite expansive-slope examples are retained. This concerns raw paired origins, not every possible current.

If rho(w)=q and p<q, the full current `N_(3w)+K+J_p-J_w`, divK=[q]-[p], requests `A_p-A_w` with all signed ranks belowq. Every nonzero terminal current remains required. The unchanged dispatcher is not extended.

For R80's words(1,2) and(1^6,2,2,1^4,2,6), the entire cell is `q=11547+16*3^12*k`, `p=11391+2^23*k`, k>=0, with gap156+114448k. Its period is8192 times smaller than the old sufficient period. Ordinary clocks remain(2,14), quotient clocks(1,13), and the peak is32q+17. The ordinary meeting need not be canonical. For oddk the local W9 row is nonblocked; for evenk put Z=6496+3^14*k and H=v2(Z). It is blocked exactly when Z/2^H=3^Hmod4. The progression k3072mod4096 lies outside the old cell and retains genuine higher R44/R52 requests, even in the native basis; the new history plan is strict. No universal seventeen-rule nonrecognition is asserted.

See [proof](../experiments/residual_progress/history_lifting/HISTORY_LIFTING.md), [compiler](../experiments/residual_progress/history_lifting/history_lifting.py), and [receipt](../experiments/residual_progress/history_lifting/history_lifting_audit.json). Checks cover18 specifications,189 lifts,592 memberships,191 native plans,62 old-phase records with38 genuine high requests,19 rejections and three complete supplied outputs with46/100/108 rows. Written algebra supplies the unbounded statements. Universal useful-word selection and terminal supply remain open.

## R82 — All-ray history classification from a finite supplied anchor

**Status: written completeness theorem within a stated ternary horizon and exact finite-table classification.**

Let Q be a checked finite absorbing canonical T-table containing every canonical origin throughN. For canonical Y>1,y>=Y with y=Ymod3^K, and thresholdq>=2, set `n=ceil((q+1)(Y+1)/(y+1))-2`. If n<=N, every canonical a<q reachingy in0..K steps is the lift of a supplied origin c<=n whose unique path visitsY, with lengthd<=K. The lift is `a=c+lambda*(y-Y)`, where lambda is its inverse slope; test a<q. This includes every inverse ray without a search cap. The proof uses alpha-beta>=1 to obtain `a+1>=(c+1)(y+1)/(Y+1)`. It makes no claim beyondK or at anchorY1.

For an affine forward endpoint y=gq+h with q>=b and Y=gb+h, the uniform anchor bound is `ceil(max(b+1,(Y+1)/g))-2`. A valuation1 canonical prefix gives exactlyb-1. The contracting paths465→43→65→49→9→7→11 and497→11 give lifted p<q even though497>465; their safe cutoff is538. This refutes the unrestricted smaller-anchor shortcut.

The supplied4892-state R80 table has exactly one canonical origin below11547 reaching17321:11391, at quotient depth13, with inverse slope2^20/3^13. Consequently, for `q=11547+16*3^D*t`, D>=1,t>=0, its one-step future has no smaller origin throughD+1 whenD<=11; whenD>=12 its sole smaller origin within that horizon is `p=11391+2^23*3^(D-12)*t`, at depth13. At t0 the table gives the unique smaller origin at every depth; positive lifts are scoped toD+1. This is sharp for the named target, not for other futures or arbitrary currents. The same theorem excludes smaller ancestors ofq throughD.

See [proof](../experiments/residual_progress/history_frontier/HISTORY_FRONTIER.md), [compiler](../experiments/residual_progress/history_frontier/history_frontier.py), and [receipt](../experiments/residual_progress/history_frontier/history_frontier_audit.json). Replay covers the full anchor,44 lifted histories,23 finite inverse trees,36 shadow words including large rays,10 cutoff controls,16 rejections and two supplied currents reconstructed from R80. No unknown absorption search is used. Universal history access remains unproved.

## R83 — High histories beyond every prescribed native growth depth

**Status: written conditional all-return-count CRT construction, complete scoped failure and full supplied finite demonstration.**

For each r>=0 put s=r+1 and choose the unique `0<L<3^(6s+2)` with `64^L=217/8272mod3^(6s+4)`. Let h=11L+8s. Two exact positive CRT cells have `v2(217b+223)=9r+17`, c=U^s(b)=137mod1024, and exact point orderh on the second quotient inverse ray ofq=3(9c-1)/16. Their smaller endpointp satisfies p<b. The slope is `9*(131072/177147)^L/18^s<=1/2`, with a strictly negative omitted affine term; the strict inequality holds for every positive member, not only eventually.

The actual upper word from3b is `(1,2,1),(1,1,2,1,1,3)^s,(1,1,3)`; the lower word fromp is `1^h,2,6L+3,1,2,1`. They meet at M=(2187c+925)/512>3b, with ordinary clocks(6r+12,h+5). Their prefix difference plusH_p-H_b has signed requestsA_p-A_b, all ranks below3b. Smaller currents remain supplied premises. The first(r,L,h) are(0,740,8148) and(1,2028089,22308995); huge later words are represented symbolically with explicit materialization caps.

For r>=1 the complete two-ray/point procedure succeeds exactly when h>=1 andp<3b; h0 restores the old exit. All ray indices are covered by a proved finite cutoff: J=floor(log2(3b-1))-1, P=floor((3/2)^J*(3b-1)), and `64^L<=floor((9P-2)/(9a0+7))`. At b96797577 onlyL0,1,2 on each ray need testing and all six fail, with full signed frontiers retained. A supplied absorption witness confirms this is a limitation of that procedure, not a missing-current theorem. Other inverse words, cycles and later histories are outside the exclusion.

See [proof](../experiments/residual_progress/native_growth_escape/NATIVE_GROWTH_ESCAPE.md), [constructor](../experiments/residual_progress/native_growth_escape/growth_escape.py), and [receipt](../experiments/residual_progress/native_growth_escape/growth_escape_audit.json). Replay covers20 symbolic depths through64,160 modular phases, four exact terminal-unit/index cells, six exhaustive failure cases,21 rejections and a capped-decision check. A fully materialized r0 comparison has8165 rows; its supplied31041/39181-arrow absorption paths compile to an exact129-row pair current. The inputs are stored losslessly and checked edge by edge. Coverage of the entire H17 type and universal terminal supply remain open.

## R84 — Complete later-target decision and sharp twenty-step quotient descent

**Status: written complete decision for one conditional comparison; terminal currents remain supplied.**

For every `q=11547+3*2^19*k`, k>=0, the first thirteen ordinary valuations are exactly `(1,2,1,1,1,1,1,2,2,1,1,2,2)`, with canonical sources and raw endpoint `R=70237+2*3^14*k`. Retain the full native plan `prefix_13(q)+J_R-J_(q/3)`, with signed requests `A_R-A_(q/3)`. The exact inequality `4(R-1)<25(q-1)` makes its original-rank decision finite.

Above q, every no-pair transition is one of `A(x)=(3x+1)/4`, `B(x)=(3x-1)/8`, `C(x)=(3x+1)/16`, on their exact guards. Their shifted contractions allow only fourteen above-threshold templates: `A^j` with j<=6, `A^i B A^j` with i+j<=2, and C. In at most seven transitions the procedure either reaches a normal form n<q or exposes a unique highest critical request of rank n>=q with coefficient+1. The lower negative frontier cannot cancel it. This is an if-and-only-if decision for this plan, not for all currents at that seed.

The full classes k12mod16 and k20mod32 succeed; k1mod4 and k7mod8 fail. The proof gives the remaining initial rows and the complete bounded decision. R81's cell intersects this family exactly when3^11 divides k, so whole successful subprogressions are new to that cell. Every member retains the old R44/R52 higher endpoint `55495+2^7*3^10*k`; no claim of entire-dispatcher nonrecognition is made. On k9954mod16384 the first quotient descent is exactly step20. The ordinary prefix-difference clocks are `(ell+beta,beta)`, ell13..20, with beta determined by terminal normalization; no uniform twenty-step ordinary bound is asserted.

See [proof](../experiments/residual_progress/history_transition/HISTORY_TRANSITION.md), [constructor](../experiments/residual_progress/history_transition/history_transition.py), and [receipt](../experiments/residual_progress/history_transition/history_transition_audit.json). Replay covers1024 full plans,70 template instances covering all fourteen words,144 progression cases,20 sharp cases,66 actual old failures and26 rejections. Three complete supplied outputs outside R81 have148/153/172 rows. All signed premises and failed leaders are retained. The fixed dispatcher is unchanged; failed leaves and universal terminal supply remain unresolved.

## R85 — All-ray exclusion of uniformly bounded smaller-history clocks

**Status: written clock-bound theorem, including exact positive critical families.**

Let canonical q>0 satisfy3^D|q, D>=1, and let its first J ordinary arrows have valuation1 with every state canonical. Write `y_a=T^a(q)=S^a(q)=(3/2)^a(q+1)-1`. For every a<=J, the only canonical origin p<=q reaching y_a in at most D+a quotient steps is q itself, at depth a. This includes every inverse word and every ray index within that clock bound. The separate ordinary-clock version holds for every positive odd q with the same divisibility and valuation-one prefix, without canonicality.

The all-ray proof follows the affine shadow `x=lambda*q+c`. Ternary precision makes each selected inverse branch legal on the shadow; `lambda-c>=1` persists. Point inverses retrace the growing prefix. A first ray makes c positive, and an explicit dyadic-denominator estimate keeps it positive until it becomes an integer. It stays a positive integer thereafter, forcing x>q. The ordinary proof separately handles negative rational shadows rather than assuming they remain integral.

For H>=max(J+1,3), the coprime conditions `q=0 mod3^D` and `q=2^H*u-1 mod2^(H+2)`, `u=-3^H mod4`, give an infinite positive progression with q/3 inW5. Thus any fixed future/partner clock budget misses some actual critical inputs, even allowing all words and inverse rays. The source depends on the chosen budget. A separate H17 CRT family excludes smaller histories to q through D and to its first future through D+1 only; later exit targets are outside that corollary.

See [proof](../experiments/residual_progress/history_cover_scope/HISTORY_CLOCK_BARRIER.md), [arithmetic constructor](../experiments/residual_progress/history_cover_scope/history_barrier.py), and [receipt](../experiments/residual_progress/history_cover_scope/history_barrier_audit.json). Replay covers62 quotient and126 ordinary domains with3911/16008 origin instances,196 critical and60 H17 CRT cells,200 inverse words,15 equality spines,1560 ordinary-word attempts and23 rejections. The absorbed q39 control still has T^3(q)=33<q and a supplied nine-row P13 current. No fixed-source nontermination, exclusion of arbitrary signed currents, unrestricted history failure, or universal supply follows.


## R86 — Exact smaller-target cone after an even complementary exit

**Status: written conditional construction and complete raw-target classification.**

Let H>=3,b>=1, q=2^H*t-1 divisible3, and `3^(H-1)t-1=4^b*u` with positive odd u and n=3^b*u1mod8. The even endpoint f=2n+1 is selected; after its normalization and one free arrow, the raw target is y=(3n+1)/4. Exactly `y<q iff 3^(H+b)<2^(H+2b+2)`, with no small-source exception. The full comparison is the ordinary prefix of length H+b+1 from q minus the single row at y, with clocks(H+b+1,1), quotient length H+b and boundary[q]-[y]. Adding native J_y-J_(q/3) retains every signed request below q throughout this cone.

For every H>=4, the least closing b gives n>q>y. Complete positive CRT cells permit every exact v3(q)=D>=1 and both ternary units. At H4,b1 the entire phase is w293mod512; its subphase w293mod4608 is outside all seventeen old direct predicates by arithmetic domain analysis. The old R48 formal current already contains the extra free step, and its W5-only requests are also strict on this cone. The new scope is exact coverage beyond the old coarse sufficient bound, not a new local orbit identity or an exclusively native-basis gain. The fixed dispatcher is unchanged.

Outside the cone only the raw-target inequality fails. The q927 control has y1321>q but further formal normalization succeeds. Do not call such a case a missing current. See [proof](../experiments/residual_progress/even_exit_history/EVEN_EXIT_HISTORY.md), [constructor](../experiments/residual_progress/even_exit_history/even_exit_history.py) and [receipt](../experiments/residual_progress/even_exit_history/even_exit_history_audit.json). Replay covers640 arithmetic cells,50 full plans,256 minimal-H cells throughH256/D32,72 valid CRT memberships in7680 attempts,34 old17 progression cases and28 explicit rejection controls. Three fully supplied outputs have29/79/73 rows. Universal terminal supply remains open.

## R87 — Every failed R84 W9 leader reduces to at most one higher W5 input

**Status: written complete local decision and bounded conditional reduction.**

For odd Q>=11547 and W9 index w with Q<=3w and32w<33Q, compose the full local R40 plan at the ORIGINAL threshold Q. Every helper is strict; at most one high request survives with coefficient+1. With d=v2(9w-1) and z=3^h(9w-1)/2^d (h=(d-5)/2 for odd d, (d-4)/2 for even d), odd d always passes. The even rows are decided completely by canonicality of3z, its comparison to Q, and the criticality/rank of f=(9z+1)/4. The only possible W9 leader is z, with16z<9w. After at most two W9 substitutions, every remaining high request is a single W5 input; the factor bound is8019/8192 relative to Q.

Every R84 failed W9 leader lies in this window. Thus the full procedure, including exact current rows and signed cancellation, either passes the original q or retains precisely its higher W5 input. On every even noncanonical-upper branch X=6z+1, R46's maximal inverse has D=h+1,j1 and origin3w. Full substitution restores self coefficient+1 with current J_w-L_lower-J_(2z+1) and lower coefficients A_w-A_(2z+1). That lower identity need not vanish. The theorem excludes progress from this exact undo, not alternative words or later histories.

See [proof](../experiments/residual_progress/w9_history_repair/W9_HISTORY_REPAIR.md), [constructor](../experiments/residual_progress/w9_history_repair/w9_history_repair.py) and [receipt](../experiments/residual_progress/w9_history_repair/w9_history_repair_audit.json). Replay covers865 generic cases,72 threshold cases,72 exact-depth cells through128,72 R84 repairs among517 examined indices,51 full inverse undos and37 rejection controls. Three fully supplied outputs have166/49/61 rows. There is no universal supply of the final W5 request or of all smaller signed premises. The dispatcher and frozen resolvers remain unchanged.


## R88 — Complete four-target history classification on a whole remaining cell

**Status: written lifting proof with complete finite inverse-tree certificates; no terminal-current supply.**

For every m>=0 let `Q=133704987+3*2^33*m`, `n=385940463+64*3^19*m`, and `y_a=3^a*(n+1)/2^a-1` for a=0,1,2,3. This is the whole k=85+16384m cell after the R87 repair and returning comparison. For each a, all canonical origins p<=Q with `T^d(p)=y_a`, `0<=d<=19+a`, consist exactly of p=Q at d=18+a. The strict smaller-origin exclusion also holds for ordinary histories to these canonical targets, and to raw r=2n+1 through19 ordinary arrows. Every inverse ray and word within the stated horizons is included.

The affine inverse bound gives the uniform anchor cutoff `c+1<133704989+1226171/387420489<133704990`; parity therefore gives c<=133704987. Four complete anchor trees contain64/78/89/101 states, each with its sole qualifying origin at depth18/19/20/21. The receipt stores every retained edge and first-excluded ray child. Each sole-hit word lifts exactly to Q. This is a finite certificate plus an all-m proof, not extrapolation from representative integers or an all-depth exclusion at a fixed source.

A single fixed quotient inverse word of length d, valid for EVERY m, would have integral origin increment `2^E*(64*3^(19+a)/2^a)/3^d`, forcing d<=19+a. Hence no one fixed word of any length gives a strictly smaller origin throughout this entire cell. The same conclusion holds for a fixed ordinary valuation word. Fixed clocks with valuations depending on m, finer parameter partitions, input-dependent words, later targets and arbitrary signed comparisons remain outside this exclusion.

The existing full comparison is preserved: `T^18(Q)=n`, `S^23(Q)=S^5(n)`, with current `K=L_23(Q)-L_5(n)` and boundary[Q]-[n]. Its first18 ordinary valuations are fixed, with total valuation26; the full23 valuations are not asserted fixed. Writing b=Q/3 and v=n/3, one has b,v<Q<n. Supplied H_v,H_b would give `div(K+H_v-H_b)=P(b)-P(v)`, leaving the higher positive P(v) premise unresolved.

See [proof](../experiments/residual_progress/history_cell_scope/HISTORY_CELL_SCOPE.md), [arithmetic implementation](../experiments/residual_progress/history_cell_scope/history_cell_scope.py), and [receipt](../experiments/residual_progress/history_cell_scope/history_cell_scope_audit.json). Independent replay derives inverse bases from elementary fibres and checks all four complete trees,28 lifts,1024 canonical-arithmetic cases, three full signed23/5 comparisons and20 domain/cap rejection controls. No absorption input discovery, accepted dispatcher rule or universal history termination is supplied.

## R89 — Retained lower histories give a sharp three-node W9 reduction

**Status: written conditional construction; complete bounded reduction with explicit terminal premises.**

For odd Q>=11547 and C in W9 with `Q<=3C` and `3C+1<4Q`, retain the original lower history H_C and only the actual upper prefix U from3C to F. The full plan is `U+J_F-J_C`, with request vector `A_F-A_C`. Every lower request is strict at Q. There is at most one high request, with coefficient+1; any high W9 index z obeys `16z<9C` and `4z<3Q`. It lies in R87's smaller window, so at most two more substitutions remove it. At most THREE W9 nodes leave only lower premises and possibly one higher W5 input. The family C585+4096j,Q441+3072j,j>=4 needs all three nodes for this procedure. Its j4 chain is16969→9545→5369 at Q12729. Sharpness is not asserted among all possible constructions.

The odd-depth actual upper endpoint is F(3z)=12z+1, with prefix length h+2; replacing it by3z uses common-tail clocks(h+3,1). The even endpoint is6z+1. In its free-arrow subcase f<(27Q-5)/16<2Q, at most two A arrows fall below Q; no B/C transition is needed for this theorem. The strict +1 condition matters: C15401,Q11551 has S(C)=Q and is rejected. The number of W9 substitutions does not bound the unbounded ordinary clocks.

On R88's entire retained cell, the first H4 block has exact second depth `d=2+v2(E)`, where `E=162818633+3^22*m`. Complete depth progressions include the extra valuation bit. All odd d>=9 and even d>=16 give a strict raw target; every m0mod16 first-depth2 W9 leader satisfies the enlarged theorem. Other phases preserve the complete formal coefficients; m10 refutes an oversimplified two-index leader list.

On the whole subcell m2736+4096l, the usual next local composition has high vector `+P(a)-P(b)`, with beta=(9E-1)/64,a12beta+1,b4beta+1. The lower retained history supplies a strict conditional plan for P(b). Substitution with its NEGATIVE coefficient cancels exactly to the upper-only plan, leaving +P(a). Combined with a fresh original comparison this is an actual25-arrow Q→X path, X18beta+1, followed by two arrows to Z=(81beta+7)/4. The inherited R87/R44 expression additionally retains three explicit lower zero-source relations D+E0+Fv and their premise vectors; these currents need not vanish.

The prescribed further continuation is a complete finite decision on that coupled subcell, leaving zero or one high W5 request. Explicit l4/l13 cases remain unresolved. A proposed recurrent contraction fails: the canonical next depth2 branch has slope `3^12/2^19>1` relative to the old raw6v+1, and its named point inverse returns exactly to Z. This is neither a terminating recursion for all exits nor supply of the remaining pair.

See [proof](../experiments/residual_progress/retained_history/RETAINED_HISTORY.md), [constructor](../experiments/residual_progress/retained_history/retained_history.py), and [receipt](../experiments/residual_progress/retained_history/retained_history_audit.json). Every actual output requires every signed terminal input. The fixed dispatcher remains unchanged. Universal current supply and Collatz remain open.

## R90 — Complete binary return and maximal-exit control at the original rank

**Status: written arithmetic classification and conditional signed construction; terminal supply remains open.**

Put A=3^12, M=2^19, B=299947, D=7153 and Phi(v)=(Av+B)/M. The broader guard is v133797mod2^18, equivalently 2^18 divides L(v)=Dv+B. The exact raw and canonical-start words both have twelve ordinary arrows; their common complete v-cylinder has modulus2^19. A guarded re-entry satisfies L(Phi(v))=(A/M)L(v). Every fixed guarded positive input has exactly floor((v2(L(v))-18)/19) complete re-entries. Each consumes19 binary digits, gains12 ternary digits and increases height. Every prescribed finite repetition count occurs in the original coupled R89 cell, but that original ternary cell is not invariant under Phi.

At maximal exit, h=v2(L(v)) is18..36. All19 rows have an exact fixed ordinary prefix followed by one arbitrary valuation a>=p, with its complete extra-bit cylinder and pullback to the original parameter. The raw endpoint comparison with the ORIGINAL Q is an exact affine inequality. For any fixed h,a, its positive terminal slope is multiplied by (A/M)^r, so that fixed template cannot give raw descent at arbitrarily large r. Native normalization can still succeed above Q; the receipt preserves65 such controls.

The existing comparison has quotient clock18+12r and ordinary clocks(23+12r,5). Its full signed pair plan retains a unique highest request P(v_r) with coefficient+1. Fresh continuation to an exit y gives prefix(Q,L)+J_y-J_(Q/3) and vector A_y-A_(Q/3). Every negative request is below Q, so extending this forward history creates no negative high cancellation. The complete exit-cell image is a tail of one progression modulo a power of3; unconditional absorption of one whole cell would already imply Collatz via its explicit ancestor-cover property. This does not make a conditional strict-premise pair repair equivalent to unconditional absorption.

See [proof](../experiments/residual_progress/phi_exit_control/PHI_EXIT_CONTROL.md), [module](../experiments/residual_progress/phi_exit_control/phi_exit_control.py), and [receipt](../experiments/residual_progress/phi_exit_control/phi_exit_control_audit.json). Replay covers10 full return plans,19 rows,171 signed exits,15 modular ancestor certificates and29 rejections. Three complete unfinished exit plans have156/283/498 rows. The binary countdown proves departure from one subsystem; it gives no decreasing measure across subsequent exits and supplies no universal terminal current.

## R91 — A finite rational basin proves an all-word precision barrier

**Status: computer-assisted inverse-word theorem with a written positive-source corollary.**

At c0=-899841/7153, every legal finite canonical quotient inverse word, with arbitrary ray indices, length d and affine slope lambda, satisfies

`lambda*(3^12/2^19)^max(0,ceil((d-5)/12)) >= 1`.

Reversing full twelve-step cycles attains equality. This is an arbitrary-length rational-shadow theorem, not an extrapolation from bounded word searches. A first strict counterword would start at primitive odd canonical -u/7153 with7153<u<7277133. The proof uses t=u-7153 and t'=alpha*t+7153*delta,0<=delta<alpha; prefix slope bounds collapse the unknown word length to that finite origin interval.

Independent signed Python and positive-magnitude C++ implementations classify all1,732,883 eligible origins. Only19 reach c0, and all19 first-hit weighted slopes are at least1. Every other origin is resolved by an actual path to a classified state, a distinct detected cycle or the invariant region x>-1. No cap is treated as failure, and none fires. Intermediate numerators reach1,049,066,989,135; the origin bound is never used as a trajectory height cap. Further visits to c0 add(12,19), preserving the score.

For the original coupled cell v0=67839005952677+2^18*3^18*ell,Q=70506316836123+3*2^45*ell, let at least r guarded Phi returns be available. Write n_r=3Phi^r(v0). **No positive canonical p<=Q reaches n_r in d<=12r+5 quotient steps**, including every inverse ray and every word in that horizon. The actual-shadow difference has ternary order12r+5, so each legal actual word lifts to the rational theorem. Its intercept is controlled by

`p >= n0+1-(243/32)*2^(7r) > Q`,

using n0=3v0>2Q and L(v0)>=81*2^(19r+18). This holds for every eligible original source, not only least CRT representatives. The known original Q reaches n_r at18+12r, thirteen steps beyond the exclusion. The ordinary comparison retains clocks(23+12r,5).

See [proof](../experiments/residual_progress/shadow_precision/SHADOW_PRECISION.md), [Python classifier](../experiments/residual_progress/shadow_precision/shadow_precision.py), [independent C++ classifier](../experiments/residual_progress/shadow_precision/independent_basin.cpp), and [receipt](../experiments/residual_progress/shadow_precision/shadow_precision_audit.json). The replay also checks306 positive inverse words on21 families through r128, all cycle branch types and invalid domains. The universal word quantifier rests on the first-counterword proof plus the exhaustive finite basin, not those positive samples. Longer positive histories, deeper ternary data, later targets and arbitrary signed currents remain available; no all-depth positive exclusion or terminal supply is claimed.

## R92 — Fourteen further history steps give only the original source

**Status: computer-assisted finite-window theorem, uniform in the source and return count.**

For every original coupled source in R90 with at least r guarded returns, put n_r=3Phi^r(v0). Among positive canonical origins p<=Q and quotient depths d<=12r+19, **the sole solution of T^d(p)=n_r is p=Q at d=12r+18**. All ray indices and intermediate heights are allowed. This extends R91 by fourteen steps and resolves the saved candidate; it supplies no new current and is not an all-depth positive-source exclusion.

The full affine bounds give normalized prefix slope1<=mu_h<102 at h=12r+5 and whole-word slope below1/2. A boundary first-hit tail has d0=12k0+5,E0=19k0+m,m8..14. Its numerator satisfies the exact selective conditions

`243u = 899841*2^m (mod7153), 7153<u<7153+(2^m/243)*(892688+12*3^12)`.

The seven classes contain67,992 odd candidates and33,995 canonical origins. Complete signed forward classification leaves exactly16 relevant first-hit tails, with no unresolved or capped path. Their actual boundary states are affine in ell with coefficient2^(m+18)*3^14 and are independent of r once r>=k0. This fixes every branch decision for the next fourteen inverse steps. Every potentially successful suffix has exponent sum at most21, so the suffix search is complete and finite. Full affine comparisons retain all intercepts and the binary guard. The only two endpoints with necessary normalized score below1/2 are `(9Q+5)/8` at suffix depth11/cost16 and `Q` at depth13/cost19. The first is always too large; the second is the self-history.

Independent positive-numerator C++ classification exhausts the larger interval7153<u<741545113:176,754,119 canonical origins,1,939 total target hits, the same16 phase/cost tails, and zero caps. Intermediate numerators reach23,508,760,799,607,151; the origin bound is not a trajectory cap. The default Python replay uses the smaller complete selective universe. See [proof](../experiments/residual_progress/deeper_window/DEEPER_WINDOW.md), [selective classifier](../experiments/residual_progress/deeper_window/sparse_basin.py), [suffix enumeration](../experiments/residual_progress/deeper_window/deeper_window.py), and [receipt](../experiments/residual_progress/deeper_window/deeper_window_audit.json).

This supports a focused pivot to later meeting targets or genuinely different signed histories. Still longer histories remain possible. No termination mechanism, universal current supply, Collatz proof or novelty claim follows.

## R93 — Actual two-source normalization and complete lower first departure

**Status: written arithmetic proof with a finite rational-orbit certificate; unfinished comparison currents.**

On the entire original coupled family, put z=471104208005+2^14*3^16*ell. Then v0=144z-43, Q=(2^31*z-665034679)/3^15, and the actual ordinary paths satisfy S^18(Q)=864z-257 and S^16(Q/3)=z. Their difference gives an exact two-atom residual `[864z-257]-[z]`, without assuming any helper current.

The guarded upper return is conjugate to Psi(z)=(3^12*z-53)/2^19. With n=v2(7153z-53), one complete re-entry is legal exactly at n>=33, consumes19 binary digits and increases z. The maximum count is floor((n-14)/19); at upper exit n=19r+h-4, h18..36. Integrality of the new z does not give an actual lower-source path to it. The return leaves the explicit additional defect `[Psi(z)]-[z]`.

The rational lower shadow starts at53/7153. Its complete448-state certificate has a71-step/cost146 preperiod and a377-step/cost739 cycle. Every state is below115 and every prefix slope is at most1; the cycle contraction extends that bound to all prefixes. If cumulative shadow costs satisfy E_i<n<=E_i+e, the actual lower path agrees through i arrows and then has valuation n-E_i when n-E_i<e, or e+j with explicit arbitrary j>=1 when equality holds. Exact extra-bit cylinders realize every row in the original parameter. This classifies the first lower departure for every upper repetition count; finite phase labels alone do not prove subsequent termination.

Every matching lower state is below z+115. The last matching state and its next12 actual arrows, including the departing arrow and at most eleven further arrows, stay below the ORIGINAL Q. The full signed path comparisons retain an upper residual source above Q and a lower source below Q. They supply neither the residual current nor a new accepted dispatcher domain.

See [proof](../experiments/residual_progress/two_source_history/TWO_SOURCE_HISTORY.md), [constructor](../experiments/residual_progress/two_source_history/two_source_history.py), and [receipt](../experiments/residual_progress/two_source_history/two_source_history_audit.json). Focused replay covers the complete rational certificate,64 initial identities,3520 exact departures,180 joint upper/lower cases through r128,739 periodic phases, three full unfinished tables and19 rejection controls. The next obligation is a comparison after this complete departure interface that supplies the positive residual with a proved original-rank decrease or other terminating construction.

## R94 — The prescribed ternary child cannot use bounded clocks

**Status: written scoped theorem with an exact finite rational-word certificate and complete cylinder constructor.**

For every digit c0..2, every ordinary clock bound K>=0 and every prescribed initial Phi return lower bound R>=0, there is an infinite positive binary progression of j for which ell=c+3j>j, the parent has at least R returns, and S^a(Q(ell)) differs from S^b(Q(j)) for ALL a,b<=K. Thus the proposed child Q(floor(ell/3)) cannot be supplied on its whole domain by a finite catalogue of word pairs, even after arbitrary finite binary refinements. The witnesses may change with K and R. This says nothing against unbounded input-dependent clocks, other child families or arbitrary signed currents.

All three digits use the same negative rational parent center q*=-515908491727/11404192419 and ell*=-22852975802/34212577257. The upper shadow follows an18-prefix and a negative12-cycle. The first two child shadows are positive. The third follows an exact112-word negative path disjoint from the entire upper orbit, then reaches1663/7153>0. Their rational orbits are therefore disjoint at every pair of clocks. Sufficient binary precision fixes both finite actual valuation words. Every prospective merger is a nonzero affine equation, whose finitely many nonnegative integer roots are excluded by further binary refinement. Precision at least19R also gives the prescribed returns. This proves whole progressions, not a finite-sample extrapolation.

See [proof](../experiments/residual_progress/child_history_scope/CHILD_HISTORY_SCOPE.md), [complete cylinder constructor/checker](../experiments/residual_progress/child_history_scope/check_child_catalogue_scope.py), and [receipt](../experiments/residual_progress/child_history_scope/child_history_audit.json). Replay covers39 complete cylinders,156 positive integer pairs, the112-word certificate and13 rejected invalid inputs. The earlier conditional child identity remains valid if its missing merger and every signed helper are supplied; no such universal supply is established.

The separate [later-target probe](../experiments/residual_progress/later_target_probe/LATER_TARGET_PROBE.md) reuses R83's exact finite cutoff to decide all rays followed by point inverses at two later exits. It preserves the direct-point/native-priority distinction and the full signed requests. The older R44 forward rule repairs the r8 example at the original rank, so a failed inverse method is not a missing-current theorem. These controls add no new accepted family or universal terminal supply.

## C1 — Independent audit of R2–R4 and of main's R5, R6, R9, R10

**Status: finite checks and model-assisted re-derivation; no discrepancy found.**

The audit re-derived Theorems 1 and 3 and rechecked them with an independent implementation. That implementation reproduces the repository packets exactly.

- **Theorem 1, (3):** the transfer identity holds exactly for every `8 <= N <= 160` and every horizon up to extinction.
- **Theorem 1, (2):** the core-remainder bounds hold for every `N <= 10^5` and for 3,132 sampled `N` up to `10^18`.
- **Table (7):** the dyadic table holds for `b <= 1500`.
- **(6):** the valuation partition passes a non-vacuous orbit-indicator test.

A least counterexample cannot be `2 mod 3`, so the least-exception route always gives pairing −1. **The `N^(3/2)` maximum principle is therefore load-bearing for statements 2 and 4.** It is not redundant.

The same independent construction also cross-checks two results committed on main in `8d62dcc`:

- **Five-ray criterion (main's R5):** its exact cutoffs, upper targets, comparison exponents, sub-96 boundary points, and `89/90` constant hold for all five rays and `3 <= b <= 400`.
- **Annular recursion (main's R6):** `Pi_(64N)=Pi_N+A_N` and `eta_(64N)=eta_N` hold, together with the supports, all 36 band coefficients, band totals, `||A_N||_1=99N/2`, `||A_N^+||_1=99N/4`, `|supp A_N|=267N/8`, and `sum y A_N(y)=63Q`. Checked for 68 cutoffs, up to expanded cutoff 262144.

The written five-ray proof was re-read and no gap was found.

This is not human peer review or formal verification. See the [negative-controls note](../collatz_research_20261017/negative_controls/NOTE.md), Sections 4, 6 and 10, and the receipts [reduction_audit.json](../collatz_research_20261017/negative_controls/reduction_audit.json) and [main_claims_audit.json](../collatz_research_20261017/negative_controls/main_claims_audit.json).

Main commit `ce56699` makes two further claims that were checked here as well:

- **R9:** `||P A_N||_1=||R A_N||_1=171N/4-|c_N|` for 68 cutoffs; the `2N` survivors; and `c_80000=0`, using an independent point evaluator.
- **R10:** `Phi(A_96)=17` at exposure depths 20–27, and `0` at depth 28.

Numbering note: the C-series comes from an independent lane (branch `claude/claude-vs-chatgpt-perf-8230f6`). It is kept separate from the R-series so the two numberings never collide.

## C2 — Negative controls on 3x+d and a scoped barrier

**Status: written lemmas plus finite certificates.**

Consider the maps `T_d(x)=(3x+d)/2^v` with `d=2^k-3`; these fix 1, and for `d>1` they also fix `d`.

- **The construction carries over.** The same right-aligned packets and a counting identity with explicit edge terms both transfer to `T_d`. The identity is checked non-vacuously.
- **The criterion fires where the conjecture is false.** Every surveyed map with nontrivial cycles has cutoffs where `<e,Pi_N> > 0`. At such a cutoff, no finite current with nonpositive residual exists and packet work grows linearly. Finite orbit certificates verify both facts.
- **`d=61` is a locally Collatz-like control.** All its core points and all seeds below 175 terminate, and the obligation holds for every `8 <= N <= 212`. It then fails at `N=213`, because of a 41-cycle with minimum 235.

Consequently, no argument that applies verbatim to `T_61` can discharge the primary obligation for `3x+1`. This includes induction on N that uses only those generic properties.

See [note](../collatz_research_20261017/negative_controls/NOTE.md), Sections 1–3, and [receipt](../collatz_research_20261017/negative_controls/negative_controls_audit.json).

## C3 — Certificate minimality

**Status: written proof; finite check against the archive.**

Suppose an exact finite current `J_0` exists for `mu`. Then every finite certificate `mu=(I-P)J+zeta` with `zeta<=0` satisfies `J>=J_0` pointwise, provided its difference support contains no nontrivial cycle. Within that comparison class, `J_0` is the unique exact current and minimizes `||J^+||_1`; one-sided minimizers need not be unique.

When all atoms terminate, `J_0=sum_j P^j mu` is the time-aggregated forward push. The archive's stored currents equal this forward aggregate row for row: 2,736 rows at `N=4096` and 132,998 rows at `N=262144`.

The lemma does not eliminate one-sided alternatives or structural search. The [PR review](../collatz_research_20261017/negative_controls/PR1_REVIEW.md) exhibits two minimum-cost1 currents for `delta21-delta3`; for actual A_768 it removes the exact current's row `J_0(5)=-55`, leaving residual `-55delta5`, with the same positive cost53758 and one fewer row. Preserve the finite-exact-current and no-cycle hypotheses of pointwise domination. A formal infinite forward sum is not automatically a finite certificate. See [note](../collatz_research_20261017/negative_controls/NOTE.md), Section5, for the corrected scope.

## C4 — Progress measures that do not separate 3x+1 from 3x+61

**Status: finite certificates.**

Consider the 64-fold increments `A'_N=Pi'_(64N)-Pi'_N` of `T_61`, at `N=8,16,24,32`.

- **Compression looks the same.** Their one-pass compression ratio is `0.849–0.863`, compared with `19/22≈0.864` at `d=1`.
- **Early exposure looks the same.** `Phi` falls by about 97% within 25 exposure depths.
- **But `Phi` never reaches zero.** At depths up to 400, `Phi` equals the pairing `<e,A'_N>`, which is 6–13. The surviving component contains the whole 41-cycle, so it can never join an absorber.

Hence neither one-pass contraction nor early `Phi` decay is evidence that `3x+1` plateaus end. See [note](../collatz_research_20261017/negative_controls/NOTE.md), Section 11, and [receipt](../collatz_research_20261017/negative_controls/progress_measures_audit.json).

## C5 — A direct attempt: negative results and class-wise equivalence

**Status: written corollary plus finite certificates. No proof of the obligation.**

- **Six exact-current samples reach the bottom.** At `N=96,168,384,768,1536,3072`, canonical exact currents carry nonzero signed traffic into1. The observed costs are approximately75N; no universal linear bound follows. The same bottom rows are not forced in one-sided alternatives, as the A_768 review example shows.
- **Class-wise equivalence.** Take any invariant class `K` with no members below 12096. Then all five-ray pairings `<1_K,Pi_M> <= 0` hold iff all annular pairings `<1_K,A_N> <= 0` hold, iff `K` is empty. The obligation therefore splits exactly into "no nontrivial cycles" and "no divergent orbits", each at full strength.
- **Controls.** For `T_-1`, `T_5` and `T_13`, each of the 14 cycle basins individually has a positive pairing.

See the [note](../collatz_research_20261017/negative_controls/NOTE.md), Section 12, and the [receipt](../collatz_research_20261017/negative_controls/attempt_probes.json).

## Open obligations and priorities

- **Primary:** construct a finite current (or one with nonpositive residual) at every cutoff on R5's five rays, and prove termination. R6's annular increments give an explicit sufficient target with its finite bases discharged. Arbitrarily large finite cost is permitted.
- **Current priority:** supply the positive W5 exit for one whole remaining type at the ORIGINAL rank, with an input-dependent construction and a proof of termination. R90 classifies all exits of one repeated growth pattern; its finite binary countdown does not control successive exits. R91 and R92 exclude every smaller origin at the repeated target through12r+19 quotient steps, across every eligible source and every return count. Prioritize later meeting targets or genuinely different signed comparisons; histories beyond the excluded window remain possible. R89's negative-history repair, R88's whole-cell scope and R85's fixed-clock barrier remain in force. Increased finite coverage alone is insufficient.
- Find an arithmetic recursion or another structural mechanism that controls unresolved positive contributions. R13 proves its total exposure depth cannot be uniformly bounded, even on one ladder. Finite successful searches alone do not prove universal existence. C3 provides a conditional cost floor, while allowing one-sided alternatives. C2/C4 require a general termination argument to use hypotheses that fail for T_61; candidate methods that extend to those maps must respect the certified failures at `(d,N)=(61,213)` and `(-1,16)`.
- Prioritize supply of retained W9 and remaining W5 inputs through smaller-origin history comparisons. R80 proves one whole blocked-W9 progression with an above-target merger and arbitrarily deep complete inverse barriers. R78 supplies complete native and next-A2 decisions; R79 shows exactly why a finite growing guard and its two standard inverse repairs can fail at the original rank. Neither closes the remaining types. R75 translates sigma plans before mixing them with rho plans; R76 retains its narrow fixed-word exclusion. R77 and the [latest pinned side-lane argument](../experiments/residual_progress/side_lane_review_fcc7e88.md) constrain hypothetical survivor complexity without proving emptiness. Preserve all signed requests, supplied histories, original-rank tests and distinct ordinary/quotient clocks. The [history audit](../experiments/residual_progress/adjacent_history/HISTORY_SCOPE.md) limits a specific older compiler; R80's particular family works with both frontiers. The W5 dispatcher and frozen internal resolvers are unchanged.
- Prove finite progress for every positive exposed-component plateau, or close R8/R9's residuals in a family with a decreasing integer parameter. R8 deletes only certified source coefficients; R9 contracts only one pass. Neither handles its full residual.
- R11 gives a finite conditional compiler that retains boundary terms and can end a plateau if its packet inputs are supplied. Develop a noncircular source of those inputs. R12 rules out obtaining a new descent merely by alternating the existing P and R operators.
- Independently audit cutoffs, absorption, the five-ray transition, finite bases, annular table, and maximum principle. Current review is computational and model-assisted. C1 is a separate, independent pass that found no error. There is still no human peer review or proof-assistant verification.
- Treat the earlier analytic mixing extension as a separate candidate with its own external dependencies. It is not needed for R2–R4.
- Keep historical failures and scoped results in the master handoff available. No Collatz proof, logarithmic mean-work theorem, or general cheap-current theorem is established here.
