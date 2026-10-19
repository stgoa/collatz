# Negative controls, an independent audit, and certificate minimality

17 October 2026. Companion to [`right_aligned_reduction.tex`](../../papers/right_aligned_reduction/right_aligned_reduction.tex).
Executables: [`affine_controls.py`](affine_controls.py), [`reduction_audit.py`](reduction_audit.py), [`main_claims_audit.py`](main_claims_audit.py), [`progress_measures_audit.py`](progress_measures_audit.py), [`attempt_probes.py`](attempt_probes.py).
Receipts: the matching `*.json` files in this directory.
Ledger entries: C1–C5 in `archive/docs/RESULTS.md`. The C-series is kept separate from the R-series used on main.

**Collatz remains unproved.** Nothing here constructs a universal current. This note:

1. tests the logic of R2–R4 on maps where the analogous conjecture is **false**;
2. records a scoped barrier showing which arguments cannot discharge the primary obligation;
3. proves conditional uniqueness and pointwise minimality for an exact comparison current; one-sided certificates need not be unique;
4. reports an independent re-audit of R2–R4 (no discrepancy found).

Status labels follow `AGENTS.md`: *written proof*, *finite certificate*, *observation* (finite data with no proof).

## 1. The maps T_d

For odd `d` with `3 ∤ d`, define `T_d(x) = (3x+d)/2^{v_2(3x+d)}` on odd `x ≥ 1`. When `d = 2^k − 3`, `T_d(1) = 1`. For `d > 1`, the point `d` is also fixed, since `T_d(d) = 4d/4 = d`. Write `A_d = {1} ∪ {d : d > 1}` for the trivial absorbing set. Here `d = 1` is the Syracuse map, and `d = −1` is conjugate to `3x+1` on negative integers.

We use the following objects:

- **Exceptional indicator.** `e_d(x) = 1` if the orbit of `x` ends in a cycle other than `{1}` or `{d}`, and `0` otherwise. It satisfies `e_d∘T_d = e_d` and vanishes on `A_d`.
- **Cutoffs and residues.** `n_0 = ⌊(N−d)/4⌋`, `n_1 = ⌊(3N+d)/2⌋`, `n_2 = ⌊(3N+d)/4⌋`, with residues `r_1 = 2d mod 3` and `r_2 = d mod 3`.
- **Source measure.** `ν_N^{(d)}` is supported on odd `x ≥ 3`, with component `i` contributing `3·1[x ≡ r_i (mod 3)] − 1` on `x ≤ n_i`. For `d = 1` this is exactly the source measure of the proof note.
- **Packets.** Within each component and valuation class, lifts form an arithmetic progression with step `2^{a+1}` in `x` and step `6` in the endpoint. Group lifts into right-aligned triples after dropping the single lift whose endpoint is 1. This gives `P ν_N = Π_N + η_N`, where `P` discards mass at 1.

At `d = 1` the independent construction in `affine_controls.py` reproduces the repository's `Π_N` and `η_N` exactly for every `8 ≤ N ≤ 3000` and for `N = 4096`. It also reproduces `η_N` at `N = 10001, 65537, 262144`.

### Lemma 1 (generic counting identity) — written proof; finite check

Let `B(u)` be the number of exceptional odd `x ≤ u`, and let `B_r(u)` count those with `x ≡ r (mod 3)`. Then

```
B(N) = B(n_0) + B_{r_1}(n_1) + B_{r_2}(n_2) + edge_d(N),
```

where `edge_d(N)` collects three kinds of terms:

- **added:** `e_d(x)` for the sources `x = 4z+d ≤ N` with `z < 0` odd;
- **subtracted:** `e_d(y)` for odd `y ≤ n_1` with `y ≡ r_1` and `(2y−d)/3 < 1`;
- **subtracted:** `e_d(y)` for odd `y ≤ n_2` with `y ≡ r_2` and `(4y−d)/3 < 1`.

All three are empty for `d = ±1`. For `d = 1` the identity is (6) of the proof note.

