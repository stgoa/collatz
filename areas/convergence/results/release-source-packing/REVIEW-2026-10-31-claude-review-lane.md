# Review of release-source-packing

Independent review of [`README.md`](README.md) (author: ChatGPT main lane, Codex; the side lane's 2026-10-17 probe checked the two families but not the capacity against the older catalogue). Scope: `A_N`, `8 | N`, odd-only `3x+1`, absorbing at 1. Every number below comes from my own script (`recompute_release.py`, outside the repository: own `S`, own `Π^R_N`, own annulus `Π^R_(64N) − Π^R_N` for `N ≤ 256` and the six-band table above, own re-implementation of the old constructor) or from the certificate run.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node release-source-packing`: `check_legacy_replay.py` `PASS` (10 s), exit 0, 10.0 s wall. The replay runs the unmodified `release_packing.py` (every multiple of 8 through 1024 and 6144: sources, capacity against the old constructor, full divergence, 27 boundary phases) and the side-lane probe `release_families_check.py` in the rebuilt legacy tree, every file byte-identical afterwards.
- **Pairs, re-derived.** `q = 54m + 31` gives `u = (4q − 1)/3 = 72m + 41`: odd, `≡ 5 (mod 18)`; `3u + 1 = 4q` with `q` odd, so the valuation is exactly 2 and `S(u) = q`; `36N < q < 54N` gives `48N − 1/3 < u < 72N − 1/3`, hence `48N < u < 72N` (`u` odd, `48N` even). `q ≡ 13 (mod 18)` in band 4 `(36N, 72N)`: table `A_N(q) = 2`, `A_N(u) = −2`; `(I − P)(−2δ_u) = −2δ_u + 2δ_q`.
- **Triples, re-derived.** `q = 108m + 31`: `u = 144m + 41` (`≡ 5 (mod 18)`, `≡ 41 (mod 144)`), `v = (3q + 1)/2 = 162m + 47` (`≡ 11`); `q = 108m + 103`: `u = 144m + 137` (`≡ 11`, `≡ 137 (mod 144)`), `v = 162m + 155` (`≡ 11`). `q ≡ 3 (mod 4)` gives valuation 1 at `q`; `u ∈ (256N/3 − 1/3, 96N − 1/3)` and `v ∈ (96N + 1/2, 108N + 1/2)` lie in band 5; table `A_N(u) = −1`, `A_N(q) = 2`, `A_N(v) = −1`; `(I − P)(−δ_u + δ_q) = −δ_u + 2δ_q − δ_v`, positive cost 1.
- **Capacity (§3), re-derived.** Old positions with (band, residue mod 18): catalogue negatives E `(2,7)`, D `(2,5), (2,17)`, B `(3,7)`, C `(3,5)`, A `(4,7), (4,1)` in `(48N, 64N)` and `(5,11)` in `(72N, 96N)`; catalogue positives `(3,11)`, `(4,17)` three times, `(4,11)`, `(5,17)` twice; five-source negatives `(4,1)`, `(4,1)` or `(4,7)`, `(5,5)`, positives `(4,11)`, `(5,17)`. New positives are `(4,13)`: unused. Pair negatives `(4,5)`: unused. Triple `v` is `(5,11)` in `(96N, 108N)`, disjoint from A's middle points in `(72N, 96N)` (`96N` even) and of different residue from the fifth atom. Triple `u` with residue 11 against A's middle points: a middle point `x_1` has `x = (2x_1 − 1)/3 ≡ 7, 55 (mod 72)`, while `(2u − 1)/3 = 91 + 96t ≡ 19, 43, 67 (mod 72)`. Triple `u` with residue 5 against the fifth atom: `41` vs `95 (mod 144)` (`13775 ≡ 95`, `1152 ≡ 0`). Overlapping current rows do not affect the identity and only lower the positive part.
- **Counts.** `P(N) = 18N/54 + O(1)`, `T(N) = 2·8N/108 + O(1)`, `2P + 2T = 26N/27 + O(1)`; `3N/2 + N/48 + 26N/27 = (648 + 9 + 416)N/432 = 1073N/432`; `3C_old + T = N/48 + 4N/27 = 73N/432`; under `N → N + 216` the intervals grow by `3888 = 72·54` and `2·1728 = 32·108`.
- **Independent code.** For every `8 | N ≤ 1024` and `N = 6144, 7200, 10008, 20000`: every pair and triple (arrows, valuations, intervals, residues mod 18 and mod 144, bands, coefficients, identities); counts equal to the floor formulas; no state reused within the new blocks or against my own re-implementation of the old constructor (catalogue plus every five-source copy found by trying every `t`); `A_N = (I − P)J_ext + Z_ext` exactly; `‖Z_ext⁺‖₁ = 99N/4 − D − 3C_old − 2P − 2T`; `‖J_ext⁺‖₁ ≤ 3C_old + T`, with equality at every tested `N`. `N = 8`: `P = 3`, `T = 2`, removed 21, residual positive mass 177, cost 2 (the receipt agrees); `N = 96`: `P = 32`, `T = 15`, removed 243; `N = 6144`: `P = 2048`, `T = 911`, removed 15,265, cost 1,040. Point evaluation of the four boundary members of each family at 20 random `N` between `8·10^6` and `8·10^9` (240 checks). From the formulas over `8 | N ≤ 200,000`: `|3P − N| ≤ 1`, `|27T − 4N| ≤ 28`, `|432·(D + 3C_old + 2P + 2T) − 1073N| ≤ 2616`, `|432·(3C_old + T) − 73N| ≤ 1752`; increments 72 and 32 under `N → N + 216` for all `N ≤ 20,000`; `(91 + 96t) mod 72 ∈ {19, 43, 67}`, `(13775 + 1152t) mod 144 = 95`, `u mod 144 = 41` for `q ≡ 31 (mod 108)`.
- **Controls.** The pair mechanism is map-independent algebra: on `3x+5` and `3x+13`, for odd `u = (4q − d)/3`, `S_d(u) = q` with valuation 2 and `2δ_q − 2δ_u = (I − P_d)(−2δ_u)` (500 cases each). The coefficients `(2, −2)` come from `A_N`, which exists only for `d = 1`; the node makes no `d`-uniform claim and no cycle claim.

## What I did not check

- The old constructor beyond my own re-derivation in the review of [`universal-annular-partial-current`](../universal-annular-partial-current/README.md).
- The legacy scripts and the side-lane probe line by line (replayed through the certificate only).
- Novelty.

## Findings

1. Proof §§1–5 (typo): about 30 missing spaces inherited from the legacy transcription ("multiple of8", "modulo54", "valuation is2", "band4", "this is19,43,or67", "through1024, plus6144", …). **Correction applied:** spaces restored on 27 lines; no wording changed.
2. Statement 4 / Proof §4 (imprecision): the positive rows of the new current are the triples' `q` rows only, pairwise distinct, so the new families cost exactly `T(N)` on their own; the combined bound `‖J_ext⁺‖₁ ≤ 3C_old + T` was attained at every tested cutoff. No change.
3. Proof §3 (imprecision): "Pair negative sources lie below `72N` and triple negative sources above `256N/3`" is the step separating the pair `u`'s from both kinds of triple negatives; correct since `256/3 > 72`. No change.

No error found; the capacity argument, which the side lane had not re-derived, holds for every `N`.

## Verdict

HOLDS WITH CORRECTIONS. Corrections: (1) typographic only (missing spaces in the legacy text).

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
