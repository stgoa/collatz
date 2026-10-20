---
id: mechanical-word-exact-denominator
kind: result
title: "Mechanical valuation words have reduced denominator exactly 2^(A/g) − 3^(k/g), so none is a nontrivial integer 3x+1 cycle"
status: formal
claim: >
  Raw odd-only clock, no absorption. For integers 0 < k <= A and 0 <= l < k let mech(A,k,l) be the mechanical
  valuation word a_i = floor(((i+1)A+l)/k) - floor((iA+l)/k), i = 0..k-1, and g = gcd(A,k). Its reduced denominator
  D/gcd(C,D) is exactly 2^(A/g) - 3^(k/g) (D = 2^A - 3^k, C the word's intercept); in the primitive case g = 1, k >=
  2, gcd(C,D) = 1. When 2^A > 3^k this is the reduced denominator of every state of the word's positive rational
  cycle of the odd-only 3x+1 map, which is an integer cycle of 3x+d exactly when it divides d. Since 2^(A0) -
  3^(k0) = 1 is impossible for k0 >= 2 (modulo 8), the reduced denominator is 1 only for A = 2k, the all-2 word,
  whose cycle is the fixed point 1: no mechanical (Christoffel) word is a nontrivial integer cycle of 3x+1, at any
  length. Other periodic valuation patterns and aperiodic orbits are not addressed. Published antecedents (Knight's
  high-cycle theorem); no novelty claimed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: []
lean:
  - LeanLane.Cyc.den_mech
  - LeanLane.Cyc.den
  - LeanLane.Cyc.mech_gcd_one
  - LeanLane.Cyc.mech_gcd_one_phase
  - LeanLane.Cyc.mech_gcd_one_phase'
  - LeanLane.Cyc.mech_D_ne_one
  - LeanLane.Cyc.gcd_rotate_eq
  - LeanLane.Cyc.exists_unique_mech_jump
  - LeanLane.Cyc.C_mech_one_sub_zero
  - LeanLane.Cyc.mech_rep
  - LeanLane.Cyc.den_rep
  - LeanLane.Cyc.gcdCD_rep
certificates: [check_balanced_cycles.py, r71_mechanical_check.py, r71a_mech_gcd_check.py, r71b_den_mech_check.py]
evidence:
  - "balanced_cycles.py, balanced_cycles_audit.json: the main lane's exact Fraction module and the receipt of check_balanced_cycles.py (source hashes of both scripts, integer cycle tables for selected controls)"
  - "side_lane_review_13590c1.md, side_lane_review_13590c1.json: the main lane's pinned review (2026-10-18) of side commit 13590c1: byte-identical reproduction of r71_mechanical_check.py, with the floating-point bounds confirmed by integer bit lengths; also records the side lane's 01:31 transfer correction (see scaling-transfer-to-3x-plus-d)"
  - "The section 0 transfer remarks and the 3x+d controls are developed in ../../attempts/scaling-transfer-to-3x-plus-d/; the state bound of section 3 is mechanical-cycles-high-rational-controls"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: r71_mechanical_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 01:43, VERIFIED, main working copy), exact rational arithmetic and the lane's own iteration: every k <= 14, every A with 3^k < 2^A <= 2^(ceil(k log2 3)+6), every offset l (735 words): the rotation identity 3B_i + D = 2^(a_i) B_(i+1) with every B_i odd, exact valuations, reduced denominator 2^(A/g) - 3^(k/g) for every state; the only integral cases are the 105 all-2 words. Reproduced by the main lane in side_lane_review_13590c1.md"
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: r71a_mech_gcd_check.py
    scope: "Feed 2026-10-19 05:44 and 08:31, VERIFIED Lean R71-a and R71-b (statement match and receipts checked), with independent exact checks: gcd(C, D) = 1 on all 16,887 primitive phase words with m <= 40, m <= A <= 2m+7; (4) with a unique nonzero jump index on all 669 such (A, m); mech_rotate on 849,520 cases and gcd rotation invariance on 19,569 random words; the repeated case gcd(C, D) = D/(2^(A/g) - 3^(m/g)) on 6,109 phase words; den = 2^(A/g) - 3^(k/g) on every phase word with k <= 48 (8,232 with D > 0 and 22,828 with D < 0, r71b_den_mech_check.py), mech_rep and den(z^k) = den(z) on 3,000 random cases, the example (6, 10): D = 295, den = 5"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Lean units R71-a (iteration 36) and R71-b (iteration 48) verified in lean/CycleSpectrum.lean with the standard axioms; statement match recorded in the legacy lean/STATE.md (see Lean)"
    link: ../../../../archive/lean-lane/STATE.md
