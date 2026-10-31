# Review of cycle-word-repeat-bound

## What I checked

- Certificate: `python3 tools/run_certificates.py --node cycle-word-repeat-bound` from the repository root: PASS, exit 0, 24.3 s wall (the tool prints 24 s). The working tree was unchanged afterwards, so the replayed probe left its receipt byte-identical.
- The proof line by line. Two occurrences of one factor of length `t` at cyclic offset `h ≢ 0 (mod m)` mean `a_i = a_(i+h)` for `t` consecutive `i`, an agreeing run of the rotation by `h`. Part 3 of [`paired-state-run-law`](../paired-state-run-law.md) (formal; any `q > 0`, distinct states, `h ≢ 0`) gives `z_end = 2·3^t·k` with `k ≠ 0`, so `2·3^t ≤ |z_end| = |n_(e+h) − n_e| ≤ H − L < H`, that is `1 + t·log₂3 < log₂H`. [`global-drift-ceiling`](../global-drift-ceiling.md) (formal, `B_le_drift`, real `B = log₂(H/L)`) gives `log₂H ≤ log₂L + (m − 1)·log₂(3/2) + δ`. Together `t < T = (Λ + (m − 1)·log₂(3/2) − 1)/log₂3`. "`p_w(n) = m` for `n ≥ T`": no two of the `m` cyclic positions carry the same factor of length `n ≥ T`; for `n ≥ m` a repeat would make `w` equal to a nonidentity rotation, excluded by primitivity. Both inputs are used inside their hypotheses (any odd `q > 0`, no order, nothing on `L/q`).
- The `q = 1` asymptotics, which the node states in one line (finding 1). From `δ_nat = Σ ln(1 + q/(3n_i)) < m·q/(3L)` (recorded as (6) of the run law) and `δ_nat ≥ η = D/2^A ≥ 2^(−172)·m^(−341)` (EXT-1): `L < m/(3η)`, so `log₂L < 172 + 342·log₂m − log₂3`, which is exactly the probe's `ℓ*`. Distinct odd states `≥ L` give `δ_nat ≤ (q/3)·(1/L + (1/2)·ln(1 + 2(m − 1)/L)) = O(log m)` (checked on the controls, ratio `≤ 0.82`); with the imported `L > 2^71` the drift is below `m/(3·2^71·ln 2)` bits. So `Λ = O(log m)` and `T = (log₂(3/2)/log₂3)·m + O(log m) = 0.36907·m + O(log m)`. Explicitly, with `L > 2^71`: at `m = 1.375·10^11`, `Λ* = 12,824.6`, `T = 5.0747·10^10 = 0.36907·m`, and `2T + 1 < m`; the inequality `2T + 1 < m` holds for every `m ≥ 24,901` even with `L ≥ 1` (`24,884` with `L > 2^71`).
- The complexity facts: a coding of a rotation by `k` intervals has `p(n) ≤ k·n` (the `n·k` cut points), Sturmian words `n + 1`, 3-interval exchanges `≤ 2n + 1`; the exclusions need `2T + 1 < m`, and `kT > m` for `k ≥ 3` since `3·0.369 > 1`, as the node says.
- Controls (my script, odd seeds `≤ 20,000`; the cycle counts 6, 2, 10, 3 for `q = 5, 7, 13, 61` equal the corpus). On all 14 cycles with `m ≥ 2` (periods 2, 3, 3, 5 ×7, 15, 17, 17, 41): the longest repeated factor `t` satisfies `2·3^t < H` and `t < T(m, Λ)` with the actual `Λ`; `p_w(n) = m` for every `n` from `⌈T⌉` to `m + 1`; the largest `t/T` is 0.52 (`q = 13`, `m = 5`). The run law itself was re-checked on all 624 maximal agreeing runs of every nonidentity rotation (`z` even and nonzero, `2^(E+1) | z_start`, `z_end = 2·3^t·k` with the same `k ≠ 0`): no failure.
- Probe replication (part (i)) with my own code: 3,918 cycles (odd `q < 2,000`, `3 ∤ q`, `m ≥ 3`, odd seeds `≤ 1,001`), 0 violations of `2·3^t < H`, maximum `(1 + t·log₂3)/log₂H = 0.970` at `q = 1,723`, `m = 219`, `t = 10`, `H = 168,863`; identical to the receipt.

## What I did not check

- Part (ii) of the probe (random rotation codings), an exploration.
- The Lean declarations of the two formal inputs beyond their `## Lean` sections.
- EXT-1 itself (replayed elsewhere), and the theory of interval-exchange codings beyond the counting bound above.
- The "Literature (calibration only)" remark.

## Findings

1. Proof, `q = 1` paragraph: "the drift is negligible and `log₂L = O(log m)` by the gap (as in [`mismatch-height-tradeoff`](../mismatch-height-tradeoff/README.md))". That node never bounds `L`. The bound is `L < m/(3δ_nat) ≤ m/(3η) ≤ 2^172·m^342/3`, so `log₂L < 172 + 342·log₂m − log₂3` (the probe's `ℓ*`), and the drift is `O(log m)` by the harmonic-sum bound (or tiny with the imported minimum). The conclusion is right; the justification should name these two bounds. Severity: imprecision.
2. Remarks, Data: "On all 3,918 actual `3x+q` cycles with `q < 2,000`": the set is the cycles of period `≥ 3` reached from odd seeds `≤ 1,001` for odd `q < 2,000` with `3 ∤ q`; "all" overstates the enumeration. The numbers reproduce exactly. Severity: imprecision.
3. Claim and Statement, "for large `m`": with the bounds above, `2T + 1 < m` holds for every `m ≥ 24,901`, far below the imported period; this could be stated. Severity: imprecision.
4. Claim: "codings of 3-interval exchanges (`p(n) = 2n + 1`)": equality needs the i.d.o.c. condition; in general `p(n) ≤ 2n + 1`, which is all the exclusion uses. Severity: typo-level.

## Verdict

HOLDS. Part 1 unconditional at every odd `q`; part 2 conditional on EXT-1 as stated. Certificate passed. No correction applied.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
