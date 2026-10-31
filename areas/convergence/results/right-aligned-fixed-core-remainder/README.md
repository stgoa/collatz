---
id: right-aligned-fixed-core-remainder
kind: result
title: Grouping depth-one source lifts from the right leaves a remainder only on the core {5, 7, 11, 13}
status: reviewed
claim: >
  Odd-only clock, absorbing at 1. For every integer N ≥ 8, b = ceil(log₂N), group the exact depth-one source
  lifts of each valuation a (1 ≤ a ≤ b) and each of the two source components of ν_N into consecutive
  triples from the right (the r = s mod 3 lowest lifts stay ungrouped). Then P ν_N = Π^R_N + η_N with every
  raw packet of the form c_0 δ_y + c_1 δ_(y+6) + c_2 δ_(y+12), (c_0, c_1, c_2) a permutation of (2, −1, −1),
  so ⟨1, Π^R_N⟩ = 0; supp η_N ⊆ {5, 7, 11, 13}; ‖η_N‖₁ ≤ 6b; and for every T ≥ 1,
  |3E_T(N) − H_(T−1)(Π^R_N)| ≤ 8 + 30b, at every horizon.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: []
certificates: [right_aligned_packets.py]
evidence:
  - "right_aligned_audit.json: receipt of right_aligned_packets.py (rewritten byte for byte by each run)"
  - "../locally-collatz-like-control-barrier/reduction_audit.py, reduction_audit.json: the PR1 lane's independent recheck of Theorem 1 (see right-aligned-reduction-independent-checks)"
  - "Legacy scripts elsewhere load this script by its old path experiments/packet_currents/right_aligned_packets.py (current construction, annular construction and residual progress lines, about 18 references in scripts and receipts); they do not run against this path"
reviewed_by:
  - by: Claude PR1 lane (Opus)
    date: 2026-10-17
    link: ../locally-collatz-like-control-barrier/NOTE.md
    scope: "NOTE §6 (ledger C1): re-derived the written argument of Theorem 1 (the valuation-partition bijections and the large-valuation tail: S(x) < 3 with 3 ∤ S(x) forces S(x) = 1) and found no gap; independent code reproduces Π^R_N and η_N exactly for 8 ≤ N ≤ 3000 and N = 4096, checks (3) at every horizon for 8 ≤ N ≤ 160 and (2) for every N ≤ 10^5 plus 3,132 sampled N ≤ 10^18. Model-assisted, not human peer review"
aliases: [R2]
tags: [convergence, packet-currents, right-aligned, reduction]
---

# Grouping depth-one source lifts from the right leaves a remainder only on the core {5, 7, 11, 13}

## Statement

Odd-only clock, absorbing at 1, with `S`, `τ`, `h_L`, `H_L` and `P` as in [`finite-current-certificate-identity`](../finite-current-certificate-identity/README.md). For an integer `N ≥ 8` put

```
b = ceil(log₂ N),   n_0 = floor((N−1)/4),   n_1 = floor((3N+1)/2),   n_2 = floor((3N+1)/4),
ν_N(x) = 1[x ≤ n_1]·(3·1[x ≡ 2 mod 3] − 1) + 1[x ≤ n_2]·(3·1[x ≡ 1 mod 3] − 1)      (x > 1 odd).
```

`|⟨1, ν_N⟩| ≤ 8`. With `Q_T(u) = Σ_(x ≤ u odd) h_T(x)` and the residue sums `R_(r,T)`, the programme's discrepancy is `E_T(N) = R_(5,T)(n_1) − Q_T(n_1)/3 + R_(1,T)(n_2) − Q_T(n_2)/3`, and `3E_T(N) = H_T(ν_N)`.

For a single exact valuation `a`, put `M_a = 2^(a+1)`. The source and endpoint lifts are `x_t = q_a + M_a·t`, `y_t = e_a + 6t`, with

```
(q_a, e_a, t_0) = ((2^a − 1)/3, 1, 1)   for a even,       ((5·2^a − 1)/3, 5, 0)   for a odd.     (1)
```

In component `i ∈ {1, 2}` keep `t_0 ≤ t ≤ ℓ_(a,i) = floor((n_i − q_a)/M_a)`, let `s_(a,i) = max(0, ℓ_(a,i) − t_0 + 1)` and `r_(a,i) = s_(a,i) mod 3`. Leave the first `r_(a,i)` lifts ungrouped and split the rest into consecutive triples, so the last triple ends at the upper cutoff. The sum of all packets over `1 ≤ a ≤ b` and both components is `Π^R_N`.

