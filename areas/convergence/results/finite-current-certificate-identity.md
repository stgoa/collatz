---
id: finite-current-certificate-identity
kind: result
title: A finite signed current with (I − P)J = μ controls the stopping work of μ at every horizon
status: written
claim: >
  Odd-only clock, absorbing at 1; P pushes a finite signed integer measure through S and kills mass at 1;
  τ is the hitting time of 1 (possibly infinite) and H_L(μ) = Σ μ(x)·min(L, τ(x)). (i) Lag formula: if
  sources x_i with weights c_i, Σ c_i = 0, reach a common state z after verified path lengths d_i without
  visiting 1, then Σ c_i·h_L(x_i) = Φ((L − τ(z))+) for every L, with Φ(u) = Σ c_i·min(u, d_i) and the value
  0 when τ(z) = ∞. (ii) Current identity: if a finite signed table J satisfies (I − P)J = μ, then
  H_L(μ) = Σ_y J(y)·1[τ(y) ≤ L] for every L ≥ 0, so −‖J⁻‖₁ ≤ H_L(μ) ≤ ‖J⁺‖₁; with a residual,
  μ = (I − P)J + ζ gives H_L(μ) ≤ ‖J⁺‖₁ + L·‖ζ⁺‖₁. (iii) Exit profiles: if the arrow graph on supp J is
  acyclic, grouping rows by first exit z from supp J and distance k gives H_L(μ) = Σ_z F_z((L − τ(z))+),
  hence Σ_z min(0, min F_z) ≤ H_L(μ) ≤ Σ_z max(0, max F_z). No convergence of any orbit is assumed.
authors:
  - ChatGPT handoff conversation (pre-repository; uploaded by Santiago Armstrong on 2026-10-17)
created: 2026-10-17
depends_on: []
evidence:
  - "packet-currents-snapshot/collatz_packet_currents/research_note.md §§3-5: the written proofs (Proposition 3.1, Theorems 4.1 and 5.1)"
  - "packet-currents-snapshot/collatz_packet_currents/certificate.py and lag_witnesses.json: three finite common-tail witnesses replayed to their meeting states, and the lag formula tested against arbitrary hypothetical remaining delays, including infinity"
reviewed_by:
  - by: Claude PR1 lane (Opus)
    date: 2026-10-17
    link: right-aligned-fixed-core-remainder/README.md
    scope: "Partial: the telescoping step of (ii), H_L((I − P)J) = ⟨1, J − P^L J⟩, was re-derived as part of the audit of the right-aligned criterion's step 4 ⇒ 2 (legacy NOTE.md §6; see qualitative-current-criterion). The lag formula (i) and the exit-profile theorem (iii) have no review on record"
aliases: [R1-b]
tags: [convergence, packet-currents, current-identity, telescoping]
---

# A finite signed current with (I − P)J = μ controls the stopping work of μ at every horizon

## Statement

Notation of [`packet-currents-snapshot`](packet-currents-snapshot/README.md): `S` the odd-only map, `τ(x)` the first hitting time of 1 (possibly `∞`), `h_L(x) = min(L, τ(x))` with `h_L(1) = 0`, `H_L(μ) = ⟨μ, h_L⟩ = Σ_(j<L) ⟨1, P^j μ⟩` for finite signed integer measures `μ` on odd states `> 1`, where `P` kills mass reaching 1. A **current** is a finite signed table `J` on odd states `> 1`, read as weights on the arrows `y → S(y)`; its **divergence** is `∂J = (I − P)J`.

1. **Common-tail lag formula (Proposition 3.1).** Let positive odd sources `x_i`, with integer weights `c_i` summing to zero, reach one positive odd state `z` after verified path lengths `d_i`, without an earlier visit to 1 (a source may be `z` itself, `d_i = 0`). Put `Φ(u) = Σ_i c_i·min(u, d_i)`. Then for every `L ≥ 0`, `Σ_i c_i·h_L(x_i) = Φ((L − τ(z))+)`, where the right side is `Φ(0) = 0` if `τ(z) = ∞`.
2. **Current identity (Theorem 4.1).** If `μ = ∂J` for a finite `J`, then for every integer `L ≥ 0`, `H_L(μ) = Σ_y J(y)·1[τ(y) ≤ L]`. Consequently `−‖J⁻‖₁ ≤ H_L(μ) ≤ ‖J⁺‖₁`. If `μ = ∂J + ζ`, then `H_L(μ) ≤ ‖J⁺‖₁ + L·‖ζ⁺‖₁`; a negative residual costs nothing for the upper bound.
3. **Exit profiles (Theorem 5.1).** Suppose the directed graph of `S` restricted to `supp J` has no cycle. For `y ∈ supp J` let `z(y)` be its first exit from `supp J` (possibly 1) and `d(y)` the path length. Put `v_z(k) = Σ_(z(y)=z, d(y)=k) J(y)`, `F_z(u) = Σ_(k≤u) v_z(k)`, `U_z = max(0, max F_z)` and `L_z = min(0, min F_z)`. Then `H_L(μ) = Σ_z F_z((L − τ(z))+)` and `Σ_z L_z ≤ H_L(μ) ≤ Σ_z U_z`. The upper cost `Σ U_z` is at most `‖J⁺‖₁`.

