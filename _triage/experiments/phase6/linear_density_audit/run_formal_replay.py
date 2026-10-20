#!/usr/bin/env python3
"""Replay pinned Lau sources offline, with content-bound, stage-specific receipts.

No download or installation occurs here. `seal-build` preserves the initial runner's
build_status.json/build.log and binds their successful result to CURRENT artifacts;
it does not manufacture an object digest at the earlier build-completion instant.
See replay_notes.md. A stage PASS is not a claim of analytic rederivation.
"""
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import tarfile
import time
import traceback
import uuid

SOURCE_COMMIT = "3a38bfbb70379e051b51155def1423846fab3a90"
SOURCE_ARCHIVE_SHA = "a97925bc3888a37476238c1d56de9e745b76a970a82e2771cbdc20c810828b77"
TOOLCHAIN_ARCHIVE_SHA = "e721cf30671d3830fa6120c7b1a4e6b22624650ce1d618c0ca28a4889f5ef324"
PROFILE_SHA = "afede27c096261909e5194216446982bb17662863345a4061a4853133dddef5d"
INITIAL_RUNNER_SHA = "c3087bbddc00de657d4addbc6ca417065e0f8bba9fd54ab57317352483dcb246"
STATEMENT_SHA = "8215385e2b8b10c7507f6587ba1aa53fd7f6825f2cd020eee13307b8bba447e2"
THEOREMS = (
    "positive_density_collatz_reaches_one",
    "positive_density_collatz_and_collatzAccel_reaches_one",
    "positive_density_collatz_and_collatzAccel_reaches_of_coprime_six",
    "positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd",
)
EXPECTED_THEOREMS = frozenset(THEOREMS + tuple("LauStatementAudit." + n for n in THEOREMS))
ALLOWED_AXIOMS = frozenset(("propext", "Quot.sound", "Classical.choice"))
STAGES = ("build", "seal-build", "statements", "kernel")


class AuditError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise AuditError(message)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def atomic_json(path, value):
    path = Path(path)
    tmp = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    tmp.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, path)


def file_binding(path):
    path = Path(path).resolve()
    require(path.is_file(), f"Missing file: {path}")
    return {"path": str(path), "sha256": sha(path)}


def check_file(binding):
    require(isinstance(binding, dict) and set(binding) == {"path", "sha256"},
            "Malformed file binding")
    require(file_binding(binding["path"]) == binding, f"File binding changed: {binding['path']}")


def archive_sources(source, replay):
    archive = source.with_name(source.name + "_source.tar.gz")
    require(sha(archive) == SOURCE_ARCHIVE_SHA, "Source archive checksum mismatch")
    snapshot_path = replay / "source_snapshot.json"
    snapshot = read_json(snapshot_path)
    require(snapshot.get("archive_sha256") == SOURCE_ARCHIVE_SHA, "Wrong snapshot archive pin")
    archived = {}
    prefix = "CollatzPositiveDensity-" + SOURCE_COMMIT
    with tarfile.open(archive, "r:gz") as tar:
        for entry in tar:
            parts = PurePosixPath(entry.name).parts
            require(parts and parts[0] == prefix and ".." not in parts,
                    f"Unexpected archive path: {entry.name}")
            require(entry.isdir() or entry.isfile(), "Archive contains link or special file")
            if entry.isfile():
                name = str(PurePosixPath(*parts[1:]))
                require(name not in archived, "Duplicate archive member")
                archived[name] = hashlib.sha256(tar.extractfile(entry).read()).hexdigest()
    require(archived == snapshot.get("files"), "Snapshot does not match the pinned archive")
    for name, digest in archived.items():
        path = source / name
        require(path.is_file() and not path.is_symlink() and sha(path) == digest,
                f"Pinned source changed or missing: {name}")
    # Detect new source files, as well as deletions; a fixed initial path list cannot.
    current = {str(p.relative_to(source)) for p in source.rglob("*.lean")
               if ".lake" not in p.relative_to(source).parts and ".git" not in p.relative_to(source).parts}
    expected = {p for p in archived if p.endswith(".lean")}
    require(current - {"StatementAudit.lean"} == expected, "Local Lean source inventory changed")
    audit_copy = source / "StatementAudit.lean"
    if audit_copy.exists():
        require(not audit_copy.is_symlink() and sha(audit_copy) == STATEMENT_SHA,
                "Existing statement audit source changed")
    return {"commit": SOURCE_COMMIT, "archive": file_binding(archive),
            "snapshot": file_binding(snapshot_path), "files": archived}


