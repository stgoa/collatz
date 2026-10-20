---
id: shared-background-copies-via-gap
kind: result
title: "C013's q = 1 restriction with the replayed gap instead of Matveev: tens of thousands of background copies"
status: written
claim: >
  Raw odd-only 3x+1 map (q = 1). Let a nontrivial integer cycle have word (U, a_0, U, a_1, …, U, a_(r−1)) with
  one background U of length n repeated r ≥ 2 times between nonconstant markers of total T, m = r(n+1).
  Substituting the replayed gap_all (EXT-1) for the Matveev bound in C013's inequality (13) gives
  n < r + 4T + 2(r−1)·log₂r + 172 + 341·log₂m. With marker average T ≤ H·r this forces
  m/r − 1 < r(1 + 4H) + 2(r−1)·log₂r + 172 + 341·log₂m, an effective form of C013's r = Ω_H(√(m/log m));
  at m = 1.375·10^11 (the imported period bound) the smallest admissible r is about 61,000 (H = 1) to about
  46,000 (H = 8), where C013 as written allows r = 6. Here r counts copies of one background, not rotation
  mismatches; markers of a q = 1 cycle may be large, and then H is unbounded. C013's algebra is main's
  written proof and is not re-verified here.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [shared-background-denominator-law]
assumes: [musson-collatz-gap-all, hercher-2023-cycle-length]
certificates: [s11_c013_gap.py]
evidence:
  - "s11_c013_gap.py, s11_c013_gap.json: side-lane script (under 1 s) that computes the table of the Statement: for a few (m, H) the smallest r compatible with C013's (13) under each bound on log₂(1/η) (gap_all and Matveev), and writes its receipt. Exits 0 at its new path and leaves its receipt byte-identical (checked at migration). It recomputes the numbers; it does not check C013's algebra. Passed at be73a66 as reviews/side_lane/s11_c013_gap.py (archive/legacy-checker-run-be73a66.md)"
aliases: [S11]
tags: [cycles, shared-background, linear-forms, effective]
---

# C013's q = 1 restriction with the replayed gap instead of Matveev: tens of thousands of background copies

## Statement

C013 ([`shared-background-denominator-law`](../shared-background-denominator-law/README.md)) treats words `w = (U, a_0, U, a_1, …, U, a_(r−1))` with nonconstant markers: background length `n`, marker total `T`, `m = r(n+1)`, `η = D/2^A`. For `q = 1` its (12)–(13) give

```
n < r + 4T + 2(r−1)·log₂ r + log₂(1/η).
```

With `gap_all` ([`musson-collatz-gap-all`](../../../../sources/musson-collatz-gap-all.md), EXT-1: `2^A ≤ 2^172·m^341·(2^A − 3^m)`), `η ≥ 2^(−172)·m^(−341)`, so

```
n < r + 4T + 2(r−1)·log₂ r + 172 + 341·log₂ m.                        (13′)
```

With marker average `T ≤ H·r`, using `m/r − 1 < r(1 + 4H) + 2(r−1)·log₂ r + 172 + 341·log₂ m`, the smallest admissible `r` is:

| `m` | `H = 1` | `H = 2` | `H = 4` | `H = 8` | C013 as written (Matveev) |
|---|---|---|---|---|---|
| `10^7` | `r ≥ 507` | 479 | 434 | 374 | `r ≥ 2` |
| `1.375·10^11` | `r ≥ ≈61,000` | ≈58,000 | ≈53,000 | ≈46,000 | `r ≥ 6` |
| `10^15` | `r ≥ ≈4.5·10^6` | ≈4.3·10^6 | ≈4.1·10^6 | ≈3.6·10^6 | `r ≥ 31,897` |

(Values above 1,000 are found with steps of 0.1%.) So, under the period import ([`hercher-2023-cycle-length`](../../../../sources/hercher-2023-cycle-length.md): every nontrivial cycle has `m > 1.375·10^11`), a hypothetical nontrivial cycle whose word is `r` copies of one background separated by nonconstant markers with average `≤ 8` needs at least about 46,000 copies. C013 as written could not exclude even `r = 6` at that period.

