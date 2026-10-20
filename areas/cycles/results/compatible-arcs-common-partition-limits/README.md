---
id: compatible-arcs-common-partition-limits
kind: result
title: "Unreviewed draft: a rotation-invariant partition or a shared background cannot cover sparse rotations"
status: proposed
claim: >
  Unreviewed work in progress (legacy C014), every part unverified. (i) For a cyclic word and a
  rotation by h with nonempty mismatch set S, the smallest cut set containing S + 1 and invariant
  under translation by h is the union of the residue classes mod d = gcd(m, h) that it meets, of size
  (m/d)·k; for coprime h it is every position. (ii) If a nonconstant primitive word of period m,
  after any cut and any repetition, has the form (U, a_0, U, a_1, …, U, a_(r−1)) with U nonempty and
  nonconstant markers, then b = |U| + 1 is a proper divisor of m and all residue columns mod b except
  the marker column are constant; so a word of prime period has no such representation. (iii) For every
  prime p ≥ 5, with A = ceil(p·log₂3) and u the lower mechanical word, w = (u_0, …, u_(p−2), 3) is
  primitive with ρ(w) = 3, A_w = A + 1 < 2p, and every state of its raw 3x+q cycle exceeds q·p/18
  (q ≤ L for p ≥ 19). No denominator bound or exclusion is claimed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [narrow-cycles-are-mechanical]
evidence:
  - "COMPATIBLE_ARCS.md: the draft's written arguments for (i)-(iii) and the q = 269 five-cycle example; OVERLAP_OBSTRUCTION.md: the rotated-resultant draft (rotated-residual-resultant-invariance); SIDE_REVIEW.md: the draft's read of the side-lane feed, including a proposed correction of C013's evidence labels; LITERATURE.md: source scope"
  - "check_overlap_arithmetic.py, overlap_arithmetic_audit.json: the draft's checker and receipt. Fails at its new path: it imports HERE.parent/'C013/check_overlap.py' and reads side-lane files from git at a fixed side commit by their old sidekick/ paths. Passed at be73a66 as experiments/cycle_spectrum/C014/check_overlap_arithmetic.py (about 21 s; archive/legacy-checker-run-be73a66.md). A passing draft checker is not a review"
  - "historical_gate.json: historical finite gate copied into the draft folder"
tags: [cycles, rotation-distance, work-in-progress, unreviewed]
---

# Unreviewed draft: a rotation-invariant partition or a shared background cannot cover sparse rotations

> **Work in progress, unreviewed.** Legacy C014 is ChatGPT's uncommitted C014 draft, committed on 2026-10-19 at the owner's request as it was left in the working copy when that lane paused (files dated 05:06–05:11). It has no report, and no other lane reviewed or verified it. Every statement below is the draft's claim, not an established result, and nothing in it upgrades any other node. Reviewing and completing it is itself a contribution.

## Statement

The draft tests two ways of extending [`shared-background-denominator-law`](../shared-background-denominator-law/README.md) from one repeated background to arbitrary sparse rotations, and claims that both fail on actual cycles.

1. **Invariant partitions need every cut.** Compare `w` with its rotation by `h`, mismatch set `S`, `|S| = s > 0`, cuts `C = S + 1`. A refinement into chronological intervals permuted by translation by `h` has cut set `F ⊇ C` with `F + h = F`, and conversely. The smallest such is

```
F_min = ∪_j (C + j·h),      |F_min| = (m/d)·k,                          (1)
```

with `d = gcd(m, h)` and `k` the number of residue classes mod `d` met by `C` (`2k ≤ s`). For `h` coprime to `m`, `F_min = Z/mZ`: `m` singleton intervals, however small `s` is. Arbitrary alphabets, periods and mismatch counts; no positivity or primitivity needed.

2. **Repetition cannot manufacture a shared background.** Let `w` be nonconstant of primitive period `m`, and suppose some cut of some repetition of `w` reads `(U, a_0, U, a_1, …, U, a_(r−1))` with `b = |U| + 1`, `r ≥ 2`, `U` nonempty and nonconstant markers. Then `b` is a proper divisor of `m`; at a suitable cut the residue columns `0, …, b − 2 (mod b)` are constant and only the marker column `b − 1` varies; the marker period is `m/b`. Conversely those column conditions give the representation. **Corollary:** a nonconstant word of prime period has no such representation, under any cut or repetition; only the empty-`U` case applies.

3. **Actual sparse-rotation cycles of every prime period.** For a prime `p ≥ 5` let `A = ceil(p·log₂3)`, `u_i = floor((i+1)A/p) − floor(iA/p)` (so `p + 2 ≤ A ≤ 2p − 2`, letters 1 and 2, last letter 2), and

