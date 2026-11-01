# Review of signed-pair-frontier-normalisation

Independent review (wave 7). Definitions were followed into [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md) (`ν`, selected), [`valuation-debt-reset-obstruction`](../valuation-debt-reset-obstruction/README.md) (the reset family and its R44 frontier), [`returning-forward-interface`](../returning-forward-interface/README.md) and [`mixed-rank-growing-blocks`](../mixed-rank-growing-blocks/README.md). Every number below comes from my scratch code (outside the repository) or from the node's proof.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node signed-pair-frontier-normalisation`: PASS, exit 0, 13.7 s wall (`check_legacy_replay.py` replays `check_frontier_normal_form.py` unchanged; receipt byte-identical).
- **Identity I, re-derived.** With `w = (64u + 5)/9`: `3w + 1 = 8(8u + 1)/3`, integral and odd because `u ≡ 4 (mod 9)`, so `S(w) = (8u+1)/3` with valuation 3 and `S((8u+1)/3) = 4u + 1 = F(u)` with valuation 1; `3(3w) + 1 = 2(32u + 3)` and `3(32u + 3) + 1 = 2(48u + 5) = 2F²(3u)`. Telescoping the eight rows gives `[3w] − [3u] + [u] − [w]`. `u ≡ 5 (mod 8)` since `64u + 5 ≡ 5` and `9^(−1) ≡ 1 (mod 8)`; `3w = 2^3 t − 1` with `t = (8u+1)/3 ≡ 3 (mod 4)` is selected, so `ρ(w) = (3w − 1)/2 > 3u ≥ ρ(u)`.
- **Identity II, re-derived.** `3b + 1 = 16(48c + 1)` (`c` odd), `3(48c + 1) + 1 = 4(36c + 1)`, `36c + 1 = F(9c)`; `3(3b) + 1 = 2(1152c + 23)`, then `2(1728c + 35)`, then `2(2592c + 53) = 2F³(h)` with `h = (81c + 1)/2` odd (`c ≡ 5 mod 8` gives `81c + 1 ≡ 6 mod 8`) and `S(27c) = h`. Telescoping the ten rows gives (6); clocks `(3, 1)` and `(4, 2)`.
- **§2.** Guards `93` and `261 (mod 512)` are disjoint; `d(w) ≤ 9w/64`; (9) by induction from the padded one-edge identities; (11), idempotence, the potential inequality (13) and the kernel statement (14) (`V/R` is free on the terminals).
- **§3.** The composite slope is a power of 2, so (16) has one solution modulo `8·9^r`; integrality at inner stages by reduction modulo `9^(r−1)`; residues 4 and 0 modulo 9; for `x ≡ 5 (mod 8)` the parents land in the guards automatically (`64x + 5 ≡ 325 (mod 512)` and `325·9^(−1) ≡ 93`).
- **§4.** `a = 9c`, `b = 256c + 5` from `u = 648c + 13`; `u ≡ 437 (mod 512)` and `a ≡ 13 (mod 128)` from `c ≡ 101 (mod 128)`; (19); (20) from (21)–(22) by cancellation, using `2592c + 53 = 4u + 1` and `1728c + 35 = (8u + 1)/3`; the three lines of (21) are valid plans because `S(h) = S(u) = (243c + 5)/4` and `S(w) = S²(3b) = 1728c + 35`.
- **§6.** `40529845 ≡ 53 (mod 128)` and `V(w) ≡ 53 (mod 128)`; `53 (mod 128)` meets neither guard (`93` and `1285 ≡ 5 (mod 128)`); helpers lie below `v`, so (23).
- **Independent computation** (scratch `recompute_r73.py`, own `S`, `ν`, `ρ`, currents with the atom at 1 killed). Identity I on all 2048 `w ≡ 93 (mod 512)` below `2^20` and identity II on all 2048 `b ≡ 1285 (mod 2048)` below `2^22`: child arithmetic, both paths and valuation words, clocks, divergences, eight and ten distinct rows, `ρ` values, converses; the converses for every `u < 300000`. 300 random signed vectors: (11), idempotence, potential nonincreasing, every surviving index terminal; generators `e_w − e_d(w)` in the kernel. 20 random words of length 1–5: exactly one residue modulo `8·9^r`, every stage in `W5` and in its guard, the child map inverts each lift, padded clocks (9). Reset family for `H = 26..35`, three members each: `u ≡ 437 (mod 512)`, `c ≡ 101 (mod 128)`, `a ≡ 13 (mod 128)`, child map, (19), the auxiliary identities of (21). Identity (20) checked against the unmodified legacy R44 current (`valuation_debt.obstruction` in a copy of the pre-migration layout) for 16 members (`H = 26..33`, two each): frontier `{u: 1, a: 1, b: −1}` and `J_44 − C_II(b) = C_I(w)` row for row. R67: six members of the cylinder with `w ≡ V(w) ≡ 53 (mod 128)`, both terminal, `V(w) > w`.
- **Controls.** No cycle is excluded and nothing is claimed `d`-uniform; the identities are `3x+1` congruence identities, so the `3x+d` controls do not apply.

## What I did not check

- (21) from the definitions of the R41/R44 plans; it was checked against the implementation on 16 members and for divergence consistency only.
- The claims of [`mixed-rank-growing-blocks`](../mixed-rank-growing-blocks/README.md) beyond the residues used in §6.
- The 12 stored compressions and the 47 pinned sources, beyond the replay.

## Findings

1. §4 (imprecision): (21) is asserted ("the R41 recursion and elementary normalizers on this family give"); its derivation needs the plan routes described in [`valuation-debt-reset-obstruction`](../valuation-debt-reset-obstruction/README.md) §2 (`w → ν(w) → (3b−1)/2`, `u → ν(u) → 3a`). Consistent with the implementation on 16 members.
2. Statement item 3 (imprecision): the clocks `(2r+2, 2)` compare `w` with the end of the listed `r`-edge word, which may itself be reducible; §3 says so, the Statement does not.
3. §1 (typo): spaces and equality signs lost in the migrated text ("w93,u13", "c5,b1285,a45").

No error found.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
