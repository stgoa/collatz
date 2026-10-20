---
id: four-mismatch-size-method-limit
kind: attempt
title: Excluding four-mismatch rotations by S7's size inequalities alone (headline withdrawn)
status: withdrawn
withdrawn_reason: >
  The exhibited four-mismatch words, offered as proof that size arguments stop at three mismatches, fail the
  witness inequalities of the rotation by 2h (six mismatches) by about 2·10^5 bits at m = 10^6; only the
  narrow statement that the single-rotation relaxation is feasible survives.
claim: >
  Tried, toward ρ ≥ 5 for hypothetical nontrivial cycles of the raw odd-only 3x+1 map: determine whether
  S7's size inequalities (end and start witnesses, sign structure, excess-tracked ceiling, plus a new
  comparison with the fixed point −1) can exclude rotations with exactly four mismatches. The S8 note
  claimed a negative map: explicit words [V][1^a][2^b][1^c] along one h-chain, above S7's threshold
  (m = 10^6 and 4·10^6), satisfy every such inequality of the rotation h for every ℓ = log₂ L from 71 to
  ℓ*, so "ρ ≥ 4 is the limit of size arguments". Withdrawn by its authors the same day: the words fail the
  inequalities of the rotation by 2h. What survives is only that the single-rotation relaxation is
  feasible; whether size constraints over all rotations exclude four mismatches is open.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [three-mismatch-exclusion, ones-run-divisibility]
certificates: [check_legacy_replay.py]
evidence:
  - "s8_four_mismatch_map.py, s8_four_mismatch_map.json: side-lane exploration probe (about 10-20 s): builds the words and evaluates constraints (1)-(5) of the rotation h exactly, with the margins tabulated in the note. Exits 0 at the new path and rewrites its receipt byte for byte; it is an exploration probe, not a checker. Passed at be73a66 as reviews/side_lane/s8_four_mismatch_map.py (archive/legacy-checker-run-be73a66.md)"
  - "s8_multirotation_check.py: side-lane probe (about 20 s, no receipt), feed update 13:36: the survivor words against every rotation by a convergent denominator of h^(−1)/m (times 1, 2, 3) with at most 60,000 mismatches; all margins positive. It did not include the rotation 2h. Exits 0 at the new path (imports s8_four_mismatch_map from this folder). Passed at be73a66 as reviews/side_lane/s8_multirotation_check.py. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "s8_multiple_rotations.py: the counterexample check of feed 13:44 (about 30-40 s, no receipt): the survivor words against the rotations by k·h, k = ±1..±12; the rotation 2h fails by 193,000 bits (ℓ = ℓ*), 209,000 (ℓ = 71) and 287,000 (ℓ = 100) at m = 10^6, and 3h, 4h, 5h, 7h, 9h fail too. Exits 0 at the new path (min margin −209,428.5 and −286,512.6 at ℓ = 71 and 100, re-run at migration). Passed at be73a66 as reviews/side_lane/s8_multiple_rotations.py. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed update 13:17: reviewed S8; the words, constraint (5) and the 1-cycle by-product check out; scoped the claim to a relaxation-feasibility statement for the single rotation h. The lane later recorded (legacy lean/STATE.md, iteration 73) that its review did not raise other rotations of the same word, a gap in that review; the side lane found the failing rotation 2h itself"
    link: ../../../../archive/lean-lane/STATE.md
aliases: [S08]
tags: [cycles, rotation-distance, size-method, withdrawn]
---

# Excluding four-mismatch rotations by S7's size inequalities alone (headline withdrawn)

