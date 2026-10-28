# Rules for agents and humans

This repository is an open, AI-assisted research notebook on the Collatz conjecture. Anyone, and anyone's AI agent, may contribute by pull request. These rules apply to every contributor, whatever the model or tool. They are short on purpose: read all of them before you change anything.

## 1. The model: a knowledge graph of small nodes

Everything the project knows is a **node**: one Markdown file with YAML frontmatter. There are four kinds:

| Kind | Records | Lives in |
|---|---|---|
| `result` | A claim with its argument (proof, exact computation, counterexample) | `areas/<area>/results/` |
| `attempt` | An approach that failed or stalled, and exactly why | `areas/<area>/attempts/` |
| `question` | An open target or a hypothesis other nodes assume | `areas/<area>/questions/` |
| `source` | An external paper, computation or library we rely on | `sources/` |

Nodes reference each other by id in their frontmatter (`depends_on`, `assumes`, `answered_by`, …). [`MAP.md`](MAP.md) is generated from those references. **The schema is binding: [`conventions/SCHEMA.md`](conventions/SCHEMA.md).** CI rejects any node that does not follow it.

## 2. Read before you write

Read in this order. Ten to fifteen minutes is enough:

1. [`README.md`](README.md): what the project is.
2. [`MAP.md`](MAP.md): every node on one page, the open questions first.
3. `areas/<area>/OVERVIEW.md` for the area you will touch: the narrative, the main lines, what was tried.
4. [`conventions/SCHEMA.md`](conventions/SCHEMA.md) and [`conventions/NOTATION.md`](conventions/NOTATION.md).
5. The nodes you will build on, and every node they depend on.

**Do not duplicate.** Before writing a node:
- search MAP.md (ids, titles, legacy IDs) and the `attempts/` folders for the idea;
- search open pull requests and issues.

If the idea is covered, extend or review the existing node instead. If it was tried and failed, start from that attempt's "What survives" section.

## 3. Where things go

| Content | Location |
|---|---|
| A node | `areas/<area>/<kind>s/<id>.md`, or `<id>/README.md` when it has attached files |
| Scripts, data, receipts, figures belonging to a node | Inside that node's folder, nowhere else |
| A review of a node | `REVIEW-<YYYY-MM-DD>-<reviewer-slug>.md` in the node's folder, and an entry in its `reviewed_by` |
| Narrative of an area: how its nodes fit, the main lines, the dead ends | `areas/<area>/OVERVIEW.md` (hand-written, short; links to nodes) |
| External works | `sources/<id>.md` (a node of kind `source`) |
| Lean proofs | `lean/`, one Lake project; one module per formalised result where practical ([`lean/README.md`](lean/README.md)) |
| Typeset expositions (`.tex`) | `papers/<slug>/<slug>.tex`; a paper cites nodes and adds no new claims |
| Conventions, schema, templates | `conventions/` |
| Repository tooling | `tools/` |
| Frozen history | `archive/`, never edited |

- **No other places.** The root holds only `README.md`, `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `LICENSE`, `MAP.md` and the folders above.
- **No running logs, feeds, status pages or hand-written indexes.** Progress is recorded by the nodes themselves (status, `created`, `reviewed_by`) and by merged pull requests. MAP.md is regenerated from them. A file that summarises other files goes stale; the generator does not.
- **One idea, one node.** A long report that proves five lemmas becomes five results, plus whatever ties them together.

## 4. Naming

- **Node ids** are descriptive kebab-case slugs: `rotation-distance-at-least-4`, not `S07` and not `new-result-2`. The file or folder name equals the id. Ids never change once merged.
- **Legacy series numbers** (`C011`, `S13`, `R71`, `V004`, …) are kept as `aliases`; MAP.md resolves them.
- **Areas** are broad topics, named by one lowercase word: `cycles`, `convergence`, `invariants`. Open a new area only by a pull request that adds its `OVERVIEW.md` and explains why the existing ones do not fit.
- **Files inside a node folder:** `README.md` (the node), `check_<topic>.py` (certificates), `explore_<topic>.py` (exploration), receipts named after their script (`check_<topic>.json`), `REVIEW-<date>-<slug>.md`.
- **Branches:** `<handle>/<short-slug>`.

## 5. Claim discipline

These are the rules reviewers enforce. Breaking one is the most common reason a PR is refused.

- **Never claim to prove the Collatz conjecture**, or to exclude all cycles, unless the full chain is `formal`.
- **Scope every claim.** State:
  - the map (`3x+1` or `3x+d`);
  - the clock (odd-only or shortcut; never mix them);
  - the class of cycles, words or orbits;
  - every bound and parameter.
- **Test cycle arguments against the controls.** An argument that would also exclude the actual cycles of `3x+5`, `3x+7`, `3x+13` or `3x+61` is wrong ([`conventions/NOTATION.md`](conventions/NOTATION.md) §3).
- **Compute before you quote.** Every number in a claim comes from a proof in the node or from a committed script whose receipt prints it.
- **Label heuristics.** A heuristic or numerical extrapolation is at most `proposed`, and its claim says "heuristic". Never derive a probability from moment bounds.
- **Name every external input** as a `source` node under `assumes`. Published bounds, outside Lean libraries and computations not re-run here all count. MAP.md then shows the result as resting on them.
- **Keep correctness, novelty and usefulness apart.** Check `sources/` and the literature before calling anything new; otherwise write "novelty undetermined".
- **Never delete or silently rewrite a merged claim.**
  - To fix it: add a dated note under `## History` and change `status` if needed.
  - A wrong claim becomes `refuted` (with `refuted_by`) or `withdrawn` (with `withdrawn_reason`).
  - Its dependents must be re-checked; the PR bot lists them.

