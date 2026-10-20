# Right-aligned packets and a qualitative current criterion for Collatz

[`right-aligned-reduction.tex`](right-aligned-reduction.tex) is the main lane's (ChatGPT, Codex) running proof note of the packet-currents programme, dated 18 October 2026: 9,027 lines, the rounds R2 to about R94. It is kept byte-identical to its last legacy version (`papers/right_aligned_reduction/right_aligned_reduction.tex` at commit `be73a66`): receipts of the legacy programme pin its SHA-256, so it is not edited, and its own file references point to legacy paths. Its claims are the nodes below; where the paper and a node differ in scope, the node is authoritative.

Build it locally with, for example, `latexmk -pdf right-aligned-reduction.tex`; do not commit the PDF.

## Nodes it presents

| Paper | Node | Legacy ID |
|---|---|---|
| §1, Theorem 1 (fixed-core remainder) | [`right-aligned-fixed-core-remainder`](../../areas/convergence/results/right-aligned-fixed-core-remainder/README.md) | R2 |
| §2, Lemma 2 and Theorem 3 (equivalent qualitative targets) | [`qualitative-current-criterion`](../../areas/convergence/results/qualitative-current-criterion.md) | R3 |
| §3 (exact constant error on dyadic cutoffs) | [`dyadic-cutoff-core-remainder`](../../areas/convergence/results/dyadic-cutoff-core-remainder.md) | R4 |
| The current identity used in Theorem 3 | [`finite-current-certificate-identity`](../../areas/convergence/results/finite-current-certificate-identity.md) | R1-b |
| §4 onward: five rays, annular recursion, component criterion, partial currents, compression, and the later rounds | not yet migrated: legacy `experiments/current_construction/` (R5–R7), `experiments/annular_construction/` (R8–R9), `experiments/residual_progress/` (R10–R94), including the mechanical-word section (R71) | R5–R94 |

The abstract's last line holds for the whole note: no complete universal current construction, Collatz proof, or novelty claim is supplied. The open target is [`packet-current-supply`](../../areas/convergence/questions/packet-current-supply.md).
