# Collatz: an open, AI-assisted research notebook

A public, verifiable record of an attack on the **Collatz conjecture**, made by AI agents under human direction and open to anyone's contributions. Every claim is a small file stating exactly what it covers, how strongly it is established, and what it rests on. Failed approaches are recorded as carefully as successes.

> **The Collatz conjecture is open. Nothing here proves it.**

## The problem

Take a positive integer. If it is even, halve it; if it is odd, triple it and add one. The conjecture says that every starting value eventually reaches 1. A counterexample would be either an orbit that grows forever or a **nontrivial cycle**.

## How the repository is organised

Knowledge is stored as a graph of small **nodes**, each one Markdown file:
- **results**: claims with proofs or exact computations;
- **attempts**: approaches that failed, and why;
- **questions**: open targets;
- **sources**: external works we rely on.

Each node declares its status (`proposed` → `written` → `reviewed` → `formal`) and the nodes it depends on.

| Read | Time | For |
|---|---|---|
| This page | 2 min | What the project is |
| [`MAP.md`](MAP.md) | 5 min | Every node on one page: open questions first, then each area's results with their strength |
| `areas/<area>/OVERVIEW.md` | 10 min | The story of one area: [`cycles`](areas/cycles/OVERVIEW.md), [`convergence`](areas/convergence/OVERVIEW.md), [`invariants`](areas/invariants/OVERVIEW.md) |
| A node | as needed | One claim and its full argument |

| Path | Contents |
|---|---|
| [`areas/`](areas/) | The nodes, by topic |
| [`sources/`](sources/) | External papers, computations and libraries, as nodes |
| [`lean/`](lean/) | Machine-checked proofs (Lean 4 + Mathlib) |
| [`papers/`](papers/) | Typeset expositions of groups of nodes |
| [`conventions/`](conventions/) | The node schema, notation, credit policy and templates |
| [`tools/`](tools/) | The checker, the map generator and the certificate runner |
| [`archive/`](archive/) | Frozen history that does not fit the graph; how the project came to be is in [`archive/HISTORY.md`](archive/HISTORY.md) |

## Verify

The tooling uses only Python 3.10+ and its standard library.

```sh
python3 tools/check.py                        # schema, references, links, Lean hygiene, MAP up to date
python3 tools/run_certificates.py --node <id> # re-run the finite checks behind one node
```

Lean proofs build with the toolchain pinned in [`lean/`](lean/): `cd lean && lake exe cache get && lake build LeanLane` builds the library of newer results; the legacy files compile one at a time (see [`lean/README.md`](lean/README.md)).

## Contribute

Anyone may contribute, with or without an AI agent. Point your agent at [`AGENTS.md`](AGENTS.md): it holds every rule. [`CONTRIBUTING.md`](CONTRIBUTING.md) has the step-by-step version for humans. Good first contributions:
- an independent review of a `written` node;
- an attack on an open question in MAP.md;
- a formalisation of a reviewed result.

A rigorous negative result ("this method cannot work, because …") is a real contribution.

**Credit.** Every contribution is a small attributed node, and credit is computed from the graph: a node earns a share of everything built on it, and reviews and documented dead ends count. The "Contributors" section of MAP.md is generated from it. Publishing your own decisive result under your own name stays yours to do. The rules are in [`conventions/CREDIT.md`](conventions/CREDIT.md).

## License

[MIT](LICENSE). Contributions are accepted under the same license.
