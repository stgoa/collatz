# Review of joint-source-unbounded-frontier

Independent review (Claude review lane, Fable 5.1; directed by Santiago Armstrong). Scratch code: own `S`, `ν`, `v2`, nothing imported from the repository.

## What I checked

- **Certificates** (`python3 tools/run_certificates.py --node joint-source-unbounded-frontier`): `r42_joint_frontier_check.py` PASS (0 s), `check_legacy_replay.py` PASS (6 s); exit 0, wall time 6.19 s. The legacy replay runs `check_joint_frontier.py` against `joint_frontier_audit.json` (8192 interface cases, 2048 block inputs, 45 parameter pairs, 11 expansion instances, 5 embeddings, 4 required-ray sources).
- **Section 1 (interface table).** Re-derived: the upper first arrow has valuation 2 and endpoint `(27v+5)/2`; for `v ≡ 3 (mod 8)` the second has valuation 1 and `9v+5 = 2^(a+1)z` gives `9·2^(a−1)z − 7`; for `v ≡ 7 (mod 8)`, `9z − 7 = (81v+17)/4`. Checked exhaustively for every `v ≡ 3 (mod 4)` below `2·10^6` (251,536 + 251,464 cases) and 3,000 random 200-bit `v`, including the words `(2,1)/(1,a)`, `(2,e+1)/(1,1)`, `a = 2 ⇔ v ≡ 11 (mod 16)`, and `z > v` exactly then and in the second row (so no height-decreasing closed family).
- **Section 2 (class `3 mod 32`).** Exhaustive for all 62,500 `v ≡ 3 (mod 32)` below `2·10^6`: `t ≡ 1 (mod 4)`, `h ≥ 2`, `u = (9v+5)/2^(h+3)`, (2), (3) with equality only at `v = 3`, (4) in both directions, the block (6) with word `(2,1,2)(1,2)^j`, clocks `3+2j` and `2`, `q ≡ 22 (mod 27)`. The two arrows (5): 2,000 random `(A, u, m ≥ 4)`; with `m = 3` the second valuation is never 2 (10,000/10,000 cases), so the hypothesis `m ≥ 4` is needed and sufficient. `q ≡ 22 (mod 27)` gives `q ≡ 1 (mod 3)`, `v3(q−1) = 1`, `unit3(q−1) = 1`, the second line of R38's complementary phases (13); 8,923 of the 62,500 blocks end at a critical canonical `q`. The pair `δ_q − δ_u` is never `C(u)` in this range.
- **Section 3 (expansion).** `r = 0..40`: `v_r` integral, `S²(v_r) = 1` with word `(1, 6r+4)`, `18v_r + 3 = 2^(6r+6) − 7`, `S^(4r+3)(18v_r+3) = q_r` with word `(2,1,2)(1,2)^(2r)`, `q_r ≡ 1 (mod 8)`, `≡ 1 (mod 3)`, canonical, `S(q_r) = (3^(4r+4) − 7)/2`; the ratio (8) agrees with `(243/16)(81/64)^r` to relative error below `2^(−6r−2)`.
- **Section 4 (embedding).** `r = 9, 18, …, 270` (30 values): `v ≡ 3 (mod 9)`, `w ≡ 17 (mod 128)`, `w ≡ 2 (mod 3)`, `v = 3(w−1)/16` (the R39 A-entry), `a = 2`, `t0 ≡ 3 (mod 4)`, `v2(3t0 − 1) = 4`, the four-arrow certificate (9) with valuations `(5, 2, 3, h+2)`, the upper prefix `S³..S⁶` and (10) with word `(1,2,2,1,3,3,2)(1,2)^(2r)`, `81x = 2^(6r+15) − 3365`, the identity `81(q_r − x_r) = 4374·81^r − 32768·64^r + 2960`, `q_r > x_r`. The sign is positive first at `r = 9` (negative for `r ≤ 8`), so "`r ≥ 9`" is sharp. `x_r` is an integer iff `9 | r` (checked `r < 60`; `ord_81(2) = 54`) and `3 | x_r` iff `27 | r` (checked `r < 120`; `ord_243(2) = 162`, `2^15 − 3365 = 243·121`). For the ten multiples of 27 up to 270: `x_r ≡ 3 (mod 12)`, `N_r < x_r < 9N_r/8 < 3N_r/2`, `p < N_r`, and `x_r/N_r = 256/243 − 3365/(81N_r)` exactly.
- **`R_(N_r)(x_r) = 1`** (left unchecked by the side lane): by the definition in [`retained-graph-complement-constructor`](../retained-graph-complement-constructor/README.md) (coefficient 1 on `x ≡ 3 (mod 12)` in `(N, 3N/2)`) and the support identity of [`outer-residual-strong-induction-support`](../outer-residual-strong-induction-support/README.md): `x_r ≡ 0 (mod 3)` has no odd Syracuse predecessor, so it is not in `S([1,N]) ∪ S²([1,N])`.
- **Stored currents.** From `actual_r27_frontier_current.csv` (119 rows = `4r + 7 + 4`, coefficients `±1`) my own divergence gives exactly `δ_x − δ_p − δ_(q_r)`, i.e. (11); `actual_r27_lower_current.csv` (4 rows) has divergence `δ_p`.
- **Controls.** The node excludes a construction, not a cycle, so the `3x+d` cycle fixtures do not bear on it. The arrows (5) are a `d`-uniform affine identity: with constants `−5d`, `−7d` (the shadow of the cycle `{−5d, −7d}` of `3x+d`) they hold verbatim for `d = 5, 7, 13, 61`, consistent with the scoped reading.

## What I did not check

- The residual machinery behind `R_N` (B09) beyond its stated definition and support identity.
- The internals of the main-lane module `joint_frontier.py` (replayed by the certificate only).
- Any statement about absorption of `q_r`: none is made.

## Findings

1. `r42_joint_frontier_check.py` (listed under `certificates`), location: whole file. It relies entirely on `assert`; under `python3 -O` it would pass vacuously (AGENTS.md §6). `tools/run_certificates.py` invokes `sys.executable script` without `-O`, so the run above is a real check. Severity: imprecision (hygiene); not changed here.
2. Statement item 3, "`N_r < x_r < 9N_r/8`": true for every positive multiple of 27; the proof's remark "between 1 and 9/8 for `r ≥ 27`" is the same bound. The integrality of `x_r` needs `9 | r` and `3 | x_r` needs `27 | r`, both sharp (see above); the statement's quantifier "every positive multiple of 27" is exactly right. Severity: none (recorded as checked).
3. Section 2, the sentence "when `q` is critical canonical it lies in R38's omitted phase": verified against R38's (13); the phase is the second line (`q ≡ 1 mod 3`, `unit3(q−1) = 1`). Severity: none.

## Verdict

HOLDS. Every displayed identity, inequality, word and quantifier of sections 1–4 re-derives and recomputes; the scope stated in the claim (a scoped failure of one prescribed block, no nontermination, no obstruction to other constructions, no positive cycle) is exactly what the proof delivers.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
