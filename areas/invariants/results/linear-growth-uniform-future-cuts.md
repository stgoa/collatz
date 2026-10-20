---
id: linear-growth-uniform-future-cuts
kind: result
title: A linear cumulative bound on a rooted section graph gives arbitrarily late cuts with a uniform future mean bound, but not bounded-width stretches
status: reviewed
claim: >
  Let B_D be the cumulative rooted ball of depth D in a graph and a_D = |B_D minus B_(D-1)|. (a) If |B_D| <= C(D+1) for
  every D, then for every real C' > C there are arbitrarily large r with |B_(r+t) minus B_r| <= C' t for every t >= 0.
  (b) Cumulative linear growth does not give arbitrarily long intervals of uniformly bounded layer width: there is a
  rooted directed graph of outdegree at most 2, every vertex with infinitely many descendants, whose layer sizes a_n
  satisfy sum_(n=1..N) a_n <= 13N but a_(2^j) = j + 2, with peaks of height at least j + 2 in every interval of 2^(j+1)
  consecutive levels. Generic graph statements; (b) does not preserve the radix identities of a section graph.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
evidence:
  - "two-exit-interior-counterexample/linear_joint.md: the written lemma (section 2), the bounded-degree control (section 3), the near-minimal binary reformulation (section 4) and the S-adic source check (section 5)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-18
    scope: "Iteration 9: linear_joint.md's uniform future-cut lemma (maximise |B_D| - C'D on a tail) and the triangular-peak profile (sum a_n <= 13N, L^3/2^(L-1) <= 8) check out"
aliases: [V008-c]
tags: [invariants, section-graph, quantitative-rigidity, growth]
---

# A linear cumulative bound on a rooted section graph gives arbitrarily late cuts with a uniform future mean bound, but not bounded-width stretches

## Statement

Let `B_D` be the cumulative rooted ball in a graph (for the quantitative goal: the exact joint section graph) and `a_D = |B_D \ B_(D−1)|` for `D ≥ 1`.

**(a) Uniform future cuts.** If `|B_D| ≤ C(D+1)` for every `D`, then for every real `C' > C` arbitrarily large integers `r` satisfy

```
|B_(r+t) \ B_r| ≤ C' t      for every integer t ≥ 0.
```

**(b) No bounded-width stretches from counting.** The layer profile `a_0 = 1`, `a_n = 2 + max_(j≥1) t_j(n)` with `t_j(n) = max(0, j − dist(n, (2Z+1)·2^j))` satisfies `|a_(n+1) − a_n| ≤ 1`, `Σ_(n=1..N) a_n ≤ 13N`, yet `a_(2^j) = j + 2` and peaks of height `≥ j + 2` recur at every integer `≡ 2^j (mod 2^(j+1))`; so for every fixed `K` every interval of levels with all widths `≤ K` has length less than `2^(j+1)` for `j + 2 > K`. The profile is realised by the distance layers of a rooted directed graph of outdegree at most two in which every vertex has infinitely many descendants.

## Proof

From [`linear_joint.md`](two-exit-interior-counterexample/linear_joint.md) §§2–3. (a): put `F(D) = |B_D| − C'D`; the bound gives `F(D) → −∞`, so for every `R` the set `{F(D) : D ≥ R}` attains its maximum at some `r ≥ R`, and `F(r+t) ≤ F(r)` is exactly the claim. (b): each triangular profile `t_j` is 1-Lipschitz with period `2^(j+1)` and mass `j²` per period; for `1 ≤ n ≤ N` only `j ≤ L = 1 + ⌊log₂ N⌋` contribute, so `Σ a_n ≤ 2N + Σ_(j≤L) (N/2^(j+1) + 1) j² ≤ 5N + Σ_(j≤L) j² ≤ 13N`, using `Σ j² ≤ L³ ≤ 8·2^(L−1) ≤ 8N` (`L³/2^(L−1)` is at most 8, attained at `L = 4`). The graph: between adjacent levels give every old vertex a successor and cover every next-level vertex; an increase by at most one needs at most one extra outgoing edge; all edges advance one level. ∎

## Remarks

- **What (a) gives.** The outside layer `B_(r+1) \ B_r` has at most `⌊C'⌋` vertices and the complete future beyond the cut keeps a uniform linear cumulative bound, returns through `B_r` included. It does not bound every later layer by `C'`, supply a periodic sequence of transition matrices, or bound an equality witness between whole sequences. Excluding these uniformly bounded-mean futures for every `C'` would address the quantitative goal [`section-count-depth-ratio-unbounded`](../questions/section-count-depth-ratio-unbounded/README.md); the lemma itself supplies neither.
- **Scope of (b).** The control invalidates a deduction from cumulative growth, finite branching and infinite descendants only. It is not an affine section graph (no radix identities, vertices are not sequences), so it does not refute a theorem using the full affine structure.
- **Near-minimal growth** (`linear_joint.md` §4): `kappa_h(D) = D + O(1)` is equivalent to one new binary state per sufficiently late depth; this diagnostic was settled in [`additive-section-excess-unbounded`](additive-section-excess-unbounded/README.md).
- The source check of `linear_joint.md` §5 (a finitary S-adic rigidity result) is not imported: its symbolic presentation and recognisability hypotheses are not supplied by a rooted count.

## History

- New node by the B16 migration (Claude, Opus 5.5) from `experiments/viewpoints/V008/linear_joint.md` and the V008 report §3 (legacy ID V008) at commit `be73a66`; the note stays in [`two-exit-interior-counterexample`](two-exit-interior-counterexample/README.md)'s folder.
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `9d66b69`. Side lane (feed 23:01): "the standard maximisation argument", read but not replayed.
