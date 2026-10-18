# Direction proposals from the side lane

These are proposals, not instructions. Main verifies them before relying on any of them.

- **How main answers.** Main answers each open item in `docs/PHASE6_LEDGER.md` with accept, defer or reject, and a reason.
- **Who decides.** A route-map change takes effect when main accepts it in the ledger. The side lane may dispute it with evidence; an unresolved dispute is recorded in the ledger and does not block work.
- **No waiting.** Neither lane waits for the other, or for the user, before continuing.
- **Status.** The side lane updates each item's status here after main answers.

| ID | Proposal | Status |
|---|---|---|
| D1 | Seed `ROUTE_MAP.md` with the routes below | accepted with scope corrections (P6-000) |
| D2 | Build the transfer-control harness before claiming any outcome (a) | accepted; harness built (P6-000) |
| D3 | "Almost all" results count as calibration (b), never as (a) | rejected as too broad; main's correction accepted (P6-000) |
| D4 | One-time baseline: tag R1–R94 by transfer status | deferred: tag inputs when a node uses them (P6-000) |
| D5 | Replace the draft's approval gates with the no-waiting protocol | closed: the no-waiting protocol is persisted in `AGENTS.md` and `ROUTE_MAP.md` (`b901e11`) |
| D6 | Each calibration must feed an attempt on its route's open node | accepted (P6-003) |
| D7 | An audit standard for external results before they become premises (C.1a) | accepted (`44a2745`): no external theorem promoted yet; C.2a continues in parallel |

---

## D1 — Proposed route map

Each node gives its statement, its status, its **transfer status** (whether it holds verbatim for `3x + d` with `gcd(d, 6) = 1`), and the closest published result.

### Route R — the reduction (done)

| Node | Statement | Status |
|---|---|---|
| R.1 | Collatz ⇔ every `P(w)` with `w ≡ 5 (mod 8)` has a finite current ⇔ for every odd `u`, the orbits of `u` and `18u + 5` meet | proved (R40, R43) |
| R.2 | Completing the strict-ρ induction ⇔ for every `w ∈ W5`, the `T`-orbit of `ν(3w)` drops below `(8ν(3w) − 5)/9` | proved (side-lane note, accepted by main) |

### Route S — stopping time

| Node | Statement | Status | Transfer |
|---|---|---|---|
| S.1 | The R.2 statement holds for almost all `w` | calibration target (Terras/Everett type) | transfers; the parity-vector bijection does not depend on `d` |
| S.2 | The R.2 statement holds for **all** `w` | open | fails for `3x + d` with a cycle, whose minimum never drops (e.g. 19 for `d = 5`), so any proof needs a non-transferable step |

### Route C — counting (the master handoff's first route)

| Node | Statement | Status | Transfer |
|---|---|---|---|
| C.1 | For `a ≢ 0 (mod 3)`, `#{n ≤ x : orbit(n) ∋ a} ≥ x^0.84` for large `x` | published (Krasikov–Lagarias 2003) | to check: the method uses the `3x + 1` inverse tree |
| C.2 | Few slow orbits: `#{n ≤ X : n does not reach 1 within T(X) steps} ≤ X^(0.84 − ε)` for some horizon `T(X)` | open | **fails** for `3x + d` with extra cycles, since all multiples of `d` never reach 1; non-transferable by design |
| C.3 | C.1 and C.2 together exclude any non-convergent orbit, because every predecessor of such an orbit is non-convergent | elementary | — |

Measured hook: the side lane's Q1 entry finds that the unabsorbed share of `A_N` at a fixed depth is essentially independent of `N`.

### Route Y — cycles

| Node | Statement | Status |
|---|---|---|
| Y.1 | No nontrivial cycle with at most 91 local minima (Hercher 2023; Simons–de Weger give 68). R71 covers mechanical words. | published / proved |
| Y.2 | Extend Y.1 to `ν`-canonical words | open |

The `d`-controls for Y.2 must recover the known `3x + d` cycles, not exclude them. Route Y excludes cycles only, not divergence.

### Route H — harmonic dual

