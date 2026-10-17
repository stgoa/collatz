# Residual progress and finite forcing

**Latest standing:** complete aggregate exposure depth is now proved unbounded,
already on the ladder `N=96*64^k`. A terminating auxiliary normalization and
an exact local input conversion sharpen the constructive target but leave
positive residuals. The merged independent lane adds valuable negative
controls; its broader claim excluding alternative one-sided currents was
corrected with exact counterexamples. Collatz remains open.

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