aliases: [R71, R71-a, R71-b]
tags: [cycles, mechanical-words, christoffel, denominators, formal]
---

# Mechanical valuation words have reduced denominator exactly 2^(A/g) − 3^(k/g), so none is a nontrivial integer 3x+1 cycle

## Statement

Raw odd-only clock, no absorption (`conventions/NOTATION.md` §2). For integers `0 < k ≤ A` and `0 ≤ l < k`, the **mechanical word** `mech(A, k, l)` has letters

    a_i = floor(((i+1)A + l)/k) − floor((iA + l)/k),     i = 0, …, k−1,

all positive, with total `A`; its intercept is `B_l = Σ_j 3^(k−1−j)·2^floor((jA+l)/k)` and `D = 2^A − 3^k`. Put `g = gcd(A, k)`, `A_0 = A/g`, `k_0 = k/g`.

1. **Exact denominator.** The reduced denominator `D/gcd(B_l, D)` of `mech(A, k, l)` is exactly

       d = 2^(A_0) − 3^(k_0).                                            (3)

   In the primitive case `g = 1`, `k ≥ 2`, `gcd(B_l, D) = 1`. When `2^A > 3^k`, `d` is the reduced denominator of every state of the word's positive rational cycle, which is an integer cycle of `3x+d'` exactly when `d | d'`.
2. **Integer cycles.** `2^(A_0) = 3^(k_0) + 1` is impossible modulo 8 for `k_0 ≥ 2`, so `d = 1` only when `k_0 = 1`, `A_0 = 2`, i.e. `A = 2k`: the all-2 word, whose cycle is the fixed point 1. No mechanical (Christoffel) word is a nontrivial integer cycle of `3x+1`, at any length.

This excludes exactly this word family. It neither excludes other periodic valuation patterns nor addresses aperiodic divergence. The rational cycles of the family sit arbitrarily far above the absorber, with `d` varying: [`mechanical-cycles-high-rational-controls`](../mechanical-cycles-high-rational-controls/README.md).

## Proof

The legacy note "R71 — Exact denominators for mechanical valuation words" follows, lightly edited (title dropped, headings demoted one level). Its §0 ("Why this matters for the side-lane transfer") is developed as the attempt [`scaling-transfer-to-3x-plus-d`](../../attempts/scaling-transfer-to-3x-plus-d/README.md); its §3 is the result [`mechanical-cycles-high-rational-controls`](../mechanical-cycles-high-rational-controls/README.md). Its command names the pre-migration path; the checker now runs from this folder.

**Status:** written elementary derivation and exact finite replay. This is a
restricted cycle result and a control family, not a Collatz convergence proof.
Related nonintegrality results are already published; no novelty is claimed.

### Why this matters for the side-lane transfer

For odd d coprime to3, the odd-only maps obey `S_d(dy)=d S_1(y)` on positive
odd rationals with denominator coprime to6. This correctly transports local
valuation identities. It sends the positive integer domain for S_d to
positive rationals in `d^(-1) Z`, not necessarily to integers for S_1.
Exact integrality can therefore distinguish whole words, at any height.
Covariance alone does not show that d can matter only in a finite base check.

Conversely, a proof intended to work on this entire rational domain must
cope with genuine positive cycles. Below we give controls with every state
above any prescribed constant, as well as the exact reason why this
particular family cannot be a nontrivial integer Collatz cycle.

### 1. General word identity and exact legality

Take k>=1 and a word of positive valuations `(a_0,...,a_(k-1))`. Let

```
A_j = a_0+...+a_(j-1), A_0=0, A=A_k,
B = sum_(j=0)^(k-1) 3^(k-1-j) 2^A_j,
D = 2^A-3^k.
```

The affine composition is `(3^k x+B)/2^A`. Suppose D>0. Its unique fixed
point is x=B/D>0. For the cyclic rotation starting at i, denote its
intercept by B_i; all rotations have the same D. Direct expansion gives

```
3B_i + D = 2^a_i B_(i+1),                (1)
```

with cyclic indices. Every B_i is odd, because its first summand is odd
and the others are even. D is odd and prime to3. Thus (1) proves the
**exact** valuation a_i, not merely divisibility by 2^a_i. The numbers
B_i/D form a genuine positive odd rational Syracuse cycle.

Since 2 and3 are units modulo D, (1) also proves that
`gcd(B_i,D)` is independent of i. The common reduced denominator is

```
d = D/gcd(B,D),                         (2)
```

