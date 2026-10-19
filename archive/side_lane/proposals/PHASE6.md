# Phase 6 proposal: from local rules to non-transferable statements

*The side lane drafted this proposal on 2026-10-18 for the user. The user decides whether to apply it. It is not a feed entry and it is not an instruction to `main`. The texts in §4 and §5 are ready to paste.*

## 0. Verdict

R1–R94 have done their job. The conjecture is now pinned to one family of pair obligations, `u ↔ 18u + 5`, and one strict-rank induction. Completing that induction is equivalent to a uniform stopping-time statement for the critical images, which is equivalent to Collatz itself.

Every local identity the programme uses transfers to `3x + d`, so more local rules cannot close the gap. The next phase should aim only at statements that use what `3x + d` lacks: positivity, integrality of whole words, and archimedean size combined with 2-adic structure.

Gemini's blueprint points at the right interface. Several of its specific rules and lemmas need correcting before they go into `AGENTS.md`; §1 gives the corrections.

## 1. Review of the Gemini blueprint

| Gemini item | Keep / fix | Why |
|---|---|---|
| Ban fixed-denominator rules | **Fix**: freeze the 17-family dispatcher and stop counting congruence-class results as progress. Do not ban congruences. | Every arithmetic lemma uses residue classes. The problem is the goal, not the tool. |
| Non-transfer gate: every lemma must hold for `d = 1` and fail for `d ∈ {5, 7, 13, 61}` | **Fix**: apply the gate to *progress mechanisms* (potentials, ranks, termination tests, claimed closures), not to every lemma. | Most true lemmas transfer; they are legitimate building blocks. The gate is the right test for anything claimed to make progress. It has one limitation: controls can only exhibit cycles, because no divergent `3x + d` orbit is known. |
| Universal shadow mandate (all expanding words `W` at once, `c_W` symbolic) | **Keep** | The side lane already has the uniform statement: expanding cycle points are dense in `Z₂`. |
| Bit budget: `v2(x − c_W) ≤ log₂(D_W x + B_W)` | **Keep, but it is elementary**, and its stated consequence is wrong | See §1.1. One episode can raise the height polynomially, so the budget grows with the height instead of burning down. |
| Shadow hand-off lemma via the ultrametric triangle inequality | **Drop as stated** | The hand-off is evaluated at the wrong state. The equality needs unequal valuations. Expanding cycle points are dense, so high agreement with *some* next shadow is automatic: the periodic extension of the orbit's own next steps always provides one. The content lies in the costs, which is the problem itself. |
| Extend R71 to W5 words with Baker-type bounds | **Keep**, with a literature check first | Steiner, Simons–de Weger (`m`-cycles, `m ≤ 68`) and Hercher (`m ≤ 91`) cover part of this ground. |
| Berg–Meinardus / harmonic duality | **Keep as an exploratory track** under strict claim discipline | The duality is genuine; R7 is its finite form. Analytic "proofs" by this route have failed before (Opfer 2011). |

### 1.1 The correct bit-budget statement

Let `W` be an expanding periodic valuation word with `k` arrows and cost `m`, so `3^k > 2^m`. Its cycle point is `c_W = −B_W/D_W` with `D_W = 3^k − 2^m`.

A positive odd `x` follows `W` for at most `r ≤ v2(D_W x + B_W)/m ≤ log₂(D_W x + B_W)/m` full periods. Over those periods,

`x_r − c_W = (3^k/2^m)^r (x − c_W)`, so the growth factor is at most `(D_W x + B_W)^λ` with `λ = (k·log₂3 − m)/m`.

For example, the all-ones word (`c_W = −1`) sends `x = 2^a − 1` to `2·3^(a−1) − 1` in `a − 1` steps, which is about `x^1.585`. So one shadow episode can raise the height polynomially, and the budget is refilled by growth. The non-transferable ingredient is the sign: `x > 0 > c_W`. The open question is what forces contraction *between* episodes, and that is the stopping-time problem again.

## 2. The pivot in one rule

The ultimate goal is unchanged: prove Collatz, or produce verified mathematics that genuinely narrows it. What changes is what counts as a batch outcome. Each batch must end with at least one of the following.

- **(a) A non-transferable lemma.** This is a written proof with a *named step* that fails for some `d ∈ {5, 7, 13, 61}`. The `d`-control harness must show that failure on a known `3x + d` cycle.
- **(b) A calibration theorem.** This is a published result re-derived inside the framework, with explicit constants: for example Terras or Everett density one, Tao's almost-bounded values, Krasikov–Lagarias predecessor counts, or Simons–de Weger. It shows the framework reaches the known frontier.
- **(c) A barrier theorem.** This proves that a named class of arguments cannot work, because the argument applies verbatim to a `3x + d` map with a known cycle.

