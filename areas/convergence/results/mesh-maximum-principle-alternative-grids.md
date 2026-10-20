---
id: mesh-maximum-principle-alternative-grids
kind: result
title: A mesh maximum principle reduces the current criterion to any grid of bounded ratio, with 21-ray and 30-ray instances
status: written
claim: >
  Odd-only clock, absorbing at 1; d_M = ⟨e, Π^R_M⟩ as in five-ray-current-criterion. (Mesh lemma) If p > 1,
  U ≥ 8, G is an unbounded set of cutoffs divisible by 4, every odd seed below U reaches 1, every integer
  n ≥ U has some M ∈ G with n ≤ M ≤ α·n, α^p·λ(p) < 1 where λ(p) = 4^(−p) + (3/2)^p/3 + (3/4)^p/3, and d_M ≤ 0
  for every M ∈ G, then every positive integer reaches 1. Instances: the 21 mantissas
  A = {8192, …, 15852} with b ≥ 3 (α = 10337/10000, p = 7/5, α^p·λ(p) < 399928193/400000000; finite base:
  odd seeds below 65536) and {m·2^b : 30 ≤ m ≤ 59, b ≥ 2} (α = 31/30, p = 4/3, bound 1199731/1200000; base
  below 120) each give the three equivalent current/work criteria of five-ray-current-criterion. Also: the
  hypotheses may be stated as limsup_L H_L(Π^R_M)/L < 1 per cutoff, or as finite rational currents with
  ‖ζ_M⁺‖₁ < 1, both equivalent to d_M ≤ 0 by integrality; and d_M ≤ c_M (c_M ≥ 0) on a mesh gives
  sup_n B(n)/n^p ≤ α^p·D/(3(1 − q)), D = sup c_M/M^p, q = α^p·λ(p) < 1. Reformulations only; no current is
  supplied.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [qualitative-current-criterion, finite-current-certificate-identity]
evidence:
  - "../five-ray-current-criterion/check_sparse_criteria.py, sparse_criteria_audit.json (a certificate of that node): the finite base below 65536 (largest hitting time 125, at 52527), the 21 mesh ratios (maximum 10668/10321), the three fifth-power root bounds and the 7/5 contraction bound, 3905 grid boundary probes for exponents 3–64, and the 30-ray constants (base below 120, largest hitting time 43)"
  - "../five-ray-current-criterion/sparse_ray_independent_audit.md: a re-check of the mesh lemma and of the 21-ray and 30-ray constants by another main-lane agent (not an independent review)"
aliases: [R5-b]
tags: [convergence, packet-currents, right-aligned, maximum-principle, grids]
---

# A mesh maximum principle reduces the current criterion to any grid of bounded ratio, with 21-ray and 30-ray instances

## Statement

Notation of [`five-ray-current-criterion`](five-ray-current-criterion/README.md): `e`, `B`, `𝓛`, `d_N = ⟨e, Π_N⟩ = 3(B(N) − (𝓛B)(N))`, odd-only clock absorbing at 1.

**Lemma (mesh maximum principle).** Let `p > 1`, `U ≥ 8`, and let `G` be an unbounded set of integer cutoffs divisible by 4. Suppose:

1. every positive odd seed below `U` reaches 1;
2. for every integer `n ≥ U` there is `M ∈ G` with `n ≤ M ≤ α·n`;
3. `α^p·λ(p) < 1`, where `λ(p) = 4^(−p) + (3/2)^p/3 + (3/4)^p/3`;
4. `d_M ≤ 0` for every `M ∈ G`.

Then every positive integer reaches 1.

**Theorem (21 rays).** Let `A = {8192, 8467, 8751, 9045, 9348, 9662, 9986, 10321, 10668, 11026, 11396, 11778, 12173, 12582, 13004, 13440, 13891, 14358, 14839, 15337, 15852}` and `G_21 = {a·2^b : a ∈ A, b ≥ 3}`. Each of the three statements of [`five-ray-current-criterion`](five-ray-current-criterion/README.md) (bounded work, exact current, current with nonpositive residual, at every cutoff of the grid) with `G_21` in place of `G_5` is equivalent to Collatz. There are 21 cutoffs in each interval `[8192·2^b, 16384·2^b)`; no uniform bound on size, running time or cost is assumed.

