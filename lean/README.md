# Lean: the formal layer

This folder holds machine-checked (Lean 4 + Mathlib) versions of results stated in prose in the result nodes under `areas/`. A declaration here counts only with its receipts: a build receipt and a `#print axioms` receipt showing only the standard axioms `propext`, `Classical.choice` and `Quot.sound`.

**Current shape, honestly stated.** This is one Lake project in name only: the `.lean` files are standalone and are compiled **one at a time** with `lake env lean <File>.lean`; they are not Lake modules of a library, and nothing imports anything else here. The goal in [`AGENTS.md`](../AGENTS.md) is one module per formalised result. Getting there means splitting `CycleSpectrum.lean` (about 14,000 lines) into modules and re-running every receipt, which needs a working toolchain. That is future work.

Each unit's statement match now lives in the `## Lean` section of its result node. The Lean lane's legacy unit table ([`archive/lean-lane/STATE.md`](../archive/lean-lane/STATE.md): for each unit, its prose source, the exact statement match, extra hypotheses, status, axioms and receipts, plus the queue of units never done) and its journal ([`archive/lean-lane/LOG.md`](../archive/lean-lane/LOG.md)) are archived, frozen as the lane left them on 2026-10-19 (legacy paths `lean/STATE.md` and `lean/LOG.md`).

## Files

| File | Imports | Contents |
|---|---|---|
| `CycleSpectrum.lean` (14,285 lines) | Mathlib | The cycle-spectrum units: C001–C013 (including the narrow-cycle exclusion `H > 2L`), R71 (the mechanical exclusion), S1–S13 (`ρ ≥ 4` given EXT-1, the Denjoy–Koksma bound, the rise lemma). Namespace `LeanLane.Cyc` and sub-namespaces. |
| `PeriodicRigidity.lean` | Mathlib | Periodic invariants of `3x+1` are constant; the `3x+5` control. `LeanLane.*`. |
| `GeneralPeriodic.lean` | Mathlib | The periodic-rigidity generalisation. `LeanLane.GenPer`. |
| `OddEventuallyPeriodic.lean` | Mathlib | V004-i: odd-eventually-periodic rigidity. `LeanLane.OddEP`. |
| `KernelClosure.lean` | Mathlib | V004-ii: ternary and binary closure of the positive-offset kernel. `LeanLane.Kernel`. |
| `V004_Final.lean` | none (a part) | V004-iii assembly proper; not compiled alone, concatenated into `V004_Assembly.lean`. |
| `V004_Assembly.lean` | Mathlib | V004-iii: binary-automatic invariant colourings are constant, with Cobham's theorem as a named hypothesis. **Generated** by `build_assembly.sh`; edit the parts, not this file. `LeanLane.V004`. |
| `ScalarInterface.lean` | Mathlib | V005-a: the scalar interface. `LeanLane.Scalar`. |
| `QuadraticSeparation.lean` | Mathlib | V006-a: quadratic separation. `LeanLane.Quad`. |
| `ReverseClosure_Final.lean` | none (a part) | V007-a assembly proper; concatenated into `ReverseClosure_Assembly.lean`. |
| `ReverseClosure_Assembly.lean` | Mathlib | V007-a: reverse closure. **Generated** by `build_reverse_assembly.sh`. `LeanLane.RevClos`. |
| `Dichotomy.lean` | `Solution.Basic` | Queue item 3: the dichotomy corollary over the audited positive-density theorem (prose: [`nonabsorbing-set-linear-lower-density`](../areas/convergence/results/nonabsorbing-set-linear-lower-density/README.md)). `LeanLane.Dichotomy`. |
| `PairObligation.lean` | `Solution.Basic` | Queue item 4 (partial): the W5 pair obligation and the `u ↔ 18u+5` reformulation. `LeanLane.Pair`. |
| `build_assembly.sh`, `build_reverse_assembly.sh` | — | Regenerate the two assembly files from their parts. |
| `lakefile.toml`, `lean-toolchain` | — | Pin the toolchain and Mathlib (below). |

**Mathlib only:** `CycleSpectrum`, `PeriodicRigidity`, `GeneralPeriodic`, `OddEventuallyPeriodic`, `KernelClosure`, `V004_Assembly`, `ScalarInterface`, `QuadraticSeparation`, `ReverseClosure_Assembly`.

**Other dependencies:** `Dichotomy` and `PairObligation` import `Solution.Basic` from the external, AI-generated `AxiomMath/CollatzPositiveDensity` library at commit `3a38bfbb70379e051b51155def1423846fab3a90` (see `audit/`). They compile only inside a checkout of that project, which is not a dependency of `lakefile.toml`, and the theorems they use are therefore an external input.

**External input EXT-1** (`Collatz.gap_all` from `mmusson/collatz`) was replayed under its own toolchain (`leanprover/lean4:v4.34.0-rc2`). It is not part of this development: see [`receipts/mmusson_gap_all.txt`](receipts/mmusson_gap_all.txt). Theorems that use it take it as an explicit hypothesis.

## Build

