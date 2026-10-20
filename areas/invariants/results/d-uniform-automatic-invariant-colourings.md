---
id: d-uniform-automatic-invariant-colourings
kind: result
title: For gcd(d, 6) = 1 the binary-automatic invariant colourings of 3x+d are the functions of n mod d constant on x2, x3 orbits
status: written
claim: >
  Let d >= 1 with gcd(d, 6) = 1 and C finite. If h : positive integers -> C is binary automatic and satisfies
  h(2n) = h(n) (n >= 1) and h(3n+d) = h(n) (odd n >= 1; for d = 1 odd n > 1 suffices), then h(n) = F(n mod d) for
  some F : Z/dZ -> C constant on the orbits of multiplication by 2 and by 3; conversely every such F gives an
  invariant periodic, hence automatic, colouring. For d = 1 this is V004. Assumes Cobham's theorem and the
  finite-kernel characterisation. The value d = 1 enters only in the commutator step (translation by d/4).
authors:
  - Claude side lane (Opus)
created: 2026-10-18
depends_on: [binary-automatic-invariant-colourings-constant, periodic-invariant-colourings-classification]
assumes: [cobham-recognizability-theorem, eilenberg-finite-kernel]
evidence:
  - "binary-automatic-invariant-colourings-constant/v004_rigidity_check.py parts (e)-(f) and its receipt: Step 1 rewrites compared on the actual cycle labellings c_d (35,433 comparisons for d = 5, 59,055 for d = 13, 200,787 for d = 61, no mismatch; offset shift bounds S = 1, 1, 2, 8 for d = 5, 7, 13, 61 at a <= 12); 707 residue-graph cases for the finish"
  - "../questions/section-count-depth-ratio-unbounded/automatic_rigidity_control.py: the d = 5 and d = 13 cycle labellings' growing 2-kernels (calibration remark 3)"
aliases: [V004-d]
tags: [invariants, automatic, cobham, 3x+d, controls, rigidity]
---

# For gcd(d, 6) = 1 the binary-automatic invariant colourings of 3x+d are the functions of n mod d constant on x2, x3 orbits

The side lane's note, kept with light edits. Its status line read: "written proof (side lane, 2026-10-18), not formally verified, novelty undetermined." It uses the same two classical inputs as the main lane's V004 theorem ([`binary-automatic-invariant-colourings-constant`](binary-automatic-invariant-colourings-constant/README.md)) and nothing else: Eilenberg's finite-kernel characterisation ([`eilenberg-finite-kernel`](../../../sources/eilenberg-finite-kernel.md)) and Cobham's theorem ([`cobham-recognizability-theorem`](../../../sources/cobham-recognizability-theorem.md)). The proof follows V004 step by step; the only change is that offsets may leave `(0, 2^a)` by a bounded amount. The main lane's V004 side review had deferred this "d-uniform candidate" because its closure uses positive offsets specific to `+1`.

## Statement

Let `d ≥ 1` with `gcd(d, 6) = 1` and let `C` be finite. Suppose `h : N_{>0} → C` is binary automatic and satisfies

```
(1_d)   h(2n) = h(n)  for n >= 1,     h(3n+d) = h(n)  for odd n >= 1.
```

For `d = 1`, odd `n > 1` suffices, because `h(4) = h(1)`.

**Theorem.** `h(n) = F(n mod d)` for some `F : Z/dZ → C` that is constant on the orbits of multiplication by 2 and 3. Conversely, every such `F` gives an invariant periodic, hence automatic, `h`.

**Corollary.** For `d = 1`, `h` is constant, which is V004.

**Examples.**

- For `d = 5, 7, 13, 61`, the only automatic invariant colorings are functions of `1_(d|n)`.
- For `d = 35`, there are 4 orbit classes.

## Proof

**Step 0: identities, for every d.** Let `m ≥ 0`, and let `u, x ≥ 1` be odd.

- `(2_d)` `h(3m+d) = h(4m+d)`. Take `n = 4m+d`; then `3n+d = 4(3m+d)`.
- `(3_d)` `h(3u) = h(9u+d) = h(12u+d) = h(16u+d)`. The first equality is `(1_d)` at `3u`; the other two are `(2_d)` at `m = 3u` and `m = 4u`.
- `(4_d)` `h(4x+d) = h(x)`. This is `(2_d)` at `m = x`, followed by `(1_d)`.

**Step 1: ternary closure up to bounded shifts.** For `a ≥ 1`, odd `r0 ∈ (0, 2^a)` and an integer `σ`, put `φ(n) = h(2^a (n+σ) + r0)`.

