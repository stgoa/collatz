# Viewpoint exploration log

## V005 — Quantitative rigidity: first bounded comparison, 2026-10-18

**Progress; active goal unresolved.** The user activated the
[quantitative brief](QUANTITATIVE_RIGIDITY_BRIEF.md): every nonconstant
finite-valued invariant must have unbounded kappa_h(D)/(D+1). The exact
goal is stronger than generic infinite-kernel growth. The
[report](../experiments/viewpoints/V005/REPORT.md) records its first batch,
the [direct proofs](../experiments/viewpoints/V005/direct_sections.md),
[graph control](../experiments/viewpoints/V005/section_graph.md), and
[primary-source audit](../experiments/viewpoints/V005/literature.md).

### Gains and bounded comparison

The direct section and literature lanes ran in parallel; root developed
the graph test. One automatic positive dyadic section forces global
constancy. The reconstruction also gives an explicit polynomial bound
between cumulative whole-kernel counts at every depth. The full positive
family has bounded depth cost under ternary sectioning, so linear binary
growth would imply linear joint binary/ternary growth of the odd section.

These results do not finish the goal. The exact graph control has all
sections nonautomatic yet count D+3, because descendant families overlap.
It retains doubling and a positive return but fails full invariance at9.
The sparse indicator of {6^(2^j)} has linear growth separately in bases2/3,
yet at least quadratic joint growth. This refutes the generic separate-base
shortcut, and Conjecture3.4 in Bell2009 as printed. No novelty or exhaustive
literature claim is made. The example fails doubling at3/6.

The [scalar interface](../experiments/viewpoints/V005/scalar_interface.md)
retains all of Collatz invariance in three equations. The preferred next
bounded test asks whether these equations prevent overlaps from sustaining
linear joint growth. Compare a joint-growth rigidity proof with direct
descendant separation; do not assume finite rank, periodicity, disjointness
or a new complexity bound for the actual bad set. The unbounded-ratio
statement remains the completion threshold, with no external blocker.

### Review, checks and preservation

Independent agent reviews cover the reconstruction and bound, sparse
example, exact graph count and scalar converse. Root and a second reviewer
replayed the standalone verifier successfully against its unchanged
[receipt](../experiments/viewpoints/V005/verification.json). It checks
224 cylinder/residue choices,896 paths and15,288 actual shortcut arrows;
5,040 tuple decompositions; graph labels and distinguishing witnesses;
59,823 sparse-cell evaluations; and45 mixed sections with990 comparisons.
The d5/d61 controls include actual nonabsorbing fixed cycles, periodic
divisibility invariants and failure of the named d1 identity.

The written universal arguments and these finite checks have separate
scopes. No equality of unknown entire sections is inferred from matching
prefixes. Historical mathematical code/evidence remains untouched, so
the Phase6 gate is not rerun. Scoped links and exact frozen comparisons
are recorded in [delivery checks](../experiments/viewpoints/V005/delivery_checks.json).

### Read-only external input

Fetched and read DIRECTIONS/newest FEED at sidekick
`3b95686f36d491a1da0b8fcf162f6c9fcceaa6e5`. Its warning that quantitative
Cobham needs an additional theorem is retained. Its stronger ratio-limit
formulation is not substituted for the accepted target. Its d-uniform
version of the full target is rejected by the periodic d5/d61 invariants.
Numerical prefix counts and explicit-Tao claims remain unadopted premises.
D1/D2/D5/D7 are retained with scope, D3 rejected, D4 deferred, D6 historical.

Fetched the Lean lane at `b980e52e4f709e88dd6cabae88073b578e0027fc` and
inspected its V004 assembly type, proof tail, reported successful build,
axiom report and matching source hash. The statement matches the main
classification with Cobham explicitly assumed. No independent local Lean
replay was performed. This is useful verification input for V004, not a
V005 complexity bound. The [side assessment](../experiments/viewpoints/V005/side_review.md)
preserves exact scopes and pins. No external lane was edited or messaged.

## V004 — Full rigidity of binary-automatic invariants, 2026-10-18

