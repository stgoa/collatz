# Review of mixed-rank-growing-blocks

## What I checked

- Certificate, from the repository root: `python3 tools/run_certificates.py --node mixed-rank-growing-blocks` gives `PASS check_legacy_replay.py (7s)`, exit code 0, 7.60 s wall (run twice, same result). [`check_legacy_replay.py`](check_legacy_replay.py) replays the unmodified `check_mixed_growth.py` in the pre-migration layout through `tools/legacy_replay.py`, requiring exit 0 and every copied file unchanged.
- Dependencies read as far as the argument needs: R25, R37, R40, R41, R43, R44 (returning interface and endpoint table), R51 (`σ`, uniform bound, fifth-exponent domain `w ≡ 437 (mod 512)`), R58 (unique excess), R62, R26.
- Constants and cylinder: `3^12 = 531441`, `2^19 = 524288`, `D = 7153`; `7153·40529845 + 311195 ≡ 0 (mod 2^26)`, and 40529845 is the least positive representative of `−B/D (mod 2^26)`. Every quantity in (2) is affine in `w` with denominator dividing `2^19`, and `n (mod 128)` needs exactly `w (mod 2^26)`, so the cylinder is the right modulus for the phases (3).
- Section 1 re-derived. With `t' = (3w+1)/32`: `S^4(q) = 162t' − 1`, `S^5(q) = (243t'−1)/2 = F(f)`, `S^6(q) = S(f)`, so `f = (243t'−3)/8 = (729w+147)/256` is the R26 `(5,3)` endpoint. `f ≡ 27 (mod 128)`, `f ≡ 0 (mod 3)` makes `f` canonical complementary (`a = 2`) and R58-exceptional (`f ≡ 27 (mod 48)`, `v2(3f−1) = 4`, `3z` selected for `z = (3f−1)/16`), with `u = 4z+1 = (3f+3)/4 = (2187w+1209)/1024` and `ρ(u) = (9f+5)/8 = (3u−1)/2 = R`; `u ≡ 21 (mod 512)`, `u ≡ 3 (mod 81)`, `3u+1 ≡ 64 (mod 1536)` give `u ∈ E` with exponent 6 and `σ(u) = 4u/3 − 1 = f`. The four offsets of (4) expand as displayed (`R − n = (85293w − 267217)/2^19 = (39u − 307)/512`).
- Section 2, the cancellation (7), re-derived. `b = f/3 ≡ 9 (mod 128)` lies in `W9` with `d = v2(9b−1) = 4`, so the R40 local plan is `Γ_b + H_R − H_h` with upper endpoint `6z+1 = (27b+5)/8 = R` and lower endpoint `h = 2z+1 = (9b+7)/8`. `y = S(b) = (f+1)/4 ≡ 7 (mod 32)` is canonical complementary; `S(y) = h ≡ 11 (mod 16)` is canonical with `h ≡ 2 (mod 3)`, so `H_h` starts with the inverse arrow back to `y`; hence `H_b = path(b→h) + H_h`, and `H_f = H_b + Γ_b + H_R − H_h = path(f→R) + H_R`, `A_f = A_R = {u:1} + A_u`. R44 at `u`: `R → r` by `1^4, 2`; `r ≡ 125 (mod 512)` gives `r = F(n)`, `n ≡ 31 (mod 128)` complementary, `n = 3v`, `v ≡ 53 (mod 128)` in `W5`, `n ≢ 27 (mod 48)` so `H_r = N_r + H_v` with requests `{v:1} + A_v` and all other ranks below `n < R`: ρ-valid. Adding the two plans cancels `N_(3u)` and `H_u`; the row `−e_f` of the block cancels `+e_f` of `path(f→R)`; what remains is the twelve rows `q → F(n)`, `N_r = e_(F(n)) − e_n`, and `H_v − H_w`, which is (5). Word: `(1,1,1,1,2)` to `F(f)`, `3` at `F(f)` (`v2(3F(f)+1) = 2 + v2(3f+1) = 3`), `2` from `S(f)` to `R`, `(1,1,1,1,2)` from `R` to `r`.
- Bound (8): `24M − 9A = 7799943 > 5422195 = 9B + 5M`, and `(9w+5)/8 < 3w` for `w ≥ 1`.
- Section 3: `Dw_(j+1) + B = A(Dw_j + B)/M` because `D + M = A`, giving (10); a copy stays in (1) while `v2(Dw_j + B) ≥ 26`, and each copy removes exactly 19 binary powers (A odd), which gives (11) and the exit range `7..25`; the word of (13) because `F` raises the first valuation by 2 and keeps the successor; `T^(12m)(3w_0) = ν(F(3w_m)) = 3w_m`.
- Section 4: the pigeonhole on `w_0 < ... < w_l` with `l` labels, heights `3w_j` strictly increasing by (10).
- Own script (standard library; own `ν`, `S` and my own implementation of the formal absorption plan `H_s` as a current with its signed `W5` request vector, R37 plan plus R40 elimination with endpoint assertions; `review-work/mixed-rank-growing-blocks/check_mixed_review.py`, outside the repository, 0.2 s). On 14 cylinder members (the twelve least and two with `w` near `2^56` and `2^74`): phases (3); classes (`q`, `n` complementary; `w`, `v` in `W5` outside `E`; `u` in `E`); ranks and (4) with the displayed offsets; the word (6); `S^13(q) = S(n)`; `T^12(q) = n`; the divergence of every plan used; (7) row for row and as request vectors; σ-validity of the first plan with `u` as its unique request of rank at least `q` (coefficient 1); ρ-validity of the R44 plan with `σ` rising from `f` to `n`; the combined current equal to `D_(q,n) + H_v − H_w` row for row, requests equal to `{v:1} + A_v − A_w`, `v` the unique request of rank at least `q`; (8). Phases, word, clocks and inequalities on 2012 further members. `f = 1371`: `R = 1543` and `A_f − A_R = {29: 1}` as retained. Repetition for `m` in `{1, 2, 3, 4, 6}` on three members of each progression: the copies lie in the domain, (10), (11) with exit valuation in `7..25`, the word of (13) and both clocks, and the telescoped request vector `{w_m:1} + A_(w_m) − A_(w_0)` for `m ≤ 3` with every other rank below `3w_(m−1)`. Guard count (11) and exit valuation on the 2999 members `40529845 + i·2^26`, `1 ≤ i < 3000` (all have count 1; the least member with two copies is `2218391138229`).
- Controls: not applicable. The construction uses `ν`, `F` and the halving identity, which exist for `3x+1` only, and nothing in the node excludes a cycle.

## What I did not check

- The theorems of the dependencies that the node invokes (R43 absorption bound, R58 excess classification, R44 endpoint table, R51 `σ` bound); my computations confirm their consequences on the tested members only.
- The internal counts of the legacy checker (16 macros, 12 prefixes, 27 families, 76 guard exits, 7 rejections) beyond the replay, and its stored unfinished currents.
- Telescoping of the currents (not only of the request vectors) for `m ≥ 2`; it follows formally from the block identity verified at each copy.

## Findings

1. Statement and claim: the absorption plan current is written `J_x` ("formal plans `[x] = div J_x + Σ A_x(v)P(v)`"), whereas R37, R40 and R43 write `H_x` and use `J_w` for a pair current of `P(w)`. The node defines its notation and is consistent internally. Imprecision (reading aid).
2. Section 1, "The sigma fifth-exponent rule at w is therefore valid": validity rests on R51's bound `σ(request) ≤ ν(f) = f < q` for the upper requests and `σ ≤ ν(w) < q` for the lower ones; both hold, and σ-validity was verified directly. No error.
3. No numerical or logical error found in (1) to (13) or in the pigeonhole of section 4.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