## Proof

From `collatz_packet_currents/research_note.md` in [`packet-currents-snapshot`](packet-currents-snapshot/README.md), kept as written.

1. If `τ(z) < ∞` then `τ(x_i) = d_i + τ(z)`. For `L ≤ τ(z)` every `h_L(x_i) = L` and the weighted sum is zero. Otherwise subtract the common `τ(z)` from `min(L, d_i + τ(z))` and use `Σ c_i = 0`. If `τ(z) = ∞`, all sources have `h_L = L` and cancel. `Φ` is piecewise linear and constant after `max d_i`, so its extrema are among `0` and the `d_i`: finite verified paths to `z` bound every future horizon without following the orbit after `z`.
2. Telescoping the sum formula for `H_L` gives `H_L((I − P)J) = ⟨1, J − P^L J⟩`, and a row `y` still contributes to `P^L J` exactly when it has not hit 1 by time `L`. Equivalently, `h_L(y) − h_L(S y) = 1[τ(y) ≤ L]` with `h_L(1) = 0`. The residual version adds `H_L(ζ) ≤ L·‖ζ⁺‖₁`.
3. Before its exit the path from `y` contains no 1, so `τ(y) = d(y) + τ(z(y))`, also when the latter is infinite. Substitute into (2), group by exit and distance, and bound each finite cumulative profile separately. No independence of the different exits' continuations is assumed; the sum of separate extrema is safe but not claimed sharp.

A verifier needs one evaluation of `S` per row: add `J(y)` at `y`, subtract it at `S(y) > 1`, compare with `μ`. Acyclicity of `supp J` is itself checked; a verified nontrivial cycle inside the support would need separate handling, and none is assumed absent as an external fact.

## Remarks

- **Why it matters.** Unlike the norm sum `Σ_j ‖P^j μ‖₁`, a current keeps cancellations between contributions that reach the same state at *different* times. For `S(u) = z > 1`, `0 ≤ h_L(u) − h_L(z) ≤ 1` for all `L`, while the synchronous absolute mass of `δ_u − δ_z` would stay 2 forever if `z` had a divergent orbit: bounding total residence can need much more than bounding the signed quantity.
- **Not new as mathematics.** The snapshot calls (i)–(iii) elementary coboundary and telescoping identities for a deterministic map, "not presented as a newly discovered general theorem". What is particular to the programme is their use for exact-source packets with finite, checkable certificates. Novelty undetermined.
- **Uses.** The step "4 ⇒ 2" of [`qualitative-current-criterion`](qualitative-current-criterion.md) is (ii) with a nonpositive residual. The finite certificates of [`packet-currents-snapshot`](packet-currents-snapshot/README.md) use (iii). [`exact-current-minimality`](exact-current-minimality.md) studies which `J` can satisfy `∂J = μ`.

## History

- Split at migration from the inherited snapshot `experiments/packet_currents/collatz_packet_currents/research_note.md` §§3–5 (part of legacy `R1`) at commit `be73a66`, by the B07 migration (Claude, Opus 5.5), because later results cite the identity on its own. Alias `R1-b` is new; the legacy ledger has only `R1`.
- The same identities appear in the origin document [`archive/handoff/COLLATZ_PROGRAMME_MASTER_HANDOFF.md`](../../../archive/handoff/COLLATZ_PROGRAMME_MASTER_HANDOFF.md) §7 (legacy path `archive/COLLATZ_PROGRAMME_MASTER_HANDOFF.md`) and in the proof of Theorem 3 of [`papers/right-aligned-reduction`](../../../papers/right-aligned-reduction/README.md).