*Proof.* Partition the odd `x ≤ N` by `a = v_2(3x+d)`, and use `e_d(x) = e_d(T_d x)` throughout.

- **Valuation 1:** `x ↦ (3x+d)/2` is a bijection onto odd `y ≡ r_1` with `x = (2y−d)/3 ≥ 1`, and `x ≤ N ⟺ y ≤ n_1`.
- **Valuation 2:** likewise onto odd `y ≡ r_2` with `y ≤ n_2`.
- **Valuation ≥ 3:** these are exactly `x = 4z + d` with `z` odd. For `z ≥ 1` we have `3x + d = 4(3z + d)`, so `T_d(x) = T_d(z)` and `e_d(x) = e_d(z)`; also `x ≤ N ⟺ z ≤ n_0`. Sources with `z < 0` and `1 ≤ x` are added separately.

Images whose preimage would be `< 1` are removed. ∎

*Finite check:* `8 ≤ N ≤ 3000` for every surveyed `d`, and `8 ≤ N ≤ 20000` for `d = −1, 61`. In all of these `e_d ≢ 0`, so the check is **non-vacuous**. At `d = 1` the identity can only be tested with `e ≡ 0`. `reduction_audit.py` therefore also tests the `d = 1` valuation partition with orbit indicators `f_z(x) = 1[z ∈ orbit(x)]`. These satisfy `f_z(x) = f_z(Sx) + 1[x = z]`, which gives `B_f(N) = B_f(n_0) − 1[z ≤ n_0] + B_{f,5 mod 6}(n_1) + B_{f,1 mod 6}(n_2) + 1[z ≤ N]`. This was checked for `z ∈ {27,31,41,47,91,103}` and `8 ≤ N ≤ 4000`.

### Lemma 2 (pairing obstruction) — written proof

Let `P_A` push forward and discard mass landing in `A_d`. Suppose `Π = (I − P_A)J + ζ` with `J` and `ζ` finite and `ζ ≤ 0`. Then `⟨e_d, Π⟩ ≤ 0`. Moreover, if every atom of a finite `Π` reaches `A_d` or a cycle, then for all large `L`

```
H_L(Π) − H_{L−1}(Π) = ⟨1, P_A^{L−1} Π⟩ = ⟨e_d, Π⟩.
```

So the work grows exactly linearly with slope `⟨e_d, Π⟩`.

*Proof.* Since `e_d` is `T_d`-invariant and vanishes on `A_d`, `⟨e_d, (I−P_A)J⟩ = Σ_y J(y)(e_d(y) − e_d(T_d y)) = 0`. Hence `⟨e_d, Π⟩ = ⟨e_d, ζ⟩ ≤ 0`. For the slope, note `h_L(y) − h_{L−1}(y) = 1[τ_A(y) ≥ L]`. Once `L` exceeds every finite `τ_A` on the support, the surviving mass is exactly the mass on nontrivial-cycle orbits. ∎

A failure at `(d, N)` is certified finitely as follows:

- list the nontrivial cycles, checked by one step each;
- give each packet atom an explicit orbit into `A_d` or onto a listed cycle;
- check that `Σ Π_N(y)·1[orbit of y ends on a cycle] > 0`.

`check_obstruction` re-verifies such certificates using only `T_d`.

## 2. Results on the controls — finite certificates

The survey covers `8 ≤ N ≤ 3000`. Here "failing" means `⟨e_d, Π_N⟩ > 0`; by Lemma 2 no finite current with nonpositive residual exists there, and packet work grows linearly.

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

Full scans over `8 ≤ N ≤ 20000` give the following:

- **`d = −1`:** 14,474 failing cutoffs. The largest pairing is 40, at `N = 13540`.
- **`d = 61`:** 12,945 failing cutoffs. The largest pairing is 36, at `N = 15589`.

Three cutoffs per map carry full obstruction certificates, with linear work slopes verified by direct iteration:

