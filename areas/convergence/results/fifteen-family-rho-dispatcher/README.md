---
id: fifteen-family-rho-dispatcher
kind: result
title: Fifteen conditional strict-rank families under one fixed-priority dispatcher
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; P(w) = [3w] - [w], rho(w) = nu(3w) on W5. The dispatcher tries, in order, the
  unchanged twelve-family dispatcher (with its complete internal priority and returned plan), then R58 on its proved
  original-rho subdomain, R59 (whose inner resolver is always the fixed old twelve, with a 10000-node inner cap; a
  capped candidate is not accepted) and R60, and uses the first success; it returns None or an integer current J
  and nonzero signed W5 coefficients with div J = P(w) - sum c(u) P(u) and rho(u) < rho(w) for every remaining
  request, checked by the shared R43 validator. It preserves every earlier accepted plan. Formal closure terminates
  by induction on rho with unrecognised leaves retained as signed inputs (a node cap raises an error, never a
  certificate), and conditional compilation requires an exact supplied current for every remaining request. This is
  termination of formal conditional composition, not recognition or supply of every leaf; the sigma induction is
  not imported, and finite acceptance counts are evidence, not asymptotic coverage.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [twelve-family-rho-dispatcher, rank-excess-absorption-classification, deferred-original-rank-testing, maximal-inverse-cycle-continuation, critical-image-rank-composition]
certificates: [check_legacy_replay.py]
evidence:
  - "check_refined_rules.py, refined_rules.py, refined_rules_audit.json: the legacy constructor and checker: all 1024 W5 inputs below 8192 (all 722 old accepted plans compared as full dictionaries and against the stored twelve-family hash; 747 accepted, two new R58 and 23 new R59 choices, 277 unresolved), witnesses 4021, 1301 and 11432437 for the R58, R59 and R60 arms, the R59/R60 overlap at 284897820661, seven supplied-current demonstrations with eight distinct supplied pairs and five negative checks. Fails at its new path: refined_rules.py loads ../selected_rules/ (now ../twelve-family-rho-dispatcher/), ../exact_absorption_bound/ (now ../rank-excess-absorption-classification/), ../deferred_rank/ (now ../deferred-original-rank-testing/) and ../cycle_inverse/ (now ../maximal-inverse-cycle-continuation/) by their pre-migration folder names, and the checker reads the twelve-family receipt from ../selected_rules/ (now ../twelve-family-rho-dispatcher/); refined_rules.py is the fixed resolver of the later legacy defect_resolution/, refined_obstruction/ and resolved_rules/ code. Passed at be73a66 as experiments/residual_progress/refined_rules/check_refined_rules.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "closure_frontier_meter.py, closure_frontier_meter.json: side-lane measurement (2026-10-18 00:22) of refined_rules.close(w) at d265d94, 200 random w = 5 (mod 8) per size from 16 to 64 bits: root accepted about 62 to 76%, complete closure about 5.5% at every size from 24 to 64 bits, median leaf-rank gap about 1.3 to 2.1 bits below rho(w). A measurement with a fixed seed, not a check, and no coverage theorem. Fails at its new path: it imports refined_rules from experiments/residual_progress/refined_rules/ by repository-relative path (now this folder). Passed at be73a66 as reviews/side_lane/closure_frontier_meter.py (archive/legacy-checker-run-be73a66.md, exit 0, 216 s); a replay with tools/legacy_replay.py reproduced its receipt byte for byte at the migration"
  - "complete_core_classes.py, complete_core_classes.json: side-lane measurement (addendum to the 00:22 entry): 16 random 32-bit w in each of the 72 W5 classes mod 576 closed with refined_rules.close; no class closes completely more than 31% of the time and 35 classes never do. A measurement, not a check. Fails at its new path for the same import reason. Passed at be73a66 as reviews/side_lane/complete_core_classes.py (archive/legacy-checker-run-be73a66.md, exit 0, 86 s); a replay with tools/legacy_replay.py reproduced its receipt byte for byte at the migration"
aliases: [R61-b]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, dispatcher, conditional-compiler]
---

# Fifteen conditional strict-rank families under one fixed-priority dispatcher

## Statement

Odd-only clock, 1 absorbing; `P(w) = [3w] − [w]`, `ρ(w) = ν(3w)` for `w ∈ W5`.

