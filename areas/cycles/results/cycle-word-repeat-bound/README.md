---
id: cycle-word-repeat-bound
kind: result
title: "No long factor repeats in a cycle word: the run bound as a factor-complexity statement"
status: reviewed
claim: >
  Let n_0, …, n_(m−1) be a primitive positive odd cycle of the odd-only 3x+q map (odd q), with word w,
  minimum L, drift δ(w) = A − m·log₂3 and Λ = log₂L + δ(w). If some factor of length t occurs twice in the
  cyclic word w at cyclic offset h ≢ 0 (mod m), then t < T = (Λ + (m − 1)·log₂(3/2) − 1)/log₂3; so every
  factor of length ≥ T occurs at most once and the factor complexity is p_w(n) = m for n ≥ T. At q = 1,
  conditional on the replayed gap (EXT-1), T ≈ 0.369·m + O(log m), so for large m no nontrivial 3x+1 cycle
  word has p_w(T) < m: in particular none is a Christoffel/Sturmian word (already known, Knight), a coding
  of a 2-interval rotation, or a coding of a 3-interval exchange. Codings of rotations by k ≥ 3 intervals
  (p(n) ≤ k·n) are not reached by counting.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [paired-state-run-law, global-drift-ceiling, mismatch-height-tradeoff]
assumes: [musson-collatz-gap-all]
certificates: [check_legacy_replay.py]
evidence:
  - "s10_repeat_complexity.py, s10_repeat_complexity.json: side-lane probe (about 7 s): (i) checks the repeat inequality 2·3^t < H on every actual 3x+q cycle with q < 2,000; (ii) on random k-interval rotation codings (k = 2, 3, 4) measures the longest repeated factor against T(m, ℓ*). Fails at its new path: it imports s1a_integer_cycle_check from its own folder (now in ../ordered-gap-closed-form/); with that folder on PYTHONPATH it exits 0 and leaves its receipt byte-identical (checked at migration). Passed at be73a66 as reviews/side_lane/s10_repeat_complexity.py (archive/legacy-checker-run-be73a66.md). Despite its s10_ prefix it belongs to S9 §5. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Repeat law re-derived from the formal run law and global-drift ceiling; the q = 1 asymptotics made explicit (log2 L < 172 + 342 log2 m - log2 3 from the gap, drift O(log m), 2T + 1 < m for m >= 24,901); certificate re-run (exit 0, 24.3 s); probe part (i) reproduced exactly (3,918 cycles, 0 violations, ratio 0.970); repeat bound, complexity and run law tested on every 3x+5, 7, 13, 61 cycle. Verdict HOLDS"
tags: [cycles, rotation-distance, factor-complexity, 3x+d]
---

# No long factor repeats in a cycle word: the run bound as a factor-complexity statement

## Statement

Primitive positive odd cycle of the odd-only `3x+q` map (odd `q`), word `w`, minimum `L`, drift `δ(w) = A − m·log₂3`, `Λ = log₂ L + δ(w)`.

1. **Repeat law (any odd `q`).** Two occurrences of the same factor of length `t` at cyclic offset `h ≢ 0 (mod m)` force `t < T(m, Λ) = (Λ + (m−1)·log₂(3/2) − 1)/log₂3`. So **no factor of length `T` repeats**: `p_w(n) = m` for every `n ≥ T`.
2. **At `q = 1`** (conditional on EXT-1, [`musson-collatz-gap-all`](../../../../sources/musson-collatz-gap-all.md)): `T ≈ 0.369·m + O(log m)`. Any word with `p(T) < m` is excluded for large `m`. That covers Sturmian/Christoffel words (`p(n) = n + 1`; Knight's theorem, [`knight-2026-high-cycles`](../../../../sources/knight-2026-high-cycles.md), already excludes them), codings of 2-interval rotations (`p(n) ≤ 2n`) and codings of 3-interval exchanges (`p(n) = 2n + 1`), since `2T + 1 < m`.
3. **What counting cannot reach.** Codings of a rotation by `k ≥ 3` intervals have only `p(n) ≤ k·n`, so counting alone does not exclude them. Three-mismatch chain words are such codings and need S7 ([`three-mismatch-exclusion`](../three-mismatch-exclusion/README.md)).

## Proof

Legacy S9 note §5 (side lane), lightly edited.

Two occurrences of the same factor of length `t` at cyclic offset `h` form an agreeing run of the rotation by `h`. So the run law ([`paired-state-run-law`](../paired-state-run-law.md)) gives `max(n_e, n_(e+h)) > 2·3^t` at the run's end `e`. With the global-drift ceiling ([`global-drift-ceiling`](../global-drift-ceiling.md)), every state satisfies `log₂ n ≤ log₂ L + (m−1)·log₂(3/2) + δ(w)`, so `1 + t·log₂3 < Λ + (m−1)·log₂(3/2)`, that is `t < T`. At `q = 1`, the drift is negligible and `log₂ L = O(log m)` by the gap (as in [`mismatch-height-tradeoff`](../mismatch-height-tradeoff/README.md)), so `T = (log₂(3/2)/log₂3)·m + O(log m) ≈ 0.369·m + O(log m)`. The class exclusions follow from `p(T) ≤ 2T + 1 < m` for large `m`.

**Novelty.** This is S5's uniform run bound read as a statement about repeats. What is new is the packaging, not the inequality.

## Remarks

- **Data** (`s10_repeat_complexity.py`).
  - On all 3,918 actual `3x+q` cycles with `q < 2,000`, the longest repeat obeys `2·3^t < H`.
  - The ratio `(1 + t·log₂3)/log₂ H` reaches 0.97 (`q = 1,723`, `m = 219`, `t = 10`). So the witness bound is nearly sharp on actual cycles.
  - Random rotation codings repeat far beyond `T` (generic rotation numbers have good rational approximations). Only badly approximable rotation numbers, like those of S8's survivors ([`four-mismatch-size-method-limit`](../../attempts/four-mismatch-size-method-limit/README.md)), keep the longest repeat short.
- **Correction before posting.** A first draft claimed `p(n) ≤ (k−1)n + 1` for `k`-interval rotation codings; the correct bound is `k·n`, fixed before the feed entry (feed S9 entry, update 13:27).
- **Literature (calibration only, feed 13:34).** A preprint on a drift-sensitive factor-complexity lower bound for infinite aperiodic parity words of the 3x+1 conjugacy map is close in spirit; only its abstract was read. No comparison is claimed.

## History

- Split from `experiments/cycle_spectrum/S09/DENOMINATOR_LAW.md` §5 (legacy ID `S09`; side-lane producer batch S9, 2026-10-19) at commit `be73a66`, by the B06 migration (Claude, Opus 5.5). The rest of the note is [`two-three-mismatch-denominator-laws`](../two-three-mismatch-denominator-laws/README.md). The probe `reviews/side_lane/s10_repeat_complexity.{py,json}` moved here.
- Side lane (Claude, Opus), feed 2026-10-19 13:27 (S9 entry, update "the repeat form"). No independent review of this section is on record: the Lean lane's 13:29 review of S9 concerned where `q` enters the laws.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No text changed. The review ([`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md)) makes the `q = 1` step explicit: `log₂L < 172 + 342·log₂m − log₂3` follows from `L < m/(3δ)` and EXT-1, the drift is `O(log m)` for distinct odd states, and `2T + 1 < m` holds for every `m ≥ 24,901`; it also notes that the 3,918 cycles of the data remark are those of period `≥ 3` reached from odd seeds `≤ 1,001`.
