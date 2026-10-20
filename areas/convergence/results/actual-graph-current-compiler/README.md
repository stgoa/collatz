---
id: actual-graph-current-compiler
kind: result
title: Thirty actual one-sided packet certificates compile into a 95-row integer absorption current for U_112
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1. A finite computation, conditional only on its own explicit inputs: with
  the exact cone plan of finite-rational-cone-integer-certificate for target m = 97 (g = 112, B = 9), thirty
  actual integer packet certificates Pi_N = (I - P)J_N + Z_N with Z_N <= 0 at the starting cutoffs a 2^b,
  a in (12, 14, 16, 18, 21), 3 <= b <= 8 (found by capped historical search; twenty of them leave some source
  states unlinked to 1 in their own graphs), together with the explicit source-scale, fixed-core,
  lower-boundary and rounding-shell terms, give the exact identity d U_112 = (I - P)J_num + Z_num with common
  denominator d = 46422343855805, 6217 rational current rows and positive residual mass
  29145292346068/46422343855805 < 1; routing the 55 integer source units along already present arrows gives a
  stored 95-row nonnegative integer current whose divergence is 1 at each odd state 3..111 and 0 elsewhere. It
  does not supply the packet certificates needed at arbitrary cutoffs.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [finite-rational-cone-integer-certificate]
evidence:
  - "actual_graph_compiler.py, forcing_demo_audit.json: the legacy compiler compile_inputs(plan, provider) and its default run, which regenerates the thirty inputs deterministically, verifies the full rational identity and the strict bound, compares the receipt (hashes of the complete numerator tables, discovery depths, unlinked-source counts) and checks every row of the stored current. Fails at its new path: it loads ../duality/finite_cone.py and experiments/packet_currents/right_aligned_packets.py by their pre-migration paths (now ../finite-rational-cone-integer-certificate/finite_cone.py and ../right-aligned-fixed-core-remainder/right_aligned_packets.py). Passed at be73a66 as experiments/residual_progress/forcing/actual_graph_compiler.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). The legacy checker of local-packet-calibration-extension loads it by its old path ../forcing/"
  - "forced_U112_current.csv: the extracted 95-row nonnegative integer current for U_112, written by actual_graph_compiler.py --write-receipt"
aliases: [R11-b]
tags: [convergence, packet-currents, finite-cone, finite-certificate, constructive]
---

# Thirty actual one-sided packet certificates compile into a 95-row integer absorption current for U_112

## Statement

A finite demonstration of the conditional theorem [`finite-rational-cone-integer-certificate`](../finite-rational-cone-integer-certificate/README.md), on actual positive odd Syracuse states with exact integer arithmetic (odd-only clock, absorbing at 1).

For the target `m = 97` (first grid cutoff `g = 112`) the exact cone at `B = 9` uses the 30 input cutoffs `a·2^b`, `a ∈ {12, 14, 16, 18, 21}`, `3 ≤ b ≤ 8` (the largest is 5376). The provider supplies actual integer currents with nonpositive residual at each, found by capped historical search; in twenty of the thirty searches some source states are still unlinked to 1 in their own exposed graphs, so the inputs use current cancellation, not only absorption of every source. Compiling them with the explicit single-cutoff source current, the signed fixed-core current, the lower-boundary currents and the negative rounding shells gives:

| Quantity | Exact result |
|---|---:|
| Common denominator d | 46422343855805 |
| Rational current rows | 6217 |
| Rational residual atoms | 4034 |
| Upper-boundary mass bound | 31562113241597 / 46422343855805 |
| Actual positive residual mass | 29145292346068 / 46422343855805 |
| Integer target source mass | 55 |
| Extracted integer current rows | 95 |

Both positive masses are below 1, so every target source lies in the absorbing component of the nonzero rational current; routing the 55 units along existing arrows only gives a 95-row nonnegative integer current with divergence 1 at each odd state 3 through 111 and zero elsewhere. This is a finite certificate conversion conditional on the supplied packet certificates; it does not construct the inputs needed at an arbitrary unresolved annulus.

## Proof

The legacy note "Compiling actual packet certificates into an integer absorption current" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

17 October 2026. This is a finite demonstration of the conditional theorem in
[FINITE_CONE.md](../finite-rational-cone-integer-certificate/README.md), using actual positive Syracuse
states and exact integer arithmetic. It does not construct the required inputs
at arbitrary cutoffs or prove Collatz.

### Reusable construction

