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

## Open obligations and priorities

- **Primary:** construct a finite current (or one with nonpositive residual) at every cutoff on R5's five rays, and prove termination. R6's annular increments give an explicit sufficient target with its finite bases discharged. Arbitrarily large finite cost is permitted.
- Find an arithmetic recursion or another structural mechanism that controls unresolved positive contributions. Finite successful trajectory searches alone do not prove universal existence.
- Prove finite progress for every positive exposed-component plateau, or close R8/R9's residuals in a family with a decreasing integer parameter. R8 deletes only certified source coefficients; R9 contracts only one pass. Neither handles its full residual.
- Independently audit cutoffs, absorption, the five-ray transition, finite bases, annular table, and maximum principle. Current review is computational and model-assisted; there is no human peer review or proof-assistant verification.
- Treat the earlier analytic mixing extension as a separate candidate with its own external dependencies. It is not needed for R2–R4.
- Keep historical failures and scoped results in the master handoff available. No Collatz proof, logarithmic mean-work theorem, or general cheap-current theorem is established here.
