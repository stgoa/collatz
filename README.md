# Collatz: an open, AI-assisted research notebook

This repository is a public, verifiable record of an attack on the **Collatz conjecture**, made by AI agents (ChatGPT/Codex and Claude) under human direction. It contains proofs, exact computations with committed receipts, machine-checked Lean proofs, and failed approaches documented as carefully as successes. It is open: **anyone, and anyone's AI agent, can contribute findings by pull request.**

> **The Collatz conjecture is open. Nothing here proves it.** Each result states exactly what it covers, and at which level of evidence.

## The problem

Take a positive integer. If it is even, halve it; if it is odd, triple it and add one. The conjecture says that every starting value eventually reaches 1. A counterexample would be either an orbit that grows forever or a **nontrivial cycle**.

Most current work here is on the cycle half: **showing that `3x+1` has no cycle other than 1 → 4 → 2 → 1.** Each candidate cycle is encoded by its word of halving counts, and the question becomes when that word's rational cycle has denominator 1 ([`docs/CONVENTIONS.md`](docs/CONVENTIONS.md)).

## Where things stand

A selection; the full picture is in [`docs/STATUS.md`](docs/STATUS.md).

- **Machine-checked:** every nontrivial cycle has a state above twice its minimum.
- **Machine-checked, conditional on a replayed external Lean result and published computational bounds:** a cycle's word differs from each of its own rotations in at least 4 places. This is the step `ρ ≥ 4` towards the target `ρ → ∞`.
- **Machine-checked:** a Denjoy–Koksma bound on the height of a cycle, and a "rise lemma". With the same external input, the rise lemma shows that short rotations of a cycle word differ from it in about `log m` places.
- **Written:** the remaining case, rotations by a positive fraction of the period, reduces to bounding the largest single halving count of a cycle by `o(m)`.
- **Finished programmes:**
  - a reduction of convergence to finite "current" certificates (frozen at R94);
  - a classification of finite-state invariants;
  - calibrations and barriers for known proof routes.

## Layout

| Path | Contents |
|---|---|
| [`docs/`](docs/) | [Status](docs/STATUS.md) · [Frontier: open problems](docs/FRONTIER.md) · [Results index](docs/RESULTS.md) · [Conventions](docs/CONVENTIONS.md) · [Literature](docs/LITERATURE.md) · [History](docs/HISTORY.md) |
| [`experiments/`](experiments/) | One folder per research line, each with a README giving its goal, status and an index. The active line is [`cycle_spectrum`](experiments/cycle_spectrum/). |
| [`collatz_research_20261017/`](collatz_research_20261017/) | The original 2026-10-17 upload and the first rounds R1–R4 (frozen). It stays at the root because frozen scripts load files from it by path. |
| [`lean/`](lean/) | The formal (Lean 4 + Mathlib) development and its build receipts |
| [`reviews/`](reviews/) | Independent checks of claims made elsewhere in the repository |
| [`papers/`](papers/) | Typeset (`.tex`) write-ups |
| [`archive/`](archive/) | Frozen history: earlier rules, maps, logs and the agents' feed |
| [`scripts/`](scripts/) | Verification tooling |

## Verify

Everything computational can be re-run with Python 3.10+ and the standard library only.

```sh
python3 scripts/check_links.py                       # every internal link resolves
python3 scripts/run_checks.py --line cycle_spectrum  # re-run the active line's checkers (~6 min)
python3 scripts/verify_all.py                        # the frozen programmes' gate (~12 min)
```

Lean proofs are built with the pinned toolchain described in [`lean/README.md`](lean/README.md). Every theorem's axioms are recorded in [`lean/receipts/`](lean/receipts/).

## Contribute

1. Read [`AGENTS.md`](AGENTS.md) (the rules, for humans and agents alike) and [`CONTRIBUTING.md`](CONTRIBUTING.md) (the playbooks).
2. Pick a target in [`docs/FRONTIER.md`](docs/FRONTIER.md), or review an existing result.
3. Open a pull request, with AI use disclosed.

A rigorous negative result ("this method cannot work, because …") is a real contribution.

## License

[MIT](LICENSE). Contributions are accepted under the same license.
