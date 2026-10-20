# Pinned Lau replay: dependency and cache inspection

Status: **execution completed**. Source compilation, statement/axiom checks, and fresh
replay into the same Lean kernel passed. See [formal_replay.json](formal_replay.json).
The numbered sections retain the chronological configuration review and execution
requirements; their historical pending language is superseded by that receipt.
See [lau_scope.md](lau_scope.md) for the mathematical statement and source pin.

## Pins reviewed

- Lau: `3a38bfbb70379e051b51155def1423846fab3a90`.
- Lean: `leanprover/lean4:v4.35.0-rc2`.
- Mathlib: `065356127b1dc0016f66b7283ce0ce2c4055aa55`.
- ProofWidgets: `4c70ac059693669e5756e32a7a94b57ee1e99dc5`.
- Remaining dependencies: the eight inherited entries in Lau's pinned `lake-manifest.json`.

Sources were inspected in `/tmp/collatz_p6_lau_3a38bfbb7037/.lake/packages` after the batch
owner downloaded them. There was no duplicate dependency fetch.

## 1. The appropriate cache roots

**Do not use `cache get Solution.Basic` to request this dependency closure.** At this pin,
`Cache.Hashing.getFileImports` filters imports to a fixed list of Mathlib/upstream package
names. `CollatzPosDens` is absent. Starting at `Solution.Basic` therefore fails to follow
the local project's imports into Mathlib. Passing the Mathlib boundary imports directly
avoids that problem. See the pinned
[Hashing implementation](https://github.com/leanprover-community/mathlib4/blob/065356127b1dc0016f66b7283ce0ce2c4055aa55/Cache/Hashing.lean).

A static traversal of the downloaded sources, including `public`, `meta`, and `import all`
forms, reduces the 145 direct Mathlib boundary names to the 16 below. They are an
irredundant subset of those boundary roots with the same traversed source-import union.
That union contains 3349 dependency source modules: 3092 Mathlib and 257 other upstream
modules. Lean/Std/Init imports stop at the toolchain boundary. These remain static module
counts, not elaborated theorem-dependency counts.

The following is a **proposed command**, not an executed receipt. It belongs in the owner's
isolated source directory with the pinned toolchain selected:

```sh
lake exe cache --repo=leanprover-community/mathlib4 --cache-from=master,legacy get \
  Mathlib.Algebra.BigOperators.ModEq \
  Mathlib.Algebra.Order.Chebyshev \
  Mathlib.Algebra.Order.Field.GeomSum \
  Mathlib.Algebra.Order.Floor.Semifield \
  Mathlib.Analysis.Complex.ExponentialBounds \
  Mathlib.Analysis.Fourier.ZMod \
  Mathlib.Analysis.Real.Pi.Bounds \
  Mathlib.Analysis.SpecialFunctions.Log.Base \
  Mathlib.Analysis.SpecialFunctions.Log.Monotone \
  Mathlib.Analysis.SpecialFunctions.Trigonometric.Series \
  Mathlib.Data.Int.CardIntervalMod \
  Mathlib.Data.List.GetD \
  Mathlib.Data.Nat.Size \
  Mathlib.Data.Set.Finite.List \
  Mathlib.InformationTheory.Coding.PrefixFree \
  Mathlib.NumberTheory.Multiplicity
```

The root inventory and traversal counts are also recorded temporarily in
`/tmp/collatz_p6_lau_cache_roots.json` and `/tmp/collatz_p6_lau_cache_roots.txt`.
The cache hashes all Mathlib roots internally before filtering requested downloads;
restricting these arguments reduces downloads, not necessarily initial source scanning.
`get-` downloads without decompression; `get` downloads and decompresses.

## 2. Network and filesystem behavior

At this Mathlib pin:

- Default public endpoint: `https://cache.mathlib.org`.
- Selected container paths: `/mathlib4-master/f/<hash>.ltar`, then
  `/mathlib4/f/<hash>.ltar` for the legacy fallback.
- `MATHLIB_CACHE_DEBUG_USE_LEGACY=1` switches the base to
  `https://lakecache.blob.core.windows.net`. This is a separate debugging fallback, not
  the meaning of the `legacy` container in the command above.
- Read redirects allow HTTPS only, at most five redirects. A redirect may change host;
  this inspection identifies configured bases, not an observed redirect trace.
- `MATHLIB_CACHE_GET_URL` overrides the entire read chain; `MATHLIB_CACHE_BASE_URL`
  overrides its base. Neither override is needed here. An isolated execution environment
  should avoid inheriting unspecified cache overrides.
- Explicit `--repo` and `--cache-from` prevent widening the requested container chain to
  fork caches. The archive checkout has no Git history; Git probes are read-only, and the
  explicit repo supplies the intended upstream identity.

These choices are defined in
[Infra](https://github.com/leanprover-community/mathlib4/blob/065356127b1dc0016f66b7283ce0ce2c4055aa55/Cache/Infra.lean) and
[Requests](https://github.com/leanprover-community/mathlib4/blob/065356127b1dc0016f66b7283ce0ce2c4055aa55/Cache/Requests.lean).

Set `MATHLIB_CACHE_DIR` to a task-specific temporary directory. Otherwise its default is
the user's shared cache. The tool writes `.ltar` archives, per-process partial downloads
and a temporary curl configuration there. It unpacks module artifacts into the relevant
package's `.lake/build/lib/lean` and `.lake/build/ir` directories. Files include `.olean`
and companions, `.ilean`, trace/hash files, optional Lean IR, generated C, and optional
extra artifacts. These are executable compiler inputs, not just documentation.

The cache executable uses `curl` for GETs, read-only Git probes, and the `leantar` bundled
in this Lean toolchain. Its startup locates the latter through `lean --print-prefix`.
The fallback that downloads a newer static curl is limited to Linux x86_64/aarch64; it
does not apply on this macOS host. See
[Cache.IO](https://github.com/leanprover-community/mathlib4/blob/065356127b1dc0016f66b7283ce0ce2c4055aa55/Cache/IO.lean).

No upload command or cloud credential is needed. The cache executable imports upload
implementations, but the proposed `get` dispatch does not invoke them.

## 3. Build hooks and executable code

### Mathlib

The pinned `lakefile.lean` defines a `post_update` hook which may build the cache executable
and run unqualified `cache get` when a downstream project updates dependencies. Set
`MATHLIB_NO_CACHE_ON_UPDATE=1`; use the already pinned manifest instead of updating it.
The cache executable itself compiles and runs Lean code, including transitive tactic/runtime
code. Building `cache` and building the proof are therefore separate execution steps from
the read-only inspection recorded here. See the
[Mathlib Lake configuration](https://github.com/leanprover-community/mathlib4/blob/065356127b1dc0016f66b7283ce0ce2c4055aa55/lakefile.lean).

### ProofWidgets

The library has a `needs := #[widgetJsAll]` build dependency. The pinned source archive
already contains `widget/js/*.js`, `widget/js/lake.trace`, `package-lock.json`, and its
trace. Mathlib supplies `errorOnBuild`, making a stale JavaScript build fail before
`npm clean-install` or `npm run build`.

There is one earlier hook: `widgetPackageLock.fetch` precedes that guard, and a stale
package-lock trace can run `npm install`. Consequently the error guard alone is not a
guarantee that no npm process can start. Preserve the shipped files/traces and deny npm/Node
execution during the replay. If the build requests regeneration, record the failure and
review that concrete dependency rather than silently installing JavaScript packages.
See the pinned
[ProofWidgets configuration](https://github.com/leanprover-community/ProofWidgets4/blob/4c70ac059693669e5756e32a7a94b57ee1e99dc5/lakefile.lean).

### Other dependencies

- `aesop`: ordinary library targets, `precompileModules=false`; no custom execution hook
  in its TOML configuration.
- `Qq`, `plausible`, `Cli`, `LeanSearchClient`: library/test declarations, no custom build
  hook in the inspected configurations.
- `batteries`: also declares linter/test executables; these are not required as separate
  replay commands.
- `importGraph`: graph-analysis executables with interpreter support; neither is needed
  for this proof build.
- `LeanSearchClient` defines optional network search commands using `curl`, with defaults
  at `leansearch.net`, `premise-search.com`, and `loogle.lean-lang.org`. This does not make
  those requests necessary to compile the Lau proof. The offline proof stage should have
  network denied.

No `native_decide` was found in the local Lau solution import closure in the earlier scan.
That finding does not describe the transitive Mathlib theorem proof terms. The actual
axiom report is still required to establish the adopted roots' axiom dependencies.

## 4. Recommended execution boundary and evidence

1. The owner first confirms isolation works, then builds/runs the reviewed cache path
   with the task-specific cache directory and explicit upstream containers.
2. After dependency retrieval, deny network and npm/Node execution and compile the Lau
   sources, explicitly including `Solution.Basic`. Keep all source pins unchanged.
3. Record Lean version, source/dependency pins, command arguments, full logs and exit codes,
   elaborated public theorem types, and their actual transitive axiom sets.
4. Compare the public types with the challenge and the adopted mathematical statement.

Using upstream precompiled dependencies means those cache artifacts remain a trust input;
this is not an independent rebuild of all of Mathlib. Cache names are source-derived lookup
keys, not a proof that downloaded objects were independently reconstructed here. Mathlib's
[cache trust model](https://github.com/leanprover-community/mathlib4/blob/065356127b1dc0016f66b7283ce0ce2c4055aa55/Cache/SECURITY.md)
states this boundary explicitly.

A successful fresh Lau source replay with these stated dependencies is independent of the
author's pipeline and is checked by Lean's kernel. A second kernel implementation remains
optional stronger evidence. Neither outcome is claimed by this configuration review.

## 5. Same-kernel fresh replay and receipt requirements

The bundled Lean source at
`/tmp/collatz_p6_replay/lean-4.35.0-rc2-darwin_aarch64/src/lean/LeanChecker.lean`
was inspected without executing it. `replayFromFresh` (line 41) imports the target and
replays its constant environment into `mkEmptyEnvironment`. The module-system scope was
checked in the bundled `src/lean/Lean/Environment.lean`, not inferred from the name:

- `withImportModules` (2458) calls `importModules` without overriding its default
  `OLeanLevel.private` (2439). The nearby documentation says this loads all data as if
  imported files had no `module` annotations.
- `importModulesCore` sets `importAll` when the global level is private (2183).
  `ImportedModule.mainModule?` therefore selects the private data part (2030–2033).
- `finalizeImport` puts these `ConstantInfo` values in `privateConstantMap` (2331 onward),
  then `base.private` (2385). The `checked` task defaults to `base.private` (574);
  `toKernelEnv` and `constants` expose that map (647, 732).

Thus the command's scope includes private theorem bodies in the imported closure,
including cached dependencies, rather than only exported signatures. Missing required
module data is an error. This is **the same Lean kernel implementation**, replaying the
imported declarations; it is not an independent source rebuild of Mathlib or a second
kernel implementation.

The initial `run_formal_replay.py` was reviewed read-only while the owner was running the
build. Its successful process exit and unchanged-source check are useful stage evidence;
final acceptance additionally needs the following bindings, which were sent to the owner:

- A startup failure must invalidate any earlier receipt for that stage; otherwise a stale
  PASS can survive an exception before the new process starts.
- Statement and kernel stages must identify the successful preceding stage and the exact
  source, specification and generated object files being checked.
- The eight expected axiom reports must actually be present and within the stated
  allowlist. Successful printing alone does not enforce an allowlist.
- Before/after source hashes detect mutation during a run, but do not show that the initial
  files matched the pinned archive. Archive comparison supplies that separate check.

The owner subsequently assigned this reviewer implementation of the receipt hardening.
The following section describes that implementation; actual stage outcomes remain in
the owner's replay receipts.

## 6. Hardened stage receipts and preserved original build

`run_formal_replay.py` now supports `build`, `seal-build`, `statements`, and `kernel`.
The running initial build used a saved earlier runner, SHA-256
`c3087bbddc00de657d4addbc6ca417065e0f8bba9fd54ab57317352483dcb246`.
Its `build_status.json` and `build.log` are never overwritten by the new runner.

After that original build completes successfully, use:

```sh
python3 -B experiments/phase6/linear_density_audit/run_formal_replay.py seal-build \
  --source /tmp/collatz_p6_lau_3a38bfbb7037 --replay /tmp/collatz_p6_replay
```

Then use the same command with `statements`, followed by `kernel`, only after the
preceding stage passes. A seal is not a build rerun. It validates the old successful
status, command, log digest and before-source hashes, and binds them to the archive-checked
sources and proof objects present **at sealing time**. The old runner did not capture
object digests at completion, so the seal makes no claim that these digests were recorded
at that earlier instant. Statements and fresh replay subsequently bind the sealed objects.

Each new attempt has its own log/status under `attempts/`. The current stage receipt is
set to RUNNING before preflight; startup exceptions become FAIL with diagnostics, never a
stale PASS. A prior successful seal cannot silently be rebound to changed objects.
Mandatory content-bound edges are build/seal → statements → kernel. The statement stage
requires exactly one axiom report for each of the four root theorems and each of the four
independent audit theorems. Only the exact names `propext`, `Quot.sound` and
`Classical.choice` are allowed.

Before/after checks bind:

- all 753 regular archive files, reconstructed directly from the checksum-pinned archive
  and compared with `source_snapshot.json`; the snapshot's boolean is not trusted;
- the complete local Lean source inventory, including top-level entry files and the
  challenge; only the prescribed `StatementAudit.lean` may be additional;
- actual dependency Git HEADs and configuration hashes; these dependency repositories
  have **no independent archive receipt**, and this is not a full dependency-source audit;
- the official release asset digest, toolchain archive, Lean/Lake/checker binaries,
  reviewed sandbox, restricted environment, independent specification and runner;
- project, cached dependency and toolchain proof objects (`.olean`, private/server parts,
  IR files), shared libraries and compiled Lake configurations, rather than just the
  top-level solution object.

The statement stage may produce only the StatementAudit module's proof objects; the
read-only seal/kernel stages must leave their object inventories unchanged. Receipt
bindings preserve exact command/log evidence and check every predecessor recursively.
They are reproducibility checks, not cryptographic signatures or an independent audit of
the compiler and operating system.

`test_formal_replay.py` exercises eleven disposable integrity tests: stale-PASS invalidation,
Popen failure, preservation of the initial live receipt, missing/failed/mutated predecessors,
mandatory chain edges, exact/multiline axiom reports, disallowed/lookalike axioms, legacy
sealing and conflicting object rebinding. The tests execute no external Lean code and
touch no live replay stage. All eleven passed before handoff. A stage PASS remains
specific to that stage; successful formal reproduction does not meet the programme's
separate requirement to independently rederive the analytic lower-density argument.
