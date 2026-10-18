# V004 — Audit against the full global-rigidity goal

**Mathematical completion: PASS.** The unchanged activated objective is
saved in [GLOBAL_RIGIDITY_BRIEF.md](../../../docs/GLOBAL_RIGIDITY_BRIEF.md).
It requires the full finite-valued binary-automatic classification;
subclasses and finite experiments alone do not complete it.

## Requirement audit

| Requirement | Delivered evidence | Limit |
|---|---|---|
| Every finite-valued binary-automatic invariant is constant | [Central proof](GLOBAL_RIGIDITY.md), §§1–5 | Uses established finite-kernel characterization and Cobham; not formally verified here. |
| Arbitrary automata, no state-size or digit-statistic restriction | All positive offsets at every depth are retained in K_+ | Finiteness follows from the stated automaticity hypothesis alone. |
| Absorber1 retained | h(4)=h(1) follows from doubling; no outgoing absorber arrow is added | Finite path checks also handle the source1 boundary explicitly. |
| Compare kernel, direct automaton and generating-function mechanisms | [Kernel](kernel_route.md), [automaton](automaton_route.md), [Mahler](mahler_route.md) notes and central comparison table | The Mahler alternative shares the same closure; it is not independent formal verification. |
| Full proof, not partial-result completion | Positive ternary closure → odd-section eventual periodicity → global odd period → residue constancy | No selected subclass or empirical inference supplies the universal step. |
| Assess relevance to actual convergence | Central proof §6 and [independent review](INDEPENDENT_REVIEW.md) | No automaticity or complexity upper bound for the actual nonabsorbing set is known here. |
| Preserve controls, failures, sources, checks | [Finite receipt](verification.json), [literature scope](literature_scope.md), [side review](side_review.md) | Novelty undetermined; finite checks do not prove the classification. |
| Repository delivery | Updated README, map, AGENTS, ledgers; delivery recorded in the [viewpoint log](../../../docs/VIEWPOINT_LOG.md) | Frozen R-series, dispatcher and open LaTeX source are unchanged. |

## Review and corrections

Three separate mathematical lanes checked the positive-offset closure.
The kernel lane supplied the elementary residue finish; the automaton and
controls lanes independently attacked its cutoff, parity, quotient and
commutator steps. The root checked the complete argument and exact source
statements. The [adversarial review](INDEPENDENT_REVIEW.md) records each
step and its quantifiers.

One wording defect in the draft consequence was corrected before delivery:
“any proper union of components” must be “any **nonempty** proper union”
when asserting an infinite kernel. The empty union has a constant automatic
indicator. This correction does not change the theorem or its proof.

The initial finite-path checker used a raw1→4 witness for one boundary
case. It was corrected to the actual absorbed path2→1 before the final
receipt. The mathematical proof had already justified h(4)=h(1) from
doubling and required no raw outgoing arrow. No frozen result was changed.

Root replayed `python3 -B experiments/viewpoints/V004/verify_examples.py`:
PASS. The receipt records741 ternary transformations,6,669 common-endpoint
comparisons,28,620 ordinary arrows,128 residue graphs through modulus255,
256 period-lifting examples, actual d5/d61 cycles and named identity
failures. Caps and invalid inputs fail closed. These are finite checks
supplementing the all-input written proof.

## What follows, and what does not

The completed theorem says a hypothetical proper component separation
cannot be represented by any finite binary automaton. Collatz itself
remains open in this repository. In particular, proving the actual bad
set automatic would, given V004, be equivalent to convergence; it is not
an intermediate milestone.

A possible next goal is quantitative rigidity: establish a growth lower
bound for the number of distinct binary sections beyond the generic
linear bound for an infinite kernel. The [map](../../../VIEWPOINT_MAP.md#focused-subsequent-programme)
records an explicit candidate and the separate statistical alternative.
No such growth theorem or feasibility claim is supplied, and this review
does not activate a new goal. Formalizing the elementary proof would be
a separate verification task, with Cobham's formal availability assessed
explicitly rather than assumed.
