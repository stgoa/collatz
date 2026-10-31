# Right-aligned packets and a qualitative current criterion for Collatz

[`right-aligned-reduction.tex`](right-aligned-reduction.tex) is the main lane's (ChatGPT, Codex) running proof note of the packet-currents programme, dated 18 October 2026: 9,027 lines, the rounds R2 to about R94. It is kept byte-identical to its last legacy version (`papers/right_aligned_reduction/right_aligned_reduction.tex` at commit `be73a66`): receipts of the legacy programme pin its SHA-256, so it is not edited, and its own file references point to legacy paths. Its claims are the nodes below; where the paper and a node differ in scope, the node is authoritative.

Build it locally with, for example, `latexmk -pdf right-aligned-reduction.tex`; do not commit the PDF.

## Nodes it presents

| Paper | Node | Legacy ID |
|---|---|---|
| §1, Theorem 1 (fixed-core remainder) | [`right-aligned-fixed-core-remainder`](../../areas/convergence/results/right-aligned-fixed-core-remainder/README.md) | R2 |
| §2, Lemma 2 and Theorem 3 (equivalent qualitative targets) | [`qualitative-current-criterion`](../../areas/convergence/results/qualitative-current-criterion.md) | R3 |
| §3 (exact constant error on dyadic cutoffs) | [`dyadic-cutoff-core-remainder`](../../areas/convergence/results/dyadic-cutoff-core-remainder/README.md) | R4 |
| The current identity used in Theorem 3 | [`finite-current-certificate-identity`](../../areas/convergence/results/finite-current-certificate-identity/README.md) | R1-b |
| §4 onward: five rays, annular recursion, component criterion, partial currents, compression, and the later rounds | [`five-ray-current-criterion`](../../areas/convergence/results/five-ray-current-criterion/README.md) (R5), [`disjoint-annular-recursion`](../../areas/convergence/results/disjoint-annular-recursion/README.md) (R6), [`orbit-component-current-criterion`](../../areas/convergence/results/orbit-component-current-criterion/README.md) (R7), [`universal-annular-partial-current`](../../areas/convergence/results/universal-annular-partial-current/README.md) (R8), [`annular-root-collapse-contraction`](../../areas/convergence/results/annular-root-collapse-contraction.md) (R9), [`exposure-potential-boundary-flux`](../../areas/convergence/results/exposure-potential-boundary-flux/README.md) (R10); the later rounds are the nodes with aliases R11–R94 in [`MAP.md`](../../MAP.md) (narrative in [`areas/convergence/OVERVIEW.md`](../../areas/convergence/OVERVIEW.md)), and the mechanical-word section (R71) is [`mechanical-word-exact-denominator`](../../areas/cycles/results/mechanical-word-exact-denominator/README.md). Legacy folders: `experiments/current_construction/`, `experiments/annular_construction/`, `experiments/residual_progress/` | R5–R94 |

The abstract's last line holds for the whole note: no complete universal current construction, Collatz proof, or novelty claim is supplied. The open target is [`packet-current-supply`](../../areas/convergence/questions/packet-current-supply.md).
