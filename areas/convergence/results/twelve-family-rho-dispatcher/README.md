---
id: twelve-family-rho-dispatcher
kind: result
title: Twelve conditional strict-rank families under one fixed-priority dispatcher
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1; P(w) = [3w] - [w], rho(w) = nu(3w) on W5. The dispatcher tries, in order,
  the unchanged nine-family dispatcher (R41, R44, R45, R46, R47, R48, R50, R52, R53 with its internal priority),
  then R55, R56 and R57, and uses the first success; it returns None or an integer current J and nonzero signed
  W5 coefficients with div J = P(w) - sum c(u) P(u) and rho(u) < rho(w) for every remaining request, checked by
  the shared R43 validator. It preserves every earlier accepted plan, and new rules cannot replace them. Formal
  closure terminates by induction on rho (unrecognised leaves are retained with exact signed coefficients; a
  node cap raises an error rather than certifying), and conditional compilation requires an exact supplied
  current for every remaining request. This is a termination statement for the conditional plan, not a proof
  that every leaf is recognised or supplied. The separate sigma rules are not included; finite acceptance counts
  are evidence, not asymptotic coverage.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [critical-image-rank-composition, low-block-continuation-prescribed-growth, selected-critical-five-forward-tables, two-selected-inverse-choices, guarded-cycle-exit-phases]
certificates: [check_legacy_replay.py]
evidence:
  - "check_selected_rules.py, selected_rules.py, selected_rules_audit.json: the legacy dispatcher and checker: all 1024 W5 candidates below 8192, every old accepted plan compared as a complete dictionary with the nine-family receipt (722 accepted versus 493 before, 229 new direct acceptances, all by R55, 302 unresolved), exact witnesses 221, 382205941 and 11324620789 for the R55, R56 and R57 branches, seven supplied-current demonstrations with 12 distinct supplied pairs (5821 closes with no input in 40 rows; 1105909 keeps four inputs, 142 rows) and five negative checks. Fails at its new path: selected_rules.py loads ../continued_rules/, ../selected_forward/, ../selected_inverse/ and ../selected_cycle_exit/ by their pre-migration folder names, and the checker reads ../continued_rules/continued_rules_audit.json (now ../low-block-continuation-prescribed-growth/); selected_rules.py is the fixed resolver of the later legacy deferred_rank/, cycle_inverse/ and refined_rules/ code. Passed at be73a66 as experiments/residual_progress/selected_rules/check_selected_rules.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "selected_rules_meter.py, selected_rules_meter.json: side-lane measurement (2026-10-17 23:51) of this dispatcher: 1,000 random w = 5 (mod 8) per size from 10 to 64 bits, accepted share about 68 to 72% at every size, of which about 21 to 25% by R55; acceptance by class at 48 bits from 57% to 92%. It measures the dispatcher, does not check it, and gives no coverage theorem. Its receipt is nondeterministic (reviews/side_lane/README.md), so it can never be a certificate. Fails at its new path: it imports selected_rules from experiments/residual_progress/selected_rules/ by repository-relative path and fibre_count_check from its own folder (now ../absorbed-fibre-uniform-counts/). Passed at be73a66 as reviews/side_lane/selected_rules_meter.py (archive/legacy-checker-run-be73a66.md, exit 0)"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Composition and termination argument re-derived from the code; every plan the dispatcher returns on the 1024 candidates below 8192 validated with an independent divergence and rank check (722 plans, 493 old ones unchanged, 229 new ones all R55 and all accepted by an independent R55 recogniser); the three branch witnesses and the two stored closed plans re-verified; certificate re-run (PASS, exit 0, 9 s). HOLDS; two imprecisions recorded, no correction"
aliases: [R57-b]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, dispatcher, conditional-compiler]
---

# Twelve conditional strict-rank families under one fixed-priority dispatcher

## Statement

Odd-only clock, 1 absorbing; `P(w) = [3w] − [w]`, `ρ(w) = ν(3w)` for `w ∈ W5`.

