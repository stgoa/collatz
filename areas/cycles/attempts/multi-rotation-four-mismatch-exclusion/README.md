---
id: multi-rotation-four-mismatch-exclusion
kind: attempt
title: Excluding four-mismatch rotations with the size inequalities of several rotations at once (paused)
status: reviewed
claim: >
  Tried, toward ρ ≥ 5 for hypothetical nontrivial cycles of the raw odd-only 3x+1 map: impose the
  end-witness size inequalities of the rotations h, 2h, …, kh of the same word at once, in a continuous
  model of S7's aligned single-drop structure (one huge letter at the top, slope log₂(3/2), ℓ/m → 0).
  Model-level findings, no exclusion claimed: the four-mismatch pattern v₂ = v₄ (which contains S8's words)
  is infeasible under h and 2h together (grid margin ≤ −0.0219m), and S8's discrete words fail 2h by about
  2·10^5 bits at m = 10^6; the pattern v₂ ≠ v₄ survives h, …, 8h but fails by 11h (grid margin ≤ −0.0066m
  over 3h..12h). Five and six mismatches survive twelve rotations in the same model (margins +0.002m to
  +0.015m), so even if every structural gap closed the method yields at most ρ ≥ 5, never a growing F(m).
  Paused by its authors; ρ ≥ 5 is neither established nor refuted.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [three-mismatch-exclusion, four-mismatch-sign-dichotomy]
evidence:
  - "s10_multirotation_lp.py, s10_multirotation_lp.json: side-lane exploration probe, the continuous witness LP (coarse grid by default, --fine adds the refinement; the receipt records the configuration). At migration it exited 0 at its new path in its default (coarse) mode (about 3 min) and left its receipt byte-identical; it is an exploration probe of the model, not a checker. Passed at be73a66 as reviews/side_lane/s10_multirotation_lp.py (archive/legacy-checker-run-be73a66.md)"
  - "s10_v2nev4_twelve_rotations.py: exploration probe (about 10 min, prints only): the v₂ ≠ v₄ grid against rotations up to 12h. Imports s10_multirotation_lp from this folder; exits 0 at its new path (coarse 8,940 points, best −0.0083; finer 90,512 points, best −0.0066, re-run at migration). Passed at be73a66 as reviews/side_lane/s10_v2nev4_twelve_rotations.py"
  - "s10_v2nev4_killers.py: exploration probe (about 1 min, prints only): the v₂ ≠ v₄ grid with h offset off rationals, and the rotation that kills each point. Imports s10_multirotation_lp from this folder; exits 0 at its new path (same histogram as below, re-run at migration). Passed at be73a66 as reviews/side_lane/s10_v2nev4_killers.py"
  - "s10_more_mismatches.py: exploration probe (about 5 min, prints only): single-chain s-mismatch models (s = 4, 5, 6) against rotations up to 12h. Exits 0 at its new path (re-run at migration). Passed at be73a66 as reviews/side_lane/s10_more_mismatches.py"
  - "s10_v2nev4_discrete.py: exploration probe (about 35 s, prints only): discrete words [V][1^a][3^b][2^c] at the model optima against rotations up to 12h. Fails at its new path: it imports s8_multirotation_check from its own folder (now in ../four-mismatch-size-method-limit/); with that folder on PYTHONPATH it exits 0 (checked at migration). Passed at be73a66 as reviews/side_lane/s10_v2nev4_discrete.py (archive/legacy-checker-run-be73a66.md)"
  - "The discrete S8 counterexample (rotation 2h) is ../four-mismatch-size-method-limit/s8_multiple_rotations.py"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Model definitions and the end-witness constraint re-derived; the v2 = v4 exclusion under h and 2h re-derived by hand in S8's configuration and confirmed by exact per-cell linear programmes (supremum of the margin -0.0097m); all five probes and the S8 counterexample re-run with matching numbers; s = 5, 6 survivors confirmed; verdict HOLDS (imprecisions recorded in History)"
aliases: [S10]
tags: [cycles, rotation-distance, size-method, paused]
---

# Excluding four-mismatch rotations with the size inequalities of several rotations at once (paused)

> **Headline (legacy note, updated 2026-10-19 after the Lean lane's steer).** In the model, the size method reaches four mismatches and stops there. Using several rotations, both four-mismatch patterns of the aligned single-drop structure are excluded: `v₂ = v₄` by `h` and `2h`; `v₂ ≠ v₄` by `h` through `12h`, with a grid margin of `0.0066m`. But five and six mismatches survive twelve rotations, with margins of `+0.002m` to `+0.015m`. So even if every structural gap closed, this method yields at most `ρ ≥ 5`, never a growing `F(m)`. The side lane therefore **paused** `ρ ≥ 5`, which would be a one-step gain needing a large case analysis, and returned to the real frontier: the height bound or genuine arithmetic.

## Idea

Legacy note `MULTI_ROTATION.md` (S10, side lane). Its status line read: "Model-level evidence plus one discrete counterexample. **No exclusion is claimed.** This note supersedes the 13:44 preliminary numbers, which came from a buggy model (§4)."

### 1. Why several rotations

Every rotation `h′` of the same cycle word gives its own witness inequalities on the same profile.
- At the end of every agreeing run of `a_i = a_(i+h′)` we have `max(n_e, n_(e+h′)) > 2·3^t` ([`paired-state-run-law`](../../results/paired-state-run-law.md)).
- All the formal lemmas are parametric in `h′`: `witness_gt`, `z_run`, `z_ne_zero` (which needs only `h′ ≢ 0`), and the ceilings. The Lean lane confirmed this.

S8 ([`four-mismatch-size-method-limit`](../four-mismatch-size-method-limit/README.md)) checked only the rotation `h` with exactly four mismatches. Its words fail the rotation by `2h`, which is still a pure size argument. That is the COUNTEREXAMPLE of 13:44, and it stands (§3).

### 2. The model

**Geometry.** Positions are scaled to `[0, 1)`, with the minimum at 0.
- The single huge letter `V` (the maximum) sits at `X = 1⁻`.
- The aligned pair of sign-change mismatches is `X − h`, `X`. The inner mismatches are `P₁`, `P₂`.
- The chain arcs are `[V][v₂…][v₃…][v₄…]`, with every arc longer than `k`.

**Mismatch sets.** The rotation by `kh` is a chain shift by `k`. Its mismatches are `X`, `X − kh`, and `P₁ − ih`, `P₂ − ih` for `i < k`. When the two arcs beside `V` differ (`v₂ ≠ v₄`), it also has `X − ih` for `1 ≤ i < k`.

**Envelope and constraint.** The envelope is `y(p) = σp` with `σ = log₂(3/2)` (the most favourable slope), and `ℓ/m → 0`. For every run of every rotation:

```
t ≤ (σ/log₂3) · max(pos(e), pos(e + kh)).
```

The witness bound needs no sign information, because the larger state is at most the larger envelope value.

## What happened

### 3. Results (after the bug fix)

| configuration | rotations used | result in the model | method |
|---|---|---|---|
| `v₂ = v₄` (includes the S8 family) | `h` | feasible: 179,700 grid points, `h ∈ [0.2575, 0.7425]` | grid, `h` step 0.0025, `p` step 0.005 |
| `v₂ = v₄` | `h, 2h` | **infeasible**: every `h`-feasible point fails `2h` by ≥ 0.0219m; random search best −0.0097m | grid + random search |
| `v₂ ≠ v₄` | `h, 2h` | feasible: 11,162 points, `h ∈ [0.256, 0.744]` | grid |
| `v₂ ≠ v₄` | `h, …, 3h` | feasible, best margin +0.0092m | grid |
| `v₂ ≠ v₄` | `h, …, 8h` | feasible, best margin +0.0002m (`h = 0.364`, `p₁ = 0.418`, `p₂ = 0.138`) | random search |
| all four arcs long, no cancellations | `h, …, 4h` | feasible, best +0.013m | random search |

**Discrete check of the S8 words** (`s8_multiple_rotations.py`, in [`four-mismatch-size-method-limit`](../four-mismatch-size-method-limit/README.md)). At `m = 10^6`, the rotation by `2h` fails by 193,000, 209,000 and 287,000 bits at `ℓ = ℓ*`, 71 and 100. Rotations `3h`, `4h`, `5h`, `7h` and `9h` fail too.

**Later updates (feed S10 entry, 14:36–14:46).**
- **The `v₂ ≠ v₄` survivor dies at `11h`** (still model-level). The best point at `h, …, 8h` (+0.0002m) survives through `10h` and fails at `11h`. Random search over `h, …, 12h` peaks at −0.0058m. On the grid, every one of the 90,512 points feasible for `h` and `2h` (`h` step 0.001, `p` step 0.0025) fails some rotation from `3h` to `12h`, by at least 0.0066m; the coarse grid gives 8,940 points and −0.0083m (`s10_v2nev4_twelve_rotations.py`).
- **The discrete words die too.** Words `[V][1^a][3^b][2^c]` at the model optima, with `m = 10^6`, fail the rotation by `7h` or `11h` by 20,000–42,000 bits, at `ℓ = ℓ*`, 1,000 and 200 (`s10_v2nev4_discrete.py`).
- **Trivial rotations (the Lean lane's review point).** A rotation `kh ≡ 0` is vacuous. With `h` offset by `1.2·10⁻⁷` off exact fractions, no `k ≤ 12` has `kh` within `10⁻⁶` of an integer, and the result is unchanged: 8,940 points feasible for `h` and `2h`, all failing some rotation from `3h` to `12h`, best −0.0083m. The killing rotation is `3h` for 7,894 points, `4h` for 224, `5h` for 104, `7h` for 8, `8h` for 210, and `11h` for 500 (`s10_v2nev4_killers.py`).
- **The reach of the method.** Same single-chain model with a singleton `V`, random search against rotations up to `12h` (`s10_more_mismatches.py`): `s = 4` is excluded (−0.0317m when `v_s = v₂`, −0.0061m when `v_s ≠ v₂`); `s = 5` survives (+0.0021m, +0.0109m); `s = 6` survives (+0.0137m, +0.0152m). So even in the model, the method's best possible output is `ρ ≥ 5`.
- **Finite `m` (the Lean lane's computation).** Solving `0.0066m = 342·log₂ m + 172` gives `m ≈ 1.1·10^6`; a formal threshold would be `2^21` if a cell's margin is uniform.

### 4. The bug, and what was retracted

- **The bug.** The first version placed `X − kh` at `1 − kh`, while `X` was `1 − 10⁻⁹`. So the `kh`-partner of the run ending at `X − kh` could wrap to the minimum (height 0) instead of landing on `X` (the maximum). That made constraints spuriously hard.
- **Retracted.** The preliminary "0 feasible points" for `v₂ ≠ v₄` with `h + 2h` and with `h + 2h + 3h`, and the margin −0.0089m. They were sent to the Lean lane and recorded there as preliminary.
- **Unaffected.** The `v₂ = v₄` conclusion and the discrete S8 counterexample.

## Why it fails

### 5. Reading

- **The cheapest four-mismatch pattern is excluded by the rotations `h` and `2h` together.** That pattern is `v₂ = v₄`: apart from `V`, only ones and one arc of 2s, which is what a tall cycle's low excess budget favours. This is model-level for general parameters and discrete for the S8 words.
- **The pattern `v₂ ≠ v₄`** survives `h, …, 8h` in the model with margins shrinking towards zero, and dies by `11h` (above). The model is generous to it in two ways: it keeps the full slope `log₂(3/2)`, although `v₂ ≠ v₄` with low excess forces a letter `≥ 3` in the middle arc, or a short arc, which lowers the slope or changes the mismatch sets; and it ignores short-arc effects.
- **Generic long-arc configurations survive `h, …, 4h` in the model.** They are consistent with a tall profile only when `|h|_m < d`, since a long arc of big letters needs two big letters `h` apart inside the descent window. That small-rotation branch is outside S7's structure. The Lean lane notes that `window_conditions` forces the two located changes into an arc shorter than `2d` there, so the spacing bound cannot hold. For `s = 4` the spacing bound is a model assumption, not a theorem.
- **Net.** `ρ ≥ 5` via size inequalities alone is neither established nor refuted. S8's headline stays withdrawn: its words are excluded.
- **Why the line was paused (feed 14:46).** Finishing `ρ ≥ 5` would need the `(1, 1, 2)` window theorem, the 2–2 case, the small-rotation branch, short arcs, certificates and `m ≥ 2^21`, all for one step that cannot be extended: five and six mismatches survive the same model.

## What survives

### 6. What a theorem would need (with the Lean lane's review points)

- **(a) Exact certificates.** Within a cell (fixed cyclic order, witness choices and wraps), every constraint is linear in `(h, p₁, p₂)`. Infeasible cells then have Farkas certificates: rational multipliers checkable by `linarith`. These should replace grids. The Lean lane's refinement: per region, find one rotation `k` with a uniform failure margin, so each cell's certificate involves only that rotation's constraints.
- **(b) Finite `m`.** The `ℓ` terms must be compared with the margins: `0.0219m` against `ℓ* ≈ 342·log₂ m + 172`. This gives a threshold `m₀`.
- **(c) The `s = 4` dichotomy.** Either one `+ → −` change, one `− → +` change and two non-change mismatches (the single-drop model is this case), or two of each. This is now formal: [`four-mismatch-sign-dichotomy`](../../results/four-mismatch-sign-dichotomy.md). The other case and the small-rotation branch need their own analysis, since the alignment transfer does not apply unchanged.
- **(d) The `v₂ ≠ v₄` pattern** with the slope cost of its letters `≥ 3` and short arcs included.

Later results narrowed the open configurations: a four-mismatch rotation needs `|h|_m ≥ 0.075m` ([`short-rotation-mismatch-growth`](../../results/short-rotation-mismatch-growth/README.md)) and forces a letter of size `≥ 0.0220m` ([`largest-letter-rho-reduction`](../../results/largest-letter-rho-reduction.md)), both conditional on EXT-1. The target itself is [`rotation-distance-at-least-5`](../../questions/rotation-distance-at-least-5.md); the growing target is [`rotation-distance-growth`](../../questions/rotation-distance-growth.md).

## History

- Migrated from `experiments/cycle_spectrum/S10/MULTI_ROTATION.md` (legacy ID `S10`; side-lane producer batch S10, 2026-10-19) at commit `be73a66`, by the B06 migration (Claude, Opus 5.5). The side-lane probes `reviews/side_lane/s10_multirotation_lp.{py,json}`, `s10_more_mismatches.py`, `s10_v2nev4_discrete.py`, `s10_v2nev4_killers.py` and `s10_v2nev4_twelve_rotations.py` moved here. The note's "Reproduce" block pointed to the old paths. The later updates in "What happened" are from the feed entry, not the note.
- Side lane (Claude, Opus), feed 2026-10-19 14:09 (FINDING, S10). **Retraction (14:09):** the preliminary S10 numbers sent to the Lean lane at 13:5x came from the buggy model (§4). Update 14:36: the `v₂ ≠ v₄` pattern dies by `11h`; Lean S10-a verified. Update 14:42: the reach of the method, and the Lean lane's review points (trivial rotations, finite `m`, certificates). Update 14:46: headline revised after the Lean lane's steer; `ρ ≥ 5` paused.
- The Lean lane's review points are on record (feed 14:36–14:46); no independent verdict on the model's conclusions is, so the status is `written`.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No text changed. Recorded: the uniform margin of the `v₂ = v₄` exclusion under `h` and `2h` is the continuous supremum `0.0097m` (exact per-cell linear programmes; the random search's `−0.0097`), not the coarse-grid `0.0219m` used in §6 (b), so the finite-`m` threshold there is about `7.0·10^5` rather than `2.9·10^5`; the single-rotation range `[0.2575, 0.7425]` is the hull of three windows with gaps `(0.369, 0.398)` and `(0.602, 0.631)`; at `ℓ = ℓ*` only `2h`, `3h`, `5h` fail on the S8 words (`4h`, `7h`, `9h` fail at `ℓ = 71, 100`); the discrete words fail by 20,261 to 42,780 bits; the symbol `d` in §5 is undefined; "at most `ρ ≥ 5`" is a model-level inference (no discrete `s = 5` word was exhibited). Review: [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
