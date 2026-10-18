# Residual progress and finite forcing

**Latest standing:** universal tripling currents on W5={5 mod8} suffice.
The common rank rho(w)=nu(3w) now proves finite signed composition of four
strictly decreasing rules, including cases where the pair index grows.
New complete domains cover parts of the returning and nonselected phases,
and a two-block inverse rule works through unbounded depth. The complement
remains an explicit missing premise. A fixed ternary valuation cannot bound
all inverse delays, even after the specified one/two forward arrows.
These are written reductions and partial constructions; Collatz remains
open. The current batch and evidence are at the end of this report.

Started 2026-10-17 from clean pushed commit `ce56699`.
The preceding goal turn made progress: universal partial currents, an exact
one-pass compression, scoped counterexamples, and their reproducible evidence
were committed and pushed. Collatz and the universal complete constructor
remain open.

## Objective and completion standard

Find a proved mechanism that resolves the remaining positive annular components.
Completion of the research goal requires a correct universal construction or
other valid proof of Collatz; a stronger reduction or finite experiment alone
does not meet that standard.

## Falsifiable directions

1. Combining root collapse with transport closes a residual class with a
   decreasing integer potential.
2. Affine tree templates extend to an actual aggregate cover, or a precise
   aggregate obstruction identifies why a fixed catalogue cannot do so.
3. The five-ray comparison admits an explicit finite forcing certificate
   with its boundary terms retained, isolating a finite constructive task.

## Checklist

- [x] Revalidate repository and previous progress.
- [x] Probe residual transport and derive its valid scope.
- [x] Test aggregate template coverage and persist a complete finite-depth obstruction.
- [x] Develop a finite constructive use of the scalar comparison.
- [x] Audit the transport and finite-cone claims independently; persist counterexamples.
- [x] Integrate verified results, run checks, and compile the current note.

## Findings

### 1. A finite compiler retains the boundary terms and uses integrality

The new [finite-cone theorem](duality/FINITE_CONE.md) converts finitely many
supplied packet certificates into an exact integer absorption current. On
grid ordinals k=5b+i the source comparison has shifts -10,+3,-2. The rational
weight `(35/27)^k` contracts strictly. A finite nonnegative inverse supplies
exact rational weights for a measure identity, retaining every source-scale
current, rounding shell, and upper/lower boundary term.

The key step is an integer-component gap: an integer source with an exact
rational current and total positive residual mass below 1 has no positive
integer component obstruction. The same finite graph therefore supplies an
integer current with nonpositive residual. For a nonnegative counting source,
all source vertices are already connected to 1.

For target m, an explicit sufficient block contains O(log m) packet cutoffs,
the largest O(m^2.14682). This bounds the inputs required by the compiler; it
does not bound their construction cost or prove that they exist universally.

The [actual demonstration](forcing/ACTUAL_COMPILER.md) supplied 30 checked
one-sided packet currents at the starting cutoffs through 5376. Twenty of
those input searches finished with sources still unlinked to 1 in their own
graphs. Exact combination produced a rational current with 6217 rows and
positive residual mass `29145292346068/46422343855805 < 1`. The compiler then
extracted a stored 95-row nonnegative integer current for U_112, using only
the already present nonzero current arrows.

**What changed:** there is now a finite constructive form of the five-ray
implication, with every boundary term retained and no global-invariance
assumption. **What remains:** the packet inputs may lie above the target
scale. Assuming them during a decreasing induction is circular. The compiler
does not supply its own universal input certificates.

### 2. Root collapse and transport have an exact normal form

The [transport note](transport/ROOT_TRANSPORT.md) proves `R^2=R` and `PR=P`,
so every word in these operators reduces to I, R, P^t, or RP^t. On roots,
RP is conjugate to ordinary killed Syracuse on odd states coprime to 3.
Interleaving the operators changes representatives and current tables; it
does not introduce a different synchronous residual dynamics.

Exactly `floor(4N/2^t)-floor(2N/2^t)` explicit top-band sources retain
coefficient +2 through t transports and collapses. This rules out a fixed
transport depth for all required annuli. At N=a*2^b the top source survives
b+2 steps at `324*a*3^b-1`, also excluding a uniform linear height bound for
this process. Historical cancellation and other arithmetic rewrites remain
possible.

**Pivot:** repeated 19/22 contraction is false, with exact N=96 norms
`3533 -> 3124`. A later reachable residual even has norm13 and positive
mass4 unchanged after one more step. A longer-block progress theorem could
still hold, but requires a new argument; a one-step claim does not.

### 3. A complete aggregate obstruction at depth 32

The [inverse exposure method](templates/AGGREGATE_EXPOSURE.md) reconstructs
an entire exposed component without enumerating the O(N) source support.
It uses exact inverse branches under proved height bounds to decide whether
an arrow is among the first D arrows from any actual source. Explicit caps
return unresolved; only a completed component supports an obstruction.

At the required cutoff `N=96*2^24=12*2^27`, the complete depth-32 component
of the top source has 35 vertices and exactly three annular sources:
`(64N-1,-2)`, `(96N-1,+2)`, `(144N-1,+2)`. Its mass is +2 and it does not
contain 1. The 9171 inverse reachability decisions exclude every extra
attachment in that entire graph. Consequently no current supported on the
depth-32 exposure graph can have a nonpositive residual for this annulus.
This also excludes an exact source cover by tree templates whose directed
source-to-anchor depths are all at most 32.

**Pivot:** a growing positive top orbit alone is not a valid aggregate
witness. At N=10368 and depth2 its complete component contains 27 sources
with total mass zero. Historical intersections attach negative coefficients
that a forward-only inspection misses. All vertices and arrows of both
examples are persisted. Independent full forward graphs match the inverse
algorithm on 48 smaller cases.

At the end of the preceding batch, the depth-32 example was only a fixed
finite obstruction. The continuation below supplies the arbitrary-depth
theorem. Its intermediate symbolic extension needed
a parameter family with a proof excluding every additional incoming source;
the current inverse method supplies a tool to investigate that condition.

## Next obligation

Supply the finite compiler's packet inputs by a noncircular construction,
or find a different exact residual class with a proved decreasing parameter.
The current partial template families remain available. Any proposed cover
must account for the complete aggregate components, including sources that
attach at unequal times. The normal form above excludes obtaining a new
residual evolution merely by rearranging P and R.

## Verification status

Scoped checkers and the actual compiler pass. Independent model reviews
checked the root-1 absorption convention, surviving-atom count and height,
finite inverse positivity, every boundary sign, the integer gap, and the
main LaTeX transcription. Three transcription clarifications were applied:
lower grid indices, least admissible B for the cutoff bound, and explicit
general-graph scope of the fixed-point threshold counterexample.

`python3 scripts/verify_all.py --cpp` passed on 17 October 2026, including
all prior archive and certificate checks and the four new default checkers.
The existing LaTeX source compiled successfully. All 44 checked local
Markdown links resolved, and `git diff --check` passed. Commit history records
delivery of this batch; the universal research goal remains open.

## Continuation from `a7b7b47`

The next batch tests three specific ways forward:

1. Lift the *complete* depth-32 obstruction across infinitely many cutoffs,
   including every excluded inverse attachment, then test arbitrary depth.
2. Determine whether adaptive positive scale comparisons can supply their
   inputs using only already absorbed smaller seeds.
3. Use auxiliary sources to move the remaining positive annular mass, and
   test whether the resulting source family closes under a decreasing rule.

### Continuation checklist

- [x] Revalidate the clean repository and read the current proof obligations.
- [x] Prove and independently audit the symbolic lift and the stronger arbitrary-depth theorem.
- [x] Resolve the scope of smaller-seed input bootstrapping.
- [x] Construct and audit an auxiliary-source rewrite and its positive remainder.
- [x] Integrate the conclusions, reproduce all checks, and compile the note.
- [x] Review the final diff and prepare the authorized Git delivery.

### New structural result: every fixed depth fails on one ladder

