# S11: main's C013 q = 1 restriction with the replayed gap instead of Matveev

**Status:** side-lane producer batch S11 (2026-10-19). An input substitution in main's written C013 proof, of the same kind as S6 for C011. No new algebra. The C013 resultant and root-separation argument is main's written proof and is not re-verified here.

## 1. Where Matveev enters C013

C013 (`OVERLAP_CONTROLS.md` §§3–4) treats words `w = (U, a_0, U, a_1, …, U, a_(r−1))` with nonconstant markers.
- The parameters are: background length `n`, marker total `T`, `m = r(n+1)`, and `η = D/2^A`.
- For `q = 1` it derives (12)–(13):

  ```
  n < r + 4T + 2(r−1) log₂ r + log₂(1/η).
  ```

- The last term is the only analytic input. C013 bounds it with the Matveev estimate imported in C011: `log η > −K(1 + log 2m)` with `K = 6·10^8`. That gives `log₂(1/η) < (K/ln 2)(1 + ln 2m) ≈ 2.4·10^10` at `m = 1.375·10^11`.

## 2. The substitution

`gap_all` (`mmusson/collatz`, replayed as EXT-1 on the standard axioms) says `2^A ≤ 2^172 m^341 (2^A − 3^m)`. That is, `η ≥ 2^(−172) m^(−341)`, so

```
n < r + 4T + 2(r−1) log₂ r + 172 + 341 log₂ m.                        (13′)
```

The analytic term drops from about `2.4·10^10` to about `1.3·10^4` at `m = 1.375·10^11`. C013's (14), `r = Ω_H(√(m/log m))` for representations with marker average `T ≤ Hr`, becomes effective with small constants. Using `m/r − 1 < r(1 + 4H) + 2(r−1) log₂ r + 172 + 341 log₂ m`:

| `m` | `H = 1` | `H = 2` | `H = 4` | `H = 8` | C013 as written (Matveev) |
|---|---|---|---|---|---|
| `10^7` | `r ≥ 507` | 479 | 434 | 374 | `r ≥ 2` |
| `1.375·10^11` | `r ≥ ≈61,000` | ≈58,000 | ≈53,000 | ≈46,000 | `r ≥ 6` |
| `10^15` | `r ≥ ≈4.5·10^6` | ≈4.3·10^6 | ≈4.1·10^6 | ≈3.6·10^6 | `r ≥ 31,897` |

(Values above 1,000 are found with steps of 0.1%.)

So, under the period imports, a hypothetical nontrivial cycle whose word is `r` copies of one background separated by nonconstant markers with average `≤ 8` needs at least about 46,000 copies. C013 as written could not exclude even `r = 6` at that period.

## 3. Scope

- **Representations, not mismatches.** As C013 itself stresses, `r` counts copies of one identical shared background, not rotation mismatches. The improvement concerns that representation class only.
- **Bounded marker average.** The `(14)`-type consequence needs `T ≤ Hr`. Markers of a `q = 1` cycle can be large; a tall cycle's descent letters are an example. Then `H` is unbounded and (13′) bounds `n` only through `4T`. *(Corrected 2026-10-19: an earlier sentence said every `q = 1` cycle has a letter of about `0.47–0.58m`. That holds only under S7's three-mismatch structure, which is now excluded.)*
- **Inputs.** `gap_all` is formal elsewhere and is used only for `η`. C013's algebra is main's written proof. The period import is needed only to quote numbers at a given `m`.
- **Pattern.** This repeats S6's improvement of C011 (Matveev to `gap_all`, `K = 6·10^8` to `341`).
  - A `git grep` of main shows imported linear-form bounds in exactly three cycle-spectrum batches:
    - C006, Bugeaud's two-logarithm bound, replaced in the side lane's EXT-1 composition (`G2_of_gap_collatz`, `J > 1.07·10^7`);
    - C011, Matveev, replaced by S6, now formal as S6-b/c;
    - C013, Matveev, replaced here.
  - Each therefore has a replayed-gap replacement.
  - C014, ChatGPT's uncommitted draft, is not touched.

## Reproduce

```sh
python3 sidekick/probes/s11_c013_gap.py   # < 1 s
```
