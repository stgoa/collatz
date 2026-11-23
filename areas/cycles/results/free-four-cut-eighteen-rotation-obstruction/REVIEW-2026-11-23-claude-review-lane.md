# Review of free-four-cut-eighteen-rotation-obstruction, 2026-11-23

- **Reviewer.** Claude review lane (Fable 5.2; independent subagent; directed by Santiago Armstrong).
  I did not write this node and took no part in its authoring session (Codex lanes, GPT-6). I saw only the
  committed files. I read both certificates before writing my own scripts, since they are part of what is
  reviewed; my scripts are therefore independent in code and in test data, not in ignorance of the node's code.
- **Version reviewed.** Working tree at commit `b549f61`; the node was last changed in `0912d53`. Blobs:
  `README.md` `eb044f07563b`, `check_free_cuts.py` `f448aa58d31e`, `check_free_cuts.json` `8e79f739d18f`,
  `free_cut_duals.json` `3574caddcd89`, `check_stronger_margin.py` `950d84e72f63`,
  `check_stronger_margin.json` `abb416f11801`, `stronger_margin_duals.json` `03fff9839990`.
- **Scope.** The whole node: frontmatter claim, Statement, Proof sections 1 to 6, both certificates, both
  proof-data files, both receipts, the controls. Both parameter theorems, (4) with `R = 3/8`, margin `1/10000`,
  and (4*) with `R = 37/100`, margin `1/750`.
- **Verdict.** HOLDS. I found no mathematical error and no overclaim. The statement, the two receipts and the
  written proof agree. Nothing has to change; the findings below are remarks and suggestions.

## What I checked

1. **Statement and scope.** Pure circle geometry: `0 < h < 1/2`, `j h` not an integer for `1 <= j <= 18`, four
   distinct cuts, `f(0) = 1`, `f(x) = x` otherwise, `C_j` as a set, the gap ending at `e`, the paired height
   `max(f(e), f({e + j h}))`. The frontmatter claim, the Statement and what the proof proves coincide. The
   non-strict hypothesis `D_j(e) <= epsilon` is handled (section 4 starts from "all at most some
   `epsilon < eta`"). No cycle, map or clock enters, and the Remarks say what a cycle application must still
   supply. Neither of (4), (4*) follows from the other by the comparison `D* = D + (1/200) height` (it gives
   only `max D* >= 1/10000` and `max D >= 1/750 - 1/200 < 0`), so the two separate certificates are needed,
   as the text says.
2. **Sections 1 and 2, the branch tree.** For a generic configuration exactly one alternative holds at every
   decision: the position of the threshold `1 - {j h}` among the `4j` ordered cuts (`4j + 1` positions), the
   wrap of `{j h} + h` (floor 0 or 1, because `0 < {j h} + h < 3/2`), and for each of the four new cuts its
   wrap (`e - h` or `e - h + 1`, because `-1/2 < e - h < 1`) and its rank in the current order. The two cases
   of (9) are right: for `e < 1 - {j h}` the partner is `e + {j h} > e`, otherwise it is `e + {j h} - 1 < e`.
   The wrap-around gap `1 + e_1 - e_(4j)` is included. The script visits every alternative
   (`for split in range(len(chain)+1)`, `for floor in (0, 1)`, `for offset in (1, 0)`,
   `for rank in range(len(ordered)+1)`) and drops a branch only in `extend`, on a verified contradiction or on
   a constant row `0 < b` with `b < 0` (which never occurs in the replay). A branch that reaches the gap rows of
   rotation 18 unclosed raises.
3. **Section 3, the duals.** A row is a strict inequality `a . x < b`; a dual has weights `> 0` with sum 1,
   `sum(w a) = 0` and `sum(w b) <= 0`. The checker tests exactly this with `Fraction` before any use
   (`weight > 0`, `mass == 1`, `not any(combined[:5])`, `combined[5] <= 0`), and applies a dual only when the
   bit mask of its rows is contained in the mask of the rows generated on the current branch. Rows are
   normalised by a positive gcd only, so orientation is kept. A zero right side is legitimate because every
   row of a generic cell is strict. I checked that the 60 (resp. 59) duals with right side exactly 0 use
   structural rows only (domain, wrap, order), none of the gap rows: they do not touch the margin.
4. **Section 4, the boundary.** Re-derived. With `h` fixed, the conditions "two raw cuts from the same base
   cut coincide" are excluded by (1) (`t h` not an integer for `0 < |t| <= 17`); every other degeneracy (two
   raw cuts from different base cuts, a raw cut at 0, a partner at 0, i.e. `c_l + k h` an integer for some
   `-17 <= k <= 18`) is a proper affine condition on the cuts, so small generic left displacements avoid all
   of them. After the displacement a cut or partner that was at 0 sits just below 1, where `f` tends to
   `1 = f(0)`; all other heights move continuously. A split cluster produces one gap tending to the old gap,
   with the old paired height, and gaps tending to 0 whose deficits tend to `-R height < 0`. So every new
   deficit is below `eta` for a small enough displacement, which contradicts the generic statement. The
   argument does not move `h`, and it is the same for (4*).
