# Review of high-smaller-origin-history

Independent review of [`README.md`](README.md) (authors: ChatGPT main lane, Codex). Scope as in the node: odd-only `3x+1`, absorbing at 1, `F(x) = 4x+1`, `T = νS`, the retained critical basis of [`common-critical-rank-basis`](../common-critical-rank-basis/README.md). My scripts (own `ν`, `T`, canonical test and R25 inverse table, validated by brute force: `ν` equals the component minimum by union-find below `2^14`; the inverse table equals brute force for every canonical `y < 3000` and `p < 4·10^5`) live outside the repository; every number below was computed by them or by the certificate.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node high-smaller-origin-history`: PASS, exit 0, 16 s wall (run concurrently with three other nodes' certificates). It replays `batch_r78_r80_check.py` (30 family cases, forward closure of the anchor) and `check_native_history.py` (54 plans, 54 W5-frontier variants, 54 old endpoint failures, 4892 anchor states, 88 + 18 inverse words, 2 supplied conversions) in the legacy layout with every file unchanged; the clone was clean afterwards. The counts in `evidence` match the stored receipt.
- **Family, (1)-(3) and Statement 1**, on 88 cases `D ∈ {12, 13, 14, 15, 16, 20, 33, 64}`, `t ∈ {0, …, 7, 10^9 + 7, 2^64, 3^40 + 2}`: `b < p < q < y`; `p, q, y` canonical; `ρ(b) = ν(3b) = q`; the equivalent form (2), `3^12 p = 2^19 q − 309105` (I recomputed `11391·3^12 − 2^19·11547 = −309105`); `q ≡ 27 (mod 96)`, `b ≡ 9 (mod 32)`, `y ≡ 1 (mod 8)`; `q − p = 156 + (2^17·3^12 − 2^36)·3^(D−12) t` with `2^17·3^12 − 2^36 = 937558016 > 0`.
- **Blocked row.** `d = v2(9b − 1) = 4`; `3z` with `z = (3q−1)/16` is selected, `3z ≡ 95 (mod 128)`, `v2(3z+1) = 5`, `(3z+1)/32 ≡ 3 (mod 4)`; the higher request `u = (3q+3)/4 = 4z + 1` lies in `E_return` (`u ≡ 5 (mod 8)`, `u ≡ 3 (mod 9)`, `3u` selected with `a = 7`). All of this is fixed by `q mod 2048`, hence holds on the whole family.
- **High merger, §2.** The word (4) is exact on every case; state `j` equals its base plus `3^j·2^(36−A_j)·3^(D−12) t` (table), canonical for `j ≤ 12`, above `q` for `1 ≤ j ≤ 12`, peak `32q + 17`; the endpoint is `24q + 13 = 16y + 5 = F²(y)`, `F(y) ≡ 5 (mod 8)`, `ν(F²(y)) = y`; affine constants `(3^13, 1779283, 2^16)`; `S²(q) = S^14(p) = (9q+5)/8 > q`; `T(q) = y = T^13(p)`. The twelve inequalities `3^j·2^(19−A_j) > 3^12` hold. Why the phases are fixed: the 2-adic modulus deciding each base state's canonical type (`8` at `x ≡ 1 mod 4`, `2^(a+2)` for a climber) has exponent `(9, 8, 7, 6, 5, 4, 3, 3, 7, 6, 5, 4, 3)` for `j = 0..12`, at most `36 − A_j` (even at most `23 − A_j`, which [`fixed-word-history-cells`](../fixed-word-history-cells/README.md) needs).
- **Current (8)-(11).** The rows `δ_q − L_p − δ_x + δ_y` have divergence `[q] − [p]` (computed row by row with my `S`; `S(x) = S(y)`). The rank bound follows from R75's `A_s(v) ≠ 0 ⇒ ρ(v) ≤ ν(s)` with `ν(p) = p` and `ν(b) = b < p` (`b ≡ 9 mod 16` is canonical), so every request has rank `≤ p < q = ρ(b)`.
- **Old W5-only frontier, §3.** `p ≡ 127 (mod 512)`, complementary with `v2(p+1) = 7`; in each residue of `p mod 3` the named seed `s` is `5 (mod 8)` with `ν(3s) = p` and `(9s+5)/8 < p`, resp. `(3p+1)/4 < p`; `(9b+5)/8 < q`.
- **Anchor, §4.** I rebuilt the forward closure of the 2887 canonical origins below 11547 under my `T`: 4892 states, maximum 3012713, 11547 absent, identical as an edge set to [`anchor_certificate.json`](anchor_certificate.json). The lift (12)-(13): an independent inverse-tree search for canonical `a ≤ q` with `T^d(a) = q`, `1 ≤ d ≤ D`, pruned only by the exact bound `x + 1 ≤ (3/2)^(D−e)(q+1)`, finds none for `(D, t) ∈ {(12,1), (12,2), (12,7), (13,1), (14,3), (16,1)}` (21-63 nodes). The recurrence (13) and `G_i > 0` hold on 200 random inverse words with ray indices up to 3; the first step is a ray since `11547 ≡ 0 (mod 3)`.
- **R44/R52, §5.** `ρ(u) = (9q+5)/8 > q`; the R44 word `1^5, 2` from `ρ(u)` ends at `n = (6561q + 8965)/1024`, `n ≡ 1 (mod 8)` canonical; `S(n) = f = (19683q + 27919)/4096`, `f ≡ 7 (mod 32)`, `f ≡ 1 (mod 3)`, complementary canonical, hence critical with request `v = (2f+1)/3 ∈ W5`, `ρ(v) = f`; `f − ρ(u) = (15075q + 25359)/4096 > 0`. Both residues are fixed by `q mod 2^17`, so this is the whole family.
- **Controls** ([`NOTATION.md`](../../../../conventions/NOTATION.md) §3). The cell and shadow arithmetic is `d`-uniform (verified on the actual `3x+5`, `3x+7`, `3x+13`, `3x+61` cycles in my review of `fixed-word-history-cells`); the only `3x+1`-specific input is the absorbing anchor table, whose hypothesis is exactly what a `3x+d` cycle breaks (my review of [`finite-anchor-history-classification`](../finite-anchor-history-classification/README.md)). Nothing here excludes a `3x+d` cycle.

## What I did not check

- R75's plans `J_p`, `J_b` and the vectors `A_p − A_b` (the receipt's 54 plans) were not rebuilt; I used R75's rank bound. The two supplied-current demonstrations and the dispatcher sample `u = 8661` were not re-run.
- The legacy checker and the side-lane probe ran only inside the replay certificate.

## Findings

1. **§3 (imprecision).** "max(p, ν(b)) = p" uses `ν(b) = b`, i.e. that `b ≡ 9 (mod 16)` is canonical; stated nowhere, though (3) gives `ρ(b) = q`. Correct.
2. **Statement 4 and §4 (imprecision).** The lift is attributed to [`inverse-only-exclusions-short-forward`](../inverse-only-exclusions-short-forward/README.md) (status `written`), but §4 re-proves it in full through (13) at the anchor 11548, so the argument does not rest on that node's text; MAP.md's chain status understates what is proved here.
3. **§5 (typo/notation).** "`n = (6561q+8965)/1024 = 73993 modulo 128`" means `n ≡ 73993 ≡ 9 (mod 128)`; likewise "`f = 55495 modulo 32`". Missing spaces throughout the lightly edited legacy text ("absorbed at1", "modulo2048").

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
