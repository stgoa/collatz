---
id: locally-collatz-like-control-barrier
kind: result
title: The packet criterion fails on 3x+d maps with cycles, including 3x+61, which looks like Collatz up to cutoff 212
status: reviewed
claim: >
  Odd-only maps T_d(x) = (3x+d)/2^(v₂(3x+d)), d = 2^k − 3, absorbing at A_d = {1} ∪ {d : d > 1}; Π_N^(d)
  the right-aligned packets built the same way. (i) Written: the exceptional count obeys the counting
  identity B(N) = B(n_0) + B_(r_1)(n_1) + B_(r_2)(n_2) + edge_d(N) (no edge terms for d = ±1); and if
  Π = (I − P_A)J + ζ with J, ζ finite and ζ ≤ 0, then ⟨e_d, Π⟩ ≤ 0, while ⟨e_d, Π⟩ > 0 forces packet work
  to grow linearly with that slope. (ii) Finite: for d ∈ {−1, 5, 13, 29, 61, 125, 253, 509} and
  8 ≤ N ≤ 3000 the pairing ⟨e_d, Π_N⟩ is positive at some cutoff; for d = 61 the criterion holds at every
  8 ≤ N ≤ 212 (all core points and seeds below 175 reach A_61) and fails first at N = 213 because of a
  41-cycle with minimum 235; full scans of 8 ≤ N ≤ 20000 give 14,474 failing cutoffs for d = −1 and
  12,945 for d = 61. (iii) Scoped barrier: no argument that uses only properties T_61 shares with T_1
  (including an induction on N from such properties) can prove statement 4 of qualitative-current-criterion.
authors:
  - Claude PR1 lane (Opus)
created: 2026-10-17
depends_on: [right-aligned-fixed-core-remainder]
certificates: [main_claims_audit.py, progress_measures_audit.py, attempt_probes.py]
evidence:
  - "NOTE.md: the PR1 lane's note (C1–C5), with the written proofs of Lemmas 1–4 and the corollary of §12; kept, links updated at migration"
  - "affine_controls.py, negative_controls_audit.json: the controls of this node and the certificate checker (python3 <this folder>/affine_controls.py --check CERT.json). Fails at the new path: it imports right_aligned_packets from its parent folder, which no longer holds it. Passed on 2026-10-17 inside the legacy gate scripts/verify_all.py --cpp, run in a temporary copy of the legacy layout (legacy archive/docs/RESEARCH_LOG.md)"
  - "reduction_audit.py, reduction_audit.json: the independent audit of R2–R4 and the minimality checks (right-aligned-reduction-independent-checks, exact-current-minimality). Fails at the new path: it reads ../collatz_packet_currents/data, now in packet-currents-snapshot/. Passed on 2026-10-17 inside scripts/verify_all.py"
  - "check_review_scope.py, review_scope_audit.json: the main lane's checker for the PR1 review's counterexamples (exact-current-minimality). Fails at the new path: it loads experiments/annular_construction/arithmetic/check_arithmetic_reductions.py relative to the repository root. Passed in the legacy gate (verify_all.py, everything passed at 9dbc71a per archive/legacy-checker-run-be73a66.md; at be73a66 the gate stopped earlier)"
  - "PR1_REVIEW.md: the main lane's review of the PR1 claims, with its later reassessments; HANDOFF_FOR_MAIN.md: the PR1 lane's hand-off to the main lane. Links into unmigrated legacy folders were turned into code spans at migration"
reviewed_by:
  - by: ChatGPT main lane (Codex)
    date: 2026-10-17
    link: PR1_REVIEW.md
    scope: "§1: C2 survives as a scoped logical barrier — a universal argument cannot rely solely on hypotheses also satisfied by a certified counterexample such as T_61; an inductive step must identify the extra arithmetic it uses. 'Not a prohibition on induction itself.' The combined verifier reproduced the receipts"
  - by: Claude side lane (Opus)
    date: 2026-10-17
    scope: "Feed 2026-10-17 19:03 (ACK: PR1 review accepted) and the TOOL entry: the controls (d, N) = (61, 213), (−1, 16) and the T_61 increments are adopted as regression tests for any generic argument or checker"
