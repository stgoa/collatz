# Collatz research

This repository is the persistent record of the Collatz programme: definitions, proofs, failed approaches, finite certificates, and executable checks. Future work should start here rather than reconstructing the programme from chat memory.

**Current standing (2026-10-17): Collatz remains unproved.** We have a written reduction that removes the uniform current-cost requirement for a revised packet family. We do not have a universal current construction, a proof of its termination, human peer review, or formal verification of the new reduction.

## Our current understanding

The programme converts an exact stopping-work discrepancy into a finite signed measure on actual Collatz states. Balanced source packets allow positive and negative contributions to cancel, including contributions that arrive at a common state at different times. A finite current certificate can be checked using one-step arithmetic without resolving the future of its exits.

The latest change is to group **depth-one source triples from the right**. The leftover endpoints then lie only in `{5, 7, 11, 13}`, all of which reach 1 within five odd-only steps. The remainder is therefore controlled at every time horizon.

For this revised family, a written maximum-principle proof shows:

> If every integer cutoff `N >= 8` admits some finite current certificate, then Collatz follows. Certificate size and positive cost may depend arbitrarily on N. A finite current with an everywhere nonpositive residual also suffices.

This criterion is equivalent to Collatz. It removes a quantitative proof obligation but does not prove that the required certificates exist. The original handoff's left-aligned packets and stored currents are a different family; their finite checks do not establish the revised universal criterion.

## Where to start

1. Read [AGENTS.md](AGENTS.md) for working rules and claim standards.
2. Read the [result ledger](docs/RESULTS.md) for exact scope, evidence, and unresolved obligations.
3. Read the [current proof note](collatz_research_20261017/right_aligned_reduction.tex). Open this source in the document editor for its PDF preview.
4. Consult the [master handoff](COLLATZ_PROGRAMME_MASTER_HANDOFF.md) for the wider programme and historical counterexamples. Its old active target is superseded only for the revised right-aligned family.

## Reproduce the finite checks

Requires Python 3.10+ and its standard library. The independent check additionally requires a C++17 compiler (`c++`, or set `CXX` to a compiler executable).

```sh
python3 scripts/verify_all.py --cpp
```

Without a compiler, omit `--cpp`; the report explicitly records that the independent C++ check was not run. The runner verifies the archive and all 31 manifest entries, reruns the stored Python certificates, and reproduces the right-aligned, negative-control, and independent-audit receipts. It uses a temporary directory so the preserved inputs and receipts stay unchanged. With `--cpp`, it also builds and runs the independent verifier at both stored cutoffs.

The checks establish finite arithmetic identities. They do not establish universal current existence or replace the written proof. Never use Python optimization flags for these assertion-based verifiers.

## Repository map

- `COLLATZ_PROGRAMME_MASTER_HANDOFF.md`: inherited proof map and historical context.
- `collatz_packet_currents_bundle.zip`: original supplied archive, retained for provenance.
- `collatz_research_20261017/collatz_packet_currents/`: extracted original proofs, scripts, complete finite current tables, and audit receipts.
- `collatz_research_20261017/right_aligned_reduction.tex`: current written reduction; maintain this existing document in place.
- `collatz_research_20261017/right_aligned_packets.py`: construction and finite regression checks for the revised family.
- `collatz_research_20261017/right_aligned_audit.json`: reproducible finite audit receipt.
- `collatz_research_20261017/negative_controls/`: the independent lane. It contains:
  - audits of R2–R4 and of later main claims;
  - negative controls on `3x+d` maps with real cycles;
  - certificate minimality, and progress-measure controls;
  - a certificate checker (`affine_controls.py --check`).

  The ledger entries are C1–C4.
- `docs/RESULTS.md`: claim ledger and next proof obligations.
- `docs/RESEARCH_LOG.md`: dated record of durable changes and validation.
- `scripts/verify_all.py`: unified verification entry point.

## Next research target

Find an arithmetic construction that produces a finite current, possibly with an everywhere nonpositive residual, for **every integer cutoff** in the right-aligned family. Prove that the construction terminates. Larger collections of successful searches do not discharge this obligation; neither does a small unresolved positive residual over an unbounded time horizon.

Two constraints from the negative-controls note bear on this target. First, the certificate for each cutoff is forced: the exact current is unique and cost-minimal, so a constructor must describe it uniformly rather than search for it. Second, any argument that also applies to the map `3x+61` fails: that map has a 41-cycle, and its criterion breaks at `N=213`.

Update this README and the result ledger whenever the standing changes. Preserve counterexamples and explain which earlier claim a new result supersedes.