def dependency_bindings(source):
    manifest = read_json(source / "lake-manifest.json")  # itself archive-verified
    result = {}
    git_env = {"PATH": "/usr/bin:/bin", "GIT_CONFIG_NOSYSTEM": "1",
               "GIT_CONFIG_GLOBAL": "/dev/null", "GIT_TERMINAL_PROMPT": "0"}
    for package in manifest["packages"]:
        require(package["type"] == "git" and package.get("subDir") is None,
                "Unexpected dependency layout")
        name = package["name"]
        require(re.fullmatch(r"[A-Za-z0-9_-]+", name) is not None and name not in result,
                "Invalid/duplicate dependency name")
        root = source / ".lake" / "packages" / name
        head = subprocess.run(["/usr/bin/git", "-C", str(root), "rev-parse", "HEAD"],
                              check=True, capture_output=True, text=True, env=git_env).stdout.strip()
        require(head == package["rev"], f"Dependency HEAD mismatch: {name}")
        config_paths = {package["configFile"], package.get("manifestFile"), "lean-toolchain"} - {None}
        configs = {}
        for rel in sorted(config_paths):
            require(not PurePosixPath(rel).is_absolute() and ".." not in PurePosixPath(rel).parts,
                    "Unsafe dependency config path")
            path = root / rel
            require(path.exists() or rel != package["configFile"], f"Missing config for {name}")
            configs[rel] = sha(path) if path.is_file() else None
        result[name] = {"head": head, "url": package["url"], "configs": configs}
    require(len(result) == 9, "Unexpected dependency count")
    return result


def environment_and_toolchain(replay):
    env_path = replay / "replay_environment.json"
    env = read_json(env_path)
    require(isinstance(env, dict) and all(isinstance(k, str) and isinstance(v, str)
                                        for k, v in env.items()), "Malformed replay environment")
    allowed = {"PATH", "TMPDIR", "MATHLIB_CACHE_DIR", "MATHLIB_NO_CACHE_ON_UPDATE",
               "GIT_CONFIG_NOSYSTEM", "GIT_CONFIG_GLOBAL", "GIT_TERMINAL_PROMPT", "LANG", "LEAN_SYSROOT"}
    require(set(env) == allowed, "Unexpected or missing environment setting")
    toolchain = (replay / "lean-4.35.0-rc2-darwin_aarch64").resolve()
    require(Path(env["LEAN_SYSROOT"]).resolve() == toolchain, "Wrong toolchain directory")
    expected = {
        "PATH": str(Path(env["LEAN_SYSROOT"]) / "bin") + ":/usr/bin:/bin:/usr/sbin:/sbin",
        "MATHLIB_NO_CACHE_ON_UPDATE": "1", "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_CONFIG_GLOBAL": "/dev/null", "GIT_TERMINAL_PROMPT": "0", "LANG": "en_US.UTF-8",
    }
    for name, value in expected.items():
        require(env[name] == value, f"Unexpected environment value: {name}")
    for name, leaf in (("TMPDIR", "tmp"), ("MATHLIB_CACHE_DIR", "cache")):
        require(Path(env[name]).resolve() == replay / leaf, f"Unexpected {name}")
    env["LEAN_NUM_THREADS"] = "4"
    profile = replay / "build.sb"
    require(sha(profile) == PROFILE_SHA, "Sandbox profile differs from reviewed profile")
    receipt = read_json(replay / "toolchain_receipt.json")
    archive_name = "lean-4.35.0-rc2-darwin_aarch64.tar.zst"
    require(receipt.get("archive") == archive_name and receipt.get("sha256") == TOOLCHAIN_ARCHIVE_SHA,
            "Wrong toolchain receipt")
    archive = replay / archive_name
    require(sha(archive) == TOOLCHAIN_ARCHIVE_SHA, "Toolchain archive checksum mismatch")
    release = read_json(replay / "lean_release.json")
    require(release.get("tag_name") == "v4.35.0-rc2", "Wrong official toolchain release")
    assets = [a for a in release["assets"] if a["name"] == archive_name]
    require(len(assets) == 1 and assets[0].get("digest") == "sha256:" + TOOLCHAIN_ARCHIVE_SHA,
            "Official release asset digest mismatch")
    binaries = {name: file_binding(toolchain / "bin" / name)
                for name in ("lean", "lake", "leanchecker", "leantar")}
    return env, {"environment_file": file_binding(env_path), "effective_environment": env,
                 "profile": file_binding(profile), "archive": file_binding(archive),
                 "receipt": file_binding(replay / "toolchain_receipt.json"),
                 "release": file_binding(replay / "lean_release.json"), "binaries": binaries}


