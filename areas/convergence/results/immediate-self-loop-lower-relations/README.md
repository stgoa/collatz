---
id: immediate-self-loop-lower-relations
kind: result
title: "The immediate blocked-W9 self-loop of R75 is zero except on u = 453 mod 576, where it reuses an accepted W9 rule"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; the retained critical basis and returning class E of R75 with formal plans
  [x] = div H_x + sum A_x(v) P(v). For u in E put b = (4u-3)/9, y = u/3, s = S(y). The sum K of the local R40
  current and the R75 returning conversion is exactly, row for row, K = H_y - delta_y - H_s with requests {b:+1} +
  A_y - A_s. Both K and A_y - A_s vanish unless u = 453 mod 576; on that whole progression, with v = (u-3)/18 = 25
  mod 32 and z = (9v+1)/2, K = H_v - delta_(3v) - H_z and A_y - A_s = {v:+1} + A_v - A_z, whose unique highest
  critical rank is rho(v) = 3v with coefficient +1, and K is nonzero. Every such v already lies in the accepted
  (nonblocked) local W9 domain, so orienting the relation supplies no new accepted domain; the parent b keeps
  coefficient +1. Scoped to the immediate loop only; longer comparisons and other currents are outside it.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [common-critical-rank-basis, critical-nine-elimination]
certificates: [check_lower_loop_recompute.py, check_legacy_replay.py]
evidence:
  - "check_lower_loop.py, lower_loop.py, lower_loop_audit.json: the legacy implementation, checker and receipt: 894 returning inputs (218 nonzero, 676 zero), 64 progression boundaries, the u = 453 example (b = 201, lower vector {5: 1, 25: 1}, 14-row current) and 6 rejections. Fails at its new path: lower_loop.py loads ../critical_basis/ (now ../common-critical-rank-basis/) by its pre-migration folder name; and Its receipt pins the SHA-256 of this node's legacy note LOWER_LOOP_SCOPE.md, now an edited README, so it fails at its new path and in a legacy replay at earlier migrations (before rewritten notes were restored from git). Passed at be73a66 as experiments/residual_progress/lower_loop_scope/check_lower_loop.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); A replay at this migration, before the note was edited, passed (exit 0, receipt unchanged). Its audit is recomputed by check_lower_loop_recompute.py. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
aliases: [R78-b]
tags: [convergence, outer-residual, critical-basis, critical-nine, self-loop, scope]
---

# The immediate blocked-W9 self-loop of R75 is zero except on u = 453 mod 576, where it reuses an accepted W9 rule

## Statement

Odd-only clock, 1 absorbing; notation and exact currents of [`common-critical-rank-basis`](../common-critical-rank-basis/README.md) (R75), with formal plans `[x] = div H_x + Σ A_x(v)P(v)`; `E` the returning class.

For `u ∈ E` put `b = (4u − 3)/9`, `y = u/3 = (3b + 1)/4`, `s = S(y)`. The sum `K` of the local R40 current ([`critical-nine-elimination`](../critical-nine-elimination/README.md)) and the R75 returning conversion is, row for row,

    K = H_y − δ_y − H_s,   requests {b: +1} + A_y − A_s.

1. **Classification.** `K` and `A_y − A_s` both vanish unless `u ≡ 453 (mod 576)`.
2. **The nonzero case.** On that whole progression put `v = (u − 3)/18 ≡ 25 (mod 32)`, `z = (9v + 1)/2`. Then `K = H_v − δ_(3v) − H_z` and `A_y − A_s = {v: +1} + A_v − A_z`; the unique largest critical rank is `ρ(v) = 3v`, coefficient `+1`, and `K ≠ 0`.
3. **Scope.** Oriented at `v`, the relation is the single arrow `3v → z` followed by existing formal plans; every such `v` has `v2(9v − 1) ≥ 5` and is already in R75's accepted local W9 domain. No new pair coverage follows, and the parent `b` keeps coefficient `+1`.

This concerns the immediate self-loop only, not longer loops, other source representations or other signed cancellations.

## Proof

The legacy note "What the nonzero lower relation in the immediate self-loop supplies" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written scope classification and finite exact audit.** This identifies
all lower relations left by the immediate blocked-W9/E composition in R75.
Its nonzero cases give already decreasing W9 comparisons. It supplies no new
accepted domain and does not concern arbitrary longer loops or other currents.

Use the notation and exact currents of the
[critical-basis compiler](../common-critical-rank-basis/README.md). Write the
original critical formal absorption plans as

    [x] = div H_x + sum A_x(v) P(v).

All missing pair currents remain premises. This note preserves the nonzero
counterexample in R75; it does not reinstate the refuted universal-zero claim.

### 1. The full immediate-loop identity

Let u belong to E_return, and set

    b = (4u-3)/9, y = u/3 = (3b+1)/4, s = S(y).

Thus y=7 modulo 24, 9y is selected, and b is the blocked W9 input.
The sum K of its local R40 current and the R75 returning conversion is
exactly, row for row,

    K = H_y - delta_y - H_s,
    requests = {b:+1} + A_y - A_s.                    (1)

To prove this, the local upper prefix is the same path 3b→rho(u) as the
returning conversion, with opposite sign. The formal plan at rho(u) is
`-N_(3u)+H_u` with requests `{u:+1}+A_u`; these terms cancel as well.
The local lower path is b→y→s. Since b is canonical and 1 modulo 8,
its formal plan begins `H_b=delta_b+H_y`. This proves (1), including the
signed rows, rather than just the divergence. In particular

    div K = -sum (A_y-A_s)(v) P(v).                  (2)