Toolchain `leanprover/lean4:v4.35.0-rc2` ([`lean-toolchain`](lean-toolchain)); Mathlib pinned at `065356127b1dc0016f66b7283ce0ce2c4055aa55` in [`lakefile.toml`](lakefile.toml).

```sh
# install elan (https://github.com/leanprover/elan) once, then, from the repository root:
cd lean
lake exe cache get                      # fetch prebuilt Mathlib for the pinned commit
sh build_reverse_assembly.sh            # regenerates V004_Assembly.lean and ReverseClosure_Assembly.lean
lake env lean CycleSpectrum.lean        # compile one file; repeat for each Mathlib-only file
```

Regenerating the assemblies must leave them byte-identical to the committed ones; otherwise the receipts no longer match. For `Dichotomy.lean` and `PairObligation.lean`, copy the file into a checkout of `AxiomMath/CollatzPositiveDensity` at the pinned commit, run `lake build Solution` there, then `lake env lean <File>.lean`.

[`../.github/workflows/lean.yml`](../.github/workflows/lean.yml) runs the Mathlib-only compile on pull requests that touch `lean/`.

## Receipts

The committed receipts were produced by the Lean lane (`Claude Lean lane (Fable)`) in a Linux container (`leanaudit`, aarch64) with the same toolchain and Mathlib: each file was copied into a Mathlib-equipped project and compiled with `lake env lean`. For each compiled file, [`receipts/`](receipts/) holds:
- `<File>.build.txt`: the build exit status; for newer receipts also the source sha256, toolchain and build time;
- `<File>.axioms.txt`: one `#print axioms` line per declaration, plus the printed statements; newer ones are headed by the source sha256;
- `<File>.sha256.txt`: the source hash;
- `toolchain.txt`: the exact `lean --version` and Mathlib revision;
- `mmusson_gap_all.txt`: the EXT-1 replay above.

Receipts written before the 2026-10-19 restructure name the old path `experiments/lean_lane/…`. Their hashes still match the files here.

`python3 tools/check_lean_receipts.py` checks, without building, that every receipt hash matches the current source and that every `#print axioms` line names only the three standard axioms. `python3 tools/check.py` scans every `lean/**/*.lean` (comments stripped) for `sorry`, `admit`, `axiom` declarations, `native_decide`, `implemented_by`, `@[extern`, `unsafe` and `opaque`.

## `audit/`

[`audit/`](audit/README.md) is an independent build-and-axioms audit (by a separate Claude session, 2026-10-18) of the external `AxiomMath/CollatzPositiveDensity` development at commit `3a38bfb`: a positive-density theorem for Collatz trajectories, which its authors say was produced and formalised autonomously by an AI system (AxiomProver). Verdict: from-source build, axioms, statement match against the human-written challenge, kernel-fix containment and independent kernel replay all **PASS**, with recorded caveats: the comparator ran without its own sandbox (the container was the sandbox), and a whole-library `lake check --paranoid` had two unexplained "rejected" reports and one out-of-memory kill. It establishes the four Lean statements as theorems of Lean + Mathlib under the standard axioms; it says nothing about the paper's prose. The README's opening "in progress" line predates its results section. `AuditChallenge.lean` and `AuditSolution.lean` are the audit's print scripts; they import the external project and are not part of this build.

[`audit/phase6/StatementAudit.lean`](audit/phase6/StatementAudit.lean) belongs to an earlier, separate replay of the same external development by the Phase 6 main lane (macOS, network-denied sandbox, 2026-10-18): the four challenge statements and their definitions copied unchanged into the namespace `LauStatementAudit`, each proved by the corresponding `Solution.Basic` theorem, followed by eight `#print axioms` commands. It was generated by `generate_statement_audit.py` and compiled inside a checkout of the external project; it imports `Solution.Basic`, is not part of this build, and its receipts (all eight axiom reports: `propext`, `Classical.choice`, `Quot.sound`; fresh same-kernel replay) are in the node [`lau-density-formal-replay`](../areas/convergence/results/lau-density-formal-replay/README.md), not in `receipts/`. It moved here from `experiments/phase6/linear_density_audit/` at the B14 migration, byte-identical (SHA-256 `8215385e2b8b10c7507f6587ba1aa53fd7f6825f2cd020eee13307b8bba447e2`, pinned in that node's `formal_replay.json`).

## How a result node uses this

A result node names the declarations that formalise its claim in its `lean` frontmatter field, fully qualified (e.g. `LeanLane.Cyc.OddCycle.Vh_le_card_mul`), and its `## Lean` section states how the Lean statement matches the prose claim, including every extra hypothesis (such as EXT-1 or `CobhamStatement`). Status `formal` needs both, plus a passing build ([`conventions/SCHEMA.md`](../conventions/SCHEMA.md) §4).

## Contributing Lean

- Standard axioms only; no `sorry`, `admit`, `native_decide`, new `axiom`s, `unsafe`, `implemented_by`, `extern` or `opaque` ([`AGENTS.md`](../AGENTS.md) §6).
- Commit the receipts with the source.
- Keep `CycleSpectrum.lean` append-only, or split it into modules in a dedicated PR.
