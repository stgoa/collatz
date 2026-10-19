# Conventions

This page defines the notation, the status vocabulary, the meaning of every ID series, and the external inputs the repository relies on. When a document uses a symbol without defining it, the meaning here applies.

## 1. Maps and clocks

| Name | Definition | Notes |
|---|---|---|
| Collatz map | `n → n/2` (even `n`), `n → 3n+1` (odd `n`) | Used for statements only; computations use the faster forms below. |
| Shortcut map `T` | `n → n/2` (even), `n → (3n+1)/2` (odd) | Counting with it is the *shortcut clock*. |
| Odd-only (Syracuse) map `S` | odd `n → (3n+1)/2^v`, where `v = v₂(3n+1) ≥ 1` | Counting with it is the *odd-only clock*. The exponent `v` is the step's **valuation** or **letter**. |
| `3x+d` family | odd `n → (3n+d)/2^v₂(3n+d)` | `d` is odd and usually coprime to 6. The S-series and Lean files call the same parameter `q`. |

- **Clocks.** Never mix the odd-only and shortcut step counts. Every statement says which one it uses.
- **Absorption.**
  - The convergence programmes (`packet_currents`, `current_construction`, `annular_construction`, `residual_progress`, `phase6`) use the odd-only clock and **absorb at 1**.
  - The cycle programme (`cycle_spectrum`) uses **raw cycles with no absorbing state**: the fixed point `1 → 1` of `3x+1` is the trivial cycle, not an absorber.
- **Cylinders.** An exact valuation cylinder for a word of total `A` lives modulo `2^(A+1)`, including the extra bit.

## 2. Cycles, words and denominators

A cycle of the odd-only `3x+d` map is a sequence of odd positive integers `n_0, …, n_(m−1)` with `2^(a_i)·n_(i+1) = 3·n_i + d`, indices taken mod `m`.

| Symbol | Meaning |
|---|---|
| `m` | Period: the number of odd steps. |
| `w = (a_0, …, a_(m−1))` | The cycle's valuation word (its letters), each `a_i ≥ 1`. |
| `A = Σ a_i` | Total valuation. |
| `D_w = 2^A − 3^m` | Must be `> 0` for a positive cycle. |
| `C_w = Σ_j 3^(m−1−j)·2^(a_0+…+a_(j−1))` | The intercept of the word's affine composition, `x → (3^m x + C_w)/2^A`. |
| `x_0 = C_w / D_w` | The word's rational cycle point, a positive rational cycle of `3x+1`. |
| `den(w) = D_w / gcd(C_w, D_w)` | The reduced denominator. `w` is an integer cycle of `3x+d` iff `den(w)` divides `d`. **The cycle half of Collatz is the statement `den(w) = 1` only for repetitions of `(2)`.** |
| rotation `h` | The cyclic shift `w^(h) = (a_h, a_(h+1), …)`, with `|h|_m = min(h, m−h)`. |
| `mis(h)`, `s(h)` | Mismatch set `{i : a_i ≠ a_(i+h)}`, and its size. |
| `ρ(w)` | `min` of `s(h)` over nonidentity rotations: the word's rotation distance. |
| `L`, `H` | Minimum and maximum element of the integer cycle. |
| `ℓ' = log₂ L`; `B = log₂(H/L)` | Log-minimum and height. Some notes use the integer dyadic band `H < 2^(B+1)·L` instead; each note says which. |
| `y_p = log₂(n_p/L)` | Log-profile. |
| `δ = A − m·log₂3` | Drift. The Lean files use the natural-log version `A·log 2 − m·log 3`. |
| `V_h` | Total letter variation at the mismatches of `h`. |
| `K(h/m)` | Sum of the partial quotients of `h/m`. |

**Primitive** means the cycle is not a repetition of a shorter cycle. Equivalently, its `m` states are distinct.

## 3. The `3x+d` controls

Any argument about cycles must remain consistent with the **actual** nontrivial cycles of other members of the `3x+d` family. Examples are the cycles of `3x+5`, `3x+7`, `3x+13` and `3x+61`. An argument that would also exclude them is wrong, or it uses a hypothesis they fail; say which.

Shared fixtures:
- `experiments/cycle_spectrum/C001/actual_cycles.json`, an actual-cycle corpus;
- `experiments/phase6/cycle_fixtures.json`.

`reviews/side_lane/s1a_integer_cycle_check.py` enumerates every cycle of `3x+q` for odd `q < 2000` from small seeds.

## 4. Status labels

New work uses the labels of [`AGENTS.md`](../AGENTS.md) §4:
- `formal`
- `proved`
- `written`
- `conditional (inputs: …)`
- `evidence`
- `heuristic`
- `open`
- `refuted`
- `withdrawn`

Older documents used other vocabularies. They map as follows:

| Legacy label (where used) | Read as |
|---|---|
| "written proof", "written theorem" (main lane, C/V/R series) | `written`; `proved` once a review is recorded |
| "finite certificate", "exact finite check" | `evidence`, or `proved` for a finite statement certified exhaustively |
| "candidate" | `open` (conjectured) |
| "refuted-scoped", "rejected mechanism" | `refuted` for the stated mechanism only |
| Side-lane feed: LEAD | a new result with a written argument (`written` or `conditional`) |
| FINDING | `evidence` |
| VERIFIED | a review verdict: numerically re-checked, or Lean receipts refereed |
| REFEREE, CONFIRMED | review verdicts |
| COUNTEREXAMPLE | `refuted` |
| CORRECTION, ACK | review traffic |
| Lean `STATE.md`: verified | `formal` |
| Lean `STATE.md`: partially verified, queued | `open` for the formal part |
| Lean `STATE.md`: replayed | an external input (§5) |
| Phase 6: non-transfer step, calibration, barrier, none | scoped grades of route-map nodes (`experiments/phase6/ROUTE_MAP.md`) |
| Handoff: CORE, FINITE, ANALYTIC CANDIDATE | `written`, `evidence`, `open` |

## 5. External inputs

Results that use these inputs are `conditional` on them. Cite the input by its ID.

| ID | Input | Status here | Where |
|---|---|---|---|
| EXT-1 | `Collatz.gap_all` from `mmusson/collatz`: `2^A ≤ 2^172·m^341·(2^A − 3^m)` whenever `0 < m` and `3^m < 2^A` | Replayed. Their Lean development was built and its axioms checked here, under its own toolchain. The proof is not ours and was not reviewed line by line. | `lean/receipts/mmusson_gap_all.txt`; `lean/STATE.md` row EXT-1 |
| Period bound | Every nontrivial cycle of `3x+1` has more than `1.375·10^11` odd steps. Source: Hercher (J. Integer Sequences 2023), Corollary 29, together with Barina (2025)'s verification of convergence below `2^71` | Published computation; not rerun here, not formal | `experiments/cycle_spectrum/C011/EXCLUSION.md` |
| Minimum bound | Every element of a nontrivial cycle exceeds `2^71`, by Barina (2025)'s verification of convergence below `2^71` | Published computation; not rerun here, not formal | `experiments/cycle_spectrum/C011/EXCLUSION.md`, `S06/` |
| Matveev | Explicit lower bound for linear forms in logarithms | Published; used by C011 and C013. S06 and S11 replace it with EXT-1. | `experiments/cycle_spectrum/C011/EXCLUSION.md` |
| AxiomMath C.1a | `AxiomMath/CollatzPositiveDensity`: positive density of predecessors | Audited: built from source, axioms and statements compared | `lean/audit/README.md`; `experiments/phase6/linear_density_audit/` |
| Classical | Cobham's theorem, Eilenberg's finite-kernel characterisation, Tao (2019), Terras/Everett, Krasikov–Lagarias, Simons–de Weger, Hercher, Knight, Halbeisen–Hungerbühler | Published; cited where used | [`docs/LITERATURE.md`](LITERATURE.md) |

## 6. ID glossary

Several series reuse letters. Always read an ID together with the folder it lives in.

| ID | Meaning | Location |
|---|---|---|
| R1–R94 | Rounds of the packet-currents (convergence) programme | R1–R4 in `experiments/packet_currents/`; R5–R7 in `experiments/current_construction/`; R8–R9 in `experiments/annular_construction/`; R10–R94 in `experiments/residual_progress/`. The numbering is in `experiments/residual_progress/REPORT.md` and `archive/docs/RESULTS.md`. |
| C1–C5 | Negative controls from the independent PR1 lane | `experiments/packet_currents/negative_controls/` |
| C001–C014 | Cycle-spectrum batches by the main lane. C014 is unreviewed work in progress. | `experiments/cycle_spectrum/C0xx/` |
| S1–S13 | Cycle-spectrum results by the side lane. S1 exists only as a feed entry and Lean units. | `experiments/cycle_spectrum/S02/`–`S13/` |
| V001–V009 | Viewpoint batches | `experiments/viewpoints/V0xx/` |
| V1–V14 | Viewpoint cards: candidate languages, not results | `experiments/viewpoints/MAP.md`, `archive/side_lane/VIEWPOINTS.md` |
| P6-000–P6-004 | Phase 6 batches | `experiments/phase6/` |
| S.1, C.1a, … | Phase 6 route-map nodes. **Not** the S- or C-series above. | `experiments/phase6/ROUTE_MAP.md` |
| L1–L5 | Phase 6 literature audits | `experiments/phase6/LITERATURE.md` |
| L1–L6 | Explicit-Tao lemmas. These collide with the audits above. | `experiments/explicit_tao/` |
| D1–D8 | Side-lane direction proposals, all resolved | `archive/side_lane/DIRECTIONS.md` |
| W5, W9 | Pair classes `w ≡ 5 (mod 8)` and `w ≡ 9 (mod 16)` in R37+ | `experiments/residual_progress/` |
| `<result>-<letter>` | A Lean unit formalising part of a result, e.g. `S13-a`, `C004-c` | `lean/STATE.md` |
| EXT-n | External inputs (§5) | `lean/STATE.md` |
| New work | Folders named `<YYYY-MM-DD>-<slug>` | `experiments/<line>/` |

## 7. Receipts

A receipt is the committed output of a script or build: `.json`, `.csv`, `.txt` or `.log`.
- It shows what the script printed or certified at the commit that produced it.
- Receipts are regenerated by their script (`--write-receipt`, or the flag documented in the script) and never edited by hand.
- Receipts and historical notes written before 2026-10-19 may mention pre-restructure paths, such as `sidekick/…`, `experiments/lean_lane/…` or `docs/RESULTS.md`. [`archive/README.md`](../archive/README.md) maps those to the current layout.