| d | N | pairing | slope verified from L = |
|---:|---:|---:|---:|
| −1 | 16 | 1 | 4 |
| −1 | 9973 | 24 | 92 |
| −1 | 13540 | 40 | 110 |
| 61 | 213 | 1 | 51 |
| 61 | 13528 | 15 | 142 |
| 61 | 15589 | 36 | 142 |

**Observation (finite).** Two maps are "locally Collatz-like": every seed below 16 and every core point reach `A_d`. These are `d = 13` and `d = 61`. In both, the first failure occurs exactly at `N = ⌈(4r − d)/3⌉`, the cutoff where the least exceptional seed `r ≡ d (mod 3)` first enters component 2 with coefficient `+2`. This is asserted in the script for both maps; it is not proved in general.

## 3. What the controls show

**Consistency of R2–R4.** On every surveyed map where the analogous conjecture is false, the right-aligned criterion fails at some cutoff, as R3's logic requires. This is a test of consistency, not a proof of R3. The proof stands on the written argument, which was re-audited below.

**A scoped barrier.** `T_61` shares the following with `T_1`:

- multiplier 3 and the fixed point 1;
- the same packet construction and triple shape `(2,−1,−1)`;
- a fixed-core remainder whose core points all reach the trivial set, which gives the all-horizon control of R2;
- the counting identity (Lemma 1);
- no exceptional seed below 175;
- the bounded-work and nonpositive-residual forms of the obligation hold at **every** cutoff `8 ≤ N ≤ 212`. There is a single nontrivial basin, so per-basin pairings `≤ 0` give a finite current with nonpositive residual.

Yet the obligation fails at `N = 213`, by a finite certificate. Two consequences follow:

- **No generic proof.** No argument for the primary obligation can use only properties that `T_61` also has.
- **No generic induction.** An induction on `N`, or any local patching from smaller cutoffs, cannot succeed unless its inductive step uses arithmetic specific to `d = 1`. On `T_61` the hypothesis holds for every `N ≤ 212` and the conclusion fails at 213.

Because R3 is an equivalence, a valid proof must in particular exclude nontrivial cycles of `T_1`. That property fails for `T_13` and `T_61`. The `d = −1` control is weaker for this purpose, because its core is already exceptional.

## 4. The maximum principle is load-bearing — written proof

### Lemma 3

Let `r` be the least exceptional odd seed of `T_d`, and suppose `(2r−d)/3 ≥ 1`. Then `r ≢ 2d (mod 3)`. In particular, a least counterexample to Collatz satisfies `r ≢ 2 (mod 3)`.

*Proof.* If `r ≡ 2d`, then `x = (2r−d)/3` is an odd integer, `T_d(x) = r`, and `1 ≤ x < r`. Since `x` is exceptional, this contradicts minimality. ∎

**Consequence.** At `N = ⌈(2r−1)/3⌉` the proof note's "second check" evaluates `⟨e, ν_N⟩ = 3·1[r ≡ 2] − 1`. By Lemma 3 this is always `−1`. That contradicts an exact current, where the pairing must be `0`. It does **not** contradict bounded-above work or a nonpositive residual, where the pairing need only be `≤ 0`. The `N^{3/2}` maximum principle is therefore necessary for statements 2 and 4 of Theorem 3, not redundant. The audit found that argument correct.

## 5. Certificate minimality — written proof; finite check

### Lemma 4

Let `μ` be a finite signed measure on odd states. Suppose a finite exact current `J_0` exists, with `(I − P_A)J_0 = μ`. Let `(J, ζ)` be finite with `μ = (I − P_A)J + ζ` and `ζ ≤ 0`, and suppose `supp(J − J_0)` contains no cycle of `T_d` outside `A_d`. Then `J ≥ J_0` pointwise, so `‖J⁺‖_1 ≥ ‖J_0⁺‖_1`. In particular `J_0` is the unique exact current with that property.