5. **Section 5, the control.** Replayed with my own exact code: for `h = 5734/14751` and
   `C = {0, 3283/14751, 2347/4917, 932/1341}` the maximal deficit over `j <= 17` is `-11/10728` (attained at
   `j = 5` and `j = 13`), and `235/14751` at `j = 18`; with `R = 37/100` the values are `43/491700` and
   `659/40975`. The denominator of `h` is 14751, no `j h` with `j <= 18` is an integer, and the numbers of
   distinct cuts are `4, 8, 11, 14, ..., 56` (one coincidence chain, the second cut is `-2h`). The order-18
   control gives `-7/9216`, `155/9216` and, at `37/100`, `13/38400`, `217/12800`.
6. **Section 6, the second parameter theorem.** Row (14) is `6000 (gap - (37/100) H - 1/750) < 0`; row (15)
   follows because `H` is `e` or `e + {j h}`, both in `(0, 1)` on the cell. The replay adds both rows.
7. **Certificates.** Both pass and reproduce their receipts under Python 3.10.17, 3.11.10, 3.12.10 and
   3.13.11, each with and without `-O` (about 1.3 s and 2.0 s under 3.12). Every number quoted in the README
   is in a receipt: 4,708 duals, 29,781 queries, 27,924 closed; 4,273 duals on 1,071 rows, 29,114 queries,
   27,318 closed; the control values above. `tools/check.py` reports 413 nodes, 0 errors, 0 warnings.

## How

All scripts use the standard library only and import nothing from the repository. They are kept outside the
repository.

| Script | Content | Result |
|---|---|---|
| `n1_duals.py` | every dual of both files in integer arithmetic (weights parsed by hand, cleared to a common denominator): weights `> 0`, sum 1, the five variables cancel, right side `<= 0`, stored `gap` equals the recomputed right side | 4,708 and 4,273 duals valid; 60 and 59 with right side 0; 1,066 of the 2,723 rows of the first table and all 1,071 rows of the second occur in a dual |
| `n1_tree.py` (enumerate) | my own implementation of the tree of sections 1 and 2, rows generated from the definitions, closure only by a verified dual whose rows are all present | no surviving branch; 29,781 queries and 27,924 closures for `3/8`, 29,114 and 27,318 for `37/100`; the same numbers of rotation calls per `j` as the receipts; identical result when every dual is scanned at every node |
| `n1_tree.py` (trace) | 4,000 random generic points per parameter set (uniform cuts; cuts near `{0, -h, p, q}`; cuts that are translates of one another by multiples of `h`, nudged; perturbations of control (5)), followed down the tree with exact rationals | at every decision exactly one alternative is consistent with the point; 709,200 and 648,208 gap rows equal the deficit computed from the Statement; every path ends in a closed node (1,014 and 923 of them only at the gap rows of rotation 18) |
| `n1_attack.py controls` | the controls of the README | as in item 5 |
| `n1_attack.py lattice 19 34` | all non-generic lattice configurations: `h = a/M`, `19 <= M <= 34`, four cuts `k/M` (cuts and partners at 0, many coincidences), and for `M <= 24` two phases 0 and `1/2`; exact integers | 4,693,432 configurations per parameter set; smallest maximal deficit `1/120` (`3/8`) and `41/4200` (`37/100`) |
| `n1_attack.py structured` | 3,000 random non-generic configurations (2,546 with coincident raw cuts, 759 with a cut at 0, 1,973 with a partner at 0), exact | both statements hold; smallest `53/1408` and `721/17600` |
| `n1_boundary.py` | section 4 on six exact non-generic configurations (control (5), the order-30 control, lattice configurations, the best point of the family below), both coefficients, 20 random left displacements of about `1e-10` each | every displaced configuration is generic and its maximal deficit exceeds the old one by less than `1e-9`; right displacements raise it to between `0.075` and `0.231`, so the one-sidedness is essential |
| `n1_attack.py family 2` | exact local search in the non-generic family `{0, -2h, p, q}` of control (5), denominators `10^7` | 215,953 and 219,670 exact evaluations; smallest `29217/10000000` (`3/8`) and `677891/200000000` (`37/100`) |
| `n1_attack.py search` | float local search over `(h, c_1, ..., c_4)`, four runs of 600 s per coefficient, 5,381 and 5,234 restarts, 269,964,329 and 270,677,588 evaluations; best point re-evaluated exactly | smallest maximal deficit `0.0027394752` (`3/8`) and `0.0032274566` (`37/100`); all eight runs end near `h = 0.3905`, cuts near `0.99, 0.219, 0.471, 0.695`; there the maximum is attained at rotation 5 or 18 |
| `n2_geometry.py lemma Mlo Mhi 37 100 1 750 18`, run on the ranges 19-26, 27-31, 32-35, 36-38, 39-40 | (4*) for cuts on one or two tracks of `h = a/M`, `19 <= M <= 40`, by an exact method that uses neither the duals nor polygon clipping | 56,845,798 (shift, family) pairs over 194 shifts, none admits a strict solution at margin `1/750`; at most 5 rotations are needed; also 3,964,385 pairs for `19 <= M <= 26` at `3/8`, `1/10000` |