The [inverse-history proof](templates/UNBOUNDED_EXPOSURE_DEPTH.md) excludes
every additional incoming source at depth D when
`N=96*64^(3^D*t-2)`, t>=1. The complete component has only the source
weights -2,+2,+2, hence mass2. The decisive inequality places every
off-chain inverse history above the entire annular source support.
It follows that the least sufficient depth on `N=96*64^k` is at least
`v_3(k+2)+1`. Two independent model audits found no gap.

The earlier [symbolic lift](templates/INFINITE_COMPONENT_FAMILY.md) is
retained: it checks 42487 affine inequalities and extends the original
depth32 witness over an infinite parameter family. The subsequent written
induction supplies arbitrary depth; that stronger quantifier does not
come from running larger scans.

### The compiler's automatic inputs preserve the unknown complement

The [local conversion](closure/LOCAL_EXTENSION.md) produces a one-sided
packet input using absorption only on `(N/4,N]`. Its negative residual
is exactly the low-quarter/outer-shell complement. Reversing this same
construction returns that complement unchanged. An independent exact
input does extend absorption to `3N/2`; a one-sided input gives an exact
unresolved-count budget. Actual examples include a sharp two-seed remainder
at N24 and a stored102-row outer certificate at N96.

**Pivot:** the raw highest packet atom is not an intrinsic input dependency,
because the explicit source-scale current removes it. The scoped positive
cone obstruction instead identifies the new seed inside a required inner
interval. Independent residual cancellation or graph connections remain
possible.

### Auxiliary normalization terminates but cannot finish with nonpositive current

The [backward rules](auxiliary/AUXILIARY_NORMAL_FORM.md) use exactly the
residue classes with a smaller ancestor within two steps. Their integer
height potential strictly decreases and the final flow is order independent.
For every annulus they place positive residuals below64N, using a
nonpositive current. Five exact floor counts leave at least21N/4 positive
mass on multiples of3, where no predecessor exists. Completing this
residual requires positive continuation current. This is a limitation of
that continuation; its positive rows may cancel the earlier negative rows.

### Review and integration of merged PR1

The user requested review of the parallel lane during this batch. The
checkout was fast-forwarded to merged commit `ba6b337`, with ongoing edits
preserved and reapplied. The [review](../../collatz_research_20261017/negative_controls/PR1_REVIEW.md)
retains the independent audit, negative controls, conditional minimality
lemma, and class-wise equivalence. It corrects the claims that there are
no alternative one-sided currents and that six traffic samples prove a
universal cost/descent requirement. For actual A768,56 different one-sided
certificates attain the same minimum positive cost53758; one removes row5.

The resulting pivot is specific: stop seeking a fixed-depth source cover
or treating early contraction as evidence of universal termination. Keep
the current framework and seek a recursion whose total depth can grow,
using arithmetic that excludes the permanent positive components in the
3x+61 controls. The remaining theorem must prove that this growth ends.

### Continuation validation

`python3 scripts/verify_all.py --cpp` passed on the integrated tree, including
the merged lane's five receipts, the review counterexamples, all four new
research checks, and the original archive/C++ checks. The first combined
run exposed a temporary-copy ordering issue in the new review stage; moving
it after its imported dependency copies fixed that issue. No mathematical
receipt changed as a result.

The existing LaTeX source compiled successfully. All83 checked local links
resolved, and the staged diff passed whitespace validation. Independent
reviews checked the new inverse-history proof, its main-note transcription,
the local conversion, and the auxiliary bounds. Git history records delivery;
the universal construction and termination goal remains open.

## Continuation from `2be37b7`: resolving selected positive clusters

This batch follows the first failure of the isolated-chain congruence,
retains graph arrows canceled by the scalar compiler, and uses signed
intermediate coefficients in the auxiliary rewrite.

### Working checklist

- [x] Read the clean repository, current invariants, and prior failure cases.
- [x] Find an actual negative attachment that resolves a positive cluster.
- [x] Derive a growing-depth arithmetic family and inspect every source sign.
- [x] Construct a partial extension from the retained input graph.
- [x] Extend the disjoint annular source catalogue with exact counts.
- [x] Audit the signed path collapse and the growing-depth family independently.
- [x] Integrate proofs, reproduce checks, and compile the existing source.
- [x] Review the integrated result and prepare the authorized Git delivery.

The candidate cancellation family is an exact identity for five actual source
atoms. A complete component is resolved in a finite example; a universal
statement about every full exposed component would be stronger and remains
open. The retained-graph extension is conditional on supplied inner absorption.
Neither construction closes its full residual.

### Result: selected arbitrarily long isolations have exact cancellations

The [release proof](release/DELAYED_RELEASE.md) constructs two negative
sources around the old mass2 chain. Its full five-source current is
nonpositive, has norm at most4h+10, and is supported in exposure at most
2h+1. The chain remains a complete positive component through h+1.
Qualifying h are unbounded, and each family occurs infinitely often on
the required ladder N=96*64^k. This supplies an explicit finite resolution
of the designated sources after a proved growing delay.

The refined inverse precision also strengthens the general ladder bound
to `d_*(96*64^k)>=v_3(k+2)+4`. Complete finite witnesses distinguish a
neutral first attachment, mass2→2, from a resolving one, mass2→0. The
general family is a five-source submeasure identity; other sources in a
larger exposed component remain to be accounted for.

The [new packing](release_packing/RELEASE_PACKING.md) separately adds
disjoint pairs and triples to the earlier source catalogue at every allowed
N. Total removed positive mass becomes1073N/432+O(1), with a full returned
current and residual. There is no assumed simultaneous packing with the
general delayed family.

### Result: retained arrows improve the conditional input

The [retained-graph theorem](complement/RETAINED_GRAPH_EXTENSION.md)
uses every K_N arrow below3N/2. Supplied inner absorption gives all lower
seeds and asymptotically47/72 of the outer shell. The improved packet
residual is a specific negative profile of mass25N/288+O(1), concentrated
at outer roots3 or7 modulo12. The proof classifies all K-only components
missing the known lower interval, including their possible second source.
Additional supplied-path intersections can help further; they are not
presumed in the arithmetic guarantee.

### Result: signed path capacity and the necessary frontier memory

The [path construction](alternating/ALTERNATING_PATHS.md) keeps each
intermediate coefficient in the restricted valuation1/valuation2 graph.
Backward ancestry terminates, yielding both a linear signed collapse and
a nonpositive-current normalizer. The latter's root residual is the exact
maximum initial prefix sum and improves the old shortcut normalization.

One-step forward/old-normalize iteration stabilizes but retains at least N
positive mass for every annulus. Explicit complete path components have a
known forbidden exit after growing depth, yet their new root heights can
grow without bound. Thus the next construction must retain the exposed
frontier and use additional cancellation or a different decreasing parameter.

### Validation and next obligation

`python3 scripts/verify_all.py --cpp` passed with all prior checks and four
new checkers. The new receipts cover69 delayed currents,36 refined complete
components, both first-attachment witnesses,129 extended-packing cutoffs,
131 entire cutoff graphs,36 mass phases,eight supplied-input conversions,
20 signed-path annuli,and11 growing-depth component examples.

The existing LaTeX source compiled successfully after an independent review
caught a missing `0<=i<m` restriction on the frontier-current formula.
It is now explicit, with zero current elsewhere. The release theorem,
precision refinement, packing capacity, and signed path arguments received
independent model reviews. All97 checked local Markdown links resolved.

**Next:** turn the delayed negative-source attachments into a capacity-safe
recursion for a complete specified residual family. Track the frontier and
every extra source that joins it. The retained input profile offers another
explicit target, but its smaller mass cannot be iterated without proving
closure. Neither successful examples nor the new partial identities prove
that every positive component eventually resolves.

### Independent side-lane review

The user added a start-of-batch feed instruction during final review.
Fetched and read `origin/claude/sidekick:sidekick/FEED.md` at
`f2af9452892887703cf5865b9ef4150faf6bafba`. The branch was not modified.
After inspecting the scripts, reproduced `sidekick/probes/depth_probe.py`
and `sidekick/probes/release_families_check.py` in a temporary snapshot of
that exact commit; both outputs matched their stored receipts. The
[review receipt](side_lane_review.json) records source hashes and outputs.