**Theorem 1 (fixed-core remainder).** For every integer `N ≥ 8`,

```
P ν_N = Π^R_N + η_N,    supp η_N ⊆ {5, 7, 11, 13},    ‖η_N‖₁ ≤ 6b.                              (2)
```

Every raw packet is `c_0 δ_y + c_1 δ_(y+6) + c_2 δ_(y+12)` with `(c_0, c_1, c_2)` a permutation of `(2, −1, −1)`; in particular `⟨1, Π^R_N⟩ = 0`. For every integer `T ≥ 1`,

```
|3E_T(N) − H_(T−1)(Π^R_N)| ≤ 8 + 30b.                                                          (3)
```

## Proof

From Theorem 1 of [`papers/right-aligned-reduction`](../../../../papers/right-aligned-reduction/README.md), kept as written.

Formula (1) solves `3x + 1 = 2^a·y` with `y` odd, using the least positive source representative modulo `2^(a+1)`. As `M_a` is a unit modulo 3, three consecutive sources visit all three residues and their coefficients sum to zero. At most two left lifts remain in each component. They have endpoints `5, 11` for odd `a` and `7, 13` for even `a`, and their absolute coefficients sum to at most 3 per component.

There is no unaccounted large-valuation tail: `x ≤ n_1 < 2^(b+1)` and `a(x) > b` imply `0 < S(x) = (3x+1)/2^(a(x)) < 3`. The endpoint is odd, so it equals 1 and is discarded by `P`. Summing the leftovers proves (2). The four core hitting times are `τ(5) = 1`, `τ(7) = 5`, `τ(11) = 4`, `τ(13) = 2`, so `|H_L(η_N)| ≤ 30b` for every `L`. Finally

```
H_T(ν_N) = ⟨1, ν_N⟩ + H_(T−1)(P ν_N) = ⟨1, ν_N⟩ + H_(T−1)(Π^R_N) + H_(T−1)(η_N),
```

which proves (3). ∎

## Certificates

[`right_aligned_packets.py`](right_aligned_packets.py) (main lane, about 3 s, standard library; checks by `assert`, so run it without `-O`). It rewrites [`right_aligned_audit.json`](right_aligned_audit.json) byte for byte. It checks:

- the core hitting times `τ(5), τ(7), τ(11), τ(13) = 1, 5, 4, 2`, and that all odd seeds below 16 reach 1;
- (2) and the packet shape for every `8 ≤ N ≤ 2048` and for `N = 4096, 10001, 262144`, against a direct push of `ν_N`;
- the dyadic table of [`dyadic-cutoff-core-remainder`](../dyadic-cutoff-core-remainder.md) for `3 ≤ b ≤ 1000`, and its all-horizon correction range `[−12, 1]`;
- the sign witness `H_39(Π^R_32) = 57`;
- the rational inequalities used in Lemma 2 of [`qualitative-current-criterion`](../qualitative-current-criterion.md).

The receipt records `universal_current_existence_proved: false`.

## Remarks

- **A new grouping.** Right alignment differs from the handoff's left-aligned packets and from the exact-source family of [`packet-currents-snapshot`](../packet-currents-snapshot/README.md): the snapshot's stored currents cannot be relabelled as certificates for `Π^R_N`. What right alignment buys is a remainder on a **fixed** four-point core whose hitting times are known, so (3) holds at every horizon with an error `O(log N)`.
- **Controls.** The same construction transfers to the maps `T_d(x) = (3x+d)/2^(v₂(3x+d))` with `d = 2^k − 3` ([`locally-collatz-like-control-barrier`](../locally-collatz-like-control-barrier/README.md)); there the core points need not reach the absorbers, as for `d = −1`.
- Novelty undetermined.

## History

- Migrated from the legacy ledger entry R2 (`archive/docs/RESULTS.md`, legacy path) and Theorem 1 of `papers/right_aligned_reduction/right_aligned_reduction.tex`, now [`papers/right-aligned-reduction/right-aligned-reduction.tex`](../../../../papers/right-aligned-reduction/right-aligned-reduction.tex), at commit `be73a66`, by the B07 migration (Claude, Opus 5.5). The script and receipt moved from `experiments/packet_currents/right_aligned_packets.py` and `right_aligned_audit.json`. Legacy status: "written elementary proof; finite implementation checks".
- Main lane (ChatGPT, Codex), 2026-10-17, commit `9e2d7cb`. Audited by the PR1 lane the same day (ledger C1).