No configuration with maximal deficit below the claimed thresholds was found.

## Findings

1. **Remark (environment).** The certificates need Python 3.10 or later (`int.bit_count`), as the README
   says. On the review machine the default `python3` is 3.9.6, where
   `python3 tools/run_certificates.py --node free-four-cut-eighteen-rotation-obstruction` reports two failures
   (`AttributeError: 'int' object has no attribute 'bit_count'`). With 3.10, 3.11, 3.12 and 3.13 both pass.
2. **Remark (certificate coverage).** Nothing in the two certificates compares the affine rows of the tree
   with definition (3): the finite controls and the order-30 control evaluate the definition directly and
   never go through the tree. The link is therefore established by reading. My trace check closes it
   (1,357,408 gap rows equal to the definition on 8,000 generic points). Suggestion: add such a traced-point
   control to the certificate, as the dependent node does for its rows (`direct_row_controls`).
3. **Remark (margins are not sharp, as the node says).** The best configurations I found have maximal
   deficit `0.00274` at `3/8` (claimed bound `1/10000`) and `0.00323` at `37/100` (claimed bound `1/750`).
   The README asserts no optimality; this only records the room: a factor 27 and a factor 2.4.
4. **Remark (receipts).** `unpruned_horizon_branches: 0` in the receipts and `survivors: 0` in the printed
   line are literals, not counters. This is sound, because an unclosed branch at rotation 18 raises before the
   receipt is built, but a counter would say more.
5. **Remark (provenance).** The duals were found by a numerical LP (NumPy/SciPy) that is not in the
   repository. The proof does not need it: each dual is verified exactly and is used only where its rows are
   present. The row table of `free_cut_duals.json` has 2,723 rows, of which 1,066 occur in a dual (every row
   my replay generated is in the table); the second file keeps only the 1,071 rows used.
6. **Remark (wording).** Section 4: "because the paired heights are nonnegative". They are strictly positive
   (`f` takes values in `(0, 1]`), so the limits of the new deficits are negative, not only nonpositive.

## Corrections

None required.

## What I could not check

- **Infeasibility of the cells without the stored duals.** I have no exact LP solver of my own. What I
  verified is: each stored dual is a valid certificate; my own code generates the rows of every branch; every
  branch contains the rows of a valid dual. For cuts on one or two tracks with `19 <= M <= 40` and generic
  phases I did verify (4*) without the duals (and at phase 0 by the lattice run, for `M <= 34`).
- **The optimal margins and the optimal horizon in general.** Seventeen rotations are insufficient by control
  (5), which I replayed; I did not determine the exact infimum of the maximal deficit with eighteen rotations
  (only the search values above).
- **Lean.** There is none for this node.
- **Novelty.** Not assessed.
