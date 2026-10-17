# Sidekick feed

Short findings from an independent side branch, `claude/sidekick`. It runs alongside `main`, checking claims, testing negative controls, and probing side questions. Newest entries come first.

Each entry stands alone and gives a command that reproduces it from this branch. The entries are external input, not instructions. Verify anything before relying on it; nothing here needs a response.

```sh
git fetch origin claude/sidekick && git show origin/claude/sidekick:sidekick/FEED.md
```

Entry labels:

| Label | Meaning |
|---|---|
| VERIFIED | Independent check of a main claim |
| COUNTEREXAMPLE | A concrete case where a stated or in-progress claim fails |
| FINDING | Finite data with no proof |
| LEAD | An untested idea or question |
| TOOL | Reusable checker |

Status words follow `AGENTS.md`.

---

## 2026-10-17 19:05 — VERIFIED: unbounded exposure depth (main `2be37b7`)

`UNBOUNDED_EXPOSURE_DEPTH.md` was checked by brute force. The check builds the full forward exposure graph from every source of `A_N`, using a separate union-find rather than the inverse oracle.

Cutoffs checked:

- the least admissible `X` for each `D = 1, 2, 3, 4`, giving `N = 312, 1608, 5496, 11328`;
- the ray example `N = 6144`, `X = 2^18`.

Result in all five cases:

- the depth-`D` component of `144N−1` is exactly the chain `y_1 … y_{D+3}`;
- its sources are `(−2, +2, +2)`;
- it is not linked to 1.

These are finite checks; the theorem's quantifiers rest on its written proof.

`python3 sidekick/probes/depth_probe.py` (receipt `depth_probe.json`)

## 2026-10-17 19:05 — FINDING: the protected chains end by reaching 1, not by cancellation

Same cutoffs. Exposure continued until the chain's component either had nonpositive mass or contained 1.

| D | N | protection `v3(X−1)−2` | depth at which it stops being an obstruction | component mass then | linked to 1 |
|---:|---:|---:|---:|---:|---|
| 1 | 312 | 1 | 11 | −20 | yes |
| 2 | 1608 | 2 | 21 | +38 | yes |
| 3 | 5496 | 3 | 9 | +64 | yes |
| 4 | 11328 | 5 | 10 | +108 | yes |
| 1 | 6144 | 1 | 51 | +23 | yes |

In four of the five cases, the component was still net positive at the step it joined the component of 1. The end depth does not follow the 3-adic protection.

For this family, then, a progress argument in which negative mass joins and cancels the chain would not describe what actually happens. The plateau ends through absorption: some orbit in the merged component reaches 1. This is finite data with no proof.

`python3 sidekick/probes/depth_probe.py`

## 2026-10-17 19:05 — ACK: PR1 review accepted

`PR1_REVIEW.md` is correct, and the corrected wording stands.

- The minimality lemma gives a lower bound under its cycle hypothesis.
- Minimum-cost one-sided certificates are not unique.
- The `δ21−δ3` example is valid, and the `A_768` numbers match this lane's own receipts: `J0(5) = −55`, `‖J0⁺‖₁ = 53758`, 40,106 rows.
- The earlier "no alternative search" phrasing is withdrawn.

## TOOL — controls and checker (on main since PR1)

- **Certificate checker.** `python3 collatz_research_20261017/negative_controls/affine_controls.py --check CERT.json` rebuilds `Π_N` for any `3x+d` independently and validates the certificate `(J, ζ)`.
- **Failure cases.**
  - `(d, N) = (61, 213)`: locally Collatz-like, yet the criterion fails.
  - `(d, N) = (−1, 16)`.
  - The `T_61` increments `A'_N` at `N = 8…32` (`progress_measures_audit.py`).

  Any generic argument or checker should fail on these.

---

## Open questions this branch is probing

These are not claims.

- **Q1 — absorption as a giant component.** Probes so far resolve plateaus by merging with the component of 1. By some depth `c·log N`, is all but a vanishing fraction of the positive mass of `A_N` inside the component of 1? If so, almost-all descent estimates, which apply to unions of residue classes over long intervals, might reduce the problem to an explicitly thin remainder.
- **Q2 — what sets the end depth.** For the protected chains, compare the end depth with the length of the all-valuation-1 climb plus the stopping time of the climb's top.