### 2. Complete zero/nonzero classification

**Theorem.** Both K and A_y−A_s vanish unless

    u = 453 mod 576.

On that entire progression put

    v = (u-3)/18 = 25 mod 32, z = (9v+1)/2.

Then b=8v+1, y=6v+1, and

    K = H_v - delta_(3v) - H_z,
    A_y-A_s = {v:+1}+A_v-A_z.                        (3)

The unique largest critical rank in this vector is rho(v)=3v, with
coefficient +1. All other requests have rank strictly below 3v.

**Proof.** Put a=v2(y+1)>=3. If y is canonical, s is canonical and 2
modulo 3, and its formal inverse step returns y. Therefore
`H_s=-delta_y+H_y`, with identical request vectors, proving zero in (1).

If y is selected, put c=(y-1)/2. Then c is canonical, s is selected, and
`nu(s)=S(c)`. The explicit selected-prefix currents satisfy
`N_y=delta_y-delta_c+N_s`: remove their first arrow on each side and the
remaining prefixes agree. Consequently (1) becomes

    K = H_c - delta_c - H_(S(c)),
    A_y-A_s = A_c-A_(S(c)).                           (4)

The condition that 9y is selected excludes a=4. For a>=5, S(c) is again
canonical and 2 modulo 3; its formal inverse step returns c, so (4) is
zero. For a=3 write y=8t-1. Selection of y requires t=3 modulo 4;
selection of 9y sharpens this to t=3 modulo 8. The condition y=7 modulo
24 also gives t=1 modulo 3. Thus t=19 modulo 24, equivalently
u=3y=453 modulo 576. Now c=3v with v=25 modulo 32, and S(c)=z.
The critical formal step at c requests P(v) and then H_v, which gives (3).

Finally A_v has rank at most v. The number z is 1 modulo 8, so its first
ordinary successor x is at most (27v+5)/8. If v2(3z+1)>=3, then x<3v.
Otherwise x=(27v+5)/8 is 1 modulo 4. If x=5 modulo 8 it normalizes below
x/4; if x=1 modulo 8 its next ordinary step is at most
(81v+23)/32<3v. These compulsory initial steps have no critical requests.
Thus every A_z request has rank below 3v. It cannot cancel the coefficient
+1 at v, so the vector and its nonzero divergence are genuinely nonzero.
The pair sources are linearly independent on finite critical supports:
the atom at the largest upper endpoint 3w has no larger index to cancel it.
This also proves K is nonzero. ∎

### 3. What orienting the relation accomplishes

Equation (3) gives the valid conditional comparison

    P(v) = div(delta_(3v)+H_z-H_v) + sum(A_z-A_v) P.  (5)

This is precisely the single ordinary arrow 3v→z, followed by the existing
formal plans. Every v=25 modulo 32 already has v2(9v−1)>=5, so it is in the
accepted local W9 domain of R75. No new pair coverage follows from (5).
The source of the b=201,u=453 counterexample is v=25, and its lower vector
is `{25:+1,5:+1}`. The original parent b still has coefficient +1 in (1).

This settles the immediate-loop simplification only. Longer comparisons,
alternative source representations and useful signed cancellations remain
outside the classification.

### 4. Reproduction

Run `python3 experiments/residual_progress/lower_loop_scope/check_lower_loop.py`.
The default replay verifies the stored receipt; `--write-receipt` refreshes
it intentionally. Checks include the full rows of (1) and (3), independent
one-arrow divergences, progression boundaries, all stated zero cases,
large exact inputs, already accepted W9 targets, and rejection controls.
Finite checks support the implementation; the universal classification
rests on the proof above. No absorption search is used.

## Certificates

[`check_lower_loop_recompute.py`](check_lower_loop_recompute.py) (written at the B13 migration; standard library). At the B13 migration no legacy check of this node passed: its legacy checker pins the SHA-256 of notes that are now edited READMEs. Since the replay restores those notes from git, the unmodified checker now passes too (see below). The certificate rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, replaces each pinned note by a placeholder, imports the unmodified legacy checker there and runs its audit, and requires the result to equal the committed receipt after removing only those note hashes; every other value, including the hashes of the pinned code and data, must agree. It writes nothing in the repository. It recomputes the 894-input classification, the 64 progression cases, the `u = 453` example and the 6 rejections (about 15 s). The command in the legacy text names `experiments/residual_progress/lower_loop_scope/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_lower_loop.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 19 s). It checks finite steps only; the status is unchanged.

## Remarks

- This settles the immediate-loop simplification only. It preserves the nonzero counterexample of [`common-critical-rank-basis`](../common-critical-rank-basis/README.md) (`u = 453`, `b = 201`) and does not reinstate the refuted universal-zero claim.
- The ledger lists this result as a supplement to R75 inside the R78 entry; the alias R78-b follows the migration plan. The main R78 result is [`native-critical-nine-continuation`](../native-critical-nine-continuation/README.md).
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/lower_loop_scope/LOWER_LOOP_SCOPE.md` (legacy ID R78-b) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "written scope classification and finite exact audit (the ledger records it as a supplement to R75 under R78)".
- The main lane's own proof, checker and default-replay review passed (archive/convergence-residual-progress/REPORT.md); that review was internal to the main lane.
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `3b0c8a5`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