The independent packing check confirms the new pair/triple identities and
their mutual capacity, while expressly leaving the older-catalogue capacity
to the main proof. The forward-graph probe confirms five older isolation
examples. At their first reported resolving depth, all five components
contain1; four still have positive source mass. Those samples complement
the new exact cancellation family and do not establish that absorption is
the only way every such cluster can resolve. The side lane's larger-scale
questions remain untested leads. The fetch/read/verify rule is now in
AGENTS.md for subsequent batches.

## Continuation from `65093c4`: coverage and a descent interface

The user requested another assessment of Claude's merged PR. A fresh remote
read identifies PR1, merged at `ba6b337`, as the only merged PR; it is already
integrated in this checkout. Its valid negative controls and corrected
minimality statement stand. The concrete same-cost counterexample checker
was rerun successfully. No later merge was found in that remote read.

**Research decision:** retain the current framework, but prioritize an
explicit reduction of remaining seeds to an already absorbed interval.
Extra cancelled mass alone does not establish that the hard residual is
being covered. Bounded local catalogues can serve as preprocessing; a
complete construction still needs unbounded excursions and a termination
argument using arithmetic that the `3x+61` control lacks.

### Batch checklist

- [x] Refresh the remote, identify the merged PR, and read the side feed.
- [x] Reproduce the new delayed-release and depth16 backward-search receipts.
- [x] Resolve the all-phase `2h+1` coverage candidate with complete components.
- [x] Prove and check a transfer from partial annular currents to the outer residual.
- [x] Bound complete source clusters in the restricted path graph and audit exit scope.
- [x] Integrate the results, reproduce all checks, and compile the existing source.
- [x] Review the final diff and prepare the authorized Git delivery.

### Latest external evidence and its limits

Reviewed `claude/sidekick` at `f12da944dc68cfaff0884d874e11bc6c2cb98d34`.
After reading the new scripts and checking that their dependencies were
unchanged from the previously inspected snapshot, both new receipts were
reproduced in temporary storage. Replacing the backward search's floating
height bounds by exact integer bounds reproduced the same complete receipt.
The [review receipt](side_lane_review_20261017_2005.json) retains the source
hashes, parameters, and results; the external branch was not modified.

For h2 the depth16 scan finds sufficient negative capacity in every tested
representative of11 classes, in some representatives of34 classes, and in
none of the four representatives of441 classes (486 classes total). For h3
the corresponding counts are20,24,1414, with two representatives per class
(1458 total). These are finite representative counts, not uniform statements
over all members of a congruence class or asymptotic densities.

Two limitations matter for strategy. Lack of two negative units within
depth16 does not exclude a deeper zero-cost backward attachment. It also
does not imply that the whole inverse tree never re-enters the annulus:
it may contain a positive source or just one negative unit. No universal
positive-cost requirement is imported from those observations.

### R19: a precise failure of the all-phase short-delay candidate

The [phase proof](release_coverage/PHASE_COVERAGE.md) establishes complete
mass2 isolation at depth5 on17 of18 coarse unit phases with h2, and at
depth7 on53 of54 phases with h3, under its explicit binary and size
conditions. Each infinite phase is proved by a finite symbolic inverse
decision tree whose arithmetic branches survive an additive translation.
The exceptional phase really adds a source; its total component need not
be resolved.

On `N=96*64^k`, every `k=2 mod27` is an infinite required-ladder witness
with h2 and positive complete depth5 component. This refutes the proposed
all-phase bound2h+1 without restricting candidate valuation words. A
separate finite1944-representative scan supplies21 complete partial-current
tables, with actual source capacities and attachment positions checked.
Deeper or phase-sensitive constructions remain possible.

### R20: a noncircular interface from cancellation to outer descent

The [transfer theorem](complement_recursion/ANNULAR_COMPLEMENT_TRANSFER.md)
uses known absorption through N and an exact partial annular block at
M=N/64. Every positive atom of A_M has an explicit ancestor at most N.
Subtracting the block's current from the certified positive-source current
therefore certifies its negative sources. Their appropriate valuation1
predecessors are actual unresolved R_N roots.

This argument validates full multiplicity: after a path is established,
it can be multiplied by2 for a coefficient2 residual root. It does not
reuse the annular source capacity. Every uncovered coefficient remains in
the exact profile. The old packed-tree catalogue covers only
`N/9216+O(1)` roots, although the overall catalogue cancels much more
annular mass. The short release pair/triple adds no further R_N coverage.

The delayed family supplies exact first descents from genuine remaining
roots to N-1 in h+r+2 arrows. All intermediate states exceed N, and the
peak exceeds `(4/3)^h N`. These are constructive branches after unbounded
excursions, including required-ladder cases. The checker validates170
branches and a coefficient2 example, plus five actual current transfers.
A full61-row current for seed9183 is stored and upgrades the N6144 packet
residual by one unit.

### R21: finite local source processing, with an explicit closure failure

The [source-cluster theorem](window_components/WINDOW_COMPONENTS.md)
proves a sharp63-arrow span for all nonzero annular sources on one complete
E0 path. An adjusted height uses the empty source half-bands and allows
single-step dips. A fixed-radius guard now recovers every source and an
exact frontier current without walking to the potentially distant root
or exit. All current rows lie below192N, with a bound on partial positive
cost. The full positive frontier residual remains present.

This finite arithmetic template scheme is not closed under continuation.
The Mersenne examples exit into components containing no original annular
source at all, so the outgoing positive mass becomes an auxiliary source.
The quarter-height bound at a high-valuation exit compares with that exit's
origin, not with the last annular source. It supplies no missing global
decrease.

### Next proof obligation after the pivot

For every remaining R_N root, construct a finite path or exact current
whose positive dependencies are already absorbed, or give another finite
progress rule with a well-founded parameter. R20 specifies a concrete
input/output interface for this task. R19 requires more than the previous
short delay formula, and R21 requires handling components without original
sources. Additional successful local templates are useful only with an
explicit account of which unresolved roots they cover. Universal coverage
and termination remain open.

### Batch validation

`python3 scripts/verify_all.py --cpp` passed, including all three new
checkers and all prior archive, certificate, negative-control, and C++
checks. Independent model reviews passed the complete phase proof,
annular-to-complement transfer, and bounded source-cluster proof.
The existing LaTeX source compiled successfully after integration review
clarified the source-cluster cutoff domain and the convention root(1)=1.
The external review reproduced both pinned new side-lane receipts,
including a second scan with exact integer height bounds. No complete
universal certificate or Collatz proof is claimed.
All122 checked local Markdown links resolve, and the staged diff passes
whitespace validation. Git history records delivery of this batch.

## Continuation from `46198fb`: half-size bridges and a stronger depth obstruction

The user asked to continue deeply, then requested another assessment of
Claude's merged work. A fresh remote fetch and GitHub read identify PR1
(`ba6b337`) as the only merged PR; main already includes it and the prior
scope corrections. The optional side branch has advanced independently.
The batch started from feed `f12da944` and reviewed its newer state at
`9a0c28d` before integration. No external branch was modified.

### Batch checklist

- [x] Refresh remote state and distinguish the merged PR from later feed work.
- [x] Prove or refute a depth bound depending only on the initial ternary order.
- [x] Construct a full shrinking family with exact residual coverage.
- [x] Audit the literature interface, sparse induction, and source reuse.
- [x] Integrate the proofs and compile the existing LaTeX source.
- [x] Complete the unified finite checks and final independent review.
- [x] Inspect the final staged changes for the authorized Git delivery.

### R22: the one-parameter depth programme fails

The [fixed-h proof](phase_depth/FIXED_H_DEPTH.md) supplies complete
positive components at every prescribed depth while h remains exactly2.
The binary precision and congruence `X=10 mod3^(D+2)` exclude all incoming
source histories, using a bounded22-case arithmetic barrier. Infinite
required-ladder realizations follow by lifting powers of2 modulo powers
of3. Thus every candidate exposure bound f(h) alone fails.