1. **Priority.** The dispatcher tries (i) the unchanged nine-family dispatcher of [`low-block-continuation-prescribed-growth`](../low-block-continuation-prescribed-growth/README.md) (R41, R44, R45, R46, R47, R48, R50, R52, R53, with its internal priority), (ii) [`selected-critical-five-forward-tables`](../selected-critical-five-forward-tables/README.md) (R55), (iii) [`two-selected-inverse-choices`](../two-selected-inverse-choices/README.md) (R56), (iv) [`guarded-cycle-exit-phases`](../guarded-cycle-exit-phases/README.md) (R57), and uses the first success. New rules cannot replace an old accepted plan. The separate `σ` rules are not imported.
2. **One step.** `one_step(w)` returns `None`, or an integer current `J` and nonzero signed `W5` coefficients with `div J = P(w) − Σ c(u) P(u)` and `ρ(u) < ρ(w)` for every remaining request; the shared validator of [`critical-image-rank-composition`](../critical-image-rank-composition/README.md) checks both on every step.
3. **Closure and compilation.** Formal closure terminates by induction on `ρ`; an unrecognised leaf contributes the exact request `{u: 1}` multiplied along its route, and a caller's node cap raises an error, never a certificate. `compile_plan` needs an exact integer current for every remaining request and rejects missing or malformed input.

This is a termination statement for constructing the conditional plan, not a proof that every leaf is recognised or supplied. The unresolved leaves are the remaining obligation, [`universal-w5-tripling-currents`](../../questions/universal-w5-tripling-currents.md). The earlier fixed-procedure obstruction of [`growing-prefix-unhandled-leading-input`](../growing-prefix-unhandled-leading-input/README.md) is not a claim against this enlarged collection.

## Proof

The legacy note "Twelve conditional families under one critical-image rank" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: composition of written strict-rank rules, with finite exact
substitutions.** This dispatcher preserves every accepted plan of the
previous nine-family compiler and adds the three selected-input rules.
Unrecognized inputs remain signed premises. Universal current supply and
Collatz remain open; no asymptotic coverage or novelty claim is made.

### Interface and priority

Use the absorbed odd Syracuse map, `P(w)=[3w]-[w]`, and
`rho(w)=nu(3w)` for positive `w=5 mod8`. The order is:

1. The unchanged [nine-family dispatcher](../low-block-continuation-prescribed-growth/continued_rules.py),
   preserving its existing internal priority and covering
   R41/R44/R45/R46/R47/R48/R50/R52/R53.
2. [R55 selected forward](../selected-critical-five-forward-tables/README.md).
3. [R56 selected inverse](../two-selected-inverse-choices/README.md).
4. [R57 selected-cycle exit](../guarded-cycle-exit-phases/README.md).

The first successful rule is used. In particular the new rules cannot
replace or invalidate an old accepted plan, and a later rule does not get
priority merely because its proof produced a demonstration seed. The
separate R51 sigma rules are not imported into this dispatcher.

`one_step(w)` returns `None` if every test fails, or an integer current `J`
and nonzero signed W5 request coefficients `c(u)` satisfying

\[
 \operatorname{div}J=P(w)-\sum_u c(u)P(u),\qquad
 \rho(u)<\rho(w)\quad\text{for every remaining request}.       \tag{1}
\]

The shared R43 validator checks both assertions on every returned step,
including steps supplied by the old dispatcher. Equal coefficients are
combined without discarding their signs.

### Finite formal closure and conditional compilation

`close(w,max_nodes=None)` applies the [R43 signed closure
compiler](../critical-image-rank-composition/README.md). Every local plan has
finite support, and every recursive request in an accepted plan strictly
decreases a positive integer rank. Induction on that rank proves that
the formal substitution tree is finite. This is a termination statement
for constructing the **conditional plan**, not a proof that every leaf
has a recognized rule or a supplied current.

If a leaf `u` is unrecognized, it contributes the exact request `{u:1}`.
Its coefficient is multiplied by all signed coefficients on its route;
requests and current rows are then combined by linearity. Memoization may
reuse a constructed local result without changing (1). A caller's node
cap raises an unresolved computation error; reaching a cap supplies no
certificate. A root unrecognized immediately returns current `{}` and
request `{w:1}`.

`compile_plan(plan,supplied)` requires an exact integer current for every
remaining nonzero request. It checks each supplied boundary before adding
the current with the stored signed multiplicity. The result then has
exact boundary `P(w)`. Missing or malformed input is rejected. No orbit
discovery, conjectural absorption or numerical small-residual shortcut
occurs in these three APIs.

### Finite audit and retained evidence

Run

```sh
python3 experiments/residual_progress/selected_rules/check_selected_rules.py
```