**Mathematical result: written proof of the full classification.** The
activated [goal](GLOBAL_RIGIDITY_BRIEF.md) required arbitrary finite automata;
another subclass would not count as completion. The
[central proof](../experiments/viewpoints/V004/GLOBAL_RIGIDITY.md) meets that
scope. The [goal review](../experiments/viewpoints/V004/GOAL_REVIEW.md)
maps every requirement to evidence and limitations.

### Mechanism and parallel comparison

The kernel, direct-automaton and generating-function lanes ran bounded
first passes. The decisive change was to retain the finite family K_+
of binary sections with positive offsets. Each ternary section stays in
K_+; the former exceptional h(3n) arose only when the offset was zero.
This preserves the additive guards and all positive integer endpoints.

Cobham's theorem makes the odd section eventually periodic. The elementary
finish then makes its odd period global, removes the3-primary factor and
uses two affine compositions to obtain a unit translation. This forces
constancy. The proof does not assume periodicity of all h prematurely.
The direct-automaton pass retained an exact counterexample to a scaling-only
shortcut. The analytic pass supplied both finite Mahler systems and scalar
elimination, but the shorter proof needs no additional Mahler theorem or
progression sufficiency input.

Three lanes audited the closure. The elementary finish received two
independent adversarial checks and root review. One draft corollary was
corrected from “proper union” to “nonempty proper union”; the empty union's
indicator is constant. The checker boundary at source1 was repaired to use
an actual absorbed path. No theorem hypothesis or frozen result changed.

### Verification and source scope

Root replay of `python3 -B experiments/viewpoints/V004/verify_examples.py`
passed. The [receipt](../experiments/viewpoints/V004/verification.json)
contains741 ternary transformations,6,669 common-endpoint comparisons,
28,620 ordinary arrows,128 residue graphs through255 and256 period-lift
examples. Actual d5/d61 cycles, divisibility colors and failure of the named
+1 identity are checked. Unknown/capped paths are not accepted. Finite
checks supplement the written proof; they do not prove the universal
classification or independently verify Cobham.

The [literature note](../experiments/viewpoints/V004/literature_scope.md)
records directly read primary theorem statements and a bounded novelty
search. Novelty, human peer review and formal verification remain unclaimed.
Fable's merged Lean-audit work concerns a different lower-density theorem;
it is not a formalization of this proof.

The frozen R1-onward ledger, dispatcher sources and open LaTeX document
were byte-compared against9190ccf and are unchanged. Existing mathematical
code/evidence was not modified, so the historical Phase6 gate was not rerun.
The new standalone verifier received its own scoped replay. The delivery
checks are recorded in
[delivery_checks.json](../experiments/viewpoints/V004/delivery_checks.json).

### Side lane and decision

Initial read-only pin: `357c387c600f495041f86b79f447cb840b4a7785`.
Delivery refresh: `5a379b292dde9601579112591444101446678fd9`; DIRECTIONS
and newest FEED were read using `git show`. Its new referee note proposes
a d-uniform periodicity theorem and reports finite-prefix kernel counts.
These were not adopted as mathematical premises. The exact
[assessment](../experiments/viewpoints/V004/side_review.md) retains the
independently checked divisibility controls and defers the broader theorem
and unreplayed counts. D1/D2/D5/D7 remain retained with scope, D3's blanket
transfer remains rejected, D4 remains deferred, and D6 is historical.

V004 completes the requested classification. It proves no regularity for
the actual nonabsorbing set. Given this theorem, proving that set automatic
would be equivalent to convergence and is not an intermediate milestone.
The map records quantitative section complexity as a possible next target,
alongside the separate statistical alternative. No follow-on goal is
activated here.

### Delivery

Committed the completed batch as
`f54b7416caac3b8d1bc3f76e8c4f572de07b830c` and pushed it to origin/main.
Immediately after the push, local HEAD and origin/main matched that commit
and the working tree was clean. The final scoped checks passed:17 Markdown
files,501 local links,15 anchors, four frozen comparisons and the standalone
arithmetic replay. This documentation follow-up records the completed
delivery; it does not alter the mathematical result or activate another goal.

## 2026-10-18 — Recommendation after the user requests a higher target

