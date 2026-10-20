#!/usr/bin/env python3
"""Replay prepared, pinned Lean sources inside the reviewed macOS sandbox.

This does not download sources or install anything. See replay_notes.md for
preparation and trust boundaries. A running or failed stage is never PASS.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("build", "statements", "kernel"))
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--replay", type=Path, required=True)
    args = parser.parse_args()
    source, replay = args.source.resolve(), args.replay.resolve()
    env = json.loads((replay / "replay_environment.json").read_text())
    env["LEAN_NUM_THREADS"] = "4"
    assert "HOME" not in env and "CODEX_HOME" not in env
    assert env["MATHLIB_NO_CACHE_ON_UPDATE"] == "1"
    profile = replay / "build.sb"
    assert profile.is_file()
    assert (source / "lean-toolchain").read_text().strip() == "leanprover/lean4:v4.35.0-rc2"
    manifest = json.loads((source / "lake-manifest.json").read_text())
    mathlib = next(p for p in manifest["packages"] if p["name"] == "mathlib")
    assert mathlib["rev"] == "065356127b1dc0016f66b7283ce0ce2c4055aa55"
    paths = [source / "lakefile.toml", source / "lake-manifest.json", source / "lean-toolchain"]
    paths += list((source / "CollatzPosDens").rglob("*.lean"))
    paths += list((source / "Solution").rglob("*.lean"))
    before = {str(p.relative_to(source)): sha(p) for p in sorted(paths)}
    lake = str(Path(env["LEAN_SYSROOT"]) / "bin" / "lake")
    if args.stage == "build":
        argv = [lake, "--no-cache", "build", "Solution.Basic"]
    elif args.stage == "statements":
        spec = Path(__file__).with_name("StatementAudit.lean")
        shutil.copyfile(spec, source / "StatementAudit.lean")
        argv = [lake, "env", "lean", "-o", ".lake/build/lib/lean/StatementAudit.olean",
                "StatementAudit.lean"]
    else:
        # Fresh replay checks imported proof objects too, including cached
        # dependencies. It is the same Lean kernel, not a second implementation.
        argv = [lake, "env", "leanchecker", "--fresh", "--verbose", "StatementAudit"]
    command = ["/usr/bin/sandbox-exec", "-f", str(profile), *argv]
    status_path = replay / (args.stage + "_status.json")
    log_path = replay / (args.stage + ".log")
    status = {
        "stage": args.stage, "status": "RUNNING", "command": command,
        "source": str(source), "source_hashes": before,
        "profile_sha256": sha(profile), "lean_threads": 4,
        "started_unix": time.time(),
    }
    if args.stage == "statements":
        status["statement_source_sha256"] = sha(source / "StatementAudit.lean")
    with log_path.open("w") as log:
        process = subprocess.Popen(command, cwd=source, env=env, stdin=subprocess.DEVNULL,
                                   stdout=log, stderr=subprocess.STDOUT)
        status["pid"] = process.pid
        status_path.write_text(json.dumps(status, indent=2) + "\n")
        print(json.dumps({"stage": args.stage, "pid": process.pid,
                          "log": str(log_path), "status": "RUNNING"}), flush=True)
        code = process.wait()
    after = {str(p.relative_to(source)): sha(p) for p in sorted(paths)}
    status.update(exit_code=code, finished_unix=time.time(), log_sha256=sha(log_path),
                  sources_unchanged=after == before)
    status["status"] = "PASS" if code == 0 and after == before else "FAIL"
    status_path.write_text(json.dumps(status, indent=2) + "\n")
    print(json.dumps({k: status[k] for k in ("stage", "status", "exit_code", "sources_unchanged")}))
    if status["status"] != "PASS":
        print(log_path.read_text()[-5000:])
        raise SystemExit(1)


if __name__ == "__main__":
    main()
