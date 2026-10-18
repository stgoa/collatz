# Phase 6 research report

## Standing

Collatz is open. The programme has pivoted from expanding the frozen local
dispatcher to named proof obligations in [ROUTE_MAP.md](../../ROUTE_MAP.md).
The setup batch built the grading and control infrastructure and is confirmed
**none**. S.1 has a verified, side-confirmed stopping calibration, pushed
as546e891. P6-002's endpoint cardinality barrier passed117 report fields and
was pushed asde32608. P6-003 now proves a stronger barrier: arbitrary-target
first-half transport cannot contract any power-growth norm with0<alpha<1.
Its full gate passed with118 report fields. This closes
the selected uniform-norm method; actual-B-specific estimates remain open.

## Mechanism and evidence

Every claimed advance must be a demonstrated non-transfer step, a published
calibration with explicit constants, or a proved barrier for a named method.
The [ledger](../../docs/PHASE6_LEDGER.md) records proposals, decisions,
transfer scope, literature and external confirmation. The
[control specification](README.md) and exact stored cycles make generic
descent and absorption claims falsifiable on maps with known cycles.

The source baseline is main `9190ccf`; the reviewed side-lane proposal pin is
`f244b7a5b77a51f8dd7e6bccf2c6d5f18932df88`. None of the side lane's new finite
exposure statistics is treated as a uniform density estimate. The primary
[literature audit](../../docs/PHASE6_LITERATURE.md) preserves theorem
quantifiers, constants and publication corrections.

## Open work

The [S.1 proof](stopping_calibration/STOPPING_CALIBRATION.md) now gives explicit
finite counts and the W5 pullback. S.2 still has every exceptional input to
eliminate. C.2 requires a power bound stronger than known density results.
Y.2 would exclude cycles only. H.2 needs new rigidity beyond the analyticity
already supplied by bounded coefficients. No route is complete.

## P6-000 checklist

- [x] Read repository standing and pin side proposals/feed.
- [x] Independently audit route scopes and primary references.
- [x] Write the route map and answer D1–D4 in the ledger.
- [x] Build exact transfer controls and reject unresolved searches.
- [x] Persist Phase 6 rules and navigation.
- [x] Complete full verification and independent review; [record](setup_verification.json).
- [x] Prepare the verified batch for commit/push; delivery is recorded in Git history.
- [x] Pushed setup as b901e11; began S.1 after the required side-lane refresh.

## P6-001 verification

- [x] Read updated side directions/feed and record setup confirmation.
- [x] Prove the explicit half-descent estimate for fixed d.
- [x] Prove the separate W5 count and clock conversion.
- [x] Independently review the argument and exact constructor/checker.
- [x] Store parameter examples, finite arithmetic and rejection evidence.
- [x] Finish the full gate; [verification record](stopping_calibration/verification.json).
- [x] Prepare the verified calibration for commit/push; delivery is recorded in Git history.
- [x] Pushed as546e891 and started S.2 after the required side-lane refresh.

Proposed label: calibration. The new statement is a known fixed-factor
stopping limit with explicit constants; every-input stopping remains open.

The secondary S.2 bounded-prefix idea was mathematically correct but
redundant with frozen R25/R31. It is recorded as **none**, the first such
attempt at S.2. Continue with methods allowing input-dependent unbounded
histories; do not reopen the finite-catalogue obstruction as a new result.

## P6-002 active checklist

- [x] Fetch/read side directions and feed at ade50f97; record every decision.
- [x] Specify the first-half transport premise and its proposed barrier label.
- [x] Reject the congruence-closure idea as redundant with frozen Monks audit.
- [x] Finish and independently review the exact transport proof/checker.
- [x] Register the checker; focused replay passed.
- [x] Full gate passed; [verification record](stopping_transport/verification.json).
- [x] Prepare the verified batch for commit/push; delivery is recorded in Git history.
- [x] Select the next global power-growth norm obligation, pending the fresh side read.

The ordinary first-passage map may take arbitrarily many arrows. The
proposed barrier concerns its aggregate endpoint multiplicities, rather
than a bounded search horizon or a new dispatcher family.

