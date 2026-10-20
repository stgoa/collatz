# Node schema

Everything this repository knows is stored as **nodes**. A node is one Markdown file with a YAML frontmatter block. [`tools/check.py`](../tools/check.py) enforces this page, and [`tools/schema.py`](../tools/schema.py) holds the same rules as data. If this page and the code disagree, the code is what CI runs; fix whichever is wrong.

## 1. Kinds

| Kind | What it records | Folder |
|---|---|---|
| `result` | A claim with an argument: a theorem, a lemma, a reduction, an exact computation, a counterexample. | `areas/<area>/results/` |
| `attempt` | An approach that failed or stalled, and why. Negative results ("method X cannot work, because …") go here when they are lessons rather than theorems; a *proved* obstruction is a `result`. | `areas/<area>/attempts/` |
| `question` | An open target: a conjecture, a missing lemma, a hypothesis that other nodes assume. Open questions form the frontier. | `areas/<area>/questions/` |
| `source` | Something external that nodes rely on: a paper, a published computation, an outside Lean library. | `sources/` |

A node is either `<id>.md`, or `<id>/README.md` when it has attached files: scripts, data, receipts, figures. Attached files live in the node's folder and nowhere else. Node folders do not nest.

## 2. IDs

- The id is a **descriptive slug**: lowercase words joined by hyphens, at most 64 characters. Examples: `rotation-distance-at-least-4`, `height-bound-denjoy-koksma`.
- The id equals the file name (without `.md`) or the folder name. It never changes once merged; if a better name appears, keep the id.
- Ids are unique across the whole repository, across all areas and kinds.
- Before choosing an id, search [`MAP.md`](../MAP.md) for the concept. If a node already covers it, extend that node or add a dependent one; do not duplicate.
- **Legacy IDs** such as `C011`, `S13`, `R71` and `V004` go in `aliases`. Aliases are unique too, and MAP.md resolves them. References inside frontmatter always use the id, never an alias.

## 3. Fields

| Field | Kinds | Required | Meaning |
|---|---|---|---|
| `id` | all | yes | §2 |
| `kind` | all | yes | `result`, `attempt`, `question` or `source`; must match the folder |
| `title` | all | yes | One line, plain words |
| `status` | all | yes | §4 |
| `claim` | result, attempt, question | yes | The exact statement, with every quantifier, parameter and scope (map, clock, class of cycles). For an attempt: what was tried and the verdict. For a question: the target. |
| `citation` | source | yes | Full bibliographic citation |
| `url` | source | no | A stable link (DOI, arXiv, repository at a commit) |
| `created` | all | yes | `YYYY-MM-DD` of the first commit of this node or of its legacy original |
| `authors` | result, attempt | yes | List of contributors. Each is a name identifying the person or the agent session, then details in parentheses: `Santiago Armstrong`, `Claude side lane (Opus 5.5)`, `ChatGPT main lane (Codex)`. The part before the parentheses is what CI compares with reviewers (§4). |
| `depends_on` | all | no | Results this argument uses. Ids of `result` nodes only. |
| `assumes` | all | no | Inputs taken without proof here: `source` nodes, open `question` nodes used as hypotheses, or results. **A node with `assumes` is conditional.** |
| `lean` | all | no | Fully qualified Lean declarations that formalise the claim, e.g. `CycleSpectrum.rho_ge_four` |
| `certificates` | all | no | Scripts in the node's folder that verify a finite step. They must exit 0 when run from the repository root; CI re-runs them when the folder changes. |
| `evidence` | all | no | Other supporting artefacts, as free text or paths: exploration scripts, data, historical receipts. **Never run by CI.** |
| `reviewed_by` | all | no | Block list of reviews. Each item has `by` and `date`, and optionally `link` (to a review file or PR) and `scope` (what was checked). |
| `supersedes` | all | no | Ids of nodes this one replaces. The old node stays, with its status updated. |
| `aliases` | all | no | Legacy IDs (§2) |
| `answered_by` | question | for `answered` | The result or attempt that settles the question |
| `refuted_by` | all | for `refuted` | A node id or a link to the counterexample |
| `withdrawn_reason` | all | for `withdrawn` | One sentence |
| `tags` | all | no | Free keywords for search |

