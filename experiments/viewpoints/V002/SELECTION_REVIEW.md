# V002 — Language-selection review

**Decision, 2026-10-18:** recommend arithmetic regularity of component
colorings (V13) as the preferred working language for the next bounded
investigation. Retain binary/ternary carry boundaries (V14) for one
complementary probe and actual integer-ensemble information (V12) as an
independent alternative. No claim of a better convergence proof strategy,
novel theorem, or regularity of the actual nonabsorbing set is made.

The [living map](../../../VIEWPOINT_MAP.md) is the user-facing comparison;
the [brief](../../../docs/VIEWPOINT_BRIEF.md) is the unchanged goal.

## Why this choice earned a recommendation

| Goal criterion | Evidence for V13 | Limitation |
|---|---|---|
| Better organized obligations | Replace unrestricted component separation with a specified regularity class and exact arithmetic functional equations | The unrestricted coloring question is still equivalent to convergence |
| Explanation of recurring failures | Every finite-period invariant collapses to a constant for d=1, over every modulus | This explains the limitation of periodic invariant separation, not every finite-state or residue method |
| Useful structure | The commutator of doubling and the affine branch gives translation by d; d=1 has a unit shift | Extending the odd branch to all residues uses periodicity, which is not available for arbitrary colorings |
| Checkable consequence | Complete elementary classification through gcd(M,d), including eventual periods and the absorber | Written and independently reviewed, not formally verified or claimed novel |
| Intermediate milestone | Classify finite-valued base-2-automatic invariant colorings | No automaticity theorem for an actual bad set; the proposed one-base classification is unproved here |
| Explicit limits | d=5 and d=61 admit the stated divisibility colorings; all clocks/domains are recorded | These simple colorings do not classify every nonprincipal basin in the controls |

The [proof and card](invariant_colors.md) supply the details. The
[example verifier](verify_examples.py) checks 480 finite quotient partitions
and exact examples; it is not the all-modulus proof. The separate
[receipt](verification.json) states its finite scope.

Compared with V13, V14 supplies a meaningful shared binary/ternary boundary
representation but no new boundary-completion estimate. V12 supplies exact
information identities and a precise candidate distribution estimate but no
new estimate. These differences support the order of bounded investigations;
they do not assign probabilities of solving Collatz.

The rejected initial shortlist had more than a first glance: the
[relational test](relational_test.md) checked both a successful and an
unfinished frozen family; the [geometric test](geometry_test.md) derived
a local tail bound and compared two tiny domains. Neither improved its
global obligation. Expanding to V11–V14 was a response to those results.

## Requirement-by-requirement completion evidence

| Requirement in the brief | Authoritative evidence | Assessment |
|---|---|---|
| Broad, substantially different survey | Fourteen entries in VIEWPOINT_MAP, with symbolic, arithmetic, geometric, operator, proof, statistical and automata objects | Met; related lenses are explicitly identified rather than counted as independent proofs |
| Short bounded probes and parallel exploration | V001 three survey lanes and three probes; V002 relational/geometric tests, statistical cards and coloring comparison | Met; no dispatcher expansion or large orbit search |
| Seven evaluation fields per candidate | Linked V001/V002 cards, independently checked for all fourteen entries | Met; deferred milestone templates are labeled as such, not ready programmes |
| Objects and structural gain | Each card's first two fields and the comparison table | Met; supporting notation and mere restatements receive scoped demotions |
| Translated unresolved difficulty | Each card's gap field, including integer realization, escape mass, legality, regularity and boundary completion | Met; none is silently assumed away |
| Worked examples | Exact affine words, R81/R93 comparisons, inverse tails, entropy mergers, finite-period argument and carry trace | Met at their stated finite/written scopes |
| Related-map controls | d=5/d=61 examples throughout, with the differing target/lattice/domain made explicit | Met; V14's control is external arithmetic, not a simulated d=5 tile system |
| Cheapest meaningful test | Each card and the map's focused programme with success/stop conditions | Met; subsequent tests are proposed, not reported as executed |
| Partial milestone, not a disguised full proof | Restricted automatic class; small-cycle window; capped ensemble estimate; scoped targets/templates in deferred cards | Met; unproved regularity, universal leaf supply and limit exchanges remain premises |
| Living comparison, shortlist, expansion and combinations | Map preserves V001 probes, closes A/B with reasons, adds V11–V14 and evaluates V13/V14 together | Met; combination has no unproved kernel-closure claim |
| Defensible recommendation and focused subsequent programme | This review and the map's three prioritized bounded tests | Met; no requirement to prove those subsequent milestones is substituted for the selection goal |
| Preserve frozen results and counterexamples | V002 delivery check restricts changes to exploration files and current-standing documentation; R1-onward ledger body compared with the batch baseline | Verification recorded in VIEWPOINT_LOG |
| References, assumptions and claim types persisted | Source links and status labels in cards, logs and this review | Met; prior-work checks are scoped and no novelty claimed |
| README and independent side lane | Updated top-level README; pinned DIRECTIONS/FEED and proposal assessment in VIEWPOINT_LOG | Met; side branch read only |
| Commit, push and appropriate verification | Example receipt plus delivery entry in VIEWPOINT_LOG; main and origin/main matched cdfb143 with a clean worktree after the successful push | Met for the substantive batch; this delivery-record follow-up is also pushed before completing the goal |

## Skeptical review and prior-work gates

An independent reviewer checked the finite-period proof, the seven-field
coverage and the recommendation. No mathematical correction was requested.
The review required three qualifications, retained in the map:

1. Working-language priority is supported; superior convergence prospects are not.
2. A finite-state carry mechanism does not imply a finite ternary kernel.
3. Fixed-budget regular predecessor languages are prior work. Their union
   over unbounded budgets need not be regular.

The [primary fixed-budget result](https://arxiv.org/html/1907.00775v4)
and [Cobham input](https://research.ibm.com/publications/on-the-base-dependence-of-sets-of-numbers-recognizable-by-finite-automata)
are now identified in V13. The source check is not an exhaustive search for
a published answer to the single-base question. That is the first proposed
follow-up, not a reason to assert novelty now.

## What remains open after selection

No automatic-coloring classification beyond the stated supplied/two-base
case has been proved here. No regularity of arbitrary component indicators,
finite boundary compression, new first-passage estimate, all-integer current
supply or Collatz convergence follows. The completed deliverable is a
reasoned choice of language, comparisons and a bounded subsequent programme.

Proceed with the map's tests only as a new bounded research batch. Broaden
again if the regularity question yields only an assumption and the boundary
test only a redraw. Do not grow a large case catalogue to preserve this choice.
