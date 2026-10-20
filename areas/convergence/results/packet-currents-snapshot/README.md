---
id: packet-currents-snapshot
kind: result
title: Exact-source ternary packets, with all-horizon current certificates at two named cutoffs (the inherited snapshot)
status: written
claim: >
  Odd-only (Syracuse) clock, absorbing at 1. Let ν_N be the programme's signed source measure and P the
  push-forward through S that kills mass reaching 1. (i) For every N ≥ 8 and 1 ≤ d ≤ b/2, b = ceil(log₂N),
  grouping consecutive exact source lifts of each valuation word in threes gives P^d ν_N = Π̂_(d,N) + η̂_(d,N),
  where every raw packet has total weight 0 and ‖η̂_(d,N)‖₁ ≤ 6·binom(b,d) + 2·Σ_(j<d) binom(b,j); at
  m = floor(2b/9) and N ≥ 512 this is ≤ 16·N^(7/9), and |3E_T(N) − H_((T−m)+)(Π̂_(m,N))| ≤ T·D*_(b,m).
  (ii) Finite only: at N = 4096 (depth 2) and N = 262144 (depth 4) stored finite currents J with
  (I − P)J = Π̂ give −1406 ≤ H_L(Π̂) ≤ 2364 and −57661 ≤ H_L(Π̂) ≤ 63824 for every horizon L, and
  −34504 ≤ E_T(262144) ≤ 37090 for 0 ≤ T ≤ 231. No bound uniform in N is claimed.
authors:
  - ChatGPT handoff conversation (pre-repository; uploaded by Santiago Armstrong on 2026-10-17)
created: 2026-10-17
depends_on: [finite-current-certificate-identity]
certificates:
  - check_manifest.py
  - collatz_packet_currents/verify_stored_currents.py
  - collatz_packet_currents/finite_source_bounds.py
  - collatz_packet_currents/update_exit_profiles.py
evidence:
  - "collatz_packet_currents/: the inherited snapshot, byte for byte as uploaded on 2026-10-17 (CRLF line endings kept by the .gitattributes pattern **/collatz_packet_currents/**). Its SHA256SUMS.txt lists 31 files; check_manifest.py recomputes them. The original zip (SHA-256 025c8fafe25940951fe408b32b1ec806259725a6b4f8855d9f2b022911fe5447) was byte-identical and is in git history"
  - "collatz_packet_currents/research_note.md: the written proofs (Theorem 2.1, Corollary 2.2, Proposition 3.1, Theorems 4.1 and 5.1) and the finite tables; RESULTS.md, audit_status.md and roadmap.md: the snapshot's own scope statements"
  - "collatz_packet_currents/certificate.py: the discovery run (packets at 14 cutoffs, currents, lag witnesses). Exits 0 at the new path in about 3 s, but rewrites certificate_results.json with a wall-clock elapsed_seconds field, so it is evidence, not a certificate; the receipt was restored. Ran inside scripts/verify_all.py in the legacy tree (temporary copy)"
  - "collatz_packet_currents/independent_verifier.cpp: the C++17 cross-check (needs g++; not a Python certificate). Its outputs independent_4096.json, independent_262144.json and independent_comparison.json are in the snapshot; verify_stored_currents.py compares against them. The compiled binary collatz_packet_currents/independent_verifier, named in the snapshot's README, is gitignored and not in the tree. The legacy gate scripts/verify_all.py --cpp compiled and compared it (passed on 2026-10-17, archive/pre-restructure-2026-10-19/docs/RESEARCH_LOG.md, legacy archive/docs/RESEARCH_LOG.md)"
  - "collatz_packet_currents/audit/: provenance of the upload and an unchanged rerun of the earlier uploaded packet certificate (audit/prior_packet_rerun.txt)"
reviewed_by:
  - by: Claude PR1 lane (Opus)
    date: 2026-10-17
    link: ../locally-collatz-like-control-barrier/NOTE.md
    scope: "Partial and finite only: the stored currents at N = 4096 (2,736 rows) and N = 262144 (132,998 rows) equal the forward aggregates Σ_j P^j Π̂ row for row (NOTE §5, reduction_audit.py). Theorem 2.1 and Corollary 2.2 were not re-derived by another lane; the side lane's survey lists R1 as not touched"
aliases: [R1]
tags: [convergence, packet-currents, finite-certificates, snapshot]
---

# Exact-source ternary packets, with all-horizon current certificates at two named cutoffs (the inherited snapshot)

## Statement

Notation (odd-only clock, absorbing at 1, as in [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md)): `S(x) = (3x+1)/2^(v₂(3x+1))` on positive odd integers, `τ(x)` the first hitting time of 1 (possibly infinite), `h_L(x) = min(L, τ(x))`, and `H_L(μ) = ⟨μ, h_L⟩` for a finite signed integer measure `μ` on odd states `> 1`. `P` pushes `μ` forward through `S` and kills mass reaching 1. For `N ≥ 8`, `n_1 = floor((3N+1)/2)`, `n_2 = floor((3N+1)/4)` and

