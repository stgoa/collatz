# Result ledger

Last updated: 2026-10-17. This ledger summarizes scope; the linked proof notes and exact data contain the supporting arguments.

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
- Find an arithmetic recursion or another structural mechanism that controls unresolved positive contributions. R13 proves its total exposure depth cannot be uniformly bounded, even on one ladder. Finite successful searches alone do not prove universal existence. C3 provides a conditional cost floor, while allowing one-sided alternatives. C2/C4 require a general termination argument to use hypotheses that fail for T_61; candidate methods that extend to those maps must respect the certified failures at `(d,N)=(61,213)` and `(-1,16)`.
- Prove finite progress for every positive exposed-component plateau, or close R8/R9's residuals in a family with a decreasing integer parameter. R8 deletes only certified source coefficients; R9 contracts only one pass. Neither handles its full residual.
- R11 gives a finite conditional compiler that retains boundary terms and can end a plateau if its packet inputs are supplied. Develop a noncircular source of those inputs. R12 rules out obtaining a new descent merely by alternating the existing P and R operators.
- Independently audit cutoffs, absorption, the five-ray transition, finite bases, annular table, and maximum principle. Current review is computational and model-assisted. C1 is a separate, independent pass that found no error. There is still no human peer review or proof-assistant verification.
- Treat the earlier analytic mixing extension as a separate candidate with its own external dependencies. It is not needed for R2–R4.
- Keep historical failures and scoped results in the master handoff available. No Collatz proof, logarithmic mean-work theorem, or general cheap-current theorem is established here.