## 6. File types

- **Markdown:** GitHub-flavoured, one `#` title per file. Use relative links to repository files only; never absolute URLs into this repository or local paths. Math must stay readable as plain text.
- **Python:** ≥ 3.10, standard library only unless the node explains why not. It runs from the repository root, finds its files relative to `Path(__file__)`, and is deterministic (fixed seeds, no wall-clock data in receipts). A certificate exits non-zero on failure and does not rely on `assert` (checks must also hold under `python3 -O`).
- **Certificates versus exploration** ([`conventions/SCHEMA.md`](conventions/SCHEMA.md) §7):
  - a *certificate* proves a finite step and is re-run by CI whenever its node folder changes;
  - an *exploration* script found or illustrated something, and is never run by CI.
  - The Markdown argument is the result; scripts are its side-car.
- **Receipts** (`.json`, `.csv`, `.txt`): written by their script, never by hand. Files over 1 MB need a reason in the PR.
- **Lean:** only in `lean/`.
  - Only the axioms `propext`, `Classical.choice` and `Quot.sound` are allowed.
  - No `sorry`, `admit`, `native_decide`, new `axiom`s, `unsafe`, `implemented_by`, `extern` or `opaque`.
  - A node is `formal` only when its `## Lean` section says how the Lean statement matches the claim.
- **LaTeX:** only in `papers/<slug>/`, sources only, never build output.
- **No other binaries** (notebooks, PDFs, images, archives) unless the node explains why.

## 7. Workflow

1. **Branch** from up-to-date `main` as `<handle>/<short-slug>`. Never push to `main` or rewrite shared history.
2. **Claim your target early.** Open a draft pull request, or comment on the question's issue, so others do not duplicate the work.
3. **Keep it small:** one result, one attempt, one review, one formalisation, or one fix per pull request. Don't reformat unrelated files.
4. **Before opening the PR, run:**

   ```sh
   python3 tools/build_map.py                         # regenerate MAP.md
   python3 tools/check.py                             # schema, references, links, Lean hygiene
   python3 tools/run_certificates.py --changed main   # certificates of the nodes you touched
   ```

5. **Open the PR** with the template. Fill in "Related nodes" and disclose AI use: which agent or model, and how autonomously it worked. In `authors` and `reviewed_by`, name an agent together with the person who directed it, e.g. `Claude review lane (Opus 5.5; directed by Jane Doe)`: credit is computed from these entries ([`conventions/CREDIT.md`](conventions/CREDIT.md)).
6. **Review.**
   - New results enter as `proposed` or `written`.
   - `reviewed` needs a `reviewed_by` entry by someone other than the authors. Agents count as reviewers if they are independent of the authoring session. Say which model.
   - `formal` needs the Lean build to pass in CI.
   - Do not merge your own pull request.

## 8. Hygiene

- No secrets, tokens, personal data or absolute local paths in any file.
- No caches or build output (`__pycache__`, `.lake/`, PDFs); `.gitignore` covers the common ones.
- Never fabricate citations, results, receipts or reviews. If you could not check something, say so.
- When unsure whether something belongs here, open an issue first.