The user observed that the selected language yielded only a small theorem
and asked for the next high-level goal. The
[proposal](NEXT_GOAL_PROPOSAL.md) raises the target to the **full**
binary-automatic invariant-coloring classification. Another selected
subclass would be progress, not completion. Mixed ternary closure, direct
automaton rigidity and a Mahler relation are candidate mechanisms to
compare. The connection to arbitrary component indicators remains separate.
This is a recommendation; it does not activate or replace a goal.

Freshly inspected side input is pinned at
`357c387c600f495041f86b79f447cb840b4a7785` (DIRECTIONS and newest FEED);
the separate explicit-Tao branch at `478a069` reports a scoped window
obstruction. Those reports are deferred as mathematical premises pending
independent checking. Existing D-numbered dispositions remain unchanged.
Remote main now contains merged PR2's Lean-audit records; the clean local
checkout was fast-forwarded to it. The proposal records the exact branches,
completed versus unfinished receipt scopes and the absence of a new replay.
No mathematical proof, evidence or code was modified for this strategy note.

## V003 — Arithmetic regularity yields a partial classification, 2026-10-18

**Substantive status:** the [report](../experiments/viewpoints/V003/REPORT.md)
delivers a digit-count classification, two kernel reductions and an exact
counterexample to a weaker closure inference. Full binary-automatic
classification remains open. The
[goal audit](../experiments/viewpoints/V003/GOAL_REVIEW.md) maps every item
of the [unchanged goal](ARITHMETIC_REGULARITY_BRIEF.md) to evidence and limits.
Repository verification and delivery are recorded below.

### Progress and comparison

The intervening goal-wording response was **no progress** for the research
goal: it supplied reusable wording but no new mathematical evidence. This
continuation inspected the saved work, completed independent proof review,
corrected scope issues and supplied reproducible checks. The substantive
V003 investigation and its delivery continuation are **progress**, with no
external blocker or inferred background process.

- **Digit-count theorem:** every invariant F(s_2(n)) is constant, for every
  function F on positive weights. This covers an explicit infinite automatic
  class, including nonperiodic descriptions, beyond V002's periodic case.
- **Kernel reduction:** all first ternary sections of the entire binary
  kernel K lie in K union {f_1}, and the pure-zero orbit f_t(n)=h(3^t n)
  has at most |K| states. The mutually linked mixed-section equations are
  retained. No whole-kernel closure is inferred.
- **Scoped barrier:** chi(oddpart(n)) is binary-automatic and invariant
  under doubling/tripling, but has infinitely many distinct mixed ternary
  sections. Its failure at the actual odd source3 preserves the full target.
- **Known cylinder result:** published progression sufficiency already
  implies the d1 constant-section consequence. Its elementary dyadic proof
  and general-d scope are retained without counting it as a new theorem.
- **Carry test closed:** the complete frontier for5 yields the existing
  relation and no additional section constraint. No broader tile search.

Recommend a bounded mixed-section probe with all guarded identities, or an
explicit finite characteristic-zero 3-Mahler relation. If that probe adds
no structure, compare V12 or broaden again. A finite automaton catalogue
would not establish the missing universal implication.

### Independent reviews and corrections

The [proof review](../experiments/viewpoints/V003/PROOF_REVIEW.md) independently
checks the kernel algebra, digit-count proof, predecessor construction and
CRT section separation. It also records the carry calculation's separate
spot checks. Three presentation issues were corrected before delivery:
the carry comparison omitted the newly proved nonzero section; the scaling
example was wrongly juxtaposed with absence of constant sections, although
it has them; and canonical mixed ternary sections of offset1 start at depth1.
The zero-extension convention and stale L6 anchor were made explicit/fixed.
No error in frozen mathematics was found or corrected.

### Read-only independent lane

Reviewed DIRECTIONS, FEED and relevant V13 notes/code/receipt after fetching
`origin/claude/sidekick` at `c583fc3e1adab7c15d6297a5acf55d7560fc5e08`.
The [assessment](../experiments/viewpoints/V003/side_review.md) records:

- **Accept, scoped:** the reported 2,400 residue component-count checks as
  external finite corroboration of V002, not an all-modulus proof or a
  replay completed in this batch.
- **Accept as a conditional tool:** invariance of one supplied automaton
  is decidable with the encoding, carries and odd-source guard fixed.