def inputs(source, replay):
    source_info = archive_sources(source, replay)
    require((source / "lean-toolchain").read_text().strip() == "leanprover/lean4:v4.35.0-rc2",
            "Wrong Lean version")
    spec = Path(__file__).with_name("StatementAudit.lean").resolve()
    require(sha(spec) == STATEMENT_SHA, "Independent statement specification changed")
    env, runtime = environment_and_toolchain(replay)
    return env, {"source_root": str(source), "replay_root": str(replay), "source": source_info,
                 "dependencies": dependency_bindings(source), "runtime": runtime,
                 "statement_specification": file_binding(spec), "runner": file_binding(__file__)}


def is_object(path):
    return any(path.name.endswith(s) for s in
               (".olean", ".olean.private", ".olean.server", ".ir", ".ir.sig", ".so", ".dylib"))


def objects(source, env):
    # Include transitive imported proof objects and native runtime modules, not just
    # the top-level .olean. These are byte bindings, not independent source rebuilds.
    roots = {"project": source / ".lake" / "build" / "lib" / "lean",
             "lake-config": source / ".lake" / "config",
             "toolchain": Path(env["LEAN_SYSROOT"]) / "lib"}
    for package in read_json(source / "lake-manifest.json")["packages"]:
        roots["dependency/" + package["name"]] = (source / ".lake" / "packages" /
                                                 package["name"] / ".lake" / "build" / "lib")
    result = {}
    for label, root in roots.items():
        for path in sorted(root.rglob("*")):
            if path.is_file() and is_object(path):
                result[label + "/" + str(path.relative_to(root))] = sha(path)
    return result


def need_objects(inventory, audit=False):
    require("project/Solution/Basic.olean" in inventory, "Missing Solution.Basic.olean")
    if audit:
        require("project/StatementAudit.olean" in inventory, "Missing StatementAudit.olean")


def statement_object(name):
    return name.startswith("project/StatementAudit.") and is_object(Path(name))


def parse_axioms(log):
    # Anchored complete reports, exact declaration names and exact axiom names.
    pattern = re.compile(r"^'([^'\n]+)' (?:does not depend on any axioms|depends on axioms:\s*\[([^\]]*)\])[ \t]*$", re.M)
    reports = {}
    matches = list(pattern.finditer(log))
    residual = pattern.sub("", log)
    require("depends on axioms" not in residual and "does not depend on any axioms" not in residual,
            "Malformed axiom report")
    for match in matches:
        name, raw = match.groups()
        require(name in EXPECTED_THEOREMS, f"Unexpected theorem axiom report: {name}")
        require(name not in reports, f"Duplicate axiom report: {name}")
        axioms = [] if raw is None or not raw.strip() else [a.strip() for a in raw.split(",")]
        require(len(axioms) == len(set(axioms)) and all(a in ALLOWED_AXIOMS for a in axioms),
                f"Disallowed or malformed axiom list for {name}: {axioms}")
        reports[name] = sorted(axioms)
    require(set(reports) == EXPECTED_THEOREMS, "Missing one or more of the eight axiom reports")
    return reports


def validate_receipt(path, source, current_inputs, current_objects, expected_stage, seen=None):
    """Validate a completed predecessor, its immutable log and its recursive chain."""
    path = Path(path).resolve()
    seen = set() if seen is None else seen
    require(str(path) not in seen, "Receipt dependency cycle")
    seen.add(str(path))
    receipt = read_json(path)
    require(receipt.get("schema") == 2 and receipt.get("stage") == expected_stage and
            receipt.get("status") == "PASS" and receipt.get("exit_code") == 0,
            f"Predecessor is not a successful {expected_stage} receipt")
    require(receipt.get("source") == str(source), "Predecessor source root mismatch")
    require(receipt.get("inputs") == current_inputs, "Predecessor inputs changed")
    require(receipt.get("objects_after") == current_objects, "Predecessor proof/runtime objects changed")
    require(receipt.get("inputs_unchanged") is True, "Predecessor input consistency absent")
    check_file(receipt["log"])
    if expected_stage == "statements":
        require(receipt.get("statement_source") == file_binding(source / "StatementAudit.lean") and
                receipt["statement_source"]["sha256"] == STATEMENT_SHA,
                "Statement source binding changed")
        require(receipt.get("axiom_reports") == parse_axioms(Path(receipt["log"]["path"]).read_text()),
                "Statement axiom receipt disagrees with its log")
    if expected_stage in ("statements", "kernel"):
        pred = receipt.get("predecessor")
        allowed = ("build", "seal-build") if expected_stage == "statements" else ("statements",)
        require(isinstance(pred, dict) and pred.get("stage") in allowed,
                f"Missing or wrong predecessor for {expected_stage}")
    else:
        require("predecessor" not in receipt, f"Unexpected predecessor for {expected_stage}")
    if "predecessor" in receipt:
        pred = receipt["predecessor"]
        check_file(pred["receipt"])
        validate_receipt(pred["receipt"]["path"], source, current_inputs,
                         receipt["objects_before"], pred["stage"], seen)
    if expected_stage == "seal-build":
        check_file(receipt["legacy_build"]["status"])
        check_file(receipt["legacy_build"]["log"])
        check_file(receipt["legacy_build"]["runner"])
    return receipt