which is coprime to6. Multiplication by d gives an integer S_d cycle.
The reduced denominator of any positive odd rational with denominator
coprime to6 is invariant under S_1: if gcd(p,q)=1 and gcd(q,6)=1, then
gcd(3p+q,q)=1, and division by powers of2 cannot cancel any factor of q.
This does not supply a nontrivial cycle at d=1.

### 2. The mechanical family

Fix integers A>=k>=1 with2^A>3^k. For `0<=l<k`, define

```
a_i(l) = floor(((i+1)A+l)/k)-floor((iA+l)/k),
B_l = sum_(j=0)^(k-1) 3^(k-1-j) 2^floor((jA+l)/k).
```

These are the specified evenly spaced, or mechanical, valuation words.
All entries are positive and their total is A. The argument below needs
only these formulas; it assumes no classification of arbitrary balanced
words and no extremal theorem about other cycles.

**Theorem.** Put `g=gcd(A,k)`, `A_0=A/g`, `k_0=k/g`. Every state in any
of these mechanical cycles has reduced denominator

```
d = 2^A_0-3^k_0.                       (3)
```

Their only positive integer case is the word consisting entirely of2s,
whose cycle is the fixed point1.

#### Primitive case

First suppose gcd(A,k)=1. Shifting the word by s places replaces its
intercept l by `l+sA mod k`: expand the floor functions and subtract the
integer `floor((sA+l)/k)`. Every l is therefore a cyclic rotation of l0.
By (1), all `gcd(B_l,D)` agree.

For k>=2, passing from l0 to l1 increases precisely one prefix floor.
Indeed, among j=0,...,k-1 there is exactly one j with
`jA=k-1 mod k`, and this j is nonzero. Hence

```
B_1-B_0 = 3^(k-1-j) 2^floor(jA/k).     (4)
```

The common gcd divides (4). Because gcd(D,6)=1, that gcd is1. For k1
we have B0=1 directly. This proves (3) in the primitive case.

#### Repeated words

For g>1, the l0 word is g repeats of the word with parameters(k_0,A_0).
More generally, writing `l=g h+r`, 0<=r<g, gives

```
floor((jA+l)/k) = floor((jA_0+h)/k_0).
```

Thus each intercept word repeats the corresponding primitive word. Its
positive fixed point is unchanged by repetition: an affine map with
slope3^k_0/2^A_0 strictly between0 and1 has the same unique fixed point
as every positive iterate. Applying the primitive case proves (3).
Using the unreduced D here would be wrong; for(k,A)=(6,10), D295 but d5.

#### Excluding nontrivial integer cycles in this family

An integer state requires d1. If k_0>=2, positivity forces A_0>=4.
But `2^A_0=3^k_0+1` is impossible modulo8: the right-hand side is2
when k_0 is even and4 when it is odd. If k_0=1, d1 forces A_0=2.
Consequently A=2k, every valuation is2, and every state is1.

The theorem excludes this entire word family, at every length. It
neither excludes other periodic valuation patterns nor addresses
aperiodic positive divergence.

### 3. Rational cycles arbitrarily far above the absorber

For each k>=1, choose A as the bit length of3^k, equivalently
`A=ceil(k log_2 3)`. Exact integer arithmetic gives

```
3^k < 2^A < 2*3^k,      0<D<3^k.
```

The word entries are1 or2. For every intercept l and every j,

```
floor((jA+l)/k) > jA/k-1,
3^(k-1-j) 2^floor((jA+l)/k)
    > (3^(k-1)/2) (2^(A/k)/3)^j >= 3^(k-1)/2.
```

Summing k terms and dividing by D<3^k proves

```
every cycle state x > k/6.             (5)
```

Given any C>0, choose an integer k>6C. This yields a rational S_1 cycle
with all states>C. With d from(3), the corresponding integer S_d cycle
has every state>C d. For k>6, d>1 and the cycle avoids the fixed absorber d.
The denominator d varies with k; this is not a construction of arbitrarily
high cycles for one fixed d. In particular, there is no constant C
uniform over all d that bounds every cycle minimum by C d.

This is a control for arguments using only identities on rationals and
size inequalities. It does **not** show that these S_d maps pass any
proposed finite base test: smaller seeds may already fail to reach d.
It therefore does not, by itself, refute a method that separately checks
all required base cases and proves a genuinely applicable integer induction.

### 4. Reproduction and exact scope

Run from the repository root:

```
python3 experiments/residual_progress/lattice_cycles/check_balanced_cycles.py
```

The [module](balanced_cycles.py) constructs exact Fraction cycles and
the [receipt](balanced_cycles_audit.json) retains source hashes and full
integer cycle tables for selected controls. The replay checks:

