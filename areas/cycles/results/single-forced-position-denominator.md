---
id: single-forced-position-denominator
kind: result
title: A reduced ordered cycle with a single forced position has D = q
status: formal
claim: >
  Raw odd-only 3x+q map, any q. In a reduced (gcd(q, n_0) = 1) circularly ordered primitive integer cycle
  whose sorted gap system has exactly one forced position (J = 1), 2^A − 3^m = q. Equivalently, for the
  word w of such a cycle gcd(C_w, D) = 1: the reduced denominator is exactly D, R71's exact denominator,
  derived from the gap closed form and q | D alone, without mechanical-word theory.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [ordered-gap-closed-form, ordered-cycle-sorted-rank-residues]
lean:
  - LeanLane.Cyc.OrdCycle.orb_inj
  - LeanLane.Cyc.OrdCycle.T_eq_zero_of_J_one
  - LeanLane.Cyc.OrdCycle.hr_eq_zero_of_J_one
  - LeanLane.Cyc.OrdCycle.T_seam_of_J_one
  - LeanLane.Cyc.OrdCycle.D_eq_q_of_J_one
evidence:
  - "Side-lane feed entry 2026-10-19 06:30, update 07:51 ('A precise form of J = 1 is R71/C004') and update 08:06 (Lean S1-d)"
  - "ordered-gap-closed-form/s1cd_gap_coprime_check.py: side-lane check; the 3 actual cycles with J = 1 have D = q (q = 5, minimum 23; q = 13, minimum 319; q = 23, minimum 7, m = 2), and all 65 rational ordered cycles with J = 1 have gcd(C, D) = 1. A certificate of that node since the B17 migration moved its helper jterm_gap_check beside it; passed at be73a66 as reviews/side_lane/s1cd_gap_coprime_check.py (archive/legacy-checker-run-be73a66.md)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Lean unit S1-d verified (iteration 46), statement checked against the feed's 07:51 argument (legacy lean/STATE.md row S1-d and its note)"
    link: ../../../archive/lean-lane/STATE.md
tags: [cycles, ordered-cycles, gap-system, exact-denominator, formal]
---

# A reduced ordered cycle with a single forced position has D = q

## Statement

Notation of [`ordered-gap-closed-form`](ordered-gap-closed-form/README.md). Let a primitive integer cycle of the raw odd-only `3x+q` map be circularly ordered and reduced (`gcd(q, n_0) = 1`), and suppose its sorted gap system has exactly one forced position: `J = 1`. Then

```
D = 2^A − 3^m = q.
```

In the word normalisation, `g = D/q = 1`: the reduced denominator is exactly `D`.

## Proof

Side-lane feed, update 07:51 (lightly edited). `J = 1` forces every sorted height to equal `h_[0] = 0`: a height change between adjacent sorted ranks would be a second forced position besides the seam. So the seam is the only forced position, and `T_seam = q·2^B` (the feed's `q·(2 − 1) = q` is the case `B = 0`). The closed form at the gap after the seam then has a single term: `D·Δ = 3^x·2^y·q`. For reduced cycles `q | D` ([`ordered-cycle-sorted-rank-residues`](ordered-cycle-sorted-rank-residues/README.md), C008's `q_dvd_D`), so `D/q` divides `3^x·2^y`; since `D` is odd and `gcd(D, 3) = 1`, `D/q = 1`.

## Lean

`lean/CycleSpectrum.lean`, Lean unit S1-d (iteration 46); axioms `propext`, `Classical.choice`, `Quot.sound`. `D_eq_q_of_J_one`: `gcd(q, n_0) = 1` and `J = 1` ⇒ `2^A − 3^m = q`. Steps: `T_eq_zero_of_J_one` (the seam is the only forced position: a pair `{r, m−1}` would give `J ≥ 2`), `hr_eq_zero_of_J_one` (all sorted heights 0), `T_seam_of_J_one` (`T_(m−1) = 2^B·q`), and `gap_closed_form` at the run start after the seam collapses to `D·Δ = 2^(E_(m−1))·2^B·q` (`orb_inj` locates the single term, `Finset.sum_eq_single`); `q ∣ D` gives `(D/q)·Δ = 2^(E+B)`, and `D` odd makes `D/q` a unit. The structure's `B` is only an upper bound on the heights, so the seam term is `2^B·q`; the extra power of two is absorbed. No `Odd q` hypothesis is needed. Starting at the run start after the seam, the seam is orbit position `m − 1`, so the single term carries `3^0` and the prose's `3^x` is `1` there.

## Remarks

- **Relation to R71.** This is R71-a's conclusion (`gcd(C, D) = 1`, the exact denominator of mechanical words, [`mechanical-word-exact-denominator`](mechanical-word-exact-denominator/README.md); see also [`narrow-cycles-are-mechanical`](narrow-cycles-are-mechanical/README.md)) for reduced ordered cycles with one forced position. "Narrow (`H < 2L`) ⇒ `J = 1`" is not formalised; with it, this would be a second formal proof of R71's exact denominator for narrow integer cycles. It adds nothing new for `d = 1`: these are bookkeeping identities for the ordered class, valid for every `q`.
- **Controls.** The actual `J = 1` cycles at `q = 5, 13, 23` have `D = q`, consistent with the claim.
- Novelty: none claimed.

## History

- Created from the side-lane feed entry of 2026-10-19 06:30 (update 07:51, "A precise form of `J = 1` is R71/C004", written at the Lean lane's request; update 08:06, Lean S1-d verified), by the B05 migration (Claude, Opus 5.5). Legacy ID S1 (part d); no legacy folder. Side lane (Claude, Opus); formalised by the Lean lane (Claude, Fable).
