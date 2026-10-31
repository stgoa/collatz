---
id: positive-offset-kernel-ternary-closure
kind: result
title: The positive-offset binary sections of a 3x+1 invariant are closed under binary and ternary sections
status: formal
claim: >
  Let h be any colouring of the nonnegative integers with h(2n) = h(n) for all n and h(3n+1) = h(n) for odd n > 1.
  For every a >= 1, 0 < r < 2^a and j in {0, 1, 2} there are a' >= 1 and 0 < r' < 2^a' with
  h(2^a (3n+j) + r) = h(2^a' n + r') for every n >= 0, where a' = a + v (v in {1, 2}) and r' = (2^v c - 1)/3 when
  3 does not divide c = 2^a j + r, and a' = a - l + 4, r' = 16u + 1 when c/3 = 2^l u with u odd. So the family
  K_+ = {n -> h(2^a n + r) : a >= 1, 0 < r < 2^a} is closed under binary and ternary sections, and a ternary
  section raises the binary depth by at most 4. No finiteness, automaticity or Cobham is involved.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
lean:
  - LeanLane.Kernel.kernel_ternary_closure
  - LeanLane.Kernel.kernel_binary_closure
  - LeanLane.Kernel.id3
  - LeanLane.Kernel.example_12n5
  - LeanLane.Kernel.example_12n3
evidence:
  - "binary-automatic-invariant-colourings-constant/README.md section 3: the written proof; binary-automatic-invariant-colourings-constant/v004_rigidity_check.py part (b): every a <= 14 (98,256 sections) checked as integer relations"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: binary-automatic-invariant-colourings-constant/v004_rigidity_check.py
    scope: "Feed 20:40 and 20:55: closure checked over 98,256 sections with independent code; Lean V004-ii read from source and receipts, statement match and witnesses confirmed"
aliases: [V004-b]
tags: [invariants, kernel, ternary-sections, closure, formal]
---

# The positive-offset binary sections of a 3x+1 invariant are closed under binary and ternary sections

## Statement

Let `h` satisfy `h(2n) = h(n)` (all `n`) and `h(3n+1) = h(n)` (odd `n > 1`); the colour set is arbitrary. Put

```
K_+ = {n ↦ h(2^a n + r) : a ≥ 1, 0 < r < 2^a},    n ≥ 0.
```

A binary section with digit `j ∈ {0, 1}` replaces `(a, r)` by `(a + 1, r + 2^a j)`, so `K_+` is closed under binary sections. **It is also closed under every ternary section:** for `a ≥ 1`, `0 < r < 2^a`, `j ∈ {0, 1, 2}` and `c = 2^a j + r` (so `0 < c < 3·2^a`),

- **Case A** (`3 ∤ c`): with `v = 1` if `c ≡ 2` and `v = 2` if `c ≡ 1 (mod 3)`, and `t = (2^v c − 1)/3` (odd, `1 ≤ t < 2^(a+v)`): `h(2^a(3n+j) + r) = h(2^(a+v) n + t)`;
- **Case B** (`3 | c`): with `c/3 = 2^ℓ u`, `u` odd, `s = a − ℓ ≥ 1`: `h(2^a(3n+j) + r) = h(2^(s+4) n + 16u + 1)`, with `16u + 1 < 2^(s+4)`.

So every ternary section raises the binary depth by at most 4. Examples, for all `n ≥ 0`: `h(12n+5) = h(8n+3)` and `h(12n+3) = h(64n+17)`.

## Proof

The written proof is §3 of [`binary-automatic-invariant-colourings-constant`](binary-automatic-invariant-colourings-constant/README.md), using its identities (2) `h(3m+1) = h(4m+1)`, `h(3m+2) = h(2m+1)` and (3) `h(3u) = h(16u+1)` for positive odd `u`. Case A: for `x = 2^(a+v) n + t`, `3x + 1 = 2^v(3·2^a n + c)`, and (1) with doubling gives the identity (the colour equality at source 1 follows from `h(4) = h(1)`). Case B: doubling and (3) give `h(3·2^a n + c) = h(3(2^s n + u)) = h(2^(s+4) n + 16u + 1)`, with `2^s n + u` positive odd including at `n = 0`. The exceptional `c = 0` term, which introduced `h(3n)` in [`binary-kernel-first-ternary-image`](binary-kernel-first-ternary-image/README.md), is absent because `r > 0`.

## Lean

Lean unit V004-ii, [`lean/KernelClosure.lean`](../../../lean/KernelClosure.lean) (receipts `lean/receipts/KernelClosure.*`; axioms `propext`, `Classical.choice`, `Quot.sound`, some lemmas only `propext`, `Quot.sound`), namespace `LeanLane.Kernel`: `kernel_ternary_closure` states exactly the closure as identities of `h`: for `1 ≤ a`, `0 < r < 2^a`, `j < 3` there exist `a' ≥ 1`, `0 < r' < 2^a'` with `h(2^a(3n+j) + r) = h(2^a' n + r')` for all `n`, including `n = 0`; the witnesses are the prose ones (`(a+2, (4c−1)/3)` for `c ≡ 1`, `(a+1, (2c−1)/3)` for `c ≡ 2`, `(a−ℓ+4, 16u+1)` for `3 | c`). `kernel_binary_closure` is the binary closure, `id3` identity (3), `example_12n5` and `example_12n3` the two worked examples. **Statement match:** exact; the file does not mention automata, finiteness or Cobham, which enter only in V004-iii. (The build receipt `KernelClosure.build.txt` is empty; the side lane noted this as a minor receipt gap, the axioms receipt showing the declarations elaborated without `sorryAx`.)

## Remarks

- The depth bound "at most 4 per ternary digit" is what V005–V009 use for their depth conversions (`J_D(b) ⊆ K^+_(1+4D)(h)`, [`automatic-section-forces-constancy`](automatic-section-forces-constancy/README.md)).
- `3x+d`: the closure holds only up to bounded offset shifts ([`d-uniform-automatic-invariant-colourings`](d-uniform-automatic-invariant-colourings/README.md), Step 1); for `d = 1` the shift bound is 0.

## History

- New node by the B16 migration (Claude, Opus 5.5) from §3 of `experiments/viewpoints/V004/GLOBAL_RIGIDITY.md` (legacy ID V004) and the Lean unit V004-ii in the legacy `lean/STATE.md`, at commit `be73a66`.
- Main lane (ChatGPT/Codex), 2026-10-18; Lean V004-ii verified 2026-10-18 (Lean lane iteration 3, `claude/lean-lane` `d6195bf`; side-lane check, feed 20:55).
