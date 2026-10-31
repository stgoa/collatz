# Review of failed-w9-leader-reduction

Independent review (Claude review lane, Fable 5.1), 2026-10-31. Notation as in the node: the critical basis of R75 (`J_s`, `A_s` unexpanded, requests in `W5 ∪ W9` of rank `≤ ν(s)`), the R40 local identity `P(w) = div L_w + Σ l_w(v) P(v)` without recursive W9 elimination, `d = v2(9w−1)`, `h`, `z`, `X = 6z+1`, `Y = 2z+1`, `u = 4z+1`. Recomputations use the review lane's own `S`, `ν`, `ρ`, currents and plans (`revlib.py`, checked against brute force), in `local_table.py` and `r84_window.py`.

## What I checked

- **Certificates.** `python3 tools/run_certificates.py --node failed-w9-leader-reduction`: both PASS, exit 0, 18 s wall (`check_w9_history_repair_recompute.py` 9 s; `check_legacy_replay.py` 9 s). The receipt's counts equal the evidence string (865, 72, 72, 72 repairs among 517 indices, 51 undos, 37 rejections, outputs of 166/49/61 rows).
- **Section 2, the table (by hand).** Odd `d`: `3z ≤ 3(9w−1)/32 < 27w/32 < 891Q/1024 < Q` since `864w < 891Q` is `32w < 33Q`. Even `d`: `z ≤ (9w−1)/16 < Q`; `Y` is safe: at `d = 4`, `Y ≡ 3 (mod 4)`, `≡ 2 (mod 3)`, canonical `Y` steps back to `(2Y−1)/3 = (3w+1)/4 < Q`, noncanonical `Y` is selected with `ν(Y) = z`; at `d ≥ 6`, `Y ≤ (27w+29)/32 < Q`. Upper endpoint: noncanonical `3z` makes `X` complementary canonical `≡ 1 (mod 3)` with first request `u = 4z+1` of rank `X` and the rest of rank `≤ ν(u) ≤ z`; canonical `3z` makes `X` its selected partner, continuing at `3z`: below `Q` nothing, complementary `≥ Q` requests `z` of rank `3z`, `3z ≡ 1 (mod 8)` steps to `f = (9z+1)/4 ≤ (81w+7)/64` (`≡ 1 (mod 3)`), where `f ≡ 1 (mod 8)` continues at `(3f+1)/4 ≤ (243w+85)/256 < Q` (this is `8019Q + 2720 < 8192Q`), noncanonical `f` has `ν(f) ≤ (f−1)/2 < Q`, and critical `f` requests `(2f+1)/3 = (3z+1)/2 < Q` at rank `f`. No other case exists, and no lower request can cancel a leader (all are `< Q`).
- **Table against actual plans.** 1290 pairs `(w, Q)`: the legacy-style exact-depth cells `w ≡ (1+2^d)·9^(−1) (mod 2^(d+1))` for `d = 4..20, 32, 64` (seven indices each), every W9 `w` in `[20009, 21033]`, 60 random 40-bit W9 inputs, with up to five thresholds each. In every case the requests of my `l_w` with rank `≥ Q` are exactly the table's prediction (`{leader: 1}` or none); all five kinds occur (440 noncanonical-upper, 63 complementary, 230 canonical-below, 57 forward, 500 odd). Whenever the leader is in W9 it is `z` and `16z < 9w`.
- **Section 3.** `16z < 9w` for even `d` from `z ≤ (9w−1)/16`; a high W9 child satisfies (3) (`32z < 18w < 33Q`); two consecutive ones would give `3w2 < 243w/256 < 8019Q/8192 < Q`. My own bounded repair on the 1290 cases: at most two substitutions (27 cases needed two), outcome strict in 940 cases and a single W5 leader with `+1` in 350; boundary re-checked with my divergence.
- **Section 4.** `w ≤ (R−1)/6 = 11706 + 3^13 k`; `33q − 32·(11706 + 3^13 k) = 6459 + 886176k`. Using the legacy R84 module for the leaders (`history_transition.plan`, a dependency, not under review): of 517 indices (`k < 512` and 869, 1062, 2917, `5 + 16·2^32`, `5 + 16·2^96`) exactly 72 fail with a W9 leader; each has `q ≤ 3w ≤ (R−1)/2`, `32w < 33q`, vector `{w: 1} + A_w − A_b` in my basis with every other rank below `q`; my repair agrees with the legacy `repair_failed` on every leader and status (47 strict, 25 with a W5 leader; 66 one substitution, 6 two). Examples: `k = 5` strict after one, `k = 38` after two; `k = 21` keeps 18839525 of rank 56518575 above `q = 33041691`; `k = 1062` keeps 1607200797 of rank 2410801195 above `q = 1670393115`. `k = 8`: `3w ≤ (raw−1)/4`, F stripping only. Cells (10): for `d = 4..30` the given `k` has `k ≡ 5 (mod 16)` and `v2(9w−1) = d` exactly.
- **Section 5.** For all 340 W9 `w < 2^14` with even `d` and noncanonical `3z`: `v3(X−1) = h+1 = D`, `4^D(X−1)/3^D + 2 = (9w+3)/2`, `v3 = 1`, R46's origin `2·((9w+3)/2)/3 − 1 = 3w`, word `1, 2^D` from `3w` to `X`; plan (11) has boundary `P(u)`; substitution into my `L_w` gives exactly `J_w − V − J_Y` and `{w: 1} + A_w − A_Y`, row for row; 148 of the 340 have a nonzero lower relation; `w = 201` gives 14 rows and `{201: 1, 25: 1, 5: 1}`.
- **Controls.** The local identity's first valuations `(1,2)` on `3w` and `(2,1)` on `w` hold for all 256 W9 `w < 2^12` under `3x+1` and for none under `3x+5` or `3x+13`; the node uses `3x+1` arithmetic only and excludes no control cycle.

## What I did not check

- R84's own construction and decision ([`later-target-twenty-step-descent`](../later-target-twenty-step-descent/README.md), `written`): the raw states being `≡ 1 (mod 3)` and `≤ R`, and the leaders, were taken from its legacy module; Statement 3 inherits that status.
- Supply of any terminal current (none is claimed).
- The receipt beyond the two certificates.

## Findings

1. (imprecision) Claim field: "decided completely by `d`, `z` and the canonicality of `3z` and of `f`" omits the three comparisons with `Q` (`6z+1 ≥ Q`, `3z ≥ Q`, `f ≥ Q`) that the Statement's table and the proof use. The Statement is exact.
2. (imprecision) Section 2, after (4): "the last strict inequality follows from (3) and `Q ≥ 11547`". It follows from (3) alone for every `Q ≥ 8` (`27·33/32 Q + 29 < 32Q`); the threshold is not needed there.
3. (note) Statement 3 rests on a `written` node (R84); within this node the window and the repair of every failed leader found by R84's code were verified.

## Verdict

HOLDS. The five-row decision, the two-substitution bound, the R84 window, the named examples and the row-for-row inverse undo were re-derived by hand and reproduced with independent code; both certificates pass. No correction to the text.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