For `j ∈ {0, 1, 2}`, write `j + σ = 3σ1 + j1` with `j1 ∈ {0, 1, 2}`. Put `c = 2^a j1 + r0`, which lies in `(0, 3·2^a)`, and `N = n + σ1`. Then `φ(3n+j) = h(3·2^a N + c)`. There are two cases.

- **Case A (`3 ∤ c`).** Choose `v ∈ {1, 2}` with `2^v c ≡ d (mod 3)`, and put `t = (2^v c − d)/3`. Then `t` is odd and `−d/3 < t < 2^(a+v)`. Whenever `x = 2^(a+v) N + t ≥ 1`, we have `3x + d = 2^v (3·2^a N + c)`, so the section equals `h(x)`.
- **Case B (`3 | c`).** Write `c/3 = 2^ℓ u` with `u` odd. Then `ℓ = v2(r0) < a` and `u < 2^s`, where `s = a − ℓ`. Put `U = 2^s N + u`. By `(3_d)`, the section equals `h(3U) = h(16U + d) = h(2^(s+4) N + 16u + d)`.

Reducing the new offset into `(0, 2^a')` changes `σ` by a bounded amount, at most `⌈d/12⌉` either way. Also `|σ1| ≤ (|σ|+2)/3`. So all shifts stay in a window `|σ| ≤ S(d)`, and every rewrite is valid from some index `n ≥ S0(d)` on.

- For `d = 1`, `S = S0 = 0`: this is exactly main's positive-offset closure `K_+`.
- The probe, for `a ≤ 12`, finds `S = S0 = 1, 1, 2, 8` for `d = 5, 7, 13, 61`.

**Step 1, conclusion.** Restricted to `n ≥ S0`, each such `φ` is a shift of an element of the binary kernel of `h`, so there are finitely many of them. Restricting to `n ≥ S0` commutes with ternary sections, because `3n+j ≥ S0` whenever `n ≥ S0`.

So for `b(n) = h(2n+1)`, every element of the 3-kernel of `b` agrees on `n ≥ S0` with one of finitely many sequences. Its first `S0` values range over the finite set `C^(S0)`. Hence the 3-kernel of `b` is finite, and `b` is 3-automatic. It is also 2-automatic, so by Cobham it is eventually periodic.

**Step 2: global odd period.** Taking `x = 2n+1` in `(4_d)` gives `b(4n + (d+3)/2) = b(n)`. Main's argument in §2 of its `INDEPENDENT_REVIEW.md`, with `G(n) = 4n + (d+3)/2`, turns an eventual period `2^e L` (with `L` odd) into a global period `L`.

**Step 3: residues.** Define `q` on `Z/LZ` by `h(x) = q(x mod L)` for odd `x`. From `(4_d)` and `(3_d)`:

```
q(4x + d) = q(x),     q(3x) = q(16x + d) = q(4x).
```

- **Removing the 3-part.** Put `H(x) = 3·4^(-1) x`, so `q∘H = q`. Then `q` descends to `Z/mZ` with `m = L/3^(e3)`.
- **Commutator.** On `Z/mZ`, put `J(x) = 4x + d`. Then `H(J(x)) = 3x + 3d/4` and `J(H(x)) = 3x + d`, so `q(z − d/4) = q(z)`. Hence `q` factors through `Z/gZ` with `g = gcd(d, m)`.

This is the **only** step where `d = 1` differs from other `d`. For `d = 1`, `1/4` is a unit, so `g = 1` and `q` is constant.

**Step 4: all valuations give invariance under ×2.** Fix a residue `x` mod `L` and `k ≥ 1`. By CRT, `L` being odd, there is an odd `x' ≡ x (mod L)` with `v2(3x' + d) = k`. Applying `(1_d)` at `x'` gives `q(2^(-k)(3x + d)) = q(x)`.

On `Z/gZ`, where `d ≡ 0`, this reads `q̄(2^(-k)·3x) = q̄(x)` for every `k ≥ 1`. Step 3 already gives `q̄(3x) = q̄(x)`. Together these give `q̄(2y) = q̄(y)`.

Therefore `h(n) = h(odd part of n) = q̄(n mod g)`. ∎

## Certificates

None attached to this node. The finite checks below are parts (e) and (f) of the side lane's [`v004_rigidity_check.py`](binary-automatic-invariant-colourings-constant/v004_rigidity_check.py), a certificate of [`binary-automatic-invariant-colourings-constant`](binary-automatic-invariant-colourings-constant/README.md).