```
ν_N(x) = 1[x ≤ n_1]·(3·1[x ≡ 5 mod 6] − 1) + 1[x ≤ n_2]·(3·1[x ≡ 1 mod 6] − 1),   x > 1 odd.
```

The programme's discrepancy satisfies `3E_T(N) = H_T(ν_N)` (research note (1.2)).

**Theorem 2.1 (exact decomposition and improved remainder).** For every `N ≥ 8` and `1 ≤ d ≤ b/2`, `b = ceil(log₂ N)`: group the exact positive source lifts `x_t = q_w + 2^(A+1)t` of each length-`d` valuation word `w` with `A ≤ b`, separately in each of the two source components, into consecutive triples. Each triple has weights a permutation of `(2, −1, −1)` and endpoints spaced by `2·3^d`. Then

```
P^d ν_N = Π̂_(d,N) + η̂_(d,N),     ‖η̂_(d,N)‖₁ ≤ D*_(b,d) := 6·binom(b,d) + 2·Σ_(j<d) binom(b,j).
```

**Corollary 2.2.** For `N ≥ 512` and `m = floor(2b/9)`: `‖η̂_(m,N)‖₁ ≤ 16·N^(7/9)`, and for every `T`, `|3E_T(N) − H_((T−m)+)(Π̂_(m,N))| ≤ T·D*_(b,m)`. On the programme's window `T ≤ ceil((b+1)·N^(1/5))` the error is at most `16(b+2)·N^(44/45) = o(N)`. This bounds the remainder, **not** the retained packet work.

**Finite certificates (named cutoffs only).** For the ten dyadic cutoffs `2^9 … 2^18` and `N = 513, 999, 4097, 10001`, finite currents `J` with `(I − P)J = Π̂_(m,N)` were constructed and their identities checked. With the exit-profile bound of [`finite-current-certificate-identity`](../finite-current-certificate-identity.md), for **every** horizon `L ≥ 0`:

| N | anchor m | positive-current cost | exit-profile lower | exit-profile upper |
|---:|---:|---:|---:|---:|
| 4,096 | 2 | 4,352 | −1,406 | 2,364 |
| 16,384 | 3 | 15,256 | −3,957 | 4,085 |
| 65,536 | 3 | 58,599 | −16,698 | 6,902 |
| 262,144 | 4 | 226,776 | −57,661 | 63,824 |

Complete tables are stored for `N = 4096` and `N = 262144` only. Combining them with the exact anchor residual gives `−2746/3 ≤ E_T(4096) ≤ 3838/3` for `0 ≤ T ≤ 69`, and `−34504 ≤ E_T(262144) ≤ 37090` for `0 ≤ T ≤ 231`.

## Proof

The written proofs are in [`collatz_packet_currents/research_note.md`](collatz_packet_currents/research_note.md) (§2 for Theorem 2.1 and Corollary 2.2; §§3–5 for the current identities, which are the node [`finite-current-certificate-identity`](../finite-current-certificate-identity.md); §6 for the finite tables). Summary of §2, kept as written:

- **Cylinders.** A length-`d` word `w` with total `A` has exact positive sources `x_t = q_w + 2^(A+1)t` and endpoints `y_t = e_w + 2·3^d·t`, where `q_w` is the least positive residue with `3^d·q_w + C_w ≡ 2^A (mod 2^(A+1))`. Source 1 and endpoint 1 are excluded by starting at `t_0 ∈ {0, 1}`; an intermediate visit to 1 would force endpoint 1, so no absorbed source is silently kept.
- **Triples.** `2^(A+1)` is a unit mod 3, so three consecutive lifts carry each source residue mod 3 once; the weights are a permutation of `(2, −1, −1)` and sum to zero. At most two lifts per word and component are left over, of absolute weight at most 3, so at most 6 per word.
- **Count.** There are `binom(b,d)` words of length `d` with `A ≤ b`. Among odd residues mod `2^(b+1)`, exactly `Σ_(j<d) binom(b,j)` have first-`d` valuation sum above `b`; `ν_N` lives below `2^(b+1)` with weights of absolute value at most 2. Summing gives `D*_(b,d)`.
- **Corollary.** `D*_(b,m) ≤ 8·Σ_(j≤m) binom(b,j)`, `H₂(2/9) < 7/9` (from `9^9 < 2^9·7^7`) and `8^9·2^7 < 16^9`. Every packet has total zero; monotonicity of `D*_(b,d)` in `d ≤ m` and the initial signed total `≤ 8 ≤ D*_(b,m)` give the transfer bound.

