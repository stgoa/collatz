#!/usr/bin/env python3
"""Generate a namespaced statement audit from the pinned public Lean challenge.

Reads source as text; never imports or executes the external Lean development.
"""

import argparse
import hashlib
from pathlib import Path
import re


SOURCE_COMMIT = "3a38bfbb70379e051b51155def1423846fab3a90"
SOURCE_SHA256 = "e3e828be137de84f97cee84c4635f5f726fb975d1641dacff3b213130f5bf235"
NAMES = [
    "positive_density_collatz_reaches_one",
    "positive_density_collatz_and_collatzAccel_reaches_one",
    "positive_density_collatz_and_collatzAccel_reaches_of_coprime_six",
    "positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd",
]


def generate(source_bytes: bytes) -> str:
    digest = hashlib.sha256(source_bytes).hexdigest()
    if digest != SOURCE_SHA256:
        raise ValueError(f"Challenge source hash mismatch: {digest}")
    source = source_bytes.decode("utf-8")
    if re.findall(r"^theorem (\w+)", source, re.M) != NAMES:
        raise ValueError("Unexpected theorem names or order")
    if source.count("  sorry") != 4:
        raise ValueError("Expected exactly four challenge proof placeholders")
    source = source.replace(
        "public import Mathlib.Analysis.SpecialFunctions.Log.Basic",
        "public import Solution.Basic",
        1,
    )
    source = source.replace("open Finset", "namespace LauStatementAudit\n\nopen Finset", 1)
    for name in NAMES:
        args = "ht hN" if name.endswith(("of_coprime_six", "of_not_three_dvd")) else "hN"
        pos = source.index("theorem " + name)
        hole = source.index("  sorry", pos)
        source = (
            source[:hole]
            + "  _root_." + name + " " + args
            + source[hole + len("  sorry"):]
        )
    source += "\nend LauStatementAudit\n\n"
    source += (
        "/-!\n## Independent namespace comparison and axiom reports\n\n"
        "Each local theorem above elaborates its copied specification, then uses only the named\n"
        "solution theorem as its proof. Successful elaboration checks definitional equality between\n"
        "the two statements, including the independently named map and constant definitions.\n"
        "This file does not import Challenge.Basic.\n-/\n\n"
    )
    for namespace in ("_root_.", "LauStatementAudit."):
        for name in NAMES:
            source += f"#print axioms {namespace}{name}\n"
            source += f"set_option pp.proofs false in\n#print {namespace}{name}\n\n"
    header = (
        "/-\nP6-004 statement correspondence audit.\n"
        "Generated from pinned AxiomMath/CollatzPositiveDensity Challenge/Basic.lean at\n"
        f"{SOURCE_COMMIT}.\nSource SHA256: {digest}.\n"
        "The specification definitions and theorem types are copied unchanged into a new namespace;\n"
        "only the import and theorem proof terms are replaced. No external code was executed to\n"
        "generate this file. A successful later compile is required before claiming correspondence.\n-/\n"
    )
    if not source.startswith("module\n"):
        raise ValueError("Unexpected module header")
    source = source.replace("module\n", "module\n\n" + header, 1)
    if re.search(r"\bsorry\b", source):
        raise ValueError("Generated Lean file still contains a proof placeholder")
    return source


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("challenge", type=Path, help="Pinned Challenge/Basic.lean")
    parser.add_argument(
        "--output", type=Path, default=Path(__file__).with_name("StatementAudit.lean")
    )
    parser.add_argument("--check", action="store_true", help="Check existing output without writing")
    args = parser.parse_args()
    generated = generate(args.challenge.read_bytes()).encode("utf-8")
    if args.check:
        if args.output.read_bytes() != generated:
            raise SystemExit("Generated statement audit differs from the saved file")
    else:
        args.output.write_bytes(generated)
    print("statement_audit_sha256:", hashlib.sha256(generated).hexdigest())
    print("source_sha256:", SOURCE_SHA256)
    print("mode:", "checked" if args.check else "generated")


if __name__ == "__main__":
    main()