**Kill rule.** If a track produces none of (a), (b) or (c) in three consecutive batches, write a one-page post-mortem and switch tracks.

## 3. Tracks

- **Track A — episodes and bit budgets** (`experiments/adelic_shadows/`).
  - Define the episode decomposition of an orbit into maximal expanding-shadow segments, recording each segment's cost and agreement.
  - Prove §1.1 exactly, including the sign argument, with the control that it fails for positive cycle points (`3x + 61`).
  - Calibrate by re-deriving the density-one stopping-time theorem for the critical images `ν(3w)` with the `8/9` threshold.
  - Only then attack between-episode contraction.
- **Track B — whole-word integrality** (`experiments/word_integrality/`).
  - Define `ν`-canonical words: words that avoid the R25 bridges and the selected climbers.
  - Characterize when `2^m − 3^k` divides `B_W` for them, extending R71.
  - Use Baker/Matveev bounds plus computation.
  - The control must recover the actual cycles of `3x + d` and must not exclude them. For example: `d = 5` with cycle minima 1, 19, 23, 187, 347; `d = 7` with 5; `d = 13` with 1, 131, 211, …; `d = 61` with 1 and 235.
  - Do the literature comparison (Steiner, Simons–de Weger, Hercher, Eliahou) before any novelty claim.
- **Track C — harmonic duality** (`experiments/harmonic_duality/`).
  - Derive the exact functional equation satisfied by invariant functionals of `T = ν∘S` and of the W5 pair relation.
  - Check it with truncated power series.
  - Relate it to Berg–Meinardus and Bell–Lagarias.
  - The deliverables are derivations and numerics, not a proof claim.
- **Track D — the original counting thesis** (`experiments/exponent_gap/`), the side lane's addition.
  - The master handoff's first route was global and non-transferable by design. Few slow orbits on average, plus Krasikov–Lagarias (any `a ≢ 0 (mod 3)` has at least `x^0.84` predecessors up to `x`), would force there to be no exception. For `3x + d` with extra cycles, a positive density of orbits ends in other cycles (all multiples of `d` already do), so the premise fails there, as it should.
  - The currents machinery was built for this route. The side lane's Q1 measurement shows that the unabsorbed share of `A_N` at a fixed exposure depth is essentially independent of `N`.
  - **Concrete target:** prove a rate for that share that is uniform in `N`. Then determine what power saving at depth `c·log N` would be needed to beat the exponent 0.84, and check how the basin of a hypothetical non-convergent orbit would appear in `A_N`'s signed mass.
- **Cross-cutting — the `d`-control harness** (`scripts/verify_all.py --transfer-controls`).
  - Every registered progress mechanism exposes a `d`-parametrized version.
  - The harness runs it on known cycle minima of `3x + d` for `d ∈ {5, 7, 13, 61}`.
  - It must report the mechanism's failure there, at a named step. A mechanism that "succeeds" on a cycle is rejected.

## 4. Concrete repository changes (paste-ready)

### 4.1 `AGENTS.md`: insert after "Start from the repository"

```markdown
## Current phase (Phase 6, from 2026-10-18)

- R1–R94 are frozen infrastructure. The seventeen-family W5 dispatcher, its resolvers and the
  history catalogues are not extended as goals in themselves. New rule families, CRT
  subfamilies, single-denominator certificates and acceptance counts count as progress only
  when they are a necessary step of an outcome below.
- Every batch ends with at least one of: (a) a non-transferable lemma, a written proof with a
  named step that fails for some d in {5,7,13,61} as shown by the d-control harness on a
  known 3x+d cycle; (b) a calibration theorem, a published result re-derived in the framework
  with explicit constants; (c) a barrier theorem proving that a named class of arguments
  cannot work because it applies verbatim to a 3x+d map with a known cycle.
- Every claimed progress mechanism (potential, rank, termination test or closure) must state
  its transfer status, which step uses positivity, integrality or size, and must be
  registered with `scripts/verify_all.py --transfer-controls`. Controls can exhibit cycles
  only; no divergent 3x+d orbit is known, so passing them does not validate the divergence
  half.
- Work in one track per batch: A episodes and bit budgets (`experiments/adelic_shadows/`),
  B whole-word integrality (`experiments/word_integrality/`), C harmonic duality
  (`experiments/harmonic_duality/`), D exponent-gap counting (`experiments/exponent_gap/`).
  Number new results R95+ with the track letter, for example "R95 [B]".
- Before asserting novelty, record the closest published result (Terras, Everett, Lagarias,
  Krasikov–Lagarias, Steiner, Simons–de Weger, Hercher, Eliahou, Berg–Meinardus,
  Bell–Lagarias, Tao). Shadowing an expanding cycle point is automatic (such points are dense
  in Z_2); results about shadows must carry costs and agreements, not bare existence.
- Kill rule: if a track produces none of (a)–(c) in three consecutive batches, write a
  one-page post-mortem in the track directory and switch tracks.
```