This is a stronger strategic restriction than failure of2h+1. A successful
constructor needs additional arithmetic state or a different mechanism.
It is not a permanent obstruction at any fixed integer: X varies with D.
The auxiliary3x-1 cycles exclude hypothetical small shadows; actual
first-integral offsets reach1 under that map.

### R23: a complete shrinking family, rather than another isolated template

For `x=2^a*t-1`, the condition `t=3^a mod4` gives
`S^a(x)=S^a((x-1)/2)`. The
[halving construction](residual_return/SHRINKING_COALESCENCE.md) provides
the exact finite bridge and preserves all residual multiplicities.
It uses supplied absorption below N, with no larger absorption assumption.
The first climb may have arbitrarily many steps and unbounded height
relative to N. The proof specifies the bridge before any future search.

The selected classes remove `25N/576+O(log N)` weighted units. The exact
remaining profile has the same leading mass, with the opposite binary
condition. At N6144 the construction certifies263 of532 units. It
subsumes the old packed-tree root class, while applying to complete
binary classes and both coefficient1 and coefficient2 roots. The stored
root79 example keeps both units throughout its current.

On the complementary branch, the exact relation is
`S^a(x)=3*2^(d-1)*w+1`, where `w=S^(a-1)((x-1)/2)` and d>=2.
Knowing the smaller partner terminates does not establish a connection
from this larger state. The simple equal-step extension already fails
at x27. Repeating a numerical half-mass reduction has no justification.

### R24: the precise completion would support induction

The [sufficient-set audit](sufficient_sets/SUFFICIENT_SETS_AUDIT.md)
distinguishes qualitative arithmetic-progression mergers from the needed
finite certified inputs. The primary sources reviewed do not supply the
missing height-controlled witness. The halving identity uses precedented
common-tail arithmetic; no novelty claim is made.

The union of all five dyadic rays has consecutive ratio at most7/6.
Starting at6144, every cutoff is divisible by512, so both the direct
bridge interface and R20's annular transfer are available. If every
complementary root can be certified from U_N at each cutoff, extension
to3N/2 supplies the next U input. This is a genuine conditional induction,
not a circular appeal to larger absorbed seeds. A draft confusion between
one factor64 ladder and the interleaved union was caught and corrected
during review.

Source reuse also has a useful distinction: two independent proofs may
use the same already absorbed seed. Combining blocks into a single
submeasure of A_M needs joint capacity bounds. Each block still needs
valid signs, coefficients, and divergence. This avoids imposing an
unnecessary packing constraint on independent root certificates.

### Direction after the independent input

Keep the exact current formulation and Claude's negative controls.
Stop treating cancellation totals, a short fixed catalogue, or the old
ternary parameter as a proposed universal progress measure. The next
positive target is the explicit complementary profile from R23, with
every proposed rule judged by a finite bridge to an already certified
input or a proved decrease on every branch. The
[latest feed review](side_lane_review_20261017_latest.md) retains the
finite stopping-cylinder checks and their limits; measured density decay
does not establish universal closure or a rate for growing bit depth.

### Batch validation

`python3 scripts/verify_all.py --cpp` passed, including both new checkers,
all prior stored evidence, the merged negative controls and review
counterexamples, and both independent C++ cutoffs. The two focused checks
also passed separately. Independent model audits passed the fixed-h proof,
halving construction, count, and sparse induction. The existing LaTeX
source compiled successfully in place. All152 checked local Markdown
links across25 programme files resolve. No universal completion is claimed.
The staged file list and diff were reviewed; whitespace validation passed.
Git history records the authorized commit and push of this batch.

## 2026-10-17: exact quotient, normalized run bridges, and infinite known targets

This batch started from main8e2b5eb and reviewed the optional side feed at
491d26d766971bdf7fdce9bba288540423fd58c8. A further remote refresh in
response to the user's question still identifies PR1 as the only merged PR.
Its negative controls and corrected minimality scope remain incorporated.
The newer findings are on the separate side branch, which was left unchanged.

### Batch checklist

- [x] Classify the full graph generated by sibling and halving identities.
- [x] Derive an exact complementary run map and normalize every return.
- [x] Prove exact weighted coverage and retain the remaining counterfamilies.
- [x] Construct and count an infinite known set at arbitrary heights.
- [x] Reproduce the new feed receipts and prove the precise prefix-rate claim.
- [x] Obtain independent model audits of all four proof/code components.
- [x] Integrate the README, ledger, agent rules and existing LaTeX source.
- [x] Finish the unified verification and final delivery review.

### R25: the elementary identities form a genuine quotient

The [complete normal form](bridge_normal_form/BRIDGE_NORMAL_FORM.md)
shows that each elementary component has exactly two F-rays, based at q
and2q+1, with q its canonical minimum. It includes arbitrary inverse uses
of the identities; these cannot lower a remaining canonical R23 root.
The canonical state space is dynamically consistent: `T nu=nu S`.
Every quotient arrow has a finite lifted current, and all inverse
branches have explicit formulas. Termination is still equivalent to
Collatz. The parametric failure of greedy inverse minimization means a
future inverse search must retain more than its smallest immediate branch.

### R26: complete run formulas give a further conditional extension

The [complementary construction](complementary_bridge/RUN_BLOCK_BRIDGES.md)
handles both parities of d after the initial climb and full valuation2
run. Applying the full normal form before comparing to N is essential:
at N168, root187 of weight2 returns to211, then canonically to105.
The stored current keeps both units. At N6144 the new rule removes146
of269 complementary units, leaving123.

The exact normalized count has a proved uniform O(log^4 N) error,
including the growing odd moduli and affine offsets. Its leading removed
mass is0.02399251818395744N, about55.2788% of the previous residual.
Together with earlier rules this covers about92.24% of the next shell
conditionally on U_N. This is one pass and is not a termination argument.
The family a=7 mod16,t=1 returns to an already canonical state at
unbounded relative height. The two transitions27→31→91 defeat a rank
depending only on(a,d), including a lexicographic label-rank/height rule.

### R27: a finite input supplies infinitely many high targets

The [known-set proof](absorbed_fibers/ABSORBED_FIBERS.md) constructs
an exact finite certificate for every x with nu(x)<=N from supplied U_N.
Its exact band counts telescope, giving
`|#(I_N intersect[X,2X))−N/4|<=2 floor(log2 N)+3`
uniformly for integer X>=N>=8. This strengthens an initial O(log^2 N)
estimate. Bridge row count is O(log N), independently of target height.

This is a substantive correction to using the finite forward-orbit union
as the entire set of available targets. It gives actual arithmetic
membership and certified states at every scale. It does not turn spatial
density into a hitting probability or show that all remaining roots meet
the known set.

### R28: the proposed barrier is valid for its specified prefix rules

The [rate proof and external audit](cylinder_barrier/CYLINDER_RATES.md)
reproduces both newly pinned receipts and proves the exact exponential
rates for the specified D/M/H symbolic slope recognizers. Compositions
and cyclic rotation give elementary lower bounds, including a fixed
escape cylinder; exponential moments give the upper bounds. The odd-step
and bit clocks have different factors,0.9465045768 and0.9659065532.

The external H dynamic program overlooks a partially known closing
valuation already at least3. Its counts remain valid for the stricter
exact-closing rule; the corrected recognizer covers more at finite depth.
The asymptotic rate is unchanged for the stated rules. This does not
prove constant-factor equivalence or finite-integer counts when depth
grows with N. The excursion experiment also concerns a finite target
set; R27 supplies a larger infinite set with a different proved density.
High common-state halving bridges already occur before any descent.

### Decision and next proof obligation

Keep the exact-current framework and Claude's negative controls. Focus
on the residual left by the normalized run rule, using the quotient's
full inverse structure and the enlarged known set. The next useful
result must prove that every remaining branch reaches an already
certified input, or provide a well-founded parameter with sufficient
arithmetic information. More density improvement by itself will not
close the induction. The present batch establishes progress, not a
universal completion or a novelty claim.

### Batch validation

