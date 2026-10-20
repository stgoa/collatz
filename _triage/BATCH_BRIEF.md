# How to migrate a batch

You are migrating one batch of legacy material from `_triage/` into the knowledge graph. This is slow, careful work. **Fidelity beats speed and beats elegance.** The repository is a research record, so a lost caveat or an inflated status is worse than an ugly node.

## 0. Read first

1. `AGENTS.md`, `conventions/SCHEMA.md` and `conventions/NOTATION.md`, in full. They are binding.
2. `_triage/MANIFEST.md`: the rows of your batch (first column).
3. Context for your area, read-only:
   - `_triage/docs/STATUS.md`, `FRONTIER.md`, `RESULTS.md`, `CONVENTIONS.md` (§4 maps legacy status labels; §6 is the ID glossary);
   - the legacy line README (e.g. `_triage/experiments/cycle_spectrum/README.md`);
   - `_triage/lean/STATE.md`, for the results that have Lean units.
4. The nodes that already exist (`MAP.md`, `areas/`, `sources/`), so that you reuse their ids instead of creating duplicates.

## 1. For each legacy unit in your batch

Read **every** file of the unit:
- Markdown, in full;
- scripts: the header, docstring and `main`;
- receipts: skim them, to know what they certify.

Then decide what nodes the unit becomes.
- **One idea, one node.** A report proving one main theorem is one `result`. A report with several independent lemmas that others cite separately becomes several results. Do not split mechanically: split where a reader would cite the pieces separately.
- **Refuted mechanisms and rejected routes** become `attempt` nodes, or `result` nodes when the obstruction is itself proved.
- **Open targets** stated in the report become `question` nodes, unless an equivalent question node already exists; then link that one.
- **Ids:** descriptive slugs per `conventions/SCHEMA.md` §2. Put the legacy ID(s) in `aliases`, e.g. `C011`, `S13`, `R71`, `V004`. When a legacy ID splits into several nodes, give the main node the plain alias and the others suffixed ones (`C011-b`, …), or none.

## 2. Moving files

- Use `git mv` for every file you keep, so history follows it. Never copy and delete.
- The legacy report (`REPORT.md`, `README.md` or similar) becomes the node's `README.md`. `git mv` it first, then edit it in place.
- Scripts, receipts and data move **byte-identical** into the node folder they support. **Never edit a legacy script or receipt.** They are hash-pinned historical artefacts.
- A file that supports several nodes goes into the folder of the main one; the others list it under `evidence` with a relative path.
- A side-lane review of the unit goes into the node folder, keeping its file name. Examples: `_triage/reviews/side_lane/c004_narrow_check.py` and its `.json`, or a `side_lane_review_*.md`.

## 3. Writing the node

- **Frontmatter:** every required field. `created` is the date of the legacy original's first commit (`git log --follow --diff-filter=A --format=%as be73a66 -- <legacy path> | tail -1`; `--follow` traces earlier renames, and for a folder take the earliest date over its files).
- **Body:** the sections of SCHEMA §6, in order.
  - The legacy text may be **lightly** edited: restructured into sections, notation aligned with NOTATION.md, links fixed, legacy status vocabulary replaced.
  - **Never change mathematical content, strengthen a claim, or drop a caveat, scope limit, correction or "heuristic" label.**
  - If the legacy text is long and well-structured, keep it, under `## Proof` or `## What happened`.
- **`## History`:** at least the line "Migrated from `<old path>` (legacy ID `<ID>`) at commit `be73a66`." Add the legacy authorship lane and any dated corrections.
- **Links:** relative links only, and every one must resolve. Links into `_triage/` are forbidden, because it will be deleted. Point to nodes. If a target has not been migrated yet, write its legacy ID in plain text and the path in a code span, not as a link.

## 4. Status: be conservative

Map legacy labels with `_triage/docs/CONVENTIONS.md` §4, then apply these rules:

| Legacy situation | New status |
|---|---|
| Complete written proof by the main lane or the side lane, with a side-lane or Lean-lane **review verdict on record** (VERIFIED, REFEREE pass, CONFIRMED, a review file) by a different lane | `reviewed`, with a `reviewed_by` entry citing the review file or feed entry |
| Complete written proof, no independent review on record | `written` |
| Lean unit marked verified in `lean/STATE.md` whose declarations exist in `lean/` | `formal`, **only if** the node's `## Lean` section can state the statement match from STATE.md. Otherwise `reviewed` or `written`, listing the declarations under `lean` anyway. |
| Finite computation | a `result` whose claim is exactly the finite statement (`written` or `reviewed`). Any extrapolation beyond it goes in a separate `proposed` node or a `question`, labelled heuristic. |
| Heuristic, candidate, conjecture | `proposed` result, or `question` |
| Rejected, refuted | `refuted` (with `refuted_by`), or an `attempt` |
| C014 (committed as unreviewed work in progress) | `proposed` |