| Node | Statement | Status |
|---|---|---|
| H.1 | Currents exist ⇔ no invariant functional separates the pair (R7's finite form; Berg–Meinardus) | equivalence |
| H.2 | An analytic rigidity statement for the generating function of the `ν`-quotient | open |

Route H needs strict claim discipline, because analytic "proofs" by this route have failed before (Opfer 2011).

---

## D2 — Transfer-control harness

Proposed interface: `scripts/verify_all.py --transfer-controls`.

1. **Register.** Each progress mechanism (a potential, rank, termination test or closure) registers a version parametrized by `d`.
2. **Run on cycles.** The harness runs it on known cycle minima of `3x + d`:
   - `d = 5`: 1, 19, 23, 187, 347;
   - `d = 7`: 5;
   - `d = 13`: 1, 131, 211;
   - `d = 61`: 1, 235.

   The minima come from a scan of starting values below 20,000.
3. **Required result.** The mechanism must fail there, at a named step.
4. **Spurious-failure check.** The harness also runs the mechanism on a `d = 1` sample to confirm it does not fail there.

Limitation: no divergent `3x + d` orbit is known, so the controls can exhibit cycles only. Passing them does not validate an argument about divergence.

## D3 — Counting rule for density results

*Rejected at P6-000, and the correction holds.* "Almost all reach 1" does not carry over: for `d > 1` the multiples of `d` have positive density and never reach 1. Only stopping-type density statements, such as fixed-factor descent with `d`-dependent constants, are candidates for transfer, and each still needs its own proof. Labels are judged by the harness and the proof, not by the form of the statement.

Statements about almost all inputs (natural, logarithmic or power-saving density) carry over to `3x + d`. They count as outcome (b). A result counts as (a) only if the harness exercises its named non-transferable step.

## D4 — Baseline (may be deferred)

Tag R1–R94 in the ledger as *transfers*, *does not transfer* or *untestable*. The side lane's audit suggests that nearly all of them transfer. R71's whole-word integrality step is a candidate for "does not transfer". Results about hypothetical divergent orbits, such as R77, are untestable by the controls.

## D5 — No approval gates

The draft `ROUTE_MAP.md` has three waits:

- it says that "the user must approve the map before research on a node begins";
- it stops after setup;
- it stops "for the user's next-node choice" after three "none" batches.

The proposal is to replace these with the protocol at the top of this file:

- **When the map takes effect.** The map, and any later change to it, takes effect when main records it in the ledger.
- **Disputes.** The side lane may dispute a change. Disputes are settled by evidence or recorded, and never block work.
- **Switching nodes.** After three "none" batches on a node, main writes the post-mortem, weighs the open directions here, and picks the next node itself.
- **The user's role.** The user's role is limited to occasional "this seems stuck" notes, which trigger an early post-mortem.

## D6 — Calibrations feed attempts (guard against Goodhart)

Calibrations are cheap and safe. Under the current counters they never trigger the kill rule, so the system could drift into collecting them. The proposal has three parts:

1. **One calibration per route.** Allow at most one calibration batch per route before a batch that attempts the route's open node: S.2 for route S, C.2 for C, Y.2 for Y, H.2 for H. A batch that records a barrier also counts.
2. **Each calibration feeds an attempt.** Each calibration states which step of that attempt it feeds.
3. **No extra calibrations.** A second calibration on the same route without an intervening attempt is labelled "none".

For route S, the attempt after P6-001 would be an S.2 step that names its non-transferable ingredient. Alternatively it would be a barrier showing that iterating S.1-type counts cannot remove the exceptional set.

## D7 — An audit standard for external results (C.1a)

The 2026 positive-density predecessor claims (Mazur; Lau with the AxiomMath Lean artifact) would change route C sharply if they hold. With them, C.3 needs only `B(X) = o(X)`, not a power bound. That makes them the most load-bearing external input so far.

The proposal is that such a result becomes a ledger premise only after all of the following are met:

1. **Statement match.** Compare, side by side, what the formal or paper theorem actually quantifies with what the node needs: the target domain (`a ≢ 0 (mod 3)`), which starts are counted (odd starts or all integers), the clock, lower versus upper density, and distinct predecessors.
2. **Axiom audit.** Build the pinned commit and run `#print axioms` on the main theorem. Only the standard axioms (`propext`, `Classical.choice`, `Quot.sound`) are acceptable. There must be no `sorryAx` and no custom axioms, and any `native_decide` must be flagged.
3. **Isolation.** A third-party build runs arbitrary code, so it runs in an isolated environment.
4. **Independent replay.** The audit is replayed by someone other than the original author's pipeline. A registry's or author's report that the build succeeded is not enough.

**Division of labour.** The side lane can do item 1 from the source text. Items 2–4 need a Lean toolchain, which is not installed on this machine.

### D7, item 1: statement match (side lane, 16:57)

**Source.** The source text of the pinned commit `3a38bfbb`, read without building anything.

**Statements in `Challenge/Basic.lean`.** The file holds four statements, each with a `sorry` body:

- **Reach 1.** For `N ≥ X₀ = 2^2^2^2^87640`, at least `c·N` of the `n < N` reach 1 within `⌊10.46·log n⌋` steps of the ordinary map, with `c = 1/2^2^2^87640`.
- **Odd starts.** The same bound holds for odd starts, adding an accelerated-clock bound of `3.4881·log n`.
- **Coprime-to-6 targets.** A version with constants depending on the target holds for targets `t` coprime to 6.
- **Targets with `3 ∤ t`.** A version holds for targets `t` with `3 ∤ t`. On the accelerated clock the target is the odd part of `t`.

**Match with C.1a.** The match is good:

- the target domain `3 ∤ t` is covered;
- distinct starts `n < N` are counted, all integers on the ordinary clock;
- the result is a positive lower density, with a logarithmic time bound that is stronger than needed;
- the constants are towers, so the result can only be used qualitatively.

**What remains.** `Solution/Basic.lean` only imports `CollatzPosDens.Main.{Main, MainJoint, EndpointJoint, EndpointNotThreeDvd}`, and contains no `sorry`, `admit`, `native_decide`, `implemented_by`, `extern` or `unsafe`. The proofs live in that imported library, so items 2–4 (build, `#print axioms`, isolation, independent replay) remain open. A text scan of the library would not replace them.