aliases: [PR1-C2]
tags: [convergence, packet-currents, negative-controls, 3x+d, barrier]
---

# The packet criterion fails on 3x+d maps with cycles, including 3x+61, which looks like Collatz up to cutoff 212

## Statement

For odd `d` with `3 ∤ d`, let `T_d(x) = (3x+d)/2^(v₂(3x+d))` on odd `x ≥ 1`. For `d = 2^k − 3`, `T_d(1) = 1`, and for `d > 1` also `T_d(d) = d`. Put `A_d = {1} ∪ {d : d > 1}`. `d = 1` is the Syracuse map; `d = −1` is conjugate to `3x+1` on the negative integers. These are the `3x+d` controls of [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §3, with absorption at `A_d` (the convergence area's convention).

- **Exceptional indicator.** `e_d(x) = 1` if the orbit of `x` ends in a cycle other than `{1}` or `{d}`, else 0. It is `T_d`-invariant and vanishes on `A_d`.
- **Cutoffs.** `n_0 = floor((N−d)/4)`, `n_1 = floor((3N+d)/2)`, `n_2 = floor((3N+d)/4)`, residues `r_1 = 2d mod 3`, `r_2 = d mod 3`.
- **Source and packets.** `ν_N^(d)` lives on odd `x ≥ 3`; component `i` contributes `3·1[x ≡ r_i mod 3] − 1` on `x ≤ n_i`. Within each component and valuation class, lifts form progressions with step `2^(a+1)` in `x` and 6 in the endpoint; dropping the single lift whose endpoint is 1 and grouping right-aligned triples gives `P ν_N = Π_N + η_N`, where `P` discards mass at `A_d`. At `d = 1` this is exactly [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md); the independent construction reproduces the repository's `Π_N` and `η_N` for every `8 ≤ N ≤ 3000` and `N = 4096`, and `η_N` at `N = 10001, 65537, 262144`.

**Lemma 1 (generic counting identity; written proof).** With `B(u)` the number of exceptional odd `x ≤ u` and `B_r(u)` those with `x ≡ r (mod 3)`,

```
B(N) = B(n_0) + B_(r_1)(n_1) + B_(r_2)(n_2) + edge_d(N),
```

where `edge_d(N)` adds `e_d(x)` for sources `x = 4z+d ≤ N` with `z < 0` odd, and subtracts `e_d(y)` for odd `y ≤ n_1`, `y ≡ r_1`, `(2y−d)/3 < 1`, and for odd `y ≤ n_2`, `y ≡ r_2`, `(4y−d)/3 < 1`. All three are empty for `d = ±1`; at `d = 1` this is (6) of [`qualitative-current-criterion`](../qualitative-current-criterion.md).

**Lemma 2 (pairing obstruction; written proof).** Let `P_A` push forward and discard mass landing in `A_d`. If `Π = (I − P_A)J + ζ` with `J, ζ` finite and `ζ ≤ 0`, then `⟨e_d, Π⟩ ≤ 0`. If every atom of a finite `Π` reaches `A_d` or a cycle, then for all large `L`, `H_L(Π) − H_(L−1)(Π) = ⟨1, P_A^(L−1) Π⟩ = ⟨e_d, Π⟩`: the work grows exactly linearly with slope `⟨e_d, Π⟩`.

**Finite certificates.** Over `8 ≤ N ≤ 3000` ("failing" means `⟨e_d, Π_N⟩ > 0`, so by Lemma 2 no finite current with nonpositive residual exists and the work grows linearly):

| d | nontrivial cycles (min:length) | least exceptional seed r | exceptional core points | failing N | first failing N |
|---:|---|---:|---|---:|---:|
| −1 | 5:2, 17:7 | 5 | 5, 7, 13 | 2668 | 16 |
| 5 | 19:3, 23:3, 187:17, 347:17 | 3 | 7, 11, 13 | 679 | 9 |
| **13** | 131:15, 211:5, 227:5, … (8 cycles) | **19** | **none** | 2348 | **21** |
| 29 | 11:9, 3811:41, 7055:41 | 3 | 5, 7, 11, 13, 17 | 2287 | 10 |
| **61** | **235:41** | **175** | **none** | 2607 | **213** |
| 125 | 10 cycles | 3 | many | 2375 | 42 |
| 253 | 7 cycles | 3 | many | 2930 | 8 |
| 509 | 5:142 | 3 | many | 1134 | 170 |

Full scans of `8 ≤ N ≤ 20000`: `d = −1` has 14,474 failing cutoffs (largest pairing 40, at `N = 13540`); `d = 61` has 12,945 (largest pairing 36, at `N = 15589`). Six cutoffs carry full obstruction certificates (explicit orbits of every atom into `A_d` or onto a listed cycle) with the linear slope verified by direct iteration: `(d, N, pairing, slope from L) = (−1, 16, 1, 4), (−1, 9973, 24, 92), (−1, 13540, 40, 110), (61, 213, 1, 51), (61, 13528, 15, 142), (61, 15589, 36, 142)`.

**Scoped barrier.** `T_61` shares with `T_1`: multiplier 3 and the fixed point 1; the packet construction and triple shape `(2, −1, −1)`; a fixed-core remainder whose core points all reach the trivial set; the counting identity; no exceptional seed below 175; and the bounded-work and nonpositive-residual forms of the obligation at **every** cutoff `8 ≤ N ≤ 212` (it has a single nontrivial basin, so per-basin pairings `≤ 0` give a finite current with nonpositive residual). Yet the obligation fails at `N = 213`. Hence no argument for statement 4 of [`qualitative-current-criterion`](../qualitative-current-criterion.md) can use only properties `T_61` also has, and an induction on `N` (or local patching from smaller cutoffs) must use arithmetic specific to `d = 1`.

## Proof

From `NOTE.md` §§1–3 in this folder, kept as written.

*Lemma 1.* Partition the odd `x ≤ N` by `a = v₂(3x+d)` and use `e_d(x) = e_d(T_d x)`. Valuation 1: `x ↦ (3x+d)/2` is a bijection onto odd `y ≡ r_1` with `x = (2y−d)/3 ≥ 1`, and `x ≤ N ⟺ y ≤ n_1`. Valuation 2: likewise onto odd `y ≡ r_2`, `y ≤ n_2`. Valuation `≥ 3`: these are exactly `x = 4z + d` with `z` odd; for `z ≥ 1`, `3x + d = 4(3z + d)`, so `T_d(x) = T_d(z)` and `e_d(x) = e_d(z)`, with `x ≤ N ⟺ z ≤ n_0`. Sources with `z < 0` and `1 ≤ x` are added separately; images whose preimage would be `< 1` are removed. ∎

*Lemma 2.* `e_d` is `T_d`-invariant and vanishes on `A_d`, so `⟨e_d, (I − P_A)J⟩ = Σ_y J(y)(e_d(y) − e_d(T_d y)) = 0` and `⟨e_d, Π⟩ = ⟨e_d, ζ⟩ ≤ 0`. For the slope, `h_L(y) − h_(L−1)(y) = 1[τ_A(y) ≥ L]`; once `L` exceeds every finite `τ_A` on the support, the surviving mass is exactly the mass on nontrivial-cycle orbits. ∎

*Certificates of failure* consist of the nontrivial cycles (each checked by one step), an explicit orbit from each packet atom into `A_d` or onto a listed cycle, and the check `Σ Π_N(y)·1[orbit of y ends on a cycle] > 0`; `check_obstruction` in `affine_controls.py` re-verifies them using only `T_d`.

*Barrier.* A valid proof of statement 4 must in particular exclude nontrivial cycles of `T_1` (statement 4 implies statement 1); that property fails for `T_13` and `T_61`, which share every listed property. The `d = −1` control is weaker for this purpose, because its core is already exceptional.

## Certificates

Each runs from the repository root in 1–2 s, standard library, checks by `assert` (run without `-O`), and rewrites its receipt byte for byte (checked at migration). They import `affine_controls` from this folder, but not its `main`, so they run although `affine_controls.py` itself does not.

- [`main_claims_audit.py`](main_claims_audit.py) → [`main_claims_audit.json`](main_claims_audit.json): the PR1 lane's cross-check of the legacy five-ray criterion and annular recursion (R5, R6; see [`right-aligned-reduction-independent-checks`](../right-aligned-reduction-independent-checks.md)), and the controls on the five-ray grid: `d = −1` fails at 24 of the 39 grid cutoffs `≤ 20000` (first at 96), `d = 61` at 23 (first at 224).
- [`progress_measures_audit.py`](progress_measures_audit.py) → [`progress_measures_audit.json`](progress_measures_audit.json): [`progress-measures-control-3x-61`](../progress-measures-control-3x-61.md).
- [`attempt_probes.py`](attempt_probes.py) → [`attempt_probes.json`](attempt_probes.json): [`class-wise-obligation-equivalence`](../class-wise-obligation-equivalence.md) and [`annular-bottom-cancellation-attempt`](../../attempts/annular-bottom-cancellation-attempt.md).

The table and scans above are in [`negative_controls_audit.json`](negative_controls_audit.json), written by `affine_controls.py`, which does not run at this path (see `evidence`).

## Remarks

- **Observation, not proved.** In the two locally Collatz-like maps `d = 13` and `d = 61` (every seed below 16 and every core point reach `A_d`), the first failure occurs exactly at `N = ceil((4r − d)/3)`, where the least exceptional seed `r ≡ d (mod 3)` first enters component 2 with coefficient `+2`. The script asserts this for both maps; it is not proved in general.
- **Scope.** The controls are finite (survey `N ≤ 3000`, scans `N ≤ 20000`); orbits are followed until they reach a cycle, and an orbit exceeding `2^64` raises an error (none occurred). The barrier rules out arguments that apply verbatim to `T_61`; it says nothing about arguments using `d = 1`-specific arithmetic. The `N^(3/2)` maximum principle is not claimed for `d ≠ 1`.
- **Consistency of the criterion.** On every surveyed map where the analogous conjecture is false, the criterion fails somewhere, as [`qualitative-current-criterion`](../qualitative-current-criterion.md) requires. This tests its logic; it does not prove it.
- **Use as regression tests.** Any constructor, progress argument or certificate checker should be run on `(d, N) = (61, 213)`, `(−1, 16)` and the `T_61` increment `A'_8`; anything that "succeeds" there is wrong. A deliberately buggy "drop the leftover positive mass" certificate for `(61, 213)` is rejected by the checker.
- **Relation to the legacy R7.** The main lane's component criterion (legacy R7, `experiments/current_construction/`, not yet migrated) characterises when currents exist through orbit-component masses; its negative-integer example overlaps the `d = −1` control. The locally Collatz-like controls and the induction barrier are not in the main lane's notes.
- Novelty undetermined.

## History

- Migrated from `experiments/packet_currents/negative_controls/` (legacy `NOTE.md` §§1–3, ledger entry C2 in `archive/docs/RESULTS.md`, legacy path) at commit `be73a66`, by the B07 migration (Claude, Opus 5.5). The whole folder moved here, because its scripts import each other; the alias is `PR1-C2`, not `C2`, to keep the PR1 series apart from the cycle series. Links in `NOTE.md` and `PR1_REVIEW.md` were updated (legacy targets not yet migrated became code spans).
- PR1 lane (Claude, Opus; branch `claude/claude-vs-chatgpt-perf-8230f6`), 2026-10-17, commit `b6f32b2`, merged into the main lane's `main` as PR1 (`ba6b337`). The C-series was kept apart from the main lane's R-series on purpose.
- 2026-10-17: the main lane reviewed PR1 (`PR1_REVIEW.md`, commit `2be37b7`); the controls and the barrier survived as scoped; the side lane accepted the review (feed 19:03).