Also retitle "Latest mathematical interfaces" to "Mathematical interfaces through R94 (frozen infrastructure)". Leave its content unchanged.

### 4.2 `README.md`: replace "What would count as the next breakthrough"

```markdown
## What would count as the next breakthrough

The local programme (R1–R94) reduced Collatz to one family of pair obligations and a
strict-rank induction whose completion is equivalent to a uniform stopping-time statement for
the critical images. Every local identity used transfers to 3x+d, so further local rules
cannot close it. Phase 6 therefore accepts only statements that use what 3x+d lacks:
positivity, whole-word integrality, or archimedean size together with 2-adic structure.
A breakthrough is a non-transferable lemma that closes a step of tracks A–D, a calibration
theorem showing the framework reaches the published frontier, or a barrier theorem that
retires a class of arguments. See AGENTS.md, "Current phase".
```

### 4.3 New `experiments/phase6/REPORT.md` skeleton

```markdown
# Phase 6: non-transferable statements

## Objective and completion standard
Prove Collatz, or verified statements that use positivity, whole-word integrality or size.
Completion requires a valid proof; each batch must produce outcome (a), (b) or (c).

## Falsifiable directions
1. A: the episode decomposition yields a calibration of density-one stopping time for the
   critical images, then a between-episode contraction lemma with a named non-transferable step.
2. B: nu-canonical words admit a divisibility obstruction to (2^m-3^k) | B_W beyond R71 that
   recovers, and does not exclude, the known 3x+d cycles.
3. C: invariant functionals of T = nu S satisfy an explicit functional equation consistent
   with truncated numerics.
4. D: the unabsorbed share of A_N decays at a rate uniform in N; quantify the power saving
   needed against the Krasikov–Lagarias exponent.

## Checklist
- [ ] Build the d-control harness and register the existing progress measures.
- [ ] Track brief and literature comparison for the chosen track.
- [ ] Outcome (a), (b) or (c), verified and persisted.
```

### 4.4 Other files

- **`archive/docs/RESULTS.md`:** add one header line saying that R1–R94 are frozen infrastructure and that new results carry track letters.
- **`experiments/residual_progress/REPORT.md`:** close Phase 5 with a three-line summary pointing to Phase 6.
- **Side lane:** it moves from verification toward track briefs, transfer audits and literature scouting. The feed conventions stay as they are.

## 5. Goal text for ChatGPT (paste-ready)

> **Goal (Phase 6, from 18 Oct 2026).** Prove the Collatz conjecture, or produce verified
> mathematics that genuinely narrows it. Results R1–R94 are frozen infrastructure: the W5 reduction
> (R40), the critical rank (R43), the normal form ν (R25), R71 and the rational-cycle shadow
> picture. Do not add rule families, CRT subfamilies or single-denominator certificates as goals in
> themselves; the seventeen-family dispatcher is frozen.
>
> Why: every local identity used so far transfers to 3x+d (gcd(d,6)=1), and the remaining gap is
> equivalent to a uniform stopping-time statement for the critical images. A proof must use
> something 3x+d does not share: positivity, integrality of whole words, or archimedean size together
> with 2-adic structure.
>
> Work in one track per batch: A episodes and bit budgets (stopping time); B whole-word integrality
> (cycles, extending R71 with Baker-type bounds); C harmonic duality (functional equations for
> invariant functionals of T = ν∘S and the W5 pairs); D the exponent-gap counting route of the master
> handoff (few slow orbits plus Krasikov–Lagarias basins).
>
> Every batch must end with at least one of: (a) a non-transferable lemma, a written proof with a
> named step that fails for some d in {5, 7, 13, 61}, shown by the d-control harness on a known 3x+d
> cycle; (b) a calibration theorem, a published result re-derived in the framework with explicit
> constants; (c) a barrier theorem, a proof that a named class of arguments cannot work because it
> applies equally to a 3x+d map with a known cycle.
>
> Before claiming novelty, record the closest published result. If a track produces none of (a)–(c)
> in three consecutive batches, write a one-page post-mortem and switch tracks. Claim discipline,
> verification and Git rules in AGENTS.md are unchanged.