No other fields are allowed. Propose new fields by pull request against this page and `tools/schema.py`.

## 4. Status

**Results and attempts** climb a ladder:

| Status | Meaning | Enforced requirement |
|---|---|---|
| `proposed` | Statement and idea; the argument is incomplete, heuristic or only numerical. | — |
| `written` | Complete argument written out in the node (or its certificates), not yet independently checked. | — |
| `reviewed` | Someone other than the authors checked the complete argument and recorded it. | `reviewed_by` has an entry whose name (the part before any parentheses, case-insensitive) differs from every author's |
| `formal` | Machine-checked in Lean in this repository. | `lean` names existing declarations; a `## Lean` section says how the Lean statement matches the claim; CI builds `lean/` |
| `refuted` | Shown false. Kept forever. | `refuted_by` |
| `withdrawn` | Retracted by the authors, e.g. found redundant or ill-posed. Kept forever. | `withdrawn_reason` |

**Questions:** `open`, `answered` (needs `answered_by`), `dropped` (explain in the body).
**Sources:** `cited` (used as published), `replayed` (re-checked here: rebuilt, re-run or re-derived; the body says how).

Rules:
- **Conditional is not a status.** A result whose chain reaches a source or an open question is conditional on it. MAP.md lists those inputs in its "Rests on" column.
- **Chain strength.** MAP.md shows, beside each result's own status, the weakest status along its dependency chain. A result is only as strong as what it uses.
- **Numerical evidence never makes a general claim `written`.** A computation proves exactly its finite statement. Anything beyond that statement is `proposed` and says "heuristic" in the claim.
- **Never delete a merged node.** Wrong claims become `refuted` or `withdrawn`, with the reason.

## 5. Frontmatter syntax

The parser ([`tools/nodes.py`](../tools/nodes.py)) accepts a small YAML subset, so that every reader agrees:

```yaml
---
id: example-node                 # key: value
title: "A title: quoted if it contains a colon"
aliases: [C011, S13]             # inline list
claim: >                         # folded block: lines indented by two spaces
  For every primitive cycle of 3x+1 with period m ≥ 2, ...
authors:                         # block list
  - Claude (Opus 5.5)
reviewed_by:                     # block list of flat mappings
  - by: Claude Fable (Lean lane)
    date: 2026-10-19
    link: https://github.com/stgoa/collatz/pull/7
---
```

Not supported: anchors, inline mappings `{…}`, nested lists, multi-document files. Indent with two spaces.

## 6. Body

After the frontmatter comes the Markdown body. Start with a `#` heading equal to the `title`. Use these sections, in this order, and skip those that do not apply:

| Kind | Sections |
|---|---|
| result | `## Statement` · `## Proof` · `## Certificates` · `## Lean` · `## Remarks` · `## History` |
| attempt | `## Idea` · `## What happened` · `## Why it fails` · `## What survives` · `## History` |
| question | `## Question` · `## Why it matters` · `## Known progress` · `## Suggested attacks` |
| source | `## Citation` · `## What we use` · `## How it is checked` |

Templates: [`conventions/templates/`](templates/). Notation: [`conventions/NOTATION.md`](NOTATION.md).

`## History` records where the node came from: legacy IDs and paths, and the commit where they last stood (e.g. "migrated from `experiments/cycle_spectrum/S13/` at `be73a66`"). It also records corrections, each dated.

## 7. Scripts

Every `.py` file attached to a node is one of two kinds:
- **Certificate**: listed under `certificates`. It checks a finite step of the argument. It is deterministic, uses the standard library only (or the README of the node says why not), runs from the repository root, locates its files relative to `Path(__file__)`, and exits non-zero on failure. CI runs it when its node's folder changes.
- **Exploration**: anything else. It found or illustrated something. It is listed under `evidence`, kept for the record, and never run by CI.

A receipt (a `.json`, `.csv` or `.txt` output) is written by its script, never by hand.