1. **Priority.** The dispatcher tries (i) the unchanged [`twelve-family-rho-dispatcher`](../twelve-family-rho-dispatcher/README.md), preserving its internal priority and returned plan, (ii) R58 ([`rank-excess-absorption-classification`](../rank-excess-absorption-classification/README.md)) on its proved original-`ρ` subdomain, (iii) R59 ([`deferred-original-rank-testing`](../deferred-original-rank-testing/README.md)), (iv) R60 ([`maximal-inverse-cycle-continuation`](../maximal-inverse-cycle-continuation/README.md)), and uses the first success. R59 always resolves its intermediate requests with the fixed **old twelve** dispatcher and a 10000-node inner cap; a capped candidate is not accepted. The `σ` induction is not imported.
2. **One step.** `one_step(w)` returns `None`, or an integer current `J` and nonzero signed `W5` coefficients with `div J = P(w) − Σ c(u) P(u)` and `ρ(u) < ρ(w)` for every remaining request; the shared validator of [`critical-image-rank-composition`](../critical-image-rank-composition/README.md) checks both on every returned plan, inherited plans included.
3. **Closure and compilation.** Formal closure terminates by induction on `ρ`; unrecognised leaves stay as signed inputs, and a caller's node cap raises an error, never a certificate. `compile_plan` needs an exact integer current for every remaining request and rejects missing or malformed input.

This is termination of formal conditional composition, not universal recognition or current supply. The unresolved leaves remain the obligation of [`universal-w5-tripling-currents`](../../questions/universal-w5-tripling-currents.md).

## Proof

The legacy note "Fifteen conditional families under the original critical-image rank" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: composition of written strict-rank rules, with finite exact
substitutions.** The previous twelve-family dispatcher keeps exact priority.
The three added rules refine an absorption bound, expand signed intermediate
requests before testing the original rank, and compare along inverse cycle
words. Unrecognized inputs remain premises. Universal current supply and
Collatz remain open; no asymptotic coverage or novelty claim is made.

### Exact interface and priority

Use the absorbed odd Syracuse map, `P(w)=[3w]-[w]`, and
`rho(w)=nu(3w)` for positive `w=5 mod8`. The first successful rule wins:

1. The unchanged [twelve-family dispatcher](../twelve-family-rho-dispatcher/README.md),
   preserving its complete internal priority and returned plan.
2. [R58 exact absorption bound](../rank-excess-absorption-classification/README.md).
3. [R59 deferred rank comparison](../deferred-original-rank-testing/README.md).
4. [R60 inverse cycle comparison](../maximal-inverse-cycle-continuation/README.md).

The separate sigma induction is not imported. In particular R58 uses its
proved original-rho subdomain, not the entire sigma-accepted class.

`one_step(w)` returns `None` or a finite integer current and signed nonzero
W5 request coefficients satisfying

\[
 \operatorname{div}J=P(w)-\sum_u c(u)P(u),\qquad
 \rho(u)<\rho(w)\quad\text{for every remaining request}.       \tag{1}
\]

The shared R43 validator checks both properties on every returned plan,
including old plans. Duplicate requests and current rows combine with their
exact signed coefficients.

#### The deferred resolver is fixed

R59 always resolves its intermediate requests with the **old twelve**
dispatcher. It does not call the new fifteen-family dispatcher, itself,
R58, or R60 as an added rule. Every accepted inner expansion decreases its
own rank. Its protected original source remains an explicit request,
unless exact cancellation removes it. Only the completed original-rho
descending result may enter (1).

The implementation uses R59's fixed 10000-node inner cap. A capped R59
candidate remains an exact unfinished plan in that underlying API and is
not accepted here. The dispatcher may then try R60. If no rule succeeds,
the original input remains unresolved. This limit can reduce recognition;
it cannot supply an omitted current. The retained capped example in the
receipt demonstrates this distinction.

### Finite formal closure and conditional supply

`close(w,max_nodes=None)` uses the [R43 signed closure
compiler](../critical-image-rank-composition/README.md). Each returned step has
finite support and each recursive request strictly decreases the positive
integer rank. Induction on rank therefore gives a finite formal
substitution tree, with unrecognized leaves kept as signed inputs.
Repeated indices may reuse a memoized result. Exact coefficient
cancellation may remove some leaves.

This is termination of **formal conditional composition**, not universal
recognition or current supply. An unrecognized root returns current `{}`
and coefficient `{w:1}`. The optional outer node cap raises an unresolved
computation error. Neither cap is treated as a certificate.