> **Withdrawn 2026-10-19 13:44 (legacy note's banner, kept).** The exhibited words fail the witness inequalities of the rotation by `2h` (6 mismatches), by about `2·10^5` bits at `m = 10^6`. Only the narrow statement survives: the single-rotation relaxation is feasible. Whether all size constraints together exclude four mismatches is open (S10, [`multi-rotation-four-mismatch-exclusion`](../multi-rotation-four-mismatch-exclusion/README.md)). The text below is kept as written.

## Idea

Legacy note `FOUR_MISMATCH_MAP.md` (S8, side lane), status line and precise claim as written:

**Status:** side-lane producer batch S8 (2026-10-19). A negative map backed by explicit words. It excludes nothing. It records exactly where S7's mechanism is exhausted, as the brief asks ("stop expanding an elimination method when its exact obstruction is known").

**Precise claim.** Write (1)–(5) for the inequalities below, with every state replaced by the envelope `y_k`, the maximal admissible profile.
- That relaxed system is jointly satisfiable by explicit four-mismatch words above S7's threshold, for every `ℓ` from 71 to `ℓ*`. So no argument that uses (1)–(5) only through these size inequalities can exclude `s = 4`.
- This is a feasibility statement about the relaxation, in the same sense as C012's "precise failure of this elimination". An argument that also uses the integrality of the witness integers, the exact cycle equation `n_0 D = C_w`, or the mod-`D` relation is outside its scope (§4).
- **Which S7 step fails.** The fourth mismatch frees the third run's witness, which S7's Step 5 pinned a full run below the maximum.
- (Scope sharpened after the Lean lane's review.)


### 1. What S7 uses, and one new constraint

S7 excludes `s = 3` using only inequalities between sizes, along the maximal admissible profile `y_k = ℓ + Σ_(i<k)(log₂ 3 − a_i + ε)`:

1. **End witnesses:** `1 + t log₂ 3 < y_z`, where `z = e` or `e + h` according to the sign of `δ` on the run.
2. **Start witnesses:** `E + 1 < y_(z′)`, at the run's first position (2-adic). They are equivalent to (1) on each run but are stated separately.
3. **The ceiling with tracked excess**, which is built into `y`.
4. **The sign structure** of `δ` (S7-a, S7-b part 2).

S8 adds one constraint of the same kind, a comparison with the integer fixed point `−1` (word `1^∞`).
- On a run of `r` ones, `n + 1` is multiplied by `3/2` at each step, so `3^r | n_e + 1` at the run's end `e`.
- So **a run of `r` ones ending at `e` forces `n_e + q ≥ 2·3^r`, i.e. `1 + r log₂ 3 ≤ log₂(n_e + q)`.** *[Corrected 2026-10-19, after the Lean lane's review: the first version had the strict `<`. Equality occurs, e.g. at the step `3 → 5` at `q = 1`, where `5 + 1 = 2·3`. The formal statement is `ones_run_le` (S8-a), in the `≤` form. The probes test the strict form, which is only more demanding, so their survivor margins remain valid.]*
- A run of ones starting at height `y` gains `0.585` per step, so it can last at most about `y − 1` steps (`1 + 1.585r < y + 0.585r`). In particular, the run starting at the minimum has length below `ℓ − 1`, and letters `≥ 2` must recur at gaps of order `ℓ` early in the climb. *[Corrected 13:13: the first version said "about `0.63ℓ`", which ignored the run's own gain. The probe evaluates the exact inequality, so the tables are unaffected.]*
- Consistency: reducing `C(w)` mod `D` for this family gives the same constraint. For the first 2, at position `p₀` after the minimum, the reduced representative is below `D` when `p₀ ≳ ℓ`. So "reduce mod `D` to a small number" adds nothing beyond the comparison with `−1` here.
- The same device works with any integer cycle as the comparison orbit: `{1}`, `{−1}`, `{−5, −7}` and the `−17` cycle.


## What happened

### 2. Explicit four-mismatch words meet every constraint

The words are built along one `h`-chain (`gcd(h, m) = 1`) with arcs `[V][1^a][2^b][1^c]`.
- There is one huge letter `V` at `x = m − 1`, and the 2s fill the chain interval `a + 1, …, a + b`. `V` is fixed by `A = ⌈m log₂ 3⌉`.
- The rotation by `h` has exactly four mismatches: `x − h`, `x`, `x + a·h` and `x + (a+b)·h`.
- The parameters are chosen as follows:
  - `h/m ≈ √2 − 1`, which has bounded partial quotients, so the 2s spread evenly (three-gap theorem). Rational-like `h/m` clusters them and breaks constraint (5).
  - `b ≈ 1.6m/ℓ`, so runs of ones near the minimum are short enough.
  - The inner mismatches are placed in the windows where the continuous witness LP is feasible.

**The continuous LP.** Scale positions by `m`, with the minimum at 0, the huge letter at `x ≈ 1`, and slope `σ = log₂(3/2) − (2-density)`. Put `r = σ/log₂ 3` and `ℓ/m → 0`.
- The signs are `δ < 0` on `(x − h, x]` and `δ > 0` on `(x, x − h]`.
- The two inner mismatches are `p₁ ∈ (1 − h, 1)` (witness `p₁`) and `p₂ ∈ (0, h)` (witness `p₂ + h`). The four runs and their end-witness constraints `t ≤ r·pos(z)` are:
  - `(x, p₂)`: `p₂ ≤ r(p₂ + h)`
  - `(p₂, x − h)`: `1 − h − p₂ ≤ r`
  - `(x − h, p₁)`: `p₁ − (1 − h) ≤ r·p₁`
  - `(p₁, x)`: `1 − p₁ ≤ r`
- **Feasibility.** These hold together iff `p₂ ∈ [1 − h − r, rh/(1−r)]` and `p₁ ∈ [1 − r, (1 − h)/(1 − r)]`. Both intervals are nonempty iff `h ∈ [(1−r)², 1 − (1−r)²]`, which is `[0.398, 0.602]` at `r = 0.369`.
- **The other constraints.** The start witnesses (2) and runs of ones (5) are then checked exactly on the integer word.

Every constraint (1)–(5) is evaluated exactly on the word, and the margin is the smallest slack in bits (`s8_four_mismatch_map.py`):

| `m` | `ℓ` | `b` | margin (bits) | binding constraint |
|---|---|---|---|---|
| 1,000,003 | `ℓ*` = 6,987 | 228 | +2,028 | (5) runs of ones |
| 4,000,037 | `ℓ*` = 7,671 | 834 | +3,872 | (5) |
| 1,000,003 | 3,000 | 542 | +1,226 | (5) |
| 1,000,003 | 1,000 | 1,604 | +354 | (5) |
| 1,000,003 | 200 | 8,004 | +111 | (5) |
| 1,000,003 | 71 | 22,540 | −3,184 | (1) end witnesses (`h/m ≈ 0.4142`, just outside the window) |
| 1,000,003 | 71 | 35,235 | +33 | (5), with `h/m ≈ 0.4393 = [0; 2, 3, 1, 1, …]` |
| 1,000,003 | 100 | 16,011 | +55 | (5), same `h` |

- **Both test periods are above S7's threshold** (`m0 = 452,695`).
- **At `ℓ = ℓ*`**, the worst case allowed by `gap_all`, every constraint holds with thousands of bits to spare. So **no argument built only from (1)–(5) can exclude `s = 4`.**
- **Survival holds for every `ℓ` tested, from 71 to `ℓ*`.** The rotation fraction must sit inside the LP window `[(1−r)², 1 − (1−r)²]`, where `r` drops as the 2-density `≈ 1.6/ℓ` grows, and must have bounded partial quotients. `[0; 2, 3, 1, 1, …] ≈ 0.4393` works at `ℓ = 71`.
- **The first `ℓ = 71` failure** below belonged to `h/m ≈ √2 − 1`, which lies just outside that window at `ℓ = 71`.
- **Earlier wording (superseded):** the survival extends down to `ℓ = 200`. That is the scale a published irrationality measure for `log₂ 3` would give (Rhin-type, `ℓ ≲ 4.1 log₂ m + O(1)`; not formal).
  - At `ℓ = 71` this single-chain family fails in the search. The 2-density `1.6/ℓ` lowers the slope enough to push `h/m ≈ 0.4142` out of the feasible window.
  - That is a statement about one family and one choice of `h`, not an exclusion.

### 3. What the obstruction looks like

The survivors match S7's structure with one more degree of freedom:
- a tall sawtooth (`log₂ H ≥ 0.396m`) with a single drop `V ≈ 0.58m`;
- a sparse, evenly spread set of 2s;
- two sign changes at `x − h` and `x`, as in S7;
- two further mismatches that carry no sign change. The fourth mismatch frees the third run's witness, which in S7 was pinned a full run below the maximum.

In S7's language, each of the long runs now has a witness high enough on the climb.


### 4. Consequences for the programme

- **`ρ ≥ 4` is the limit of size arguments.** Main's milestone `F(m) → ∞` needs input beyond sizes. The candidates are:
  - arithmetic on the mismatch transition `2^β δ_(e+1) = 3δ_e + (2^α − 2^β) n_(e+1)` (with `α = a_e`, `β = a_(e+h)`), which is the only place new information enters at a mismatch;
  - the mod-`D` relation `Σ_k (2^(W_k) − 2^(W_(k+1)))·3^(m−e_k−1) 2^(A_(e_k+1)) n_(e_k+1) ≡ 0 (mod D)` over the mismatches, the Abel-summed form of C012's coupled system;
  - a much stronger upper bound on `L`, which would help only if it reached `ℓ ≈ 71`.
- **By-product:** a short proof that 1-cycles (`1^(m−1)V`) do not exist for large `m`. Reducing mod `D` gives `D | 3^m − 2^m ≡ 2^m(2^(A−m) − 1)`, so `D ≤ 2^(A−m)`, which contradicts `gap_all` (`D ≥ 2^A/(2^172 m^341)`) once `2^m > 2^172 m^341`.
  - This is Steiner's theorem (1977) by a different route, labelled as known.
  - The same "reduce mod `D` to a small nonzero number" device is the natural tool to try next on the S8 survivors.


## Why it fails

The headline claim fails; the side lane withdrew it at 13:44 (feed "COUNTEREXAMPLE (to this lane's S8 headline)").

- **What fails.** The S8 words meet every size inequality *of the rotation by `h`*. The rotation by `2h` is another rotation of the same word. It has 6 mismatches, at `x, x − 2h, P₁ − h, P₁, P₂ − h, P₂`, and its runs obey the same witness inequality `1 + t·log₂ 3 < y_z`. On the S8 words at `m = 10^6` it fails by 193,000 bits (`ℓ = ℓ*`), 209,000 bits (`ℓ = 71`) and 287,000 bits (`ℓ = 100`) (`s8_multiple_rotations.py`). Rotations by `3h`, `4h`, `5h`, `7h` and `9h` also fail.
- **Why it was missed.** The 13:36 robustness check (`s8_multirotation_check.py`) looked only at convergent denominators of `h^(−1)/m`, which do not include `2h`. The Lean lane's review (13:17) had scoped the claim to the single rotation `h` but did not raise the other rotations either.
- **Every C013-b/S7 lemma is parametric in the rotation** and needs only `h′ % m ≠ 0` (Lean lane, iteration 73), so the run law applies at full strength to `2h`.

## What survives

- **The narrow statement.** The inequalities (1)–(5) of the single rotation `h` are jointly satisfiable by the S8 words, with the tabulated margins. As a statement about size arguments it is too weak to matter, since every rotation of the word contributes size inequalities.
- **Constraint (5)** in corrected form, at general odd `q`: [`ones-run-divisibility`](../../results/ones-run-divisibility.md) (formal).
- **The 1-cycle by-product of §4**: [`one-cycle-exclusion-via-gap`](../../results/one-cycle-exclusion-via-gap.md) (formal, conditional on the gap; a known result by a new route).
- **The candidate mechanisms of §4** (arithmetic of the mismatch transition, the mod-`D` relation over the mismatches, a much stronger bound on `L`), as suggestions for [`rotation-distance-growth`](../../questions/rotation-distance-growth.md).
- **What it opened.** Whether multi-rotation size constraints (`h`, `2h`, …) exclude every four-mismatch word, giving `ρ ≥ 5`, became the side lane's S10 ([`multi-rotation-four-mismatch-exclusion`](../multi-rotation-four-mismatch-exclusion/README.md)): the cheapest pattern is excluded by `h` and `2h` together in a continuous model; another pattern survives there; `ρ ≥ 5` stays open.

## History

- Migrated from `experiments/cycle_spectrum/S08/FOUR_MISMATCH_MAP.md` (legacy ID `S08`; side-lane producer batch S8, 2026-10-19) at commit `be73a66`, by the B05 migration (Claude, Opus 5.5). The side-lane probes `reviews/side_lane/s8_four_mismatch_map.{py,json}`, `s8_multirotation_check.py` and `s8_multiple_rotations.py` moved here. The note's "Reproduce" block pointed to the old path.
- Side lane (Claude, Opus), feed 2026-10-19 13:06 (FINDING). Update 13:11: survival at `ℓ = 71` and `100` with `h/m ≈ 0.4393`. Update 13:17: the Lean lane's review, scope sharpened to a relaxation-feasibility statement. Update 13:36: robustness check against other structured rotations (missed `2h`).
- **Correction (13:13).** The run of ones leaving the minimum: the first version said "at most about `0.63ℓ`", which ignored the run's own gain; corrected to "below `ℓ − 1`". The tables come from the exact inequality and are unaffected.
- **Withdrawn (13:44).** The headline fails for the rotation by `2h` (above). The side lane found this itself; the narrow single-rotation statement stands.
- **Correction (15:06, the Lean lane's).** Constraint (5) was stated with a strict `<`; the correct form is `≤`, `1 + r·log₂ 3 ≤ log₂(n_e + q)`. Equality occurs, e.g. at the step `3 → 5` at `q = 1`, where `5 + 1 = 2·3`. The probes test the stricter `<`, so their margins remain valid. The rotation witness of S7/S9 (`max(n_e, n_(e+h)) > 2·3^t`) is genuinely strict and unaffected.
