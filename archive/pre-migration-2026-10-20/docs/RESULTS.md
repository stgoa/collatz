# Results index

One row per result or batch, grouped by research line. Statuses follow [`AGENTS.md`](../AGENTS.md) §4; legacy labels are translated per [`CONVENTIONS.md`](CONVENTIONS.md) §4. The authoritative status of a Lean unit is its row in [`lean/STATE.md`](../lean/STATE.md).

When you add a result, add its row here and in the line's `README.md`.

## Cycle spectrum (active): `experiments/cycle_spectrum/`

The goal is in [`BRIEF.md`](../experiments/cycle_spectrum/BRIEF.md) and the batch log in [`LOG.md`](../experiments/cycle_spectrum/LOG.md).

Batches C001–C014 come from the main lane; results S01–S13 come from the side lane.

| ID | Result | Status |
|---|---|---|
| [C001](../experiments/cycle_spectrum/C001/REPORT.md) | A fixed perturbation bounds cycle-denominator cancellation for repeated-block words. | `written`; C001-a/b `formal` |
| [C002](../experiments/cycle_spectrum/C002/REPORT.md) | Two growing blocks: different equal-total blocks give denominator `> 2^m`. Proportional slopes give explicit growth. | `written`; C002-a `formal`; C002-b partly `formal`: (6)–(8) and the `K = 0` core |
| [C003](../experiments/cycle_spectrum/C003/REPORT.md) | Bounded-denominator layers of nondegenerate two-block powers are finite. | `written`, reviewed by an agent; C003-a `formal` |
| [C004](../experiments/cycle_spectrum/C004/REPORT.md) | `H < 2L` is equivalent to a mechanical word, so every nontrivial cycle has `H > 2L`. | `formal` (C004-a…d with R71) |
| [C005](../experiments/cycle_spectrum/C005/REPORT.md) | Concatenations of rotations of one mechanical base are never integer cycles. | `written`; C005-a…h `formal` |
| [C006](../experiments/cycle_spectrum/C006/REPORT.md) | Ordered cycles: few height changes force large gaps, `J ≥ √m − O(log m)`. | `written`, conditional on a two-log bound; C006-a…f `formal` |
| [C007](../experiments/cycle_spectrum/C007/REPORT.md) | The candidate law `B ≤ q − 1` survives tests; two shortcuts refuted. | candidate `open`; shortcuts `refuted` |
| [C008](../experiments/cycle_spectrum/C008/REPORT.md) | Sorted residue progression; primewise height matching refuted. | `written` + `refuted` (scoped) |
| [C009](../experiments/cycle_spectrum/C009/REPORT.md) | Excursion compression rejected. | `refuted` (mechanism) |
| [C010](../experiments/cycle_spectrum/C010/REPORT.md) | Gap lattices: exact equivalence; local odd rounding rejected. | `written`; C010-a/b/c `formal` |
| [C011](../experiments/cycle_spectrum/C011/REPORT.md) | A word with a two-defect rotation is never an integer cycle (`ρ ≥ 3`). | `conditional` (Matveev, period bound); C011-a `formal` |
| [C012](../experiments/cycle_spectrum/C012/REPORT.md) | What a uniform rotation bound must retain; adjugate elimination rejected. | `written` + `refuted` (scoped) |
| [C013](../experiments/cycle_spectrum/C013/REPORT.md) | Shared background with nonconstant markers forces denominator growth. | `conditional` (Matveev); C013-a/b `formal` |
| [C014](../experiments/cycle_spectrum/C014/COMPATIBLE_ARCS.md) | Limits of a common partition for compatible arcs. | **work in progress**, unreviewed |
| S01 | Equal-total word pairs: the J-term gap lead. Feed entry only, no note. | units S1-a…e `formal` |
| [S02](../experiments/cycle_spectrum/S02/RENORMALISATION.md) | Run-compression renormalisation of ordered cycles rejected; exact obstruction. | `refuted` (mechanism); identities `formal` |
| [S03](../experiments/cycle_spectrum/S03/INVERSION_PAIRS.md) | Ordering up to `H < 16L` reduces to excluding the pair `(n, 8n+1)`; route blocked. | reduction `formal` |
| [S04](../experiments/cycle_spectrum/S04/BAND1_GCD.md) | No law for `gcd(C, D)` on ordered band-1 cycles. | `evidence` (negative) |
| [S05](../experiments/cycle_spectrum/S05/MISMATCH_HEIGHT.md) | `s > log₂3·m/(B + 342 log₂m + 172)` for every rotation. | `formal`, conditional on EXT-1 |
| [S06](../experiments/cycle_spectrum/S06/C011_VIA_S5.md) | C011 without Matveev, for `m ≥ 24,891`. | `formal`, conditional on EXT-1 |
| [S07](../experiments/cycle_spectrum/S07/THREE_MISMATCHES.md) | No rotation with exactly three mismatches, so `ρ ≥ 4`. | `formal`, conditional on EXT-1 (`m ≥ 2^19`) |
| [S08](../experiments/cycle_spectrum/S08/FOUR_MISMATCH_MAP.md) | The claim "the size method stops at three" was withdrawn after a counterexample. | `withdrawn`; by-products `formal` |
| [S09](../experiments/cycle_spectrum/S09/DENOMINATOR_LAW.md) | S06 and S07 as denominator laws for every `3x+q`. | `formal` |
| [S10](../experiments/cycle_spectrum/S10/MULTI_ROTATION.md) | Several rotations in a model: the size method reaches `s = 4`. | `evidence` (model); `ρ ≥ 5` paused |
| [S11](../experiments/cycle_spectrum/S11/C013_GAP.md) | C013 at `q = 1` with EXT-1 instead of Matveev. | `written`, conditional on EXT-1 |
| [S12](../experiments/cycle_spectrum/S12/DENJOY_KOKSMA.md) | Denjoy–Koksma height bound and denominator law. | `formal`, no external input |
| [S13](../experiments/cycle_spectrum/S13/RISE_LEMMA.md) | Rise lemma; short rotations grow like `log m`; reduction to the largest letter. | lemma `formal`; thresholds conditional on EXT-1 |