`python3 scripts/verify_all.py --cpp` passed, reproducing all four new
receipts, every earlier repository check and both independent C++ cutoffs.
The existing LaTeX source compiled successfully after the final
transcription clarifications. All162 checked local links across the ten
integration and new proof Markdown files resolve. New source/data files
use LF endings. Independent model audits passed the proofs, current
conversion, count formulas and integrated mathematical statements.
Whitespace and final file-scope reviews passed. Git history records the
authorized commit and push of this batch.

## Batch after541101a: shrinking pairs, saturation and bounded-run obstruction

Previous goal turn: **progress**. Its four results and checks were committed
and pushed as541101a. This batch started from a clean tree and fetched the
optional side feed atceb94fc372533e6fdc196595a817e8c01bc62d51.

Working hypotheses:

1. Closing all supplied paths under the elementary identities may supply a
   useful finite certificate core beyond the cutoff-only target test.
2. The unresolved return family may admit richer arithmetic progress;
   bounded run lengths alone might still permit arbitrarily long growth.
3. The latest merger/sign heuristic may overstate what the sampled sets
   and future peak heights imply.

Checklist:

- [x] Read current state and pin the optional feed.
- [x] Prove and implement the exact saturation of supplied known paths.
- [x] Test the growing return family against actual known partner history.
- [x] Prove or refute long growth with bounded run labels.
- [x] Independently audit new external claims and preserve scope corrections.
- [x] Integrate durable results, run required checks and compile.

### Findings and decision

| Hypothesis | Outcome | Evidence |
|---|---|---|
| Complete supplied history has a finite useful representation | Proved exactly for elementary identities plus forward arrows | [R29 proof and compiler](known_saturation/KNOWN_SATURATION.md) |
| Growing normalized returns may still have decreasing paired arithmetic | Proved on complete infinite subfamilies, at every recursive depth | [R30 shrinking pairs](second_return/SHRINKING_PAIRS.md) |
| Bounded run lengths might restore a finite-label height rank | Refuted for all finite-label potentials nondecreasing in height | [R31 repeated words](bounded_run_cycles/BOUNDED_RUN_GROWTH.md) |
| High future peaks force cancellation while high | Refuted by an infinite capacity-checked actual annular family | [R32 scope audit](merger_scope/MERGER_SCOPE.md) |

**R29: finite representation of all supplied history.** The exact closure
is E_N=nu^(-1)(Q_N), where Q_N normalizes the supplied forward paths.
The ordinary core W_Q={S(q),3q+2:q in Q} is forward closed and has exactly
2|Q| states. Every member of the infinite closure enters it in one arrow.
Minimum-origin labels preserve the smallest canonical starting seed for
each target, and exact high-band counts work for arbitrary finite Q.
At N384 the stored weight2 certificate for415 uses the known state1579,
above the cutoff. However415 itself was already S^4(327); all sampled
extra R26 successes were already in the supplied closure. This is useful
history reuse, not evidence for a new universal merger. The cutoff-only
fibres and finite forward union are generally incomparable; E_N contains
both. This clarifies earlier uses of the word "larger".

**R30: the constructive advance.** For w=3 modulo8, even
h=v2(3w-1)=2k+2 gives paired endpoints4z+1 and2z+1,
z=3^k(3w-1)/2^h. Canonical z terminates. The class z101 modulo128
reduces to w'=(3z+1)/16<w/4, with the child current subtracted.
This gives a terminating partial recognizer. Exact infinite cylinders
realize arbitrarily many recursive transitions followed by a terminal
branch. Lifting them to w=(3^(a-1)-1)/8 yields actual required-ray
roots2^a-1 and same-clock mergers with2^(a-1)-1 below N.
The first exponent classes are199 modulo256 and2887 modulo65536.
A separate39 modulo2^20 class has a stored191-row absorption current
for549755813887 from the supplied path of274877906943. All bridge
construction uses prescribed finite prefixes; only the finite input
demonstration discovers a known lower-seed path under a stated cap.
The old normalized return grows without bound along each accepted class.

**R31: a stronger failed progress candidate.** The repeated word
(1,2,1,1,1,1,2,2) has paired map(6561x+9221)/2048 and yields arbitrary
numbers of growing returns using only(2,2),(5,4). Exact binary cylinders
and CRT place these seeds in actual required-ray residuals. They remain
above N and outside the cutoff-only known set for the prescribed duration.
Repeating a finite label at a larger height contradicts any potential
that strictly decreases every return but is nondecreasing in height
within each label. The seed varies with the requested duration;
no divergent positive integer is produced. Pair recursion uses different
arithmetic information and remains compatible with this obstruction.

**R32: external findings retained at their valid scope.** The pinned R24
receipt was reproduced and all ten peak/sign cells rebuilt exactly.
S(x)<=3nu(x)+2 gives an actual fixed-lookahead bound. A precisely defined
normalized slope test, with all bits charged, retains R28's two rates;
this does not bound arbitrary common-tail constructions. Actual positive
and negative annular sources can cancel at a successor below both before
a shared climb of arbitrarily large relative height. Allowing arbitrary
common tails gives exactly the basin of1, leaving construction as the
open issue. The later feed read at d2d85e1e49f0018a648c6daadc4fc93290c0d107
withdraws the universal merger claim. Its newer R26/R27 checks and
quotient probe were read, not rerun in this batch. Their T-step clock
must remain distinct from R26's variable-length return clock.

### Pivot and remaining obligation

The remote read still shows only merged PR1, already incorporated. Keep
its negative controls and the exact-current framework. Focus the next
constructive batch on the odd-h and unhandled z branches of R30, retaining
known smaller-seed history and every sign. Accepted recursive branches
decrease; completeness of the branch system is the missing theorem.
No improved global coverage fraction follows from the current examples.
R29 supplies the exact target compiler, and the full inverse structure
remains available for additional arithmetic comparisons. A possible next
lead is inverse valuation1 ancestry for canonical q=2 modulo3; it requires
its own complete proof and coverage accounting before use.

### Validation

All four focused checkers passed. Independent model proof/code audits
passed all four results and the new paired merger clocks. Integration
review clarified the supplied-history membership, conditional height
bound and integer band endpoints. The existing LaTeX source compiled
successfully after those corrections.

`python3 scripts/verify_all.py --cpp` passed, including all four new
checkers, every prior repository check, the31 archive manifest entries,
and independent C++ verification at both stored cutoffs. All191 checked
local links across ten integration/proof Markdown files resolve. New
files use LF endings and whitespace review passed. Git history records
the authorized commit and push of this batch. The research goal remains
active: this batch is progress, and universal convergence is still open.

## Current batch after64fff1d: mixed pairs, inverse ancestry and missing domains

Previous goal turn: **progress**. R29–R32 and all checks were committed
and pushed as64fff1d. This batch begins from a clean tree. The optional
feed was fetched and read atd2d85e1e49f0018a648c6daadc4fc93290c0d107,
unchanged from the last read; its text remains optional external evidence.

Working hypotheses:

1. R30 odd-h and other even branches admit exact smaller-parameter pair
   recursions that can be composed without losing signs or clocks.
2. Complete decreasing inverse ancestry supplies a uniform arithmetic
   extension of the cutoff-only return test on actual residual families.
3. General complementary roots reduce to a finite collection of pair
   types; identifying their full domains may reveal what universal closure
   would actually require.

Checklist:

- [x] Revalidate the clean committed state and read the optional feed.
- [x] Derive and test additional shrinking pair branches and complete mixed words.
- [x] Prove the full decreasing inverse-ancestry rule and actual weighted coverage.
- [x] Derive the general half-seed pair interface and audit its static scope.
- [x] Construct two dynamic entries from the missing1-modulo8 pair domain.
- [x] Independently review proofs, constructors and count formulas; persist evidence.
- [x] Run the full `python3 scripts/verify_all.py --cpp` gate.
- [x] Compile the integrated LaTeX source and verify local links and references.
- [x] Prepare the verified batch for staged review and authorized Git delivery.

### Outcomes and proof limits

