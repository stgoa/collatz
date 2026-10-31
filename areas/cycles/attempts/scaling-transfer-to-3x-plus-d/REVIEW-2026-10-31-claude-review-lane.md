# Review of scaling-transfer-to-3x-plus-d

Independent review of the attempt. Scope: the covariance `S_d(dy) = d·S_1(y)` of the odd-only maps, `gcd(d, 6) = 1`, what it transports and what it does not; the verdict that covariance alone cannot confine `d` to a finite base region. The question for an attempt is whether "Why it fails" and "What survives" are correct and claim nothing unproved.

## What I checked

- Read `AGENTS.md`, `conventions/SCHEMA.md`, `conventions/NOTATION.md` §3, `CONTRIBUTING.md` ("Review a node"), `areas/cycles/OVERVIEW.md`, the node, its dependencies [`mechanical-word-exact-denominator`](../../results/mechanical-word-exact-denominator/README.md) and [`mechanical-cycles-high-rational-controls`](../../results/mechanical-cycles-high-rational-controls/README.md) (both formal), the statements of the convergence nodes it cites (R23 [`halving-coalescence-return`](../../../convergence/results/halving-coalescence-return/README.md), R40 [`critical-nine-elimination`](../../../convergence/results/critical-nine-elimination/README.md), R54 [`growing-prefix-unhandled-leading-input`](../../../convergence/results/growing-prefix-unhandled-leading-input/README.md)), and the pinned review [`side_lane_review_678e565.md`](side_lane_review_678e565.md) for context.
- **Certificate.** `python3 tools/run_certificates.py --node scaling-transfer-to-3x-plus-d`: PASS, exit 0, 1.47 s wall; the receipt `transfer_3xd.json` was rewritten byte for byte (clean working tree afterwards). Its case counts 1000, 999, 998, 996, 984 and 16 families per `d` and 50,000 meeting pairs match the node's evidence text.
- **Covariance, re-derived.** `S_d(dy) = (3dy + d)/2^(v2(d(3y+1))) = d·(3y+1)/2^(v2(3y+1))` because `d` is odd; this needs only an odd denominator for `y`. Tested with exact rationals on 10,000 random positive `y` with odd denominator, `d ∈ {1, 5, 7, 13, 61}`: 0 violations, equal valuations.
- **The lattice statement.** Division by `d` sends `Z` to `d^(−1)·Z`; integer `S_1` inputs correspond to the multiples of `d`. Immediate.
- **Controls** `3x+5` (6 cycles), `3x+7` (2), `3x+13` (10), `3x+61` (3), from odd seeds `≤ 20000`, my own code: for every cycle the reduced denominator `den(w) = D_w/gcd(C_w, D_w)` divides `d`, `n_0 = d·C_w/D_w` exactly, and the rational point `C_w/D_w` follows the cycle's word under `S_1` and returns. This is the covariance in the integer direction and the "rational cycle controls" bullet: `C_w` is odd (its `j = 0` term is `3^(m−1)`, the others even), so `den·x_i` is odd and the valuations are exact; scaling by `den` gives an integer `3x+den` cycle.
- **Mechanical denominators.** `2^(A/g) − 3^(k/g)` spot-checked on 1,118 words `mech(A, k, l)`, `k ≤ 12`: 0 violations (the result is formal anyway).
- **W5 reformulation.** `w = 4u + 1` with `u` odd is `≡ 5 (mod 8)`; `3w + 1 = 4(3u + 1)` gives `S(w) = S(u)`; `9w + 1 = 2(18u + 5)` with `18u + 5` odd gives `S(3w) = 18u + 5`; verified for all odd `u < 2·10^5`. R40 says Collatz holds iff every `w ∈ W5` has a finite exact current for `[3w] − [w]`, i.e. the orbits of `w` and `3w` meet; after one step of each this is "the orbits of `u` and `18u + 5` meet", and conversely a meeting of `u`'s orbit with that of `18u + 5` passes through `S(u)`. The reformulation is correct given R40.
- **R23 halving** in its `d`-form on the certificate's cases (my code): 0 violations in 1000/999/998/996/984 cases; the selection `t·d^(−1) ≡ 3^a (mod 4)` is the `q = 1` condition `t ≡ 3^a (mod 4)` read on `y = x/d`, as the covariance predicts. R54: `2187 = 3^7` and `2048 = 2^11` match the word `(1, 1, 1, 2, 1, 1, 4)`; the certificate checks the family.
- **Catalogue.** `archive/side-lane/frameworks/rational_cycles.py` re-run in scratch: exit 0, 81 s; 3,889 cycles, the only integral one `{1}`, largest minimum `319/13`, as the pinned review records.

## What I did not check

- R40's equivalence itself (`critical-nine-elimination` is `written`, not reviewed); the W5 bullet is conditional on it.
- The exact derivation of `Ψ(q) = (2187q + 2363)/2048` beyond the certificate's exact check.
- Feed timestamps and the attribution of the withdrawal (01:31): provenance only.

## Findings

1. **Gap (certificate hygiene, no mathematical effect).** `transfer_3xd.py` performs every check with `assert`, guarded by `assert not sys.flags.optimize`; under `python3 -O` the guard itself disappears and the script passes vacuously. Demonstrated on a scratch copy with the selected class deliberately broken (`pow(3, a + 1, 4)`): it fails normally (exit 1, `AssertionError`) but exits 0 and prints `"status": "PASS"` under `-O`. `AGENTS.md` §6 requires certificates not to rely on `assert`. The runner uses plain `python3`, so CI does check. The script's source hash is pinned by the main lane's review, so I did not modify it; the authors should convert the asserts to explicit checks that `sys.exit(1)`.
2. **Imprecision ("What survives", third bullet).** "lists 3,889 such cycles for `k ≤ 9`" omitted the catalogue's bound on the total, `⌈k·log₂3⌉ ≤ A ≤ ⌈k·log₂3⌉ + 2` (`KMAX = 9`, `EXTRA = 2` in the script); without it the family is infinite. Corrected by adding the qualifier.
3. **Imprecision (metadata).** The W5 bullet rests on R40, linked in the text but absent from `depends_on`/`assumes`, so MAP.md does not show it. Left to the authors.

## Verdict

HOLDS WITH CORRECTIONS. Correction applied: finding 2. Findings 1 and 3 are recorded under History for the authors; no claim changes.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
