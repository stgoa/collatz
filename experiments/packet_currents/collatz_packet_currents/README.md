# Reproduction

Read `research_note.md` first. The general packet-remainder theorem is separate from the finite current-cost data. The latter do not prove a uniform bound or Collatz.

Python3.10+; standard library only. The independent verifier uses C++17 and no extra libraries.

## Check the stored certificates without any new hitting-time search

```sh
python verify_stored_currents.py > stored_verification_output.txt
```

This uses source cylinders, one-step arrows in the stored currents, and finite exit profiles. It does not call the trajectory-to-core current constructor or follow an exit's unresolved future.

## Rebuild the complete research calculation

```sh
python certificate.py > certificate_output.txt
python update_exit_profiles.py > exit_profile_output.txt
python finite_source_bounds.py > finite_source_bounds_output.txt

g++ -O2 -std=c++17 -Wall -Wextra independent_verifier.cpp -o independent_verifier
./independent_verifier 4096 2 data > independent_4096.json
./independent_verifier 262144 4 data > independent_262144.json
python verify_stored_currents.py > stored_verification_output.txt
```

The constructor follows finite orbits to generate the currents and aborts if it cannot certify a path within its cap. Its success for every future source cutoff is not claimed.

The largest supplied current has132998 nonzero rows. The data files are research certificates, not spreadsheet deliverables. Positive and negative integer weights must be retained exactly.

## Files

- research_note.md: full written proofs and limitations.
- roadmap.md: next uniform estimate, explicitly unproved.
- certificate.py: exact packets and finite current discovery/checks.
- update_exit_profiles.py: all-horizon bounds from finite current exits.
- finite_source_bounds.py: two named source-power-window certificates.
- verify_stored_currents.py: verification only, no new tail search.
- independent_verifier.cpp: direct-source packet construction and independent current check.
- data/packets_*.csv and data/current_*.csv: complete stored integer measures.
- data/exit_profiles_*.json: integer level sums at current exits.
- lag_witnesses.json: finite paths, arrival lags and tail-independent bounds.
- audit/: original-upload provenance and unchanged certificate output.

Use normal Python mode, not `python -O`, because assertions perform the exact checks. The scripts do not constitute Lean verification.