| Direction | Outcome | Durable evidence |
|---|---|---|
| Extend the paired recursion beyond R30's even branch | Three shrinking branches compose for every finite mixed word | [R33 mixed rules](paired_completion/MIXED_SHRINKING_RULES.md) |
| Recognize useful lower ancestors of normalized returns | Complete local inverse formula and complete families with unbounded old return height | [R34 inverse ancestry](inverse_ancestry/INVERSE_ANCESTRY.md) |
| Reduce every complementary root to pair comparisons | Exact two-type decomposition; a restricted static catalogue remains incomplete | [R35 pair scope](pair_scope/PAIR_SCOPE.md) |
| Escape the missing1-modulo8 pair domain | Two dynamic entries into the mixed recursion, including new smaller-half mergers | [R36 missing-domain construction](pair_one/MISSING_PAIR_DOMAIN.md) |

**R33: arbitrary finite mixtures of shrinking pair rules.** For P(w)=delta_(3w)-delta_w,
w=3 modulo8, the new odd-h branch O adds its smaller child current. The new
even branch E1 and retained E2 branch subtract theirs. Every child is less
than w/2; E2 retains the stronger w/4 bound. Exact backward affine lifting
gives a complete nonempty binary cylinder for any finite branch word followed
by a terminal class, including all required valuation bits. The merger clock
adds k+1 for O and k+2 for E1/E2. Every such cylinder lifts to actual
Mersenne residual roots with a supplied smaller-half partner.

The conditional binary-cylinder measure accepted by this particular
recognizer is exactly32/157. This follows from its exact uniform child maps,
not a model of orbit independence. It is neither a weighted R_N fraction
nor a repeatable residual contraction. At a631 the new bridge's source and
old return are absent from the elementary-plus-forward closure of the
supplied single lower-seed path; the full U_N history was not constructed.
Parent or child failures remain unresolved.

**R34: full decreasing inverse ancestry with actual coverage.** For canonical
q, h=v3(q+1) and eta(q)=2^h(q+1)/3^h-1 describe every strictly decreasing
canonical inverse edge. They give a nonpositive bridge to the unique local
minimum, not to a global ancestor minimum. Applying this to R26's canonical
return recognizes supplied forward history through an explicit lower seed.
The recognized target q lies in R29's known closure; the originating x still
uses its separate R26 bridge and need not already lie there.

The cylinder x19199 modulo65536 certifies the new root84735 at N65536,
using p45243 below the cutoff although the old return67865 exceeds it.
For every inverse depth h>=2, another complete cylinder has p<(2/3)x
and old return q>x, with q/x unbounded across the families. Every actual
R_N source in it therefore has p<N. Its exact
weighted count has leading term25N/(72*2^K) and error at most6 for each
fixed family. Both source weights occur on required rays; a full171-row
weight2 certificate is stored. The whole extended rule also has an exact
finite CRT count. It leaves every even-d return unchanged, and no leading
coefficient for its full residual or uniform density for the family union
is claimed.

**R35: the missing comparison is explicit.** Every complementary root's
smaller-half path reaches w after its prescribed first run. The remaining
source is delta_f-delta_w, a finite sum of tripling pairs and, for even d,
one doubling pair. The helper parameters can exceed the original source
without bound. Universal doubling-pair currents are themselves equivalent
to Collatz by strong induction, so the two formal types do not supply a
decreasing universal construction.

Even granting every tripling pair in the3-modulo8 domain, the static graph
of those pairs plus elementary identities has an exact decreasing component
label. It leaves an infinite actual a3-modulo16 Mersenne family unresolved
after its first run. This is an operation-set obstruction only; arbitrary
ordinary arrows and other proof methods are outside it.

**R36: dynamic bridges cross that static boundary.** The complete domains
w17 modulo128 and w105 modulo256 reduce to smaller3-modulo8 children,
adding the child current in both cases. Their clock increments are1 and2.
Every complete mixed child cylinder has a branch A parent; branch B
requires the child origin to be11 modulo16. In the
a3-modulo16 Mersenne family, the classes a1699 and a659 modulo4096 now
merge with their smaller halves at times a+4 and a+5 respectively, despite
unbounded old return heights. These are consistent with R35 because they
use additional ordinary arrows. The a659 supplied-input conversion has3200
rows; the small stored current for315 has11. The example a147 still returns
an unresolved child, so the new entries do not complete that missing domain.

### Verification and external state

All four focused checkers and independent model proof/code audits passed.
The full `python3 scripts/verify_all.py --cpp` gate also passed, including
the four new checkers and all previous repository checks. The new checks
include4096 mixed-pair inputs and510 mixed cylinders;4096 inverse targets,
2048 return branches and eight exact full-profile counts; the complete
bounded static pair graph and integrality-preserving parameter cases; and
4096 missing-domain inputs,213 complete cylinders and71 exponent lifts.
Current conversions retain all source weights and supplied-input boundaries.

The full gate passed again after adding the external reproduction record.
The existing LaTeX source compiled successfully in the desktop editor.
All218 local Markdown links across ten integration and proof files resolve;
the TeX has no undefined references or duplicate labels. All29 changed or
new files use LF endings. Independent review of the integrated mathematics
passed, including the explicit inverse-profile cutoff domain. Final staged
review and authorized delivery are recorded by the accompanying Git history.
The optional feed pin at batch start was unchanged
`d2d85e1e49f0018a648c6daadc4fc93290c0d107` and was read only. A subsequent
remote check after the user's PR report found origin/main still at64fff1d
and only merged PR1, atba6b337, already an ancestor. The newer side-feed
read at `e3111d3b74e410cd300b01b842c57bbc5e32d058` reports checks of R30–R32
and accepts R32's scope correction. Its new source and both pinned dependencies
were inspected and reproduced unmodified in temporary storage; the published
receipt matches exactly. The [hashed reproduction record](side_lane_review_e3111d3.json)
also records independent checks of the sharper main clocks.
Its recursion index is shifted by one: the reported checks for
199/455 use clock a+6 where the main prescribed clock is a+3, and2887
uses a+9 instead of a+6. Equality at those later times is compatible with
the earlier mergers; it is a weaker clock check, not a contradiction.

### Decision and next obligation

Extend the exact pair rules to their remaining domains, with a decreasing
parameter or another finite progress argument on every accepted rewrite.
Keep ordinary arrows available when a static identity component is exhausted.
The general half-seed decomposition specifies which signed comparisons still
need currents, but neither its finite number of formal types nor binary
coverage measures supplies those currents. Inverse ancestry can recognize
additional known targets while leaving the even-d obstruction explicit.

The required next theorem is universal coverage of a sufficient complementary
root family from already supplied smaller inputs, preserving signs, source
weights and clocks. All present recognizers can terminate unresolved. This
batch is constructive progress; it does not complete that theorem or prove
Collatz, and no novelty claim is made.

## Active batch after1603bf3: complete pair domains

Previous goal turn: **progress**, committed and pushed as1603bf3 with the
full verification gate and integrated proof review passing. This batch starts
from a clean tree. The independent feed was refreshed and read at
dbb0dea5930ec667b70b5dfcbb595e5d566451b0. New entries report checks of
R33–R36 and failed tripling mergers on the control maps; these are external
inputs to verify before use. The side branch remains unchanged.

Working hypotheses:

1. The entire odd-parity residual pair admits a closed reduction, with a
   genuine decrease on a whole missing arithmetic domain.
2. Even-d comparisons admit an additional state or paired invariant that
   avoids R34's complete lack of improvement on that branch.
3. Universal tripling relations have a precise sufficient-set scope;
   classifying it will expose which auxiliary obligations are circular.

Checklist:

- [x] Revalidate the committed state and skim the refreshed independent feed.
- [x] Derive complete odd-parity and even-return interfaces; retain failures.
- [x] Determine the logical and constructive scope of universal tripling.
- [x] Verify new external control evidence before relying on it.
- [x] Independently audit any new proofs and executable constructions.
- [x] Persist results, update standing, run the required gate and compile.
- [x] Review and package the verified batch for the authorized commit/push recorded by the accompanying Git history.

### Results and hypothesis outcomes

