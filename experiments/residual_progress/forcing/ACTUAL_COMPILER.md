# Compiling actual packet certificates into an integer absorption current

17 October 2026. This is a finite demonstration of the conditional theorem in
[FINITE_CONE.md](../duality/FINITE_CONE.md), using actual positive Syracuse
states and exact integer arithmetic. It does not construct the required inputs
at arbitrary cutoffs or prove Collatz.

## Reusable construction

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

## Actual demonstration

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

## Reproduce

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