def legacy_build(source, replay, current_inputs):
    status_path, log_path = replay / "build_status.json", replay / "build.log"
    legacy = read_json(status_path)
    require(legacy.get("schema") is None and legacy.get("stage") == "build" and
            legacy.get("status") == "PASS" and legacy.get("exit_code") == 0 and
            legacy.get("sources_unchanged") is True, "Initial build is not completed PASS")
    require(legacy.get("source") == str(source), "Initial build source root mismatch")
    require(legacy.get("profile_sha256") == PROFILE_SHA and legacy.get("lean_threads") == 4,
            "Initial build profile/threads mismatch")
    require(legacy.get("log_sha256") == sha(log_path), "Initial build log hash mismatch")
    env = current_inputs["runtime"]["effective_environment"]
    command = ["/usr/bin/sandbox-exec", "-f", str(replay / "build.sb"),
               str(Path(env["LEAN_SYSROOT"]) / "bin" / "lake"), "--no-cache", "build", "Solution.Basic"]
    require(legacy.get("command") == command, "Unexpected initial build command")
    archived = current_inputs["source"]["files"]
    expected_names = {"lakefile.toml", "lake-manifest.json", "lean-toolchain"} | {
        p for p in archived if p.endswith(".lean") and p.startswith(("CollatzPosDens/", "Solution/"))}
    require(legacy.get("source_hashes") == {p: archived[p] for p in expected_names},
            "Initial build before-hashes disagree with the pinned source archive")
    original_runner = replay / "run_formal_replay_initial.py"
    require(sha(original_runner) == INITIAL_RUNNER_SHA, "Initial runner checksum mismatch")
    return {"status": file_binding(status_path), "log": file_binding(log_path),
            "runner": file_binding(original_runner),
            "artifact_timing": "Objects are bound at sealing time, not retrospectively at build completion."}


def predecessor(stage, source, replay, current_inputs, current_objects):
    if stage == "statements":
        # An existing failed seal is never bypassed by falling back to another build.
        path = replay / "seal-build_status.json"
        pred_stage = "seal-build" if path.exists() else "build"
        if pred_stage == "build":
            path = replay / "build_status.json"
    else:
        path, pred_stage = replay / "statements_status.json", "statements"
    record = validate_receipt(path, source, current_inputs, current_objects, pred_stage)
    # Pin the immutable per-attempt receipt, not merely a mutable 'latest' pointer.
    immutable = Path(record["attempt_status_path"])
    require(read_json(immutable) == record, "Latest/immutable predecessor receipt disagreement")
    return {"stage": pred_stage, "receipt": file_binding(immutable)}