P6-002 now has a written scoped barrier and three independent model reviews.
Its general-d theorem excludes every finite arbitrary-target cardinality
multiplier with one uniform o(X) error. The d=1 sparse refinements exclude
the analogous cardinality bound at scale X^alpha. The remaining global
power-growth norm and actual-bad-set methods are not refuted. No human
review or proof-assistant verification is implied.

## Historical next-batch choice from P6-002

Select S.2's remaining global power-growth norm as the next attempted
method, subject to the next batch's fresh side-lane read. Define
`||A||_alpha=sup_X #(A intersect [1,X])/X^alpha`. Read-only derivation
suggests a useful separation: at d=1 the one-arrow half-descent preimage
operator has norm at most10/13 for4/5<=alpha<1, but the full first-half
operator expands a specified sparse set already through four words
`(3),(5),(2,3),(1,5)`. For targets
`A_(alpha,d)={18 ceil(j^(1/alpha))+5d:j>=1}`, the proposed leading ratio is
`(3/8)^alpha+(3/32)^alpha+(9/32)^alpha+(9/64)^alpha`, greater than241/240
when0<alpha<=7/8. This is a **candidate for P6-003**, not an accepted result
or an additional checker in P6-002. It would target a new explicit
contraction premise; actual-B-specific arithmetic estimates remain open.

C.1 was considered as an alternative. The published0.84 computation needs
a reconstructed59,049-principal-variable certificate; the paper's summary
decimals do not supply it. A small k=2 exponent2/5 benchmark is a possible
later entry, not the stated0.84 calibration. H.2's conditional natural-
boundary classification currently replaces the missing assertion with an
unproved regularity assumption. Defer both while testing the explicit
power-norm premise. No source from either alternative is imported as a
new proof premise in P6-002.

## P6-003 checklist and decision

- [x] Fetch/read side pin0ed286c5; record P6-001 confirmation and accept D6.
- [x] Prove and audit one-arrow contraction and the four-word expansion.
- [x] Extend to every0<alpha<1 using S.1 finite cylinders and inverse-residue averaging.
- [x] Finish integrated exact replay and independent final-text review.
- [x] Pass the full gate and persist its [report/source hashes](growth_norm_transport/verification.json).
- [x] Prepare the verified batch for commit/push; delivery is recorded in Git history.
- [ ] Start the next audit after the fresh side read.

The proof is in [GROWTH_NORM_TRANSPORT.md](growth_norm_transport/GROWTH_NORM_TRANSPORT.md).
It uses the calibration in an actual S.2 attempt, satisfying accepted D6.
The norm witness depends on alpha,d; its residue exists by finite averaging.
Exact affine thresholds turn homogeneous crossing words into genuine
first-half paths. No stochastic assumption about an infinite integer orbit
is used. The result transfers to all fixed supported d, so its label is
barrier, not(a). Universal convergence remains unproved.

Next examine a specific estimate for the actual nonabsorbing set B, retaining
B=E disjoint-union L^(-1)(B). This requires additional information from
invariance; simply applying the failed arbitrary-target bound is unavailable.
Further variants of the same power-norm barrier are not the next task.

## New evidence while the P6-003 gate runs

The literature check found recent primary manuscripts claiming a linear
predecessor lower bound. [L3a](../../docs/PHASE6_LITERATURE.md) pins their
statements and the Lau source commit. The local elementary counting steps
passed preliminary reading; the inherited analytic input and formal
build are not independently verified here. These results are not premises
of P6-003.

Revise the next choice to C.1a's targeted input audit, then an attempt on
C.2a. If the new lower bound checks out, an actual-B sublinear upper count
would suffice, without improving the historical0.84 predecessor exponent.
This is a reason to audit the new input before reconstructing that old
large certificate. The full statistical upper condition remains open.

The next formal audit has a practical dependency: neither `lean` nor `lake`
is currently available on the command path. No package was installed during
this batch. Source-level inspection and reported external builds remain
distinct from an independent local formal replay.

The [next-attempt note](NEXT_ATTEMPT.md) preserves a concrete open inequality
for the actual B, its elementary conditional bootstrap, and the exact d>1
failure. It uses finite maxima rather than assuming a finite global norm.
The inherited S.1 count supplies an explicit half-exception bound; the
transport inequality itself remains missing. This preparation earns no
additional batch label or non-transfer result.