- 1320 positive arbitrary words of lengths1..5 and valuations1..4,
  including each rotation, denominator invariance and exact scaled steps;
- 336 mechanical parameter pairs, k1..48 and seven consecutive totals
  beginning at `ceil(k log_2 3)`, including8232 intercepts, rotation
  identities, primitive gcds, repeated-word reduction and integer cases;
- 130 high controls, k1..128 and256/512, with exact bound(5), and11 invalid
  input rejections.

The finite checks support the implementation. The proofs above establish
the universal statements for this specified family. No dispatcher rule,
pair-current domain, universal stopping time or new Collatz proof is supplied.

### 5. Primary literature and positioning

Barry Brent's [2002 paper on rational dynamics](https://arxiv.org/abs/math/0204170)
discusses fixed denominators, cyclic parity formulas and scaling. Our
Section1 uses the odd-only clock and gives its full arithmetic derivation.

Kevin Knight's [*Collatz high cycles do not exist*](https://doi.org/10.1016/j.disc.2025.114812),
Discrete Mathematics349(3),2026,114812, already excludes integer high
cycles using Christoffel words. The journal abstract and section previews
were consulted; we do not assert priority for the nonintegrality conclusion.
The mechanical class is connected to that established direction, and its
exact denominator formula here is proved without importing an extremal
characterization or any claim about all parity words.

Fernández and Ibáñez's [2026 preprint](https://arxiv.org/abs/2607.24844)
studies extremal Christoffel parity patterns and explicitly relates its
results to Knight. Its shortcut clock differs from our k odd-only steps
with total valuation A. No theorem from that preprint is required above.

## Certificates

- [`check_balanced_cycles.py`](check_balanced_cycles.py) (under 1 s; main lane): the replay of section 4 of the note: 1320 positive words of lengths 1–5 and valuations 1–4 (every rotation, denominator invariance, exact scaled steps), 336 mechanical parameter pairs (`k = 1..48`, seven consecutive totals from `⌈k log₂3⌉`; 8232 intercepts, rotation identities, primitive gcds, repeated-word reduction, integer cases), 130 high controls with bound (5), and 11 rejections, compared with `balanced_cycles_audit.json`. It runs at this path.
- [`r71_mechanical_check.py`](r71_mechanical_check.py) (under 1 s; side lane, independent code): the 735-word check listed under `reviewed_by`; it rewrites its receipt byte for byte.
- [`r71a_mech_gcd_check.py`](r71a_mech_gcd_check.py) (about 2 s) and [`r71b_den_mech_check.py`](r71b_den_mech_check.py) (about 1 s; side lane, independent code): the exact checks of the Lean statements R71-a and R71-b listed under `reviewed_by`. They print their report and write a receipt only when given an output path.

## Lean

`lean/CycleSpectrum.lean`, Lean units R71-a and R71-b (legacy `lean/STATE.md`, now [`archive/lean-lane/STATE.md`](../../../../archive/lean-lane/STATE.md); namespace `LeanLane.Cyc`). Axioms `propext`, `Classical.choice`, `Quot.sound` (some helpers fewer); receipts `lean/receipts/CycleSpectrum.*`. No external input. In the file, `mech A m l` is the word above (with `m` for `k`), `C` the recursive intercept (`C_mech` recovers the closed sum `B_l`), `D w = 2^(Σw) − 3^|w|`, and `den w = D w / gcd(C w, D w)` is the reduced denominator.

