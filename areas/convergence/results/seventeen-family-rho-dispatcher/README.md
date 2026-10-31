---
id: seventeen-family-rho-dispatcher
kind: result
title: Seventeen conditional strict-rank families with fixed inner resolvers
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1; P(w) = [3w] - [w], rho(w) = nu(3w) on W5. The dispatcher tries, in order,
  the unchanged fifteen-family dispatcher (with its complete internal priority and returned plan), then R62's
  defect resolution and R64's lifted inverse comparison, and uses the first success; it returns None or an integer
  current J and nonzero signed W5 coefficients with div J = P(w) - sum c(u) P(u) and rho(u) < rho(w) for every
  remaining request, checked by the R43 validator. R59 keeps its fixed old-twelve resolver and R62's optional audit
  its fixed old-fifteen resolver; neither calls this dispatcher. R63 and R65 are not rules. Formal closure
  terminates by induction on rho with unrecognised leaves retained (a node cap raises an error, never a
  certificate), and conditional compilation requires an exact supplied current for every remaining request. This
  is termination of formal conditional composition, not recognition or supply of every leaf; the sigma induction
  is not imported, and finite acceptance counts are evidence, not asymptotic coverage.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [fifteen-family-rho-dispatcher, absorption-defect-original-rank-resolution, lifted-inverse-ray-cycle, critical-image-rank-composition]
certificates: [check_legacy_replay.py]
evidence:
  - "check_resolved_rules.py, resolved_rules.py, resolved_rules_audit.json: the legacy constructor and checker: all 1024 W5 inputs below 8192 (all 747 previously accepted plans preserved as full dictionaries, matching the fifteen-family hash; 747 accepted, 277 unresolved, no new input in the window), witnesses 53173 (R62) and 36641534965 (R64) outside the window, the R45-priority overlap at 20405, six supplied-current demonstrations with 14 distinct supplied pairs and five negative checks. Fails at its new path: resolved_rules.py loads ../refined_rules/ (now ../fifteen-family-rho-dispatcher/), ../defect_resolution/ (now ../absorption-defect-original-rank-resolution/) and ../refined_obstruction/ (now ../exponent-eleven-fifteen-rule-classification/) by their pre-migration folder names; it is the fixed resolver loaded by the later legacy native_history/, even_exit_history/ and later_target_probe/ code. Passed at be73a66 as experiments/residual_progress/resolved_rules/check_resolved_rules.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Dispatcher code checked against the claim (priority, fixed inner resolvers, R43 validation); all 1024 window plans, their closures, the two witnesses, the overlap, the six supplied conversions and 360 random inputs re-validated with the lane's own nu, rho and divergence; certificate re-run (PASS, exit 0, 10 s). Verdict HOLDS, two imprecision-level findings, no correction"
aliases: [R64-b]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, dispatcher, conditional-compiler]
---

# Seventeen conditional strict-rank families with fixed inner resolvers

## Statement

Odd-only clock, 1 absorbing; `P(w) = [3w] − [w]`, `ρ(w) = ν(3w)` for `w ∈ W5`.

1. **Priority.** The dispatcher tries (i) the unchanged [`fifteen-family-rho-dispatcher`](../fifteen-family-rho-dispatcher/README.md), (ii) R62's defect resolution ([`absorption-defect-original-rank-resolution`](../absorption-defect-original-rank-resolution/README.md)), (iii) R64's lifted inverse comparison ([`lifted-inverse-ray-cycle`](../lifted-inverse-ray-cycle/README.md)), and uses the first success. R63 ([`exponent-eleven-fifteen-rule-classification`](../exponent-eleven-fifteen-rule-classification/README.md)) is an obstruction and R65 ([`adjacent-source-defect-equivalence`](../adjacent-source-defect-equivalence/README.md)) a reformulation; neither is a rule.
2. **Fixed inner resolvers.** R59 keeps the old twelve-family resolver, R62's optional `fixed_resolution` audit keeps the old fifteen-family resolver; neither calls this dispatcher.
3. **One step, closure, compilation.** As for the fifteen-family dispatcher: `one_step` returns `None` or an exact strict-`ρ` plan checked by the validator of [`critical-image-rank-composition`](../critical-image-rank-composition/README.md); formal closure terminates by induction on `ρ` with unrecognised leaves retained, a node cap raising an error; `compile_plan` needs an exact supplied current for every remaining request.

This is termination of formal conditional composition, not universal recognition or supply; the remaining inputs are the obligation of [`universal-w5-tripling-currents`](../../questions/universal-w5-tripling-currents.md).

## Proof

The legacy note "Seventeen conditional families with fixed inner resolvers" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: composition of written strict-rank rules, with finite exact
substitutions.** The fifteen-family dispatcher keeps its exact priority.
The added defect-resolution and lifted-inverse rules use the same positive
integer rank. Unrecognized inputs remain explicit premises. Universal
current supply and Collatz remain open; this note makes no density or
novelty claim.

### Interface and priority

Use absorbed odd Syracuse, `P(w)=[3w]-[w]`, and `rho(w)=nu(3w)` for
positive `w=5 mod8`. The first successful rule wins:

1. The unchanged [fifteen-family dispatcher](../fifteen-family-rho-dispatcher/README.md),
   preserving every internal priority and its complete returned plan.
2. [R62 defect resolution](../absorption-defect-original-rank-resolution/README.md).
3. [R64 lifted inverse comparison](../lifted-inverse-ray-cycle/README.md).

