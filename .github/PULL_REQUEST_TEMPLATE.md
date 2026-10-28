<!-- Read AGENTS.md first. Delete the comment lines when done. -->

## What this adds
<!-- One of: new result · attempt · question · source · review · formalisation · correction · tooling/docs.
     Two or three sentences. -->

## Related nodes
<!-- Required. The existing nodes this builds on, extends, overlaps with or contradicts, by id. Say how you
     checked that the contribution is not a duplicate (MAP.md, attempts/, open PRs). -->

## Claims
<!-- For each new or changed node: its id, status, and the scoped claim. For cycle arguments: which 3x+d
     controls you tested against and how the argument stays consistent with them. -->

## How to check it
<!-- Where the argument is. Commands to re-run certificates. Lean declarations, if any. -->

## AI disclosure
- Agents/models used: <!-- e.g. Claude Opus 5.5 via Claude Code; none -->
- Autonomy: <!-- fully autonomous / human-directed / human-written -->
- Directed by: <!-- the person accountable for the agents' work; also written as "directed by" in authors and reviewed_by (conventions/CREDIT.md §4) -->
- What a human checked: <!-- … -->

## Checklist
- [ ] `python3 tools/build_map.py && python3 tools/check.py` passes.
- [ ] Certificates of the touched nodes pass (`python3 tools/run_certificates.py --changed main`).
- [ ] Every number in a claim comes from a proof or a committed script; heuristics are labelled.
- [ ] External inputs are `source` nodes listed under `assumes`.
- [ ] No merged claim was deleted or silently rewritten.
