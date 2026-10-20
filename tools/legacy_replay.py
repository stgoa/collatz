#!/usr/bin/env python3
"""Replay legacy checkers, unmodified, in a temporary copy of the pre-migration layout.

Before the 2026-10-19/20 migration, the research scripts lived under `experiments/`, `reviews/` and
`lean/`. They load each other's files by those paths and pin each other's hashes. The migration moved
every file byte-identically into node folders, so most of them no longer run where they now live.
This tool rebuilds the old tree in a temporary directory from `tools/legacy_paths.json`
(legacy path -> current path, one entry per legacy file) and runs legacy scripts there. Files that
were rewritten during the migration (mostly notes whose hashes legacy receipts pin) map to null and
are restored with their original bytes from git at be73a66, so their checkers still pass when the
history is available. Nothing in the repository is written.

A replay passes when every script exits 0 **and** every copied file is byte-identical afterwards,
so a checker that rewrites its receipt must reproduce it exactly.

Node certificates call it with the scripts that check that node:

    import legacy_replay
    sys.exit(legacy_replay.main(["experiments/residual_progress/nonselected_inverse/check_inverse_phases.py"]))

Command line:

    python3 tools/legacy_replay.py <legacy script path> [...]   # replay these scripts
    python3 tools/legacy_replay.py --update-map                  # regenerate legacy_paths.json from git

Each script runs from its own legacy folder, without -O, as `scripts/verify_all.py` ran them at
commit be73a66. Standard library only.
"""
from __future__ import annotations

import filecmp
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "tools" / "legacy_paths.json"
LEGACY_COMMIT = "be73a66"
TIMEOUT = 1800


def load_map() -> dict[str, str]:
    return json.loads(MAP.read_text(encoding="utf-8"))


def update_map() -> int:
    """Map every legacy file at LEGACY_COMMIT to its current path, following byte-identical moves.

    A legacy file maps to a current file when git sees an exact rename (100% similarity), or when the
    path is unchanged and the content identical. Files that were rewritten (node READMEs whose legacy
    notes are hash-pinned) or removed map to null; the replay restores their original bytes from git.
    """
    head = "HEAD"
    out = subprocess.run(["git", "diff", "--find-renames=100%", "--name-status", "-z", LEGACY_COMMIT, head],
                         cwd=ROOT, capture_output=True, check=True).stdout.decode().split("\0")
    renames, changed = {}, set()
    i = 0
    while i < len(out) and out[i]:
        status = out[i]
        if status.startswith("R"):
            old, new = out[i + 1], out[i + 2]
            if status == "R100":
                renames[old] = new
            changed.add(old)
            i += 3
        else:
            changed.add(out[i + 1])
            i += 2
    legacy = subprocess.run(["git", "ls-tree", "-r", "--name-only", "-z", LEGACY_COMMIT], cwd=ROOT,
                            capture_output=True, check=True).stdout.decode().split("\0")
    mapping = {}
    for path in legacy:
        if not path:
            continue
        if path in renames:
            mapping[path] = renames[path]
        elif path not in changed:
            mapping[path] = path
        else:
            mapping[path] = None          # rewritten or removed: restored from git at replay time
    # Only research material is replayed; documentation at the old root is not needed.
    mapping = {k: v for k, v in sorted(mapping.items())
               if k.startswith(("experiments/", "reviews/", "lean/", "papers/", "scripts/"))}
    MAP.write_text(json.dumps(mapping, indent=0, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{MAP.relative_to(ROOT)}: {len(mapping)} legacy files mapped")
    return 0


def restore_from_git(tmp: Path, paths: list[str]) -> Path | None:
    """Extract the original bytes of `paths` at LEGACY_COMMIT into tmp; return a pristine copy's root."""
    if not paths:
        return None
    try:
        blob = subprocess.run(["git", "archive", LEGACY_COMMIT, "--", *paths], cwd=ROOT,
                              capture_output=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        print(f"note: git history at {LEGACY_COMMIT} is unavailable; {len(paths)} rewritten legacy "
              "files are absent from the replay, and checkers that hash them will fail")
        return None
    pristine = tmp.parent / (tmp.name + "-git")
    for target in (tmp, pristine):
        with tarfile.open(fileobj=io.BytesIO(blob)) as tar:
            try:
                tar.extractall(target, filter="data")
            except TypeError:            # Python without extraction filters
                tar.extractall(target)
    return pristine


def build(tmp: Path, mapping: dict[str, str | None]) -> dict[Path, Path]:
    """Lay out the legacy tree in tmp. Returns {copied file: reference file} for the final comparison."""
    copied = {}
    for legacy, current in mapping.items():
        if current is None:
            continue
        src = ROOT / current
        if not src.is_file():
            continue
        dest = tmp / legacy
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        copied[dest] = src
    from_git = [legacy for legacy, current in mapping.items() if current is None]
    pristine = restore_from_git(tmp, from_git)
    if pristine is not None:
        for legacy in from_git:
            copied[tmp / legacy] = pristine / legacy
    return copied


def main(scripts: list[str], args: dict[str, list[str]] | None = None) -> int:
    """Replay `scripts` (legacy paths); `args` optionally maps a script to its command-line arguments."""
    mapping = load_map()
    missing = [s for s in scripts if s not in mapping]
    if missing:
        for s in missing:
            print(f"FAIL {s}: not in tools/legacy_paths.json (not migrated byte-identically?)")
        return 1
    failures = []
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONOPTIMIZE", "PYTHONPATH")}
    with tempfile.TemporaryDirectory() as name:
        tmp = Path(name) / "legacy"
        tmp.mkdir()
        copied = build(tmp, mapping)
        for script in scripts:
            path = tmp / script
            try:
                proc = subprocess.run([sys.executable, "-B", path.name, *((args or {}).get(script, []))],
                                      cwd=path.parent, env=env, capture_output=True, text=True,
                                      timeout=TIMEOUT)
            except subprocess.TimeoutExpired:
                failures.append(f"{script}: timed out after {TIMEOUT}s")
                continue
            if proc.returncode != 0:
                tail = (proc.stdout + proc.stderr).strip().splitlines()[-3:]
                failures.append(f"{script}: exit {proc.returncode}: " + " | ".join(tail))
        for dest, src in copied.items():
            if not dest.is_file() or not filecmp.cmp(src, dest, shallow=False):
                failures.append(f"{dest.relative_to(tmp)} changed during the replay")
    for line in failures:
        print("FAIL", line)
    if failures:
        return 1
    print(f"PASS: {len(scripts)} legacy check(s) replayed in the legacy layout; every file unchanged")
    return 0


if __name__ == "__main__":
    argv = sys.argv[1:]
    if argv == ["--update-map"]:
        sys.exit(update_map())
    if not argv or argv[0].startswith("-"):
        print(__doc__)
        sys.exit(2)
    sys.exit(main(argv))