*Proof.* Let `K = J − J_0`, so `(I − P_A)K = −ζ ≥ 0`. At `y ∈ A_d`, no mass arrives, so `K(y) = −ζ(y) ≥ 0`.

Now let `F⁻ = {y ∉ A_d : K(y) < 0}`. For `y ∈ F⁻`,

```
K(y) = −ζ(y) + Σ_{T x = y} K(x) ≥ Σ_{T x = y} K(x),
```

so some predecessor `x` has `K(x) < 0`, i.e. `x ∈ F⁻`. Since `F⁻` is finite, repeatedly choosing negative predecessors must revisit a state, which gives a cycle inside `supp K`. This contradicts the hypothesis, so `F⁻ = ∅`. For uniqueness, apply the lemma to `±K`. ∎

When every atom of `μ` terminates, `J_0 = Σ_j P^j μ` is the time-aggregated forward push. Lagged cancellations at merge points are automatically included, which is why `J_0` can stop at "exits" short of 1.

*Finite checks.* The archive's stored currents equal this forward aggregate **row for row**: 2,736 rows at `N = 4096` and 132,998 rows at `N = 262144`. Pointwise monotonicity was spot-checked on 60 random nonnegative perturbations at `N = 32, 100, 513`.

**Corrected scope after review.** The lemma supplies a cost lower bound relative to a finite exact current under its stated hypothesis. It does not imply uniqueness of one-sided certificates or eliminate structural certificate searches. For example, `mu=delta21-delta3` has exact current `J_0=delta21-delta3-delta5`, while `J=delta21-delta3`, `zeta=-delta5` is a different one-sided certificate. Both attain minimum positive cost1. The actual annulus A_768 likewise has an alternative of the same minimum cost with the row at5 removed. Full identities and receipts are in [PR1_REVIEW.md](PR1_REVIEW.md).

When every source terminates, the finite canonical exact current is the forward aggregate. Without that hypothesis, a formal infinite sum is not automatically a finite current, and synchronous pushforwards need not extinguish after unequal-time cancellations. The programme permits one-sided certificates obtained before all source futures are known. Describing the canonical exact currents is a possible sufficient route; it is not a requirement on every allowed constructor. The no-cycle condition also remains necessary for the lemma's stated pointwise domination and exact uniqueness conclusion.

## 6. Independent audit of R2–R4 — finite checks; no discrepancy found

The checks below use the generic construction, not the repository code.

| Item | Check | Range |
|---|---|---|
| Theorem 1 (3) | `3E_T(N) − H_{T−1}(Π_N) = ⟨1, ν_N⟩ + H_{T−1}(η_N)` exactly, with `E_T` built from `Q_T` and `R_{r,T}` as defined | every `8 ≤ N ≤ 160` and every `T` up to extinction; largest gap 17, within `8 + 30b` |
| Theorem 1 (2) | `supp η_N ⊆ {5,7,11,13}`, `‖η_N‖_1 ≤ 6b` | every `N ≤ 10^5`, plus 3,132 sampled `N` up to `10^18` (including `2^b ± 1, 2^b + 3`) |
| (7) dyadic table | period-6 core remainder; transfer correction in `[−12, 1]` | `b = 3 … 1500` |
| Lemma 2 (`505/512`) | ratio bounds algebraic for `N ≥ 16`; numeric maximum ratio 0.96751 | `16 ≤ N ≤ 2·10^4` |
| (6) partition | non-vacuous orbit-indicator test (Lemma 1 above) | `8 ≤ N ≤ 4000` |
| least-exception arithmetic | `n_1 ∈ {r, r+1}`, `n_2 < r`; Lemma 3 predecessor | odd `r ≤ 10^6` |

I re-derived the written arguments of Theorems 1 and 3 and found no gap. The checked points were:

- the valuation-partition bijections;
- the large-valuation tail (`S(x) < 3` and `3 ∤ S(x)` force `S(x) = 1`);
- the telescoping in "4 ⇒ 2";
- the limit (5);
- the maximizer argument.

