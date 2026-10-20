"""The node schema as data: one place that check.py, build_map.py and the docs agree on.

Human-readable version: conventions/SCHEMA.md. Keep the two in step.
"""

KINDS = ("result", "attempt", "question", "source")

STATUSES = {
    "result": ("proposed", "written", "reviewed", "formal", "refuted", "withdrawn"),
    "attempt": ("proposed", "written", "reviewed", "formal", "refuted", "withdrawn"),
    "question": ("open", "answered", "dropped"),
    "source": ("cited", "replayed"),
}

# Strength order for the "weakest link" computation. Terminal statuses are not on the ladder.
LADDER = ("proposed", "written", "reviewed", "formal")

REQUIRED = {
    "result": ("id", "kind", "title", "status", "claim", "authors", "created"),
    "attempt": ("id", "kind", "title", "status", "claim", "authors", "created"),
    "question": ("id", "kind", "title", "status", "claim", "created"),
    "source": ("id", "kind", "title", "status", "citation", "created"),
}

ALLOWED = {
    "id", "kind", "title", "status", "claim", "citation", "url", "created", "authors",
    "assumes", "depends_on", "lean", "certificates", "evidence", "reviewed_by", "supersedes",
    "aliases", "answered_by", "refuted_by", "withdrawn_reason", "tags",
}

LIST_FIELDS = {
    "authors", "assumes", "depends_on", "lean", "certificates", "evidence", "reviewed_by",
    "supersedes", "aliases", "answered_by", "tags",
}

REVIEW_KEYS_REQUIRED = ("by", "date")
REVIEW_KEYS_ALLOWED = {"by", "date", "link", "scope"}

# Which kinds each reference field may point at.
TARGETS = {
    "depends_on": ("result",),
    "assumes": ("result", "question", "source"),
    "supersedes": ("result", "attempt", "question"),
    "answered_by": ("result", "attempt"),
}

ID_RE = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
ID_MAX = 64
ALIAS_RE = r"^[A-Za-z0-9][A-Za-z0-9._-]*$"
DATE_RE = r"^\d{4}-\d{2}-\d{2}$"

# Lean hygiene: forbidden tokens in lean/**/*.lean, matched after comments are stripped (tools/check.py).
LEAN_FORBIDDEN = (
    r"\bsorry\b", r"\badmit\b", r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*axiom\b", r"\bnative_decide\b", r"\bimplemented_by\b",
    r"@\[extern", r"\bunsafe\b", r"\bopaque\b",
)
