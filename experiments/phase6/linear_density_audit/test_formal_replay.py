#!/usr/bin/env python3
"""Disposable receipt-integrity tests; no Lean, network, or live-stage execution."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("formal_replay", Path(__file__).with_name("run_formal_replay.py"))
r = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(r)


class ReceiptTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="collatz_receipt_test_")
        self.root = Path(self.tmp.name).resolve()
        self.source = self.root / "source"
        self.replay = self.root / "replay"
        self.source.mkdir()
        self.replay.mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def fixture(self, stage="build", objects=None):
        log = self.replay / (stage + ".log")
        log.write_text("fixture output\n")
        receipt = {"schema": 2, "stage": stage, "status": "PASS", "exit_code": 0,
                   "source": str(self.source), "inputs": {"fixture": 1},
                   "inputs_unchanged": True, "objects_after": objects or {"object": "hash"},
                   "log": r.file_binding(log)}
        path = self.replay / (stage + "_status.json")
        r.atomic_json(path, receipt)
        return path, receipt

    def test_preflight_failure_replaces_old_pass(self):
        path, old = self.fixture()
        with patch.object(r, "inputs", side_effect=FileNotFoundError("missing environment")):
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(r.run("build", self.source, self.replay), 1)
        latest = r.read_json(path)
        self.assertEqual(latest["status"], "FAIL")
        self.assertIn("missing environment", latest["error"])
        previous = list((self.replay / "attempts").glob("*_previous_status.json"))
        self.assertEqual(len(previous), 1)
        self.assertEqual(r.read_json(previous[0]), old)
        self.assertIn("FileNotFoundError", Path(latest["log"]["path"]).read_text())

    def test_popen_failure_replaces_old_pass(self):
        path, _ = self.fixture()
        with patch.object(r, "inputs", return_value=({"LEAN_SYSROOT": "/nonexistent"}, {"fixture": 1})), \
             patch.object(r, "objects", return_value={}), \
             patch.object(r.subprocess, "Popen", side_effect=OSError("cannot start")), \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(r.run("build", self.source, self.replay), 1)
        self.assertEqual(r.read_json(path)["status"], "FAIL")
        self.assertIn("cannot start", r.read_json(path)["error"])

    def test_legacy_build_never_overwritten(self):
        path = self.replay / "build_status.json"
        path.write_text('{"stage":"build","status":"RUNNING"}\n')
        before = path.read_bytes()
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(r.run("build", self.source, self.replay), 1)
        self.assertEqual(path.read_bytes(), before)
        attempted = list((self.replay / "attempts").glob("*_status.json"))
        self.assertEqual(len(attempted), 1)
        self.assertEqual(r.read_json(attempted[0])["status"], "FAIL")

    def test_predecessor_rejects_status_source_log_input_and_object_changes(self):
        path, good = self.fixture()
        args = (path, self.source, {"fixture": 1}, {"object": "hash"}, "build")
        r.validate_receipt(*args)
        cases = [("status", "FAIL"), ("status", "RUNNING"), ("exit_code", 1),
                 ("source", "/wrong"), ("inputs", {"fixture": 2}),
                 ("objects_after", {"object": "changed"}), ("inputs_unchanged", False)]
        for field, value in cases:
            with self.subTest(field=field, value=value):
                r.atomic_json(path, dict(good, **{field: value}))
                with self.assertRaises(r.AuditError):
                    r.validate_receipt(*args)
        r.atomic_json(path, good)
        Path(good["log"]["path"]).write_text("changed")
        with self.assertRaises(r.AuditError):
            r.validate_receipt(*args)
        path.unlink()
        with self.assertRaises(FileNotFoundError):
            r.validate_receipt(*args)

    def test_chain_detects_changed_predecessor_receipt(self):
        path, _ = self.fixture()
        child, receipt = self.fixture("statements")
        statement = self.source / "StatementAudit.lean"
        statement.write_bytes(Path(__file__).with_name("StatementAudit.lean").read_bytes())
        Path(receipt["log"]["path"]).write_text(valid_reports())
        receipt.update(log=r.file_binding(receipt["log"]["path"]),
                       axiom_reports=r.parse_axioms(valid_reports()),
                       statement_source=r.file_binding(statement),
                       predecessor={"stage": "build", "receipt": r.file_binding(path)},
                       objects_before={"object": "hash"})
        r.atomic_json(child, receipt)
        args = (child, self.source, {"fixture": 1}, {"object": "hash"}, "statements")
        r.validate_receipt(*args)
        missing = dict(receipt)
        missing.pop("predecessor")
        r.atomic_json(child, missing)
        with self.assertRaises(r.AuditError):
            r.validate_receipt(*args)
        r.atomic_json(child, receipt)
        path.write_text(path.read_text() + "\n")
        with self.assertRaises(r.AuditError):
            r.validate_receipt(*args)

    def legacy_fixture(self):
        env = {"LEAN_SYSROOT": "/fixture/toolchain"}
        archived = {"lakefile.toml": "a", "lake-manifest.json": "b", "lean-toolchain": "c",
                    "Solution/Basic.lean": "d", "CollatzPosDens.lean": "e"}
        runner = self.replay / "run_formal_replay_initial.py"
        runner.write_text("# fixture original runner\n")
        log = self.replay / "build.log"
        log.write_text("initial successful build\n")
        status = {"stage": "build", "status": "PASS", "exit_code": 0,
                  "sources_unchanged": True, "source": str(self.source),
                  "profile_sha256": r.PROFILE_SHA, "lean_threads": 4,
                  "log_sha256": r.sha(log),
                  "source_hashes": {k: v for k, v in archived.items() if k != "CollatzPosDens.lean"},
                  "command": ["/usr/bin/sandbox-exec", "-f", str(self.replay / "build.sb"),
                              "/fixture/toolchain/bin/lake", "--no-cache", "build", "Solution.Basic"]}
        r.atomic_json(self.replay / "build_status.json", status)
        current = {"runtime": {"effective_environment": env}, "source": {"files": archived}}
        return current, runner

    def test_seal_preserves_initial_bytes_and_labels_timing(self):
        current, runner = self.legacy_fixture()
        paths = [self.replay / "build_status.json", self.replay / "build.log"]
        before = [p.read_bytes() for p in paths]
        inv = {"project/Solution/Basic.olean": "fixture-object"}
        with patch.object(r, "INITIAL_RUNNER_SHA", r.sha(runner)), \
             patch.object(r, "inputs", return_value=({}, current)), \
             patch.object(r, "objects", return_value=inv), \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(r.run("seal-build", self.source, self.replay), 0)
        sealed = r.read_json(self.replay / "seal-build_status.json")
        self.assertEqual(sealed["status"], "PASS")
        self.assertIn("sealing time", sealed["legacy_build"]["artifact_timing"])
        self.assertEqual([p.read_bytes() for p in paths], before)
        self.assertEqual(sealed["objects_after"], inv)

    def test_seal_rejects_changed_original_log_or_before_hashes(self):
        current, runner = self.legacy_fixture()
        with patch.object(r, "INITIAL_RUNNER_SHA", r.sha(runner)):
            r.legacy_build(self.source, self.replay, current)
            altered = dict(current, source={"files": dict(current["source"]["files"], **{"Solution/Basic.lean": "wrong"})})
            with self.assertRaises(r.AuditError):
                r.legacy_build(self.source, self.replay, altered)
            (self.replay / "build.log").write_text("changed")
            with self.assertRaises(r.AuditError):
                r.legacy_build(self.source, self.replay, current)

    def test_existing_seal_cannot_silently_rebind_changed_object(self):
        current, runner = self.legacy_fixture()
        inv = {"project/Solution/Basic.olean": "original-object"}
        with patch.object(r, "INITIAL_RUNNER_SHA", r.sha(runner)), \
             patch.object(r, "inputs", return_value=({}, current)), \
             patch.object(r, "objects", return_value=inv), \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(r.run("seal-build", self.source, self.replay), 0)
        changed = {"project/Solution/Basic.olean": "changed-object"}
        with patch.object(r, "INITIAL_RUNNER_SHA", r.sha(runner)), \
             patch.object(r, "inputs", return_value=({}, current)), \
             patch.object(r, "objects", return_value=changed), \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(r.run("seal-build", self.source, self.replay), 1)
        self.assertEqual(r.read_json(self.replay / "seal-build_status.json")["status"], "FAIL")


def valid_reports(multiline=False):
    axioms = "[propext,\n Quot.sound, Classical.choice]" if multiline else "[propext, Quot.sound, Classical.choice]"
    return "\n".join(f"'{name}' depends on axioms: {axioms}" for name in sorted(r.EXPECTED_THEOREMS)) + "\n"


class AxiomTests(unittest.TestCase):
    def test_exact_and_multiline_reports(self):
        self.assertEqual(set(r.parse_axioms(valid_reports())), r.EXPECTED_THEOREMS)
        self.assertEqual(r.parse_axioms(valid_reports()), r.parse_axioms(valid_reports(True)))
        empty = "\n".join(f"'{name}' does not depend on any axioms" for name in r.EXPECTED_THEOREMS)
        self.assertEqual(set(r.parse_axioms(empty)), r.EXPECTED_THEOREMS)

    def test_missing_duplicate_unexpected_and_malformed_reports(self):
        lines = valid_reports().splitlines()
        variants = ["\n".join(lines[:-1]), "\n".join(lines[:-1] + [lines[0]]),
                    valid_reports() + "'unknown' depends on axioms: []\n",
                    valid_reports().replace("[propext, Quot.sound, Classical.choice]", "[propext", 1),
                    valid_reports().replace("[propext, Quot.sound, Classical.choice]", "[propext,, Quot.sound]", 1)]
        for text in variants:
            with self.subTest(text=text[:60]), self.assertRaises(r.AuditError):
                r.parse_axioms(text)

    def test_exact_allowlist_rejects_nonstandard_and_lookalikes(self):
        for name in ("sorryAx", "Lean.ofReduceBool", "evil.propext", "propext_suffix", "Classical.choiceX"):
            with self.subTest(name=name), self.assertRaises(r.AuditError):
                r.parse_axioms(valid_reports().replace("propext", name, 1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