This is a careful model-assisted review, **not** human peer review or formal verification.

## 7. Data for the constructor lane — observations

Over all 255 tested cutoffs (`8 ≤ N ≤ 256` and `N = 384, 512, 768, 1024, 1536, 2048`), the extinction time of `P^j Π_N` equals the largest stopping time among packet atoms. Synchronous pushing never cancels the slowest trajectories early. All savings in `J_N` come from time-aggregated (lagged) cancellation.

The true all-horizon work `W(N) = sup_L H_L(Π_N)` compared with the forced certificate cost `‖J_N⁺‖_1`:

| N | 8 | 32 | 128 | 256 | 384 | 512 | 768 | 1024 | 1536 | 2048 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| W(N) | 2 | 57 | 123 | 258 | 338 | 193 | 65 | 8 | 76 | 12 |
| ‖J_N⁺‖_1 | 2 | 71 | 174 | 411 | 643 | 619 | 551 | 851 | 1710 | 1909 |

The full table is in `reduction_audit.json`. `W(N)` is small at dyadic `N`, consistent with the exact formula (8). The forced cost is not.

## 8. Using the checker

```sh
python3 collatz_research_20261017/negative_controls/affine_controls.py --check CERT.json
```

`CERT.json` has the form `{"d": 1, "N": 32, "J": {"5": 2, ...}, "zeta": {...}}`. The checker rebuilds `Π_N` independently and returns exit status 0 if and only if `Π_N = (I − P_A)J + ζ` with `ζ ≤ 0`.

A constructor or checker should be run on the controls as well. Any claimed certificate for `d = 61` at `N = 213`, or for `d = −1` at `N = 16`, is necessarily wrong. A deliberately buggy "drop the leftover positive mass" certificate for `(61, 213)` is rejected.

## 9. Limitations

- **Finite ranges.** Controls are finite certificates on finite ranges. The survey uses `N ≤ 3000`; the full scans use `N ≤ 20000`.
- **Unresolved orbits.** Orbits are followed until they reach a cycle. An orbit exceeding `2^64` raises an error rather than being guessed; none occurred.
- **The barrier is scoped.** It rules out arguments that apply verbatim to `T_61`. It says nothing about arguments that use `d = 1`-specific arithmetic.
- **Maximum principle for d ≠ 1.** The `N^{3/2}` contraction is not claimed for `d ≠ 1`, because the cutoff offsets change the constants. The control failures are certified directly instead.
- **Lemma 4 assumptions.** Lemma 4 assumes no nontrivial cycle inside the finite difference support. For `d = 1` this is checkable for any explicit certificate.

## 10. Cross-audit of main's five-ray criterion and annular recursion

Main commit `8d62dcc` added two results. `main_claims_audit.py` checks both using only the construction in this directory.