- **Qualify the numerical state bound:** the claimed70 follows from an
  external absorption bound and a normalized leading-zero convention.
  Canonical-positive-only machines give69 by the stated argument instead.
  No externally reported numerical absorption cutoff is adopted into our
  independently verified evidence, and neither bound classifies unbounded
  automata.
- **Retain D1/D2/D5 with prior scopes; reject D3's broad transfer claim;
  defer D4 and the historical D6 calibration sequence; retain D7's formal
  audit standard.** Corrections to older density proposals remain in force.
  The separate reported Linux replay is uninspected input.

The side branch was not edited or pushed. Its favorable recommendation of
V13 is a judgment, not a premise for any of the V003 proofs.

### Verification and delivery

The [standalone verifier](../experiments/viewpoints/V003/verify_examples.py)
and [receipt](../experiments/viewpoints/V003/verification.json) passed the
author's replay, independent reviewer replay and coordinating-agent replay.
They check:

- 127 digit-count family instances and three connecting sources;
- 315 parity classes, with 3,780 explicit predecessor paths over five d
  values and six targets, replaying 85,758 shortcut arrows and 7,740
  compressed odd arrows;
- 1,524 affine inverse branches, 762 divisible-offset cases, 117
  pure-zero mergers and 468 mixed-pair index identities;
- 72 pairwise mixed-section witnesses and 256 nonperiod witnesses for
  the scaling counterexample;
- the complete carry patch and its closed zero tail, retaining all clocks;
- the d5 length3 and d61 length41 nonabsorbing cycles, divisible fixed
  points, 252 binary CRT color fixtures, 132 doubling/odd-part checks,
  66 absorbed-arrow and 64 ordinary odd-source color checks, and both
  named failures of the unchanged d1 section identity.

These are bounded checks; written proofs supply the unbounded quantifiers.
The checker compares the receipt without mutating it. Unknown flags and a
corrupted receipt were also confirmed to fail without changing evidence.

The [delivery integrity receipt](../experiments/viewpoints/V003/delivery_checks.json)
records the coordinating-agent audit: all changed tracked files are standing
documentation; new files are confined to the brief and V003; the R1-onward
ledger body, seventeen-family dispatcher/proof and open LaTeX match both
the batch baseline c47d91b and frozen baseline9190ccf byte for byte. Local
link/fragment checks passed, as did `git diff --check`. No historical
mathematical code or Phase6 infrastructure changed, so the full historical
gate was not rerun. Fresh origin/main matched the batch baseline before
the commit.

### Delivered batch and completion audit

The substantive batch was committed as
`2ac44efffcf93d5c1d8d8807d4e7cd2492182946` and successfully pushed to
`origin/main`. Immediately afterward, local main and origin/main both
resolved to that commit and `git status --porcelain` was empty. The final
integrity receipt records118 checked local links and17 local fragments.

The unchanged-goal audit confirms all four research-approach requirements,
the explicit infinite-class result, the kernel gain, the scoped obstruction,
controls, references, recommendation and repository delivery. Full automatic
classification remains open and is not substituted for the goal's expressly
accepted demonstrated-gain outcome. This documentation follow-up records the
observed delivery; it is also committed and pushed before the goal-status
update. No research requirement is being waived to end the batch.

## V002 — Expanded survey and working-language recommendation, 2026-10-18

**Status:** substantive comparison completed; delivery checks and commit are
recorded below. Recommend V13 arithmetic regularity of component colorings,
with one V14 carry-boundary probe and V12 as a statistical alternative.
The [selection review](../experiments/viewpoints/V002/SELECTION_REVIEW.md)
audits the unchanged brief. This completes the language-selection deliverable
once its delivery checks pass; it supplies no convergence theorem.

### Progress and bounded scope

The previous research batch V001 was **progress**: it changed authoritative
files and supplied three discrimination probes, delivered at `77ce821` with
delivery record `bff8938`. V002 continued from its two explicit tests, not
from a new proof campaign. The intervening requested goal wording is retained
as conversation context; the persisted brief is unchanged.