**Theorem (30 rays).** The same holds for `G_30 = {m·2^b : 30 ≤ m ≤ 59, b ≥ 2}`.

**Subunit defects.** (a) For each `M`, the hypothesis may be replaced by `limsup_(L→∞) H_L(Π_M)/L < 1`; by integrality this is equivalent to `d_M ≤ 0`. (b) A finite **rational** current and residual `Π_M = (I − P)J_M + ζ_M` with `‖ζ_M⁺‖₁ < 1` gives `d_M ≤ 0`. (c) If `d_M ≤ c_M` with `c_M ≥ 0` on a mesh with exponent `p`, ratio `α` and `q = α^p·λ(p) < 1`, and `D = sup_(M ∈ G) c_M/M^p`, then after the same terminating finite base `sup_(n ≥ 1) B(n)/n^p ≤ α^p·D/(3(1 − q))`.

## Proof

From §§3–6 of the legacy sparse-criteria note, kept as written.

**Mesh lemma.** At a selected cutoff `M`, divisibility by 4 gives the exact cutoffs `n_0 = M/4 − 1`, `n_1 = 3M/2`, `n_2 = 3M/4`. Therefore `𝓛(n^p)(M) < λ(p)·M^p`. Also `B(n) ≤ n`, so `B(n)/n^p → 0`. If an exceptional seed exists, this ratio attains a positive global maximum `C` at some integer `n ≥ U`. Choose `M` as in hypothesis 2. By monotonicity of `B`, equation (1) of [`five-ray-current-criterion`](five-ray-current-criterion/README.md), and the definition of `C`,

```
C·n^p = B(n) ≤ B(M) ≤ (𝓛B)(M) ≤ C·(𝓛(n^p))(M) < C·λ(p)·M^p ≤ C·λ(p)·α^p·n^p < C·n^p.
```

This contradiction proves the lemma. Initial powers of 2 reduce the even case to the odd case; every comparison uses the same odd-only clock. ∎

**21 rays: the arithmetic constants.** Include the wraparound successor `16384 = 2·8192` after the final mantissa `15852`. The maximum of the 21 successive ratios is the interior ratio

```
max_(0 ≤ i < 21) a_(i+1)/a_i = 10668/10321 < α := 10337/10000,     a_21 = 16384.        (4)
```

For an arbitrary integer `n ≥ 65536`, take `b = floor(log₂ n) − 13` and choose the least `a·2^b ≥ n` with `a ∈ A`; if there is none, choose `8192·2^(b+1)`. Here `b ≥ 3`. The chosen cutoff is the least `M ∈ G_21` above `n`, and (4) gives `n ≤ M ≤ α·n`. The integer implementation uses the bit length of `n`, with no floating arithmetic.

Take `p = 7/5`. Put `t_1 = α/4`, `t_2 = 3α/2`, `t_3 = 3α/4` and `(r_1, r_2, r_3) = (5821, 11918, 9032)/10000`. The three exact rational inequalities `t_i^2 < r_i^5` give `t_i^(7/5) = t_i·(t_i^2)^(1/5) < t_i·r_i`. Hence

```
α^(7/5)·λ(7/5) = t_1^(7/5) + t_2^(7/5)/3 + t_3^(7/5)/3 < t_1 r_1 + t_2 r_2/3 + t_3 r_3/3 = 399928193/400000000 < 1.   (5)
```

The finite base is every odd seed below 65536; the companion script verifies all 32768 by exact Syracuse iteration, with cycle detection and a 10000-step cap. All reached 1; the largest hitting time was 125, uniquely at seed 52527. Each of the three current/work hypotheses implies `d_M ≤ 0` exactly as in [`qualitative-current-criterion`](qualitative-current-criterion.md). The mesh lemma, (4)–(5) and the finite base imply Collatz. Conversely, under Collatz every finite packet is eventually absorbed and has a finite exact current; an exact current is also one with nonpositive residual and gives a finite work bound. ∎

