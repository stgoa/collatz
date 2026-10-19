<!-- Read AGENTS.md and CONTRIBUTING.md first. Delete the comment lines when done. -->

## Type
<!-- one of: result · review · formalisation (Lean) · correction · literature · tooling/docs -->

## Summary
<!-- What does this PR add or change, in two or three sentences? -->

## Claims and status
<!-- For each claim: the exact statement, with all quantifiers and parameters, and its status label from
     AGENTS.md §4 (formal / proved / written / conditional (inputs: …) / evidence / heuristic / open /
     refuted / withdrawn). -->

## Evidence and how to reproduce
<!-- Proof location, scripts and receipts, Lean declarations. Give the exact commands to re-run. -->

## Dependencies and external inputs
<!-- Results in this repository you rely on, and any external input (docs/CONVENTIONS.md §5). -->

## Controls
<!-- How the argument stays consistent with the actual 3x+d cycles (docs/CONVENTIONS.md §3), and which
     controls you ran. -->

## Literature and novelty
<!-- What you searched, what you found. Write "novelty undetermined" if unsure. -->

## AI disclosure
- Agents/models used: <!-- e.g. Claude Opus 5.5 via Claude Code; GPT-…; none -->
- Autonomy: <!-- fully autonomous / human-directed / human-written -->
- What a human checked: <!-- … -->

## Checklist
- [ ] Files are placed as in AGENTS.md §2. New result folders are named `<YYYY-MM-DD>-<slug>`.
- [ ] Each new result `README.md` starts with the status header.
- [ ] The index rows are updated: the line `README.md` and `docs/RESULTS.md`; `docs/STATUS.md` and `docs/FRONTIER.md` if they are affected.
- [ ] `python3 scripts/check_links.py` passes.
- [ ] The relevant checks pass (`scripts/run_checks.py --line …`, your own `check_*.py`, and `scripts/verify_all.py` if frozen lines were touched).
- [ ] No frozen path was edited (AGENTS.md §6); receipts were produced by scripts.
- [ ] No secrets, absolute local paths or large binaries.