- **(3), every word and phase.** `den_mech`: for `0 < k ≤ A` and `l < k`, `den (mech A k l) = 2^(A / gcd A k) − 3^(k / gcd A k)`. It needs no hypothesis `2^A > 3^k`; the prose assumes it only to make the cycle positive. "Every state" is the same number because the rotations of a mechanical word are its phases (`mech_rotate`, unit C004-b) and `gcd(C, D)` is rotation invariant (`gcd_rotate_eq`).
- **Primitive case.** `mech_gcd_one` and `mech_gcd_one_phase` (`m ≥ 2`, `A ≥ m`, `gcd(A, m) = 1` ⇒ `gcd(C, D) = 1` for every phase), through `exists_unique_mech_jump` (exactly one `j < m` with `m | jA + 1`) and `C_mech_one_sub_zero` (the note's (4): `B_1 − B_0 = 3^(m−1−j)·2^⌊jA/m⌋`); `mech_gcd_one_phase'` extends it to `k_0 = 1`, where the word is `(A_0)` and `C = 1`.
- **Repeated words.** `mech_rep` (`mech(gA_0, gk_0, gh + r) = (mech A_0 k_0 h)^g` for `r < g`), `gcdCD_rep` and `den_rep` (`den(z^k) = den(z)`): the prose's "the fixed point is unchanged by repetition", proved by scaling `C` and `D` by the same `G_k > 0`.
- **Integer cycles.** `mech_D_ne_one`: `2^A − 3^m ≠ 1` for `m ≥ 2`, `A ≥ m` (the modulo-8 argument). Part 2 is the immediate combination: by `den_mech`, `den = 1` means `2^(A_0) − 3^(k_0) = 1`; `mech_D_ne_one` excludes `k_0 ≥ 2` (with `A_0 ≥ k_0`), and `k_0 = 1` forces `2^(A_0) = 4`, `A = 2k`. This case split is not a separate declaration; the same split is carried out inside `den_mech_gt_one` (see [`mechanical-cycles-high-rational-controls`](../mechanical-cycles-high-rational-controls/README.md)). The integer-cycle form for actual cycles is `LeanLane.Cyc.OddCycle.narrow_integer_cycle` of [`narrow-cycles-are-mechanical`](../narrow-cycles-are-mechanical/README.md).

## Remarks

- **Literature; no novelty claimed.** The exclusion of mechanical (upper Christoffel) words as integer cycles is Knight's published theorem ([`knight-2026-high-cycles`](../../../../sources/knight-2026-high-cycles.md)); the Lean lane's literature calibration (2026-10-19) labels R71-a "known theorem, formalised here", and the Christoffel case is also kernel-checked in `mmusson/collatz` ([`musson-collatz-gap-all`](../../../../sources/musson-collatz-gap-all.md)). The affine word formula and rational cycle points are classical background ([`halbeisen-1997-rational-cycles`](../../../../sources/halbeisen-1997-rational-cycles.md)). The exact denominator (3) in the repeated case (R71-b) has novelty undetermined. These sources are antecedents, not premises: the proof here imports none of them.
- **Controls.** The exclusion is specific to `d = 1`: mechanical words are genuine integer cycles of `3x+d` whenever `2^(A_0) − 3^(k_0)` divides `d` (for example the `3x+5` cycle `(23, 37, 29)`, word `(1,2,2)`, and the `3x+13` mechanical cycle with minimum 319). The only `d = 1` input is that `2^(A_0) − 3^(k_0) = 1` has no solution with `k_0 ≥ 2`.
- **Uses.** The last step of the narrow-cycle corollary [`narrow-cycles-are-mechanical`](../narrow-cycles-are-mechanical/README.md) (C004) and of [`rotation-block-exclusion`](../rotation-block-exclusion/README.md) (C005); the exact denominator of [`narrow-cycle-spectrum-law`](../narrow-cycle-spectrum-law.md) and of the adjacent-defect case of [`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md); the mechanical families of [`close-pair-lattice-criterion`](../../attempts/close-pair-lattice-criterion/README.md) and [`local-odd-rounding-exclusion`](../../attempts/local-odd-rounding-exclusion/README.md). The same exact denominator for reduced ordered cycles with one forced position is [`single-forced-position-denominator`](../single-forced-position-denominator.md) (S1-d), by another route.
- **Residual progress.** In the legacy line this was R71 of the residual-progress rounds, written to scope the side lane's `3x+d` transfer; the convergence integer-prefix theorem [`exit18-return-integer-cylinders`](../../../convergence/results/exit18-return-integer-cylinders/README.md) notes that this closure obstruction does not apply to finite prefixes.

## History

- Migrated from `experiments/residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md` (legacy ID R71; Lean units R71-a, R71-b) at commit `be73a66`, by the B12 migration (Claude, Opus 5.5), into the cycles area. Note, module, checker and receipt moved byte-identical. The side-lane checks `reviews/side_lane/r71_mechanical_check.*`, `r71a_mech_gcd_check.*`, `r71b_den_mech_check.*` and the main lane's review `experiments/residual_progress/side_lane_review_13590c1.md` and `.json` moved here. Section 3 became [`mechanical-cycles-high-rational-controls`](../mechanical-cycles-high-rational-controls/README.md) (R71-c, R71-d); section 0 the attempt [`scaling-transfer-to-3x-plus-d`](../../attempts/scaling-transfer-to-3x-plus-d/README.md). Legacy status: "self-contained derivation and finite exact implementation of a restricted cycle result with published antecedents".
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `ea3278e` (the R69–R71 round). Formalised by the Lean lane (Claude Lean lane, Fable), 2026-10-19: R71-a (iteration 36), R71-b (iteration 48).