The finite tables are certificates checked by the scripts below, not consequences of a general argument. The snapshot itself calls its proofs "candidate written proofs, not kernel-checked formalizations" with "no independent human review" (`collatz_packet_currents/audit_status.md`).

## Certificates

All four run from the repository root in about a second each and use only the standard library. The three legacy scripts check by `assert`, so they must run without `-O`.

- [`check_manifest.py`](check_manifest.py) (new at migration): recomputes the SHA-256 of all 31 files listed in [`collatz_packet_currents/SHA256SUMS.txt`](collatz_packet_currents/SHA256SUMS.txt) and exits 1 on any mismatch. It certifies that the snapshot is the 2026-10-17 upload, byte for byte.
- [`collatz_packet_currents/verify_stored_currents.py`](collatz_packet_currents/verify_stored_currents.py): rebuilds the packets at `N = 4096` and `262144` from source cylinders, checks `(I − P)J = Π̂` row by row on the stored currents, the acyclicity of their support and the stored exit profiles, and compares with the C++ outputs. It follows no exit beyond the table. Rewrites `stored_verification.json` byte for byte.
- [`collatz_packet_currents/finite_source_bounds.py`](collatz_packet_currents/finite_source_bounds.py): the two complete finite-source error certificates above. Rewrites `finite_source_error_certificates.json` byte for byte.
- [`collatz_packet_currents/update_exit_profiles.py`](collatz_packet_currents/update_exit_profiles.py): the all-horizon exit-profile bounds at the 14 cutoffs from the stored discovery receipt. Rewrites `exit_profile_results.json` and `data/exit_profiles_*.json` byte for byte.

Each of these exits 0 at its new path and leaves every manifest hash unchanged (checked at migration).

## Remarks

- **Scope.** The remainder theorem is uniform in `N`; the current tables are not. Fourteen cutoffs were tested and two complete tables are stored. The discovery constructor follows finite orbits to a small core and aborts on a path-cap exceedance or an unhandled cycle; its success at other cutoffs is not claimed. Making the current cost uniform is the open question [`uniform-current-cost`](../../questions/uniform-current-cost.md).
- **A different grouping from the later programme.** The hatted family `Π̂` keeps the exact ancestral word and source interval of every packet. It differs from the uploaded homogeneous-cell family, and from the depth-one right-aligned family `Π^R_N` of [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md); these tables cannot be relabelled as certificates for `Π^R_N`.
- **Sign.** Packet balance does not fix the sign of the work: the snapshot's examples are `−δ_6929 − δ_6947 + 2δ_6965`, with `−75 ≤ H_L ≤ 0`, and `δ_55 + δ_73 − 2δ_91`, with `0 ≤ H_L ≤ 17`, for every `L` (research note (3.2), (3.3)).
- **Independent computation.** The C++ verifier rebuilds the packets by direct iteration of every source, without cylinder inversion, and checks every current row and exit profile; its outputs agree. Its author is the same assistant, so this is algorithmic cross-checking, not independent authorship (`audit_status.md`).
- **Literature.** Finite parity cylinders are classical (Bernstein–Lagarias, *The 3x+1 conjugacy map*, Canad. J. Math. 48 (1996)); no theorem of [`tao-2019-almost-all`](../../../../sources/tao-2019-almost-all.md) is used. The note claims no novelty; novelty undetermined.

## History

- Migrated from `experiments/packet_currents/` at commit `be73a66` (legacy ID `R1`), by the B07 migration (Claude, Opus 5.5). This README was the line README `experiments/packet_currents/README.md`; the snapshot `experiments/packet_currents/collatz_packet_currents/` moved here unchanged. Until 2026-10-19 the folder was the top-level `collatz_research_20261017/`.
- The snapshot was uploaded on 2026-10-17 by Santiago Armstrong from a ChatGPT conversation, together with the origin document [`archive/handoff/COLLATZ_PROGRAMME_MASTER_HANDOFF.md`](../../../../archive/handoff/COLLATZ_PROGRAMME_MASTER_HANDOFF.md) (legacy path `archive/COLLATZ_PROGRAMME_MASTER_HANDOFF.md`; §§2–10 develop the same material). The main lane (ChatGPT, Codex) entered it as R1, "inherited written proofs and finite certificates", recorded the zip hash, and checked all 31 manifest entries in its gate `scripts/verify_all.py`.
- 2026-10-17: the PR1 lane (Claude, Opus) checked the stored currents against forward aggregates (see `reviewed_by`).
- The main lane's packet-currents programme (R1–R94) was later declared frozen at R94; that is a history note, not a status.
- Legacy scripts in other lines (current construction, annular construction, residual progress) load `experiments/packet_currents/right_aligned_packets.py` and this snapshot's `data/` by their old paths; see [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md).
