# Contributing

Anyone can contribute: a human, an AI agent, or a human working with one. Every contribution arrives as a pull request (PR). Maintainers review each PR before it is merged into `main`.

Agents should read [`AGENTS.md`](AGENTS.md) first; it holds the binding rules. This page explains the workflow and gives step-by-step playbooks for each kind of contribution.

## What is welcome

| Kind | Example |
|---|---|
| **A new result** | A proof, a counterexample, a computation with receipts, or a sharper bound on an open target in [`docs/FRONTIER.md`](docs/FRONTIER.md). |
| **A review** | An independent check of a claim already here: re-derive the proof, re-run the scripts, write a new checker, or find a gap. |
| **A formalisation** | A Lean proof of a written result, under `lean/`. |
| **A correction** | A demonstrated error in an existing claim, with a counterexample or a gap in its argument. |
| **Literature** | Prior work that anticipates, contradicts or strengthens a result here. |
| **Tooling or docs** | Better checks, CI, explanations. |

Negative results are valuable. A well-scoped "this method cannot work, and here is why" is a contribution. Many results here are exactly that.

## The workflow

1. **Pick a target.** Use [`docs/FRONTIER.md`](docs/FRONTIER.md), or open an issue with the *Research proposal* template.
2. **Fork the repository, then branch** off `main` as `<handle>/<short-slug>`.
3. **Add your files** where [`AGENTS.md`](AGENTS.md) §2 says. A new result is one folder: `experiments/<line>/<YYYY-MM-DD>-<slug>/`. It holds a `README.md` with the status header, plus any scripts and their receipts.
4. **Update the indexes:**
   - the line's `experiments/<line>/README.md`;
   - [`docs/RESULTS.md`](docs/RESULTS.md);
   - [`docs/STATUS.md`](docs/STATUS.md) and [`docs/FRONTIER.md`](docs/FRONTIER.md), only if your result changes them.
5. **Run the checks:**

   ```sh
   python3 scripts/check_links.py
   python3 scripts/run_checks.py --line <line>
   python3 path/to/your/check_<topic>.py
   ```

6. **Open the PR** against `main`. Fill in the template, including the AI-disclosure section.
7. **Respond to review.** Reviewers may ask for sharper scope, more controls, or an independent check.

## Playbooks

### A new result

1. Write the claim first, as one or two sentences with every quantifier and parameter. Choose the honest status: `written`, `conditional`, `evidence` or `heuristic`.
2. Write the argument in the folder's `README.md`. Long proofs may be split into extra `.md` files in the same folder.
3. If the claim involves computation, add `check_<topic>.py`:
   - it writes `check_<topic>.json` with `--write-receipt`;
   - it compares against that receipt by default.

   Commit both files.
4. Test the claim against the `3x+d` controls ([`docs/CONVENTIONS.md`](docs/CONVENTIONS.md) §3). A statement about integer cycles of `3x+1` must not, by its argument, also exclude the actual cycles of `3x+5`, `3x+7`, `3x+13` or `3x+61`.
5. List every external input you rely on (published theorems, computational bounds, replayed Lean results). If any are used, the status is `conditional (inputs: …)`.
6. Search the literature and say what you found. If unsure, write "novelty undetermined".

### A review

1. Create `reviews/<topic>/`. It holds a `README.md` that states:
   - what was reviewed: path and commit;
   - what was checked;
   - the verdict, one of `confirmed`, `confirmed with corrections`, `gap found` or `refuted`.
2. Prefer *independent* checks: new code written from the statement, not a re-run of the author's script.
3. If the reviewed result's status should change (e.g. `written` → `proved`), say so in the PR. Update its index rows in the same PR.

### A formalisation (Lean)

1. Follow [`lean/README.md`](lean/README.md) for the toolchain and build recipe.
2. Add the statement and proof, then record the build output and `#print axioms` in `lean/receipts/`.
3. Add a row to `lean/STATE.md` saying exactly how the Lean statement matches the prose claim, including any extra hypotheses.
4. A reviewer checks the receipts and the statement match before the result is marked `formal`.

### A correction

1. Show the error: a counterexample (with a script, if computational) or the precise gap.
2. At the top of the affected file, add a dated note: `> **Correction (YYYY-MM-DD):** … — see <link>`. Change the status label, and update the index rows.
3. Never delete the original text. The record of what was claimed is part of the research.

## Disclosure of AI use

This project is an experiment in AI-assisted research, so disclosure is required, not optional. In the PR template, state:
- which agents or models produced the work;
- how autonomous they were (fully autonomous, human-directed, or human-written);
- what the human checked.

## Review standards

Reviewers ask:
- Is the claim scoped exactly?
- Does the evidence match the status label?
- Do the scripts run and reproduce their receipts?
- Are the controls respected?
- Are external inputs named?
- Is novelty claimed only after a literature check?

## License

By contributing you agree that your contribution is licensed under the [MIT License](LICENSE).

## Conduct

Be precise and be kind. Criticise claims, not people. A refuted claim is a normal outcome of research, not a failure of its author.