`actual_graph_compiler.py::compile_inputs(plan, provider)` accepts the exact
rational plan from `finite_forcing_plan` and a provider of finite packet
certificates. For each requested N, the provider returns an integer current J
and an everywhere nonpositive residual Z. The compiler reconstructs the actual
right-aligned packet source and verifies `Pi_N=(I-P)J+Z` coefficient by
coefficient. It also checks that the data are integers on positive odd states.

It then adds the explicit single-cutoff source current, the signed fixed-core
absorption current, the lower-boundary absorption currents, and the negative
rounding shells, with the exact finite-cone weights. Every rational coefficient
is represented over one common integer denominator d. The complete identity
is independently checked as

`d U_g = (I-P)J_num + Z_num`.

The compiler verifies `sum max(Z_num(x),0) < d`. An unabsorbed component with
one target source would have source mass at least d; its boundary sum cannot
equal a residual whose entire positive mass is smaller than d. Hence all
target sources are already connected to the absorber in the graph of the
nonzero rational current. The final step routes their integer masses to 1
using **only those existing arrows**. It adds no new orbit exposure.

The output is an exact nonnegative integer current for U_g. This is a finite
certificate conversion, conditional on the supplied packet certificates.
The demonstration's provider uses capped historical search; a reached cap
raises an unresolved error instead of claiming nonexistence or success.

### Actual demonstration

Target m=97 has first covering grid point g=112. The exact cone at B=9
uses 30 input cutoffs, all `a*2^b` with a in `{12,14,16,18,21}` and
`3<=b<=8`; the largest is 5376. These are the finite starting cutoffs
already identified by the annular recursion, but the demo supplies actual
nonpositive-residual currents rather than assuming all source paths exposed.

Twenty of the 30 input searches finish while some source states are still
unlinked to 1 in their own exposed graphs. Their current and residual hashes,
discovery depths, and unlinked-source counts are stored in the receipt.
This distinguishes current cancellation from simply following every input
source to absorption.

The compiled certificate has:

| Quantity | Exact result |
|---|---:|
| Common denominator d | 46422343855805 |
| Rational current rows | 6217 |
| Rational residual atoms | 4034 |
| Upper-boundary mass bound | 31562113241597 / 46422343855805 |
| Actual positive residual mass | 29145292346068 / 46422343855805 |
| Integer target source mass | 55 |
| Extracted integer current rows | 95 |

Both positive-mass fractions are strictly below 1. The final 95-row current
is stored as [forced_U112_current.csv](forced_U112_current.csv). Its exact
divergence is 1 at each odd state 3 through 111 and zero everywhere else.
The receipt stores hashes of the complete rational numerator tables; default
reproduction reconstructs and verifies them before comparing the hashes.

### Reproduce

```sh
python3 experiments/residual_progress/forcing/actual_graph_compiler.py
```

The default run regenerates the packet inputs deterministically, verifies the
full rational identity and strict bound, compares the persisted receipt, and
checks every row of the final stored current. Use `--write-receipt` only to
deliberately regenerate the JSON and final CSV. All searches are capped.

This is a proof of the finite compiler's behavior on these inputs. The
general theorem rests on the finite cone identity and integer-component
lemma. Neither the theorem nor the example supplies the larger packet
certificates needed to apply the compiler to an arbitrary unresolved annulus.

## Certificates

No certificate runs at this path. The legacy compiler `actual_graph_compiler.py` (which regenerates and checks everything above) loads two modules by their pre-migration paths; it is evidence only. The stored current [`forced_U112_current.csv`](forced_U112_current.csv) can be checked by hand: each row is an odd state and its integer current, and the divergence `J − PJ` must be the counting measure of the odd states 3..111. The commands in the legacy text name the pre-migration path `experiments/residual_progress/forcing/`.

## Remarks

- This demonstration is a proof of the compiler's behaviour on these inputs; the general theorem rests on the finite cone identity and the integer-component lemma of [`finite-rational-cone-integer-certificate`](../finite-rational-cone-integer-certificate/README.md). The inputs at the 30 starting cutoffs are the finite base already identified by [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md).
- A reached search cap raises an unresolved error instead of claiming success or nonexistence.
- Novelty undetermined.

## History

- Migrated from `experiments/residual_progress/forcing/ACTUAL_COMPILER.md` (the ledger lists it under R11; alias R11-b here) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). Note, script, receipt and stored current moved byte-identical.
- Main lane (ChatGPT, Codex), 2026-10-17. The round report says an independent model review checked the proof and all signs in the compiler; that review was run by the main lane's own agents and is not counted as independent.