**R37: exact critical domain.** The map w->nu(3w) bijects
W={5 mod8} union {9 mod16} onto complementary canonical q not2 modulo3.
Its inverse is smaller than q. The other canonical branches already descend
by a forward arrow or a smaller exact predecessor. Thus universal finite
tripling currents on W are equivalent to Collatz. A separate formal graph
using all elementary and hypothetical tripling edges has a decreasing
normalizer, with logarithmically many pair requests. The executable compiler
retains these requests and rejects missing or incorrect inputs. Neither
the logical equivalence nor the formal plan constructs the missing currents.

**R38: complete odd-h interface.** For Q(z)=delta_(6z+1)-delta_z,
an elementary bridge reduces to P(u), where u=z if3z is canonical and
u=4z+1 otherwise. Consequently every odd-h run has one exact child source.
All h>=7 children are below7w/8, including the intercept; direct low-h
children also shrink. Nondirect h3 and h5 children expand, with complete
infinite examples. The parent clock retains a maximum with the selected
partner length. This settles the high odd-h arithmetic interface but leaves
the child currents in W open.

The entire R35 static catalogue connects Q endpoints exactly in3 modulo8.
The other Q indices biject to the same critical roots as R37. An exact
finite input set compiles supplied exact or one-sided Q currents into U_M;
the M128 demonstration stores all11 inputs and the112-row output current.
Actual odd-h indices have ternary unit1, with an exact restricted critical
image. The opposite phases cannot be assumed supplied. A repeated-word CRT
family stays in these omitted phases for arbitrarily many growing returns,
on actual weight2 required-ray sources. This excludes only the named bounded
descending phase tests, not full known-history closure or unrestricted
logical sufficiency of the restricted inputs.

**R39: keeping an even pair together.** The split d4 catalogue is fully
classified: it succeeds exactly on B inputs whose mixed child is accepted.
Simultaneous R33 acceptance of P(v) and P(6v+1) is impossible by infinite
descent on the same paired condition. Keeping C(v)=delta_(18v+3)-delta_v
instead supplies a valid smaller child t=(3v-1)/8, including7 modulo8.
The full terminal v39 modulo8192 and its inverse cylinders give arbitrary
recursive depth, with exact signs and clocks. This adds A-family d4
half-seed comparisons which the split catalogue rejects.

The original equal clocks are a+ell+2, initially a+5 for B and a+r+7
for A depth r. Every a>=2 has complete integral original-source cylinders;
their old return ratios grow without bound with a. Each fixed period-L
cylinder has exact full-weight count25N/(72L) with error at most6 for8|N.
Both source weights occur on the required rays, and two full weight2
conversion currents are stored. All A inputs, all d4, and all even d
are still open; no global union density or repeated contraction is claimed.

### External review and checks

The two new pinned side-lane probes and their dependencies were inspected
and reproduced unmodified in temporary storage. Both receipts matched.
Four independently reconstructed control paths/cycles have nonzero invariant
pairings, ruling out the stated control tripling currents. The saved witness
checker is part of the full gate. The larger random sample counts mentioned
in the feed were not reproduced, and the d>1 absorbing convention is explicit.
See [the review](PAIR_DOMAIN_REVIEW.md) and its hashed receipt.

A fresh remote read responding to the user's PR question still found only
merged PR1, already an ancestor, main=origin/main=1603bf3 and the unchanged
side-feed pin. The recommendation is a focused pivot toward the complete
critical domain and joint comparisons. The merged audit does not justify
abandoning exact current constructions.

All three new focused default checkers and the saved external-cycle checker
passed. Independent model proof/code reviews passed R37, R38 and R39,
including clocks, signs, full input sets, scope restrictions and source weights.
The existing LaTeX source compiled successfully in the desktop editor.
The full `python3 scripts/verify_all.py --cpp` gate passed, including all
new checkers, every previous certificate/control check, all31 archive
manifest entries, and both independent C++ cutoffs. Final independent
review of the integrated README, agent rules, ledger and TeX passed.
All218 local Markdown links across the26 changed/new files resolve;
LF endings and TeX references pass. The staged whitespace and scope review
passed. The accompanying Git history records the authorized delivery.
The goal remains active; this batch is classified as progress.

### Decision and next obligation

This batch is constructive progress plus an exact scope reduction. The next
target is a complete rule on a remaining part of W, with no hidden universal
pair assumption. The h3/5 expansion formulas and noncanonical even-return
helpers identify where a new state or multi-step progress argument is needed.
The coupled source is a concrete example of gaining a valid reduction by
retaining cancellation between unresolved helpers.

Do not replace this target with a larger finite scan or another isolated
merger family. R38's restricted ternary domain is smaller than its finite
compiler's universal input set, and R39 does not exhaust W. Universal
completion remains open; no Collatz proof or novelty claim is made.

## Batch after436f51f: complete critical-nine elimination and exact remaining dependencies

Previous goal turn: **progress**, committed and pushed as436f51f. The
working tree and main/origin-main agreement were rechecked. The optional
side feed initially remained at dbb0dea5930ec667b70b5dfcbb595e5d566451b0.
A later fetch advanced it to1a2dfc5710c5e17a4f42355a3dce2d6984b2b09b.
The new R37–R39 probe and its two dependencies were inspected and reproduced
unmodified in temporary storage under a60-second cap. The published receipt
matched. No side-branch mutation was made. A fresh remote PR listing again
found only merged PR1, already an ancestor of main.

### Hypotheses and outcomes

1. **Full W9 closure: proved as a domain elimination.** Every W9 request
   reduces to a finite signed collection of W5 inputs, bounded by(9w+3)/4.
   Every recursive W9 child strictly decreases. The complete low-even
   exceptions request a larger W5 input, so a claim that the entire pair
   parameter always decreases would be false. The W5-only equivalence
   is the constructive progress in R40; it leaves universal input supply open.
2. **Full W5 descent: partial, with an exact failed composition.** R41
   gives a complete shrinking rule on E_good, defined in its proof note.
   Universal currents on W5 minus E_good suffice. The other eligible row
   returns P(w) with coefficient+1; P21 is an exact tautology. The infinite
   w21 modulo2304 family preserves this defect. These are recipe loops,
   not positive Collatz cycles. The failure is recorded rather than iterated
   as if smaller intermediate parameters established a global rank.
3. **Joint-state closure: the simple proposal fails.** R42 covers the
   full two-arrow C interface and the whole missing v3 modulo32 block.
   Consuming the binary exponent increases the ternary coefficient. An
   actual required-ray family has an absorbed smaller half but a retained
   positive frontier with unbounded ratio to the original root. A separate
   R41 theorem exhausts all inverse rays and rules out fixed-depth ancestor
   descent, including complete elementary normalization, as a general repair.

### Durable evidence

- [R40 proof and compiler](w9_closure/CRITICAL_NINE_ELIMINATION.md):4096
  local cases,4096 sharper endpoint bounds,616 exact high-valuation cases,
  2688 direct affine-table cases,256 recursive eliminations,10 actual input
  substitutions and four rejection cases. P1561 has an explicit nine-row
  current with no missing premises; this is a finite example.
- [R41 proof and compiler](critical_inverse/CRITICAL_INVERSE.md):1820
  phase currents,1024 W5 absorption plans,683 E plans (455 descending and
  228 self-dependent),24 actual pair compilations,73 inverse-affine samples,
  2478 finite inverse words,27 CRT samples throughdepth128 and six independent
  all-origin checks throughdepth6. The exact whole-tree claim rests on its
  shadow proof, not these bounded tests. P69/P117 tables are in the receipt.
- [R42 proof and interface](joint_frontier/JOINT_FRONTIER.md):8192 complete
  interface cases,2048 full subdomain blocks,45 parameter pairs,11 expansion
  instances,five d4 embeddings and four actual required-ray roots. The
  stored r27 comparison has119 rows and a four-row lower input; its positive
  frontier is explicit and remains unresolved by this block.
