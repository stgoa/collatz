# Review of binary-kernel-first-ternary-image

## What I checked

- Every identity of the Proof, re-derived (below): (1), (2), the display `h(3u) = h(9u+1) = h(12u+1) = h(16u+1)`, (4), the two cases (5) and (6) of the Proposition (3), the chain behind (7), the finiteness (8) and the four section equations (9); the control sequences of section 5 (binary digit-sum parity, the mod-8 character `g`) and the `3x+d` remark of section 6.
- The arithmetic of (5) and (6) for all `a <= 8`, `0 <= r < 2^a`, `j < 3` (1,022 nondivisible and 511 divisible cases: `t` odd, `1 <= t < 2^(a+v)`, `3(2^(a+v) n + t) + 1 = 2^v (3 2^a n + c)`; respectively `0 <= t < 2^a`), and the chain of (7) for `t <= 6` and odd `u < 40` (`3 m_i + 1` and `4 m_i + 1` with `m_i = 4^i 3^(t-i) u`). Own code, not committed.
- Certificates: none listed. The evidence certificate `../digit-count-invariant-colourings-constant/verify_examples.py` (key `kernel_arithmetic` of its receipt: 762 divisible-index checks, 1,524 nondivisible actual branches, pure-zero orbits for `t <= 12`) was re-run with `python3 tools/run_certificates.py --node digit-count-invariant-colourings-constant`: both scripts of that node PASS, exit 0, 2 s and 0 s (wall 2.85 s).
- Controls, own code: the "which cycle" colourings `c_5` (labels 1, 5, 19, 23, 187, 347) and `c_13` (10 labels) of `3x+5` and `3x+13`, built as the area's `automatic_rigidity_control.py` builds them and verified invariant under `x -> 2x` and odd `x -> 3x+d` up to `1.2 * 10^5`. The `d = 1` identities fail on them, as section 6 predicts: on `c_5`, (1) at `m = 1`, (2) at `m = 1`, `h(3u) = h(16u+1)` at `u = 3`, (4) at `n = 1`, (7) with `t = 1` at `u = 3`; on `c_13` at `m = 3`, `m = 6`, `u = 7`, `n = 3`, `u = 7`. In particular `T_1 h` differs from `B_(2,1) h` and `T_2 h` from `B_(1,1) h` there. The `d`-forms hold with no failure in the tested ranges: `h(3m+d) = h(4m+d)` (the identity section 6 names), `h(3m + (d+3)/2) = h(2m+1)`, `h(3u) = h(16u+d)` for odd `u`, and `h(3^t u) = h(4^(t+1) u + d)` for `t <= 3`. The equations (9) use doubling only and hold on `c_5` and `c_13` for `t <= 2`.
- Links and frontmatter after converting the node to a folder.

Key derivations. (1): for `m >= 1`, `4m+1` is odd and `> 1`, so `h(4m+1) = h(12m+4) = h(3m+1)`; `m = 0` reads `h(1) = h(1)`. (2): `h(2m+1) = h(6m+4) = h(3m+2)` for `m >= 1`, and `h(2) = h(1)`. For odd `u >= 1`, `3u` is odd and `> 1`, so `h(3u) = h(9u+1)`, then (1) at `m = 3u` and at `m = 4u`. (4): `f_1(2n) = h(6n) = h(3n)` and `f_1(2n+1) = h(3(2n+1)) = h(16(2n+1)+1) = h(32n+17)`; so a binary section of `f_1` with offset `2^k (2m+1)`, `k < a`, equals `n -> h(2^(a-k+4) n + 32m + 17)`, a member of `K`, and offset 0 returns `f_1`. (5): with `c = 2^a j + r` and `3` not dividing `c`, `t = (2^v c - 1)/3` is an odd integer with `1 <= t < 2^v c/3 < 2^(a+v)`; `x = 2^(a+v) n + t` is odd and `3x + 1 = 2^v (3 2^a n + c)`, so `h(3 2^a n + c) = h(x)` (at `x = 1` this is `h(4) = h(1)` or `h(2) = h(1)`). (6): `3 | c`, `t = c/3 < 2^a`, and `h(3(2^a n + t)) = f_1(2^a n + t)` lies in `K` or equals `f_1` by (4). (7): `h(3^t u) = h(3^(t+1) u + 1)` (odd source `3^t u`, or `h(4) = h(1)` when `t = 0`, `u = 1`), then (1) at `m_i = 4^i 3^(t-i) u` for `i = 0, ..., t`. (8): `f_t(n) = f_t(oddpart n)` and `f_t(0) = h(1)` for every `t`, so `f_t` is determined by its odd section `n -> h(2^(2t+3) n + 2^(2t+2) + 1)`, a member of `K`. (9): `u_t(2n) = f_t(6n+1) = b_t(3n)`, `u_t(2n+1) = f_t(6n+4) = f_t(3n+2) = v_t(n)`, `v_t(2n) = f_t(6n+2) = u_t(n)`, `v_t(2n+1) = f_t(6n+5) = b_t(3n+2)`. Control `g` of section 5: multiplication by 3 sends `1, 3, 5, 7 (mod 8)` to `3, 1, 7, 5`, so `g(3n) = g(n)`; `g(3) = +1` and `g(10) = g(5) = -1`, so `g(3*3+1)` differs from `g(3)`; the non-periodicity argument (`oddpart(c 2^k + P) = m (mod 8)` for `k > a+3`) is right.

## What I did not check

- Cobham's theorem (mentioned only hypothetically in section 5; the claim does not use it).
- The literature statements of section 6 (no novelty is claimed).
- Equality of entire sections on `c_5` and `c_13` beyond the tested ranges; the controls only need a failure, which is exact.

## Findings

1. Imprecision (claim, section 1): "`h` finite-valued" and "`K` finite (binary automaticity)" are hypotheses no displayed identity uses. (1)-(7) and the Proposition (3) hold for every invariant colouring with any value set, and (8) is trivial when `K` is infinite. Harmless; the finite case is the one the node is about.
2. Imprecision (section 3): "`0 <= t < 2^(a+v)`" for the offset in case (5); in fact `t >= 1`, since `t` is odd, which is what membership in `K` with the stated offset range needs. Nothing uses `t = 0`.
3. Cross-reference (section 5): Cobham's theorem is linked to an external publisher page rather than to the source node [`cobham-recognizability-theorem`](../../../../sources/cobham-recognizability-theorem.md). The claim does not use Cobham, so no `assumes` entry is needed; a link to the source node would follow the repository convention. Not changed here.
4. Housekeeping: the `evidence` paths were written relative to a folder (`../digit-count-...`) while the node was a single file; after this review's folder conversion they resolve.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
