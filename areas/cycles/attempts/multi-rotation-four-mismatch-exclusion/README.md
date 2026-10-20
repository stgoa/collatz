# S10: four mismatches under several rotations at once (a scoped finding)

> **Headline (updated 2026-10-19, after the Lean lane's steer).** In the model, the size method reaches four mismatches and stops there. Using several rotations, both four-mismatch patterns of the aligned single-drop structure are excluded:
> - `v₂ = v₄` by `h` and `2h`;
> - `v₂ ≠ v₄` by `h` through `12h`, with a grid margin of 0.0066m.
>
> But five and six mismatches survive twelve rotations, with margins of +0.002m to +0.015m. So even if every structural gap closed, this method yields at most `ρ ≥ 5`, never a growing `F(m)`. The side lane has therefore **paused** `ρ ≥ 5`, which would be a one-step gain needing a large case analysis, and returned to the real frontier: the height bound or genuine arithmetic.

**Status:** side-lane producer batch S10 (2026-10-19). Model-level evidence plus one discrete counterexample. **No exclusion is claimed.** This note supersedes the 13:44 preliminary numbers, which came from a buggy model (§4).

## 1. Why several rotations

Every rotation `h′` of the same cycle word gives its own witness inequalities on the same profile.
- At the end of every agreeing run of `a_i = a_(i+h′)` we have `max(n_e, n_(e+h′)) > 2·3^t`.
- All the formal lemmas are parametric in `h′`: `witness_gt`, `z_run`, `z_ne_zero` (which needs only `h′ ≢ 0`), and the ceilings. The Lean lane confirmed this.

S8 checked only the rotation `h` with exactly four mismatches. Its words fail the rotation by `2h`, which is still a pure size argument. That is the COUNTEREXAMPLE of 13:44, and it stands (§3).

## 2. The model

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

## 3. Results (after the bug fix)

| configuration | rotations used | result in the model | method |
|---|---|---|---|
| `v₂ = v₄` (includes the S8 family) | `h` | feasible: 179,700 grid points, `h ∈ [0.2575, 0.7425]` | grid, `h` step 0.0025, `p` step 0.005 |
| `v₂ = v₄` | `h, 2h` | **infeasible**: every `h`-feasible point fails `2h` by ≥ 0.0219m; random search best −0.0097m | grid + random search |
| `v₂ ≠ v₄` | `h, 2h` | feasible: 11,162 points, `h ∈ [0.256, 0.744]` | grid |
| `v₂ ≠ v₄` | `h, …, 3h` | feasible, best margin +0.0092m | grid |
| `v₂ ≠ v₄` | `h, …, 8h` | feasible, best margin +0.0002m (`h = 0.364`, `p₁ = 0.418`, `p₂ = 0.138`) | random search |
| all four arcs long, no cancellations | `h, …, 4h` | feasible, best +0.013m | random search |

**Discrete check of the S8 words** (`s8_multiple_rotations.py`). At `m = 10^6`, the rotation by `2h` fails by 193,000, 209,000 and 287,000 bits at `ℓ = ℓ*`, 71 and 100. Rotations `3h`, `4h`, `5h`, `7h` and `9h` fail too.

## 4. The bug, and what was retracted

- **The bug.** The first version placed `X − kh` at `1 − kh`, while `X` was `1 − 10⁻⁹`. So the `kh`-partner of the run ending at `X − kh` could wrap to the minimum (height 0) instead of landing on `X` (the maximum). That made constraints spuriously hard.
- **Retracted.** The preliminary "0 feasible points" for `v₂ ≠ v₄` with `h + 2h` and with `h + 2h + 3h`, and the margin −0.0089m. They were sent to the Lean lane and recorded there as preliminary.
- **Unaffected.** The `v₂ = v₄` conclusion and the discrete S8 counterexample.

## 5. Reading

- **The cheapest four-mismatch pattern is excluded by the rotations `h` and `2h` together.** That pattern is `v₂ = v₄`: apart from `V`, only ones and one arc of 2s, which is what a tall cycle's low excess budget favours. This is model-level for general parameters and discrete for the S8 words.
- **The pattern `v₂ ≠ v₄` survives `h, …, 8h` in the model.** Its margins shrink towards zero (+0.0002m at `8h`). The model is generous to it in two ways:
  - It keeps the full slope `log₂(3/2)`. But `v₂ ≠ v₄` with low excess forces a letter `≥ 3` in the middle arc, or a short arc, which lowers the slope or changes the mismatch sets.
  - It ignores short-arc effects.

  Its exact status is open.
- **Generic long-arc configurations survive `h, …, 4h` in the model.** They are consistent with a tall profile only when `|h|_m < d`, since a long arc of big letters needs two big letters `h` apart inside the descent window. That small-rotation branch is outside S7's structure.
  - The Lean lane notes that `window_conditions` forces the two located changes into an arc shorter than `2d` there, so the spacing bound cannot hold.
  - For `s = 4` the spacing bound is a model assumption, not a theorem.
- **Net.** `ρ ≥ 5` via size inequalities alone is neither established nor refuted. S8's headline stays withdrawn: its words are excluded.

## 6. What a theorem would need (with the Lean lane's review points)

- **(a) Exact certificates.** Within a cell (fixed cyclic order, witness choices and wraps), every constraint is linear in `(h, p₁, p₂)`. Infeasible cells then have Farkas certificates: rational multipliers checkable by `linarith`. These should replace grids.
- **(b) Finite `m`.** The `ℓ` terms must be compared with the margins: `0.0219m` vs `ℓ* ≈ 342 log₂ m + 172`. This gives a threshold `m₀`.
- **(c) The `s = 4` dichotomy.** Either one `+ → −` change, one `− → +` change and two non-change mismatches (the single-drop model is this case), or two of each. The Lean lane will formalise this. The other case and the small-rotation branch need their own analysis, since the alignment transfer does not apply unchanged.
- **(d) The `v₂ ≠ v₄` pattern** with the slope cost of its letters `≥ 3` and short arcs included.

## Reproduce

```sh
python3 reviews/side_lane/s10_multirotation_lp.py --fine   # ~4 min, grid scans (fixed model)
python3 reviews/side_lane/s8_multiple_rotations.py          # ~35 s, the discrete S8 counterexample
```