`compile_plan(plan,supplied)` requires an exact current for every remaining
nonzero input. It verifies every supplied boundary before adding that
current with its signed multiplicity. Equation (1) then telescopes to the
exact boundary `P(w)`. Missing or incorrect supply is rejected. These three
APIs do not discover unknown absorption paths.

### Reproducible finite evidence

Run

```sh
python3 experiments/residual_progress/refined_rules/check_refined_rules.py
```

The checker examines all 1024 W5 inputs below8192. It compares all 722 old
accepted plans as full dictionaries and checks their current/request hash
against the stored twelve-family receipt. Every new acceptance is compared
with the first successful added rule. This finite window does not establish
a limiting or uniform density.

The stored window has747 accepted inputs, comprising all722 old plans,
two new R58 choices and23 new R59 choices;277 inputs remain unresolved.
No input in this small window selects R60, so the separate branch witness
below is necessary. The explicit unresolved root is21, retaining `{21:1}`
with rank31 and no current rows.

Separate witnesses4021,1301,11432437 exercise the R58,R59,R60 winning arms.
The last comes from R60's exact parameter family with
`k=1,j=3,unit=2,index=0`. Another R60 family member284897820661 is accepted
by R59 first. The checker preserves that overlap explicitly; an R60
family's exclusion from the old twelve does not imply exclusion from R59.

Seven exact supplied-current demonstrations use
221,4021,245,1301,787733,11432437,284897820661. Recognized descendants are
expanded before supplying the remaining leaves. Complete plans, supplied
input currents, and final currents for1301 and11432437 are stored in
`refined_rules_audit.json`. Other demonstrations retain exact hashes and
request lists and are reproduced by the checker.

These demonstrations use eight distinct supplied pairs in total. The245
closure has no remaining input and yields17 current rows. The stored1301
and11432437 conversions each retain two supplied pairs and yield59 and133
rows respectively. The large overlap witness expands41 recognized nodes,
retains three supplied pairs, and yields91 rows. These are finite
certificate sizes, not uniform complexity bounds.

Fixture path discovery has cycle detection, a10000-step cap and a512-bit
cap; outer closure has a10000-node cap. These bounded discoveries supply
only the displayed finite examples and are separate from the symbolic
proofs. Five negative checks reject two invalid domains, a zero closure
cap, missing supply, and incorrect supply. An additional explicit R59
zero-cap check preserves its high frontier and verifies no accepted step
is returned.

`--write-receipt` regenerates the evidence. Default execution compares the
complete result, including source hashes, with the stored receipt. All
remaining signed leaves continue to be the unproved input obligation.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B12 migration; standard library). The legacy scripts of this folder load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the legacy checker `check_refined_rules.py` (about 5 s; the 1024-input window, the three branch witnesses, the overlap, the supplied-current demonstrations and the negative checks, compared with `refined_rules_audit.json`). The two side-lane meters are measurements and are not certificates (see `evidence`). The commands in the legacy text name `experiments/residual_progress/refined_rules/`.

## Remarks

- **Later.** R61 ([`exponent-eleven-exit-continuation`](../exponent-eleven-exit-continuation/README.md)) is a scoped obstruction, not a rule of this dispatcher; R63 ([`exponent-eleven-fifteen-rule-classification`](../exponent-eleven-fifteen-rule-classification/README.md)) classifies the whole R61 family under these fifteen rules. The seventeen-family dispatcher [`seventeen-family-rho-dispatcher`](../seventeen-family-rho-dispatcher/README.md) appends R62 and R64 after them.
- **Side-lane measurements.** The full signed closure either finishes outright (a size-stable complete core of about 5.5% of sampled inputs) or stalls a median 1.3 to 2.1 bits below `ρ(w)`; the core is not a union of low-modulus classes. These are finite samples, not density statements (main lane, `side_lane_review_767af32.md` and the later 33c3829 review).
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/refined_rules/REFINED_RULES.md` (legacy ID R61, the companion dispatcher of the R61 round) at commit `be73a66`, by the B12 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical; `check_legacy_replay.py` was added at the migration. The side-lane meters `reviews/side_lane/closure_frontier_meter.*` and `complete_core_classes.*` moved here. Legacy status: "composition of written strict-rank rules, with finite exact substitutions".
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `d265d94`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