**30 rays.** The base of `G_30` is 120 and its mesh ratio is `31/30`. Take `p = 4/3`. With `(u_1, u_2, u_3) = (31/120, 31/20, 31/40)` and `(s_1, s_2, s_3) = (6369, 11573, 9186)/10000`, the exact inequalities `u_i < s_i^3` give

```
(31/30)^(4/3)·λ(4/3) < u_1 s_1 + u_2 s_2/3 + u_3 s_3/3 = 1199731/1200000 < 1.
```

The finite base contains the odd seeds below 120 (largest odd-only hitting time 43). The mesh lemma gives the three equivalent criteria on `G_30`. ∎

**Subunit defects.** For any finite signed integer measure `μ`, the work is eventually affine,

```
H_L(μ) = L·⟨e, μ⟩ + Σ_(x : τ(x) < ∞) μ(x)·τ(x),
```

once `L` exceeds the finitely many finite hitting times in its support. So its limiting slope exists and is an integer, and

```
limsup_(L→∞) H_L(Π_M)/L < 1     for every selected cutoff M                            (6)
```

is equivalent to `d_M ≤ 0`, which is equivalent to boundedness above for this finitely supported packet. The strict bound may depend on `M`; there is no uniform margin below 1. Equation (6) is an alternative formulation, not a weaker existence statement.

For (b): invariance of `e` annihilates the divergence and gives `d_M = ⟨e, ζ_M⟩ < 1`, hence `d_M ≤ 0`. This explicitly enlarges the coefficient domain to the rationals; with integer residuals, subunit positive mass simply means the residual is everywhere nonpositive. The strict inequality is essential: a budget of one unresolved positive unit can leave `d_M = 1`. Bounds such as `‖ζ_M⁺‖₁ = o(M)` or a small percentage of total source mass need not be below one and do not establish (6).

For (c): at a positive maximizer `n` and its next selected cutoff `M`, `B(n) ≤ 𝓛B(M) + c_M/3`, and dividing by `n^p` proves `sup_n B(n)/n^p ≤ α^p·D/(3(1 − q))`. A positive right-hand side controls this weighted exceptional count; it does not prove that it vanishes. ∎

## Remarks

- **Superseded as the primary target.** These grids were the investigation's earlier choices; [`five-ray-current-criterion`](five-ray-current-criterion/README.md) has a much smaller finite base (96) and uses a ray-dependent comparison weight rather than a power. The 21-ray grid has fewer required families than the 30-ray grid; the 30-ray grid has simpler mantissas and a smaller base. No optimality of 21 is claimed.
- **Splitting by 64.** Writing `b = r + 6k`, `r = 3, …, 8`, the 21-ray grid gives 126 fixed sequences under multiplication of the cutoff by 64. This reduces the family of required cutoffs; it is still an infinite universal existence/termination obligation, and finite certificates at some exponents do not establish it.
- **Rational currents.** Part (b) is the seed of the finite-rational-cone conversion [`finite-rational-cone-integer-certificate`](finite-rational-cone-integer-certificate/README.md) (legacy R11).
- The general mesh lemma rests on the written argument; the script checks only its constants and finite bases. Novelty undetermined.

## History

- Migrated from `experiments/current_construction/frontier/sparse_current_criteria.md` §§3–6 (part of the legacy R5 round) at commit `be73a66`, by the B08 migration (Claude, Opus 5.5). The legacy note retained these as "scoped alternatives from this investigation", superseded by the five-ray theorem. Legacy status: "written conditional proofs with exact finite checks".
- Main lane (ChatGPT, Codex), 2026-10-17. The 21-ray constants received "a separate exact rational arithmetic audit by another research agent" of the main lane (legacy `sparse_ray_independent_audit.md`, now in [`five-ray-current-criterion`](five-ray-current-criterion/README.md)); no review from another lane is on record.