The checker examines all 1024 W5 candidates below 8192. Every old accepted
plan is compared as a complete dictionary, and its current/request digest
must match the previously stored nine-family receipt. For each new
acceptance, the checker also reconstructs the first successful new rule
and verifies exact priority, current and coefficients. The resulting
counts are finite evidence, not asymptotic estimates.

The stored window has 722 accepted inputs versus 493 previously, with
229 new direct acceptances and 302 unresolved inputs. All 229 new window
acceptances choose R55 by priority. Separate exact witnesses 221,
382205941 and 11324620789 exercise the R55, R56 and R57 winning branches
respectively; this prevents small-window overlap from leaving either later
dispatch branch untested.

Seven supplied-current demonstrations use seeds 221, 2813, 10357, 5821,
93301, 1105909 and 11324620789. Each closes all recognized descendants
before supplying the remaining leaves. The full closed plans, supplied
input currents and output currents for 5821 and 1105909 are retained in
`selected_rules_audit.json`; the other examples retain exact hashes and
request lists and are reproduced by the checker. Fixture input discovery
has cycle detection, a 10000-step cap and a 512-bit cap. Formal closure
has a 10000-node cap. These capped discoveries are finite demonstration
inputs, independent of the symbolic rule proofs.

The checker additionally retains an explicit unrecognized root and tests
invalid domains, a closure cap, missing supply and incorrect supply.
`--write-receipt` regenerates the evidence; the default invocation compares
the complete result and source hashes against the stored receipt.
The seven conversions use 12 distinct supplied pairs in total. The closed
5821 plan has no remaining input and produces a 40-row exact current;
1105909 retains four signed supplied inputs and produces 142 rows. Five
negative checks cover invalid domains, the node cap and invalid supply.

This enlarged conditional compiler can be used wherever an exact supplied
W5 comparison is required. Its unresolved leaves are the remaining
obligation. The previous fixed-procedure R54 obstruction is not a claim
against this enlarged rule collection, and no conclusion about a union
with the separate sigma induction is drawn.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B11 migration; standard library). The legacy scripts in this folder load their sibling modules by pre-migration folder names, so they no longer run here. This certificate rebuilds the legacy directory layout in a temporary directory from the node folders that now hold those files, runs the unmodified legacy checks there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied receipt unchanged. It writes nothing in the repository. It replays: the legacy checker `check_selected_rules.py` (about 2 s; the 1024-candidate replay against the nine-family receipt and `selected_rules_audit.json`). The command in the legacy text names `experiments/residual_progress/selected_rules/`.

## Remarks

- **Measurement (side lane, finite).** The meter in this folder reports a size-stable accepted share of about 70% of sampled `W5`, up from about 43% for the seven-family union, mostly from R55; R56 is never the accepting rule in the samples and R57 accepts at most 0.2%, because of priority. These samples give no coverage theorem, and the meter's receipt is nondeterministic.
- **Later uses.** It is the fixed resolver of [`deferred-original-rank-testing`](../deferred-original-rank-testing/README.md) and the reference for the "old twelve" exclusions of [`rank-excess-absorption-classification`](../rank-excess-absorption-classification/README.md) and [`maximal-inverse-cycle-continuation`](../maximal-inverse-cycle-continuation/README.md); the later fifteen-family dispatcher [`fifteen-family-rho-dispatcher`](../fifteen-family-rho-dispatcher/README.md) (R61-b) appends R58–R60.
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/selected_rules/SELECTED_RULES.md` (legacy ID: part of R57; alias R57-b given at the migration) at commit `be73a66`, by the B11 migration (Claude, Opus 5.5). The plan attached this dispatcher to [`guarded-cycle-exit-phases`](../guarded-cycle-exit-phases/README.md) as evidence; it has its own note and is cited separately by R58–R60, so it became its own node. Note, scripts and receipt moved byte-identical, with the side-lane meter `reviews/side_lane/selected_rules_meter.*`; `check_legacy_replay.py` was added at the migration. Legacy status: "composition of written strict-rank rules, with finite exact substitutions".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `7206f9c`.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No correction; the review validates every plan returned on the 1024-candidate window with an independent divergence and rank check and records two imprecisions (the actual internal priority of the nine old rules is R41, R45, R44, R46, R47, R48, R50, R52, R53; `one_step` raises on inputs outside `W5` instead of returning `None`). See [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
