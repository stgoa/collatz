# S.2 power-growth norm transport

[Written proof](GROWTH_NORM_TRANSPORT.md) and two exact focused audits for
P6-003. The full repository gate passed; see [verification.json](verification.json).

```sh
python3 experiments/phase6/growth_norm_transport/check_growth_norm.py
python3 experiments/phase6/growth_norm_transport/check_all_exponents.py
```

Default invocations check stored receipts without writing files. The first
checks the one-arrow bound and explicit four-word expansion. The second
checks finite first-crossing codes, inverse residues, raw cylinders and the
S.1 feed to the proof for every0<alpha<1. The winning target residue exists
by finite averaging; the huge full catalogue is not materialized.

The main theorem excludes arbitrary-target contraction in these norms.
Collatz and estimates using the actual nonabsorbing set remain open.