Parallel follow-ups tested the relational and geometric shortlist, while a
separate lane examined occupation measures and actual integer-ensemble
information. Arithmetic regularity and two-dimensional base conversion
expanded the survey to fourteen views. No frozen proof, existing mathematical
code, dispatcher, receipt or open LaTeX source was edited. A small standalone
example verifier was added for reproducibility; it uses no Phase6 machinery.

### Findings and decisions

- **Demote A: relational histories.** The R81 successful merger already
  carries the proposed relation; R93 already has the compact asynchronous
  invariant. Missing guards or a deleted coordinate defect create false
  closure. No new accepted domain or simpler closure obligation resulted.
- **Demote B: graph geometry.** An inverse-tail bound `4/(3n_0)` is useful
  for approximation but transfers to known-cycle controls. Comparing the
  height-13 domain with the supplied path of 7 exposes the unresolved
  excursion. No weighted growing-domain estimate was obtained.
- **V11: keep as a diagnostic.** Occupation measures distinguish cycle mass
  from escape of mass. Small stationarity defect alone supplies no tightness;
  tightness alone does not identify the absorbing cycle.
- **V12: retain an alternative.** Integer endpoint laws retain conditioning
  and actual merger information. The card states a quantitative first-passage
  target; no estimate has been derived. Literature comparison comes first.
- **V13: preferred working language.** For every finite period M and fixed
  positive odd d coprime to3, invariant colorings factor through gcd(M,d)
  and multiplication-by2/3 orbits. Eventual periodicity becomes global.
  At d=1 all such colors are constant; d=5/61 divisibility colors survive.
  This written proof is independently reviewed, not claimed novel or formally verified.
  Classifying the single-base automatic class is a partial next target;
  automaticity of an actual bad set is not supplied.
- **V14: one complementary test.** Shared binary/ternary carry boundaries
  preserve more than separate norms. Their finite alphabet does not bound
  the growing frontier or imply finite kernel closure. The nonlocal bootstrap,
  finite-input zero tail and all three clocks must be retained.

The selected programme has specific tests and stop conditions in the map.
Several deferred cards contain useful milestone templates but no selected
family; they are not described as ready proof programmes. No extended
automata search or new dispatcher catalogue is part of this batch.

### Read-only independent lane

The preparatory read used `8878d5f87f5336afc70724544771fc3e920856d8`.
The final fresh fetch reviewed DIRECTIONS, FEED and VIEWPOINTS at
`21ab2a031cee71454a84047ef406c1b99a5a87c2`. The latter reviews V001 at main
`bff8938`. It supplies no review of the new V002 coloring proof. The side
branch was neither edited nor pushed.

Retain D1/D2/D5 as scoped in V001; D3 remains rejected as too broad; D4 is
deferred; D6's former route sequence remains historical. D7's audit standard
is retained, and our completed P6-004 replay remains the adopted evidence.
The feed reports a separate Linux audit in draft PR2; no result from that
uninspected build is imported. Its report about interruption of an old main
gate does not invalidate the independently completed, retained retry.

The side's new density proposal is **retained under historical C.2a, not
adopted as a fifteenth independent language**. Independent assessment:

1. For d=1, the audited predecessor theorem implies B is empty or has
   positive lower density. This correct deduction and the target-dependent
   comparison were already persisted in the
   [matched-density note](../experiments/phase6/linear_density_audit/next_upper_attempt.md).
   It is not a literal zero-or-one density theorem.
2. The explicit lower constants `c(a)=1/(a^4 L)` have infimum zero over an
   unbounded inverse-closed bad set. There is no positive minimum over all
   unknown bad targets. A contradiction needs comparison at a particular
   target, such as the successor of a hypothetical least bad seed.