```
w = (u_0, …, u_(p−2), 3),   m = p,   A_w = A + 1 < 2p,   D_w = 2^(A+1) − 3^p > 0.     (2)
```

`w` is primitive with letters 1, 2, 3 and a unique 3; `C_w = C_u`. The rotation by `h` with `hA ≡ 1 (mod p)` differs from `w` exactly at `{j − 1, j, p − 1}` with `j = p − h`, and every nonidentity rotation (coprime shift) meets all three symbols along its orbit, so `ρ(w) = 3` (3). Every rotated intercept satisfies `C/D_w > p/18` (4), so the raw primitive `3x+q` cycle (`q = D_w/gcd(C_w, D_w)`) has `L/q > p/18`, and `q ≤ L` for `p ≥ 19`. Both coverage failures (1) and (2) occur on this family: bounded `ρ`, unbounded period, unbounded `L/q`. No bound on `q` is claimed.

**Example.** `p = 5`, `A = 8`: `u = (1,2,1,2,2)`, `w = (1,2,1,2,3)`, `C_w = 319`, `D_w = q = 269`, `g = 1`, states `(319, 613, 527, 925, 761)`; rotation by two mismatches at positions 2, 3, 4.

## Proof

The draft's arguments are in [`COMPATIBLE_ARCS.md`](COMPATIBLE_ARCS.md) §§1–3 (kept unchanged, with its work-in-progress banner). In outline: (1) the orbits of `+h` are the residue classes mod `d`, each of size `m/d`. (2) With `d = gcd(m, b)`, the length condition `m | rb` makes the block starts visit every position of their class mod `d`, so each interior offset forces equality along a class mod `d`; `d = m` contradicts nonconstant markers; if `d < m` and `b > d`, the `b − 1` interior offsets meet every class mod `d`, so `w` would have period `d < m`; hence `b = d < m`. (3) Comparing mechanical phases 0 and 1 changes exactly one internal prefix floor (index `j` with `jA ≡ −1 mod p`), which with the edited last letter gives the three mismatches; for (4), prefix sums satisfy `P_j > jA/p − 1`, so each intercept summand exceeds `3^(p−1)/2`, raising one valuation never lowers an intercept, and `D_w < 3·3^p`.

None of this has been checked by anyone other than its author.

## Remarks

- **Scope (the draft's own).** These are coverage obstructions for two proposed reductions (a literal invariant interval partition; a common nonempty background), not failures of the shared-background theorem and not impossibility results for overlapping-arc methods: methods may keep overlapping intervals, compressed runs or identities without a partition. Neither part gives a lower bound on the cost of every arithmetic representation.
- **Controls.** The `q = 5, 7, 13` cycles remain legal; repeated `(2)` has no mismatches and is outside both hypotheses. [`two-defect-rotation-exclusion`](../two-defect-rotation-exclusion/README.md) and [`shared-background-denominator-law`](../shared-background-denominator-law/README.md) are unchanged.
- **Prior art (draft's audit, [`LITERATURE.md`](LITERATURE.md)).** Rotation Hamming distance is an established combinatorial object (Gabrić, "Words that almost commute"); the mechanical prefix construction is that of [`narrow-cycles-are-mechanical`](../narrow-cycles-are-mechanical/README.md) and R71. No novelty claimed.
- **Evidence-label dispute.** The draft's [`SIDE_REVIEW.md`](SIDE_REVIEW.md) proposes correcting C013's "nondiscriminating" label (see [`rotation-defect-denominator-candidate`](../../questions/rotation-defect-denominator-candidate.md)); the scope note it refers to (`EVIDENCE_SCOPE.md`) was never written.
- **Next step proposed by the draft.** A relative cancellation bound for compatible overlapping arcs whose cost is controlled by mismatch count, without the partition or common-background reductions: [`rotation-distance-growth`](../../questions/rotation-distance-growth.md).

## History

- Migrated from `experiments/cycle_spectrum/C014/` (legacy ID `C014`; no report; `COMPATIBLE_ARCS.md` is the draft's lead note and stays here unchanged apart from one link repair in `LITERATURE.md`) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Status `proposed` because the legacy record marks C014 as unreviewed work in progress; no claim was upgraded. Part of the draft became [`rotated-residual-resultant-invariance`](../rotated-residual-resultant-invariance.md).
- Main lane (ChatGPT/Codex), drafted 2026-10-19 (05:06–05:11) and left uncommitted when that lane paused; committed at the owner's request on 2026-10-19.
- **Link repair (2026-10-19, B04 migration).** `LITERATURE.md` linked to `../C011/` and `../C013/` legacy paths; only those link targets were repointed. It is not pinned by any receipt.