Authors, written as name before parentheses, as the reviewer check requires:
- main lane: `ChatGPT main lane (Codex)`;
- side lane: `Claude side lane (Opus)`;
- Lean lane: `Claude Lean lane (Fable)`;
- other Claude lanes: `Claude audit lane (Opus)`, `Claude explicit-Tao lane (Opus)`, `Claude PR1 lane (Opus)`;
- the owner: `Santiago Armstrong`.

External inputs (published bounds, outside Lean libraries) go under `assumes` as `source` ids. Batch B01 created the sources. If you need one that does not exist, create it with the source template.

## 5. Scripts: certificate or evidence

Legacy scripts load each other by their pre-migration paths, so most no longer run where they now live. **`tools/legacy_replay.py` replays them unmodified**: it rebuilds the pre-migration tree in a temporary directory from `tools/legacy_paths.json` and requires exit 0 with every file byte-identical afterwards.

1. After your move commit, run `python3 tools/legacy_replay.py --update-map`. It regenerates the map from git, adding your moved files; include `tools/legacy_paths.json` in your edit commit.
2. For each legacy check script of a node, first try it in place: `python3 _triage/try_script.py <current path>` (10-minute timeout). If it exits 0 and leaves its receipt unchanged (`git status`), list it under `certificates`.
3. Otherwise replay it. Rewritten legacy notes (for example a `REPORT.md` that became a node README) are restored from git with their original bytes, so checkers that pin their note's hash still replay: `python3 tools/legacy_replay.py <legacy path> [...]` (legacy path = its path at `be73a66`, e.g. `experiments/residual_progress/nonselected_inverse/check_inverse_phases.py`). If the replay passes, the node gets **one** certificate `check_legacy_replay.py` that replays its scripts. Copy the shape of `areas/convergence/results/critical-image-rank-composition/check_legacy_replay.py`: the docstring names what each script checks, and `SCRIPTS` lists the legacy paths. Scripts that need arguments use `legacy_replay.main(SCRIPTS, args={...})`.
4. A script that fails both ways, needs network access, or is exploration goes under `evidence`, as: `<file>: passed at be73a66 as <old path> (archive/legacy-checker-run-be73a66.md)`. Use whatever note is true for that script ("failed at be73a66 by design: pinned to a historical commit", "exploration probe, not a checker", …).
5. Never edit legacy scripts or receipts, and do not "fix" scripts to make them pass.
6. Only if a node has no passing legacy check at all may you write **one new, small certificate** in its folder. It must use the standard library only, run from the repository root, and recompute what the legacy receipt certifies (or a stated part of it) from the committed data. Its docstring opens with "Written at the <batch> migration", and the node's `## Certificates` section says so. It must agree with the legacy receipt.

## 6. Bookkeeping

- For every manifest row of your batch, change `pending` to its fate: `node <id>[, <id>…]`, `archive <path>` or `dropped: <reason>`. Every row must end non-pending.
- Material that is valuable but fits no node goes to `archive/<area>-<what>/`, for example lane logs and briefs. Add a row to `archive/README.md`. Drop only true duplicates and generated junk, and say why.
- If your batch is the last one of an area, write that area's `OVERVIEW.md`:
  - at most ~120 lines;
  - the question, the main lines, the strongest results, the open questions, the dead ends;
  - every claim linked to its node.
  - It summarises; it does not prove.
- Run `python3 tools/build_map.py && python3 tools/check.py`. It must report **0 errors**.

## 7. Commit

**Two commits per batch, so that `git log --follow` traces every file.**
1. A **move commit**, `Migrate <batch> (1/2): move files`. It contains only `git mv`s: each legacy report moves to its node path (`.../<id>/README.md` or `.../<id>.md`) and each script or receipt to its node folder, all byte-identical, with no edits.
2. An **edit commit**, `Migrate <batch> (2/2): <one line>`, with the frontmatter, the rewrites, new files, the manifest and MAP.md.

**Forward references:** when a node needs a target owned by a later batch, add a row to `_triage/FOLLOWUPS.md`. When your batch creates a target listed there, resolve its rows and delete them.

Work in the main worktree, on branch `refactor/pristine`. Batches run one at a time. Stage only your own paths (for example `git add areas/cycles _triage MAP.md`). Never run `git add -A` at the root: the untracked `sidekick/` folder must stay untracked. In the edit commit's message, the body lists the nodes created, with their statuses, and anything archived or dropped. End it with the Co-Authored-By line you were given.

Do not push. Do not touch files outside your batch, except:
- `MAP.md` and `tools/legacy_paths.json` (regenerated);
- `_triage/MANIFEST.md` (your rows);
- `archive/README.md` (your rows);
- `sources/` (new sources only);
- your area's `OVERVIEW.md`.

## 8. Report back

Report:
- the nodes created (id, kind, status);
- the status decisions that were judgement calls, and why;
- the scripts that moved from passing to evidence-only;
- anything you could not place;
- anything that looked wrong in the legacy material. Report it; do not fix the mathematics.