3. [Tao v7, Theorem 3.1](https://arxiv.org/html/1909.03562v7#S3) does give a
   fixed-height tail bound of the form `C/(log V)^c`. Its unspecified
   constants do not give the proposed numerical upper fraction at a verified
   cutoff, or the missing target-matched inequality. This is a legitimate
   quantitative question already on the historical route, not a new estimate.
4. The audited qualitative transfer uses fixed positive odd d coprime to3
   and eligible targets. It did not transfer Lau's explicit constants to
   every d. Multiples-of-d controls are separate elementary facts.

The side's “known dead end” label for V3 is too strong if read as an
impossibility theorem: the inspected relaxation is solved, while arbitrary
legal-path lifting remains unsupplied. Keep the scoped V001 verdict. Its
V6 recommendation as measurement is consistent with our new local estimate,
but the executed global-gain test gives no further geometry-only priority.

### Verification and delivery

The local delivery checks passed:

- `python3 experiments/viewpoints/V002/verify_examples.py`: 480 exact
  residue partitions for d in {1,5,7,13,61}, M=1..96; R81/R93 ordinary
  histories and the missing-guard example; cycle/entropy examples; inverse
  tail entries and the supplied path; the four-transition carry trace.
  The deterministic receipt pins the verifier and preserves finite scope.
- Root read the full verifier and replayed it independently. Its author
  additionally checked rejection of a corrupted receipt and unknown options
  without mutation. No mathematical discrepancy was found.
- Independent review checked all fourteen cards against the seven fields,
  the elementary proof and the recommendation. Its cautions about working
  language versus convergence, untested carry closure and prior automata
  work were incorporated.
- Local documentation checks passed for 20 Markdown files, 473 links and
  12 local anchors. `git diff --check` passed. The R1-onward ledger body,
  exact goal brief and open LaTeX bytes match baseline `bff8938`. Tracked
  changes are confined to the six current-standing documents and the new
  V002 exploration directory; historical mathematical files are unchanged.

The all-modulus result rests on the written proof; the 480-partition scan
only illustrates it. The full historical finite gate is not rerun because
this batch changes no existing mathematical code or evidence. Primary sources,
formula/domain checks, bounded exact examples, independent skeptical review,
links and preservation checks are proportionate to these claims.

The final independent delivery review passed after the map, README and
selection audit were written. It requested only the novelty-wording correction
above. The exploration batch was committed as
`cdfb1434b26598067d1f2ec1a78f60bdebd1c388` and successfully pushed to
`origin/main`. Local main and origin/main matched that commit and the working
tree was clean immediately after the push. This documentation follow-up
records that observed delivery and the review's wording correction. Its own
push and clean-state check precede the goal-status update.

All requirements of the language-selection brief have evidence in the
selection review. The chosen subsequent tests are explicitly future work;
none is a missing part of the comparative deliverable. No independent
external audit is being waited on. Collatz convergence remains open.

## V001 — Breadth first, 2026-10-18

**Status:** completed initial survey and bounded discrimination probes.
The active goal remains open: no language has yet earned a deep investigation.
The [brief](VIEWPOINT_BRIEF.md) is the exact user-approved goal, persisted
from the active goal record. [VIEWPOINT_MAP.md](../VIEWPOINT_MAP.md) is the
living comparison and next-test register.

### Scope and baseline

The user replaced the prove-or-narrow objective with exploration of
Grothendieck-style changes of viewpoint. R1–R94, the seventeen-family
dispatcher, stored certificates and the open LaTeX source remain frozen.
The prior P6-004 audit was completed and committed as `5a11fcb` before
this exploration batch. Its full119-field gate, source compilation,
statement/axiom checks and same-kernel replay are evidence for that audit,
not verification of any new viewpoint.

Three parallel first passes compared nine views: symbolic/arithmetic,
operators/geometry, and rewriting/induced dynamics/abstract interpretation.
We added rational denominator layers as a tenth view after the initial
comparison. Three bounded follow-ups tested lifting, loop summaries and
finite Dirichlet domains. No new dispatcher cases, large orbit searches,
long proof development or LaTeX edits were undertaken.

### Findings and decisions

1. **Legal-path information is easily lost.** Exact guarded affine blocks
   compose with a domain pullback, retaining offsets and clocks. A slope,
   product of factors, or integer intermediate alone does not certify a
   Collatz arrow. The semigroup probe identifies an unsupplied multiplication
   bridge in one published induction step. Defer that route without an
   independent lifting mechanism.
2. **Loop exhaustion is not global progress.** R31's exact counter controls
   one guarded phase while height grows. The raw word can continue after
   that guard ends. R77 and subsequent work already contain this mechanism;
   unary inducing adds no new coverage here. A relational pilot must improve
   on the existing asynchronous history results.
3. **Geometric quantities need genuine estimates.** Positive finite-domain
   voltage is existing component membership. Voltage values additionally
   lose mass through real escape edges. Potential theory remains a different
   toolset, but no arithmetic energy bound or advantage was found.
4. **Changing d changes the arithmetic domain and target.** Rational
   normalization places trajectories in invariant reduced-denominator layers.
   A d-system can contain several layers, and its target is1/d. This is
   useful control bookkeeping, not a new denominator-one progress mechanism.

Retain two conditional portfolios for further short tests: exact relational
arithmetic histories, and arithmetic graph geometry. Absorbing operators
provide a common quantitative observable. Defer pure semigroup completion,
bare groupoid/homology renaming, and unary return catalogues. The next tests
and their stop conditions are explicit in the map. If those tests only
recover existing results, fan out again rather than deepen by default.

### Independent side lane

Fetched `origin claude/sidekick main`; main was
`44a2745a7e89c316e9d9bac3ce5feea77e7bca2c` before the local audit commit.
Read both DIRECTIONS and FEED at
`54bb81b89e8eb2d8bfc25aa263147669d28e5c19`. The new feed item is a source-only
statement comparison for D7; it is not an independent confirmation of our
later executed replay. The exact pinned formal source and our retained
statement output govern the numerical constants. No new side claim was
adopted as a viewpoint theorem, and the side branch was unchanged.

| Proposal | Current decision | Reason |
|---|---|---|
| D1: route map | Retain as evidence | User's new goal makes it informative rather than restrictive. |
| D2: known-cycle controls | Retain | They expose false progress arguments; each new claim still needs a declared test. |
| D3: all density claims transfer | Reject, as previously corrected | Stopping and absorption claims have different transfer behavior. |
| D4: classify every frozen result by transfer | Defer | Classify only inputs actually used; a wholesale audit would distract from breadth. |
| D5: proceed without routine approval waits | Retain | User has authorized autonomous exploration and repository delivery. |
| D6: calibration-to-route-attempt sequence | Historical, superseded for exploration | The new objective evaluates languages and information loss, not Phase6 batch grades. |
| D7: external theorem audit standard | Retain; completed for the adopted formal-source theorem | P6-004 records actual isolated execution and its explicit trust boundaries. Side confirmation is separate. |

### Verification and limitations

- Root reviewed the ten cards and three probes, including exact domain,
  signed-boundary, ordinary/shortcut/quotient/auxiliary-clock distinctions.
  Primary literature is linked beside imported claims; no novelty asserted.
- Checked elementary affine compositions, the extra-bit counterexample at35,
  the d5 cycle and inverse escape arrows, the two eight-arrow R31 examples,
  and the stated rational voltage comparison. These checks support the
  examples only; the notes identify their elementary all-input arguments
  separately and cite frozen results where used.
- Independent synthesis review passed after correcting two summary claims:
  V4 is an exact survival observable while V6 gives auxiliary lower bounds;
  the geometric target must specify50%, since a tiny positive fraction is
  already supplied by the audited lower theorem. The review also caught a
  stale nine-versus-ten count, corrected in README. Link/anchor/consistency
  checks are recorded at delivery below. No new executable mathematical checker
  was added. The historical full gate was not rerun for this prose survey.
- The frozen result-ledger body from R1 onward, mathematical source,
  dispatcher and open LaTeX document were checked unchanged. Active-goal
  sections of README/AGENTS and historical-status banners were updated.

This batch does not prove a new absorption fraction, an aperiodic exclusion,
a universal current, a spectral gap or a novel theory. It rejects several
unearned inferences and makes the next language tests more discriminating.

### Delivery

Independent review and focused arithmetic checks passed. Local checks covered
17 Markdown files,473 links and nine intra-document anchors, with no errors.
The R1-onward result body and open LaTeX source are unchanged. The survey was committed as `77ce821` and pushed to `origin/main`, together
with the completed P6-004 audit at `5a11fcb`. Local main and origin/main
matched at `77ce821d2fcc38c705974f7b1ac40a3216f6a79d` and the working tree
was clean immediately after that push. This documentation follow-up records
the actual delivery. The exploration goal remains active.
