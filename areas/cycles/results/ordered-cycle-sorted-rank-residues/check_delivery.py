#!/usr/bin/env python3
"""Check C008 completed receipts, pinned reviews, links and frozen history.

This does not rerun the historical gate or the mathematical experiments.
Those commands have their own independent receipts and exit statuses.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = 'dddbe334159f0fd658974627127b9e8b237add40'
FROZEN = '9190ccf2519acc56446dd027c6cbf8d45dcceeb6'
TOP = ('AGENTS.md', 'README.md', 'VIEWPOINT_MAP.md', 'docs/CYCLE_SPECTRUM_BRIEF.md',
       'docs/CYCLE_SPECTRUM_LOG.md', 'docs/RESEARCH_LOG.md', 'docs/RESULTS.md', 'docs/VIEWPOINT_LOG.md')


def require(ok, message):
    if not ok:
        raise ValueError(message)


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def report():
    gate = json.loads((HERE/'historical_gate.json').read_text())
    require(len(gate) == 119, 'historical gate coverage')
    metadata = {'archive_sha256', 'manifest_entries', 'scope'}
    require(all(isinstance(v, str) and v.startswith('PASS') for k, v in gate.items()
                if k not in metadata), 'historical gate contains non-PASS result')
    receipt = json.loads((HERE/'height_matching_audit.json').read_text())
    spectrum = json.loads((HERE/'residue_spectrum_audit.json').read_text())
    # The matching receipt's status field describes scope; its executable
    # emits PASS only after comparing the complete independently rebuilt data.
    require(spectrum['status'] == 'PASS' and not receipt['existing']['full_denominator_failures']
            and receipt['existing']['counts']['primitive_cycles'] == 1185,
            'mathematical receipt coverage')
    pins = {
        'check_height_matching.py': 'f8d63a71dc57206386c35cfcadba62a29969f1405aa8be665fa39158e99d1f39',
        'height_matching_audit.json': '8be1fb6414481b333f36cd007e4542a2c9e009d6339afd7fb3771b6e79b7361a',
        'MATCHING_ARITHMETIC.md': 'aefff8c4a83e236c341ecbd2c37e7b6d7cb41d2aa87c3459a44f9d722a2a53ad',
        'INDEPENDENT_MATCHING.md': '21b37af7f124364e57b041a18cd8b96fec818a14a55451e7528d74aff1c3931e',
    }
    require(all(digest(HERE/p) == h for p, h in pins.items()), 'reviewed source changed')
    for p, h in spectrum['source_sha256'].items():
        require(digest(ROOT/p) == h, 'spectrum dependency changed')
    previous = git('ls-tree', '-r', '--name-only', BASE, 'experiments/cycle_spectrum').decode().splitlines()
    previous = [p for p in previous if re.match(r'experiments/cycle_spectrum/C00[1-7]/', p)]
    require(all((ROOT/p).read_bytes() == git('show', BASE+':'+p) for p in previous), 'historical cycle batch changed')
    marker = '## R1 — Exact source transport and original packets'.encode()
    require((ROOT/'docs/RESULTS.md').read_bytes().split(marker, 1)[1] ==
            git('show', FROZEN+':docs/RESULTS.md').split(marker, 1)[1], 'frozen result ledger changed')
    kept = ['collatz_research_20261017/right_aligned_reduction.tex',
            'experiments/residual_progress/resolved_rules/RESOLVED_RULES.md',
            'experiments/residual_progress/resolved_rules/resolved_rules.py']
    require(all((ROOT/p).read_bytes() == git('show', FROZEN+':'+p) for p in kept), 'frozen file changed')
    files = [ROOT/p for p in TOP]+sorted(HERE.glob('*.md'))
    links, errors = 0, []
    for path in files:
        body = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)', body):
            target = target.split('#', 1)[0].strip('<>')
            if not target or re.match(r'[a-zA-Z]+:', target):
                continue
            links += 1
            destination = path.parent/target
            # This receipt is the output being constructed, not an external input.
            if destination.resolve() == HERE/'delivery_checks.json':
                continue
            if not destination.exists():
                errors.append([str(path.relative_to(ROOT)), target])
    require(not errors, 'broken local link: '+repr(errors))
    git('diff', '--check')
    hashes = {str(p.relative_to(ROOT)): digest(p) for p in sorted(HERE.iterdir())
              if p.is_file() and p.name != 'delivery_checks.json'}
    return dict(status='PASS', baseline_commit=BASE, frozen_commit=FROZEN,
        goal_status='All-cycle objective active; ordered q1 exclusion remains open and is only an intermediate recommendation.',
        historical_gate=dict(status='PASS', command='python3 scripts/verify_all.py --cpp --transfer-controls',
                             field_count=len(gate), independent_cpp=gate['independent_cpp'],
                             phase6_transfer_controls=gate['phase6_transfer_controls']),
        source_reviews=dict(status='PASS', pinned_sha256=pins),
        preservation=dict(C001_C007_files_unchanged=len(previous), R1_onward_byte_identical=True,
                          frozen_files_byte_identical=kept, git_diff_check='PASS'),
        markdown_checks=dict(files=len(files), existing_local_links=links, errors=errors),
        batch_file_sha256=hashes,
        side_reviewed_commit='aab73dd4cf84561d5bd1f59b8eb1be5b4825f6bf')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = report()
    path = HERE/'delivery_checks.json'
    if args.write:
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(json.loads(path.read_text()) == result, 'delivery receipt mismatch')
    print(json.dumps({k: result[k] for k in ('status', 'preservation', 'markdown_checks')}))


if __name__ == '__main__':
    main()