- [External reproduction](side_lane_review_1a2dfc5.json) retains source
  hashes and the matched receipt:16668 critical roots/images,100000 odd
  interfaces and6250 joint inputs. Three additional W5 control witnesses
  were independently reconstructed and included in the exact cycle checker.
  The updated [parallel-work assessment](PAIR_DOMAIN_REVIEW.md) answers the
  user's pivot question and preserves the earlier PR scope corrections.
- [External sieve audit](sufficient_sets/RECURSIVE_SIEVE_AUDIT.md) records
  the exact witness11 to a displayed set equality in Ansari's Lemma3.1.
  The primary PDF transcription was independently checked. This identifies
  a proof gap; the paper's theorem is not claimed false or used as a premise.

### Review and validation

Independent model reviews checked R40's signed recursion and bounds, R41's
whole phase and complete inverse theorem, and R42's full frontier and actual
source embedding. A review caught a transcription error in R40's d8 table:
its intercept is55, not175. The note and shared summaries were corrected,
and2688 direct affine-row checks were added. The constructor already used
the correct formula4z+1. Stored CSV files use LF endings. Default focused
replays pass. The existing LaTeX source compiled successfully in the desktop
editor. The full `python3 scripts/verify_all.py --cpp` gate passed, including all
new and previous checks, all31 original manifest entries and both independent
C++ cutoffs. The final integrated-document model review passed after
clarifying that the ternary unit belongs to z and bounding the ordinary
predecessor statement explicitly. Local links, LF endings, TeX references
and whitespace/scope review passed. The accompanying Git history records
the authorized delivery.

### Decision and next obligation

This batch meets the complete-subdomain progress test: W9 is no longer an
independent universal premise, and E_good has a complete smaller-W5 rule.
The remaining sufficient set is B5=W5 minus E_good. Resolve a complete
part of B5, or prove a rank for a recursion that permits intermediate
increases without returning an unresolved input unchanged. A useful test
case is the entire returning E row, not only P21 or one more successful
merger. Any proposed general argument must respect the W5 control cycles.

Do not repeat the inverse/W9 composition on its returning row, infer
progress from the shrinking lower joint parameter, or replace a missing
current by a conditional formal plan. R41 excludes only fixed inverse
preprocessing; additional forward moves, unbounded inverse depth, signed
common-tail currents and supplied-history reuse remain available. No global
residual fraction, novelty claim or Collatz proof follows. The goal remains
active; the batch is classified as **progress**.

Checklist:

- [x] Revalidate the committed state and skim the independent feed.
- [x] Derive complete critical-domain interfaces and retain scoped failures.
- [x] Test combined-source closure and valid inverse reductions.
- [x] Independently review the new proofs and executable constructions.
- [x] Persist the changed understanding and exact evidence; update standing.
- [x] Complete the full verification and final integrated-document review.
- [x] Review and deliver the verified batch under existing authorization.

## Batch after4a45eb0: common rank and further complete domains

The previous goal turn was **progress**: R40–R42, proofs, code and evidence
were committed and pushed as4a45eb0 after the full Python/C++ gate and
LaTeX compiler passed. Revalidated clean main=origin/main. The independent
feed was fetched and skimmed at unchanged1a2dfc5710c5e17a4f42355a3dce2d6984b2b09b;
no new finding or branch mutation occurred at that initial read. A later
user-requested remote refresh found the same already merged PR1 and new
feed8c3f96f9b3da3df68ba49bfe2a5dfdd64e04abf1. Its additional finite checks
were read, not reproduced or used as premises in this batch.

Working hypotheses:

1. An additional forward comparison breaks the entire returning E dependency,
   or a complete further subdomain, without a hidden same-or-larger W5 input.
2. The full W5 source has a paired valuation interface with a useful closed
   affine state and a rank beyond the original input height.
3. The complete inverse barrier admits an exact escape classification beyond
   its ternary precision, or a forward/inverse combination yields new descent.

### Outcomes and falsified candidates

1. **Partial forward progress, not whole-row closure.** R44 proves the
   returning interface and complete a3/a4 subdomains, with a nonempty
   family at every initial exponent a. It also identifies exact undo
   recipes. Review corrected the first undo endpoint from a-2 to a-3:
   the next state is1 modulo8 and is where the prescribed forward step
   can begin progress. Index-only acceptance was rejected for the common
   rank, with w6645→4205 as a retained counterexample.
2. **A successful common rank.** R43 proves the fully expanded W9 rank
   bound and the absorption bound, then uses rho to combine exact rules.
   R45 classifies both nonselected base inverse branches, with strict
   descent on w20 modulo27 or91 modulo243. The1613→2549 dependency is
   valid because its rank drops4839→3823. The failed h1,p0 rows are literal
   self-requests; every other failed positive-h row retains a uniquely
   largest expanding request. Repeating those same branches is not progress.
3. **Variable-depth escape succeeds on complete families.** R46 proves an
   exact two-block slope test, including integer endpoints, and a whole
   four-step escape classification. It also proves that inverse delay is
   unbounded even at fixed v3(q-1)=1, and persists after one/two forward
   arrows. Thus fixed-depth or valuation-only preprocessing is abandoned
   as a universal completion; longer comparisons remain available.

### Durable evidence

- [R43 proof and union](critical_rank/CRITICAL_IMAGE_RANK.md):2048 W9
  bounds,4096 absorption bounds,195 accepted rules among1024 candidates,
  58 mixed closures and seven actual substitutions. P749 stores its inputs
  and output; P1029 closes without supplied currents by signed cancellation.
- [R44 proof](returning_phase/RETURNING_FORWARD_INTERFACE.md):2048 endpoint
  bounds,228 returning inputs,456 undo checks,96 CRT examples through a128,
  12 actual substitutions and six rejection checks.
- [R45 proof](nonselected_inverse/NONSELECTED_INVERSE_PHASES.md):4096
  nonselected inputs,2731 complete positive-h plans,288 parameter cases,
  911 exact self-returns and four actual substitutions, with a stored1613
  fixture demonstrating index growth and rank decrease.
- [R46 proof](inverse_escape/INVERSE_ESCAPE.md):2731 word cases,444 exact
  parameter examples through D256/j182,317 strict plans,16 actual
  substitutions,227 depth4 targets,3229 finite inverse words,48 long-ray
  words and15 complete small-origin checks. Three current tables are saved.

### Review and current validation

Independent model proof/code audits passed all four results and the mixed
compiler, after correcting the R44 undo endpoint. The focused checkers
pass and deterministic receipts are retained. The existing TeX source was
updated in place and the desktop compiler reports success. The full `python3 scripts/verify_all.py --cpp` gate passed, including all
four new checks, all previous checks,31 archive manifest entries and both
independent C++ cutoffs. Final integrated-document review passed after
correcting a TeX reference, making the inverse slope hypothesis explicit,
clarifying that run lengths grow as a varies, and splitting the two R45
auxiliary rank bounds correctly. The existing TeX compiled successfully
after those changes. All266 checked local links resolve;39 TeX labels are
unique and every reference resolves. All29 changed/new files have LF
endings and staged whitespace review passes. The accompanying Git history
records the authorized delivery.

### Decision and next obligation

This batch meets the complete-subdomain progress test and is **progress**.
Keep exact signed currents and use rho for mixed induction. Let A be the
accepted union of R41,R44,R45,R46. Universal supply on W5 minus A remains
the required premise. The nonselected multiples of3, failed base phases,
and unaccepted returning inputs are concrete next domains. Find a complete
new reduction or prove eventual rank decrease through a broader comparison.
More isolated examples or sample percentages do not close that obligation.
The goal stays active. Claude's controls remain useful; the fresh remote
read gives no new merged result requiring abandonment of the programme.

Checklist:

- [x] Revalidate the authoritative state and independent feed.
- [x] Derive and falsify candidate rules on complete remaining domains.
- [x] Prove successful reductions and retain exact failed dependencies.
- [x] Independently audit the mathematical and executable claims.
- [x] Persist standing, proofs and reproducible evidence.
- [x] Run the full verification gate and finish integration review.
- [x] Review and prepare the verified batch for authorized commit and push; delivery is recorded by the accompanying Git history.