## Viewpoints (finished): `experiments/viewpoints/`

| ID | Result | Status |
|---|---|---|
| [V001](../experiments/viewpoints/V001/lifting_probe.md) | Guarded affine composition versus semigroup lifting, a bounded probe. | `evidence` |
| [V002](../experiments/viewpoints/V002/SELECTION_REVIEW.md) | Language selection: arithmetic regularity of colourings. | decision |
| [V003](../experiments/viewpoints/V003/REPORT.md) | Arithmetic regularity: partial results; completed by V004. | `written` |
| [V004](../experiments/viewpoints/V004/GLOBAL_RIGIDITY.md) | Every binary-automatic Collatz-invariant colouring is constant. [D-uniform extension](../experiments/viewpoints/V004/D_UNIFORM_AUTOMATIC.md) for all `3x+d`. | `formal` with Cobham as a named hypothesis (V004-iii); extension `written` |
| [V005](../experiments/viewpoints/V005/REPORT.md) | Quantitative rigidity: local reconstruction; two growth shortcuts rejected. | `written`; V005-a `formal` |
| [V006](../experiments/viewpoints/V006/REPORT.md) | Quadratic separation theorem. | `written`; V006-a `formal` |
| [V007](../experiments/viewpoints/V007/REPORT.md) | First finite-separator obstruction: single exits excluded. | `written`; V007-a `formal` |
| [V008](../experiments/viewpoints/V008/REPORT.md) | Boundary size alone cannot prove the growth theorem. | `refuted` (extension) |
| [V009](../experiments/viewpoints/V009/REPORT.md) | Unbounded additive excess and a global detection bound. | `written`; the unbounded-ratio goal stays `open` |

## Phase 6 (finished): `experiments/phase6/`

[`ROUTE_MAP.md`](../experiments/phase6/ROUTE_MAP.md) defines the route nodes; [`LEDGER.md`](../experiments/phase6/LEDGER.md) records the grades.

| ID | Result | Status |
|---|---|---|
| [P6-001](../experiments/phase6/stopping_calibration/STOPPING_CALIBRATION.md) | Stopping-time calibration for route node S.1. | calibration, confirmed |
| [P6-002](../experiments/phase6/stopping_transport/STOPPING_TRANSPORT.md) | Endpoint-cardinality barrier. | barrier |
| [P6-003](../experiments/phase6/growth_norm_transport/GROWTH_NORM_TRANSPORT.md) | Arbitrary-target transport cannot contract any power-growth norm. | barrier, confirmed |
| [P6-004](../experiments/phase6/linear_density_audit/README.md) | Audit of the external positive-density claim, route node C.1a. | audit |

## Packet currents (frozen)

R1–R94 split across four folders:
- `experiments/packet_currents/` (R1–R4 and controls C1–C5);
- `experiments/current_construction/` (R5–R7);
- `experiments/annular_construction/` (R8–R9);
- `experiments/residual_progress/` (R10–R94).

[`experiments/residual_progress/REPORT.md`](../experiments/residual_progress/REPORT.md) and the archived [`RESULTS.md`](../archive/docs/RESULTS.md) give the full round-by-round index.

| Range | Result | Status |
|---|---|---|
| R1–R4 | Right-aligned depth-one reduction; finite current certificates suffice on five rays. Proof note: [`papers/right_aligned_reduction`](../papers/right_aligned_reduction/right_aligned_reduction.tex). | `written` + `evidence` |
| R5–R7 | Five-ray reduction, annular recursion, current-existence criterion, per-packet obstruction ([report](../experiments/current_construction/REPORT.md)). | `written` + `evidence` |
| R8–R9 | Affine lifting and universal partial currents; a contraction attempt fails ([report](../experiments/annular_construction/REPORT.md)). | `written` + `evidence` |
| R10–R94 | Residual progress: many partial constructions and exact obstructions. Universal terminal supply unresolved ([report](../experiments/residual_progress/REPORT.md)). | frozen; the objective is `open` |
| C1–C5 | Negative controls from the independent lane, with corrections ([PR1 review](../experiments/packet_currents/negative_controls/PR1_REVIEW.md)). | `evidence` |

## Explicit Tao (closed): `experiments/explicit_tao/`

| ID | Result | Status |
|---|---|---|
| L2–L3 | Valuation-tail lemmas, with a finite certificate. | `written` + `evidence` |
| L4 | The printed architecture is vacuous unless `log x > 6.27·10^13`. Leg 1 closed as a scoped barrier. | barrier; "re-optimisation cannot help" is a candidate (`open`) |
| L5–L6, Legs 2–3 | Not started. | `open` |

## Formal development: `lean/`

[`lean/STATE.md`](../lean/STATE.md) is the unit table: every formalised statement, its prose source, status, axioms and receipts. [`lean/README.md`](../lean/README.md) summarises it and explains how to build.
