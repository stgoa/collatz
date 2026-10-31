# Review of finite-anchor-history-classification

Independent review of [`README.md`](README.md) (authors: ChatGPT main lane, Codex). Scope as in the node: odd-only `3x+1`, absorbing at 1, `T = νS` with the complete inverse branches of [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md). Own scripts (own `ν`, `T`, canonical test and inverse table, validated by brute force as described in my review of [`high-smaller-origin-history`](../high-smaller-origin-history/README.md)) live outside the repository; every number below comes from them or from the certificate.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node finite-anchor-history-classification`: PASS, exit 0, 1 s wall. `r82_anchor_lift_check.py` rewrites [`r82_anchor_lift_check.json`](r82_anchor_lift_check.json) byte-identically (clone clean). The legacy `check_history_frontier.py` is not a certificate (stale pin, as `evidence` says); I read it and `history_frontier.py` but did not run them.
- **Theorem 1, re-derived.** Shadow legality: `a_i − c_i = 2^(E_i)(y − Y)/3^i` is divisible by `3^(K−i)`, so actual and shadow states agree modulo 3 before every step `i ≤ K` and the branch outputs are integral canonical states. With `λ_i = αλ_(i−1)`, `c_i = αc_(i−1) + β`: `G_i = αG_(i−1) + (α − β − 1)/(Y+1)`, which is (3), and `G_i ≥ 0` from `α − β ≥ 1` (equality only at the point branch). From `y ≥ Y`: `a_i + 1 ≥ (c_i + 1)(y+1)/(Y+1)`, so `a_i < q` gives `c_i + 1 < C` and `c_i ≤ ⌈C⌉ − 2 = n`. The forward path of `c` is unique and meets `Y` once because `Q` is absorbing and `Y > 1`; the converse is the same divisibility read backwards. Machine check by **forward** brute force (not inverse trees, unlike the probe) on 300 random instances (canonical `Y < 3000`, `K ≤ 6`, canonical `y = Y + 3^K s`, `q < 5000`): the lift set, built from origins `c ≤ n` by iterating `T` with slopes `2^E/3^d` read off the actual edges, equals the set of canonical `a < q` with `T^d(a) = y` found by iterating every `a`; 143 instances nonempty, depths up to 6. Hypothesis control: with `y ≡ Y` only modulo `3^(K−1)` the sets differ (`Y = 967`, `y = 1147`, `K = 3`, `q = 2933`: the actual origin `(679, 3)` is missed), so the ternary congruence is needed as stated.
- **Statement 2.** `C(q) = (q+1)(Y+1)/(gq + h + 1)` is a Möbius function of `q`, so its supremum on `q ≥ b` is `max(b + 1, (Y+1)/g)`; for `j` valuation-one quotient steps from a complementary climber, `Y + 1 = (3/2)^j (b+1)` and `n = b − 1` (2250 instances). Contracting control: `465 → 43 → 65 → 49 → 9 → 7 → 11` under `T`, `T(497) = 11`, multipliers `2^15/3^6` and `2^7/3`; for `D ≤ 7` and five values of `t` the lifts (6) satisfy `T^6(q) = T(p) = y`, `p − q = 32 − 26624·3^D t < 0`, all canonical, `y ≡ 11 (mod 16)`; the bound is `393216/729`, cutoff `538 ≥ 497 > 464 = b − 1`, so the naive cutoff would miss the partner.
- **Statement 3.** Anchor table rebuilt from scratch (4892 states, 2887 origins, 11547 absent, equal to the stored table); the catalogue for `Y = 17321` is exactly `{(11391, 13)}` with the listed path and slope `2^20/3^13` (`E = 20` summed over the thirteen edges). For `D = 1..14` and `t ∈ {0, 1, 2, 5, 1000, random < 10^12}` (84 cases): `q, y` canonical, `q/3 ≡ 9 (mod 16)`, cutoff `11546`, `y − Y = 8·3^(D+1) t`; an independent inverse-tree search (pruning `x + 1 ≤ (3/2)^rem (q+1)`, at most 53 nodes) finds no origin for `D ≤ 11` and exactly `p = 11391 + 2^23·3^(D−12) t` at depth 13 for `D ≥ 12`, with `p < q`; the same search from `q` finds no ancestor `≤ q` within `D`. An exhaustive forward sweep (own C program, own `ν`) over all canonical `a ≤ q` agrees: for `D = 12`, `t = 1` (`q = 8514603`, `y = 12771905`, horizon 13; 2,128,652 states) the only hits are `a = 8399999 = 11391 + 2^23` at depth 13 and `q` itself at depth 1; for `D = 11`, `t = 1` (`q = 2845899`, `y = 4268849`, horizon 12; 711,478 states) only `q` itself at depth 1.
- **§4.** `div(δ_x + N_(S(x))) = [x] − [T(x)]`, hence `div K = [q] − [p]` and the rank bound from R75.
- **Controls** ([`NOTATION.md`](../../../../conventions/NOTATION.md) §3). For `3x+5` the origin 19 visits 31 at depths 1, 4, 7, 10, … (the cycle `19, 31, 49`): "at most one such path" is exactly the absorbing hypothesis the controls violate, so the theorem does not transfer to `3x+d` and excludes none of their cycles.

## What I did not check

- The receipt's two reconstructed supplied currents and the legacy checker (not a certificate).
- [`decreasing-w5-phase-inverse-barrier`](../decreasing-w5-phase-inverse-barrier/README.md) beyond the inverse table and `α − β ≥ 1`, which I re-verified.

## Findings

1. **Certificates (gap, hygiene).** [`r82_anchor_lift_check.py`](r82_anchor_lift_check.py) checks only by `assert` and rewrites its receipt instead of comparing with the committed one. On a scratch copy with `11391` changed to `11393`, `python3 r82_anchor_lift_check.py` exits 1 but `python3 -O r82_anchor_lift_check.py` exits 0. [`AGENTS.md`](../../../../AGENTS.md) §6 asks certificates not to rely on `assert`. `tools/run_certificates.py` runs without `-O`, so the recorded PASS is valid; the file is the side lane's probe and was not touched.
2. **§1 (imprecision).** "If `a_i < q`, then `c_i + 1 < C`": the proof actually gives `c_i + 1 ≤ q(Y+1)/(y+1)`, slightly sharper when `C` is an integer; harmless.
3. **§3 (imprecision).** "`y − Y = 8·3^(D+1)·t`" is correct, but the text does not say that this is why the horizon is `D + 1` (the theorem needs `y ≡ Y (mod 3^K)` with `K = D + 1`).

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