### Checks

Probe: `v004_rigidity_check.py` (in the V004 node's folder), which reports PASS.

- **(e) Closure on actual colorings.** Every Step-1 rewrite (states with `a ≤ 7`, 31 consecutive `n` each) was compared on the actual cycle labelling `c_d`. That labelling is a genuine nonconstant invariant coloring.
  - For `d = 5`: 35,433 comparisons; cycles through 1, 5, 19, 23, 187 and 347.
  - For `d = 13`: 59,055 comparisons.
  - For `d = 61`: 200,787 comparisons.
  - No mismatch in any of them.
- **(f) Finish on residue graphs.** There were 707 cases, with `d ∈ {1, 5, 7, 13, 61, 35, 65}` and odd `m ≤ 301`, `3 ∤ m`.
  - The residue graph with edges `x ~ 4x+d` and `y ~ 3·4^(-1) y` has exactly as many components as there are `⟨3, 4⟩`-orbits on `Z/gcd(d, m)Z`.
  - Adding the valuation edges `x ~ 2^(-k)(3x+d)` leaves exactly the `⟨2, 3⟩`-orbits, which is V13's periodic classification.
  - The two orbit counts can differ: 3 versus 2 orbits on `Z/13Z`, and 6 versus 4 on `Z/65Z`. That is why Step 4 is needed.

## Remarks

### What it says about the programme

These are calibration remarks, not results.

1. **What automata detect.** In every `3x + d`, binary automata detect exactly the congruence classes mod `d` up to `⟨2, 3⟩`, and nothing else. V004's `d = 1` statement is that d-uniform rigidity combined with the fact that `d = 1` has no congruence obstruction.
2. **Real separations in 3x+5 are non-automatic.** For `3x + 5`, the theorem shows that the actual cycle partition among non-multiples of 5 is non-automatic. That partition has at least five cycles: through 1, 19, 23, 187 and 347. These are genuine separations, not hypothetical ones. Being non-automatic is therefore not evidence that a separation does not exist.
3. **The proposed κ(D)/D target.** This is main's possible next milestone. The `d = 5` and `d = 13` cycle labellings already have at least 242 and 259 distinct binary sections by depth 9. These are rigorous lower bounds from distinct 60-term prefixes, computed in `automatic_rigidity_control.py`. So the d-analogue of the target is not contradicted, and a proof that never uses `d = 1` beyond Step 3 would hold equally for those real separations. Turning any complexity lower bound into convergence still needs an upper bound on the complexity of the actual bad set. None is known or suggested.

### Literature boundary

- **Shallit–Wilson** (Bull. EATCS 46, 1992) prove that the binary ancestors of a fixed `x` reached within a bounded number of odd steps form a regular language. This is the fixed-depth ancestor language, as Stérin's arXiv:1907.00775 abstract describes it. It does not concern unbounded invariant classes, and so does not overlap V004 or this note. Main's V003 literature note draws the same distinction.
- **No source was found** for the classification of automatic invariant colorings for general `d`. This is a search outcome, not a novelty claim.

- **Not reviewed or formalised.** No proof-level review by another lane is on record. Of its steps, Steps 2–4 for `d = 1` and the periodic classification (Step 4's `⟨×2, ×3⟩` conclusion is the periodic classification at modulus `g`) are formal elsewhere ([`odd-eventually-periodic-invariants-constant`](odd-eventually-periodic-invariants-constant.md), [`periodic-invariant-colourings-classification`](periodic-invariant-colourings-classification/README.md)); the side lane noted (feed 22:42) that the `d`-version of the closure up to shifts (Step 1) is the one remaining unformalised piece.
- The main lane did not adopt a `d`-uniform growth theorem for non-periodic invariants (feed 23:01, "main's transfer point is fair").

## History

- Migrated from `experiments/viewpoints/V004/D_UNIFORM_AUTOMATIC.md` (legacy ID V004; the side lane's write-up, first committed on the side-lane branch as `writeup/D_UNIFORM_AUTOMATIC.md` and placed in the V004 folder at the 2026-10-19 restructure) at commit `be73a66`, by the B16 migration (Claude, Opus 5.5). Text kept; the status paragraph rewritten as the introduction above, the checks moved under Certificates, the programme remarks and literature boundary under Remarks.
- Claude side lane (Opus), 2026-10-18 (feed 20:40, REFEREE V004).
