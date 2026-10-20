---
id: whole-packet-historical-certificates
kind: result
title: Whole-packet historical searches give an exact current at N = 65536 and a one-sided current at N = 2053 that cancels unresolved futures
status: written
claim: >
  Finite statements, odd-only 3x+1 map absorbing at 1, right-aligned packets Π^R_N. (a) Stored, checked
  certificates: an exact current for Π^R_65536 with 53,621 nonzero rows and positive cost 74,725, and a current
  for Π^R_2053 with 1,532 rows, positive cost 1,950 and an everywhere nonpositive residual of four atoms and
  total mass −5. (b) With historical exposure from every source atom (cap 96), at the ten cutoffs N = 120, 236,
  480, 517, 1984, 2053, 3008, 8197, 15104, 65536 the first exact and one-sided successes occur at the depths
  of the table (72 and 72 at 65536); at 2053 the exact current is found while 27 sources, in two components of
  mass zero, have no path to 1 in the exposed graph, and the one-sided one with 32 sources unlinked; at
  65536 the exposed graph already links every source to 1. These certify only the named finite measures;
  no uniform exposure depth and no universal current existence follows.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [orbit-component-current-criterion, right-aligned-fixed-core-remainder]
certificates: [check_stored_currents.py, check_legacy_replay.py]
evidence:
  - "whole_packet_demo.py, whole_packet_audit.json, and the four CSV tables: the legacy experiment that ran the searches, rebuilt each packet, checked every divergence, compared exact historical currents with synchronous ones, and checked the stored tables and its receipt. Fails at its new path: it imports verify_obstructions from its own folder (now ../orbit-component-current-criterion/) and loads experiments/packet_currents/right_aligned_packets.py relative to the repository root (now ../right-aligned-fixed-core-remainder/). Passed at be73a66 as experiments/current_construction/obstructions/whole_packet_demo.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "The depth table, the unlinked-source counts and the synchronous comparison rest on that legacy run and its receipt; check_stored_currents.py re-checks only the two stored tables (part (a))"
aliases: [R7-c]
tags: [convergence, packet-currents, right-aligned, finite-certificate, historical-search]
---

# Whole-packet historical searches give an exact current at N = 65536 and a one-sided current at N = 2053 that cancels unresolved futures

## Statement

Odd-only clock, absorbing at 1; packets `Π^R_N` as in [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md). The constructor is the complete historical search of [`orbit-component-current-criterion`](../orbit-component-current-criterion/README.md): it exposes at most `d` steps from **every nonzero source atom** of `Π^R_N`, joins historical intersections, and tests the total signed source mass in each finite component. A component containing 1 is resolved; all others must have mass zero for an exact current, or mass at most zero for a nonpositive-residual current.

**(a) Stored certificates.**

| N | Type | Rows | Positive cost | Residual |
|---:|---|---:|---:|---|
| 65536 | exact | 53,621 | 74,725 | 0 |
| 2053 | nonpositive residual | 1,532 | 1,950 | 4 atoms, total mass −5 |

**(b) Search depths** (finite caps: historical depth 96, synchronous depth 512, 1,000 odd-only steps per source for the separate hitting-time comparison; all ten inputs succeeded within these caps):

| Cutoff N | Historical exact depth | Historical one-sided depth | Synchronous exact depth |
|---:|---:|---:|---:|
| 120 | 12 | 12 | 44 |
| 236 | 12 | 8 | 51 |
| 480 | 50 | 13 | 61 |
| 517 | 50 | 15 | 61 |
| 1984 | 31 | 28 | 78 |
| 2053 | 26 | 17 | 78 |
| 3008 | 43 | 30 | 86 |
| 8197 | 45 | 44 | 97 |
| 15104 | 44 | 37 | 101 |
| 65536 | 72 | 72 | 128 |

Depth means the maximum exposed prefix length from each original source; it is not a current-row count, a wall-clock measure, or the length of paths assembled by joining prefixes.

**(c) Cancellation versus compressed halting.** At the deliberately chosen non-grid cutoff **2053**, the exact current is found while **27 sources have no path to 1 in the exposed graph**; they occupy two components of mass zero, with 18 and 9 sources, and their futures cancel without being followed to the absorber. The one-sided certificate stops earlier, with 32 sources unlinked to 1 across six components of masses `0, 0, −2, −1, −1, −1`. At all the sampled earlier 30-ray cutoffs, and at 65536 (also on the five-ray grid), the exposed graph at exact success already links every source to 1.

