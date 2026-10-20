---
id: ansari-sieve-step-counterexample
kind: result
title: A displayed set identity in the proof of Ansari's recursive sieve lemma fails at n = 1
status: written
claim: >
  For the residue sets defined in Lemma 3.1 of ansari-2025-recursive-sieve (as transcribed in the checker),
  the concluding equality F_(n+1) = F'_n minus A' (printed page 478) is false: at n = 1, F_2 = (3, 7, 15, 19)
  mod 36 while F'_1 minus A' = (3, 7, 11, 15, 19, 23, 27, 31) mod 36, so 11 lies on the right but not the left;
  for every n = 1..8 the left side is a proper subset of the right, with 4 2^(n-1) versus 8 2^(n-1) residues,
  and the least extra residue is 8 3^(n-1) + 3. This is an exact finite counterexample to one displayed proof
  step; it does not claim that the paper's theorem is false, and no conclusion depending on that step is used
  as a premise in this repository.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
certificates: [check_recursive_sieve.py]
aliases: [R24-b]
tags: [convergence, sufficient-sets, external-check, counterexample, literature-audit]
---

# A displayed set identity in the proof of Ansari's recursive sieve lemma fails at n = 1

## Statement

[`ansari-2025-recursive-sieve`](../../../../sources/ansari-2025-recursive-sieve.md) defines recursively sufficient sets and proposes a ternary-digit sieve. With its sets transcribed as in [`check_recursive_sieve.py`](check_recursive_sieve.py) (residues `3 + 4·s` modulo `4·3^(n+1)`, `s` with ternary digits as stated), the concluding equality of the proof of Lemma 3.1, `F_(n+1) = F'_n \ A'`, fails already at `n = 1`:

| Set | Residues modulo 36 |
|---|---|
| `F_2` | 3, 7, 15, 19 |
| `F'_1` | 3, 7, 11, 15, 19, 23, 27, 31, 35 |
| `A'` | 35 |
| `F'_1 \ A'` | 3, 7, 11, 15, 19, 23, 27, 31 |

So 11 belongs to the right side but not the left. Removing only the top-digit pair `(2, 2)` does not restrict both digits to `{0, 1}`; the recursive sufficiency of the four additionally removed classes needs a separate argument, which the displayed proof does not supply. For `n = 1, …, 8` the left side is a proper subset of the right, of sizes `4·2^(n−1)` and `8·2^(n−1)`, and the least extra residue is `8·3^(n−1) + 3`.

This is an exact counterexample to one displayed proof step, not a claim that the paper's theorem is false.

## Proof

The legacy note "A failed set identity in a potentially relevant sieve proof" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: exact counterexample to one displayed proof step; no claim that
the paper's theorem is false.**

Ansari's [2025 paper](https://nntdm.net/papers/nntdm-31/NNTDM-31-3-471-480.pdf)
defines recursively sufficient sets and proposes a ternary-digit sieve.
We checked Lemma3.1 before importing that sieve. Its concluding equality
on printed page478, `F_(n+1)=F'_n\A'`, fails already at n=1:

| Set | Residues modulo36 |
|---|---|
| F2 | 3,7,15,19 |
| F'1 | 3,7,11,15,19,23,27,31,35 |
| A' | 35 |
| F'1 minus A' | 3,7,11,15,19,23,27,31 |

Thus11 belongs to the asserted right side but not the left. Removing
only the top-digit pair(2,2) does not restrict both digits to{0,1}.
The recursive sufficiency of the four additional removed classes needs
a separate argument. The displayed proof does not supply it.

We therefore do not use this lemma, the resulting sieve, or the reported
verification extension as premises. The elementary definition and
smaller-seed induction principle are unaffected. Our R37/R38 reductions
have their own explicit currents and input dependencies.

Reproduce the finite set arithmetic:

```sh
python3 experiments/residual_progress/sufficient_sets/check_recursive_sieve.py
```

## Certificates

[`check_recursive_sieve.py`](check_recursive_sieve.py) (instant, standard library; legacy script, unchanged). It builds the three residue sets for `n = 1, …, 8` and checks the strict inclusion, the two sizes and the least extra residue, printing a one-line PASS. It passes at its new path. It uses `assert`; run it without `-O`. It ran at `be73a66` only inside `scripts/verify_all.py`, after the gate's stopping point (archive/legacy-checker-run-be73a66.md; the gate passed in full at `9dbc71a`).

## Remarks

- **Consequence for this repository.** The lemma, the resulting sieve and the reported verification extension are not used as premises. The elementary definition and the smaller-seed induction principle are unaffected. The later reductions of the line (legacy R37, R38, `experiments/residual_progress/tripling_equivalence/` and `odd_pair_closure/`, not yet migrated) have their own explicit currents and input dependencies.
- The check was made before importing the sieve, as part of the sufficient-set audit of [`five-ray-profile-completion-suffices`](../five-ray-profile-completion-suffices/README.md). The primary PDF and the finite set arithmetic were read separately (legacy research log).

## History

- Migrated from `experiments/residual_progress/sufficient_sets/RECURSIVE_SIEVE_AUDIT.md` with its checker (filed under legacy R24; alias R24-b here) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). The source node [`ansari-2025-recursive-sieve`](../../../../sources/ansari-2025-recursive-sieve.md) was created at the migration from what the legacy text states. Legacy status: "exact counterexample to one displayed proof step; no claim that the paper's theorem is false".
- Main lane (ChatGPT, Codex), 2026-10-17 (recorded in the round report of the R37–R39 batch).
