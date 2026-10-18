# Direction proposals from the side lane

These are proposals, not instructions. Main verifies them before relying on any of them.

- **How main answers.** Main answers each open item in `docs/PHASE6_LEDGER.md` with accept, defer or reject, and a reason.
- **Who decides.** The user approves changes to the route map.
- **Status.** The side lane updates each item's status here after main answers.

| ID | Proposal | Status |
|---|---|---|
| D1 | Seed `ROUTE_MAP.md` with the routes below | open |
| D2 | Build the transfer-control harness before claiming any outcome (a) | open |
| D3 | "Almost all" results count as calibration (b), never as (a) | open |
| D4 | One-time baseline: tag R1–R94 by transfer status | open (may be deferred) |

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

Statements about almost all inputs (natural, logarithmic or power-saving density) carry over to `3x + d`. They count as outcome (b). A result counts as (a) only if the harness exercises its named non-transferable step.

## D4 — Baseline (may be deferred)

Tag R1–R94 in the ledger as *transfers*, *does not transfer* or *untestable*. The side lane's audit suggests that nearly all of them transfer. R71's whole-word integrality step is a candidate for "does not transfer". Results about hypothetical divergent orbits, such as R77, are untestable by the controls.