## Proof

Exact finite computation. The searches, divergence checks and depth table come from the legacy `whole_packet_demo.py` and its receipt `whole_packet_audit.json` (see `evidence`). Part (a) is re-checked by the certificate below.

**Why the exact currents agree with synchronous ones.** Every sampled exact historical current agrees coefficient by coefficient with the full synchronous current. This is expected after the separate finite check that the sources terminate: finite currents on an absorbing functional component are unique. If a finite signed current has zero divergence, each state with nonzero outgoing weight must have at least one predecessor with nonzero weight. Following such predecessors inside the finite support forces a cycle. A deterministic cycle cannot have a forward path leaving it, so the original state itself must lie on that cycle. Thus all nonzero support lies on directed cycles, and conservation makes the weight constant around each cycle: the kernel consists of finite cycle circulations. An absorbing component, with its absorber's outgoing edge excluded, has no such cycles. Unknown disjoint nonabsorbing cycles could supply irrelevant additional circulations in the general graph; they play no role in these tables. ∎

## Certificates

[`check_stored_currents.py`](check_stored_currents.py) (written at the migration, under 1 s, standard library). It rebuilds `Π^R_65536` (34,716 atoms) and `Π^R_2053` (1,086 atoms) with the constructor of [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md), and checks `Π^R_N = (I − P)J + Z` exactly for [`exact_65536.csv`](exact_65536.csv) with the empty residual [`exact_residual_65536.csv`](exact_residual_65536.csv), and for [`one_sided_2053.csv`](one_sided_2053.csv) with [`one_sided_residual_2053.csv`](one_sided_residual_2053.csv), together with the row counts, positive costs, residual sign and residual mass of part (a).

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `whole_packet_demo.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 34 s). It checks finite steps only; the status is unchanged.

## Remarks

- **Two mechanisms.** At 2053 the certificate genuinely uses signed-current cancellation of unresolved common futures; at 65536 the exposed graph proves absorption of every source, and the smaller discovery depth is shared-path compression. Neither finite example proves universal termination. If an argument instead shows that all sources enter a known halting interval, it should be described as a descent proof; presenting it as current cancellation would hide the true obligation.
- **Cost.** Earlier stopping and fewer rows do not automatically mean smaller positive cost: at 2053 the exact current has 1,636 rows and positive cost 1,887, the one-sided one 1,532 rows and cost 1,950. In all samples, synchronous extinction occurs at the largest individual source hitting time, independently checked with a finite cap.
- **Uniform aggregate exposure depth.** A uniform depth `D` for whole packets is a separate candidate, not a theorem: [`uniform-aggregate-exposure-depth`](../../questions/uniform-aggregate-exposure-depth.md). The per-triple obstruction [`bounded-packet-certificate-obstruction`](../bounded-packet-certificate-obstruction.md) does not rule it out, because the aggregate construction allows cancellation between triples. Depths at most 71 already fail at 65536 for this exposure rule, in both modes; the sample is too small to infer eventual boundedness or growth.
- **Next obligation (legacy).** A recursive arithmetic proof controlling the signed mass of exposed components, with depth depending on the cutoff: explain why unresolved components always have nonpositive mass, or why a positive component must eventually merge or reach an already verified component. This became [`annular-component-progress-lemma`](../../questions/annular-component-progress-lemma.md).
- The 65536 table certifies the revised (right-aligned) family at one cutoff; it is separate from the stored currents of the inherited snapshot ([`packet-currents-snapshot`](../packet-currents-snapshot/README.md)), which use another packet family.

## History

- Migrated from `experiments/current_construction/obstructions/whole_packet_findings.md` (part of the legacy R7 round) at commit `be73a66`, by the B08 migration (Claude, Opus 5.5); the demo, receipt and four tables moved byte-identical. `check_stored_currents.py` was added at the migration because the demo no longer runs at its new path. Legacy status: "finite certificate results"; "these experiments do not prove universal existence, a uniform exposure depth, or Collatz convergence".
- Main lane (ChatGPT, Codex), 2026-10-17. No review from another lane is on record.
