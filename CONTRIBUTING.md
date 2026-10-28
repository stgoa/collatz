# Contributing

All rules are in [`AGENTS.md`](AGENTS.md); they apply to humans and agents alike. This page is the step-by-step version.

## Add a result

1. Read [`MAP.md`](MAP.md) and the area's `OVERVIEW.md`. Make sure the result is not already there, and not already recorded as a failed attempt.
2. Copy [`conventions/templates/result.md`](conventions/templates/result.md) to `areas/<area>/results/<your-id>.md`. If you have scripts or data, use `areas/<area>/results/<your-id>/README.md` and put them in that folder.
3. Fill in the frontmatter:
   - give the scoped `claim`;
   - list in `depends_on` every result you use;
   - list in `assumes` every external input (as a `source` node, which you may need to add) and every open question you assume.
4. Write the argument. If a finite step is checked by a script, list it under `certificates` and make sure it exits 0.
5. If the result changes the story of the area, add a sentence and a link to the area's `OVERVIEW.md`.
6. Run `python3 tools/build_map.py && python3 tools/check.py`, then open a pull request.

## Record a failed approach

Copy [`conventions/templates/attempt.md`](conventions/templates/attempt.md) to `areas/<area>/attempts/<id>.md`. The most useful parts are **Why it fails** (exact, with the obstruction) and **What survives**.

## Pose a question

Copy [`conventions/templates/question.md`](conventions/templates/question.md) to `areas/<area>/questions/<id>.md`. A good question is precise enough that a reader knows when it is answered.

## Review a node

1. Check the argument line by line, re-run its certificates, and test it against the `3x+d` controls ([`conventions/NOTATION.md`](conventions/NOTATION.md) §3).
2. Write `REVIEW-<YYYY-MM-DD>-<your-slug>.md` in the node's folder. If the node is a single file, turn it into a folder first: `<id>.md` becomes `<id>/README.md`. Say what you checked, what you did not check, and your verdict.
3. Add a `reviewed_by` entry with `by`, `date`, `link` (to your review file) and `scope`. If the argument holds and you are independent of its authors, raise `status` to `reviewed`. If you found an error, say so in the review and do not raise the status; the authors or a later PR correct or refute the node.

## Formalise a result

Add the Lean code under [`lean/`](lean/) (see its README), list the declarations under the node's `lean` field, and write a `## Lean` section explaining how the Lean statement matches the claim. Set `status: formal` once CI builds it. Formalising is authorship: add yourself to the node's `authors` as `Your Name (Lean formalisation)` ([`conventions/CREDIT.md`](conventions/CREDIT.md) §4).

## Pull requests

- Use the template, and list the related nodes.
- Disclose AI use: which agents or models, and how autonomously they worked. In `authors` and `reviewed_by`, name an agent with the person who directed it: `Claude review lane (Opus 5.5; directed by Jane Doe)`.
- Credit is computed from the graph ([`conventions/CREDIT.md`](conventions/CREDIT.md)). Your share appears in the "Contributors" section of MAP.md after merge.
- CI runs `tools/check.py` on every PR. It also runs the certificates of the nodes you touched and builds Lean when `lean/` changes. A bot comment summarises how the PR changes the graph and which dependents to re-check.
- Do not merge your own pull request.