## Proof

Legacy note `C013_GAP.md` (S11, side lane), lightly edited. Its status line read: "An input substitution in main's written C013 proof, of the same kind as S6 for C011. No new algebra. The C013 resultant and root-separation argument is main's written proof and is not re-verified here."

**Where Matveev enters C013.** In C013's (13) the last term `log₂(1/η)` is the only analytic input. C013 bounds it with the Matveev estimate imported in C011: `log η > −K(1 + log 2m)` with `K = 6·10^8`. That gives `log₂(1/η) < (K/ln 2)(1 + ln 2m) ≈ 2.4·10^10` at `m = 1.375·10^11`.

**The substitution.** `gap_all` gives `log₂(1/η) ≤ 172 + 341·log₂ m`, about `1.3·10^4` at `m = 1.375·10^11`. Everything else in C013's derivation of (13) and (14) is unchanged, and the table is the computation of the smallest `r` (`s11_c013_gap.py`).

## Certificates

`s11_c013_gap.py` recomputes the table of the Statement and rewrites `s11_c013_gap.json`; at migration it exited 0 with the receipt unchanged. It does not check C013's algebra, which is main's written proof.

## Remarks

- **Representations, not mismatches.** As C013 itself stresses, `r` counts copies of one identical shared background, not rotation mismatches. The improvement concerns that representation class only.
- **Bounded marker average.** The `(14)`-type consequence needs `T ≤ H·r`. Markers of a `q = 1` cycle can be large; a tall cycle's descent letters are an example. Then `H` is unbounded and (13′) bounds `n` only through `4T`.
- **Inputs.** `gap_all` is formal elsewhere (replayed) and is used only for `η`. C013's algebra is main's written proof. The period import is needed only to quote numbers at a given `m`. Because this node depends on [`shared-background-denominator-law`](../shared-background-denominator-law/README.md), MAP.md also lists that node's inputs (Matveev, and the two-primes bound used in its part (iv)); the substitution here removes Matveev from (13) itself.
- **Pattern.** This repeats S6's improvement of C011 ([`two-mismatch-exclusion-via-gap`](../two-mismatch-exclusion-via-gap/README.md): Matveev to `gap_all`, `K = 6·10^8` to `341`). A `git grep` of main showed imported linear-form bounds in exactly three cycle-spectrum batches:
  - C006, Bugeaud's two-logarithm bound, replaced in the side lane's EXT-1 composition (`G2_of_gap_collatz`, `J > 1.07·10^7`; see [`ordered-cycle-height-change-growth`](../ordered-cycle-height-change-growth.md));
  - C011, Matveev, replaced by S6, now formal as S6-b/c;
  - C013, Matveev, replaced here.
  - Each therefore has a replayed-gap replacement.
  - The grep also hits C002 (`INDEPENDENT_SLOPES.md` §5). That is a non-import: C002 proves its power-gap lemma from its own Input B, "without importing an additional theorem on linear forms in logarithms". The Lean lane checked this.
  - C014, ChatGPT's uncommitted draft, is not touched.
- **Reviews wanted.** The legacy frontier listed S11 among the written results with no independent review.

## History

- Migrated from `experiments/cycle_spectrum/S11/C013_GAP.md` (legacy ID `S11`; side-lane producer batch S11, 2026-10-19) at commit `be73a66`, by the B06 migration (Claude, Opus 5.5). The probe `reviews/side_lane/s11_c013_gap.{py,json}` moved here. The note's "Reproduce" block pointed to the old path.
- Side lane (Claude, Opus), feed 2026-10-19 14:57 (LEAD, S11). No independent review of the substitution is on record; the Lean lane checked only the C002 non-import point.
- **Correction (2026-10-19, in the note).** An earlier sentence of "Bounded marker average" said every `q = 1` cycle has a letter of about `0.47–0.58m`. That holds only under S7's three-mismatch structure, which is now excluded ([`three-mismatch-exclusion`](../three-mismatch-exclusion/README.md)); the sentence was removed.