**Five rays (main's R5).** For every `a ∈ {12,14,16,18,21}` and `3 ≤ b ≤ 400`, the script checks:

- the exact cutoffs `(n_0,n_1,n_2) = (M/4−1, 3M/2, 3M/4)`;
- the upper targets `M' ≥ 3M/2` and `M'/2 ≥ n_2`;
- the comparison exponents `5(b+s)+j − (5b+i) = 3` and `F(M/4) = 2^{−10/3}F(M)`;
- that every target with exponent below 3 lies below 96.

The constant uses `2^{10} > 10^3` and `2^5 > 3^3`, which give `λ_5 < 89/90`. I re-read the written maximum-principle argument on the grid and found no gap.

**Annular recursion (main's R6).** For 68 cutoffs `N ∈ {8, 16, …, 512, 768, 1024, 2048, 4096}`, the script checks that `Π_{64N} − Π_N` matches the stated six-band table modulo 18 at every odd endpoint in `(Q, 64Q)`. It also checks:

- `η_{64N} = η_N`;
- `supp Π_N ⊂ (1, Q)`;
- band totals are zero;
- `Σ A_N = 0` and `Σ y·A_N(y) = 63Q`;
- `‖A_N‖_1 = 99N/2`, `‖A_N⁺‖_1 = 99N/4`, and `|supp A_N| = 267N/8`.

**Controls on the grid.** Restricted to the 39 five-ray cutoffs `≤ 20000`, the criterion still fails on both false analogues:

- `d = −1`: 24 grid failures, the first at `N = 96`;
- `d = 61`: 23 grid failures, the first at `N = 224`.

This is a consistency observation only. The five-ray inclusions use `d = 1` offsets and do not transfer verbatim to these maps.

**Relation to main's R7.** Main's graph theorem characterizes when exact and one-sided currents exist through orbit-component masses. Its negative-integer example overlaps the `d = −1` control here. Three things here are not in main's notes:

- the locally Collatz-like controls `d = 13, 61`;
- the induction barrier;
- the uniqueness and minimality of Lemma 4.

Main's per-packet row lower bound and Lemma 4 are complementary. Every certificate dominates the forced current pointwise, and that forced current is itself large for individual packets.

## 11. Progress measures do not separate 3x+1 from 3x+61

Main commit `ce56699` measures partial progress on the annuli `A_N` in two ways:

- **(R9)** a one-pass root compression with exact norm `171N/4 − |c_N| ≤ (19/22)‖A_N‖_1`;
- **(R10)** the exposure potential `Φ`, the positive mass of exposed components not containing 1.

The main open obligation there is to prove that every positive `Φ`-plateau ends.

**Cross-audit (finite checks).** `progress_measures_audit.py` reproduces these claims with the construction in this directory:

- the R9 norm formula and `‖R A_N‖_1 = ‖P A_N‖_1` for 68 cutoffs `N ≤ 4096`;
- the `2N` positive survivors `p ≡ −1 (mod 36)` in `(32Q, 64Q)`;
- `c_80000 = 0`, by an independent point evaluator for `Π_N(y)`;
- the R10 trace `Φ(A_96) = 17` at exposure depths 20–27 and `0` at depth 28.

**Control (finite certificates).** For `T_61`, consider the 64-fold increments `A'_N = Π'_{64N} − Π'_N` at `N = 8, 16, 24, 32`. Their exact behaviour is in `progress_measures_audit.json`.

| N | ‖A'_N‖_1 | one-pass ratio ‖P A'‖/‖A'‖ | Φ at depth 0 | Φ at depth 25 | Φ at depth 400 | permanent mass |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 460 | 0.863 | 228 | 7 | 7 | 7 |
| 16 | 864 | 0.855 | 431 | 16 | 13 | 13 |
| 24 | 1264 | 0.849 | 630 | 16 | 13 | 13 |
| 32 | 1660 | 0.853 | 829 | 10 | 6 | 6 |

For comparison, the d=1 ratio is `19/22 ≈ 0.864`.

In every case the surviving positive component contains the whole 41-cycle `235 → …`. The cycle is closed under `T_61`, so no further exposure can join it to an absorber, and `Φ` is constant from then on. The permanent mass equals the pairing `⟨e_61, A'_N⟩`.

**Consequence.** One-pass contraction near `19/22`, and a rapid early fall of `Φ` by roughly 97%, both occur on a map where the plateau never ends. These statistics are therefore not evidence that `3x+1` plateaus end. A proof of the progress obligation has to use some property of `3x+1` that `T_61` lacks (Section 3).

*Observation, not a check in the receipt:* the in-progress transport numbers in main's working copy at 18:00 were also reproduced:

- `‖P^k A_96‖_1 = 4752, 4103, 3533, 3124` for `k = 0…3`;
- `P^79 A_96` and `P^80 A_96` both have norm 13 and positive mass 4;
- `R P^78 A_96` equals their nine-row table.

## 12. A direct attempt on the annular obligation, and why it stops

This section records a time-boxed attempt to prove the five-ray obligation using main's results (R5–R13) together with C1–C4. **No proof was found.** The section records what the attempt rules out.

### 12.1 High-level annihilation fails — finite certificates

The plan was to show that the positive and negative mass of `A_N` cancel above some height `Q/C`. That would make the bottom of the dynamics irrelevant and leave an almost scale-free problem.

For the canonical exact current `J_N = Σ_j P^j A_N`, at the six sampled cutoffs `N = 96, 168, 384, 768, 1536, 3072`:

- `J_N` reaches state 5 in every case;
- its signed traffic into 1 is nonzero through several entry states;
- that traffic grows with N: at `N = 3072` it is `−136` through 5, `+146` through 341, plus smaller terms (receipt `attempt_probes.json`).

These six exact currents do not cancel entirely before the bottom. This does not require every one-sided certificate to retain those rows: the A_768 counterexample in the PR review removes the row at5 with unchanged positive cost. It also does not exclude paying for a verified finite core in a different construction.

The six observed positive costs are approximately `75N`, about 3 times the source positive mass. This is finite data, not a proved universal linear bound. In these examples most mass cancels within a few steps and some signed traffic reaches1.

### 12.2 Class-wise equivalence — written proof

**Corollary.** Let `K` be a set of odd positive integers with `x ∈ K ⟺ S(x) ∈ K` for `x > 1`, `1 ∉ K`, and `K ∩ [1, 12096) = ∅`. Then the following are equivalent:

- (a) `K = ∅`;
- (b) `⟨1_K, Π_M⟩ ≤ 0` for every `M` in main's five-ray grid `G_5`;
- (c) `⟨1_K, A_N⟩ ≤ 0` for every increment on main's 30 sequences `N = a·2^r·64^k`.

*Proof.*

- **(a) ⇒ (c)** is trivial.
- **(c) ⇒ (b).** Along a sequence, `Π_{N_k} = Π_{N_0} + Σ_{i<k} A_{N_i}`. The pairing `⟨1_K, Π_{N_0}⟩ = ⟨1_K, ν_{N_0}⟩` vanishes, because `ν_{N_0}` lives below `3·5376/2 < 12096`. Here `1_K` is invariant and vanishes on the core and at 1. Every grid point lies on one of the 30 sequences.
- **(b) ⇒ (a).** Main's five-ray maximum principle uses only three facts about the exceptional indicator: the counting identity (valid for any invariant indicator vanishing at 1 and on the core), monotonicity of the count, and vanishing below 96. All three hold for `1_K`. ∎

If 3x+1 has a nontrivial cycle, the basin of that cycle is such a `K`, by the repository's finite base checks. If it has divergent orbits, the union of their basins is such a `K`. So the packet obligation is equivalent, class by class, to the two classical problems — no nontrivial cycles and no divergent orbits — each at full strength. It gives no separate leverage on either one.

*Finite check on controls.* For `T_−1`, `T_5` and `T_13`, each of the 14 nontrivial cycle basins separately has a positive pairing at some cutoff. That cutoff is usually close to the basin's least seed (`attempt_probes.json`). This is a check on controls, not on 3x+1.

### 12.3 Why the attempt stops

The tested ingredients do not yet close the universal obligation:

1. **Exact-current minimality is conditional (C3)**, and the six sampled exact currents carry traffic into1 (12.1). One-sided alternatives remain available.
2. **Each orbit class must be excluded separately**, at full strength (12.2).
3. **Generic arguments are ruled out (C2, C4).**

One possible direction is d=1-specific self-similarity (main's R6), together with a proved rule for continuing unresolved components. This is not an exhaustive classification of possible proofs.

- `T_61` has no exact `×64` recursion, so it does not satisfy the first ingredient.
- The negative integers fail the third ingredient, since they have small cycles.

But main's source recurrence contains the expanding `3N/2` term, and every exceptional status propagates upward along valuation-1 climbs. An induction on scale therefore never closes without controlling climbs, and controlling climbs is the classical problem.

**Conclusion.** Proving the five-ray obligation is equivalent, with no change in strength, to proving the Collatz conjecture.