The separate sigma induction is not imported. R62 uses only plans that
pass the original-rho comparison after retaining and combining all signed
requests. R63 is an obstruction result and R65 is a reformulation; neither
is an additional dispatch rule.

`one_step(w)` returns `None` or a finite integer current and signed W5
request coefficients satisfying

\[
 \operatorname{div}J=P(w)-\sum_u c(u)P(u),\qquad
 \rho(u)<\rho(w)\quad\text{for every nonzero request}.       \tag{1}
\]

The [R43 validator](../critical-image-rank-composition/README.md) checks the
exact boundary and every strict inequality on each returned plan,
including an inherited plan. Equal requests and current rows combine
with their integer coefficients; negative requests remain negative.

#### The inner resolvers remain fixed

R59 retains the old twelve-family resolver. R62's optional
`fixed_resolution` audit retains the old fifteen-family resolver.
Neither resolver calls this new dispatcher. R62's dispatched `one_step`
uses its exact first/second continuation plans and the original-rho test;
its optional fixed-resolver audit is a separate interface. This keeps the
proved fixed-fifteen obstruction separate from the broader seventeen-rule
closure.

The inherited R59 inner cap stays in force. A capped candidate is not an
accepted strict-rank step; later dispatch rules may still be tried.
No omitted request is treated as supplied.

### Finite formal composition and supplied currents

`close(w,max_nodes=None)` uses the R43 signed closure compiler. Each
recognized node has finite support and its children have strictly smaller
positive integer rank. Induction on rank gives finite formal composition,
with every unrecognized leaf kept as a signed input. Memoization and exact
cancellation may reduce the resulting expression.

This formal termination does not prove universal recognition or provide
unknown currents. An unrecognized root returns no current rows and the
request `{w:1}`. An optional outer node cap raises an unresolved
computation error.

`compile_plan(plan,supplied)` requires a finite exact current for every
remaining nonzero request. It checks each supplied boundary and adds the
current with its signed coefficient. Equation (1) then telescopes to
`P(w)`. Missing or incorrect supplied currents are rejected. The three
public APIs do not search for unknown absorption paths.

### Reproducible finite evidence

Run:

```sh
python3 experiments/residual_progress/resolved_rules/check_resolved_rules.py
```

The checker examines all 1024 W5 inputs below 8192. All 747 previously
accepted plans are preserved as full dictionaries, and their combined
current/request hash matches the stored fifteen-family receipt. This
window has 747 accepted inputs and 277 unresolved inputs; neither new rule
adds an input in this small window. These finite counts do not establish
asymptotic coverage.

Separate witnesses exercise both added winning arms:

| Input | First successful rule | Earlier fifteen rules |
|---:|---|---|
|53173|R62 defect resolution|all unrecognized|
|36641534965|R64 lifted inverse|all unrecognized|

The R64 witness is `parameter_family(0,14,remainder=1)`: it uses zero cycle
blocks and a maximal point depth 14, with an eighteen-arrow inverse word.
Its direct conditional plan has nine signed requests. A further overlap
check uses 20405: R62 recognizes it, but the older R45 plan retains
priority unchanged.

Six exact supplied-current demonstrations use
221,53173,85941,15224757,11432437,36641534965. Recognized descendants are
expanded before supplying the remaining leaves. The demonstrations use
fourteen distinct supplied pairs in total and produce respectively
41,92,65,59,133,102 current rows. Complete plans, supplied current tables,
and output currents for 15224757 and 36641534965 are retained in
`resolved_rules_audit.json`; the other examples retain exact hashes and
are reconstructed by the checker. The two stored examples retain five
and four signed input pairs respectively.

The unresolved root 21 remains `{21:1}`, with rank 31 and no current rows.
Five negative checks reject two invalid domains, a zero outer closure
cap, missing supply, and a supplied current with the wrong boundary.
Fixture discovery has cycle detection, a 10000-step cap and a 512-bit cap;
formal closure demonstrations have a 10000-node cap. These bounded
fixtures are evidence only for the displayed inputs.

`--write-receipt` regenerates the evidence. Default execution compares
the complete result, including local source hashes, with the stored
receipt. Every remaining signed input remains an explicit proof
obligation.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B12 migration; standard library). The legacy scripts of this folder load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the legacy checker `check_resolved_rules.py` (about 7 s; the 1024-input window, the two witnesses, the overlap, six supplied-current demonstrations and five negative checks, compared with `resolved_rules_audit.json`). The commands in the legacy text name `experiments/residual_progress/resolved_rules/`.

## Remarks

- This is the frozen W5 dispatcher of the later legacy rounds: R75 ([`common-critical-rank-basis`](../common-critical-rank-basis/README.md)) and the native/history rounds R78–R94 (from [`native-critical-nine-continuation`](../native-critical-nine-continuation/README.md) to [`prescribed-ternary-child-unbounded-clocks`](../prescribed-ternary-child-unbounded-clocks/README.md)) leave it unchanged.
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/resolved_rules/RESOLVED_RULES.md` (legacy ID R64, the companion dispatcher of the R62-R65 round) at commit `be73a66`, by the B12 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical; `check_legacy_replay.py` was added at the migration. Legacy status: "composition of written strict-rank rules, with finite exact substitutions".
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `793e835`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No correction to the claim or proof; the review records that the R62 arm's code also carries R58's plan (dead under the stated priority) and that an arm failing the R43 validator would raise rather than return None ([`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md)).