def run(stage, source, replay):
    replay.mkdir(parents=True, exist_ok=True)
    source, replay = source.resolve(), replay.resolve()
    attempts = replay / "attempts"
    attempts.mkdir(exist_ok=True)
    attempt = f"{stage}-{time.time_ns()}-{uuid.uuid4().hex[:8]}"
    status_path = replay / (stage + "_status.json")
    attempt_status = attempts / (attempt + "_status.json")
    log_path = attempts / (attempt + ".log")
    status = {"schema": 2, "stage": stage, "status": "RUNNING", "source": str(source),
              "attempt": attempt, "attempt_status_path": str(attempt_status),
              "started_unix": time.time(), "runner_pid": os.getpid()}
    lock = (replay / (stage + ".lock")).open("a+")
    publish = False
    previous_path = None
    process = None

    def save():
        atomic_json(attempt_status, status)
        if publish:
            atomic_json(status_path, status)

    try:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        # The live legacy build uses no lock: never overwrite it, even on rejection.
        if stage == "build" and status_path.exists() and read_json(status_path).get("schema") != 2:
            raise AuditError("Preserving initial build receipt; use seal-build after its completion")
        if status_path.exists():
            previous_path = attempts / (attempt + "_previous_status.json")
            shutil.copyfile(status_path, previous_path)
        publish = True
        save()  # invalidates any stale PASS before reading environment or starting Popen
        with log_path.open("w") as log:
            log.write(f"Stage {stage}; attempt {attempt}\n")
            log.flush()
            env, before = inputs(source, replay)
            status["inputs"] = before
            before_objects = objects(source, env)
            status["objects_before"] = before_objects
            if stage in ("statements", "kernel"):
                need_objects(before_objects, audit=(stage == "kernel"))
                status["predecessor"] = predecessor(stage, source, replay, before, before_objects)
            if stage == "seal-build":
                need_objects(before_objects)
                if previous_path is not None and read_json(previous_path).get("status") == "PASS":
                    validate_receipt(previous_path, source, before, before_objects, "seal-build")
                status["legacy_build"] = legacy_build(source, replay, before)
                status["scope"] = "Seal of original successful build plus current pinned sources and objects; no build rerun."
                status["exit_code"] = 0
                log.write("Initial successful build receipt validated; current source/object bindings recorded.\n")
            else:
                lake = str(Path(env["LEAN_SYSROOT"]) / "bin" / "lake")
                if stage == "build":
                    require(not any(n.startswith("project/") for n in before_objects),
                            "Fresh build requires an empty local proof-object inventory")
                    argv = [lake, "--no-cache", "build", "Solution.Basic"]
                elif stage == "statements":
                    shutil.copyfile(Path(__file__).with_name("StatementAudit.lean"), source / "StatementAudit.lean")
                    argv = [lake, "env", "lean", "-o", ".lake/build/lib/lean/StatementAudit.olean", "StatementAudit.lean"]
                else:
                    require(sha(source / "StatementAudit.lean") == STATEMENT_SHA, "Copied statement source mismatch")
                    argv = [lake, "env", "leanchecker", "--fresh", "--verbose", "StatementAudit"]
                command = ["/usr/bin/sandbox-exec", "-f", str(replay / "build.sb"), *argv]
                status["command"] = command
                save()
                process = subprocess.Popen(command, cwd=source, env=env, stdin=subprocess.DEVNULL,
                                           stdout=log, stderr=subprocess.STDOUT)
                status["pid"] = process.pid
                save()
                print(json.dumps({"stage": stage, "pid": process.pid, "log": str(log_path), "status": "RUNNING"}), flush=True)
                status["exit_code"] = process.wait()
                require(status["exit_code"] == 0, f"Stage process exited {status['exit_code']}")
            log.flush()
        _, after = inputs(source, replay)
        status["inputs_unchanged"] = before == after
        require(status["inputs_unchanged"], "Source/config/toolchain/specification inputs changed during stage")
        after_objects = objects(source, env)
        status["objects_after"] = after_objects
        need_objects(after_objects, audit=stage in ("statements", "kernel"))
        if stage in ("seal-build", "kernel"):
            require(after_objects == before_objects, "Proof/runtime objects changed during read-only stage")
        elif stage == "statements":
            require({n: h for n, h in after_objects.items() if not statement_object(n)} ==
                    {n: h for n, h in before_objects.items() if not statement_object(n)},
                    "Statement stage changed objects outside StatementAudit")
            status["axiom_reports"] = parse_axioms(log_path.read_text())
        if "predecessor" in status:
            pred = status["predecessor"]
            check_file(pred["receipt"])
            validate_receipt(pred["receipt"]["path"], source, after, before_objects, pred["stage"])
        if stage in ("statements", "kernel"):
            require(sha(source / "StatementAudit.lean") == STATEMENT_SHA,
                    "Statement source missing or changed after execution")
            status["statement_source"] = file_binding(source / "StatementAudit.lean")
        if stage == "seal-build":
            require(legacy_build(source, replay, after) == status["legacy_build"], "Initial build evidence changed during sealing")
        status["status"] = "PASS"
    except BaseException as exc:
        if process is not None and process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
        status["status"] = "FAIL"
        status["error"] = f"{type(exc).__name__}: {exc}"
        with log_path.open("a") as log:
            traceback.print_exc(file=log)
    finally:
        status["finished_unix"] = time.time()
        status["log"] = file_binding(log_path)
        save()
        lock.close()
    print(json.dumps({k: status.get(k) for k in ("stage", "status", "exit_code", "error", "attempt_status_path")}))
    return 0 if status["status"] == "PASS" else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=STAGES)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--replay", type=Path, required=True)
    args = parser.parse_args()
    raise SystemExit(run(args.stage, args.source, args.replay))


if __name__ == "__main__":
    main()
